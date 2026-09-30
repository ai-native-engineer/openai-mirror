"""수집기 공용 상태: 재시도 정책, 404 판정, 실행 manifest, 표면별 coverage.

manifest는 `<repo>/_mirror-state/`(gitignored)에 쓴다.
- `runs/<UTC시각>-<collector>.json`: 실행 1회의 전체 기록. 지우지 않고 누적한다.
- `surfaces/<surface>.json`: 표면별 최신 URL 상태. 전체 범위 실행은 URL 집합을 교체하고,
  --include/--only/--limit 같은 부분 실행은 건드린 URL만 갱신한다.

URL 상태
- saved: 이번 실행에서 저장 / existing: 기존 파일이 있어 증분 skip
- thin: 200이지만 본문이 기준 미만(client-only)이라 미저장
- moved: 404였지만 redirect·경로 변경·같은 slug의 공개 URL을 찾음(target 기록)
- gone: 404/410 재확인 + 대안 URL 없음 = 원본 삭제 확정
- unresolved: 재시도 소진, 확정 안 된 404, 기타 4xx, 열거 실패. 하나라도 있으면 실행은 실패다.
"""

import json
import os
import random
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from urllib.parse import urlsplit, urlunsplit

STATE_DIR = "_mirror-state"
SURFACES = [
    ("openai.com", "openai.com"),
    ("openai-sites", "Foundation/Fund/Alignment/Spinning Up/Progress/DevDay"),
    ("academy", "Academy"),
    ("developers", "developers"),
    ("help", "Help"),
    ("model-spec", "Model Spec"),
    ("learn", "Learn"),
    ("deployment-safety", "Deployment Safety"),
    ("trust", "Trust"),
    ("youtube", "YouTube"),
    ("pdf", "PDF"),
]
SURFACE_HOSTS = {
    "openai.com": ["openai.com"],
    "openai-sites": [
        "openaifoundation.org",
        "openai.fund",
        "alignment.openai.com",
        "spinningup.openai.com",
        "progress.openai.com",
        "devday.openai.com",
    ],
    "academy": ["academy.openai.com"],
    "developers": ["developers.openai.com"],
    "help": ["help.openai.com"],
    "model-spec": ["model-spec.openai.com"],
    "learn": ["learn.chatgpt.com"],
    "deployment-safety": ["deploymentsafety.openai.com"],
    "trust": ["trust.openai.com"],
}
HOST_SURFACE = {h: s for s, hosts in SURFACE_HOSTS.items() for h in hosts}
SAVED = {"saved", "existing"}


def surface_of(url):
    return HOST_SURFACE.get(urlsplit(url).netloc, "other")


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------- 재시도


class Result:
    """수집기 fetch 결과. status는 HTTP 코드, error는 예외/추출 실패 메시지."""

    def __init__(
        self,
        url,
        body="",
        status=None,
        error="",
        retry_after=None,
        canonical="",
        thin_reason="",
    ):
        self.url, self.body, self.status, self.error = url, body, status, error
        self.retry_after, self.canonical, self.thin_reason = (
            retry_after,
            canonical,
            thin_reason,
        )
        self.attempts, self.resolution, self.target, self.note = 1, "", "", ""
        self.final_url = ""

    @property
    def kind(self):
        if self.error:
            return "network/extract"
        if self.status and self.status != 200:
            return f"http-{self.status}"
        return "ok"


def retryable(res):
    return (
        bool(res.error)
        or res.status == 429
        or (res.status is not None and 500 <= res.status < 600)
    )


def parse_retry_after(value):
    try:
        return max(0.0, float(value))
    except (TypeError, ValueError):
        return None


def canonical_of(html):
    m = re.search(
        r'<link[^>]+rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', html or "", re.I
    ) or re.search(
        r'<link[^>]+href=["\']([^"\']+)["\'][^>]*rel=["\']canonical', html or "", re.I
    )
    return m.group(1) if m else ""


class RetryPolicy:
    """exponential backoff. 429는 모든 worker가 함께 쉬도록 전역 cooldown을 건다.

    min_interval은 worker 전체의 요청 시작 간격이다. Academy는 분당 요청 수보다 순간 burst에 429를 준다.
    """

    def __init__(self, retries=4, backoff=2.0, max_wait=90.0, min_interval=0.0):
        self.retries, self.backoff, self.max_wait = retries, backoff, max_wait
        self.min_interval = min_interval
        self._lock = threading.Lock()
        self._pause_until = 0.0
        self._next_slot = 0.0

    def delay(self, attempt, retry_after=None):
        d = self.backoff * (2 ** (attempt - 1))
        if retry_after:
            d = max(d, retry_after)
        return min(self.max_wait, d * (1 + random.random() * 0.2))

    def cooldown(self, seconds):
        with self._lock:
            self._pause_until = max(self._pause_until, time.monotonic() + seconds)

    def wait_turn(self):
        while True:
            with self._lock:
                now = time.monotonic()
                left = self._pause_until - now
                if left <= 0:
                    slot = max(now, self._next_slot)
                    self._next_slot = slot + self.min_interval
                    break
            time.sleep(min(left, 5))
        if slot > now:
            time.sleep(slot - now)

    def run(self, fn, url):
        attempt = 0
        while True:
            self.wait_turn()
            attempt += 1
            try:
                res = fn(url)
            except Exception as e:  # 수집기 fetch가 흘린 예외도 재시도 대상이다.
                res = Result(url, error=f"{type(e).__name__}: {e}"[:200])
            res.attempts = attempt
            if not retryable(res) or attempt > self.retries:
                return res
            d = self.delay(attempt, res.retry_after)
            print(
                f"  retry {attempt}/{self.retries} in {d:.0f}s: {url} [{res.kind} {res.error[:60]}]",
                flush=True,
            )
            if res.status == 429:
                self.cooldown(d)
            else:
                time.sleep(d)


def add_retry_args(ap, retries=4, backoff=2.0, max_wait=90.0, min_interval=0.0):
    ap.add_argument(
        "--min-interval",
        type=float,
        default=min_interval,
        help=f"모든 worker 합산 요청 시작 간격 초 (기본 {min_interval})",
    )
    ap.add_argument(
        "--retries",
        type=int,
        default=retries,
        help=f"429/5xx/timeout/추출 오류 재시도 횟수 (기본 {retries})",
    )
    ap.add_argument(
        "--retry-backoff",
        type=float,
        default=backoff,
        help=f"첫 재시도 대기 초, 매회 2배 (기본 {backoff})",
    )
    ap.add_argument(
        "--retry-max-wait",
        type=float,
        default=max_wait,
        help=f"재시도 1회 최대 대기 초 (기본 {max_wait})",
    )
    ap.add_argument(
        "--state-dir", default="", help=f"manifest 위치 (기본 <out>/{STATE_DIR})"
    )


def policy_from(a):
    return RetryPolicy(a.retries, a.retry_backoff, a.retry_max_wait, a.min_interval)


# ---------------------------------------------------------------- 404 판정


def slug_of(url):
    parts = [p for p in urlsplit(url).path.split("/") if p]
    return parts[-1] if parts else ""


def slug_index(urls):
    idx = {}
    for u in urls:
        s = slug_of(u)
        # 한 단어 slug(chatgpt, agents)는 다른 문서와 겹친다(실측 오판 3건). 두 단어 이상만 근거로 쓴다.
        if "-" in s.strip("-") and len(s) >= 8:
            idx.setdefault(s, []).append(u)
    return idx


def slash_variant(url):
    p = urlsplit(url)
    path = p.path[:-1] if p.path.endswith("/") and len(p.path) > 1 else p.path + "/"
    return urlunsplit((p.scheme, p.netloc, path, "", ""))


def resolve_404(res, fetch, policy, candidates=(), allowed_hosts=None):
    """404를 삭제로 확정하기 전에 canonical·경로 변경·같은 slug의 공개 URL을 확인한다.

    res를 제자리 갱신해 돌려준다. resolution: ok(일시적 404) / moved / gone / unresolved.
    """
    url = res.url
    alts = []
    if res.canonical:
        c = (
            res.canonical
            if "://" in res.canonical
            else urlunsplit(
                urlsplit(url)._replace(path=res.canonical, query="", fragment="")
            )
        )
        if c.rstrip("/") != url.rstrip("/") and urlsplit(c).path.strip("/"):
            alts.append(c)
    alts.append(slash_variant(url))
    # 같은 slug가 여러 하위 경로(클럽별 사본 등)에 흩어져 있으면 공개 정본은 대개 얕은 경로다. 얕은 순으로 시도한다.
    others = sorted((c for c in candidates if c.rstrip("/") != url.rstrip("/")),
                    key=lambda c: (len([x for x in urlsplit(c).path.split("/") if x]), c))
    alts += others[:5]
    hosts = allowed_hosts or {urlsplit(url).netloc}
    checked = []
    for alt in dict.fromkeys(alts):
        if urlsplit(alt).netloc not in hosts:
            continue
        r = policy.run(fetch, alt)
        checked.append(f"{alt}={r.status or r.kind}")
        if r.status == 200 and not r.error:
            r.resolution, r.target = "moved", alt
            res.resolution, res.target, res.note = "moved", alt, "; ".join(checked)
            return res, r
    confirm = policy.run(fetch, url)
    if confirm.status == 200 and not confirm.error:
        confirm.resolution, confirm.note = "ok", "404 재확인에서 200"
        return confirm, None
    res.note = "; ".join(checked)
    if confirm.status in (404, 410):
        res.resolution = "gone"
        res.note = f"{confirm.status} 재확인, 대안 {len(checked)}개 모두 실패" + (
            f" ({res.note})" if res.note else ""
        )
    else:
        res.resolution = "unresolved"
        res.note = f"404 재확인 결과 {confirm.status or confirm.kind}" + (
            f" ({res.note})" if res.note else ""
        )
    return res, None


def fetch_resolved(fetch, url, policy, slugs=None, allowed_hosts=None):
    """재시도 + 404 판정. (주 결과, 이동한 대상 결과 또는 None)."""
    res = policy.run(fetch, url)
    if res.status in (404, 410):
        cands = (slugs or {}).get(slug_of(url), [])
        return resolve_404(res, fetch, policy, cands, allowed_hosts)
    return res, None


# ---------------------------------------------------------------- manifest


class Manifest:
    def __init__(self, out, collector, argv, state_dir=""):
        self.out = out
        self.collector = collector
        self.argv = list(argv)
        self.state_dir = state_dir or os.path.join(out, STATE_DIR)
        self.started = now_iso()
        self.records = {}
        self.complete = set()  # 이번 실행이 전체 URL 집합을 열거한 표면
        self.enum_errors = []  # 열거 실패(sitemap/BFS) -> 발견 집합이 불완전
        self.stale_checked = {}  # surface -> {파일 상대경로: stale 검증 판정}
        self._lock = threading.Lock()

    def _rec(self, url):
        rec = self.records.get(url)
        if rec is None:
            rec = self.records[url] = {
                "url": url,
                "surface": surface_of(url),
                "status": "pending",
                "http": None,
                "saved": False,
                "thin": False,
                "error": "",
                "attempts": 0,
                "retried": False,
                "target": "",
                "note": "",
                "checked_at": "",
            }
        return rec

    def discover(self, urls):
        with self._lock:
            for u in urls:
                self._rec(u)

    def mark(self, url, status, **fields):
        with self._lock:
            rec = self._rec(url)
            rec.update(fields)
            rec["status"] = status
            rec["saved"] = status in SAVED
            rec["thin"] = status == "thin"
            rec["checked_at"] = now_iso()

    def existing(self, urls):
        for u in urls:
            self.mark(u, "existing")

    def result(self, res, saved, min_len):
        """fetch 결과 하나를 상태로 바꾼다. 반환: 최종 상태."""
        common = {
            "http": res.status,
            "error": res.error,
            "attempts": res.attempts,
            "retried": res.attempts > 1,
            "target": res.target,
            "note": res.note,
        }
        if saved:
            status = "saved"
        elif res.resolution in ("moved", "gone", "unresolved"):
            status = res.resolution
        elif res.error or res.status != 200:
            status = "unresolved"
        else:
            status = "thin"
            common["note"] = (
                res.thin_reason or f"본문 {len(res.body.strip())}자 < {min_len}"
            )
        self.mark(res.url, status, **common)
        return status

    def enum_error(self, url, err, surface=None):
        with self._lock:
            self.enum_errors.append(
                {
                    "url": url,
                    "surface": surface or surface_of(url),
                    "error": str(err)[:200],
                }
            )

    def unresolved(self):
        return [
            r for r in self.records.values() if r["status"] in ("unresolved", "pending")
        ] + self.enum_errors

    def counts(self):
        rows = {}
        for r in self.records.values():
            row = rows.setdefault(
                r["surface"],
                {
                    "discovered": 0,
                    "saved": 0,
                    "retried": 0,
                    "unresolved": 0,
                    "thin": 0,
                    "http404": 0,
                    "moved": 0,
                    "gone": 0,
                },
            )
            row["discovered"] += 1
            row["saved"] += r["saved"]
            row["retried"] += r["retried"]
            row["unresolved"] += r["status"] in ("unresolved", "pending")
            row["thin"] += r["thin"]
            row["http404"] += r["http"] in (404, 410)
            row["moved"] += r["status"] == "moved"
            row["gone"] += r["status"] == "gone"
        for e in self.enum_errors:
            rows.setdefault(
                e["surface"],
                {
                    "discovered": 0,
                    "saved": 0,
                    "retried": 0,
                    "unresolved": 0,
                    "thin": 0,
                    "http404": 0,
                    "moved": 0,
                    "gone": 0,
                },
            )["unresolved"] += 1
        return rows

    def write(self):
        for r in self.records.values():
            if r["status"] == "pending":
                r["status"], r["note"] = "unresolved", "처리되지 않음(중단 또는 누락)"
        os.makedirs(os.path.join(self.state_dir, "runs"), exist_ok=True)
        os.makedirs(os.path.join(self.state_dir, "surfaces"), exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        run = {
            "collector": self.collector,
            "argv": self.argv,
            "started": self.started,
            "finished": now_iso(),
            "complete_surfaces": sorted(self.complete),
            "counts": self.counts(),
            "enumeration_errors": self.enum_errors,
            "records": sorted(self.records.values(), key=lambda r: r["url"]),
        }
        run_fp = os.path.join(self.state_dir, "runs", f"{stamp}-{self.collector}.json")
        _dump(run_fp, run)
        surfaces = (
            {r["surface"] for r in self.records.values()}
            | {e["surface"] for e in self.enum_errors}
            | self.complete
        )
        for s in surfaces:
            merge_surface(
                self.state_dir,
                s,
                self.collector,
                run_fp,
                [r for r in self.records.values() if r["surface"] == s],
                [e for e in self.enum_errors if e["surface"] == s],
                s in self.complete,
                {"stale_checked": self.stale_checked[s]} if s in self.stale_checked else None,
            )
        return run_fp

    def report(self):
        rows = self.counts()
        for s in sorted(rows):
            c = rows[s]
            print(
                f"manifest[{s}]: 발견 {c['discovered']} / 저장 {c['saved']} / 재시도 {c['retried']} / "
                f"unresolved {c['unresolved']} / thin {c['thin']} / 404 {c['http404']} "
                f"(moved {c['moved']}, gone {c['gone']})",
                flush=True,
            )
        bad = self.unresolved()
        for r in bad[:20]:
            print(
                f"  unresolved: {r['url']} [{r.get('http') or ''} {r.get('error') or r.get('note', '')}]".rstrip(),
                flush=True,
            )
        return len(bad)


def _dump(fp, data):
    tmp = fp + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write("\n")
    os.replace(tmp, fp)


def surface_path(state_dir, surface):
    return os.path.join(state_dir, "surfaces", f"{surface}.json")


def load_surface(state_dir, surface):
    fp = surface_path(state_dir, surface)
    if not os.path.isfile(fp):
        return None
    with open(fp, encoding="utf-8") as f:
        return json.load(f)


def merge_surface(
    state_dir, surface, collector, run_fp, records, enum_errors, complete, extra=None
):
    prev = load_surface(state_dir, surface) or {}
    if complete:
        urls = {r["url"]: r for r in records}
        state = {"last_full_run": run_fp, "enumeration_errors": enum_errors}
    else:
        urls = dict(prev.get("urls", {}))
        urls.update({r["url"]: r for r in records})
        state = {
            "last_full_run": prev.get("last_full_run", ""),
            "enumeration_errors": prev.get("enumeration_errors", []) + enum_errors,
        }
    state.update(
        {
            "surface": surface,
            "collector": collector,
            "updated": now_iso(),
            "last_run": run_fp,
            "urls": urls,
        }
    )
    state["stale_checked"] = prev.get("stale_checked", {})  # stale 검증을 새로 하지 않은 실행은 이전 판정을 유지
    state.update(extra or {})
    os.makedirs(os.path.dirname(surface_path(state_dir, surface)), exist_ok=True)
    _dump(surface_path(state_dir, surface), state)


# ---------------------------------------------------------------- 수집 루프

def collect(urls, fetch, policy, concurrency, slugs=None, allowed_hosts=None, every=50, label=""):
    """재시도 + 404 판정을 병렬로 수행. [(주 결과, 이동 대상 결과|None)]."""
    results = []
    with ThreadPoolExecutor(max_workers=max(1, concurrency)) as ex:
        futs = [ex.submit(fetch_resolved, fetch, u, policy, slugs, allowed_hosts) for u in urls]
        for i, f in enumerate(as_completed(futs), 1):
            results.append(f.result())
            if i % every == 0:
                print(f"  {label}{i}/{len(urls)}", flush=True)
    return results


def candidate_pages(results, min_len, discovered):
    """저장 후보 본문. 이동 대상은 이번 발견 집합에 없을 때만 대상 URL로 저장한다."""
    pages = {}
    for res, moved in results:
        if res.status == 200 and not res.error and res.resolution not in ("moved", "gone", "unresolved") \
                and len(res.body.strip()) >= min_len:
            pages[res.url] = res.body
        if moved is not None and moved.url not in discovered and len(moved.body.strip()) >= min_len:
            pages[moved.url] = moved.body
    return pages


def keep_pages(pages, min_len, measure=lambda m: m):
    """boilerplate 제거·정리 후 다시 길이를 잰다. 비어 버린 문서는 저장하지 않는다(thin)."""
    kept, dropped = {}, {}
    for u, m in pages.items():
        n = len(measure(m).strip())
        if n >= min_len:
            kept[u] = m
        else:
            dropped[u] = n
    return kept, dropped


def record_results(manifest, results, saved, dropped, min_len):
    for res, moved in results:
        if res.url in dropped:
            res.thin_reason = f"boilerplate 제거 후 본문 {dropped[res.url]}자 < {min_len}"
        manifest.result(res, res.url in saved, min_len)
        if moved is not None and moved.url in saved:
            manifest.result(moved, True, min_len)


# ---------------------------------------------------------------- stale 검증

SOURCE_RE = re.compile(r"^<!-- source: (\S+) -->")


def source_url(fp):
    with open(fp, encoding="utf-8", errors="replace") as f:
        m = SOURCE_RE.match(f.readline())
    return m.group(1) if m else ""


def _norm(url):
    p = urlsplit(url)
    return p.netloc + p.path.rstrip("/")


def stale_files(repo, surface, urls):
    known = {os.path.abspath(md_dest(repo, u)) for u in urls}
    return [f for f in surface_files(repo, surface) if os.path.abspath(f) not in known]


def live_seeds(state_dir, surface):
    """이전 stale 검증에서 공개 상태로 확인된 sitemap 밖 URL. 다음 실행의 발견 집합에 편입한다."""
    st = load_surface(state_dir, surface) or {}
    return {v["url"] for v in st.get("stale_checked", {}).values() if v.get("verdict") == "live" and v.get("url")}


def verify_stale(manifest, repo, surface, known_urls, fetch, policy, concurrency, soft_target=None, adopt_live=True):
    """발견 집합 밖 생성물의 원본을 확인해 moved/gone/live/unresolved로 판정한다. 파일은 지우지 않는다.

    fetch(url)는 final_url(HTTP redirect 후 주소)과 body를 채운 Result를 돌려줘야 한다.
    live는 이번 실행에 existing으로 기록하고 이후 실행의 발견 집합에 편입한다. adopt_live는 bool 또는 url -> bool.
    """
    files = stale_files(repo, surface, known_urls)

    def check(fp):
        url = source_url(fp)
        v = {"url": url, "checked_at": now_iso()}
        if not url:
            return fp, dict(v, verdict="unresolved", note="source 헤더 없음")
        r = policy.run(fetch, url)
        v["http"] = r.status
        if r.error:
            v.update(verdict="unresolved", note=r.error[:120])
        elif r.status == 200:
            final = r.final_url or url
            soft = soft_target(url, r.body) if soft_target else ""
            if _norm(final) != _norm(url):
                v.update(verdict="moved", target=final)
            elif soft and _norm(soft) != _norm(url):
                v.update(verdict="moved", target=soft)
            else:
                v.update(verdict="live")
        elif r.status in (404, 410):
            again = policy.run(fetch, url)
            v.update(verdict="gone" if again.status in (404, 410) else "unresolved",
                     note=f"{r.status} 재확인 {again.status or again.kind}")
        else:
            v.update(verdict="unresolved", note=f"http {r.status}")
        return fp, v

    # 이전에 live로 편입된 URL은 이번에는 발견 집합 안이라 stale로 안 잡힌다. 판정을 유지해야 다음 실행에서도 편입된다.
    prev = (load_surface(manifest.state_dir, surface) or {}).get("stale_checked", {})
    known = set(known_urls)
    checked = {rel: v for rel, v in prev.items() if v.get("verdict") == "live" and v.get("url") in known}
    adopt = adopt_live if callable(adopt_live) else (lambda _u: adopt_live)
    with ThreadPoolExecutor(max_workers=max(1, concurrency)) as ex:
        for fp, v in ex.map(check, files):
            checked[os.path.relpath(fp, repo)] = v
            if v["verdict"] == "live" and adopt(v["url"]):
                manifest.discover([v["url"]])
                manifest.mark(v["url"], "existing", http=200, note="sitemap 밖 공개 URL(stale 검증)")
    manifest.stale_checked[surface] = checked
    counts = {}
    for v in checked.values():
        counts[v["verdict"]] = counts.get(v["verdict"], 0) + 1
    print(f"  stale 검증[{surface}]: 파일 {len(files)} -> {counts}", flush=True)
    return checked


# ---------------------------------------------------------------- coverage


def md_dest(out, url):
    """crawl-mirror.dest와 같은 규칙(<host>/<path>.md, 루트는 <host>.md)."""
    sp = urlsplit(url)
    path = sp.path.strip("/")
    return os.path.join(out, f"{sp.netloc}/{path}" if path else sp.netloc) + ".md"


def surface_files(repo, surface):
    files = []
    for host in SURFACE_HOSTS.get(surface, []):
        root_md = os.path.join(repo, host + ".md")
        if os.path.isfile(root_md):
            files.append(root_md)
        base = os.path.join(repo, host)
        for current, dirs, names in os.walk(base):
            dirs[:] = [
                d for d in dirs if not d.endswith((".parts", ".assets"))
            ]  # 분할 조각·자산은 원 문서 소속
            files.extend(os.path.join(current, n) for n in names if n.endswith(".md"))
    return files


def body_len(fp):
    with open(fp, encoding="utf-8", errors="replace") as f:
        lines = f.read().splitlines()
    return len("\n".join(lines[1:]).strip())


def coverage(repo, state_dir=""):
    """표면별 coverage 행과 완결 여부. 네트워크를 쓰지 않는다."""
    state_dir = state_dir or os.path.join(repo, STATE_DIR)
    rows, problems = [], []
    for surface, label in SURFACES:
        st = load_surface(state_dir, surface)
        row = {
            "surface": surface,
            "label": label,
            "discovered": 0,
            "saved": 0,
            "retried": 0,
            "unresolved": 0,
            "thin": 0,
            "http404": 0,
            "stale": 0,
            "state": "missing",
        }
        if st is None:
            problems.append(
                f"{label}: manifest 없음 (수집기를 전체 범위로 실행해야 함)"
            )
            rows.append(row)
            continue
        recs = list(st.get("urls", {}).values())
        row["state"] = "full" if st.get("last_full_run") else "partial"
        if not st.get("last_full_run"):
            problems.append(f"{label}: 전체 범위 실행 기록 없음(부분 실행만 있음)")
        row["discovered"] = len(recs)
        row["saved"] = sum(r["status"] in SAVED for r in recs)
        row["retried"] = sum(bool(r.get("retried")) for r in recs)
        row["unresolved"] = sum(
            r["status"] in ("unresolved", "pending") for r in recs
        ) + len(st.get("enumeration_errors", []))
        row["http404"] = sum(r.get("http") in (404, 410) for r in recs)
        thin_urls = {r["url"] for r in recs if r["status"] == "thin"}
        if not st.get("last_full_run"):
            row["stale"] = None  # 발견 집합이 부분이면 stale을 셀 수 없다.
            row["thin"] = len(thin_urls)
        elif "stale" in st:  # YouTube/PDF는 전용 감사가 계산해 넣는다.
            row["stale"] = len(st["stale"])
            row["thin"] = len(thin_urls)
        else:
            known = {
                os.path.abspath(md_dest(repo, r["url"])): r
                for r in recs
                if r["status"] not in ("gone", "moved")
            }
            files = [os.path.abspath(f) for f in surface_files(repo, surface)]
            stale = [f for f in files if f not in known]
            row["stale"] = len(stale)
            verdicts = st.get("stale_checked", {})
            kinds = {}
            for f in stale:
                k = verdicts.get(os.path.relpath(f, repo), {}).get("verdict", "unchecked")
                kinds[k] = kinds.get(k, 0) + 1
            row["stale_kinds"] = kinds
            if kinds.get("unresolved"):
                problems.append(f"{label}: stale 검증 unresolved {kinds['unresolved']}개")
            empty = {known[f]["url"] for f in files if f in known and body_len(f) < 20}
            row["thin"] = len(thin_urls | empty)
        if row["unresolved"]:
            problems.append(f"{label}: unresolved {row['unresolved']}개")
        rows.append(row)
    return rows, problems


def print_coverage(rows, problems):
    head = f"{'surface':<18} {'발견':>6} {'저장':>6} {'재시도':>5} {'unres':>5} {'thin':>5} {'404':>5} {'stale':>5}  state"
    print("URL coverage (표면별)")
    print("  " + head)
    for r in rows:
        print(
            f"  {r['surface']:<18} {r['discovered']:>6} {r['saved']:>6} {r['retried']:>5} {r['unresolved']:>5} "
            f"{r['thin']:>5} {r['http404']:>5} {'-' if r['stale'] is None else r['stale']:>5}  {r['state']}"
        )
    for r in rows:
        if r.get("stale_kinds") and r["stale"]:
            print(f"  stale[{r['surface']}]: " + ", ".join(f"{k} {v}" for k, v in sorted(r["stale_kinds"].items())))
    total_unres = sum(r["unresolved"] for r in rows)
    if problems:
        print(f"coverage 미완결 (unresolved 합계 {total_unres}):")
        for p in problems:
            print(f"  - {p}")
    else:
        print("coverage 완결: 모든 표면이 전체 범위 manifest를 갖고 unresolved=0")


def self_test():
    import tempfile

    calls = []

    def flaky(url):
        calls.append(url)
        if len(calls) < 3:
            return Result(url, status=429, retry_after=0)
        return Result(url, body="x" * 300, status=200)

    p = RetryPolicy(retries=3, backoff=0.01, max_wait=0.02)
    r = p.run(flaky, "https://academy.openai.com/a")
    assert r.status == 200 and r.attempts == 3
    r = RetryPolicy(retries=1, backoff=0.01, max_wait=0.01).run(
        lambda u: Result(u, status=503), "https://academy.openai.com/b"
    )
    assert r.status == 503 and r.attempts == 2
    assert (
        RetryPolicy(0, 0.01, 0.01)
        .run(lambda u: 1 / 0, "https://x/")
        .error.startswith("ZeroDivisionError")
    )

    pages = {"https://academy.openai.com/public/new/some-lesson": 200}

    def site(url):
        return Result(
            url,
            body="y" * 300 if pages.get(url) == 200 else "",
            status=pages.get(url, 404),
        )

    res, moved = fetch_resolved(
        site, "https://academy.openai.com/public/old/some-lesson", p, slug_index(pages)
    )
    assert (
        res.resolution == "moved"
        and moved.url == "https://academy.openai.com/public/new/some-lesson"
    )
    res, moved = fetch_resolved(
        site, "https://academy.openai.com/public/old/gone-lesson", p, slug_index(pages)
    )
    assert res.resolution == "gone" and moved is None
    # 클럽 사본 12개가 모두 404이고 공개 정본은 얕은 경로 하나뿐인 경우(2026-09-30 Academy 실측).
    clubs = [f"https://academy.openai.com/public/clubs/c{i:02d}/videos/builder-bootcamp-rag" for i in range(12)]
    live = "https://academy.openai.com/public/videos/builder-bootcamp-rag"

    def club_site(url):
        return Result(url, body="z" * 300 if url == live else "", status=200 if url == live else 404)

    res, moved = fetch_resolved(club_site, clubs[0], p, slug_index(clubs + [live]))
    assert res.resolution == "moved" and moved.url == live, res.note
    seen = []

    def first_404_then_403(
        url,
    ):  # 첫 응답만 404, 재확인은 403 -> 삭제로 확정할 수 없다.
        seen.append(url)
        return Result(url, status=404 if len(seen) == 1 else 403)

    res, _ = fetch_resolved(first_404_then_403, "https://academy.openai.com/x", p)
    assert res.resolution == "unresolved"

    d = tempfile.mkdtemp()
    m = Manifest(d, "t", [])
    m.complete.add("academy")
    m.discover(["https://academy.openai.com/a", "https://academy.openai.com/b"])
    m.existing(["https://academy.openai.com/a"])
    m.result(Result("https://academy.openai.com/b", status=429), False, 150)
    assert len(m.unresolved()) == 1
    m.write()
    os.makedirs(os.path.join(d, "academy.openai.com"))
    for name in ("a.md", "orphan.md"):
        with open(os.path.join(d, "academy.openai.com", name), "w") as f:
            f.write(
                "<!-- source: https://academy.openai.com/x -->\n\nbody long enough here\n"
            )
    rows, problems = coverage(d)
    ac = next(r for r in rows if r["surface"] == "academy")
    assert (ac["discovered"], ac["saved"], ac["unresolved"], ac["stale"]) == (
        2,
        1,
        1,
        1,
    ), ac
    assert any("unresolved" in p for p in problems)
    pol = RetryPolicy(0, 0.01, 0.01)

    def web(url):
        r = Result(url, status=200 if "moved" in url or "live" in url else 404)
        r.final_url = url.replace("old-moved", "new") if "moved" in url else url
        return r

    for name in ("old-moved", "still-live", "dead"):
        with open(os.path.join(d, "academy.openai.com", name + ".md"), "w") as f:
            f.write(f"<!-- source: https://academy.openai.com/{name} -->\n\nbody long enough here\n")
    m2 = Manifest(d, "t2", [])
    m2.complete.add("academy")
    m2.discover(["https://academy.openai.com/a"])
    m2.existing(["https://academy.openai.com/a"])
    got = verify_stale(m2, d, "academy", ["https://academy.openai.com/a"], web, pol, 2)
    verdicts = {k.rsplit("/", 1)[-1]: v["verdict"] for k, v in got.items()}
    assert verdicts == {"old-moved.md": "moved", "still-live.md": "live", "dead.md": "gone", "orphan.md": "gone"}, verdicts
    m2.write()
    assert live_seeds(os.path.join(d, STATE_DIR), "academy") == {"https://academy.openai.com/still-live"}
    m3 = Manifest(d, "t3", [])
    m3.complete.add("academy")
    known3 = ["https://academy.openai.com/a", "https://academy.openai.com/still-live"]
    m3.discover(known3)
    verify_stale(m3, d, "academy", known3, web, pol, 2)
    m3.write()
    assert live_seeds(os.path.join(d, STATE_DIR), "academy") == {"https://academy.openai.com/still-live"}  # 진동 없음
    print("self-test ok")


if __name__ == "__main__":
    import sys

    if sys.argv[1:] == ["--self-test"]:
        self_test()

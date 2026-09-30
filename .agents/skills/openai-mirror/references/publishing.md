# 갱신과 발행

미러 갱신, 검증, commit, push 절차의 정본이다.

## 증분 갱신

repo root에서 실행한다.

```bash
bash .agents/skills/openai-mirror/scripts/refresh.sh --check
bash .agents/skills/openai-mirror/scripts/refresh.sh
```

이 entrypoint는 공개 사이트, Academy, 공식 문서, YouTube, 페이지 인라인 자막, Vimeo 렌더, OpenAI 소유 PDF를 순서대로 갱신하고, YouTube 색인과 PDF coverage 상태를 기록한 뒤 worktree 생성물과 전체 트리를 검증한다. Python 의존성이 없으면 기존 `uv` 환경에 필요한 패키지만 설치한다.

한 단계가 실패해도 나머지 단계는 끝까지 실행하고, 마지막에 `refresh 미완료: 실패 단계 ...`와 함께 non-zero로 끝난다. 이때는 완료로 보고하지 않고 `_mirror-state/runs/`의 최신 manifest에서 unresolved URL을 확인한다. Academy 429처럼 일시 오류로 남은 URL은 다음 명령으로 그 URL만 다시 받을 수 있다.

```bash
python3 .agents/skills/openai-mirror/scripts/academy-extract.py . --retry-unresolved
```

`--check`는 의존성 preflight만 실행한다. 원본 최신성, 전체 생성물 provenance, 표면별 URL coverage는 다음 감사로 확인한다. coverage 표에서 모든 표면이 `full`이고 unresolved 합계가 0이어야 완료다.

```bash
python3 .agents/skills/openai-mirror/scripts/verify-publish.py . --tree-audit
```

사이트, Academy, 공식 문서의 기존 본문까지 다시 받으려면 다음을 쓴다.

```bash
bash .agents/skills/openai-mirror/scripts/refresh.sh --force
```

YouTube 자막을 캐시에서 다시 받거나 영상 참조만 다시 렌더링할 때는 다음 옵션을 함께 전달할 수 있다.

```bash
bash .agents/skills/openai-mirror/scripts/refresh.sh --refetch
bash .agents/skills/openai-mirror/scripts/refresh.sh --render-only
```

원본 열거에서 사라진 문서는 매 실행 `삭제 후보`/`stale 후보`로 출력되고 `_mirror-state/surfaces/`에 남는다. `--prune-stale`는 그 목록을 사용자에게 보여 주고 삭제 승인을 받은 뒤에만 사용한다. 이 옵션은 Deployment Safety 구 생성물과 YouTube 색인 밖 파일을 목록 출력 후 지운다.

## 검토와 commit

1. `git status --short`와 `git diff --stat`로 변경 도메인과 규모를 확인한다.
2. 변경된 생성물 도메인만 `git add -A -- <domain-root>...`로 스테이징한다.
3. 다음 staged 검증을 실행한다.
4. diff가 있으면 그 회차의 추가·변경 영역을 설명하는 commit 하나를 만든다.

```bash
python3 .agents/skills/openai-mirror/scripts/verify-publish.py . --staged
python3 .agents/skills/openai-mirror/scripts/verify-publish.py . --tree-audit
git diff --cached --stat
git commit -m "Update mirror: <changed area> (YYYY-MM-DD)"
```

`README.md`, `README.ko.md`, `AGENTS.md`, `.agents/` 같은 소스 변경은 생성물 갱신 commit과 분리한다. 생성물 diff가 없으면 빈 commit을 만들지 않는다.

## push와 완료 확인

push는 사용자가 `push` 또는 그에 준하는 명시적 요청을 한 경우에만 수행한다. `openai-mirror` 호출이나 일반 갱신 요청만으로는 push 승인을 포함하지 않는다.

1. `git log --oneline @{upstream}..HEAD`와 `git diff --stat @{upstream}..HEAD`로 전송될 전체 범위를 확인한다.
2. 미러 갱신 관련 commit만 있으면 `git push`한다. 새 diff가 없어도 검증된 미전송 commit이 있으면 push한다.
3. `git rev-parse HEAD`와 `git rev-parse @{upstream}`이 같은지 확인한 뒤 완료를 보고한다.

예상 밖 commit, 불명확한 upstream, 검증 실패가 있으면 push하지 않고 정확한 범위를 보고한다. force push는 사용하지 않는다.

## 삭제 반영

증분 실행은 원본에서 사라진 페이지를 자동 삭제하지 않는다. 삭제를 반영할 때는 삭제 목록을 먼저 검토하고 다음 두 검증에만 `--allow-deletes`를 붙인다.

```bash
python3 .agents/skills/openai-mirror/scripts/verify-publish.py . --allow-deletes
python3 .agents/skills/openai-mirror/scripts/verify-publish.py . --staged --allow-deletes
```

예상하지 않은 rename/copy, 100MB 초과 파일, source header 누락, 허용 도메인 밖 변경은 발행하지 않는다.

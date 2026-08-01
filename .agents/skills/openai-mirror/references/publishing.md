# 갱신과 발행

미러 갱신, 검증, commit, push 절차의 정본이다.

## 증분 갱신

repo root에서 실행한다.

```bash
bash .agents/skills/openai-mirror/scripts/refresh.sh --check
bash .agents/skills/openai-mirror/scripts/refresh.sh
```

이 entrypoint는 공개 사이트, Academy, 공식 문서, YouTube, 페이지 인라인 자막, Vimeo 렌더, OpenAI 소유 PDF를 순서대로 갱신한 뒤 worktree 생성물을 검증한다. Python 의존성이 없으면 기존 `uv` 환경에 필요한 패키지만 설치한다.

사이트, Academy, 공식 문서의 기존 본문까지 다시 받으려면 다음을 쓴다.

```bash
bash .agents/skills/openai-mirror/scripts/refresh.sh --force
```

## 검토와 commit

1. `git status --short`와 `git diff --stat`로 변경 도메인과 규모를 확인한다.
2. 변경된 생성물 도메인만 `git add -A -- <domain-root>...`로 스테이징한다.
3. 다음 staged 검증을 실행한다.
4. diff가 있으면 그 회차의 추가·변경 영역을 설명하는 commit 하나를 만든다.

```bash
python3 .agents/skills/openai-mirror/scripts/verify-publish.py . --staged
git diff --cached --stat
git commit -m "Update mirror: <changed area> (YYYY-MM-DD)"
```

`README.md`, `README.ko.md`, `AGENTS.md`, `.agents/` 같은 소스 변경은 생성물 갱신 commit과 분리한다. 생성물 diff가 없으면 빈 commit을 만들지 않는다.

## push와 완료 확인

이 스킬로 일반 갱신·재생성을 요청한 것은 현재 branch의 검증된 미전송 미러 관련 commit을 public repo에 push하는 승인까지 포함한다. 별도 확인을 위해 중단하지 않는다.

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

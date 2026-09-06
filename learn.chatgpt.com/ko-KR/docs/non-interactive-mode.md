<!-- source: https://learn.chatgpt.com/ko-KR/docs/non-interactive-mode -->

비대화형 모드에서는 대화형 TUI를 열지 않고 스크립트(예: 지속적 통합(CI) 작업)에서 Codex를 실행할 수 있습니다.
`codex exec` 명령어로 실행합니다.

플래그별 자세한 내용은 [`codex exec`](/codex/developer-commands?surface=cli#cli-codex-exec)에서 확인하세요.

## `codex exec` 사용 시점

Codex로 다음 작업을 수행하려면 `codex exec` 명령어를 사용하세요:

- 파이프라인(CI, 병합 전 검사, 예약 작업)의 일부로 실행합니다.
- 다른 도구로 파이프할 수 있는 출력을 생성합니다(예: 릴리스 노트 또는 요약 생성).
- 명령어 출력을 Codex로 보내고 Codex 출력을 다른 도구로 전달하는 CLI 워크플로우에 자연스럽게 통합합니다.
- 명시적으로 사전 설정한 샌드박스와 승인 설정으로 실행합니다.

## 기본 사용법

작업 프롬프트를 하나의 인수로 전달하세요:

```bash
codex exec "summarize the repository structure and list the top 5 risky areas"

`codex exec` 명령어가 실행되는 동안 Codex는 진행 상황을 `stderr`로 스트리밍하고 최종 에이전트 메시지만 `stdout`에 출력합니다. 따라서 최종 결과를 쉽게 리디렉션하거나 파이프로 전달할 수 있습니다:

```bash
codex exec "generate release notes for the last 10 commits" | tee release-notes.md

세션 롤아웃 파일을 디스크에 저장하지 않으려면 `--ephemeral` 옵션을 사용하세요:

```bash
codex exec --ephemeral "triage this repository and suggest next steps"

stdin이 파이프로 연결된 상태에서 프롬프트 인수도 제공하면 Codex는 프롬프트를 지시문으로, 파이프로 전달된 내용을 추가 컨텍스트로 처리합니다.

명령어 하나로 입력을 생성해 Codex에 직접 전달할 수 있습니다:

```bash
curl -s https://jsonplaceholder.typicode.com/comments \
  | codex exec "format the top 20 items into a markdown table" \
  > table.md

더 복잡한 stdin 파이핑 패턴은 [고급 stdin 파이핑](#advanced-stdin-piping)을 참고하세요.

## 권한과 안전

기본적으로 `codex exec` 명령어는 읽기 전용 샌드박스에서 실행됩니다. 자동화 환경에서는 워크플로우에 필요한 최소 권한만 설정하세요:

- 편집 허용: `codex exec --sandbox workspace-write "<task>"`
- 더 광범위한 접근 허용: `codex exec --sandbox danger-full-access "<task>"`

`danger-full-access`는 통제된 환경(예: 격리된 CI 러너 또는 컨테이너)에서만 사용하세요.

Codex는 `codex exec --full-auto`를 사용 중단 예정(deprecated)인 호환성 플래그로 유지하며 경고를 출력합니다. 새 스크립트에서는 명시적인 `--sandbox workspace-write` 플래그를 사용하세요.

실행 시 `$CODEX_HOME/config.toml` 파일을 불러오지 않으려면 `--ignore-user-config` 옵션을 사용하고, 통제된 자동화 환경에서 사용자와 프로젝트의 execpolicy `.rules` 파일을 건너뛰려면 `--ignore-rules` 옵션을 사용하세요.

활성화된 MCP 서버를 `required = true`로 설정했는데 초기화에 실패하면 `codex exec` 명령어는 해당 서버 없이 계속 실행되지 않고 오류와 함께 종료됩니다.

## 기계 판독 가능한 출력 만들기

스크립트에서 Codex 출력을 처리하려면 JSON Lines 출력을 사용하세요:

```bash
codex exec --json "summarize the repo structure" | jq

`--json` 옵션을 활성화하면 `stdout` 출력이 JSON Lines(JSONL) 스트림으로 바뀌어 Codex가 실행 중 내보내는 모든 이벤트를 캡처할 수 있습니다. 이벤트 유형에는 `thread.started`, `turn.started`, `turn.completed`, `turn.failed`, `item.*`, `error` 등이 포함됩니다.

항목 유형에는 에이전트 메시지, 추론, 명령어 실행, 파일 변경, MCP 도구 호출, 웹 검색, 계획 업데이트가 포함됩니다.

JSON 스트림 예시(각 줄은 JSON 객체):

```jsonl
{"type":"thread.started","thread_id":"0199a213-81c0-7800-8aa1-bbab2a035a53"}
{"type":"turn.started"}
{"type":"item.started","item":{"id":"item_1","type":"command_execution","command":"bash -lc ls","status":"in_progress"}}
{"type":"item.completed","item":{"id":"item_3","type":"agent_message","text":"Repo contains docs, sdk, and examples directories."}}
{"type":"turn.completed","usage":{"input_tokens":24763,"cached_input_tokens":24448,"output_tokens":122,"reasoning_output_tokens":0}}

최종 메시지만 필요하면 `-o <path>`/`--output-last-message <path>` 옵션을 사용해 파일에 기록하세요. 최종 메시지는 파일에 기록되는 동시에 `stdout`에도 출력됩니다(자세한 내용은 [`codex exec`](/codex/developer-commands?surface=cli#cli-codex-exec)에서 확인하세요).

## 스키마로 구조화된 출력값 만들기

후속 단계에서 구조화된 데이터가 필요하면 `--output-schema` 옵션을 사용해 JSON Schema를 준수하는 최종 응답을 요청하세요.
이 방식은 작업 요약, 위험 보고서, 릴리스 메타데이터 등 안정적인 필드가 필요한 자동화 워크플로우에 유용합니다.

`schema.json`

```json
{
  "type": "object",
  "properties": {
    "project_name": { "type": "string" },
    "programming_languages": {
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["project_name", "programming_languages"],
  "additionalProperties": false
}

스키마를 지정해 Codex를 실행하고 최종 JSON 응답을 디스크에 저장하세요:

```bash
codex exec "Extract project metadata" \
  --output-schema ./schema.json \
  -o ./project-metadata.json

최종 출력 예시(stdout):

```json
{
  "project_name": "Codex CLI",
  "programming_languages": ["Rust", "TypeScript", "Shell"]
}

## 자동화 환경에서 인증하기

`codex exec` 명령어는 기본적으로 저장된 CLI 인증 정보를 재사용합니다. CI에서는 일반적으로 자격 증명을 명시적으로 제공합니다:

신뢰할 수 있는 클라우드 또는 CI 런타임이 이미 수명이 짧은 워크로드
토큰을 받는다면, OpenAI 자격 증명을 저장하는 대신
[워크로드 ID 페더레이션](/ko-KR/codex/enterprise/workload-identity)을
사용하세요.

### API 키 인증 사용

GitHub Actions에서는 CLI를 직접 설치하고 인증하는 대신 [Codex GitHub Action](/ko-KR/codex/github-action)을 사용하세요. 이 GitHub Action은 Codex를 설치하고 Responses API 프록시를 시작한 뒤 구성 가능한 안전 전략으로 Codex를 실행하여 API 키 노출을 줄이도록 설계되었습니다.

레포지토리에서 관리하는 코드를 체크아웃하거나 실행하는 워크플로우에서는 `OPENAI_API_KEY` 또는 `CODEX_API_KEY`를 작업 수준의 환경 변수로 설정하지 마세요. 같은 작업에서 실행되는 빌드 스크립트, 테스트, 종속성 수명 주기 훅 또는 침해된 액션이 해당 환경 변수를 읽을 수 있습니다.

다른 자동화 환경에서는 `CODEX_API_KEY`를 해당 키가 필요한 Codex
호출에만 설정하고, 동일한
프로세스 환경에서 신뢰할 수 없는 코드가 실행되지 않도록 하세요.

한 번 실행할 때 다른 API 키를 사용하려면 `CODEX_API_KEY`를 인라인으로 설정하세요:

```bash
CODEX_API_KEY=<api-key> codex exec --json "triage open bug reports"

`CODEX_API_KEY`는 `codex exec`, `codex review`, TypeScript
SDK 및 `codex exec-server --remote`와 함께 사용할 수 있습니다.

API 키 대신 Codex 사용자 계정으로 CI/CD 작업을 실행해야 한다면 이 내용을 읽어보세요.
예를 들어 신뢰할 수 있는 러너에서 ChatGPT 관리형 Codex 액세스를 사용하는 엔터프라이즈 팀이나
API 키 사용 대신 ChatGPT/Codex 요청 한도가 필요한 사용자가 이에 해당합니다.

API 키는 프로비저닝과 교체가 더 간단하므로 자동화의 기본 인증 방식으로 적합합니다.
특별히 Codex 계정으로 실행해야 하는 경우에만
이 방식을 사용하세요.

`~/.codex/auth.json`에는 액세스 토큰이 포함되어 있으므로 비밀번호처럼 취급하세요. 이 파일을
커밋하거나 티켓에 붙여 넣거나 채팅으로 공유하지 마세요.

공개 또는 오픈 소스 레포지토리에서는 이 워크플로우를 사용하지 마세요. 러너에서 `codex login`
명령어를 사용할 수 없다면 보안 스토리지를 통해 `auth.json` 파일을 미리 배치하고,
러너에서 Codex를 실행해 Codex가 동일한 위치에서 파일을 갱신하도록 한 다음, 갱신된 파일을
실행 사이에도 유지하세요.

[CI/CD에서 Codex 계정 인증 유지(고급)](/codex/auth/ci-cd-auth)을 참고하세요.

## 비대화형 세션 재개

이전 실행을 이어서 진행해야 한다면(예: 2단계 파이프라인) `resume` 하위 명령어를 사용하세요:

```bash
codex exec "review the change for race conditions"
codex exec resume --last "fix the race conditions you found"

`codex exec resume <SESSION_ID>` 명령어로 특정 세션 ID를 지정할 수도 있습니다.

## Git 레포지토리 필수

Codex는 파괴적인 변경을 방지하기 위해 Git 레포지토리 안에서 명령어를 실행하도록 요구합니다. 환경이 안전하다고 확신하면 `codex exec --skip-git-repo-check` 옵션으로 이 검사를 건너뛸 수 있습니다.

## 일반적인 자동화 패턴

### 예시: GitHub Actions에서 CI 실패 자동 수정

GitHub Actions 워크플로우에서는 Codex를 설치하고 API 키를 셸 단계에 전달하는 대신 [`openai/codex-action`](https://github.com/openai/codex-action)을 사용하세요. 이 GitHub Action은 OpenAI API 키를 위한 보안 프록시를 시작합니다.

CI 워크플로우가 실패할 때 Codex가 수정안을 자동으로 제안하도록 할 수 있습니다. 패턴은 다음과 같습니다:

1. 메인 CI 워크플로우가 오류로 종료되면 후속 워크플로우를 트리거합니다.
2. 레포지토리 읽기 권한만으로 실패를 일으킨 커밋을 체크아웃합니다.
3. Codex를 실행하기 전에 설정 명령어를 실행하되, 해당 단계에 OpenAI API 키를 노출하지 않습니다.
4. Codex GitHub Action을 실행합니다.
5. Codex의 로컬 변경 사항을 패치 아티팩트로 저장합니다.
6. 별도의 작업에서 패치를 적용하고 Pull Request를 생성하세요.

아래 Codex 작업에는 `contents: read`만 설정되어 있습니다. Codex 실행 후에는 diff만 아티팩트로 직렬화합니다. `open_pr` 작업에는 레포지토리 쓰기 권한이 부여되지만 `OPENAI_API_KEY`는 전달되지 않습니다.

이 예시는 Node.js 프로젝트를 가정합니다. 사용하는 스택에 맞게 설정 및 테스트 명령을 조정하세요.

더 자세한 보안 체크리스트는 [Codex GitHub Action 보안 가이드](https://github.com/openai/codex-action/blob/main/docs/security.md)를 참조하세요.

```yaml
name: Codex auto-fix on CI failure

on:
  workflow_run:
    workflows: ["CI"]
    types: [completed]

jobs:
  generate_fix:
    if: ${{ github.event.workflow_run.conclusion == 'failure' }}
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      has_patch: ${{ steps.diff.outputs.has_patch }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.workflow_run.head_sha }}
          fetch-depth: 0
          persist-credentials: false

      - uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install dependencies
        run: |
          if [ -f package-lock.json ]; then npm ci; fi

      - name: Run Codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt: |
            The CI workflow "${{ github.event.workflow_run.name }}" failed for commit
            ${{ github.event.workflow_run.head_sha }}.

            Run `npm test --silent` to reproduce the failure. Identify the minimal
            change needed to make the tests pass, implement only that change, and
            run `npm test --silent` again.

            Do not refactor unrelated files.

      - name: Create patch artifact
        id: diff
        run: |
          git add -N .
          git diff --binary HEAD > codex.patch
          if [ -s codex.patch ]; then
            echo "has_patch=true" >> "$GITHUB_OUTPUT"
          else
            echo "has_patch=false" >> "$GITHUB_OUTPUT"
          fi

      - name: Upload patch artifact
        if: steps.diff.outputs.has_patch == 'true'
        uses: actions/upload-artifact@v4
        with:
          name: codex-fix-patch
          path: codex.patch
          if-no-files-found: error

  open_pr:
    runs-on: ubuntu-latest
    needs: generate_fix
    if: needs.generate_fix.outputs.has_patch == 'true'
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.workflow_run.head_sha }}
          fetch-depth: 0

      - uses: actions/download-artifact@v4
        with:
          name: codex-fix-patch

      - name: Apply Codex patch
        run: git apply --index codex.patch

      - name: Open pull request
        env:
          GH_TOKEN: ${{ github.token }}
          FAILED_HEAD_BRANCH: ${{ github.event.workflow_run.head_branch }}
          FAILED_HEAD_SHA: ${{ github.event.workflow_run.head_sha }}
          RUN_ID: ${{ github.event.workflow_run.run_id }}
        run: |
          branch="codex/auto-fix-$RUN_ID"

          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git switch -c "$branch"
          git commit -m "Auto-fix failing CI via Codex"
          git push origin "$branch"

          {
            echo "Codex generated this patch after CI failed for \`$FAILED_HEAD_SHA\`."
            echo
            echo "Review the changes before merging."
          } > pr-body.md

          gh pr create \
            --base "$FAILED_HEAD_BRANCH" \
            --head "$branch" \
            --title "Auto-fix failing CI via Codex" \
            --body-file pr-body.md

## 고급 stdin 파이핑

다른 명령에서 Codex 입력을 생성하는 경우, 지침의 출처에 따라 stdin 패턴을 선택하세요. 지침을 이미 알고 있고 파이프로 전달되는 출력을 컨텍스트로 사용하려면 prompt-plus-stdin 방식을 사용하세요. stdin 전체를 프롬프트로 사용하려면 `codex exec -` 명령을 사용하세요.

### prompt-plus-stdin 사용

Prompt-plus-stdin은 다른 명령에서 Codex가 검사할 데이터를 이미 생성하는 경우 유용합니다. 이 모드에서는 지침을 직접 작성하고 출력을 파이프로 전달해 컨텍스트로 사용합니다. 따라서 명령 출력, 로그, 생성된 데이터를 기반으로 하는 CLI 워크플로우에 자연스럽게 활용할 수 있습니다.

```bash
npm test 2>&1 \
  | codex exec "summarize the failing tests and propose the smallest likely fix" \
  | tee test-summary.md

### 로그 요약

```bash
tail -n 200 app.log \
  | codex exec "identify the likely root cause, cite the most important errors, and suggest the next three debugging steps" \
  > log-triage.md

### TLS 또는 HTTP 문제 조사

```bash
curl -vv https://api.example.com/health 2>&1 \
  | codex exec "explain the TLS or HTTP failure and suggest the most likely fix" \
  > tls-debug.md

### Slack 게시용 업데이트 준비

```bash
gh run view 123456 --log \
  | codex exec "write a concise Slack-ready update on the CI failure, including the likely cause and next step" \
  | pbcopy

### CI 로그를 바탕으로 Pull Request 댓글 초안 작성

```bash
gh run view 123456 --log \
  | codex exec "summarize the failure in 5 bullets for the pull request thread" \
  | gh pr comment 789 --body-file -

### stdin을 프롬프트로 사용할 때 `codex exec -` 사용

프롬프트 인수를 생략하면 Codex는 stdin에서 프롬프트를 읽습니다. 이 동작을 명시적으로 강제하려면 `codex exec -` 명령을 사용하세요.

다른 명령이나 스크립트가 전체 프롬프트를 동적으로 생성할 때는 `-` 센티널이 유용합니다. 프롬프트를 파일에 저장하거나, 셸 스크립트로 프롬프트를 조합하거나, 실시간 명령 출력과 지침을 결합한 뒤 전체 프롬프트를 Codex에 전달하는 경우에 적합합니다.

```bash
cat prompt.txt | codex exec -

```bash
printf "Summarize this error log in 3 bullets:\n\n%s\n" "$(tail -n 200 app.log)" \
  | codex exec -

```bash
generate_prompt.sh | codex exec - --json > result.jsonl

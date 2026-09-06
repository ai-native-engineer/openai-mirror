<!-- source: https://learn.chatgpt.com/ko-KR/docs/github-action -->

Codex GitHub Action(`openai/codex-action@v1`)을 사용하면 GitHub Actions 워크플로우의 CI/CD 작업에서 Codex를 실행하고 패치를 적용하거나 검토 결과를 게시할 수 있습니다.
이 액션은 Codex CLI를 설치하고, API 키를 제공하면 Responses API 프록시를 시작하며, 지정한 권한으로 `codex exec` 명령을 실행합니다.

다음과 같은 작업에 이 액션을 사용하세요:

- CLI를 직접 관리하지 않고 Pull Request 또는 릴리스에 대한 Codex 피드백을 자동화합니다.
- CI 파이프라인의 일부로 Codex 기반 품질 검사를 통과한 변경 사항만 허용합니다.
- 워크플로우 파일에서 반복 가능한 Codex 작업(코드 검토, 릴리스 준비, 마이그레이션)을 실행합니다.

[비대화형 모드](/ko-KR/codex/non-interactive-mode)에서 CI 예시를 확인하고 [openai/codex-action 레포지토리](https://github.com/openai/codex-action)에서 소스 코드를 살펴보세요.

## 사전 요구 사항

- OpenAI 키를 GitHub 시크릿(예: `OPENAI_API_KEY`)으로 저장하고 워크플로우에서 참조하세요.
- Linux 또는 macOS 러너에서 작업을 실행하세요. Windows에서는 `safety-strategy: unsafe`로 설정하세요.
- Codex가 레포지토리 콘텐츠를 읽을 수 있도록 액션을 호출하기 전에 코드를 체크아웃하세요.
- 실행할 프롬프트를 결정하세요. `prompt` 입력에 인라인 텍스트를 제공하거나, `prompt-file` 입력으로 레포지토리에 커밋된 파일을 지정할 수 있습니다.

## 워크플로우 예시

아래 샘플 워크플로우는 새 Pull Request를 검토하고 Codex의 응답을 캡처한 다음 PR에 다시 게시합니다.

```yaml
name: Codex pull request review
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  codex:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      final_message: ${{ steps.run_codex.outputs.final-message }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: refs/pull/${{ github.event.pull_request.number }}/merge
          fetch-depth: 0
          persist-credentials: false

      - name: Run Codex
        id: run_codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt-file: .github/codex/prompts/review.md
          output-file: codex-output.md

  post_feedback:
    runs-on: ubuntu-latest
    needs: codex
    if: needs.codex.outputs.final_message != ''
    permissions:
      issues: write
      pull-requests: write
    steps:
      - name: Post Codex feedback
        uses: actions/github-script@v7
        with:
          github-token: ${{ github.token }}
          script: |
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.payload.pull_request.number,
              body: process.env.CODEX_FINAL_MESSAGE,
            });
        env:
          CODEX_FINAL_MESSAGE: ${{ needs.codex.outputs.final_message }}

`.github/codex/prompts/review.md` 경로를 원하는 프롬프트 파일로 바꾸거나, 인라인 텍스트를 사용하려면 `prompt` 입력을 사용하세요. 또한 이 예시에서는 나중에 검토하거나 아티팩트로 업로드할 수 있도록 최종 Codex 메시지를 `codex-output.md` 파일에 기록합니다.

## `codex exec` 구성

`codex exec` 옵션에 매핑되는 액션 입력을 설정하여 Codex 실행 방식을 세부 조정하세요:

- `prompt` 또는 `prompt-file`(하나 선택): 작업 지침을 인라인으로 입력하거나 작업이 담긴 Markdown 또는 텍스트 파일의 레포지토리 경로를 지정합니다. 프롬프트는 `.github/codex/prompts/` 디렉터리에 저장하는 것이 좋습니다.
- `codex-args`: 추가 CLI 플래그입니다. 세션, 프로필 또는 MCP 설정을 구성하려면 JSON 배열(예: `["--ephemeral"]`)이나 셸 문자열(`--profile ci`)을 제공하세요.
- `model` 및 `effort`: 원하는 Codex 에이전트 구성을 선택합니다. 기본값을 사용하려면 비워 두세요.
- `sandbox`: 실행 중 Codex에 필요한 권한에 맞게 샌드박스 모드(`workspace-write`, `read-only`, `danger-full-access`)를 선택합니다.
- `output-file`: 이후 단계에서 업로드하거나 차이를 비교할 수 있도록 최종 Codex 메시지를 디스크에 저장합니다.
- `codex-version`: 특정 CLI 릴리스를 고정합니다. 비워 두면 게시된 최신 버전을 사용합니다.
- `codex-home`: 여러 단계에서 구성 파일이나 MCP 설정을 재사용하려면 공유 Codex 홈 디렉터리를 지정합니다.

## 권한 관리

별도로 제한하지 않으면 GitHub 호스팅 러너에서 Codex에 광범위한 접근 권한이 부여됩니다. 다음 입력으로 노출 범위를 제어하세요:

- `safety-strategy`(기본값: `drop-sudo`)은 Codex 실행 전에 `sudo` 명령을 제거합니다. 이 변경은 해당 작업에서 되돌릴 수 없으며 메모리에 있는 시크릿을 보호합니다. Windows에서는 `safety-strategy: unsafe` 설정을 사용해야 합니다.
- `unprivileged-user` 설정은 특정 계정으로 Codex를 실행할 수 있도록 `safety-strategy: unprivileged-user` 설정과 `codex-user` 입력을 함께 사용합니다. 해당 사용자가 체크아웃된 레포지토리 파일을 읽고 쓸 수 있는지 확인하세요(소유권 수정 방법은 [`unprivileged-user` 예시](https://github.com/openai/codex-action/blob/main/examples/unprivileged-user.yml)에서 확인하세요).
- `read-only` 모드는 Codex가 파일을 변경하거나 네트워크를 사용하지 못하게 하지만, Codex는 여전히 상승된 권한으로 실행됩니다. 시크릿을 보호할 때 `read-only` 설정에만 의존하지 마세요.
- `sandbox` 설정은 Codex 자체에서 파일 시스템과 네트워크 접근을 제한합니다. 작업을 완료할 수 있는 범위에서 가장 제한적인 옵션을 선택하세요.
- `allow-users` 및 `allow-bots` 입력은 워크플로우를 트리거할 수 있는 계정을 제한합니다. 기본적으로 쓰기 권한이 있는 사용자만 액션을 실행할 수 있습니다. 신뢰할 수 있는 계정을 추가로 허용하려면 명시적으로 나열하고, 기본 동작을 사용하려면 필드를 비워 두세요.

## 출력 캡처

이 액션은 마지막 Codex 메시지를 `final-message` 출력으로 내보냅니다. 이를 작업 출력에 매핑하거나(위 예시 참조) 이후 단계에서 직접 처리하세요. 러너에서 전체 실행 기록을 수집하려면 `output-file` 입력과 아티팩트 업로드 기능을 함께 사용하세요. 구조화된 데이터가 필요하면 `codex-args` 입력으로 `--output-schema` 플래그를 전달하여 JSON 구조를 강제하세요.

## 보안 체크리스트

- 워크플로우를 시작할 수 있는 사용자를 제한하세요. 누구나 레포지토리를 대상으로 Codex를 실행하도록 허용하지 말고, 신뢰할 수 있는 이벤트나 명시적 승인을 사용하세요.
- 프롬프트 인젝션을 방지하려면 Pull Request, 커밋 메시지 또는 이슈 본문에서 가져온 프롬프트 입력을 정제하세요. Codex에 전달하기 전에 HTML 주석이나 숨겨진 텍스트를 검토하세요.
- `safety-strategy` 설정을 `drop-sudo` 상태로 유지하거나 Codex를 비특권 사용자로 실행하여 `OPENAI_API_KEY` 시크릿을 보호하세요. 다중 테넌트 러너에서는 절대로 액션을 `unsafe` 모드로 두지 마세요.
- 이후 단계가 예상치 못한 상태 변경을 이어받지 않도록 작업의 마지막 단계에서 Codex를 실행하세요.
- 프록시 로그나 액션 출력에 시크릿 정보가 노출되었다고 의심되면 즉시 키를 교체하세요.

## 문제 해결

- **prompt와 prompt-file을 모두 설정함**: 입력 소스를 정확히 하나만 제공하도록 중복 입력을 제거하세요.
- **responses-api-proxy가 서버 정보를 기록하지 않음**: API 키가 있고 유효한지 확인하세요. 프록시는 `openai-api-key` 입력을 제공할 때만 시작됩니다.
- **`sudo` 제거를 예상했지만 `sudo` 명령이 성공함**: `sudo` 권한을 복원한 이전 단계가 없는지, 러너 OS가 Linux 또는 macOS인지 확인하세요. 새 작업에서 다시 실행하세요.
- **`drop-sudo` 적용 후 권한 오류 발생**: 액션을 실행하기 전에 쓰기 권한을 부여하세요(예: `chmod -R g+rwX "$GITHUB_WORKSPACE"` 명령을 사용하거나 unprivileged-user 패턴을 적용).
- **권한 없는 트리거가 차단됨**: 기본값으로 허용되는 쓰기 권한 보유 공동 작업자 외에 서비스 계정도 허용하려면 `allow-users` 또는 `allow-bots` 입력을 조정하세요.

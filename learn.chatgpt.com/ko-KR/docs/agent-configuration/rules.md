<!-- source: https://learn.chatgpt.com/ko-KR/docs/agent-configuration/rules -->

규칙을 사용하여 Codex가 샌드박스 외부에서 실행할 수 있는 명령어를 제어하세요.

규칙은 실험적 기능이며 변경될 수 있습니다.

## 규칙 파일 만들기

1. 활성 구성 계층 옆의 `rules/` 폴더에 `.rules` 파일을 만드세요(예: `~/.codex/rules/default.rules`).
2. 규칙을 추가하세요. 이 예에서는 `gh pr view` 명령어의 샌드박스 외부 실행을 허용하기 전에 프롬프트를 표시합니다.

   ```python
   # Prompt before running commands with the prefix `gh pr view` outside the sandbox.
   prefix_rule(
       # The prefix to match.
       pattern = ["gh", "pr", "view"],

       # The action to take when Codex requests to run a matching command.
       decision = "prompt",

       # Optional rationale for why this rule exists.
       justification = "Viewing PRs is allowed with approval",

       # `match` and `not_match` are optional "inline unit tests" where you can
       # provide examples of commands that should (or should not) match this rule.
       match = [
           "gh pr view 7888",
           "gh pr view --repo openai/codex",
           "gh pr view 7888 --json title,body,comments",
       ],
       not_match = [
           # Does not match because the `pattern` must be an exact prefix.
           "gh pr --repo openai/codex view 7888",
       ],
   )

3. Codex를 다시 시작하세요.

Codex는 시작할 때 [팀 구성](/ko-KR/codex/enterprise/admin-setup#step-4-standardize-local-configuration-with-team-config) 위치와 경로가 `~/.codex/rules/`인 사용자 계층을 포함해 모든 활성 구성 계층 아래의 `rules/`를 스캔합니다. `<repo>/.codex/rules/` 아래의 프로젝트 로컬 규칙은 프로젝트의 `.codex/` 계층이 신뢰된 경우에만 로드됩니다.

TUI의 허용 목록에 명령어를 추가하면 Codex는 이후 실행에서 프롬프트를 건너뛸 수 있도록 사용자 계층의 `~/.codex/rules/default.rules`에 기록합니다.

스마트 승인이 활성화되어 있으면(기본값)
Codex가 권한 상향 요청 중 사용할 `prefix_rule`을 제안할 수 있습니다. 수락하기 전에
제안된 접두사를 주의 깊게 검토하세요.

관리자는
[`requirements.toml`](/ko-KR/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml)에서 제한을 적용하는 `prefix_rule` 항목을 강제할 수도 있습니다.

## 규칙 필드 이해하기

`prefix_rule()`에서 지원하는 필드는 다음과 같습니다:

- `pattern` **(필수)**: 일치시킬 명령어 접두사를 정의하는 비어 있지 않은 목록입니다. 각 요소는 다음 중 하나입니다:
  - 리터럴 문자열(예: `"pr"`).
  - 해당 인수 위치에서 여러 대안과 일치시키는 리터럴 유니온(예: `["view", "list"]`).
- `decision` **(기본값: `"allow"`)**: 규칙이 일치할 때 수행할 동작입니다. 둘 이상의 규칙이 일치하면 Codex는 가장 제한적인 결정(`forbidden` \> `prompt` \> `allow`)을 적용합니다.
  - `allow`: 프롬프트 없이 샌드박스 외부에서 명령어를 실행합니다.
  - `prompt`: 일치하는 각 호출 전에 프롬프트를 표시합니다.
  - `forbidden`: 프롬프트 없이 요청을 차단합니다.
- `justification` **(선택 사항)**: 규칙의 근거를 설명하는, 사람이 읽을 수 있는 비어 있지 않은 문자열입니다. Codex가 승인 프롬프트나 거부 메시지에 이 근거를 표시할 수 있습니다. `forbidden`을 사용할 때는 적절한 경우 근거에 권장 대안을 포함하세요(예: `"Use \`rg\` instead of \`grep\`."\`).
- `match` 및 `not_match` **(기본값: `[]`)**: Codex가 규칙을 로드할 때 검증하는 예시입니다. 규칙이 적용되기 전에 오류를 찾아내는 데 사용하세요.

Codex가 명령어 실행을 검토할 때 명령어의 인수 목록을 `pattern`과 비교합니다. 내부적으로 Codex는 명령어를 `execvp(3)`에 전달되는 것과 같은 인수 목록으로 취급합니다.

## 셸 래퍼와 복합 명령어

일부 도구는 다음과 같이 여러 셸 명령어를 하나의 호출로 래핑합니다:

```text
["bash", "-lc", "git add . && rm -rf /"]

이런 명령어는 하나의 문자열 안에 여러 작업을 숨길 수 있으므로 Codex는 `bash -lc`, `bash -c` 및 이에 대응하는 `zsh`/`sh` 명령어를 특별히 처리합니다.

### Codex가 스크립트를 안전하게 분할할 수 있는 경우

셸 스크립트가 다음과 같이 구성된 선형 명령어 체인이라면:

- 일반 단어만 사용(변수 확장 및 `VAR=...`, `$FOO`, `*` 등은 사용하지 않음)
- 안전한 연산자(`&&`, `||`, `;` 또는 `|`)로만 연결

그러면 Codex는 tree-sitter를 사용해 스크립트를 파싱하고, 규칙을 적용하기 전에 개별 명령어로 분할합니다.

위 스크립트는 두 개의 별도 명령어로 취급됩니다:

- `["git", "add", "."]`
- `["rm", "-rf", "/"]`

그런 다음 Codex는 각 명령어를 규칙과 비교해 평가하며, 가장 제한적인 결과가 우선 적용됩니다.

`pattern=["git", "add"]`에 대해 허용을 설정해도 Codex는 `git add . && rm -rf /` 명령어를 자동으로 허용하지 않습니다. `rm -rf /` 부분이 별도로 평가되어 전체 호출의 자동 허용을 막기 때문입니다.

이를 통해 안전한 명령어에 위험한 명령어를 몰래 끼워 넣는 것을 방지합니다.

### Codex가 스크립트를 분할하지 않는 경우

스크립트에서 다음과 같은 고급 셸 기능을 사용하면:

- 리디렉션(`>`, `>>`, `<`)
- 치환(`$(...)`, `...`)
- 환경 변수(`FOO=bar`)
- 와일드카드 패턴(`*`, `?`)
- 제어 플로우(`if`, `for`, 대입문과 함께 사용되는 `&&` 등)

그러면 Codex는 스크립트를 해석하거나 분할하려고 하지 않습니다.

이 경우 전체 호출은 다음과 같이 취급됩니다:

```text
["bash", "-lc", "<full script>"]

규칙은 해당 **단일** 호출에 적용됩니다.

이렇게 처리하면 안전한 경우에는 명령어별 평가로 보안을 확보하고, 안전하지 않은 경우에는 보수적으로 동작할 수 있습니다.

## 규칙 파일 테스트하기

`codex execpolicy check`를 사용하여 규칙이 명령어에 어떻게 적용되는지 테스트하세요:

```shell
codex execpolicy check --pretty \
  --rules ~/.codex/rules/default.rules \
  -- gh pr view 7888 --json title,body,comments

이 명령어는 가장 제한적인 결정과 일치하는 모든 규칙을 보여주는 JSON을 출력하며, 일치한 규칙의 `justification` 값도 포함합니다. 여러 파일을 결합하려면 `--rules` 플래그를 두 번 이상 사용하고, 출력에 서식을 적용하려면 `--pretty`를 추가하세요.

## 규칙 언어 이해하기

`.rules` 파일 형식은 `Starlark`를 사용합니다([언어 사양](https://github.com/bazelbuild/starlark/blob/master/spec.md) 참조). 문법은 Python과 비슷하지만 안전하게 실행할 수 있도록 설계되었습니다. 따라서 규칙 엔진은 파일 시스템을 건드리는 등의 사이드 이펙트 없이 이를 실행할 수 있습니다.

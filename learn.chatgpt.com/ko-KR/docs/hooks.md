<!-- source: https://learn.chatgpt.com/ko-KR/docs/hooks -->

훅은 Codex의 기능을 확장하는 프레임워크입니다. 에이전트 루프 중에 스크립트나 MCP
도구를 실행하여 다음과 같은 기능을 구현할 수 있습니다:

- 채팅을 사용자 지정 로깅/분석 엔진으로 전송
- 팀의 프롬프트를 스캔하여 실수로 API 키를 붙여넣지 못하도록 차단
- 채팅을 요약해 영구 메모리를 자동으로 생성
- 채팅 턴이 중지될 때 사용자 지정 검증을 실행하여 표준 준수 보장
- 특정 디렉터리에서 프롬프팅 사용자 지정

유의할 런타임 동작:

- 여러 파일에 있는 훅 중 조건에 일치하는 훅은 모두 실행됩니다.
- 동일한 이벤트에 일치하는 명령어 훅이 여러 개이면 동시에 시작되므로,
한 훅이 다른 일치하는 훅의 시작을 막을 수 없습니다.
- 비관리형 훅은 실행 전에 검토하고 신뢰하도록 설정해야 합니다.

훅은 대화의 여러 시점에서 실행됩니다:

| 시점                              | 훅                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 턴 진행 중                     | `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `UserPromptSubmit`, `SubagentStop`, `Stop` |
| 사용자가 진행 중인 턴을 중단할 때 | `Interrupt` (하위 에이전트에서는 실행되지 않음)                                                                                   |
| 세션 또는 하위 에이전트 시작 시 | `SessionStart`, `SubagentStart`                                                                                           |
| 메인 스레드 종료 시         | `SessionEnd` (하위 에이전트에서는 실행되지 않음)                                                                                  |

## Codex가 훅을 찾는 위치

Codex는 활성 설정 레이어가 있는 위치에서 다음 두 가지 형식으로 정의된 훅을 찾습니다:

- `hooks.json`
- `config.toml`에 포함된 인라인 `[hooks]` 테이블

설치된 플러그인은 플러그인 매니페스트 또는 기본 `hooks/hooks.json` 파일로
수명 주기 설정을 함께 제공할 수도 있습니다. 플러그인 패키징 규칙은
[플러그인
빌드](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks)를 참조하세요.

실제로 가장 유용한 위치 네 곳은 다음과 같습니다:

- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

훅 소스가 둘 이상이면 Codex는 일치하는 모든 훅을 로드합니다.
우선순위가 높은 설정 레이어가 우선순위가 낮은 레이어의 훅을 대체하지는 않습니다.
한 레이어에 `hooks.json`과 인라인 `[hooks]`가 모두 있으면 Codex는
둘을 병합하고 시작 시 경고를 표시합니다. 레이어마다 한 가지 형식만 사용하는 것이 좋습니다.

Codex는 활성화된 플러그인에 포함된 훅도 찾을 수 있습니다. 플러그인에 포함된
훅은 다른 훅 소스와 함께 로드되며, 다른 비관리형 훅과 동일한 신뢰 검토 플로우를
따릅니다.

프로젝트 로컬 훅은 프로젝트의 `.codex/` 레이어가 신뢰된 경우에만 로드됩니다.
신뢰되지 않은 프로젝트에서도 Codex는 사용자 및 시스템 훅을
각각의 활성 설정 레이어에서 계속 로드합니다.

## 훅 검토 및 신뢰 설정

Codex는 실행 가능한 훅을 결정하기 전에 설정된 훅의 목록을 표시합니다. 비관리형
훅을 실행하려면 실제로 실행할 훅의 정의를 검토하고 신뢰하도록 설정해야 합니다.
Codex는 훅의 현재 해시를 기준으로 신뢰 상태를 기록하므로, 새로 추가되거나 변경된
훅은 검토 대상으로 표시되며 신뢰하도록 설정할 때까지 실행되지 않습니다.

CLI에서 `/hooks`를 사용하면 훅 소스를 확인하고, 새 훅이나 변경된 훅을 검토하고,
훅을 신뢰하도록 설정하거나 개별 비관리형 훅을 비활성화할 수 있습니다.
시작할 때 검토가 필요한 훅이 있으면 Codex는 `/hooks`를 열라는 경고를 출력합니다.

시스템, MDM, 클라우드 또는 `requirements.toml` 소스의 관리형 훅은 관리형으로 표시되고
정책에 따라 신뢰된 것으로 처리되며, 사용자 훅 브라우저에서는 비활성화할 수 없습니다.

Codex 외부에서 이미 훅 소스를 검증하는 일회성 자동화에서는
`--dangerously-bypass-hook-trust`를 전달하세요. 해당 호출에서는 저장된 훅 신뢰 상태가 없어도
활성화된 훅을 실행할 수 있습니다.

## 설정 구조

훅은 세 계층으로 구성됩니다:

- `PreToolUse`, `PostToolUse`, `PreCompact`,
`SubagentStart` 또는 `Stop` 등의 훅 이벤트
- 해당 이벤트의 일치 조건을 정하는 매처 그룹
- 매처 그룹의 조건이 일치할 때 실행되는 하나 이상의 훅 핸들러

```json
{
  "description": "Optional lifecycle hooks for this workspace.",
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_start.py",
            "statusMessage": "Loading session notes",
            "additionalContextLimit": 5000
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_end.py",
            "timeout": 3
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py\"",
            "statusMessage": "Checking Bash command"
          }
        ]
      }
    ],
    "PermissionRequest": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/permission_request.py\"",
            "statusMessage": "Checking approval request"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py\"",
            "statusMessage": "Reviewing Bash output"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/user_prompt_submit_data_flywheel.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/stop_continue.py\"",
            "timeout": 30
          }
        ]
      }
    ]
  }
}

참고:

- `description` 필드는 `hooks.json` 파일의 선택적 최상위 메타데이터입니다.
  어떤 훅이 실행되는지에는 영향을 주지 않습니다.
- `timeout`의 단위는 초입니다.
- `timeout`을 생략하면 Codex는 대부분의 훅에 `600`초를 사용합니다.
  - `SessionEnd` 및 `Interrupt`의 기본 시간 제한은 `1`초이며 최대 `3`초까지 지원합니다.
- `statusMessage` 필드는 선택 사항입니다.
- `additionalContextLimit` 설정은 명령어 훅이 모델에 보낼 수 있는 `additionalContext`의 양을 정합니다.
  이 한도를 넘으면 Codex는 전체 텍스트를 디스크에 저장하고 대신 더 짧은 미리 보기를 보냅니다.
  [대용량 훅 출력](#large-hook-output)을 참조하세요.
- `commandWindows` 필드는 Windows에서만 사용할 대체 명령어를 지정하는 선택 항목입니다.
TOML에서는 `command_windows` 또는 `commandWindows`를 사용하세요.
- 명령어 훅을 [백그라운드에서
  실행](#run-hooks-in-the-background)하려면 `async`를 `true`로 설정하세요.
- `command` 및 `mcp_tool` 핸들러를 지원합니다. `prompt` 및 `agent` 핸들러는
  파싱되지만 실행은 건너뜁니다.
- 명령은 세션의 `cwd`를 작업 디렉터리로 사용해 실행됩니다.
- 레포지토리 로컬 훅은 `.codex/hooks/...` 같은 상대 경로를 사용하기보다
  git 루트를 기준으로 경로를 해석하는 것이 좋습니다. Codex는 하위 디렉터리에서 시작될 수 있으며,
  git 루트 기준 경로를 사용하면 훅 위치가 일정하게 유지됩니다.

`config.toml`에 작성한 동일한 설정의 인라인 TOML:

```toml
[[hooks.SessionStart]]
matcher = "^compact$"

[[hooks.SessionStart.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/session_start.py"'
additionalContextLimit = 5000

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"

[[hooks.PostToolUse]]
matcher = "^Bash$"

[[hooks.PostToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py"'
timeout = 30
statusMessage = "Reviewing Bash output"

## MCP 도구 훅

MCP 도구 훅을 사용하면 수명 주기 이벤트에서 이미 연결된 MCP 서버의 도구를 호출할 수 있습니다.
구조화된 인수를 도구에 직접 전달하며, 명령어 훅과 동일한
신뢰 검토 절차와 출력 규약을 따릅니다.

### MCP 도구 훅 설정

이 훅은 Codex가 파일을 작성하거나 수정한 뒤 `scanner` MCP 서버에
각 패치를 스캔하도록 요청합니다:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "mcp_tool",
            "server": "scanner",
            "tool": "scan_patch",
            "input": { "patch": "${tool_input.command}" },
            "timeout": 30,
            "statusMessage": "Scanning edited files"
          }
        ]
      }
    ]
  }
}

| 필드           | 의미                                                          |
| --------------- | ---------------------------------------------------------------- |
| `type`          | `mcp_tool`이어야 합니다.                                              |
| `server`        | 이미 연결된 MCP 서버의 이름이며, 필수 항목입니다.                |
| `tool`          | 해당 서버가 제공하는 도구의 이름이며, 필수 항목입니다.                  |
| `input`         | 인수 템플릿을 담은 JSON 객체로, 선택 항목입니다. 기본값은 `{}`입니다.    |
| `timeout`       | 실제 실행에 적용되는 제한 시간(초)입니다. 선택 사항이며 기본값은 `600`입니다. |
| `statusMessage` | 훅이 실행되는 동안 표시할 메시지입니다. 선택 사항입니다.                      |

### 훅 이벤트 값으로 인수 확장

훅 이벤트의 필드를 점 표기법으로 읽을 때는 `${field.nested}` 형식을 사용하세요. 값 전체를 차지하는 플레이스홀더는
JSON 타입을 유지합니다. 문자열의 일부로 포함된 플레이스홀더는 텍스트로 변환됩니다.
Codex는 객체와 배열을 재귀적으로 확장합니다.

이벤트에 포함된 내용이 `{"tool_input":{"file_path":"src/main.rs","count":3}}`인 경우,
다음 인수 템플릿은:

```json
{
  "path": "${tool_input.file_path}",
  "count": "${tool_input.count}",
  "message": "Scanning ${tool_input.file_path}"
}

다음과 같이 변환됩니다:

```json
{
  "path": "src/main.rs",
  "count": 3,
  "message": "Scanning src/main.rs"
}

### 실행 및 수명 주기

- 훅은 기존 MCP 연결을 사용합니다. 서버를 시작하거나 다시 연결하지 않습니다.
- 도구가 차단 결정을 반환하면 훅이 작업을 차단할 수 있습니다.
오류가 발생하거나 서버가 없거나 도구를 사용할 수 없는 경우에는 작업을 차단하지 않습니다.
- MCP 도구 훅은 동기적으로 실행됩니다. 도구 승인을 요청하거나
다른 훅을 트리거하지 않습니다.
- 훅과 서버의 제한 시간 중 더 짧은 시간이 적용됩니다. MCP 유도에 대한
응답을 기다리는 시간은 제한 시간에 포함되지 않습니다.
- `SessionStart` 훅은 MCP 서버가 준비되기 전에 실행될 수 있습니다.
  이 경우 세션을 차단하지 않습니다.
- `SessionEnd`는 MCP 도구 훅을 지원하지 않습니다.

## 훅 끄기

훅은 기본적으로 활성화되어 있습니다. `config.toml`에서 훅을 끄려면 다음과 같이 설정하세요:

```toml
[features]
hooks = false

정식 기능 키로 `hooks`를 사용하세요. `codex_hooks`는 사용 중단 예정(deprecated)인 별칭으로
계속 사용할 수 있습니다. 관리자는 `requirements.toml`에서도 같은 방식으로
`[features].hooks = false`를 설정해 훅을 강제로 끌 수 있습니다.

## `requirements.toml`의 관리형 훅

엔터프라이즈에서 관리하는 요구 사항에서도 `[hooks]` 아래에 훅을 인라인으로 정의할 수 있습니다.
이는 관리자가 MDM이나 다른 기기 관리 시스템으로 실제 스크립트를 배포하면서
훅 구성을 강제로 적용하려는 경우에 유용합니다.
로컬에서 훅을 비활성화한 사용자에게도 관리형 훅을 강제로 적용하려면
`requirements.toml`에서 `[hooks]`와 함께 `[features].hooks = true` 설정을 고정하세요. 사용자, 프로젝트, 세션 및
플러그인 훅은 무시하되 관리자의 관리형 훅은 계속 허용하려면
`allow_managed_hooks_only = true`를 설정하세요.

```toml
allow_managed_hooks_only = true

[features]
hooks = true

[hooks]
managed_dir = "/enterprise/hooks"
windows_managed_dir = 'C:\enterprise\hooks'

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
command_windows = 'py -3 C:\enterprise\hooks\pre_tool_use_policy.py'
timeout = 30
statusMessage = "Checking managed Bash command"

관리형 훅 참고 사항:

- macOS와 Linux에서는 `managed_dir` 설정을 사용합니다.
- Windows에서는 `windows_managed_dir` 설정을 사용합니다.
- Codex는 `managed_dir`의 스크립트를 배포하지 않습니다.
  엔터프라이즈 도구로 스크립트를 별도로 설치하고 업데이트해야 합니다.
- 관리형 훅 명령어에는 설정된 관리형 디렉터리 아래에 있는
스크립트의 절대 경로를 사용하세요.
- `allow_managed_hooks_only = true`를 설정하면 사용자, 프로젝트, 세션 및
  플러그인 소스의 훅은 건너뛰지만, `requirements.toml` 및
  다른 관리형 구성 계층의 관리형 훅은 계속 로드합니다.

## 플러그인에 포함된 훅

플러그인이 활성화되면 Codex는 해당 플러그인의 수명 주기 훅을
사용자 훅, 프로젝트 훅 및 관리형 훅과 함께 로드할 수 있습니다.

기본적으로 Codex는 플러그인 루트에서 `hooks/hooks.json` 파일을 찾습니다.
플러그인 매니페스트 파일인 `.codex-plugin/plugin.json`에 `hooks` 항목을 지정하면
이 기본값을 재정의할 수 있습니다. 매니페스트 항목에는 `./`로 시작하는 경로,
`./`로 시작하는 경로의 배열, 인라인 훅 객체 또는
인라인 훅 객체의 배열을 사용할 수 있습니다.

```json
{
  "name": "repo-policy",
  "hooks": "./hooks/hooks.json"
}

매니페스트의 훅 경로는 플러그인 루트를 기준으로 해석되며
해당 루트 내부에 있어야 합니다. 매니페스트에 `hooks` 항목이 정의되어 있으면
Codex는 기본 `hooks/hooks.json` 파일 대신 해당 매니페스트 항목을 사용합니다.

플러그인 훅 명령어에는 다음 환경 변수가 전달됩니다:

- `PLUGIN_ROOT`는 Codex 전용 확장 변수로,
  설치된 플러그인의 루트를 가리킵니다.
- `PLUGIN_DATA`는 Codex 전용 확장 변수로,
  플러그인의 쓰기 가능한 데이터 디렉터리를 가리킵니다.
- Codex는 기존 플러그인 훅과의 호환성을 위해
  `CLAUDE_PLUGIN_ROOT`와 `CLAUDE_PLUGIN_DATA`도 설정합니다.

플러그인 훅은 다른 훅과 동일한 이벤트 스키마를 사용합니다. 플러그인을 설치하거나
활성화해도 해당 훅이 자동으로 신뢰되지는 않습니다. 사용자가 현재 훅 정의를 검토하고
신뢰하기 전까지 Codex는 플러그인에 포함된 훅을 건너뜁니다.

## 매처 패턴

`matcher` 필드는 훅이 실행될 조건을 필터링하는 정규식 문자열입니다.
지원되는 이벤트가 발생할 때마다 매칭하려면 `"*"` 또는 `""` 값을 사용하거나
`matcher` 필드를 아예 생략하세요.

현재 Codex 이벤트 중 일부에만 `matcher`가 적용됩니다:

| 이벤트               | `matcher`의 필터링 대상 | 참고                                                        |
| ------------------- | ---------------------- | ------------------------------------------------------------ |
| `PermissionRequest` | 도구 이름              | 지원 대상에는 `Bash`, `apply_patch`\*, MCP 도구 이름이 포함됩니다 |
| `PostToolUse`       | 도구 이름              | [도구 적용 범위](#tool-coverage)를 참조하세요                          |
| `PostCompact`       | 컨텍스트 압축 트리거     | 값은 `manual` 또는 `auto`입니다                                |
| `PreCompact`        | 컨텍스트 압축 트리거     | 값은 `manual` 또는 `auto`입니다                                |
| `PreToolUse`        | 도구 이름              | [도구 적용 범위](#tool-coverage)를 참조하세요                          |
| `SessionEnd`        | 종료 사유             | 현재는 `other`만 사용됩니다                                       |
| `SessionStart`      | 시작 방식           | 값은 `startup`, `resume`, `clear`, `compact`입니다       |
| `SubagentStart`     | 하위 에이전트 유형          | 시작되는 하위 에이전트에 따라 값이 달라집니다                    |
| `SubagentStop`      | 하위 에이전트 유형          | 중지되는 하위 에이전트에 따라 값이 달라집니다                     |
| `UserPromptSubmit`  | 지원되지 않음          | 이 이벤트에서는 모든 `matcher` 설정이 무시됩니다           |
| `Stop`              | 지원되지 않음          | 이 이벤트에서는 모든 `matcher` 설정이 무시됩니다           |
| `Interrupt`         | 지원되지 않음          | 이 이벤트에서는 모든 `matcher` 설정이 무시됩니다           |

\*`apply_patch`의 경우 `matcher` 값으로 `Edit` 또는 `Write`도 사용할 수 있습니다.

예:

- `Bash`
- `^apply_patch$`
- `Edit|Write`
- `mcp__filesystem__read_file`
- `mcp__filesystem__.*`
- `startup|resume|clear|compact`
- `manual|auto`

### 도구 지원 범위

`PreToolUse`와 `PostToolUse`는 셸 및 MCP 호출 외의 도구 호출도 관찰할 수 있습니다. 대부분의
로컬 함수 도구는 같은 훅 경로를 사용하므로 도구 이름으로 매칭하고
JSON 인수를 검사할 수 있으며, `PreToolUse`에서는 호출을 차단하거나 수정할 수도 있습니다.

| 도구 경로                         | `PreToolUse` | `PostToolUse` | 참고 사항                                                                                                                    |
| --------------------------------- | ------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 셸 명령어                    | 예          | 예           | `Bash`로 매칭합니다.                                                                                                         |
| 통합 실행(`exec_command`)     | 예          | 예           | `Bash`로 매칭합니다. 이후 `write_stdin`로 폴링할 때 원래 명령어가 완료되면 해당 명령어의 `PostToolUse`를 전달할 수 있습니다. |
| `apply_patch`                     | 예          | 예           | `apply_patch`, `Edit` 또는 `Write`로 매칭합니다.                                                                              |
| MCP 도구                         | 예          | 예           | `mcp__filesystem__read_file` 같은 MCP 도구 이름으로 매칭합니다.                                                           |
| 기타 로컬 함수 도구        | 예          | 예           | `update_plan` 같은 함수 도구 이름으로 매칭합니다. `spawn_agent`는 `Agent`로도 매칭됩니다.                                 |
| `WebSearch` 같은 호스팅 도구 | 아니요           | 아니요            | 이 도구들은 로컬 함수 도구의 훅 경로를 사용하지 않습니다.                                                                       |

`write_stdin`은 기존 통합 실행 세션에서 데이터를 전달하는 수단입니다.
입력을 보내거나 이미 `PreToolUse`를 거친 명령어를 폴링할 때
`PreToolUse`를 다시 실행하지 않습니다.

일부 특수 도구 경로는 기본 훅 경로를 사용하지 않도록 선택할 수 있습니다. 도구
훅은 유용한 안전장치로 활용하되, 완전한 통제 수단으로 간주하지 마세요.

## 공통 입력 필드

모든 명령어 훅은 `stdin`으로 JSON 객체 하나를 받습니다.

일반적으로 사용하는 공통 필드는 다음과 같습니다:

| 필드             | 유형             | 의미                                                             |
| ----------------- | ---------------- | ------------------------------------------------------------------- |
| `session_id`      | `string`         | 현재 Codex 세션 ID입니다. 하위 에이전트 훅은 상위 세션 ID를 사용합니다. |
| `transcript_path` | `string \| null` | 세션 대화 기록 파일의 경로(파일이 있는 경우)                         |
| `cwd`             | `string`         | 세션의 작업 디렉터리                                   |
| `hook_event_name` | `string`         | 현재 훅 이벤트 이름                                             |
| `model`           | `string`         | Codex 전용 확장 필드. 활성 모델의 슬러그                         |

턴 단위 훅의 이벤트별 표에는 `turn_id`가
Codex 전용 확장 필드로 나열되어 있습니다.

`SessionStart`, `PreToolUse`, `PermissionRequest`, `PostToolUse`,
`UserPromptSubmit`, `SubagentStart`, `SubagentStop`, `Stop`, `Interrupt`에는
`permission_mode`도 포함됩니다. 이 필드는 현재 권한 모드를 `default`,
`acceptEdits`, `plan`, `dontAsk` 또는 `bypassPermissions`로 나타냅니다.

`transcript_path`는 편의상 채팅 대화 기록을 가리키지만,
대화 기록 형식은 훅을 위한 고정된 인터페이스가 아니며 향후 변경될 수 있습니다.

전체 전송 형식이 필요하면 [스키마](#schemas)를 참조하세요.

## 공통 출력 필드

`SessionStart`, `PreCompact`, `PostCompact`, `UserPromptSubmit`,
`SubagentStop`, `Stop`은 다음 공통 JSON 필드를 지원합니다. `SubagentStart`에서는
`systemMessage` 및 훅별 컨텍스트에 같은 형식을 사용할 수 있지만,
`continue: false`로는 하위 에이전트가 중지되지 않습니다:

```json
{
  "continue": true,
  "stopReason": "optional",
  "systemMessage": "optional",
  "suppressOutput": false
}

| 필드            | 동작                                          |
| ---------------- | ----------------------------------------------- |
| `continue`       | `false`이면 해당 훅 실행을 중지된 상태로 표시      |
| `stopReason`     | 중지 사유로 기록됨             |
| `systemMessage`  | UI 또는 이벤트 스트림에 경고로 표시됨 |
| `suppressOutput` | 현재 파싱되지만 아직 동작은 구현되지 않음            |

출력 없이 종료 코드 `0`으로 종료하면 성공으로 처리되며 Codex는 계속 진행합니다.

`PreToolUse`와 `PermissionRequest`는 `systemMessage`를 지원하지만, `continue`,
`stopReason`, `suppressOutput`은 현재 해당 이벤트에서 지원되지 않습니다.
`PreToolUse` 훅이 지원되지 않는 필드 중 하나를 반환하면 Codex는
해당 훅 실행을 실패로 표시하고 오류를 보고한 뒤 도구 호출을 계속 진행합니다.

`PostToolUse`는 `systemMessage`, `continue: false`, `stopReason`을 지원합니다.
`suppressOutput`은 파싱되지만 현재 해당 이벤트에서는 지원되지 않습니다.

### 대용량 훅 출력

기본적으로 Codex는 모델에 전달되는 각 훅 출력 메시지를 약
2,500토큰으로 제한합니다. 훅이 이보다 많은 출력을 반환하면 전체 텍스트를
`<temp_dir>/hook_outputs/<session_id>/<uuid>.txt`에 저장하고, 저장된 파일 경로와 함께 텍스트의 앞부분과 뒷부분을 담은
미리보기를 모델에 제공합니다. 이 동작을
**스필링이라고** 합니다. Codex는 크기가 너무 큰 출력을 디스크에 저장하고
모델에 전달할 짧은 미리보기로 대체합니다. 파일을 쓸 수 없더라도 모델에는
잘린 미리보기가 제공됩니다.

  훅과 플러그인의 컨텍스트는 간결하게 유지하세요. 여러 훅과 플러그인의 컨텍스트가
  쌓이면 모델 성능이 저하될 수 있습니다. `additionalContextLimit` 값을 높이면
  그 위험이 커집니다. 훅 자체에서 출력량을 엄격히 제한하지 않는 한
  한도를 `0`으로 설정하지 마세요. 그렇지 않으면 훅 하나가
  컨텍스트 윈도우 전체를 차지할 수 있습니다.

`additionalContext`를 반환하는 명령어 훅에서는 핸들러의
`additionalContextLimit` 값을 설정해 대략적인 토큰
임곗값을 조정하세요:

```json
{
  "type": "command",
  "command": "python3 ~/.codex/hooks/session_start.py",
  "additionalContextLimit": 5000
}

`additionalContextLimit`을 생략하면 기본 임곗값인 `2500`토큰을 사용합니다.
다른 임곗값을 지정하려면 양의 정수를 사용하세요. `0`을 사용하면 핸들러의
추가 컨텍스트 전체를 모델에 직접 전달합니다. Codex는
매칭되는 핸들러를 각각 독립적으로 평가합니다. 추가 컨텍스트를 생성할 수 없는
이벤트에서는 `additionalContextLimit` 값을 무시하고
구성 경고를 보고합니다.

이 설정은 `additionalContext`에만 적용됩니다. 도구 피드백과
이어가기 프롬프트에는 기본 한도가 계속 적용됩니다.

크기가 너무 큰 출력은 디스크에 기록될 수 있으므로 훅 출력에 비밀 정보나
기타 민감한 데이터를 포함하지 마세요.

## 백그라운드에서 훅 실행

기본적으로 Codex는 명령어 훅이 끝날 때까지 기다린 후
해당 훅을 트리거한 작업을 계속합니다. `async`를 `true`로 설정하면
Codex가 작업을 계속하는 동안 명령어 훅을 백그라운드에서 실행할 수 있습니다.

### 백그라운드 훅 설정

`hooks.json`의 명령어 핸들러에 `"async": true`를 추가하세요:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/post_tool_use.py",
            "async": true,
            "timeout": 120
          }
        ]
      }
    ]
  }
}

`config.toml`의 인라인 훅에서는 `async = true`로 설정하세요:

```toml
[[hooks.PostToolUse]]
matcher = "Bash"

[[hooks.PostToolUse.hooks]]
type = "command"
command = "python3 ~/.codex/hooks/post_tool_use.py"
async = true
timeout = 120

백그라운드 훅의 입력, 매처, 신뢰 검토, 시간 제한 및
[대용량 출력 처리](#large-hook-output) 방식은 동기식 명령어 훅과 동일합니다.
다른 명령어 훅과 마찬가지로 `timeout`은 초 단위이며 기본값은
`600`입니다. `Interrupt` 훅의 시간 제한은 기본 1초, 최대 3초이며,
백그라운드에서 실행할 때도 동일합니다.

### 백그라운드 훅의 실행 방식

백그라운드 훅이 완료되면 Codex는 대화 중 다음 안전한 시점에
지원되는 정보성 출력을 전달합니다:

- 진행 중인 턴이 있으면 Codex는 현재 모델 요청과 도구 호출이
완료될 때까지 기다린 다음, 해당 턴의 다음 모델 요청에서
출력을 사용할 수 있도록 합니다.
- 진행 중인 턴이 없으면 Codex는 다음 사용자 턴까지 기다립니다.
백그라운드 훅이 완료되어도 새 턴이 시작되지는 않습니다.

동기식 훅과 동일한 이벤트별 JSON 출력을 사용하세요.
Codex는 `additionalContext`를 모델의 컨텍스트에 추가하고
`systemMessage`를 경고로 표시합니다.

  백그라운드 훅은 자신을 트리거한 작업을 차단, 승인, 수정하거나
다른 방식으로 제어할 수 없습니다. 도구 정책, 권한 결정,
프롬프트 거부 또는 턴 계속 진행에는 동기식 훅을 사용하세요.

### 제한 사항

- Codex는 세션당 최대 8개의 백그라운드 훅을 동시에 실행합니다.
추가 훅은 실행 중인 훅이 완료될 때까지 기다립니다.
- 일치하는 각 호출은 독립적으로 실행되며, 백그라운드 훅은
시작 순서와 다른 순서로 완료될 수 있습니다.
- 세션이 끝나면 Codex는 완료되지 않은 백그라운드 훅을 취소하고
아직 전달되지 않은 출력을 폐기합니다.
- `SessionEnd` 훅은 항상 동기식으로 실행됩니다.

## 훅

### SessionStart

이 이벤트에서 `matcher`는 `source`에 적용됩니다.

다음은 [공통 입력 필드](#common-input-fields)에 추가되는 필드입니다:

| 필드    | 유형     | 의미                                                             |
| -------- | -------- | ------------------------------------------------------------------- |
| `source` | `string` | 세션 시작 방식: `startup`, `resume`, `clear` 또는 `compact` |

`stdout`으로 출력한 일반 텍스트는 추가 개발자 컨텍스트로 제공됩니다.

`stdout`의 JSON 출력은 [공통 출력 필드](#common-output-fields)와
다음과 같은 훅 전용 형식을 지원합니다:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "Load the workspace conventions before editing."
  }
}

해당 `additionalContext` 텍스트는 추가 개발자 컨텍스트로 제공됩니다.

Codex가 루트 세션의 컨텍스트를 압축하면, `source: "compact"` 조건과 일치하는
`SessionStart` 훅이 다음 모델 요청 전에 실행됩니다.
턴 도중에 자동 컨텍스트 압축이 발생할 때도 마찬가지입니다. Codex는
이후 사용자 턴까지 기다리지 않고 곧바로 이어지는 실행에
훅의 추가 컨텍스트를 전달합니다. 훅이 `continue: false`를 반환하면
Codex는 모델 요청을 추가로 보내지 않고 턴을 종료합니다.

### SessionEnd

`SessionEnd` 훅을 사용하면 세션이 끝날 때 최종 메모를 저장하거나 파일을 정리하는 등의
명령어를 실행할 수 있습니다. 아직 열려 있는 대화를 보관하거나 삭제할 때,
Codex가 정상적으로 종료될 때, 또는 대화가 유휴 상태이며
연결된 어느 클라이언트에도 열려 있지 않은 상태로 30분이 지났을 때 메인 스레드에서 실행됩니다.
하위 에이전트에서는 실행되지 않습니다.

대화를 벗어나거나 `thread/unsubscribe`를 호출해도 세션이 즉시
종료되지는 않으므로 `SessionEnd` 훅이 바로 실행되지 않습니다.
훅은 실행되는 동안에도 세션 대화 기록을 읽을 수 있습니다.

이 이벤트에서 `matcher`는 `reason` 값을 기준으로 필터링합니다. 현재 `reason` 값은 항상 `other`입니다.
`matcher`를 생략하거나 값으로 `other`를 사용하면 모든 `SessionEnd` 이벤트에서 실행됩니다.

다음은 [공통 입력 필드](#common-input-fields)에 추가되는 필드입니다:

| 필드    | 유형     | 의미                        |
| -------- | -------- | ------------------------------ |
| `reason` | `string` | 세션 종료 사유: `other` |

예를 들어 `SessionEnd` 명령어는 다음 입력을 받습니다:

```json
{
  "session_id": "thr_123",
  "transcript_path": "/workspace/.codex/rollout.jsonl",
  "cwd": "/workspace",
  "hook_event_name": "SessionEnd",
  "reason": "other"
}

`SessionEnd` 훅은 `async` 값이 `true`인 경우에도 항상 동기식으로 실행됩니다.
이 훅은 참고용이므로 출력이 Codex의 동작을 바꾸거나 스레드를 열린 상태로 유지하지 않습니다.
명령어가 시간 초과되거나 오류로 종료되면 Codex는 이를 훅 실패로 보고합니다.

### SubagentStart

이 이벤트에서 `matcher`는 `agent_type`에 적용됩니다.

다음은 [공통 입력 필드](#common-input-fields)에 추가되는 필드입니다:

| 필드             | 유형     | 의미                                        |
| ----------------- | -------- | ---------------------------------------------- |
| `turn_id`         | `string` | Codex 전용 확장 필드. 현재 활성 Codex 턴 ID |
| `agent_id`        | `string` | 하위 에이전트 식별자                    |
| `agent_type`      | `string` | 하위 에이전트 유형 또는 프로필                       |
| `permission_mode` | `string` | 현재 권한 모드                        |

`stdout`으로 출력한 일반 텍스트는 하위 에이전트에 추가 개발자 컨텍스트로 제공됩니다.

`stdout`의 JSON 출력은 `systemMessage`와 다음과 같은 훅 전용 형식을 지원합니다:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SubagentStart",
    "additionalContext": "Review the repository test conventions first."
  }
}

해당 `additionalContext` 텍스트는 하위 에이전트에 추가 개발자 컨텍스트로
제공됩니다. `continue: false`는 호환성을 위해 파싱되지만,
하위 에이전트의 시작을 막지는 않습니다.

### PreToolUse

`PreToolUse` 훅은 Bash, `apply_patch`를 통한 파일 편집,
MCP 도구 호출 및 기타 로컬 함수 도구를 가로챌 수 있습니다. 지원되는 경로와 예외는 [도구
적용 범위](#tool-coverage)를 참조하세요.

`matcher`는 `tool_name`과 매처 별칭에 적용됩니다.
`apply_patch`를 통한 파일 편집에서는 `matcher` 값으로 `apply_patch`, `Edit` 또는 `Write`를 사용할 수 있습니다.
훅 입력에 포함되는 값은 여전히 `tool_name: "apply_patch"`입니다.

다음은 [공통 입력 필드](#common-input-fields)에 추가되는 필드입니다:

| 필드         | 유형         | 의미                                                                                                                          |
| ------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `turn_id`     | `string`     | Codex 전용 확장 필드. 현재 활성 Codex 턴 ID                                                                                   |
| `tool_name`   | `string`     | 표준 훅 도구 이름(예: `Bash`, `apply_patch` 또는 `mcp__fs__read` 같은 MCP 이름)                                     |
| `tool_use_id` | `string`     | 이 호출의 도구 호출 ID                                                                                                 |
| `tool_input`  | `JSON value` | 도구별 입력입니다. `Bash`와 `apply_patch`는 `tool_input.command`를 사용합니다. MCP 및 기타 로컬 함수 도구는 각자의 인수를 전송합니다. |

`stdout`으로 출력한 일반 텍스트는 무시됩니다.

`stdout`으로 출력하는 JSON에는 `systemMessage`를 사용할 수 있습니다. 지원되는 도구 호출을 거부하려면
다음 훅 전용 구조를 반환하세요:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command blocked by hook."
  }
}

Codex는 다음과 같은 이전 차단 형식도 허용합니다:

```json
{
  "decision": "block",
  "reason": "Destructive command blocked by hook."
}

종료 코드를 `2`로 설정하고 차단 사유를 `stderr`에 쓸 수도 있습니다.

차단하지 않고 모델에 전달할 컨텍스트를 추가하려면
`hookSpecificOutput.additionalContext`를 반환하세요:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "additionalContext": "The pending command touches generated files."
  }
}

지원되는 도구 호출을 차단하지 않고 수정하려면
`permissionDecision: "allow"`와 함께 `updatedInput`을 반환하세요:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "updatedInput": {
      "command": "echo rewritten"
    }
  }
}

Bash 명령어와 `apply_patch`에서는 `updatedInput`에 문자열 타입의
`command` 필드를 포함해야 합니다. MCP 및 기타 로컬 함수 도구에서 `updatedInput`은
기존 인수를 대체하는 객체입니다. `updatedInput`은 반드시
`permissionDecision: "allow"`와 함께 반환하세요. 그 외의 `updatedInput` 형식은
오류로 보고됩니다.

`permissionDecision: "ask"`, 기존 형식인 `decision: "approve"`, `continue: false`,
`stopReason`, `suppressOutput` 모두 파싱되지만 아직 지원되지 않습니다. Codex는
훅 실행을 실패로 표시하고 오류를 보고한 뒤 도구 호출을 계속합니다.

### PermissionRequest

`PermissionRequest` 훅은 Codex가 승인을 요청하기 직전에 실행됩니다.
셸 권한 상승이나 관리형 네트워크 승인이 그 예입니다. 요청을 허용하거나 거부할 수도 있고,
결정을 내리지 않고 일반 승인 프롬프트가 계속 진행되도록 할 수도 있습니다.
승인이 필요 없는 명령어에는 실행되지 않습니다.

`matcher`는 `tool_name` 및 매처 별칭에 적용됩니다. 현재 표준 값에는
`Bash`, `apply_patch` 및
`mcp__server__tool` 같은 MCP 도구 이름이 포함됩니다. `apply_patch`는 `Edit` 및 `Write`와도 일치합니다.

[공통 입력 필드](#common-input-fields) 외에 다음 필드가 제공됩니다:

| 필드                    | 유형             | 의미                                                                                                        |
| ------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------- |
| `turn_id`                | `string`         | Codex 전용 확장 필드. 활성 Codex 턴 ID                                                                 |
| `tool_name`              | `string`         | 훅의 표준 도구 이름. 예: `Bash`, `apply_patch` 또는 `mcp__fs__read` 같은 MCP 이름                   |
| `tool_input`             | `JSON value`     | 도구별 입력입니다. `Bash`와 `apply_patch`는 `tool_input.command`를 사용하며, MCP 도구는 모든 인수를 전송합니다. |
| `tool_input.description` | `string \| null` | 사람이 읽을 수 있는 승인 사유(Codex가 제공하는 경우)                                                             |

`stdout`으로 출력한 일반 텍스트는 무시됩니다.

일부 도구 입력에는 사람이 읽을 수 있는 설명이 포함될 수 있지만,
모든 도구에 `tool_input.description` 필드가 있다고 가정해서는 안 됩니다.

요청을 승인하려면 다음을 반환하세요:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow"
    }
  }
}

요청을 거부하려면 다음을 반환하세요:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "deny",
      "message": "Blocked by repository policy."
    }
  }
}

일치하는 여러 훅이 결정을 반환할 때는 `deny`가 하나라도 있으면 우선 적용됩니다.
그렇지 않고 `allow`가 있으면 승인 프롬프트를 표시하지 않고 요청을 진행합니다.
일치하는 훅 중 어느 것도 결정을 내리지 않으면 Codex는 일반 승인 플로우를 사용합니다.

`PermissionRequest`에서는 `updatedInput`, `updatedPermissions`, `interrupt` 필드를 반환하지 마세요.
이 필드는 향후 동작을 위해 예약되어 있으며, 현재는 사용 시
요청이 차단됩니다.

### PostToolUse

`PostToolUse` 훅은 Bash,
`apply_patch`, MCP 도구 호출, 기타 로컬 함수 도구 등 지원되는 도구가 출력을 생성한 후 실행됩니다.
Bash의 경우 0이 아닌 상태 코드로 종료된 명령어 뒤에도 실행됩니다. 이미 실행된 도구의
사이드 이펙트는 되돌릴 수 없습니다. 지원되는 경로와 예외는 [도구 지원 범위](#tool-coverage)를
참고하세요.

`matcher`는 `tool_name` 및 매처 별칭에 적용됩니다.
`apply_patch`로 파일을 편집할 때는 `matcher` 값으로 `apply_patch`, `Edit`, `Write`를 사용할 수 있습니다.
훅 입력에는 여전히 `tool_name: "apply_patch"`가 전달됩니다.

[공통 입력 필드](#common-input-fields) 외에 다음 필드가 제공됩니다:

| 필드           | 유형         | 의미                                                                                                                          |
| --------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `turn_id`       | `string`     | Codex 전용 확장 필드. 활성 Codex 턴 ID                                                                                   |
| `tool_name`     | `string`     | 훅의 표준 도구 이름. 예: `Bash`, `apply_patch` 또는 `mcp__fs__read` 같은 MCP 이름                                     |
| `tool_use_id`   | `string`     | 이번 호출의 도구 호출 ID                                                                                                 |
| `tool_input`    | `JSON value` | 도구별 입력입니다. `Bash`와 `apply_patch`는 `tool_input.command`를 사용합니다. MCP 및 기타 로컬 함수 도구는 각 도구의 인수를 전송합니다. |
| `tool_response` | `JSON value` | 도구별 출력입니다. MCP 도구는 MCP 호출 결과를 전송합니다. 기타 로컬 함수 도구는 일반적으로 모델에 전달하는 출력을 전송합니다.    |

`stdout`으로 출력한 일반 텍스트는 무시됩니다.

`stdout`으로 출력하는 JSON에는 `systemMessage`와 다음 훅 전용 구조를 사용할 수 있습니다:

```json
{
  "decision": "block",
  "reason": "The Bash output needs review before continuing.",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "The command updated generated files."
  }
}

해당 `additionalContext` 텍스트는 개발자 컨텍스트에 추가됩니다.

이 이벤트에서 `decision: "block"`은 이미 완료된 Bash 명령어를 되돌리지 않습니다.
대신 Codex는 피드백을 기록하고 도구 결과를 해당 피드백으로 교체한 뒤,
훅이 제공한 메시지를 바탕으로 모델 실행을 계속합니다.

종료 코드를 `2`로 설정하고 피드백 사유를 `stderr`에 쓸 수도 있습니다.

명령어가 이미 실행된 후 원래 도구 결과에 대한 일반 처리를 중단하려면
`continue: false`를 반환하세요. Codex는 도구 결과를 제공한 피드백이나 중단 메시지로
교체한 뒤 이를 바탕으로 계속 진행합니다.

`updatedMCPToolOutput`과 `suppressOutput` 모두 파싱되지만 아직 지원되지 않습니다.
Codex는 훅 실행을 실패로 표시하고 오류를 보고한 뒤,
도구 결과에 대한 일반 처리를 계속합니다.

#### 코드 모드에서의 도구 호출

모델이 코드 모드에서 JavaScript로 도구를 호출하면 훅의 결정은
해당 중첩 호출에 적용됩니다. `PreToolUse` 훅은 도구가 실행되기 전에 실행을 막거나
입력을 수정할 수 있습니다. 차단 결정을 내리는 `PostToolUse` 훅은 도구의 사이드 이펙트를 되돌릴 수는 없지만,
원래 결과가 실행 중인 스크립트에 전달되는 것은 막을 수 있습니다.

| 훅 결과                                                      | 코드 모드가 받는 결과                                                                                    |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `PreToolUse` 훅이 차단                                              | 도구가 실행되기 전에 도구의 프로미스가 거부됩니다.                                                         |
| `PreToolUse` 훅이 `updatedInput`을 반환                              | 도구가 수정된 입력으로 실행되고, 프로미스는 그 결과로 이행됩니다.                      |
| `PostToolUse` 훅이 `decision: "block"`을 반환하거나 종료 코드 `2`로 종료 | 도구가 실행된 뒤, 훅이 제시한 사유로 프로미스가 거부됩니다.                                          |
| `PostToolUse` 훅이 `continue: false`를 반환                          | Codex는 훅 피드백을 모델에 표시되는 결과로 사용하지만, 중첩 도구 호출의 프로미스는 거부하지 않습니다. |

### PreCompact

`PreCompact` 훅은 Codex가 채팅 컨텍스트를 압축하기 전에 실행됩니다. `matcher`는
`trigger`에 적용되며, 이 필드의 값은 `manual` 또는 `auto`입니다.

[공통 입력 필드](#common-input-fields) 외에 다음 필드가 제공됩니다:

| 필드     | 유형     | 의미                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Codex 전용 확장 필드. 활성 Codex 턴 ID |
| `trigger` | `string` | 컨텍스트 압축이 시작된 계기: `manual` 또는 `auto`  |

`stdout`으로 출력한 일반 텍스트는 무시됩니다.

`stdout`으로 출력하는 JSON은 [공통 출력 필드](#common-output-fields)를 지원합니다.
일치하는 `PreCompact` 훅이 `continue: false`를 반환하면
Codex는 컨텍스트 압축 전에 중지됩니다.

### PostCompact

`PostCompact`는 Codex가 채팅의 컨텍스트를 압축한 후 실행됩니다.
`matcher`는 `trigger`에 적용되며, 이 필드의 값은 `manual` 또는 `auto`입니다.

다음은 [공통 입력 필드](#common-input-fields)에 추가되는 필드입니다:

| 필드     | 유형     | 의미                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Codex 전용 확장 필드. 활성 Codex 턴 ID |
| `trigger` | `string` | 컨텍스트 압축 트리거: `manual` 또는 `auto`  |

`stdout`으로 출력된 일반 텍스트는 무시됩니다.

`stdout`으로 출력하는 JSON은 [공통 출력 필드](#common-output-fields)를 지원합니다.
일치하는 `PostCompact` 훅이 `continue: false`를 반환하면
Codex는 컨텍스트 압축 후에 중지됩니다.

### UserPromptSubmit

이 이벤트에서는 현재 `matcher`를 사용하지 않습니다.

다음은 [공통 입력 필드](#common-input-fields)에 추가되는 필드입니다:

| 필드     | 유형     | 의미                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Codex 전용 확장 필드. 활성 Codex 턴 ID |
| `prompt`  | `string` | 전송 직전의 사용자 프롬프트            |

`stdout`으로 출력된 일반 텍스트는 개발자 컨텍스트에 추가됩니다.

`stdout`으로 출력하는 JSON은 [공통 출력 필드](#common-output-fields)와
다음과 같은 훅 전용 구조를 지원합니다:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "Ask for a clearer reproduction before editing files."
  }
}

이 `additionalContext` 텍스트는 개발자 컨텍스트에 추가됩니다.

프롬프트를 차단하려면 다음을 반환하세요:

```json
{
  "decision": "block",
  "reason": "Ask for confirmation before doing that."
}

종료 코드 `2`로 종료하고 차단 사유를 `stderr`에 기록할 수도 있습니다.

### SubagentStop

이 이벤트에서는 `matcher`가 `agent_type`에 적용됩니다.

다음은 [공통 입력 필드](#common-input-fields)에 추가되는 필드입니다:

| 필드                    | 유형             | 의미                                         |
| ------------------------ | ---------------- | ----------------------------------------------- |
| `turn_id`                | `string`         | Codex 전용 확장 필드. 활성 Codex 턴 ID  |
| `agent_id`               | `string`         | 하위 에이전트 식별자                     |
| `agent_type`             | `string`         | 하위 에이전트 유형 또는 프로필                        |
| `agent_transcript_path`  | `string \| null` | 하위 에이전트 대화 기록 파일 경로(있는 경우)    |
| `stop_hook_active`       | `boolean`        | 이 하위 에이전트가 이미 실행을 이어간 적이 있는지 여부     |
| `last_assistant_message` | `string \| null` | 하위 에이전트의 최신 어시스턴트 메시지(있는 경우) |

`SubagentStop` 훅이 종료 코드 `0`으로 종료될 때는 `stdout`으로 JSON을 출력해야 합니다.
이 이벤트에서는 일반 텍스트 출력이 유효하지 않습니다.

`stdout`으로 출력하는 JSON은 [공통 출력 필드](#common-output-fields)를 지원합니다.
Codex에 하위 에이전트 플로우를 이어가도록 요청하려면 다음을 반환하세요:

```json
{
  "decision": "block",
  "reason": "Run one more focused pass inside the subagent."
}

종료 코드 `2`로 종료하고 계속 진행해야 하는 이유를 `stderr`에 기록할 수도 있습니다.

일치하는 `SubagentStop` 훅 중 하나라도 `continue: false`를 반환하면
일치하는 다른 `SubagentStop` 훅이 계속 진행하도록 결정하더라도
이 결정이 우선합니다.

### Stop

이 이벤트에서는 현재 `matcher`를 사용하지 않습니다.

다음은 [공통 입력 필드](#common-input-fields)에 추가되는 필드입니다:

| 필드                    | 유형             | 의미                                           |
| ------------------------ | ---------------- | ------------------------------------------------- |
| `turn_id`                | `string`         | Codex 전용 확장 필드. 활성 Codex 턴 ID    |
| `stop_hook_active`       | `boolean`        | 이 턴이 `Stop`에 의해 이미 이어서 진행된 적이 있는지 여부 |
| `last_assistant_message` | `string \| null` | 최신 어시스턴트 메시지 텍스트(있는 경우)       |

`Stop` 훅이 종료 코드 `0`으로 종료될 때는 `stdout`으로 JSON을 출력해야 합니다.
이 이벤트에서는 일반 텍스트 출력이 유효하지 않습니다.

`stdout`으로 출력하는 JSON은 [공통 출력 필드](#common-output-fields)를 지원합니다.
Codex가 계속 진행하도록 하려면 다음을 반환하세요:

```json
{
  "decision": "block",
  "reason": "Run one more pass over the failing tests."
}

종료 코드 `2`로 종료하고 계속 진행해야 하는 이유를 `stderr`에 기록할 수도 있습니다.

이 이벤트에서 `decision: "block"`은 턴을 거부하지 않습니다.
대신 Codex에 계속 진행하도록 지시하고, 새 사용자 프롬프트 역할을 하는 후속 프롬프트를 자동으로 생성합니다.
이때 지정한 `reason` 값을 프롬프트 텍스트로 사용합니다.

일치하는 `Stop` 훅 중 하나라도 `continue: false`를 반환하면
일치하는 다른 `Stop` 훅이 계속 진행하도록 결정하더라도 이 결정이 우선합니다.

### Interrupt

메인 스레드에서 진행 중인 턴을 중단하면 `Interrupt`가 실행됩니다.
중단 사실을 기록하거나 훅이 시작한 작업을 정리하는 데 사용하세요.
유휴 상태의 스레드나 하위 에이전트에서는 실행되지 않으며, 설정된 `matcher`는 모두 무시됩니다.

이 이벤트에는 [공통 입력 필드](#common-input-fields) 외에도
중단된 턴의 ID인 `turn_id`와 `permission_mode`가 포함됩니다.

명령어 훅의 기본 제한 시간은 1초입니다.
제한 시간은 1초에서 3초 사이로만 설정할 수 있습니다. 훅 출력으로는
중단을 막거나 턴을 다시 시작할 수 없습니다. 출력 없이 종료 코드 `0`으로 종료하거나,
선택 사항인 `systemMessage`를 포함한 JSON을 반환해 경고를 표시하세요.
이 이벤트에서는 일반 텍스트 출력이 유효하지 않습니다.

```json
{ "systemMessage": "Saved the interrupted turn to the local audit log." }

## 스키마

  링크된 `main` 브랜치의 스키마에는 현재 릴리스에 없는 훅 필드가 포함될 수 있습니다.
  현재 릴리스의 동작은 이 페이지를 기준으로 확인하세요.

현재 사용되는 정확한 데이터 전송 형식이 필요하면
[Codex GitHub 레포지토리](https://github.com/openai/codex/tree/main/codex-rs/hooks/schema/generated)의 생성된 스키마를 참조하세요.

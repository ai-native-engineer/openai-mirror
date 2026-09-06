<!-- source: https://learn.chatgpt.com/ko-KR/docs/config-file/config-advanced -->

공급자, 정책, 통합을 더 세밀하게 제어해야 할 때 이 옵션을 사용하세요. 빠르게 시작하려면 [기본 구성](/ko-KR/codex/config-file/config-basic)을 참고하세요.

프로젝트 지침, 재사용 가능한 기능, 사용자 지정 슬래시 명령어, 하위 에이전트 워크플로우, 통합에 관한 배경 정보는 [맞춤 설정](/ko-KR/codex/customization/overview)을 참고하세요. 구성 키는 [구성 참조 자료](/ko-KR/codex/config-file/config-reference)에서 확인하세요.

## 프로필

프로필을 사용하면 이름이 지정된 구성 레이어를 저장하고
CLI에서 프로필을 전환할 수 있습니다. `--profile profile-name` 옵션을 지정하면 Codex는
`~/.codex/config.toml` 파일을 로드한 다음 그 위에 `~/.codex/profile-name.config.toml` 파일을 적용합니다.
프로필 이름에는 문자, 숫자, 하이픈, 밑줄을 사용할 수 있습니다.

각 프로필마다 별도의 TOML 파일을 만드세요. 프로필 파일에는
최상위 구성 키를 사용하고 `[profiles.profile-name]` 아래에 중첩하지 마세요.

```toml
# ~/.codex/deep-review.config.toml
model = "gpt-5.5"
model_reasoning_effort = "xhigh"
approval_policy = "on-request"
model_catalog_json = "/Users/me/.codex/model-catalogs/deep-review.json"

```shell
codex --profile deep-review
codex exec --profile deep-review "review this change"

프로필 파일은 기본 사용자 설정보다 우선하지만
프로젝트 및 CLI 구성보다는 우선순위가 낮으므로 기본 구성과 다른
값만 포함하면 됩니다. 프로필 파일에서 `model_catalog_json`도 재정의할 수 있으며,
두 파일에 모두 이 값이 설정되어 있으면 Codex는 프로필의 값을 사용합니다.

Codex 0.134.0 이상에서는 `--profile`이 `config.toml`에서
`[profiles.profile-name]` 설정을 더 이상 읽지 않으며, 최상위 `profile = "profile-name"` 선택기도
더 이상 지원되지 않습니다. 기존 프로필 설정을
`~/.codex/profile-name.config.toml`로 옮긴 다음 해당
`[profiles.profile-name]` 테이블과 `profile = "profile-name"` 선택기를
`config.toml`에서 제거하세요.

## CLI에서 일회성 재정의

`~/.codex/config.toml` 파일을 편집하는 것 외에도 CLI에서 한 번 실행할 때만 구성을 재정의할 수 있습니다:

- 전용 플래그가 제공되는 경우에는 이를 우선 사용하세요(예: `--model`).
- 임의의 키를 재정의해야 할 때는 `-c` / `--config` 옵션을 사용하세요.

예시:

```shell
# Dedicated flag
codex --model gpt-5.6-terra

# Generic key/value override (value is TOML, not JSON)
codex --config model='"gpt-5.6-terra"'
codex --config sandbox_workspace_write.network_access=true
codex --config 'shell_environment_policy.include_only=["PATH","HOME"]'

참고:

- 키에 점 표기법을 사용하면 중첩된 값을 설정할 수 있습니다(예: `mcp_servers.context7.enabled=false`).
- `--config` 값은 TOML로 파싱됩니다. 확실하지 않으면 셸이 공백을 기준으로 값을 분리하지 않도록 값을 따옴표로 감싸세요.
- 값을 TOML로 파싱할 수 없으면 Codex는 이를 문자열로 처리합니다.

## 구성 및 상태 저장 위치

Codex는 로컬 상태를 `CODEX_HOME` 아래에 저장합니다(기본값: `~/.codex`).

해당 위치에서 흔히 볼 수 있는 파일은 다음과 같습니다:

- `config.toml`(로컬 구성)
- `auth.json`(파일 기반 자격 증명 저장 방식을 사용하는 경우) 또는 OS 키체인/키링
- `history.jsonl`(기록 보존이 활성화된 경우)
- 로그, 캐시 등의 기타 사용자별 상태

자격 증명 저장 모드를 비롯한 인증 세부 정보는 [인증](/ko-KR/codex/auth)을 참고하세요. 전체 구성 키 목록은 [구성 참조 자료](/ko-KR/codex/config-file/config-reference)에서 확인하세요.

레포지토리 또는 시스템 경로에 포함된 공유 기본값, 규칙, 스킬에 관한 내용은 [팀 구성](/ko-KR/codex/enterprise/admin-setup#step-4-standardize-local-configuration-with-team-config)을 참고하세요.

기본 제공 OpenAI 공급자가 LLM 프록시, 라우터 또는 데이터 레지던시가 활성화된 프로젝트를 가리키도록 설정하기만 하면 되는 경우, 새 공급자를 정의하지 말고 `config.toml`에서 `openai_base_url`을 설정하세요. 이렇게 하면 별도의 `model_providers.<id>` 항목 없이 기본 제공 `openai` 공급자의 기본 URL을 변경할 수 있습니다.

```toml
openai_base_url = "https://us.api.openai.com/v1"

## 프로젝트 구성 파일(`.codex/config.toml`)

Codex는 사용자 설정뿐 아니라 레포지토리의 `.codex/config.toml` 파일에서 프로젝트 범위 재정의도 읽습니다. 프로젝트 루트에서 현재 작업 디렉터리까지 탐색하며 발견되는 모든 `.codex/config.toml` 파일을 로드합니다. 여러 파일에서 같은 키를 정의한 경우 작업 디렉터리에 가장 가까운 파일이 우선합니다.

보안을 위해 Codex는 프로젝트가 신뢰된 경우에만 프로젝트 범위 구성 파일을 로드합니다. 프로젝트가 신뢰되지 않으면 `.codex/config.toml`, 프로젝트 로컬 훅, 프로젝트 로컬 규칙을 포함하는 프로젝트의 `.codex/` 레이어를 무시합니다. 사용자 및 시스템 레이어는 별도로 유지되며 계속 로드됩니다.

프로젝트 구성의 상대 경로(예: `model_instructions_file`)는 `config.toml` 파일이 있는 `.codex/` 폴더를 기준으로 해석됩니다.

프로젝트 구성 파일에서는 자격 증명을 리디렉션하거나 호스트 소유의 앱 요청
메타데이터를 변경하거나, 공급자 인증을 변경하거나, 구성 프로필을 선택하거나,
로컬 머신에서 알림/텔레메트리 명령어를 실행하는 설정을 재정의할 수 없습니다. Codex는
프로젝트의 `.codex/config.toml`에 다음 키가 있으면 무시하고 시작할 때
경고를 표시합니다: `openai_base_url`, `chatgpt_base_url`,
`apps_mcp_product_sku`, `model_provider`, `model_providers`, `notify`,
`profile`, `profiles`, `experimental_realtime_ws_base_url`, `otel`. 공급자,
알림, 텔레메트리 키는 사용자 수준의
`~/.codex/config.toml`에서 설정하고, 구성 프로필은 `--profile profile-name`과
`~/.codex/profile-name.config.toml` 파일을 사용해 선택하세요.

## 훅

Codex는 활성 구성 레이어와 같은 위치에 있는 `hooks.json` 파일이나
`config.toml` 파일의 인라인 `[hooks]` 테이블에서도 수명 주기 훅을 로드할 수 있습니다.

실제로 가장 유용한 위치 네 곳은 다음과 같습니다:

- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

프로젝트 로컬 훅은 프로젝트의 `.codex/` 레이어가 신뢰된 경우에만 로드됩니다.
사용자 수준 훅은 프로젝트의 신뢰 여부와 무관합니다.

인라인 TOML 훅은 `hooks.json`과 동일한 이벤트 구조를 사용합니다:

```toml
[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"

한 레이어에 `hooks.json`과 인라인 `[hooks]` 테이블이 모두 있으면 Codex는
둘 다 로드하고 경고를 표시합니다. 레이어마다 한 가지 형식만 사용하세요.

현재 이벤트 목록, 입력 필드, 출력 동작, 제한 사항은
[훅](/ko-KR/codex/hooks)을 참고하세요.

## 에이전트 역할(`config.toml`의 `[agents]`)

하위 에이전트 역할 구성(`config.toml`의 `[agents]`)에 관한 자세한 내용은 [하위 에이전트](/ko-KR/codex/agent-configuration/subagents)를 참고하세요.

## 프로젝트 루트 감지

Codex는 작업 디렉터리에서 시작해 프로젝트 루트에 도달할 때까지 상위 디렉터리를 탐색하며 `.codex/` 레이어와 `AGENTS.md` 등의 프로젝트 구성을 찾습니다.

기본적으로 Codex는 `.git`이 있는 디렉터리를 프로젝트 루트로 간주합니다. 이 동작을 맞춤 설정하려면 `config.toml` 파일에서 `project_root_markers` 값을 설정하세요:

```toml
# Treat a directory as the project root when it contains any of these markers.
project_root_markers = [".git", ".hg", ".sl"]

상위 디렉터리 검색을 건너뛰고 현재 작업 디렉터리를 프로젝트 루트로 사용하려면 `project_root_markers = []` 설정을 적용하세요.

## 사용자 지정 모델 공급자

모델 공급자는 Codex가 모델에 연결하는 방식(기본 URL, 통신 API, 인증, 선택적 HTTP 헤더)을 정의합니다. 사용자 지정 공급자는 예약된 기본 제공 공급자 ID인 `openai`, `ollama`, `lmstudio`을 재사용할 수 없습니다.

추가 공급자를 정의하고 `model_provider` 값이 해당 공급자를 가리키도록 설정하세요:

```toml
model = "gpt-5.6-terra"
model_provider = "proxy"

[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "http://proxy.example.com"
env_key = "OPENAI_API_KEY"

[model_providers.local_ollama]
name = "Ollama"
base_url = "http://localhost:11434/v1"

[model_providers.mistral]
name = "Mistral"
base_url = "https://api.mistral.ai/v1"
env_key = "MISTRAL_API_KEY"

사용자 지정 공급자가 독립형 웹 검색 엔드포인트를 지원한다면
공급자 구성에 해당 기능을 명시하세요:

```toml
[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "https://proxy.example.com/v1"
env_key = "OPENAI_API_KEY"
supports_standalone_web_search = true

사용자 지정 공급자에서 이 설정의 기본값은 `false`입니다. 독립형 웹 검색은
개발 중이며 기본적으로 꺼져 있습니다. 공급자의 해당 기능을 `true`로 설정하는 것만으로는
활성화되지 않습니다. 공급자가 호환되는 엔드포인트를 지원해야 하며,
선택한 모델과 런타임도 독립형 검색을 지원해야 합니다.
설정된 [`web_search` 모드](/ko-KR/codex/web-search)와
관리형 검색 제한도 계속 적용됩니다.

필요할 때 요청 헤더를 추가하세요:

```toml
[model_providers.example]
http_headers = { "X-Example-Header" = "example-value" }
env_http_headers = { "X-Example-Features" = "EXAMPLE_FEATURES" }

공급자 인증을 위해 Codex가 외부 자격 증명 도우미에서 베어러 토큰을 가져와야 한다면 명령어 기반 인증을 사용하세요:

```toml
[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "https://proxy.example.com/v1"
wire_api = "responses"

[model_providers.proxy.auth]
command = "/usr/local/bin/fetch-codex-token"
args = ["--audience", "codex"]
timeout_ms = 5000
refresh_interval_ms = 300000

인증 명령어는 `stdin` 입력을 받지 않으며 토큰을 stdout에 출력해야 합니다. Codex는 앞뒤 공백을 제거하고 빈 토큰을 오류로 처리하며 `refresh_interval_ms`에 설정된 간격에 따라 선제적으로 갱신합니다. 인증 재시도 후에만 갱신하려면 `refresh_interval_ms = 0` 설정을 사용하세요. `[model_providers.<id>.auth]`는 `env_key`, `experimental_bearer_token`, `requires_openai_auth` 중 어느 것과도 함께 사용하지 마세요.

### Amazon Bedrock 공급자

Codex에는 기본 제공 `amazon-bedrock` 모델 공급자가 포함되어 있습니다. 해당 공급자를
`model_provider` 값으로 직접 지정하세요. 사용자 지정 공급자와 달리 이 기본 제공 공급자는
중첩된 AWS 프로필 및 리전 재정의만 지원합니다.

```toml
model_provider = "amazon-bedrock"
model = "<bedrock-model-id>"

[model_providers.amazon-bedrock.aws]
profile = "default"
region = "eu-central-1"

`profile` 값을 생략하면 Codex는 표준 AWS 자격 증명 체인을 사용합니다.
`region` 값에는 요청을 처리할 지원되는 Bedrock 리전을 지정하세요.

전체 설정 플로우, 인증 옵션, 지원 모델 및 기능
제공 여부는 [Amazon Bedrock에서 ChatGPT Work와
Codex 사용하기](/ko-KR/codex/amazon-bedrock)를 참고하세요.

## OSS 모드(로컬 공급자)

`--oss` 옵션을 전달하면 Codex를 Ollama 또는 LM Studio 같은
로컬 “오픈 소스” 공급자와 함께 실행할 수 있습니다. `--local-provider` 옵션으로 한 번 실행할 공급자를 선택하거나
`oss_provider`에 기본 공급자를 설정하세요. 둘 다 설정하지 않으면
대화형 CLI에서 공급자를 선택하라는 메시지가 표시되고 `codex exec` 명령은 오류와 함께 종료됩니다.

```toml
# Default local provider used with `--oss`
oss_provider = "ollama" # or "lmstudio"

## Azure 공급자 및 공급자별 튜닝

```toml
[model_providers.azure]
name = "Azure"
base_url = "https://YOUR_PROJECT_NAME.openai.azure.com/openai"
env_key = "AZURE_OPENAI_API_KEY"
query_params = { api-version = "2025-04-01-preview" }
wire_api = "responses"
request_max_retries = 4
stream_max_retries = 10
stream_idle_timeout_ms = 300000

기본 제공 OpenAI 공급자의 기본 URL을 변경하려면 `openai_base_url` 설정을 사용하세요. 기본 제공 공급자 ID는 재정의할 수 없으므로 `[model_providers.openai]` 테이블은 만들지 마세요.

## 데이터 레지던시를 사용하는 API 조직

[데이터 레지던시](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)를 활성화해 생성한 프로젝트에서는 모델 공급자를 만들어 `base_url`을 [올바른 접두사](/api/docs/guides/your-data#which-models-and-features-are-eligible-for-data-residency)로 업데이트할 수 있습니다. 데이터 레지던시가 적용된 ChatGPT 워크스페이스에는 사용자 지정 공급자가 필요하지 않습니다. ChatGPT로 로그인하면 Codex가 워크스페이스의 레지던시 설정을 준수합니다.

```toml
model_provider = "openaidr"
[model_providers.openaidr]
name = "OpenAI Data Residency"
base_url = "https://us.api.openai.com/v1" # Replace 'us' with domain prefix

## 모델 추론, 상세도 및 제한

```toml
model_reasoning_summary = "none"          # Disable summaries
model_verbosity = "low"                   # Shorten responses
model_supports_reasoning_summaries = true # Force reasoning
model_context_window = 128000             # Context window size

`model_verbosity` 설정은 Responses API를 사용하는 공급자에만 적용됩니다. Chat Completions 공급자는 이 설정을 무시합니다.

## 승인 정책 및 샌드박스 모드

승인 엄격도(Codex의 일시 중지 시점에 영향)와 샌드박스 수준(파일 및 네트워크 접근에 영향)을 선택하세요.

`config.toml`을 편집할 때 알아둘 운영상의 세부 사항은 [일반적인 샌드박스 및 승인 조합](/ko-KR/codex/agent-approvals-security#common-sandbox-and-approval-combinations), [쓰기 가능한 루트의 보호된 경로](/ko-KR/codex/agent-approvals-security#protected-paths-in-writable-roots), [네트워크 접근](/ko-KR/codex/agent-approvals-security#network-access)을 참조하세요.

파일 시스템과 네트워크 접근 권한을 함께 구성하는 베타 권한 프로필에 대해서는 [권한](/ko-KR/codex/permissions)을 참조하세요.

세분화된 승인 정책(`approval_policy = { granular = { ... } }`)을 사용해 개별 프롬프트 범주를 허용하거나 자동으로 거부할 수도 있습니다. 일부 경우에는 일반적인 대화형 승인을 사용하고, `request_permissions` 또는 스킬 스크립트 프롬프트 등은 자동으로 거부하려는 경우에 유용합니다.

`approvals_reviewer = "auto_review"`을 설정하면 대상이 되는 대화형 승인 요청이
자동 검토를 거치게 됩니다. 이는 검토자만 변경하며
샌드박스 경계는 변경하지 않습니다.

`[auto_review].policy`로 로컬 검토자 정책 지침을 지정하세요.
관리형 `guardian_policy_config` 설정이 우선 적용됩니다.

```toml
approval_policy = "untrusted"   # Other options: on-request, never, or { granular = { ... } }
approvals_reviewer = "user"     # Or "auto_review" for automatic review
sandbox_mode = "workspace-write"
allow_login_shell = false       # Optional hardening: disallow login shells for shell tools

# Example granular approval policy:
# approval_policy = { granular = {
#   sandbox_approval = true,
#   rules = true,
#   mcp_elicitations = true,
#   request_permissions = false,
#   skill_approval = false
# } }

[sandbox_workspace_write]
exclude_tmpdir_env_var = false  # Allow $TMPDIR
exclude_slash_tmp = false       # Allow /tmp
writable_roots = ["/Users/YOU/.pyenv/shims"]
network_access = false          # Opt in to outbound network

[auto_review]
policy = """
Use your organization's automatic review policy.
"""

### 이름이 지정된 권한 프로필

기본 제공 프로필, 사용자 지정 프로필 구문, 파일 시스템 및
네트워크의 전체 구성 모델에 대해서는 [권한](/ko-KR/codex/permissions)을 참조하세요.

전체 키 목록과 요구 사항의 제약 조건은
[구성 참조](/ko-KR/codex/config-file/config-reference)와
[관리형 구성](/ko-KR/codex/enterprise/managed-configuration)에서 확인하세요.

  workspace-write 모드에서는 일부 환경이 `.git/`과 `.codex/`를
  워크스페이스의 나머지 영역에 쓸 수 있을 때에도 읽기 전용으로 유지합니다. 따라서
  `git commit` 같은 명령어를 샌드박스 외부에서
  실행하려면 여전히 승인이 필요할 수 있습니다. Codex가 특정 명령어를 건너뛰도록 하려면(예: 샌드박스 외부에서 `git
  commit` 차단)
<a href="/codex/agent-configuration/rules">규칙</a>을 사용하세요.

샌드박스를 완전히 비활성화하세요(환경에서 이미 프로세스를 격리하는 경우에만 사용):

```toml
sandbox_mode = "danger-full-access"

## 셸 환경 정책

`shell_environment_policy` 설정은 Codex가 실행하는 명령어에 전달할
환경 변수를 제어합니다. `inherit = "none"` 설정으로 빈 환경에서 시작하거나
`inherit = "core"` 설정으로 축소된 변수 집합을 상속하세요. 불필요한 비밀 정보가 실행되는 명령어에 전달되지 않도록 명시적 값과
키 기반 필터를 추가하세요.

```toml
[shell_environment_policy]
inherit = "core"
set = { MY_FLAG = "1" }
ignore_default_excludes = false

[shell_environment_policy.filters]
"AWS_*" = "exclude"
"AZURE_*" = "exclude"

필터 패턴은 대소문자를 구분하지 않으며 `*` 및 `?`를 지원합니다. `"exclude"` 설정을 사용하면
일치하는 변수를 제거할 수 있습니다. `"include"` 설정을 사용하는 패턴이 하나라도 있으면 Codex는
포함 패턴과 일치하는 변수만 유지합니다. 포함 규칙은 이미 제외된 변수를
복원하지 않습니다. 구성 레이어 간에 필터 키를 병합할 때는
대소문자를 구분하지 않습니다.

`ignore_default_excludes`의 기본값은 `true`이므로 Codex는
`KEY`, `SECRET`, `TOKEN` 중 하나가 포함된 이름의 변수를 자동으로 제거하지 않습니다. 값을 `false`로 설정하면
명시적 필터가 실행되기 전에 이러한 자동 제외가 적용됩니다.

Codex는 자동 제외, 사용자 지정 제외,
`set`의 값, 포함 패턴 허용 목록을 순서대로 적용합니다. `set` 설정은 제외 처리 후
실행되므로 제외된 변수를 복원할 수 있습니다. 다만 포함 패턴 허용 목록은
복원된 값을 다시 제거할 수 있습니다.

이전 방식의 `exclude` 및 `include_only` 배열은 기존
구성에서 계속 지원됩니다. 같은 구성 레이어에서 두 배열 중 어느 것도
`[shell_environment_policy.filters]` 설정과 함께 사용하지 마세요. Codex는
이 조합을 거부합니다.

## MCP 서버

자세한 구성 방법은 전용 [MCP 문서](/ko-KR/codex/extend/mcp)를 참조하세요.

## 관측 가능성 및 텔레메트리

OpenTelemetry(OTel) 로그 내보내기를 활성화하여 Codex 실행(API 요청, SSE/이벤트, 프롬프트, 도구 승인/결과)을 추적하세요. 기본적으로 비활성화되어 있으며 `[otel]`에서 활성화할 수 있습니다:

```toml
[otel]
environment = "staging"   # defaults to "dev"
exporter = "none"         # set to otlp-http or otlp-grpc to send events
log_user_prompt = false   # redact user prompts unless explicitly enabled

익스포터를 선택하세요:

```toml
[otel]
exporter = { otlp-http = {
  endpoint = "https://otel.example.com/v1/logs",
  protocol = "binary",
  headers = { "x-otlp-api-key" = "${OTLP_TOKEN}" }
}}

```toml
[otel]
exporter = { otlp-grpc = {
  endpoint = "https://otel.example.com:4317",
  headers = { "x-otlp-meta" = "abc123" }
}}

`exporter = "none"` 설정을 사용하면 Codex는 이벤트를 기록하지만 전송하지 않습니다. 익스포터는 비동기식으로 일괄 처리하며 종료 시 플러시합니다. 이벤트 메타데이터에는 서비스 이름, CLI 버전, 환경 태그, 대화 ID, 모델, 샌드박스/승인 설정, 이벤트별 필드가 포함됩니다([구성 참조](/ko-KR/codex/config-file/config-reference) 참고).

### 내보내는 항목

Codex는 실행 및 도구 사용에 관한 구조화된 로그 이벤트를 내보냅니다. 대표적인 이벤트 유형은 다음과 같습니다:

- `codex.conversation_starts` (모델, 추론 설정, 샌드박스/승인 정책)
- `codex.api_request` (시도, 상태/성공 여부, 소요 시간, 오류 세부 정보)
- `codex.sse_event` (스트림 이벤트 종류, 성공/실패 여부, 소요 시간, `response.completed` 이벤트의 토큰 수)
- `codex.websocket_request` 및 `codex.websocket_event` (요청 소요 시간 및 메시지별 종류/성공 여부/오류)
- `codex.user_prompt` (길이; 명시적으로 활성화하지 않으면 내용은 가려짐)
- `codex.tool_decision` (승인/거부 여부 및 결정이 구성에 따른 것인지 사용자가 내린 것인지)
- `codex.tool_result` (소요 시간, 성공 여부, 출력 스니펫)

### 내보내는 OTel 메트릭

OTel 메트릭 파이프라인을 활성화하면 Codex는 API, 스트림, 도구 활동에 관한 카운터와 소요 시간 히스토그램을 내보냅니다.

아래 각 메트릭에는 다음 기본 메타데이터 태그도 포함됩니다: `auth_mode`, `originator`, `session_source`, `model`, `app.version`.

| 메트릭                                | 유형      | 필드              | 설명                                                       |
| ------------------------------------- | --------- | ------------------- | ----------------------------------------------------------------- |
| `codex.api_request`                   | 카운터   | `status`, `success` | HTTP 상태 및 성공/실패 여부별 API 요청 수.             |
| `codex.api_request.duration_ms`       | 히스토그램 | `status`, `success` | API 요청 소요 시간(밀리초).                             |
| `codex.sse_event`                     | 카운터   | `kind`, `success`   | 이벤트 종류 및 성공/실패 여부별 SSE 이벤트 수.                |
| `codex.sse_event.duration_ms`         | 히스토그램 | `kind`, `success`   | SSE 이벤트 처리 소요 시간(밀리초).                    |
| `codex.websocket.request`             | 카운터   | `success`           | 성공/실패 여부별 WebSocket 요청 수.                       |
| `codex.websocket.request.duration_ms` | 히스토그램 | `success`           | WebSocket 요청 소요 시간(밀리초).                       |
| `codex.websocket.event`               | 카운터   | `kind`, `success`   | 유형 및 성공/실패 여부별 WebSocket 메시지/이벤트 수.        |
| `codex.websocket.event.duration_ms`   | 히스토그램 | `kind`, `success`   | WebSocket 메시지/이벤트 처리 소요 시간(밀리초).      |
| `codex.tool.call`                     | 카운터   | `tool`, `success`   | 도구 이름 및 성공/실패별 도구 호출 수.           |
| `codex.tool.call.duration_ms`         | 히스토그램 | `tool`, `success`   | 도구 이름 및 결과별 도구 실행 시간(밀리초). |

텔레메트리와 관련된 보안 및 개인정보 보호 지침은 [보안](/ko-KR/codex/agent-approvals-security#monitoring-and-telemetry)에서 자세히 확인하세요.

### 메트릭

기본적으로 Codex는 소량의 익명 사용량 및 상태 데이터를 OpenAI에 주기적으로 전송합니다. 이 데이터는 Codex가 제대로 작동하지 않는 상황을 감지하고 어떤 기능과 구성 옵션이 사용되는지 파악하는 데 도움이 되므로, Codex 팀이 가장 중요한 부분에 집중할 수 있습니다. 이러한 메트릭에는 개인 식별 정보(PII)가 포함되지 않습니다. 메트릭 수집은 OTel 로그/트레이스 내보내기와 별개로 이루어집니다.

한 컴퓨터에서 ChatGPT 데스크톱 앱, Codex CLI, IDE 확장의 메트릭 수집을 모두 비활성화하려면 구성에서 분석 플래그를 설정하세요:

```toml
[analytics]
enabled = false

각 메트릭에는 고유 필드와 아래의 기본 컨텍스트 필드가 포함됩니다.

#### 기본 컨텍스트 필드(모든 이벤트/메트릭에 적용)

- `auth_mode`: `swic` | `api` | `unknown`.
- `model`: 사용된 모델의 이름.
- `app.version`: Codex 버전.

#### 메트릭 카탈로그

각 메트릭에는 필수 필드와 위의 기본 컨텍스트 필드가 포함됩니다. 아래 메트릭 이름에서는 `codex.` 접두사를 생략합니다.
대부분의 메트릭 이름은 `codex-rs/otel/src/metrics/names.rs`에 모여 있으며, 이 파일 외부에서 생성되는 기능별 메트릭도 여기에 포함됩니다.
메트릭에 `tool` 필드가 포함된 경우 이는 내부에서 사용된 도구(예: `apply_patch` 또는 `shell`)를 나타내며, 실제 셸 명령이나 `codex`가 적용하려는 패치 내용은 포함하지 않습니다.

#### 런타임 및 모델 전송

| 메트릭                                          | 유형      | 필드               | 설명                                                  |
| ----------------------------------------------- | --------- | -------------------- | ------------------------------------------------------------ |
| `api_request`                                   | 카운터   | `status`, `success`  | HTTP 상태 및 성공/실패별 API 요청 수.        |
| `api_request.duration_ms`                       | 히스토그램 | `status`, `success`  | API 요청 시간(밀리초).                        |
| `sse_event`                                     | 카운터   | `kind`, `success`    | 이벤트 종류 및 성공/실패별 SSE 이벤트 수.           |
| `sse_event.duration_ms`                         | 히스토그램 | `kind`, `success`    | SSE 이벤트 처리 시간(밀리초).               |
| `websocket.request`                             | 카운터   | `success`            | 성공/실패별 WebSocket 요청 수.                  |
| `websocket.request.duration_ms`                 | 히스토그램 | `success`            | WebSocket 요청 시간(밀리초).                  |
| `websocket.event`                               | 카운터   | `kind`, `success`    | 유형 및 성공/실패별 WebSocket 메시지/이벤트 수.   |
| `websocket.event.duration_ms`                   | 히스토그램 | `kind`, `success`    | WebSocket 메시지/이벤트 처리 시간(밀리초). |
| `responses_api_overhead.duration_ms`            | 히스토그램 |                      | WebSocket 응답에서 측정한 Responses API 오버헤드 시간.      |
| `responses_api_inference_time.duration_ms`      | 히스토그램 |                      | WebSocket 응답에서 측정한 Responses API 추론 시간.     |
| `responses_api_engine_iapi_ttft.duration_ms`    | 히스토그램 |                      | Responses API 엔진 IAPI의 첫 토큰까지 걸린 시간.        |
| `responses_api_engine_service_ttft.duration_ms` | 히스토그램 |                      | Responses API 엔진 서비스의 첫 토큰까지 걸린 시간.     |
| `responses_api_engine_iapi_tbt.duration_ms`     | 히스토그램 |                      | Responses API 엔진 IAPI의 토큰 간 시간.         |
| `responses_api_engine_service_tbt.duration_ms`  | 히스토그램 |                      | Responses API 엔진 서비스의 토큰 간 시간.      |
| `transport.fallback_to_http`                    | 카운터   | `from_wire_api`      | WebSocket에서 HTTP로 폴백한 횟수.                            |
| `remote_models.fetch_update.duration_ms`        | 히스토그램 |                      | 원격 모델 정의를 가져오는 데 걸린 시간.                      |
| `remote_models.load_cache.duration_ms`          | 히스토그램 |                      | 원격 모델 캐시를 로드하는 데 걸린 시간.                         |
| `startup_prewarm.duration_ms`                   | 히스토그램 | `status`             | 결과별 시작 시 사전 워밍업 소요 시간.                         |
| `startup_prewarm.age_at_first_turn_ms`          | 히스토그램 | `status`             | 첫 번째 실제 턴에서 시작 시 사전 워밍업이 완료될 때의 경과 시간.    |
| `cloud_requirements.fetch.duration_ms`          | 히스토그램 |                      | 워크스페이스 관리형 클라우드 요구 사항 가져오기 소요 시간.         |
| `cloud_requirements.fetch_attempt`              | 카운터   | 참고 사항 참조             | 워크스페이스 관리형 클라우드 요구 사항 가져오기 시도 횟수.         |
| `cloud_requirements.fetch_final`                | 카운터   | 참고 사항 참조             | 워크스페이스 관리형 클라우드 요구 사항 가져오기의 최종 결과.    |
| `cloud_requirements.load`                       | 카운터   | `trigger`, `outcome` | 워크스페이스 관리형 클라우드 요구 사항 로드 결과.           |

`cloud_requirements.fetch_attempt` 메트릭에는 `trigger`, `attempt`, `outcome`, `status_code` 필드가 포함됩니다. `cloud_requirements.fetch_final` 메트릭에는 `trigger`, `outcome`, `reason`, `attempt_count`, `status_code` 필드가 포함됩니다.

#### 턴 및 도구 활동

| 메트릭                                 | 유형      | 필드                                                                    | 설명                                                                                                      |
| -------------------------------------- | --------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `turn.e2e_duration_ms`                 | 히스토그램 |                                                                           | 한 턴 전체의 엔드투엔드 소요 시간.                                                                                 |
| `turn.ttft.duration_ms`                | 히스토그램 |                                                                           | 턴에서 첫 토큰이 생성되기까지 걸리는 시간.                                                                                  |
| `turn.ttfm.duration_ms`                | 히스토그램 |                                                                           | 턴에서 모델의 첫 출력 항목이 생성되기까지 걸리는 시간.                                                                      |
| `turn.network_proxy`                   | 카운터   | `active`, `tmp_mem_enabled`                                               | 해당 턴에서 관리형 네트워크 프록시가 활성 상태였는지 여부.                                                       |
| `turn.memory`                          | 카운터   | `read_allowed`, `feature_enabled`, `config_use_memories`, `has_citations` | 턴별 메모리 읽기 가능 여부와 메모리 인용 사용 여부.                                                     |
| `turn.tool.call`                       | 히스토그램 | `tmp_mem_enabled`                                                         | 턴에서 도구가 호출된 횟수.                                                                                |
| `turn.token_usage`                     | 히스토그램 | `token_type`, `tmp_mem_enabled`                                           | 토큰 유형별 턴당 토큰 사용량(`total`, `input`, `cached_input`, `output` 또는 `reasoning_output`).          |
| `tool.call`                            | 카운터   | `tool`, `success`                                                         | 도구 이름 및 성공/실패 여부에 따른 도구 호출 횟수.                                                          |
| `tool.call.duration_ms`                | 히스토그램 | `tool`, `success`                                                         | 도구 이름과 결과에 따른 도구 실행 시간(밀리초).                                                |
| `tool.unified_exec`                    | 카운터   | `tty`                                                                     | TTY 모드별 통합 exec 도구 호출 횟수.                                                                             |
| `approval.requested`                   | 카운터   | `tool`, `approved`                                                        | 도구 승인 요청 결과(`approved`, `approved_with_amendment`, `approved_for_session`, `denied`, `abort`). |
| `mcp.call`                             | 카운터   | 참고 사항 참조                                                                  | MCP 도구 호출 결과.                                                                                      |
| `mcp.call.duration_ms`                 | 히스토그램 | 참고 사항 참조                                                                  | MCP 도구 호출 소요 시간.                                                                                    |
| `mcp.tools.list.duration_ms`           | 히스토그램 | `cache`                                                                   | 캐시 적중/미적중 상태를 포함한 MCP 도구 목록 조회 소요 시간.                                                          |
| `mcp.tools.fetch_uncached.duration_ms` | 히스토그램 |                                                                           | 캐시 미적중 시 MCP 도구를 가져오는 데 걸린 시간.                                                                |
| `mcp.tools.cache_write.duration_ms`    | 히스토그램 |                                                                           | Codex 앱의 MCP 도구 캐시 쓰기 소요 시간.                                                                    |
| `hooks.run`                            | 카운터   | `hook_name`, `source`, `status`                                           | 훅 이름, 소스, 상태별 훅 실행 횟수.                                                                 |
| `hooks.run.duration_ms`                | 히스토그램 | `hook_name`, `source`, `status`                                           | 훅 실행 시간(밀리초).                                                                               |

`mcp.call` 및 `mcp.call.duration_ms` 메트릭에는 `status`가 포함됩니다. 일반 도구 호출에서 내보내는 데이터에는 `tool`도 포함되며, 사용 가능한 경우 `connector_id`와 `connector_name`도 포함됩니다. 차단된 Codex 앱 MCP 호출은 `status`만 포함된 `mcp.call`을 내보낼 수 있습니다.

#### 스레드, 작업 및 기능

| 메트릭                            | 유형      | 필드                | 설명                                                                      |
| --------------------------------- | --------- | --------------------- | -------------------------------------------------------------------------------- |
| `feature.state`                   | 카운터   | `feature`, `value`    | 기본값과 다른 기능 값(기본값이 아닌 값마다 한 행씩 내보냄).         |
| `status_line`                     | 카운터   |                       | 상태 표시줄이 설정된 상태로 시작된 세션.                                   |
| `model_warning`                   | 카운터   |                       | 모델에 전달된 경고.                                                       |
| `thread.started`                  | 카운터   | `is_git`              | 작업 디렉터리가 Git 레포지토리에 속하는지 여부를 태그로 기록한 새 스레드 생성.    |
| `conversation.turn.count`         | 카운터   |                       | 스레드 종료 시 기록되는 스레드별 사용자/어시스턴트 턴 수.              |
| `thread.fork`                     | 카운터   | `source`              | 기존 스레드를 포크하여 새 스레드 생성.                                |
| `thread.rename`                   | 카운터   |                       | 스레드 이름 변경.                                                                  |
| `thread.side`                     | 카운터   | `source`              | 별도 대화 생성.                                                       |
| `thread.skills.enabled_total`     | 히스토그램 |                       | 새 스레드에서 활성화된 스킬 수.                                       |
| `thread.skills.kept_total`        | 히스토그램 |                       | 프롬프트 렌더링 후 유지된 활성 스킬 수.                            |
| `thread.skills.truncated`         | 히스토그램 |                       | 스킬 렌더링으로 인해 활성화된 스킬 목록이 잘렸는지 여부(`1` 또는 `0`).          |
| `task.compact`                    | 카운터   | `type`                | 유형별 컨텍스트 압축 횟수(`remote` 또는 `local`, 수동 및 자동 포함). |
| `task.review`                     | 카운터   |                       | 시작된 검토 횟수.                                                     |
| `task.undo`                       | 카운터   |                       | 실행 취소 동작이 발생한 횟수.                                                |
| `task.user_shell`                 | 카운터   |                       | 사용자 셸 동작 횟수(예: TUI의 `!`).                       |
| `shell_snapshot`                  | 카운터   | 참고 사항 참조              | 셸 스냅샷 생성 성공 여부.                                       |
| `shell_snapshot.duration_ms`      | 히스토그램 | `success`             | 셸 스냅샷 생성에 걸린 시간.                                                   |
| `skill.injected`                  | 카운터   | `status`, `skill`     | 스킬별 주입 결과.                                               |
| `plugins.startup_sync`            | 카운터   | `transport`, `status` | 선별된 플러그인의 시작 시 동기화 시도 횟수.                                            |
| `plugins.startup_sync.final`      | 카운터   | `transport`, `status` | 선별된 플러그인의 시작 시 동기화 최종 결과.                                       |
| `multi_agent.spawn`               | 카운터   | `role`                | 역할별 에이전트 생성 횟수.                                                            |
| `multi_agent.resume`              | 카운터   |                       | 에이전트 재개 횟수.                                                                   |
| `multi_agent.nickname_pool_reset` | 카운터   |                       | 에이전트 닉네임 풀 재설정 횟수.                                                      |

`shell_snapshot` 메트릭에는 `success`가 포함되며, 실패한 경우 `failure_reason`도 포함됩니다.

#### 메모리 및 로컬 상태

| 메트릭                         | 유형      | 필드                    | 설명                                               |
| ------------------------------ | --------- | ------------------------- | --------------------------------------------------------- |
| `memory.phase1`                | 카운터   | `status`                  | 상태별 메모리 1단계 작업 수.                      |
| `memory.phase1.e2e_ms`         | 히스토그램 |                           | 메모리 1단계의 전체 소요 시간.                   |
| `memory.phase1.output`         | 카운터   |                           | 메모리 1단계에서 기록된 출력 수.                           |
| `memory.phase1.token_usage`    | 히스토그램 | `token_type`              | 토큰 유형별 메모리 1단계 토큰 사용량.                 |
| `memory.phase2`                | 카운터   | `status`                  | 상태별 메모리 2단계 작업 수.                      |
| `memory.phase2.e2e_ms`         | 히스토그램 |                           | 메모리 2단계의 전체 소요 시간.                   |
| `memory.phase2.input`          | 카운터   |                           | 메모리 2단계 입력 수.                               |
| `memory.phase2.token_usage`    | 히스토그램 | `token_type`              | 토큰 유형별 메모리 2단계 토큰 사용량.                 |
| `memories.usage`               | 카운터   | `kind`, `tool`, `success` | 종류, 도구 및 성공/실패별 메모리 사용량.          |
| `external_agent_config.detect` | 카운터   | 참고 사항 참조                  | 마이그레이션 항목 유형별 외부 에이전트 설정 감지 횟수.  |
| `external_agent_config.import` | 카운터   | 참고 사항 참조                  | 마이그레이션 항목 유형별 외부 에이전트 설정 가져오기 횟수.     |
| `db.backfill`                  | 카운터   | `status`                  | 초기 상태 DB 백필 결과(`upserted`, `failed`). |
| `db.backfill.duration_ms`      | 히스토그램 | `status`                  | 초기 상태 DB 백필 소요 시간.                |
| `db.error`                     | 카운터   | `stage`                   | 상태 DB 작업 중 발생한 오류.                        |

`external_agent_config.detect` 및 `external_agent_config.import` 메트릭에는 `migration_type` 필드가 포함됩니다. 스킬 마이그레이션에는 `skills_count` 필드도 포함됩니다.

#### Windows 샌드박스

| 메트릭                                           | 유형      | 필드                                    | 설명                                           |
| ------------------------------------------------ | --------- | ----------------------------------------- | ----------------------------------------------------- |
| `windows_sandbox.setup_success`                  | 카운터   | `originator`, `mode`                      | Windows 샌드박스 설정 성공 횟수.                      |
| `windows_sandbox.setup_failure`                  | 카운터   | `originator`, `mode`                      | Windows 샌드박스 설정 실패 횟수.                       |
| `windows_sandbox.setup_duration_ms`              | 히스토그램 | `result`, `originator`, `mode`            | Windows 샌드박스 설정 소요 시간.                       |
| `windows_sandbox.elevated_setup_success`         | 카운터   |                                           | Windows 샌드박스를 관리자 권한으로 설정하는 데 성공한 횟수.             |
| `windows_sandbox.elevated_setup_failure`         | 카운터   | 참고 사항 참조                                  | Windows 샌드박스를 관리자 권한으로 설정하는 데 실패한 횟수.              |
| `windows_sandbox.elevated_setup_canceled`        | 카운터   | 참고 사항 참조                                  | 관리자 권한으로 Windows 샌드박스를 설정하려다 취소된 횟수.     |
| `windows_sandbox.elevated_setup_duration_ms`     | 히스토그램 | `result`                                  | Windows 샌드박스를 관리자 권한으로 설정하는 데 걸린 시간.              |
| `windows_sandbox.elevated_prompt_shown`          | 카운터   |                                           | 관리자 권한 샌드박스 설정 프롬프트가 표시된 횟수.                  |
| `windows_sandbox.elevated_prompt_accept`         | 카운터   |                                           | 관리자 권한 샌드박스 설정 프롬프트를 수락한 횟수.               |
| `windows_sandbox.elevated_prompt_use_legacy`     | 카운터   |                                           | 관리자 권한 설정 프롬프트에서 사용자가 레거시 샌드박스를 선택한 횟수.   |
| `windows_sandbox.elevated_prompt_quit`           | 카운터   |                                           | 관리자 권한 설정 프롬프트에서 사용자가 종료를 선택한 횟수.                   |
| `windows_sandbox.fallback_prompt_shown`          | 카운터   |                                           | 폴백 샌드박스 프롬프트 표시.                        |
| `windows_sandbox.fallback_retry_elevated`        | 카운터   |                                           | 사용자가 폴백 프롬프트에서 권한 상승 설정을 다시 시도함. |
| `windows_sandbox.fallback_use_legacy`            | 카운터   |                                           | 사용자가 폴백 프롬프트에서 레거시 샌드박스를 선택함.   |
| `windows_sandbox.fallback_prompt_quit`           | 카운터   |                                           | 사용자가 폴백 프롬프트에서 종료함.                   |
| `windows_sandbox.legacy_setup_preflight_failed`  | 카운터   | 참고                                  | 레거시 Windows 샌드박스 설정 사전 점검 실패.       |
| `windows_sandbox.setup_elevated_sandbox_command` | 카운터   |                                           | 권한 상승 샌드박스 설정 명령어 호출.               |
| `windows_sandbox.createprocessasuserw_failed`    | 카운터   | `error_code`, `path_kind`, `exe`, `level` | Windows `CreateProcessAsUserW` 실패.              |

Windows 설정 실패에 관한 세부 정보가 있으면 권한 상승 설정 실패 메트릭에 `code`와 `message`가 포함되며, 공유 설정 경로에서 내보낸 경우에는 `originator`도 포함될 수 있습니다. `windows_sandbox.legacy_setup_preflight_failed` 메트릭은 공유 설정 경로에서 내보낸 경우 `originator`를 포함하지만, 폴백 프롬프트 사전 점검 실패에는 필드가 전혀 포함되지 않을 수도 있습니다.

### 피드백 제어

기본적으로 로컬 클라이언트에서는 사용자가 `/feedback`에서 피드백을 보낼 수 있습니다. 같은 기기의 ChatGPT 데스크톱 앱, Codex CLI, IDE 확장 전체에서 피드백 수집을 비활성화하려면 구성을 업데이트하세요:

```toml
[feedback]
enabled = false

비활성화하면 `/feedback`에 비활성화 안내가 표시되고 Codex는 피드백 제출을 거부합니다.

### 추론 이벤트 숨기기 또는 표시하기

과도한 “추론” 출력(예: CI 로그)을 줄이려면 해당 출력을 숨길 수 있습니다:

```toml
hide_agent_reasoning = true

모델이 내보내는 원시 추론 내용을 표시하려면:

```toml
show_raw_agent_reasoning = true

원시 추론은 워크플로우에서 허용 가능한 경우에만 활성화하세요. 일부 모델이나 제공자(예: `gpt-oss`)는 원시 추론을 내보내지 않으므로, 이 경우에는 설정을 변경해도 눈에 보이는 효과가 없습니다.

## 알림

Codex가 지원하는 이벤트(현재는 `agent-turn-complete`만 해당)를 내보낼 때마다 외부 프로그램을 실행하려면 `notify`를 사용하세요. 기본 제공 TUI 알림에서 처리하지 않는 데스크톱 토스트, 채팅 웹훅, CI 업데이트 또는 기타 별도 채널 알림에 유용합니다.

```toml
notify = ["python3", "/path/to/notify.py"]

다음은 `agent-turn-complete`에 반응하는 `notify.py` 예시(일부 생략)입니다:

```python
#!/usr/bin/env python3

def main() -> int:
    notification = json.loads(sys.argv[1])
    if notification.get("type") != "agent-turn-complete":
        return 0
    title = f"Codex: {notification.get('last-assistant-message', 'Turn Complete!')}"
    message = " ".join(notification.get("input-messages", []))
    subprocess.check_output([
        "terminal-notifier",
        "-title", title,
        "-message", message,
        "-group", "codex-" + notification.get("thread-id", ""),
        "-activate", "com.googlecode.iterm2",
    ])
    return 0

if __name__ == "__main__":
    sys.exit(main())

스크립트는 JSON 인수 하나를 받습니다. 일반적으로 사용되는 필드는 다음과 같습니다:

- `type`(현재 `agent-turn-complete`)
- `thread-id`(세션 식별자)
- `turn-id`(턴 식별자)
- `cwd`(작업 디렉터리)
- `input-messages`(해당 턴으로 이어진 사용자 메시지)
- `last-assistant-message`(마지막 어시스턴트 메시지 텍스트)

스크립트를 디스크의 원하는 위치에 저장한 다음 `notify`에 해당 경로를 지정하세요.

#### `notify`와 `tui.notifications` 비교

- `notify`는 외부 프로그램을 실행하며 웹훅, 데스크톱 알림 도구, CI 훅에 적합합니다.
- `tui.notifications`는 TUI에 내장되어 있으며 필요에 따라 이벤트 유형(예: `agent-turn-complete`, `approval-requested`)별로 필터링할 수 있습니다.
- `tui.notification_method` 설정으로 TUI가 터미널 알림을 내보내는 방식(`auto`, `osc9` 또는 `bel`)을 제어합니다.
- `tui.notification_condition` 설정은 터미널에 포커스가 없을 때만(`unfocused`) TUI 알림을 보낼지,
  상태와 관계없이 항상(`always`) 보낼지 제어합니다.

`auto` 모드에서 Codex는 OSC 9 알림(일부 터미널이 데스크톱 알림으로 해석하는 터미널 이스케이프 시퀀스)을 우선 사용하며, 그렇지 않으면 BEL(`\x07`)을 대신 사용합니다.

정확한 키는 [구성 참조 자료](/ko-KR/codex/config-file/config-reference)에서 확인하세요.

## 히스토리 보존

기본적으로 Codex는 `CODEX_HOME` 아래에 로컬 세션 대화 기록을 저장합니다(예: `~/.codex/history.jsonl`). 로컬 히스토리 보존을 비활성화하려면:

```toml
[history]
persistence = "none"

히스토리 파일의 최대 크기를 제한하려면 `history.max_bytes` 값을 설정하세요. 파일이 제한을 초과하면 Codex는 가장 오래된 항목을 삭제하고 최신 기록은 유지하면서 파일을 정리합니다.

```toml
[history]
max_bytes = 104857600 # 100 MiB

## 클릭 가능한 인용

해당 기능을 지원하는 터미널/편집기 통합을 사용하면 Codex가 파일 인용을 클릭 가능한 링크로 표시할 수 있습니다. Codex가 사용할 URI 스킴을 선택하려면 `file_opener`를 설정하세요:

```toml
file_opener = "vscode" # or cursor, windsurf, vscode-insiders, none

예: `/home/user/project/main.py:42` 같은 인용은 클릭 가능한 `vscode://file/...:42` 링크로 변환할 수 있습니다.

## 프로젝트 지침 탐색

Codex는 `AGENTS.md` 및 관련 파일을 읽어 세션의 첫 번째 턴에 제한된 분량의 프로젝트 지침을 포함합니다. 다음 두 설정으로 이 동작을 제어할 수 있습니다:

- `project_doc_max_bytes`: 각 `AGENTS.md` 파일에서 읽을 분량
- `project_doc_fallback_filenames`: 특정 디렉터리 수준에 `AGENTS.md`가 없을 때 추가로 확인할 파일 이름

자세한 단계별 안내는 [AGENTS.md를 사용한 맞춤 지침](/ko-KR/codex/agent-configuration/agents-md)에서 확인하세요.

## 데스크톱

이 섹션의 옵션은 ChatGPT 데스크톱 앱에만 적용됩니다.

### 맞춤 파일 핸들러 추가

ChatGPT 데스크톱 앱이 기본적으로 지원하지 않는 편집기나 내부 런처로 파일을 열려면 사용자 수준의 `~/.codex/config.toml` 파일에서
`desktop.custom_file_handlers` 아래에 항목을 추가하세요.
각 항목은 앱의
 **다음에서 열기** 메뉴에 편집기 대상을 추가합니다.
`command`가 실제로 존재하는 절대 경로이거나 앱의 `PATH`에서 찾을 수 있으면 해당 대상이 목록에 표시됩니다.

다음 예시는 파일을 핸들러에 전달하는 세 가지 방법을 보여 줍니다:

```toml
# Append the opened path directly after the command.
[desktop.custom_file_handlers.vscodium]
label = "VSCodium"
icon = "/Users/you/.codex/icons/vscodium.png"
command = "codium"

# Place fixed arguments before the opened path.
[desktop.custom_file_handlers.textedit]
label = "TextEdit"
icon = "/Users/you/.codex/icons/textedit.png"
command = "/usr/bin/open"
args = ["-a", "TextEdit"]

# Append one JSON argument with the path and editor context.
[desktop.custom_file_handlers.company_editor]
label = "Company Editor"
icon = "/opt/company/editor/icon.png"
command = "/opt/company/bin/editor"
input = "json_argument"

`config.toml`을 저장한 다음 ChatGPT 데스크톱 앱을 다시 시작하세요.

핸들러 ID는 TOML 테이블 헤더의 마지막 세그먼트입니다. 길이는
1–64자여야 하며 ASCII 영문자나 숫자로 시작해야 합니다. 나머지에는
ASCII 영문자, 숫자, 마침표, 밑줄 또는 하이픈만 사용할 수 있습니다. 앱은
ID에 `custom:` 접두사를 붙여 표시합니다. 예를 들어 `company_editor`는
`custom:company_editor`가 됩니다. 마침표가 포함된 ID는 TOML이 중첩 테이블로
해석하지 않도록 따옴표로 묶으세요. 예:

```toml
[desktop.custom_file_handlers."company.editor"]
label = "Company Editor"
icon = "/opt/company/editor/icon.png"
command = "/opt/company/bin/editor"

각 핸들러는 다음 필드를 지원합니다:

| 필드          | 필수 | 설명                                                                                                                                                              |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `label`        | 예      | 앱에 표시되는 이름입니다.                                                                                                                                                 |
| `icon`         | 예      | `apps/vscode.png` 같은 번들 앱 아이콘, base64 `data:image/...` URL, `file:` URI 또는 로컬 이미지의 절대 경로입니다. 지원되지 않는 소스를 지정하면 기본 VS Code 아이콘이 사용됩니다. |
| `command`      | 예      | 감지하여 실행할 실행 파일 경로 또는 명령어 이름입니다.                                                                                                                    |
| `args`         | 아니요       | `command`와 파일 입력 사이에 삽입되는 문자열 배열입니다. 기본값은 `[]`입니다.                                                                                            |
| `input`        | 아니요       | 앱이 파일 입력을 전달하는 방식입니다. `path`, `json_argument`, `json_stdin` 중 하나를 사용합니다. 기본값은 `path`입니다.                                                                              |
| `supports_ssh` | 아니요       | SSH 워크스페이스의 파일에 핸들러를 제공할지 여부입니다. 기본값은 `false`입니다. 핸들러에 원격 호스트 및 경로의 세부 정보가 필요하면 `json_stdin` 방식을 사용하세요.                     |

`input` 값에 따라 `args` 뒤에 오는 내용이 결정됩니다:

- `path` 사용 시 경로가 명령어의 마지막 인수로 추가됩니다.
- `json_argument` 사용 시 `target`, `path`, `appPath` 및
`location` 필드를 포함하는 JSON 객체가 추가됩니다. `location` 값은 1부터 시작하는 `line` 및
`column` 값을 포함하는 객체이거나 `null`입니다.
- `json_stdin` 사용 시 인수를 추가하는 대신 JSON 객체를 표준 입력에
  씁니다. 객체에는 `hostConfig`, `remoteWorkspaceRoot` 및
`remotePath` 필드도 포함되며, 해당하지 않는 필드의 값은 `null`입니다.

예를 들어 사용자가 특정 소스 위치를 열 때 `company_editor` 핸들러가 다음
인수를 받을 수 있습니다:

```json
{
  "target": "custom:company_editor",
  "path": "/repo/src/index.ts",
  "appPath": null,
  "location": { "line": 12, "column": 3 }
}

사용자 지정 핸들러를 기본 편집기로 선택하면 프로젝트별 기본 설정을 포함해
기본 제공 편집기를 선택할 때와 같은 방식으로 해당 선택이 저장됩니다.

## TUI 옵션

하위 명령어 없이 `codex` 명령어를 실행하면 대화형 터미널 UI(TUI)가 시작됩니다. Codex는 `[tui]`에서 다음과 같은 TUI 전용 구성 옵션을 제공합니다:

- `tui.notifications`: 알림 활성화/비활성화(또는 특정 유형으로 제한)
- `tui.notification_method`: 터미널 알림 방식으로 `auto`, `osc9`, `bel` 중 하나 선택
- `tui.notification_condition`: 알림 발생 조건으로 `unfocused` 또는 `always`를
  선택
- `tui.animations`: ASCII 애니메이션 및 반짝임 효과 활성화/비활성화
- `tui.alternate_screen`: 대체 화면 사용 제어(터미널 스크롤백을 유지하려면 `never`로 설정)
- `tui.show_tooltips`: 환영 화면에서 온보딩 툴팁 표시 또는 숨기기

`tui.notification_method`의 기본값은 `auto`입니다. `auto` 모드에서 Codex는 터미널이 OSC 9 알림을 지원하는 것으로 보이면 OSC 9 알림(일부 터미널이 데스크톱 알림으로 해석하는 터미널 이스케이프 시퀀스)을 우선 사용하고, 그렇지 않으면 BEL(`\x07`)을 사용합니다.

전체 키 목록은 [구성 참조 자료](/ko-KR/codex/config-file/config-reference)에서 확인하세요.

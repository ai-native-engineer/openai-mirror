<!-- source: https://learn.chatgpt.com/ko-KR/docs/extend/mcp -->

모델 컨텍스트 프로토콜(MCP)은 모델을 도구 및 컨텍스트와 연결합니다. MCP를 사용하면
ChatGPT나 Codex가 타사 문서에 액세스하거나 브라우저, Figma 같은
개발자 도구와 상호 작용하도록 할 수 있습니다.

ChatGPT 웹은 플러그인이 제공하는 원격 MCP 기반 도구를 사용할 수 있습니다. 로컬 Codex
클라이언트도 MCP 서버에 직접 연결하고 구성을 공유할 수 있습니다.

<a id="supported-mcp-features"></a>

ChatGPT 데스크톱 앱, Codex CLI, IDE 확장은 MCP 서버를 지원하며
동일한 Codex 호스트의 MCP 구성을 공유합니다.

아래의 지원 기능은 Codex 호스트에 구성된 MCP 서버에 적용됩니다.
호스팅된 플러그인 도구는 지원하는 기능이 다를 수 있습니다.

## 지원되는 MCP 기능

- **STDIO 서버**: 명령어로 시작하여 로컬 프로세스로 실행되는 서버입니다.
  - 환경 변수
- **Streamable HTTP 서버**: 주소로 접속하는 서버입니다.
  - Bearer 토큰 인증
  - 클라이언트 ID 메타데이터 문서(CIMD)와
동적 클라이언트 등록(DCR)을 포함한 OAuth 인증
  - 신뢰할 수 있는 자사 서버용 ChatGPT 세션 인증
- **서버 지침**: Codex는 초기화 중 반환되는 MCP `instructions` 필드를 읽고, 서버 도구와 함께 서버 전반에 적용되는 지침으로 사용합니다.

Codex용 MCP 서버를 구축하거나 유지 관리한다면 서버 전체에 적용되는 도구 간 워크플로우, 제약 조건, 요청 한도를 `instructions`에 포함하세요. Codex가 서버 사용 방식을 결정할 때 핵심 지침을 참고할 수 있도록 처음 512자만으로도 내용이 완결되게 작성하세요.

## Codex를 MCP 서버에 연결

Codex는 다른 Codex 구성 설정과 함께 MCP 구성을 `config.toml`에 저장합니다. 기본적으로 `~/.codex/config.toml`에 저장하지만, `.codex/config.toml` 파일을 사용해 MCP 서버의 범위를 프로젝트로 한정할 수도 있습니다(신뢰할 수 있는 프로젝트만 해당).

ChatGPT 데스크톱 앱, Codex CLI, IDE 확장은 이 구성을 공유합니다.
MCP 서버를 한 번 구성하면 설정을 다시 하지 않고도
이 클라이언트들을 번갈아 사용할 수 있습니다.

### ChatGPT 데스크톱 앱에서 구성

1. **설정을** 열고 **MCP 서버를** 선택하세요.
2. **서버 추가를** 선택하세요.
3. 이름을 입력하고 **STDIO** 또는 **Streamable HTTP를** 선택한 다음,
   서버의 명령어나 URL을 입력하세요.
4. 서버를 저장한 다음 **다시 시작을** 선택하세요.

서버 목록에서 활성화된 서버와 OAuth가 필요한 서버를 확인할 수 있습니다.
OAuth 서버에 로그인이 필요하면 **인증을** 선택하세요. Composer에 `/mcp` 명령어를 입력하면
연결된 서버를 확인할 수 있습니다.

## ChatGPT 웹에서 MCP 기반 도구 사용

호스팅 환경의 ChatGPT Work 채팅에서 [플러그인](/ko-KR/codex/plugins)을 설치하면
함께 제공되는 커넥터와 원격 MCP 도구를 사용할 수 있습니다. 설치 후에는 채팅과 Work에서
해당 도구를 사용할 수 있습니다. 워크스페이스 관리자는
사용할 수 있는 플러그인과 도구를 제어할 수 있습니다.

ChatGPT 웹은 로컬 Codex 구성 파일을 읽지 않으며 로컬
Codex 명령어 메뉴도 제공하지 않습니다. **플러그인** 탭을 열어
사용할 수 있는 도구를 둘러보고 관리하세요.

### CLI로 구성

#### MCP 서버 추가

```bash
codex mcp add <server-name> --env VAR1=VALUE1 --env VAR2=VALUE2 -- <stdio server-command>

예를 들어 개발자 문서용 무료 MCP 서버인 Context7을 추가하려면 다음 명령어를 실행할 수 있습니다:

```bash
codex mcp add context7 -- npx -y @upstash/context7-mcp

#### 기타 CLI 명령어

구성된 서버를 확인하려면 `codex mcp list` 명령어를 실행하세요. 사용 가능한 모든 MCP
명령어를 확인하려면 `codex mcp --help` 명령어를 실행하세요. OAuth를 지원하는 서버의 경우
`codex mcp login <server-name>` 명령어를 실행하세요.

#### 터미널 UI(TUI)

`codex` TUI에서 `/mcp` 명령어를 사용하면 활성 MCP 서버를 확인할 수 있습니다.

### IDE 확장에서 구성

1. 톱니바퀴 메뉴를 연 다음 **MCP 서버를** 선택하세요.
2. **서버 추가를** 선택하세요.
3. 이름을 입력하고 **STDIO** 또는 **Streamable HTTP를** 선택한 다음,
   서버의 명령어나 URL을 입력하세요.
4. 서버를 저장한 다음 **확장 프로그램 다시 시작을** 선택하세요.

MCP 서버 목록에서 활성화된 서버와 OAuth가 필요한 서버를 확인할 수 있습니다.
OAuth 서버에 로그인이 필요하면 **인증을** 선택하세요.

### config.toml로 구성

더 세밀하게 제어하려면 `~/.codex/config.toml` 파일이나 프로젝트 범위의
`.codex/config.toml` 파일을 수정하세요. [구성 참조 자료](/ko-KR/codex/config-file/config-reference)에서
지원되는 모든 MCP 옵션의 목록을 확인하고 검색할 수 있습니다.

구성 파일의 `[mcp_servers.<server-name>]` 테이블에서 각 MCP 서버를 구성하세요.

<a id="stdio-servers"></a>

#### STDIO 서버

- `command`(필수): 서버를 시작하는 명령어입니다.
- `args`(선택 사항): 서버에 전달할 인수입니다.
- `env`(선택 사항): 서버에 설정할 환경 변수입니다.
- `env_vars`(선택 사항): 허용하고 전달할 환경 변수입니다.
- `cwd`(선택 사항): 서버를 시작할 작업 디렉터리입니다.
- `experimental_environment`(선택 사항): `remote`로 설정하면 원격 실행기 환경을 사용할 수 있을 때
  해당 환경을 통해 stdio 서버를 시작합니다.

`env_vars`에는 변수 이름만 지정하거나 소스가 지정된 객체를 넣을 수 있습니다:

```toml
env_vars = ["LOCAL_TOKEN", { name = "REMOTE_TOKEN", source = "remote" }]

문자열 항목과 `source = "local"` 설정은 Codex의 로컬 환경에서 값을 읽습니다.
`source = "remote"` 설정은 원격 실행기 환경에서 값을 읽으며,
원격 MCP stdio가 필요합니다.

<a id="streamable-http-servers"></a>

#### Streamable HTTP 서버

- `url`(필수): 서버 주소입니다.
- `auth`(선택 사항): 구성된 Bearer 토큰과
  인증 헤더 다음으로 시도할 인증 방식입니다. 저장된 MCP OAuth 자격 증명을 사용하려면 `oauth`(기본값)로 설정하세요.
  `chatgpt`로 설정하면 신뢰할 수 있는 자사 ChatGPT 오리진에 대해
  현재 ChatGPT 세션을 사용하며, 저장된 OAuth를 대체 인증 수단으로 사용합니다.
- `bearer_token_env_var`(선택 사항): `Authorization` 헤더로 전송할 Bearer 토큰이 들어 있는 환경 변수의 이름입니다.
- `http_headers`(선택 사항): 헤더 이름을 정적 값에 매핑한 맵입니다.
- `env_http_headers`(선택 사항): 헤더 이름을 환경 변수 이름에 매핑한 맵입니다. 값은 환경에서 가져옵니다.
- `http_headers_helper`(선택 사항): 헤더 이름과 문자열 값으로 이루어진 JSON 객체를 출력하는
  로컬 명령어입니다. 출력 예시는 `{"X-Auth": "temporary-token"}`입니다.
  로컬 환경에서 이루어지는 HTTP MCP 연결을 지원하며,
  stdio 서버나 원격 실행 환경을 통한 연결은 지원하지 않습니다.

Codex는 연결에 사용할 헬퍼 헤더를 캐시합니다. 동일 오리진에 대한 POST 요청이
`401` 또는 `403`를 반환하면 헤더를 한 번 갱신하고,
헬퍼가 변경된 값을 반환한 경우에만 재시도합니다. 명시적으로 지정한 Bearer 토큰과 OAuth 자격 증명은
헬퍼가 제공한 `Authorization` 헤더보다 우선합니다.
OAuth `403` 응답이 권한 범위 부족을 나타내는 경우에는
헬퍼 갱신이 실행되지 않습니다.

어느 소스에서도 자격 증명을 가져올 수 없으면 Codex는
인증 없이 서버에 연결할 수 있습니다. `codex mcp login <server-name>` 명령어를 별도로 실행해
MCP OAuth 로그인을 시작하세요.

#### 기타 구성 옵션

- `startup_timeout_sec`(선택 사항): 서버 시작 제한 시간(초)입니다. 기본값은 `10`입니다.
- `tool_timeout_sec`(선택 사항): 서버의 도구 실행 제한 시간(초)입니다. 기본값은 `60`입니다.
- `enabled` (선택 사항): 서버를 삭제하지 않고 비활성화하려면 `false`로 설정하세요.
- `required` (선택 사항): 활성화된 이 서버를 초기화할 수 없을 때 시작이 실패하도록 하려면 `true`로 설정하세요.
- `enabled_tools` (선택 사항): 도구 허용 목록입니다.
- `disabled_tools` (선택 사항): 도구 차단 목록입니다(`enabled_tools` 적용 후 처리).
- `default_tools_approval_mode` (선택 사항): 이 서버에서 제공하는
  도구의 기본 승인 방식입니다. 지원되는 값은 `auto`, `prompt`, `writes` 및
`approve`입니다. `writes` 모드에서는 읽기 전용으로 표시되지 않은 도구에 대해 승인을 요청합니다.
- `tools.<tool>.approval_mode` (선택 사항): 도구별 승인 방식을 재정의합니다.
- `tools.<tool>.output_token_limit` (선택 사항): 단일 도구의 출력에 적용할 토큰 예산으로, 양수여야 합니다.
  직렬화를 위한 기본 20% 여유분을 적용하기 전의 값입니다.
  해당 도구의 출력 잘림 기준으로 쓰이는 모델의 기본 토큰 예산을 재정의합니다.

최상위 `mcp_optional_startup_grace_ms` 설정은 Codex가 초기 도구 카탈로그를 구성할 때
필수가 아닌 MCP 서버를 기다리는 시간을 제어합니다.
기본값은 `1000`밀리초입니다. `0`으로 설정하면 대신 각 서버의
`startup_timeout_sec`에 지정된 시간만큼 기다립니다. 필수 서버에는 계속
각 서버의 시작 제한 시간이 적용됩니다.

#### OAuth 클라이언트 등록 및 콜백

인가 서버에서 사전 등록된 OAuth 클라이언트를 요구하는 경우 MCP 서버를 추가할 때
해당 클라이언트 ID를 지정하세요:

```bash
codex mcp add example --url https://mcp.example.com --oauth-client-id my-client

Codex는 공급자에 등록할 전체 콜백 URL을 표시합니다:

```text
OAuth callback URL: http://127.0.0.1/callback

Codex는 이후 로그인에 사용할 수 있도록 `config.toml`에 클라이언트 ID와 함께
콜백을 저장합니다:

```toml
[mcp_servers.example]
url = "https://mcp.example.com"

[mcp_servers.example.oauth]
client_id = "my-client"
callback_url = "http://127.0.0.1/callback"

사전 등록된 클라이언트를 새로 추가한 경우,
인가 서버가
`authorization_response_iss_parameter_supported: true` 값을 명시하고 메타데이터에
`issuer` 값을 제공할 때만 고정 콜백을 사용합니다. 발급자 식별 지원을 명시하지 않으면 Codex는
`http://127.0.0.1/callback/XuuuHAzzHOni`처럼 서버별 콜백 ID를 덧붙입니다. 저장된 콜백이 없는 기존 클라이언트는
콜백 ID별 리디렉션을 계속 사용합니다.

로그인 시 사용할 콜백은 OAuth 구성과
인가 서버 메타데이터에 따라 결정됩니다:

| OAuth 구성                                                | 발급자 식별 지원           | 사용되는 콜백                                                                                                                                      |
| ------------------------------------------------------------------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `callback_url` 설정, `client_id` 미설정                                 | 지원                | 설정된 콜백을 클라이언트 등록에 사용합니다.                                                                                           |
| `callback_url` 설정, `client_id` 미설정                                 | 미지원              | 설정된 콜백에 서버별 콜백 ID를 덧붙여 클라이언트 등록에 사용합니다.                                             |
| `client_id` 및 `callback_url` 설정                                     | 지원                | 설정된 콜백을 재사용하며, 인가 응답에는 일치하는 `iss` 값이 포함되어야 합니다.                                                     |
| `client_id` 및 올바른 콜백 ID로 끝나는 `callback_url` 설정 | 미지원              | 설정된 콜백을 변경 없이 재사용합니다.                                                                                                       |
| `client_id` 및 올바른 콜백 ID가 없는 `callback_url` 설정   | 미지원              | 설정된 콜백은 무시됩니다. Codex는 `mcp_oauth_callback_url` 값에 콜백 ID를 덧붙여 사용하며, 이 값이 설정되지 않았다면 `http://127.0.0.1/callback`에 콜백 ID를 덧붙여 사용합니다. |
| `client_id` 설정, `callback_url` 미설정                    | 지원 여부 무관 | Codex는 전역 콜백 또는 기본 콜백에 서버별 콜백 ID를 덧붙여 사용합니다.                                                           |

대체 콜백을 사용해도 저장된 콜백 URL은 변경되지 않습니다. Codex는 경로와 쿼리 문자열을 포함한
MCP 서버 URL에서 콜백 ID를 생성합니다. 자동 로그인과 명시적으로 시작한 로그인에는
동일한 선택 규칙이 적용됩니다.

사용자 지정 콜백 경로나 원격
Devbox 인그레스 URL이 필요하면 `mcp_oauth_callback_url` 값을 설정하세요. 새로 추가한 사전 등록 클라이언트는
공급자가 발급자 식별을 지원하면 해당 URL을 그대로 사용합니다. 그렇지 않으면
설정된 URL에 서버별 콜백 ID를 덧붙여 사용합니다. 항상
`codex mcp add`에서 표시하는 콜백을 정확히 그대로 등록하세요.

포트가 없는 `http://127.0.0.1` 콜백의 경우 Codex는 표시하고 저장하는
URL에서 리스너 포트를 생략한 뒤, 인가 과정에서 현재 사용 중인 리스너 포트를
삽입합니다. 이 치환은 `localhost`, IPv6 호스트,
HTTPS URL 또는 이미 포트가 포함된 콜백에는 적용되지 않습니다. 인가 서버는
[RFC 8252 7.3절](https://www.rfc-editor.org/rfc/rfc8252#section-7.3)에 따라
가변 루프백 포트를 허용해야 합니다.

고정 전역 리스너 포트를 사용하려면 `mcp_oauth_callback_port` 값을 설정하고,
특정 서버에 다른 값을 적용하려면 `mcp_servers.<server-name>.oauth.callback_port` 값을 설정하세요.
콜백 URL에 포트를 명시해도 리스너가 설정되지는 않습니다. 직접 연결하는
루프백 콜백에는 포트가 없는 `http://127.0.0.1` 주소를 사용하거나
콜백 URL과 리스너에 같은 포트를 명시적으로 설정하세요. 프록시를 거치는 콜백은
외부 URL의 포트를 로컬 리스너 포트와 의도적으로 다르게
설정할 수 있습니다. 로컬 콜백 URL은 로컬 인터페이스에 바인딩되며, 로컬이 아닌 콜백 URL은
`0.0.0.0`에 바인딩됩니다.

Codex는 인가 코드를 교환하기 전에 반환된 `iss` 값을 검증합니다.
`iss` 값이 일치하지 않으면 항상 응답을 거부합니다. 발급자 식별 지원이 명시된 경우에는
`iss` 값이 없어도 응답을 거부합니다. 어느 경우든 코드를 교환하거나
다른 콜백으로 대체하지 않습니다. 콜백 URL 형식이 잘못되었거나 발급자 식별 지원을 명시하면서도
메타데이터에 발급자 정보를 제공하지 않은 경우에도 오류로 중단됩니다.
[사용자 인증](/plugins/build/auth)을 참고하세요.

MCP 서버가 `scopes_supported` 값을 명시하면 Codex는
OAuth 로그인 시 서버가 명시한 스코프를 우선 사용합니다. 그렇지 않으면
`config.toml`에 설정된 스코프를 사용합니다.

#### OAuth 클라이언트 등록

Codex는 [OAuth 클라이언트 ID 메타데이터 문서(CIMD)](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/)와
동적 클라이언트 등록(DCR)을 지원합니다. 기본적으로 Codex는
인가 서버가
`client_id_metadata_document_supported: true` 값을 명시하고, `none` 값을
`token_endpoint_auth_methods_supported`에 포함하며, 콜백이 지원되는
루프백 URL을 사용하는 경우 CIMD를 자동으로 선택합니다. 그렇지 않으면 사용 가능한 경우 DCR을 사용합니다. OAuth 클라이언트
ID가 설정되어 있으면 해당 ID를 항상 우선 사용하고 클라이언트 등록을 건너뜁니다.

CIMD를 사용할 때 Codex는 ChatGPT에서 호스팅하는 MCP 서버별
메타데이터 문서를 사용합니다:

```text
https://chatgpt.com/oauth/codex/<callback_id>/client.json

Codex는 MCP 서버 URL에서 `<callback_id>`를 생성하고 이를
루프백 리디렉션 URI에 포함합니다. 예를 들면
`http://127.0.0.1:<port>/callback/<callback_id>`입니다. 메타데이터 문서에는
해당 루프백 URI가 포트 없이 등록됩니다. 인가 서버는
로그인 시 선택한 포트를 허용하되 호스트와 경로가 정확히 일치하는지 확인해야 합니다. 이는
[RFC 8252](https://www.rfc-editor.org/rfc/rfc8252.html#section-7.3)의 요구 사항입니다. 사용자 지정
콜백 호스트, 경로 또는 쿼리 매개변수를 사용하려면 DCR이나 설정된 OAuth
클라이언트 ID가 필요합니다.

고정된 공유 CIMD 문서 지원 기능은 현재 개발 중이며 곧 제공될 예정입니다:

```text
https://chatgpt.com/oauth/codex/client.json

인가 서버가
`authorization_response_iss_parameter_supported: true` 값을 명시하고,
메타데이터에 유효한 `issuer` 값을 제공하며,
인가 응답에 일치하는 `iss` 값을 포함하면 Codex는
공유 `/callback` 경로를 사용하는 고정 문서를 사용할 예정입니다. 발급자에 바인딩된 응답을 제공하지 않는 서버는
콜백별 문서를 계속 사용하게 됩니다.

CLI 로그인 한 번에 사용할 등록 방식을 선택하려면
`--oauth-client-registration` 옵션을 사용하세요:

```bash
codex mcp login <server-name> --oauth-client-registration cimd
codex mcp login <server-name> --oauth-client-registration dcr

기본값은 `auto`입니다. 선택한 등록 방식은 현재 로그인에만 적용되며
`config.toml`에 저장되지 않습니다.

#### config.toml 예시

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
env_vars = ["LOCAL_TOKEN"]

[mcp_servers.context7.env]
MY_ENV_VAR = "MY_ENV_VALUE"

```toml
# Optional MCP OAuth callback overrides (used by `codex mcp login`)
mcp_oauth_callback_port = 5555
mcp_oauth_callback_url = "https://devbox.example.internal/callback"

```toml
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
http_headers = { "X-Figma-Region" = "us-east-1" }

```toml
[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
enabled_tools = ["open", "screenshot"]
disabled_tools = ["screenshot"] # applied after enabled_tools
default_tools_approval_mode = "prompt"
startup_timeout_sec = 20
tool_timeout_sec = 45
enabled = true

[mcp_servers.chrome_devtools.tools.open]
approval_mode = "approve"
output_token_limit = 30000

### 플러그인에서 제공하는 MCP 서버

설치된 플러그인은 자체 매니페스트에 MCP 서버를 포함할 수 있습니다.
이 서버는 플러그인에서 실행되므로 사용자 설정에서는 서버의
트랜스포트 명령어를 지정하지 않습니다. 다만 사용자 설정의
`plugins.<plugin>.mcp_servers.<server>`에서 활성화 여부와 도구 정책은 제어할 수 있습니다.

```toml
[plugins."sample@test".mcp_servers.sample]
enabled = true
default_tools_approval_mode = "prompt"
enabled_tools = ["read", "search"]

[plugins."sample@test".mcp_servers.sample.tools.search]
approval_mode = "approve"

플러그인에서 제공하는 HTTP MCP 서버는 `.mcp.json`에 OAuth 설정도 선언할 수 있습니다.
플러그인 매니페스트는 camelCase 형식의 필드 이름인 `clientId`, `callbackUrl`,
`callbackPort`를 사용합니다:

```json
{
  "mcpServers": {
    "sample": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "clientId": "my-pre-registered-client",
        "callbackUrl": "http://127.0.0.1/callback/registered"
      }
    }
  }
}

플러그인에서 제공하는 MCP 서버에도 다른 MCP 서버와 동일한
콜백 선택 규칙이 적용됩니다. 플러그인이 `clientId` 값을 제공하고, 공급자가
발급자에 바인딩된 콜백을 지원하지 않으며, `callbackUrl`에 서버별 콜백 ID가
없으면 Codex는 로그인 시 해당 URL을 무시합니다. 대신 `mcp_oauth_callback_url` 값을 사용하고,
이 값이 설정되지 않았다면 `http://127.0.0.1/callback` 주소를 사용하며, 두 경우 모두 콜백 ID를 덧붙입니다.
설정된 `callbackUrl` 값은 변경되지 않습니다.

플러그인의 `oauth.callbackPort` 설정은 전역
`mcp_oauth_callback_port` 설정보다 우선합니다. 둘 다 설정되지 않으면 Codex는 임시 포트를 선택합니다.
`callbackUrl`에 포함된 포트로 리스너 포트가 결정되지는 않습니다. 고정 포트로 직접 연결하는
루프백 콜백의 경우 두 값을 동일하게 설정하세요:

```json
{
  "callbackUrl": "http://127.0.0.1:4321/callback/registered",
  "callbackPort": 4321
}

원격 인그레스나 다른 프록시를 사용하는 경우, 프록시가 설정된 리스너로 요청을 전달한다면
콜백 URL의 포트와 로컬 리스너 포트를
의도적으로 다르게 설정할 수 있습니다.

## 유용한 MCP 서버 예시

MCP 서버 목록은 계속 늘어나고 있습니다. 대표적인 서버는 다음과 같습니다:

- [OpenAI 문서 MCP](/learn/docs-mcp): OpenAI 개발자 문서를 검색하고 읽습니다.
- [Context7](https://github.com/upstash/context7): 최신 개발자 문서에 연결합니다.
- Figma [로컬](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/) 및 [원격](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/): Figma 디자인에 액세스합니다.
- [Playwright](https://www.npmjs.com/package/@playwright/mcp): Playwright를 사용해 브라우저를 제어하고 검사합니다.
- [Chrome 개발자 도구](https://github.com/ChromeDevTools/chrome-devtools-mcp/): Chrome을 제어하고 검사합니다.
- [Sentry](https://docs.sentry.io/product/sentry-mcp/#codex): Sentry 로그에 액세스합니다.
- [GitHub](https://github.com/github/github-mcp-server): `git`이 지원하는 범위를 넘어 GitHub를 관리합니다(예: Pull Request 및 이슈).

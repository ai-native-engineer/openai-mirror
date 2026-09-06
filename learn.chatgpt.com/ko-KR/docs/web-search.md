<!-- source: https://learn.chatgpt.com/ko-KR/docs/web-search -->

ChatGPT에는 자체 웹 검색 도구가 포함되어 있습니다. 모든 웹 검색 결과를
신뢰할 수 없는 입력으로 취급하세요.

ChatGPT 데스크톱 앱의 채팅에서 최신 정보를 요청하세요. ChatGPT는
검색 활동을 다른 도구 호출과 함께 대화 기록에 남깁니다.

ChatGPT Web에서 최신 정보나 출처를 요청하세요. ChatGPT가 웹 검색을 사용하면 검색 결과와
인용이 채팅에 표시됩니다. 워크스페이스
설정에서 검색 사용 가능 여부를 제한할 수 있습니다.

CLI에서 한 번의 실행으로 실시간 결과를 가져오려면 `--search`를 전달하세요:

```bash
codex --search "Summarize the latest release notes for this dependency"

검색 활동은 대화형 트랜스크립트와
`codex exec --json` 출력에서 `web_search` 항목으로 표시됩니다.

IDE 확장에서는 편집기에서 작업하는 동안 Codex에 검색을 요청하세요. 이
확장은 연결된 Codex 호스트의 검색 모드를 사용합니다. 검색 활동은
채팅 기록에 표시됩니다.

## 로컬 웹 검색 구성

로컬 Codex 채팅에서는 기본적으로 캐시 검색이 활성화됩니다. 캐시 모드에서는
임의의 페이지를 실시간으로 가져오는 대신 OpenAI가 관리하는 인덱스를 사용하므로
프롬프트 인젝션 위험을 줄일 수 있지만 완전히 없애지는 못합니다.

웹 검색은 호스팅되는 도구이며, 샌드박스에서 실행되는 로컬 명령어의 네트워크 기능과는 별개입니다.
권한 프로필의 네트워크 프록시나 도메인 허용 목록을 사용하지 않으며,
명령어의 네트워크 액세스가 비활성화된 경우에도 계속 사용할 수 있습니다. 필요에 따라
`web_search`, `tools.web_search.allowed_domains`, 관리형
`allowed_web_search_modes` 설정으로 웹 검색을 구성하세요. 검색 도메인 필터는
로컬 명령어 트래픽, 앱, 커넥터 또는 MCP 서버를 제한하지 않습니다.

최신 정보가 필요한 작업에는 실시간 검색을 사용하세요. `config.toml`에서
`web_search = "live"`로 설정하세요. `web_search = "disabled"`로 설정하면
도구가 꺼집니다. `"indexed"` 모드에서는 검색 인덱스가 요청을 허용한 경우에만
외부 웹에 액세스할 수 있습니다. Codex가 전체 권한으로 실행되면 웹 검색은
기본적으로 실시간 결과를 사용합니다. 구성 파일의 위치와 우선순위는 [기본 구성](/ko-KR/codex/config-file/config-basic)을
참조하세요.

### 사용자 지정 모델 제공업체로 검색

사용자 지정 모델 제공업체는 호환되는 검색 엔드포인트를 지원하는 경우 독립형 웹 검색도
지원하도록 설정할 수 있습니다:

```toml
model_provider = "custom"
web_search = "live"

[model_providers.custom]
name = "Custom Responses provider"
base_url = "https://example.com/v1"
env_key = "CUSTOM_RESPONSES_API_KEY"
supports_standalone_web_search = true

사용자 지정 제공업체의 기본 설정은 `supports_standalone_web_search = false`입니다.
독립형 웹 검색은 아직 개발 중이며 기본적으로 꺼져 있습니다.
이 제공업체 기능을 설정하는 것만으로는 독립형 웹 검색이 활성화되지 않습니다. 제공업체와
선택한 모델, 런타임도 모두 독립형 검색을 지원해야 합니다. 워크스페이스 제한과
관리형 검색 제한도 계속 적용됩니다.

Codex 클라우드 환경에 적용되는 네트워크 경계에 관한 내용은 [인터넷
액세스](/ko-KR/codex/cloud/internet-access)를 참조하세요.

<!-- source: https://learn.chatgpt.com/ko-KR/docs/agent-approvals-security -->

Codex는 코드와 데이터를 보호하고 오용 위험을 줄이는 데 도움이 됩니다.

  이 페이지에서는 샌드박스, 승인,
  네트워크 액세스 등 Codex를 안전하게 운영하는 방법을 설명합니다. 연결된 GitHub 레포지토리를
  검사하는 제품인 Codex Security를 찾고 있다면 [Codex Security](/ko-KR/codex/security)를 참조하세요.

기본적으로 에이전트는 네트워크 액세스가 꺼진 상태로 실행됩니다. 로컬에서 Codex는 OS가 강제하는 샌드박스를 사용해 접근 범위를 제한하며, 이 범위는 일반적으로 현재 워크스페이스입니다. 또한 승인 정책으로 작업을 실행하기 전에 멈추고 사용자에게 승인을 요청해야 하는 시점을 제어합니다.

ChatGPT 데스크톱 앱,
Codex CLI, IDE 확장에서 샌드박스가 작동하는 방식은 [샌드박스](/ko-KR/codex/sandboxing)에서 개괄적으로 설명합니다.
엔터프라이즈 보안에 대한 폭넓은 개요는 [Codex 보안 백서](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click)를 참조하세요.

## 샌드박스 및 승인

Codex의 보안 제어는 서로 연동되는 두 계층으로 구성됩니다:

- **샌드박스 모드**: Codex가 모델이 생성한 명령어를 실행할 때 기술적으로 수행할 수 있는 작업을 결정합니다. 예를 들어 파일을 쓸 수 있는 위치와 네트워크에 액세스할 수 있는지를 제어합니다.
- **승인 정책**: Codex가 작업을 실행하기 전에 사용자에게 승인을 요청해야 하는 시점을 결정합니다. 예를 들어 샌드박스를 벗어나거나 네트워크를 사용하거나 신뢰하는 명령어 목록에 없는 명령어를 실행하는 경우입니다.

Codex는 실행 위치에 따라 서로 다른 샌드박스 모드를 사용합니다:

- **Codex 클라우드**: OpenAI가 관리하는 격리된 컨테이너에서 실행되므로 호스트 시스템이나 관련 없는 데이터에 접근할 수 없습니다. 런타임은 두 단계로 구성됩니다. 설정 단계는 에이전트 단계 전에 실행되며, 지정된 종속성을 설치하기 위해 네트워크에 액세스할 수 있습니다. 이어지는 에이전트 단계는 해당 환경의 인터넷 액세스를 활성화하지 않으면 기본적으로 오프라인으로 실행됩니다. 클라우드 환경에 구성된 시크릿은 설정 단계에서만 사용할 수 있으며 에이전트 단계가 시작되기 전에 제거됩니다.
- **Codex CLI / IDE 확장**: OS 수준의 메커니즘이 샌드박스 정책을 강제합니다. 기본적으로 네트워크 액세스가 차단되며 쓰기 권한은 활성 워크스페이스로 제한됩니다. 허용 가능한 위험 수준에 따라 샌드박스, 승인 정책, 네트워크 설정을 구성할 수 있습니다.

`Auto` 프리셋(예: `--sandbox workspace-write --ask-for-approval on-request`)에서는 Codex가 작업 디렉터리에서 파일을 읽고 수정하며 명령어를 자동으로 실행할 수 있습니다.

Codex는 워크스페이스 외부의 파일을 수정하거나 네트워크 액세스가 필요한 명령어를 실행하려면 승인을 요청합니다. 변경 없이 채팅하거나 계획을 세우려면 `/permissions` 명령어를 사용해 `read-only` 모드로 전환하세요.

Codex는 셸 명령어나 파일 변경이 아니더라도 사이드 이펙트가 명시된 앱(커넥터) 도구 호출에 대해 승인을 요청할 수 있습니다. 도구에 파괴적 작업을 나타내는 어노테이션이 있으면 파괴적인 앱/MCP 도구 호출에는 항상 승인이 필요합니다. 단, 도구에 읽기 어노테이션도 있으면 읽기 어노테이션이 우선합니다.

## 안전 모니터링 및 일시 중지된 작업

GPT-6 Astra는 Codex와 ChatGPT Work에서 안전 모니터링을 제공합니다. 모니터링은
비동기적으로 실행되며, 잠재적으로 안전하지 않은 모델 동작을 감지하면 작업을 일시 중지할 수 있습니다.
일시 중지를 유발한 동작이 수행된 뒤에 작업이 중지될 수도 있습니다. 모니터링은
샌드박스, 권한, 결과 검토를 대체하지 않습니다.

작업이 일시 중지되면 안내를 읽고, 감지 결과가 제공되는 경우 이를 검토하세요.
작업을 안전하게 계속할 수 있는지 확인한 후에만 재개하세요. 안내에 작업이 종료되었다고
표시되거나 재개 옵션이 없다면 해당
인터페이스에서는 작업을 재개할 수 없습니다.

| 사용 환경 및 데이터 제어                                                                               | 감지 결과 및 작업 재개                                       |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| 감지 결과 확인 및 작업 재개 플로우를 지원하며, 여기에 나열된 데이터 제어가 적용되지 않는 Codex 및 ChatGPT Work 클라이언트 | 작업을 재개하기 전에 감지 결과를 검토하세요.                      |
| Codex CLI 및 모바일                                                                                    | 전체 감지 결과 확인 및 작업 재개 기능을 사용할 수 없습니다. 작업이 종료됩니다. |
| 데이터 비보관, 수정된 악용 모니터링 또는 미국 외 지역의 데이터 저장 레지던시                        | 전체 감지 결과 확인 및 작업 재개 기능을 사용할 수 없습니다. 작업이 종료됩니다. |

안전 모니터링은 작업 중 모델의 동작을 평가합니다.
[자동 승인 검토](/ko-KR/codex/sandboxing/auto-review)는 이미 승인이 필요한 개별 동작을
실행 전에 평가합니다. 자동 승인 검토에서 승인된 동작이 포함된 작업도
이후 모니터링에 의해 일시 중지될 수 있습니다.

## 네트워크 액세스 

Codex 클라우드에서 전체 인터넷 액세스 또는 도메인 허용 목록을 활성화하려면 [에이전트 인터넷 액세스](/ko-KR/codex/cloud/internet-access)를 참조하세요.

ChatGPT 데스크톱 앱, Codex CLI, IDE 확장의 기본 `workspace-write` 샌드박스 모드에서는 구성에서 활성화하지 않는 한 네트워크 액세스가 꺼진 상태로 유지됩니다:

```toml
[sandbox_workspace_write]
network_access = true

### 네트워크 격리

네트워크 액세스는 스크립트,
프로그램, 명령어가 생성한 하위 프로세스에 적용되는 대상 규칙으로 제어됩니다. 명령어의 네트워크 액세스가
이미 활성화되어 있다면 `network_proxy` 기능을 켜서 해당 트래픽을
구성한 네트워크 정책에 따라 제한하세요. 도메인 규칙을 추가하는 것만으로는
프록시가 활성화되지 않습니다.

```toml
[features.network_proxy]
enabled = true
domains = { "api.openai.com" = "allow", "example.com" = "deny" }

일회성 CLI 세션에서 기능을 켜거나 끄기만 할 때는 불리언 축약형을 사용하고,
정책 옵션도 설정할 때는 테이블 형식을 사용하세요:

```bash
codex \
  -c 'features.network_proxy=true' \
  -c 'sandbox_workspace_write.network_access=true'

codex \
  -c 'features.network_proxy.enabled=true' \
  -c 'features.network_proxy.domains={ "api.openai.com" = "allow", "example.com" = "deny" }' \
  -c 'sandbox_workspace_write.network_access=true'

이 기능은 이미 활성화된 네트워크 액세스를 제어하는 방식을 변경하며,
자체적으로 네트워크 액세스를 허용하지는 않습니다. 명령어의 네트워크 액세스 허용 여부는 `sandbox_workspace_write.network_access` 설정을
`workspace-write` 구성과 함께 사용해 결정하세요:

- 네트워크 꺼짐 + `network_proxy` 켜짐: 네트워크는 계속 꺼져 있으며 이 기능은 아무런 영향을 주지 않습니다.
- 네트워크 켜짐 + `network_proxy` 꺼짐: 네트워크는 계속 켜져 있으며
  외부로의 직접 연결이 제한 없이 허용됩니다.
- 네트워크 켜짐 + `network_proxy` 켜짐: 네트워크는 계속 켜져 있으며 아웃바운드 트래픽은
  구성된 네트워크 정책에 따라 제한됩니다.

프록시 기능은 [권한 프로필](/ko-KR/codex/permissions#network-permissions)에도 적용됩니다.
프로필의 `network.enabled = true` 설정은 명령어의 네트워크 액세스를 허용하고,
`features.network_proxy = true` 설정은 해당 프로필에 지정된
도메인 규칙의 적용을 활성화합니다:

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit]
extends = ":workspace"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"

이 예시에서 프록시 기능을 생략하면 명령어가 네트워크에 직접
액세스하며 `api.openai.com` 허용 규칙은 접속 대상을 제한하지 않습니다.

관리자가 관리하는 `experimental_network` 요구 사항은 사용자가 기능을 켜고 끄는
설정과 별개입니다. 이 요구 사항으로 `features.network_proxy` 없이도
샌드박스 네트워킹을 구성하고 시작할 수 있지만, 현재
샌드박스에서 네트워크 액세스가 꺼져 있다면 이를 켜지는 않습니다. 관리자 측 `requirements.toml` 형식은
[관리형 구성](/ko-KR/codex/enterprise/managed-configuration#configure-network-access-requirements)을 참조하세요.

#### 네트워크 정책

도메인 규칙은 허용 목록을 기반으로 적용됩니다:

- 정확히 지정한 호스트 규칙은 해당 호스트에만 적용됩니다.
- `*.example.com` 패턴은 `api.example.com` 같은 하위 도메인과 일치하지만
`example.com`에는 일치하지 않습니다.
- `**.example.com` 패턴은 에이펙스 도메인과 하위 도메인 모두와 일치합니다.
- 전역 `*` 허용 규칙은 거부되지 않은 모든 공개 호스트와 일치합니다. `*` 사용은
  광범위한 네트워크 액세스를 허용하는 것으로 간주하고, 가능하면 범위를 한정한 규칙을 사용하세요.
- `deny` 규칙은 항상 `allow` 규칙보다 우선하며, 전역 `*` 패턴은 허용 규칙에서만 유효합니다.

#### 로컬 및 프라이빗 대상

기본적으로 `allow_local_binding = false` 설정은 루프백, 링크 로컬,
프라이빗 대상을 차단합니다:

- 특정 예외: 명령어에서 로컬 대상 하나에 액세스해야 한다면 정확한 로컬 IP 리터럴이나 `localhost`에 대한 허용 규칙을
  추가하세요.
- 광범위한 액세스: 의도적으로 로컬/프라이빗 대상에 대한 접근 범위를
  넓히려는 경우에만 `allow_local_binding = true` 설정을 사용하세요.
- 와일드카드: 와일드카드 규칙은 명시적인 로컬 예외로 간주되지 않습니다.
- 주소 확인 결과: 로컬/프라이빗 IP로 확인되는 호스트 이름은
허용 목록과 일치하더라도 계속 차단됩니다.

#### DNS 리바인딩 보호

호스트 이름을 허용하기 전에 Codex는 가능한 범위에서 DNS 및 IP
분류 검사를 수행합니다:

- 조회가 실패하거나 시간이 초과되면 차단됩니다.
- 공개 주소가 아닌 주소로 확인되는 호스트 이름은 차단됩니다.
- 이 검사는 DNS 리바인딩 위험을 줄이지만 완전히 없애지는 못합니다.
리바인딩을 완전히 방지하려면 확인된 IP 주소를 전송 계층까지
고정해야 합니다.

악성 DNS까지 위협 범위에 포함된다면 하위 계층에서도 아웃바운드 트래픽 제어를 적용하세요.

#### 위험한 설정

다음 두 설정은 신뢰 경계를 의도적으로 확장합니다:

- `dangerously_allow_non_loopback_proxy = true` 설정은 프록시 리스너를
  루프백 범위 밖으로 노출할 수 있습니다.
- `dangerously_allow_all_unix_sockets = true` 설정은 Unix 소켓 허용 목록을 우회합니다.

엄격하게 통제되는 환경에서만 사용하세요. Unix 소켓 프록시가 활성화되면
루프백 외 주소에 바인딩하도록 요청하더라도 리스너는 루프백으로만 제한됩니다.
따라서 샌드박스 네트워킹이 로컬 데몬에 원격으로 접근하는 통로가 되지 않습니다.

`network_proxy`는 기본적으로 비활성화되어 있습니다. 활성화하면 다음과 같이 동작합니다:

| 설정                                | 기본값 | 동작                                                                                                                                                                              |
| -------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enabled`                              | `false` | 명령어의 네트워크 액세스가 이미 활성화된 경우에만 샌드박스 네트워킹을 시작합니다.                                                                                                           |
| `domains`                              | 설정되지 않음   | 허용 목록 방식으로 동작하므로 `allow` 규칙을 추가하기 전에는 어떤 외부 대상에도 액세스할 수 없습니다. 정확한 호스트, 범위가 제한된 와일드카드, 전역 `*` 허용 규칙을 지원하며, `deny`가 항상 우선합니다. |
| `unix_sockets`                         | 설정되지 않음   | 명시적인 `allow` 규칙을 추가하기 전에는 어떤 Unix 소켓 대상에도 액세스할 수 없습니다.                                                                                                         |
| `allow_local_binding`                  | `false` | 정확한 로컬 IP 리터럴 또는 `localhost` 허용 규칙을 추가하거나 더 넓은 범위의 로컬/사설 네트워크 액세스를 명시적으로 허용하지 않는 한 로컬 및 사설 네트워크 대상을 차단합니다.                |
| `enable_socks5`                        | `true`  | 정책에서 허용하는 경우 SOCKS5 기능을 제공합니다.                                                                                                                                         |
| `enable_socks5_udp`                    | `true`  | SOCKS5를 사용할 수 있을 때 SOCKS5를 통한 UDP 통신을 허용합니다.                                                                                                                                      |
| `allow_upstream_proxy`                 | `true`  | 샌드박스 네트워킹에서 환경에 설정된 업스트림 프록시를 사용할 수 있도록 합니다.                                                                                                               |
| `dangerously_allow_non_loopback_proxy` | `false` | 의도적으로 로컬호스트 외부에 노출하지 않는 한 리스너 엔드포인트를 루프백으로 제한합니다.                                                                                            |
| `dangerously_allow_all_unix_sockets`   | `false` | 의도적으로 보호를 우회하지 않는 한 Unix 소켓 액세스를 허용 목록 기반으로 유지합니다.                                                                                              |

### 명령어 네트워크 프록시 외부의 트래픽

네트워크 프록시는 로컬 명령어 샌드박스에서 실행되는 스크립트, 프로그램,
하위 프로세스를 필터링합니다. 웹 검색, 앱 또는 커넥터 도구 호출,
MCP 서버 연결, 브라우저 또는 컴퓨터 사용 활동, Codex 클라우드 작업,
클라이언트의 모델 및 인증 요청은 필터링하지 않습니다. 이러한 기능에는
별도의 서비스 연결, 기능 설정, 워크스페이스 정책 또는
환경 제어가 적용됩니다.

브라우저 도구는 오리진에 액세스하기 전에 관리형 네트워크 차단 규칙과 배타적 허용 목록을
별도로 확인합니다. 브라우저 오리진 정책으로 사이트 액세스,
업로드, 다운로드, 개발자 도구를 추가로 제한할 수 있습니다.
[관리형 브라우저 제어](/ko-KR/codex/enterprise/managed-configuration#control-browser-and-computer-use)를 참조하세요.

관리 대상 사용자에게는 명령어 네트워크 정책을
`allowed_web_search_modes`, 승인된 `mcp_servers`, 앱, 플러그인, 브라우저 또는 컴퓨터 사용에 적용되는
기능 요구 사항 등의 제어 수단과 함께 적용하세요. 자세한 내용은
[관리형 구성](/ko-KR/codex/enterprise/managed-configuration)을 참조하세요.

실행되는 명령어에 전체 네트워크 액세스 권한을 부여하지 않고도 [웹 검색 도구](https://platform.openai.com/docs/guides/tools-web-search)를 제어할 수 있습니다. Codex는 기본적으로 웹 검색 캐시를 사용해 결과에 액세스합니다. 이 캐시는 OpenAI가 관리하는 웹 검색 결과 인덱스이므로 캐시 모드에서는 실시간 페이지를 가져오는 대신 미리 인덱싱된 결과를 반환합니다. 따라서 임의의 실시간 콘텐츠로 인한 프롬프트 인젝션에 노출될 위험은 줄어들지만, 웹 검색 결과는 여전히 신뢰할 수 없는 정보로 취급해야 합니다. `--yolo` 또는 다른 [전체 권한 샌드박스 설정](#common-sandbox-and-approval-combinations)을 사용하는 경우 웹 검색은 기본적으로 실시간 결과를 반환합니다. 실시간 탐색을 허용하려면 `--search`를 사용하거나 `web_search = "live"`로 설정하고, 도구를 비활성화하려면 `"disabled"`로 설정하세요:

```toml
web_search = "cached"  # default
# web_search = "disabled"
# web_search = "live"  # same as --search

외부 웹 액세스를 검색 인덱스를 통해 제한해야 하는 경우
`web_search = "indexed"`로 설정하세요. Codex에서 네트워크 액세스나 웹 검색을 활성화할 때는 주의하세요.
프롬프트 인젝션으로 인해 에이전트가 신뢰할 수 없는 지침을 가져와 따를 수 있습니다.

## 기본값 및 권장 사항

- 시작 시 Codex는 폴더의 버전 관리 여부를 확인하고 다음 설정을 권장합니다:
  - 버전 관리되는 폴더: `Auto`(워크스페이스 쓰기 + 요청 시 승인)
  - 버전 관리되지 않는 폴더: `read-only`
- 설정에 따라 Codex는 온보딩 프롬프트나 `/permissions` 등을 통해 작업 디렉터리를 명시적으로 신뢰할 때까지 `read-only` 모드로 시작할 수도 있습니다.
- 워크스페이스에는 현재 디렉터리와 `/tmp` 같은 임시 디렉터리가 포함됩니다. 워크스페이스에 포함된 디렉터리를 확인하려면 `/status` 명령어를 사용하세요.
- 기본값을 적용하려면 `codex` 명령어를 실행하세요.
- 다음과 같이 명시적으로 설정할 수도 있습니다:
  - `codex --sandbox workspace-write --ask-for-approval on-request`
  - `codex --sandbox read-only --ask-for-approval on-request`

### 쓰기 가능한 루트의 보호된 경로

기본 `workspace-write` 샌드박스 정책에서도 쓰기 가능한 루트에는 보호된 경로가 포함됩니다:

- `<writable_root>/.git`은 디렉터리인지 파일인지와 관계없이 읽기 전용으로 보호됩니다.
- `<writable_root>/.git`이 포인터 파일(`gitdir: ...`)인 경우, 해당 포인터가 가리키는 Git 디렉터리 경로도 읽기 전용으로 보호됩니다.
- `<writable_root>/.agents` 경로가 디렉터리로 존재하면 읽기 전용으로 보호됩니다.
- `<writable_root>/.codex` 경로가 디렉터리로 존재하면 읽기 전용으로 보호됩니다.
- 보호는 재귀적으로 적용되므로 해당 경로 아래의 모든 항목이 읽기 전용입니다.

### 승인 프롬프트 없이 실행

`--ask-for-approval never` 또는 축약형 `-a never`를 사용하면 승인 프롬프트를 비활성화할 수 있습니다.

이 옵션은 모든 `--sandbox` 모드에서 사용할 수 있으므로 Codex의 자율성 수준은 계속 제어할 수 있습니다. Codex는 설정한 제약 조건 안에서 최대한 작업을 수행합니다.

Codex가 승인 프롬프트 없이 파일을 읽고 수정하며 네트워크에 액세스하면서 명령어를 실행하도록 하려면 `--sandbox danger-full-access`(또는 `--dangerously-bypass-approvals-and-sandbox` 플래그)을 사용하세요. 사용하기 전에 신중히 판단하세요.

절충안으로 `approval_policy = { granular = { ... } }` 설정을 사용하면 특정 승인 프롬프트 범주는 대화형으로 유지하고 나머지는 자동으로 거부할 수 있습니다. 이 세분화된 정책은 샌드박스 승인, execpolicy-rule 프롬프트, MCP 프롬프트, `request_permissions` 프롬프트, 스킬 스크립트 승인에 적용됩니다.

### 승인 요청 자동 검토

기본적으로 승인 요청은 사용자에게 전달됩니다:

```toml
approvals_reviewer = "user"

승인 요청 자동 검토는
`approval_policy = "on-request"` 설정이나 세분화된 승인 정책처럼 승인이 대화형으로 처리되는 경우에 적용됩니다.
`approvals_reviewer = "auto_review"`로 설정하면 검토 대상 승인 요청이
Codex의 실행 전에 검토 에이전트를 거치도록 할 수 있습니다:

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"

검토자의 전체 수명 주기, 트리거 조건, 구성 우선순위 및
실패 시 동작은
[자동 검토](/ko-KR/codex/sandboxing/auto-review)를 참조하세요.

검토자는 샌드박스 권한 상승, 차단된 네트워크 요청,
`request_permissions` 프롬프트 또는
사이드 이펙트가 있는 앱 및 MCP 도구 호출처럼 이미 승인이 필요한 작업만 평가합니다. 샌드박스 내부에서 처리되는 작업은
추가 검토 없이 계속 진행됩니다.

검토자 정책은 데이터 유출, 자격 증명 탐색, 지속적인 보안 약화, 파괴적인 작업을
확인합니다. 위험도가 낮거나 중간인 작업은 정책에서 허용하면 진행할 수 있습니다.
치명적인 위험이 있는 작업은 거부됩니다. 위험도가 높은 작업은 사용자의 충분한
권한 부여가 있어야 하며 일치하는 거부 규칙이 없어야 합니다. 프롬프트 생성,
검토 세션 또는 파싱에 실패하면 작업이 차단됩니다. 시간 초과는 별도로
표시되지만, 이 경우에도 작업은 실행되지 않습니다.

[기본 검토자 정책](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md)은
오픈 소스 Codex 레포지토리에서 확인할 수 있습니다. 엔터프라이즈는 이 정책의 테넌트별 섹션을
관리형 요구 사항의 `guardian_policy_config` 설정으로 대체할 수 있습니다.
로컬 `[auto_review].policy` 텍스트도 지원되지만, 관리형 요구 사항이
우선합니다. 자세한 설정 방법은
[관리형 구성](/ko-KR/codex/enterprise/managed-configuration#configure-automatic-review-policy)을 참조하세요.

ChatGPT 데스크톱 앱에서는 이러한 검토가 검토 중, 승인됨, 거부됨, 중단됨,
시간 초과 등의 상태가 표시된 자동 검토 항목으로 나타납니다.
검토 대상 요청의 위험 수준과 사용자 권한 부여에 대한
평가도 함께 표시될 수 있습니다.

자동 검토는 추가 모델 호출을 사용하므로 Codex 사용량이 증가할 수 있습니다. 관리자는
`allowed_approvals_reviewers` 설정으로 이를 제한할 수 있습니다.

### 일반적인 샌드박스 및 승인 조합

| 목적                                                            | 플래그 / 구성                                                                                                                      | 효과                                                                                                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| 자동(프리셋)                                                     | _플래그 불필요_ 또는 `--sandbox workspace-write --ask-for-approval on-request`                                                      | Codex는 워크스페이스에서 파일을 읽고 수정하며 명령어를 실행할 수 있습니다. 워크스페이스 외부를 수정하거나 네트워크에 액세스하려면 승인이 필요합니다. |
| 안전한 읽기 전용 탐색                                           | `--sandbox read-only --ask-for-approval on-request`                                                                                 | Codex는 파일을 읽고 질문에 답할 수 있습니다. 파일 수정, 명령어 실행 또는 네트워크 액세스에는 승인이 필요합니다.                               |
| 비대화형 읽기 전용(CI)                                    | `--sandbox read-only --ask-for-approval never`                                                                                      | Codex는 파일만 읽을 수 있으며 승인을 요청하지 않습니다.                                                                                              |
| 자동으로 수정하되 신뢰할 수 없는 명령어를 실행할 때는 승인 요청 | `--sandbox workspace-write --ask-for-approval untrusted`                                                                            | Codex는 파일을 읽고 수정할 수 있지만 신뢰할 수 없는 명령어를 실행하기 전에 승인을 요청합니다.                                                           |
| 자동 검토 모드                                                  | `--sandbox workspace-write --ask-for-approval on-request -c approvals_reviewer=auto_review` 또는 `approvals_reviewer = "auto_review"` | 표준 on-request 모드와 샌드박스 경계는 같지만, 대상 승인 요청을 사용자에게 표시하는 대신 자동 검토 기능이 검토합니다.  |
| 위험한 전체 권한                                             | `--dangerously-bypass-approvals-and-sandbox`(별칭: `--yolo`)                                                                      |  샌드박스 없음, 승인 없음 _(권장하지 않음)_                                                                               |

비대화형 실행에는 `codex exec --sandbox workspace-write` 명령어를 사용하세요. Codex는 이전 `codex exec --full-auto` 호출 방식을 사용 중단 예정(deprecated)인 호환성 경로로 유지하며 경고를 출력합니다.

`--ask-for-approval untrusted` 옵션을 사용하면 Codex는 안전하다고 알려진 읽기 작업만 자동으로 실행합니다. 상태를 변경하거나 외부 실행 경로를 호출할 수 있는 명령어(예: 파괴적인 Git 작업이나 Git 출력/구성 재정의 플래그)에는 승인이 필요합니다.

#### `config.toml`에서 구성하기

전반적인 구성 워크플로우는 [기본 구성](/ko-KR/codex/config-file/config-basic), [고급 구성](/ko-KR/codex/config-file/config-advanced#approval-policies-and-sandbox-modes), [구성 참조 자료](/ko-KR/codex/config-file/config-reference)를 확인하세요.

```toml
# Always ask for approval mode
approval_policy = "untrusted"
sandbox_mode    = "read-only"
allow_login_shell = false # optional hardening: disallow login shells for shell-based tools

# Optional: Allow network in workspace-write mode
[sandbox_workspace_write]
network_access = true

# Optional: granular approval policy
# approval_policy = { granular = {
#   sandbox_approval = true,
#   rules = true,
#   mcp_elicitations = true,
#   request_permissions = false,
#   skill_approval = false
# } }

프리셋을 [프로필 파일](/ko-KR/codex/config-file/config-advanced#profiles)로 저장한 다음 `codex --profile profile-name` 명령어로 선택할 수도 있습니다:

```toml
# ~/.codex/full_auto.config.toml
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

```toml
# ~/.codex/readonly_quiet.config.toml
approval_policy = "never"
sandbox_mode    = "read-only"

### 로컬에서 샌드박스 테스트하기

Codex 샌드박스에서 명령어가 어떻게 실행되는지 확인하려면 다음 Codex CLI 명령어를 사용하세요:

```bash
# macOS
codex sandbox macos [--permissions-profile <name>] [--log-denials] [COMMAND]...
# Linux
codex sandbox linux [--permissions-profile <name>] [COMMAND]...
# Windows
codex sandbox windows [--permissions-profile <name>] [COMMAND]...

`sandbox` 명령어는 `codex debug`로도 실행할 수 있으며, 플랫폼 도우미에도 별칭이 있습니다(예: `codex sandbox seatbelt`, `codex sandbox landlock`).

## OS 수준 샌드박스

Codex는 OS에 따라 서로 다른 방식으로 샌드박스를 적용합니다:

- **macOS는** Seatbelt 정책을 사용하며, 선택한 `--sandbox` 모드에 해당하는 프로필(`-p`)을 적용해 `sandbox-exec`으로 명령어를 실행합니다. 제한된 읽기 액세스에 플랫폼 기본값이 활성화되면 Codex는 `/System`에 대한 액세스를 광범위하게 허용하는 대신 선별된 macOS 플랫폼 정책을 추가하여 일반적인 도구와의 호환성을 유지합니다.
- **Linux는** 기본적으로 `bwrap`과 `seccomp`를 함께 사용합니다.
- **Windows에서는** [Windows Subsystem for Linux 2 (WSL2)](/ko-KR/codex/windows/wsl)에서 실행할 때 Linux 샌드박스 구현을 사용합니다. WSL1은 Codex `0.114`까지 지원되었지만, `0.115`부터 Linux 샌드박스가 `bwrap` 기반으로 전환되어 더 이상 지원되지 않습니다. Windows에서 네이티브로 실행할 때 Codex는 [Windows 샌드박스](/ko-KR/codex/windows/windows-sandbox#windows-sandbox) 구현을 사용합니다.

Windows에서 사용하는 Codex IDE 확장은 WSL2를 직접 지원합니다. WSL2를 사용할 수 있을 때마다 에이전트가 WSL2 내부에서 실행되도록 VS Code 설정에 다음을 지정하세요:

```json
{
  "chatgpt.runCodexInWindowsSubsystemForLinux": true
}

이렇게 하면 호스트 OS가 Windows인 경우에도 IDE 확장에 Linux 샌드박스의 명령어 실행, 승인 및 파일 시스템 액세스 규칙이 그대로 적용됩니다. 자세한 내용은 [WSL 가이드](/ko-KR/codex/windows/wsl)를 참조하세요.

Windows에서 네이티브로 실행할 때는 `config.toml`에서 네이티브 샌드박스 모드를 구성하세요:

```toml
[windows]
sandbox = "unelevated" # or "elevated"
# sandbox_private_desktop = true  # default; set false only for compatibility

자세한 내용은 [Windows 설정 가이드](/ko-KR/codex/windows/windows-sandbox#windows-sandbox)를 참조하세요.

Docker 같은 컨테이너 환경에서 Linux를 실행할 때 호스트 또는 컨테이너 구성에서 Codex에 필요한 네임스페이스, setuid `bwrap` 또는 `seccomp` 작업을 차단하면 샌드박스가 작동하지 않을 수 있습니다.

이 경우 필요한 격리 기능을 제공하도록 Docker 컨테이너를 구성한 다음, 컨테이너 안에서 `codex` 명령어를 `--sandbox danger-full-access` 옵션 또는 `--dangerously-bypass-approvals-and-sandbox` 플래그와 함께 실행하세요.

### Dev Containers에서 Codex 실행하기

호스트에서 Linux 샌드박스를 직접 실행할 수 없거나 조직에서 이미 컨테이너 기반 개발을 표준으로 사용한다면 Dev Containers로 Codex를 실행하고 Docker가 외부 격리 경계를 제공하도록 하세요. 이 방식은 Visual Studio Code Dev Containers와 호환 도구에서 사용할 수 있습니다.

[Codex 보안 devcontainer 예제](https://github.com/openai/codex/tree/main/.devcontainer)를 참조 구현으로 사용하세요. 이 예제는 Codex, 일반적인 개발 도구, `bubblewrap`, 방화벽 기반 아웃바운드 제어 기능을 설치합니다.

  Devcontainer는 상당한 보호 기능을 제공하지만 모든
  공격을 막지는 못합니다. 컨테이너 안에서 Codex를 `--sandbox danger-full-access` 또는
`--dangerously-bypass-approvals-and-sandbox` 옵션으로 실행하면 악성
  프로젝트가 Codex 자격 증명을 포함해 devcontainer 내부에서
  접근 가능한 모든 항목을 외부로 유출할 수 있습니다. 이 방식은 신뢰할 수 있는 레포지토리에서만 사용하고,
  권한이 높은 다른 환경과 마찬가지로 Codex 활동을 모니터링하세요.

참조 구현에는 다음이 포함됩니다:

- Codex와 일반적인 개발 도구가 설치된 Ubuntu 24.04 기본 이미지;
- 아웃바운드 액세스를 위한 허용 목록 기반 방화벽 프로필;
- 컨테이너에서 워크스페이스를 다시 열기 위한 VS Code 설정 및 권장 확장 프로그램;
- 명령어 기록과 Codex 구성을 위한 영구 마운트;
- `bubblewrap`: 컨테이너가 필요한 기능 권한을 부여하면 Codex가 Linux 샌드박스를 계속 사용할 수 있도록 합니다.

사용해 보려면 다음 단계를 따르세요:

1. Visual Studio Code와 [Dev Containers 확장 프로그램](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)을 설치하세요.
2. Codex 예제의 `.devcontainer` 설정을 레포지토리에 복사하거나 Codex 레포지토리에서 직접 시작하세요.
3. VS Code에서 **Dev Containers: Open Folder in Container...** 명령어를 실행한 다음 `.devcontainer/devcontainer.secure.json` 파일을 선택하세요.
4. 컨테이너가 시작되면 터미널을 열고 `codex` 명령어를 실행하세요.

CLI에서도 컨테이너를 시작할 수 있습니다:

```bash
devcontainer up --workspace-folder . --config .devcontainer/devcontainer.secure.json

이 예제는 세 가지 주요 구성 요소로 이루어집니다:

- `.devcontainer/devcontainer.secure.json` 파일은 컨테이너 설정, 기능 권한, 마운트, 환경 변수 및 VS Code 확장 프로그램을 제어합니다.
- `.devcontainer/Dockerfile.secure` 파일은 Ubuntu 기반 이미지와 설치할 도구를 정의합니다.
- `.devcontainer/init-firewall.sh` 스크립트는 아웃바운드 네트워크 정책을 적용합니다.

참조 방화벽은 출발점으로 활용하도록 설계되었습니다. 격리를 위해 도메인 허용 목록에 의존한다면 TTL을 고려한 갱신이나 DNS 인식 방화벽 등 환경에 적합한 DNS 리바인딩 및 DNS 갱신 보호 대책을 구현하세요.

컨테이너 안에서 다음 모드 중 하나를 선택하세요:

- Dev Container 프로필에서 `bwrap`이 내부 샌드박스를 만드는 데 필요한 기능 권한을 부여한다면 Codex의 Linux 샌드박스를 활성화된 상태로 유지하세요.
- 컨테이너를 보안 경계로 사용하려는 경우 Codex가 두 번째 샌드박스 계층을 만들지 않도록 컨테이너 안에서 `--sandbox danger-full-access` 옵션으로 Codex를 실행하세요.

## 버전 관리

Codex는 버전 관리 워크플로우에서 가장 효과적으로 작동합니다:

- 기능 브랜치에서 작업하고, 작업을 위임하기 전에 `git status`로 작업 디렉터리에 미반영 변경 사항이 없는지 확인하세요. 그러면 Codex 패치를 더 쉽게 분리하고 되돌릴 수 있습니다.
- 추적 중인 파일을 직접 수정하기보다는 패치 기반 워크플로우(예: `git diff`/`git apply`)를 사용하세요. 자주 커밋해 작은 단위로 롤백할 수 있도록 하세요.
- Codex의 제안을 다른 PR과 동일하게 다루세요. 변경 사항에 맞는 검증을 수행하고 diff를 검토한 뒤, 감사를 위해 결정 사항을 커밋 메시지에 기록하세요.

## 모니터링 및 텔레메트리

Codex는 OpenTelemetry(OTel)를 통한 옵트인 모니터링을 지원합니다. 이를 통해 팀은 로컬 보안 기본 설정을 약화하지 않고 사용 내역을 감사하고 문제를 조사하며 컴플라이언스 요구 사항을 충족할 수 있습니다. 텔레메트리는 기본적으로 비활성화되어 있으므로 구성에서 명시적으로 활성화하세요.

### 개요

- Codex는 로컬 실행이 자체적으로 이루어지도록 OTel 내보내기를 기본적으로 비활성화합니다.
- 활성화하면 Codex는 채팅, API 요청, SSE/WebSocket 스트림 활동, 사용자 프롬프트(기본적으로 내용 가림), 도구 승인 결정 및 도구 결과를 포함하는 구조화된 로그 이벤트를 생성합니다.
- Codex는 내보내는 이벤트에 `service.name`(생성 주체), CLI 버전, 환경 레이블을 태그로 추가해 개발/스테이징/프로덕션 트래픽을 구분합니다.

### OTel 활성화하기(옵트인)

Codex 구성(일반적으로 `~/.codex/config.toml`)에 `[otel]` 블록을 추가하고 익스포터와 프롬프트 텍스트 기록 여부를 선택하세요.

```toml
[otel]
environment = "staging"   # dev | staging | prod
exporter = "none"          # none | otlp-http | otlp-grpc
log_user_prompt = false     # redact prompt text unless policy allows

- `exporter = "none"` 설정은 계측을 활성 상태로 유지하지만 데이터를 어디에도 전송하지 않습니다.
- 자체 수집기로 이벤트를 전송하려면 다음 중 하나를 선택하세요:

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

Codex는 이벤트를 일괄 처리하고 종료 시 남은 이벤트를 전송합니다. Codex는 자체 OTel 모듈에서 생성한 텔레메트리만 내보냅니다.

### 이벤트 범주

대표적인 이벤트 유형은 다음과 같습니다:

- `codex.conversation_starts` (모델, 추론 설정, 샌드박스/승인 정책)
- `codex.api_request` (시도, 상태/성공 여부, 소요 시간, 오류 세부 정보)
- `codex.sse_event` (스트림 이벤트 유형, 성공/실패, 소요 시간, `response.completed`의 토큰 수)
- `codex.websocket_request` 및 `codex.websocket_event` (요청 소요 시간과 메시지별 유형/성공 여부/오류)
- `codex.user_prompt` (길이. 내용은 기록을 명시적으로 활성화하지 않으면 마스킹됨)
- `codex.tool_decision` (승인/거부, 결정 출처: 구성 또는 사용자)
- `codex.tool_result` (소요 시간, 성공 여부, 출력 일부)

관련 OTel 메트릭은 카운터와 소요 시간 히스토그램 쌍으로 구성되며, `codex.api_request`, `codex.sse_event`, `codex.websocket.request`, `codex.websocket.event`, `codex.tool.call`와 각각에 대응하는 `.duration_ms` 계측 항목을 포함합니다.

전체 이벤트 목록과 구성 참조 자료는 [GitHub의 Codex 구성 문서](https://github.com/openai/codex/blob/main/docs/config.md#otel)를 참조하세요.

### 보안 및 개인정보 보호 지침

- 정책에서 프롬프트 내용 저장을 명시적으로 허용하지 않는 한 `log_user_prompt = false` 설정을 유지하세요. 프롬프트에는 소스 코드와 민감한 데이터가 포함될 수 있습니다.
- 텔레메트리는 직접 관리하는 수집기로만 전송하고, 규정 준수 요구 사항에 맞는 보존 한도와 접근 제어를 적용하세요.
- 도구 인수와 출력값을 민감한 정보로 취급하세요. 가능하면 수집기나 SIEM에서 민감한 정보를 마스킹하세요.
- Codex가 세션 대화 기록을 `CODEX_HOME` 하위에 저장하지 않도록 하려면 로컬 데이터 보존 설정(예: `history.persistence` / `history.max_bytes`)을 검토하세요. [고급 구성](/ko-KR/codex/config-file/config-advanced#history-persistence) 및 [구성 참조 자료](/ko-KR/codex/config-file/config-reference)를 참조하세요.
- 네트워크 액세스를 끈 상태로 CLI를 실행하면 OTel 데이터를 수집기로 내보낼 수 없습니다. 내보내려면 `workspace-write` 모드에서 OTel 엔드포인트에 대한 네트워크 액세스를 허용하거나, 수집기 도메인을 승인 목록에 추가한 후 Codex 클라우드에서 내보내세요.
- 승인이나 샌드박스 관련 변경 사항과 예상치 못한 도구 실행이 있는지 이벤트를 주기적으로 검토하세요.

OTel은 선택 사항이며, 위에서 설명한 샌드박스 및 승인 보호 기능을 대체하는 것이 아니라 보완하도록 설계되었습니다.

## 관리형 구성

엔터프라이즈 관리자는 [관리형 구성](/ko-KR/codex/enterprise/managed-configuration)에서 워크스페이스의 Codex 보안 설정을 구성할 수 있습니다. 설정 및 정책에 대한 자세한 내용은 해당 페이지를 참조하세요.

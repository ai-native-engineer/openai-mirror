<!-- source: https://learn.chatgpt.com/ko-KR/docs/permissions -->

베타 기능입니다. 권한 프로필은 현재 활발히 개발 중이며 변경될 수 있습니다.

  권한 프로필은 기존 샌드박스 설정과 함께 사용할 수 없습니다.
  `default_permissions` 및 `[permissions]` 조합과 `sandbox_mode` /
`sandbox_workspace_write` 조합 중 하나만 구성하세요. 로드된 구성 파일에
  `sandbox_mode`가 있거나 `--sandbox`를 전달하거나 선택한 구성 프로필에
`sandbox_mode`가 설정되어 있으면 Codex는 `default_permissions` 대신
기존 샌드박스 설정을 사용합니다.

관리형 `allowed_permission_profiles`는 예외로, Codex가
권한 프로필을 사용하도록 합니다. 관리형 프로필 허용 목록을 배포하기 전에
`sandbox_mode`와 `[sandbox_workspace_write]` 같은 기존 설정을 제거하세요.
여러 버전이 혼재된 엔터프라이즈 배포에서는 모든 클라이언트가
Codex 0.138.0 이상을 실행할 때까지 관리형 `allowed_sandbox_modes` 요구 사항을
임시 호환성 제약 조건으로 유지할 수 있습니다.

권한 프로필을 사용하면 Codex가 사용자를 대신해 실행하는 로컬 명령어에
최소 권한 경계를 적용할 수 있습니다. 프로필은 명령어가 읽거나 쓸 수 있는 항목을 정의하는
파일 시스템 규칙과 명령어가 연결할 수 있는 대상을 정의하는 네트워크 규칙을
결합한 이름이 지정된 정책입니다.

  프로필의 `network.enabled = true` 설정은 명령어의 네트워크 액세스를 허용하지만
  네트워크 프록시를 시작하지는 않습니다. 프로필의 도메인 규칙을 적용하려면
`features.network_proxy = true`를 `config.toml`에 설정하거나 활성화된
  관리자 관리형 `[experimental_network]` 요구 사항을 사용하세요. 프록시가 활성화되지
  않으면 프로필의 도메인 규칙으로 직접적인 네트워크 액세스를 제한할 수 없습니다.

프로필을 사용하면 컴퓨터나 네트워크에 광범위한 액세스 권한을 부여하지 않고도
현재 채팅에 필요한 만큼만 Codex에 권한을 부여할 수 있습니다. 예를 들어 읽기 전용 프로필을
사용하면 Codex가 프로젝트를 수정하지 않고 검사할 수 있으며, 쓰기 가능 프로필을
사용하면 수정 범위를 선택한 워크스페이스 루트로 제한할 수 있습니다.

로컬 권한 프로필은 macOS, Linux, WSL 및 네이티브
Windows에서 지원됩니다. 플랫폼별 세부 정보와
주의 사항은 [범위 및 적용 방식](#scope-and-enforcement)을 참조하세요.

Codex 클라우드 네트워크 설정은 [인터넷 액세스](/ko-KR/codex/cloud/internet-access)를 참조하세요.

## 프로필 정의 및 선택

Codex에는 세 가지 기본 제공 권한 프로필이 포함되어 있습니다:

- `:read-only`는 로컬 명령어 실행을 읽기 전용으로 유지합니다.
- `:workspace`는 활성 워크스페이스 루트와 시스템 임시 디렉터리에서 쓰기를 허용합니다.
- `:danger-full-access`는 로컬 샌드박스 제한을 제거하므로,
  이처럼 광범위한 액세스를 의도한 경우에만 사용해야 합니다.

`[permissions.<name>]` 아래에 이름이 지정된 프로필을 만든 다음 최상위
`default_permissions` 키를 해당 프로필 이름이나 앞서 소개한 기본 제공 프로필 중 하나로 설정하세요.
이 예시에서 `project-edit`는 기본 제공 값이 아니라 사용자가 정의한
프로필 이름입니다.

엔터프라이즈 관리자는 관리형 `requirements.toml`에서 프로필을 정의하고
사용자가 선택할 수 있는 프로필을 제한할 수 있습니다.
`allowed_permission_profiles`가 설정되면 목록에 포함되지 않은 프로필은 거부됩니다.
여기에는 목록에 없는 기본 제공 프로필과 향후 Codex 버전에 추가되는 프로필도 포함됩니다.
권장되는 관리형 구성은 [사용 가능한 권한 프로필 제어](/ko-KR/codex/enterprise/managed-configuration#control-available-permission-profiles)를
참조하세요.

사용자 정의 프로필에서는 서로 관련된 두 가지 개념을 사용합니다:

- `[permissions.<name>.workspace_roots]`는 해당 프로필에서
  워크스페이스 루트로 간주할 실제 디렉터리를 추가합니다.
- `[permissions.<name>.filesystem.":workspace_roots"]`는 실제로 적용되는 모든 워크스페이스 루트에서 Codex가 적용할
  파일 시스템 규칙을 정의합니다. 여기에는 현재 세션의 런타임 워크스페이스 루트와
  앞서 프로필에 정의한 루트가 포함됩니다.

프로필에도 일반적인 구성 레이어 모델이 적용됩니다. 우선순위가 더 높은 레이어에서는
프로필 전체를 다시 명시하지 않고도 같은 이름의 프로필에 항목을 추가하거나
기존 항목을 교체할 수 있습니다.

예를 들어 조직 수준 구성과 사용자 수준 구성에서 동일한 프로필을
각각 독립적으로 확장할 수 있습니다:

```toml
# /etc/codex/config.toml
[permissions.server.workspace_roots]
"~/code/server" = true

```toml
# ~/.codex/config.toml
[permissions.server.workspace_roots]
"~/code/mobile-app" = true

`server`가 활성화되면 두 워크스페이스 루트가 모두
실제로 적용되는 프로필에 포함됩니다.

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit.workspace_roots]
"~/code/app" = true
"~/code/shared-lib" = true

[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"
".devcontainer" = "read"
"**/*.env" = "deny"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"
"objects.githubusercontent.com" = "allow"
"*.github.com" = "allow"
"tracking.example.com" = "deny"

이 프로필은 다음을 수행합니다:

- 일반적인 개발자 도구에 필요한 최소한의 런타임 경로를 읽습니다.
- 현재 세션과 프로필에 정의된 루트에 동일한 워크스페이스 루트 규칙을
적용합니다.
- 각 루트에서 `.devcontainer/` 같은 IDE 관련 설정을
  읽기 전용으로 유지합니다.
- 글로브 규칙과 일치하는 환경 파일에 대한 액세스를 거부합니다.
- 구성된 도메인 정책을 통해서만 네트워크 액세스를 허용합니다.

활성 프로필에서는 더 넓은 경로에 읽기 또는 쓰기 권한이 부여되어도
범위가 더 좁은 거부 규칙은 계속 적용됩니다. 예를 들어 워크스페이스 루트에
쓰기 권한을 부여하면서 일치하는 `.env` 경로는 `deny`로 설정할 수 있습니다.

## 프로필 확장

프로필이 기본 제공 프로필이나 이름이 지정된 다른 프로필과 거의 같다면 `extends`를
사용하세요. 기본 보호 기능을 이어받을 수 있도록 처음부터 만드는 대신
기본 제공 프로필을 확장하는 것이 좋습니다. 예를 들어 `:workspace`를 확장하면
명시적으로 재정의하지 않는 한 워크스페이스 루트의 `.codex` 디렉터리가
읽기 전용으로 유지됩니다. 상위 프로필은 한 번만 설정한 다음 차이가 있는
규칙만 추가하거나 재정의하세요.

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit]
description = "Project editing with OpenAI API access."
extends = ":workspace"

[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"

이 프로필은 `:workspace`를 기반으로 하며, 일치하는 `.env` 파일은 계속 거부하고
`api.openai.com`에 대한 요청을 허용합니다. 프로필은 `:read-only`,
`:workspace` 또는 이름이 지정된 다른 프로필을 확장할 수 있지만,
`:danger-full-access`는 확장할 수 없습니다. Codex는 알 수 없는 상위 프로필과 상속
순환도 거부합니다.

## 구성 사양

| 항목                                                             | 유형 / 값              | 기본값                 | 세부 정보                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------- | -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `default_permissions`                                             | 문자열 형식의 프로필 이름        | 없음                    | Codex가 기본적으로 적용하는 권한 프로필의 이름을 지정합니다. `[permissions]` 아래의 프로필이나 `:workspace` 같은 기본 제공 프로필과 일치해야 합니다. 동작을 예측할 수 있도록 명시적으로 설정하세요. 관리형 요구 사항에서는 `:workspace`와 `:read-only`가 모두 명시적으로 허용된 경우에만 이 값을 생략할 수 있습니다. 이 구성에서 관리형 `allowed_permission_profiles`가 권한 프로필을 사용하도록 지정하지 않으면 Codex는 기존 샌드박스 설정을 사용합니다. |
| `[permissions.<name>]`                                            | 테이블                      | 없음                    | 이름이 지정된 프로필을 정의합니다. `default_permissions`는 프로필 하나를 기본값으로 선택하며, 다른 권한 프로필 설정에서도 이 프로필 이름을 사용합니다.                                                                                                                                                                                                                                                                               |
| `permissions.<name>.description`                                  | 문자열                     | 없음                    | 프로필에 사람이 읽을 수 있는 설명을 제공합니다. 프로필은 `extends`를 통해 상위 프로필의 설명을 상속하지 않습니다.                                                                                                                                                                                                                                                                                                 |
| `permissions.<name>.extends`                                      | 문자열 형식의 프로필 이름        | 없음                    | 이름이 지정된 다른 프로필이나 기본 제공 `:read-only` 또는 `:workspace` 프로필을 기반으로 이 프로필을 구성합니다. Codex는 `:danger-full-access`, 알 수 없는 상위 프로필, 상속 순환을 거부합니다.                                                                                                                                                                                                                                            |
| `[permissions.<name>.workspace_roots]`                            | 테이블                      | 없음                    | 프로필에 정의된 워크스페이스 루트를 추가합니다. 이 루트에는 현재 세션의 런타임 워크스페이스 루트와 함께 `:workspace_roots` 파일 시스템 규칙이 적용됩니다.                                                                                                                                                                                                                                                                                |
| `permissions.<name>.workspace_roots."<path>"`                     | 불리언                    | `false`                 | 값을 `true`로 설정하면 해당 경로를 프로필의 워크스페이스 루트 집합에 추가합니다. `false`로 설정된 항목은 비활성 상태로 유지됩니다.                                                                                                                                                                                                                                                                                                                        |
| `[permissions.<name>.filesystem]`                                 | 테이블                      | 없음                    | 파일 시스템 경로를 액세스 값 또는 범위가 지정된 하위 경로 맵에 매핑합니다. 파일 시스템 테이블이 없거나 비어 있으면 파일 시스템 액세스가 제한된 상태로 유지되며 시작 시 경고가 표시됩니다.                                                                                                                                                                                                                                                               |
| `permissions.<name>.filesystem.glob_scan_max_depth`               | 숫자                     | 없음                    | Codex가 샌드박스 시작 전에 일치 항목의 스냅샷을 생성할 때 Linux, WSL 및 네이티브 Windows에서 읽기 거부 글로브의 확장을 제한합니다. 값이 클수록 시작 시 스캔 작업량이 증가할 수 있습니다. 범위가 제한되지 않은 `**` 패턴에 제한된 사전 확장이 필요하면 `1` 이상의 값을 사용하세요.                                                                                                                                                              |
| `[permissions.<name>.filesystem]."<path>"`                        | `read`, `write` 또는 `deny` | 없음                    | 지원되는 경로에 대한 직접 액세스 권한을 부여합니다. `deny`는 액세스를 거부하며, 구체성이 같은 `write` 또는 `read` 항목보다 우선합니다. Codex는 활성 런타임에서 적용할 수 없는 직접 쓰기 규칙을 거부합니다.                                                                                                                                                                                                                            |
| `[permissions.<name>.filesystem."<path>"]."<subpath>"`            | `read`, `write` 또는 `deny` | 없음                    | `<path>`의 하위 경로에 대한 액세스를 허용합니다. 기본 경로에는 `.`을 사용하세요. 다른 하위 경로는 상대적인 하위 경로여야 하며 `.` 또는 `..` 구성 요소를 포함할 수 없습니다.                                                                                                                                                                                                                                                                  |
| `[permissions.<name>.network]`                                    | 테이블                      | 없음                    | 명령어의 네트워크 액세스와 활성 네트워크 프록시가 적용하는 정책을 구성합니다. 관리자 관리형 네트워크 요구사항이 프록시를 시작하는 경우를 제외하고 `features.network_proxy`를 활성화하세요.                                                                                                                                                                                                                                    |
| `permissions.<name>.network.enabled`                              | 불리언                    | `false`                 | 프로필에서 실행되는 명령어의 네트워크 액세스를 활성화합니다. 네트워크 프록시를 시작하지는 않으며, 활성 프록시가 없으면 명령어가 도메인 제한 없이 직접 연결할 수 있습니다.                                                                                                                                                                                                                                                  |
| `[permissions.<name>.network.domains]`                            | 테이블                      | 없음                    | 호스트 패턴을 `allow` 또는 `deny`에 매핑합니다. 규칙은 네트워크 프록시가 활성화된 경우에만 적용됩니다. 활성 프록시는 `allow` 항목이 없으면 도메인 요청을 차단하며, 거부 항목은 허용 항목보다 우선합니다.                                                                                                                                                                                                                 |
| `permissions.<name>.network.domains."<pattern>"`                  | `allow` 또는 `deny`          | 없음                    | 정확히 일치하는 호스트, 하위 도메인용 `*.example.com`, 에이펙스 도메인과 하위 도메인용 `**.example.com`, 허용 전용 전역 와일드카드 `*`를 지원합니다. 호스트 패턴은 앞뒤 공백 제거, 소문자 변환, 후행 점 제거, 단순 포트나 대괄호 제거를 거쳐 정규화됩니다.                                                                                                                                                           |
| `[permissions.<name>.network.unix_sockets]`                       | 테이블                      | 없음                    | Unix 소켓 허용 목록을 재정의하는 항목을 매핑합니다. Docker 같은 로컬 통합에만 사용하세요.                                                                                                                                                                                                                                                                                                                                         |
| `permissions.<name>.network.unix_sockets."<path>"`                | `allow` 또는 `deny`          | 없음                    | `allow`로 Unix 소켓의 절대 경로를 유효 허용 목록에 추가하거나 `deny`로 해당 경로를 거부합니다. 거부된 항목은 유효 허용 목록에서 제외됩니다.                                                                                                                                                                                                                                                                |
| `permissions.<name>.network.proxy_url`                            | URL 문자열                 | `http://127.0.0.1:3128` | `HTTP_PROXY`, `HTTPS_PROXY`, WebSocket 프록시 변수 및 관련 도구의 프록시 환경 변수에 사용되는 HTTP 프록시 리스너입니다.                                                                                                                                                                                                                                                                                            |
| `permissions.<name>.network.enable_socks5`                        | 불리언                    | `true`                  | `ALL_PROXY` 및 FTP 프록시 변수에 사용되는 SOCKS5 리스너를 활성화합니다.                                                                                                                                                                                                                                                                                                                                                     |
| `permissions.<name>.network.socks_url`                            | URL 문자열                 | `http://127.0.0.1:8081` | SOCKS5 리스너 주소입니다.                                                                                                                                                                                                                                                                                                                                                                                                      |
| `permissions.<name>.network.enable_socks5_udp`                    | 불리언                    | `true`                  | SOCKS5 리스너가 활성화된 경우 SOCKS5 UDP 지원을 활성화합니다.                                                                                                                                                                                                                                                                                                                                                               |
| `permissions.<name>.network.allow_upstream_proxy`                 | 불리언                    | `true`                  | 네트워크 샌드박스 프록시가 아웃바운드 요청에 업스트림 `HTTP(S)_PROXY` 및 `ALL_PROXY` 설정을 따르도록 허용합니다.                                                                                                                                                                                                                                                                                                          |
| `permissions.<name>.network.allow_local_binding`                  | 불리언                    | `false`                 | 값이 `true`이면 로컬/사설 네트워크 보호 기능을 비활성화합니다. `false`이면 `localhost` 또는 `127.0.0.1` 같은 정확한 로컬 주소 리터럴을 허용 목록에 명시적으로 추가해야 하며, 로컬 또는 사설 IP 주소로 확인되는 호스트명은 계속 차단됩니다.                                                                                                                                                                                                |
| `permissions.<name>.network.dangerously_allow_non_loopback_proxy` | 불리언                    | `false`                 | 프록시 리스너가 루프백이 아닌 주소에 바인딩하도록 허용합니다. 일반적인 로컬 개발에서는 이 값을 설정하지 마세요.                                                                                                                                                                                                                                                                                                                            |
| `permissions.<name>.network.dangerously_allow_all_unix_sockets`   | 불리언                    | `false`                 | Unix 소켓 프록시가 지원되는 환경에서 Unix 소켓 허용 목록을 우회합니다. 로컬 제한을 광범위하게 우회할 수 있는 수단입니다.                                                                                                                                                                                                                                                                                                               |

## 파일 시스템 권한

파일 시스템 항목에는 `read`, `write`, `deny` 중 하나를 사용합니다:

| 액세스  | 의미                                                                                                                           |
| ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `read`  | 명령어가 해당 경로 아래의 파일을 읽고 디렉터리 목록을 조회할 수 있도록 허용합니다. 해당 위치에서는 파일을 생성하거나 수정하거나 이름을 변경하거나 삭제할 수 없습니다. |
| `write` | 명령어가 해당 경로 아래의 파일을 읽고 수정할 수 있도록 허용합니다. OS가 허용하면 파일을 생성하거나 이름을 변경하거나 삭제할 수도 있습니다.  |
| `deny`  | 해당 경로 아래에서 읽기와 쓰기를 모두 거부합니다. 더 넓은 `read` 또는 `write` 허용 범위 안에서 액세스를 거부할 하위 경로를 지정할 때 사용합니다.         |

더 구체적인 항목이 더 넓은 범위의 항목보다 우선합니다. 두 항목이
같은 경로를 대상으로 하면 `deny`가 `write`보다 우선하고, `write`가
`read`보다 우선합니다.

이 우선순위에 따라 프로필에서 먼저 넓은 작업 영역을 지정한 다음,
읽기가 차단되어야 하는 파일이나 디렉터리를 따로 제외할 수 있습니다:

```toml
[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"
".devcontainer" = "read"
"**/*.env" = "deny"

이 예에서는 워크스페이스 루트의 쓰기 권한이 유지되며, `.devcontainer/`는
쓰기 권한 없이 읽기만 가능합니다. 패턴과 일치하는 환경 파일에는
샌드박스에서 실행되는 명령어가 액세스할 수 없습니다.

더 구체적인 경로를 지정하면 넓은 거부 범위 안의 더 좁은 하위 트리에 대한 액세스를 다시 허용할 수도 있습니다:

```toml
[permissions.project-edit.filesystem]
"~/Documents" = "deny"
"~/Documents/codex" = "write"

지원되는 경로 형식:

| 경로               | 의미                                                                                     | 하위 경로 범위 지정 |
| ------------------ | ------------------------------------------------------------------------------------------- | --------------- |
| `:root`            | 파일 시스템 루트                                                                         | `.`만        |
| `:minimal`         | 일반적인 도구에 필요한 플랫폼 및 런타임 경로                                           | `.`만        |
| `:workspace_roots` | 현재 세션의 워크스페이스 루트와 활성화된 모든 프로필 정의 워크스페이스 루트      | 예             |
| `:tmpdir`          | 사용 가능한 경우 `$TMPDIR` 위치                                               | `.`만        |
| `:slash_tmp`       | 존재하는 경우 `/tmp` 폴더                                                             | `.`만        |
| `/absolute/path`   | macOS/Linux/WSL의 `/path`, 네이티브 Windows의 `C:\path` 등 플랫폼별 절대 경로 | 예             |
| `~/path`           | 현재 사용자의 홈 디렉터리 아래에 있는 경로                                              | 예             |

네이티브 Windows에서는 홈 디렉터리 기준 상대 경로에
`~\work`처럼 백슬래시도 사용할 수 있습니다.

`:root`는 프로필에 의도적으로 광범위한 읽기 권한이 필요한 경우에만 사용하세요:

```toml
[permissions.audit.filesystem]
":root" = "read"

`:workspace_roots` 아래에 중첩 항목을 사용해 액세스 범위를 워크스페이스 루트
기준 상대 하위 경로로 제한하세요:

```toml
[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"          # each workspace root
"docs" = "read"        # each workspace-root docs directory
"generated" = "deny"   # each workspace-root generated directory

중첩 하위 경로는 워크스페이스 루트 안에 있어야 합니다.
`../other-repo`처럼 상위 디렉터리로 이동하는 경로는 거부됩니다.

### 정확한 경로나 glob 패턴으로 읽기 거부

더 넓은 프로필 규칙이 인접한 경로의 액세스를 허용하더라도 Codex가 읽어서는 안 되는 파일이나 하위 트리에는 `deny`를 사용하세요.
정확한 경로는 위치가 일정한
`~/.ssh` 같은 경로에 적합합니다. 레포지토리마다 정확한 위치가 달라지는
민감한 파일군을 프로필에 포함해야 할 때는 glob 패턴이 더 적합합니다.

`:workspace_roots` 아래에 glob 패턴이 있으면 Codex는 이를 각
유효 워크스페이스 루트를 기준으로 해석합니다. 예:

```toml
[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

이 규칙은 각 런타임 워크스페이스 루트나 프로필에 정의된 워크스페이스 루트 아래에서 패턴과 일치하는 `.env` 파일의 읽기를 거부합니다.
일반적인 워크스페이스 쓰기는 유지하면서
환경 파일, 생성된 시크릿 또는 이와 유사하게 자격 증명이 포함된 파일을
읽을 수 없게 하려는 경우 사용하세요.

`deny` glob 패턴은 읽기 거부 규칙으로 지원됩니다. `read` 또는 `write` glob 패턴은
Linux, WSL 및 네이티브 Windows 샌드박스에서 이식성이 떨어지므로 가능하면 정확한
경로나 `"docs/**" = "read"` 같은 하위 트리 규칙을 사용하세요.

Linux, WSL 및 네이티브 Windows에서는 범위가 제한되지 않은 `**` 읽기 거부 패턴을
샌드박스 시작 전에 제한된 깊이까지 사전 확장해야 할 수 있습니다. `glob_scan_max_depth`는
`"**/*.env" = "deny"`처럼 범위가 제한되지 않은 패턴을 사용할 때 설정하세요:

```toml
[permissions.project-edit.filesystem]
glob_scan_max_depth = 3

[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

`glob_scan_max_depth`는 `1` 이상이어야 합니다. 값이 클수록 샌드박스 시작 전에
더 깊이 스캔하므로 Linux, WSL 및 네이티브 Windows에서 시작 시 작업량이 늘어날 수 있습니다.
깊이를 제한하는 사전 확장을 사용하지 않으려면
`*.env`, `*/*.env`, `*/*/*.env`처럼 깊이를 직접 지정해 나열하세요.

동일한 규칙을 현재 세션 루트 외의 위치에도 적용해야 한다면 프로필에
재사용 가능한 워크스페이스 루트를 추가하세요:

```toml
[permissions.project-edit.workspace_roots]
"~/code/app" = true
"~/code/shared-lib" = true

이 프로필이 활성화되면 Codex는 `:workspace_roots` 규칙을
현재 세션의 런타임 워크스페이스 루트와 프로필에 정의되어 활성화된
각 워크스페이스 루트에 적용합니다.

네이티브 Windows에서는 `D:\work` 같은 드라이브 문자 경로와
`\\server\share` 같은 UNC 경로가 절대 경로로 지원됩니다.

## 네트워크 권한

네트워크 액세스와 네트워크 필터링은 별도 설정입니다. 명령의 네트워크 액세스를 허용하려면
`permissions.<name>.network.enabled = true`로 설정하고,
프로필의 도메인 규칙을 적용하려면 `features.network_proxy`를 활성화하세요:

```toml
[features]
network_proxy = true

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"example.com" = "allow"      # exact host
"*.example.com" = "allow"    # subdomains only
"**.example.com" = "allow"   # apex and subdomains
"ads.example.com" = "deny"   # deny wins over allow

동작은 두 설정의 조합에 따라 달라집니다:

- 네트워크 비활성화: 프록시 기능과 관계없이 명령이 네트워크에
액세스할 수 없습니다.
- 네트워크 활성화, 프록시 비활성화: 명령이 네트워크에 제한 없이 직접
액세스합니다. 권한 프로필의 도메인 규칙은 적용되지 않습니다.
- 네트워크 활성화, 프록시 활성화: 명령이 프록시를 사용하며, 프록시가 프로필의
도메인 규칙을 적용합니다. 활성 프록시에 허용된 도메인이 없으면 외부
대상에 대한 액세스를 차단합니다.

`[permissions.<name>.network.domains]` 항목을 추가하거나
`permissions.<name>.network.enabled = true`로 설정해도
`features.network_proxy`는 활성화되지 않습니다. 대신 관리자가
`[experimental_network]`를 `requirements.toml`에 설정해 프록시를 활성화할 수 있습니다.
[관리형 구성](/ko-KR/codex/enterprise/managed-configuration#configure-network-access-requirements)을 참고하세요.

네트워크 샌드박스 프록시는 활성화되면 기본적으로 로컬 리스너에 바인딩됩니다:

```toml
[permissions.project-edit.network]
enabled = true
proxy_url = "http://127.0.0.1:3128"
enable_socks5 = true
socks_url = "http://127.0.0.1:8081"
enable_socks5_udp = true

특정 런타임과 통합하는 경우가 아니라면 리스너 설정을
기본값으로 유지하세요. `dangerously_*` 네트워크 키는 특수 환경에서 제한을 우회하기 위한
수단이므로 일반적인 로컬 개발에는 사용하지 마세요.

### 로컬 및 사설 네트워크

네트워크 프록시가 활성화되면 Codex는 DNS 리바인딩과 로컬 서비스에 대한 의도치 않은
액세스를 방지하기 위해 기본적으로 로컬/사설 네트워크 보호 기능을 적용합니다.
리터럴로 지정된 로컬 대상을 의도적으로 허용하려면 정확한
호스트 또는 IP 리터럴을 허용 목록에 추가하세요:

```toml
[permissions.project-edit.network.domains]
"localhost" = "allow"
"127.0.0.1" = "allow"

`allow_local_binding = true`로 설정하는 경우는 프로필이 로컬 또는 사설 주소로 해석되는
허용 목록의 호스트명에 연결해야 할 때로 제한하세요:

```toml
[permissions.project-edit.network]
enabled = true
allow_local_binding = true

[permissions.project-edit.network.domains]
"localhost" = "allow"

### Unix 소켓

Unix 소켓 프록시는 Docker 같은 도구를 위한 로컬 제한 우회 수단입니다. 꼭 필요한 경우에만
사용하세요:

```toml
[permissions.project-edit.network.unix_sockets]
"/var/run/docker.sock" = "allow"
"/tmp/old.sock" = "deny"

상속된 허용 항목을 포함하여 소켓 경로를 거부하려면 `deny`를 사용하세요.
거부된 소켓 경로는 실제 적용되는 허용 목록에서 제외됩니다.

Unix 소켓이 활성화된 경우 프록시 리스너를 루프백 주소에 바인딩된 상태로 유지하세요.

## 이전 샌드박스 설정에서 마이그레이션

파일 시스템과 네트워크 동작을 하나의 재사용 가능한 프로필로 정의하려는 경우 권한 프로필이 기존 `sandbox_mode` 및
`sandbox_workspace_write` 조합을 대체합니다.
각 세션에서는 두 방식 중 하나만 사용하고
함께 사용하지 마세요.

권장 시작점:

- 읽기 전용 워크플로우에는 기본 제공 `:read-only` 프로필을 사용하거나
  필요한 위치에만 읽기 권한을 부여하는 사용자 지정 프로필을 정의하세요.
- 워크스페이스를 편집하려면 기본 제공 `:workspace` 프로필을 사용하거나
  `:workspace_roots`를 통해 쓰기를 허용하고
  워크플로우에 필요한 추가 임시 경로 또는 캐시 경로만 포함하는 사용자 지정 프로필을 정의하세요.
- 제한 없는 로컬 실행에는 `:danger-full-access`를
  가장 광범위한 로컬 액세스 권한을 의도적으로 허용하려는 경우에만 사용하세요.

프로필은 세션의 기본 로컬 권한 수준을 정의합니다. 조직이 관리하는
요구 사항에 따라 사용자 설정으로 완화해서는 안 되는 제한이
추가될 수 있습니다. [관리형 구성](/ko-KR/codex/enterprise/managed-configuration)에서
관리자가 적용하는 파일 시스템 및 네트워크 제약 조건을 확인하세요.

## 범위 및 적용

권한 프로필은 로컬 샌드박스에서 실행되는 명령의 권한 경계를 정의합니다.
승인 정책과 함께 웹 검색, 커넥터, MCP 서버, 내장 브라우저, 컴퓨터 사용,
Codex 클라우드에 대한 별도 제어 기능을 사용하세요.

### 프로필이 제어하는 항목

- **로컬 명령 실행:** 권한 프로필은 사용자 컴퓨터에서 실행되는 샌드박스 명령을
  제어합니다. 커넥터, MCP 서버, 브라우저 또는
  컴퓨터 사용 인터페이스, Codex 클라우드 환경 설정 및 승인된
  권한 상승에는 각각 별도의 제어 기능이 적용됩니다.
- **파일 시스템 쓰기:** 쓰기 권한이 있는 프로필은 영구적인 변경 사항을 만들 수 있습니다.
  스크립트, 빌드 단계, 패키지 관리자 훅, 셸 시작 파일,
  공유 디렉터리에 쓰는 작업은 민감한 작업으로 취급하세요. 이후 다른 도구나 사용자가
  원래 샌드박스 컨텍스트 밖에서 해당 파일을 실행할 수 있기 때문입니다.
- **아웃바운드 대상:** 네트워크 도메인 규칙은 네트워크 프록시가 활성화된 동안에만
  샌드박스 명령 트래픽이 도달할 수 있는 대상을 제한합니다.
  허용된 대상의 신뢰성까지 판단하지는 않으며, 와일드카드
  허용 규칙은 여전히 광범위합니다.
- **로컬 서비스:** 활성화된 네트워크 프록시는 기본적으로 로컬 및 사설 네트워크
  대상을 차단합니다. `localhost`, 사설 IP 또는 Unix 소켓을 허용 목록에 추가하거나
`allow_local_binding = true`로 설정하면 로컬 서비스 액세스가 명시적으로 허용됩니다.

### 네트워크 프록시가 제어하지 않는 항목

네트워크 프록시는 샌드박스 내부에서 실행되는 로컬 명령의 트래픽만
필터링합니다. 다음 항목에는 프로필의 도메인 허용 목록이 적용되지 않습니다:

- **웹 검색:** 호스팅되는 검색 도구는 자체 액세스 설정을 사용합니다.
`web_search`로 제어하고, 관리형 클라이언트에는 `allowed_web_search_modes`도
  사용하세요. `tools.web_search.allowed_domains`는 명령의 네트워크 액세스가 아니라
  검색 결과를 필터링합니다.
- **앱 및 커넥터:** 커넥터 기반 도구는 자체 서비스 측 연결,
  워크스페이스 권한, 앱 또는 도구 설정을 사용합니다.
- **MCP 서버:** 로컬 및 원격 MCP 서버는 자체 프로세스나
  전송 방식을 사용합니다. `mcp_servers` 설정과 관리형 서버
  허용 목록을 사용해 제어하세요.
- **브라우저 및 컴퓨터 사용:** 브라우저 탐색과 컴퓨터 사용 작업에는
  별도의 기능 제어 및 승인 제어가 적용됩니다.
- **Codex 서비스 트래픽:** 모델, 인증 및 기타 클라이언트 서비스
  요청에는 클라이언트의 별도 HTTP 및 시스템 프록시 설정이 적용됩니다.
- **Codex 클라우드:** 이러한 작업에는 환경별
[인터넷 액세스 설정](/ko-KR/codex/cloud/internet-access)이 적용됩니다.

이러한 기능을 제한하려면 각 기능을 직접 설정하세요. 명령의 네트워크
허용 목록은 Codex가 수행할 수 있는 모든 작업에 적용되는 전역 네트워크 정책이 아닙니다.

### 정책 적용 방식

- macOS에서 Codex는 Seatbelt 샌드박스 프로필을 사용합니다. 선택한 정책을 플랫폼 샌드박스에서
적용할 수 없으면 Codex는 사용자에게 알리지 않은 채 샌드박스 밖에서 명령을 실행하지 않고
명령 실행을 거부합니다.
- Linux와 WSL에서 Codex는 [bubblewrap](https://github.com/containers/bubblewrap)과
  [seccomp](https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html)를 사용하며,
  호환성을 위한 폴백 경로에서는 Landlock도 사용할 수 있습니다. 가장 강력한
  적용 방식은 사용자 네임스페이스와 커널 지원 여부에 따라 달라집니다. 제한된
  컨테이너 호스트에서는 호환성 경로를 사용해야 할 수 있으며, 지원되지 않는 분할 정책은
  거부됩니다.
- 네이티브 Windows에서는 [`elevated` 샌드박스](/ko-KR/codex/windows/windows-sandbox#windows-sandbox)가
  전용 저권한 샌드박스 사용자, 파일 시스템 권한 경계 및
  방화벽 규칙을 사용할 수 있어 가장 강력합니다. `unelevated`
  샌드박스는 네트워크 격리가 더 약한 폴백이며
  읽기/쓰기 분리 예외를 모두 적용할 수 없어 지원되지 않는 정책은 거부됩니다.
  Linux 샌드박스 모델이 필요하면 WSL을 사용하세요.

### 운영 지침

작업을 완료할 수 있는 범위에서 권한이 가장 제한적인 프로필을 선택하세요. 특히 쓰기 또는
아웃바운드 네트워크 액세스를 허용할 때는 더욱 중요합니다. 승인 정책, 시크릿 처리,
허용 규칙을 해당 액세스 수준에 맞추세요.

## 일반적인 프로필

### 네트워크 허용 목록을 사용하는 읽기 전용

```toml
default_permissions = "readonly-net"

[features]
network_proxy = true

[permissions.readonly-net.filesystem]
":minimal" = "read"

[permissions.readonly-net.filesystem.":workspace_roots"]
"." = "read"

[permissions.readonly-net.network]
enabled = true

[permissions.readonly-net.network.domains]
"api.openai.com" = "allow"

### 워크스페이스로 제한된 파일 액세스

다음은 Codex가 워크스페이스 폴더에 쓸 수 있도록 허용하면서 파일 시스템의 나머지 영역에 대한 읽기는 거부하는 권한 프로필의 예입니다. 단, `:minimal`에서 정한 제한적인 예외는 허용됩니다.

```toml
default_permissions = "workspace-only"

[permissions.workspace-only]
# By extending the :workspace profile, you get Codex's safeguards to ensure
# subfolders such as .codex/ and .git/ within a workspace root are read-only
# while the rest of the folder is writable.
extends = ":workspace"

[permissions.workspace-only.filesystem]
# By default, deny read access to all files on disk.
":root" = "deny"

# Though in practice, a software agent needs to be able to read folders that
# contain common tools, such as `/usr/bin`, to get work done, so grant access
# to a "minimal" set of files and folders, as determined by Codex.
":minimal" = "read"

# By extending the :workspace profile, :tmpdir and :slash_tmp are "write" by
# default, though you can deny access to them altogether, if desired.
":tmpdir" = "deny"
":slash_tmp" = "deny"

### 네트워크 접근을 허용하지 않는 워크스페이스 쓰기

```toml
default_permissions = "project-edit"

[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"

[permissions.project-edit.network]
enabled = false

### 공개 웹 접근을 허용하는 워크스페이스 쓰기

```toml
default_permissions = "workspace-net"

[features]
network_proxy = true

[permissions.workspace-net.filesystem]
":minimal" = "read"

[permissions.workspace-net.filesystem.":workspace_roots"]
"." = "write"

[permissions.workspace-net.network]
enabled = true

[permissions.workspace-net.network.domains]
"*" = "allow"

공용 네트워크 접근을 허용하려는 경우에만
 전역 `"*"` 허용 규칙을 사용하세요. 거부 규칙으로 광범위한 허용 목록의 범위를 좁힐 수 있습니다.

<!-- source: https://learn.chatgpt.com/ko-KR/docs/enterprise/managed-configuration -->

관리형 구성은 ChatGPT 데스크톱 앱, Codex CLI 및 IDE 확장에서 지원 대상 기능의 로컬 런타임 동작을 제어합니다. 지원되는 요구 사항은 클라이언트와 버전에 따라 다를 수 있습니다. 관리형 구성은 ChatGPT 워크스페이스 액세스 권한을 부여하거나, 사용 라이선스를 할당하거나, 워크스페이스 역할 기반 접근 제어(RBAC)를 대체하지 않습니다. 워크스페이스 기능 액세스는 [역할 및 워크스페이스 권한](/ko-KR/codex/enterprise/roles-and-workspace-permissions)을 참조하고, 로컬 런타임 정책은 이 페이지를 참조하세요.

엔터프라이즈 관리자는 지원되는 로컬 클라이언트의 동작을 다음 두 가지 방식으로 제어할 수 있습니다:

- **요구 사항**: 관리자가 강제 적용하며 사용자가 재정의할 수 없는 제약 조건입니다.
- **관리형 기본값**: 지원되는 클라이언트가 시작될 때 적용되는 초기값입니다. 실행 중에는 사용자가 설정을 변경할 수 있지만, 클라이언트를 다음에 시작하면 관리형 기본값이 다시 적용됩니다.

## 관리자가 강제 적용하는 요구 사항(requirements.toml)

요구 사항은 보안에 민감한 설정을 제한합니다. 여기에는 승인 정책, 승인 검토자, 자동 검토 정책, 샌드박스 모드, 권한 프로필, 웹 검색 모드, 관리형 훅, 사용자가 활성화할 수 있는 MCP 서버, 사용자가 추가하거나 플러그인 설치에 사용하거나 새로 고칠 수 있는 사용자 구성 플러그인 마켓플레이스 소스가 포함됩니다. 예를 들어 `config.toml`, [프로필 파일](/ko-KR/codex/config-file/config-advanced#profiles), CLI 구성 재정의를 바탕으로 구성을 결정할 때 값이 강제 적용된 규칙과 충돌하면 로컬 클라이언트는 호환되는 값으로 대체하고 사용자에게 알립니다. `mcp_servers` 허용 목록을 구성하면 클라이언트는 이름과 식별 정보가 모두 승인된 항목과 일치하는 MCP 서버만 활성화하며, 그렇지 않은 서버는 비활성화합니다.

요구 사항은 `requirements.toml`의 `[features]` 테이블을 통해 [기능 플래그](/ko-KR/codex/config-file/config-basic/#feature-flags)도 제한할 수 있습니다. 기능이 항상 보안에 민감한 것은 아니지만 엔터프라이즈에서는 원하는 경우 값을 고정할 수 있습니다. 생략된 키는 제한되지 않습니다.

Codex 0.138.0 이상에서는 [권한 프로필](/ko-KR/codex/permissions)에
`allowed_permission_profiles`와 관리형 `default_permissions`를 사용하는 것이 좋습니다.
`allowed_sandbox_modes`는 여전히 `sandbox_mode`를 구성하는
레거시 배포에서만 사용하세요.

정확한 키 목록은 [구성 참조 자료의 `requirements.toml` 섹션](/ko-KR/codex/config-file/config-reference#requirementstoml)을 확인하세요.

### 위치 및 우선순위

지원되는 각 로컬 클라이언트는 우선순위가 낮은 항목부터 높은 항목 순으로 요구 사항을 결합합니다:

1. 시스템 `requirements.toml`(Linux와 macOS를 포함한 Unix 시스템에서는
   `/etc/codex/requirements.toml`, Windows에서는
   `%ProgramData%\OpenAI\Codex\requirements.toml`).
2. 클라우드 구성 번들을 통해 전달되는 엔터프라이즈 관리형 요구 사항.
3. 로컬 클라이언트가 요구 사항으로 재해석하는 레거시 `managed_config.toml` 필드.
4. `com.openai.codex:requirements_toml_base64`를 통해
전달되는 macOS 관리형 환경설정(MDM).

우선순위가 높은 레이어는 낮은 레이어의 일반 스칼라 및 목록 값을
재정의합니다. 테이블은 키별로 병합되지만 규칙, 훅, 파일 시스템 제한 등의
요구 사항은 필드별로 결합 방식이 다릅니다.
모든 필드가 동일한 방식으로 병합된다고 가정하지 말고
[`requirements.toml` 참조 자료](/ko-KR/codex/config-file/config-reference#requirementstoml)에서
현재 스키마를 확인하세요.

하위 호환성을 위해 지원되는 로컬 클라이언트는 레거시
`approval_policy`, `approvals_reviewer`, `sandbox_mode` 필드를
요구 사항으로 재해석합니다. 이 변환은 필요한 경우 호환성을 위한 선택지를 추가합니다.
명시적인 허용 목록은 `requirements.toml`에 정의하세요.

### 클라우드 관리형 요구 사항

사용자가 지원되는 플랜의 ChatGPT 계정으로 로그인하면 지원되는 로컬 클라이언트는
워크스페이스와 연결된 관리자 강제 적용 요구 사항을 받을 수 있습니다. 이는
`requirements.toml` 호환 정책을 전달하는 채널입니다. 워크스페이스 액세스 권한을
부여하거나 워크스페이스 RBAC를 대체하지는 않습니다.

[관리형 구성](https://chatgpt.com/codex/settings/managed-configs)을 열어 클라우드 관리형 요구 사항을
만들고 할당하세요. 예를 들어 다음 정책은 승인 및 샌드박스 선택지를
제한하고 지원되는 셸 진입점이 실행되기 전에
확인을 요청합니다:

```toml
allowed_approval_policies = ["on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

[rules]
prefix_rules = [
  { pattern = [{ any_of = ["bash", "sh", "zsh"] }], decision = "prompt", justification = "Require explicit approval for shell entry points" },
]

관리 대상 클라이언트의 모든 버전이 선택한 키를 지원하는지 확인하고
조직 전체에 할당하기 전에 소규모 그룹을 대상으로 정책을 테스트하세요. 현재 스키마는
구성 참조 자료에서 확인하고, 현재 할당 동작은
관리 화면에서 확인하세요.

서비스는 로그인한 사용자에게 적용되는 엔터프라이즈 관리형 요구 사항
레이어를 선택합니다. 로컬 클라이언트는 이러한 레이어를
[위치 및 우선순위](#locations-and-precedence)에 설명된 다른 요구 사항 소스와 함께 평가합니다.
워크스페이스에서 요구 사항을 생성하고 할당할 때는 현재 관리 화면을
사용하세요. 복사한 그룹 매칭 알고리즘에 의존하지 마세요.
이 동작은 관리 서비스가 담당하므로 로컬 요구 사항 형식과
별개로 변경될 수 있습니다.

지원되는 키와 예시는
[requirements.toml 예시](#example-requirementstoml)와
[`requirements.toml` 참조 자료](/ko-KR/codex/config-file/config-reference#requirementstoml)를 확인하세요.

#### 로컬 클라이언트가 클라우드 관리형 요구 사항을 적용하는 방식

사용자가 지원되는 로컬 클라이언트를 시작하고 지원되는 플랜의 ChatGPT 계정으로
로그인하면 클라이언트는 먼저 유효하고 로그인한 사용자와 일치하는 캐시 항목이
있는지 확인합니다. 유효한 항목이 없으면 적용 대상 번들을 가져오며
필요한 경우 재시도하고, 성공하면 서명된 캐시 항목을 기록합니다. 요청이
실패하거나 시간이 초과된 상황에서 유효한 캐시도 없으면 클라우드 구성 번들 로드는
오류를 반환합니다. 클라우드 관리형 요구 사항 레이어가 빠진 상태로
아무 알림 없이 시작하지 않습니다.

캐시 처리가 끝나면 클라이언트는 클라우드 요구 사항을 위에서 설명한
다른 요구 사항 레이어와 결합합니다. 백그라운드 새로 고침은 다음 시작 시 사용할
캐시를 업데이트할 수 있지만 현재 프로세스에 이미 로드된 요구 사항을
대체하지는 않습니다.

### 관리자와 직원의 사용 경험 확인

관리형 정책마다 담당자를 지정하고 적용 대상 사용자나 그룹을 기록하세요.
파일 시스템, 네트워크, 승인 또는 권한 프로필을 제한하는 경우에는
해당 제한이 필요한 업무상 사유를 문서화하세요.

적용 범위를 확대하기 전에 대표 사용자와 함께 승인된 워크플로우와 의도적으로
허용하지 않은 워크플로우를 테스트하세요. 워크스페이스 역할이나 그룹만으로
로컬 제한이 적용된다고 가정하지 말고 지원되는 클라이언트에서
실제로 적용된 설정을 확인하세요.

### requirements.toml 예시

이 예시는 `--ask-for-approval never`와 `--sandbox danger-full-access`(`--yolo` 포함)를 차단합니다:

```toml
allowed_approval_policies = ["untrusted", "on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

### 앱샷 비활성화

관리 대상 사용자의 앱샷을 비활성화하려면 최상위 `allow_appshots` 요구 사항을 설정하세요:

```toml
allow_appshots = false

앱샷을 사용할 수 있는 환경에서 `allow_appshots = false`로 설정하면 앱샷이 비활성화됩니다.
키를 생략하면 요구 사항에서 앱샷을 제한하지 않으며 일반적인 제품
가용성 검사가 적용됩니다. 실제로 적용되는 요구 사항을
`configRequirements/read`로 조회하는 App Server 클라이언트는 동일한 제한을
`allowAppshots` 값으로 전달받습니다. `allowAppshots` 값이 생략되거나 `null`이면
앱샷이 비활성화되지 않습니다.

### 기기 원격 제어 비활성화

관리 대상 사용자의 [기기 원격 제어](/ko-KR/codex/remote-connections#pick-up-work-from-another-device)를
비활성화하려면 최상위 `allow_remote_control` 요구 사항을 설정하세요:

```toml
allow_remote_control = false

기기 원격 제어를 지원하는 환경에서 `allow_remote_control = false`로 설정하면
해당 기능이 비활성화됩니다. 키를 생략하면 요구 사항에서 기기 원격 제어를
제한하지 않으며 일반적인 제품 가용성 검사가 적용됩니다. 이 요구 사항은
SSH 원격 연결을 비활성화하지 않습니다.

### 사용 가능한 권한 프로필 제어

`allowed_permission_profiles`를 사용해 사용자가 선택할 수 있는 기본 제공 및 맞춤
[권한 프로필](/ko-KR/codex/permissions)을 제어하세요. 이는
`allowed_sandbox_modes`에 대응하는 권한 프로필용 설정입니다. 사용자의
권한 선택 방식에 맞는 허용 목록을 사용하세요.

권한 프로필 허용 목록에는 Codex 0.138.0 이상이 필요합니다. Codex 0.137.0 및
이전 버전은 `allowed_permission_profiles`와 관리형
`default_permissions`를 무시합니다.

관리 대상 클라이언트가 모두 해당 기능을 지원하는 버전을 실행하는 경우에만 아래
권한 프로필 예시를 사용하세요. 전체 클라이언트 업그레이드가
완료될 때까지 관리형 맞춤 프로필을 배포하지 마세요.

테이블이 있으면 이 테이블이 허용되는 프로필의 전체 목록입니다.
`true`로 설정된 프로필만 허용하며, 생략되거나 `false`로 설정된 프로필은
향후 Codex 버전에 추가되는 기본 제공 프로필을 포함해 모두 거부합니다.

#### 표준 프로필 허용

이 정책은 읽기 전용 및 워크스페이스 액세스는 허용하지만 전체 권한은 허용하지 않습니다:

```toml
default_permissions = ":workspace"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
# ":danger-full-access" is omitted, so it is denied.

#### 최소 권한을 갖는 관리형 기본값 추가

관리자는 같은 요구 사항 소스에 맞춤 프로필을 정의할 수 있습니다.
사용자가 로드한 구성의 이름과 충돌하지 않는 조직 고유의 프로필 이름을
사용하세요. 맞춤 이름은 `:` 문자로 시작할 수 없으며,
예약된 이름인 `filesystem`도 사용할 수 없습니다.

Codex 0.137.0 또는 이전 버전을 실행하는 클라이언트에는 관리형 맞춤 프로필을
배포하지 마세요. 이러한 클라이언트는 프로필 테이블은 인식하지만 해당 프로필을 선택하는
관리형 기본값은 인식하지 못합니다.

예:

```toml
default_permissions = "acme_review_only"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
acme_review_only = true
# ":danger-full-access" is intentionally omitted, so it is denied.

[permissions.acme_review_only]
description = "Review code without modifying the workspace."
extends = ":read-only"

#### 엔터프라이즈에서 정의한 프로필만 허용

사용자가 관리자 정의 프로필만 선택해야 하는 경우 모든 기본 제공 프로필을 생략하세요:

```toml
default_permissions = "acme_workspace"

[allowed_permission_profiles]
acme_workspace = true

[permissions.acme_workspace]
description = "Workspace access with sensitive files denied."
extends = ":workspace"

[permissions.acme_workspace.filesystem]
glob_scan_max_depth = 3

[permissions.acme_workspace.filesystem.":workspace_roots"]
"**/*.env" = "deny"

사용자가 기본 제공 `:workspace` 프로필을 직접 선택할 수 없더라도,
맞춤 프로필은 `:workspace`를 확장할 수 있습니다.

#### 다른 소스에서 허용한 프로필 비활성화

권한 허용 목록은 프로필 이름별로 결합됩니다. 클라우드 요구 사항의
우선순위가 시스템 요구 사항보다 높으므로 클라우드 요구 사항에서 `false`를
사용해 시스템 파일이 허용한 프로필을 비활성화할 수 있습니다.

클라우드 요구 사항:

```toml
default_permissions = ":read-only"

[allowed_permission_profiles]
":read-only" = true
":workspace" = false

시스템 요구 사항:

```toml
[allowed_permission_profiles]
":read-only" = true
":workspace" = true  # Not honored because cloud requirements set this to false.

`default_permissions`를 허용된 프로필로 명시적으로 설정하세요. 이 값을 생략하면
`:workspace`와 `:read-only`가 모두 명시적으로 허용된 경우에만
로컬 런타임이 `:workspace`를 기본값으로 사용합니다. `allowed_permission_profiles`가
없으면 관리형 요구 사항은 사용자가 선택할 수 있는 프로필 이름을
제한하지 않습니다. 각 항목에는 기본 제공 프로필이나 로드된 구성 또는
요구 사항 소스에 정의된 맞춤 프로필의 이름을 지정해야 합니다. 맞춤 프로필의 동작을
중앙에서 제어하려면 관리형 요구 사항에 정의하세요.

### 호스트별 샌드박스 요구 사항 재정의

하나의 관리형 정책으로 호스트마다 다른 샌드박스 요구 사항을 적용하려면
`[[remote_sandbox_config]]`를 사용하세요. 예를 들어 노트북에는 더 엄격한 기본값을
유지하면서 조건에 일치하는 개발 머신이나 CI 러너에는 워크스페이스 쓰기를
허용할 수 있습니다. 현재 호스트별 항목은 `allowed_sandbox_modes`만 재정의합니다:

```toml
allowed_sandbox_modes = ["read-only"]

[[remote_sandbox_config]]
hostname_patterns = ["*.devbox.example.com", "runner-??.ci.example.com"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

로컬 런타임은 각 `hostname_patterns` 항목을 가능한 범위에서 확인한
호스트 이름과 비교합니다. 전체 도메인 이름을 확인할 수 있으면 이를
우선 사용하고, 그렇지 않으면 로컬 호스트 이름을 사용합니다. 일치 여부는 대소문자를 구분하지 않습니다.
`*`는 임의의 문자열과 일치하고, `?`는 한 문자와 일치합니다.

동일한 요구 사항 소스에서는 처음 일치하는 `[[remote_sandbox_config]]` 항목이
우선 적용됩니다. 일치하는 항목이 없으면 로컬 런타임은 최상위
`allowed_sandbox_modes`를 유지합니다. 호스트 이름 일치는 정책 선택에만 사용되므로
기기가 인증되었다는 증거로 간주하지 마세요.

웹 검색 모드도 제한할 수 있습니다:

```toml
allowed_web_search_modes = ["cached"] # "disabled" remains implicitly allowed

`allowed_web_search_modes = []` 설정에서는 `"disabled"`만 허용됩니다.
예를 들어 `allowed_web_search_modes = ["cached"]` 설정은 `danger-full-access` 세션에서도 실시간 웹 검색을 차단합니다.

### 네트워크 액세스 요구 사항 구성

  `[experimental_network]` 설정은 실험 단계에 있으며 변경될 수 있습니다.
  사용자가 사용하는 로컬 클라이언트 버전과 운영 체제에서 검증하지 않은 채
  이러한 요구 사항을 엔터프라이즈 배포 전반에 적용하지 마세요.
  Windows 지원은 아직 제한적입니다. 해당 환경에서 테스트하지 않았다면
  Windows 사용자에게 이 정책을 적용하지 마세요.

관리자가 네트워크 액세스 요구 사항을 중앙에서 정의해야 한다면
`requirements.toml`의 `[experimental_network]` 섹션을 사용하세요. 이 요구 사항은
사용자의 `features.network_proxy` 토글과 별개입니다. 해당 기능 플래그 없이도
샌드박스 네트워킹을 구성할 수 있지만, 활성 샌드박스에서 네트워킹을 꺼 둔 경우
명령어에 네트워크 액세스 권한을 부여하지 않습니다. 관리형 프록시를 활성화하려면
`experimental_network.enabled = true`로 설정하세요. 도메인 규칙만으로는
프록시가 활성화되지 않습니다.

```toml
[experimental_network]
enabled = true
managed_allowed_domains_only = true

[experimental_network.domains]
"api.openai.com" = "allow"
"**.example.com" = "allow"
"blocked.example.com" = "deny"
"**.exfil.example.com" = "deny"

`experimental_network.managed_allowed_domains_only = true` 설정은
`[experimental_network.domains]`에 관리자가 직접 관리하는 `"allow"` 항목도 정의하고
해당 규칙만 적용하려는 경우에만 사용하세요.
관리형 허용 규칙 없이 `true`로 설정하면 사용자가 추가한 도메인 허용 규칙은
더 이상 효력이 없습니다. 정식 `domains` 맵과 기존
`allowed_domains` 또는 `denied_domains` 목록을 함께 사용하지 마세요.

`*.example.com`은 하위 도메인에만 일치합니다. `**.example.com`은 루트 도메인과
그 하위 도메인에 일치합니다. 일치하는 거부 규칙이 허용 규칙보다 우선합니다.

도메인 구문, 로컬/사설 대상 규칙, 거부 규칙 우선 적용 방식,
DNS 리바인딩 제한은 [에이전트 승인 및 보안](/ko-KR/codex/agent-approvals-security#network-isolation)에 설명된
샌드박스 네트워킹 동작과 동일합니다.

프록시는 샌드박스 안에서 실행되는 로컬 명령어의 트래픽을 라우팅합니다. 브라우저 도구도
오리진에 접근하기 전에 관리형 네트워크 거부 규칙과 배타적 허용 목록을 확인합니다.
이는 별도의 정책 검사이며, 브라우저 트래픽을 명령어 프록시로 라우팅하는 것은 아닙니다.
프록시는 웹 검색, 앱과 커넥터, MCP 서버, 네이티브 앱 트래픽,
Codex 서비스 요청 또는 Codex 클라우드 트래픽을 필터링하지 않습니다.
각 영역에 맞는 제어 수단을 사용하세요:

- `allowed_web_search_modes`로 웹 검색을 제한하세요.
- `features.apps = false`로 앱과 커넥터 통합을 비활성화하고,
지원되는 경우 `features.plugins = false`로 플러그인을 비활성화하세요.
- 관리형 `mcp_servers` 승인 목록을 사용해 MCP 서버를 제한하세요.
- `browser_use`, `in_app_browser`,
`computer_use` 등의 기능 요구 사항을 사용해 브라우저와 컴퓨터 사용 기능을 제한하세요.
- 클라우드 환경 설정에서 Codex 클라우드의 네트워크 액세스를 구성하세요.

명령어용 도메인 허용 목록은 이러한 기능별
제어 수단을 대체하지 않습니다.

### 브라우저 및 컴퓨터 사용 제어

`requirements.toml`의 `[browser_use]` 및 `[computer_use]` 테이블을 사용해
지원되는 데스크톱 클라이언트를 제한하세요. 배포 환경의 클라이언트 버전과
운영 체제에서 정책을 검증하세요. 허용 규칙을 구성해도
플러그인이 설치되거나 운영 체제 권한이 부여되지 않으며,
여전히 검토가 필요한 동작이 승인되지도 않습니다.

브라우저 액세스를 제어하려면 오리진 정책을 구성하세요. 오리진은 스킴과
호스트, 선택적 포트로 구성되며, `https://example.com` 또는
`https://*.example.com:8443`와 같은 형식입니다. 경로, 쿼리 또는 프래그먼트는 포함하지 마세요.
명령어 네트워크 도메인 규칙과 달리 브라우저 오리진 규칙은 HTTP와 HTTPS를 구분하고
포트도 비교합니다.

이 예시는 브라우저 액세스를 승인된 사이트로 제한하고, 해당 사이트에서 업로드와
전체 Chrome DevTools Protocol(CDP) 액세스를 차단합니다:

```toml
[browser_use]
allow_history_access = false
allow_global_persistent_approval = false

[browser_use.default_origin_policy]
access = "deny"

[browser_use.origins."https://example.com"]
access = "allow"
uploads = "deny"
downloads = "allow"
full_cdp_access = "deny"
persistent_approval = false
access_approval_lifetime = "turn"

일치하는 오리진 규칙은 필드별로 적용됩니다. 일치하는 거부 규칙이 우선하며,
그 외에는 일치하는 규칙에서 지정하지 않은 필드에 기본 오리진 정책의 값이 적용됩니다.
로컬 구성으로 제한을 추가할 수는 있지만 관리형 거부 규칙을 완화할 수는 없습니다.
네트워크 거부 규칙과 배타적 관리형 네트워크 허용 목록도 계속 적용됩니다.

브라우저 동작에 대한 자동 승인 검토를 비활성화하려면
`browser_use.disable_auto_review = true`로 설정하세요. 특정 오리진에서 이를 제한하려면
해당 오리진 정책에 `auto_review = "deny"`를 설정하세요. 이 설정은 승인 처리 방식을 제어하며,
모델 안전 모니터링을 비활성화하지는 않습니다.

네이티브 앱의 경우 기본 액세스 정책을 설정하고 허용할 앱을 지정하세요.
예를 들어 다음 macOS 정책은 계산기를 허용하고 승인 저장을 차단합니다:

```toml
[computer_use]
default_app_access = "deny"
allow_persistent_approval = false

[computer_use.macos.bundle_ids]
"com.apple.calculator" = "allow"

Windows 정책에서는 패키지 앱을 식별할 때
`computer_use.windows.aumids`를 사용하고, 실행 파일을 식별할 때는
`computer_use.windows.exes`를 사용할 수 있습니다. 실행 파일 규칙에는 `publisher_name`,
`product_name`, `access` 항목이 필수이며, `binary_name` 항목은 선택 사항입니다.
표시 이름만 사용하지 말고 앱의 검증된 식별 정보를 사용하세요.

전체 필드는 [구성 참조 자료](/ko-KR/codex/config-file/config-reference#requirementstoml)에서 확인하세요.
관리 대상 macOS 기기에 대해서는
[잠금 상태 사용 제한](#restrict-locked-computer-use)을 참조하세요.

### 기능 플래그 고정

관리형 `requirements.toml`을 적용받는 사용자의
[기능 플래그](/ko-KR/codex/config-file/config-basic/#feature-flags)도 고정할 수 있습니다:

```toml
[features]
personality = true
unified_exec = false

# Disable surface-specific features when needed.
browser_use = false
browser_use_full_cdp_access = false
browser_use_external = false
in_app_browser = false
in_app_updates = false
computer_use = false

런타임 기능에는 `config.toml`의 `[features]` 테이블에 정의된
정식 기능 키를 사용하세요. 로컬 런타임은 인식된 기능을 고정된 설정에 맞도록
정규화하며, `config.toml` 또는 프로필 파일의 기능 설정에
충돌하는 값을 쓰려는 작업을 거부합니다.

<a id="disable-codex-feature-surfaces"></a>

- `in_app_browser = false`로 설정하면 기본 제공 브라우저 패널이 비활성화됩니다.
- `in_app_updates = false`로 설정하면 지원되는 환경에서 다시 시작할 때
  ChatGPT 데스크톱 앱 자체의 업데이터가 비활성화됩니다. 외부 패키지 배포에는 영향을 주지 않으며
  이전 앱 버전에 대한 지원을 연장하지도 않습니다. 설정 및 롤아웃 지침은
[앱 업데이트 관리](/ko-KR/codex/enterprise/manage-app-updates)를 참조하세요.
- `browser_use = false`로 설정하면 브라우저의 컴퓨터 사용 기능이 비활성화되고 브라우저 에이전트도 사용할 수 없게 됩니다.
- `browser_use_full_cdp_access = false`로 설정하면 브라우저 개발자 모드를 포함해
  로컬 런타임의 전체 CDP 액세스가 비활성화되며,
  ChatGPT 데스크톱 앱에서 해당 설정을 활성화할 수 없게 됩니다.
- `browser_use_external = false`로 설정하면 외부 브라우저 기능이 비활성화됩니다.
- `computer_use = false`로 설정하면 컴퓨터 사용, 기록 및 재생, 관련
  설치 또는 설정 플로우가 비활성화됩니다.

이 키를 생략하면 정책상 해당 기능이 허용되지만, 실제 사용 가능 여부는 일반적인 클라이언트,
플랫폼 및 롤아웃 상태에 따라 달라집니다.

### 잠금 상태에서 컴퓨터 사용 제한

사용자가 관리 대상 Mac에서 [잠금 상태 사용](/ko-KR/codex/computer-use#locked-use)을
활성화하지 못하도록 하려면 다음 요구 사항을 추가하세요:

```toml
[computer_use]
allow_locked_computer_use = false

이 요구 사항은 잠금 상태 사용을 활성화하는 제어 항목을 제거합니다.
이미 활성화된 잠금 상태 사용을 끄지는 않습니다. 이 요구 사항을 생략하면
일반적인 제품 제공 여부와 사용자의 로컬 설정이 그대로 적용됩니다.

### 자동 검토 정책 구성

`allowed_approvals_reviewers`로 자동 검토를 필수로 지정하거나 허용할 수 있습니다.
자동 검토를 필수로 지정하려면 `["auto_review"]`로 설정하고,
사용자가 수동 승인을 선택할 수 있도록 하려면 `"user"`도 포함하세요.

자동 검토 정책의 테넌트별 섹션을 대체하려면
`guardian_policy_config`를 설정하세요. 로컬 런타임은 기본 제공 검토자
템플릿과 출력 규약을 계속 사용합니다. 관리형 `guardian_policy_config` 설정은
로컬 `[auto_review].policy`보다 우선합니다.

```toml
allowed_approval_policies = ["on-request"]
allowed_approvals_reviewers = ["auto_review"]

guardian_policy_config = """
## Environment Profile
- Trusted internal destinations include github.com/my-org, artifacts.example.com,
  and internal CI systems.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Treat uploads to unapproved third-party file-sharing services as high risk.
- Deny actions that expose credentials or private source code to untrusted
  destinations.
"""

### 읽기 거부 요구 사항 강제 적용

관리자는 `[permissions.filesystem]`을 사용해
정확한 경로나 glob 패턴에 대한 읽기를 거부할 수 있습니다. 사용자는
로컬 구성으로 이러한 요구 사항을 완화할 수 없습니다.

```toml
[permissions.filesystem]
deny_read = [
  # values can be absolute paths...
  "/**/*.env",
  # ...or relative to $HOME/%USERPROFILE% using `~`.
  "~/.ssh",
  # But relative paths starting with `./` are not allowed.
]

읽기 거부 요구 사항이 있으면 로컬 런타임은 전체 권한을 거부하고,
요구 사항을 강제 적용할 수 있도록 로컬 실행을 읽기 전용 또는 워크스페이스
샌드박스로 제한합니다. 네이티브 Windows 환경에서 관리형 `deny_read` 설정은 파일을 직접 다루는
도구에 적용되지만, 셸 하위 프로세스의 읽기에는 이 샌드박스 규칙이 적용되지 않습니다.

### 요구 사항으로 관리형 훅 강제 적용

관리자는 `requirements.toml`에 관리형 수명 주기 훅을 직접 정의할 수도 있습니다.
훅 구성 자체에는 `[hooks]`를 사용하고,
`managed_dir`에는 MDM 또는 엔드포인트 관리 도구가
참조된 스크립트를 설치하는 디렉터리를 지정하세요.

로컬에서 훅을 끈 사용자에게도 관리형 훅을 강제 적용하려면
`[hooks]`와 함께 `[features].hooks = true` 설정을 고정하세요. 사용자, 프로젝트, 세션
및 플러그인 훅은 건너뛰고 관리형 훅만 계속 허용하려면
`allow_managed_hooks_only = true`로 설정하세요.

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

참고:

- 로컬 런타임은 `requirements.toml`의 훅 구성을 강제 적용하지만,
  `managed_dir`에 있는 스크립트는 배포하지 않습니다.
- 해당 스크립트는 MDM 또는 기기 관리 솔루션으로 배포하세요.
- 관리형 훅 명령어는 구성된 관리형 디렉터리 아래에 있는
스크립트의 절대 경로를 참조해야 합니다.
- `allow_managed_hooks_only = true`로 설정하면 사용자, 프로젝트, 세션 및
  플러그인 소스의 훅은 건너뛰지만, `requirements.toml` 및 다른
  관리형 구성 레이어의 훅은 계속 로드합니다.

### 요구 사항으로 명령어 규칙 강제 적용

관리자는 `requirements.toml`의 `[rules]` 테이블을 사용해
명령어를 제한하는 규칙을 강제 적용할 수도 있습니다. 이러한 규칙은 일반 `.rules` 파일과 병합되며,
가장 제한적인 결정이 계속 우선합니다.

`.rules` 파일과 달리 요구 사항 규칙에는 `decision`을 반드시 지정해야 하며,
그 값은 `"prompt"` 또는 `"forbidden"`여야 합니다(`"allow"`는 사용할 수 없음).

```toml
[rules]
prefix_rules = [
  { pattern = [{ token = "rm" }], decision = "forbidden", justification = "Use git clean -fd instead." },
  { pattern = [{ token = "git" }, { any_of = ["push", "commit"] }], decision = "prompt", justification = "Require review before mutating history." },
]

로컬 클라이언트에서 활성화할 수 있는 MCP 서버를 제한하려면
`mcp_servers` 승인 목록을 추가하세요. stdio 서버는 `command`를 기준으로,
스트리밍 가능한 HTTP 서버는 `url`을 기준으로 일치 여부를 확인하세요:

```toml
[mcp_servers.docs]
identity = { command = "codex-mcp" }

[mcp_servers.remote]
identity = { url = "https://example.com/mcp" }

`identity.command`의 문자열 형식은 구성된 `command` 값만 비교합니다.
`args`, `cwd`, `env`, `env_vars` 항목은 검사하지 않습니다.

전체 stdio 호출을 제한하려면 실행 파일과 각
위치 인수를 비교하도록 설정하세요:

```toml
[mcp_servers.internal.identity]
command = { executable = "/usr/local/bin/codex-mcp", args = [
  { match = "exact", value = "serve" },
  { match = "prefix", value = "--workspace=" },
] }

실행 파일, 인수 개수 및 인수 순서가 모두 일치해야 합니다. 인수와 URL 규칙은
`exact`, `prefix`, 전체 값을 대상으로 하는 `regex` 일치를 지원합니다.
구조화된 명령어 규칙도 `cwd`, `env`, `env_vars` 항목을 검사하지 않습니다.
플러그인에 포함된 MCP 서버는
`plugins.<plugin>.mcp_servers.<server>` 아래에서 동일한 식별 정보 형식을 사용합니다.

`mcp_servers` 항목이 있지만 비어 있으면 로컬 클라이언트가 모든 MCP 서버를 비활성화합니다.

### 플러그인 사용 가능 여부 제어

지원되는 로컬 클라이언트에서 플러그인을 끄려면
`requirements.toml`에서 `features.plugins` 값을 `false`로 설정하세요:

```toml
features.plugins = false

사용자가 API 키로 Codex에 로그인할 때도 이 설정이 적용됩니다.
지원되는 구성은 [`features.plugins`
참조 자료](/ko-KR/codex/config-file/config-reference#requirementstoml)에서
확인하세요.

### 플러그인 마켓플레이스 소스 제한

사용자가 구성한 마켓플레이스 소스에 대한 작업을 제한하려면
`restrict_to_allowed_sources = true`로 설정하고 소스 규칙을 하나 이상 정의하세요:

```toml
[marketplaces]
restrict_to_allowed_sources = true

[marketplaces.allowed_sources.company_plugins]
source = "git"
url = "https://github.com/example/company-plugins.git"
ref = "main"

[marketplaces.allowed_sources.internal_git]
source = "host_pattern"
host_pattern = '^git\.example\.com$'

[marketplaces.allowed_sources.local_plugins]
source = "local"
path = "/opt/company/codex-plugins"

Git 규칙은 정규화된 레포지토리 URL을 비교하며,
`ref` 값이 있으면 그 값도 정확히 일치해야 합니다. 호스트 패턴은 소문자로 변환한 Git 호스트를
비교하는 정규 표현식입니다. 호스트 전체를 일치시키려면 `^` 및 `$` 기호를 사용하세요.
로컬 규칙에는 정규화된 절대 경로가 필요합니다. 전체 스키마와 병합 동작은
[`requirements.toml` 참조 자료](/ko-KR/codex/config-file/config-reference#requirementstoml)에서 확인하세요.

이 요구 사항은 사용자가 구성한 소스에서 규칙과 일치하지 않는 마켓플레이스 추가,
플러그인 설치 및 구성된 Git 마켓플레이스 새로 고침 작업을 거부합니다.
Codex가 관리하는 OpenAI 마켓플레이스는 소스와 예약된 이름이 일치하면
계속 사용할 수 있습니다. 이 요구 사항은 이미 구성된 사용자 마켓플레이스나
해당 플러그인을 런타임에 필터링하지 않습니다.

이러한 소스 제한은 로컬 클라이언트가 플러그인 마켓플레이스 작업을 지원하는 경우에만 적용됩니다. 해당 클라이언트는 데스크톱 앱의 ChatGPT와 Codex, 그리고 Codex CLI입니다.
이 제한은 웹이나 모바일의 ChatGPT에서 플러그인 사용을 제어하지 않으며,
IDE 확장에 플러그인을 추가하지도 않습니다.

## 관리형 기본값(`managed_config.toml`)

관리형 기본값은 지원되는 로컬 클라이언트가 시작할 때 사용할 구성을 정합니다.
시작 시 사용자의 로컬 `config.toml` 및 CLI `--config`로
재정의한 값보다 우선합니다. 사용자는 현재 실행 중에도 이러한 설정을 변경할 수 있으며,
다음에 클라이언트를 시작하면 기본값이 다시 적용됩니다.

ChatGPT로 로그인한 사용자의 모델을 관리형 기본값, macOS MDM 프로필 또는 저장된 구성에서 `gpt-5.4`
또는 `gpt-5.4-mini`로 고정했다면 2026년 8월 31일 전에 해당 설정을 업데이트하세요. `gpt-5.4`는 `gpt-5.6-terra`로, `gpt-5.4-mini`는
`gpt-5.6-luna`로 바꾸세요. OpenAI API와 자체 API 키로 인증한 Codex는
영향을 받지 않습니다. [워크스페이스 모델
가용성](/ko-KR/codex/enterprise/workspace-model-availability#prepare-for-the-gpt-54-retirement)을 참조하세요.

관리형 기본값이 요구사항을 충족하는지 확인하세요. 로컬 런타임은
허용되지 않은 값을 거부합니다.

### 우선순위와 계층 구조

로컬 런타임은 다음 순서로 최종 적용 구성을 조합합니다.
위쪽 항목이 아래쪽 항목보다 우선합니다:

- 관리형 환경설정(macOS MDM, 가장 높은 우선순위)
- `managed_config.toml`(시스템/관리형 파일)
- `config.toml`(사용자의 기본 구성)

CLI에서 `--config key=value`로 재정의한 값은 기본 구성에 적용되지만 관리형 계층이 그보다 우선합니다. 따라서 로컬 플래그를 지정하더라도 실행할 때마다 관리형 기본값으로 시작합니다.

클라우드 관리형 요구사항은 관리형 기본값이 아니라 요구사항 계층에 적용됩니다. 우선순위는 위의 관리자가 적용하는 요구사항 섹션을 참조하세요.

### 위치

- Linux/macOS(Unix): `/etc/codex/managed_config.toml`
- Windows/Unix 외 운영체제: `~/.codex/managed_config.toml`

파일이 없으면 로컬 런타임은 관리형 계층을 건너뜁니다.

### macOS 관리형 환경설정(MDM)

macOS에서는 관리자가 다음 위치에 base64로 인코딩된 TOML 페이로드를 제공하는 기기 프로필을 배포할 수 있습니다:

- 환경설정 도메인: `com.openai.codex`
- 키:
  - `config_toml_base64`(관리형 기본값)
  - `requirements_toml_base64`(요구사항)

로컬 런타임은 이러한 "관리형 환경설정" 페이로드를 TOML로 파싱합니다.
관리형 기본값(`config_toml_base64`)에는 관리형 환경설정이
가장 높은 우선순위로 적용됩니다. 요구사항(`requirements_toml_base64`)의 우선순위는
위에서 설명한 클라우드 관리형 요구사항의 적용 순서를 따릅니다.
요구사항에 사용하는 동일한 `[features]` 테이블을 `requirements_toml_base64`에서도 사용할 수 있습니다.
여기에도 정식 기능 키를 사용하세요.

### MDM 설정 워크플로우

로컬 런타임은 표준 macOS MDM 페이로드를 적용하므로
`Jamf Pro`, `Fleet` 또는 `Kandji` 같은 도구로 설정을 배포할 수 있습니다.
간단한 배포 절차는 다음과 같습니다:

1. 관리형 페이로드를 TOML로 작성한 다음 줄 바꿈 없이 `base64`로 인코딩하세요.
2. MDM 프로필의 `com.openai.codex` 도메인에 있는 `config_toml_base64`(관리형 기본값) 또는 `requirements_toml_base64`(요구사항) 키에 이 문자열을 입력하세요.
3. 프로필을 배포한 다음 사용자에게 지원되는 로컬 클라이언트를 다시 시작하고
시작 시 표시되는 구성 요약에 관리형 설정값이 반영되었는지 확인하도록 요청하세요.
4. 정책을 철회하거나 변경할 때는 관리형 페이로드를 업데이트하세요. 클라이언트는
다음 실행 시 갱신된 환경설정을 읽습니다.

페이로드에 비밀 정보나 자주 변경되는 동적 값을 포함하지 마세요. 관리형 TOML도 다른 MDM 설정과 마찬가지로 변경 관리 절차에 따라 관리하세요.

### managed\_config.toml 예시

```toml
# Set conservative defaults
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

[sandbox_workspace_write]
network_access = false             # keep network disabled unless explicitly allowed

[otel]
environment = "prod"
exporter = "otlp-http"            # point at your collector
log_user_prompt = false            # keep prompts redacted
# exporter details live under exporter tables; see Monitoring and telemetry above

### 권장 가드레일

- 대부분의 사용자에게는 승인 절차를 적용한 `workspace-write`를 우선 사용하고, 전체 권한은 통제된 컨테이너에만 허용하세요.
- 보안 검토에서 수집기 사용이나 워크플로우에 필요한 도메인 접근을 허용한 경우가 아니라면 `network_access = false` 설정을 유지하세요.
- 관리형 구성으로 OTel 설정(익스포터, 환경)을 고정하되, 정책에서 프롬프트 내용 저장을 명시적으로 허용하지 않는 한 `log_user_prompt = false` 설정을 유지하세요.
- 로컬 `config.toml`과 관리형 정책 간의 차이를 정기적으로 감사해 구성 드리프트를 감지하세요. 관리형 계층은 로컬 플래그와 파일보다 우선해야 합니다.

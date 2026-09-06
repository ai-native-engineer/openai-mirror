<!-- source: https://learn.chatgpt.com/ko-KR/docs/enterprise/workload-identity -->

워크로드 ID 페더레이션을 사용하면 개인 액세스 토큰이나 다른 장기 OpenAI 자격 증명을 저장하지 않고도 신뢰할 수 있는 자동화 프로세스에서 Codex를 사용할 수 있습니다. 워크로드가 이미 운영 중인 공급자에서 발급한 단기 ID 토큰을 제시하면 OpenAI는 해당 토큰을 검증하고 관리형 ChatGPT 워크스페이스의 사용자 또는 서비스 계정에 대한 단기 액세스 토큰을 반환합니다.

클라우드 플랫폼,
Kubernetes, CI 시스템 및 OIDC 토큰이나
SPIFFE JWT-SVID를 발급할 수 있는 다른 환경에서 무인으로 실행되는 Codex 프로세스에 워크로드 ID를 사용하세요. 공유 신뢰 모델과 별도의 OpenAI API 플로우는
[워크로드 ID 개요](/api/docs/guides/workload-identity-federation)를 참조하세요.

  Codex 워크로드 ID 페더레이션은 베타 버전이며 해당
  워크스페이스에서 활성화해야 합니다. 이용 권한을 요청하려면 OpenAI 담당자 또는 [OpenAI
  지원팀](https://help.openai.com/en/articles/6614161-how-can-i-contact-support)에 문의하세요.

## 시작하기 전에

다음이 필요합니다:

- OpenAI Admin Portal에서 워크로드 ID를 관리할 권한.
- 관리형 ChatGPT 워크스페이스.
- 해당 워크스페이스의 활성 멤버인 ChatGPT 사용자 또는 서비스 계정이나, 설정 중 이러한 계정을 생성할 수 있는 권한.
- 발급자, 대상 및 식별 클레임을 알고 있는 OIDC 토큰 또는 SPIFFE JWT-SVID.
- 절대 경로에 있는 보호된 파일에서 해당 토큰을 최신 상태로 유지할 수 있는 런타임.
- Codex 0.148.0 이상.
- ChatGPT 인증과 페더레이션 규칙에서 선택한 워크스페이스를 허용하는
  실제로 적용되는 Codex 인증 정책. 자세한 내용은 [로그인
  방식 또는 워크스페이스 적용](/ko-KR/codex/auth#enforce-a-login-method-or-workspace)을 참조하세요.

OpenAI는 토큰 교환 중 보안 주체를 생성하거나 워크스페이스 멤버로 추가하지 않습니다. 관리자가 워크로드를 연결하기 전에 보안 주체를 선택하거나 생성해야 합니다. 실제 사용자 계정을 생성하면 워크스페이스 좌석 하나를 사용하며 해당 워크스페이스의 멤버십 규칙이 적용됩니다.

네이티브 Windows에서는 **권한 상승**
[Windows 샌드박스](/ko-KR/codex/windows/windows-sandbox)를 사용하세요. 다른 Windows 샌드박스 모드에서는
모델이 제어하는 명령어로부터 ID 토큰 파일을 보호할 수 없습니다.

## ID 토큰 가져오기

워크로드 런타임이 업스트림 ID 토큰을 가져오고 갱신합니다. Codex는 사용자를 대신해 클라우드 메타데이터 서비스나 ID 공급자의 클라이언트 라이브러리를 호출하지 않습니다.

| 런타임                          | 권장 토큰 파일 소스                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Kubernetes, AKS, EKS 또는 GKE     | 프로젝션된 서비스 계정 토큰을 마운트하고 Codex가 해당 파일을 참조하도록 설정하세요. 플랫폼이 토큰을 교체합니다.                                  |
| Microsoft Entra 관리 ID | Azure IMDS에 토큰을 요청하고 만료 전에 파일을 교체하는 신뢰할 수 있는 호스트 프로세스 또는 사이드카를 실행하세요.                |
| AWS 아웃바운드 ID 페더레이션 | 리전별 STS `GetWebIdentityToken`을 호출하고 만료 전에 파일을 교체하는 신뢰할 수 있는 호스트 프로세스를 실행하세요.                   |
| Google Cloud                     | 메타데이터 서버에 ID 토큰을 요청하고 만료 전에 파일을 교체하는 신뢰할 수 있는 호스트 프로세스를 실행하세요.        |
| Oracle Cloud Infrastructure      | 인스턴스 보안 주체를 사용해 IDCS 액세스 토큰을 요청하고 만료 전에 파일을 교체하는 신뢰할 수 있는 호스트 프로세스를 실행하세요. |
| GitHub Actions                   | 작업의 OIDC 토큰을 요청하여 보호된 파일에 저장하고, 이후 토큰을 교환하기 전에 새 토큰을 요청하세요.                    |
| SPIFFE                           | SPIFFE Workload API 또는 승인된 헬퍼를 사용해 최신 JWT-SVID를 파일에 저장하세요.                                      |
| 사용자 지정 OIDC 공급자             | 발급자의 워크로드 플로우를 사용해 JWT를 가져온 다음 JWT가 만료되기 전에 보호된 파일을 갱신하세요.                            |

공급자별 가이드에 따라 토큰 발급을 설정하고 샘플 토큰을 확인하세요:

- [Microsoft Azure](/api/docs/guides/workload-identity-federation/microsoft-azure)
- [AWS](/api/docs/guides/workload-identity-federation/aws)
- [Google Cloud](/api/docs/guides/workload-identity-federation/google-cloud)
- [Oracle Cloud Infrastructure](/api/docs/guides/workload-identity-federation/oracle-cloud)
- [GitHub Actions](/api/docs/guides/workload-identity-federation/github-actions)
- [Kubernetes](/api/docs/guides/workload-identity-federation/kubernetes)
- [SPIFFE](/api/docs/guides/workload-identity-federation/spiffe)

샘플 토큰을 로컬에서 디코딩하고 `iss`, `aud`, `sub` 및 신뢰할
기타 클레임을 기록하세요. 디코딩만으로는 서명이 검증되지 않습니다. 프로덕션 토큰을
웹사이트에 붙여넣거나 로그에 기록하지 마세요.

## 워크로드 연결

관리자는 Codex를 시작하기 전에 공급자와 페더레이션 규칙을 생성합니다.

1. OpenAI Admin Portal에서 [워크로드 ID](https://admin.openai.com/workload-identity)를 열고
    **워크로드 연결을** 선택하세요.
2. Codex용으로 설정된 공급자를 재사용하거나 새 공급자를 생성하세요. 공급자 프리셋은 GitHub Actions, Microsoft Entra ID, Google Cloud, AWS, Kubernetes, SPIFFE 및 사용자 지정 OIDC 공급자에 일반적으로 필요한 설정을 자동으로 입력합니다.
3. **Codex** 및 워크로드가 사용할 수 있는 관리형 워크스페이스를 선택하세요.
4. 워크로드를 식별할 수 있는 최대한 제한적인 조건을 추가하세요. 주체, 정확히 일치하는 클레임, CEL 조건 또는 이들의 조합으로 일치 여부를 확인하세요. 허용 대상을 추가하여 규칙이 수락하는 토큰을 제한하세요. 구성된 모든 매처의 검사를 통과해야 합니다.
5. 규칙을 기존 ChatGPT 사용자 또는 서비스 계정 하나에 매핑하거나 설정 중에 새 계정을 생성하세요.
6. 공급자, 조건, 워크스페이스, 보안 주체, 스코프 및 액세스
   토큰 유효 기간을 검토하세요. **워크로드 연결을** 선택한 다음 **설정 다운로드를** 선택하세요.

다운로드한 파일에는 비밀 정보가 아닌 페더레이션 규칙 ID와 Codex가 ID 토큰을 읽을 경로가 포함됩니다. 자격 증명은 포함되지 않습니다.

설정을 자동화하려면 [워크로드 ID Admin
API](/api/docs/guides/workload-identity-federation/admin-api)를 사용하세요. 매처의
동작과 예시는 [페더레이션 규칙
참조 자료](/api/docs/guides/workload-identity-federation/federation-rules)를 확인하세요.

## Codex 프로세스 설정

Codex를 시작하는 프로세스에는 다음 두 가지 워크로드 ID 변수가 필요합니다:

```bash

`OPENAI_FEDERATION_RULE_ID`는 비밀 정보가 아닙니다. 토큰 파일은 비밀 정보입니다. 토큰 파일에는 절대
경로를 사용하세요. `/var/run/secrets/openai.com` 같은 전용 디렉터리는 워크로드
계정이 소유하고 권한 모드는 `0700`이어야 합니다. 신뢰할 수 있는 호스트 프로세스만
이 디렉터리에 파일을 쓸 수 있어야 합니다. 이 디렉터리는 레포지토리와
Codex 도구가 접근할 수 있는 다른 경로 외부에 두세요. 자격 증명이 로그, 셸 기록, 빌드 아티팩트에 포함되지 않도록 하세요.

### 감사 식별 정보 추가

런타임 인스턴스가 하나의 페더레이션 규칙을 공유하는 경우 토큰 발급 감사 이벤트에서
각 인스턴스를 식별할 수 있습니다. 선택 사항인
`OPENAI_WORKLOAD_IDENTITY_CONTEXT` 변수를 문자열로 인코딩한 JSON
객체로 설정하세요:

```bash

  "instance_id": "runner-42",
  "display_name": "payments-prod",
  "labels": {
    "environment": "production",
    "region": "us-west-2"
  }
}'

객체에는 `instance_id`가 필수입니다. 또한 `display_name` 및 최대
8개의 라벨을 포함할 수 있습니다. 인코딩된 객체의 최대 크기는 1,024바이트입니다. `instance_id` 및
`display_name`의 길이는 각각 최대 128자입니다. 라벨 키는 최대 64자까지
허용되며 라벨 값은 최대 256자입니다.

식별자는 ASCII 영문자 또는 숫자로 시작해야 합니다. 그 뒤에는
영문자, 숫자, `.`, `_`, `:`, `/`, `@`, `-`도 포함할 수 있습니다. 라벨 키에 허용되는 문자는 영문자,
숫자, `.`, `_`, `-`입니다.

OpenAI는 이 컨텍스트를 검증된 워크로드 ID가 아니라 클라이언트가 보고한 감사 식별 정보로 취급합니다. 이 정보는 인증, 권한 부여, 규칙 일치, 스코프, 요청 한도, 취소, 기능 게이트 또는 지표에 영향을 주지 않습니다. 자격 증명, 비밀 정보, 개인정보, 프롬프트, 모델 출력 또는 기타 고객 콘텐츠를 포함하지 마세요.

컨텍스트가 유효하면 OpenAI는 테넌트,
공급자, 페더레이션 규칙, `instance_id` 범위에서 일관된 귀속 ID를 생성합니다. 귀속 정보를 나타내기 위해 액세스 토큰에는
해당 ID가 포함되지만 컨텍스트는 포함되지 않습니다. 토큰 발급 성공 감사 이벤트에는
ID와 정규화된 컨텍스트가 포함됩니다. 컨텍스트가 제한을 초과하거나
이 스키마를 위반하면 `invalid_grant` 오류와 함께 교환에 실패합니다.

Codex는 프로세스가 시작될 때 컨텍스트를 읽으며, 이 컨텍스트와 규칙 ID, 토큰 파일 경로를 모델이 제어하는 셸, 훅 또는 MCP 서버에 전달하지 않습니다. 컨텍스트를 변경한 후에는 Codex를 다시 시작하세요.

### 토큰 파일 보호 및 주기적 교체

관리형 Linux, macOS, WSL 배포 환경에서는 토큰 디렉터리 전체를
관리형 요구 사항의 [`permissions.filesystem.deny_read`](/ko-KR/codex/enterprise/managed-configuration#enforce-deny-read-requirements)에
추가하세요:

```toml
[permissions.filesystem]
deny_read = ["/var/run/secrets/openai.com"]

이렇게 하면 모델이 제어하는 명령어가 현재 사용 중인 토큰이나 임시 대체 파일을 읽지 못하지만, Codex 호스트 프로세스는 여전히 해당 토큰을 교환에 사용할 수 있습니다. 프로젝션된 토큰 볼륨의 경우 토큰 마운트 전체와 마운트 외부에 있는 실제 저장 경로 또는 해석된 대상 경로에 대한 읽기를 차단하세요. 파일 권한과 환경 변수 정리만으로는 동일한 사용자 권한으로 실행되는 다른 프로세스로부터 자격 증명을 보호할 수 없습니다. 네이티브 Windows에서는 앞에서 설명한 권한이 상승된 샌드박스를 사용하세요.

파일을 프로젝션하지 않는 토큰 공급원이라면 신뢰할 수 있는 호스트 프로세스가 보호된 디렉터리에 교체 파일을 매번 작성한 후 이름을 바꿔 올바른 위치에 배치하도록 하세요. 원자적으로 이름을 변경하면 Codex가 일부만 기록된 토큰을 읽지 않습니다. 예를 들어 다음 호스트 소유 갱신 스크립트를 공급자의 토큰 명령어에 맞게 수정하세요. 스크립트를 실행하기 전에 디렉터리를 프로비저닝하세요:

```bash
set -eu
TOKEN_DIR="/var/run/secrets/openai.com"
TOKEN_FILE="$TOKEN_DIR/identity-token"
umask 077
TOKEN_TEMP="$(mktemp "$TOKEN_DIR/.identity-token.XXXXXX")"
trap 'rm -f -- "$TOKEN_TEMP"' EXIT
trap 'exit 1' HUP INT TERM
your-identity-provider-command > "$TOKEN_TEMP"
test -s "$TOKEN_TEMP"
mv -f -- "$TOKEN_TEMP" "$TOKEN_FILE"

갱신 프로세스는 Codex가 제어할 수 있는 셸이나 도구 외부에서 실행하세요.
갱신 및 정리 중에도 읽기 차단을 유지하세요. 강제 중단으로
임시 파일이 남더라도 해당 파일은 반드시 읽기가 차단된
디렉터리 안에 있어야 합니다. 워크로드 아이덴티티 설정을 `config.toml`에 넣지 마세요.

## 연결 검증

다운로드한 환경을 불러와 선택된 인증 방법을 확인하세요:

```bash
. ./workload-identity-idpm_example.env
codex login status

PowerShell에서는:

```powershell
$env:OPENAI_FEDERATION_RULE_ID = "idpm_..."
$env:OPENAI_IDENTITY_TOKEN_FILE = "C:\run\openai\identity-token"
codex login status

검증에 성공하면 `Logged in using workload identity` 메시지가 출력됩니다. 이는 Codex가
설정된 페더레이션 규칙을 통해 토큰을 교환했음을 의미합니다. 이 명령어는
실제로 적용된 워크스페이스, 보안 주체 또는 규칙을 출력하지 않습니다. 워크로드를 시작하기 전에
Admin Portal에서 해당 값을 확인하세요. Codex에 다른 인증 방법이
표시된다면 필수 WIF 변수 두 개가 프로세스에 전달되지 않은 것입니다.

공급자가 **어설션 재사용 방지** 기능을 사용하고 어설션에 `jti`
클레임이 있으면 이 검증 과정에서 해당 `jti`가 소모됩니다. 다른 Codex 프로세스를 시작하기 전에
새 `jti`가 포함된 어설션을 새로 발급받아 기록하세요.

같은 환경에서 간단한 요청을 실행하세요:

```bash
codex exec "Reply with only: workload identity is working"

Codex는 업스트림 토큰을 교환하고 OpenAI 액세스 토큰을 메모리에 보관합니다.
두 자격 증명 모두 `auth.json`, 시스템 키링 또는
`config.toml`에 기록하지 않습니다.

## 토큰 최신 상태 유지

업스트림 토큰이 만료되기 전에 아이덴티티 토큰 파일을 갱신하세요. Codex는 새로운 OpenAI 액세스 토큰이 필요할 때 파일을 다시 읽습니다. OpenAI 토큰은 업스트림 토큰의 만료 시점과 페더레이션 규칙의 유효 기간 종료 시점 중 더 이른 시점에 만료되며, 유효 기간은 최대 1시간입니다.

관리자가 재사용 방지를 활성화하면 각 업스트림 JWT에는
고유한 `jti`가 필요합니다. 새 `jti`가 포함된 어설션을 새로 발급받아
매번 교환 전에 기록하세요. 여기에는 장시간 실행되는 프로세스에서의 갱신도 포함됩니다.
`jti`가 없는 어설션에는 재사용 방지가 적용되지 않습니다.

Codex는 각 호스트 프로세스 내에서 하나의 인메모리 교환 세션을 공유합니다. 해당 프로세스에서 동시에 발생하는 요청은 유효한 OpenAI 액세스 토큰을 재사용하며, 토큰이 만료되면 하나의 갱신 작업을 공유합니다. 별도 프로세스는 각각 별도로 토큰을 교환하므로 공급자가 각 프로세스에 사용을 허용한 어설션이 필요합니다.

## 자격 증명 우선순위

워크로드 아이덴티티에 필요한 두 변수는 다른 모든 자격 증명 소스보다 우선합니다:

1. `OPENAI_FEDERATION_RULE_ID` 또는
`OPENAI_IDENTITY_TOKEN_FILE` 중 하나라도 설정되어 있으면 Codex는 워크로드 아이덴티티를 선택합니다.
2. 필수 변수 중 하나만 설정되어 있으면 Codex는 오류를 반환합니다. API 키, 액세스 토큰 또는 저장된 로그인 정보를 대체 인증 수단으로 사용하지 않습니다.
3. `OPENAI_WORKLOAD_IDENTITY_CONTEXT`만으로는 워크로드 아이덴티티가 선택되지 않습니다.
4. 필수 WIF 변수 두 개가 모두 없으면 Codex는 해당 사용 환경의
   일반적인 자격 증명 규칙을 적용합니다. API 키 인증을 허용하는
   사용 환경에서는 `CODEX_API_KEY`가 `codex exec`,
`codex review`, TypeScript SDK, `codex exec-server --remote`에서 우선 적용됩니다. 다른
   사용 환경에서는 `CODEX_ACCESS_TOKEN` 또는 저장된 로그인 정보를 사용할 수 있습니다.

SDK의 `apiKey` 옵션은 `CODEX_API_KEY`로 변환되지만, 필수 WIF 변수가 하나라도 설정되어 있으면
WIF가 여전히 우선합니다. WIF를 사용할 때는 이 옵션을 생략해
워크로드에 사용하지 않는 장기 자격 증명이 포함되지 않도록 하세요.

기존 워크로드를 중단 없이 전환하려면 현재 자격 증명을 사용할 수 있는 상태에서 WIF를 구성하세요. 필수 WIF 변수 두 개를 모두 설정한 상태로 새 프로세스를 시작하세요. 이전 자격 증명이 남아 있어도 WIF가 우선 적용됩니다. 워크로드가 WIF로 정상적으로 실행되면 런타임과 시크릿 저장소에서 이전 자격 증명을 제거한 다음 폐기하세요. 폐기하기 전에는 필수 WIF 변수 두 개를 모두 제거하고 새 프로세스를 시작해 이전 상태로 롤백할 수 있습니다.

## 지원되는 Codex 사용 환경

Codex 프로세스가 실행되는 머신에서 워크로드 아이덴티티를 구성하세요.

| 사용 환경                                         | 지원 여부 및 호스트 경계                                                                               |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| 대화형 `codex`, `resume`, `fork`       | 지원됩니다. 구성된 환경에서 CLI를 시작하세요.                                                 |
| `codex exec`, `exec resume`, `codex review` | 지원됩니다. 필수 WIF 변수 중 하나라도 설정되어 있으면 WIF가 우선 적용됩니다.                                      |
| TypeScript SDK                                  | 지원됩니다. 부모 프로세스가 필수 WIF 변수와 선택적인 귀속 컨텍스트를 제공합니다. |
| `codex app-server`                              | 지원됩니다. 원격 클라이언트가 아니라 app-server 호스트에서 WIF를 구성하세요.                                |
| `codex exec-server --remote`                    | 원격 환경 레지스트리에 대한 인증을 지원합니다. exec-server 호스트에서 WIF를 구성하세요. |
| 로컬 exec-server 프로세스 작업            | WIF 인증을 사용하지 않습니다. 로컬 exec-server 프로토콜을 통해 실행됩니다.                         |
| `codex mcp-server`                              | 지원되지 않습니다.                                                                                          |

원격 app-server 및 exec-server 클라이언트는 자체 프로토콜을 통해 업스트림 아이덴티티 토큰을 전송하지 않습니다.

## 액세스 권한 변경 또는 제거

규칙의 주체, 대상, 클레임, CEL 조건, 권한 범위 또는 토큰 유효 기간을 변경하면 이후의 새 교환부터 적용됩니다. 변경 전에 발급된 토큰은 유효 기간이 끝날 때까지 유효할 수 있습니다.

액세스를 즉시 차단하려면 공급자 또는 규칙을 비활성화하세요. 비활성화하면 새로운 교환이 차단되고 해당 리소스를 통해 이미 발급된 OpenAI 액세스 토큰도 폐기됩니다. 보관 처리해도 액세스에 동일한 효과가 적용되며 되돌릴 수 없습니다. 공급자의 신뢰 설정을 변경하는 경우에도 새 설정이 적용되기 전에 이미 발급된 토큰이 폐기됩니다.

## 변경 사항 감사

공급자와 페더레이션 규칙을 생성, 업데이트 또는 보관 처리하면 감사
이벤트가 발생합니다. [Compliance API 및 감사 이벤트
안내](/ko-KR/codex/enterprise/compliance-api)를 참고해 워크스페이스에서 지원하는
이벤트를 내보내세요. 이벤트를 아이덴티티 공급자의 발급 로그와 대조하고,
두 시스템 어디에도 업스트림 어설션이나 OpenAI 액세스 토큰을 기록하지 마세요.

프로세스가 `OPENAI_WORKLOAD_IDENTITY_CONTEXT` 값을 제공하면 성공한
토큰 발급 감사 이벤트에도 앞서 설명한 일관된 귀속 ID와
정규화된 컨텍스트가 포함됩니다.

## 문제 해결

| 증상                                                               | 확인 사항                                                                                                              |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Codex에 워크로드 아이덴티티 구성이 불완전하다는 메시지가 표시됨              | 동일한 프로세스에 필수 변수 두 개를 모두 설정하고 토큰 파일 경로를 절대 경로로 지정하세요.                               |
| Codex에 로그인 정책에서 워크로드 아이덴티티를 허용하지 않는다는 메시지가 표시됨 | 적용되는 정책에서 ChatGPT 인증을 허용하고, 허용된 워크스페이스에 규칙의 워크스페이스를 포함하세요. |
| Codex에 다른 자격 증명이 표시됨                                      | 필수 WIF 변수 두 개를 Codex 프로세스에 모두 불러온 다음 새 프로세스를 시작하고 `codex login status` 명령어를 다시 실행하세요.  |
| OpenAI가 워크로드 컨텍스트를 거부함                                       | JSON 구조, 크기, 허용되는 문자 및 필드 제한을 확인하세요. 민감한 정보나 고객 콘텐츠를 제거하세요.            |
| OpenAI가 토큰을 거부함                                              | `iss`, `aud`, 만료 시점, 서명 키, 어설션 유효 기간을 공급자 구성과 비교하세요.               |
| 규칙이 일치하지 않음                                               | 클라이언트가 의도한 규칙 ID를 사용하고, 주체 검사, 대상 검사, 클레임 정확 일치 검사 및 CEL 검사를 모두 통과하는지 확인하세요.  |
| OpenAI가 보안 주체를 거부함                                          | 사용자 또는 서비스 계정이 활성 상태이고 선택한 워크스페이스의 활성 멤버인지 확인하세요.                   |
| OpenAI가 재사용된 어설션을 거부함                                   | 새 `jti`가 포함된 새 JWT를 발급받으세요. 재사용 방지 기능이 적용된 동일한 어설션으로 재시도하지 마세요.                                  |
| 장시간 실행되는 프로세스가 갱신을 중단함                               | 호스트 갱신 프로세스가 만료 전에 토큰 파일을 계속 교체하고 있는지 확인하세요.                                  |

공급자 검증, 제한 사항 및 CEL에 관한 자세한 내용은 [페더레이션 규칙
참조 자료](/api/docs/guides/workload-identity-federation/federation-rules)를 참조하세요.

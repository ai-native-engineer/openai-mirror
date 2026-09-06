<!-- source: https://learn.chatgpt.com/ko-KR/docs/auth -->

## OpenAI 인증

<a id="sign-in-with-chatgpt"></a>

OpenAI 모델을 사용할 때 Codex는 두 가지 로그인 방식을 지원합니다:

- 구독을 통해 이용하려면 ChatGPT로 로그인
- 사용량 기반으로 이용하려면 API 키로 로그인

ChatGPT 데스크톱 앱, Codex CLI, IDE 확장은 로컬 작업에서 두 로그인 방식을 모두 지원합니다.
Codex 클라우드는 ChatGPT로 로그인해야 합니다.

로그인 방식에 따라 적용되는 관리자 제어 및 데이터 처리 정책도 달라집니다.

- ChatGPT로 로그인하면 Codex 사용에는 ChatGPT 워크스페이스
권한과 역할 기반 접근 제어(RBAC), ChatGPT Enterprise의
데이터 보존 및 레지던시 설정이 적용됩니다.
- API 키를 사용하면 API 조직의 보존 및
데이터 공유 설정이 적용됩니다.

관리형 워크스페이스에서 인증은 액세스를 제어하는 여러 계층 중 하나일 뿐입니다.
워크스페이스 멤버십과 프로비저닝에 따라 로그인할 수 있는 사용자가 결정되며,
사용자 라이선스와 워크스페이스 역할에 따라 사용할 수 있는 제품 영역과 기능이 결정됩니다.
ChatGPT 데스크톱 앱, Codex CLI 또는 IDE 확장에서 로컬로 작업할 때는
권한 프로필이 에이전트가 기기에서 수행할 수 있는 작업을 제한합니다.
이러한 제어를 계획하려면 [그룹 및 프로비저닝](/ko-KR/codex/enterprise/groups-and-provisioning)과
[역할 및 워크스페이스 권한](/ko-KR/codex/enterprise/roles-and-workspace-permissions)을
참고하세요.

### ChatGPT로 로그인

ChatGPT 데스크톱 앱, Codex CLI 또는 IDE 확장에서 ChatGPT로 로그인하면 로그인 플로우에서 브라우저 창이 열립니다. 로그인하면 브라우저가 자격 증명을 Codex에 전달합니다.

### ChatGPT 웹

[ChatGPT](https://chatgpt.com)를 열어 로그인한 다음 작업할 워크스페이스를 선택하세요.
ChatGPT 웹은 브라우저에서 인증된 세션을 유지합니다.

#### ChatGPT 데스크톱 앱

로그아웃 상태 화면에서 **로그인 계속하기** 옵션을 선택한 다음
브라우저 플로우를 완료하세요.

#### Codex CLI

`codex login` 명령을 실행한 다음 브라우저 플로우를 완료하세요.
유효한 세션이 없을 때 사용하는 기본 인증 경로입니다.

#### IDE 확장

로그아웃 상태 화면에서 **ChatGPT로 로그인** 옵션을 선택한 다음
브라우저 플로우를 완료하세요.

<a id="sign-in-with-an-api-key"></a>

### API 키로 로그인

ChatGPT 데스크톱 앱, Codex CLI 또는 IDE 확장에 API 키로 로그인할 수도 있습니다. API 키는 [OpenAI 대시보드](https://platform.openai.com/api-keys)에서 발급받으세요.

#### ChatGPT 데스크톱 앱

로그아웃 상태 화면에서 **다른 방법으로 로그인** 옵션을 선택하고 키를 입력한 다음
 **계속** 버튼을 선택하세요.

#### Codex CLI

키를 `codex login` 명령의 stdin으로 파이프하세요:

```shell
printenv OPENAI_API_KEY | codex login --with-api-key

#### IDE 확장

로그아웃 상태 화면에서 **API 키 사용** 옵션을 선택하고 키를 입력한 다음
**확인** 버튼을 선택하세요.

OpenAI는 API 키 사용량을 OpenAI Platform 계정에 표준 API 요금으로 청구합니다. 자세한 내용은 [API 요금 페이지](https://openai.com/api/pricing/)를 참고하세요.

API 키 인증은 로컬 Codex 워크플로우를 지원하지만,
ChatGPT 워크스페이스 액세스나 클라우드 서비스에 의존하는 일부 기능은 제한되거나 사용할 수 없습니다.
플랜별 지원 여부는
[기능 제공 여부](/ko-KR/codex/pricing#feature-availability)에서 비교하세요.

Codex CLI와 ChatGPT 데스크톱 앱의 Codex에서 API 키 인증을 사용하면
OpenAI가 엄선한 지원 대상 플러그인에 액세스할 수 있습니다. 일부 플러그인은
연결 플로우에 지원되지 않는 OAuth 기능이
필요하므로 사용할 수 없습니다. 자세한 내용은 [플러그인 사용](/ko-KR/codex/plugins#api-key-availability)을 참고하세요.

API 키로 로그인하면 Codex에는 ChatGPT 플랜에 포함된 크레딧 대신
표준 API 요금이 적용됩니다.

CI/CD 작업과 같은 프로그래밍 방식의 Codex CLI 워크플로우에는 API 키 인증을 사용하세요.
신뢰할 수 없거나 공개된 환경에 Codex 실행을 노출하지 마세요.

### 인증 확인 또는 로그아웃

프로필 메뉴를 열어 활성 계정과 워크스페이스를 확인하세요.
해당 브라우저에서 ChatGPT 웹 세션을 종료하려면 **로그아웃** 옵션을 선택하세요.

프로필 메뉴를 열어 활성 계정 또는 API 키 상태를 확인하세요.
현재 자격 증명을 삭제하려면 **로그아웃** 옵션을 선택하세요.

`codex login status` 명령을 실행해 현재 인증 방식을 확인하세요. 저장된
인증 정보의 경우 `codex logout` 명령을 실행해 현재 자격 증명을 삭제하세요.
프로세스에서 워크로드 ID를 선택하면 인증은 프로세스 환경에서 제어하므로 Codex는 `codex login`과
`codex logout` 명령을 거부합니다.

프로필 메뉴를 열어 활성 계정 또는 API 키 상태를 확인하세요.
현재 자격 증명을 삭제하려면 **로그아웃** 옵션을 선택하세요.

### 엔터프라이즈 자동화에 Codex 액세스 토큰 사용

ChatGPT Enterprise 워크스페이스에서는 관리자가 액세스 토큰 권한을 부여해
허가받은 멤버가 신뢰할 수 있는 비대화형 Codex 로컬 워크플로우용
Codex 액세스 토큰을 만들도록 할 수 있습니다. 브라우저 로그인 없이 자동화에
ChatGPT 워크스페이스 액세스, ChatGPT에서 관리하는 Codex 사용 권한 또는
엔터프라이즈 워크스페이스 제어가 필요한 경우 액세스 토큰을 사용하세요.

액세스 토큰은 신뢰할 수 있는 스크립트, 스케줄러, 비공개 CI 러너에서 사용하기 위한 것입니다.
일반적인 OpenAI API 호출에는 계속 Platform API 키를 사용하세요.

설정 단계, 권한, 교체 및 취소 지침은
[액세스 토큰](/ko-KR/codex/enterprise/access-tokens)을 참고하세요.

클라우드 플랫폼, CI 시스템 또는 클러스터에서 수명이 짧은
워크로드 토큰을 이미 발급한다면 OpenAI 자격 증명을 저장하는 대신
[워크로드 ID 페더레이션](/ko-KR/codex/enterprise/workload-identity)을
사용하세요.

환경에서 이미 Codex 액세스 토큰을 제공하는 경우 이를 CLI로 파이프하세요:

```shell
printenv CODEX_ACCESS_TOKEN | codex login --with-access-token

## Codex 클라우드 계정 보안 강화

Codex 클라우드는 코드베이스와 직접 상호작용하므로 다른 여러 ChatGPT 기능보다 더 강력한 보안이 필요합니다. 다중 인증(MFA)을 사용 설정하세요.

소셜 로그인 제공업체(Google, Microsoft, Apple)를 사용하는 경우 ChatGPT 계정에서 다중 인증(MFA)을 사용 설정하지 않아도 되지만, 소셜 로그인 제공업체에서 설정할 수 있습니다.

설정 방법은 다음을 참고하세요:

- [Google](https://support.google.com/accounts/answer/185839)
- [Microsoft](https://support.microsoft.com/en-us/topic/what-is-multifactor-authentication-e5e39437-121c-be60-d123-eda06bddf661)
- [Apple](https://support.apple.com/en-us/102660)

통합 로그인(SSO)으로 ChatGPT에 액세스하는 경우 조직의 SSO 관리자는 모든 사용자에게 다중 인증(MFA)을 적용해야 합니다.

이메일과 비밀번호로 로그인하는 경우 Codex 클라우드에 액세스하기 전에 계정에 다중 인증(MFA)을 설정해야 합니다.

계정에서 여러 로그인 방식을 지원하며 그중 하나가 이메일과 비밀번호인 경우, 다른 방식으로 로그인하더라도 Codex에 액세스하기 전에 다중 인증(MFA)을 설정해야 합니다.

<a id="login-caching"></a>

## 로그인 정보 캐싱

ChatGPT 또는 API 키로 ChatGPT 데스크톱 앱, Codex CLI 또는 IDE 확장에 로그인하면 로그인 정보가 캐시되어 재사용됩니다. CLI와 확장은 동일한 캐시된 로그인 정보를 공유합니다. 둘 중 하나에서 로그아웃하면 다음에 CLI나 확장을 시작할 때 다시 로그인해야 합니다.

Codex는 로그인 정보를 로컬의 일반 텍스트 파일인 `~/.codex/auth.json` 또는 운영체제별 자격 증명 저장소에 캐시합니다.

ChatGPT로 로그인한 세션에서는 Codex가 사용 중 토큰이 만료되기 전에 자동으로 갱신하므로, 활성 세션은 일반적으로 브라우저에서 다시 로그인하지 않아도 계속 유지됩니다.

<a id="credential-storage"></a>
<a id="enforce-a-login-method-or-workspace"></a>

## 자격 증명 저장

`cli_auth_credentials_store` 설정으로 Codex CLI의 캐시된 자격 증명 저장 위치를 지정하세요:

```toml
# file | keyring | auto
cli_auth_credentials_store = "keyring"

- `file`은 자격 증명을 `auth.json` 파일에 저장합니다. 파일은 `CODEX_HOME` 아래에 위치하며, 기본 경로는 `~/.codex`입니다.
- `keyring`은 자격 증명을 운영체제의 자격 증명 저장소에 저장합니다.
- `auto`는 운영체제의 자격 증명 저장소를 사용할 수 있으면 이를 사용하고, 사용할 수 없으면 `auth.json` 파일을 대신 사용합니다.

전체 `config.toml` 스키마는
[구성 참조 자료](/ko-KR/codex/config-file/config-reference)에서 확인하세요.

  파일 기반 저장소를 사용하는 경우 `~/.codex/auth.json` 파일을 비밀번호처럼 취급하세요.
  이 파일에는 액세스 토큰이 포함되어 있습니다. 커밋하거나 티켓에 붙여 넣거나
  채팅으로 공유하지 마세요.

## 로그인 방법 또는 워크스페이스 제한 적용

관리형 환경에서 관리자는 사용자의 인증 방식을 제한할 수 있습니다:

```toml
# Only allow ChatGPT login or only allow API key login.
forced_login_method = "chatgpt" # or "api"

# When using ChatGPT login, restrict users to a specific workspace.
forced_chatgpt_workspace_id = "00000000-0000-0000-0000-000000000000"

현재 자격 증명이 구성된 제한 사항과 일치하지 않으면 Codex는 사용자를 로그아웃시키고 종료됩니다.

이러한 설정은 보통 사용자별 설정보다는 관리형 구성을 통해 적용합니다. [관리형 구성](/ko-KR/codex/enterprise/managed-configuration)을 참고하세요.

## 로그인 진단

`codex login` 명령을 직접 실행하면 설정된 로그 디렉터리에
전용 `codex-login.log` 파일이 생성됩니다. 브라우저 로그인 또는 기기 코드 오류를
디버깅하거나 지원팀에서 로그인 관련 로그를 요청할 때 이 파일을 사용하세요.

## 사용자 지정 CA 번들

네트워크에서 기업용 TLS 프록시 또는 사설 루트 CA를 사용하는 경우 로그인하기 전에
`CODEX_CA_CERTIFICATE` 값을 PEM 번들로 설정하세요.
`CODEX_CA_CERTIFICATE`가 설정되지 않았으면 Codex는 `SSL_CERT_FILE`을 대신 사용합니다.
동일한 사용자 지정 CA 설정이 로그인, 일반 HTTPS 요청, 보안 WebSocket
연결에 적용됩니다.

```shell

codex login

## 헤드리스 기기에서 로그인

Codex CLI로 ChatGPT에 로그인할 때 다음과 같은 상황에서는 브라우저 기반 로그인 UI가 작동하지 않을 수 있습니다:

- 원격 또는 헤드리스 환경에서 CLI를 실행하고 있습니다.
- 로컬 네트워크 구성으로 인해 로그인 후 OAuth 토큰을 CLI로 반환할 때 Codex가 사용하는 로컬호스트 콜백이 차단됩니다.

이러한 경우 기기 코드 인증(베타)을 우선 사용하세요. 대화형 로그인 UI에서 **기기 코드로 로그인** 옵션을 선택하거나 `codex login --device-auth` 명령을 직접 실행하세요. 사용 중인 환경에서 기기 코드 인증이 작동하지 않으면 대체 방법 중 하나를 사용하세요.

### 권장: 기기 코드 인증(베타)

1. ChatGPT 보안 설정(개인 계정) 또는 ChatGPT 워크스페이스 권한(워크스페이스 관리자)에서 기기 코드 로그인을 활성화하세요.
2. Codex를 실행 중인 터미널에서 다음 옵션 중 하나를 선택하세요:
   - 대화형 로그인 UI에서 **기기 코드로 로그인** 옵션을 선택하세요.
   - `codex login --device-auth` 명령을 실행하세요.
3. 브라우저에서 링크를 열고 로그인한 다음 일회용 코드를 입력하세요.

사용 중인 환경에서 기기 코드 로그인을 사용할 수 없다면 아래의
대체 방법 중 하나를 사용하세요.

### 대체 방법: 로컬에서 인증한 후 인증 캐시 복사

브라우저가 있는 머신에서 로그인 플로우를 완료할 수 있다면 캐시된 자격 증명을 헤드리스 머신으로 복사할 수 있습니다.

1. 브라우저 기반 로그인 플로우를 사용할 수 있는 머신에서 `codex login` 명령을 실행하세요.
2. 로그인 캐시가 `~/.codex/auth.json` 경로에 있는지 확인하세요.
3. `~/.codex/auth.json` 파일을 헤드리스 머신의 `~/.codex/auth.json` 경로로 복사하세요.

`~/.codex/auth.json` 파일을 비밀번호처럼 취급하세요. 이 파일에는 액세스 토큰이 포함되어 있습니다. 커밋하거나 티켓에 붙여 넣거나 채팅으로 공유하지 마세요.

운영체제에서 자격 증명을 `~/.codex/auth.json` 파일이 아닌 자격 증명 저장소에 저장하는 경우 이 방법이 적용되지 않을 수 있습니다.
파일 기반 저장소 구성 방법은 [자격 증명 저장](/ko-KR/codex/auth#credential-storage)을 참고하세요.

SSH를 통해 원격 머신으로 복사하세요:

```shell
ssh user@remote 'mkdir -p ~/.codex'
scp ~/.codex/auth.json user@remote:~/.codex/auth.json

또는 `scp` 없이 실행할 수 있는 한 줄 명령을 사용하세요:

```shell
ssh user@remote 'mkdir -p ~/.codex && cat > ~/.codex/auth.json' < ~/.codex/auth.json

Docker 컨테이너로 복사하세요:

```shell
# Replace MY_CONTAINER with the name or ID of your container.
CONTAINER_HOME=$(docker exec MY_CONTAINER printenv HOME)
docker exec MY_CONTAINER mkdir -p "$CONTAINER_HOME/.codex"
docker cp ~/.codex/auth.json MY_CONTAINER:"$CONTAINER_HOME/.codex/auth.json"

신뢰할 수 있는 CI/CD 러너에서 이 패턴을 더 고급 방식으로 활용하는 방법은
[CI/CD에서 Codex 계정 인증 유지(고급)](/codex/auth/ci-cd-auth)을 참고하세요.
이 가이드에서는 일반 실행 중 Codex가 `auth.json` 파일을 갱신하고
업데이트된 파일을 다음 작업을 위해 보관하는 방법을 설명합니다. 자동화에는 여전히
API 키를 기본으로 사용하는 것이 좋습니다.

### 대체 방법: SSH를 통한 로컬호스트 콜백 포워딩

로컬 머신과 원격 호스트 간에 포트를 포워딩할 수 있다면 Codex의 로컬 콜백 서버(기본값: `localhost:1455`)를 터널링하여 표준 브라우저 기반 플로우를 사용할 수 있습니다.

1. 로컬 머신에서 포트 포워딩을 시작하세요:

```shell
ssh -L 1455:localhost:1455 user@remote

2. 해당 SSH 세션에서 `codex login` 명령을 실행한 다음 출력된 주소를 로컬 머신에서 여세요.

## 대체 모델 제공업체

구성 파일에서 [사용자 지정 모델 제공업체](/ko-KR/codex/config-file/config-advanced#custom-model-providers)를 정의할 때 다음 인증 방법 중 하나를 선택할 수 있습니다:

- **OpenAI 인증**: OpenAI 인증을 사용하려면 `requires_openai_auth = true`로 설정하세요. 그러면 ChatGPT 또는 API 키로 로그인할 수 있습니다. LLM 프록시 서버를 통해 OpenAI 모델에 액세스할 때 유용합니다. `requires_openai_auth = true`로 설정하면 Codex는 `env_key` 값을 무시합니다.
- **환경 변수 인증**: 로컬 환경의 `<ENV_VARIABLE_NAME>` 환경 변수에 저장된 제공업체별 API 키를 사용하려면 `env_key = "<ENV_VARIABLE_NAME>"` 설정을 적용하세요.
- **인증 없음**: `requires_openai_auth` 값을 설정하지 않거나 `false`로 설정하고 `env_key` 값도 설정하지 않으면 Codex는 해당 제공업체에 인증이 필요하지 않다고 간주합니다. 로컬 모델에 유용합니다.

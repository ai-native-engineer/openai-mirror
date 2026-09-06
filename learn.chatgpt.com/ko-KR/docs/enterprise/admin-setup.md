<!-- source: https://learn.chatgpt.com/ko-KR/docs/enterprise/admin-setup -->

이 가이드를 참고해 다음 관리 영역별로 ChatGPT Enterprise 도입을 계획하세요:

- 워크스페이스 액세스.
- ChatGPT 데스크톱 앱, Codex CLI, IDE 확장의 적용 대상 기능에 대한 로컬 런타임 정책.
- Codex 클라우드.
- Platform API 액세스.
- 플러그인 및 커넥터 액세스.
- 연결된 시스템의 권한.

새로 도입할 때는 단계를 순서대로 완료하세요. 특정 영역만 변경하려면 링크된 문서를 참조하세요.

워크스페이스 설정의 **Codex 및 Work 로컬** 섹션에서는 Codex와 Work의 로컬
액세스를 **멤버의 Codex 및 Work 로컬 사용 허용** 항목으로 함께 관리합니다. 일부 워크스페이스에서는
 **Codex 로컬** 및 **Work 로컬** 섹션을 별도로 제공합니다. 이 경우
 **멤버의 Codex 로컬 사용 허용** 항목은 Codex를, **Work 로컬
사용** 항목은 Work를 제어합니다. 어느 한쪽을 활성화해도 다른 쪽이 활성화되지는 않습니다.
이 레이블은 워크스페이스 권한을 나타내며, 별도의 제품이나 클라이언트를 의미하지 않습니다.
토큰 권한과 자격 증명 유효 기간 제한은 워크스페이스에 따라 **액세스
토큰** 섹션이나 로컬 액세스 섹션에 표시됩니다.
관리형 구성은 별도의 정책 계층으로, 해당 클라이언트의 적용 대상 기능에 대해
지원되는 런타임 동작을 제한할 수 있습니다. 이 가이드에서는 동작이나 제공 여부가 다르면
각 환경을 구체적으로 명시합니다.

먼저
[역할 및 워크스페이스 권한](/ko-KR/codex/enterprise/roles-and-workspace-permissions)에서 기준이 되는 권한 체계를 확인하세요.
ChatGPT 워크스페이스의 최신 절차는 도움말 센터 지침을, 로컬 및 호스팅 런타임의
동작은 링크된 개발자 문서를 참조하세요.

<a id="enterprise-grade-security-and-privacy"></a>

엔터프라이즈 보안, 개인정보 보호 및 런타임 보호 조치는
[에이전트 승인 및 보안](/ko-KR/codex/agent-approvals-security)과
[Codex 보안 백서](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click)를 참조하세요.

<a id="pre-requisites-determine-owners-and-rollout-strategy"></a>

## 1단계: 책임자 지정 및 도입 방식 선택

도입 과정의 각 영역에 책임자를 지정하세요:

- **워크스페이스 액세스:** 멤버십, 시트, 역할 및 지원되는
  워크스페이스 기능.
- **로컬 런타임 정책:** 승인, 권한 프로필, 파일 시스템 및
  네트워크 액세스와 지원되는 로컬 클라이언트의 기타 요구 사항.
- **Codex 클라우드:** 호스팅 환경, 레포지토리 연결 및 클라우드
  런타임 정책.
- **연결된 시스템:** 공급자 측 애플리케이션 설치, 계정 및
  권한.
- **보고 및 컴플라이언스:** 분석 기능 액세스, 감사 데이터 내보내기 및
  다운스트림 데이터 처리.

각 대상 그룹에 ChatGPT 데스크톱 앱, Codex CLI, IDE 확장의 적용 대상 로컬 기능과 Codex 클라우드 중 무엇이 필요한지, 여러 환경을 함께 사용해야 하는지 결정하세요. 워크플로우에서 API 키 인증을 사용하는 경우 Platform API 액세스는 별도의 조직 및 프로젝트 단위로 관리하세요.

## 2단계: 워크스페이스 액세스 및 ID 구성

ChatGPT 워크스페이스의 멤버십, 시트, 그룹 및 지원되는 RBAC 권한을 사용해 대상 그룹이 지원되는 워크스페이스 기능을 사용할 수 있도록 하세요. 동일한 역할이 모든 환경을 제어한다고 가정하지 말고, 최신 워크스페이스 지침에 따라 로컬 클라이언트와 Codex 클라우드 액세스를 확인하세요. 기본 제공 관리자 역할은 워크스페이스를 관리하는 사람에게만 부여하세요.

워크스페이스의 제어 항목과 레이블은 시간이 지나면서 변경됩니다. 최신 절차는 다음 자료를 참조하세요:

- [멤버, 시트 유형, 역할 및 액세스 관리](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [역할 기반 접근 제어 구성](https://help.openai.com/en/articles/11750701-rbac)
- [워크스페이스 설정 관리](https://help.openai.com/en/articles/8411955)
- [그룹 및 프로비저닝](/ko-KR/codex/enterprise/groups-and-provisioning)
- [사용자 수명 주기 관리](/ko-KR/codex/enterprise/user-lifecycle)
- [인증](/ko-KR/codex/auth)

도입 범위를 확대하기 전에 대상 그룹을 대표하는 멤버로 로그인과 기능 액세스를 테스트하세요. 워크스페이스 액세스만으로는 연결된 서비스의 레포지토리나 파일에 액세스하거나 작업을 실행할 권한이 부여되지 않습니다.

## 3단계: 로컬 런타임 요구 사항 구성

로컬 요구 사항은 사용자가 ChatGPT 데스크톱 앱, Codex CLI 또는 IDE 확장에서
지원되는 로컬 실행을 시작할 때 런타임 동작을 제한합니다. 지원되는 클라우드, 기기 또는 시스템 채널을 통해
`requirements.toml` 파일을 배포하세요. 이 정책은
ChatGPT 워크스페이스의 역할 및 그룹과 별도로 유지하세요.

새로 배포할 때는 레거시 샌드박스 모드 제한을 기반으로 구성하는 대신 지원되는 로컬 클라이언트의 권한 프로필을 사용하세요. 예를 들면 다음과 같습니다:

```toml
default_permissions = ":workspace"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true

지원되는 브라우저 및 데스크톱 환경 전반에서 컴퓨터 사용을 비활성화하려면 이 기능에 관여하는 공개 기능 키를 각각 제한하세요:

```toml
[features]
browser_use = false
browser_use_full_cdp_access = false
browser_use_external = false
in_app_browser = false
computer_use = false

공식 키 목록, 전달 방식, 우선순위와
추가 예시는
[관리형 구성](/ko-KR/codex/enterprise/managed-configuration) 및
[`requirements.toml` 참조 자료](/ko-KR/codex/config-file/config-reference#requirementstoml)에서 확인하세요.

<a id="team-config"></a>
<a id="step-4-standardize-local-configuration-with-team-config"></a>

## 4단계: 레포지토리 구성 표준화

레포지토리 범위 구성을 사용하면 사용자마다 설정을 반복하지 않고 프로젝트 기본값, 규칙 및
스킬을 공유할 수 있습니다. 각 기능의 문서에 명시된 위치에 따라
`.codex` 또는 `.agents`에 구성을 체크인하세요:

| 유형          | 참고 자료                                           | 용도                                                  |
| ------------- | ------------------------------------------------ | ---------------------------------------------------------- |
| 구성 | [기본 구성](/ko-KR/codex/config-file/config-basic) | 지원되는 로컬 클라이언트의 레포지토리 기본값 설정        |
| 규칙         | [규칙](/ko-KR/codex/agent-configuration/rules)        | 샌드박스 외부에서 승인이 필요한 명령어 제어 |
| 스킬        | [스킬 빌드하기](/ko-KR/codex/build-skills)              | 지원되는 클라이언트에서 레포지토리 워크플로우를 사용할 수 있도록 설정   |

레포지토리 구성은 기본값과 재사용 가능한 워크플로우를 제공할 수 있습니다. 워크스페이스, 모델, Platform API 또는 연결된 시스템에 대한 액세스 권한은 부여할 수 없습니다.

## 5단계: Codex 클라우드 구성

Codex 클라우드는 호스팅 환경과 연결된 소스 레포지토리를 사용합니다. 각 관리 영역을 다음과 같이 계획하세요:

1. 지원되는 워크스페이스 제어 항목을 통해 대상 그룹에 Codex 클라우드 액세스 권한을 부여하세요.
2. 지원되는 소스 시스템 통합을 설치하고 구성하세요.
3. 소스 시스템에서 각 대상 그룹이 필요한 레포지토리에만 액세스할 수 있도록 제한하세요.
4. 해당 레포지토리의 클라우드 환경, 시크릿 및 인터넷 액세스를 구성하세요.
5. 코드 검토와 같은 선택적 호스팅 워크플로우를 구성하세요.
6. 의도한 워크스페이스 및 레포지토리 권한을 보유하고 대상 그룹을 대표하는 사용자로 테스트하세요.

Codex 클라우드는 연결된 소스 시스템에서 제공하는 레포지토리 권한과
보호 조치를 준수합니다. 워크스페이스 액세스로는 이러한 제어를 우회할 수 없습니다.
Codex 클라우드 설정 및 런타임 지침은 [클라우드 환경](/ko-KR/codex/environments/cloud-environment),
[GitHub 통합](/ko-KR/codex/third-party/github),
[에이전트 승인 및 보안](/ko-KR/codex/agent-approvals-security) 문서에서
확인하세요.

## 6단계: 플러그인 및 연결된 기능 구성

플러그인 설치, 번들 스킬, 커넥터 기반 기능, 커넥터 작업, 소스 시스템의 권한 부여를 각각 별도의 결정 사항으로 검토하세요. 커넥터 기반 기능을 비활성화해도 플러그인이나 번들 스킬이 반드시 제거되는 것은 아닙니다.

도입 대상에 플러그인이나 스킬을 포함하기 전에 다음을 확인하세요:

1. 출처, 책임자, 대상 그룹 및 검토 날짜를 확인하세요.
2. 번들로 제공되는 스킬, 커넥터, MCP 서버, 훅과 각 기능에 필요한 데이터 및 액션을 검토하세요.
3. 민감하지 않은 데이터와 필요한 최소한의 액세스 권한으로 테스트하세요.
4. 재검토와 사용 종료 담당자를 기록하세요.

플러그인은 웹, 데스크톱, 모바일용 ChatGPT의 채팅과 Work, ChatGPT 데스크톱 앱의 Codex, Codex CLI 플러그인 브라우저에서 사용할 수 있습니다.
IDE 확장에서는 사용할 수 없습니다.
ChatGPT와 Codex는 하나의 공통 공개 플러그인 디렉터리를 공유하며, 워크스페이스 제어에 따라 멤버가 액세스할 수 있는 플러그인이 결정됩니다.

전체 체계는 [플러그인 제어](/ko-KR/codex/enterprise/apps-and-connectors)와
[스킬 제어](/ko-KR/codex/enterprise/skills)를 참조하세요.

## 7단계: 거버넌스 및 관측 가능성 설정

확인하려는 내용에 맞는 보고 수단을 선택하세요:

<a id="analytics-api-setup-steps"></a>
<a id="compliance-api-setup-steps"></a>

- ChatGPT 워크스페이스 분석과 Codex 분석을 대화형으로 살펴보려면
  [워크스페이스 분석](/ko-KR/codex/enterprise/workspace-analytics)을 사용하세요.
- Codex 분석 API를 통해 프로그래밍 방식으로 집계 보고를 수행하려면
  [분석 API](/ko-KR/codex/enterprise/analytics-api)를 사용하세요.
- 감사 및 조사 기록에는
  [Compliance API](/ko-KR/codex/enterprise/compliance-api)를 사용하세요.
- 플랜에 따라 Codex 활동이 사용 가능한 ChatGPT 워크스페이스
  크레딧을 소모하는 경우에는
  [ChatGPT 사용 한도 및 지출 제어](/ko-KR/codex/enterprise/usage-limits)를 사용하세요.

현재 액세스 요구 사항, 스키마, 필드, 보존 기간 및 요청 동작은 인증 후 열람할 수 있는 API 레퍼런스에서 확인하세요. 이 가이드에 복사된 API 명세를 기반으로 연동을 구축하지 마세요.

연동 경계를 보호하세요:

- API 키와 기타 연동 자격 증명은 조직의 시크릿 관리 시스템에 저장하세요.
- 다운스트림 시스템과 보존된 데이터에 대한 액세스를 승인된 사용자로 제한하세요.
- 내보낸 Compliance API 기록은 민감도와 조직의 보존 정책에 따라 보호하고, 현재 API 명세를 기준으로 수집 및 삭제 워크플로우를 테스트하세요.

## 8단계: 롤아웃 검증 및 유지 관리

대표 계정을 사용해 해당하는 모든 관리 영역을 검증하세요:

- ChatGPT 워크스페이스 멤버십, 시트 및 지원되는 역할 권한.
- ChatGPT 데스크톱 앱, Codex CLI 및 IDE 확장의 적용 대상 로컬 기능(로그인 및 실제로 적용되는 런타임 요구 사항 포함).
- Codex 클라우드 액세스, 환경 구성 및 레포지토리 권한.
- API 키를 사용하는 워크플로우에 필요한 Platform API 조직 및 프로젝트 액세스.
- 플러그인 설치, 번들로 제공되는 스킬, 커넥터 액세스 및 지원되는 액션.
- 연결된 시스템의 권한 부여 및 데이터 액세스.
- 담당 관리자의 분석 및 컴플라이언스 액세스 권한.

각 제어 항목의 담당자와 최신 절차를 확인할 수 있는 출처를 기록하세요. 이 기록을 바탕으로 관리자는 UI나 정책이 바뀔 때 관리 체계를 변경하지 않고 절차를 업데이트할 수 있습니다.

초기 롤아웃 후 액세스, 연결된 기능, 크레딧 사용량, 지원 관련 피드백과 팀이 실제로 사용하는 워크플로우를 검토하세요. 이러한 사항이 달라지면 롤아웃 범위와 관리자 지침을 조정하세요.

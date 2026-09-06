<!-- source: https://learn.chatgpt.com/ko-KR/docs/enterprise/workspace-model-availability -->

사용할 수 있는 모델은 제품 사용 환경과 로그인 방식에 따라 달라집니다. ChatGPT 워크스페이스의 모델 설정은 ChatGPT 데스크톱 앱의 Codex, Codex CLI, IDE 확장, Codex 클라우드 또는 OpenAI API에 자동으로 적용되지 않습니다.

전체 관리 체계는
[역할 및 워크스페이스 권한](/ko-KR/codex/enterprise/roles-and-workspace-permissions)을 참조하세요.

## 모델 액세스의 적용 범위 확인하기

| 제품 또는 인증 범위                                                         | 모델 액세스 결정 기준                                                                                  | 최신 정보 출처                                                                                                                |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| ChatGPT 워크스페이스                                                                          | 워크스페이스 플랜, 멤버의 액세스 권한, 워크스페이스 설정 및 지원되는 역할 권한                 | [ChatGPT Enterprise 및 Edu 모델과 한도](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-models-limits) |
| ChatGPT 로그인으로 사용하는 ChatGPT 데스크톱 앱의 Codex, Codex CLI 및 IDE 확장        | 해당 클라이언트가 지원하는 모델 및 로그인한 ChatGPT 계정에 부여된 액세스 권한    | [Codex 모델](/ko-KR/codex/models) 및 최신 워크스페이스 지침                                                                  |
| Codex 클라우드                                                                                | 호스팅된 Codex 워크플로우가 지원하는 모델 및 로그인한 ChatGPT 계정에 부여된 액세스 권한 | [Codex 모델](/ko-KR/codex/models) 및 [Codex 클라우드](/ko-KR/codex/cloud)                                                                 |
| API 키 인증으로 사용하는 ChatGPT 데스크톱 앱의 Codex, Codex CLI 및 IDE 확장 | 해당 키에 연결된 OpenAI API 조직 및 프로젝트                                       | [인증](/ko-KR/codex/auth) 및 [API 플랫폼](https://platform.openai.com/docs/overview)                        |

사용자가 실제로 이용하는 제품 환경에 해당하는 최신 정보 출처를 확인하세요. 모델 카탈로그를 그대로 복사하거나 ChatGPT 모델 선택기 설정이 ChatGPT 데스크톱 앱의 Codex, Codex CLI, IDE 확장, Codex 클라우드 및 API 플랫폼에도 동일하게 적용된다고 가정하지 마세요.

## 직원의 초기 사용 환경을 명확하게 설정하기

시범 그룹을 초대하기 전에 워크스페이스의 [모델 설정](https://help.openai.com/en/articles/8411955)을
검토하세요. 워크스페이스 소유자와 관리자는 채팅용 초기 기본값과
Work 및 Codex용 초기 기본값을 각각 설정할 수 있습니다. 지원되는 경우
채팅, Work 및 로컬 Codex 사용 환경의 초기 모델, 추론 수준,
속도와 새 채팅 동작을 선택하세요.

이러한 선택은 권한이 아닌 기본값으로 간주하세요. 사용할 수 있는 모델은 여전히 멤버의 시트와 역할, 워크스페이스 또는 API 계정, 강제 적용되는 워크스페이스 요구 사항, 사용 중인 제품 환경에 따라 달라집니다. 초기 기본값으로는 사용할 수 없는 모델에 대한 액세스 권한을 부여하거나 해당 요구 사항을 무시할 수 없습니다. Codex 클라우드는 기본 모델 변경을 지원하지 않습니다.

패스트 모드 사용 가능 여부는 워크스페이스와 제품 사용 환경, 그리고
[`requirements.toml`](/ko-KR/codex/config-file/config-reference#requirementstoml)에서 강제 적용되는
`features.fast_mode` 설정에 따라 달라집니다.
이 설정으로 관리형 로컬 Codex 클라이언트의 패스트 모드를 켜짐 또는 꺼짐으로 고정할 수 있습니다.
이는 초기 기본값이 아니며 워크스페이스나 제품에서 허용하는 사용 가능 범위를 바꿀 수 없습니다.

## 엔터프라이즈에서 GPT-6 Astra 사용하기

초기 출시 기간에는 조직에 Daybreak 액세스 권한이 있어야
관리자가 Astra를 활성화할 수 있습니다. ChatGPT Enterprise에서는
출시 후 첫 2주 동안 Astra가 기본적으로 꺼져 있습니다. 자격 요건을 충족하는
워크스페이스의 관리자는 사용자 또는 그룹을 대상으로
채팅, Work 및 Codex에서 Astra를 활성화할 수 있습니다. 기존 제품 이용 자격 요건은 그대로 적용됩니다.
[워크스페이스 모델 설정](https://help.openai.com/en/articles/8411955)을 검토하고
시범 그룹이 사용하는 각 클라이언트에서 이용 가능한지 확인하세요.

액세스를 활성화하는 것과 초기 모델을 선택하는 것은 별개의 결정입니다.
Astra를 기본값으로 설정하기 전에 해당 시트, 역할 및 과금 방식을 확인하세요.
사용 한도와 과금 안내는 [요금](/ko-KR/codex/pricing)을 참조하고,
검토를 위해 일시 중지되는 작업에 대해서는
[안전 모니터링](/ko-KR/codex/agent-approvals-security#safety-monitoring-and-paused-tasks)을 참조하세요.

API 키로 로그인하는 경우 Astra 액세스는 해당 키에 연결된 API 조직과 프로젝트에 따라 결정됩니다. ChatGPT 워크스페이스에서 Astra를 활성화해도 API 액세스 권한이 부여되지는 않습니다. API 키를 통한 조기 액세스에는 클라이언트 구성도 필요합니다. 설정 방법은 OpenAI 계정 담당팀에 문의하세요. 모델을 선택하거나 로컬 구성을 변경하는 것만으로는 액세스 권한이 부여되지 않습니다.

## GPT-5.4 제공 종료에 대비하기

2026년 8월 31일부터 ChatGPT로 로그인한 사용자는 Codex에서 GPT-5.4와 GPT-5.4 mini를 더 이상 사용할 수 없습니다. 그 전에 영향을 받는 워크스페이스 기본값, 저장된 모델 설정, 관리형 구성, 맞춤형 에이전트와 예약 작업을 업데이트하세요:

- `gpt-5.4`를 `gpt-5.6-terra`(GPT-5.6 Terra)로 교체하세요.
- `gpt-5.4-mini`를 `gpt-5.6-luna`(GPT-5.6 Luna)로 교체하세요.

OpenAI API와 자체 API 키로 인증한 Codex에는 영향이 없습니다.
마이그레이션에 대한 자세한 내용은
[Codex 모델](/ko-KR/codex/models#deprecated-codex-models)과
[관리형 구성](/ko-KR/codex/enterprise/managed-configuration)을 참조하세요.

## 모델 액세스와 런타임 권한 구분하기

모델 액세스는 지원되는 제품 환경에서 인증된 사용자가 모델을 사용할 수 있는지를 결정합니다. 로컬 권한 프로필과 관리형 요구 사항은 로컬 실행이 시작된 후 에이전트가 수행할 수 있는 작업을 결정합니다. 여기에는 변경 가능한 파일과 접근 가능한 네트워크 대상 등이 포함됩니다.

권한 프로필로는 모델 액세스를 부여할 수 없습니다. 모델 액세스 역시 실행에 적용되는 샌드박스, 승인 정책, 네트워크 제어 또는 소스 시스템 권한을 완화할 수 없습니다.

## 모델 액세스 문제 해결하기

사용자가 예상한 모델을 선택할 수 없는 경우:

- 제품 사용 환경과 로그인 방식을 확인하세요.
- ChatGPT 워크스페이스 또는 플랫폼 API 조직과 프로젝트를 확인하세요.
- 해당 인증 범위에 적용되는 현재 액세스 제어를 검토하세요.
- 선택한 로컬 클라이언트나 Codex 클라우드에서 해당 모델을 지원하는지 확인하세요.

## 최신 정보 출처

- [ChatGPT Enterprise 및 Edu 모델과 한도](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-models-limits)
- [워크스페이스 설정 관리](https://help.openai.com/en/articles/8411955)
- [역할 기반 접근 제어](https://help.openai.com/en/articles/11750701-rbac)
- [Codex 모델](/ko-KR/codex/models)
- [플랜별 Codex 기능 사용 가능 여부](/ko-KR/codex/pricing#feature-availability)
- [인증](/ko-KR/codex/auth)

## 관련 문서

- [관리자용 도입 가이드](/ko-KR/codex/enterprise/admin-setup)
- [그룹 및 프로비저닝](/ko-KR/codex/enterprise/groups-and-provisioning)
- [역할 및 워크스페이스 권한](/ko-KR/codex/enterprise/roles-and-workspace-permissions)
- [관리형 구성](/ko-KR/codex/enterprise/managed-configuration)

<!-- source: https://learn.chatgpt.com/ko-KR/docs/enterprise/service-accounts -->

서비스 계정을 사용하면 직원 계정에 의존하지 않고 조직 전체에서 헤드리스 Codex 워크플로우를 실행하고 확장할 수 있습니다. 각 지속적 통합(CI) 러너, 예약 작업, 공유 연동에는 독립된 ChatGPT 워크스페이스 계정이 부여되며, 일반 사용자와 동일한 그룹, 역할, 접근 제어 및 감사 추적 기능이 적용됩니다.

워크스페이스 소유자와 관리자만 서비스 계정을 만들 수 있습니다. 다른 사용자나 그룹에 계정 관리, 플러그인 설정, 액세스 토큰 생성 권한을 부여할 수도 있습니다.

서비스 계정은 사용량 기반 요금제에서만 이용할 수 있습니다.

서비스 계정은 워크스페이스에서 사람이 아닌 주체를 나타냅니다. [개인 액세스 토큰](/ko-KR/codex/enterprise/access-tokens)은 토큰을 생성한 워크스페이스 구성원을 나타냅니다. API 플랫폼 프로젝트의 서비스 계정과 API 키에는 별도의 프로젝트 접근 권한과 결제 체계가 적용됩니다.

## 서비스 계정 생성 및 설정

이 대화형 가이드에서는 GitHub를 예로 들어 계정 생성, 플러그인 설정, 토큰 생성, 그룹 및 역할 할당 과정을 안내합니다.

1. 워크스페이스 설정에서 [서비스 계정](https://chatgpt.com/admin/service-accounts)을 여세요.
2. 더하기(**+**) 버튼을 선택한 다음, `release-automation`처럼 용도를 알 수 있는 이름을 입력하세요.
3. **생성을** 선택하세요.

## 플러그인 연결

서비스 계정에서 사용할 플러그인을 별도로 설정하세요. 계정을 생성한 사용자의 플러그인이나 연결된 앱은 상속되지 않습니다.

1. 계정의 **플러그인** 섹션을 열고 **플러그인 추가를** 선택하세요.
2. 플러그인을 선택한 후 설정됨 또는 활성화됨 상태로 표시되는지 확인하세요.

**설정** 및 **관리자** 역할은 플러그인을 설정할 수 있습니다. **사용자** 역할은 설정할 수 없습니다.

## 액세스 토큰 생성

서비스 계정의 상세 페이지에서 토큰을 생성하세요. 이 토큰은 토큰을 생성한 사용자가 아니라 서비스 계정을 나타냅니다.

1. 계정을 열고 **액세스 토큰** 섹션에서 **토큰 생성을** 선택하세요.
2. 토큰 이름을 지정하고 **Codex** 범위를 확인한 후 만료 기간을 선택하세요.
3. **생성을** 선택하고 토큰을 시크릿 관리 도구에 저장하세요.

토큰 전체 값은 한 번만 표시됩니다. 선택할 수 있는 만료 기간은 워크스페이스 정책에 따라 결정됩니다.

## 역할 및 그룹 할당

서비스 계정도 워크스페이스의 사용자와 마찬가지로 워크스페이스 역할을 부여받고 그룹에 가입할 수 있습니다. 계정을 생성한 사용자의 권한은 상속되지 않으므로 접근 권한을 직접 할당하세요.

사용자나 그룹이 계정을 관리할 수 있도록 하려면 **공유를** 선택한 다음 **사용자 또는 그룹 추가를** 선택하고 역할을 할당하세요:

| 공유 계정 역할 | 계정 및 플러그인 설정 | 서비스 계정 액세스 토큰 생성 |
| ------------------- | ------------------------------------- | ------------------------------------ |
| **사용자**            | 아니요                                    | 예                                  |
| **설정**       | 예                                   | 아니요                                   |
| **관리자**         | 예                                   | 예                                  |

이 역할은 계정을 관리하는 사용자에게 적용되며, 서비스 계정에 할당된 워크스페이스 역할 및 그룹과는 별개입니다.

**설정** 및 **관리자** 역할은 계정을 활성화하거나 비활성화할 수 있습니다. 워크스페이스 소유자와 관리자만 계정을 생성, 삭제 또는 공유할 수 있습니다. 운영 담당자는 본인의 ChatGPT 계정에 로그인한 상태에서 공유 계정을 관리합니다.

워크스페이스 권한에 관한 자세한 내용은 [역할 및 워크스페이스 권한](/ko-KR/codex/enterprise/roles-and-workspace-permissions)을 참고하세요.

## 로그인 없이 Codex 실행

서비스 계정 액세스 토큰을 사용하려면 Codex CLI 버전 `0.142.0` 이상이 필요합니다. `CODEX_ACCESS_TOKEN`을 설정한 후 브라우저를 열지 않고 Codex를 실행하세요:

```bash

codex exec --json "Inspect this repository and summarize its current state."

CI에서는 시크릿 관리 도구나 러너 시크릿을 통해 토큰을 전달하세요.

신뢰할 수 있는 머신에 로그인 정보를 저장하려면 표준 입력으로 토큰을 전달하세요:

```bash
printf '%s' "$CODEX_ACCESS_TOKEN" | codex login --with-access-token
codex exec "Summarize the changes in the current branch."

이렇게 하면 인증 정보가 로컬에 저장됩니다. 공유 러너나 임시 러너에서는 로그인 정보를 저장하지 말고 `CODEX_ACCESS_TOKEN`을 사용하세요.

## SCIM으로 서비스 계정 프로비저닝

워크스페이스에서 System for Cross-domain Identity Management (SCIM) 프로토콜을 통한 서비스 계정 프로비저닝을 지원하는 경우, ID 공급자에서 `userType`을 `ServiceAccount`로 설정하세요:

```json
{
  "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
  "userName": "svc-codex-release@company.example",
  "displayName": "Codex release automation",
  "active": true,
  "userType": "ServiceAccount"
}

해당 계정을 워크스페이스와 필요한 그룹에 할당한 다음 동기화하세요. ID 공급자는 계정 이름, 그룹 소속 및 수명 주기를 관리합니다. SCIM으로 관리되는 계정은 ChatGPT에서 이름을 변경하거나 삭제할 수 없습니다. 자세한 내용은 [그룹 및 프로비저닝](/ko-KR/codex/enterprise/groups-and-provisioning)을 참고하세요.

## Admin API로 서비스 계정 관리

워크스페이스에서 Admin API를 사용할 수 있다면 ChatGPT Admin API 키로 계정, 토큰, 공유를 관리하세요. 읽기 작업에는 `chatgpt.enterprise.service_account.read` 권한이, 변경 작업에는 `chatgpt.enterprise.service_account.write` 권한이 필요합니다. 서비스 계정 토큰으로는 Admin API 요청을 인증할 수 없습니다.

[Admin API 레퍼런스](https://chatgpt.com/public/admin/api-reference)에서 사용 가능한 작업과 현재 요청 경로를 확인하세요.

### 계정

| 작업                    | 메서드   | 설명                               |
| ---------------------------- | -------- | ------------------------------------------ |
| 계정 목록 조회                | `GET`    | 워크스페이스의 서비스 계정을 반환합니다         |
| 계정 생성            | `POST`   | 지정한 이름으로 서비스 계정을 생성합니다            |
| 계정 조회               | `GET`    | 서비스 계정 하나를 반환합니다                |
| 계정 활성화 또는 비활성화 | `PATCH`  | 계정의 `enabled` 값을 업데이트합니다      |
| 계정 삭제            | `DELETE` | 계정을 삭제하고 해당 계정의 토큰을 취소합니다 |

`POST /v1/manage/workspaces/{workspace_id}/service-accounts` 요청으로 계정을 생성하세요. 계정을 업데이트할 때는 `enabled` 값만 변경할 수 있습니다.

### 토큰

| 작업      | 메서드   | 설명                         |
| -------------- | -------- | ------------------------------------ |
| 토큰 목록 조회    | `GET`    | 계정의 토큰 메타데이터를 반환합니다 |
| 토큰 생성 | `POST`   | 권한 범위가 지정된 액세스 토큰을 생성합니다        |
| 토큰 취소 | `DELETE` | 토큰 하나를 영구적으로 취소합니다        |

예를 들어 다음과 같이 30일 후 만료되는 Codex 토큰을 생성할 수 있습니다:

```json
{
  "name": "production-release-runner",
  "ttl": 2592000,
  "scopes": ["chatgpt.workspace.feature.allow-codex-local-access.access"]
}

`ttl`은 토큰의 유효 기간을 초 단위로 나타냅니다. 유효 기간을 지정할 경우 1년 미만이어야 하며 워크스페이스의 만료 정책을 따라야 합니다. 전체 `access_token` 값은 토큰을 생성할 때만 반환됩니다.

Admin API로 공유 계정의 액세스 권한 목록을 조회하고 권한을 추가, 업데이트, 삭제할 수도 있습니다. 역할 값은 `manager`, `configurer`, `user`이며 `configurer`는 ChatGPT에서 **설정** 역할로 표시됩니다.

## 서비스 계정 보안 및 관리

- 워크플로우에 필요한 역할과 그룹만 할당하고 플러그인과 연결도 필요한 것만 허용하세요.
- 토큰을 시크릿 관리 도구에 보관하고 신뢰할 수 있는 러너를 사용하세요.
- 자격 증명이 로그, 채팅 메시지, 소스 코드 관리 시스템에 노출되지 않도록 하세요.
- 만료 기한을 설정하고 계정의 액세스 권한과 활동을 정기적으로 검토하세요.
- 토큰을 교체하려면 새 토큰을 생성하고 워크플로우를 업데이트한 뒤 액세스를 확인하고 워크스페이스나 Admin API에서 기존 토큰을 취소하세요.
- 노출된 토큰은 즉시 취소하고 해당 계정의 최근 활동을 조사하세요.
- 사용하지 않는 계정은 워크스페이스나 Admin API에서 비활성화하거나 삭제하세요. 두 경우 모두 모든 활성 토큰이 취소됩니다. 비활성화된 계정은 다시 활성화해 새 토큰으로 사용할 수 있지만, 삭제는 되돌릴 수 없습니다.

실행 주체는 서비스 계정으로 기록됩니다. 제공되는 워크스페이스 분석 및 감사 기록을 통해 토큰을 생성하거나 계정 설정을 변경한 사람도 확인할 수 있습니다. 기록되는 이벤트 범위는 [Admin API 레퍼런스](https://chatgpt.com/public/admin/api-reference)에서 확인하세요.

## 관련 문서

- [인증](/ko-KR/codex/auth)
- [개인 액세스 토큰](/ko-KR/codex/enterprise/access-tokens)
- [역할 및 워크스페이스 권한](/ko-KR/codex/enterprise/roles-and-workspace-permissions)
- [그룹 및 프로비저닝](/ko-KR/codex/enterprise/groups-and-provisioning)
- [거버넌스](/ko-KR/codex/enterprise/governance)
- [Compliance API 및 감사 이벤트](/ko-KR/codex/enterprise/compliance-api)
- [비대화형 모드](/ko-KR/codex/non-interactive-mode)

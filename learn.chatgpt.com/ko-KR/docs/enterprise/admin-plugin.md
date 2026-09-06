<!-- source: https://learn.chatgpt.com/ko-KR/docs/enterprise/admin-plugin -->

이 가이드에서 Admin 플러그인이 일반적인 관리 업무를 어떻게 지원하는지 알아보고 작업을 준비하세요. 필요한 승인과 컨텍스트를 갖춘 뒤 주요 사용 사례별 프롬프트를 사용해 보세요.

## 1. Admin 플러그인의 용도 알아보기

Admin 플러그인은 ChatGPT Work 안에서 설정, 권한, 제어 기능을 직접 관리할 수 있도록 돕습니다. 자연어로 목표를 설명하면 플러그인이 필요한 입력 정보를 수집하고 현재 상태를 조회한 뒤, 확인한 내용을 설명하고 지원 범위 내에서 다음 단계를 안내합니다.

### Admin 플러그인으로 할 수 있는 일

- API 요청을 직접 작성할 필요 없이 관리 요청을 명확한 워크플로우로 정리합니다.
- 결정을 내리거나 변경을 승인하기 전에 현재 워크스페이스 상태를 검토합니다.
- 사용이 허가된 소스와 필드 중 어떤 것이 답변의 근거인지 보여 주고, 확인하지 못한 내용도 함께 제시합니다.
- 지원되는 변경을 적용하기 전에 검토할 수 있도록 일시 중지하고, 변경 후에는 레코드를 다시 조회해 결과를 확인합니다.

플러그인은 내부적으로 일부 관리 API와 연결이 승인된 데이터 소스를 사용합니다. 모든 관리 시스템을 통합하거나, 사용자 권한을 확대하거나, 모든 API 작업을 ChatGPT에서 사용할 수 있게 해 주지는 않습니다. 플러그인이 읽거나 변경할 수 있는 범위는 여전히 데이터를 소유한 시스템이 제어합니다.

### 관리 API로 할 수 있는 일

관리 API는 소프트웨어가 정해진 형식으로 데이터나 지원되는 작업을 요청할 수 있게 해 줍니다. 조직은 관리 API를 사용해 내부 프로세스나 외부 도구를 구축할 수 있습니다. 대표적인 예로는 정기 보고서, 여러 레코드에 걸친 반복 작업, 승인된 시스템과의 연결이 있습니다. 이러한 워크플로우에는 일반적으로 엔지니어링, 보안, 거버넌스 검토가 필요합니다.

이 가이드를 활용하기 위해 API 워크플로우를 구축할 필요는 없습니다. 나머지 내용은 Admin 플러그인을 중심으로 설명합니다. 또한 ChatGPT 워크스페이스 관리와 OpenAI API 플랫폼 관리는 별개이며, 각각 고유한 권한 및 인증 요건이 있습니다.

### 인증 정보 보호하기

조직에서 승인한 연결과 비밀 정보 저장 시스템만 사용하세요. 실제 관리 API 키를 ChatGPT, Codex, 문서 또는 소스 파일에 절대 붙여 넣지 마세요.

## 2. Admin 플러그인 사용 준비하기

플러그인이 지원하는 일회성 작업을 자연어로 처리하고 싶을 때 Admin 플러그인을 사용하세요. 목표를 설명하고 고정 ID 또는 보고에 필요한 승인된 컨텍스트를 제공하세요. 플러그인은 사용자가 계속 진행할지 결정하기 전에 확인한 내용이나 변경 계획을 보여 줍니다.

플러그인은 해당 작업에 사용이 허가된 소스, 인증 정보, 작업만 사용합니다. 모든 관리 시스템을 통합하거나 사용자에게 더 넓은 권한을 부여하지 않습니다. 원본 시스템의 정보가 여전히 판단 기준이 됩니다.

### 시작하기 전에

1. 레코드가 있는 관리 영역을 찾으세요.
2. 필요한 입력 정보를 준비하고 승인을 받으세요.
3. 읽기 전용 요청으로 시작하세요.
4. 어떤 소스와 필드를 사용했는지, 무엇을 확인하지 못했는지 플러그인에 물어보세요.
5. 지원되는 변경을 적용하려면 승인하기 전에 계획을 검토하세요. 그런 다음 플러그인에 레코드를 다시 조회해 결과를 확인해 달라고 요청하세요.

워크스페이스에서 플러그인을 사용할 수 있고 필요한 권한이 있는지 확인하세요. 아래의 역할 및 접근 권한 사용 사례는 현재 문서에 명시된 플러그인의 지원 범위를 반영합니다. 플러그인은 역할, 기능별 권한, 사용자나 그룹의 역할 할당을 검토할 수 있습니다. 사용자가 확인한 후에는 기존 그룹에 기존 역할을 할당할 수도 있습니다.

플러그인은 역할을 만들거나, 역할의 권한을 변경하거나, 특정 커넥터에 대한 접근 권한을 확인할 수 없습니다.

분석 사용 사례에는 연결이 승인된 데이터 소스에 대한 접근 권한이 필요합니다. ROI 분석에는 승인된 비즈니스 또는 엔지니어링 성과 데이터도 필요하며, 사용 기록만으로는 충분하지 않습니다.

## 3. Admin 플러그인의 주요 사용 사례 살펴보기

사용 사례를 선택하고 각 플레이스홀더를 승인된 요청의 값으로 바꾼 다음, 단계를 순서대로 따르세요. 플러그인이 지원하며 이미 승인된 변경 작업이 아니라면 읽기 전용 요청으로 시작하세요.

### 워크스페이스 역할 목록 조회하기

**사용해 볼 프롬프트**

```text
List the roles in workspace {workspace_id}. Separate built-in and custom roles. For each role, explain which features it can use and show the users or groups assigned to it. Don’t make changes.

**진행 단계**

1. **준비:** 워크스페이스 ID와 이 정보를 조회할 권한이 있는지 확인하세요.
2. **실행:** 읽기 전용으로 역할 목록을 요청하세요.
3. **검토:** 역할 유형, 기능 접근 권한, 할당 내역을 확인하세요.
4. **검증:** 예상과 다른 내용은 변경하지 말고 살펴보세요.

### 개별 역할 검토하기

**사용해 볼 프롬프트**

```text
Review role {role_id}. Explain its permissions in plain language, show who has it, and flag anything that looks broader than expected. Don’t edit the role.

**진행 단계**

1. **준비:** 역할 ID와 워크스페이스를 확인하세요.
2. **실행:** 읽기 전용으로 역할 검토를 요청하세요.
3. **검토:** 권한과 할당 내역이 해당 역할의 목적에 맞는지 확인하세요.
4. **검증:** 역할 담당자에게 물어볼 내용을 적어 두세요. 플러그인으로는 역할을 만들거나 해당 역할의 권한을 수정할 수 없다는 점을 기억하세요.

### 사용자 또는 그룹의 접근 권한 파악하기

**사용해 볼 프롬프트**

```text
Help me understand the access for user {user_id} or group {group_id}. Show their assigned roles, explain what access those roles provide, and point out overlaps or gaps. Clearly say what you can’t verify.

**진행 단계**

1. **준비:** 사용자 또는 그룹의 고정 ID를 사용하세요.
2. **실행:** 플러그인에 접근 권한을 설명해 달라고 요청하세요.
3. **검토:** 어떤 역할이 할당되어 있고 각 역할이 어떤 접근 권한을 제공하는지 확인하세요. 중복되거나 빠진 권한이 있으면 기록하세요.
4. **검증:** 플러그인이 조회할 수 없는 항목은 추측하지 말고 '알 수 없음'으로 표시하세요.

### 그룹에 기존 역할 할당하기

**사용해 볼 프롬프트**

```text
Before making a change, show the current roles for group {group_id} and explain what role {role_id} would add. Confirm the recorded approver and wait for my explicit approval. After the assignment, verify the group’s updated roles.

**진행 단계**

1. **준비:** 그룹 ID와 역할 ID를 확인하세요. 승인된 요청과 기록된 승인자를 확인하세요.
2. **실행:** 플러그인에 현재 역할과 변경될 내용을 보여 달라고 요청하세요.
3. **검토:** 계획이 승인된 요청과 일치할 때만 승인하세요.
4. **검증:** 할당 후 그룹을 다시 조회해 승인된 대로 기존 역할이 추가되었는지 확인하세요.

### 일반적인 커넥터 권한 확인하기

**사용해 볼 프롬프트**

```text
Check whether user {user_id} has general connector access through their assigned roles. Ask the plugin to show which permissions support its answer. If it can’t verify access to a specific connector, have it say so clearly.

**진행 단계**

1. **준비:** 사용자 ID와 해당 사용자의 접근 권한을 검토할 권한이 있는지 확인하세요.
2. **실행:** 일반적인 권한 확인을 요청하세요.
3. **검토:** 할당된 역할과 답변의 근거로 사용된 권한을 확인하세요.
4. **검증:** 일반적인 권한 확인 용도로만 사용하세요. 특정 커넥터나 연결된 항목에 대한 접근 권한을 입증하지는 않습니다.

### 승인된 변경 사항의 문제 해결

**예시 프롬프트**

```text
Review approved change {change_record_id}. Compare the requested result with the current workspace. If it failed, check the workspace and role first. Then confirm who owns the record, explain the issue, and suggest the safest next step.

**단계**

1. **준비:** 승인된 변경 기록과 의도한 결과를 확인하세요.
2. **실행:** 요청 내용과 현재 워크스페이스 상태를 비교해 달라고 플러그인에 요청하세요.
3. **검토:** 워크스페이스와 역할을 확인하세요. 그런 다음 레코드 소유자를 확인하세요.
4. **검증:** 다음 단계를 결정하기 전에 현재 워크스페이스 상태를 판단의 기준으로 삼으세요.

### 비용 및 모델 조합 최적화

**예시 프롬프트**

```text
For {date_range} in workspace {workspace_id}, group verified token use and cost by use case. Compare models and reasoning modes using the speed and quality information available. Flag costly workflows when the data shows little evidence of value. Recommend where spending could be reduced or redirected toward work with stronger productivity or cost results. Include any approved revenue or quality signals. Estimate possible savings, explain tradeoffs, and separate verified observations from assumptions or missing inputs. Keep this read-only.

**단계**

1. **준비:** 워크스페이스와 날짜 범위를 확인하세요. 비용 데이터가 전체 기간을 포함하는지, 승인된 성능 또는 성과 필드 중 어떤 필드를 사용할 수 있는지도 확인하세요.
2. **실행:** 비용과 모델을 비교해 달라고 요청하세요.
3. **검토:** 데이터가 보여 주는 사실과 가정, 누락된 입력 정보, 트레이드오프를 구분하세요.
4. **검증:** 실행에 옮기기 전에 Finance 및 워크플로우 담당자와 함께 절감 가능한 비용을 확인하세요.

### 사용량 및 도입 현황 파악

**예시 프롬프트**

```text
Analyze workspace {workspace_id} during {date_range}. Show tasks and token use by team and business function. Group cost by use case. Summarize what teams use ChatGPT and Codex to accomplish. Include examples from Legal, Marketing, and Sales. Compare available use of skills and plugins. Only report tool calls, connected apps, and multi-tool workflows if those fields are available. Show where teams use more advanced workflows and where there may be room to expand. Rank the top {5_or_10} use cases and show whether a small group of highly active users accounts for most usage. Don’t guess about activity that is not in the data.

**단계**

1. **준비:** 워크스페이스, 날짜 범위, 팀 매핑을 확인하세요. 사용자별 보고가 승인되었는지도 확인하세요.
2. **실행:** 사용량과 도입 현황을 분석해 달라고 요청하세요.
3. **검토:** 요청한 필드 중 어떤 필드를 사용할 수 있는지 확인하세요. 누락된 활동 정보는 추측하지 말고 제외하세요.
4. **검증:** 사용량이 많다는 것만으로 고급 활용, 비즈니스 가치, 개인의 성과가 입증되지는 않습니다.

### 비즈니스 가치 및 ROI 측정

**예시 프롬프트**

```text
For workspace {workspace_id} in {date_range}, combine verified usage and cost with approved outcomes. Estimate value by team and use case. Include approved Sales measures for productivity, revenue, and quality. Compare teams and models, as well as workflows and user segments. Rank returns against cost. Show the sources and formula. Clearly state assumptions, limits, and missing inputs. Don’t claim ChatGPT caused the outcomes. Keep this read-only.

**단계**

1. **준비:** 워크스페이스와 날짜 범위를 확인한 다음 승인된 성과 정보를 확인하세요. 계산식과 개인정보 보호 규칙을 검토하세요.
2. **실행:** ROI 분석을 요청하세요.
3. **검토:** 모든 출처와 가정을 확인하세요. 한계나 누락된 입력 정보를 빠짐없이 기록하세요.
4. **검증:** 사용량만으로는 ROI나 인과관계를 입증할 수 없습니다. Finance 및 비즈니스 담당자와 함께 결과를 검토하세요.

### Codex ROI 평가

**예시 프롬프트**

```text
For workspace {workspace_id}, combine verified Codex usage and cost from {date_range} with approved engineering outcomes. Estimate ROI by team, repository, and workflow. Compare productivity and delivery speed with code quality and engineering cost. Identify workflows that show high value or use many resources. Recommend changes to the model, reasoning mode, or workflow. Explain the tradeoffs and uncertainty. Present the findings as patterns in the available data, not proof that Codex caused the outcome. Return findings only; do not make changes.

**단계**

1. **준비:** 워크스페이스와 보고 기간을 확인하세요. 팀 및 레포지토리 매핑과 승인된 기준 데이터를 검토하세요.
2. **실행:** Codex ROI 분석을 요청하세요.
3. **검토:** 관찰된 패턴과 가정을 구분하세요. 사용자 및 레포지토리 데이터를 보호하세요.
4. **검증:** 권고 사항과 성과 비교 기준을 엔지니어링 팀과 함께 검토하세요.

## 4. API 워크플로우가 적합할 수 있는 경우

일부 조직은 API로 자체 관리 프로세스나 외부 도구를 구축합니다. 이 방식은 일정에 따라 실행하거나 지속적으로 수행하는 작업을 지원할 수 있습니다. 많은 레코드를 다루거나 승인된 내부 시스템에 연결해야 하는 프로세스에도 도움이 될 수 있습니다. 이는 Admin 플러그인의 안내에 따라 작업하는 방식과는 별개입니다.

명확히 정의된 관리 작업부터 시작하세요. 필요한 입력 정보와 권한, 검토 시점, 예상 결과, 결과를 기록할 방법을 파악하세요. 조직에서 이를 자동화한다면 관련 엔지니어링, 보안, 거버넌스 팀을 참여시키고, 자격 증명은 승인된 비밀 정보 저장소에 보관하며, 배포 전에 워크플로우를 테스트하세요.

### 관련 리소스

- [ChatGPT 워크스페이스 Admin API 레퍼런스](https://chatgpt.com/public/admin/api-reference)
- [관리 범위](/ko-KR/codex/enterprise/roles-and-workspace-permissions#understand-the-control-boundaries)
- [ChatGPT 워크스페이스 Analytics API](/ko-KR/codex/enterprise/analytics-api)
- [ChatGPT 워크스페이스 Compliance API](/ko-KR/codex/enterprise/compliance-api)

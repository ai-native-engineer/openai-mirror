<!-- source: https://learn.chatgpt.com/ko-KR/docs/security/plugin/triage-backlog -->

`$codex-security:triage-finding`을 사용해 현재 레포지토리를 기준으로 기존 보안 이슈를 검토하세요.
이 워크플로우는 읽기 전용 정적 분석을 수행합니다. Codex는 각 보안 이슈를
입증되지 않은 주장으로 간주하고, 코드를 실행하지 않은 채 레포지토리의
증거를 조사합니다.

평가할 레포지토리로 범위가 지정된 Codex 프로젝트에서 이 워크플로우를
실행하세요. Codex가 레포지토리의 소스 코드를 읽을 수 있어야 합니다. Jira 및 Linear
커넥터는 보안 이슈 데이터를 제공할 수 있지만, GitHub 보안 이슈에는 인증된
GitHub REST 액세스가 필요합니다. 어느 방식도 소스 코드 액세스를 대체하지 않습니다.

내부적으로 Codex는 참조된 코드나 버전 정보부터 확인합니다. 그런 다음
공격자가 제어할 수 있다고 주장된 소스, 관련 보안 제어, 위험한 싱크 및
도달 가능한 경로를 추적합니다. 또한 제품 영역과 신뢰 경계를 확인하고,
상충하는 증거를 찾고, 입증이 부족한 부분을 기록합니다. 이어서 Codex는
각 보안 이슈에 하나의 판정을 반환하고, 조치나 추가 검토가 필요한 이슈의
우선순위를 정합니다.

`$codex-security:validation`은 코드를 빌드하거나 실행하고,
보안 이슈에 초점을 맞춘 테스트나 개념 증명을 만들거나 실제 인터페이스를 사용해
보안 이슈를 재현하거나 반증할 수 있다는 점에서 이 워크플로우와 다릅니다. 트리아지는 기존
백로그를 분류하고 우선순위를 정할 때 사용하세요. 정적 증거만으로 판단하기 어려운 보안 이슈를
런타임 증거로 해결할 수 있다면 검증을 사용하세요.

  백로그 트리아지는 기존 보안 이슈에서 시작합니다. 레포지토리에서 새로운
  취약점을 찾으려면 [보안 스캔을 실행하세요](/ko-KR/codex/security/plugin/scans). 트리아지는
  레포지토리를 변경하거나 수정 사항을 구현하지 않습니다.

## 트리아지할 보안 이슈 선택

다음 출처에서 단일 보안 이슈 또는 보안 이슈 모음을 제공할 수 있습니다:

| 출처                   | 제공할 정보                                                                                                                                                                                                                                                                                                                                                                                                                                        | 요구 사항                                                                                                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 붙여넣거나 로컬에 저장한 보안 이슈 | SARIF 결과, CVE 또는 GHSA, 보안 권고, 스캐너 티켓, 버그 바운티 보고서, Codex Security 보안 이슈 아티팩트 또는 자연어로 작성한 취약점 주장.                                                                                                                                                                                                                                                                                          | 커넥터가 필요하지 않습니다.                                                                                                                                                                           |
| Jira 또는 Linear           | 보안 또는 취약점 이슈의 정확한 URL이나 식별자, Jira JQL, Linear 팀, 프로젝트 또는 검색 구문. Codex는 트리아지 전에 선택된 이슈의 내용을 가져옵니다.                                                                                                                                                                                                                                                                            | 읽기 권한이 있는 [Atlassian Rovo를 통한 Jira](codex://plugins/plugin_connector_692de805e3ec8191834719067174a384) 또는 [Linear](codex://plugins/plugin_asdk_app_69a089a326dc8191b32a3f2553f5be2c). |
| GitHub                   | 레포지토리와 다음 보안 이슈 출처 중 하나: 코드 스캔, `Dependabot` 취약점 및 멀웨어, 보안 권고와 비공개 취약점 보고서 또는 모든 출처. 레포지토리를 지정하지 않으면 Codex는 가능한 경우 현재 Codex 프로젝트에 연결된 GitHub 레포지토리를 사용합니다. GitHub 이슈는 기본 GitHub 출처에 포함되지 않습니다. GitHub 이슈를 트리아지하려면 특정 이슈를 제공하거나 GitHub 이슈를 명시적으로 요청하세요. | `gh auth token`, `GH_TOKEN`, `GITHUB_TOKEN` 등을 사용한 인증된 GitHub REST 액세스. 선택한 레포지토리와 보안 이슈 유형을 읽을 권한이 있어야 합니다.                                      |

Codex는 제공된 각 보안 이슈에 대해 입력 순서대로 결과를 하나씩 유지하여
각 원본 보안 이슈를 추적할 수 있게 합니다. 중복으로 보이는 보안 이슈도 병합하거나
제외하지 않습니다.

## 읽기 전용 트리아지 실행

보안 이슈를 붙여넣거나 로컬 아티팩트를 사용하는 경우 다음과 같은 프롬프트를 보내세요:

```text
Use $codex-security:triage-finding to triage these existing security findings against this repository:

[Paste the findings or provide the artifact path.]

Jira 또는 Linear 이슈의 경우 이슈 집합을 지정하고 소스 시스템을
읽기 전용으로 유지하세요:

```text
Use $codex-security:triage-finding to import and triage the security findings from [Jira or Linear issue URLs, identifiers, or query] against this repository.
Do not change the source issues.

GitHub 보안 이슈의 경우 레포지토리와 출처를 지정하세요:

```text
Use $codex-security:triage-finding to import and triage [code scanning, Dependabot vulnerabilities and malware, security advisories and private vulnerability reports, or all] from [owner/repository] against this repository.

현재 Codex 프로젝트에 연결된 GitHub 레포지토리를 사용하려면 보안 이슈
출처만 지정하세요:

```text
Use $codex-security:triage-finding to import and triage [code scanning, Dependabot vulnerabilities and malware, security advisories and private vulnerability reports, or all] from GitHub against this repository. Use the GitHub repository attached to the current Codex project.

워크플로우는 다음 순서로 진행됩니다:

1. 보안 이슈 수집 및 정리

   Codex는 요청된 이슈나 GitHub 콘텐츠를 가져오고, 출처 식별자와 참조 정보를
보존하며, 입력마다 하나의 트리아지 항목을 만듭니다. 판정을 내리기 전에
전체 항목 목록을 구성합니다.

2. 레포지토리 컨텍스트 확인

   Codex는 가능한 경우 현재 레포지토리와 리비전을 확인합니다. `SECURITY.md`가
있으면 이를 읽어 지원되는 버전, 신뢰할 수 있는 입력, 제품 경계 및
   평가 범위 밖의 영역을 평가에 반영합니다.

3. 정적 증거 조사

   각 보안 이슈에 대해 Codex는 공격자가 제어한다고 주장된 소스와 관련 보안 제어,
취약한 싱크, 도달 가능한 경로 및 지원 대상 보안 경계를 추적합니다. 또한
주장을 뒷받침하는 증거와 주장에 반하는 증거를 기록하고, 입증이 부족한 부분도
명시합니다.

4. 판정 및 순위 지정

   Codex는 모든 보안 이슈에 판정과 신뢰도를 지정합니다. 또한
`confirmed` 및 `needs_review` 보안 이슈를 악용 가능성에 따라 각각 별도의 대기열에서 순위를 매깁니다.

## 결과 검토

| 판정          | 의미                                                                                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `confirmed`      | 명시된 전제 조건에서 취약한 경로에 도달할 수 있고, 이 경로가 지원 대상 보안 경계를 넘는다는 점이 레포지토리 증거로 확인됩니다.                     |
| `not_actionable` | 영향받지 않는 버전, 도달할 수 없는 경로, 효과적인 보호 장치 또는 제품에 포함되지 않은 영역 등이 레포지토리 증거로 확인되므로 해당 주장은 성립하지 않습니다.                 |
| `needs_review`   | 필수 정보가 누락되었거나 모호하거나 런타임, 환경 또는 정책에 따라 달라지기 때문에 레포지토리의 증거만으로는 판단할 수 없습니다. |

  악용 가능성 순위는 각 판정 대기열에서 독립적으로 `1`부터 시작하는 양의 정수를 사용합니다.
  따라서 수정 우선순위와 아직 해결되지 않은 검토 작업을 구분할 수 있습니다.
  순위 `1`은 해당 결과 집합에서 악용 가능성이 가장 높은 `confirmed` 보안 이슈 또는
  우선순위가 가장 높은 `needs_review` 보안 이슈를 뜻합니다. 이 순위는 스캐너 심각도 점수가 아니며,
  `not_actionable` 보안 이슈에는 순위를 지정하지 않습니다.

각 보안 이슈에서 다음을 검토하세요:

- 판정과 순위를 정한 근거
- 주장을 뒷받침하는 증거와 주장에 반하는 증거
- 남은 미해결 질문과 입증이 부족한 부분
- 영향받는 위치와 구성 요소
- 제품 영역과 출처의 신뢰 수준
- 권장되는 다음 단계
- 판정이 `confirmed`인 경우 [`$codex-security:fix-finding`](/ko-KR/codex/security/plugin/fix-findings)에
  전달할 내용

제공된 모든 보안 이슈에 결과가 하나씩 있고 Codex가 각 이슈의 출처 식별자를 보존하며
모든 불확실성이 명시되면 트리아지가 완료됩니다. 트리아지 결과를 검토한 후
Codex에 다시 기록하도록 요청하지 않는 한 Jira, Linear 및 기타 백로그 레코드는
변경되지 않습니다.

## 다음 단계

- `confirmed`: 담당자가 해당 보안 이슈를 수정 대상으로 수락한 후
[`$codex-security:fix-finding`](/ko-KR/codex/security/plugin/fix-findings)을 사용해 이슈를 수정하고
  검증하세요. 트리아지는 프롬프트에 바로 사용할 수 있는 인계 내용을 준비하지만 스킬을
  자동으로 호출하지는 않습니다.
- `needs_review`: 코드를 실행하여 입증이 부족한 부분을 해소할 수 있다면
`$codex-security:validation`을 사용해 범위가 제한된 동적 검증을 수행하세요.
  트리아지 결과에서 보안 이슈에 대한 주장, 영향을 받는 위치, 전제 조건, 정적 증거 및
  입증이 부족한 부분을 전달하세요:

  ```text
  Use $codex-security:validation to dynamically validate finding [triage item ID or source ID] from the backlog triage result. Use the strongest realistic, bounded method, record exactly what was tested, and preserve any remaining proof gaps.

  트리아지와 달리 검증에서는 코드를 빌드하거나 실행하고, 특정 테스트나
  개념 증명을 만들거나 실제 인터페이스를 사용할 수 있습니다. 제안된 명령을
  승인하기 전에 검토하고 [Codex 승인 및 보안
  정책](/ko-KR/codex/agent-approvals-security)을 계속 적용하세요.

- `needs_review`: 보안 이슈가 제품 정책이나 배포
  컨텍스트에 따라 달라지는 경우 코드를 변경하기 전에 나열된 미해결 질문에 답하세요.
- `not_actionable`: 증거를 트리아지 기록과 함께 보관하세요. Codex는
  원본 티켓을 자동으로 닫거나 업데이트하지 않습니다.
- 제공된 백로그 이외의 취약점을 찾으려면 [보안
  스캔을 실행하세요](/ko-KR/codex/security/plugin/scans).

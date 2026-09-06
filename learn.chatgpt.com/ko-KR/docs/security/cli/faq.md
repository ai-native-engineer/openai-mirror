<!-- source: https://learn.chatgpt.com/ko-KR/docs/security/cli/faq -->

터미널에서 레포지토리를 스캔하고 보안 이슈를 관리할 때 자주 묻는 질문과 답변을
확인하세요. 설치하고 첫 스캔을 실행하려면
[CLI 빠른 시작](/ko-KR/codex/security/cli)을 참조하세요.

## 레포지토리 스캔

### CLI는 누가 사용할 수 있나요

`@openai/codex-security` 패키지는 공개되어 있습니다.

스캔을 실행하려면 Codex Security 사용 권한이 필요합니다.
최상의 결과를 얻으려면 [Trusted Access for Cyber](https://chatgpt.com/cyber) 인증을 받은 계정을 사용하세요.

### 로그인한 후에도 스캔에서 API 키를 사용하는 이유는 무엇인가요

환경에 `OPENAI_API_KEY` 또는 `CODEX_API_KEY`가 설정되어 있으면
대화형 터미널 없이 실행하는 스캔과 JSON 및 JSONL 스캔은 ChatGPT 또는 액세스 토큰으로 로그인한 후에도
기본적으로 환경의 API 키를 사용합니다.
텍스트를 출력하는 대화형 스캔은 ChatGPT 로그인도 사용할 수 있는 경우 인증 방식을
선택하라는 메시지를 표시합니다. 드라이 런에서는 사용자 입력을 요청하거나 자격 증명을 로드하지 않습니다.

스캔에 저장된 자격 증명을 사용하려면 명시적으로 선택하세요:

```bash
npx @openai/codex-security scan . --auth chatgpt

`OPENAI_API_KEY` 또는 `CODEX_API_KEY`에 설정된 API 키를 반드시 사용하도록 하려면:

```bash
npx @openai/codex-security scan . --auth api-key

저장된 자격 증명을 자동으로 기본값으로 사용하려면
`unset OPENAI_API_KEY CODEX_API_KEY` 명령어를 실행하세요. 지원되는 모든 인증 모드는
[CLI 참조 자료](/ko-KR/codex/security/cli/reference#select-scan-authentication)에서 확인하세요.

### 레포지토리 일괄 스캔은 어떻게 작동하나요

GitHub CLI로 로그인하세요:

```bash
gh auth login

GitHub 계정 또는 조직에서 레포지토리를 찾아 선택하세요:

```bash
npx @openai/codex-security bulk-scan

미리 준비한 목록을 사용하려면 레포지토리 CSV와 출력 디렉터리를 지정하세요:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

[일괄 보안 스캔 실행](/ko-KR/codex/security/cli/bulk-scans)에서 GitHub 레포지토리 검색,
CSV 형식, 캠페인 결과 및 사용 가능한 옵션을 확인하세요.

### 중단된 일괄 스캔을 재개할 수 있나요

예. 원래 CSV와 출력 디렉터리를 사용해 동일한 일괄 스캔 명령어를 실행하세요.
Codex Security는 스캔이 완료된 레포지토리를 건너뜁니다.

레포지토리 또는 스캔에서 일시적인 오류가 발생했을 때 재시도하려면 `--max-attempts 3`을 추가하세요:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --max-attempts 3

검사 범위가 `partial` 또는 `unknown`인 상태로 완료된 스캔은 결과를 유지하며
캠페인은 종료 코드 `2`로 종료됩니다. 이러한 스캔은
`--max-attempts` 옵션을 사용해도 재시도되지 않습니다.

### 스캔에 아키텍처와 보안 정책을 어떻게 활용하나요

아키텍처 문서, 위협 모델 또는 보안 정책을
`--knowledge-base`로 전달하세요:

```bash
npx @openai/codex-security scan . \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

Codex Security는 이러한 문서를 현재 스캔의 컨텍스트로 사용합니다.
지원되는 파일 형식과 디렉터리 처리 방식은 [보안
컨텍스트 추가](/ko-KR/codex/security/cli/reference#add-security-context)를 참조하세요.

## 보안 이슈와 검사 범위

### 팀은 이전 스캔 결과를 어디에서 찾을 수 있나요

해당 레포지토리의 저장된 스캔 목록을 확인하세요:

```bash
npx @openai/codex-security scans list /path/to/repository

결과에 표시된 스캔 ID로 해당 스캔의 보안 이슈를 확인하세요:

```bash
npx @openai/codex-security scans show SCAN_ID

완료된 각 스캔의 보고서, 보안 이슈, 검사 범위 및 관련 아티팩트는
함께 보관됩니다. 전체 구조는 [스캔
아티팩트](/ko-KR/codex/security/cli/reference#scan-artifacts)를 참조하세요.

저장된 스캔 및 워커 이벤트를 확인하려면 `scans logs SCAN_ID` 명령어를 실행하세요.
이 로그의 정보는 가려지지 않으며 소스 코드나 자격 증명이 포함될 수 있습니다.

### CLI가 스캔 기록을 저장할 수 없으면 어떻게 해야 하나요

Codex Security는 워크벤치 데이터베이스에 스캔 기록을 보관합니다.
기본 상태 디렉터리에 쓸 수 없다면 레포지토리 외부의
비공개 디렉터리를 선택하세요:

```bash

### 스캔에서는 신규 및 기존 보안 이슈를 어떻게 구분하나요

레포지토리의 모든 스캔에서 확인된 미해결 보안 이슈 목록을 조회하세요:

```bash
npx @openai/codex-security findings list /path/to/repository

목록에는 최신 스캔에서 확인된 보안 이슈와 해당 스캔에서 확인되지 않은
이전 미해결 보안 이슈가 표시됩니다.

두 스캔의 보안 이슈를 비교하세요:

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

비교 과정에서는 근본 원인을 기준으로 보안 이슈를 자동으로 매칭하고 저장된
매칭 결과를 재사용하며 신규, 지속, 재개, 해결 및 상태를 알 수 없는
보안 이슈를 식별합니다. 후속 스캔이 원래 대상과 영향받은 경로를 누락 없이
검사한 경우에만 해당 보안 이슈가 해결된 것으로 간주됩니다.

### 오탐 피드백은 어떻게 작동하나요

저장된 스캔을 확인해 발생 ID를 찾으세요:

```bash
npx @openai/codex-security scans show SCAN_ID

해당 보안 이슈가 적용되지 않는 이유를 기록하세요:

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The framework escapes this input before it reaches the query"

이후 같은 레포지토리를 스캔하면 해당 설명이 컨텍스트로 제공됩니다.
다만 현재 소스, 보안 통제 및 도달 가능성은 여전히 독립적으로 확인합니다.
보안 이슈를 기각해도 규칙, 경로 또는 취약점 유형이 검사 대상에서 제외되지는 않습니다.

명령어에 관한 자세한 내용은 [보안 이슈
참조 자료](/ko-KR/codex/security/cli/reference#codex-security-findings)를 확인하세요.

### 반복 스캔에서 서로 다른 보안 이슈가 나올 수 있는 이유는 무엇인가요

스캔 구성이 같아도 AI 지원 스캔의 결과는 달라질 수 있습니다. 먼저
기준 스캔을 다시 실행하세요:

```bash
npx @openai/codex-security scans rerun BASELINE_SCAN_ID

재실행 시 원래 스캔 구성이 유지되며 동일한 플러그인
버전이 필요합니다. 설치된 플러그인이 변경되었다면 명령어 실행이 중단됩니다.

기준 스캔과 새 스캔을 비교하세요:

```bash
npx @openai/codex-security scans compare BASELINE_SCAN_ID REPEAT_SCAN_ID

컨텍스트 부족이 결과 차이에 영향을 줄 수 있다면 공통 아키텍처 및 보안 지침을
제공하세요. 매칭을 통해 여러 실행에서 근본 원인이 같은 보안 이슈를 식별할 수
있지만 스캔 결과가 항상 동일하게 나오는 것은 아닙니다. 더 이상 나타나지 않는
중요한 보안 이슈는 직접 다시 확인하세요.

### 팀은 수정 사항으로 문제가 해결되었는지 어떻게 확인할 수 있나요

수정 사항을 적용한 후 원래 스캔을 다시 실행하세요:

```bash
npx @openai/codex-security scans rerun BEFORE_SCAN_ID

원래 보안 이슈와 새 스캔 결과를 비교하세요:

```bash
npx @openai/codex-security scans compare BEFORE_SCAN_ID AFTER_SCAN_ID

새 스캔이 원래 대상과 영향받은 경로를 누락 없이 검사하는지
확인하세요. 그런 다음 현재 체크아웃한 코드를 기준으로 원래 보안 이슈를
직접 다시 확인하세요:

```bash
npx @openai/codex-security validate /path/to/original/findings.json \
  "Recheck the SQL injection in src/orders.ts:42 against the current code"

보안 이슈가 나타나지 않는다는 사실이나 스캔 비교만으로는 수정 사항으로 문제가 해결되었음을 입증할 수 없습니다.

### 불완전한 검사 범위는 무엇을 의미하나요

검사 범위는 `complete`, `partial` 또는 `unknown`일 수 있습니다. `coverage.json`에서
제외된 경로, 검사가 보류된 영역 및 미해결 사항을 확인한 후
스캔 결과를 검토 근거로 활용하세요.

검사 범위가 부분적이거나 확인되지 않은 스캔은 심각도 정책이 없어도 종료 코드 `2`를
반환합니다. 이 경우에도 확인 가능한 보안 이슈와 검사 범위는 유지됩니다.
후속 스캔에서 이전 보안 이슈가 발견된 원래 경로를 검사하지 않으면
해당 이슈가 더 이상 존재하지 않는다고 확인할 수 없습니다.

## 자동화 및 비용

### 심층 스캔의 시간 제한은 어떻게 적용되나요

심층 스캔을 시작할 때 워커의 실행 기한을 설정하세요:

```bash
npx @openai/codex-security scan . --mode deep --max-time-hours 1.5

기본값은 `96`시간입니다. 소수를 포함해 `96` 이하의 모든 양수를
사용할 수 있습니다. 기한이 되면 Codex Security는 실행을 마치지 못한 워커를 중단하고
완료된 표준 스캔 결과를 보존해 최종 보고서에 집계합니다.
소스 검토를 마친 워커가 하나도 없으면 보고서에 검사 범위가 부분적인 것으로 기록되며
CLI는 종료 코드 `2`를 반환합니다.

설정을 계속 유지하거나 일괄 캠페인에 적용하려면 `max_time_hours` 값을
`[deep_scan]` 아래에 설정하세요. 자세한 내용은 [심층 스캔
구성](/ko-KR/codex/security/cli/reference#configure-deep-scans)을 참조하세요.

### 스캔 비용 한도는 어떻게 적용되나요

스캔을 시작하기 전에 예상 비용 한도를 USD 단위로 설정하세요:

```bash
npx @openai/codex-security scan . --max-cost 5

이 한도는 예상치이며 엄격한 지출 상한은 아닙니다. 이미 진행 중인
요청은 한도를 초과한 후 완료될 수 있습니다. Codex Security가 완료된 워커 결과를
집계한 후 심층 스캔이 한도에 도달하면 CLI는 부분 검사 범위가 포함된
완료 보고서를 저장하고 종료 코드 `2`로 종료됩니다. 그렇지 않으면
사용 가능한 부분 출력을 보존합니다.

### 스캔으로 커밋과 Pull Request를 검사할 수 있나요

스테이징된 변경 사항과 스테이징되지 않은 변경 사항을 대상으로 커밋 전 보안 검사를 설치하세요:

```bash
npx @openai/codex-security install-hook

Pull Request를 검사하려면 커밋된 변경 사항을 스캔하고 심각도
임곗값을 설정하세요:

```bash
npx @openai/codex-security scan . \
  --diff origin/main \
  --fail-on-severity high

전체 스캔에서 선택한 심각도 이상의 보안 이슈를 발견하면 종료 코드 `1`을
반환합니다. [CI에서 스캔 실행](/ko-KR/codex/security/cli/ci)에서
전체 GitHub Actions 워크플로우, 아티팩트 처리, SARIF 내보내기를 확인하세요.

### 다른 애플리케이션에서 스캔을 직접 실행할 수 있나요

네. [TypeScript SDK](/ko-KR/codex/security/sdk)를 사용하면 애플리케이션이나 개발자 도구에서 스캔을 시작하고,
대상을 선택하며 보안 이슈와 커버리지를 확인하고 진행 상황을 추적하는 동시에
비용을 제어할 수 있습니다.

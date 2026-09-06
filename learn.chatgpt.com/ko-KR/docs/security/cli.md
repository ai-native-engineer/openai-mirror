<!-- source: https://learn.chatgpt.com/ko-KR/docs/security/cli -->

Codex Security는 보안 및 엔지니어링 팀이 취약점을 발견하고 확인하고 수정하도록
지원합니다. 명령줄 인터페이스(CLI)를 사용해 소유하거나 평가 권한이 있는
레포지토리를 스캔하고, 시간 경과에 따른 보안 이슈를 검토하며, 변경사항이 반영되기
전에 확인하세요.

  `@openai/codex-security` 패키지는 공개되어 있습니다. 스캔을 실행하려면 Codex
  Security 액세스 권한이 필요합니다. Codex에서 대화형 스캔을 실행하려면 [Codex
  Security 플러그인 빠른 시작](/ko-KR/codex/security/plugin)부터 진행하세요. 연결된 GitHub
  레포지토리에 대해서는 [Codex Security 클라우드 설정](/ko-KR/codex/security/setup)을 참조하세요.

## 사전 요구 사항 확인

CLI를 사용하려면 Node.js 22(22.13.0 이상), 24 또는 26이 필요합니다. 스캔, 일괄 스캔,
내보내기, 스캔 기록, 저장된 보안 이슈를 사용하려면 Python 3.10 이상도 필요합니다.
자세한 내용은 [인증 및
사전 요구 사항](/ko-KR/codex/security/cli/reference#authentication-and-prerequisites)을 참조하세요.

## CLI 설정 및 확인

`npx`로 CLI를 실행하고 버전을 확인하세요:

```bash
npx @openai/codex-security --version

패키지 버전과 함께 제공되는 플러그인의 버전을 모두 확인하려면 다음 명령어를 실행하세요:

```bash
npx @openai/codex-security info --json

패키지 변경 사항은 [CLI 및 SDK 릴리스](https://github.com/openai/codex-security/releases)에서
확인하세요.

사용 가능한 명령어를 나열하세요:

```bash
npx @openai/codex-security --help

[CLI 참조 자료](/ko-KR/codex/security/cli/reference)도 확인하세요.

## 로그인

로컬에서 사용하려면 ChatGPT 계정으로 로그인하세요:

```bash
npx @openai/codex-security login

원격 또는 헤드리스 머신에서는 기기 인증을 사용하세요:

```bash
npx @openai/codex-security login --device-auth

CI 및 기타 자동화 워크플로우에서는 OpenAI API 키를 설정하세요:

```bash

AWS 자격 증명은 [Amazon Bedrock
설정](/ko-KR/codex/security/cli/reference#use-amazon-bedrock)을 참조하세요. [OpenRouter 또는
Fireworks](/ko-KR/codex/security/cli/reference#use-openrouter-or-fireworks)를 사용하려면 공급자의 API 키를
설정하고 `--provider` 및 `--model` 옵션으로 모델을 선택하세요.

API 키도 설정되어 있을 때 ChatGPT 로그인을 사용하려면 해당 방식을 명시적으로 선택하세요:

```bash
npx @openai/codex-security scan . --auth chatgpt

환경에 설정된 API 키를 반드시 사용하려면 API 키 인증을 선택하세요:

```bash
npx @openai/codex-security scan . --auth api-key

계정과 레포지토리에 따라 레포지토리 전체를 스캔하려면
[Trusted Access for Cyber](https://chatgpt.com/cyber)도 필요할 수 있습니다.

## 스캔 준비

신뢰할 수 있고 평가 권한이 있는 레포지토리를 선택하세요. 스캔은
로컬 운영체제 권한을 사용하며 승인을 받기 위해 일시 중지되지 않습니다.
스캔 프로세스가 실행 환경을 상속할 수 있으므로 시작하기 전에
관련 없는 자격 증명을 제거하세요. [로컬 스캔
권한](/ko-KR/codex/security/cli/reference#local-scan-permissions)을 참조하세요.

스캔 결과를 저장할 디렉터리는 레포지토리 외부에서 선택하세요:

```bash
REPOSITORY=/path/to/repository
SCAN_DIR=/path/outside/repository/codex-security-results

`--output-dir` 옵션을 생략하면 Codex Security는 자체 영구
상태 디렉터리에 결과를 저장합니다. 결과에 소스 코드 발췌문과 취약점 세부 정보가 포함될 수 있으므로
비공개 저장 위치와 적절한 보존 정책을 선택하세요.

기본 상태 디렉터리에 쓸 수 없다면 스캔 대상 레포지토리 외부에서
쓰기 가능한 디렉터리를 선택하세요:

```bash

스캔을 시작하기 전에 레포지토리, 대상, 출력 디렉터리를 확인하세요:

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR" --dry-run

드라이런은 `--knowledge-base` 경로를 포함한 로컬 입력을 확인하지만
Codex를 시작하거나 자격 증명을 로드하거나 플러그인의 Python
인터프리터를 점검하지는 않습니다.

## 첫 스캔 실행

표준 스캔을 실행하고 선택한 디렉터리에 결과를 보관하세요:

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR"

대화형 터미널에는 실시간 스캔 대시보드가 표시됩니다. `--headless` 옵션을 추가하면
대신 진행 상황이 일반 텍스트 줄로 표시됩니다. CI와 대화형 세션이 없는 터미널에서는
진행 상황이 자동으로 일반 텍스트 줄로 표시됩니다.

대시보드에는 실시간 세션 세부 정보도 표시됩니다. 소스 코드나
자격 증명이 포함될 수 있으므로 공유하기 전에 내용을 검토하세요.

기본적으로 CLI는 스캔 진행 상황과 완료 요약을 stderr에 기록합니다.
전체 스캔 결과는 stdout에 출력하지 않습니다. 스캔이 완료되면 다음과 같은
요약이 출력됩니다:

```text
  REPORT    /path/outside/repository/codex-security-results/report.md

  FINDINGS  2 (2 confirmed this scan; 0 previously found; 1 high, 1 medium)
  COVERAGE  complete
  ELAPSED   42s
  RESULTS   /path/outside/repository/codex-security-results

사용 가능한 경우 토큰 사용량과 예상 비용이 표시됩니다. 전체 결과를 기계 판독 가능한
JSON으로 출력하려면 구조화된 출력을 명시적으로 요청하세요:

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR" --json

스캔은 기본적으로 보고서만 생성하므로 보안 이슈를 로컬에서
계속 검토할 수 있습니다. [CI에서 스캔을
실행](/ko-KR/codex/security/cli/ci)할 준비가 되면 심각도 임곗값을 추가하는 것이 좋습니다.

## 모델 및 추론 수준 선택

스캔에서는 기본적으로 `gpt-5.6-sol` 모델과 `xhigh` 추론 수준을 사용합니다. 작업에
필요한 경우 다른 모델과 추론 수준을 선택하세요:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --model gpt-5.6-terra \
  --effort high

지원되는 추론 수준은 `minimal`, `low`, `medium`, `high`, `xhigh` 및
`max`입니다.

## 결과 검토

읽기 쉬운 결과를 보려면 `report.md`를 여세요. 스캔 디렉터리에는
자동화에 사용되는 구조화된 파일도 포함되어 있습니다:

```text
codex-security-results/
├── scan-manifest.json
├── findings.json
├── coverage.json
├── report.md
├── artifacts/
└── exports/
    └── results.sarif       # when produced

- `scan-manifest.json`에는 대상, 범위, 생성 주체, 봉인된
  아티팩트가 기록됩니다.
- `findings.json`에는 각 보안 이슈의 심각도, 신뢰도, 위치, 증거,
  수정 방법이 기록됩니다.
- `coverage.json`에는 검토된 영역, 제외 항목, 보류된 작업, 미해결
  질문, 커버리지 완전성이 기록됩니다.

커버리지 상태는 `complete`, `partial`, `unknown` 중 하나입니다. 스캔을 검토 근거로 삼기 전에
보류된 영역이나 미해결 질문을 확인하세요.
[CLI 참조 자료](/ko-KR/codex/security/cli/reference#scan-artifacts)에서
전체 아티팩트 및 출력 규약을 확인할 수 있습니다.

## 보안 이슈 검토 및 패치

보안 이슈가 발견된 대화형 스캔을 완료하면 CLI에서 보안 이슈
브라우저를 제공합니다. 증거를 검토하고 수정할 보안 이슈를 선택하세요. 저장된
작업은 Codex 데스크톱 앱에서 확인할 수 있습니다.

브라우저를 사용하지 않고 심각도가 높거나 치명적인 보안 이슈를 패치하려면:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --patch --patch-severity high --json

검증된 패치를 커밋하고 GitHub Pull Request를 생성하려면 `--create-pr` 옵션을 추가하세요.

저장된 보안 이슈를 패치하거나 Linear 이슈를 가져올 수도 있습니다.
[`validate` 및 `patch` 참조 자료](/ko-KR/codex/security/cli/reference#codex-security-validate-and-codex-security-patch)를 확인하세요.

## 다음 스캔 선택

레포지토리에 독립된 서비스나 패키지가 포함되어 있다면 경로 스캔을 사용하세요:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --path services/billing \
  --path packages/auth

기준 리비전과 `HEAD` 사이에 커밋된 변경사항을 검토하세요:

```bash
npx @openai/codex-security scan "$REPOSITORY" --diff origin/main --head HEAD

`HEAD`를 기준으로 스테이징된 변경사항과 스테이징되지 않은 변경사항을 검토하세요:

```bash
npx @openai/codex-security scan "$REPOSITORY" --working-tree --base HEAD

diff 스캔과 작업 트리 스캔에서는 레포지토리 인수로 Git 작업 트리 루트를
지정해야 합니다. diff 스캔을 시작하기 전에 선택한 리비전을 가져오세요.

레포지토리나 경로를 더 폭넓게 검토해야 할 때는 심층 모드를 사용하세요:

```bash
npx @openai/codex-security scan "$REPOSITORY" --mode deep

워커, 하위 에이전트, 스캔 중지 시점을 제어하려면:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --mode deep \
  --workers 2 \
  --subagents 0 \
  --stop-after-no-new 3 \
  --max-discovery-runs 10 \
  --max-time-hours 1.5

이 옵션은 심층 모드에서만 사용할 수 있습니다. 심층 모드는 레포지토리와 경로 대상을
지원하지만 diff 스캔이나 작업 트리 스캔은 지원하지 않습니다. 여기서 `--workers` 옵션은 단일 스캔 내에서
독립적으로 실행되는 표준 스캔 워커를 제어하고, `bulk-scan --workers` 옵션은 동시에 실행되는
레포지토리 스캔을 제어합니다. `--max-time-hours` 옵션에는 `96` 이하의 양수를 지정할 수 있으며,
시간을 소수 단위로도 설정할 수 있습니다. 한도에 도달하면 완료되지 않은 워커를 중지하고,
완료된 스캔 결과를 보존하여 최종 보고서에 취합합니다.

## 아키텍처 및 보안 컨텍스트 추가

아키텍처 문서, 위협 모델 또는 보안 정책을 스캔 컨텍스트로
제공하세요. 그러면 Codex Security가 시스템의 실제 작동 방식을 기준으로
보안 이슈를 평가하는 데 도움이 됩니다:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

## 맞춤형 스캔 지침 추가

보안 우선순위에 집중하도록 스캔 지침을 추가하세요. 후속 지침에는
두 번째 파일을 사용하세요:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --scan-prompt-file /path/to/scan.md \
  --post-scan-prompt-file /path/to/follow-up.md

성공한 스캔과 커버리지가 불완전하거나 오류가 발생한 스캔이 끝나면
동일한 인증 세션에서 후속 작업이 실행됩니다. 후속 작업에 실패하면 CLI가
경고를 표시하고 완료된 스캔 결과를 유지합니다. 스캔이 취소되거나
비용 한도에 도달한 경우에는 후속 작업이 실행되지 않습니다. 두 옵션 모두
`bulk-scan`에서도 사용할 수 있으며, CSV의 `prompt` 열에 레포지토리별 지침을 추가할 수 있습니다.

## 스캔 예산 설정

`--max-cost` 옵션을 사용하면 예상 모델 비용이 USD로 지정한 한도를
초과할 때 스캔을 중지할 수 있습니다:

```bash
npx @openai/codex-security scan "$REPOSITORY" --max-cost 5

이미 진행 중인 요청은 한도를 조금 초과한 상태에서 완료될 수 있습니다. 심층
스캔 중 Codex Security가 완료된 워커 결과를 집계한 뒤 한도에
도달하면 CLI는 완성된 보고서를 저장하고 커버리지를 `partial`로 표시한 뒤
종료 코드 `2`를 반환합니다. 스캔에서 완성된 보고서를 생성할 수 없는 경우
사용 가능한 부분 출력은 디스크에 그대로 남습니다.

## 커밋할 때마다 변경 사항 미리 스캔

레포지토리에 Git pre-commit 보안 검사를 설치하세요:

```bash
npx @openai/codex-security install-hook

이 검사는 커밋할 때마다 스테이징된 변경 사항과 스테이징되지 않은 변경 사항을 스캔합니다.
기존 pre-commit 스크립트를 대체하지 않으며 심각도가 높은 보안 이슈나
스캔 오류가 있으면 커밋을 차단합니다.

## 레포지토리 대량 스캔

레포지토리를 검색하기 전에 GitHub에 로그인하세요:

```bash
gh auth login

GitHub 계정이나 조직에서 레포지토리를 검색하고 선택하세요:

```bash
npx @openai/codex-security bulk-scan

대화형 플로우에서는 보관된 레포지토리와 포크가 제외되며, 스캔을 시작하기 전에
선택한 레포지토리를 확인하라는 메시지가 표시됩니다.

미리 준비한 레포지토리 목록을 스캔하려면 CSV와 출력 디렉터리를 지정하세요:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

같은 명령어를 다시 실행하면 기존 대량 스캔을 재개할 수 있습니다. Codex Security는
완료된 레포지토리를 건너뜁니다. 레포지토리 또는 스캔에서 일시적인 오류가 발생했을 때 재시도하려면 `--max-attempts 3`을
추가하세요.

GitHub 검색, CSV 준비, 캠페인 결과, Docker 설정에 관한 자세한 내용은
[대량 보안 스캔 실행](/ko-KR/codex/security/cli/bulk-scans)을 참조하세요.

## Docker에서 대량 스캔 실행

Codex Security Docker 이미지를 사용할 권한이 있다면 제공된 보안 강화 Compose 구성과
보안 프로필을 Linux Docker 호스트에서 사용하세요. 호스트는 비특권 사용자
네임스페이스 생성을 지원해야 합니다. 레포지토리 CSV를 제공하고 결과와 로그인 상태를
영구 마운트 디렉터리에 보관하세요. 자격 증명은 실행 환경이나
시크릿 관리자를 통해 제공하세요:

```bash
docker compose run --rm codex-security \
  bulk-scan /input/repositories.csv \
  --output-dir /output \
  --workers 4

컨테이너는 대화형 프롬프트 없이 대량 스캔을 실행합니다. 레포지토리를 대화형으로 검색하려면
Docker 외부에서 CLI를 사용하세요. 비공개
레포지토리의 경우 `GH_TOKEN`이나 `GITHUB_TOKEN`을 실행 환경이나
시크릿 관리자를 통해 제공하세요. 계정과 레포지토리 접근 권한을 포함한 [로그인 요구 사항](#sign-in)은
컨테이너 스캔에도 적용됩니다.

## 저장된 스캔 다시 확인

레포지토리의 저장된 스캔 목록을 확인하세요:

```bash
npx @openai/codex-security scans list "$REPOSITORY"

결과에서 스캔 ID를 복사해 해당 스캔의 보안 이슈와 구성을 확인하세요:

```bash
npx @openai/codex-security scans show SCAN_ID

스캔 및 관련 워커의 저장된 이벤트를 확인하려면:

```bash
npx @openai/codex-security scans logs SCAN_ID

저장된 로그에서는 민감한 정보가 가려지지 않으며 소스 코드나 자격 증명이 포함될 수 있습니다.
공유하기 전에 검토하세요.

레포지토리의 모든 스캔에서 미해결 보안 이슈 목록을 확인하세요:

```bash
npx @openai/codex-security findings list "$REPOSITORY"

최신 스캔에서 이전에 발견된 보안 이슈가 확인되지 않아도 해당 이슈는 미해결 상태로 유지됩니다.

검토한 보안 이슈를 오탐으로 표시하려면 해당 이슈가 적용되지 않는 이유를
설명하세요:

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The route already checks permissions"

이후 스캔에서는 해당 설명을 고려하지만 현재 코드는 다시 검사합니다.

원래 구성을 사용해 현재 체크아웃을 대상으로 동일한 스캔을 실행하세요:

```bash
npx @openai/codex-security scans rerun SCAN_ID

두 스캔을 비교해 새로 발견되었거나, 지속되거나, 다시 열렸거나, 해결되었거나, 상태를 알 수 없는
보안 이슈를 찾으세요:

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

비교 시 근본 원인을 기준으로 보안 이슈를 자동으로 매칭하고 저장된
매칭 결과를 재사용합니다.

대량 스캔용 CSV 형식, 스캔 기록 필터, 명령어 옵션은
[CLI 참조 자료](/ko-KR/codex/security/cli/reference)에서 확인하세요.

목표에 맞는 워크플로우를 선택해 계속 진행하세요:

- [대량 보안 스캔 실행](/ko-KR/codex/security/cli/bulk-scans)을 통해 GitHub
  레포지토리를 검색하거나 고정된 CSV 인벤토리를 스캔하세요.
- [CLI 자주 묻는 질문](/ko-KR/codex/security/cli/faq)에서 스캔 기록,
  오탐 피드백, 커버리지, 수정 사항 검증에 관한 답변을 확인하세요.
- [CI에서 스캔 실행](/ko-KR/codex/security/cli/ci)을 통해 Pull Request를 검토하고 결과를
  보존하며 심각도 정책을 설정하세요.
- [CLI 참조 자료](/ko-KR/codex/security/cli/reference)에서 모든 플래그,
  출력 형식, 아티팩트, 종료 코드를 확인하세요.
- [TypeScript SDK를 통합](/ko-KR/codex/security/sdk)해
  애플리케이션이나 개발자 도구에서 스캔을 실행하세요.

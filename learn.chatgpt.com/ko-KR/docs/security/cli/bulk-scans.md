<!-- source: https://learn.chatgpt.com/ko-KR/docs/security/cli/bulk-scans -->

`npx @openai/codex-security bulk-scan` 명령어로 여러 레포지토리를 하나의
캠페인에서 검토하세요. 개인 GitHub 계정이나
조직에서 레포지토리를 탐색하거나, 각 레포지토리를 정확한 Git
리비전에 고정하는 CSV를 제공하세요.

  `@openai/codex-security` 패키지는 공개되어 있습니다. 스캔을 실행하려면
  Codex Security 액세스 권한이 필요합니다. [CLI 빠른 시작](/ko-KR/codex/security/cli)을 참고해
  CLI를 설치하고 로그인하세요.

## 레포지토리 소스 선택

| 소스           | 사용 시점                                                                          |
| ---------------- | --------------------------------------------------------------------------------------- |
| GitHub 탐색 | 개인 GitHub 계정이나 조직에서 대화형으로 레포지토리를 선택합니다. |
| CSV 인벤토리    | 정확한 레포지토리 리비전을 대상으로 반복 실행 가능한 자동화 캠페인을 실행합니다.                |

두 워크플로우 모두 진행 상태를 저장하고 레포지토리별 결과를 보존하므로,
중단된 후에도 캠페인을 재개할 수 있습니다.

## GitHub 레포지토리 탐색

GitHub CLI로 로그인하세요:

```bash
gh auth login

대화형 일괄 스캔을 시작하세요:

```bash
npx @openai/codex-security bulk-scan

CLI가 다음 단계를 안내합니다:

1. 개인 GitHub 계정이나 조직을 선택하세요.
2. 최근 90일 동안 활동한 레포지토리를 검토하세요.
3. 레포지토리 목록을 검색하고 스캔할 레포지토리를 선택하세요.
4. 스캔 결과를 저장할 디렉터리를 선택하세요.
5. 선택한 레포지토리를 검토하고 캠페인을 확정하세요.

아카이브된 레포지토리와 포크는 탐색 대상에서 제외됩니다.
CLI는 선택한 각 레포지토리의 정확한 기본 브랜치 커밋을
`<output-directory>/repositories.csv`에 기록합니다. 선택을 확정하기 전에는
스캔이 시작되지 않습니다.

GitHub Enterprise Server를 사용하려면 먼저 GitHub 호스트에 로그인하세요:

```bash
gh auth login --hostname github.example.com

레포지토리 탐색을 시작할 때 `GH_HOST`를 설정하세요:

```bash
GH_HOST=github.example.com npx @openai/codex-security bulk-scan

대화형 탐색에는 터미널이 필요합니다. CI나 컨테이너에서 실행하거나 미리 준비한
레포지토리 목록을 사용할 때는 CSV 인벤토리를 대신 사용하세요.

## 레포지토리 CSV 만들기

각 레포지토리와 고정된 리비전을 한 행씩 입력한 CSV를 만드세요:

```csv
id,repository,revision,scope,mode,prompt
payments,https://github.com/example/payments.git,0123456789abcdef0123456789abcdef01234567,services/api,standard,Review payment authorization and refunds.
identity,https://github.com/example/identity.git,fedcba9876543210fedcba9876543210fedcba98,,deep,Review session and identity boundaries.

CSV는 다음 열을 지원합니다:

| 열       | 필수 | 설명                                                                                                |
| ------------ | -------- | ---------------------------------------------------------------------------------------------------------- |
| `id`         | 예      | 고유한 레포지토리 식별자입니다. 영문자, 숫자, 마침표, 하이픈 또는 밑줄을 사용하세요.                      |
| `repository` | 예      | HTTPS URL, SSH URL 또는 로컬 레포지토리 경로입니다. 상대 경로는 CSV 파일이 있는 디렉터리를 기준으로 해석됩니다.               |
| `revision`   | 예      | 40자 또는 64자로 구성된 전체 Git 커밋 SHA입니다. 브랜치 이름, 태그 및 축약된 커밋 해시는 지원되지 않습니다. |
| `scope`      | 아니요       | 스캔할 디렉터리를 레포지토리 기준 상대 경로로 지정합니다. 전체 레포지토리를 스캔하려면 값을 생략하세요.                       |
| `mode`       | 아니요       | `standard` 또는 `deep`입니다. 명령어에서 선택한 모드를 사용하려면 값을 생략하세요.                                   |
| `prompt`     | 아니요       | 해당 레포지토리 전용 스캔 지침입니다.                                                             |

로컬 레포지토리의 전체 커밋 SHA를 확인하려면 다음 명령어를 실행하세요:

```bash
git -C /path/to/repository rev-parse HEAD

## CSV로 캠페인 실행

CSV와 레포지토리 외부의 비공개 출력 디렉터리를 지정하세요:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

`--workers` 옵션은 동시에 실행되는 레포지토리 스캔 수를 제어하며 기본값은 `4`입니다.
이 옵션은 각 심층 스캔에서 독립적으로 실행되는 표준 스캔 워커 수를 설정하지 않습니다.
해당 제한은
[`[deep_scan]`](/ko-KR/codex/security/cli/reference#configure-deep-scans)에서 설정하세요. `--mode
deep` 옵션을 사용하면 자체 `mode`가 없는 행에 심층 스캔이 적용됩니다. 각 CSV 행에서는
스캔 모드와 레포지토리 범위를 개별적으로 선택할 수 있습니다.

`[deep_scan].max_time_hours`를 설정하면 캠페인의 각 심층 스캔에서
워커 실행을 제한할 수 있습니다. `--max-time-hours` 플래그는 `scan`에서만 사용할 수 있으며 `bulk-scan`에서는 사용할 수 없습니다.

CLI는 고정된 각 리비전을 체크아웃하고 선택한 대상을 스캔한 뒤 결과를
기록하고 임시로 체크아웃한 레포지토리를 제거합니다. 스캔이 전체 범위를
포괄하고 필요한 결과 아티팩트가 모두 존재하는 경우에만 해당 레포지토리가
완료된 것으로 간주됩니다.

## 보안 컨텍스트와 지침 공유

아키텍처 문서, 위협 모델 또는 보안 정책을 모든 스캔에 추가하려면
`--knowledge-base`를 사용하세요. 파일이나 디렉터리를 더 추가하려면 이 플래그를 반복해서 지정하세요:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

공통 스캔 지침을 추가하거나 각 스캔 후 후속 작업을 실행하려면
프롬프트 파일을 제공하세요:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --scan-prompt-file scan-instructions.md \
  --post-scan-prompt-file follow-up.md

CLI는 공통 스캔 지침 뒤에 각 레포지토리의 CSV `prompt`를 추가합니다.
후속 지침은 성공한 스캔뿐 아니라 스캔 범위가 불완전하거나 오류가 발생한 스캔 후에도
동일한 인증 세션에서 실행되지만, 스캔이 취소되거나 비용 한도에 도달하면
실행되지 않습니다. 프롬프트 파일 경로는
현재 디렉터리를 기준으로 해석됩니다.

## 모델 및 추론 노력 수준 선택

일괄 스캔에서는 기본적으로 `gpt-5.6-sol` 모델과 `xhigh` 추론 노력 수준을 사용합니다.
CSV 캠페인에 다른 모델과 추론 노력 수준을 선택하려면 다음을 실행하세요:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --model gpt-5.6-terra \
  --effort high

대화형 레포지토리 탐색에서도 동일한 옵션을 사용할 수 있습니다:

```bash
npx @openai/codex-security bulk-scan --model gpt-5.6-terra --effort high

지원되는 추론 노력 수준은 `minimal`, `low`, `medium`, `high`, `xhigh`입니다.

OpenRouter 또는 Fireworks를 사용하려면 각각 `OPENROUTER_API_KEY` 또는 `FIREWORKS_API_KEY`를 설정하고
`--provider`와 `--model`을 지정하세요. 자격 증명과
사용 예시는 [OpenRouter 또는 Fireworks
설정](/ko-KR/codex/security/cli/reference#use-openrouter-or-fireworks)이나 [Amazon Bedrock
설정](/ko-KR/codex/security/cli/reference#use-amazon-bedrock)을 참고하세요.

## 캠페인 결과 검토

출력 디렉터리에는 고정된 캠페인, 추가만 가능한 결과 원장,
그리고 각 레포지토리와 실행 시도별로 구분된 아티팩트가 포함됩니다:

```text
security-scans/
├── manifest.json
├── results.jsonl
├── checkouts/
└── artifacts/
    ├── payments/
    │   └── attempt-1/
    │       ├── scan-manifest.json
    │       ├── findings.json
    │       ├── coverage.json
    │       └── report.md
    └── identity/
        └── attempt-1/
            ├── scan-manifest.json
            ├── findings.json
            ├── coverage.json
            └── report.md

- `manifest.json`에는 캠페인의 레포지토리, 고정된 리비전, 범위, 스캔
  모드, 공통 지침 또는 레포지토리별 지침이 기록됩니다.
- `results.jsonl`에는 각 레포지토리의 실행 시도와 상태, 아티팩트
  디렉터리, 확인 가능한 비용 또는 오류 세부 정보가 기록됩니다.
- `report.md`에는 레포지토리 실행 시도 한 건에 대한 읽기 쉬운 보고서가 포함되어 있습니다.
- `findings.json`과 `coverage.json`에는 해당 실행 시도의 보안 이슈와
  검토 범위가 기록됩니다.

결과를 다른 곳에서 사용할 수 있어야 한다면 완료된 레포지토리 스캔 하나를 내보내세요:

```bash
npx @openai/codex-security export \
  /path/outside/repositories/security-scans/artifacts/payments/attempt-1 \
  --export-format sarif \
  --output /path/outside/repositories/payments.sarif

결과에는 소스 코드 발췌 내용과 취약점 세부 정보가 포함될 수 있습니다.
출력 디렉터리는 스캔한 레포지토리 외부에 비공개로 보관하고
적절한 보존 정책을 적용하세요.

## 캠페인 재개

동일한 CSV와 출력 디렉터리를 사용해 원래 명령어를 다시 실행하세요:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

CLI는 완료되지 않은 레포지토리 스캔을 재개하고 완료된 스캔은 건너뜁니다.
커버리지가 불완전한 스캔은 재시도하지 않습니다. 해당 결과는 계속 확인할 수 있으며,
명령어는 종료 코드 `2`로 종료됩니다.

기존 출력 디렉터리에서는 레포지토리 인벤토리나 스캔 및 후속 지침을
변경하지 마세요. CLI는 고정된 매니페스트를 확인하고 다른
캠페인은 거부합니다. 레포지토리, 리비전, 범위, 스캔 모드, 공유 지침
또는 레포지토리별 지침을 변경할 때는 새 출력 디렉터리를 사용하세요.

## 레포지토리 오류 재시도

`--max-attempts`를 사용해 일시적인 체크아웃 오류나 스캔 오류가 발생한
레포지토리를 재시도하세요:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --max-attempts 3

기본값은 레포지토리당 한 번의 시도입니다. 각 시도에는 별도의
실행 기록과 아티팩트 디렉터리가 생성됩니다. 체크아웃 오류, 스캔 실패,
필수 아티팩트 누락은 재시도 대상입니다. 커버리지가 불완전한 상태로 완료된
스캔은 재시도하지 않습니다.

대량 스캔의 종료 코드는 다음과 같습니다:

| 종료 코드 | 의미                                                                                                               |
| --------- | --------------------------------------------------------------------------------------------------------------------- |
| `0`       | 모든 레포지토리의 스캔이 성공적으로 완료되었습니다.                                                                              |
| `2`       | 레포지토리 스캔이 완료되지 않았거나, 스캔 커버리지가 불완전했거나, 명령어 실행 중 입력 또는 런타임 오류가 발생했습니다. |
| `130`     | Ctrl-C로 캠페인이 중단되었습니다.                                                                                      |
| `143`     | SIGTERM으로 캠페인이 종료되었습니다.                                                                                      |

## Docker에서 대량 스캔 실행

[Codex Security
레포지토리](https://github.com/openai/codex-security)에는 Linux Docker 호스트에서 자동화된 CSV 캠페인을 실행하기 위한
보안이 강화된 Compose 구성이 포함되어 있습니다. 호스트는
비특권 사용자 네임스페이스 생성을 지원해야 합니다.

레포지토리 CSV, 스캔 결과 및 로그인 상태를 영구
디렉터리에 마운트한 상태로 유지하세요. OpenAI 자격 증명은 환경 변수 또는 시크릿
관리자를 통해 제공하세요. 비공개 GitHub 레포지토리에는 `GH_TOKEN` 또는 `GITHUB_TOKEN`도
같은 방식으로 제공하세요.

마운트한 CSV와 출력 디렉터리를 사용해 이미지를 실행하세요:

```bash
docker compose run --rm codex-security \
  bulk-scan /input/repositories.csv \
  --output-dir /output \
  --workers 4

앞서 마운트한 CSV와 출력 디렉터리를 그대로 사용해 캠페인을 재개하세요.
GitHub Enterprise Server의 경우 `CODEX_SECURITY_GIT_HOST`를 GitHub 호스트로 설정하세요.

사용 가능한 모든 플래그는 [bulk-scan 명령어
참조 자료](/ko-KR/codex/security/cli/reference#codex-security-bulk-scan)에서 확인하세요.
스캔 커버리지와 보안 이슈에 관한 자주 묻는 질문은 [CLI
자주 묻는 질문](/ko-KR/codex/security/cli/faq)을 참조하세요.

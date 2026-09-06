<!-- source: https://learn.chatgpt.com/ko-KR/docs/security/cli/reference -->

이 참조 자료에서 지원되는 `codex-security` 명령어, 플래그,
출력 형식과 종료 동작을 확인하세요. 안내에 따라 첫 스캔을 진행하려면
[CLI 빠른 시작](/ko-KR/codex/security/cli)부터 확인하세요.

  `@openai/codex-security` 패키지는 공개되어 있습니다. 스캔을 실행하려면
  Codex Security 액세스 권한이 필요합니다. 스캔은 로컬 권한을 사용하며
  승인을 기다리기 위해 일시 중지되지 않습니다. 시작하기 전에 [로컬 스캔
  권한](#local-scan-permissions)을 검토하세요.

`npx @openai/codex-security`로 CLI를 실행하세요.

## 명령어 개요

```text
usage: codex-security [--version] <command> [options]

CLI는 다음 명령어를 제공합니다:

| 명령어                       | 용도                                               |
| ----------------------------- | ----------------------------------------------------- |
| `codex-security scan`         | Codex Security 스캔을 실행합니다.                            |
| `codex-security install-hook` | Git pre-commit 보안 스캔을 설치합니다.               |
| `codex-security bulk-scan`    | 레포지토리를 검색하고 재개 가능한 일괄 스캔을 실행합니다.   |
| `codex-security scans`        | 저장된 스캔 로그를 나열, 검사, 비교하고 가져옵니다. |
| `codex-security findings`     | 저장된 보안 이슈를 검토하고 업데이트합니다.            |
| `codex-security export`       | 완료된 보안 이슈를 CSV, JSON 또는 SARIF 형식으로 내보냅니다.     |
| `codex-security publish`      | 완료된 스캔의 보안 이슈를 Linear에 게시합니다.            |
| `codex-security validate`     | 하나 이상의 보안 이슈 후보를 확인합니다.        |
| `codex-security patch`        | 하나 이상의 보안 이슈에 패치를 적용합니다.                    |
| `codex-security login`        | 로그인하거나 자격 증명을 저장하거나 로그인 상태를 확인합니다.  |
| `codex-security logout`       | 저장된 로그인 정보를 삭제합니다.                            |
| `codex-security info`         | SDK와 번들 플러그인의 읽기 전용 메타데이터를 표시합니다.       |

CLI는 다음 연동 명령어도 제공합니다:

| 명령어                      | 용도                               |
| ---------------------------- | ------------------------------------- |
| `codex-security completions` | 셸 자동 완성 스크립트를 생성합니다.    |
| `codex-security mcp`         | CLI를 MCP 서버로 등록합니다.    |
| `codex-security skills`      | Codex Security 스킬을 에이전트에 동기화합니다. |

사용 가능한 모든 명령어를 나열합니다:

```bash
npx @openai/codex-security --help

명령어의 인수와 옵션을 확인하려면 해당 명령어에 `--help`를 추가하세요:

```bash
npx @openai/codex-security scan --help

`codex-security --version` 명령어는 설치된 버전을 출력하고 종료합니다.
`codex-security info --json` 명령어는 SDK와 번들 플러그인의 버전을 출력합니다.
두 명령어 모두 Python이 필요하지 않습니다.

### 명령어 검색 및 에이전트 연결

에이전트가 읽을 수 있는 명령어 매니페스트를 출력합니다:

```bash
npx @openai/codex-security --llms

스캔 인수 스키마를 JSON으로 확인합니다:

```bash
npx @openai/codex-security scan --schema --format json

Bash용 셸 자동 완성을 생성합니다:

```bash
npx @openai/codex-security completions bash

해당 셸을 사용하려면 `bash`를 `zsh` 또는 `fish`로 바꾸세요.

스캔 결과는 `--format toon|json|yaml|jsonl` 및 `--full-output` 옵션을 지원합니다.
프레임워크 수준의 `--format` 옵션은 `--export-format` 옵션과 별개입니다.
후자는 완료된 스캔에서 내보내는 아티팩트의 형식을 선택합니다. 전역 명령어 도움말에는
`md`도 표시되지만, 스캔 결과는 Markdown 출력을 지원하지 않습니다.

CLI를 MCP 서버로 등록합니다:

```bash
npx @openai/codex-security mcp add

Codex Security 스킬을 에이전트에 동기화합니다:

```bash
npx @openai/codex-security skills add

MCP는 읽기 전용 `info` 메타데이터 명령어만 제공합니다. 스캔, 내보내기,
인증, 검증 및 패치는 CLI에서만 사용할 수 있습니다.

## `codex-security scan`

레포지토리, 선택한 경로, 커밋된 변경 사항 또는
작업 트리를 대상으로 스캔을 실행합니다.

```text
usage: codex-security scan [-h] [--auth {auto,chatgpt,api-key}]
                           [--provider {openai,openrouter,fireworks,amazon-bedrock}]
                           [--path PATH | --diff BASE | --working-tree]
                           [--head HEAD] [--base BASE]
                           [--knowledge-base PATH] [--scan-prompt-file FILE]
                           [--post-scan-prompt-file FILE]
                           [--mode {standard,deep}] [--workers N]
                           [--subagents N] [--stop-after-no-new N]
                           [--max-discovery-runs N] [--max-time-hours HOURS]
                           [--model MODEL]
                           [--effort {minimal,low,medium,high,xhigh,max}]
                           [--output-dir DIR]
                           [--archive-existing]
                           [--plugin-path PATH] [--python PATH]
                           [--codex KEY=VALUE] [--fail-on-severity LEVEL]
                           [--patch] [--patch-severity {critical,high,medium,low}]
                           [--create-pr]
                           [--max-cost USD] [--dry-run] [--headless] [--verbose]
                           [--json] [--format {toon,json,yaml,jsonl}]
                           [--full-output] [repository]

`repository`의 기본값은 현재 디렉터리입니다.

### 스캔 인증 선택

기본값인 `--auth auto`를 사용하면 자격 증명이 자동으로 선택됩니다.
ChatGPT 로그인과 `OPENAI_API_KEY` 또는 `CODEX_API_KEY`를 모두 사용할 수 있으면,
텍스트를 출력하는 대화형 스캔에서는 사용할 자격 증명을 묻습니다. CI 스캔, JSON 및
JSONL 스캔과 대화형 터미널 없이 실행되는 다른 스캔에서는
환경 변수에 설정된 API 키를 사용합니다. 드라이 런에서는 사용자에게 묻거나 자격 증명을 불러오지 않습니다.

저장된 자격 증명을 사용하려면 `--auth chatgpt`를 전달하세요:

```bash
npx @openai/codex-security scan . --auth chatgpt

환경 변수의 API 키를 사용하려면 `--auth api-key`를 전달하세요:

```bash
npx @openai/codex-security scan . --auth api-key

자동 선택 시 저장된 자격 증명을 기본으로 사용하려면
`unset OPENAI_API_KEY CODEX_API_KEY`를 실행하세요.

### OpenRouter 또는 Fireworks 사용

API 키와 명시적으로 지정한 모델을 사용해 OpenRouter를 선택하세요:

```bash

npx @openai/codex-security scan . \
  --provider openrouter \
  --model anthropic/claude-sonnet-4.5

API 키와 명시적으로 지정한 모델을 사용해 Fireworks를 선택하세요:

```bash

npx @openai/codex-security scan . \
  --provider fireworks \
  --model accounts/fireworks/models/qwen3-235b-a22b

두 프로바이더 모두 `bulk-scan`도 지원합니다.

### Amazon Bedrock 사용

`--provider amazon-bedrock`으로 Amazon Bedrock을 선택하고
`--model`로 Bedrock 모델을 명시적으로 지정하세요:

```bash
npx @openai/codex-security scan . \
  --provider amazon-bedrock \
  --model openai.gpt-5.6-sol

`AWS_REGION`을 설정하고 `AWS_BEARER_TOKEN_BEDROCK`, 표준 AWS
액세스 키, AWS 프로필, 웹 ID, 컨테이너 자격 증명 또는
기본 AWS 자격 증명 체인으로 인증하세요. Bedrock 스캔에서는
`--auth`, ChatGPT 로그인 또는 OpenAI API 키 대신 AWS 자격 증명을 사용합니다. `scan` 및 `bulk-scan` 명령어 모두
`--provider`를 지원합니다.

### 스캔 대상 선택

각 스캔에서 대상 유형을 하나만 선택하세요.

| 인수                 | 설명                                                                     |
| ------------------------ | ------------------------------------------------------------------------------- |
| `--path PATH`            | 레포지토리 기준 상대 경로를 스캔합니다. 경로를 추가하려면 플래그를 반복해서 사용하세요.         |
| `--diff BASE`            | `BASE`부터 `--head`까지 커밋된 변경 사항을 스캔합니다. 헤드의 기본값은 `HEAD`입니다.    |
| `--head HEAD`            | `--diff`에 사용할 헤드 리비전을 설정합니다.                                             |
| `--working-tree`         | 스테이징된 변경 사항과 스테이징되지 않은 변경 사항을 `--base` 기준으로 스캔합니다. 베이스의 기본값은 `HEAD`입니다. |
| `--base BASE`            | `--working-tree`에 사용할 베이스 리비전을 설정합니다.                                     |
| `--mode {standard,deep}` | 스캔 모드를 선택합니다. 기본값은 `standard`입니다.                                |

`--path`, `--diff`, `--working-tree`는 함께 사용할 수 없습니다. `--head`를 사용하려면
`--diff`가 필요하고, `--base`를 사용하려면 `--working-tree`가 필요합니다. 심층 모드는
레포지토리와 경로 대상을 지원합니다.

Diff 스캔과 작업 트리 스캔에서는 레포지토리 인수로 Git 작업 트리의
루트를 지정해야 합니다. 선택한 ref는 해당 체크아웃에 존재해야 합니다.

전체 레포지토리를 스캔합니다:

```bash
npx @openai/codex-security scan .

선택한 경로를 스캔합니다:

```bash
npx @openai/codex-security scan . --path src --path tests

커밋된 변경 사항을 스캔합니다:

```bash
npx @openai/codex-security scan . --diff origin/main --head HEAD

스테이징된 변경 사항과 스테이징되지 않은 변경 사항을 스캔합니다:

```bash
npx @openai/codex-security scan . --working-tree --base HEAD

레포지토리를 더 심층적으로 검토합니다:

```bash
npx @openai/codex-security scan . --mode deep

### 심층 스캔 구성

`--mode deep`과 함께 다음 옵션을 사용해 워커의 동시 실행 수와 실행 시간을 제어하세요:

| 인수                 | 설명                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------- |
| `--workers N`            | 동시에 실행할 수 있는 독립적인 표준 스캔 워커 수의 한도입니다. 기본값은 `4`입니다.                |
| `--subagents N`          | 각 워커에서 사용할 수 있는 하위 에이전트 수입니다. 기본값은 `3`입니다.                                   |
| `--stop-after-no-new N`  | 완료된 워커 스캔에서 `N`회 연속으로 새 보안 이슈가 발견되지 않으면 중지합니다. 기본값은 `4`입니다. |
| `--max-discovery-runs N` | 독립적인 표준 스캔의 총 실행 횟수 한도입니다. 기본값은 `40`입니다.                       |
| `--max-time-hours HOURS` | 워커 실행 시간 한도이며 단위는 시간입니다. 기본값은 `96`이며 소수도 지정할 수 있습니다.             |

`--subagents`에는 0 또는 양의 정수를 지정할 수 있습니다. `--max-time-hours`에는
`96` 이하의 양수를 지정할 수 있습니다. 나머지 옵션에는
양의 정수를 지정해야 합니다. 이러한 옵션은 표준 스캔에서는 사용할 수 없습니다.

예를 들어 워커 2개를 사용하고 최대 10회 실행하도록 허용한 뒤
1.5시간이 지나면 워커 실행을 중지하도록 설정합니다:

```bash
npx @openai/codex-security scan . \
  --mode deep \
  --workers 2 \
  --subagents 0 \
  --stop-after-no-new 3 \
  --max-discovery-runs 10 \
  --max-time-hours 1.5

시간 한도에 도달하면 완료되지 않은 워커를 중지하고 완료된
스캔 결과를 보존한 뒤 최종 보고서에 집계합니다. 어떤 워커도
소스 검토를 완료하지 못하면 부분 커버리지를 기록하고 종료 코드 `2`를 반환합니다.

지속적으로 적용할 기본값을 `~/.codex/codex-security/config.toml`에 설정하세요. `CODEX_HOME`을 설정한 경우에는
`$CODEX_HOME/codex-security/config.toml`에 설정하세요:

```toml
[deep_scan]
workers = 2
subagents = 0
stop_after_no_new = 3
max_discovery_runs = 10
max_time_hours = 1.5

명령줄 옵션은 이러한 기본값보다 우선합니다. `scan --workers`는
한 번의 심층 스캔에서 독립적인 표준 스캔 워커를 제어하고, `bulk-scan --workers`는
동시에 실행되는 레포지토리 스캔을 제어합니다. `stop_after_consecutive_errors`는
TOML 파일에서만 설정할 수 있으며 기본값은 `3`입니다.

### 보안 컨텍스트 추가

`--knowledge-base PATH` 옵션으로 아키텍처 문서, 위협 모델 또는
보안 정책을 제공하세요. 파일이나 디렉터리를 더 지정하려면 이 옵션을 반복하세요:

```bash
npx @openai/codex-security scan . \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

지원되는 문서 형식에는 `.md`, `.markdown`, `.txt`, `.pdf`, `.docx`
파일이 포함됩니다. CLI는 디렉터리를 재귀적으로 검색하고 링크된 입력 경로를 거부하며,
링크된 디렉터리 항목은 건너뜁니다. 추출한 문서 내용은
저장된 스캔 결과에 포함하지 않습니다.

### 스캔 지침 추가

스캔 지침을 추가하려면 텍스트 또는 Markdown 파일을
`--scan-prompt-file` 옵션으로 제공하세요. `--post-scan-prompt-file` 옵션을 사용하면
스캔이 성공한 뒤뿐 아니라 커버리지가 불완전하거나 오류가 발생한 뒤에도
동일한 인증 세션에서 후속 지침을 실행할 수 있습니다:

```bash
npx @openai/codex-security scan . \
  --scan-prompt-file security-focus.md \
  --post-scan-prompt-file follow-up.md

예를 들어 스캔 프롬프트에서 권한 부여 경계에 집중하도록 요청하고,
후속 지침에서는 스캔 디렉터리에 새 `post-scan-summary.md` 파일을 작성하도록 하세요.
후속 작업이 실패하면 CLI는 경고를 표시하고 완료된 스캔을 보존합니다.
스캔이 취소되거나 비용
한도에 도달하면 후속 작업은 실행되지 않습니다.

### 출력 및 정책 옵션 설정

다음 옵션을 사용해 아티팩트를 보관하거나 이전 결과를 보존하거나
기계 판독 가능한 결과를 생성하세요.

| 인수                   | 설명                                                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `--output-dir DIR`         | 스캔 아티팩트를 스캔 대상을 포함하는 Git 작업 트리 외부의 비공개 디렉터리에 저장합니다. 기본적으로 Codex Security의 영구 상태 저장소를 사용합니다. |
| `--archive-existing`       | 기존 결과를 `DIR.previous-<timestamp>-<id>`로 이동한 뒤 빈 출력 디렉터리에서 시작합니다. `--output-dir` 옵션이 필요합니다.  |
| `--fail-on-severity LEVEL` | 완료된 스캔에서 심각도가 `critical`, `high`, `medium` 또는 `low` 중 지정한 수준 이상인 보안 이슈가 보고되면 종료 코드 `1`을 반환합니다.                  |
| `--patch`                  | 스캔을 완료한 후 선택한 보안 이슈를 수정하고 검증합니다.                                                                      |
| `--patch-severity LEVEL`   | 심각도가 `critical`, `high`, `medium` 또는 `low` 중 지정한 수준 이상인 보안 이슈를 패치합니다. 기본값은 `low`입니다.                                        |
| `--create-pr`              | 검증된 패치 파일을 커밋하고 GitHub Pull Request를 생성합니다. `--patch` 옵션이 필요합니다.                                              |
| `--max-cost USD`           | 예상 모델 비용이 지정한 USD 금액을 초과하면 스캔을 중지합니다.                                                  |
| `--dry-run`                | 스캔을 시작하지 않고 레포지토리, 대상, 지식 베이스, 출력 디렉터리, Codex 구성을 확인합니다.             |
| `--headless`               | 대화형 스캔 대시보드 대신 일반 텍스트로 진행 상황을 표시합니다.                                                          |
| `--verbose`                | 민감 정보를 가린 수명 주기, 인증, 진행 상황, 비용 진단 정보를 stderr에 출력합니다.                                          |
| `--json`                   | 매니페스트, 보안 이슈, 커버리지, 경로, 턴 메타데이터를 하나의 JSON 문서로 출력합니다.                                           |
| `--format FORMAT`          | 전체 스캔 결과를 `toon`, `json`, `yaml` 또는 `jsonl` 형식으로 출력합니다.                                                        |
| `--full-output`            | 기본 구조화 출력 형식으로 전체 결과를 출력합니다.                                                        |

비용 한도는 추정치일 뿐 엄격한 지출 상한은 아닙니다. 이미 진행 중인 요청은
한도를 약간 초과한 상태로 완료될 수 있습니다. 심층 스캔에서 Codex Security가
완료된 워커 결과를 집계한 뒤 한도에 도달하면 CLI는 사용 가능한 결과를
봉인하고 커버리지를 `partial`로 표시한 다음 종료 코드 `2`를 반환합니다.
그렇지 않으면 `2`를 반환하고 사용 가능한 부분 결과를 디스크에 남겨 둡니다.

`--output-dir` 옵션을 생략하면 결과는
`$CODEX_HOME/state/plugins/codex-security/scans/<repository>` 아래에 계속 저장됩니다. `CODEX_HOME`의
기본값은 `~/.codex`입니다. `CODEX_SECURITY_STATE_DIR` 환경 변수를 설정하면 결과를 대신
`$CODEX_SECURITY_STATE_DIR/scans/<repository>` 아래에 저장할 수 있습니다. 이러한 디렉터리에는
소스 코드 발췌문과 취약점 세부 정보가 포함될 수 있으므로
권한과 보존 설정을 적절히 관리하세요.

워크벤치는 스캔 기록을
`$CODEX_HOME/state/plugins/codex-security/workbench.sqlite3`에 저장합니다.
`CODEX_SECURITY_STATE_DIR` 환경 변수를 설정하면 워크벤치 데이터베이스도 이동합니다.

출력 디렉터리는 스캔 대상 디렉터리와 이를 포함하는
모든 Git 작업 트리 외부에 있어야 합니다. 스캔 시
`--archive-existing` 옵션을 사용하면 기존 결과 디렉터리를 대체할 수 있습니다.

출력 디렉터리를 재사용하기 전에 이전 결과를 보존하려면 다음과 같이 합니다:

```bash
npx @openai/codex-security scan . \
  --output-dir /path/outside/repository/results \
  --archive-existing

스캔은 기본적으로 보고서만 생성합니다. `--fail-on-severity` 옵션을 추가해
CI에서 심각도 정책을 평가하세요:

```bash
npx @openai/codex-security scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --json \
  --fail-on-severity high \
  > /path/outside/repository/codex-security.json

드라이런은 지식 베이스 문서를 비롯한 로컬 입력을 확인하지만
자격 증명을 로드하거나 Codex를 시작하거나 플러그인의 Python
인터프리터를 검사하지는 않습니다:

```bash
npx @openai/codex-security scan . \
  --output-dir /path/outside/repository/results \
  --dry-run

### 런타임 구성

모델, 인터프리터, 플러그인 또는
Codex 구성 값을 명시적으로 지정해야 할 때 런타임 옵션을 사용하세요.

| 인수                                                  | 설명                                                                                              |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `--auth {auto,chatgpt,api-key}`                           | 스캔 자격 증명을 선택합니다. 기본값은 `auto`입니다.                                                      |
| `--provider {openai,openrouter,fireworks,amazon-bedrock}` | 추론 제공업체를 선택합니다. 기본값은 `openai`입니다.                                                  |
| `--model MODEL`                                           | 모델을 선택합니다. 기본값은 `gpt-5.6-sol`입니다. OpenRouter, Fireworks, Amazon Bedrock에서는 반드시 지정해야 합니다.  |
| `--effort {minimal,low,medium,high,xhigh,max}`            | 모델의 추론 수준을 선택합니다. 기본값은 `xhigh`입니다.                                             |
| `--plugin-path PATH`                                      | Codex Security 플러그인 디렉터리 또는 ZIP 파일을 사용해 번들 플러그인을 대체합니다.                             |
| `--python PATH`                                           | 플러그인 런타임에 사용할 Python 인터프리터를 선택합니다.                                                    |
| `--codex KEY=VALUE`                                       | 격리된 Codex 구성 값을 재정의합니다. 값에는 TOML 구문을 사용합니다. 값을 여러 개 지정하려면 플래그를 반복해서 사용합니다. |

TOML을 작성하지 않고 다른 모델과 추론 수준을 선택하려면 다음과 같이 합니다:

```bash
npx @openai/codex-security scan . --model gpt-5.6-terra --effort high

`--codex` 옵션으로 전달하는 문자열 값은 TOML 파서가
문자열로 인식하도록 따옴표로 감싸세요:

```bash
npx @openai/codex-security scan . --codex 'model="gpt-5.6-terra"'

## `codex-security install-hook`

현재 레포지토리에 Git pre-commit 보안 검사를 설치합니다:

```bash
npx @openai/codex-security install-hook

이 검사는 커밋할 때마다 스테이징된 변경 사항과 스테이징되지 않은 변경 사항을 스캔하며,
심각도가 높은 보안 이슈나 스캔 오류가 있으면 커밋을 차단합니다. `core.hooksPath` 설정을 따르며
기존 pre-commit 스크립트를 대체하지 않습니다. 필요한 경우 심각도 임곗값을
다르게 설정하세요:

```bash
npx @openai/codex-security install-hook . --fail-on-severity medium

## `codex-security bulk-scan`

GitHub 레포지토리를 검색하여 스캔하거나 레포지토리 CSV를 사용해
재개 가능한 스캔을 실행하세요:

GitHub 레포지토리 검색, CSV 인벤토리, 캠페인 결과,
컨테이너 기반 스캔에 관한 전체 가이드는 [대량 보안 스캔
실행](/ko-KR/codex/security/cli/bulk-scans)을 참고하세요.

```text
usage: codex-security bulk-scan [input] [--output-dir DIR]
                                [--workers N] [--mode {standard,deep}]
                                [--provider {openai,openrouter,fireworks,amazon-bedrock}]
                                [--model MODEL]
                                [--effort {minimal,low,medium,high,xhigh,max}]
                                [--knowledge-base PATH]
                                [--scan-prompt-file FILE]
                                [--post-scan-prompt-file FILE]
                                [--max-attempts N] [--plugin-path PATH]
                                [--python PATH] [--codex KEY=VALUE]

`npx @openai/codex-security bulk-scan`을 인수 없이 실행하면 레포지토리를
대화형으로 선택할 수 있습니다. 이 플로우를 사용하려면 GitHub CLI에 로그인해야 합니다.

대화형 탐색 중에 모델과 추론 수준을 선택하려면:

```bash
npx @openai/codex-security bulk-scan --model gpt-5.6-terra --effort high

미리 준비한 레포지토리 목록을 사용하려면 CSV 파일과 `--output-dir` 옵션을 지정하세요:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

CSV에는 `id`, `repository`, `revision` 열이 필요합니다. 리비전은
전체 커밋 해시여야 합니다. 선택 사항인 `scope`, `mode`, `prompt` 열로
개별 레포지토리를 구성할 수 있습니다:

```csv
id,repository,revision,scope,mode,prompt
service,https://github.com/example/service.git,0123456789abcdef0123456789abcdef01234567,src,standard,Review authorization boundaries.

`--knowledge-base PATH` 옵션을 사용해 모든 레포지토리에서 보안 문서를
공유하세요. `--scan-prompt-file FILE` 옵션으로 공통 스캔 지침을 추가할 수 있으며,
CSV의 `prompt` 열은 해당 공통 프롬프트 뒤에 레포지토리별
지침을 추가합니다. `--post-scan-prompt-file FILE` 옵션은 커버리지가 불완전하거나 오류가 발생한
스캔을 포함해 각 스캔 후 후속 지침을 실행합니다. 스캔이 취소되거나
비용 한도에 도달하면 실행되지 않습니다.

`--workers` 옵션은 동시에 실행되는 레포지토리 스캔 수를 제한하며 기본값은 `4`입니다. `--mode`의
기본값은 `standard`이고 `--max-attempts`의 기본값은 `1`입니다. 레포지토리 또는 스캔 오류를 재시도하려면
`--max-attempts` 옵션을 설정하세요. 커버리지가 불완전한 상태로 완료된 스캔은
재시도하지 않습니다. 해당 결과는 계속 확인할 수 있으며,
명령어는 종료 코드 `2`를 반환합니다.

기존 출력 디렉터리에서 작업을 재개하려면 같은 명령어를 다시 실행하세요. CLI는
커버리지가 불완전한 스캔을 포함해 완료된 스캔을 건너뜁니다.

컨테이너 기반 캠페인은 [Docker에서 대량 스캔
실행](/ko-KR/codex/security/cli/bulk-scans#run-bulk-scans-in-docker)을 참고하세요.

## `codex-security scans`

### 저장된 스캔 찾기

현재 디렉터리에 해당하는 저장된 스캔을 나열합니다:

```bash
npx @openai/codex-security scans

다른 레포지토리의 스캔을 나열합니다:

```bash
npx @openai/codex-security scans list /path/to/repository

특정 출력 디렉터리에 저장된 스캔을 찾습니다:

```bash
npx @openai/codex-security scans list --scan-root /path/outside/repository/results

### 스캔 확인 또는 다시 실행

저장된 스캔의 결과와 구성을 표시합니다:

```bash
npx @openai/codex-security scans show SCAN_ID

`--show-linked-findings` 옵션을 추가하면 이전 스캔의 보안 이슈 링크도 포함됩니다.

원래 구성을 사용해 현재 체크아웃을 대상으로 스캔을 다시 실행합니다:

```bash
npx @openai/codex-security scans rerun SCAN_ID

재실행하려면 원래 스캔에 기록된 플러그인 버전이 필요합니다. 설치된
버전이 다르면 다른 플러그인으로 실행하지 않고 명령어가
중단됩니다.

### 저장된 스캔 로그 확인

스캔과 해당 워커에 대해 저장된 전체 세션 이벤트를 확인합니다. 이 로그는
민감한 정보가 가려지지 않아 소스 코드나 자격 증명이 포함될 수 있으므로
공유하기 전에 검토하세요:

```bash
npx @openai/codex-security scans logs SCAN_ID

`--json` 옵션을 추가하면 전체 정보가 포함된 결과를 기계가 읽을 수 있는 형식으로 출력합니다.

### 보안 이슈 매칭 및 비교

두 스캔을 비교해 새로 발견되었거나, 지속되거나, 다시 열렸거나, 해결되었거나, 상태를 알 수 없는
보안 이슈를 찾습니다:

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

비교 과정에서는 근본 원인이 같은 보안 이슈를 자동으로 매칭하고
저장된 매칭 결과를 재사용합니다. 매칭 결과를 명시적으로 저장하려면 `scans match` 명령어를 사용하세요:

```bash
npx @openai/codex-security scans match PREVIOUS_SCAN_ID CURRENT_SCAN_ID

후속 스캔의 커버리지가 불완전하거나 해당 보안 이슈의 원래 위치를
포함하지 않으면 이슈의 상태는 알 수 없음으로 분류됩니다. 기존 매칭 결과를 다시 계산하려면 `--force` 옵션을 `match` 명령어에
추가하세요.

다른 체크아웃에서 실행한 스캔까지 포함해 현재 레포지토리에서 완료된 모든
스캔을 매칭합니다:

```bash
npx @openai/codex-security scans match --all

같은 구성으로 다시 실행해도 스캔 결과는 달라질 수 있습니다. 매칭과
비교는 변경 사항을 추적할 뿐, 결과가 항상 동일하도록 만들거나
취약점이 더 이상 존재하지 않음을 입증하지는 않습니다. `validate` 명령어로 현재 코드에서
중요한 보안 이슈를 다시 확인하세요.

## `codex-security findings`

현재 레포지토리의 스캔 전반에서 열린 상태의 보안 이슈를 나열합니다:

```bash
npx @openai/codex-security findings list

다른 체크아웃을 확인하려면 레포지토리 경로를 전달하세요:

```bash
npx @openai/codex-security findings list /path/to/repository

구조화된 출력에는 `--json` 옵션을 추가하세요. 목록에는 최신 스캔에서 발견된
보안 이슈와 해당 스캔에서 확인되지 않은 이전 보안 이슈가 표시됩니다.

이전에 발견된 보안 이슈는 해결하거나 무시 처리할 때까지 열린 상태로 유지됩니다(최신
스캔에서 발견되지 않았다는 사실은 문제가 해결되었다는 증거가 아닙니다).

검토한 보안 이슈를 오탐으로 기록합니다:

```text
usage: codex-security findings false-positive OCCURRENCE_ID
                       --reason REASON

저장된 스캔을 확인해 해당 보안 이슈의 발생 기록을 식별합니다:

```bash
npx @openai/codex-security scans show SCAN_ID

오탐으로 판단한 구체적인 이유를 기록합니다:

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The framework escapes this input before it reaches the query"

이유를 비워 둘 수 없습니다. Codex Security는 해당 레포지토리에 대한 결정을 저장해
향후 스캔에 컨텍스트로 제공합니다. 각 스캔은 현재 소스, 보안 제어,
도달 가능성을 독립적으로 다시 확인합니다. 이전 결정으로 규칙, 경로 또는
취약점 유형이 검사 대상에서 제외되지는 않습니다.

## `codex-security export`

완료되어 봉인된 스캔에서 CSV, JSON 또는 SARIF를 내보냅니다. 내보내기 작업은
출력을 기록하기 전에 스캔 아티팩트를 검증하며, Codex 런타임과
자격 증명은 변경하지 않습니다.

```text
usage: codex-security export [--export-format {csv,json,sarif}]
                             [--output FILE|-] [--source-root PATH]
                             [--python PATH] scan_dir

`scan_dir`은 완료된 스캔의 디렉터리입니다.

| 인수                           | 설명                                                                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------- |
| `--export-format {csv,json,sarif}` | 내보내기 형식을 선택합니다. 기본값은 `sarif`입니다.                                           |
| `--output FILE\|-`                 | 선택한 형식을 파일이나 stdout에 기록합니다. 기본값은 현재 디렉터리의 파일입니다. |
| `--source-root PATH`               | 레포지토리 체크아웃을 사용해 SARIF에 소스 코드 줄의 지문을 추가합니다.                          |
| `--python PATH`                    | 번들 내보내기 도구에서 사용할 Python 인터프리터를 선택합니다.                                     |

`--source-root` 옵션은 `--export-format sarif` 옵션과 함께 사용할 때만 작동합니다. JSON은
봉인된 보안 이슈 문서를 보존합니다. CSV에는 이식 가능한 보안 이슈 열이 포함되며,
로컬 워크벤치의 트리아지 상태는 포함되지 않습니다.

`--output` 옵션을 지정하지 않으면 CLI는 현재 작업 디렉터리에서 SARIF를 `results.sarif`에, JSON을
`findings.json`에, CSV를 `findings.csv`에 기록합니다.
내보낸 결과에는 소스 코드 발췌문과 취약점 세부 정보가 포함될 수 있습니다. 명령어를
레포지토리 외부에서 실행하거나 `--output` 옵션에 스캔한 체크아웃
외부의 비공개 경로를 지정하세요.

SARIF를 파일에 기록합니다:

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format sarif \
  --source-root /path/to/repository \
  --output /path/outside/repository/exports/results.sarif

SARIF를 stdout에 기록합니다:

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format sarif \
  --source-root . \
  --output -

보안 이슈를 JSON으로 내보냅니다:

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format json \
  --output /path/outside/repository/exports/findings.json

보안 이슈를 CSV로 내보냅니다:

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format csv \
  --output /path/outside/repository/exports/findings.csv

## `codex-security publish scan`

완료된 스캔의 모든 보안 이슈를 Linear에 게시합니다:

```text
usage: codex-security publish scan [SCAN_DIR] --to linear
                                   [--linear-team TEAM_ID]
                                   [--project PROJECT_ID]
                                   [--linear-api-key KEY]
                                   [--linear-assignee EMAIL_OR_USER_ID]
                                   [--dry-run] [--json]

`SCAN_DIR`에는 완료되어 봉인된 스캔이 포함되어 있어야 합니다. 대화형
터미널에서 이 인수를 생략하면 로컬 스캔 기록에서 완료된 스캔을 선택할 수 있습니다. 이슈를 생성하려면
해당 스캔과 보안 이슈도 로컬 스캔 기록에 존재해야 합니다. 드라이
런은 이 저장 여부를 확인하지 않고 봉인된 아티팩트를 검증합니다.

| 인수                             | 설명                                                                                                                                                      |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--to linear`                        | Linear에 게시합니다. 필수 인수입니다.                                                                                                                    |
| `--linear-team TEAM_ID`              | Linear 팀을 선택합니다. 생략하면 `CODEX_SECURITY_LINEAR_TEAM`을 사용하며, 둘 중 하나는 반드시 지정해야 합니다.                                                                 |
| `--project PROJECT_ID`               | Linear 프로젝트를 선택합니다. 생략하면 `CODEX_SECURITY_LINEAR_PROJECT`를 사용합니다. 둘 다 설정하지 않으면 이슈가 팀에 직접 생성됩니다.                          |
| `--linear-api-key KEY`               | 직접 게시하려면 Linear 개인 API 키를 사용합니다. 생략하면 `CODEX_SECURITY_LINEAR_API_KEY`를 사용합니다.                                                         |
| `--linear-assignee EMAIL_OR_USER_ID` | 생성된 이슈의 담당자를 이메일 주소 또는 Linear 사용자 ID로 지정합니다. `--linear-api-key` 또는 `CODEX_SECURITY_LINEAR_API_KEY`가 필요합니다. 생략하면 이슈에 담당자가 지정되지 않습니다. |
| `--dry-run`                          | Codex를 시작하거나 Linear와 통신하거나 이슈를 생성하거나 게시 상태를 기록하지 않고 이슈 페이로드를 준비합니다.                                                 |
| `--json`                             | 구조화된 게시 결과를 stdout에 기록합니다. 진행 상황은 stderr에 계속 출력됩니다.                                                                                      |

  Linear 이슈 설명과 드라이 런 출력에는 소스 코드 스니펫과
취약점 세부 정보가 포함될 수 있습니다. 권한이 있는 Linear 팀 또는
프로젝트에만 게시하고, 저장된 출력은 민감한 정보로 취급하세요.

드라이 런이 아닌 실행은 매번 보안 이슈마다 새 이슈를 생성하려고 시도합니다.
동일한 스캔을 다시 게시해도 기존 이슈를 매칭하거나, 업데이트하거나, 재사용하지 않습니다.
일부 보안 이슈의 게시에 실패하면 이미 생성된 이슈는 그대로 유지되며,
명령어는 종료 코드 `2`를 반환합니다.
`--json` 옵션을 사용한 경우 중복을 방지하려면 재시도하기 전에 `created` 및 `failed` 결과를
검토하세요.

게시하기 전에 이슈 페이로드를 미리 확인하세요:

```bash
npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --dry-run \
  --json

### 연결된 Linear 앱으로 게시

Linear API 키가 없으면 이 명령어는 기존 구성과 연결된 Linear 앱을 사용해 Codex를 시작합니다. 게시하기 전에 로그인하고 Linear를 Codex 계정에 연결하세요:

```bash
npx @openai/codex-security login
npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --project PROJECT_ID

### Linear API 키로 게시

`--linear-api-key` 또는 `CODEX_SECURITY_LINEAR_API_KEY`를 지정하면 Linear API를 통해
직접 게시하며 Codex를 시작하지 않습니다. 직접 게시할 때 담당자를 선택하지
않으면 이슈가 미할당 상태로 유지됩니다:

```bash

npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --linear-assignee teammate@example.com

명령줄 값은 해당 환경 변수보다 우선합니다. API
키는 `CODEX_SECURITY_LINEAR_API_KEY`를 `--linear-api-key`보다 우선 사용하세요.
명령줄 인수가 셸 기록과 프로세스 목록에 표시될 수 있기 때문입니다.

## `codex-security validate` 및 `codex-security patch`

보안 이슈 후보의 유효성을 확인하세요:

```bash
npx @openai/codex-security validate findings.json \
  "Possible SQL injection in src/query.ts:42"

기본 제공되는 해결 스킬로 수정안을 생성하세요:

```bash
npx @openai/codex-security patch findings.json \
  "Missing authorization check in src/routes.ts:18"

각 위치 인수에는 리터럴 텍스트 또는 파일 경로를 지정할 수 있습니다. 입력은
현재 디렉터리를 기준으로 합니다. `validate`를 사용해 수정한 보안 이슈나
이후 스캔에서 더 이상 보고되지 않는 보안 이슈를 다시 확인하세요. 스캔 결과를
비교하는 것만으로는 수정이 성공했음을 입증할 수 없습니다.

두 명령어 모두 `--effort`로 추론 수준을 선택하세요:

```bash
npx @openai/codex-security validate "Possible SQL injection" --effort high

### 스캔 후 보안 이슈 패치

`scan --patch`를 사용해 스캔이 완료된 후 보안 이슈를 수정하세요. 이를 위해서는
`@openai/codex-security` 0.1.15 이상이 필요합니다. 기본 심각도 임계값은
`low`입니다. 이 명령어는 심각도가 높거나 치명적인 보안 이슈를 선택합니다:

```bash
npx @openai/codex-security scan . --patch --patch-severity high --json

검증되었거나 이미 수정된 보안 이슈는 `--fail-on-severity`를 트리거하지 않습니다.

### 저장된 보안 이슈 패치

보안 이슈 ID 또는 발생 ID를 지정해 원래 레포지토리를 패치하거나, 저장된 스캔에서 보안 이슈를 선택하세요:

```bash
npx @openai/codex-security patch OCCURRENCE_ID
npx @openai/codex-security patch --scan SCAN_ID --severity high --json
npx @openai/codex-security patch --scan latest --severity medium

`--scan latest`는 현재 레포지토리에서 가장 최근에 완료된 스캔을 선택합니다.
저장된 보안 이슈 관련 명령어는 `--json`을 지원하지만, 리터럴 텍스트나 파일 입력에서는 이 옵션을 사용할 수 없습니다.

`--create-pr`을 추가해 검증된 패치 파일만 커밋하고 GitHub CLI로
Pull Request를 생성하세요:

```bash
npx @openai/codex-security patch --scan SCAN_ID --severity high --create-pr

푸시 또는 Pull Request 생성이 실패하면 출력된 `patch --resume-pr BRANCH`
명령어를 같은 레포지토리에서 실행해 다시 시도하세요.

### Linear 이슈 패치

개인 API 키를 사용하려면 `CODEX_SECURITY_LINEAR_API_KEY` 또는 `LINEAR_API_KEY`를 설정하고,
OAuth 토큰을 사용하려면 `LINEAR_ACCESS_TOKEN`을 설정하세요. 키가 셸 기록에 남지 않도록
`--linear-api-key KEY` 대신 환경 변수를 사용하세요.

ID 또는 URL로 이슈를 가져오세요. 여러 이슈를 선택하려면 `--linear-issue`를
반복해서 지정하세요:

```bash
npx @openai/codex-security patch --linear-issue SEC-123 --linear-issue SEC-124

`--linear-project`를 사용해 프로젝트의 미해결 이슈를 선택하세요. `--linear-filter`를
추가하면 선택 범위를 좁힐 수 있습니다:

```bash
npx @openai/codex-security patch --linear-project "Security backlog" \
  --linear-filter '{"labels":{"name":{"eq":"security"}}}'

필터에서 `state`를 설정하지 않는 한 CLI는 완료되었거나 취소된 이슈를 제외합니다.
Linear 이슈는 변경하지 않습니다.

## `codex-security login`, `logout` 및 `info`

대화형으로 로그인하세요:

```bash
npx @openai/codex-security login

원격 또는 헤드리스 머신에서 기기 인증을 사용하세요:

```bash
npx @openai/codex-security login --device-auth

현재 로그인 상태를 확인하세요:

```bash
npx @openai/codex-security login status

저장된 로그인 정보를 삭제하세요:

```bash
npx @openai/codex-security logout

API 키를 stdin으로 전달해 저장하세요:

```bash
printenv OPENAI_API_KEY | npx @openai/codex-security login --with-api-key

엔터프라이즈 액세스 토큰을 저장하세요:

```bash
printenv CODEX_ACCESS_TOKEN | npx @openai/codex-security login --with-access-token

SDK와 기본 제공 플러그인의 읽기 전용 메타데이터를 확인하세요:

```bash
npx @openai/codex-security info --json

CLI를 MCP 서버로 노출하면 `info` 명령어만 사용할 수 있습니다.
스캔, 내보내기, 게시, 로그인, 검증 및 패치는 CLI에서만 사용할 수 있습니다.

## 스캔 출력 확인

기본적으로 스캔은 전체 스캔 결과를 stdout에 기록하지 않고 진행 상황, 완료 요약 및 오류를
stderr에 출력합니다. 구조화된 스캔 결과를 stdout에 출력하려면 `--json`,
`--format` 또는 `--full-output`을 지정하세요.

대화형 터미널에서는 현재 스캔 단계, 검토한 파일, 활동, 토큰 사용량 및 예상 비용을
실시간 대시보드에 표시합니다. CI와 리디렉션된 출력에서는 진행 상황을 일반 텍스트로
표시합니다. `--headless`를 추가하면 대화형 터미널에서도 진행 상황을
일반 텍스트로 표시할 수 있습니다:

```bash
npx @openai/codex-security scan . --headless

대시보드에는 실시간 세션 세부 정보도 표시됩니다. 이 정보는 민감한 내용이 가려지지 않으며 소스 코드나 자격 증명이 포함될 수 있습니다. 공유하기 전에 검토하세요.

### 상세 진단 정보

`--verbose`를 추가해 민감한 정보를 가린 수명 주기, 인증, 진행 상황 및 비용
진단 정보를 stderr에 출력하세요:

```bash
npx @openai/codex-security scan . --verbose

`CODEX_SECURITY_LOG_LEVEL=debug`를 설정하면 플래그 없이도 동일한 진단 정보를
활성화할 수 있습니다. `LOG_LEVEL=debug`도
`CODEX_SECURITY_LOG_LEVEL`이 설정되어 있지 않으면 진단 정보를 활성화합니다.

### 완료 요약

스캔이 완료되면 레포지토리의 미해결 보안 이슈 수, 심각도별 분류, 커버리지, 경과 시간, 보고서 경로, 결과 디렉터리를 stderr에 기록합니다. 확인할 수 있는 경우 토큰 사용량과 예상 비용도 포함합니다:

```text
  REPORT    /path/to/scan/report.md

  FINDINGS  4 (3 confirmed this scan; 1 previously found; 1 critical, 2 high, 1 informational)
  COVERAGE  complete
  ELAPSED   1s
  TOKENS    1,250 input, 200 cached, 30 output
  RESULTS   /path/to/scan

정보성 보안 이슈도 요약의 전체 건수에 포함됩니다. 심각도 정책은
현재 스캔에서 발견된 `critical`, `high`, `medium`, `low` 수준의
보안 이슈만 평가하며, 레포지토리 전체 건수에 포함된 이전 보안 이슈는 평가하지 않습니다.

### JSON 출력

`scan --json`은 완전한 JSON 문서 하나를 stdout에 출력합니다. 최상위 구조는
다음과 같습니다:

```text
manifest
repositoryFindings
findings
coverage
scanDir
threadId
reportPath
artifactsDir
sarifPath
cost
turn
  id
  status
  durationMs
  finalResponse
  usage

[패치](#patch-findings-after-a-scan)를 수행하면 JSON 출력에 패치
결과가 포함되며, Pull Request가 생성된 경우 해당 정보도 포함됩니다.

진행 상황, 완료 요약, 아카이브 알림 및 오류는 계속 stderr에 출력됩니다.
완료된 스캔은 심각도 정책에 따라
종료 코드 `1`이 반환되거나 커버리지 불완전으로 종료 코드 `2`가 반환되더라도 전체 JSON 결과를 출력합니다.

  `codex-security scan --json`은 JSON 문서 하나를 출력합니다. `codex exec --json`은
  JSON Lines 이벤트 스트림을 출력합니다. 실행하는
  명령어에 맞는 출력 형식을 사용하세요.

## 스캔 아티팩트

완료된 스캔은 사람이 읽을 수 있는 보고서와 구조화된 아티팩트를 함께 보관합니다:

```text
<scan-directory>/
├── scan-manifest.json
├── findings.json
├── coverage.json
├── report.md
├── artifacts/
└── exports/
    └── results.sarif       # when produced

구조화된 파일은 각각 용도가 다릅니다:

| 파일                    | 내용                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `scan-manifest.json`    | 스캔 식별 정보, 상태, 대상, 범위, 생성 주체 및 봉인된 아티팩트 기록.                                                    |
| `findings.json`         | 보안 이슈 식별자, 심각도, 신뢰도, 분류 체계, 위치, 증거, 검증, 데이터 흐름, 도달 가능성 및 해결 방안. |
| `coverage.json`         | 검토한 영역, 제외 항목, 보류된 작업, 미해결 질문 및 커버리지 완전성.                                        |
| `report.md`             | 사람이 읽을 수 있는 스캔 보고서.                                                                                                           |
| `artifacts/`            | 보조 스캔 아티팩트.                                                                                                      |
| `exports/results.sarif` | 스캔 중 생성된 SARIF(있는 경우).                                                                                  |

커버리지 완전성 값은 다음 세 가지입니다:

- `complete`: 스캔에서 선택한 범위의 커버리지를 완전한 것으로 기록합니다.
- `partial`: 스캔에서 보류된 작업이나 기타 커버리지 제한 사항을 기록합니다.
- `unknown`: 스캔에서 커버리지 완전성을 알 수 없는 것으로 보고합니다.

커버리지를 보안 판단의 근거로 사용하기 전에 검토가 보류된 영역, 명시적으로 제외된 항목 및 미해결 질문을 검토하세요.

## 종료 코드와 시그널

CLI는 다음 종료 코드를 사용합니다:

| 종료 코드  | 조건                                                                                                                                                                     |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0`   | 스캔이 전체 범위의 검사를 완료하고 심각도 정책을 통과했거나, 일괄 스캔 또는 게시가 실패 없이 완료되었거나, 다른 명령어가 성공했습니다.                  |
| `1`   | 완료된 스캔에서 설정된 심각도 이상의 보안 이슈가 보고되었습니다.                                                                                                       |
| `2`   | CLI에서 입력, 런타임 또는 내보내기 오류가 발생했거나, 스캔 커버리지가 불완전하거나, 일괄 스캔 중 오류가 발생한 레포지토리가 있거나, 게시하지 못한 보안 이슈가 하나 이상 있습니다. |
| `130` | Ctrl-C로 스캔 또는 게시가 중단되었습니다.                                                                                                                                     |
| `143` | SIGTERM으로 스캔 또는 게시가 종료되었습니다.                                                                                                                                     |

커버리지가 `partial` 또는 `unknown`인 스캔은 심각도 정책이 없어도 `2`을
반환합니다. 구조화된 출력을 요청하면 완료된 스캔과
부분적으로 완료된 게시에서도 사용 가능한 결과를 stdout에 출력합니다. CLI는
작업이 중단되거나 런타임 오류가 발생하면 부분 출력의
위치를 표시합니다.

## 로컬 스캔 권한

CLI 및 SDK 스캔은 사용자의 로컬 운영체제 권한으로 실행됩니다. 모든 스캔은
`codex_security_scan` 파일 시스템 프로필을 사용하고 `approvalPolicy`를
`"never"`로 설정합니다. 이 프로필은 로컬 파일 시스템을 읽고
워크스페이스 루트 및 선택한 스캔 상태 디렉터리에 쓰는 작업을 허용합니다. 스캔은
대화형 승인을 요청하기 위해 중단되지 않습니다.

CLI의 `--codex` 또는 SDK의 `codexOverrides`로 지정하는
`approval_policy`, `sandbox_mode`, 파일 시스템 권한 등의 설정으로는 이러한 스캔 제어를
대체하거나 제한할 수 없습니다. 호스트와 네트워크 제한은 계속 적용됩니다.

스캔 및 워크벤치 프로세스는 관련 없는 API 토큰과 클라우드 자격 증명을 포함한
사용자의 환경을 상속할 수 있습니다. 신뢰할 수 있으며 검사할 권한이 있는 레포지토리만
스캔하고, 스캔에 필요한 자격 증명만 제공하세요.

## 인증 및 사전 요구 사항

`OPENAI_API_KEY` 또는 `CODEX_API_KEY`를 설정하거나,
`npx @openai/codex-security login`으로 로그인하거나, 기존 파일 기반 Codex
로그인 정보를 사용하세요. OpenRouter 또는 Fireworks를 사용하는 경우 해당 제공업체의 API 키를 설정하고
모델을 선택하세요. Amazon Bedrock에서는 Bedrock API 키나 표준 AWS
자격 증명 체인을 대신 사용하세요.

자격 증명 선택 방법은 [스캔
인증 선택](#select-scan-authentication)을 참조하세요.

CI에서는 API 키의 범위를 스캔 단계로 제한하고 신뢰할 수 있는 워크플로우를 사용하세요.

CLI를 사용하려면 Node.js 22(22.13.0 이상), 24 또는 26이 필요합니다. 스캔, 일괄 스캔,
내보내기, 스캔 기록 및 저장된 보안 이슈에도 Python 3.10 이상이 필요합니다.
Python 3.10에는 `tomli`도 필요합니다. `--python`을 `scan`, `bulk-scan` 또는
`export`와 함께 사용하거나, Python 기반 명령어에는 `PYTHON`을 설정하세요.

다음으로 [CLI 빠른 시작](/ko-KR/codex/security/cli), [일괄 스캔
가이드](/ko-KR/codex/security/cli/bulk-scans), [CLI 자주 묻는 질문](/ko-KR/codex/security/cli/faq), [CI
가이드](/ko-KR/codex/security/cli/ci) 또는 [TypeScript SDK 가이드](/ko-KR/codex/security/sdk)를 확인하세요.

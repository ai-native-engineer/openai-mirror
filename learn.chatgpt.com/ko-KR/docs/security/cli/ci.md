<!-- source: https://learn.chatgpt.com/ko-KR/docs/security/cli/ci -->

CI에서 Codex Security CLI를 실행하면 Pull Request 또는 병합 요청의 정확한 변경 사항을 검토하고 보안 이슈와 커버리지를 보존하며, 원하는 경우 선택한 심각도에 따라 검사를 실패 처리할 수 있습니다. 먼저 참고용 결과로 시작해 스캔 품질과 실행 시간을 검토한 다음 레포지토리에 적합한 심각도 정책을 추가하세요.

  공개된 `@openai/codex-security` 패키지를 설치하세요. 스캔을 실행하려면
  여전히 Codex Security 접근 권한이 필요합니다.

이 가이드에서는 GitHub Actions와 GitLab CI/CD 예제를 제공합니다. 동일한 스캔 및 내보내기 명령어를 다른 CI 시스템에서도 사용할 수 있습니다.

## 워크플로우 준비

OpenAI API 키를 CI 제공업체의 시크릿 저장소에
`CODEX_SECURITY_API_KEY`라는 이름으로 저장하세요.

이 시크릿을 스캔 단계의 `OPENAI_API_KEY` 환경 변수에 직접 매핑하세요.
자격 증명의 사용 범위를 스캔 프로세스로 제한하고
`--auth api-key` 옵션으로 명시적으로 선택하세요.

신뢰할 수 있는 레포지토리와 Pull Request에 대해서만 워크플로우를 실행하세요. 스캔은 러너의 로컬 권한을 사용하며 승인을 기다리며 일시 중지되지 않습니다. 스캔 프로세스가 작업 환경을 상속할 수 있으므로 관련 없는 토큰과 클라우드 자격 증명이 작업 환경에 포함되지 않도록 하세요.

러너에는 다음 항목이 필요합니다:

- Node.js 22(22.13.0 이상), 24 또는 26.
- Python 3.10 이상.
- 배포된 `@openai/codex-security` 패키지. 레포지토리 체크아웃 디렉터리 외부에
  설치되어 있어야 합니다.
- Git이 병합 베이스를 계산하는 데 필요한 Pull Request 또는 병합 요청의 헤드 및 베이스 이력.

## GitHub Actions 워크플로우 추가

비공개 또는 내부 레포지토리에서는 SARIF를 업로드하기 전에
[GitHub Code Security](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github)를
활성화하세요.

`.github/workflows/codex-security.yml` 파일을 만드세요. Pull Request를 체크아웃하기 전에
`@openai/codex-security` 패키지를
`$RUNNER_TEMP/codex-security` 아래에 설치해 신뢰할 수 있는 실행 파일을
`$RUNNER_TEMP/codex-security/node_modules/.bin/codex-security` 경로에서 사용할 수 있도록 하세요:

```yaml
name: Codex Security scan

on:
  pull_request:

jobs:
  codex-security:
    if: github.event.pull_request.head.repo.full_name == github.repository && github.actor != 'dependabot[bot]'
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write
    steps:
      - name: Set up Node.js
        uses: actions/setup-node@820762786026740c76f36085b0efc47a31fe5020 # v7
        with:
          node-version: "26"

      - name: Set up Python
        uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97 # v7
        with:
          python-version: "3.14"

      - name: Install Codex Security
        run: |
          set -euo pipefail
          npm install \
            --prefix "$RUNNER_TEMP/codex-security" \
            --ignore-scripts \
            --no-audit \
            --no-fund \
            @openai/codex-security

      - name: Verify Codex Security
        env:
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
        run: |
          set -euo pipefail
          test -x "$CODEX_SECURITY_BIN"
          "$CODEX_SECURITY_BIN" --version

      - name: Check out the pull request
        uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0
          persist-credentials: false

      - name: Scan the pull request
        env:
          OPENAI_API_KEY: ${{ secrets.CODEX_SECURITY_API_KEY }}
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
          CODEX_SECURITY_STATE_DIR: ${{ runner.temp }}/codex-security-state
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
          HEAD_SHA: ${{ github.event.pull_request.head.sha }}
          SCAN_DIR: ${{ runner.temp }}/codex-security-results
        run: |
          set -euo pipefail
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_SHA")"
          "$CODEX_SECURITY_BIN" scan . \
            --diff "$BASE_REVISION" \
            --head "$HEAD_SHA" \
            --auth api-key \
            --output-dir "$SCAN_DIR" \
            --json > "$RUNNER_TEMP/codex-security.json"

      - name: Export SARIF
        id: export-sarif
        if: always()
        env:
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
          SCAN_DIR: ${{ runner.temp }}/codex-security-results
          SARIF_FILE: ${{ runner.temp }}/codex-security.sarif
        run: |
          set -euo pipefail
          if test -f "$SCAN_DIR/scan-manifest.json"; then
            "$CODEX_SECURITY_BIN" export "$SCAN_DIR" \
              --export-format sarif \
              --source-root "$GITHUB_WORKSPACE" \
              --output "$SARIF_FILE"
            echo "available=true" >> "$GITHUB_OUTPUT"
          fi

      - name: Upload SARIF
        if: always() && steps.export-sarif.outputs.available == 'true'
        uses: github/codeql-action/upload-sarif@e4fba868fa4b1b91e1fdab776edc8cfbe6e9fb81 # v4
        with:
          sarif_file: ${{ runner.temp }}/codex-security.sarif
          ref: refs/pull/${{ github.event.pull_request.number }}/head
          sha: ${{ github.event.pull_request.head.sha }}
          category: codex-security

      - name: Preserve scan results
        if: always()
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7
        with:
          name: codex-security-results
          path: |
            ${{ runner.temp }}/codex-security-results
            ${{ runner.temp }}/codex-security.json
          if-no-files-found: warn
          retention-days: 7

워크플로우는 Pull Request 헤드를 체크아웃하고 병합 베이스를 계산한 다음
두 리비전 사이에 커밋된 변경 사항을 스캔합니다. 전체 이력을 사용하면
스캔 대상을 정확하게 지정할 수 있습니다. `persist-credentials: false` 설정은 체크아웃된
Git 구성에 레포지토리 토큰이 저장되지 않도록 합니다. 체크아웃 전에 CLI를 설치하고
절대 경로로 실행하면 레포지토리에서 제어하는 실행 파일에
스캔 자격 증명이 노출되지 않도록 할 수 있습니다. `--auth api-key` 옵션은 범위가 제한된 API 키를 명시적으로 선택합니다.
스캔 이력은 레포지토리 외부의 쓰기 가능한
상태 디렉터리에 저장됩니다.

`--json` 옵션은 완전한 JSON 문서 하나를 stdout에 기록하므로 워크플로우에서
직접 저장할 수 있습니다. 진행 상황, 완료 요약, 오류는 stderr에 기록됩니다.
이는 JSON Lines 이벤트 스트림을 출력하는 `codex exec --json`와 다릅니다.

내보내기 단계에서는 완료 후 봉인된 스캔을 읽고 SARIF를 작성합니다. Codex 런타임과 자격 증명은 변경하지 않습니다. 스캔 아티팩트에는 취약한 소스 코드 조각, 증거, 수정 세부 정보가 포함될 수 있습니다. 레포지토리에 적합한 접근 제어와 짧은 보존 기간을 선택하세요.

## GitLab CI/CD 파이프라인 추가

보호된 기본 브랜치 스캔, 선택적으로 활성화하는 예약 심층 스캔,
별도의 SARIF 정책 기반 통과 여부 판정, 선택 사항인 검증된 초안 병합 요청을 갖춘
프로덕션 워크플로우가 필요하면 [GitLab CI/CD에서
Codex Security 실행](/ko-KR/codex/security/cli/ci/gitlab)을 참조하세요.

GitLab Ultimate 19.2 이상에서는
[SARIF 2.1.0 보고서](https://docs.gitlab.com/ci/yaml/artifacts_reports/#artifactsreportssarif)를 수집할 수 있습니다.
파이프라인을 실행하기 전에 마스킹 및 숨김 처리된
`CODEX_SECURITY_API_KEY` CI/CD 변수를 추가하세요.

다음 최소 예제는 스캔만 수행하는 `security` 작업을 루트
`.gitlab-ci.yml`에 추가합니다. 파일의 기존 단계와 작업은 모두 유지하세요.
기본적으로 병합 요청의 변경 사항을 스캔합니다. 기본 브랜치 전체도 스캔하려면
`CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` 값을 `"true"`로 설정하세요:

```yaml
variables:
  CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH: "false"

stages:
  - test
  - security

codex-security:
  stage: security
  image: node:26-bookworm-slim
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID'
      variables:
        CODEX_SECURITY_SCAN_SCOPE: "diff"
    - if: '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH && $CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH == "true"'
      variables:
        CODEX_SECURITY_SCAN_SCOPE: "full"
  variables:
    GIT_DEPTH: "0"
    CODEX_SECURITY_CLI_DIR: "/tmp/codex-security-cli"
  before_script:
    - |
      set -eu
      apt-get update -qq
      apt-get install -y -qq --no-install-recommends \
        ca-certificates \
        git \
        python3 \
        ripgrep
      npm install \
        --prefix "$CODEX_SECURITY_CLI_DIR" \
        --ignore-scripts \
        --no-audit \
        --no-fund \
        @openai/codex-security@0.1.20

      test -x "$CODEX_SECURITY_BIN"
      "$CODEX_SECURITY_BIN" --version
  script:
    - |
      set -eu
      if test -z "${CODEX_SECURITY_API_KEY:-}"; then
        echo "Set the CODEX_SECURITY_API_KEY CI/CD variable." >&2
        exit 2
      fi

      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY

      case "${CODEX_SECURITY_SCAN_SCOPE:-}" in
        diff)
          BASE_SHA="$CI_MERGE_REQUEST_DIFF_BASE_SHA"
          HEAD_SHA="$CI_COMMIT_SHA"
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_SHA")"
          set -- --diff "$BASE_REVISION" --head "$HEAD_SHA"
          echo "Scanning committed changes from $BASE_REVISION to $HEAD_SHA."
          ;;
        full)
          set -- --mode standard
          echo "Scanning the complete default branch at $CI_COMMIT_SHA."
          ;;
        *)
          echo "Unsupported Codex Security scan scope: ${CODEX_SECURITY_SCAN_SCOPE:-unset}" >&2
          exit 2
          ;;
      esac

      SCAN_DIR="/tmp/codex-security-results-$CI_JOB_ID"
      JSON_FILE="/tmp/codex-security-$CI_JOB_ID.json"
      SARIF_FILE="/tmp/codex-security-$CI_JOB_ID.sarif"

      install -d -m 700 "$CODEX_SECURITY_STATE_DIR" "$SCAN_DIR"

      set +e
      OPENAI_API_KEY="$codex_security_api_key" \
        "$CODEX_SECURITY_BIN" scan . \
          "$@" \
          --auth api-key \
          --output-dir "$SCAN_DIR" \
          --json > "$JSON_FILE"
      scan_exit="$?"
      set -e
      unset codex_security_api_key

      install -d -m 700 codex-security-artifacts/results
      cp -R "$SCAN_DIR"/. codex-security-artifacts/results/
      if test -s "$JSON_FILE"; then
        cp "$JSON_FILE" codex-security-artifacts/codex-security.json
      fi
      printf '%s\n' "$scan_exit" > codex-security-artifacts/scan-exit-code.txt

      export_exit=0
      if test -f "$SCAN_DIR/scan-manifest.json"; then
        set +e
        "$CODEX_SECURITY_BIN" export "$SCAN_DIR" \
          --export-format sarif \
          --source-root "$CI_PROJECT_DIR" \
          --output "$SARIF_FILE"
        export_exit="$?"
        set -e
        if test -s "$SARIF_FILE"; then
          cp "$SARIF_FILE" codex-security-artifacts/codex-security.sarif
        fi
      fi

      if test "$scan_exit" -ne 0; then
        exit "$scan_exit"
      fi
      exit "$export_exit"
  artifacts:
    when: always
    access: maintainer
    expire_in: 7 days
    paths:
      - codex-security-artifacts/
    reports:
      sarif: codex-security-artifacts/codex-security.sarif

기본적으로 이 작업은 같은 프로젝트의 브랜치에서 생성된 병합 요청에만
실행되므로 포크 파이프라인에는 스캔 자격 증명이 전달되지 않습니다.
그룹, 프로젝트 또는 파이프라인 수준에서 `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` 값을 `"true"`로
설정하면 기본 브랜치에서도 표준 전체 스캔을 실행할 수 있습니다.
전체 스캔은 diff 스캔보다 오래 걸리고 비용도 더 많이 듭니다.

`GIT_DEPTH: "0"` 설정은 병합 요청 스캔 시
`CI_MERGE_REQUEST_DIFF_BASE_SHA`와 `CI_COMMIT_SHA`를 기준으로 병합 베이스를 계산하는 데 필요한 이력을 제공합니다.

작업은 CLI를 `/tmp` 아래에 설치하고 절대 경로로 실행하며
API 키를 스캔 프로세스에만 노출합니다. `artifacts: when: always` 설정은 스캔이 실패해도
SARIF 보고서를 보존하며, `artifacts:access: maintainer` 설정은
상세 스캔 결과에 대한 접근을 제한합니다.

`.gitlab-ci.yml`의 변경으로 CI/CD 변수가 노출될 수 있으므로 작업을 실행하기 전에
파이프라인 변경 사항을 검토하세요.
[`CODEX_SECURITY_API_KEY`를 보호](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#control-access-to-protected-variables-and-runners)하면
GitLab은 같은 프로젝트의 보호된 브랜치 간 병합 요청이면서
사용자가 대상 브랜치에 접근할 수 있는 경우에만 해당 변수를 제공합니다.

이 섹션 시작 부분에 링크된 GitLab 전용 가이드에서는 이 최소 작업을 프로덕션 워크플로우로 확장하는 방법을 설명합니다.

## 심각도 정책 선택

두 예제 모두 `--fail-on-severity` 옵션을 생략하므로 보고 전용으로 실행됩니다.
보안 이슈를 검사 통과 여부에 반영할 준비가 되면
스캔 명령어에 임곗값을 추가하세요:

```bash
"$CODEX_SECURITY_BIN" scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --fail-on-severity high

지원되는 임곗값은 `critical`, `high`, `medium`, `low`입니다.
임곗값은 현재 스캔에서 발견된 해당 심각도 이상의 보안 이슈에 적용됩니다.
이전에 발견되어 레포지토리 요약에 표시되는 미해결 보안 이슈는 정책에 영향을 주지 않습니다.

스캔 단계에서는 다음 종료 코드를 사용합니다:

| 종료 코드  | 의미                                                                                 |
| ----- | --------------------------------------------------------------------------------------- |
| `0`   | 커버리지가 완전한 상태로 스캔이 완료되었으며, 설정된 정책이 있다면 해당 정책도 모두 통과했습니다.            |
| `1`   | 완료된 스캔에 임곗값 이상의 심각도를 가진 보안 이슈가 포함되어 있습니다.                        |
| `2`   | CLI에서 입력 오류 또는 런타임 오류를 감지했거나 완료된 스캔의 커버리지가 불완전합니다. |
| `130` | Ctrl-C로 스캔이 중단되었습니다.                                                            |
| `143` | SIGTERM으로 스캔이 종료되었습니다.                                                            |

커버리지가 `partial` 또는 `unknown`인 스캔은 심각도 정책이 없어도 `2`를 반환합니다.
이 경우에도 CLI는 확인 가능한 보안 이슈와 커버리지를 기록합니다.
검사 결과를 확정적으로 받아들이기 전에 `coverage.json`에서 스캔이 보류된 영역을 검토하세요.

## 기존 결과 디렉터리가 있을 때 다시 시도

각 CI 작업에는 새 러너 디렉터리를 사용하세요. 영구 러너 또는 자체 호스팅
러너에서는 `--archive-existing` 옵션으로 이전 결과를 보존하세요:

```bash
"$CODEX_SECURITY_BIN" scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --archive-existing

이 명령어는 이전 결과를 별도로 보관하고 빈 스캔 디렉터리에서 시작합니다.

## CI 스캔 문제 해결

- **알 수 없는 Git 참조 또는 예상치 못한 diff:** 베이스와 헤드 이력을 가져와
  병합 베이스를 계산하고 두 리비전을 모두 명시적으로 전달하세요.
- **보호되었거나 비어 있지 않은 출력 디렉터리:** 해당 경로를 포함하는 Git 작업 트리
  외부의 비공개 디렉터리를 선택하세요. 디렉터리에 이미 결과가 있으면
  `--archive-existing` 옵션을 사용하세요.
- **자격 증명 누락:** 신뢰할 수 있는 워크플로우 또는 파이프라인에서
  `CODEX_SECURITY_API_KEY`를 사용할 수 있고, 스캔 프로세스의
`OPENAI_API_KEY` 환경 변수에 직접 매핑되어 있는지 확인하세요.
- **스캔 이력 오류:** `CODEX_SECURITY_STATE_DIR`에 레포지토리 외부의
  쓰기 가능한 디렉터리를 지정하세요.
- **Python 설정 오류:** 러너에서 Python 3.10 이상을 사용하는지 확인하세요.
- **불완전한 커버리지:** 보류된 영역과 미해결 질문을 포함한 `coverage.json` 내용을
  검토한 다음 적절한 대상 또는 환경으로 다시 실행하세요.
- **SARIF 내보내기 오류:** 스캔이 완료되었고 전체 스캔
  디렉터리를 사용할 수 있는지 확인하세요. 내보내기 과정에서는
  SARIF를 작성하기 전에 봉인된 아티팩트를 검증합니다.
- **SARIF 업로드 오류:** GitHub Actions에서는 조직에서 해당 레포지토리에 대해
  GitHub Code Security를 활성화했으며, 워크플로우가
`actions: read`, `contents: read`, `security-events: write` 권한을 부여하는지 확인하세요.
  GitLab CI/CD에서는 프로젝트가 GitLab Ultimate 19.2 이상을 사용하며
  작업이 `artifacts:reports:sarif`를 통해 SARIF 2.1.0 파일을 업로드하는지 확인하세요.

모든 명령어, 플래그, 아티팩트, 출력 필드에 관한 내용은 [CLI
참조 자료](/ko-KR/codex/security/cli/reference)를 확인하세요. 대화형 플러그인 기반 CI
검토에 관한 내용은 [코드 변경 사항의 보안 검토](/ko-KR/codex/security/plugin/code-changes#automate-reviews-in-cicd)를 참조하세요.

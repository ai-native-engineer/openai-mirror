<!-- source: https://learn.chatgpt.com/ko-KR/docs/security/plugin/code-changes -->

Git으로 관리되는 하나의 변경 세트에서 보안 회귀를 찾으려면 보안 변경 검토를 실행하세요.
Codex는 변경된 소스 계열 파일 각각과 이를 직접 지원하는 코드를 검토합니다.
검토 범위를 레포지토리 전체 감사로 확대하지는 않습니다.

특정 변경 사항 대신 레포지토리 전체를 스캔하려면 [보안
스캔 실행](/ko-KR/codex/security/plugin/scans)을 참조하세요.

## 수동 검토 실행

데스크톱 앱에서 **보안을** 열고 **스캔을** 선택한 다음 **+ 스캔을** 선택하세요.
레포지토리를 선택한 다음 **변경 사항을** 선택하세요. 커밋되지 않은 변경 사항,
단일 커밋 또는 기준 및 헤드 리비전을 검토하세요. **정밀 스캔은** 
변경 사항 스캔에서 사용할 수 없습니다.

대화에서 Codex에 커밋되지 않은 변경 사항을 검토해 달라고 요청할 수도 있습니다:

```text
Use $codex-security:security-diff-scan to review my current uncommitted changes for security regressions.

커밋 또는 브랜치 범위의 경우 필요에 따라 두 리비전을 모두 지정하세요:

```text
Use $codex-security:security-diff-scan to review the changes from origin/main to HEAD for security regressions. Focus on authentication, authorization, input handling, filesystem access, network requests, and secrets.

로컬 체크아웃에서 기준 및 헤드 리비전을 사용할 수 있는 경우
Pull Request를 지정할 수도 있습니다.

## 설정 단계에서 변경 사항 확인

1. **변경 사항을** 선택하세요.
2. 체크아웃한 레포지토리, 현재 브랜치, 최신 커밋을 확인하세요.
3. **검토할 변경 사항에서** 다음 중 하나를 선택하세요:
   - 현재 작업 트리의 경우 `Uncommitted changes`.
   - 단일 커밋 검토의 경우 최신 커밋.
   - 브랜치 또는 Pull Request 범위의 경우 기준 및 헤드 리비전.
4. 요약이 검토하려는 변경 사항을 설명하는지 확인하세요.
5. **스캔 시작을** 선택하세요.

Codex는 다른 브랜치를 체크아웃하거나 선택한 작업 트리를 전환하지 않습니다. 요청한
리비전을 로컬에서 사용할 수 없다면 검토 전에 가져오거나, 로컬에서 사용할 수 있는
기준 및 헤드 리비전을 제공하세요.

## 보안 이슈 처리

결과를 검토한 후 [수락한
보안 이슈를 수정하고 검증](/ko-KR/codex/security/plugin/fix-findings)하거나 [보안 이슈를 내보내고
추적](/ko-KR/codex/security/plugin/export-findings)하세요.

## CI/CD에서 검토 자동화

베타 독립 실행형 CLI를 사용할 수 있다면 [CI에서 Codex Security
실행](/ko-KR/codex/security/cli/ci)을 참조해 구조화된 JSON, 심각도 정책, SARIF
업로드에 대해 확인하세요. 설치된 플러그인 스킬을
`codex exec`으로 호출하려면 이 섹션의 안내를 따르세요.

러너가 사용자 상호작용 없이 Codex CLI를
호출할 수 있다면 CI에서 `$codex-security:security-diff-scan`을 실행하세요. 먼저 스캔
자격 증명을 노출하지 않고 CLI를 설치하세요:

```bash
npm install --global @openai/codex

CLI에 Codex Security 플러그인을 설치하세요:

```bash
codex plugin add codex-security@openai-curated

설치 명령어는 공개 Codex CLI 플러그인 마켓플레이스를 사용합니다.
CI에서 특정 플러그인 버전이나 기능에 의존하기 전에 [플러그인 변경 로그](/ko-KR/codex/security/plugin/changelog)를
확인하세요.

다음으로 CI 비밀 저장소의 OpenAI API 키를
`CODEX_SECURITY_API_KEY`로 제공하세요. 자격 증명은 스캔할 때만 노출하세요:

```bash
CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
  --sandbox workspace-write \
  "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."

쓰기 가능한 샌드박스에서는 스캔이 임시 아티팩트를 생성할 수 있습니다. 프롬프트는
여전히 Codex가 소스 체크아웃을 변경하지 않도록 요구합니다.

스캔 출력은
`$TMPDIR/codex-security-scans/<repository>/<scan-id>/`에 기록됩니다:

| 파일                 | 내용                                                                                                                                                  |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `report.md`          | 전체 스캔 디렉터리의 내용을 확인할 수 있는 기본 진입점.                                                                                              |
| `findings/<slug>/`   | 요청 시 제공되는 상세 취약점 보고서와 이를 뒷받침하는 개념 증명 파일.                                                                     |
| `hardening/`         | 요청 시 제공되는 구조적 보안 강화 지침과 이를 뒷받침하는 제안.                                                                                   |
| `findings.json`      | 안정적인 식별자, 심각도, 신뢰도, 소스 위치, 해결 방법이 포함된 보안 이슈입니다. 승인된 내부 보안 워크플로우 또는 다운스트림 도구에 전달하세요. |
| `scan-manifest.json` | 검토 대상, 리비전, 아티팩트 해시가 포함된 봉인된 스캔 확인서.                                                                             |
| `coverage.json`      | 검토된 영역과 검토가 보류된 영역, 제외 항목, 검사 범위의 완전성.                                                                                    |

전체 구조는 [`findings.json` 스키마](https://github.com/openai/plugins/blob/main/plugins/codex-security/schemas/findings.schema.json)에
정의되어 있습니다. 이 스키마에는 다음 필드가 포함됩니다:

| 필드                     | 타입   | 설명                                                            |
| ------------------------- | ------ | ---------------------------------------------------------------------- |
| `documentType`            | 문자열 | 문서를 `codex-security.findings`로 식별합니다.                  |
| `schemaVersion`           | 문자열 | 보안 이슈 스키마의 버전을 식별합니다.                                |
| `scanId`                  | 문자열 | 보안 이슈를 생성한 스캔을 식별합니다.                        |
| `findings`                | 배열  | 0개 이상의 보안 이슈 객체를 포함합니다.                                 |
| `findings[].findingId`    | 문자열 | 보안 이슈 핑거프린트에서 파생된 안정적인 보안 이슈 식별자.        |
| `findings[].occurrenceId` | 문자열 | 특정 스캔에서 나타난 해당 보안 이슈의 발생 건을 식별합니다.          |
| `findings[].ruleId`       | 문자열 | 취약점 계열을 식별합니다.                                   |
| `findings[].identity`     | 객체 | 시맨틱 앵커와 선택적 형제 인스턴스 식별자를 포함합니다. |
| `findings[].fingerprints` | 객체 | 핑거프린트 알고리즘과 주 핑거프린트를 포함합니다.            |
| `findings[].title`        | 문자열 | 보안 이슈의 짧은 제목을 제공합니다.                                      |
| `findings[].summary`      | 문자열 | 취약점과 그 영향을 요약합니다.                           |
| `findings[].severity`     | 객체 | 심각도 수준과 선택적인 점수 산정 세부 정보를 포함합니다.              |
| `findings[].confidence`   | 객체 | 신뢰도 수준과 그 근거를 포함합니다.                           |
| `findings[].taxonomy`     | 객체 | 취약점 범주와 CWE 식별자를 포함합니다.               |
| `findings[].locations`    | 배열  | 영향받는 파일, 줄 번호, 각 위치의 역할을 나열합니다.                |
| `findings[].remediation`  | 문자열 | 권장 수정 방법을 설명합니다.                                         |
| `findings[].provenance`   | 객체 | 보안 이슈의 출처를 식별합니다.                                  |

예를 들어 다음 명령어는 보안 이슈마다 탭으로 구분된 행을 하나씩 출력합니다:

```bash
jq -r '
  .findings[] |
  [.findingId, .severity.level, .confidence.level, .locations[0].path, .locations[0].startLine, .title] |
  @tsv
' findings.json

이 예에서는 Node.js와 `npm`, Git, Python 3, `jq`, 제공업체의 명령줄 도구를 갖춘
신뢰할 수 있는 Linux 러너를 사용한다고 가정합니다. `npm` 전역 패키지 접두사에는
쓰기 권한이 있어야 합니다.

사용 중인 CI 제공업체에 맞는 예를 선택하세요:

스캔 결과에는 민감한 취약점 세부 정보가 포함될 수 있습니다. 아티팩트는
비공개로 유지하고, 공개 대상과 내용 및 필요한 승인을 검토한 후에만
보안 이슈를 공개하세요.

  <div slot="github">

```yaml
name: Codex Security review

on:
  pull_request:

jobs:
  security-review:
    if: github.event.pull_request.head.repo.full_name == github.repository
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0
          persist-credentials: false

      - name: Install Codex Security
        env:
          CODEX_HOME: ${{ runner.temp }}/codex-home
        run: |
          npm install --global @openai/codex
          codex plugin add codex-security@openai-curated

      - name: Review code changes
        env:
          CODEX_SECURITY_API_KEY: ${{ secrets.CODEX_SECURITY_API_KEY }}
          CODEX_HOME: ${{ runner.temp }}/codex-home
          TMPDIR: ${{ runner.temp }}/codex-security
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
          HEAD_REVISION: ${{ github.event.pull_request.head.sha }}
        run: |
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_REVISION")"
          CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
            --sandbox workspace-write \
            "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: codex-security-review
          path: ${{ runner.temp }}/codex-security/codex-security-scans

  </div>

  <div slot="gitlab">

마스킹된 `CODEX_SECURITY_API_KEY` CI/CD 변수를 만들고, 보안 이슈를 공유하기 전에 스캔
아티팩트를 비공개로 검토하세요.

```yaml
codex-security-review:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID'
  variables:
    GIT_DEPTH: "0"
  script:
    - |
      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY

      npm install --global @openai/codex
      codex plugin add codex-security@openai-curated
      CODEX_API_KEY="$codex_security_api_key" codex exec \
        --sandbox workspace-write \
        "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
  after_script:
    - |
      unset CODEX_SECURITY_API_KEY
      scan_root="/tmp/codex-security-$CI_JOB_ID/codex-security-scans"
      if [ -d "$scan_root" ]; then
        tar -czf codex-security-artifacts.tar.gz -C "$scan_root" .
      fi
  artifacts:
    when: always
    paths:
      - codex-security-artifacts.tar.gz

  </div>

  <div slot="azure">

```yaml
trigger: none

pool:
  vmImage: ubuntu-latest

steps:
  - checkout: self
    fetchDepth: 0

  - bash: |
      set -euo pipefail

      npm install --global @openai/codex
      codex plugin add codex-security@openai-curated
    displayName: Install Codex Security

  - bash: |
      set -euo pipefail

      CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
        --sandbox workspace-write \
        "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
    displayName: Review code changes
    condition: and(succeeded(), ne(variables['System.PullRequest.IsFork'], 'True'))
    env:
      CODEX_SECURITY_API_KEY: $(CODEX_SECURITY_API_KEY)

  - publish: $(Agent.TempDirectory)/codex-security/codex-security-scans
    artifact: codex-security-review
    condition: always()

Azure Repos에서는 Pull Request에서 파이프라인이 실행되도록
 **빌드 유효성 검사** 브랜치 정책을 구성하세요.

  </div>

  <div slot="jenkins">

```groovy
pipeline {
  agent { label 'linux' }
  stages {
    stage('Codex Security review') {
      when {
        allOf {
          changeRequest()
          expression { !env.CHANGE_FORK?.trim() }
        }
      }
      steps {
        sh '''#!/usr/bin/env bash
          set -euo pipefail

          mkdir -p "$TMPDIR"
          git fetch --no-tags origin "$CHANGE_TARGET"
          target="$(git rev-parse FETCH_HEAD)"
          git fetch --no-tags origin "$CHANGE_BRANCH"
          git rev-parse FETCH_HEAD > "$TMPDIR/head"
          git merge-base "$target" "$(cat "$TMPDIR/head")" > "$TMPDIR/base"
          npm install --global @openai/codex
          codex plugin add codex-security@openai-curated
        '''
        withCredentials([string(credentialsId: 'codex-security-api-key', variable: 'CODEX_SECURITY_API_KEY')]) {
          sh '''#!/usr/bin/env bash
            set +x
            set -euo pipefail

            CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
              --sandbox workspace-write \
              "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
          '''
        }
      }
      post {
        always {
          sh '''#!/usr/bin/env bash
            set -euo pipefail
            scan_root="/tmp/codex-security-$BUILD_TAG/codex-security-scans"
            if [ -d "$scan_root" ]; then
              tar -czf codex-security-artifacts.tar.gz -C "$scan_root" .
            fi
          '''
          archiveArtifacts artifacts: 'codex-security-artifacts.tar.gz', allowEmptyArchive: true
        }
      }
    }
  }
}

  </div>

이 예에서는 포크된 Pull Request를 건너뜁니다. 자격 증명이 필요한 작업은 보호된
파이프라인 정의에서만 실행하고, 스캔 자격 증명을 안전하게 맡길 수 있는
기여자에게만 실행을 허용하세요. `codex-security-scans`를 아카이브해 구조화된 보안 이슈,
매니페스트, 커버리지, `report.md`와 요청된
`findings/` 또는 `hardening/` 결과물을 함께 보관하세요. 먼저 결과를 참고용으로 사용하고,
작업을 필수 검사로 지정하기 전에 커버리지와 런타임을 검토하세요.

API 키 처리와 샌드박스 제어에 관한 자세한 내용은 [비대화형
모드](/ko-KR/codex/non-interactive-mode)를 참고하세요. 조직에서 [Codex
GitHub Action](/ko-KR/codex/github-action) 사용을 허용하면 이 액션으로 런타임에 CLI를 설치할 수 있지만,
플러그인을 먼저 설치하고 해당 액션의 `codex-home`
입력이 동일한 `CODEX_HOME`을 가리키도록 설정해야 합니다.

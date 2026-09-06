<!-- source: https://learn.chatgpt.com/ko-KR/docs/security/cli/ci/gitlab -->

GitLab CI/CD에서 Codex Security를 실행해 커밋된 변경 사항과 보호된
브랜치를 스캔하고, GitLab Security에 보안 이슈를 게시하세요. 원하는 경우 검증된
수정 사항을 초안 병합 요청으로 제안할 수도 있습니다.

이 워크플로우는 스캔 자격 증명을 레포지토리 쓰기 권한과 분리합니다.
생성된 변경 사항은 병합 전에 반드시 사람이 검토해야 합니다.

스캔 결과만 보고하는 방식으로 시작하세요. 프로젝트의 러너, 보안 이슈,
자격 증명의 사용 범위를 확인한 후에만 수정 기능을 활성화하세요.

## 시작하기 전에

다음이 필요합니다:

- Codex 샌드박스의 사용자 네임스페이스를 지원하는
신뢰할 수 있는 러너가 있는 GitLab 프로젝트.
- GitLab 프로젝트의 Maintainer 또는 Owner 역할. 이 역할로
[프로젝트 CI/CD 변수](https://docs.gitlab.com/ci/variables/)와 보호된
  리소스를 구성할 수 있습니다.
- Codex Security 이용 권한이 있는 OpenAI API 키. Platform
  API 키를 사용하는 조직은 [Trusted Access for Cyber
  이용을 신청](https://openai.com/form/enterprise-trusted-access-for-cyber/)할 수 있습니다.
  ChatGPT 인증을 사용하는 개인은 [개인용 Trusted Access
  플로우](https://chatgpt.com/cyber)를 이용할 수 있습니다. 일부 계정이나 레포지토리는 전체 레포지토리를
  스캔하려면 이 권한이 필요합니다.
- [SARIF 2.1.0
  수집](https://docs.gitlab.com/user/application_security/detect/sarif/)을 위한 GitLab Ultimate 19.2 이상.
- 병합 요청 작업에서 병합 기준점을 계산하는 데 필요한 전체 Git 이력.

파이프라인 이미지는 Node.js 26, Python 3, Git, `rg`, 고정된 버전의
Codex Security CLI를 설치합니다. 자동 수정을 하려면 기존
회귀 테스트와 보호된 자격 증명 없이 레포지토리에서 정의한 명령어를
실행할 수 있는 러너도 필요합니다.

## 스캔 전용 파이프라인으로 시작

`CODEX_SECURITY_API_KEY`라는 이름의 GitLab CI/CD 변수를 만들고
마스킹, 숨김, 보호를 설정하세요. Codex Security 이용 권한이 있는 OpenAI Platform API 키를
사용하고, 변수의 환경 범위를 `codex-security/openai`로 설정하세요.
[환경 범위가 지정된 CI/CD 변수](https://docs.gitlab.com/ci/environments/#limit-the-environment-scope-of-a-cicd-variable)를 참고하세요.

먼저 테스트 프로젝트에 이 최소 구성의 파이프라인을 추가하세요. 이 파이프라인은 조건을 충족하는 보호된 병합 요청에서 커밋된 변경 사항을 스캔하고,
성공한 보고 작업에서 SARIF를 게시한 다음,
별도의 게이트에서 스캐너 결과를 복원합니다:

```yaml
stages:
  - security_scan
  - security_gate

.codex-security-merge-request:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID && $CI_MERGE_REQUEST_SOURCE_BRANCH_PROTECTED == "true" && $CI_MERGE_REQUEST_TARGET_BRANCH_PROTECTED == "true"'

codex-security:
  extends: .codex-security-merge-request
  stage: security_scan
  image: node:26-bookworm-slim
  environment:
    name: codex-security/openai
    action: access
  variables:
    GIT_DEPTH: "0"
  before_script:
    - npm install --prefix /tmp/codex-security-cli --ignore-scripts --no-audit --no-fund @openai/codex-security@0.1.20
  script:
    - |
      set -eu
      test -n "${CODEX_SECURITY_API_KEY:-}"

      CODEX_SECURITY_BIN="/tmp/codex-security-cli/node_modules/.bin/codex-security"
      RESULTS_DIR="/tmp/codex-security-results-$CI_JOB_ID"
      ARTIFACT_DIR="codex-security-artifacts"
      BASE_REVISION="$(git merge-base \
        "$CI_MERGE_REQUEST_DIFF_BASE_SHA" "$CI_COMMIT_SHA")"
      install -d -m 700 "$RESULTS_DIR" "$ARTIFACT_DIR/results"

      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY
      set +e
      OPENAI_API_KEY="$codex_security_api_key" \
        "$CODEX_SECURITY_BIN" scan . \
          --diff "$BASE_REVISION" \
          --head "$CI_COMMIT_SHA" \
          --auth api-key \
          --output-dir "$RESULTS_DIR" \
          --json
      scan_exit="$?"
      set -e
      unset codex_security_api_key

      case "$scan_exit" in
        0|1|2) ;;
        *) exit "$scan_exit" ;;
      esac

      "$CODEX_SECURITY_BIN" export "$RESULTS_DIR" \
        --export-format sarif \
        --source-root "$CI_PROJECT_DIR" \
        --output "$ARTIFACT_DIR/results.sarif"
      test -s "$ARTIFACT_DIR/results.sarif"
      cp -R "$RESULTS_DIR"/. "$ARTIFACT_DIR/results/"
      printf '%s\n' "$scan_exit" > "$ARTIFACT_DIR/scan-exit-code.txt"
      exit 0
  artifacts:
    when: always
    access: maintainer
    expire_in: 7 days
    paths:
      - codex-security-artifacts/
    reports:
      sarif: codex-security-artifacts/results.sarif

codex-security-gate:
  extends: .codex-security-merge-request
  stage: security_gate
  image: alpine:3.20
  needs:
    - job: codex-security
      artifacts: true
  script:
    - exit "$(cat codex-security-artifacts/scan-exit-code.txt)"

  

시크릿이 포함된 작업을 실행하기 전에 `.gitlab-ci.yml`의 모든 변경 사항을 검토하세요.
이 최소 예제에서는 전체 스캔과 수정 기능을 의도적으로 제외했습니다.

## 프로덕션 파이프라인 도입

1. [전체 GitLab 파이프라인을 다운로드](/codex/security/cli/ci/gitlab.yml)한 후
   레포지토리 루트에 `.gitlab-ci.yml`로 저장하세요. 레포지토리에
   파이프라인이 이미 있다면 예제의 단계, 숨겨진 템플릿,
   작업을 기존 파일에 병합하세요.
2. 기존 빌드, 테스트, 배포 단계는 유지하세요. 프로젝트에서
`workflow: rules`를 사용한다면, 스캔하려는 파이프라인 이벤트가
   허용되는지 확인하세요.

이 예제는 `security_scan`, `security_remediation`, `security_publish`,
`security_gate` 단계를 추가합니다. 스캔 결과만 보고하는 데는
`CODEX_SECURITY_API_KEY`만 필요합니다.

스캔 작업은 기본적으로 같은 프로젝트 안에서 보호된 브랜치 간에 생성된
병합 요청에만 실행됩니다. 보호된 기본 브랜치로의 푸시와 수동 파이프라인을
스캔하려면 `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH=true`를 설정하세요.
보호된 기본 브랜치에서 예약 심층 스캔을 활성화하려면 `CODEX_SECURITY_SCHEDULED_DEEP_SCAN=true`를 설정하고
시간과 비용 한도를 명시적으로 구성하세요.

병합 요청 파이프라인은 다음 조건을 모두 충족할 때만 보호된 변수와 러너에 접근할 수 있습니다:

- 같은 프로젝트의 소스 브랜치와 대상 브랜치를 모두 보호해야 합니다.
- 프로젝트에서 [병합 요청 파이프라인이 보호된 변수와
  러너에 접근하도록 허용](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#control-access-to-protected-variables-and-runners)해야 합니다.
- 파이프라인을 시작하는 사용자가 대상 브랜치에 푸시하거나 병합할 수 있어야 합니다.

포크 파이프라인과 보호되지 않은 병합 요청에는 스캔
자격 증명이 제공되지 않습니다. 시크릿이 포함된 작업을 실행하기 전에
`.gitlab-ci.yml`의 모든 변경 사항을 검토하세요. 변수를 마스킹하고 숨겨도
신뢰할 수 없는 CI 코드가 안전해지는 것은 아닙니다.

## 스캔 실행 및 보안 이슈 검토

조건을 충족하는 보호된 병합 요청을 만들거나 보호된 기본 브랜치에서
파이프라인을 실행하세요. 유료 전체 레포지토리 스캔을 실행하기 전에
작은 변경 내역부터 시작하세요.

`codex-security` 작업을 열고 아티팩트에 다음 항목이 포함되어 있는지 확인하세요:

- `scan-manifest.json`
- `findings.json`
- `coverage.json`
- `results.sarif`
- `scan-exit-code.txt`

그런 다음 파이프라인의 **보안** 탭을 열어 수집 경고를 검토하고,
보안 이슈 식별자, 심각도, 소스 위치를 확인하세요. 기본 브랜치 스캔은
프로젝트 취약점 기록도 생성합니다. 병합 요청의 보안 이슈는
파이프라인의 보안 탭이나 병합 요청의 보안 위젯에 표시되지만,
프로젝트 전체의 취약점 기록을 생성하지는 않습니다.

스캔 결과에는 취약한 소스 코드 조각, 증거, 수정 세부 정보가
포함될 수 있으므로 아티팩트 접근을 제한하세요.

## 스캔 프로필 선택

파이프라인은 트리거에 따라 프로필을 선택합니다:

| 트리거                                        | 대상          | 모드       | 추론 수준  |
| ---------------------------------------------- | --------------- | ---------- | ------- |
| 같은 프로젝트 내 보호된 병합 요청           | 커밋된 변경 내역  | `standard` | `low`   |
| 보호된 기본 브랜치 푸시 또는 수동 실행(별도 활성화 필요) | 전체 레포지토리 | `standard` | `high`  |
| 보호된 기본 브랜치의 예약 실행(별도 활성화 필요)    | 전체 레포지토리 | `deep`     | `xhigh` |

병합 요청 스캔은 커밋된 변경 사항에 집중해 피드백을 제공합니다.
기본 브랜치 스캔은 통합된 레포지토리를 검토합니다. 예약 심층 스캔은
더 넓은 범위를 주기적으로 검사합니다. 완료된 변경 내역 스캔은 해당
변경 사항에만 적용되며, 전체 레포지토리에 문제가 없음을 보여 주지는 않습니다.

이 워크플로우는 레포지토리 외부에 CLI를 설치하고 절대 경로로
실행합니다. 모의 실행 사전 점검은 해당 프로세스에만 제공된 API 키를 사용하지만,
유료 스캔을 시작하거나 API 인증, Codex Security 이용 권한, 할당량,
모델 가용성을 확인하지는 않습니다.

워크플로우는 스캔 상태와 결과를 작업 트리 외부에 기록하고,
`OPENAI_API_KEY`를 스캔 프로세스에만 제공합니다. CLI는 모든 GitLab 변수를 상속하는 대신
명시적으로 지정한 소수의 환경 변수만 전달받습니다. 변경 내역 스캔에서는
워크플로우가 병합 기준점을 계산하고, 검토된 베이스 및
헤드 리비전으로 스캔 대상을 고정합니다.

이 예제에서 `@openai/codex-security`의 고정 버전은 `0.1.20`입니다. 버전을 변경하기 전에 인증,
아티팩트, SARIF 수집, 정책 게이트 동작을 다시 테스트하세요.

## 보고와 정책 적용 분리

GitLab은 성공한 보고 작업에서 SARIF를 수집합니다. 파이프라인은 먼저
보고서를 게시한 다음 별도의
`codex-security-gate` 작업에서 스캐너의 종료 상태를 복원합니다.

보고 작업은 종료 코드가 `0` 또는 `1`일 때의 보안 이슈를 수용합니다.
종료 코드가 `2`인 경우에는 스캔 매니페스트가 스캔 완료를 입증하고,
커버리지가 명시적으로 `partial`이며 비어 있지 않은 SARIF 보고서가 존재할 때만 수용합니다.
그 밖의 런타임, 구성, 내보내기 실패는 계속 진행을 차단합니다.

최종 게이트는 다음 스캐너 종료 코드를 그대로 유지합니다:

| 종료 코드 | 의미                                                                     |
| ---- | --------------------------------------------------------------------------- |
| `0`  | 누락된 검사 범위 없이 스캔을 완료했으며 정책 기준을 통과했습니다.            |
| `1`  | 스캔을 완료했으며 심각도가 설정된 임계값 이상인 보안 이슈가 발견되었습니다. |
| `2`  | 스캔 커버리지가 불완전하거나 입력 또는 런타임 오류가 발생했습니다.              |

이 예제에서는 부분 커버리지의 처리 기준을 조정하는 동안 종료 코드 `2`도 일시적으로 허용합니다.
불완전한 커버리지가 파이프라인을 차단해야 한다면 이 허용 설정을 제거하세요.

수정과 게시는 최종 정책 게이트 전에 실행됩니다. 이후 게이트가 파이프라인을 실패로 처리하더라도 조건에 맞는 보안 이슈에 대해서는 검증된 초안 병합 요청을 생성할 수 있습니다.

## 검증된 수정 활성화

자동 수정은 선택 사항이며 보호된 기본 브랜치의 파이프라인에서만 실행됩니다. Codex 수정 프로세스와 레포지토리에서 관리하는 검증 명령어에는 GitLab 프로젝트 액세스 토큰이나 러너가 주입한 자격 증명이 전달되지 않습니다.

이 워크플로우는 세 가지 보안 원칙을 지킵니다. 레포지토리에서 관리하는 명령어에는 OpenAI나 GitLab 자격 증명을 절대 전달하지 않고, 게시 작업에만 레포지토리 쓰기 권한을 부여하며, 생성된 모든 변경 사항은 사람이 검토하고 병합할 때까지 초안으로 유지합니다.

워크플로우는 다음과 같이 동작합니다:

1. 전체 스캔 커버리지와 심각도가 `high` 또는 `critical`인
   보안 이슈가 필요합니다.
2. 패치를 적용하기 전에 설정된 회귀 테스트가 실패하는지 확인합니다.
3. 해당 문제에 집중한 패치를 생성하고 CI, 자격 증명, 바이너리 또는 기타 보호된 파일의 변경을 거부합니다.
4. OpenAI, GitLab, 레지스트리, 배포 또는 작업 토큰 자격 증명 없이 회귀 테스트를 실행합니다.
5. `verify-fix` 명령어로 `fixed`, `still_vulnerable` 또는 `inconclusive`를 반환합니다.
   `verify-fix`가 `fixed`를 반환하고
   검증 과정에서 패치가 변경되지 않은 경우에만 작업이 패치를 게시합니다.

수정 기능을 활성화하려면 다음 보호된 변수를 설정하세요:

- `CODEX_SECURITY_ENABLE_REMEDIATION`을 `true`로 설정하세요.
- `CODEX_SECURITY_VERIFICATION_COMMAND`에 기존 회귀 테스트를 설정하세요.
  이 테스트는 수정 전에는 종료 코드 `1`, 수정 후에는 종료 코드 `0`으로 종료해야 합니다.
- 필요하면 `CODEX_SECURITY_SETUP_COMMAND`에 비대화형 종속성
  설정 명령어를 지정하세요.

특정 구현이 아니라 근본적인 보안 불변 조건을 검증하는 회귀 테스트를 선택하세요. 생성된 테스트 변경 사항과 소스 변경 사항도 똑같이 꼼꼼하게 검토하세요.

<details>
  <summary>고급: 레포지토리 명령어 격리</summary>

`validate`, `patch`, `verify-fix` 명령어에는 해당 프로세스에서만 사용할 수 있는
`CODEX_API_KEY`가 전달됩니다. 레포지토리에서 관리하는 설정 및 테스트 명령어는
추적 중인 소스 파일의 쓰기 가능한 복사본에서 별도의 일반 사용자 권한으로 실행됩니다.
이 복사본에서는 Git 메타데이터, 서브모듈 콘텐츠,
다운로드한 아티팩트를 의도적으로 제외합니다. `.git` 또는
서브모듈이 필요한 설정 및 테스트 명령어는 자격 증명 없이 실행하도록 별도로 설계한 작업에서 실행해야 합니다.

root 소유의 Codex 단계만 원본 체크아웃이나 그 옆에 있는 GitLab
파일 변수 디렉터리에 접근할 수 있습니다. 복사본의 정리된 환경에는
`PATH`, `HOME`, `LANG`, `CI`, `CI_PROJECT_DIR`만 포함됩니다. 명령어에 다른
비밀 정보가 아닌 값이 필요하면 명령어를 검토한 후 해당 값을 허용 목록에 추가하세요. 러너에서
사용자를 전환할 수 없다면 수정 기능을 활성화하기 전에 검증을 자격 증명이 없는 별도
작업으로 옮기세요.

</details>

## 초안 병합 요청 게시

Developer 역할과 `api` 및 `write_repository` 권한 범위로 [GitLab 프로젝트 액세스
토큰](https://docs.gitlab.com/user/project/settings/project_access_tokens/#create-a-project-access-token)을 만드세요.
토큰을 보호, 마스킹, 숨김 설정을 적용한
`GITLAB_REMEDIATION_TOKEN` 변수에 저장하고, 범위는
`codex-security/publish` 환경으로만 제한하세요.

`CODEX_SECURITY_CREATE_MR=true`로 설정해 게시를 활성화하세요. 비밀 정보가 아닌 변수인
`CODEX_SECURITY_MR_TEST_COMMAND`에는 생성되는 모든 수정 브랜치가 통과해야 하는 해당 프로젝트의 보안 회귀
테스트를 설정하세요. 생성된 보호되지 않은 병합 요청에서 명령어를 읽을 수 있도록
이 변수는 보호되지 않은 상태로 유지하세요.
게시 워크플로우는 다음과 같이 동작합니다:

- 레포지토리 쓰기 토큰을 받지만 OpenAI 자격 증명은 받지 않습니다.
- `codex-security/fix-<finding-hash>` 브랜치를 생성합니다.
- 초안 병합 요청을 생성하며, 이미 열려 있는 초안이 있으면 중복 생성하지 않고 기존 초안을 재사용합니다.
- 보호되지 않은 수정 브랜치의 회귀 테스트를 추적 중인 파일만 포함한 복사본에서 보호된 자격 증명 없이 일반 사용자 권한으로 실행합니다.
- 생성된 변경 사항을 절대 자동으로 병합하지 않습니다.

프로젝트 액세스 토큰 대신 `CI_JOB_TOKEN`을 사용하지 마세요. 이 토큰은 필요한
병합 요청 생성 작업을 수행할 수 없습니다. 병합하기 전에 제안된 패치,
검증 근거, 보안 이슈를 검토하세요.

## 선택적 변수 설정

활성화할 기능에 필요한 변수만 설정하세요:

| 변수                                  | 필요한 경우                       | 기본값 또는 용도                                          |
| ----------------------------------------- | --------------------------------- | ----------------------------------------------------------- |
| `CODEX_SECURITY_API_KEY`                  | 모든 스캔                        | 보호, 마스킹, 숨김 설정 적용; 범위를 `codex-security/openai`로 제한 |
| `CODEX_SECURITY_VERSION`                  | CLI 업그레이드                       | `0.1.20`로 고정됨; 변경 전 재테스트 필요                  |
| `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` | 기본 브랜치 전체 스캔         | 명시적으로 활성화해야 함; 기본적으로 비활성화됨                             |
| `CODEX_SECURITY_SCHEDULED_DEEP_SCAN`      | 예약 심층 스캔              | 명시적으로 활성화해야 함; 기본적으로 비활성화됨                             |
| `CODEX_SECURITY_DEEP_MAX_TIME_HOURS`      | 예약 심층 스캔              | 시간 예산을 `0` 초과, `8` 미만으로 설정해야 함     |
| `CODEX_SECURITY_DEEP_MAX_COST`            | 예약 심층 스캔              | 예상 비용 가드레일(USD, 필수): `0` 초과      |
| `CODEX_SECURITY_ENABLE_REMEDIATION`       | 패치 생성                  | 보호된 변수로 활성화해야 함; 기본적으로 비활성화됨                            |
| `CODEX_SECURITY_VERIFICATION_COMMAND`     | 패치 생성                  | 회귀 테스트(보호됨)                                   |
| `CODEX_SECURITY_SETUP_COMMAND`            | 수정 설정(선택 사항)        | 종속성 설치(보호됨)                           |
| `CODEX_SECURITY_REMEDIATION_EFFORT`       | 수정 세부 조정(선택 사항)       | `high`                                                      |
| `CODEX_SECURITY_MAX_CHANGED_FILES`        | 패치 크기 제한(선택 사항)         | `8`; 허용 범위는 `1`부터 `20`까지                         |
| `CODEX_SECURITY_CREATE_MR`                | 초안 병합 요청 생성      | 보호된 변수로 활성화해야 함; 기본적으로 비활성화됨                            |
| `GITLAB_REMEDIATION_TOKEN`                | 초안 병합 요청 생성      | 범위가 `codex-security/publish`로 제한된 Developer 역할의 프로젝트 토큰  |
| `CODEX_SECURITY_GITLAB_INTERNAL_URL`      | 자체 호스팅 환경에서 게시(선택 사항)   | 러너에서 접근할 수 있는 GitLab 오리진                     |
| `CODEX_SECURITY_MR_TEST_COMMAND`          | 초안 병합 요청 게시    | 프로젝트별 회귀 테스트(필수, 비밀 정보 아님)       |
| `CODEX_SECURITY_MR_SETUP_COMMAND`         | 수정 브랜치 설정(선택 사항) | 종속성 설정(비밀 정보 아님)                                 |

GitLab이 `CI_*` 변수를 제공합니다. 파이프라인이
`CODEX_SECURITY_BIN`, `CODEX_SECURITY_EFFORT`, `CODEX_SECURITY_MODE`,
`CODEX_SECURITY_STATE_DIR`, `CODEX_SECURITY_TARGET` 변수를 관리하므로
프로젝트 변수로 구성하지 마세요. diff 스캔에서는 CLI가 정규화된 base 및 head 리비전을 바탕으로
정규 대상 식별자를 도출합니다.

## 정책 적용 및 비용 조정

병합 요청 피드백에는 변경 사항에 집중하는 diff 스캔을, 기본 브랜치에는 표준 레포지토리 스캔을,
더 넓은 범위의 검사에는 예약된 심층 스캔을 사용하세요. 레포지토리 전체를 스캔하는 두 프로필은
기본적으로 비활성화되어 있습니다. 예약된 심층 스캔에는
`CODEX_SECURITY_DEEP_MAX_TIME_HOURS`와 `CODEX_SECURITY_DEEP_MAX_COST`도 필요합니다.
CLI 시간 한도는 작업의 제한 시간인 8시간 미만으로 유지하세요. 예산을 설정하기 전에
대표적인 실행 사례에서 시간과 비용을 측정하세요. `--max-cost`는 실제 청구액의 절대 상한이 아니라
예상 비용에 대한 가드레일로 보세요.

결과만 보고하는 스캔으로 시작하세요. 팀에서 대표적인 보안 이슈와 검사 범위, 비용, 실행 시간을
검토한 후 `--fail-on-severity`를 추가하세요. 심각도 정책과 종료 코드에 관한 자세한 내용은 [CI에서 Codex Security
실행하기](/ko-KR/codex/security/cli/ci)를
참조하세요.

작업이 실패한 경우:

- 스캔 아티팩트가 없으면 구성이나 러너에 문제가 있다는 신호입니다.
- 아티팩트는 있지만 검사 범위가 불완전하다면 `coverage.json`을 검토하세요.
- GitLab에 보안 이슈가 표시되지 않으면 SARIF 보고서 작업이 성공했는지,
GitLab이 보고서를 수락했는지 확인하세요.
- 수정 작업이 생략되었다면 보호된 브랜치인지, 전체 범위가 검사되었는지 확인하고,
보안 이슈의 심각도, 검증 명령어, 기능 활성화 변수를 점검하세요.
- 게시 오류가 발생하면 프로젝트 토큰의 역할, 권한 범위,
환경 제한을 확인하세요.

모든 명령어, 플래그, 아티팩트에 관한 내용은 [Codex Security CLI
참조 자료](/ko-KR/codex/security/cli/reference)를 확인하세요.

<!-- source: https://learn.chatgpt.com/ko-KR/docs/security/plugin/export-findings -->

완료된 Codex Security 스캔은 다음 두 가지 방식으로 활용할 수 있습니다:

- **내보내기** 기능은 이식 가능한 JSON, CSV 또는 SARIF 파일을 생성합니다.
- **보안 이슈 추적** 기능은 선택한 보안 이슈를 Linear, GitHub 또는 Jira
  이슈나 비공개 GitHub Security Advisory 초안 하나로 준비합니다. Codex는
  중복을 확인하고 작성하기 전에 사용자의 승인을 기다립니다.

어느 워크플로우도 봉인된 스캔 번들을 변경하지 않습니다.

  사용 가능한 아티팩트 링크와 내보내기 형식은 Codex 인터페이스와
  설치된 플러그인 버전에 따라 달라집니다. 자동화에서 해당 형식을 사용하기 전에
  [플러그인
  변경 로그](/ko-KR/codex/security/plugin/changelog)를 확인하세요.

## 이식 가능한 아티팩트 내보내기

데스크톱 앱에서 **보안** \> **스캔** 메뉴로 이동해 완료된 스캔을 여세요.
사용 가능한 아티팩트 링크를 열어 `report.md`, `findings.json`,
`scan-manifest.json`, `coverage.json` 및 SARIF 보고서(있는 경우)를 확인하세요.

지원되는 다른 형식을 만들려면 완료된 스캔의 봉인된 번들을 변경하지 않고
보안 이슈를 내보내도록 Codex에 요청하세요:

```text
Export the findings from [completed scan directory] as [JSON, CSV, or SARIF]. Do not modify the sealed scan bundle or upload its contents.

대상에 맞는 형식을 선택하세요:

| 형식 | 용도                                                        |
| ------ | ----------------------------------------------------------------- |
| JSON   | 도구와 스크립트에서 사용할 수 있도록 봉인된 구조화 보안 이슈 데이터를 보존합니다.    |
| CSV    | 스프레드시트에서 보안 이슈와 현재 로컬 트리아지 상태를 검토합니다.  |
| SARIF  | 보안 이슈를 SARIF 교환 형식을 지원하는 도구로 전송합니다. |

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    완료된 스캔에서 커버리지, 보안 이슈, 스캔 매니페스트, Markdown 보고서 또는 SARIF
아티팩트를 여세요.
  </figcaption>
</figure>

**Markdown 보고서를** 선택하면 설정한 외부
편집기에서 `report.md`가 열립니다. 사용하는 편집기는 시스템 설정에 따라 달라지며,
아래 예시에는 생성된 보고서의 내용이 나와 있습니다.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    생성된 Markdown 보고서에서 스캔 범위, 위협 모델, 검증된 보안 이슈 및 상세 보고서
링크를 검토하세요.
  </figcaption>
</figure>

반환된 아티팩트 경로를 사용하세요. 다른 도구에서 전체 스캔
컨텍스트가 필요하면 원본 `scan-manifest.json`, `findings.json` 및
`coverage.json` 파일을 함께 보관하세요. 내보내기는 보안 이슈를 코드 스캔
서비스에 업로드하지 않습니다.

## 선택한 보안 이슈 추적

`$codex-security:track-findings` 명령어를 실행할 때는 같은 봉인된 스캔의 검증된 보안 이슈 하나 또는
명시적으로 선택한 보안 이슈 최대 25개로 구성된 배치를 지정하세요. 한 번
실행할 때는 프로바이더 하나와 대상 하나를 사용합니다. 비공개 GitHub Security
Advisory 초안에는 보안 이슈를 하나만 포함할 수 있습니다.

Linear 이슈를 준비하려면 다음을 보내세요:

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for the Linear team [team] and project [project, if
any]. Check for duplicates and show me the exact issue title, body, metadata,
and destination. Do not create or update anything until I approve that payload.

GitHub 이슈를 준비하려면 다음을 보내세요:

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for GitHub repository [owner/repository]. Check open
and closed issues for duplicates and show me the exact issue title, body,
metadata, repository visibility, and authenticated transport. Do not create or
update anything until I approve that payload.

Jira 이슈를 준비하려면 다음을 보내세요:

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for Jira project [project key] as [issue type].
Check for duplicates and show me the exact issue summary, description,
metadata, and destination. Do not create or update anything until I approve
that payload.

Codex에서 Jira 추적을 사용하려면 Atlassian Rovo 플러그인이 필요합니다. 이슈를 재사용하려면
읽기 권한이 필요하고, 이슈를 만들거나 업데이트하려면 읽기 및 쓰기 권한이 필요합니다.

비공개 GitHub Security Advisory 초안을 준비하려면 다음을 보내세요:

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] as a private draft GitHub Security Advisory in
[owner/repository]. Verify the sealed source revision, repository, affected
paths, package metadata, and duplicate state. Show me the exact advisory
payload, authenticated GitHub CLI identity, and disclosure warnings. Do not
create anything until I approve that payload.

  보안 권고 초안을 만들려면 봉인된 `git_revision` 스캔의 보안 이슈 하나가 있어야 하고,
  소스 레포지토리는 검증된 공개 공식 레포지토리여야 하며 관리자 권한도 필요합니다. 이
  워크플로우는 보안 권고를 일괄 처리하거나 업데이트, 게시 또는 종료하지 않습니다. 소스가 이러한 요구 사항을 충족하지 않으면 승인된
  비공개 이슈 대상을 사용하세요.

## 제안된 쓰기 작업 검토

1. 보안 이슈 ID와 핑거프린트가 대상이었던 봉인된 스캔에서 나온 것인지 확인하세요.
2. 프로바이더와 정확한 대상(Linear 팀, GitHub 레포지토리, Jira 프로젝트 또는
보안 권고 레포지토리), 그리고 실제 대상의 공개 범위를 확인하세요.
3. 중복 확인 결과를 검토하세요: `create`, `reuse`, `update` 또는 `blocked`.
4. 제안된 제목, 본문, 소스 위치 및 프로바이더 메타데이터 전체를 확인하세요. 대상에
노출해서는 안 되는 익스플로잇 세부 정보나 내부 증거는
삭제하세요.
5. 해당 페이로드만 내용 그대로 승인하세요. 대상, 공개 범위, 보안 이슈 세트 또는 본문이
변경되면 새 미리보기가 필요합니다.

민감한 보안 이슈는 비공개 대상으로 보내야 합니다. 내부 또는 공개 GitHub 레포지토리에
이슈를 만들려면 공개 범위에 대한 명시적 경고와 전체 콘텐츠의
승인이 필요합니다. 보안 권고 초안의 설명은 결국 공개될 것으로 간주하고
승인하기 전에 자격 증명, 비공개 증거 및 불필요한 익스플로잇
세부 정보를 삭제하세요.

Codex 대화에서 외부 작업을 검토하고 승인하세요. 승인해도 보안 워크벤치에
별도의 이슈 또는 보안 권고 화면이 생성되지는 않습니다.

## 추적된 항목 확인

제안된 쓰기 작업을 승인하면 Codex가 봉인된 소스,
대상, 접근 권한 및 중복 상태를 다시 확인합니다. 배치의 경우 보안 이슈를
하나씩 처리하며 불확실한 결과가 처음 나오면 중단합니다. 생성, 업데이트 또는
재사용은 Codex가 바로 그 이슈를 다시 읽고 바인딩 식별자와
콘텐츠를 검증한 후에만 완료됩니다.

반환된 이슈 또는 보안 권고의 정식 URL을 트리아지 기록과 함께 보관하세요.
담당자가 해당 항목을 수정 대상으로 수락하면 [보안 이슈 수정 및 검증](/ko-KR/codex/security/plugin/fix-findings)을
진행하세요.

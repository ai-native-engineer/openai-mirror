<!-- source: https://learn.chatgpt.com/ko-KR/docs/security/plugin -->

Codex Security는 코드를 스캔해 취약점을 찾고, 실제 문제일 가능성이 있는
보안 이슈를 검증합니다. 보고 대상 이슈마다 결과 검토에 필요한 증거와
조치 지침을 제공합니다. 본인이 소유하거나 평가할 권한이 있는 코드만
스캔하세요.

이 빠른 시작 가이드에 따라 플러그인을 설치하고 Codex에서 로컬 레포지토리의
표준 읽기 전용 스캔을 실행하세요.

  이 페이지에서는 데스크톱 앱 또는 Codex CLI에서 사용하는 Codex Security 플러그인을 설명합니다.
  Codex 클라우드에서 연결된 GitHub 레포지토리를 스캔하려면 [Codex Security 클라우드
  설정](/ko-KR/codex/security/setup)을 참조하세요.

## 플러그인 설치

1. [ChatGPT 데스크톱 앱의 Codex](/ko-KR/codex/app)를 여세요.
2. **플러그인을** 열고 **Codex Security를** 검색하거나 아래 버튼을 사용하세요:

   <div className="not-prose my-6">
     
       Codex Security 플러그인 설치
     
   </div>

3. 플러그인이 활성화되어 있는지 확인한 다음 사이드바에서 **보안을** 여세요.

1. 터미널에서 평가하려는 레포지토리로 이동해 Codex를 시작하세요:

   ```bash
   codex

2. `/plugins` 명령어를 입력하고 **Codex Security를** 검색한 다음 **플러그인
   설치를** 선택하세요.
3. 해당 레포지토리의 새 채팅을 시작하려면 `/new`를 입력하세요.

로컬 레포지토리용 Codex Security를 설치하려면 ChatGPT 데스크톱 앱
또는 Codex CLI를 사용하세요.

  특정 기능을 활용하거나 장시간 실행되는 스캔을 시작하기 전에
  [플러그인 변경 로그](/ko-KR/codex/security/plugin/changelog)를 확인하세요. 데스크톱 앱 사이드바에
   **보안이** 표시되지 않으면 앱과 플러그인을 업데이트하고
  플러그인이 활성화되어 있는지 확인하세요.

## 첫 번째 스캔 실행

최상의 스캔 품질을 위해 <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code> 모델을 사용하고
추론 수준은 `xhigh`로 설정하세요.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    레포지토리를 선택하고 새 보안 스캔을 구성한 다음 시작하세요.
  </figcaption>
</figure>

1. 스캔 설정 열기

   사이드바에서 **보안을** 선택하고 **스캔을** 연 다음 **+ 스캔을** 선택하세요.

2. 코드베이스와 스캔 범위 선택

   기존 레포지토리를 선택하거나 다른 폴더를 사용하세요. **코드베이스를** 선택하고
    **심층 스캔은** 꺼 둔 상태로 레포지토리 전체나 폴더 하나를 선택하세요.
   브랜치와 리비전이 스캔하려는 코드를 가리키는지 확인하세요.

3. 관련 컨텍스트 추가

   모델과 추론 수준을 선택하세요. 검토에 참고할 특정 공격 벡터,
   보안상 민감한 영역 또는 레포지토리 세부 정보를 설명해야 할 때만
    **추가 컨텍스트를** 여세요.

   <figure className="not-prose my-6">
     
     <figcaption className="mt-3 text-sm text-secondary">
       추가 컨텍스트를 켜서 공격 벡터, 중점 영역, 관련
보안 지침을 설명하세요.
     </figcaption>
   </figure>

4. 스캔 시작

   **스캔 시작을** 선택하고 보안 워크벤치에서 스캔 단계별 진행 상황을 확인하세요.
   스캔을 수행하는 Codex 작업을 살펴보려면 **활동 보기를** 선택하세요.

5. 결과 검토

   완료된 스캔을 열어 보안 이슈, 커버리지, 사용 가능한 보고서 산출물을 확인하세요.
    **보안 이슈에서** 여러 스캔의 이슈를 검토하거나
    **레포지토리에서** 레포지토리의 스캔 기록을 확인하세요.

   <figure className="not-prose my-6">
     
     <figcaption className="mt-3 text-sm text-secondary">
       보안 워크벤치에서 스캔 결과, 보안 이슈, 커버리지를 검토하세요.
     </figcaption>
   </figure>

1. 표준 스캔 요청

   새 채팅에서 다음 프롬프트를 보내세요:

   ```text
   Run a Codex Security scan on this repository.

2. 스캔 완료 대기

   Codex는 설정 워크스페이스를 열지 않고 터미널에서 스캔을 실행합니다. Codex가
완료를 알릴 때까지 작업을 계속 실행하세요. Codex가 구성상의 제한을 발견하면
구성 업데이트를 승인하기 전에 해당 제한과 제안된 변경 사항의
정확한 내용을 검토하세요.

3. 결과 검토

   터미널에서 요약을 검토한 다음 생성된 `report.md`를 열어
   전체 결과를 확인하세요.

이 로컬 플러그인 워크플로우는 ChatGPT 데스크톱 앱 또는 Codex CLI에서 실행하세요.

## 스캔으로 생성되는 항목

완료된 스캔은 **스캔에서** 계속 확인할 수 있습니다.
보안 워크벤치에서 보안 이슈와 커버리지를 검토하거나
 **보안 이슈** 및 **레포지토리에서** 관련 이슈와 레포지토리 기록을 확인하세요.
스캔하면 아래 파일도 생성됩니다.

스캔이 완료될 때마다 터미널에 요약이 표시되고
아래 파일이 생성됩니다.

이 로컬 플러그인 워크플로우는 ChatGPT 데스크톱 앱 또는 Codex CLI에서 실행하세요.

- `report.md`: 스캔 결과를 읽고 확인하는 기본 문서입니다.
- `findings/<slug>/`: 상세한 취약점 보고서와 이를 뒷받침하는
  개념 증명 파일이 있을 때 생성됩니다.
- `hardening/`: 구조적 보안 강화 지침과 이를 뒷받침하는 제안 또는
  다이어그램이 있을 때 생성됩니다.
- 자동화 및 통합을 위한 구조화된 스캔 데이터가 `scan-manifest.json`, `findings.json`,
`coverage.json`에 저장됩니다. 이 파일을 열지 않고도
  스캔 결과를 검토할 수 있습니다.

결과를 공유하거나 보관할 때는 `report.md`의 링크가 계속 작동하도록
스캔 디렉터리 전체를 함께 유지하세요.

## 다음 워크플로우 선택

- [보안 워크벤치 사용](/ko-KR/codex/security/plugin/workbench): 데스크톱 앱에서 저장된 스캔, 보안 이슈,
  레포지토리 및 스캔 활동을 관리하세요.
- [CLI에서 스캔 실행](/ko-KR/codex/security/cli): 베타 액세스 권한이 있고 구조화된 결과를 제공하는
  반복 가능한 터미널 워크플로우가 필요할 때 사용하세요.
- [표준 스캔 또는 범위 지정 스캔 실행](/ko-KR/codex/security/plugin/scans): 기본 워크플로우로
  레포지토리나 폴더 하나를 검토하세요.
- [첫 번째 스캔 평가](/ko-KR/codex/security/plugin/scans#assess-a-first-scan): 결과를 알려진 이슈와 비교하고
  다시 스캔할 시점을 결정하세요.
- [심층 스캔 실행](/ko-KR/codex/security/plugin/deep-scans): 실행 시간을 더 길게 확보할 수 있을 때
  더 철저하게 스캔하세요.
- [코드 변경 사항 검토](/ko-KR/codex/security/plugin/code-changes): Pull Request, 커밋, 브랜치 범위 또는
  작업 트리 패치를 평가하세요.
- [백로그 트리아지하기](/ko-KR/codex/security/plugin/triage-backlog):
  기존 보안 이슈를 검토하세요.
- [보안 이슈 수정 및 검증](/ko-KR/codex/security/plugin/fix-findings): 보안 이슈 하나를 조치하기로 결정한 후
  해당 이슈를 수정하고 검증하세요.
- [보안 이슈 내보내기 또는 추적](/ko-KR/codex/security/plugin/export-findings): JSON, CSV, SARIF, 승인이 필요한
  Linear, GitHub 또는 Jira 이슈나 비공개
  GitHub Security Advisory 초안을 생성하세요.
- [취약점 보고서 작성](/ko-KR/codex/security/plugin/vulnerability-reports): 제공된 보안 이슈, 공개 관련 메모,
  소스 및 PoCs를 바탕으로
  그 자체로 완결된 보고서를 작성하세요.
- [보안 강화 방안 제안](/ko-KR/codex/security/plugin/security-hardening): 스캔 결과나 기타
  보안 증거를 바탕으로 구조적 또는 아키텍처 차원의
  방안을 검토하세요.

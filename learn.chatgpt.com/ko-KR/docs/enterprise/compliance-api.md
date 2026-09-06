<!-- source: https://learn.chatgpt.com/ko-KR/docs/enterprise/compliance-api -->

감사 가능한 기록이 필요한 보안, 법무, 거버넌스 및 조사
워크플로우에는 Compliance API를 사용하세요. 도입 현황과 추세는 컴플라이언스 기록이 아닌
분석 기능으로 측정하세요.

[Admin API 레퍼런스](https://chatgpt.com/public/admin/api-reference)는
현재 액세스 요구 사항, 이벤트 지원 범위, 라우트,
스키마, 필터, 보존 및 요청 처리 방식에 관한 기준 문서입니다.

사용 가능한 컴플라이언스 기능과 일반적인 통합 패턴을 살펴보려면
[컴플라이언스 플랫폼 가이드](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers)를 참조하세요.

## Compliance API를 사용하는 경우

다음과 같은 경우에 Compliance API가 적합합니다:

- 지원되는 기록을 감사 또는 조사 시스템으로 내보내야 하는 경우.
- 조직의 보존 및 법적 보존 절차를 적용해야 하는 경우.
- Codex 활동을 다른 보안 또는 신원 데이터와 연계해야 하는 경우.
- 승인된 보안, 법무 또는 거버넌스 조사를 지원해야 하는 경우.

Compliance API는 생산성 대시보드가 아닙니다. 코드 품질이나
개인별 성과를 추정하는 데 사용하지 마세요. 도입 현황 보고에는 [워크스페이스 분석](/ko-KR/codex/enterprise/workspace-analytics)
또는 [Analytics API](/ko-KR/codex/enterprise/analytics-api)를 사용하세요.

## 시작하기

1. [Admin API 레퍼런스](https://chatgpt.com/public/admin/api-reference)를 열고
   관리자 역할로 필요한 컴플라이언스 리소스에
   액세스할 수 있는지 확인하세요.
2. 지속적으로 수집하려면 추가만 가능한 컴플라이언스 로그 스트림을 사용하세요.
현재 지원되는 리소스와 조회 방식은
API 레퍼런스에서 확인하세요.
3. [로그 파일을 다운로드](#download-logs)하고 비프로덕션 환경의
   보안 정보 및 이벤트 관리(SIEM) 시스템이나 데이터 레이크로 수집하는 과정을 테스트하세요.
4. 지속적인 수집 일정을 설정하고 내보낸 기록에 조직의 액세스,
보존 및 법적 보존 통제를 적용하세요. 소스 시스템의 보존 기간이
조직의 보존 정책을 대체한다고 가정하지 마세요.

예를 들어 보안 팀은 조사를 위해 변경 불가능한 컴플라이언스 이벤트를
자체 SIEM으로 스트리밍하거나, 해당 이벤트를 승인된 전자증거개시
워크플로우로 전달할 수 있습니다. 이 가이드의 엔드포인트 명세를 복사해 사용하지 말고, 현재 라우트와
스키마는 API 레퍼런스에서 확인하세요.

### 로그 다운로드

[Bash 스크립트](/downloads/compliance-api/download_compliance_files.sh) 또는
[PowerShell 스크립트](/downloads/compliance-api/download_compliance_files.ps1)를 다운로드하세요.
두 스크립트 모두 지정된 타임스탬프 이후의 사용 가능한 모든 로그 파일을 페이지네이션에 따라 나열하고 다운로드하며,
JSONL을 표준 출력에 기록합니다. 오류는 표준 오류로 출력합니다.

`COMPLIANCE_API_KEY`를 엔터프라이즈 Compliance API 키로 설정하세요.
`<workspace_or_org_id>`는 ChatGPT 워크스페이스 ID 또는 API 플랫폼 조직 ID로 바꾸고,
`<after>`는 시간대가 포함된 ISO 8601 타임스탬프로 바꾸세요.
이 예제는 `AUTH_LOG` 파일을 한 번에 100개씩 가져옵니다.

macOS 또는 Linux에서 Bash, `curl`, `jq`를 설치한 다음 아래 명령어를 실행하세요:

```bash
bash ./download_compliance_files.sh "<workspace_or_org_id>" AUTH_LOG 100 "<after>" > output.jsonl

Windows용 스크립트는 PowerShell 5.1 이상을 지원합니다. 다운로드한 파일을 검토하세요.
Windows에서 파일을 차단하고 조직의 실행 정책이 차단 해제를 허용하는 경우,
`Unblock-File -Path .\download_compliance_files.ps1`을 실행하세요. 이 예제에서는
PowerShell 7을 사용해 바이트 순서 표시 없이 UTF-8로 저장합니다:

```powershell
.\download_compliance_files.ps1 "<workspace_or_org_id>" AUTH_LOG 100 "<after>" |
  Set-Content -Encoding utf8NoBOM output.jsonl

## 관리 범위 확인

컴플라이언스 적용 범위는 ChatGPT 워크스페이스와 현재 API 레퍼런스에 명시된
제품을 기준으로 합니다. Platform API 조직 데이터에는
별도의 API 데이터 및 관리 통제가 적용됩니다.

현재 라우트, 이벤트 지원 범위, 스키마,
필터, 보존 방식, 권한 요구 사항 및 요청 처리 방식에 관한 기준 문서는 API 레퍼런스입니다.
이 페이지에서는 해당 명세를 중복해서 제공하지 않습니다.

## 관련 문서

- [워크스페이스 분석](/ko-KR/codex/enterprise/workspace-analytics)
- [관리자용 도입 가이드](/ko-KR/codex/enterprise/admin-setup)
- [거버넌스](/ko-KR/codex/enterprise/governance)
- [Analytics API](/ko-KR/codex/enterprise/analytics-api)

<!-- source: https://learn.chatgpt.com/ko-KR/docs/security -->

Codex Security는 보안 및 엔지니어링 팀이 취약점을 찾아 확인하고
수정할 수 있도록 지원하는 애플리케이션 보안 에이전트입니다. Codex, 터미널,
TypeScript SDK 또는 연결된 GitHub
레포지토리에서 사용할 수 있습니다.

권장 절차에 따라 첫 로컬 스캔을 실행하려면 [Codex Security 플러그인
빠른 시작](/ko-KR/codex/security/plugin)부터 시작하세요.

## 데스크톱 앱에서 Codex Security 사용

ChatGPT 데스크톱 앱에서 ChatGPT 드롭다운을 열고 **Codex를** 선택하세요.
Codex Security 플러그인을 설치하고 활성화한 다음 사이드바에서 **보안을** 
여세요. 보안 워크벤치에서 스캔, 보안 이슈, 레포지토리를 한곳에서
관리할 수 있으며, Codex는 각 스캔을 작업으로 실행합니다.

- **스캔에서** 새 스캔을 시작하고 진행 상황을 추적하며 저장된 결과를 검토하세요.
- **보안 이슈에서** 완료된 스캔 전반의 보안 이슈와 증거를 살펴보세요.
- **레포지토리에서** 레포지토리 기록과 미해결 보안 이슈를 검토하세요.

데스크톱 앱의 전체 워크플로우는 [보안 워크벤치 사용](/ko-KR/codex/security/plugin/workbench)에서
확인하세요.

### 플러그인 사용 사례 살펴보기

- 레포지토리 또는 범위를 지정한 단일 폴더를 대상으로 [보안 스캔을 실행하세요](/ko-KR/codex/security/plugin/scans).
- 더 광범위한 검토가 필요하고 완료까지 더 오래 기다릴 수 있다면 [심층 보안 스캔을 실행하세요](/ko-KR/codex/security/plugin/deep-scans).
- Pull Request 또는 브랜치를 병합하기 전에 [코드 변경 사항을 검토하세요](/ko-KR/codex/security/plugin/code-changes).
- 검토할 기존 보안 이슈가 있다면 [백로그 트리아지하기](/ko-KR/codex/security/plugin/triage-backlog) 절차를 따르세요.
- 승인된 보안 이슈에 범위가 제한된 패치를 적용해 [보안 이슈를 수정하고 검증하세요](/ko-KR/codex/security/plugin/fix-findings).
- 보안 이슈를 이식 가능한 아티팩트로 내보내거나 승인이 필요한 추적 대상에서 관리하려면 [보안 이슈 내보내기 또는 추적](/ko-KR/codex/security/plugin/export-findings)을 사용하세요.
- 제공된 보안 이슈, 공개 메모, 소스 코드, PoC를 바탕으로 [취약점 보고서를 작성하세요](/ko-KR/codex/security/plugin/vulnerability-reports).
- 스캔 결과나 기타 보안 증거를 바탕으로 [보안 강화 방안을 제안하세요](/ko-KR/codex/security/plugin/security-hardening).
- Codex Security 플러그인의 최신 소식은 [새로운 기능 보기](/ko-KR/codex/security/plugin/changelog)에서 확인하세요.

  데스크톱 보안 워크벤치와 Codex CLI는 Codex Security 플러그인을 사용합니다.
  Codex Security 클라우드는 Codex 클라우드를 통해 연결된 GitHub 레포지토리를 스캔합니다.
  Codex의 샌드박스, 승인, 네트워크 제어, 관리자 설정에 관한 자세한 내용은
[에이전트 승인 및 보안](/ko-KR/codex/agent-approvals-security)을 참조하세요.

## Codex Security CLI 및 SDK

CLI와 TypeScript SDK는 공개
[`@openai/codex-security`](https://github.com/openai/codex-security) 패키지로 제공됩니다.
CLI는 `npx`로 실행하세요:

```bash
npx @openai/codex-security --help

스캔을 실행하려면 Codex Security 사용 권한이 필요합니다. 최상의 결과를 얻으려면
[Trusted Access for Cyber](https://chatgpt.com/cyber) 인증을 받은 계정을 사용하세요.

여러 레포지토리에서 장기간에 걸쳐 플러그인과 동일한 스캐너를 사용하세요. CLI는
GitHub 레포지토리를 탐색하고 대량 스캔을 재개하며, 여러 스캔의 보안 이슈를 추적하고
오탐 피드백을 기록합니다. 아키텍처와 보안
정책을 추가하거나, 예상 비용 한도를 설정하거나, CI와 커밋 전에 검사를 실행할 수 있습니다.
TypeScript SDK를 사용하면 스캔, 진행 상황 보고, 비용 제어 기능을
애플리케이션이나 개발자 도구에 통합할 수 있습니다.

- [CLI 빠른 시작](/ko-KR/codex/security/cli)에 따라 CLI를 설정하고,
  레포지토리 사전 점검을 수행한 후 로컬 스캔을 실행하세요.
- GitHub
  레포지토리를 탐색하거나 CSV 인벤토리를 바탕으로 재개 가능한 캠페인을 실행하려면 [대량 보안 스캔을 실행하세요](/ko-KR/codex/security/cli/bulk-scans).
- Pull Request 변경 사항을 검토하고, 아티팩트를 보존하고, SARIF를 업로드하고, 심각도 정책을 설정하려면
  [CI에서 스캔을 실행하세요](/ko-KR/codex/security/cli/ci).
- 스캔 기록, 오탐 피드백, 검사 범위, 수정 검증에 관한 답변은
  [CLI 관련 자주 묻는 질문](/ko-KR/codex/security/cli/faq)에서 확인하세요.
- [CLI 참조 자료](/ko-KR/codex/security/cli/reference)에서 지원되는
  명령어, 플래그, 출력 형식, 아티팩트, 종료 코드를 확인하세요.
- 코드에서 대상을 선택하고, 결과를 살펴보고, 진행 상황을 추적하고, 스캔을 취소하려면
  [TypeScript SDK를 통합하세요](/ko-KR/codex/security/sdk).

## Codex Security 클라우드

Codex Security 클라우드는 현재 연구 프리뷰 단계입니다. 연결된
GitHub 레포지토리를 스캔하여 잠재적인 보안 이슈를 찾습니다.

팀에서 다음 작업을 수행할 수 있도록 지원합니다:

1. 레포지토리별 위협 모델과 실제 코드 컨텍스트를 사용하여 **잠재적 취약점을 찾습니다** .
2. 검토 전에 보안 이슈를 검증하여 **노이즈를 줄입니다** .
3. 우선순위가 매겨진 결과, 증거, 제안된 패치 옵션을 제공하여 **보안 이슈가 수정으로 이어지도록 합니다** .

## Codex Security 클라우드 작동 방식

Codex Security는 연결된 레포지토리를 커밋별로 스캔합니다.
레포지토리에서 스캔 컨텍스트를 구성하고, 해당 컨텍스트를 바탕으로 잠재적 취약점을 확인한 다음, 신뢰도가 높은 보안 이슈를 격리된 환경에서 검증한 후 결과로 제시합니다.

이 워크플로우는 다음에 중점을 둡니다:

- 일반적인 시그니처가 아닌 레포지토리별 컨텍스트
- 오탐을 줄이는 데 도움이 되는 검증 증거
- GitHub에서 검토할 수 있는 제안된 수정 사항

## Codex Security 클라우드 이용 권한 및 사전 요구 사항

Codex Security 클라우드는 Codex 클라우드를 통해 연결된 GitHub 레포지토리와
연동됩니다. 레포지토리가 표시되지 않으면 Codex 클라우드 워크스페이스에서 해당 레포지토리를
사용할 수 있는지 확인하거나 OpenAI 계정 담당 팀에 문의하세요.

## 관련 문서

- [Codex Security 플러그인 빠른 시작](/ko-KR/codex/security/plugin)에서는 설치와 첫 로컬 스캔 과정을 단계별로 안내합니다.
- [보안 워크벤치](/ko-KR/codex/security/plugin/workbench)에서는 데스크톱 앱의 저장된 스캔, 보안 이슈, 레포지토리, 스캔 활동을 설명합니다.
- [Codex Security CLI 빠른 시작](/ko-KR/codex/security/cli)에서는 설정, 사전 점검, 첫 터미널 스캔 과정을 단계별로 안내합니다.
- [대량 보안 스캔 실행](/ko-KR/codex/security/cli/bulk-scans)에서는 GitHub 레포지토리 탐색, CSV 인벤토리, 캠페인 결과, 재개 방식을 설명합니다.
- [Codex Security CLI 관련 자주 묻는 질문](/ko-KR/codex/security/cli/faq)에서는 스캔, 보안 이슈, 검사 범위, 비용에 관한 일반적인 질문에 답합니다.
- [Codex Security TypeScript SDK](/ko-KR/codex/security/sdk)에서는 애플리케이션이나 개발자 도구에서 스캔을 실행하는 방법을 설명합니다.
- [Codex Security 클라우드 설정](/ko-KR/codex/security/setup)에서는 설정, 스캔, 보안 이슈 검토를 자세히 설명합니다.
- [보안 검토](/ko-KR/codex/security/security-review)에서는 GitHub Pull Request에 대한 심층 보안 검토를 실행하는 방법을 설명합니다.
- [위협 모델 개선](/ko-KR/codex/security/threat-model)에서는 범위, 진입점, 중요도 가정을 조정하는 방법을 설명합니다.
- [Codex Security 클라우드 관련 자주 묻는 질문](/ko-KR/codex/security/faq)에서는 클라우드 제품에 관한 일반적인 질문을 다룹니다.

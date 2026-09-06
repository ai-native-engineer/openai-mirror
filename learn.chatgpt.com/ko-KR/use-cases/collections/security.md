<!-- source: https://learn.chatgpt.com/ko-KR/use-cases/collections/security -->

# 보안

Codex는 엔지니어링 및 보안 팀이 승인된 코드를 평가하고 증거를
수집해, 검토된 보안 이슈를 필요한 범위에서 수정할 수 있도록 지원합니다. 다음 사용 사례에서는
레포지토리 스캔, 변경 사항 검토, 종속성 사고, 취약점
해결을 다룹니다.

## 레포지토리 평가

Codex Security 플러그인을 사용해 승인된
레포지토리 전체를 종합적으로 스캔하고, 잠재적인 보안 이슈를 검토하며, 사람의
분류 작업을 지원하는 보고서를 생성하세요. 종합 스캔은 여러 독립된
워커가 탐색을 반복하므로 시간이 더 오래 걸립니다.

## 병합 전 변경 사항 검토

Codex에 Pull Request, 브랜치, 커밋 또는 작업 트리 diff에서
보안 회귀가 발생했는지 검사하고 변경된 코드와 연결된 증거를 제시하도록 요청하세요.

## 종속성 사고 감사

공개 패키지 또는 공급망 관련 권고를 바탕으로 매니페스트, 잠금 파일, 스크립트,
워크플로우, 노출 경로를 포괄하는 읽기 전용 레포지토리 감사를 수행하세요.

## 검토된 보안 이슈 해결

보안 보고서, 권고 또는 티켓에 있는 승인된 보안 이슈를 Codex에 전달한 후,
최소한의 수정만 적용하고 취약한 동작이 더 이상 재현되지 않는지
검증하도록 하세요.

- [심층 보안 스캔 실행](/ko-KR/use-cases/deep-security-scan)

- [코드 변경 사항 보안 스캔](/ko-KR/use-cases/scan-code-changes-for-security)

- [종속성 인시던트 감사하기](/ko-KR/use-cases/dependency-incident-audits)

- [취약점 백로그 해결](/ko-KR/use-cases/remediate-vulnerability-backlog)

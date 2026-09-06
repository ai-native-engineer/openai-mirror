<!-- source: https://learn.chatgpt.com/ko-KR/docs/security/plugin/security-hardening -->

`$codex-security:propose-security-hardening`을 사용해 수집한 보안 증거를
구조적 또는 아키텍처 차원의 보안 강화 방안으로 구체화하세요.
이 워크플로우는 완료된 Codex Security 스캔을 분석하거나, 제공된
보안 이슈, 공개 보고서, 인시던트 검토 자료, 평가 문서 및
소스 코드를 바탕으로 분석을 시작할 수 있습니다.

결과물은 패치가 아니라 설계 포트폴리오이며, 취약점이 해결됨을
입증하지는 않습니다. Codex는 사용자가 방안을 선택하고 해당 변경을 수행하도록 명시적으로
요청한 후에만 레포지토리를 변경합니다.

## 증거 준비

워크플로우에 다음을 제공하세요:

- 스캔 디렉터리 또는 명시적으로 지정한 보안 이슈 및 보고서 모음.
- 가능한 경우 대상 소스 트리와 관련 리비전 또는 스냅샷.
- 보안 이슈를 뒷받침하는 PoCs, 트레이스, 인시던트 증거 또는 평가
자료.
- 성능, 메모리, 호환성, 안정성, 운영, 제공 일정 또는 변경 범위에 대한
제약 조건.

워크플로우는 증거를 사용해 반복적으로 위반되는 불변 조건, 분산된
제어 수단, 권한이 집중되는 병목 지점, 취약한 격리 경계, 반복되는
보완 패턴을 식별합니다. 또한 아키텍처 변경보다 국소적인 수정이 더
적절하다는 결론을 내릴 수도 있습니다.

## 워크플로우 실행

다음과 같은 프롬프트를 보내세요:

```text
Use $codex-security:propose-security-hardening to analyze [scan directory or finding paths] against [source tree and revision]. Develop evidence-backed structural hardening options with engineering tradeoffs, before-and-after diagrams, a migration plan, and an implementation handoff. Do not modify the repository.

## 포트폴리오 검토

유용한 포트폴리오는 다음 요건을 충족해야 합니다:

- 각 변경 제안을 구체적인 보안 이슈, 소스 코드 및 위협 모델의
근거와 연결해야 합니다.
- 현재 설계와 새 설계가 유지해야 할 보안 불변 조건을
설명해야 합니다.
- 잔여 리스크, 성능,
안정성, 운영, 호환성, 마이그레이션 비용을 고려해 서로 다른 방안을 비교해야 합니다.
- 증거가 뒷받침하는 경우에만 방안을 추천하고, 가정과 미해결 질문을 명확히
밝혀야 합니다.
- 롤아웃, 검증, 롤백 및 구현에 관한 지침을 포함해야 합니다.
- 관찰된 사실, 추론, 제안된 설계 속성을 구분해야 합니다.

방안을 선택하기 전에 증거와 장단점을 검토하세요. 아키텍처
다이어그램이나 설계 권고안은 기존에 발견된 보안 이슈 또는 구현된 수정 사항에 대한
검증을 대신할 수 없습니다.

## 스캔의 보안 강화 지침 활용

보고 대상 보안 이슈가 있는 표준, 심층 또는 변경 스캔에 대해
보안 강화 포트폴리오를 요청할 수 있습니다. Codex는 포트폴리오를 `hardening/hardening.md`에,
구조화된 분석을 `hardening/hardening.json`에 기록하고, 관련 제안이나
다이어그램을 `hardening/` 아래에 저장합니다. 스캔은 `report.md`에 포트폴리오 링크를 추가합니다.

해당 링크를 계속 사용할 수 있도록 전체 스캔 디렉터리를 그대로 보관하세요.
포트폴리오 작성의 근거가 된 개별 보고서를 검토하려면 [취약점
보고서 작성](/ko-KR/codex/security/plugin/vulnerability-reports)을 참고하세요.

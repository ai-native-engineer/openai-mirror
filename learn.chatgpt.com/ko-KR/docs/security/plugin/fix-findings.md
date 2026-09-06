<!-- source: https://learn.chatgpt.com/ko-KR/docs/security/plugin/fix-findings -->

Codex Security를 사용하면 수락된 보안 이슈를 해당 이슈에 집중한
검증된 패치로 수정할 수 있습니다. Codex Security 워크벤치에서 작업하거나 프롬프트,
명령줄 또는 CI/CD에서 수정 워크플로우를 실행할 수 있습니다. Codex는 이슈를 검증하고,
테스트를 안전하게 실행할 수 있고 현실적으로도 가능한 경우, 수정 전에는 실패하고 수정 후에는
통과하는 회귀 테스트를 추가합니다. 또한 정상 동작이 계속 유지되는지도 확인합니다.
회귀 테스트가 안전하지 않거나 실행할 수 없으면 Codex는 검증 근거가 부족한 부분을
기록하고, 대신 반복 실행 가능한 가장 강력한 검증 아티팩트를
제공합니다.

먼저 수락된 보안 이슈 하나를 선택해 제안된 패치와 검증 근거를 검토하세요.
워크플로우가 기준을 충족하면 수락된 다른 보안 이슈를 별도의 Codex 작업이나
CI/CD 잡에서 하나씩 처리하세요. 각 작업의 범위를 하나의 이슈로 제한하면 코드
변경과 검증 근거를 더 쉽게 검토할 수 있습니다.

## UI에서 보안 이슈 수정

**보안 이슈** 목록에서 수락된 보안 이슈를 열거나 **스캔** 목록에서 완료된 스캔을 여세요.
근거를 검토한 다음 **패치를** 사용해 하나의 보안 이슈에 집중한 수정 사항을 생성하고 검토한 후
적용하고 검증하세요.

1. 해당 이슈에 집중한 패치 생성

   보안 이슈를 열고 **패치** 탭을 선택한 다음 **패치 생성을** 선택하세요.
   가능하면 Codex가 이슈를 검증하거나 재현하고, 선택한 체크아웃을 수정하지 않은 채 패치
   아티팩트를 작성합니다.

2. 제안된 diff 검토

   변경된 모든 소스 코드, 회귀 테스트, 검증 아티팩트를 확인하세요. 광범위한
리팩터링, 무관한 정리 작업, 다른 보안 통제를 약화하는 변경은
거부하세요.

3. 로컬에 패치 적용

   diff에 문제가 없다고 판단한 후에만 **패치 적용을** 선택하세요. Codex는 생성된
   패치를 그대로 작업 트리에 적용하고 그 상태를 기록합니다. 계속하기 전에
   작업 트리의 diff를 검토하세요.

4. 수정 사항 검증

   **수정 사항 검증을** 선택하세요. Codex는 원래 재현 절차를 다시 실행하거나 사용할 수 있는 가장 강력한
   익스플로잇 검사를 수행합니다. 회귀 테스트를 안전하게 실행할 수 있고 현실적으로도 가능하면 Codex는
   수정 전에는 실패하고 수정 후에는 통과하는지 확인합니다. 테스트가
   안전하지 않거나 실행할 수 없으면 검증 근거가 부족한 부분을 기록하고, 대신
   반복 실행 가능한 가장 강력한 검증 아티팩트를 제공합니다. 또한
   정상 동작, 주변의 우회 경로, 관련 레포지토리 테스트도 확인합니다.

5. 보안 이슈를 신중하게 종료

   검증이 완료되어도 보안 이슈가 자동으로 종료되지는 않습니다. 명령, 결과,
아직 검증 근거가 부족한 부분을 검토한 다음 정확한 사유로 보안 이슈를
종료하거나, 추가 작업을 위해 열린 상태로 유지하세요.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    생성된 보안 수정 사항을 체크아웃에 적용하기 전에 검토하세요.
  </figcaption>
</figure>

## CLI에서 보안 이슈 수정

스캔, 티켓, 보안 권고, 공개 제보, 보안 평가 또는 내부 검토를 통해 수락된
보안 이슈에는 Codex CLI를 사용하세요.

다음 명령을 실행하기 전에 `codex exec`에서 사용하는 `CODEX_HOME`에 Codex Security를
설치하세요. 새 CI 러너에는 마켓플레이스 플러그인이 기본으로
포함되지 않습니다.

```text
Use $codex-security:fix-finding to fix finding <finding-id> from <report-path>. Validate the issue, make the smallest safe change, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.

알려진 소스, 싱크, 공격자 입력, 영향, 예상 불변 조건, 재현 절차,
영향받는 파일, 검증 명령어를 포함하세요. 누락된 기술 세부 사항은 Codex가
레포지토리를 검사해 확인할 수 있습니다. 제품 정책이나 의도된 보안 불변 조건을
가정하기 전에는 먼저 질문해야 합니다.

자동 실행에서는 코드를 체크아웃하고 보안 이슈 보고서를 사용할 수 있도록 준비한 다음,
러너의 `CODEX_HOME`에 플러그인을 설치하세요. 이어서 워크스페이스 쓰기 권한을
활성화하고 프롬프트를 `codex exec`에 전달하세요:

```bash
codex exec --sandbox workspace-write 'Use $codex-security:fix-finding to fix finding <finding-id> from <report-path>. Validate the issue, make the smallest safe change, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.'

## CI/CD에서 보안 이슈 스캔 및 수정

두 스킬 중 어느 것이든 호출하기 전에 러너의 `CODEX_HOME`에 Codex Security를
설치하세요. 아래 명령은 설치된 플러그인을 사용할 뿐, 플러그인을 설치하지는 않습니다.

CI/CD에서는 변경 사항 스캔과 수정 작업을 분리하고, 스캔이 체크아웃을
변경하지 않도록 하세요. 완료된 스캔 디렉터리는 잡 아티팩트로 보존하고
보안 이슈를 검토한 다음, 수정 대상으로 수락한 보안 이슈마다 별도의 Codex 작업이나
CI/CD 잡을 시작하세요.

기본적으로 `codex exec`은 읽기 전용 샌드박스를 사용합니다. 변경 사항 스캔과
수정 작업을 모두 `--sandbox workspace-write`로 실행하세요. 스캔에서 임시 아티팩트를
저장하려면 이 권한이 필요하지만, 프롬프트에는 여전히 `Do not modify
the checkout`라는 요구 사항을 명시해야 합니다. 수정 작업에서 해당 이슈에 집중한
패치와 검증 근거를 작성할 때도 같은 권한이 필요합니다. 자세한 내용은 [권한 및
안전](/ko-KR/codex/non-interactive-mode#permissions-and-safety)을 참고하세요.

각 스캔과 수락된 보안 이슈마다 다음을 수행하세요:

1. 변경 사항의 베이스 및 헤드 리비전을 확인하세요.
2. 체크아웃을 수정하지 않고 해당 diff를 대상으로 `$codex-security:security-diff-scan`을
   실행하세요.
3. 스캔 디렉터리 전체를 보존하고 수정할 보안 이슈를 선택하세요.
4. 수락된 보안 이슈마다 `$codex-security:fix-finding`을 한 번씩 호출하고 보안 이슈 ID와
   완료된 스캔 디렉터리를 전달하세요.
5. 하나의 보안 이슈에 집중한 패치를 생성하고, 수정 전에는 실패하고 수정 후에는
통과하는 회귀 테스트를 추가하세요. 이 테스트가 안전하지 않거나 실행할 수 없다면
검증 근거가 부족한 부분을 기록하고, 대신 반복 실행 가능한 가장 강력한 검증
아티팩트를 사용하세요.
6. 원래 이슈와 정상 동작을 검증하세요. 각 패치, 테스트 또는 대체 검증
아티팩트, 검증 명령어, 검증 근거가 부족한 부분을 각각 독립적으로
반환하세요.

먼저 체크아웃을 수정하지 않고 변경 사항을 스캔하세요:

```bash
codex exec --sandbox workspace-write 'Use $codex-security:security-diff-scan to review changes from <base-revision> to <head-revision> for security regressions. Do not modify the checkout.'

그런 다음 완료된 스캔에서 수락된 보안 이슈 하나를 수정하세요:

```bash
codex exec --sandbox workspace-write 'Use $codex-security:fix-finding to fix finding <finding-id> from <completed-scan-directory>. Validate the finding, generate one minimal patch, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.'

남아 있는 수락된 보안 이슈마다 두 번째 명령어를 별도의 작업 또는 잡에서
반복 실행하세요. 검증 후에는 일반적인 코드 검토 및 릴리스 프로세스를 통해 각 패치를
병합하세요. 수정하기 전에 보안 이슈를 다른 팀에 전달하려면
[보안 이슈 내보내기 또는
추적](/ko-KR/codex/security/plugin/export-findings)을 참고하세요.

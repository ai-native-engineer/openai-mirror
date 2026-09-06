<!-- source: https://learn.chatgpt.com/ko-KR/docs/sandboxing/auto-review -->

자동 검토는 샌드박스 경계에서 수동 승인을 별도의
검토 에이전트로 대체합니다. 메인 Codex 에이전트는 동일한 샌드박스 내에서
동일한 승인 정책과 네트워크 및 파일 시스템 제한을 그대로 적용받으며 실행됩니다.
달라지는 것은 검토 대상 권한 상승 요청을 누가 검토하느냐뿐입니다.

  자동 검토는 승인이 대화형일 때만 적용됩니다. 실제로는
  `approval_policy = "on-request"` 또는 관련 프롬프트 범주를 계속 표시하는 세분화된 승인 정책이어야
  합니다. `approval_policy = "never"`인 경우
  검토할 항목이 없습니다.

ChatGPT 데스크톱 앱에서 승인된 Daybreak 모델을 선택하면
해당 모드를 계정에서 사용할 수 있고 조직 정책에서 허용하는 경우 권한 제어가
**대신 승인으로** 자동 전환됩니다. 데스크톱 앱의 `/model` 명령어를 사용할 때도
동일하게 적용됩니다. 해당 모드를 사용할 수 없으면 현재 권한 모드는
그대로 유지됩니다. 모델을 선택해도 조직의 관리형 요구 사항이
재정의되지는 않습니다.

승인된 보안 모델에 **전체 권한을** 사용 설정하기 전에
ChatGPT 데스크톱 앱은 위험한 작업에 대한 모델별 경고를 표시합니다.
이 경고는 **대신 승인을** 권장하고
[검토자 정책 구성](#configuration)으로 연결됩니다. 이 경고가
샌드박스 경계를 복원하거나 조직 정책을 재정의하는 것은 아닙니다.

## 자동 검토 작동 방식

전체적인 플로우는 다음과 같습니다:

1. 메인 에이전트는 `read-only` 또는 `workspace-write` 내에서 작업합니다.
2. 샌드박스 경계를 넘어야 할 때 승인을 요청합니다.
3. `approvals_reviewer = "auto_review"`이면 Codex는 사람의 처리를 기다리며 중단하는 대신
   해당 승인 요청을 별도의 검토 에이전트로 라우팅합니다.
4. 검토 에이전트는 해당 작업을 실행할지 결정하고 근거를 반환합니다.
5. 작업이 승인되면 실행을 계속합니다. 거부되면 메인
에이전트에 실질적으로 더 안전한 경로를 찾거나 중단하고
사용자에게 문의하라는 지시가 내려집니다.

자동 검토는 검토 주체만 바꿀 뿐 권한을 부여하지 않습니다. 이는
`writable_roots`의 범위를 확장하거나 네트워크 접근을 사용 설정하거나 보호된 경로에 대한 보호를 약화하지 않습니다.
Codex가 이미 승인이 필요한 작업을 처리하는 방식만 변경합니다.

## 실행 조건

자동 검토는 원래라면 사람의 처리를 기다리며 일시 중지되는 승인 요청을 평가합니다.
여기에는 다음이 포함됩니다:

- 샌드박스 권한 상승을 요청하는 셸 또는 exec 도구 호출.
- 현재 샌드박스 또는 정책에 의해 차단된 네트워크 요청.
- 허용된 쓰기 가능 루트 외부의 파일 편집.
- 도구 주석 또는 구성된 승인 모드에 따라 승인이 필요한 MCP 또는 앱 도구
호출.
- 컴퓨터 사용을 통한 새 웹사이트 또는 도메인 접근.

자동 검토는 샌드박스 내에서 이미 허용된 일반 작업에는 실행되지 않습니다.
활성 `sandbox_mode`에서 명령어를 실행할 수 있거나 도구 호출이
허용된 정책 범위 내에 있으면 메인 에이전트는 검토 없이 계속합니다.

컴퓨터 사용은 별도의 경우입니다. 컴퓨터 사용에 대한 App 승인은 여전히
사용자에게 직접 표시되므로 자동 검토가 이러한 App 수준 프롬프트를 대체하지 않습니다.

## 자동 검토가 차단하는 작업

전체적으로 자동 검토는 다음과 같은 작업을 차단하도록 설계되었습니다:

- 비공개 데이터, 비밀 정보 또는 자격 증명을 신뢰할 수 없는 대상으로 전송
- 자격 증명, 토큰, 쿠키 또는 세션 자료 탐색
- 광범위하거나 지속적인 보안 약화
- 되돌릴 수 없는 중대한 피해 위험이 있는 파괴적 작업

정확한 정책은 오픈 소스 Codex 레포지토리의 다음 파일에 있습니다:
[policy\_template.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy_template.md)
및
[policy.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md).
이 정책은 `guardian_policy_config`를 사용해 엔터프라이즈별로 맞춤 설정하거나
로컬 [`[auto_review].policy`](/ko-KR/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)를 사용해 사용자별로 맞춤 설정할 수 있습니다.

## 검토 에이전트에 표시되는 정보

검토 에이전트 자체도 Codex 에이전트지만 메인 에이전트보다 역할이 제한적입니다.
역할은 경계를 넘는 특정 작업을 실행할지 결정하는 것입니다.

검토 에이전트에는 간결한 대화 기록과 정확한 승인 요청이 표시됩니다. 여기에는
일반적으로 사용자 메시지, 표시된 어시스턴트 업데이트, 관련 도구
호출 및 도구 출력, 현재 승인을 요청하는 작업이 포함됩니다. 누락된 컨텍스트를
수집하기 위해 읽기 전용 검사를 수행할 수도 있지만 실제로는 거의 수행하지 않습니다.

숨겨진 어시스턴트 추론은 포함되지 않습니다. 자동 검토에는 보존된
채팅 항목과 도구 관련 증거만 표시되며 비공개 추론 과정은 표시되지 않습니다.

## 거부 및 실패 동작

명시적 거부는 일반적인 샌드박스 오류로 처리되지 않습니다. Codex는
검토 근거를 메인 에이전트에 반환하고 더 강력한 지시를 추가합니다:

- 우회 방법, 간접 실행 또는 정책 회피를 통해 동일한 결과를
얻으려고 하지 마세요.
- 실질적으로 더 안전한 대안이 있을 때만 계속하세요.
- 그렇지 않으면 중단하고 사용자에게 문의하세요.

Codex는 턴마다 거부 서킷 브레이커도 적용합니다. 현재
오픈 소스 구현에서 자동 검토는 같은 턴에 연속 거부가 `3`회에 도달하거나
최근 `50`회의 검토로 구성된 슬라이딩 윈도우에서 거부가 `10`회에 도달하면
해당 턴을 중단합니다.

거부가 아닌 결과가 나오면 연속 거부 카운터가 초기화됩니다. 서킷 브레이커가 작동하면
Codex는 에이전트가 추가 권한 상승 시도를 반복하지 않도록 경고를 표시하고,
인터럽트로 현재 턴을 중단합니다.

시간 초과는 명시적 거부와 별도로 표시되며, 시간 초과만으로 해당 작업이
안전하지 않다고 단정할 수 없다는 사실이 메인 에이전트에 전달됩니다.

거부된 작업을 명시적으로 재정의하는 경로도 있습니다. 현재
오픈 소스 TUI에서 `/approve`를 실행해 **자동 검토 거부** 선택기를 연 다음,
최근에 거부된 작업 하나를 선택하여 한 번 재시도하도록 승인합니다. Codex는 작업당 최근 거부를 최대 10건까지
기록합니다. 이 승인은 제한적으로 적용됩니다. 즉, 향후의 유사한 작업이 아니라 정확히
거부된 해당 작업에만 적용되고, 동일한 컨텍스트에서 한 번 재시도할 수 있도록
기록되며, 재시도 역시 자동 검토를 거칩니다. 내부적으로
Codex는 해당 작업과 정확히 일치하는 개발자 범위 승인 마커를 삽입합니다.
이후 검토 에이전트는 이러한 명시적인 사용자 재정의를 컨텍스트로 확인하지만
여전히 정책을 따르며, 정책상 사용자가 해당 유형의 거부를 재정의할 수 없으면
다시 거부할 수 있습니다.

## 구성

설정 세부 정보는
[관리형 구성](/ko-KR/codex/enterprise/managed-configuration#configure-automatic-review-policy)을 참조하세요.

기본 검토자 정책은 오픈 소스 Codex 레포지토리의 다음 파일에 있습니다:
[core/src/guardian/policy.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md).
엔터프라이즈는 관리형 요구 사항에서 테넌트별 섹션을
`guardian_policy_config`로 대체할 수 있습니다. 개별 사용자는 로컬
[`[auto_review].policy`](/ko-KR/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)를
`config.toml`에 설정할 수도 있지만
관리형 요구 사항이 우선합니다:

```toml
[auto_review]
policy = """
YOUR POLICY GOES HERE
"""

정책을 맞춤 설정하려면 먼저 기본 정책 문구 전체를 복사한 다음,
개별 위험 프로필에 맞춰 반복적으로 조정하세요.

## 승인된 사이버 보안 작업 구성

승인된 보안 작업에서는 자동 검토를 서면으로 명시된
작업 범위 및 최소 권한 원칙의 [권한 프로필](/ko-KR/codex/permissions)과 함께 사용하세요.
승인된 랩 대상을 사용하고 작업 내용과 수행 기간을 문서화하세요.
프로덕션 시스템, 관련 없는 호스트, 자격 증명 및 지속적 변경 사항은
명시적으로 승인되지 않는 한 범위에서 제외하세요.

`[auto_review].policy`와 `guardian_policy_config`는 모두 현재 검토자 정책을
대체합니다. 모델에 포함된 정책이나 조직에서 관리하는 정책과
병합되지 않습니다. 기본 제공 검토 지침과 응답
형식은 계속 적용됩니다. 두 예시 중 하나를 사용하기 전에 현재
정책 전체를 복사하고 기존 규칙을 모두 유지한 채 승인된 작업에 필요한 규칙을 추가하세요.
대문자 자리표시자를 이 전체 정책으로 바꾸세요. 현재 정책에
접근할 수 없다면 재정의하지 마세요.

다음 로컬 `config.toml` 템플릿은 검토를 사용 설정하고 기존 검토자 정책 뒤에
범위가 지정된 조건을 추가합니다:

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"
default_permissions = ":workspace"

[auto_review]
policy = """
PASTE THE COMPLETE ACTIVE REVIEWER POLICY HERE BEFORE USING THIS EXAMPLE.

## Environment Profile
- Authorized target: lab.example.com.
- Approved actions: inspect the target, reproduce authorized vulnerabilities,
  and validate fixes within the documented engagement window.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Allow only actions against the approved target that match the documented
  engagement scope and approved actions.
- Deny out-of-scope or unknown hosts, production access, credential theft,
  persistence, data exfiltration, destructive operations, and policy bypass.
- Deny ambiguous actions and high-impact changes until a human explicitly
  approves the exact target, action, and side effects.
"""

예시 대상과 허용된 작업을 실제 승인 범위로 바꾸세요.
독립적인 파일 시스템 및 네트워크 규칙으로 대상 제한을 적용하세요.
검토자 지침은 이러한 경계를 대체하지 않습니다.

조직은 관리형 `requirements.toml`에서 동일한 조건을 적용할 수 있습니다:

```toml
allowed_approval_policies = ["on-request"]
allowed_approvals_reviewers = ["auto_review"]
allowed_sandbox_modes = ["read-only", "workspace-write"]
default_permissions = ":workspace"

guardian_policy_config = """
PASTE THE COMPLETE ACTIVE REVIEWER POLICY HERE BEFORE USING THIS EXAMPLE.

## Environment Profile
- Authorized target: lab.example.com.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Allow only approved actions against the documented engagement target.
- Deny out-of-scope hosts, production access, credential theft, persistence,
  data exfiltration, destructive operations, and attempts to bypass policy.
- Deny ambiguous or high-impact actions until a human explicitly approves the
  exact target, action, and side effects.
"""

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
# ":danger-full-access" is omitted, so it is denied.

`allowed_permission_profiles`는 현재 권한 프로필을 제어합니다.
또한 `allowed_sandbox_modes`는 레거시 `sandbox_mode`를 계속 사용하는
배포 환경에서 전체 권한 사용을 차단합니다.

관리형 `guardian_policy_config`가 사용자의 로컬
`[auto_review].policy`보다 우선합니다. `approval_policy = "on-request"` 또는 다른 적용 가능한
대화형 승인 정책을 사용하고 강제 가능한 샌드박스 경계를 유지하세요.
`approval_policy = "never"`, `:danger-full-access` 또는 `--yolo`를 사용하면 작업이
검토에 필요한 경계 통과 승인 요청의 생성을 피할 수 있습니다.

허용 목록에 있는 네트워크 대상이라는 이유만으로 검토가 실행되지는 않습니다.
샌드박스 내부 작업도 검토 에이전트에 전달해야 한다면 `decision = "prompt"`가 지정된
명시적인 [명령어 규칙](/ko-KR/codex/agent-configuration/rules)을 추가하거나 민감한 MCP 도구에 승인을 요구하도록
구성하세요.

모델 접근 권한, 보안 작업 설정 및 맞춤형 에이전트 워크플로우는 [모델 및 신뢰할 수 있는 접근 권한](/ko-KR/codex/cyber-safety)과 [권장
구성](/ko-KR/codex/cyber-safety/recommended-configuration)을 참조하세요.
엔터프라이즈의 우선 적용 규칙 및 지원되는 클라이언트 버전은 [관리형 구성](/ko-KR/codex/enterprise/managed-configuration#configure-automatic-review-policy)을
참조하세요. 맞춤형 API 또는 Agents SDK 하네스에는
[가드레일 및 사람의 검토](/api/docs/guides/agents/guardrails-approvals#review-cybersecurity-actions-before-execution)를 사용하세요.

## 보안을 약화하지 않고 검토량 줄이기

샌드박스가 자주 사용하는 안전한 워크플로우를 이미 포괄할 때 자동 검토가 가장
효과적으로 작동합니다. 일반적인 작업까지 너무 많이 검토해야 한다면 불필요하게 발생하는
권한 상승 요청을 계속 승인하도록 검토 에이전트를 조정하지 말고 먼저 경계를 바로잡으세요.

실제로 가장 효과가 큰 변경 사항은 다음과 같습니다:

- 의도적으로 사용하는 스크래치 디렉터리나 인접 레포지토리에 대해 범위를 좁힌
[`writable_roots`](/ko-KR/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)를
  추가하세요.
- 범위가 좁은 [접두사 규칙](/ko-KR/codex/agent-configuration/rules)을 추가하세요. `["cargo", "test"]` 또는 `["pnpm", "run", "lint"]`처럼 정확한 명령어
  접두사를 `["python"]` 또는 `["curl"]`처럼 광범위한
  패턴보다 우선하여 사용하세요. 광범위한 규칙은 자동 검토가 보호하려는 바로 그
  경계를 없애는 경우가 많습니다.

자동 검토 세션 대화 기록은 기본적으로 `~/.codex/sessions` 아래에
보존됩니다. 따라서 정책이나 권한을 변경하기 전에 Codex에 해당 위치의 과거 트래픽을
분석해 달라고 요청할 수 있습니다.

## 제한 사항

자동 검토는 장시간 실행되는 에이전트 기반 작업의 기본 운영 기준을 개선하지만,
결정론적인 보안 보장을 제공하지는 않습니다.

- 경계를 넘기 위해 승인을 요청하는 작업만 평가합니다.
- 특히 적대적이거나 이례적인 상황에서는 여전히 판단을 잘못할 수 있습니다.
- 효과적인 샌드박스 설계와 모니터링,
조직별 정책을 대체하지 않고 보완해야 합니다.

연구의 이론적 근거와 공개된 평가 결과는
[자동 검토에 관한 Alignment Research 게시물](https://alignment.openai.com/auto-review/)을 참조하세요.

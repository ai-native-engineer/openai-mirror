<!-- source: https://learn.chatgpt.com/ko-KR/docs/agent-configuration/subagents -->

ChatGPT Work와 Codex는 특화된 에이전트를 병렬로 생성하고 결과를 하나의 응답으로 모으는 하위 에이전트 워크플로우를 실행할 수 있습니다. 코드베이스 탐색이나 여러 단계로 구성된 기능 구현 계획을 실행하는 등 병렬 처리에 적합한 복잡한 작업에 특히 유용합니다.

로컬 Codex 클라이언트에서는 작업에 따라 모델 구성과 지침이 서로 다른 커스텀 에이전트를 정의할 수도 있습니다.

## 이용 가능 여부

이용 자격이 있는 계정에서는 ChatGPT Work의 하위 에이전트 워크플로우를 사용하고 관련 활동을 확인할 수 있습니다.

<a id="custom-agents"></a>

현재 Codex 릴리스에서는 하위 에이전트 워크플로우가 기본적으로 활성화되어 있습니다. 하위 에이전트 활동은 ChatGPT 데스크톱 앱, Codex CLI, IDE 확장에 표시됩니다.

각 하위 에이전트가 개별적으로 모델과 도구를 사용하므로 하위 에이전트 워크플로우는 비슷한 작업을 단일 에이전트로 실행할 때보다 더 많은 토큰을 소비합니다.

ChatGPT Work에서 독립적으로 처리할 수 있는 작업을 하위 에이전트에 위임하도록 ChatGPT에 요청하세요. 하위 에이전트는 ChatGPT의 호스팅 환경에서 실행되며, 활동과 결과가 채팅에 표시됩니다. 대부분의 추론 수준에서는 위임을 명시적으로 요청해야 합니다. Ultra 설정에서는 에이전트의 병렬 작업으로 속도나 품질을 크게 높일 수 있을 때 ChatGPT가 먼저 판단해 작업을 위임할 수 있습니다.

앱 채팅에서 Codex에 독립적으로 처리할 수 있는 작업을
하위 에이전트에 위임해 달라고 요청하세요. 현재 로컬 Codex 릴리스에서는 직접 요청하거나
적용되는 `AGENTS.md` 또는 스킬 지침에서 위임을 요청하면 작업을 위임합니다.
앱에 각 하위 에이전트 스레드가 표시되므로 작업 내용과
주 채팅에 반환된 요약을 확인할 수 있습니다.

대화형 CLI 세션에서 Codex에 하위 에이전트를 사용해 달라고 요청하세요.
Codex는 적용되는 `AGENTS.md` 또는 스킬 지침에서 위임을 요청할 때도 이를 따를 수 있습니다.
`/agent`를 사용해 실행 중인 에이전트 스레드를 확인하고 스레드 간에 전환하세요.
주 스레드는 하위 에이전트의 결과를 모아 최종 응답에 반영합니다.

IDE 채팅에서 Codex에 독립적으로 처리할 수 있는 작업을 하위 에이전트에 위임해 달라고 요청하세요.
Codex는 적용되는 `AGENTS.md` 또는 스킬 지침에서 위임을 요청할 때도
이를 따를 수 있습니다. 백그라운드 에이전트 UI를 사용할 수 있으면
활성 하위 에이전트가 Composer 위에 표시됩니다. 패널을 펼쳐 상태를 확인하거나,
활성 하위 에이전트를 모두 중지하거나, 개별 하위 에이전트 스레드를 여세요.

## 하위 에이전트 워크플로우의 이점

컨텍스트 윈도우가 크더라도 모델에는 한계가 있습니다. 요구사항, 제약 조건, 결정 사항을 정의하는 주 채팅에 탐색 메모, 테스트 로그, 스택 트레이스, 명령어 출력처럼 노이즈가 많은 중간 출력이 쌓이면 시간이 지날수록 세션의 신뢰성이 낮아질 수 있습니다.

이러한 현상은 흔히 다음과 같이 설명합니다:

- **컨텍스트 오염**: 유용한 정보가 노이즈가 많은 중간 출력에 묻힙니다.
- **컨텍스트 부패**: 채팅에 관련성이 낮은 세부 정보가 쌓이면서 성능이 저하됩니다.

자세한 배경은 [컨텍스트 부패](https://research.trychroma.com/context-rot)에 관한 Chroma의 글을 참고하세요.

하위 에이전트 워크플로우를 사용하면 노이즈가 많은 작업을 주 스레드에서 분리할 수 있습니다:

- **주 에이전트가** 요구사항, 결정 사항, 최종 결과에 집중하도록 하세요.
- 탐색, 테스트 또는 로그 분석에 특화된 **하위 에이전트를** 병렬로 실행하세요.
- 하위 에이전트가 중간 출력 원문 대신 **요약을** 반환하도록 하세요.

작업을 서로 독립적으로 병렬 실행할 수 있다면 시간도 절약할 수 있습니다. 또한 큰 작업을 범위가 명확한 작은 단위로 나누면 더 쉽게 처리할 수 있습니다. 예를 들어 Codex는 수백만 토큰 규모의 문서 분석을 더 작은 문제로 나누고 핵심 내용을 추려 주 스레드에 반환할 수 있습니다.

우선 탐색, 테스트, 트리아지, 요약처럼 읽기 비중이 큰 작업에 병렬 에이전트를 사용하세요. 여러 에이전트가 코드를 동시에 편집하면 충돌이 생기고 조정에 드는 부담이 커질 수 있으므로 쓰기 비중이 큰 병렬 워크플로우는 더 신중하게 사용하세요.

## 핵심 용어

Codex는 하위 에이전트 워크플로우에서 다음과 같은 관련 용어를 사용합니다:

- **하위 에이전트 워크플로우**: Codex가 에이전트를 병렬로 실행하고 결과를 결합하는 워크플로우입니다.
- **하위 에이전트**: Codex가 특정 작업을 맡기기 위해 시작하는 에이전트입니다.
- **에이전트 스레드**: 하위 에이전트가 작업하는 스레드입니다. 지원되는 클라이언트에서는 이 스레드를 열어 진행 상황이나 결과를 확인할 수 있습니다.

## 하위 에이전트 워크플로우 실행

대부분의 추론 수준에서는 하위 에이전트 사용이나 에이전트의 병렬 작업을 직접 요청하세요. Ultra 설정에서는 선제적 위임이 활성화되므로 ChatGPT가 별도 요청 없이도 독립적으로 처리하기에 적합한 작업을 위임할 수 있습니다.

하위 에이전트 사용이나 에이전트의 병렬 작업을 직접 요청하세요. 적용되는 프로젝트 또는 스킬 지침에서 위임을 요청하는 경우에도 Codex가 작업을 위임할 수 있습니다.

수동으로 실행하려면 “에이전트 두 개를 생성해”, “이 작업을 병렬로 위임해”, “항목마다 에이전트를 하나씩 사용해”처럼 직접 지시하면 됩니다. 각 하위 에이전트가 개별적으로 모델과 도구를 사용하므로 하위 에이전트 워크플로우는 비슷한 작업을 단일 에이전트로 실행할 때보다 더 많은 토큰을 소비합니다.

효과적인 하위 에이전트 프롬프트에는 작업을 어떻게 나눌지, Codex가 모든 에이전트의 작업이 끝날 때까지 기다린 후 계속 진행해야 하는지, 어떤 요약이나 결과를 반환해야 하는지를 명확히 설명해야 합니다.

```text
Review this branch with parallel subagents. Spawn one subagent for security risks, one for test gaps, and one for maintainability. Wait for all three, then summarize the findings by category with file references.

## 모델과 추론 설정 선택

에이전트마다 필요한 모델과 추론 설정이 다릅니다.

ChatGPT Work의 Composer에서 모델과 추론 수준을 선택하세요.
선택한 모델에 따라 **Light**, **Medium**, **High**,
**Extra High**, **Max** 등의 추론 수준을 사용할 수 있습니다. **Ultra** 옵션은
이용 자격이 있는 계정과 지원되는 모델에서만 사용할 수 있습니다. 최대 수준으로 추론하며,
ChatGPT가 적합한 작업을 먼저 판단해 하위 에이전트에 위임할 수 있습니다.

다른 추론 수준에서 작업을 병렬로 위임하려면 하위 에이전트 사용을 명시적으로 요청하세요.

하위 에이전트의 모델이나 `model_reasoning_effort`를 구성하지 않으면
하위 에이전트는 상위 에이전트의 모델과 추론 강도를 상속합니다.
명시적인 생성 요청이나 `[agents]` 기본값에 따라 모델을 선택했지만
추론 강도를 명시적으로 지정하거나 구성하지 않은 경우에는
해당 모델의 기본 추론 강도를 사용합니다. 작업마다 지능, 속도, 비용의 균형을 맞추려면
프롬프트에서 특정 모델이나 추론 강도를 요청하거나,
`config.toml`에서 `[agents]` 기본값을 구성하거나, 커스텀 에이전트 파일에 `model` 및
`model_reasoning_effort`를 직접 설정하세요.
예를 들어 빠른 스캔에는 <code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code> 모델을, 더 까다로운 추론에는 추론 강도를 높인 <code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code> 구성을 사용하세요.

  Codex의 대부분 작업은{" "}
<code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code> 모델로 시작하세요. 가벼운 하위 에이전트 작업에
더 빠르고 비용이 적게 드는 옵션이 필요하면{" "}
  <code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code> 모델을 사용하세요.

### 모델 선택

- **<code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code>**: 까다로운 작업을 맡는 에이전트에는 이 모델부터 사용하세요. 넓은 컨텍스트 전반에서 계획을 세우고, 도구를 사용하고, 검증하며, 끝까지 수행해야 하는 모호한 다단계 작업에 가장 뛰어납니다.
- **<code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code>**: 탐색, 읽기 위주의 스캔, 대용량 파일 검토, 보조 문서 처리처럼 깊이보다 속도와 효율이 중요한 에이전트에 사용하세요. 핵심 결과를 추려 주 에이전트에 반환하는 병렬 작업자에 적합합니다.
- **<code>{RECOMMENDED_MODEL_REFERENCES.latestNanoModel.slug}</code>**: 명확하거나 반복 가능하거나 처리량이 많은 작업을 좁은 범위에서 빠르게 수행하는 에이전트에 사용하세요.

### 추론 강도(`model_reasoning_effort`)

- **`ultra`**: 선택한 모델에서 지원하며
  가장 깊이 있는 추론이 필요할 때 사용하세요.
- **`max`** 및 **`xhigh`**: 선택한 모델이 해당 수준을 지원하며
  특히 까다로운 추론이 필요할 때 사용하세요.
- **`high`**: 에이전트가 복잡한 로직을 추적하거나, 가정을 확인하거나, 엣지 케이스를 검토해야 할 때 사용하세요(예: 검토 또는 보안 중심 에이전트).
- **`medium`**: 대부분의 에이전트에 적합한 균형 잡힌 기본값입니다.
- **`low`**: 작업이 단순하고 속도가 가장 중요할 때 사용하세요.

추론 강도를 높이면 응답 시간과 토큰 사용량이 늘어나지만 복잡한 작업의 품질을 높일 수 있습니다. 자세한 내용은 [모델](/ko-KR/codex/models), [기본 구성](/ko-KR/codex/config-file/config-basic), [구성 참조 자료](/ko-KR/codex/config-file/config-reference) 문서를 참고하세요.

## 오케스트레이션 및 스레드 제어

ChatGPT 또는 Codex가 새 하위 에이전트 생성, 후속 지침 전달, 결과 대기, 에이전트 스레드 닫기 등 에이전트 간 오케스트레이션을 처리합니다.

여러 에이전트가 실행 중이면 Codex는 요청한 모든 결과가 준비될 때까지 기다린 다음 하나로 통합한 응답을 반환합니다.

대부분의 추론 수준에서 ChatGPT는 직접 요청을 받은 후 에이전트를 생성합니다. Ultra 설정에서는 병렬 작업이 유용할 때 ChatGPT가 먼저 판단해 작업을 위임할 수도 있습니다.

현재 로컬 Codex 릴리스에서는 직접 요청을 받거나 적용되는 프로젝트 또는 스킬 지침에 따라 에이전트를 생성합니다.

작동 방식을 확인하려면 프로젝트에서 다음 프롬프트를 사용해 보세요:

```text
I would like to review the following points on the current PR (this branch vs main). Spawn one agent per point, wait for all of them, and summarize the result for each point.
1. Security issue
2. Code quality
3. Bugs
4. Race
5. Test flakiness
6. Maintainability of the code

## 하위 에이전트 관리

**하위 에이전트** 화면을 열면 읽기 전용 **활성** 및 **완료** 목록을 볼 수 있습니다.
완료된 하위 에이전트를 선택해 세부 정보와 결과를 확인하세요.
웹 사이드바에는 하위 에이전트 활동이 표시되지만,
개별 하위 에이전트를 중지하거나 작업 방향을 조정하는 제어 기능은 없습니다.

- 주 스레드에 표시된 활동에서 하위 에이전트 스레드를 열어 작업 내용을 확인하세요.
- 실행 중인 하위 에이전트의 작업 방향을 조정하거나 중지하거나, 완료된 하위 에이전트 스레드를 닫으려면 Codex에 직접 요청하세요.

  

  

- CLI에서 `/agent` 명령어를 사용해 활성 에이전트 스레드 간에 전환하고 진행 중인 스레드를 확인하세요.
- 실행 중인 하위 에이전트의 작업 방향을 조정하거나 실행을 중지하거나 완료된 에이전트 스레드를 닫으려면 Codex에 직접 요청하세요.

- 백그라운드 에이전트 패널을 사용할 수 있으면 패널을 펼쳐 상태를 확인하거나, 활성 하위 에이전트를 중지하거나, 하위 에이전트 스레드를 여세요.
- 실행 중인 하위 에이전트의 작업 방향을 조정하거나 실행을 중지하거나 완료된 하위 에이전트 스레드를 닫으려면 Codex에 직접 요청하세요.

## 승인 및 샌드박스 제어

하위 에이전트는 현재 샌드박스 정책을 상속합니다.

ChatGPT Work는 자체 호스팅 환경에서 하위 에이전트를 실행하며, 로컬 Codex 샌드박스나 승인 모드 제어 기능을 제공하지 않습니다. 하위 에이전트는 상위 채팅에서 사용할 수 있는 도구를 사용합니다. 웹사이트 및 커넥터 권한은 도구별로 적용됩니다.

하위 에이전트는 Composer 아래에서 선택한 권한 모드를 상속합니다. Codex에 작업 위임을 요청하기 전에 상위 턴에 사용할 권한 모드를 선택하세요.

대화형 CLI 세션에서는 주 스레드를 보고 있는 동안에도
비활성 에이전트 스레드에서 승인 요청이 표시될 수 있습니다. 승인 오버레이에는
요청이 발생한 스레드의 라벨이 표시되며, `o` 키를 누르면
요청을 승인하거나 거부하거나 답변하기 전에 해당 스레드를 열 수 있습니다.

비대화형 플로우이거나 실행 중에 새 승인 요청을 표시할 수 없는 경우, 새 승인이 필요한 작업은 실패하며 Codex는 해당 오류를 상위 워크플로우에 전달합니다.

Codex는 하위 에이전트를 생성할 때 상위 턴에 현재 적용 중인 런타임 재정의를 다시 적용합니다.
여기에는 세션 중 대화형으로 선택한 샌드박스 및 승인 설정이 포함되며,
`/permissions` 변경 사항이나 `--yolo` 옵션도 해당됩니다.
선택한 커스텀 에이전트 파일에 다른 기본값이 설정되어 있어도 마찬가지입니다.

하위 에이전트는 Composer 아래에서 선택한 권한 모드를 상속합니다. Codex에 작업 위임을 요청하기 전에 상위 턴에 사용할 권한 모드를 선택하세요.

개별 [커스텀 에이전트](#custom-agents)의 샌드박스 구성을 재정의할 수도 있습니다. 예를 들어 특정 에이전트가 읽기 전용 모드로 작업하도록 명시할 수 있습니다.

## 커스텀 에이전트

Codex에는 다음과 같은 기본 제공 에이전트가 포함되어 있습니다:

- `default`: 범용 폴백 에이전트입니다.
- `worker`: 구현 및 수정 작업을 위한 실행 중심 에이전트입니다.
- `explorer`: 읽기 중심의 코드베이스 탐색 에이전트입니다.

커스텀 에이전트를 직접 정의하려면 개인용 에이전트는
`~/.codex/agents/`에, 프로젝트 범위의 에이전트는 `.codex/agents/`에
독립된 TOML 파일을 추가하세요.

각 파일은 하나의 커스텀 에이전트를 정의합니다. Codex는 생성된 세션의 구성 레이어로 이 파일들을 로드하므로, 커스텀 에이전트에서도 일반 Codex 세션 구성과 동일한 설정을 재정의할 수 있습니다. 이 방식은 전용 에이전트 매니페스트보다 복잡하게 느껴질 수 있으며, 작성과 공유 기능이 발전함에 따라 형식이 변경될 수 있습니다.

모든 독립된 커스텀 에이전트 파일에는 다음 항목을 정의해야 합니다:

- `name`
- `description`
- `developer_instructions`

커스텀 에이전트 파일에 `model` 또는 `model_reasoning_effort`가 설정되어 있으면
파일의 값이 우선합니다. 파일을 적용하기 전에 Codex는 각 설정값을
생성 시 명시한 값, 해당 `[agents]` 기본값,
상위 에이전트의 값 순으로 결정합니다. 명시적인 생성 요청이나 `[agents]` 기본값으로
모델을 선택했지만 어느 쪽에서도 추론 강도를 지정하지 않으면
Codex는 해당 모델의 기본 추론 강도를 사용합니다. 커스텀 에이전트 파일에서 `model`만 설정하면
앞서 결정된 추론 강도가 유지됩니다. 파일에 `model_reasoning_effort`도 설정하면
추론 강도를 바꿀 수 있습니다. 선택한 모델이 해당 강도를 지원하지 않거나
다른 강도를 사용하려는 경우에 설정하세요. `sandbox_mode`, `mcp_servers`,
`skills.config` 같은 다른 세션 설정은 커스텀 에이전트 파일에서 생략하면
상위 에이전트의 값을 상속합니다.

### 전역 설정

전역 하위 에이전트 설정은 기존과 같이 [구성](/ko-KR/codex/config-file/config-basic#configuration-precedence)의 `[agents]` 아래에 있습니다.

| 필드                                       | 유형    | 필수 | 용도                                                             |
| ------------------------------------------- | ------- | :------: | ------------------------------------------------------------------- |
| `agents.enabled`                            | 불리언 |    아니요    | 멀티 에이전트 도구를 활성화하거나 비활성화합니다.                                |
| `agents.max_concurrent_threads_per_session` | 숫자  |    아니요    | 주 에이전트 스레드를 제외하고, 생성된 에이전트 스레드 중 동시에 열어 둘 수 있는 수를 제한합니다. |
| `agents.default_subagent_model`             | 문자열  |    아니요    | 생성되는 에이전트의 기본 모델을 설정합니다.                           |
| `agents.default_subagent_reasoning_effort`  | 문자열  |    아니요    | 생성되는 에이전트의 기본 추론 강도를 설정합니다.                |
| `agents.interrupt_message`                  | 불리언 |    아니요    | 에이전트 턴이 중단될 때 모델에 표시되는 메시지를 기록합니다.   |

**참고:**

- `agents.enabled`의 기본값은 `true`입니다. 멀티 에이전트 도구를 비활성화하려면 `false`로 설정하세요.
- `agents.max_concurrent_threads_per_session`을 설정하지 않으면 Codex가 기본값을 선택합니다. 기존 구성에서는 `agents.max_threads`를 레거시 별칭으로 계속 사용할 수 있습니다.
- 생성 시 명시한 값이 `agents.default_subagent_model`과 `agents.default_subagent_reasoning_effort`보다 우선합니다.
- `agents.interrupt_message`의 기본값은 `true`입니다. 모델에 표시되는 중단 메시지를 에이전트의 컨텍스트에서 제외하려면 `false`로 설정하세요.
- 커스텀 에이전트 이름이 `explorer` 같은 기본 제공 에이전트의 이름과 일치하면 커스텀 에이전트가 우선합니다.

### 커스텀 에이전트 파일 스키마

| 필드                    | 유형   | 필수 | 용도                                                         |
| ------------------------ | ------ | :------: | --------------------------------------------------------------- |
| `name`                   | 문자열 |   예    | Codex가 이 에이전트를 생성하거나 지칭할 때 사용하는 에이전트 이름입니다. |
| `description`            | 문자열 |   예    | Codex가 이 에이전트를 사용해야 하는 상황을 설명하는 사용자용 안내입니다.     |
| `developer_instructions` | 문자열 |   예    | 에이전트의 동작을 정의하는 핵심 지침입니다.             |

커스텀 에이전트 파일에는 `config.toml`에서 지원하는 `model`, `model_reasoning_effort`, `sandbox_mode`, `mcp_servers`, `skills.config` 등의 다른 키도 포함할 수 있습니다.

Codex는 `name` 필드로 커스텀 에이전트를 식별합니다. 파일 이름을
에이전트 이름과 일치시키는 것이 가장 간단한 규칙이지만, `name` 필드가
최종 기준입니다.

### 커스텀 에이전트 예시

가장 효과적인 커스텀 에이전트는 담당 범위가 좁고 동작 원칙이 명확합니다. 각 에이전트에 명확한 작업 하나와
그 작업에 맞는 도구 사용 범위, 관련된 다른 작업으로 범위를 벗어나지 않도록 하는
지침을 제공하세요.

#### 예시 1: PR 검토

이 패턴에서는 검토 작업을 역할별로 특화된 세 개의 커스텀 에이전트에 나누어 맡깁니다:

- `pr_explorer`는 코드베이스의 구조를 파악하고 근거를 수집합니다.
- `reviewer`는 정확성, 보안, 테스트 측면의 위험 요소를 찾습니다.
- `docs_researcher`는 전용 MCP 서버를 사용해 프레임워크 또는 API 문서를 확인합니다.

프로젝트 설정(`.codex/config.toml`):

```toml
[agents]
max_concurrent_threads_per_session = 8

`.codex/agents/pr-explorer.toml`:

```toml
name = "pr_explorer"
description = "Read-only codebase explorer for gathering evidence before changes are proposed."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Stay in exploration mode.
Trace the real execution path, cite files and symbols, and avoid proposing fixes unless the parent agent asks for them.
Prefer fast search and targeted file reads over broad scans.
"""

`.codex/agents/reviewer.toml`:

```toml
name = "reviewer"
description = "PR reviewer focused on correctness, security, and missing tests."
model = "gpt-5.6-terra"
model_reasoning_effort = "high"
sandbox_mode = "read-only"
developer_instructions = """
Review code like an owner.
Prioritize correctness, security, behavior regressions, and missing test coverage.
Lead with concrete findings, include reproduction steps when possible, and avoid style-only comments unless they hide a real bug.
"""

`.codex/agents/docs-researcher.toml`:

```toml
name = "docs_researcher"
description = "Documentation specialist that uses the docs MCP server to verify APIs and framework behavior."
model = "gpt-5.6-luna"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Use the docs MCP server to confirm APIs, options, and version-specific behavior.
Return concise answers with links or exact references when available.
Do not make code changes.
"""

[mcp_servers.openaiDeveloperDocs]
url = "https://developers.openai.com/mcp"

이 설정은 다음과 같은 프롬프트에 적합합니다:

```text
Review this branch against main. Have pr_explorer map the affected code paths, reviewer find real risks, and docs_researcher verify the framework APIs that the patch relies on.

#### 예시 2: 프런트엔드 통합 디버깅

이 패턴은 UI 회귀 문제, 간헐적으로 실패하는 브라우저 플로우, 애플리케이션 코드와 실행 중인 제품에 걸쳐 발생하는 통합 버그를 다룰 때 유용합니다.

프로젝트 설정(`.codex/config.toml`):

```toml
[agents]
max_concurrent_threads_per_session = 6

`.codex/agents/code-mapper.toml`:

```toml
name = "code_mapper"
description = "Read-only codebase explorer for locating the relevant frontend and backend code paths."
model = "gpt-5.6-luna"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Map the code that owns the failing UI flow.
Identify entry points, state transitions, and likely files before the worker starts editing.
"""

`.codex/agents/browser-debugger.toml`:

```toml
name = "browser_debugger"
description = "UI debugger that uses browser tooling to reproduce issues and capture evidence."
model = "gpt-5.6-terra"
model_reasoning_effort = "high"
sandbox_mode = "workspace-write"
developer_instructions = """
Reproduce the issue in the browser, capture exact steps, and report what the UI actually does.
Use browser tooling for screenshots, console output, and network evidence.
Do not edit application code.
"""

[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
startup_timeout_sec = 20

`.codex/agents/ui-fixer.toml`:

```toml
name = "ui_fixer"
description = "Implementation-focused agent for small, targeted fixes after the issue is understood."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
developer_instructions = """
Own the fix once the issue is reproduced.
Make the smallest defensible change, keep unrelated files untouched, and validate only the behavior you changed.
"""

[[skills.config]]
path = "/Users/me/.agents/skills/docs-editor/SKILL.md"
enabled = false

이 설정은 다음과 같은 프롬프트에 적합합니다:

```text
Investigate why the settings modal fails to save. Have browser_debugger reproduce it, code_mapper trace the responsible code path, and ui_fixer implement the smallest fix once the failure mode is clear.

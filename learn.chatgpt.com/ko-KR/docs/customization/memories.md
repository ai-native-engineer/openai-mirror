<!-- source: https://learn.chatgpt.com/ko-KR/docs/customization/memories -->

메모리를 사용하면 ChatGPT와 Codex가 이전 작업의 유용한 컨텍스트를 후속
작업에 활용할 수 있습니다.
ChatGPT 웹은 ChatGPT 메모리를 사용하지만, 로컬 Codex 클라이언트는 별도의 로컬
메모리 저장소와 제어 기능을 사용합니다.

필수 팀 지침은 `AGENTS.md` 또는 버전 관리되는 문서에 보관하세요.
메모리는 필요한 정보를 다시 불러오는 보조 수단으로 활용하되, 항상 적용해야 하는
규칙의 유일한 출처로 삼지 마세요.

ChatGPT 데스크톱 앱에서 `/memories`를 사용해 현재 채팅이 로컬 메모리를 사용할지,
향후 메모리 생성에 활용될지 선택하세요. 이 기능을 켜거나 끄려면
**설정 \> 개인 맞춤 설정에서** 관리하세요.

**설정 \> 개인 맞춤 설정에서** ChatGPT 메모리를 관리하세요. ChatGPT Work는
계정 및 워크스페이스에 제공되는 메모리 설정을 사용하며, 로컬 Codex
메모리 저장소나 로컬 메모리 제어 기능은 사용하지 않습니다.

Codex CLI의 대화형 세션에서 `/memories`를 사용하면 현재 채팅이 기존 로컬
메모리를 사용할지, 향후 메모리 생성의 입력으로 사용될지를 제어할 수 있습니다.
명령어를 사용할 수 없다면 [로컬 메모리 구성](#configure-local-memories)을
참조하세요.

IDE 확장은 연결된 Codex 호스트의 로컬 메모리 저장소를 사용합니다. 해당
호스트에서 메모리가 활성화되어 있으면 Codex CLI와 동일한 채팅별 제어
기능을 사용하세요.

[컴퓨터 사용 기록](/ko-KR/codex/customization/computer-history)은 허용된 앱과 웹사이트에서의 활동을
ChatGPT와 Codex가 참조할 수 있는 메모리와 타임라인으로 만드는
macOS 데스크톱 기능입니다.

<a id="how-memories-work"></a>
<a id="memory-storage"></a>
<a id="control-memories-per-thread"></a>
<a id="control-memories-per-chat"></a>
<a id="control-memories-per-task"></a>
<a id="review-memories"></a>

## 로컬 Codex 메모리의 작동 방식

메모리를 활성화하면 Codex는 조건을 충족하는 이전 채팅의 유용한 컨텍스트를 로컬
메모리 파일로 만들 수 있습니다. Codex는 진행 중이거나 단시간만 이어진 세션을 제외하고,
생성된 메모리 필드에서 비밀 정보를 가리며, 각 채팅이 끝나는 즉시 처리하는 대신
백그라운드에서 메모리를 업데이트합니다.

채팅이 끝나도 메모리가 바로 업데이트되지 않을 수 있습니다. Codex는 아직 진행
중인 작업을 요약하지 않도록 채팅이 충분히 오래 유휴 상태가 될 때까지
기다립니다.

메모리 생성은 Codex 요청 한도의 남은 비율이 설정된 임계값보다 낮으면
백그라운드 처리 단계를 건너뛸 수도 있습니다. 이는 한도에 가까워졌을 때 Codex가
할당량을 소모하지 않도록 하기 위한 것입니다.

## 로컬 메모리 저장 위치

Codex는 사용자의 Codex 홈 디렉터리 아래에 메모리를 저장합니다. 기본 경로는
`~/.codex`입니다. [구성 및 상태 저장 위치](/ko-KR/codex/config-file/config-advanced#config-and-state-locations)에서
Codex가 `CODEX_HOME`을 사용하는 방식을 확인하세요.

주요 메모리 파일은 `~/.codex/memories/`에 저장되며, 요약,
장기 보존 항목, 최근 입력, 이전 채팅의 근거 자료가 포함됩니다.

이 파일은 생성된 상태 데이터로 취급하세요. 문제를 해결하거나 Codex 홈 디렉터리를
공유하기 전에 검사할 수 있지만, 직접 편집하는 방식을 주요 제어 수단으로
사용해서는 안 됩니다.

<a id="control-local-memories-per-task"></a>

## 채팅별 로컬 메모리 제어

ChatGPT 데스크톱 앱과 Codex TUI에서 `/memories`를 사용해 현재 채팅의
메모리 동작을 제어하세요. 채팅별 옵션을 사용하면 현재 채팅이 기존
메모리를 사용할 수 있는지와 Codex가 이 채팅을 향후 메모리 생성에
사용할 수 있는지를 결정할 수 있습니다.

채팅별 선택 사항은 전역 메모리 설정을 변경하지 않습니다.

## 로컬 메모리 검토

메모리에 비밀 정보를 저장하지 마세요. Codex는 생성된 메모리 필드에서 비밀 정보를
가리지만, Codex 홈 디렉터리나 생성된 메모리 아티팩트를 공유하기 전에는 메모리
파일을 검토해야 합니다.

<a id="enable-memories"></a>
<a id="configuration"></a>

## 로컬 메모리 구성

로컬 Codex 메모리는 기본적으로 꺼져 있습니다. ChatGPT 데스크톱 앱에서
**설정 \> 개인 맞춤 설정을** 열고 **메모리 활성화를** 켜세요.

구성 파일을 사용해 설정하려면 `config.toml`에 기능 플래그를 추가하세요:

```toml
[features]
memories = true

구성 파일 위치와 메모리 관련 설정의 전체 목록은
[기본 구성](/ko-KR/codex/config-file/config-basic)과 [구성
참조 자료](/ko-KR/codex/config-file/config-reference)에서 확인하세요.

일반적으로 사용하는 메모리 관련 설정은 다음과 같습니다:

- `memories.generate_memories`: 새로 만든 채팅을 메모리 생성용 입력으로
  저장할 수 있는지 제어합니다.
- `memories.use_memories`: Codex가 기존 메모리를 향후 세션에
  주입할지 제어합니다.
- `memories.disable_on_external_context`: `true`로 설정하면 MCP 도구 호출, 웹 검색, 도구 검색 등
  외부 컨텍스트를 사용한 채팅을 메모리 생성에서 제외합니다.
  이전 키인 `memories.no_memories_if_mcp_or_web_search`도
  여전히 별칭으로 허용됩니다.
- `memories.min_rate_limit_remaining_percent`: 메모리 생성을 시작하기 위한 Codex 요청 한도 잔여 비율의
  최솟값을 제어합니다.
- `memories.extract_model`: 채팅별 메모리 추출에 사용할 모델을
  재정의합니다.
- `memories.consolidation_model`: 전역 메모리 통합에 사용할 모델을
  재정의합니다.

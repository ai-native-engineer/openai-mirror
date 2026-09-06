<!-- source: https://learn.chatgpt.com/ko-KR/docs/agent-configuration/agents-md -->

Codex는 작업을 시작하기 전에 `AGENTS.md` 파일을 읽습니다. 전역 지침에 프로젝트별 재정의를 계층적으로 적용하면 어떤 레포지토리를 열어도 일관된 기준으로 각 작업을 시작할 수 있습니다.

## Codex가 지침을 찾는 방식

Codex는 시작할 때 지침 체인을 구성합니다(실행당 한 번, TUI에서는 일반적으로 세션을 시작할 때 한 번). 다음 우선순위에 따라 지침을 찾습니다:

1. **전역 범위:** Codex는 홈 디렉터리(별도로 `CODEX_HOME`를 설정하지 않았다면 기본값은 `~/.codex`)에서 `AGENTS.override.md` 파일이 있으면 이 파일을 읽고, 없으면 `AGENTS.md` 파일을 읽습니다. 이 수준에서는 비어 있지 않은 첫 번째 파일만 사용합니다.
2. **프로젝트 범위:** Codex는 프로젝트 루트(일반적으로 Git 루트)에서 현재 작업 디렉터리까지 경로를 따라 내려갑니다. 프로젝트 루트를 찾지 못하면 현재 디렉터리만 확인합니다. 이 경로의 각 디렉터리에서 `AGENTS.override.md`, `AGENTS.md`, 그리고 `project_doc_fallback_filenames`에 지정된 대체 이름을 차례로 확인합니다. Codex는 디렉터리마다 최대 하나의 파일만 포함합니다.
3. **병합 순서:** Codex는 루트부터 아래로 내려오며 파일 사이에 빈 줄을 넣어 연결합니다. 현재 디렉터리에 더 가까운 파일일수록 결합된 프롬프트에 나중에 추가되므로 앞선 지침을 재정의합니다.

Codex는 빈 파일을 건너뛰고, 결합된 크기가 `project_doc_max_bytes`에 정의된 한도(기본값 32 KiB)에 도달하면 파일 추가를 중단합니다. 이 설정에 관한 자세한 내용은 [프로젝트 지침 탐색](/ko-KR/codex/config-file/config-advanced#project-instructions-discovery)을 참조하세요. 한도에 도달하면 한도를 늘리거나 지침을 중첩 디렉터리에 나누어 배치하세요.

## 전역 지침 만들기

모든 레포지토리가 공통 작업 규칙을 상속하도록 Codex 홈 디렉터리에 지속적으로 적용되는 기본 설정을 만드세요.

1. 디렉터리가 있는지 확인하세요:

   ```bash
   mkdir -p ~/.codex

2. 재사용할 기본 설정을 담은 `~/.codex/AGENTS.md` 파일을 만드세요:

   ```md
   # ~/.codex/AGENTS.md

   ## Working agreements

   - Always run `npm test` after modifying JavaScript files.
   - Prefer `pnpm` when installing dependencies.
   - Ask for confirmation before adding new production dependencies.

3. 파일을 불러오는지 확인하려면 어디서든 Codex를 실행하세요:

   ```bash
   codex --ask-for-approval never "Summarize the current instructions."

   예상 결과: Codex는 작업을 제안하기 전에 `~/.codex/AGENTS.md`의 항목을 인용합니다.

기본 파일을 삭제하지 않고 전역 지침을 일시적으로 재정의해야 할 때는 `~/.codex/AGENTS.override.md`를 사용하세요. 공유 지침을 복원하려면 재정의 파일을 제거하세요.

## 프로젝트 지침 계층화하기

레포지토리 수준 파일을 사용하면 전역 기본 설정을 계속 상속하면서 Codex에 프로젝트 규칙을 알릴 수 있습니다.

1. 레포지토리 루트에 기본 설정을 다루는 `AGENTS.md` 파일을 추가하세요:

   ```md
   # AGENTS.md

   ## Repository expectations

   - Run `npm run lint` before opening a pull request.
   - Document public utilities in `docs/` when you change behavior.

2. 특정 팀에 다른 규칙이 필요하면 중첩 디렉터리에 재정의 파일을 추가하세요. 예를 들어 `services/payments/`에 `AGENTS.override.md` 파일을 만드세요:

   ```md
   # services/payments/AGENTS.override.md

   ## Payments service rules

   - Use `make test-payments` instead of `npm test`.
   - Never rotate API keys without notifying the security channel.

3. payments 디렉터리에서 Codex를 시작하세요:

   ```bash
   codex --cd services/payments --ask-for-approval never "List the instruction sources you loaded."

   예상 결과: Codex는 전역 파일을 첫 번째로, 레포지토리 루트의 `AGENTS.md`를 두 번째로, payments 재정의 파일을 마지막으로 표시합니다.

Codex는 현재 디렉터리에 도달하면 검색을 중단하므로, 특정 작업용 재정의 파일은 해당 작업 위치에 최대한 가까이 두세요.

다음은 전역 파일과 payments 전용 재정의 파일을 추가한 레포지토리의 예시입니다:

## 코드 검토 규칙 추가하기

[GitHub에서 Codex 코드 검토](/ko-KR/codex/third-party/github#customize-what-codex-reviews)를 사용하려면
규칙이 적용되는 코드에서 가장 가까운 `AGENTS.md` 파일에
`## Code Review Rules` 섹션을 추가하세요. 레포지토리 전체 검사는 루트에 두고
서비스별 검사는 중첩 파일에 두세요.

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

규칙은 간결하게 작성하고, 문제로 표시해야 할 동작과 안전한 해결 방법 또는
예외를 설명하세요. 서식 및 린트 검사는 CI에 맡기세요. 설정과
규칙 작성 지침은 [Codex가 검토할 항목
사용자 지정](/ko-KR/codex/third-party/github#customize-what-codex-reviews)을 참조하세요.

## 대체 파일 이름 사용자 지정하기

레포지토리에서 이미 다른 파일 이름(예: `TEAM_GUIDE.md`)을 사용하고 있다면 Codex가 이 파일을 지침 파일로 처리하도록 대체 목록에 추가하세요.

1. Codex 구성을 편집하세요:

   ```toml
   # ~/.codex/config.toml
   project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]
   project_doc_max_bytes = 65536

2. 업데이트된 구성을 불러오도록 Codex를 다시 시작하거나 새 명령어를 실행하세요.

이제 Codex는 각 디렉터리에서 `AGENTS.override.md`, `AGENTS.md`, `TEAM_GUIDE.md`, `.agents.md` 순으로 확인합니다. 이 목록에 없는 파일 이름은 지침을 찾을 때 무시됩니다. 바이트 한도가 커졌으므로 지침이 잘리기 전에 결합할 수 있는 지침의 양이 늘어납니다.

대체 목록을 설정하면 Codex는 다른 이름의 파일도 지침으로 처리합니다:

프로젝트별 자동화 사용자처럼 다른 프로필을 사용하려면 `CODEX_HOME` 환경 변수를 설정하세요:

```bash
CODEX_HOME=$(pwd)/.codex codex exec "List active instruction sources"

예상 결과: 출력에 사용자 지정 `.codex` 디렉터리를 기준으로 한 파일 목록이 표시됩니다.

## 설정 확인하기

- 레포지토리 루트에서 `codex --ask-for-approval never "Summarize the current instructions."`를 실행하세요. Codex가 전역 및 프로젝트 파일의 지침을 우선순위에 따라 출력해야 합니다.
- `codex --cd subdir --ask-for-approval never "Show which instruction files are active."`를 사용해 중첩된 재정의 파일이 더 광범위한 규칙을 대체하는지 확인하세요.
- Codex가 불러온 지침 파일을 감사하려면 `codex -c log_dir=./.codex-log` 명령으로 일반 텍스트 TUI 로그를 사용 설정한 뒤 `./.codex-log/codex-tui.log`를 확인하세요. 또는 세션 로깅을 사용 설정했다면 최신 `session-*.jsonl` 파일을 검사하세요.
- 지침이 최신 상태가 아닌 것 같으면 대상 디렉터리에서 Codex를 다시 시작하세요. Codex는 실행할 때마다(TUI 세션을 시작할 때도) 지침 체인을 다시 구성하므로 수동으로 지울 캐시는 없습니다.

## 지침 탐색 문제 해결하기

- **아무 지침도 불러오지 못함:** 작업하려는 레포지토리에 있는지, `codex status` 명령이 보고하는 워크스페이스 루트가 예상과 일치하는지 확인하세요. 지침 파일에 내용이 있는지도 확인하세요. Codex는 빈 파일을 무시합니다.
- **잘못된 지침이 표시됨:** 디렉터리 트리의 상위 경로나 Codex 홈 디렉터리 아래에 `AGENTS.override.md` 파일이 있는지 확인하세요. 일반 파일로 되돌리려면 재정의 파일의 이름을 바꾸거나 파일을 제거하세요.
- **Codex가 대체 파일 이름을 무시함:** `project_doc_fallback_filenames`에 파일 이름을 오타 없이 추가했는지 확인한 다음, 업데이트된 구성이 적용되도록 Codex를 다시 시작하세요.
- **지침이 잘림:** 중요한 지침이 온전히 유지되도록 `project_doc_max_bytes` 값을 늘리거나 큰 파일을 여러 중첩 디렉터리로 나누세요.
- **프로필 혼동:** Codex를 실행하기 전에 `echo $CODEX_HOME` 명령을 실행하세요. 기본값이 아닌 값이 설정되어 있으면 Codex는 편집한 곳과 다른 홈 디렉터리를 사용합니다.

## 다음 단계

- 자세한 내용은 공식 [AGENTS.md](https://agents.md) 웹사이트에서 확인하세요.
- [Codex 프롬프팅](/ko-KR/codex/prompting)에서 지속적으로 적용되는 지침과 잘 어울리는 대화 패턴을 살펴보세요.

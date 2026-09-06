<!-- source: https://learn.chatgpt.com/ko-KR/docs/cli-customization -->

Codex CLI는 대화형 세션이 표시되는 방식과 명령 및 프롬프트를 입력하는 방식을
조정할 수 있는 터미널별 옵션을 제공합니다.

## 구문 강조 및 테마

터미널 UI(TUI)는 펜스로 감싼 Markdown 코드 블록과 파일 diff에 구문 강조를
적용합니다. `/theme` 명령어를 실행해 테마 선택기를 열고 테마를 미리 본 다음,
선택한 테마를 `$CODEX_HOME/config.toml`의 `tui.theme`에 저장하세요.

사용자 지정 테마를 추가하려면 `.tmTheme` 파일을 `$CODEX_HOME/themes`에 배치한 다음
테마 선택기에서 해당 테마를 선택하세요.

## 셸 자동 완성

Bash, Z shell, Fish 또는 PowerShell용 자동 완성 스크립트를 생성하세요:

```bash
codex completion zsh

셸 구성 파일에서 스크립트를 로드하세요. Z shell의 경우 다음을 추가하세요:

```bash
eval "$(codex completion zsh)"

Z shell에서 `command not found: compdef` 오류가 발생하면 Codex 자동 완성을 로드하기 전에
자동 완성 시스템을 초기화하세요:

```bash
autoload -Uz compinit && compinit
eval "$(codex completion zsh)"

셸을 다시 시작하고 `codex`를 입력한 다음 <kbd>Tab</kbd> 키를 눌러 자동 완성이 작동하는지 확인하세요.

## 프롬프트 편집기

긴 프롬프트를 작성할 때는 Composer에서 <kbd>Ctrl</kbd>+<kbd>G</kbd>를 눌러
`VISUAL`에 지정된 편집기를 여세요. `VISUAL`이 설정되지 않은 경우에는 `EDITOR`에 지정된 편집기가 열립니다.
프롬프트를 전송하기 전에 내용을 저장하고 편집기를 닫아 텍스트를 Composer로 되돌리세요.

대화형 키보드 조작 방법과 전체 명령 및 옵션 목록은
[명령](/codex/developer-commands?surface=cli#cli-interactive-shortcuts)에서 확인하세요.

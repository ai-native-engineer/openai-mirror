<!-- source: https://learn.chatgpt.com/ko-KR/docs/reference/troubleshooting -->

## 자주 묻는 질문

### Codex가 수정하지 않은 파일이 사이드 패널에 표시됨

프로젝트가 Git 레포지토리에 있으면 검토 패널에는
Codex가 만들지 않은 변경 사항을 포함해 프로젝트의 Git 상태에 따른 변경 사항이
자동으로 표시됩니다.

검토 창에서는 스테이징된 변경 사항과 아직 스테이징되지 않은 변경 사항 사이를
전환하고, 브랜치를 main과 비교할 수 있습니다.

마지막 Codex 턴의 변경 사항만 보려면 diff
창을 **마지막 턴** 보기로 전환하세요.

[검토 창 사용 방법 자세히 알아보기](/ko-KR/codex/code-review?surface=app).

### 사이드바에서 프로젝트 제거

사이드바에서 프로젝트를 제거하려면 프로젝트 이름 위에 마우스 포인터를 올리고
점 3개를 클릭한 다음 "제거"를 선택하세요. 복원하려면 **채팅** 옆의
**새 프로젝트 추가** 버튼이나 다음 단축키를 사용해 프로젝트를 다시 추가하세요.

<kbd>Cmd</kbd>+<kbd>O</kbd>.

<a id="find-archived-threads"></a>
<a id="find-archived-tasks"></a>

### 보관된 채팅 찾기

보관된 채팅은 [설정](codex://settings)에서 찾을 수 있습니다. 채팅 보관을
해제하면 사이드바의 원래 위치에 다시 나타납니다.

<a id="only-some-threads-appear-in-the-sidebar"></a>
<a id="only-some-tasks-appear-in-the-sidebar"></a>

### 사이드바에 일부 채팅만 표시됨

사이드바에서는 프로젝트 상태에 따라 채팅을 필터링할 수 있습니다. 찾는 채팅이 보이지 않으면
**채팅** 옆의 필터 아이콘을 선택한 다음 **시간순을** 선택하세요.
그래도 채팅이 보이지 않으면 [설정](codex://settings)을 열고
**보관된 채팅을** 확인하세요.

### 작업 트리에서 코드가 실행되지 않음

작업 트리는 별도 디렉터리에 생성되며 기본적으로 Git에 체크인된 파일이
포함됩니다. 프로젝트의 종속성과 도구를 관리하는 방식에 따라
[로컬 환경](/ko-KR/codex/environments/local-environment)을 사용해 작업 트리에서 설정 스크립트를 실행하거나
[`.worktreeinclude`](/ko-KR/codex/environments/git-worktrees#copy-ignored-local-files-into-managed-worktrees)를 사용해 무시된 설정 파일을 복사해야 할 수 있습니다.
또는 일반 로컬 프로젝트에서 변경 사항을 체크아웃할 수도 있습니다.
자세한 내용은 [작업 트리 문서](/ko-KR/codex/environments/git-worktrees)를
참조하세요.

### App이 팀원이 공유한 로컬 환경을 인식하지 못함

로컬 환경 구성은 프로젝트 루트의 `.codex` 폴더 안에 있어야 합니다.
프로젝트가 여러 개인 모노레포지토리에서 작업한다면
반드시 `.codex` 폴더가 있는
디렉터리를 프로젝트로 여세요.

### Codex가 Apple Music 접근을 요청함

작업에 따라 Codex가 파일 시스템을 탐색해야 할 수 있습니다. macOS의 특정
디렉터리(예: Music, Downloads, Desktop)에 접근하려면 사용자의
추가 승인이 필요합니다. Codex가 홈 디렉터리를 읽어야 하는 경우
macOS에서 해당 폴더에 대한 접근을 승인하라는 메시지가 표시됩니다.

<a id="automations-create-many-worktrees"></a>

### 예약 작업으로 많은 작업 트리가 생성됨

예약 작업을 자주 실행하면 시간이 지나면서 많은 작업 트리가 생성될 수 있습니다. 더 이상 필요하지 않은
예약 실행은 보관하고, 작업 트리를 유지하려는 경우가 아니라면 실행을
고정하지 마세요.

### 잘못된 대상을 선택한 후 프롬프트 복구

실수로 잘못된 대상(**로컬**, **작업 트리** 또는 **클라우드**)에서 채팅을 시작했다면 현재 실행을 취소한 후 메시지 입력창에서 위쪽 화살표 키를 눌러 이전 프롬프트를 복구할 수 있습니다.

### Codex CLI에서는 작동하지만 ChatGPT 데스크톱 앱에서는 작동하지 않는 기능

ChatGPT 데스크톱 앱과 Codex CLI에는 서로 다른 Codex 버전이 포함될 수 있어
기능이 한쪽에 먼저 제공될 수 있습니다. 실험적 기능은
Codex CLI에 먼저 제공될 수도 있습니다.

시스템의 Codex CLI 버전을 확인하려면 다음을 실행하세요:

```bash
codex --version

ChatGPT 데스크톱 앱에 번들로 포함된 Codex 버전을 확인하려면
호환성을 위해 유지되는 `Codex.app` 번들 경로를 사용하세요:

```bash
/Applications/Codex.app/Contents/Resources/codex --version

## 피드백 및 로그

팀에 피드백을 보내려면 메시지 입력창에 <kbd>/</kbd>를 입력하세요. 기존 채팅에서
피드백을 보내면 기존 세션도 피드백과 함께 공유할지
선택할 수 있습니다. 피드백을 제출하면 팀과 공유할 수 있는
세션 ID가 발급됩니다.

이슈를 신고하려면:

1. Codex GitHub 레포지토리에서 [기존 이슈](https://github.com/openai/codex/issues)를 확인하세요.
2. [새 GitHub 이슈 열기](https://github.com/openai/codex/issues/new?template=2-bug-report.yml&steps=Uploaded%20thread%3A%20019c0d37-d2b6-74c0-918f-0e64af9b6e14)

추가 로그는 다음 위치에서 확인할 수 있습니다:

- App 로그(macOS): `~/Library/Logs/com.openai.codex/YYYY/MM/DD`
- 세션 기록: `$CODEX_HOME/sessions`(기본값: `~/.codex/sessions`)
- 보관된 세션: `$CODEX_HOME/archived_sessions`(기본값: `~/.codex/archived_sessions`)

로그를 공유하기 전에 검토하여 민감한 정보가 포함되어 있지 않은지
확인하세요.

## 멈춤 상태 및 복구 방법

채팅이 멈춘 것처럼 보이면 다음을 시도하세요:

1. Codex가 승인을 기다리고 있는지 확인하세요.
2. 터미널을 열고 `git status` 같은 기본 명령어를 실행하세요.
3. 범위가 더 좁고 구체적인 프롬프트로 새 채팅을 시작하세요.

실수로 작업 트리 생성을 취소해 프롬프트가 사라졌다면 메시지 입력창에서 위쪽
화살표 키를 눌러 복구하세요.

## 터미널 문제

**터미널이 멈춘 것처럼 보임**

1. 터미널 패널을 닫으세요.
2. <kbd>Ctrl</kbd>+<kbd>\`</kbd> 키를 눌러 다시 여세요.
3. `pwd` 또는 `git status` 같은 기본 명령어를 다시 실행하세요.

명령이 예상과 다르게 작동하면 먼저 터미널에서 현재 디렉터리와
브랜치를 확인하세요.

계속 멈춰 있다면 진행 중인 채팅이 끝날 때까지 기다린 다음 앱을 다시 시작하세요.

**글꼴이 올바르게 표시되지 않음**

Codex는 검토 창, 통합 터미널, 그 밖에 앱 안에서 표시되는 모든 코드에 같은 글꼴을 사용합니다. [설정](codex://settings) 창의 **코드 글꼴** 옵션에서 글꼴을 설정할 수 있습니다.

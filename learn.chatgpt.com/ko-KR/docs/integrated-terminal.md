<!-- source: https://learn.chatgpt.com/ko-KR/docs/integrated-terminal -->

ChatGPT 데스크톱 앱의 각 채팅에는 현재 프로젝트 또는
작업 트리 전용 터미널이 포함되어 있습니다. 앱 오른쪽 상단의 터미널 아이콘을 선택하거나
<kbd>Ctrl</kbd>+<kbd>\`</kbd> 키를 눌러 여세요.

  
    
  

## 프로젝트 실행 및 검증

터미널을 사용하면 앱을 전환하지 않고도 변경 사항을 검증하고, 스크립트를 실행하며,
Git 작업을 수행할 수 있습니다. ChatGPT는 현재 터미널 출력을 읽을 수 있으므로
함께 작업하는 동안 실행 중인 개발 서버를 확인하거나
실패한 빌드를 참고할 수 있습니다.

자주 사용하는 명령은 다음과 같습니다:

- `git status`
- `git pull --rebase`
- `pnpm test` 또는 `npm test`
- `pnpm run lint` 또는 프로젝트에 맞는 다른 검사 명령

## 재사용 가능한 액션 만들기

정기적으로 실행하는 명령어가 있다면 [로컬 환경](/ko-KR/codex/environments/local-environment#actions)에 액션을 정의하세요.
액션은 ChatGPT 데스크톱 앱에 바로가기로 표시되며
통합 터미널에서 실행됩니다.

<kbd>Cmd</kbd>+<kbd>K</kbd> 키를 누르면 앱 명령 팔레트가 열리지만
터미널 내용은 지워지지 않습니다. 터미널 내용을 지우려면 <kbd>Ctrl</kbd>+<kbd>L</kbd> 키를 누르세요.

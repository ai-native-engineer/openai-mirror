<!-- source: https://learn.chatgpt.com/ko-KR/docs/windows/wsl -->

WSL2를 사용하면 Codex는 네이티브
[Windows 샌드박스](/ko-KR/codex/windows/windows-sandbox)가 아니라 Linux 환경에서 실행됩니다. Linux 네이티브
도구가 필요하거나, 레포지토리와 개발 워크플로우가 이미 WSL2에 설정되어 있거나,
두 가지 네이티브 Windows 샌드박스 모드가 모두 현재 환경에서 작동하지 않는 경우 WSL2를 선택하세요.

WSL1은 Codex `0.114`까지 지원되었습니다. Codex `0.115`부터 Linux
샌드박스가 `bubblewrap`으로 전환되어 WSL1은 더 이상 지원되지 않습니다.

## WSL 내에서 VS Code 실행

단계별 지침은 [공식 VS Code WSL 튜토리얼](https://code.visualstudio.com/docs/remote/wsl-tutorial)을 참고하세요.

### 사전 요구 사항

- WSL이 설치된 Windows가 필요합니다. WSL을 설치하려면 PowerShell을 관리자 권한으로 연 다음 `wsl --install`을 실행하세요(일반적으로 Ubuntu를 선택합니다).
- [WSL 확장 프로그램](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)이 설치된 VS Code가 필요합니다.

### WSL 터미널에서 VS Code 열기

```bash
# From your WSL shell
cd ~/code/your-project
code .

이렇게 하면 WSL 원격 창이 열리고, 필요한 경우 VS Code Server가 설치되며, 통합 터미널은 Linux에서 실행됩니다.

### WSL에 연결되었는지 확인

- 녹색 상태 표시줄에 `WSL: <distro>`가 표시되는지 확인하세요.
- 통합 터미널에는 `C:\` 대신 `/home/...` 같은 Linux 경로가 표시되어야 합니다.
- 다음 명령으로 확인할 수 있습니다:

  ```bash
  echo $WSL_DISTRO_NAME

  배포판 이름이 출력됩니다.

  상태 표시줄에 "WSL: ..." 표시가 없으면 `Ctrl+Shift+P`를 누르고
`WSL: Reopen Folder in WSL` 항목을 선택하세요. 최상의 성능을 위해 레포지토리는 `/home/...` 아래에 두고
`C:\` 아래에는 두지 마세요.

  Windows 앱이나 프로젝트 선택기에 WSL 레포지토리가 표시되지 않으면
파일 선택기 또는 파일 탐색기의 경로 입력란에 <code>\\wsl$</code> 경로를 입력한 다음
  배포판의 홈 디렉터리로 이동하세요.

## WSL에서 Codex CLI 사용

관리자 권한으로 연 PowerShell 또는 Windows 터미널에서 다음 명령을 실행하세요:

```powershell
# Install default Linux distribution (like Ubuntu)
wsl --install

# Start a shell inside Windows Subsystem for Linux
wsl

그런 다음 WSL 셸에서 다음 명령을 실행하세요:

```bash
# Install and run Codex in WSL
curl -fsSL https://chatgpt.com/codex/install.sh | sh
codex

## WSL에서 코드 작업

- <code>/mnt/c/...</code>처럼 Windows에 마운트된 경로에서 작업하면 Windows 네이티브 경로에서 작업할 때보다 느릴 수 있습니다. I/O 속도를 높이고 심볼릭 링크와 권한 문제를 줄이려면 레포지토리를 Linux 홈 디렉터리 아래(예: <code>~/code/my-app</code>)에 두세요:
  ```bash
  mkdir -p ~/code && cd ~/code
  git clone https://github.com/your/repo.git
  cd repo
- Windows에서 파일에 액세스해야 한다면 해당 파일은 파일 탐색기의 <code>\\wsl$\\Ubuntu\\home&lt;user\></code> 아래에서 찾을 수 있습니다.

## 문제 해결 및 자주 묻는 질문

- <code>/mnt/c</code> 아래에서 작업하고 있지 않은지 확인하세요. 레포지토리는 WSL 내부(예: <code>~/code/...</code>)로 이동하세요.
- 필요한 경우 WSL의 메모리와 CPU를 늘리고, WSL을 최신 버전으로 업데이트하세요:
  ```powershell
  wsl --update
  wsl --shutdown

WSL 내에 바이너리가 존재하고 `PATH`에 포함되어 있는지 확인하세요:

```bash
which codex || echo "codex not found"

바이너리를 찾을 수 없다면 [Codex CLI 설정 안내](#use-codex-cli-with-wsl)를 따르세요.

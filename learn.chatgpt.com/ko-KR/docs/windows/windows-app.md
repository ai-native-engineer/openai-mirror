<!-- source: https://learn.chatgpt.com/ko-KR/docs/windows/windows-app -->

# Windows용 ChatGPT 데스크톱 앱

[Windows용 ChatGPT 데스크톱 앱](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi)에서는 프로젝트를 넘나들며 작업하고,
여러 채팅을 병렬로 실행하고, 결과를 검토하는 모든 과정을 하나의 인터페이스에서 처리할 수 있습니다.
Windows 앱은 작업 트리, 예약 작업, Git
기능, 내장 브라우저, 파일 미리 보기, 플러그인, 스킬 등의 핵심 워크플로우를 지원합니다.
PowerShell과
[Windows 샌드박스](/ko-KR/codex/windows/windows-sandbox#windows-sandbox)를 사용해 Windows에서 네이티브로 실행하거나,
[Linux용 Windows 하위 시스템 2(WSL2)](#windows-subsystem-for-linux-wsl)에서 실행하도록 구성할 수 있습니다.

  
    
  

## ChatGPT 데스크톱 앱 다운로드

Windows용 [ChatGPT 데스크톱 앱](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi)을 다운로드하세요.

그런 다음 [빠른 시작](/ko-KR/codex/quickstart?setup=app)에 따라 시작하세요.

엔터프라이즈 설치 및 업데이트 옵션은
[Windows 앱 배포](/ko-KR/codex/enterprise/windows-deployment)를 참고하세요.

명령줄 설치 방식을 선호한다면 다음을 실행하세요:

```powershell
winget install --id 9PLM9XGG6VKS -s msstore
```

## 네이티브 샌드박스

Windows의 ChatGPT 데스크톱 앱은 에이전트가 PowerShell에서 실행될 때 네이티브 [Windows 샌드박스](/ko-KR/codex/windows/windows-sandbox#windows-sandbox)를 지원하며, 에이전트를 [Linux용 Windows 하위 시스템 2(WSL2)](#windows-subsystem-for-linux-wsl)에서 실행하면 Linux 샌드박스를 사용합니다. 어느 모드에서든 샌드박스 보호를 적용하려면 Codex에 메시지를 보내기 전에 Composer 아래에서 **승인 요청을** 선택하세요.

  Codex를 전체 권한 모드로 실행하면 작업 범위가 프로젝트
  디렉터리로 제한되지 않으며, 데이터 손실로 이어질 수 있는 의도치 않은 파괴적 작업을
  수행할 수 있습니다. 샌드박스 경계를 유지하고 필요한 예외에만
[규칙](/ko-KR/codex/agent-configuration/rules)을 사용하세요. 또는
[승인 정책을
  never로 설정](/ko-KR/codex/agent-approvals-security#run-without-approval-prompts)하면
  Codex가 권한 상승을 요청하지 않고
  [승인 및 보안 설정](/ko-KR/codex/agent-approvals-security)에 따라 문제 해결을 시도합니다.

## 개발 환경에 맞게 사용자 지정

<section class="feature-grid">

<div>

### 기본 편집기

Visual Studio, VS Code 또는 다른 편집기 중에서 **열기에** 사용할 기본 앱을 선택하세요.
이 선택은 프로젝트별로 재정의할 수 있습니다.
프로젝트의 **열기** 메뉴에서 이미 다른 앱을 선택했다면
해당 프로젝트별 선택이 우선 적용됩니다.

</div>

  
    
  

</section>

<section class="feature-grid inverse">

<div>

### 통합 터미널

기본 통합 터미널도 선택할 수 있습니다. 설치되어 있는 항목에 따라 다음 옵션을
사용할 수 있습니다:

- PowerShell
- 명령 프롬프트
- Git Bash
- WSL

이 변경 사항은 새 터미널 세션에만 적용됩니다. 통합 터미널이 이미 열려 있다면 새 기본
터미널이 표시되도록 앱을 다시 시작하거나 새 채팅을
시작하세요.

</div>

  
    
  

</section>

## Linux용 Windows 하위 시스템(WSL)

기본적으로 ChatGPT 데스크톱 앱은 Windows 네이티브 Codex 에이전트를 사용하므로,
에이전트는 PowerShell에서 명령을 실행합니다. 앱은
Linux용 Windows 하위 시스템 2(WSL2)에 있는 프로젝트에서도 필요에 따라 `wsl` CLI를 사용해 작업할 수 있습니다.

WSL 파일 시스템에서 프로젝트를 추가하려면 **새 프로젝트 추가를** 클릭하거나
<kbd>Ctrl</kbd>+<kbd>O</kbd>를 누른 다음, `\\wsl$\` 경로를 파일
탐색기 창에 입력하세요. 이어서 Linux 배포판과
열려는 폴더를 선택하세요.

Windows 네이티브 에이전트를 계속 사용하려면 프로젝트를 Windows 파일 시스템에
저장하고, WSL에서는
`/mnt/<drive>/...` 경로를 통해 접근하는 것이 좋습니다. WSL 파일 시스템에서 프로젝트를
직접 여는 것보다 이 구성이 더 안정적입니다.

에이전트 자체를 WSL2에서 실행하려면 **[설정](codex://settings)을** 열고,
에이전트를 Windows 네이티브에서 WSL로 전환한 다음 **앱을 다시 시작하세요**.
다시 시작하기 전에는 변경 사항이 적용되지 않습니다. 다시 시작해도 프로젝트는
그대로 유지됩니다.

Codex `0.114`까지 WSL1을 지원했습니다. Codex `0.115`부터 Linux
샌드박스가 `bubblewrap`으로 전환되어 WSL1은 더 이상 지원되지 않습니다.

  
    
  

통합 터미널은 에이전트와 별도로 구성합니다. 터미널 옵션은
[개발 환경에 맞게 사용자 지정](#customize-for-your-dev-setup)을
참고하세요. 워크플로우에 따라 에이전트는 WSL에서 실행하고 터미널에서는 PowerShell을
사용하거나, 둘 다 WSL을 사용하도록 설정할 수 있습니다.

## 유용한 개발자 도구

몇 가지 일반적인 개발자 도구가 이미 설치되어 있을 때 Codex가 가장 원활하게 작동합니다:

- **Git**: ChatGPT 데스크톱 앱의 검토 패널을 지원하며 변경 사항을 확인하거나
  되돌릴 수 있게 합니다.
- **Node.js**: 에이전트가 작업을 더
  효율적으로 수행하는 데 사용하는 일반적인 도구입니다.
- **Python**: 에이전트가 작업을 더
  효율적으로 수행하는 데 사용하는 일반적인 도구입니다.
- **.NET SDK**: 네이티브 Windows 앱을 빌드할 때 유용합니다.
- **GitHub CLI**: ChatGPT 데스크톱 앱에서 GitHub 전용 기능을 사용할 수 있게 합니다.

Windows 기본 패키지 관리자인 `winget`을 사용해 설치하려면 다음 내용을
[통합 터미널](/ko-KR/codex/integrated-terminal)에 붙여 넣거나
Codex에 설치를 요청하세요:

```powershell
winget install --id Git.Git
winget install --id OpenJS.NodeJS.LTS
winget install --id Python.Python.3.14
winget install --id Microsoft.DotNet.SDK.10
winget install --id GitHub.cli
```

GitHub CLI를 설치한 후 `gh auth login`을 실행하면 앱에서
GitHub 기능이 활성화됩니다.

다른 Python 또는 .NET 버전이 필요하면 패키지 ID를 원하는
버전으로 변경하세요.

## 문제 해결 및 자주 묻는 질문

### 관리자 권한으로 명령 실행

Codex에서 관리자 권한으로 명령을 실행해야 한다면 ChatGPT
데스크톱 앱 자체를 관리자 권한으로 시작하세요. 설치 후 시작 메뉴를 열고
앱을 찾은 다음 **관리자 권한으로 실행을** 선택하세요. Codex 에이전트는 해당
권한 수준을 상속합니다.

### PowerShell 실행 정책이 명령을 차단하는 경우

PowerShell에서 Node.js나 `npm` 같은 도구를 사용한 적이 없다면
Codex 에이전트 또는 통합 터미널에서 실행 정책 오류가 발생할 수 있습니다.

Codex가 PowerShell 스크립트를 생성하는 경우에도 이런 문제가 발생할 수 있습니다. 이 경우
PowerShell에서 스크립트를 실행하려면 제한 수준이 더 낮은 실행 정책이
필요할 수 있습니다.

오류는 다음과 같이 표시될 수 있습니다:

```text
npm.ps1 cannot be loaded because running scripts is disabled on this system.
```

일반적인 해결 방법은 실행 정책을 `RemoteSigned`로 설정하는 것입니다:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

정책을 변경하기 전에 Microsoft의
[실행 정책 가이드](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies)에서
자세한 내용과 기타 옵션을 확인하세요.

### Windows의 로컬 환경 스크립트

[로컬 환경](/ko-KR/codex/environments/local-environment)에서 여러 플랫폼에서 동작하는
`npm` 스크립트 같은 명령을 사용한다면, 모든 플랫폼에서 하나의 공유 설정 스크립트나
액션 모음을 사용할 수 있습니다.

Windows에 특화된 동작이 필요하면 Windows 전용 설정 스크립트나
Windows 전용 액션을 만드세요.

액션은 통합 터미널에서 사용하는 환경에서 실행됩니다.
[개발 환경에 맞게 사용자 지정](#customize-for-your-dev-setup)을 참고하세요.

로컬 설정 스크립트는 에이전트 환경에서 실행됩니다. 에이전트가 WSL을 사용하면 WSL에서,
그 외에는 PowerShell에서 실행됩니다.

### WSL과 구성, 인증 및 세션 공유

Windows 앱은 Windows 네이티브 Codex와 동일한 Codex 홈 디렉터리를 사용합니다:
`%USERPROFILE%\.codex`.

WSL 내에서도 Codex CLI를 실행하면 CLI는 기본적으로 Linux 홈
디렉터리를 사용하므로 Windows 앱과 구성, 캐시된 인증 정보 또는
세션 기록을 자동으로 공유하지 않습니다.

공유하려면 다음 방법 중 하나를 사용하세요:

- WSL의 `~/.codex`를 파일 시스템의 `%USERPROFILE%\.codex`와 동기화하세요.
- `CODEX_HOME`을 설정해 WSL이 Windows의 Codex 홈 디렉터리를 사용하도록 지정하세요:

```bash

```

모든 셸에 이 설정을 적용하려면
`~/.bashrc` 또는 `~/.zshrc` 같은 WSL 셸 프로필에 추가하세요.

### Git 기능을 사용할 수 없음

Windows에 Git이 네이티브로 설치되어 있지 않으면 앱의 일부
기능을 사용할 수 없습니다. `winget install Git.Git` 명령어를 PowerShell 또는 `cmd.exe`에서 실행해 설치하세요.

### `\\wsl$`에서 연 프로젝트에서 Git이 감지되지 않음

현재 WSL에서도 접근할 수 있는 프로젝트에 Windows 네이티브 에이전트를
사용하려면 프로젝트를 Windows 네이티브 드라이브에 저장하고
WSL에서 `/mnt/<drive>/...` 경로로 접근하는 방법이 가장 안정적입니다.

### 열기 대화 상자에 `Cmder`가 표시되지 않음

`Cmder`가 설치되어 있는데도 Codex의 열기 대화 상자에 표시되지 않으면
Windows 시작 메뉴에 추가하세요. `Cmder`를 마우스 오른쪽 버튼으로 클릭해 **시작 메뉴에 추가를** 선택한 다음
Codex를 다시 시작하거나 시스템을 재부팅하세요.

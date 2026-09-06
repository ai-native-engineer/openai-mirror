<!-- source: https://learn.chatgpt.com/ko-KR/docs/sandboxing -->

샌드박스는 에이전트에 컴퓨터에 대한 무제한 접근 권한을 부여하지 않으면서
자율적으로 작업하도록 하는 경계입니다. 로컬 채팅이
**ChatGPT 데스크톱 앱**, **Codex CLI** 또는 **IDE 확장에서** 명령을 실행하면, 해당 명령은 전체 권한이 아니라 기본적으로
제한된 환경에서 실행됩니다.

이 환경은 에이전트가 독자적으로 수행할 수 있는 작업을 정의합니다. 예를 들어 수정할 수 있는 파일과
명령의 네트워크 사용 가능 여부가 여기에 해당합니다. 작업이 정해진 경계 안에서
이루어지는 경우 에이전트는 확인을 받기 위해 멈추지 않고 계속 작업할 수 있습니다. 이 경계를
벗어나야 하는 경우에는 승인 플로우가 적용됩니다.

  샌드박스와 승인은 서로 다른 제어 수단이지만 함께 작동합니다.
샌드박스는 기술적 경계를 정의하고, 승인 정책은 에이전트가 그 경계를
넘기 전에 언제 멈춰 승인을 요청해야 하는지를 결정합니다.

## 샌드박스의 역할

샌드박스는 기본 제공 파일 작업뿐 아니라 별도로 실행되는 명령에도
적용됩니다. 에이전트가 `git`, 패키지 관리자 또는 테스트 러너 같은 도구를 실행하면
해당 명령에도 동일한 샌드박스 경계가 적용됩니다.

Codex는 각 OS에서 해당 플랫폼의 네이티브 메커니즘으로 제한을 적용합니다. 구현 방식은
macOS, Linux, WSL2, 네이티브 Windows에서 각각 다르지만, 모든 환경에서
기본 원리는 같습니다. 에이전트에 제한된 작업 공간을 제공하여 일상적인 작업을
명확한 경계 안에서 자율적으로 실행할 수 있도록 합니다.

## 샌드박스가 중요한 이유

샌드박스는 승인 피로를 줄여 줍니다. 위험이 낮은 명령을 실행할 때마다
확인을 요청하는 대신, 에이전트는 이미 승인된 경계 안에서 파일을 읽고 편집하며
일상적인 프로젝트 명령을 실행할 수 있습니다.

또한 에이전트 기반 작업에 더 명확한 신뢰 모델을 제공합니다. 에이전트의 의도만
신뢰하는 것이 아니라, 강제 적용되는 제한 안에서 작동한다는 점도
신뢰할 수 있습니다. 따라서 언제 작업을 멈추고 도움을 요청할지 파악하면서
에이전트가 독립적으로 작업하도록 할 수 있습니다.

## 시작하기

기본 권한 모드에서는 샌드박스가 자동으로 적용됩니다.

### 사전 요구 사항

**macOS에서는** 기본 제공 Seatbelt
프레임워크를 사용하므로 별도의 설정 없이 샌드박스가 작동합니다.

**Windows에서는** Codex가 PowerShell 실행 시 네이티브 [Windows
샌드박스](/ko-KR/codex/windows/windows-sandbox#windows-sandbox)를 사용하고, WSL2 실행 시에는
Linux 샌드박스 구현을 사용합니다.

**Linux 및 WSL2에서는** 먼저 패키지 관리자로 `bubblewrap`을 설치하세요:

  <div slot="ubuntu-debian">

```bash
sudo apt install bubblewrap

  </div>

  <div slot="fedora">

```bash
sudo dnf install bubblewrap

  </div>

Codex는 `PATH`에서 처음 찾은 `bwrap` 실행 파일을 사용합니다. 사용 가능한 `bwrap`
실행 파일이 없으면 Codex에 포함된 헬퍼를 대신 사용하지만, 이 헬퍼는
비특권 사용자 네임스페이스 생성이 지원되어야 작동합니다. `bwrap`을 제공하는
배포판 패키지를 설치하면 안정적으로 구성할 수 있습니다.

`bwrap`이 없거나 헬퍼가 필요한 사용자 네임스페이스를
생성할 수 없으면 Codex가 시작 시 경고를 표시합니다. 이 AppArmor 설정에 제한을 두는
배포판에서는 `bwrap` AppArmor 프로필을 로드하는 방법을 우선 사용하세요. 그러면 `bwrap`을
시스템 전체의 제한을 해제하지 않고 계속 실행할 수 있습니다.

  **Ubuntu AppArmor 참고:** Ubuntu 25.04에서는 Ubuntu 패키지 레포지토리에서 `bubblewrap`을 설치하면
  별도의 AppArmor 설정 없이 정상적으로 작동해야 합니다.
`bwrap-userns-restrict` 프로필은 `apparmor` 패키지에 포함되어 있으며
`/etc/apparmor.d/bwrap-userns-restrict`에 위치합니다.

Ubuntu 24.04에서는 `bubblewrap`을 설치한 후에도 Codex가 필요한 사용자
네임스페이스를 생성할 수 없다는 경고를 표시할 수 있습니다. 추가 프로필을 복사하고 로드하세요:

```bash
sudo apt update
sudo apt install apparmor-profiles apparmor-utils
sudo install -m 0644 \
  /usr/share/apparmor/extra-profiles/bwrap-userns-restrict \
  /etc/apparmor.d/bwrap-userns-restrict
sudo apparmor_parser -r /etc/apparmor.d/bwrap-userns-restrict

`apparmor_parser -r`을 실행하면 재부팅하지 않고 프로필을 커널에 로드할 수 있습니다.
모든 AppArmor 프로필을 다시 로드할 수도 있습니다:

```bash
sudo systemctl reload apparmor.service

해당 프로필을 사용할 수 없거나 해당 프로필로 문제가 해결되지 않으면 다음 명령으로
AppArmor의 비특권 사용자 네임스페이스 제한을 비활성화할 수 있습니다:

```bash
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0

## 권한 작동 방식

사용 중인 인터페이스의 권한 제어를 사용해 Codex의 로컬 작업 처리 방식을
변경하세요.

승인은 Codex가 작업 전에 언제 일시 중지할지 결정하고, 샌드박스는
명령이 접근할 수 있는 파일과 네트워크 리소스를 결정합니다. 한 번 승인하거나
세션 전체에 대해 승인하는 등 승인 범위를 선택할 수 있다면 작업을 계속하는 데
필요한 최소 범위를 선택하세요. 프로젝트 경계를 기본값으로 유지하고,
관련 없는 레포지토리까지 접근 권한을 확대하는 대신 별도의 프로젝트나 작업 트리를
사용하세요.

ChatGPT Work는 관리형 격리 환경에서 코드와 셸 명령을 실행합니다.
사용 가능한 기능은 워크스페이스 정책과 도구별 제어 설정에 따라
결정됩니다. 해당 설정을 사용할 수 있다면 **설정 \> 데이터 제어 \> Work
네트워크 액세스에서** 코드와 셸 명령의 네트워크 액세스를 관리하세요. 해당 명령이
공용 인터넷에 연결되도록 하려면 **공용 인터넷 액세스 허용을** 
활성화하세요. 이 설정이 꺼져 있으면 명령은 관리형 허용 목록에 있는 필수
호스트 이름에만 연결할 수 있습니다.

웹 검색, 플러그인, 원격 브라우저에는 각각 별도의 제어 설정이 적용됩니다.
변경 사항은 현재 코드 또는 셸 실행이 끝나고 Work가
실행 환경을 새로 고친 후 적용됩니다. ChatGPT 웹에서는 로컬
Codex 샌드박스나 승인 모드 선택기를 제공하지 않습니다.

ChatGPT 데스크톱 앱에서는 Composer 아래의 권한 제어를 사용하세요.
구성에 따라 메뉴에 **승인 요청**,
조건을 충족하는 승인 요청을 위한 **대신 승인** , **전체 권한**, 이름이 지정된 권한 프로필 또는
사용자 지정 권한 프로필이 표시될 수 있습니다.

CLI에서
[`/permissions`](/codex/developer-commands?surface=cli#cli-update-permissions-with-permissions)
명령을 입력해 권한 선택기를 열고 활성 권한 프로필을 변경하세요.

IDE 확장에서는 Composer 아래의 권한 제어를 사용하세요.
구성에 따라 메뉴에 **승인 요청**,
조건을 충족하는 승인 요청을 위한 **대신 승인** , **전체 권한**, 이름이 지정된 권한 프로필 또는
사용자 지정 권한 프로필이 표시될 수 있습니다.

<div class="not-prose my-8 max-w-[18rem] mr-auto">
  
    
      
    
  
</div>

<a id="configure-defaults"></a>

## 기본값 구성

항상 동일한 방식으로 시작하려면 `config.toml`에 기본값을 설정하세요.
작동 방식은 [기본 구성](/ko-KR/codex/config-file/config-basic)에서 설명하며,
[구성 참조 자료](/ko-KR/codex/config-file/config-reference)에서 다음 설정의 정확한 키를 확인할 수 있습니다:
`sandbox_mode`, `approval_policy`, `approvals_reviewer`,
`sandbox_workspace_write.writable_roots`. 이 설정을 사용하면 에이전트의 기본 자율성 수준,
쓰기가 허용되는 디렉터리, 승인을 위해 멈춰야 하는 시점,
조건을 충족하는 승인 요청의 검토 주체를 결정할 수 있습니다.

대표적인 샌드박스 모드는 다음과 같습니다:

- `read-only`: 에이전트는 파일을 확인할 수 있지만, 승인 없이는 파일을 편집하거나
  명령을 실행할 수 없습니다.
- `workspace-write`: 에이전트는 파일을 읽고 워크스페이스 안에서 편집하며, 그 경계 안에서
  일상적인 로컬 명령을 실행할 수 있습니다. 로컬 작업을 간편하게 수행하기 위한
  기본 모드입니다.
- `danger-full-access`: 에이전트가 샌드박스 제한 없이 실행됩니다. 이에 따라 파일 시스템과
  네트워크 경계가 제거되므로 에이전트에 전체 권한을 부여하려는 경우에만
  사용해야 합니다.

대표적인 승인 정책은 다음과 같습니다:

- `untrusted`: 에이전트는 신뢰할 수 있는 명령 집합에 포함되지 않은 명령을 실행하기 전에
  승인을 요청합니다.
- `on-request`: 에이전트는 기본적으로 샌드박스 안에서 작업하며,
  경계를 벗어나야 할 때 승인을 요청합니다.
- `never`: 에이전트는 승인을 요청하기 위해 작업을 멈추지 않습니다.

승인을 대화형으로 처리하는 경우 검토 주체도
`approvals_reviewer` 설정으로 선택할 수 있습니다:

- `user`: 승인 프롬프트가 사용자에게 표시됩니다. 기본값입니다.
- `auto_review`: 조건을 충족하는 승인 프롬프트는 검토 에이전트에게 전달됩니다
([자동 검토](/ko-KR/codex/sandboxing/auto-review) 참조).

전체 권한 구성에는 `sandbox_mode = "danger-full-access"` 설정과
`approval_policy = "never"` 설정을 함께 사용합니다. 반면 위험이 더 낮은 로컬 자동화
프리셋에는 `sandbox_mode = "workspace-write"` 설정과
`approval_policy = "on-request"` 설정을 함께 사용하며, 이에 해당하는 CLI 플래그는
`--sandbox workspace-write --ask-for-approval on-request`입니다. 그런 다음 수동 승인을 사용하려면
`approvals_reviewer = "user"` 설정을 유지하고, 승인을 자동으로 검토하려면
`approvals_reviewer = "auto_review"` 설정을 사용하면 됩니다.

에이전트가 여러 디렉터리에서 작업해야 하는 경우 쓰기 가능한 루트를 사용하면
샌드박스를 완전히 제거하지 않고도 수정할 수 있는 위치를 확장할 수 있습니다.
신뢰 경계를 더 넓히거나 좁혀야 한다면 일회성 예외에 의존하는 대신
기본 샌드박스 모드와 승인 정책을 조정하세요.

워크플로우에 특정 예외가 필요하면 [규칙](/ko-KR/codex/agent-configuration/rules)을 사용하세요. 규칙을 사용하면
샌드박스 외부의 명령 접두사를 허용하거나, 실행 전에 승인을 요청하도록 하거나,
금지할 수 있습니다. 액세스를 광범위하게 확대하는 것보다 이 방법이 더 적합한 경우가 많습니다.
IDE별 설정으로 이동하는 방법은 [Codex IDE 확장 설정](/codex/developer-settings?surface=ide)을 참조하세요.

자동 검토를 사용할 수 있더라도 샌드박스 경계는 달라지지 않습니다.
자동 검토는 해당 경계에서 발생하는 승인 요청에 사용할 수 있는 `approvals_reviewer`
옵션 중 하나입니다. 이러한 요청에는 샌드박스 권한 상승, 차단된 네트워크 액세스,
여전히 승인이 필요한 사이드 이펙트가 있는 도구 호출 등이 포함됩니다. 샌드박스 안에서
이미 허용된 작업은 추가 검토 없이 실행됩니다. 검토 에이전트의 수명 주기, 트리거 유형,
승인 거부의 의미와 구성에 관한 자세한 내용은
[자동 검토](/ko-KR/codex/sandboxing/auto-review)를 참조하세요.

플랫폼별 자세한 내용은 해당 플랫폼 문서를 참고하세요. 네이티브 Windows의 설정,
동작 및 문제 해결 방법은 [Windows](/ko-KR/codex/windows/windows-sandbox)를 참조하세요. 샌드박스와 승인에 관한 관리자
요구 사항 및 조직 차원의 제약 조건은
[에이전트 승인 및 보안](/ko-KR/codex/agent-approvals-security)을 참조하세요.

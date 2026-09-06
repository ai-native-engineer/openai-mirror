<!-- source: https://learn.chatgpt.com/ko-KR/docs/linux/linux-app -->

Linux용 ChatGPT 데스크톱 앱이 프리뷰로 제공됩니다. 사용 중인 Linux 배포판과 프로세서 아키텍처에 맞는 패키지를 설치한 다음 ChatGPT 계정으로 로그인하여 프로젝트, 로컬 파일, Codex로 작업하세요.

## 지원되는 배포판 및 아키텍처

프리뷰는 다음 Linux 배포판의 데스크톱 버전을 지원합니다.

- Ubuntu 24.04 LTS 및 26.04 LTS
- Debian 13
- Fedora 43 및 44

지원되는 각 배포판에는 x64 및 ARM64 프로세서용 패키지가 제공됩니다. 프로세서 아키텍처를 확인하려면 다음 명령을 실행하세요.

```bash
uname -m

출력값이 `x86_64`이면 x64 프로세서입니다. `aarch64` 또는
`arm64`이면 ARM64 프로세서입니다.

## 적합한 패키지 다운로드

Ubuntu 또는 Debian에서는 `.deb`을, Fedora에서는 `.rpm`을 선택하세요.

| 배포판     | 아키텍처 | 다운로드                                                                                                          |
| ---------------- | ------------ | ----------------------------------------------------------------------------------------------------------------- |
| Ubuntu 또는 Debian | x64          | [x64용 `.deb` 다운로드](https://persistent.oaistatic.com/codex-app-prod/linux/deb/latest/chatgpt_amd64.deb)     |
| Ubuntu 또는 Debian | ARM64        | [ARM64용 `.deb` 다운로드](https://persistent.oaistatic.com/codex-app-prod/linux/deb/latest/chatgpt_arm64.deb)   |
| Fedora           | x64          | [x64용 `.rpm` 다운로드](https://persistent.oaistatic.com/codex-app-prod/linux/rpm/latest/chatgpt.x86_64.rpm)    |
| Fedora           | ARM64        | [ARM64용 `.rpm` 다운로드](https://persistent.oaistatic.com/codex-app-prod/linux/rpm/latest/chatgpt.aarch64.rpm) |

## Ubuntu 또는 Debian에 설치

프로세서 아키텍처에 맞는 `.deb` 패키지를 다운로드하세요. 그런 다음
터미널을 열고 패키지가 있는 디렉터리로 이동한 후
`apt`로 설치하세요.

```bash
cd ~/Downloads
sudo apt install ./chatgpt_amd64.deb

ARM64의 경우 `chatgpt_amd64.deb`을 `chatgpt_arm64.deb`으로 바꾸세요.

애플리케이션 메뉴에서 **ChatGPT** 앱을 열거나 터미널에서 `chatgpt`를 실행하세요.
ChatGPT 계정으로 로그인한 후
[데스크톱 앱 빠른 시작](/ko-KR/codex/quickstart?setup=app)을 따라 진행하세요.

## Fedora에 설치

프로세서 아키텍처에 맞는 `.rpm` 패키지를 다운로드하세요. 그런 다음
터미널을 열고 패키지가 있는 디렉터리로 이동한 후
`dnf`로 설치하세요.

```bash
cd ~/Downloads
sudo dnf install ./chatgpt.x86_64.rpm

ARM64의 경우 `chatgpt.x86_64.rpm`을 `chatgpt.aarch64.rpm`으로 바꾸세요.

애플리케이션 메뉴에서 **ChatGPT** 앱을 열거나 터미널에서 `chatgpt`를 실행하세요.
ChatGPT 계정으로 로그인한 후
[데스크톱 앱 빠른 시작](/ko-KR/codex/quickstart?setup=app)을 따라 진행하세요.

## 앱 업데이트

패키지를 설치하면 서명된 OpenAI 패키지 레포지토리가 설정됩니다. 이후 업데이트는 사용 중인 배포판의 패키지 관리자로 설치하세요.

Ubuntu 또는 Debian에서는 다음 명령을 실행하세요.

```bash
sudo apt update
sudo apt install --only-upgrade chatgpt

Fedora에서는 다음 명령을 실행하세요.

```bash
sudo dnf upgrade --refresh chatgpt

## 호환성 및 제한 사항

프리뷰는
[지원되는 배포판 및 아키텍처](#supported-distributions-and-architectures)에 나열된 데스크톱 배포판을 지원합니다.
다른 Linux 배포판에서도 작동할 수 있지만 공식적으로 지원되지는 않습니다.

일부 기능에는 별도의 플랫폼 요구 사항이 적용됩니다. 예를 들어
[컴퓨터 사용](/ko-KR/codex/computer-use)은 macOS와 Windows에서 사용할 수 있지만
Linux 프리뷰에서는 아직 사용할 수 없습니다. 향후 릴리스에서 Linux도 지원할 예정입니다.

## Wayland 지원

네이티브 Wayland 지원은 실험 단계이며 계속 개선될 예정입니다. Wayland 세션에서는 가능한 경우 앱이 XWayland를 사용합니다. 네이티브 Wayland를 명시적으로 선택하려면 앱을 완전히 종료한 다음 터미널에서 실행하세요.

```bash
chatgpt --ozone-platform=wayland

네이티브 Wayland 지원이 개선되는 동안 플로팅 창, 창 위치 지정, 포커스, 키보드 단축키 등의 일부 기능이 완전히 작동하지 않을 수 있습니다.

## 다음 단계

- [데스크톱 앱 빠른 시작](/ko-KR/codex/quickstart?setup=app)을 따라 진행하세요.
- 브라우저 연동을 위해 [Chrome 확장 프로그램](/ko-KR/codex/chrome-extension)을 설정하세요.
- 로컬 프로젝트 및 명령의 [권한](/ko-KR/codex/permissions)을 검토하세요.

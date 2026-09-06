<!-- source: https://learn.chatgpt.com/ko-KR/docs/enterprise/windows-deployment -->

사용자는 ChatGPT 데스크톱 앱을 직접 설치할 수 있으며, IT 팀은
엔터프라이즈 관리 도구로 앱을 배포할 수도 있습니다. 이 앱에는 Store 서명이 적용되어 있지만
사용자가 설치하거나 업데이트하기 위해 Microsoft Store를 열 필요는 없습니다.

## 사용자가 앱을 설치하고 업데이트하도록 허용

사용자가 자신의 애플리케이션을 직접 관리할 수 있다면
[웹 설치 프로그램](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi)을 사용하도록 안내하세요.
이 설치 프로그램은 표준 설치 및 자동 업데이트
환경을 제공합니다. 설치 또는
업데이트 중 Microsoft Store 구성 요소가 표시될 수 있지만, 사용자가 Store를 직접 탐색할 필요는 없습니다.

명령줄에서 앱을 설치할 수도 있습니다:

```powershell
winget install --id 9PLM9XGG6VKS -s msstore

## 엔터프라이즈 관리 도구로 앱 배포

조직에서 소프트웨어를 중앙 관리하는 경우 Microsoft Intune이나
호환되는 다른 모바일 기기 관리(MDM) 또는 소프트웨어 배포
플랫폼을 사용하세요. 플랫폼에서 Microsoft Store 앱 배포를 지원하면
Store 앱 플로우에서 ChatGPT from OpenAI를 검색하거나 다음 Store 제품 ID를 사용하세요:

```text
9PLM9XGG6VKS

설정 세부 정보는 다음 Microsoft 문서를 참조하세요:

- [엔터프라이즈 배포 가이드](https://1drv.ms/b/c/123ec1ed6c72a14a/IQDVdo5pE5P3QKg5r0eieSvfAeE7cW0yy58ncBFW7OYajwU?e=dGH94F)
- [Intune 배포 가이드](https://1drv.ms/b/c/123ec1ed6c72a14a/IQDh_5o31T6XT7bUn5RPldEJAZX58gEuRr8YnJD7d2IMpec?e=nByKw6)
- [MECM 배포 가이드](https://1drv.ms/b/c/123ec1ed6c72a14a/IQB829f_TSbkR7-H9qA4Q9ntAa9D2He3qMjXksWi2ozdeg8?e=GTKgAl)
- [Microsoft Intune에 Microsoft Store 앱 추가](https://learn.microsoft.com/en-us/intune/app-management/deployment/add-microsoft-store)

<a id="manage-in-app-updates"></a>

### 앱 업데이트 관리

설정 지침과 롤아웃 가이드는
[앱 업데이트 관리](/ko-KR/codex/enterprise/manage-app-updates)를 참조하세요.

## Microsoft 배포 서비스 없이 설치

환경에서 초기 설치에 Microsoft 앱 배포 서비스를 사용할 수 없다면
기기 아키텍처별로 Store 서명 MSIX 패키지를
다운로드하세요:

| 기기 아키텍처 | 패키지                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------- |
| x64                 | [ChatGPT-x64.msix](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-x64.msix)     |
| Arm64               | [ChatGPT-arm64.msix](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-arm64.msix) |

이 고정 링크는 각
아키텍처용으로 가장 최근에 게시된 Store 서명 패키지를 가리킵니다. 라이선스 파일이 필요한
오프라인 배포 워크플로우에서는
[오프라인 라이선스(`ChatGPT-License.xml`)](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-License.xml)도 다운로드하세요.
적절한 MSIX를 MDM
또는 소프트웨어 배포 플랫폼에 등록하고, 필요한 경우 라이선스 파일도 함께 등록하세요.

초기 설치 후
`persistent.oaistatic.com`에 접속할 수 있는 기기는 관리형
구성에서 앱의 내장 업데이터를 비활성화하지 않는 한 업데이트를 자동으로 설치할 수 있습니다. 앱 내
업데이트를 비활성화한 경우 MDM 또는 소프트웨어 배포 도구를 통해 새 버전의 패키지를 배포하세요.

이 배포 방식의 특징은 다음과 같습니다:

- 제한된 환경에서의 초기 설치를 지원합니다.
- x64 및 Arm64 기기를 지원합니다.
- 독립 실행형 MSI 또는 Store를 통하지 않는 EXE는 제공하지 않습니다.

## 관련 리소스

- [앱 업데이트 관리](/ko-KR/codex/enterprise/manage-app-updates)
- [Windows용 ChatGPT 데스크톱 앱](/ko-KR/codex/app/windows)

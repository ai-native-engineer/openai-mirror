<!-- source: https://learn.chatgpt.com/ko-KR/docs/enterprise/skills -->

스킬은 지침과 보조 리소스로 구성된 재사용 가능한 워크플로우입니다.
ChatGPT 워크스페이스 스킬, ChatGPT 데스크톱 앱, Codex CLI 또는 IDE 확장의 대상 로컬 기능에서 사용하는
파일 시스템 스킬, 스킬을 패키징하는 플러그인에는 각각 별도의 수명 주기 및
접근 제어가 적용됩니다.

전체 관리 모델에 대한 자세한 내용은
[역할 및 워크스페이스 권한](/ko-KR/codex/enterprise/roles-and-workspace-permissions)을 참조하세요.

<a id="distinguish-the-distribution-models"></a>

## 스킬 배포 및 관리

| 배포 모델      | 용도                                                                                           | 관리 범위                                                                       |
| ----------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| ChatGPT 워크스페이스 스킬 | 지원되는 ChatGPT 워크스페이스 기능을 통한 승인된 워크플로우 공유 또는 설치              | ChatGPT 워크스페이스 스킬의 권한 및 수명 주기 제어                                    |
| 로컬 파일 시스템 스킬  | 레포지토리, 사용자, 관리자 또는 번들 시스템 위치에 설치된 워크플로우 불러오기     | 파일 시스템 배포, 로컬 클라이언트 구성 및 런타임 권한                  |
| 플러그인                  | 하나 이상의 스킬을 선택적 커넥터, MCP 서버, 훅 및 표시용 메타데이터와 함께 패키징 | 플러그인 사용 가능 여부와 설치, 그리고 번들에 포함된 각 기능의 개별 제어 |

ChatGPT 워크스페이스 스킬 배포, 로컬 파일 시스템 스킬 설치 및
사용 환경별 플러그인 설치는 서로 별개의 경로입니다. 스킬을 옮겨도
ChatGPT 워크스페이스에서의 소유권, 공유, 역할 할당, 플러그인
설치 상태 또는 커넥터 인증은 이전되지 않습니다.

플러그인은 웹, 데스크톱, 모바일용 ChatGPT의 채팅과 Work,
ChatGPT 데스크톱 앱의 Codex 및 Codex CLI 플러그인 브라우저에서 사용할 수 있습니다.
IDE 확장에서는 제공되지 않습니다.
지원되는 이러한 환경에서는 ChatGPT와 Codex가 공유하는 하나의 통합 디렉터리에서
공개 플러그인을 가져옵니다.

## 제어 주체

파일 시스템 위치와 작성 방법은 [스킬 빌드](/ko-KR/codex/build-skills)에서,
현재 워크스페이스 절차는 [ChatGPT의 스킬](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)에서,
플러그인 패키징은 [플러그인 빌드](https://developers.openai.com/plugins/build/plugins)에서
확인하세요.

ChatGPT 워크스페이스 제어는 로컬 파일 시스템 스킬이나 플러그인을 설치하지 않습니다.
파일 시스템 배포는 ChatGPT 워크스페이스에서의 소유권이나 역할을 할당하지 않습니다.
플러그인을 설치해도 커넥터, MCP 서버 또는
연결된 서비스에 대한 접근 권한이 부여되지 않습니다. 각 기능은
해당 기능을 관리하는 제어 화면에서 구성하세요.

## 관련 문서

- [스킬 및 플러그인](/ko-KR/codex/skills-and-plugins)
- [플러그인](/ko-KR/codex/plugins)
- [스킬 빌드](/ko-KR/codex/build-skills)
- [플러그인 빌드](https://developers.openai.com/plugins/build/plugins)
- [관리자 배포 가이드](/ko-KR/codex/enterprise/admin-setup)
- [플러그인 제어](/ko-KR/codex/enterprise/apps-and-connectors)

<!-- source: https://learn.chatgpt.com/ko-KR/docs/build-plugins -->

플러그인을 빌드하거나 제출하려면
[developers.openai.com의 전체 개발 문서](/plugins)를 참조하세요.

<div className="not-prose my-6">
  
    플러그인 빌드 및 제출
  
</div>

이 페이지에서는 플러그인을 간략히 소개합니다. 플러그인은 설치 가능한 패키지로,
스킬이나 MCP 서버 또는 둘 다를 포함할 수 있습니다.
MCP 서버는 선택적으로 UI를 반환할 수도 있습니다.

ChatGPT와 Codex는 하나의 통합 플러그인 디렉터리를 공유합니다. 공개 플러그인을 한 번
게시하면 두 제품 모두 지원되는 화면에서 같은 등록 항목을 찾을 수 있습니다.
개발 중에는 통합 디렉터리에 제출하기 전에 로컬 마켓플레이스를 사용해
패키지를 테스트하세요.

GitHub를 통해 워크스페이스에 배포하는 방법은
[플러그인 관리](/ko-KR/codex/enterprise/plugin-management)를 참조하세요.

개인 워크플로우 하나를 계속 다듬는 중이라면 스킬부터 시작하세요.
해당 워크플로우를 공유하거나 관련 스킬을 패키지로 묶거나,
외부 서비스에 연결하거나 안정적인 기능을 팀에 배포하려면 플러그인을 빌드하세요.

## `@plugin-creator`로 플러그인 만들기

가장 빠르게 설정하려면 ChatGPT Work 모드에서 기본 제공 `@plugin-creator` 스킬을 사용하거나
Codex에서 `$plugin-creator`를 사용하세요.

  
    
  

원하는 결과와 포함할 스킬 또는 MCP 서버를 설명하고,
테스트용 로컬 마켓플레이스 항목이 필요한지도 알려 주세요. 예:

```text
@plugin-creator Create a plugin named meeting-follow-up.
Include a skill that turns meeting notes into decisions, owners, and next steps.
Add it to a personal marketplace so I can test it locally.

이 스킬은 필수 `.codex-plugin/plugin.json` 매니페스트를 만들고 플러그인 폴더를 정리하며,
플러그인을 로컬 마켓플레이스에 추가할 수도 있습니다.

  
    
  

작업이 완료되면 다음을 진행하세요:

1. `.codex-plugin/plugin.json`을 검토하세요.
2. 플러그인에 포함된 각 스킬을 `skills/`에서 확인하세요.
3. ChatGPT 또는 Codex를 새로 고친 다음 해당 로컬 마켓플레이스
소스에서 플러그인을 설치하세요.
4. 새 대화에서 대표적인 요청으로 플러그인을 테스트하세요.

플러그인에 MCP 서버가 포함되어 있다면 먼저 해당 서버를 빌드하고 테스트한 다음,
등록된 연결 정보를 `@plugin-creator`에 제공하세요. 도구, 인증, 배포 및 테스트는
[MCP 서버 워크플로우](https://developers.openai.com/plugins/build/mcp-server)의 전체 절차에 따라
진행하세요.

## 스킬만 포함된 플러그인 직접 만들기

최소 구성의 플러그인에는 매니페스트와 하나 이상의 스킬이 포함됩니다:

```text
meeting-follow-up/
├── .codex-plugin/
│   └── plugin.json
└── skills/
    └── meeting-follow-up/
        └── SKILL.md

`.codex-plugin/plugin.json`을 만드세요:

```json
{
  "name": "meeting-follow-up",
  "version": "1.0.0",
  "description": "Turn meeting notes into decisions and next steps",
  "skills": "./skills/"
}

그런 다음 `skills/meeting-follow-up/SKILL.md`를 추가하세요:

```md
---
name: meeting-follow-up
description: Extract decisions, owners, and next steps from meeting notes.
---

Review the meeting notes. Return:

1. Decisions
2. Action items with owners
3. Open questions

플러그인 이름은 케밥 케이스로 지정하고 일관되게 유지하세요.
ChatGPT와 Codex가 해당 워크플로우를 적용할 상황을 파악할 수 있도록 스킬 설명을 구체적으로 작성하세요.

`@plugin-creator`를 사용해 폴더를 로컬 마켓플레이스에 추가한 다음,
공유하기 전에 플러그인을 설치하고 테스트하세요.

## 개발 문서에서 더 알아보기

개발에 관한 전체 안내는
[플러그인 문서](https://developers.openai.com/plugins/)에서 확인하세요. 다음 내용을 다룹니다:

- [플러그인 아키텍처](https://developers.openai.com/plugins/concepts/plugins)
- [스킬 빌드](https://developers.openai.com/plugins/build/skills)
- [MCP 서버 빌드](https://developers.openai.com/plugins/build/mcp-server)
- [선택적 UI 추가](https://developers.openai.com/plugins/build/chatgpt-ui)
- [플러그인 패키징](https://developers.openai.com/plugins/build/plugins)
- [플러그인 테스트](https://developers.openai.com/plugins/deploy/connect-chatgpt)
- [제출 및 게시](https://developers.openai.com/plugins/deploy/submission)

플러그인을 찾아보거나 설치, 활성화 또는 제거하려면 [플러그인
사용](/ko-KR/codex/plugins)을 참조하세요.

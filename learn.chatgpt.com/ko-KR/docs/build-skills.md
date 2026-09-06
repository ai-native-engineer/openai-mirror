<!-- source: https://learn.chatgpt.com/ko-KR/docs/build-skills -->

에이전트 스킬로 ChatGPT와 Codex에 작업별 기능을 추가하세요.
스킬은 지침, 리소스, 선택적 스크립트를 하나로 묶어 두 제품 모두
워크플로우를 안정적으로 수행할 수 있게 합니다. 스킬은
[오픈 에이전트 스킬 표준](https://agentskills.io)을 기반으로 합니다.

스킬은 재사용 가능한 워크플로우를 작성하는 형식입니다. 플러그인은
ChatGPT와 Codex가 공유하는 범용 플러그인 디렉터리를 통해
재사용 가능한 스킬과 커넥터를 배포합니다. 플러그인은 웹, 데스크톱,
모바일에서 사용하는 ChatGPT의 채팅과 Work, ChatGPT 데스크톱 앱의 Codex,
Codex CLI에서 작동합니다. 먼저 스킬로 워크플로우를 설계한 다음
[플러그인](https://developers.openai.com/plugins/build/plugins)으로 패키징하면
다른 사람이 설치할 수 있습니다.

독립형 스킬은 ChatGPT 데스크톱 앱, Codex CLI, IDE
확장에서 사용할 수 있습니다. 플러그인에 포함된 스킬은 웹, 데스크톱,
모바일에서 사용하는 ChatGPT의 채팅과 Work에서도 사용할 수 있습니다.

ChatGPT 데스크톱 앱의 사이드바에서 **스킬을** 열어 여러 프로젝트에서 만든
스킬을 확인하고 살펴보세요.

  
    
  

스킬은 **점진적 공개** 방식으로 컨텍스트를 효율적으로 관리합니다. ChatGPT와
Codex는 먼저 각 스킬의 이름과 설명을 확인한 뒤 해당 스킬을
사용하기로 결정하면 `SKILL.md`의 전체 지침을 불러옵니다.

Codex의 초기 목록에는 각 스킬의 파일 경로도 포함됩니다. 다른 프롬프트
내용을 밀어내지 않도록 이 목록은 모델 컨텍스트 윈도우의 최대 2%만
사용하며, 컨텍스트 윈도우 크기를 알 수 없으면 최대 8,000자를 사용합니다.
설치된 스킬이 많으면 Codex는 먼저 스킬 설명을 줄입니다. 스킬 세트가 크면
초기 목록에서 일부 스킬을 제외하고 경고를 표시할 수 있습니다.

이 한도는 초기 스킬 목록에만 적용됩니다. Codex는 스킬을 선택하면 해당 스킬의 SKILL.md 지침 전체를 읽습니다.

스킬은 `SKILL.md` 파일과 선택적 스크립트 및 참조 자료로 구성된 디렉터리입니다. `SKILL.md` 파일에는 `name`과 `description` 항목이 반드시 포함되어야 합니다.

<a id="how-codex-uses-skills"></a>

## ChatGPT와 Codex의 스킬 사용 방식

ChatGPT와 Codex는 다음 두 가지 방식으로 스킬을 활성화할 수 있습니다:

1. **명시적 호출:** 프롬프트에 스킬을 직접 포함하세요. ChatGPT에서는
   `@` 기호를 입력해 스킬을 선택하세요. Codex CLI 또는 IDE 확장에서는
`/skills` 명령어를 실행하거나 `$` 기호를 입력해 스킬을 지정하세요.
2. **암시적 호출:** ChatGPT나 Codex는 작업 내용이
   스킬의 `description`과 일치하면 해당 스킬을 선택할 수 있습니다.

암시적 매칭은 `description`에 따라 이루어지므로 적용 범위와 경계가 분명한
간결한 설명을 작성하세요. 설명이 축약되어도 호스트가 스킬을 찾을 수 있도록
핵심 사용 사례와 트리거 키워드를 앞부분에 배치하세요.

## 스킬 만들기

워크플로우를 이미 알고 있고 말로 설명하는 것보다 보여 주는 편이 쉽다면
[기록 및 재생](/ko-KR/codex/extend/record-and-replay)을 사용하세요. 레코더가 워크플로우를 캡처하고
각 단계를 검토한 뒤 시연 내용을 바탕으로 재사용 가능한 스킬의 초안을
작성합니다.

원하는 스킬을 설명해서 만들려면 내장 생성기를 사용하세요.
ChatGPT Work에서는 `@skill-creator`로 호출합니다. Codex에서는 다음과 같이 호출합니다:

```text
$skill-creator

생성기는 스킬의 기능, 실행되어야 하는 시점, 지침만 포함할지 스크립트도 포함할지를 묻습니다. 기본적으로는 지침만 포함합니다.

또는 `SKILL.md` 파일이 들어 있는 폴더를 만들어 스킬을 직접 만들 수 있습니다:

```md
---
name: skill-name
description: Explain exactly when this skill should and should not trigger.
---

Skill instructions for ChatGPT or Codex to follow.

Codex는 스킬 변경 사항을 자동으로 감지합니다. 업데이트가 표시되지 않으면 Codex를 다시 시작하세요.

<a id="where-to-save-skills"></a>

## Codex가 로컬 스킬을 불러오는 위치

Codex는 레포지토리, 사용자, 관리자, 시스템 위치에서 스킬을 읽습니다. 레포지토리에서는 현재 작업 디렉터리부터 레포지토리 루트까지 각 디렉터리의 `.agents/skills` 경로를 검색합니다. 두 스킬의 `name` 값이 같아도 병합하지 않으며, 두 스킬 모두 스킬 선택기에 표시될 수 있습니다.

| 스킬 범위 | 위치                                                                                                  | 권장 용도                                                                                                                                                                                        |
| :---------- | :-------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `REPO`      | `$CWD/.agents/skills` <br /> 현재 작업 디렉터리: Codex를 실행하는 위치입니다.                           | 레포지토리나 코드 환경에서 작업하는 팀은 작업 폴더와 관련된 스킬을 체크인할 수 있습니다. 예를 들어 특정 마이크로서비스나 모듈에만 해당하는 스킬입니다.                              |
| `REPO`      | `$CWD/../.agents/skills` <br /> Git 레포지토리에서 Codex를 실행할 때 CWD의 상위에 있는 폴더입니다.         | 중첩 폴더가 있는 레포지토리에서는 조직이 상위 폴더의 공유 영역과 관련된 스킬을 체크인할 수 있습니다.                                                                       |
| `REPO`      | `$REPO_ROOT/.agents/skills` <br /> Git 레포지토리에서 Codex를 실행할 때의 최상위 루트 폴더입니다. | 중첩 폴더가 있는 레포지토리에서는 조직이 레포지토리를 사용하는 모든 사람을 위한 스킬을 체크인할 수 있습니다. 이러한 스킬은 레포지토리의 모든 하위 폴더에서 사용할 수 있는 루트 스킬로 작동합니다. |
| `USER`      | `$HOME/.agents/skills` <br /> 사용자 개인 폴더에 체크인된 모든 스킬입니다.                         | 사용자가 작업하는 모든 레포지토리에서 사용할 사용자별 스킬을 선별해 관리하는 데 사용합니다.                                                                                                           |
| `ADMIN`     | `/etc/codex/skills` <br /> 머신이나 컨테이너의 공유 시스템 위치에 체크인된 모든 스킬입니다. | SDK 스크립트와 자동화에 사용하거나 머신의 각 사용자가 이용할 수 있는 기본 관리자 스킬을 체크인하는 데 사용합니다.                                                                                     |
| `SYSTEM`    | OpenAI가 Codex와 함께 번들로 제공합니다.                                                                             | skill-creator 스킬과 plan 스킬처럼 폭넓은 사용자에게 유용한 스킬입니다. Codex를 시작하는 모든 사용자가 이용할 수 있습니다.                                                                   |

Codex는 심볼릭 링크로 연결된 스킬 폴더를 지원하며, 이러한 위치를 검색할 때 심볼릭 링크의 대상을 따라갑니다.

이 위치들은 스킬 작성과 로컬 탐색을 위한 것입니다.
재사용 가능한 스킬을 단일 레포지토리 밖으로 배포하거나 필요에 따라 커넥터와
함께 묶으려면 [플러그인](https://developers.openai.com/plugins/build/plugins)을 사용하세요.

## 플러그인으로 스킬 배포하기

스킬 폴더를 직접 사용하는 방식은 로컬 작성과 레포지토리 범위의
워크플로우에 가장 적합합니다. 재사용 가능한 스킬을 배포하거나,
두 개 이상의 스킬을 하나로 묶거나, 스킬을 커넥터와 함께 제공하려면
[플러그인](https://developers.openai.com/plugins/build/plugins)으로 패키징하세요.

플러그인은 하나 이상의 스킬을 포함할 수 있습니다. 또한 등록된 MCP 서버
연결, 번들로 제공되는 MCP 서버 구성, 표시용 애셋을 하나의 패키지로
선택적으로 묶을 수 있습니다.

## 로컬에서 사용할 선별된 스킬 설치하기

로컬 Codex 환경에 기본 제공 스킬 외의 선별된 스킬을 추가하려면 `$skill-installer`를 사용하세요. 예를 들어 `$linear` 스킬을 설치하려면 다음과 같이 합니다:

```bash
$skill-installer linear

설치 프로그램에 다른 레포지토리의 스킬을 다운로드하도록 요청할 수도 있습니다.
Codex는 새로 설치된 스킬을 자동으로 감지합니다. 스킬이 표시되지 않으면
Codex를 다시 시작하세요.

이 방법은 로컬 설정과 실험에 사용하세요. 직접 만든 스킬을 재사용 가능한 형태로
배포하려면 플러그인을 사용하는 것이 좋습니다.

## 로컬 Codex 스킬 활성화 또는 비활성화

스킬을 삭제하지 않고 비활성화하려면 `[[skills.config]]` 항목을 `~/.codex/config.toml`에 추가하세요:

```toml
[[skills.config]]
path = "/path/to/skill/SKILL.md"
enabled = false

`~/.codex/config.toml` 파일을 변경한 후 Codex를 다시 시작하세요.

## 선택적 메타데이터

`agents/openai.yaml`을 추가하면 [ChatGPT 데스크톱 앱](/ko-KR/codex/app)의 UI 메타데이터를 구성하고, 호출 정책을 설정하며, 도구 종속성을 선언해 스킬을 더 원활하게 사용할 수 있습니다.

```yaml
interface:
  display_name: "Optional user-facing name"
  short_description: "Optional user-facing description"
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
  brand_color: "#3B82F6"
  default_prompt: "Optional surrounding prompt to use the skill with"

policy:
  allow_implicit_invocation: false

dependencies:
  tools:
    - type: "mcp"
      value: "openaiDeveloperDocs"
      description: "OpenAI Docs MCP server"
      transport: "streamable_http"
      url: "https://developers.openai.com/mcp"

`allow_implicit_invocation`(기본값: `true`): `false`로 설정하면 Codex는 사용자 프롬프트에 따라 스킬을 암시적으로 호출하지 않습니다. 명시적인 `$skill` 호출은 계속 작동합니다.

## 모범 사례

- 각 스킬은 하나의 작업에만 집중하도록 만드세요.
- 결정론적 동작이나 외부 도구가 필요한 경우가 아니라면 스크립트보다 지침을 우선하세요.
- 입력과 출력을 명시하고 각 단계를 명령문으로 작성하세요.
- 스킬 설명에 따라 프롬프트를 테스트하여 스킬이 올바른 조건에서 실행되는지 확인하세요.

더 많은 예시는
[GitHub CI 복구](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci),
[PDF](https://github.com/openai/skills/tree/main/skills/.curated/pdf),
[Linear](https://github.com/openai/skills/tree/main/skills/.curated/linear),
[openai/skills](https://github.com/openai/skills) 및
[에이전트 스킬 사양](https://agentskills.io/specification)을 참조하세요. 설치 가능한 형태로
배포하려면 [플러그인](https://developers.openai.com/plugins/build/plugins)을 권장합니다.

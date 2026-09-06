<!-- source: https://learn.chatgpt.com/ko-KR/docs/custom-prompts -->

사용자 지정 프롬프트는 사용 중단 예정(deprecated)입니다. Codex가 명시적으로 또는 암묵적으로 호출할 수 있는 재사용 가능한
  지침에는 [스킬](/ko-KR/codex/build-skills)을 사용하세요.

사용자 지정 프롬프트(사용 중단 예정(deprecated))를 사용하면 Markdown 파일을 재사용 가능한 프롬프트로 만들어 Codex CLI와 Codex IDE 확장에서 모두 슬래시 명령어로 호출할 수 있습니다.

사용자 지정 프롬프트는 명시적으로 호출해야 하며 로컬 Codex 홈 디렉터리(예: `~/.codex`)에 저장되므로 레포지토리를 통해 공유되지 않습니다. 프롬프트를 공유하거나 Codex가 암묵적으로 호출하도록 하려면 [스킬을 사용하세요](/ko-KR/codex/build-skills).

1. 프롬프트 디렉터리를 만드세요:

   ```bash
   mkdir -p ~/.codex/prompts

2. 재사용할 지침을 담은 `~/.codex/prompts/draftpr.md` 파일을 만드세요:

   ```markdown
   ---
   description: Prep a branch, commit, and open a draft PR
   argument-hint: [FILES=<paths>] [PR_TITLE="<title>"]
   ---

   Create a branch named `dev/<feature_name>` for this work.
   If files are specified, stage them first: $FILES.
   Commit the staged changes with a clear message.
   Open a draft PR on the same branch. Use $PR_TITLE when supplied; otherwise write a concise summary yourself.

3. 새 프롬프트를 로드하도록 Codex를 다시 시작하세요(CLI 세션을 다시 시작하고, IDE 확장을 사용 중이면 다시 로드하세요).

예상 결과: 슬래시 명령어 메뉴에 `/prompts:draftpr`을 입력하면 프런트 매터의 설명과 함께 사용자 지정 명령어가 표시되며, 파일과 PR 제목은 선택 사항이라는 힌트도 나타납니다.

## 메타데이터와 인수 추가

Codex는 다음에 세션이 시작될 때 프롬프트 메타데이터를 읽고 자리표시자를 해석합니다.

- **설명:** 팝업에서 명령어 이름 아래에 표시됩니다. YAML 프런트 매터에 `description:` 형식으로 설정하세요.
- **인수 힌트:** 어떤 매개변수를 받는지 `argument-hint: KEY=<value>` 형식으로 문서화하세요.
- **위치 기반 자리표시자:** `$1`부터 `$9`까지는 명령어 뒤에 공백으로 구분해 입력한 인수로 확장됩니다. `$ARGUMENTS`에는 모든 인수가 포함됩니다.
- **명명된 자리표시자:** 예를 들어 `$FILE`, `$TICKET_ID` 같은 대문자 이름을 사용하고 값을 `KEY=value` 형식으로 입력하세요. 공백이 포함된 값은 따옴표로 묶으세요(예: `FOCUS="loading state"`).
- **리터럴 달러 기호:** 확장된 프롬프트에서 `$` 하나를 출력하려면 `$$` 형식으로 작성하세요.

프롬프트 파일을 수정한 후 업데이트를 로드하려면 Codex를 다시 시작하거나 새 채팅을 여세요. Codex는 프롬프트 디렉터리에서 Markdown 형식이 아닌 파일을 무시합니다.

## 사용자 지정 명령어 호출 및 관리

1. Codex(CLI 또는 IDE 확장)에서 `/`를 입력해 슬래시 명령어 메뉴를 여세요.
2. `prompts:` 또는 프롬프트 이름(예: `/prompts:draftpr`)을 입력하세요.
3. 필요한 인수를 입력하세요:

   ```text
   /prompts:draftpr FILES="src/pages/index.astro src/lib/api.ts" PR_TITLE="Add hero animation"

4. Enter 키를 눌러 확장된 지침을 전송하세요(필요하지 않은 인수는 생략해도 됩니다).

예상 결과: Codex가 `draftpr.md`의 내용을 확장하면서 자리표시자를 입력한 인수로 바꾼 다음, 결과를 메시지로 전송합니다.

`~/.codex/prompts/` 아래의 파일을 수정하거나 삭제하여 프롬프트를 관리하세요. Codex는 이 폴더의 최상위 Markdown 파일만 스캔하므로 각 사용자 지정 프롬프트를 하위 디렉터리가 아닌 `~/.codex/prompts/` 바로 아래에 두세요.

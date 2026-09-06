<!-- source: https://learn.chatgpt.com/ko-KR/docs/automations -->

반복 작업이 백그라운드에서 실행되도록 예약하세요. ChatGPT 웹과 모바일에서는
지원 대상 요금제를 이용하면 지원되는 앱 이벤트로도 작업을 실행할 수 있습니다. **예약됨에서**
활성, 일시 중지, 완료 상태의 작업과 최근 실행 내역을 검토하세요. 더 복잡한 작업에는
예약 작업과 [스킬](/ko-KR/codex/build-skills)을 함께 사용할 수 있습니다.

ChatGPT 데스크톱 앱의 예약 작업은 로컬 프로젝트를 대상으로
프로젝트 디렉터리나 격리된 작업 트리에서 실행할 수 있습니다. 예약 작업에 로컬 파일이 필요하면
컴퓨터를 켜 두고 앱을 실행해 두세요.

워크스페이스에서 예약 작업이 활성화되어 있으면 웹의 채팅이나
ChatGPT Work에서 작업을 만들고 **예약됨에서** 실행을 관리하세요. Web 작업은
업로드된 컨텍스트와 연결된 도구를 사용할 수 있지만,
컴퓨터의 폴더에서 직접 작업할 수는 없습니다.

Codex CLI는 예약됨 관리 인터페이스를 제공하지 않습니다. ChatGPT 웹이나
데스크톱 앱에서 예약 작업을 만들고 관리하세요. CLI에서는 프롬프트, 스킬 또는 스크립트를
미리 준비하고 테스트할 수 있습니다.

IDE 확장은 예약됨 관리 인터페이스를 제공하지 않습니다.
ChatGPT 웹이나 데스크톱 앱에서 예약 작업을 만들고 관리하세요. IDE 확장에서는
프롬프트, 스킬 또는 워크스페이스 변경 사항을 미리 준비하고
테스트할 수 있습니다.

<a id="managing-tasks"></a>
<a id="ask-codex-to-create-or-update-automations"></a>
<a id="ask-chatgpt-to-create-or-update-scheduled-tasks"></a>
<a id="thread-automations"></a>
<a id="scheduled-tasks-in-threads"></a>
<a id="scheduled-tasks-in-chats"></a>
<a id="schedule-work-from-a-task"></a>
<a id="schedule-a-task-inside-a-chat"></a>
<a id="test-automations"></a>
<a id="test-scheduled-tasks"></a>
<a id="worktree-cleanup-for-automations"></a>
<a id="worktree-cleanup-for-scheduled-tasks"></a>
<a id="permissions-and-security-model"></a>
<a id="examples"></a>
<a id="automatically-create-new-skills"></a>
<a id="stay-up-to-date-with-your-project"></a>
<a id="combining-automations-with-skills-to-fix-your-own-bugs"></a>
<a id="combining-scheduled-tasks-with-skills-to-fix-your-own-bugs"></a>

## 웹에서 예약 작업 관리

**예약됨을** 열어 작업 상태와 최근 실행 내역을 검토하세요. 실행할 때마다
저장된 프롬프트로 시작해야 한다면 독립형 예약 작업을 사용하세요. ChatGPT가
기존 컨텍스트를 유지하며 같은 채팅으로 돌아오게 하려면
채팅 안에서 예약 작업을 사용하세요.

웹의 예약 작업은 해당 채팅에서 사용할 수 있는 업로드된 파일, 연결된 도구, 스킬,
플러그인을 사용할 수 있습니다. 실행 사이에 로컬 폴더나 작업 트리를
계속 사용할 수 있도록 유지하지는 않습니다. 반복 실행에도 적용할 지침은 작업 프롬프트나
첨부된 스킬에 넣고, 필요한 소스 자료는 접근 가능한 프로젝트, 업로드한 자료 또는
연결된 서비스에 보관하세요.

작업을 예약하기 전에 일반 웹 채팅에서 프롬프트를 테스트하세요.
처음 몇 번의 실행을 검토한 다음, 결과 범위가 너무 넓거나 추가 컨텍스트가 필요하면
프롬프트, 도구 또는 실행 주기를 조정하세요.

## 앱 이벤트로 작업 실행

지원 대상 요금제에서는 Gmail, Slack 또는 GitHub에서 지원되는 이벤트가
발생할 때 예약 작업을 실행할 수 있습니다. 이벤트 기반 작업은 ChatGPT 웹과
모바일에서 사용할 수 있습니다. ChatGPT 데스크톱 앱, Codex CLI 또는
IDE 확장에서는 사용할 수 없습니다.

ChatGPT에 작업을 만들어 달라고 요청한 다음, 감지할 이벤트와 이벤트가 발생했을 때
수행할 작업을 설명하세요. 트리거는 작업의 실행 시점을, 저장된 프롬프트는
실행할 때마다 수행할 내용을 결정합니다. 한 작업에 여러 이벤트 트리거를 사용할 수 있지만,
이벤트 트리거와 시간 기반 일정을 함께 사용할 수는 없습니다.

지원되는 이벤트 트리거는 다음과 같습니다:

- **Gmail:** 새 수신 메시지. 필요에 따라 발신자나 제목으로 필터링할 수 있습니다.
- **Slack:** 선택한 채널의 새 메시지. 필요에 따라 작성자와
  스레드 답글 포함 여부로 필터링할 수 있습니다. 반응, 메시지 수정 및 삭제,
  다이렉트 메시지는 지원하지 않습니다.
- **GitHub:** 레포지토리의 Pull Request 활동. Pull Request,
  작성자, 제목 또는 레이블로 필터링하고, 검토, 댓글, 커밋 업데이트를 실행 조건에 포함할지 아니면
  병합할 때만 작업을 실행할지 선택하세요.

작업을 만들기 전에 앱을 연결하고 권한을 부여하세요. Slack에서는
작업이 모니터링하는 모든 채널에 `@ChatGPT`를 추가하세요. GitHub에서는 연결된 앱에
레포지토리 접근 권한이 있어야 합니다.

조건에 맞는 이벤트 여러 개가 짧은 시간 안에 발생하면 ChatGPT가 이를
한 번의 실행으로 묶어서 처리할 수 있습니다. **예약됨을** 열어 대기 중인 이벤트를 확인하거나 **지금 실행을**
선택해 처리하세요.

사용 가능 여부는 요금제와 워크스페이스 설정에 따라 달라집니다. 관리형
워크스페이스에서는 관리자가 **이벤트 기반
예약 작업 허용** 권한으로 접근을 제어할 수 있습니다.

예를 들어 텔레메트리 오류를 평가하고 수정 사항을 제출하거나
최근 코드베이스 변경 사항에 대한 보고서를 작성하도록 작업을 예약할 수 있습니다. 같은 컨텍스트를
계속 사용해야 하는 작업은 [기존 채팅 안에서 예약하세요](#schedule-a-task-inside-a-chat).

프로젝트 단위 예약 작업을 사용하려면 컴퓨터를 켜 두고 ChatGPT
데스크톱 앱을 실행해 두세요. 예약된 실행 시점에도 선택한 프로젝트를
디스크에서 사용할 수 있어야 합니다.

Git 레포지토리에서는 예약 작업을 로컬
프로젝트에서 실행할지 새 [작업 트리](/ko-KR/codex/environments/git-worktrees)에서 실행할지 선택할 수 있습니다. 두 옵션 모두
백그라운드에서 실행됩니다. 작업 트리를 사용하면 예약 작업의 변경 사항을 완료하지 않은 로컬
작업과 분리할 수 있습니다. 반면 로컬 프로젝트에서 실행하면 현재 작업 중인
파일이 수정될 수 있습니다. 버전 관리를 하지 않는 프로젝트에서는 예약 작업이
프로젝트 디렉터리에서 직접 실행됩니다.

모델과 추론 수준은 기본 설정을 그대로 사용해도 됩니다. 예약 작업의 실행 방식을 더 세밀하게 제어하려면
직접 선택할 수도 있습니다.

예약 작업이 ChatGPT 로그인으로 `gpt-5.4` 또는 `gpt-5.4-mini`를 사용한다면,
해당 모델의 지원이 종료되는 2026년 8월 31일 전에 작업을 업데이트하세요. `gpt-5.4` 대신
`gpt-5.6-terra`를, `gpt-5.4-mini` 대신 `gpt-5.6-luna`를 사용하세요.

  

예약 작업은 기본 샌드박스 설정으로 사용자 개입 없이 실행됩니다. 작업을 성공적으로 수행할 수 있는
최소한의 접근 권한부터 시작하고, 네트워크나 더 광범위한 파일 접근 권한은 필요한 경우에만
부여하세요. [샌드박스 이해하기](/ko-KR/codex/sandboxing).

## 예약 작업 관리

ChatGPT 데스크톱 앱 사이드바의 **예약됨에서** 모든 예약 작업과
실행 내역을 확인할 수 있습니다.

**예약됨** 화면은 받은 편지함 역할을 합니다. 확인 결과가 있는 예약 작업의 실행 내역이
여기에 표시되며, 확인이 필요한 실행에는 읽지 않음 표시가 나타납니다.

  

독립형 예약 작업은 예약된 실행마다 새 채팅을 시작하고
 **예약됨에** 결과를 보고합니다. 각 실행이 독립적이어야 하거나
예약 작업 하나를 하나 이상의 프로젝트에서 실행해야 할 때 사용하세요. 사용자 지정
주기가 필요하면 사용자 지정 일정 설정을 사용하세요. 고급 일정을 설정하려면
다음과 같은 RFC 5545 반복 규칙(RRULE)을 수정하세요.
`RRULE:FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0`.

Git 레포지토리의 각 예약 작업은 로컬 프로젝트나
전용 백그라운드 [작업 트리](/ko-KR/codex/environments/git-worktrees)에서 실행할 수 있습니다. 예약 작업의 변경 사항을
완료하지 않은 로컬 작업과 분리하려면
작업 트리를 사용하세요. 예약 작업이 메인 체크아웃에서 직접 작업하게 하려면 로컬 모드를 사용하되,
현재 편집 중인 파일이 변경될 수 있다는 점에 유의하세요.
버전 관리를 하지 않는 프로젝트에서는 예약 작업이 프로젝트 디렉터리에서
직접 실행됩니다. 같은 예약 작업을 둘 이상의 프로젝트에서 실행할 수도 있습니다.

웹의 ChatGPT Work에서 만들었거나 데스크톱 앱의 ChatGPT Work 또는
Codex에서 만든 예약 작업은 플러그인을 사용할 수 있습니다. 예약 작업은 스킬도 사용할 수 있습니다.
예약 작업을 쉽게 유지 관리하고 팀 간에 공유하려면
[스킬](/ko-KR/codex/build-skills)로 수행할 작업을 정의하고 도구와 컨텍스트를 제공하세요.
워크플로우가 자동 도구 선택에 의존해서는 안 되는 경우에는
작업 프롬프트에서 특정 스킬을 선택하거나 호출하세요.

## ChatGPT에 예약 작업 생성 또는 업데이트 요청하기

ChatGPT 또는 Codex 채팅에서 예약 작업을 만들고 업데이트할 수 있습니다.
수행할 작업과 실행 시점, 매번 현재 채팅으로 돌아올지
새 채팅을 시작할지를 설명하세요. ChatGPT는 프롬프트 초안을 작성하고 적절한
실행 대상을 선택하며, 작업 범위나 실행 주기가 바뀌면
예약 작업을 업데이트할 수 있습니다.

예를 들어 배포가 완료될 때까지 현재 채팅에서 후속 확인을 하도록 예약해 달라고
ChatGPT에 요청할 수 있습니다. 또는 프로젝트를 정기적으로 확인하는
독립형 예약 작업을 만들어 달라고 요청할 수 있습니다.

스킬로도 예약 작업을 만들거나 업데이트할 수 있습니다. 예를 들어 Pull Request를
지속적으로 관리하는 스킬은 GitHub 플러그인으로 PR 상태를 확인하고
새로운 검토 피드백을 반영해 수정하는 예약 작업을 설정할 수 있습니다.

## 채팅 안에서 작업 예약

ChatGPT가 일정에 따라 기존 채팅으로 돌아오게 하려면 해당 채팅 안에서 작업을
예약하세요. 예약 작업은 매번 새 프롬프트로 시작하지 않고
채팅의 기존 컨텍스트를 사용합니다.

채팅 안의 예약 작업에서는 후속 확인을 자주 반복해야 할 때 분 단위 간격을 사용하고,
특정 시각에 확인해야 할 때는 일간 또는 주간
일정을 사용할 수 있습니다.

다음과 같은 작업은 채팅 안에서 예약하세요:

- 장시간 실행되는 작업이 완료될 때까지 확인하기
- 지원되는 개별 앱 이벤트에 대응하는 대신 정기적인 스냅샷이 필요할 때
연결된 소스를 일정한 주기로 확인하기
- ChatGPT에 일정한 주기로 검토 루프를 이어 가도록 알리기
- PR 상태 확인과 새로운 피드백 반영처럼 플러그인을 사용하는 스킬 기반 워크플로우
실행하기
- 컨텍스트를 유지하며 진행 중인 조사 또는 트리아지 채팅 이어 가기

각 실행이 독립적이어야 하거나
확인 결과가 **예약됨에** 별도 실행 내역으로 표시되어야 한다면 독립형 예약 작업을 사용하세요.

채팅 안에서 작업을 예약할 때는 반복 실행에도 유효한 프롬프트를 작성하세요. 예약 작업이 실행될 때마다
ChatGPT가 할 일, 보고할 중요한 내용이 있는지 판단하는 방법,
실행을 멈추거나 사용자에게 입력을 요청할 시점을 설명해야 합니다.

## 예약 작업 테스트

작업을 예약하기 전에 일반 채팅에서 프롬프트를 직접
테스트하세요. 그러면 다음 사항을 확인할 수 있습니다:

- 프롬프트가 명확하고 범위가 올바르게 설정되어 있습니다.
- 선택했거나 기본값으로 둔 모델, 추론 수준, 도구가 예상대로 작동합니다.
- 생성된 결과를 검토할 수 있습니다.

예약 실행을 시작하면 처음 몇 번의 결과를 검토하고 필요에 따라
프롬프트나 실행 주기를 조정하세요.

ChatGPT 데스크톱 앱에서는 예약 작업 프롬프트에
`$skill-name`을 사용해 스킬을 명시적으로 호출할 수 있습니다.

## 예약 작업용 작업 트리 정리

Git 레포지토리에서 작업 트리를 사용하도록 선택한 경우, 실행 주기가 짧으면 시간이 지나면서
작업 트리가 많이 생길 수 있습니다. 더 이상 필요 없는 예약 실행 내역은 보관 처리하고,
작업 트리를 유지하려는 경우가 아니라면 실행 내역을 고정하지 마세요.

## 권한 및 보안 모델

예약 작업은 사용자 개입 없이 실행되며 기본 샌드박스 설정을 사용합니다.

이러한 제한을 쉽게 설명한 내용은
[샌드박스 개요](/ko-KR/codex/sandboxing)를 참고하세요. 파일 시스템 및 네트워크 규칙은
[권한](/ko-KR/codex/permissions)을 참고하세요.

- 샌드박스가 **읽기 전용** 모드이면, 도구 호출에 파일 수정,
  네트워크 접근 또는 컴퓨터의 앱 사용이 필요한 경우 해당 호출은 실패합니다.
  샌드박스 설정을 워크스페이스 쓰기로 변경하는 것을 고려하세요.
- 샌드박스가 **workspace-write** 모드이면, 도구 호출에
  워크스페이스 외부의 파일 수정, 네트워크 접근 또는 컴퓨터의 앱 사용이
  필요한 경우 해당 호출은 실패합니다. 샌드박스 밖에서 실행할 명령어를 선별해
  허용 목록에 추가하려면 [규칙](/ko-KR/codex/agent-configuration/rules)을 사용할 수 있습니다.
- 샌드박스가 **전체 권한** 모드이면, ChatGPT가 사용자에게 묻지 않고
  파일을 변경하거나 명령어를 실행하고 네트워크에 접근할 수 있어
  백그라운드 예약 작업에 높은 위험이 따릅니다. 샌드박스 설정을 워크스페이스 쓰기로 변경하고,
  [규칙](/ko-KR/codex/agent-configuration/rules)을 사용해 에이전트가 전체 권한으로 실행할 수 있는 명령어를
  선별하여 지정하는 것을 고려하세요.

관리형 환경에서는 관리자가 요구 사항을 강제 적용해
이러한 동작을 제한할 수 있습니다. 예를 들어 `approval_policy =
"never"` 설정을 금지하거나 허용되는 샌드박스 모드를 제한할 수 있습니다. 자세한 내용은
[관리자가 강제 적용하는 요구 사항(`requirements.toml`)](/ko-KR/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml)을 참고하세요.

조직 정책에서 허용하는 경우 예약 작업은 `approval_policy = "never"` 설정을
사용합니다. 관리자 요구 사항에서 `approval_policy = "never"` 설정을 허용하지 않으면,
예약 작업에는 선택한 권한 모드의
승인 방식이 대신 적용됩니다.

## 예시

### 새 스킬 자동으로 만들기

```markdown
Scan all of the `~/.codex/sessions` files from the past day and if there have been any issues using particular skills, update the skills to be more helpful. Personal skills only, no repo skills.

If there’s anything we’ve been doing often and struggle with that we should save as a skill to speed up future work, let’s do it.

Definitely don't feel like you need to update any- only if there's a good reason!

Let me know if you make any.

### 프로젝트의 최신 상황 파악하기

```markdown
Look at the latest remote origin/master or origin/main . Then produce an exec briefing for the last 24 hours of commits that touch 

Formatting + structure:

- Use rich Markdown (H1 workstream sections, italics for the subtitle, horizontal rules as needed).
- Preamble can read something like “Here’s the last 24h brief for <directory>:”
- Subtitle should read: “Narrative walkthrough with owners; grouped by workstream.”
- Group by workstream rather than listing each commit. Workstream titles should be H1.
- Write a short narrative per workstream that explains the changes in plain language.
- Use bullet points and bolding when it makes things more readable
- Feel free to make bullets per person, but bold their name

Content requirements:

- Include PR links inline (e.g., [#123](...)) without a “PRs:” label.
- Do NOT include commit hashes or a “Key commits” section.
- It’s fine if multiple PRs appear under one workstream, but avoid per‑commit bullet lists.

Scope rules:

- Only include changes within the current cwd (or main checkout equivalent)
- Only include the last 24h of commits.
- Use `gh` to fetch PR titles and descriptions if it helps.
  Also feel free to pull PR reviews and comments

### 예약 작업과 스킬을 함께 사용해 자신이 만든 버그 수정하기

자신의 커밋으로 발생한 버그 수정을 시도하는 새 `$recent-code-bugfix` 스킬을 만들고 [개인 스킬에 저장하세요](/ko-KR/codex/build-skills#where-to-save-skills).

```markdown
---
name: recent-code-bugfix
description: Find and fix a bug introduced by the current author within the last week in the current working directory. Use when a user wants a proactive bugfix from their recent changes, when the prompt is empty, or when asked to triage/fix issues caused by their recent commits. Root cause must map directly to the author’s own changes.
---

# Recent Code Bugfix

## Overview

Find a bug introduced by the current author in the last week, implement a fix, and verify it when possible. Operate in the current working directory, assume the code is local, and ensure the root cause is tied directly to the author’s own edits.

## Workflow

### 1) Establish the recent-change scope

Use Git to identify the author and changed files from the last week.

- Determine the author from `git config user.name`/`user.email`. If unavailable, use the current user’s name from the environment or ask once.
- Use `git log --since=1.week --author=<author>` to list recent commits and files. Focus on files touched by those commits.
- If the user’s prompt is empty, proceed directly with this default scope.

### 2) Find a concrete failure tied to recent changes

Prioritize defects that are directly attributable to the author’s edits.

- Look for recent failures (tests, lint, runtime errors) if logs or CI outputs are available locally.
- If no failures are provided, run the smallest relevant verification (single test, file-level lint, or targeted repro) that touches the edited files.
- Confirm the root cause is directly connected to the author’s changes, not unrelated legacy issues. If only unrelated failures are found, stop and report that no qualifying bug was detected.

### 3) Implement the fix

Make a minimal fix that aligns with project conventions.

- Update only the files needed to resolve the issue.
- Avoid adding extra defensive checks or unrelated refactors.
- Keep changes consistent with local style and tests.

### 4) Verify

Attempt verification when possible.

- Prefer the smallest validation step (targeted test, focused lint, or direct repro command).
- If verification cannot be run, state what would be run and why it wasn’t executed.

### 5) Report

Summarize the root cause, the fix, and the verification performed. Make it explicit how the root cause ties to the author’s recent changes.

그런 다음 새 예약 작업을 만드세요:

```markdown
Check my commits from the last 24h and submit a $recent-code-bugfix.

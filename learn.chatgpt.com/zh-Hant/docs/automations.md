<!-- source: https://learn.chatgpt.com/zh-Hant/docs/automations -->

設定週期性排程，讓任務在背景執行。在網頁版和行動版 ChatGPT 中，
若您使用符合資格的方案，也可以由支援的應用程式事件觸發任務。
您可以在「 **已排程**」中檢視啟用中、已暫停及已完成的任務，以及近期執行記錄。
您也可以將排程任務與[技能](/zh-Hant/codex/build-skills)搭配使用，處理更複雜的工作。

在 ChatGPT 桌面版應用程式中，排程任務可以處理本機專案，
並在專案目錄或隔離的工作樹中執行。若排程任務需要本機檔案，
請讓電腦保持開機，並讓應用程式持續執行。

若您的工作區已啟用排程任務，您可以從網頁版的「對話」或
ChatGPT Work 建立任務，並在「 **已排程**」中管理執行記錄。
網頁版任務可以使用已上傳的上下文和已連線的工具，
但無法直接處理您電腦上資料夾內的內容。

Codex CLI 不提供「已排程」管理介面。請使用網頁版 ChatGPT
或桌面版應用程式建立及管理排程任務。您可以先用 CLI
準備及測試提示詞、技能或指令碼。

IDE 擴充功能不提供「已排程」管理介面。
請使用網頁版 ChatGPT 或桌面版應用程式建立及管理排程任務。
您可以先用 IDE 擴充功能準備及測試提示詞、技能，
或工作區中的變更。

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

## 在網頁版管理排程任務

開啟「 **已排程** 」，檢視任務狀態和近期執行記錄。
如果每次執行都應從已儲存的提示詞開始，請使用獨立排程任務。
如果希望 ChatGPT 返回同一個對話並沿用現有上下文，
請在該對話中使用排程任務。

網頁版排程任務可使用該對話能存取的已上傳檔案、已連線工具、技能和
外掛程式。不同次執行之間，不會保留可供使用的本機資料夾或工作樹。
請將長期適用的指示寫入任務提示詞或附加的技能，
並將必要的來源資料放在可存取的專案、上傳檔案
或已連線的服務中。

為任務設定排程前，請先在網頁版的一般對話中測試提示詞。
檢視前幾次執行結果，
若結果範圍太廣或需要更多上下文，再調整提示詞、工具或執行頻率。

## 透過應用程式事件觸發任務

若您使用符合資格的方案，排程任務可在支援的 Gmail、Slack 或
GitHub 事件發生時執行。由事件觸發的任務適用於網頁版和行動版 ChatGPT，
但不適用於 ChatGPT 桌面版應用程式、Codex CLI
或 IDE 擴充功能。

請 ChatGPT 建立任務，並描述要監看的事件，以及事件發生時
應執行的動作。觸發條件決定任務何時執行；已儲存的提示詞
決定每次執行的工作內容。單一任務可使用多個事件觸發條件，
但不能同時使用事件觸發條件和時間排程。

支援的事件觸發條件包括：

- **Gmail：** 新收到的郵件，可選擇依寄件者或主旨篩選。
- **Slack：** 所選頻道中的新訊息，可選擇依傳送者篩選，
  並決定是否包含討論串回覆。
  不支援表情符號回應、訊息編輯、訊息刪除或私訊。
- **GitHub：** 程式碼庫中的 Pull Request 活動。可依 Pull Request、
  作者、標題或標籤篩選，並選擇是否要讓審查、留言、提交更新
  觸發任務，或僅在合併時觸發。

建立任務前，請先連線至應用程式並完成授權。若使用 Slack，
請將 `@ChatGPT` 加入任務監看的每個頻道。若使用 GitHub，
已連線的應用程式必須具備該程式碼庫的存取權。

當多個符合條件的事件在短時間內接連發生時，ChatGPT 可能會將它們
合併於一次執行中處理。開啟「 **已排程** 」即可檢視待處理事件，或選擇「 **立即執行**」
來處理這些事件。

是否可用取決於您的方案與工作區設定。
在受管理的工作區中，管理員可透過「 **允許由事件觸發的
排程任務** 」權限控制存取。

例如，您可以排程任務來評估遙測錯誤並提交修正，
或針對程式碼庫的近期變更建立報告。
若持續進行的工作需要沿用相同上下文，請[在現有對話中排程任務](#schedule-a-task-inside-a-chat)。

對於以專案為範圍的排程任務，請讓電腦保持開機，
並讓 ChatGPT 桌面版應用程式持續執行。任務預定執行時，
所選專案必須仍存在於磁碟上且可供存取。

在 Git 程式碼庫中，您可以選擇讓排程任務在本機專案中執行，
或在新的[工作樹](/zh-Hant/codex/environments/git-worktrees)中執行。兩種方式都會在背景執行。
工作樹可將排程任務的變更與尚未完成的本機工作分開；
在本機專案中執行則可能修改您仍在編輯的檔案。
在未使用版本控制的專案中，排程任務會直接在
專案目錄中執行。

您也可以保留模型和推理強度的預設設定；
若想進一步控制排程任務的執行方式，也可以明確指定模型和推理強度。

如果排程任務透過 ChatGPT 登入使用 `gpt-5.4` 或 `gpt-5.4-mini`，
請在這些模型於 2026 年 8 月 31 日停止提供前更新任務。請將 `gpt-5.4` 替換為
`gpt-5.6-terra`，並將 `gpt-5.4-mini` 替換為 `gpt-5.6-luna`。

  

排程任務會使用您的預設沙盒設定，在無人監督下執行。
請先授予能讓任務成功執行的最小存取權限，僅在必要時才授予網路
或更廣泛的檔案存取權。[瞭解沙盒](/zh-Hant/codex/sandboxing)。

## 管理排程任務

在 ChatGPT 桌面版應用程式側邊欄的「 **已排程** 」中，
即可找到所有排程任務及其執行記錄。

「 **已排程** 」檢視畫面就像您的收件匣。有發現事項的排程任務執行記錄會顯示在這裡，
需要您留意的執行記錄則會顯示未讀標記。

  

獨立排程任務在每次排程執行時都會開始新對話，
並在「 **已排程**」中回報結果。如果每次執行應彼此獨立，
或同一項排程任務需要在一個或多個專案中執行，請使用這類任務。
如需自訂執行頻率，請使用自訂排程控制項。如需進階排程，
請編輯其 RFC 5545 週期規則（RRULE），例如
`RRULE:FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0`。

在 Git 程式碼庫中，每項排程任務都可以在本機專案中執行，
或在專用的背景[工作樹](/zh-Hant/codex/environments/git-worktrees)中執行。
如果想將排程任務的變更與尚未完成的本機工作隔離，請使用工作樹。
如果想讓排程任務直接在主要簽出目錄中工作，請使用本機模式，
但請注意，它可能會修改您正在編輯的檔案。
在未使用版本控制的專案中，排程任務會直接在專案目錄中執行。
同一項排程任務也可以在多個專案中執行。

透過網頁版 ChatGPT Work，或桌面版應用程式中的 ChatGPT Work 或
Codex 建立的排程任務，都可以使用外掛程式。排程任務也可以使用技能。
為了讓排程任務易於維護並可供不同團隊共用，請使用
[技能](/zh-Hant/codex/build-skills)定義動作，並提供工具和上下文。
如果工作流程不應依賴自動選擇工具，請在任務提示詞中
選取或叫用特定技能。

## 請 ChatGPT 建立或更新排程任務

您可以在 ChatGPT 或 Codex 對話中建立及更新排程任務。
請描述工作內容、執行時間，
以及每次執行應返回目前的對話還是開始新對話。
ChatGPT 可以草擬提示詞、選擇適當的執行位置，
並在任務範圍或執行頻率變更時更新任務。

例如，您可以在等待部署完成時，請 ChatGPT 從目前的對話
排程後續追蹤；也可以請它建立獨立排程任務，
定期檢查某個專案。

技能也可以建立或更新排程任務。例如，持續監看 Pull Request 的技能
可以設定排程任務，透過 GitHub 外掛程式檢查 PR 狀態，
並依據新的審查意見進行修正。

## 在對話中排程任務

如果希望 ChatGPT 按排程返回現有對話，請在該對話中排程任務。
排程任務會沿用該對話的現有上下文，
而不是每次都從新的提示詞開始。

對話中的排程任務可以使用以分鐘為單位的間隔，持續進行主動追蹤；
如果需要在特定時間確認進度，
也可以設定每日或每週排程。

在對話中排程任務的用途包括：

- 檢查長時間執行的作業，直到完成
- 需要定期取得快照，而非回應某個支援的應用程式事件時，
依固定頻率檢查已連線的來源
- 提醒 ChatGPT 依固定頻率持續進行審查
- 執行由技能驅動且使用外掛程式的工作流程，例如檢查 PR 狀態
並處理新的意見回饋
- 延續進行中的研究或問題分流對話，同時保留上下文

如果每次執行應彼此獨立，或發現事項應以個別執行記錄
顯示在「 **已排程**」中，請使用獨立排程任務。

在對話中排程任務時，請確保提示詞能長期適用。
提示詞應說明 ChatGPT 每次排程執行時該做什麼、如何判斷是否有重要事項需要回報，
以及何時停止或向您詢問。

## 測試排程任務

為任務設定排程前，請先在一般對話中手動測試提示詞。
這有助於確認：

- 提示詞清楚明確，且範圍設定正確。
- 所選或預設的模型、推理強度和工具都能如預期運作。
- 產生的輸出可供審查。

開始排程執行後，請檢視前幾次輸出，
並視需要調整提示詞或執行頻率。

在 ChatGPT 桌面版應用程式中，您可以在排程任務的提示詞中
使用 `$skill-name`，明確觸發技能。

## 清理排程任務的工作樹

如果您為 Git 程式碼庫選用工作樹，頻繁執行的排程可能會逐漸建立大量工作樹。
請封存不再需要的排程執行記錄；
除非打算保留其工作樹，否則請避免釘選執行記錄。

## 權限與安全性模型

排程任務會使用您的預設沙盒設定，在無人監督下執行。

如需這些界限的白話說明，請參閱
[沙盒概覽](/zh-Hant/codex/sandboxing)。如需瞭解檔案系統與網路規則，
請參閱[權限](/zh-Hant/codex/permissions)。

- 如果您的沙盒模式為 **唯讀**，工具呼叫若需要
  修改檔案、存取網路或操作您電腦上的應用程式，就會失敗。
  請考慮將沙盒設定改為工作區寫入。
- 如果您的沙盒模式為 **workspace-write**，工具呼叫若需要
  修改工作區以外的檔案、存取網路或操作您電腦上的應用程式，
  就會失敗。您可以透過
  [規則](/zh-Hant/codex/agent-configuration/rules)，將特定指令加入允許清單，讓這些指令在沙盒外執行。
- 如果您的沙盒模式為 **完整存取權**，在背景執行的排程任務會有
  較高風險，因為 ChatGPT 可能在未先詢問您的情況下修改檔案、執行指令
  及存取網路。請考慮將沙盒設定改為工作區寫入，並
  使用[規則](/zh-Hant/codex/agent-configuration/rules)，指定智慧體可以
  使用完整存取權執行哪些指令。

如果您使用的是受管理的環境，管理員可以透過
強制規定限制這些行為。例如，他們可以禁止使用 `approval_policy =
"never"`，或限制允許使用的沙盒模式。請參閱
[管理員強制規定（`requirements.toml`）](/zh-Hant/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml)。

如果您的組織政策允許，排程任務會使用 `approval_policy = "never"`。
如果管理員規定禁止使用 `approval_policy = "never"`，
排程任務就會改採您所選權限模式
的核准方式。

## 範例

### 自動建立新技能

```markdown
Scan all of the `~/.codex/sessions` files from the past day and if there have been any issues using particular skills, update the skills to be more helpful. Personal skills only, no repo skills.

If there’s anything we’ve been doing often and struggle with that we should save as a skill to speed up future work, let’s do it.

Definitely don't feel like you need to update any- only if there's a good reason!

Let me know if you make any.

### 掌握專案最新動態

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

### 結合排程任務與技能，修正自己引入的錯誤

建立名為 `$recent-code-bugfix` 的新技能，用來嘗試修正您自己的提交所引入的錯誤，並[將它儲存在您的個人技能中](/zh-Hant/codex/build-skills#where-to-save-skills)。

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

接著，建立新的排程任務：

```markdown
Check my commits from the last 24h and submit a $recent-code-bugfix.

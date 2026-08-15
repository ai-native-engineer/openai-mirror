<!-- source: https://academy.openai.com/public/resources/ai-skills-jam-for-k-12-educators-salt-lake-city-2026-07-22 -->

# AI Skills Jam for K-12 Educators: Salt Lake City

![AI Skills Jam for K-12 Educators: Salt Lake City](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-Academy-Event-Card-Templates-8--5c724fb4-6478-4acf-9bcb-2a5c71b4eab9-1784772307149.jpeg?fit=scale-down&width=1200)

## Slides and the follow-along site from our event

July 23, 2026 · Last updated on August 10, 2026

![AI Skills Jam for K-12 Educators: Salt Lake City](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-Academy-Event-Card-Templates-8--5c724fb4-6478-4acf-9bcb-2a5c71b4eab9-1784772307149.jpeg?fit=scale-down&width=1200)

Thank you for being part of the AI Skills Jam for K-12 Educators! Revisit the presentation and educator demos from Jam Day and keep jamming with the Learning Activities on the  [follow-along site](https://openai-k12-jam.vercel.app/) (password: K12JAM).

﻿ [Click here](https://docs.google.com/presentation/d/11yU-CGY__r7tEHUwgyIa9RxHZfzZ-Bjq4G4eAtZFAwY/edit?usp=sharing) to view and use the cards to post on social media. Please remember to use  <#OpenAIAcademy>#OpenAIK12EducatorsJam

View our slides from the day below:

Experiencing slow loading? [Download](https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/EXT-SLC-AI-Skills-Jam-for-K-12-Educators-1f3ec11d-919f-449c-8bb2-6daa9f6060f4-1786380999059.pdf) the file to view.

﻿

Moving work from Jam Day Workspace to another Workspace:

We know many of you are excited to continue jamming after yesterday. The SLC K-12 Edu Jam demo workspace will remain open for the next month. Before moving to another workspace, please preserve your work using the steps below.

1. Export your ChatGPT conversations

The demo workspace has data export enabled. Each person can export their own conversations and associated data:

1. Sign in to ChatGPT and confirm that you are in the Edu Jam workspace.

2. Open your profile menu and select Settings.

3. Select Data controls.

4. Under Export data, select Export.

5. If prompted, verify your account through email, return to ChatGPT, and restart the export.

6. Select Confirm export.

7. When the export email arrives, download the ZIP file while signed in to the same account that requested it.

﻿

Exports can take up to seven days, and the download link expires after 24 hours. The ZIP may contain conversations.json, files used in conversations, and related metadata. Each user can export only their own data.

OpenAI’s Edu export instructions:  <https://help.openai.com/en/articles/20001279-exporting-data-from-a-chatgpt-edu-workspace>﻿

2. Preserve projects created with Codex

Codex project files and outputs created on your computer remain on that computer unless you move or share them. However, do not assume that the Codex task history associated with the demo workspace will appear after you sign in to another workspace.

Before signing out:

1. Open each local project in Codex.

2. Send Codex the preservation prompt below.

3. Let Codex inspect the project and write the important context into durable project files.

4. Review Codex’s readiness report and address anything it identifies as existing only in a conversation, an untracked file, or another temporary location.

5. If permitted by district policy, back up the complete project folder to district-approved storage.

6. Sign out of the demo workspace, sign in to the district workspace, and reopen the same local project folder in Codex.

﻿

ChatGPT Work and Codex FAQ:  <https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex>﻿

Codex project-preservation prompt

Text:

*Prepare this project so it can be safely continued after I sign out of my current ChatGPT/Codex workspace and sign in to a different workspace.*

*Your goal is to make the project self-contained on disk so that a fresh Codex session can open this folder, understand the project, and continue the work without relying on this conversation history.*

*Please do the following:*

*1. Inspect the entire project folder and any project context available in this task. Review the repository structure, documentation, configuration, source files, generated assets, and current work in progress.*

*2. Check the project's current state, including:*

*- Git branch and status, if this is a Git repository*

*- Modified, uncommitted, untracked, and relevant ignored files*

*- Important outputs or decisions that currently exist only in this conversation*

*- Incomplete work, known issues, blockers, and next steps*

*- The last working or verified state of the project*

*3. Preserve the important context in durable Markdown files:*

*- Update the existing AGENTS.md file with stable instructions that a future Codex session should follow.*

*- If no AGENTS.md exists, create one at the appropriate project root.*

*- Create or update docs/PROJECT\_HANDOFF.md for the current implementation state, work in progress, decisions, blockers, and recommended next actions.*

*- Update the README or other existing documentation only where that is the appropriate canonical location.*

*- Preserve existing documentation and manual edits. Add or revise information carefully rather than replacing useful content wholesale.*

*4. Document, as applicable:*

*- The project's purpose and intended outcome*

*- Architecture and major components*

*- Canonical files and important directories*

*- Setup, build, run, test, and validation commands*

*- Required tools and dependencies*

*- Environment-variable names and configuration requirements, but never secret values*

*- Important product or technical decisions and their rationale*

*- External services, data sources, APIs, or local assets the project depends on*

*- Current work in progress*

*- Known bugs, limitations, and unresolved questions*

*- A prioritized list of next steps*

*- How a future Codex session can verify that the project still works*

*5. Identify anything that could be lost or become difficult to recover after switching workspaces, especially:*

*- Information that exists only in Codex conversation history*

*- Untracked or ignored local files*

*- Files stored outside this project folder*

*- Unsaved generated assets*

*- External links or resources that require the current account*

*- Work that has not been written to disk*

*6. Do not expose or write passwords, tokens, credentials, private keys, or other secrets into the documentation. Record only the name and purpose of any required secret or environment variable.*

*7. Do not delete, reset, clean, move, commit, push, or substantially rewrite project files unless I explicitly ask. Do not change the project's behavior merely to prepare this handoff.*

*8. After writing the documentation, re-read every file you created or changed and verify that it is accurate and internally consistent.*

*Finish with a "Workspace-switch readiness report" that lists:*

*- Files created or updated*

*- What project knowledge is now preserved*

*- Any information you could not preserve*

*- Local, untracked, ignored, or external items that still require manual attention*

*- Whether the project is ready to reopen from a fresh Codex session*

*- The exact first prompt I should use after signing in to the new workspace*

*If you cannot inspect part of the project or cannot write the required files, stop and explain the exact limitation instead of claiming the handoff is complete.*

First prompt after signing in to the new workspace

Text:

*Open and assess this project as a continuation of previous work. Read AGENTS.md, docs/PROJECT\_HANDOFF.md, the README, and any other documentation they reference. Then inspect the current project state and summarize the goal, architecture, last verified status, outstanding risks, and recommended next action. Do not make changes until you have confirmed that the documented state matches the files currently on disk.*

Having trouble? Please reach out to [[email protected]](/cdn-cgi/l/email-protection)

## Popular

Blog

[K-12: Prompt Pack for Administrators (Principals, Curriculum Leads)](/public/clubs/k-12-administrators-and-district-leaders-gcxd3/blogs/k-12-prompt-pack-for-administrators)

By Juliann Igo

Blog

[K-12: Prompt Pack for IT Staff (Technology Directors, Coordinators, and Support Teams)](/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/k-12-prompt-pack-for-it-staff)

By Juliann Igo

Blog

[A 12-week AI pilot for faster audits and more unclaimed property returned](/public/blogs/north-carolina-department-of-state-treasurer-chatgpt-pilot-audit)

Dive in

## Related

Resource

[AI Skills Jam for K-12 Educators: Phoenix](/public/resources/ai-skills-jam-for-k-12-educators-phoenix-2026-07-22)

Jul 23rd, 2026 • Views 34

Resource

[APAC Disaster Management AI Skills Jam: Learn Sessions Companion](/public/resources/apac-disaster-management-ai-skills-jam-learn-sessions-companion-2026-06-10)

Jun 10th, 2026 • Views 537

Resource

[AI Skills Jam for K-12 Educators: San Bernadino](/public/resources/ai-skills-jam-for-k-12-educators-san-bernadino-2026-07-22)

Jul 23rd, 2026 • Views 46

Resource

[AI Skills Jam for Disaster Management Professionals](/public/resources/ai-skills-jam-for-disaster-management-professionals-2026-03-29)

Mar 29th, 2026 • Views 1.2K

Resource

[AI Skills Jam for K-12 Educators: Phoenix](/public/resources/ai-skills-jam-for-k-12-educators-phoenix-2026-07-22)

Jul 23rd, 2026 • Views 34

Resource

[AI Skills Jam for K-12 Educators: San Bernadino](/public/resources/ai-skills-jam-for-k-12-educators-san-bernadino-2026-07-22)

Jul 23rd, 2026 • Views 46

Resource

[AI Skills Jam for Disaster Management Professionals](/public/resources/ai-skills-jam-for-disaster-management-professionals-2026-03-29)

Mar 29th, 2026 • Views 1.2K

Resource

[APAC Disaster Management AI Skills Jam: Learn Sessions Companion](/public/resources/apac-disaster-management-ai-skills-jam-learn-sessions-companion-2026-06-10)

Jun 10th, 2026 • Views 537

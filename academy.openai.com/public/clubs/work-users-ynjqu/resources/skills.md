<!-- source: https://academy.openai.com/public/clubs/work-users-ynjqu/resources/skills -->

[Work Users](/en/public/clubs/work-users-ynjqu/overview)

[navigation.content](/en/public/clubs/work-users-ynjqu/content)

Article

February 25, 2026 · Last updated on May 29, 2026

# Skills

![Skills](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Work-Users-Cover-Images-85--020c7915-f579-4476-af19-643c7d47b6f8-1772554679393.jpeg?fit=scale-down&width=1200)

# Workplace & Business

# Advanced & Builder Skills

## Shareable, easy to build, and works across all products and surfaces.

![Skills](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Work-Users-Cover-Images-85--020c7915-f579-4476-af19-643c7d47b6f8-1772554679393.jpeg?fit=scale-down&width=1200)

## **Introducing skills in ChatGPT**

Skills turn the way you already work into reusable workflows that ChatGPT can follow consistently—so you spend less time re-explaining steps, formats, and requirements, and more time getting to a solid result.

If you’ve ever found yourself reusing the same prompt or pasting the same template again and again, skills are designed for that problem.

In this article, you’ll learn what skills are, when they help most, how to build and use them, and what admins should know when enabling them for a team. *Note that this article covers using skills within ChatGPT for new users, but skills can be exported and imported into other tools that support the* [*Agent Skills format*](https://agentskills.io/home)*.*

## **What are skills?**

A **skill** is a reusable, shareable workflow that tells ChatGPT how to do a specific task. Instead of starting from scratch each time, you save the “how” once so it can be applied reliably whenever the task comes up.

A skill typically includes:

* A name and description that help ChatGPT recognize when the skill is relevant.

* The actual workflow steps/instructions—usually written in a simple file called SKILL.md.

* Resources the workflow depends on, like templates, examples, brand guidelines, schemas, or tool/app access.

See the [Help Center](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) for more information.

## **Why use skills?**

Skills are most useful when getting a good output from ChatGPT depends on following a repeatable approach—especially when there are multiple steps, strict formatting, or policies to follow.

Skills help with:

* **Consistency:** fewer missed sections, less drift in tone or format, closer adherence to preferred format

* **Built-in best practices:** lightweight enough for everyday users, but grounded in SME-approved workflows.

* **Sharing the playbook:** teams can use the same standard process directly in ChatGPT instead of relying on tribal knowledge.

* **Reuse across surfaces:** build once, apply broadly (including across ChatGPT experiences).

### **What’s a** **SKILL.md** **file?**

This file format might be new to you, so let’s break down what you’ll see when you create a skill from a chat.

A **SKILL.md** file is the skill’s playbook: a plain-text set of instructions that tells ChatGPT how to run a workflow consistently. It’s written in **Markdown** (the “.md” part), a lightweight formatting style that uses simple symbols—like # for headings and - for lists—so the file is easy to read and edit in almost any tool.

![](https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/some-file-c4361b33-e5fc-457f-b12c-f495bb1d8020-1772161908423.png)

Because it’s plain text and Markdown-based, **SKILL.md is portable**: you can share it, version it, and reuse it across different tools. It’s also designed as an [**open and standardized format**](https://agentskills.io/home), so you may see the same pattern used by other AI apps and platforms.

The file generally outlines:

* what the skill does,

* what inputs it needs,

* the steps it should follow,

* the required output format,

* and the checks it should run before finalizing.

![](https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/some-file-9e795ef5-a65f-4476-87d9-657eb2d767c8-1772640976329.jpeg)

## **How to build and use skills**

### **1) Think of a repeatable task**

Good first skills come from work you already do often—where consistency matters (monthly reporting, recurring exec updates, a standard customer email + follow-up checklist, compliance-safe summaries, etc).

Ensure you know the input (what the user will typically provide, like files, links, context, fields), the output (the expected format, tone, length, etc. of the final product), and any guardrails (what must be included—and what must not happen),

There are a few different patterns we usually see in skills:

* **Reusable processes (multi-step workflows):** “Run the playbook” tasks where steps matter: ex. compliance-ready reporting, finance reconciliation logic, or “create an exec report from two CSVs.”

* **Tool-based workflows (consistent use of systems):** “How to pull the right thing from the right system,” such as: “Use Gong to pull new insights for an account,” or “Create an exec summary using two connected sources.”

* **Conventions and standards (voice, structure, quality bar):** Skills that enforce format and style even when content changes—like “draft a blog post using our style guide and these uploaded notes.”

*Design tip: skills often work best as* ***small building blocks*** *you can mix and match, rather than one massive end-to-end skill. If a workflow is long, split it into phases (research and write report → write email update and share).*

Take a look at your job description. What processes do you do over and over? What does "good" look like for this?

![](https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/some-file-60a82fb4-74cf-41aa-9159-950931dc1fb4-1772554477355.jpeg)

### **2) Write down the instructions**

*If you’re new to building skills, the best way to start is just by starting a new chat and creating a prompt that starts with “Build me a skill….”. Note that you can also build skills outside of ChatGPT and upload them.*

Ask ChatGPT to create a skill, and fill in the rest of the prompt with a description of the skill you want ChatGPT to build. We recommend you capture:

* job-to-be-done (what it’s for)

* required inputs

* step-by-step process (numbered steps help)

* required output format (uploaded examples help)

* final quality checks

*Tip: drafting the workflow by dictation, or speaking to ChatGPT, often speeds up the first version.*

### **3) Review and install the skill**

ChatGPT will then provide you with a draft of the skill and the ability to install it. You’ll see a modal appear with the draft of the skill. You can continue to refine, or click **Install** to install for yourself.

![](https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/some-file-5bd25409-fb00-4f8d-be2d-baa23fcb1c87-1772161908367.png)

### **4) Use it in day-to-day work**

Once enabled in your workspace, ChatGPT can use a relevant skill automatically—or you can select one explicitly by @-mentioning it. Skills can also be used across experiences like custom GPTs and projects and can incorporate apps (formerly connectors)

You can also combine multiple skills for multi-phase work (extract → draft → QA → package).

### **5) Share it—or keep it personal**

If allowed by your workspace settings, you can share your skill with others in your workspace, or even install it on their behalf. Note that workspace owners have full control of who can share and install skills

![](https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/some-file-1c126a30-e76f-40a3-b0e7-2db7005d4dfc-1772161908411.png)

## Using skills across other tools

Skills can be exported and imported into other tools that support the [Agent Skills format](https://agentskills.io/home), including in OpenAI tools like [Codex](https://developers.openai.com/codex/skills/).

## **Skills vs custom GPTs**

Skills could be a better option for your repeatable workflows because they teach ChatGPT to follow defined steps, conventions, and formatting more predictably. And because skills can stay “always on” when relevant, your users don’t have to remember to call a specific GPT to get the right output.

During the beta, we’ll learn from customer feedback on how teams use skills alongside GPTs. After that time, we’ll offer options for both users and admins to convert GPTs into skills when they’re better suited for repeatable workflows.

Here’s a simple framework to think about how these fit together:

* **Skills** = reusable workflows that teach ChatGPT how to complete specific tasks

* **GPTs** = goal-oriented, custom versions of ChatGPT that extend the expertise of a team, or help with time-based projects

* **Projects** = teams can work from the same context, files, and conversations towards an end goal

## **Practical skill use cases for work**

Check out some additional examples of each type of skill across roles.

|  |  |  |  |
| --- | --- | --- | --- |
| **Department** | **Reusable process skill** | **Tool-based skill** | **Conventions/standards skill** |
| Marketing | **campaign-brief-builder**  Create a skill that turns a rough marketing idea into a complete campaign brief, including the goal, target audience, key message, channels, and timeline. | **multi-channel-performance-digest** Create a skill that pulls key metrics from connected analytics sources and drafts a weekly multi-channel performance summary with insights and recommended actions. | **brand-voice-content-polish**  Create a skill that rewrites marketing drafts to match our brand voice and standard content structure. |
| Sales | **discovery-to-next-steps**  Create a skill that converts discovery call notes into customer pain points, qualification summary, and a clear next-steps plan. | **sf-opportunity-health-check**  Create a skill that reviews Salesforce opportunity fields and recent activity, plus call notes if connected, to flag deal risks and recommend actions. | **outbound-email-personalization-style** Create a skill that produces outbound sales emails using our team’s preferred structure, tone, and length. |
| Finance | **monthly-close-narrative**  Create a skill that drafts a monthly close readout summarizing variance drivers, key risks, and decisions needed. | **budget-vs-actuals-explainer**  Create a skill that pulls budget and actuals from connected sheets or finance systems and explains variances in plain language. | **finance-memo-standard**  Create a skill that formats financial analysis into a consistent finance memo with assumptions, method, results, and sensitivities. |
| Engineering | **design-doc-to-plan** Create a skill that converts a design doc into an execution plan with milestones, owners, dependencies, and open questions. | **jira-sprint-planner-from-notes**  Create a skill that turns sprint planning notes into Jira-ready epics and stories with acceptance criteria and estimate placeholders. | **pr-description-and-changelog-style** Create a skill that standardizes pull request descriptions and release notes according to our engineering conventions. |
| Operations | **ops-playbook-writer** Create a skill that turns an operational process into a standard operating procedure with steps, handoffs, SLAs, and exception handling. | **ops-report-from-sheets**  Create a skill that pulls operational KPIs from connected spreadsheets and drafts a weekly operations report. | **ops-update-template** Create a skill that writes operations updates in a consistent format covering what changed, impact, actions, and owners. |
| Customer Success | **qbr-storyline-builder** Create a skill that builds a QBR outline covering outcomes, adoption, value delivered, risks, and renewal plan. | **account-brief-from-systems**  Create a skill that pulls account context from connected CRM, call, and usage sources to create an account briefing and recommended priorities. | **customer-comms-tone-guide**  Create a skill that drafts customer emails in our preferred tone—clear, direct, and professional—with standard sections. |
| IT | **incident-postmortem-writer**  Create a skill that produces a blameless incident postmortem including timeline, root cause, and prevention actions. | **servicenow-ticket-triage**  Create a skill that summarizes new ServiceNow tickets, or similar IT tickets, and proposes routing, priority, and next actions. | **it-change-communication-template**  Create a skill that writes IT change notices with consistent language for risk, timing, and user impact. |
| Legal | **contract-review-summary**  Create a skill that creates a structured contract review summary with issues, fallback positions, and requested redlines. | **policy-qa-from-knowledgebase** Create a skill that looks up and summarizes policy language from connected legal knowledge sources and cites the relevant sections. | **legal-memo-standard** Create a skill that drafts internal legal memos in a consistent format with the question, short answer, analysis, and recommendation. |
| HR | **interview-kit-builder** Create a skill that creates role scorecards, interview questions, and evaluation rubrics from a job scope. | **job-post-from-requisition**  Create a skill that pulls role details from Workday or a similar system and drafts a job post plus an outreach blurb. | **people-comms-style** Create a skill that writes HR announcements in our standard tone with inclusive and compliance-friendly phrasing. |
| Management | **weekly-status-multi-format**  Create a skill that turns raw team updates into three outputs: a team update, an executive summary, and a risk-and-asks note. | **team-health-digest** Create a skill that pulls signals from connected tools such as Jira, Sheets, and Slack to summarize team momentum, blockers, and current focus. | **1on1-agenda-template** Create a skill that generates consistent 1:1 agendas with coaching prompts, goals, and follow-up items. |
| Executives | **exec-decision-brief** Create a skill that converts messy inputs into a one-page decision brief with options, tradeoffs, and a recommendation. | **exec-briefing-from-systems** Create a skill that pulls cross-functional signals from connected sources to draft a daily or weekly executive briefing. | **board-readout-style** Create a skill that writes board-ready updates with crisp structure, metrics-first framing, and minimal jargon. |

## **Admin FAQs**

See the [Help Center](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) for more information.

### **Accessing and managing skills**

**Are skills available in my workspace?**Yes. During the initial beta, skills are off by default—workspace owners can enable them in workspace settings.

**My team uses Codex and other AI tools. Can the same skills be used across products?**While they don’t sync across products yet, OpenAI skills follow the [Agent Skills](https://agentskills.io/home) open standard—so you can download them from one product and install them in another.

**What controls do I have on member use of skills in my workspace?**Workspace owners can control the ability for users in their workspace to create and use skills, to make their created skills available to others in their workspace, and to install skills on behalf of other users. This can be managed in your [Permissions and Roles](https://chatgpt.com/admin/permissions?tab=general) settings, and can be managed via RBAC.

### **Enterprise security & privacy**

**What is a skill from a security perspective?**A skill is a reusable workflow packaged as instructions (and sometimes examples/resources) so ChatGPT follows an agreed process more consistently. For admins, skills can help standardize “how work gets done” in a way that’s visible and easier to govern than ad-hoc prompting.

**Do skills change the Enterprise data privacy posture (including training)?**Skills don’t introduce a new category of data use on their own—they structure the work people are already doing in ChatGPT.

**If I am on a credit-based plan, how do skills affect my team’s credit usage?**
Skills themselves have no impact on credits, but if a user has many complex skills, ChatGPT might more frequently default to thinking models to accomplish these tasks.

**What happens when a skill uses apps or other external tools?**Skills only instruct ChatGPT to use the tools and apps it already has access to, so the same permissions and org controls already apply and governance aligns with your existing connector/app policies.

Table Of Contents

[ChatGPT for any role](/en/public/clubs/work-users-ynjqu/resources/chatgpt-for-any-role)

[Prompting](/en/public/clubs/work-users-ynjqu/resources/prompting)

[ChatGPT for marketing](/en/public/clubs/work-users-ynjqu/resources/use-cases-marketing)

[How marketing teams use Codex: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/how-marketing-teams-use-codex-webinar-resource-guide-2026-06-22)

Jun 23rd, 2026 • Views 175

[26:13](/en/public/clubs/work-users-ynjqu/videos/how-business-operations-teams-use-codex-2026-06-17)

Video

[How business operations teams use Codex [Recording]](/en/public/clubs/work-users-ynjqu/videos/how-business-operations-teams-use-codex-2026-06-17)

Jun 18th, 2026 • Views 646

[26:34](/en/public/clubs/work-users-ynjqu/videos/how-marketing-teams-use-codex-recording-2026-06-22)

Video

[How marketing teams use Codex [Recording]](/en/public/clubs/work-users-ynjqu/videos/how-marketing-teams-use-codex-recording-2026-06-22)

Jun 23rd, 2026 • Views 400

[How business operations teams use Codex: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/how-business-operations-teams-use-codex-webinar-resource-guide-2026-06-17)

Jun 18th, 2026 • Views 230

[How marketing teams use Codex: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/how-marketing-teams-use-codex-webinar-resource-guide-2026-06-22)

Jun 23rd, 2026 • Views 175

[26:34](/en/public/clubs/work-users-ynjqu/videos/how-marketing-teams-use-codex-recording-2026-06-22)

Video

[How marketing teams use Codex [Recording]](/en/public/clubs/work-users-ynjqu/videos/how-marketing-teams-use-codex-recording-2026-06-22)

Jun 23rd, 2026 • Views 400

[How business operations teams use Codex: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/how-business-operations-teams-use-codex-webinar-resource-guide-2026-06-17)

Jun 18th, 2026 • Views 230

[26:13](/en/public/clubs/work-users-ynjqu/videos/how-business-operations-teams-use-codex-2026-06-17)

Video

[How business operations teams use Codex [Recording]](/en/public/clubs/work-users-ynjqu/videos/how-business-operations-teams-use-codex-2026-06-17)

Jun 18th, 2026 • Views 646

<!-- source: https://academy.openai.com/public/resources/chatgpt-enterprise-user-analytics-guide -->

[Admins](/en/public/clubs/admins-6o6xf/overview)

[navigation.content](/en/public/clubs/admins-6o6xf/content)

# ChatGPT Enterprise workspace analytics guide

![ChatGPT Enterprise workspace analytics guide](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Admins-Cover-Images-23--f28feaa8-a1a8-42a0-b4de-e39744a35367-1773166023775.jpeg?fit=scale-down&width=1200)

# Leaders & Admins

# Workplace & Business

# Deployment & Adoption

## Drive action by understanding how your team is using ChatGPT Enterprise

March 10, 2026 · Last updated on May 29, 2026

![ChatGPT Enterprise workspace analytics guide](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Admins-Cover-Images-23--f28feaa8-a1a8-42a0-b4de-e39744a35367-1773166023775.jpeg?fit=scale-down&width=1200)

Workspace analytics gives you a broad view of how adoption is progressing in your ChatGPT Enterprise workspace. It shows current usage patterns across seats, active users, trends, and benchmarks, with filters by date and group so you can see how adoption differs across parts of the organization.

Use it to answer practical questions about your adoption:

1. Who has access, and how is adoption changing over time?

2. Which groups are building repeat usage, and which are still early?

3. Where should we look more closely to understand what is working and what may need support?

Workspace analytics helps you move from a high-level readout to a closer investigation. You can filter the data, compare cohorts, and drill into specific usage patterns to understand what is gaining traction and where it may be worth scaling what is already working.

## **What you can do with workspace analytics**

Workspace analytics helps you:

* **Show trends:** show activation and engagement trends leaders can understand quickly.

* **Diagnose drop-offs:** identify where adoption is stalling (access → activation → weekly usage → depth).

* **Target interventions:** pick specific teams/cohorts and measure whether your changes worked.

* **Scale visibility safely:** share read-only analytics with the right stakeholders.

## **How to access workspace analytics**

Workspace owners, admins, and analytics viewers (a new role) have access to workspace analytics in Workspace Settings > Workspace Analytics.

Consider assigning **analytics viewer** access to AI champions/enablement leads, department leads who are accountable for adoption, and program owners who prepare regular readouts. This keeps reporting and action planning focused without expanding admin permissions.

The first tab that will load is your overview tab, which shows:

* **Seats purchased:** licenses your org pays for

* **Seats enabled:** licenses assigned to real users (via provisioning/invites/SSO)

* **Seats activated:** enabled users who have begun using the product

* **WAU:** users active weekly

* **Power users:** enabled users in the top 20% by message usage, with activity in 3+ tools

See more details about data definitions in our [Help Center](https://help.openai.com/en/articles/10875114-user-analytics-for-chatgpt-enterprise-and-edu).

## **Interpreting workspace analytics: funnel + trend**

Think of workspace analytics as a window into how adoption is developing across your organization. It lets you see how usage evolves over time—from access, to first use, to repeat use, and eventually deeper adoption. If progress slows at any stage, focus on resolving that bottleneck before investing further downstream.

### **Key questions:**

|  |  |  |
| --- | --- | --- |
| **Question** | **Where to look** | **What it usually means** |
| Are people getting access? | Seats purchased vs. seats enabled | Setup/provisioning is (or isn’t) working |
| Are people starting to use ChatGPT? | Seats enabled vs. active users | Onboarding is (or isn’t) turning access into first use |
| Is usage becoming a habit? | WAU trend lines | Adoption is compounding—or fading after initial interest |
| What’s driving usage changes? | Breakdowns by model/tool/connector + task insights | What actually changed month-over-month |
| Are we “healthy” for our stage? | Benchmarks | Directional comparison to peer set (triage, not a verdict) |

## **How to read core metrics**

|  |  |  |
| --- | --- | --- |
| **Metric** | **What it tells you** | **If it’s weak, try this next** |
| **Purchased vs enabled** | Whether rollout mechanics are working | Fix provisioning, SSO, invitations, group rules; confirm comms/instructions |
| **Enabled vs active** | Whether people got past setup and started using ChatGPT | Run onboarding that’s tied to one real workflow; use starter prompts + manager reinforcement |
| **WAU trend** | Whether usage is becoming routine | Compare trend before/after a specific intervention (training, comms, workflow pack) |
| **WAU per activated user** | Whether activated users are returning consistently | Look for “one-and-done” patterns; add habit-forming nudges, office hours, role-based prompt packs |
| **Messages per WAU** | How much work is being done by weekly users | Often signals depth; investigate what workflows are driving volume (task insights) |
| **Benchmarks** | Whether activation/engagement/depth look typical for peers | Use to prioritize where to investigate—not to auto-judge performance |

## **Diving deeper**

The overview tab helps you understand the top-line story: how many people have access, how many are active, and whether usage is growing over time. The Users, GPTs, Projects, and Skills tabs help you explain *why* those patterns are happening by showing where usage is concentrating, what kinds of assets are gaining traction, and which behaviors look repeatable enough to scale.

A useful way to read these tabs is to treat them as a second layer of analysis on top of the overview metrics. If enabled seats are rising but active use is not, the Users tab can help you see which groups have not yet turned access into adoption. If WAU or messages per WAU are rising, the GPTs, Projects, and Skills tabs can help you see whether that growth is tied to a few specific assets or to broader workflow adoption.

* **Users:** See which groups are building repeat usage, which are still early, and where adoption may need more support.

* **GPTs, Projects, and Skills:** Look for assets and workflows that are attracting sustained engagement, not just one-time experimentation.

* **Scaling signals:** When usage is concentrated around a specific GPT, Project, Skill, or team, that can point to a strong use case worth documenting and sharing more broadly.

* **Next step:** Start with the workflows that show repeat engagement, then test focused enablement to help similar teams adopt them.

Across these tabs, look for the same pattern: usage that is not only high, but repeatable. A strong candidate for scaling usually shows up as continued engagement over time, concentration around a specific asset or workflow, and evidence that the pattern is tied to real work rather than one-time experimentation. That is the same reason task insights is useful: it helps connect usage back to concrete jobs to be done and identify workflows worth scaling.

Once you identify a promising GPT, Project, Skill, or high-usage cohort, the next step is not to broadcast it to the whole organization at once. Start by documenting the workflow clearly, identifying which teams have similar needs, and testing a focused intervention such as a workflow pack, office hours session, or manager-led example. Then measure whether adoption grows in the next few weeks using the same overview and deeper tabs. This keeps scaling grounded in evidence rather than anecdotes.

## **Using benchmarks comparison**

Benchmarks give you a directional comparison against others in your industry. They help you answer a narrow question: are your activation, engagement, or depth metrics roughly in range for peers, or is something noticeably ahead or behind? That makes them useful as a reference point, not as a score or verdict.

A good way to use benchmarks is to start with the metric that stands out, then ask what part of the adoption journey it reflects. If activation is low relative to peers, look first at access and onboarding. If weekly activity is low, check whether people found a real workflow, came back after first use, or dropped off after initial curiosity.

Being below benchmark does not automatically mean something is wrong, and above benchmark does not automatically mean adoption is healthy. Use benchmarks to guide better questions, then confirm the story with the rest of your analytics and with conversations with the teams closest to the work.

## **Task insights**

Use task insights to connect activity to concrete jobs to be done. Look for workflows that repeat across teams, where strong usage is tied to a specific task pattern, and where one-time experimentation is not yet turning into repeat behavior.

This is most helpful for:

* Finding **repeatable workflows** worth scaling

* Understanding differences between **high-usage** and **low-usage** teams

* Translating usage telemetry into an enablement plan

## **Reviewing workspace analytics regularly**

Use this as a lightweight monthly operating rhythm for reviewing adoption and choosing your next intervention.

|  |  |  |  |
| --- | --- | --- | --- |
| **Step** | **What to do** | **Output you want** | **Example result statement** |
| **1) Check the funnel** | Calculate purchased → enabled, then enabled → active | A clear “main constraint” statement | “Adoption is limited by activation: many seats are enabled, but a smaller share have started using ChatGPT.” |
| **2) Look at the trend** | WAU trend line | A direction statement: rising / flat / falling | “Weekly active users have been rising steadily over the past month.” |
| **3) Choose two cohorts** | One lagging group + one healthy comparison | A targeted focus area (not the whole company) | “Team A shows strong weekly usage, while Team B has similar access but much lower activity.” |
| **4) Diagnose drivers** | Breakdowns + task insights | A hypothesis about what’s driving the pattern | “The increase in usage appears tied to growing adoption of a connector-based workflow.” |
| **5) Pick one intervention** | Training, workflow pack, office hours, manager message | A single, testable action | “We’ll run a short enablement session for Team B focused on the workflows Team A is using.” |
| **6) Measure before/after** | Compare 2–4 weeks pre/post | A plain-language result statement | “Weekly activity in Team B increased after the targeted training session.” |

## **Example prompts for analysis**

You can go even deeper if you export your data from the analytics dashboard. Below are some simple prompts to analyze the data. Just click on the use case and drop your CSV into chat.
*Tip: Create a Custom GPT or a skill to automate this in the future.*

| Use case | When to use |
| --- | --- |
| ﻿[Generate a weekly AI adoption update for Slack or Teams](https://chat.openai.com/?q=I%20am%20uploading%20one%20or%20more%20ChatGPT%20Workspace%20Analytics%20exports.%20Analyze%20the%20latest%20file%20and%2C%20if%20multiple%20files%20are%20provided%2C%20compare%20them%20to%20show%20week-over-week%20change.%20Write%20a%20concise%20but%20substantive%20weekly%20AI%20adoption%20update%20for%20Slack%20or%20Microsoft%20Teams.%20Include%3A%201)%20a%201-2%20sentence%20headline%20summary%20of%20overall%20workspace%20health%2C%202)%20the%20most%20important%20metric%20changes%20such%20as%20activation%2C%20WAU%2C%20engagement%20depth%2C%20and%20feature%20usage%2C%203)%20notable%20teams%2C%20cohorts%2C%20or%20power%20users%20driving%20growth%2C%204)%20meaningful%20drops%2C%20flat%20areas%2C%20or%20anomalies%20that%20need%20attention%2C%205)%20one%20or%20two%20emerging%20use%20cases%20or%20patterns%20worth%20sharing%2C%20and%206)%202-3%20recommended%20next%20actions.%20Keep%20the%20tone%20clear%2C%20professional%2C%20and%20ready%20to%20paste%20into%20an%20internal%20channel.%20Use%20plain%20language%20and%20avoid%20repeating%20every%20metric%20that%20is%20already%20obvious%20from%20the%20dashboard.)﻿ | Weekly internal status updates for admins, champions, or enablement leads. |
| ﻿[Create an executive-ready AI adoption brief](https://chat.openai.com/?q=I%20am%20uploading%20a%20ChatGPT%20Workspace%20Analytics%20export%20and%20may%20also%20upload%20older%20exports%20for%20comparison.%20Create%20an%20executive-ready%20briefing%20for%20senior%20leaders%20who%20do%20not%20need%20a%20tour%20of%20the%20dashboard.%20Translate%20the%20data%20into%20clear%20business%20insights.%20Focus%20on%3A%201)%20whether%20adoption%20is%20broadening%2C%20deepening%2C%20or%20stalling%2C%202)%20whether%20usage%20suggests%20real%20workflows%20or%20light%20experimentation%2C%203)%20which%20teams%20or%20user%20groups%20appear%20to%20be%20getting%20the%20most%20value%2C%204)%20what%20risks%20or%20gaps%20leaders%20should%20care%20about%2C%205)%20what%20the%20data%20does%20and%20does%20not%20prove%2C%20and%206)%203%20recommended%20leadership%20actions.%20Write%20the%20output%20as%20a%20short%20executive%20memo%20with%20a%20tight%20headline%2C%20an%20overall%20readout%2C%20key%20findings%2C%20risks%2C%20and%20next%20steps)﻿ | Leadership reviews, CIO updates, QBRs, and sponsor briefings. |
| ﻿[Write a weekly champion update for the team](https://chat.openai.com/?q=I%20am%20uploading%20a%20ChatGPT%20Workspace%20Analytics%20export.%20Write%20a%20weekly%20update%20for%20an%20internal%20AI%20champions%20group.%20Focus%20on%20what%20they%20can%20learn%20from%20the%20data%20and%20what%20they%20can%20do%20next.%20Include%3A%201)%20a%20short%20summary%20of%20workspace%20momentum%2C%202)%20the%20most%20important%20behavior%20changes%20or%20use%20case%20signals%2C%203)%20teams%20or%20users%20who%20appear%20to%20be%20building%20repeatable%20workflows%2C%204)%20underused%20areas%20where%20champions%20could%20intervene%2C%20and%205)%20a%20short%20call%20to%20action%20for%20the%20champions%20network.%20Write%20it%20in%20a%20clear%2C%20useful%2C%20non-hypey%20tone)﻿ | Keeping an internal champions network aligned on where to focus. |
| ﻿[Create a targeted enablement plan for under-engaged teams](https://chat.openai.com/?q=I%20am%20uploading%20a%20ChatGPT%20Workspace%20Analytics%20export.%20Identify%20teams%2C%20groups%2C%20or%20cohorts%20with%20low%20activation%20or%20engagement.%20For%20each%20one%2C%20suggest%20a%20targeted%20enablement%20approach.%20Include%20recommended%20training%20topics%2C%20example%20use%20cases%20relevant%20to%20their%20role%2C%20and%20specific%20ways%20to%20introduce%20ChatGPT%20into%20their%20daily%20workflows.%20Focus%20on%20practical%2C%20role-specific%20actions%20rather%20than%20generic%20advice .)﻿ | When certain departments lag behind adoption |
| ﻿[Recommended next enablement content to build](https://chat.openai.com/?q=I%20am%20uploading%20a%20ChatGPT%20Workspace%20Analytics%20export.%20Based%20on%20the%20usage%20patterns%20and%20task%20signals%20in%20the%20data%2C%20recommend%20what%20enablement%20content%20should%20be%20created%20next.%20Examples%20might%20include%20workshops%2C%20guides%2C%20templates%2C%20or%20short%20training%20sessions.%20Explain%20why%20these%20would%20have%20the%20highest%20impact .)﻿ | Planning education or enablement programs. |
| ﻿[Identify power users and explain why they matter](https://chat.openai.com/?q=I%20am%20uploading%20a%20ChatGPT%20Workspace%20Analytics%20export.%20Identify%20the%20users%20or%20teams%20who%20appear%20to%20be%20power%20users%20or%20high-impact%20adopters.%20Do%20not%20just%20rank%20by%20message%20volume.%20Instead%2C%20look%20for%20signals%20of%20consistent%20usage%2C%20workflow%20depth%2C%20feature%20diversity%2C%20and%20evidence%20that%20their%20usage%20may%20be%20repeatable%20or%20valuable.%20Summarize%20who%20stands%20out%2C%20why%20they%20stand%20out%2C%20what%20patterns%20they%20may%20represent%2C%20and%20how%20an%20admin%20or%20champion%20could%20turn%20their%20behavior%20into%20examples%2C%20training%2C%20or%20peer%20enablement)﻿ | Finding internal advocates and use cases worth scaling. |
| ﻿[Create a leadership narrative about AI adoption and value](https://chat.openai.com/?q=I%20am%20uploading%20a%20ChatGPT%20Workspace%20Analytics%20export.%20Write%20a%20leadership%20narrative%20that%20explains%20how%20AI%20adoption%20is%20developing%20in%20this%20organization.%20Use%20the%20data%20to%20tell%20a%20clear%20story%20about%20what%20is%20working%2C%20where%20usage%20is%20maturing%2C%20where%20it%20is%20still%20shallow%2C%20and%20what%20signals%20suggest%20real%20workflow%20value.%20Avoid%20hype%20and%20avoid%20claiming%20ROI%20the%20data%20cannot%20support.%20Include%20a%20short%20section%20called%20What%20this%20data%20suggests%20and%20another%20called%20What%20we%20should%20do%20next)﻿ | When leaders need interpretation, not just metrics. |
| ﻿[Diagnose adoption risks and early warning signs](https://chat.openai.com/?q=I%20am%20uploading%20a%20ChatGPT%20Workspace%20Analytics%20export.%20Analyze%20the%20data%20for%20early%20warning%20signs%20that%20adoption%20may%20stall%2C%20remain%20shallow%2C%20or%20become%20overly%20concentrated%20in%20a%20small%20set%20of%20users.%20Look%20for%20patterns%20such%20as%20declining%20WAU%2C%20flat%20activation%2C%20low%20depth%20of%20usage%2C%20sharp%20drops%20after%20spikes%2C%20or%20limited%20feature%20adoption.%20Explain%20which%20signals%20are%20most%20concerning%2C%20why%20they%20matter%2C%20and%20what%20an%20admin%20or%20champion%20should%20do%20in%20response)﻿ | Spotting issues before they become larger rollout problems. |
| ﻿[Analyze adoption by team using multiple uploaded files](https://chat.openai.com/?q=I%20am%20uploading%20a%20ChatGPT%20Workspace%20Analytics%20export%20and%20one%20or%20more%20additional%20files%20such%20as%20a%20department%20mapping%2C%20HRIS%20export%2C%20or%20team%20list.%20Combine%20these%20files%20to%20analyze%20adoption%20patterns%20by%20team%2C%20function%2C%20or%20cohort.%20Identify%20which%20groups%20have%20the%20broadest%20adoption%2C%20which%20show%20deeper%20usage%2C%20which%20appear%20under-engaged%2C%20and%20what%20differences%20may%20matter%20for%20enablement.%20Summarize%20the%20results%20in%20plain%20language%20and%20end%20with%20recommended%20actions%20for%20the%20groups%20that%20need%20attention)﻿ | When you want department-level or cohort-level insights beyond the base export. |
| ﻿[Build a repeatable weekly analytics review template](https://chat.openai.com/?q=I%20am%20uploading%20a%20ChatGPT%20Workspace%20Analytics%20export.%20Use%20it%20to%20generate%20a%20repeatable%20weekly%20analytics%20review%20template%20that%20an%20admin%2C%20program%20manager%2C%20or%20AI%20champion%20could%20reuse%20every%20week.%20The%20template%20should%20include%20sections%20for%20headline%20summary%2C%20key%20metric%20changes%2C%20notable%20teams%20or%20users%2C%20emerging%20use%20cases%2C%20risks%20or%20open%20questions%2C%20and%20recommended%20actions.%20Make%20the%20template%20structured%20enough%20to%20reuse%20but%20written%20in%20plain%20language%20so%20someone%20could%20paste%20in%20fresh%20data%20next%20week%20and%20get%20a%20similar%20output)﻿ | Establishing a durable review cadence and standard format. |

## **Admin FAQ**

Please visit the [OpenAI Help Center](https://help.openai.com/en/articles/10875114-user-analytics-for-chatgpt-enterprise-and-edu) for more detailed information.

**Q: Can admins export the data?**

A: Yes. Admins can generate on-demand CSV exports for Users, GPTs, and Projects. Exports are available for a selected week or month, and custom date ranges are not currently supported.

**Q: Does workspace analytics replace the Compliance API?**

A: No. Workspace analytics is an aggregated analytics experience, not a raw log interface. It does not expose message text, file contents, or item-level compliance records. For raw logs, legal and security workflows, and compliance controls, use the Compliance API.

**Q: Can we segment analytics by team, department, or business unit?**

A: Some views support segmentation by SCIM groups, which can represent teams, departments, or business units depending on how your identity provider is configured. If you need additional breakdowns, export the data and combine it with your internal systems.

**Q: What should admins know about Task Insights privacy and controls?**

A: Task Insights is designed for aggregate analysis only and does not expose individual prompts or conversations. It is enabled by default, and workspace admins or owners can turn it off in Workspace settings under Usage Analytics.

**Q: Can admins customize the impact survey?**

A: No. The impact survey is currently fixed and cannot be customized, though workspace admins and owners can opt out of OpenAI-created impact surveys in Workspace settings.

Table Of Contents

[Empowering and supporting your team](/en/public/clubs/admins-6o6xf/resources/empowering-and-supporting-your-team)

[Welcome to the For Work Admins Track!](/en/public/clubs/admins-6o6xf/resources/welcome-admins)

[Feature controls and integrations with your tools](/en/public/clubs/admins-6o6xf/resources/feature-controls-and-integrations-with-your-tools)

[Communicating about ChatGPT Enterprise to your team](/en/public/clubs/admins-6o6xf/resources/team-communication)

Aug 5th, 2025 • Views 12.2K

[Automate provisioning and unlock actionable analytics with SCIM](/en/public/clubs/admins-6o6xf/resources/scim)

Mar 11th, 2026 • Views 856

[Leading impactful ChatGPT Trainings](/en/public/clubs/admins-6o6xf/resources/leading-impactful-chatgpt-trainings)

Sep 23rd, 2025 • Views 5.5K

[Planning your ChatGPT rollout](/en/public/clubs/admins-6o6xf/resources/planning-your-chatgpt-rollout)

Jul 11th, 2025 • Views 5.8K

[Communicating about ChatGPT Enterprise to your team](/en/public/clubs/admins-6o6xf/resources/team-communication)

Aug 5th, 2025 • Views 12.2K

[Leading impactful ChatGPT Trainings](/en/public/clubs/admins-6o6xf/resources/leading-impactful-chatgpt-trainings)

Sep 23rd, 2025 • Views 5.5K

[Planning your ChatGPT rollout](/en/public/clubs/admins-6o6xf/resources/planning-your-chatgpt-rollout)

Jul 11th, 2025 • Views 5.8K

[Automate provisioning and unlock actionable analytics with SCIM](/en/public/clubs/admins-6o6xf/resources/scim)

Mar 11th, 2026 • Views 856

# ChatGPT Workspace Analytics

<!-- vimeo: 1161527304 | track: English (auto-generated) -->

[▶ Watch on Vimeo](https://vimeo.com/1161527304)

<details>
<summary>자막: ChatGPT Workspace Analytics</summary>

Workspace Analytics gives chat, GPT admins a clear view of adoption Over time, you can see activation and engagement trends spot where usage is stalling and use that signal to guide more targeted rollout decisions. We've expanded workspace analytics with new benchmarks, flexible trend views, impact survey insights, task insights, and easier sharing. Together these updates make it easier to understand adoption and bring the right stakeholders into the review process. Let's see the new experience. First, open your workspace settings, then click on workspace analytics. You'll arrive at the overview tab. Filtering by group allows you to see analytics from specific groups you've set up in your group's tab. Your workspace health chart will show key metrics over time, like weekly active users and number of enabled seats. You can then scroll down through the tab to see data over time in more detail. For example, you can see trends like unique active users and total messages, but also dig more deeply into what models, tools, apps, gpt, and skills your users are interacting with. You can also click into some workspace insights in the weekly summary. Other tabs take you deeper into these overview metrics. For more advanced exploration, you can see individual usage in the user tab as well as filter for AI power users. AI power users are helpful to identify because these users can act as internal advocates for chat GPT adoption, as well as mentors for newer users. The GPTs tab gives more details on custom GPTs that were created and used in your workspace. You can use these to identify valuable use cases and scale them across your teams. You can also see projects in more detail similar to the GPTs and projects tabs. The skills tab helps you see which skills are utilized most often across your workspace, and also trends over time. The benchmarks tab helps you compare key metrics to other workspaces in your industry. You can also switch to a different industry to compare. You can compare metrics like user activation rate, and weekly active usage, as well as model and tool usage. The task insights tab gives you more information about what tasks people in your organization are using. Chat GPT for. If you have skim data configured, you can also see a heat map of tasks across different skim groups. We have enabled an automated impact survey for your users where you can get insights into real feedback from your team on how chat GPT is affecting their productivity. The impact survey is on by default, but can be turned off in your workspace settings. Check out the OpenAI help center for more details about the impact survey and other analytics features. When viewing this overview data, you can choose a different date range to see trends over a longer period of time. You can customize and export of this data by date range. We recommend creating a skill or custom GPT and Chat GPT that analyzes this data when you upload it. We have some recommendations for prompts in the Open AI Academy. We've added a new role type called analytics viewer. This is a good role for internal champions and team leads who wanna have access to workspace analytics, but don't need full admin privileges. Find more resources for how to drive adoption of AI with your team in the Open AI Academy. I.

</details>

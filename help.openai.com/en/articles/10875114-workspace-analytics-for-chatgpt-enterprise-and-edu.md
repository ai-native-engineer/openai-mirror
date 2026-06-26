<!-- source: https://help.openai.com/en/articles/10875114-workspace-analytics-for-chatgpt-enterprise-and-edu -->

# Workspace analytics for ChatGPT Enterprise and Edu

Understand adoption, engagement, and how teams use ChatGPT across your workspace with built-in analytics and reporting.

Updated: 14 hours ago

*This article outlines what’s included in workspace analytics and how to navigate the dashboard to understand adoption and engagement across your workspace.*  
  
*For guidance on how to operationalize these insights (playbooks, enablement motions, champion programs), see our Academy guide:* [*ChatGPT Enterprise workspace analytics guide*](https://academy.openai.com/public/clubs/admins-6o6xf/resources/chatgpt-enterprise-user-analytics-guide)

# Overview

Workspace analytics in ChatGPT Enterprise and Edu provides a workspace-level view of adoption and usage so you can monitor trends, identify patterns, and report progress over time.

## Accessing workspace analytics

In ChatGPT Enterprise or Edu:

* Go to **Workspace settings** > **Workspace analytics.**
* Visit <https://chatgpt.com/admin/usage>.

## Permissions

Viewing workspace analytics is available to:

* Members with the analytics viewer role
* Workspace admins
* Workspace owners

# Workspace analytics dashboard sections

## Overview

Use **Overview** for a quick health check of adoption and engagement. It provides trend views that help you understand how usage changes over time, including:

* Unique active users
* Total messages
* GPT messages
* Tool messages
* Project, app, and skill usage trends
* Breakdowns by SCIM groups, when configured

  + If your workspace has enabled SCIM, analytics views can be segmented by the groups that are synced from your identity provider. Using SCIM groups that represent real organizational units (such as teams or departments) can help enable more meaningful analytics breakdowns.
  + To learn more about SCIM, please see our collection of articles on [SSO, SCIM, and User Management](https://help.openai.com/collections/11585137).

## Benchmarks

Use **Benchmarks** to compare key adoption and engagement signals against an industry median:

* Activation rate
* WAU (weekly active users) per activated user
* Messages per WAU

You can select a benchmark industry from the in-product dropdown.

## Impact

Use **Impact** to understand workspace-level outcomes reported through optional in-product surveys.  
  
  
**Impact** surfaces aggregated, self-reported signals from the **Impact survey** that help teams understand how ChatGPT affects work across the organization, including:

* Share of respondents reporting positive impact on productivity, time saved, work quality, work satisfaction, ability to complete new tasks, and stakeholder service
* Per-question response distributions
* Survey participation rate (respondents as a share of workspace members)

These signals are intended for directional analysis and organizational insight. They are not compliance logs and do not represent a causal ROI measurement.

For more information on impact surveys, see: [Managing impact surveys in workspace analytics](https://help.openai.com/articles/20001149).

## Task insights

**Task insights** shows aggregated patterns of work in ChatGPT by classifying conversations into broad task categories and topics. It provides workspace-level insights without exposing individual prompts, conversations, or user-level activity.

### Task type

The **Task type** section shows the distribution of conversations across task categories, helping you quickly understand the most common ways ChatGPT is used in your workspace and how those patterns change over time.

### Heat map

The **Heat map** compares task types across a second dimension so you can analyze usage patterns in more detail. Depending on available data, it shows how task types relate to conversation topics or organizational units.  
  
Note: SCIM groups with fewer than 10 members will not appear as a row in the task insights heat map.

### Disabling task insights

The **Task insights** tab and conversation classification are enabled by default. Workspace admins and owners may opt out by:

1. Go to **Workspace settings**
2. Scroll to the **Workspace analytics** section under the **General** tab
3. Turn off **Enable task insights**

## Users

The **Users** section helps with license and engagement tracking:

* Seats purchased
* Seats enabled
* Active users
* Pending invites
* Per-user usage metrics (for example: total, GPT, tool, project, and connector activity)
* Power users (your most engaged users: top 20% message senders with 75+ messages/week and 3+ different tools per month)

## GPTs

**GPT** analytics includes:

* Total GPTs
* GPTs created in period
* GPTs active in period
* GPT-level usage and reach metrics

## Projects

**Project** analytics includes:

* Total projects
* Projects created in period
* Projects active in period
* Project-level usage and reach metrics

## Skills

**Skills** analytics includes:

* Skill usage trends
* Top skills by message activity

# Export

Use **Export** to generate on-demand CSV reports for the following data types:

* GPTs
* Impact survey
* Projects
* Users

For Users, GPTs, and Projects exports, select a preset date range or select **Custom** to choose a start date and end date. Custom export ranges can cover up to 12 months and cannot end after the current date.  
  
Non-CSV export formats and additional tabs are not currently supported.

## Generate a CSV report

1. Go to **Workspace settings** **>** **Workspace analytics**.
2. Select **Export data**.
3. Select a **Data type**.
4. Select a preset **Date range**, or select **Custom** and choose a start date and end date.
5. Select **Generate CSV**.

# Data coverage and limitations

Workspace analytics is an **aggregated analytics experience**. It is not a raw log interface and does not expose:

* Message text
* File contents
* Item-level compliance records

For raw logs, legal/security workflows, and compliance controls, use the Compliance API.

## Data freshness

Workspace analytics is not real-time. Data is refreshed regularly every 1–24 hours, typically within 6–12 hours. Data availability has a target of up to 48 hours, calculated using UTC reporting days. Use the last updated timestamp, shown in UTC, to confirm freshness.

## Workspaces with EU data residency

In workspaces with EU data residency, **Task insights** is **disabled** by default. A workspace owner can enable the feature at any time in **Workspace settings**.  
  
Once enabled, ChatGPT will begin generating **aggregate Task insights data** for the workspace. If Task insights is later disabled, new Task insights data will stop being generated. Previously generated aggregate data is currently not deleted.

# FAQ

## Can I segment analytics by team, department, or business unit?

Some workspace analytics views support segmentation by SCIM groups, which can represent teams, departments, or business units depending on how your identity provider has been configured. If you need additional breakdowns, you can export reports and combine them with your internal data.

## Can I change the impact survey or make my own?

Workspace owners can create an **Admin-created** survey from the **Impact** tab, but they can’t customize the survey questions or answer choices. Admin-created surveys use the same built-in question set as OpenAI-created surveys. For more information, see: [Managing impact surveys in workspace analytics](https://help.openai.com/articles/20001149).

## Can I export the Task insights reports?

No. We are actively working on this and hope to introduce this ability in a future update.

## Why don’t Compliance API counts match workspace analytics?

Counts can differ because the Compliance API returns raw system data, while Workspace Analytics reports cleaned analytics data. For example, the API may include internal system messages or records without timestamps that analytics excludes.

## What’s the difference between “Filter by Group” in Overview and “All organizational units” in Task insights?

In **Overview**, the dropdown menu **Filter by Group** includes all groups available in the workspace, including both SCIM-managed groups and groups created in the ChatGPT UI.  
  
In **Task insights**, the dropdown menu **All organizational units** includes only SCIM groups. In this view, organizational units correspond to SCIM groups.

### What if my workspace doesn’t use SCIM?

If your workspace does not use SCIM, admins do not need to manually create or map groups for **Task insights**. Instead, **Task insights** shows an alternate view based on the intersection of **Task type** and **Conversation topic**, rather than organizational units.  
  
Conversation topics are automatically generated and may include categories such as **Sales** or **Engineering**.

# Appendix: Export data reference

The following tables describe the columns included in current export files.

## Common columns in Users, GPTs, and Projects exports

|  |  |
| --- | --- |
| **Column** | **Description** |
| cadence | The reporting period type. Current values include Weekly, Monthly, Partial Weekly, Partial Monthly, and Date Range. |
| period\_start | The start date of the reporting period. |
| period\_end | The end date of the reporting period. For partial periods, this reflects the latest available end date in the export. |
| account\_id | The workspace account ID associated with the report. |

**Map fields**

Maps connecting an item, such as a model, GPT, tool, or project, to its associated message count. In CSV exports, these maps are represented as serialized text.

## User report

A per-user workspace usage report for the selected period. It combines user identity and status fields with aggregate usage metrics for messages, GPTs, tools, and projects.

**Column**

**Description**

public\_id

The public ID associated with the user.

name

The user’s name. This may be blank for pending users.

email

The user’s email address.

role

The user-entered onboarding role.

user\_role

The workspace role as of period end.

seat\_type

The user’s assigned seat type when the export is generated. Possible values are `ChatGPT`, `Codex`, and `Automation`. This optional field appears only for eligible workspaces.

department

The user-entered onboarding department.

groups

Group membership data for the user as of period end.

user\_status

The user record status as of period end.

created\_or\_invited\_date

The date the user was provisioned or invited.

is\_active

Whether the user sent at least one message during the reporting period.

first\_day\_active\_in\_period

The first day the user was active in the reporting period.

last\_day\_active\_in\_period

The last day the user was active in the reporting period.

messages

Total messages sent by the user in the period.

messages\_rank

Rank by total messages within the workspace for the period.

model\_to\_messages

Serialized map of model family to message count.

gpt\_messages

Messages the user sent to custom GPTs in the period.

gpts\_messaged

Number of distinct custom GPTs the user messaged in the period.

gpt\_to\_messages

Serialized map of GPT ID to message count.

tool\_messages

Count of message records associated with tool activity for the user during the reporting period. This may not equal the number of user-visible tool actions or tool invocations.

tools\_messaged

Number of distinct tools used in the period.

tool\_to\_messages

Serialized map from reporting tool category to the number of associated message records for the user during the selected period. Categories may not correspond one-to-one with user-visible actions or tool invocations.

Search

Messages associated with ChatGPT web search activity.

Container

Messages associated with isolated sandbox execution used during supported tool, file, code, or command workflows.

Chain of Thought Summarizer

Messages associated with summarized reasoning status produced during some reasoning and tool workflows. This does not expose raw chain-of-thought content.

API Tool

Messages associated with ChatGPT’s resource and app-tool routing framework. This does not represent the customer’s use of the OpenAI developer API. Depending on the workflow, it can include app- or connector-backed tool activity.

project\_messages

Messages the user sent inside projects in the period.

projects\_messaged

Number of distinct projects the user contributed to in the period.

project\_to\_messages

Serialized map of project ID to message count.

projects\_created

Projects created by the user in the period.

last\_day\_active

The last day the user was active in this or any prior period.

## GPT report

A per-GPT workspace usage report for the selected period. It shows GPT identity, creator metadata, activity, and usage within the workspace.

|  |  |
| --- | --- |
| **Column** | **Description** |
| gpt\_id | The custom GPT ID. |
| gpt\_name | The GPT name as of period end. |
| config\_type | The GPT config state. Current raw values in code are live and draft. |
| gpt\_description | The GPT description as of period end. |
| gpt\_url | The GPT URL. |
| gpt\_creator\_public\_id | The public ID of the GPT creator. |
| is\_active | Whether the GPT received at least one message in the period. |
| first\_day\_active\_in\_period | The first day the GPT was active in the period. |
| last\_day\_active\_in\_period | The last day the GPT was active in the period. |
| messages\_workspace | Messages sent to the GPT within your workspace in the period. |
| unique\_messagers\_workspace | Count of distinct workspace users who messaged the GPT in the period. |
| gpt\_creator\_email | The creator email, when available. |

## Project report

A per-project workspace usage report for the selected period. It mirrors the GPT export structure, but with project-specific identifiers and creator metadata.

|  |  |
| --- | --- |
| **Column** | **Description** |
| project\_id | The project ID. |
| project\_name | The project name as of period end. |
| config\_type | The raw config state from the analytics source. |
| project\_description | The project description as of period end. |
| project\_url | The project URL. |
| project\_creator\_public\_id | The public ID of the project creator. |
| is\_active | Whether the project received at least one message in the period. |
| first\_day\_active\_in\_period | The first day the project was active in the period. |
| last\_day\_active\_in\_period | The last day the project was active in the period. |
| messages\_workspace | Messages sent inside the project within your workspace in the period. |
| unique\_messagers\_workspace | Count of distinct workspace users who contributed to the project in the period. |
| project\_creator\_email | The creator email, when available. |

## Impact survey report

A response-level export of Impact survey data for the selected workspace. Based on the exported fields, each row represents one answered survey question for one respondent.

|  |  |
| --- | --- |
| **Column** | **Description** |
| date\_partition | The date associated with the survey response row. |
| workspace\_id | The workspace account ID associated with the response. |
| name | The respondent’s name. |
| email | The respondent’s email address. |
| survey\_id | The survey ID. |
| survey\_name | The survey name. |
| question\_id | The survey question ID. |
| answer\_id | The selected answer ID for that question. |

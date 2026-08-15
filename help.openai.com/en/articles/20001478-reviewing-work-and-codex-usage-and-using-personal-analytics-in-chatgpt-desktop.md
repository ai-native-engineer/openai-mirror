<!-- source: https://help.openai.com/en/articles/20001478-reviewing-work-and-codex-usage-and-using-personal-analytics-in-chatgpt-desktop -->

# Reviewing Work and Codex usage and using Personal Analytics in ChatGPT Desktop

Learn how to review Work and Codex credit usage, check monthly usage limits, and use Personal Analytics to explore activity patterns.

Updated: 4 hours ago

Personal Analytics may not yet be available to all Enterprise and Edu workspaces.

For eligible Enterprise/Edu workspaces, ChatGPT Desktop provides two separate ways to understand Work and Codex usage:

* In **Settings****, Usage & billing** shows monthly limits and usage history across Work and Codex, plus locally available high-usage chats and per-chat details where available.
* **Personal Analytics** is a separate plugin that lets eligible members ask questions about their own Work and Codex activity and available aggregated workspace trends.

Use [**Usage & billing**](/en/articles/20001001) for Work and Codex usage and limit information. When **Personal Analytics** is available, use it to explore patterns and ask follow-up questions. Regular Chat usage is not included in these Work and Codex usage views.

Ensure that your ChatGPT Desktop app is upgraded to at least version **26.812.10818** before the full feature set described in this Help Article is made available.

## Availability and prerequisites

**Usage & billing** is available in eligible Enterprise workspaces that use credit-based billing. Monthly usage and history cover Work and Codex. A workspace owner or admin can control whether members see usage in credits and dollars.

To configure usage visibility as a workspace owner or admin:

1. Open [**Admin Console**](https://admin.openai.com/).
2. Select **Usage limits**.
3. Select **Workspace**.
4. Select **Usage visibility and requests**.
5. Enable **Allow users to see usage in credits and dollars**.

When **Personal Analytics** is available for your workspace, a workspace admin must enable it before members can install and connect it from **Plugins** in ChatGPT Desktop. If you do not see **Personal Analytics** in **Plugins**, it is not yet available for your account or is not enabled for your workspace.

# Review Work and Codex usage and billing

## Review overall usage

1. Open the account menu in ChatGPT Desktop.
2. Select **Settings**.
3. Select **Usage & billing**.

## Check monthly usage

Under **General usage limits**, **Monthly usage** shows your personal credit limit across Work and Codex, credits used, remaining allowance, and available reset information for the current monthly period.

Use the monthly-usage meter to check what remains before starting larger tasks. If the page shows percentages instead of exact amounts, your workspace admin controls whether detailed values are available.

![Monthly usage meter showing the used and remaining allowance for the current period.](https://images.ctfassets.net/j22is2dtoxu1/5l6gdJYDQNCAEhFL8KcgBt/6eb728abeb0486fadef7b55bb7173f47/20001478-monthly-usage.png)

*Monthly usage shows the used and remaining allowance across Work and Codex for the current period.*

## Request a higher usage limit

If **Request limit increase** is available, select it, explain what you need, and submit the request for workspace-admin review.

## Review usage history

Select **7D** or **30D** to set the reporting period. You can group credit usage by **Surface**, **Model**, **Reasoning**, or **Speed** to compare usage across Work and Codex and see which settings contributed to usage.

![Credit history chart grouped by surface, model, reasoning, or speed.](https://images.ctfassets.net/j22is2dtoxu1/1MPyqZkw4PkJ8rmVWtWUjf/b0db945af1a7d39a1c44dedab06c023b/20001478-credit-history-groups.png)

*Group Work and Codex credit history by surface, model, reasoning, or speed.*

**Credit history** shows Work and Codex credit usage over time. **Token history** separates uncached input, cached input, and output tokens. These views can help explain why similar tasks use different amounts.

Plugin activity counts calls by plugin. Skill activity counts invocations by skill. Use these views to understand which Work and Codex workflows contributed to recent activity.

## Find high-usage Work and Codex chats

**Top consuming chats** lists locally available Work and Codex chats that were active in the past 30 days and ranks them by lifetime credit usage. The 30-day period determines which chats appear; each total covers that chat's full available history.

Open a Work or Codex chat to review its model, reasoning, and speed breakdown.

![List of recently active chats ranked by lifetime credit usage.](https://images.ctfassets.net/j22is2dtoxu1/4iVLRjBX2piBD3ssNxX1Wz/d0da0b35e942f71d3dbb564345d55b99/20001478-top-consuming-chats.png)

*Top consuming chats ranks recently active Work and Codex chats by lifetime credit usage.*

## Review usage for a single Work or Codex chat

Open a Work or Codex chat and select the usage indicator in the chat header. The usage details can include:

* Lifetime credits used by the Work or Codex chat.
* An estimated cost, when available.
* The model, reasoning effort, and speed associated with the usage.

Current Work or Codex chat totals generally refresh about once per minute.

![Chat usage details showing credits, an estimated cost when available, and usage settings.](https://images.ctfassets.net/j22is2dtoxu1/302lo4RjqLjE7cKY9G94Hy/f4f61b276dae3b75130ee57653e3beab/20001478-chat-usage-details.png)

*Work and Codex chat usage details show credits, an estimated cost when available, and the settings associated with the usage.*

### What Work and Codex chat-level usage may not include

A Work or Codex chat’s displayed usage is an estimate for the main conversation - not a complete record of every billable action associated with that chat.

* **Sub-agents and separate tasks:** Work delegated to sub-agents or run in separate tasks may not be included in the main Work or Codex chat’s total.
* **Image generation and other tools:** Images and certain separately billed tool activity may not appear in the Work or Codex chat’s displayed usage.
* **Background activity:** Some automated or system-generated work associated with a task may not be included in its total.
* **Reporting delays or incomplete data:** Recent activity may take time to appear, and some Work and Codex chat-level usage records may be unavailable.

Usage that does not appear in a Work or Codex chat’s total or **Top consuming chats** may still consume credits and count toward your usage limits. For complete spend information, refer to your workspace’s billing and usage records.

## Understand cost estimates and data freshness

Usage is displayed in **c****redits**, which are billing units. Note that this view is not an invoice - refer to your invoice to track specific dollar spend. Included usage, prepaid usage, and the amount billed to the workspace can differ from the estimate.

Work and Codex chat usage and monthly usage generally refresh about once per minute. Historical charts refresh less frequently, and current-day activity may take longer to appear.

A **7D** or **30D** chart covers the selected reporting period. **Top consuming chats** uses the 30-day period to select locally available Work and Codex chats, then ranks those chats by lifetime usage.

# Set up Personal Analytics

## Enable Personal Analytics for a workspace

To enable Personal Analytics as a workspace owner or admin:

1. Go to Workspace settings -> Plugins.
2. Find **Personal Analytics**, then enable it.

![Workspace plugin catalog showing Personal Analytics enabled for members.](https://images.ctfassets.net/j22is2dtoxu1/2w9MzvNcZzJgMFsVOhmAPS/0bbe59cd7c061812b7dce2715edb6aa0/20001478-personal-analytics-plugin-catalog.png)

*Workspace admins enable Personal Analytics from the plugin catalog.*

## Install and connect Personal Analytics

To install Personal Analytics in ChatGPT Desktop:

1. Select **Plugins** in the sidebar.
2. Select **Personal Analytics**.
3. Select **Install**. When installation finishes, the button changes to **Try now**.
4. Select **Try now**.
5. Confirm that **Personal Analytics** shows **Connected**.

# Use Personal Analytics

Open Personal Analytics or mention @personal-analytics in a Work or Codex chat, then ask questions in plain language.

## Review personal usage

*Example prompt:*

@personal-analytics analyze my Work and Codex usage over the past week

A personal Work and Codex usage summary can include turns, tokens, credits, models, task types, accepted code, code-review activity, skills, plugins, and current usage limits when available.

![Personal Analytics usage summary showing recent Codex activity categories.](https://images.ctfassets.net/j22is2dtoxu1/1MjaqnJJvftp1VkOwT3jS1/2145585f13422707378d055f564ff382/20001478-personal-usage-summary.png)

*A personal Work and Codex usage summary can include turns, tokens, credits, models, task types, and other recent activity.*

## Explore specific breakdowns

*Example prompts include:*

* @personal-analytics show my Work and Codex usage this week by reasoning effort and speed
* Which models, plugins, and task types are most common in my workspace’s Work and Codex usage?

## Get usage suggestions

*Example prompt:*

Compare my plugin mix with Work and Codex usage trends in my workspace and suggest gaps.

Personal Analytics can provide suggestions based on your Work and Codex activity and available Work and Codex usage trends in your workspace.

## Understand Personal Analytics data

Personal Analytics uses a read-only connection to OpenAI's ChatGPT backends. It can show Work and Codex activity associated with your signed-in identity and aggregated Work and Codex usage trends in your workspace.

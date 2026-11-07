<!-- source: https://help.openai.com/en/articles/20001613-setting-up-and-using-chatgpt-for-financial-services -->

# Setting up and using ChatGPT for Financial Services

Learn how to set up your workspace, use financial data, and adapt ChatGPT for Financial Services to your team’s workflows.

Updated: 10 days ago

This guide is for workspace owners, administrators, and team members using ChatGPT for Financial Services. Administrators can follow the setup steps, and team members can use the guidance and examples to get started.

For plan eligibility, included financial datasets, data delays and usage caps, privacy controls, and applicable terms, see: [ChatGPT for Financial Services](https://help.openai.com/articles/20001517).

ChatGPT supports financial research and does not replace professional financial or investment advice. Check important information against its sources and review outputs before using them.

## Before you begin

ChatGPT Work is required to use ChatGPT for Financial Services.

Start with the [Work admin FAQ](https://learn.chatgpt.com/docs/enterprise/work-admin-faq). For execution, security, and data handling, see: [Work overview](https://learn.chatgpt.com/docs/enterprise/chatgpt-work-overview).

# Set up your workspace

**Setup video:** Open the [setup walkthrough](https://screen.studio/share/PUsqHTfN) on Screen Studio for help enabling Financial Services, managing access, and configuring firm templates. The video opens on an external site.

## Prepare workspace access

1. Follow the [setup walkthrough](https://screen.studio/share/PUsqHTfN) to configure your workspace.
2. [Enable ChatGPT Work](https://help.openai.com/articles/20001275#configure-work-access-for-your-workspace) for your team from **Workspace settings** > **Permissions & roles**. For complete configuration instructions, see: [Admin rollout guide](https://learn.chatgpt.com/docs/enterprise/admin-setup).
3. Decide whether your team needs local computer access. You can enable Work Cloud while leaving local access disabled. Users can still work with uploaded files and approved connected sources.
4. Enable ChatGPT for Financial Services and decide which workspace members can use it. These controls manage access to Financial Services features and built-in financial data sources. Connections to your firm’s data and existing provider subscriptions have separate permissions, described below. Follow the [setup walkthrough](https://screen.studio/share/PUsqHTfN) for the access controls.

## Choose optional connections

Included datasets remain available without a separate provider login. Additional sources may require your organization’s existing subscription, sign-in, and workspace permissions.

For setup and permission controls, see: [Plugins and data connections](https://learn.chatgpt.com/docs/enterprise/apps-and-connectors).

Recommended connection types include:

* Email, chat, and calendar, such as Outlook and Teams.
* Firm data repositories, such as SharePoint, with at least read-only access.
* Existing third-party data subscriptions, such as S&P CapIQ and FactSet.
* Connections for specific workflows, such as [Datasite](https://openai.com/business/plugins/datasite/) for virtual data rooms or [DealCloud](https://openai.com/business/plugins/intapp-celeste/) for deal customer relationship management (CRM).

Choose the connections and permissions appropriate to your team’s tasks and your firm’s policies. Read-only access still allows content to be read and processed. Review the connection’s permissions and data-sharing implications before enabling it.

## Configure firm templates and style guides

You can provide templates and style guides for your workspace. Coordinate configuration with the administrator responsible for Financial Services access. For guidance on adding templates, watch the [setup walkthrough](https://screen.studio/share/PUsqHTfN) (timestamp: 1:40).

After templates are configured, include a template-based task when you verify setup below.

## Set usage limits

Admins can set monthly usage limits using workspace defaults, group limits, or individual overrides. For configuration instructions, see: [Usage limits and spend controls](https://learn.chatgpt.com/docs/enterprise/usage-limits).

Review the applicable workspace and user settings before rollout. Per-user usage limits are separate from provider coverage, dataset-specific caps, and access permissions. For more information, see: [ChatGPT Enterprise usage limits](https://help.openai.com/articles/20001001).

## Verify setup

1. Sign in as a user with the permissions you want to test and start a task in ChatGPT Work. You do not need to manually trigger Financial Services with a command such as @Financial.
2. Ask for a known document or data point from each approved source relevant to the test. Choose material the user is authorized to access and that is within the source’s coverage. Ask ChatGPT to identify any sources it could not access or retrieve information from.
3. If your firm has configured templates, ask for a short presentation using a firm template. Open the resulting file and check the branding, layout, and contents.

# Start using Financial Services

Eligible new users are guided through onboarding to connect available financial data providers and get started with tasks relevant to their work.

## Get better results

* Choose the most capable model available, particularly for Excel and PowerPoint tasks.
* Attach a relevant reference, such as a prior slide or workbook. Explain what to follow from the example and include any missing context.
* Be specific about the output. For example: “Create a stock-price slide for [company] covering the past year. Annotate major price movements with sourced explanations, and flag any moves you cannot explain.”
* Keep the initial task focused, such as one slide or analysis, rather than a full pitch deck.
* For complex tasks, ask ChatGPT to propose a plan first. Review the approach and clarify assumptions before continuing.

# Adapt ChatGPT to your workflows

For an individual task, provide an approved example of prior work along with relevant context and instructions. Explain which layout, terminology, or conventions ChatGPT should follow and what the example does not show. Share only materials the task is authorized to use.

ChatGPT for Financial Services does not include general financial-services practitioner skills for tasks such as discounted cash flow (DCF) modeling, pitch decks, or earnings analysis.

For complex, recurring workflows, such as earnings updates or quarterly portfolio reporting, use the built-in [skill-creator](https://learn.chatgpt.com/docs/build-skills#create-a-skill) to capture your team’s methods, checks, and output requirements in a reusable skill. Test it on representative tasks before sharing it more broadly.

# Troubleshooting

## Resolve access issues

If the Financial Services settings are unavailable, contact Support for help. For a connected-source error, check connection approval, sign-in, workspace permissions, provider entitlements, and source coverage.

If a result is incomplete, check the requested dates and company coverage, including the delays and caps in [ChatGPT for Financial Services](https://help.openai.com/articles/20001517). Do not assume every missing result indicates a setup failure.

## Contact Support

For technical help, open the [OpenAI Help Center](https://help.openai.com/) and select the chat bubble to contact Support. Include the task, expected result, relevant source, and any error message.

## Provide feedback

1. Enter /feedback in the message box and select **Feedback**.
2. Describe what happened and what you expected.
3. Follow the prompts to submit your feedback.

# FAQ

## If we upgrade to Enterprise, can we keep our chat history and saved memories?

* From a personal workspace, eligible users can migrate supported chats and saved memories under the same account. Review the restrictions and implications before proceeding. For details, see: [Migrating your personal workspace](https://help.openai.com/articles/8801890).
* From ChatGPT Business, contact your OpenAI account team about upgrading the existing workspace while retaining its data.
* If you plan to move into a separate Enterprise workspace, discuss migration options with your OpenAI account team. For more information, see: [ChatGPT Business FAQ](https://help.openai.com/articles/8542115).

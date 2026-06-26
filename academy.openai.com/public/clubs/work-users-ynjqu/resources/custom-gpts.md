<!-- source: https://academy.openai.com/public/clubs/work-users-ynjqu/resources/custom-gpts -->

[Work Users](/en/public/clubs/work-users-ynjqu/overview)

[navigation.content](/en/public/clubs/work-users-ynjqu/content)

# Custom GPTs

![Custom GPTs](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Work-Users-Cover-Images-29--22a5e259-2c2b-4646-aa42-e7573a3b24d9-1754317218808.jpeg?fit=scale-down&width=1200)

# Workplace & Business

# Advanced & Builder Skills

## Build repeatable workflows with custom GPTs.

July 23, 2025 · Last updated on May 29, 2026

![Custom GPTs](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Work-Users-Cover-Images-29--22a5e259-2c2b-4646-aa42-e7573a3b24d9-1754317218808.jpeg?fit=scale-down&width=1200)

# **Custom GPTs**

ChatGPT includes custom GPTs, which are custom versions of ChatGPT that help with repeatable work—like writing in a format or style, analyzing common data sets, generating visuals, and more. Each one has tailored instructions to guide responses, and you can add files or connect tools to help your team move faster and stay consistent. They're especially helpful for eliminating the need to repeatedly enter detailed instructions, context, or files into a chat. Anyone can create a custom GPT for specific tasks or workflows.

*Please note that recordings may show a different or previous version of the ChatGPT UI.*

## Custom GPTs vs. Chat

**Chat** is ideal for quick, one-off tasks. **Custom GPTs** provide more tailored support, especially when you:

* **Automate repeat tasks**: Let a custom GPT handle prompts you use often.

* **Share tasks with your team**: Help ensure consistent, efficient outputs for shared tasks.

* **Add integrations**: Connect to more data or third-party services for deeper answers.

* **Stay in context**: A custom GPT can remember its purpose and resources, so you don’t have to re-explain each time.

If you often reuse a prompt or see a use case your team could benefit from, it’s likely time to build a GPT.

## **GPTs built by the OpenAI team**

|  |  |
| --- | --- |
| ﻿[ChatGPT for work use cases](https://chatgpt.com/g/g-h5aUtVu0G-chatgpt-use-cases-for-work)﻿ | Brainstorm role-specific ways to apply ChatGPT |
| ﻿[Professional Writing Coach](https://chatgpt.com/g/g-ZRYV8dzO8-professional-writing-coach)﻿ | Polish emails, reports, and presentations |
| ﻿[Data Analyst](https://chatgpt.com/g/g-HMNcP6w7d-data-analyst)﻿ | Summarize, chart, and explain uploaded data |
| ﻿[Coding Assistant](https://chatgpt.com/g/g-vK4oPfjfp-coding-assistant)﻿ | Generate, review, and debug code snippets |
| ﻿[Visual Designer](https://chatgpt.com/g/g-n7u0emyLB-visual-designer)﻿ | Turn text prompts into on-brand images |

## **How to build a GPT**

### **1. Identify strong use cases**

The first step in building a GPT is to identify your use case. Focus on routine tasks that could benefit from improved efficiency. Ask yourself:

* Where can you save time on recurring tasks?

* Which tasks could be streamlined?

#### **Example GPTs for your role**

|  |  |  |  |
| --- | --- | --- | --- |
| **Role** | **Custom GPT** | **Description** | **Custom action integration (optional)** |
| **Marketing** | Campaign copy crafter | Generates and A/B-tests ad copy, social posts,and email subject lines while enforcing brand voice | Mailchimp - create a draft email campaign to A/B test |
| **Product** | User story drafter | Transforms feature ideas into polished user stories with acceptance criteria and priority tags | JIRA - add a user-story issue to the backlog |
| **Finance** | Variance analyzer | Pulls actuals vs. budget, flags key deltas, and drafts commentary for monthly close reports | NetSuite SuiteQL - pull budget vs. actuals |
| Sales | Prospect email tailor | Crafts personalized outreach emails using CRM fields and product benefits in the desired tone | Salesforce - fetch lead/contact fields |
| Engineering | Code review assistant | Reviews diffs for style, security, and performance issues, suggesting inline improvements | GitHub - comment inline on a PR diff |
| HR | Job description builder | Creates competency-based, inclusive job descriptions aligned to role seniority and company tone | Greenhouse - create a new job post |
| IT | Article generator | Converts resolved tickets and agent notes into clear, searchable how-to or troubleshooting articles with consistent formatting and tags | ServiceNow - publish knowledge-base article |

### **2. Create GPT**

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdj231H5SxHzIUUIWk7hedkCW4aeLXmMn8bFA5hpMtYI-RxU2fzJfJiXNqN9vmU_P45c1o6VCtCPEQd6S-uzUfh8ugonBQc5fnUIoxSyR4WuQSuC8sMyFB7LSH5LbN8H3z-DXGwuQ?key=0GQfd8VDgIprxAJeiq-paQ)

When you open the GPT builder, you will see two tabs: 'Configure' and 'Create'. In the Create tab, you can message the GPT Builder to help you build a new GPT. You can say something like, "Make a creative who helps generate visuals for new products" or "Make a software engineer who helps format my code." Defining clear objectives ensures your GPT stays focused and relevant.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe2icmHXnkUc91sbnC3BE_3v26xBbNnVheqiFKngncmUMgiUijwBNMe6m1mIBkZT0F-gbTovbDCbK9EK33S1L4x7_6JzbyV3Vc9pttCnwdPJKBBek5Bqn72ZNgKCL4-ENRODaOOyQ?key=0GQfd8VDgIprxAJeiq-paQ)

**Tip:** Start in **Create**. Describe your objectives and let ChatGPT draft the GPT’s instructions. Then move to **Configure** to fine-tune the build.

### **3. Configure GPT**

Go to the **Configure** tab and complete the required fields:

* **Name**: Give your GPT a clear, descriptive name so it is easy to find and its purpose is immediately understood.

* **Description**: Add details to help users understand what your GPT can do.

* **Instructions**: Provide clear guidelines on how the GPT should behave, including its functions, tone, and any behaviors to avoid. Follow best practices for writing instructions.

* **Conversation starters**: Add example prompts that appear when users open the GPT. These help guide users on how to begin their interaction.

* **Knowledge**: Upload proprietary documents like policies, procedures, and FAQs to give your GPT the business context it needs for accurate answers.

* **Capabilities**: Enable features such as image generation, data analysis, web search, and canvas.

* **Custom actions**: Set up actions so your GPT can call third-party APIs to retrieve data, modify external sources, or trigger external processes.

**Tip***:* To configure Custom Actions, check out the comprehensive guide on the [OpenAI Cookbook.](https://cookbook.openai.com/examples/chatgpt/gpt_actions_library/.gpt_action_getting_started)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdjBj2Uq5Wa0g6pY8dS-sCfFoSBqwTti__aKRRr7iewoh-29E_W4dGWXPwkyR_7Bj53sB98ouLPAjcTilVEOYKfgQqa1XU3R58yHCDujpQuCTziapGdYifBpKQ1WETERuFiySTCeQ?key=0GQfd8VDgIprxAJeiq-paQ)

### **4. Test your GPT's performance**

Before [sharing your GPT](https://help.openai.com/en/articles/9083988-how-to-share-gpts-within-workspaces), it is important to check that it works as expected. You can do this with evals, a simple way to test its performance.

**Set up your eval:**

* Write 10 to 15 questions that reflect the tasks your GPT should handle.

* Include the correct answers for each question.

* Use these questions to see if your GPT gives accurate and reliable responses.

* Review the results and adjust your GPT’s instructions or knowledge if needed.

**Tip:** When making changes, don’t forget to **click the “update” button** in the top right.. It’s easy to miss, especially when you're returning to reconfigure an existing GPT.

## **Additional resources**

﻿[GPT FAQ](https://help.openai.com/en/articles/8554407-gpts-faq)﻿

﻿[GPT Building](https://help.openai.com/en/articles/8554397-creating-a-gpt)﻿

﻿[GPT Instruction Writing](https://help.openai.com/en/articles/9358033-key-guidelines-for-writing-instructions-for-custom-gpts)﻿

﻿[GPT Custom Action Cookbook](https://cookbook.openai.com/examples/chatgpt/gpt_actions_library/.gpt_action_getting_started)﻿

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

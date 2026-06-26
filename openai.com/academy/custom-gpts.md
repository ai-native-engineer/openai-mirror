<!-- source: https://openai.com/academy/custom-gpts/ -->

April 10, 2026

OpenAI Academy

# Using custom GPTs

Build purpose-built ChatGPT assistants that follow your instructions, use your context, and streamline repeatable work.

Some versions of ChatGPT let you build **custom GPTs**—purpose-built versions of ChatGPT designed for a specific task or workflow. Instead of starting from a blank chat each time, a custom GPT can follow your preferred format, use your team’s context, and produce more consistent outputs—whether you’re drafting content, analyzing recurring datasets, generating visuals, or answering common questions.

Custom GPTs are powered by tailored instructions that define how the GPT behaves. You can also add knowledge (files you upload) and enable tools (such as web search, data analysis, or connected actions). The result: less re-explaining, less copy/pasting, and fewer “wait—what’s the context again?” moments.

You can explore custom GPTs [here⁠(opens in a new window)](https://chatgpt.com/gpts).

## Custom GPTs vs. general chat

A regular chat is well-suited for quick, one-off tasks—brainstorming ideas, quick rewrites, or answering a question in the moment.

A **custom GPT** is a better fit when you need something repeatable and consistent. For example:

* **Automating repeat tasks**: Save a prompt you use often and turn it into a reliable workflow.
* **Adding tools or integrations**: Pull in more context, analyze files, or use connected apps for deeper answers.
* **Maintaining consistent context**: Apply the same structure, tone, or instructions without restating them.

If you find yourself reusing the same prompt, re-uploading the same files, or rewriting the same instructions for teammates—it may be time to build a custom GPT.

## Custom GPTs built by the OpenAI team

|  |  |
| --- | --- |
| **Custom GPT** | **Purpose** |
| [ChatGPT Use Cases for Work⁠(opens in a new window)](https://chatgpt.com/g/g-h5aUtVu0G-chatgpt-use-cases-for-work) | Brainstorm role-specific ways to apply ChatGPT |
| [Professional Writing Coach⁠(opens in a new window)](https://chatgpt.com/g/g-ZRYV8dzO8-professional-writing-coach) | Polish emails, reports, and presentations |
| [Data Analyst⁠(opens in a new window)](https://chatgpt.com/g/g-HMNcP6w7d-data-analyst) | Summarize, chart, and explain uploaded data |
| [Coding Assistant⁠(opens in a new window)](https://chatgpt.com/g/g-vK4oPfjfp-coding-assistant) | Generate, review, and debug code snippets |
| [Visual Designer⁠(opens in a new window)](https://chatgpt.com/g/g-n7u0emyLB-visual-designer) | Turn text prompts into on-brand images |

## How to build a custom GPT

### 1. Identify strong use cases

Good GPTs usually begin with a simple, repeatable need. Focus on workflows that occur regularly—such as drafting the same type of message, summarizing recurring meetings, answering common questions, or turning raw data into a consistent weekly report.

Example use cases:

* **Knowledge Assistant / FAQ Bot:** Answers questions from documents or internal resources.
* **Writing & Editing Assistant:** Rewrites, polishes, or formats text for tone, clarity, and style.
* **Learning Companion / Tutor:** Explains concepts, quizzes users, and generates study materials.
* **Project / Workflow Assistant:** Summarizes meetings, tracks progress, and drafts status updates.
* **Data & Insights Assistant**: Analyzes data, summarizes trends, and generates visual or narrative reports.

### 2. Create GPT

To get started, open **GPTs** from the ChatGPT sidebar, then select **Create** to open the GPT builder.

When you open the GPT builder, you will see two tabs: **Create** and **Configure**. In the **Create** tab, you can message the GPT Builder to help you build a new GPT. You can say something like, "Make a creative who helps generate visuals for new products" or "Make a software engineer who helps format my code." Defining clear objectives ensures your GPT stays focused and relevant.

If you want to define the details of your GPT more precisely, go to the **Configure** tab and complete the required fields:

* **Name**: Choose a clear, descriptive name so it's easy to find and its purpose is immediately understood.
* **Description**: Explain what the GPT does and when to use it.
* **Instructions**: Define how the GPT should behave, including its functions, tone, and any behaviors to avoid.
* **Conversation starters (Optional)**: Provide example prompts that appear when users open the GPT. These help guide users on how to begin their interaction.
* **Knowledge**: Upload relevant documents to give your GPT the context it needs for accurate answers.
* **Capabilities**: Enable features such as image generation, data analysis, web search, and canvas.
* **Custom actions**: Set up actions so your GPT can call third-party APIs to retrieve data, modify external sources, or trigger external processes.

Writing instructions is often the most challenging step, as it requires translating your goals into clear, actionable guidance the GPT can follow. A simple way to move faster is to ask ChatGPT to draft a first version, then refine it based on real examples.

**Tip***:* To configure custom actions, see the comprehensive guide on the [OpenAI Cookbook.⁠(opens in a new window)](https://cookbook.openai.com/examples/chatgpt/gpt_actions_library/.gpt_action_getting_started)

### 3. Test your GPT’s performance

Before [sharing your GPT⁠(opens in a new window)](https://help.openai.com/articles/9083988-how-to-share-gpts-within-workspaces), it is important to check that it works as expected. You can do this with evals, a simple way to assess its outputs.

**Set up your evaluation:**

* Write 10 to 15 questions that reflect the tasks your GPT should handle.
* Include the correct answers for each question.
* Use these questions to see if your GPT gives accurate and reliable responses.
* Review the results and adjust your GPT’s instructions or knowledge if needed.

**Tip:** When making changes, don’t forget to click **“Update”** in the top right to save them. It’s easy to miss, especially when you're returning to reconfigure an existing GPT.

Building a custom GPT doesn’t have to be complex. Start with a workflow you already repeat, draft a first version of the instructions, and test it with a small set of examples. You’ll learn quickly what to adjust—and small refinements usually make a big difference. Once it feels reliable, share it with your team so everyone can get to the same quality output faster, with less effort.

## Additional resources

* [GPT FAQ⁠(opens in a new window)](https://help.openai.com/articles/8554407-gpts-faq)
* [GPT Building⁠(opens in a new window)](https://help.openai.com/articles/8554397-creating-a-gpt)
* [GPT Instruction Writing⁠(opens in a new window)](https://help.openai.com/articles/9358033-key-guidelines-for-writing-instructions-for-custom-gpts)
* [GPT Custom Action Cookbook⁠(opens in a new window)](https://cookbook.openai.com/examples/chatgpt/gpt_actions_library/.gpt_action_getting_started)

## Continue learning with OpenAI Academy

Discover additional guides and resources to help you build practical AI skills.

[View all topics](/academy/)

## Keep reading

![Academy > Skills > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/5HjfQo619jC918nhDM0S4p/a788f0e356c534e61f30e6607402b5ab/skills.png?w=3840&q=90&fm=webp)

[Using skills in ChatGPT | OpenAI

OpenAI AcademyApr 10, 2026](/academy/skills/)

![Academy > Prompting > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/6KuWyesIgCbrJUzXckTYSx/20183733ba66b4b535fe978fc7ec985b/your-first-chat.png?w=3840&q=90&fm=webp)

[Prompting fundamentals | OpenAI

OpenAI AcademyApr 10, 2026](/academy/prompting/)

![Academy > Personalizing ChatGPT > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/2s9rOdoSHProR3I6Ai5P5/8ca619f82211ade2d76316f04aa3fbcc/personalizing-chatgpt.png?w=3840&q=90&fm=webp)

[Personalizing ChatGPT | OpenAI

OpenAI AcademyApr 10, 2026](/academy/personalization/)

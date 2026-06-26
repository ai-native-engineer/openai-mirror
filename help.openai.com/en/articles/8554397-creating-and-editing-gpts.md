<!-- source: https://help.openai.com/en/articles/8554397-creating-and-editing-gpts -->

# Creating and editing GPTs

Create, configure, test, and manage GPTs in ChatGPT, including instructions, knowledge, capabilities, apps, actions, and version history.

Updated: 2 days ago

*As of February 13, 2026, models GPT-4o, GPT-4.1, GPT-4.1 mini, OpenAI o4-mini, and GPT-5 (Instant and Thinking) have been retired from ChatGPT and are no longer available. API access remains unchanged.*  
  
*For more information, please refer to our article:* [*Retiring GPT-4o and other ChatGPT models*](https://help.openai.com/articles/20001051)

# Overview

You can create a GPT from the GPTs area in ChatGPT. The editor lets you build a GPT conversationally or configure it directly. This article walks through creating, configuring, testing, and updating a GPT.

## Availability

Building and editing GPTs is limited to the web experience. Mobile apps support using GPTs but not building them.  
  
This article applies to paid ChatGPT users and, in managed workspaces, to users who have permission to create or edit GPTs.

# Create a GPT

To create a GPT, start from the GPTs area in ChatGPT:

1. Open **Explore** **GPTs** in the ChatGPT sidebar or visit [**https://chatgpt.com/gpts**](https://chatgpt.com/gpts).
2. Select **Create** to open the GPT builder.
3. Choose how you want to build:
4. **Conversational builder:** Describe what you want, and ChatGPT will help draft the GPT for you.
5. **Configuration view:** Set up the GPT directly by editing its fields.

# GPT configuration options

## Name, description, and conversation starters

These are user-facing fields. They determine how your GPT appears to others, how easily people can find it, and how they get started using it.

### Name

The title of your GPT. This is what users see in search results, the GPT Store, shared links, and at the top of the chat. Use a clear, specific name so users immediately understand what the GPT does.

### Description

A short summary of your GPT. Use it to explain the GPT’s purpose, who it is for, and what kinds of tasks it helps with. This also appears in previews and in GPT Store listings before someone opens it.

### Conversation starters

Example prompts shown when someone opens the GPT. These help users understand what they can ask and how to interact with it. Include a few realistic, high-value prompts that reflect the GPT’s intended use.

## Instructions

Instructions define how your GPT behaves: what it should do, how it should respond, and what it should avoid. These are applied to every conversation and guide the GPT’s tone, structure, and decision-making.

### Writing effective instructions

* For multi-step workflows, use explicit step structure, for example: “When X happens → do Y,” and separate sections with clear delimiters.
* Prefer positive, concrete instructions (“Do X”) over long lists of prohibitions (“Don’t do Y”) when possible.
* If your GPT must apply specific definitions or classifications, include brief examples of acceptable and unacceptable outputs.
* Use headings and lists so priorities and steps are visually distinct.

## Knowledge

Knowledge lets your GPT use information from files you upload. It works best for reference material you want the GPT to draw from when answering questions, such as documentation, guides, handbooks, or internal content.  
  
Unlike instructions, which define how your GPT should behave, files uploaded as knowledge give it source material to use during a conversation.

### File limits

You can attach up to 20 files to a GPT. Each file can be up to 512 MB.  
  
GPTs support most common document, spreadsheet, image, text, and code file types. Accepted file types can vary by model, and some file types are only available if the setting **Code Interpreter & Data Analysis** is enabled for the GPT.

### Best practices

* Use knowledge for reference material, not rules or behavior. Put rules, tone, and workflow guidance in instructions.
* Prefer clear, text-forward files when possible. Complex layouts can make uploaded content harder for the GPT to use effectively.
* If you want the GPT to cite or quote uploaded content, say so in the instructions and specify the format you want.
* Test your GPT in Preview after uploading files to make sure it uses the content the way you expect.

## Recommended model

The recommended model is the model your GPT suggests to users when they start a new conversation. Setting one helps guide users toward the best option for the GPT’s task, especially when more than one model is available.  
  
If the recommended model is not available to a user, a similar model may be selected automatically. If you don’t set a recommended model, users can choose whichever model they prefer.  
  
Note that users can still switch to a different model if additional models are available to them.

## Capabilities

Capabilities extend what your GPT can do. You can enable built-in features and connect external tools from this section. Availability depends on your account, workspace setup, and region.

* **Web search:** Retrieve up-to-date information from the web.
* **Image generation:** Create images from text prompts.
* **Canvas:** Draft, edit, and refine longer or structured content.
* **Code Interpreter & Data Analysis:** Run calculations, analyze data, and generate charts.
* **Apps:** Use external tools and services that users have connected.

If apps are enabled, the GPT can use tools available to the user. If restricted, users may be prompted to connect specific apps. Users may also be asked to confirm when an app is used.

## Actions

Actions allow your GPT to connect to external APIs that you define.  
  
Use actions when your GPT needs to retrieve data or take actions in external systems, such as calling APIs or triggering workflows.  
  
A GPT can use either apps or actions, but not both at the same time.  
  
For detailed setup and configuration instructions, see: [Configuring actions in GPTs](https://help.openai.com/articles/9442513).

## Test your GPT

Before sharing or publishing to the GPT Store, use the built-in **Preview** to try real prompts, check tone and accuracy, and refine the setup.  
  
Before adding more tools, tighten instructions and add examples. This often fixes issues faster than adding features.

## Save, update, and versioning

Changes save to a draft automatically while you edit. When you are ready to create a new GPT, select **Create**. If you are editing an existing GPT, select **Update** to apply your latest draft changes.

### Version history

You can use version history to review and restore earlier versions. While editing a GPT, open the more options menu (•••) to access version history.  
  
  
***Note:***\* If you restore an older version of a GPT that uses actions, you may need to reconfigure its authentication afterward.\*

## Manage or edit a GPT

To edit a GPT you created:

1. Open **Explore** **GPTs** in ChatGPT or visit <https://chatgpt.com/gpts>.
2. Select **My GPTs**
3. Choose the GPT you want to update
4. Select **Edit GPT**

If you are already chatting with a GPT, you can also open its menu and select **Edit GPT**.  
  
From the editor, you can:

* Make changes to the GPT.
* Select **Share** to manage access for the GPT.
* Open the more options menu (•••) to copy the GPT link, view version history, duplicate the GPT, or delete it.

Note that some options depend on whether the GPT has been created and on your permissions. For example, the GPT link and version history are only available after a GPT has been created, and **Delete GPT** appears only if you have permission to remove it.

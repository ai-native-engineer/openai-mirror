<!-- source: https://help.openai.com/en/articles/12515353-build-with-the-apps-sdk -->

# Build with the Apps SDK

Build, test, and prepare ChatGPT apps with the Apps SDK and Model Context Protocol.

The **Apps SDK**, available in preview, lets developers design both the logic and the interface of an app that runs inside ChatGPT. It is built on the **Model Context Protocol (MCP)**, an open standard for connecting ChatGPT to external tools and data. The Apps SDK extends MCP so apps built with it can run anywhere that adopts the standard. The Apps SDK is open source.

## Getting started

1. **Read the** [**Apps SDK documentation**](https://developers.openai.com/apps-sdk) for design guidelines and example apps.
2. **Build your app** using your own code. Define the chat behavior and UI. Connect to your existing backend so that in the future, your users can sign in or access premium features.
3. **Test in ChatGPT** by using [Developer Mode](https://platform.openai.com/docs/guides/developer-mode) to create a custom app and iterate on your app’s experience. Business and Enterprise/Edu admins can enable developer mode from [Workspace settings](https://www.chatgpt.com/admin/ca), and allow authorized users to develop and test internal apps - see [Developer Mode and full MCP connectors in ChatGPT](/en/articles/12584461-developer-mode-and-full-mcp-connectors-in-chatgpt-beta) for more detail.
4. **Prepare for app submission** by reviewing the draft [developer guidelines](http://developers.openai.com/apps-sdk/app-developer-guidelines) on safety, privacy, and functionality.

## Submissions and directory

* We are accepting app submissions. See [submitting apps to the ChatGPT app](/en/articles/20001040) directory for more information.
* Apps that meet higher design and functionality standards may be eligible to be featured more prominently.

## Monetization

Details will be shared in the future. Support is planned for the [**Agentic Commerce Protocol**](https://developers.openai.com/commerce), an open standard that enables instant checkout in ChatGPT.

# Safety and privacy

Our developer guidelines will require that developers follow OpenAI [usage policies](https://openai.com/policies/usage-policies/), be appropriate for all audiences, and provide a clear privacy policy for their app. Please note that we have shared a draft of developer guidelines as an early preview for developers, but that these guidelines and required standards are subject to change as we learn and hear more from our developer community.

# FAQ

#### What is the Apps SDK?

A developer toolkit that extends the Model Context Protocol so you can define an app’s chat logic and interface, connect it to your backend, and run it inside ChatGPT.

#### Who can build apps?

Developers with Developer Mode access can build and test apps today using the Apps SDK preview. To submit apps to the app directory, follow the separate ChatGPT app submission flow.

#### Can ChatGPT Business, Enterprise, and Edu businesses use apps?

Business and Enterprise/Edu are supported now in the Apps SDK preview: workspace admins can enable developer mode and allow authorized users to develop and test internal apps for their workspace.

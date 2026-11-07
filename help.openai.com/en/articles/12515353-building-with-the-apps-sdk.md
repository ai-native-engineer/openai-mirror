<!-- source: https://help.openai.com/en/articles/12515353-building-with-the-apps-sdk -->

# Building with the Apps SDK

Build, test, and prepare ChatGPT apps with the Apps SDK and Model Context Protocol.

Updated: 9 days ago

The **Apps SDK**, available in preview, lets developers design both the logic and the interface of an app that runs inside ChatGPT. It is built on the **Model Context Protocol (MCP)**, an open standard for connecting ChatGPT to external tools and data. The Apps SDK extends MCP so apps built with it can run anywhere that adopts the standard. The Apps SDK is open source.

# Getting started

1. Read the [Apps SDK documentation](https://developers.openai.com/apps-sdk) for design guidelines and example apps.
2. Build your app using your own code. Define the chat behavior and UI. Connect to your existing backend so that in the future, your users can sign in or access premium features.
3. Test in ChatGPT by using [custom MCP app setup](https://developers.openai.com/plugins/deploy/connect-chatgpt) to create a custom app and iterate on your app’s experience. Business and Enterprise/Edu admins can manage custom MCP app permissions from [**Workspace settings**](https://www.chatgpt.com/admin/ca), and allow authorized users to develop and test internal apps - see [Connecting custom MCP servers in ChatGPT](https://help.openai.com/articles/12584461) for more detail.

   Workspace admins can also open the **Apps** page from [**Admin console**](https://admin.openai.com). Select the intended ChatGPT workspace, open **Plugins**, and select **Manage Legacy Apps**. Use the custom MCP app setup instructions above to create and test an app.
4. Prepare for app submission by reviewing the draft [developer guidelines](http://developers.openai.com/apps-sdk/app-developer-guidelines) on safety, privacy, and functionality.

# Submissions and directory

* We are accepting app submissions. See [submitting apps to the ChatGPT app](https://help.openai.com/articles/20001040) directory for more information.
* Apps that meet higher design and functionality standards may be eligible to be featured more prominently.

# Monetization

Details will be shared in the future. Support is planned for the [**Agentic Commerce Protocol**](https://developers.openai.com/commerce), an open standard that enables instant checkout in ChatGPT.

# Safety and privacy

Our developer guidelines will require that developers follow OpenAI [usage policies](https://openai.com/policies/usage-policies/), be appropriate for all audiences, and provide a clear privacy policy for their app. Please note that we have shared a draft of developer guidelines as an early preview for developers, but that these guidelines and required standards are subject to change as we learn and hear more from our developer community.

# FAQ

## What is the Apps SDK?

A developer toolkit that extends the Model Context Protocol so you can define an app’s chat logic and interface, connect it to your backend, and run it inside ChatGPT.

## Who can build apps?

Developers with permission to create custom apps can build and test apps using the Apps SDK preview. To submit apps to the app directory, follow the separate ChatGPT app submission flow.

## Can ChatGPT Business, Enterprise, and Edu businesses use apps?

Business and Enterprise/Edu are supported in the Apps SDK preview. Workspace admins and owners can create and test custom apps. Enterprise/Edu admins can also grant selected members permission to create and test apps.

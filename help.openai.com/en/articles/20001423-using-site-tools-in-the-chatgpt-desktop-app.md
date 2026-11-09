<!-- source: https://help.openai.com/en/articles/20001423-using-site-tools-in-the-chatgpt-desktop-app -->

# Using site tools in the ChatGPT desktop app

Search, edit, and complete tasks on supported websites without leaving ChatGPT.

Updated: 9 days ago

Site tools let ChatGPT work directly with websites open in the ChatGPT desktop app’s built-in browser. Instead of relying only on clicks and typing, ChatGPT can use tools a website provides to find information, update content, and work with interactive tools.

Site tools use WebMCP, a proposed [web standard](https://webmachinelearning.github.io/webmcp/). They are available when your account has access and the website provides site tools.

# Use site tools

1. Open the built-in browser from the ChatGPT desktop app toolbar.
2. Visit the website you want to use and sign in directly on the website if needed.
3. If the website provides site tools, an arrow appears in the address bar. Select it to see the available tools.
4. Tell ChatGPT what you want to do, such as finding information or updating a document.
5. Review any website-access prompt before ChatGPT continues.
6. Check the result on the webpage or in your conversation.

The arrow in the address bar is gray when site tools are available and turns blue while ChatGPT is using them. Select the arrow to see which tools the website provides, including whether they can read information or make changes. Select a tool to learn what it does.

When a website provides a tool that matches your request, ChatGPT can discover and use it automatically. After ChatGPT uses a site tool, select the arrow in the address bar, then select the **“recently used”** button to view recently used tools.

# Search, edit, and update supported websites

If the website supports site tools, ChatGPT can help you:

* Search documentation or compare information.
* Edit a document, shared whiteboard, or notebook.
* Explore a dashboard or another interactive page.
* Build a travel itinerary or compare available options.
* Update a shopping cart.

Each website decides which tools to provide. Available site tools can vary between websites and pages.

# Work from the current page and account

Site tools use the webpage you have open, its current state, and your signed-in session. You and ChatGPT can work on the same live page and review changes as they happen.

Your conversation shows site-tool activity in the order it occurs. In **Sources**, activity is organized by website and includes the tools ChatGPT used.

The built-in browser has its own browser state. If you are already signed in to the same website in Chrome, you may need to sign in again in the built-in browser.

# Manage website access safely

Site tools may expose functionality not otherwise present on the webpage, which carries with it novel risks including data exfiltration and prompt injection. ChatGPT uses multiple safeguards to help protect your data and keep you in control.

Site tools follow the same safety checks and confirmation requirements as other browser tasks. ChatGPT asks for permission before interacting with a website. We recommend only interacting with websites you trust.

## Data sharing and sensitive actions

ChatGPT asks for confirmation before sensitive activities, including sharing personal information, making purchases, deleting data, changing account permissions, or sending messages on your behalf.

Before sharing sensitive information, ChatGPT explains what information will be shared, where it will be sent, and why. It asks for your confirmation immediately before sending it, even if you previously approved the website or task.

Instructions from a website or site tool cannot authorize ChatGPT to share information or take sensitive actions on your behalf. If a site tool requests information from outside the current webpage, ChatGPT asks you to verify the request before proceeding.

Enter passwords directly on the website, **never in your ChatGPT conversation.**

## Additional safety checks

Site tools have an additional layer of protection beyond ChatGPT’s standard browser safeguards. Before each call, ChatGPT reviews the tool and the information it would receive to help prevent unauthorized data sharing or actions that don’t match your request.

## Report safety and security vulnerabilities

We welcome reports of safety or security issues you find while using site tools. Report security vulnerabilities through our [Security Bug Bounty](https://bugcrowd.com/engagements/openai), or prompt-injection and other AI safety issues through our [Safety Bug Bounty](https://openai.com/index/safety-bug-bounty/).

# FAQ

## Why didn’t ChatGPT use a site tool?

Site tools are available only when your account and selected model support them and the current webpage provides a tool that matches your request.

Not every website supports site tools, and supported websites may not provide a tool for every task. Tools provided only by embedded content are not currently supported.

If a site tool is unavailable, ChatGPT may still be able to help using its regular browsing capabilities.

## Do I need to install or configure anything?

No separate connection is required. Site tools are currently available only in the ChatGPT desktop app’s built-in browser, not in Chrome. When site tools are available to your account, ChatGPT automatically discovers the tools a supported webpage provides.

## Can site tools work across browser tabs?

ChatGPT can work across tabs, but each site tool is available only on the webpage that provides it. A tool from one page does not carry over to another page or website.

## What happens when I close the webpage?

Site tools are available only while the relevant webpage is open. Reopen the page if you want ChatGPT to use its tools.

## Can I turn off site tools?

Yes. In the ChatGPT desktop app, open **Browser settings**, select **Permissions**, and turn off **Enable site tools**.

## What is WebMCP?

WebMCP is a proposed web standard that lets websites make tools available directly to AI agents. Site tools use it to help ChatGPT work with the page you are viewing.

[Learn more about the built-in browser](https://help.openai.com/articles/20001277)

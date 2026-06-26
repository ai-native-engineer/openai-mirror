<!-- source: https://help.openai.com/en/articles/10093903-chatgpt-search-for-enterprise-and-edu -->

# ChatGPT search for Enterprise and Edu

Learn how ChatGPT search works for Enterprise and Edu workspaces, including admin controls, data sharing, sources, and usage limits.

Updated: 10 days ago

# Overview

ChatGPT search can help ChatGPT answer questions with timely information from the web and links to relevant sources. ChatGPT may choose to search the web based on what you ask, or you can manually choose search when it is available.  
  
For Enterprise and Edu workspaces, ChatGPT search is subject to workspace settings, role permissions where available, usage limits, and applicable restricted-access controls.

## Availability

ChatGPT search can be accessed at [chatgpt.com](https://chatgpt.com/?hints=search) and, where available, in ChatGPT desktop and mobile apps.  
  
Access depends on your ChatGPT plan, workspace settings, role permissions where available, and any restricted-access mode that applies to the workspace.

# How it works

When you ask a question, ChatGPT may determine that current information from the web would improve the response. If ChatGPT search is available, ChatGPT can turn the request into one or more search queries, retrieve relevant results, and use those results to generate an answer with links to sources.  
  
Depending on your request and workspace settings, ChatGPT search may return specialized visual or interactive results, such as structured information, calculations, weather, sports, finance, or other timely information.  
  
For Enterprise and Edu workspaces, ChatGPT search is also shaped by workspace settings, role permissions where available, usage limits, and applicable restricted-access controls. If search is disabled for a workspace or role, ChatGPT will not use web search for affected users, even if a user asks ChatGPT to search.

# Information shared when ChatGPT searches

To provide relevant responses for users in Enterprise and Edu workspaces, ChatGPT searches based on prompts and may share disassociated search queries with the Bing search engine to return web results. Structured data based on your prompt may be shared with Bing or third-party data providers to return specialized visual or interactive results, such as structured information, calculations, weather, sports, finance, or other timely information.  
  
Data sent to Bing and data providers is disassociated from a user’s account. For instance, this data is not accompanied by user or account IDs, device IDs, assigned session IDs, or IP addresses. Requests to these providers are sent on behalf of OpenAI and are not connected to a specific customer or user account.  
  
ChatGPT also collects general location information based on IP address. ChatGPT may share approximate user location derived from an IP address with Bing and specialized data providers to improve the accuracy of results. The IP address itself is not shared with these providers.  
  
ChatGPT for Healthcare workspaces do not use Bing for web search and do not use specialized data providers.

# Managing ChatGPT search for your workspace

Workspace owners and admins can enable or disable ChatGPT search for their workspace and GPTs created in that workspace with the **Web search** setting. For more information about workspace-level admin settings, see: [Managing workspace settings in ChatGPT Enterprise](https://help.openai.com/articles/8411955).  
  
When **Web search** is enabled, ChatGPT and GPTs created in the workspace can browse the internet and use eligible data providers to return relevant information. When **Web search** is disabled, ChatGPT and GPTs created in the workspace cannot use web search, even if a user asks ChatGPT to search or manually selects search.  
  
The **Web search** setting does not apply to third-party GPTs. For more information about GPT controls in managed workspaces, see: [Managing GPT access in Enterprise and Edu workspaces](https://help.openai.com/articles/8555535).  
  
To manage this setting:

1. Go to [Admin settings](https://chatgpt.com/admin/settings).
2. Select **Manage workspace** if prompted.
3. Find **Web search**.
4. Turn **Web search** on or off for the workspace.

## Role-based access controls

In workspaces where role-based access controls are available, admins can also manage ChatGPT search access by role using the **Web search** permission. For more information about role permissions, see: [RBAC](https://help.openai.com/articles/11750701).  
  
If **Web search** access is removed from a role, users assigned to that role cannot use ChatGPT search. Features that require web search, such as [ChatGPT agent](https://help.openai.com/articles/11752874) and [deep research](https://help.openai.com/articles/10500283), may also be unavailable.

# Using ChatGPT search

ChatGPT may automatically search the web when a prompt may benefit from current or recent information.  
  
You can also manually choose web search when it is available:

1. Open [ChatGPT](https://chatgpt.com/).
2. Select the **+** icon and select **Web search**, or type **/** and select **Web search** from the menu.
3. Confirm that **Search** appears in the conversation bar.
4. Enter a prompt or search query.

Users can also type / and select **Search** from the menu.  
  
If the option is available, you can regenerate a response with search by selecting the refresh icon and then selecting **Try again**. This lets ChatGPT try the response again with additional information from the web.

# Viewing sources

ChatGPT responses that use search can include inline citations. Users can select a citation to view the source.  
  
On desktop web, hovering over a citation may show more information about the source.  
  
Users can also find cited sources and other relevant links by selecting **Sources** at the end of a response.  
  
Search results may occasionally include images at the top of a response. You can select an image to view citation details and a link to the source.

# Search, apps, and GPTs

ChatGPT search is separate from [apps](/en/articles/11487775-apps-in-chatgpt).  
  
When connected sources are selected in a conversation, ChatGPT may prioritize connected sources and use web search only when connected sources cannot answer the request, depending on the user’s selection and workspace settings.  
  
Workspace **Web search** controls apply to ChatGPT and GPTs created in the workspace. They do not apply to third-party GPTs.

# Limits and restricted access

Search queries in ChatGPT are subject to the user’s ChatGPT plan usage limits. For more information about Enterprise and Edu models and limits, see: [ChatGPT Enterprise and Edu - Models and Limits](https://help.openai.com/articles/11165333).  
  
In some restricted workspace modes, live web search may be unavailable. Depending on the workspace configuration, ChatGPT may use cached web results instead of live searches, or web search may be disabled. For more information about restricted web search behavior, see: [Offline web search for ChatGPT workspaces](https://help.openai.com/articles/20001203) and [Lockdown Mode](https://help.openai.com/articles/20001061).  
  
If search behavior changes for a specific group, admins should review the workspace **Web search** setting, the user's role permissions, and any Lockdown Mode role assignment.

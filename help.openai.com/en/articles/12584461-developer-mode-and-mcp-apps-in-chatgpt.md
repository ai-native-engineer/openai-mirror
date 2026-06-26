<!-- source: https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt -->

# Developer mode and MCP apps in ChatGPT

Updated: 15 days ago

***Note:*** *Full MCP (Model Context Protocol) support, including modify/write actions, is rolling out in beta to ChatGPT* ***Business, Enterprise, and Edu plans****, Functionality, UI, and permissions may change as we iterate.*

# **Overview**

Using ChatGPT [developer mode](https://platform.openai.com/docs/guides/developer-mode), your organization can build, test, and deploy MCP-powered apps that let ChatGPT securely take action in your tools.  
  
  
**Review and publish custom MCP apps for your company.**  Admins/owners and authorized developers (Enterprise/Edu only) can upload and test MCP apps privately in developer mode – both apps they’ve built, and popular connectors built by others.  
  
  
**Take action with your company’s tools and systems from ChatGPT**, moving beyond read/search by creating apps with interactive UI and apps with full MCP support - including write/modify actions. Kick off workflows, create project management tasks, update your CRM, or combine apps for complex orchestrations.  
  
  
**Test and vet apps before you deploy** - only admins/owners can enable developer mode or publish MCP apps after testing. Enterprise/Edu admins can further control developer authorization and workspace access by RBAC.  
  
Review [Apps in ChatGPT](/en/articles/11487775) and [Build with the Apps SDK](/en/articles/12515353-build-with-the-apps-sdk) for more detail on ChatGPT apps.

# **Availability and requirements**

Apps, full MCP support and developer mode is available for ChatGPT Business and Enterprise/Edu customers on ChatGPT web. Admins/owners can enable developer mode in [workspace settings](https://chatgpt.com/admin/ca), create and test custom apps, and publish them for their workspace.  
  
Enterprise/Edu admins can further use [RBAC](/en/articles/11750701-rbac) to provide developer mode access to select individuals, and then choose who can access each vetted app.

# **Deploying an app**

## **Enabling developer mode**

Workspace admins must first enable developer mode from their [Admin workspace settings.](https://chatgpt.com/admin/ca) The developer mode toggle can be found in **Workspace Settings** **→ Permissions & Roles → Connected Data Developer mode / Create custom MCP connectors.**  See section below for plan specific details.

### **Business plans**

Only admins/owners can enable developer mode and deploy an app. Admins cannot enable developer mode for individual members in their workspace.   
  
You can view the current list of admins and owners for your workspace from Workspace **Settings → Members.**  
  
  
Each admin/owner must enable developer mode for themselves; the toggle does not apply to all admins/owners in a workspace.   
  
Enable developer mode when creating a new custom app, from **Workspace settings > Apps > Create.**

### **Enterprise/Edu plans**

Admins/owners can enable developer mode from their user settings. Navigate to **Settings → Apps → Advanced Settings** to toggle.  
  
You can also enable developer mode for yourself when creating a custom app, from **Workspace settings → Apps &→ Create.**   
  
  
Use RBAC to enable developer mode for a specific set of workspace members.   
  
After access is granted, enabled members can toggle developer mode for their account by navigating to **Settings → Apps → Advanced Settings**.

## **Configuring an app**

You can create a new app or from admin settings or user settings.

* Confirm developer mode is enabled for your account (see above).
* Admins/owners: from **Workspace settings**, navigate to **Apps → Create**.
* Authorized users (including admins/owners): from **user settings**, navigate to **Apps → Create**.
* Provide the endpoint and required metadata for your MCP server.
* Pick the authentication mechanism, if applicable.
* Click **Scan Tools** and wait for the scan to complete. If your server uses OAuth, complete the authorization prompt, then wait for the tool scan to finish.
* Click **Create**.
* After configuration, the app appears as a draft in [**Workspace Settings**](https://www.chatgpt.com/admin/ca) → **Apps → Drafts**.
* In user settings, the new app appears under **Settings → Apps → Enabled Apps**. The new app will have the label **Dev** next to its name.

### **If using OAuth for authentication**

When configuring an app, confirm if your OAuth/OpenID Connect provider is configured to issue refresh tokens, as additional configurations are required in order to maintain connectivity.  
  
For OpenID Connect providers, the standard way to request a refresh token is to include the **offline\_access** scope in the authorization request, and for the provider to advertise support for it in its discovery metadata.  
  
Verify the provider’s discovery **.well-known** **endpoints** (**.well-known/openid-configuration** or **.well-known/oauth-authorization-server**) list **offline\_access** (or your provider’s equivalent) in **scopes\_supported** or a similar capability field. If **offline\_access** (or the equivalent refresh token scope) is not advertised or refresh tokens are not being issued, enable offline or refresh access in your provider’s admin console, tenant settings, or metadata configuration, then recreate the app so ChatGPT fetches the updated metadata.  
  
If OAuth is configured without `offline_access`, ChatGPT may lose access after the original authorization expires because refresh-token renewal may be unavailable, and users may need to reauthenticate.

## Test the new app in ChatGPT

1. Open a new chat and select your draft app from the ChatGPT tools menu, or refer to the app in your prompt.
2. Try different prompts and use cases for your app.
3. Use tools exposed by the app, including write actions.
4. Confirm actions when prompted. ChatGPT asks for confirmation based on app permissions and the action's context. Before testing, review app permissions so testers know what to expect.

These app permissions apply to ChatGPT conversations. Workspace Agents use per-agent controls set by the agent's builder to determine which app actions are available and when end users are asked to approve them. For agent behavior, see: [ChatGPT Workspace Agents for Enterprise and Business](https://help.openai.com/articles/20001143).

## Publish app

***Note:*** *You are responsible for verifying the MCP server and app is safe and appropriate for your organization before publishing.* [*Learn more*](https://platform.openai.com/docs/mcp#risks-and-safety)

Only Admins and Owners can publish apps. Go to **Workplace** **Settings → Apps** to publish. Click on **Drafts** and then the **Publish** button. Review safety warnings (especially for write actions). Once published, apps appear in the workspace’s approved connectors list and in users’ **Apps** settings in ChatGPT with the label **custom** next to the app name.

For Business plans, apps cannot be updated after publishing at launch. To change tools or metadata after publishing, you must recreate and republish. While an app is still in developer mode, the app owner can edit its name and logo from the app's Manage menu in Apps settings. Enterprise/Edu plans have additional controls available to them - read on to find out more.

**Enterprise/Edu Admin & Owner controls**

Enterprise/Edu admins/owners can further use [RBAC](/en/articles/11750701-rbac) to determine who can access the app, and control specific actions that app or connector can take prior to publishing.

* After clicking **Publish** (in the previous step), use **Configure Actions** in the modal that appears to determine what actions the app is allowed, by selecting/deselecting the action. You can also click **Refresh** to pull new actions (deselected by default) or updates to action definitions. Use **Configure Access** to select specific groups to provide access to, prior to publishing.

You can also control app actions after publishing.

* Locate the app in **Workspace Settings** **→ Apps,** and click the ellipsis menu (...) next to the app to be configured, and click **Action control.**
* Updates to the MCP server are not automatically enabled - you can click the **Refresh** button to obtain the latest set of actions, or updates to existing actions. New actions are disabled by default, and changes to existing actions are shown as a diff.

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-bf4a03c572cc602de99fced3/c6cdebce4ed8cd635edd77e899670b10/7a085c78-3467-48a3-a58d-fd003b728eb2)

## Use the new app in chats

* Start a chat and select one or more apps, or use [company knowledge.](/en/articles/12628342-company-knowledge-in-chatgpt-business-enterprise-and-edu)
* You can invoke multiple first-party and third-party apps in a single prompt (e.g., retrieve internal data and then create a ticket based on the result).
* Note: if you use company knowledge, only apps with search/fetch functionality are included.
* For write or modify actions, ChatGPT may ask for confirmation based on app permissions and the action's context. Review app permissions before publishing so users understand when ChatGPT may ask before using the app.

# **Security, safety, and data considerations**

***Note:*** *Connecting to unsafe or untrusted MCP servers may increase exposure to security risks (including prompt injection). Only connect servers you* ***trust****, and ensure builders understand the risks before enabling developer mode.* [Learn more](https://platform.openai.com/docs/mcp#risks-and-safety)

Developer mode is a powerful capability that requires responsible setup and oversight. For write or modify actions, ChatGPT may ask for confirmation depending on app permissions, the action's context, and the action's potential impact. Some especially risky actions may be blocked instead of being presented for approval. Admins/owners see risk warnings when enabling apps that can write or modify data.  
  
You are responsible for vetting and verifying the suitability of custom apps and connectors you build, or third party apps and connectors you add for use in your workspace. Ensure all technical, usage and policy checks pass before you deploy a custom connector.

# **Compliance API**

User conversations — including those using any app — are available in the [Compliance API](https://intercom.help/openai/en/articles/9261474-compliance-api-for-enterprise-customers) for Enterprise/Edu customers.

# **FAQ**

## **Who can enable developer mode?**

* **Enterprise/Edu:** Admins grant access in **Permissions & Roles → Connected Data**. Enabled users then turn it on in **Settings → Apps → Advanced Settings.** Only Admins/Owners can publish. Admins can further configure who gets access by using [RBAC](/en/articles/11750701-rbac).
* **Business**: Only Admins can use developer mode. Turn it on via User Settings → Apps → Advanced settings → Developer mode or **Workspace settings → Apps → Create** on developer mode. Then publish in Workspace settings → Apps.

## **Are there geo restrictions?**

No.

## **Can I test Apps built with Apps SDK in developer mode?**

Yes, you can test apps and apps in development mode

## **Are MCP apps available on mobile?**

No - web only.

## **Can apps be updated after publishing? Can I toggle on/off specific tools (read vs. write vs. fetch)?**

Business admins/owners cannot currently update apps and apps after publishing; recreate and republish to update tools or metadata. Enterprise/Edu admins/owners can enable or disable app/connector actions after publishing. See the Publish app / apps section for more detail.

## **What safety controls are in place for write actions?**

ChatGPT can ask for confirmation before important actions or other changes based on app permissions and the action's context. Admins see risk warnings when enabling apps that can write or modify data.

## **How does OpenAI review app safety?**

OpenAI performs red-teaming, monitoring, and warnings for write actions. Apps in the OpenAI-approved registry have been reviewed before availability. You are responsible for verifying that any app or connector is appropriate for your organization, including apps and connectors you develop, or third party apps and connectors you upload.

## **Can I upload an app someone else built?**

Yes. Admins and developers can upload any app (including open-source or vendor-built). Verify safety and suitability before publishing.

## **Can ChatGPT use multiple apps at once?**

Yes. Workspaces can invoke multiple first-party and third-party apps in a single prompt.

## **Should I use an OpenAI-built app or a custom MCP app?**

OpenAI-built apps are search-only today and do not support write actions. Use custom MCP apps for write/modify capabilities.

## **Can I connect to a local MCP server?**

Not directly. ChatGPT connects to remote MCP servers. If your MCP server runs on a private network, on-premises, or on a developer machine, use [Secure MCP Tunnel](https://developers.openai.com/api/docs/guides/secure-mcp-tunnels) to connect it to supported OpenAI products without exposing the server to the public internet.

## **Are search and fetch tools required for connected servers?**

No. They are no longer required.

## **Can agent mode and deep research use custom apps?**

[Agent mode](https://Agent%20Mode) will not use custom apps. [Deep research](/en/articles/10500283-deep-research) can use custom apps, but for read/fetch actions only - not for write actions.

## **Are apps and full MCP beta available to Pro users?**

Pro users can build apps using the AppsSDK. Full MCP is only available to Business and Enterprise/Edu users, currently. Pro users can connect MCPs with read/fetch permissions in developer mode.

Note that Pro users must continue enabling developer mode to use custom apps.

## **Can I use my custom app with company knowledge?**

Company knowledge supports custom apps with fetch/search access. Enterprise admins and owners govern who can see and access these apps using [RBAC](/en/articles/11750701-rbac). [Apps](/en/articles/11487775) with interactive UI are not currently supported in company knowledge.

## **Do MCP app changes auto-update in my workspace?**

No. After an admin first approves an MCP app for the workspace, ChatGPT uses a “frozen” snapshot of its available tools and inputs. Changes made later by the app’s developer are not applied until an admin reviews and publishes an update.

## **What happens if a tool definition changed after approval?**

If the live app no longer matches the frozen snapshot, tool calls can error. Backward-compatible updates (for example, adding a new optional parameter) may continue to work. If the tool definition is not backward compatible, admins/owners must refresh the tool actions from Workspace settings before continuing. Review the **Publish App** section in this article for more information on how to publish the change.

## **Will users see a prompt to update or notify the admin if a call errors?**

No. Error messages today do not include an auto-prompt to update, and admins are not proactively notified when an app needs review.

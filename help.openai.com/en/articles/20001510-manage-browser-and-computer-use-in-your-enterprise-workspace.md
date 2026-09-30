<!-- source: https://help.openai.com/en/articles/20001510-manage-browser-and-computer-use-in-your-enterprise-workspace -->

# Manage browser and computer use in your Enterprise workspace

Codex administrators can manage access to the in-app browser and control how Codex uses websites and desktop applications. Policies can apply across your workspace or to selected groups.

Updated: 8 hours ago

GPT‑6 Pro, powered by GPT‑6 Astra, is available in ChatGPT for Pro $100, Pro $200, Business and Enterprise plans. Enterprise access also depends on your workspace’s model-access permissions. Plus plans include GPT‑6 Astra in ChatGPT Work and Codex.

**Note**: Astra requires Codex CLI version **0.153.0 or newer**. Additionally, please update to the latest available ChatGPT Desktop app. If you do not see Astra available in Chat, Work or Codex in the desktop app, ensure that you update your app by clicking Menu > **Check for Updates,** even if you recently updated the app due to an automatic update notification or by clicking on the update icon in the sidebar.

# What these controls cover

* **In-app browser:** Lets members open and view websites inside the Codex desktop app.
* **Browser Use:** Lets Codex work with websites through the in-app browser or Chrome using the ChatGPT Chrome extension.
* **Computer Use:** Lets Codex interact with desktop applications on macOS and Windows.

# Set a policy for your workspace or a group

Open [Policies & Configurations](https://chatgpt.com/codex/cloud/settings/policies). You need the appropriate Codex administrator permission to access this page.

1. Select an existing policy or create a new one.
2. Choose who the policy applies to. Use the workspace baseline for general restrictions or a targeted policy for a selected group.
3. Open **Requirements** and configure the Browser Use, Computer Use, and in-app browser controls.
4. Preview the policy for an affected user, then save your changes.

**Requirements** set limits that members cannot relax. **Defaults** are starting settings that members can change within those limits. **Not configured** leaves a setting unset in this policy; another applicable policy or the product default supplies its value.

Policies are processed from top to bottom, and more than one policy can apply to a user. When a matching policy uses **Stops after match**, policies below it are skipped, including the workspace baseline.

# Choose which browser and computer features are available

You can disable the in-app browser pane, Browser Use in the in-app browser, Browser Use through the Chrome extension, or native Computer Use.

You can also prevent members from importing settings and browsing data, including cookies, passwords, and history, from an external browser into the in-app browser. Browser Use access to browser history has a separate control.

# Control browser access and capabilities

## Choose which sites are accessible

In **Browser Use site rules**, set default site access to **Allow** or **Block**, then add exceptions. To allow only approved sites, set default site access to Block and add Allow rules for those sites.

Select **Add site rule** and enter the site’s origin, such as https://example.com. An origin identifies the protocol, host, and port, rather than an individual page. Use supported patterns when a rule should cover multiple hosts.

A site-specific field set to **Default** uses the corresponding value from the Default row. If multiple site rules match, **Block** takes precedence for each permission.

## Choose what Browser Use can do

Use the default and site-specific controls to manage:

* **Site access:** Access to the website.
* **Uploads:** Uploading files to the website.
* **Downloads:** Downloading files from the website.
* **Debug / CDP:** Advanced browser access through the Chrome DevTools Protocol. A separate feature control can disable full CDP access across Browser Use.

## Configure browser approvals

Allowing an operation in a policy does not approve it on a member’s behalf. Approval settings control how access requests are reviewed and how long approvals last.

* **Auto-review:** If auto-review is generally enabled, you can disable it for Browser Use. You can also disable it for individual sites.
* **Approval duration:** An ordinary website approval can last for one turn or one thread. A turn is Codex’s work in response to a user message; a thread is the conversation. You can configure the default duration and site-specific settings. This is separate from saved **Always allow** approvals.
* **Saved site approvals:** Choose whether members can save **Always allow** approvals for individual websites. You can restrict saved approvals by site.
* **Approvals across sites:** Choose whether members can save approvals for capabilities across all websites, including access, uploads, downloads, full CDP access, and history.

Members cannot use an approval to override an admin restriction. Computer Use has a separate control for saved application approvals.

# Review site-tool availability separately

Site tools let ChatGPT work directly with websites open in the ChatGPT desktop app’s built-in browser. Where site tools are available, ChatGPT can use actions provided by a webpage. Allowing browser use does not by itself establish that site tools are available for every account, model or browser - the current page must also provide a supported tool.

Workspace requirements, the user’s browser settings and website-access approvals are separate - a user approval cannot override an administrator restriction. Do not change security requirements solely because a site-tool option is missing.

For the supported browser, end-user controls and site-tool behavior, see: [Using site tools in the ChatGPT desktop app](https://help.openai.com/articles/20001423).

# Control native application access

You can disable Computer Use or restrict it to selected applications.

In **Computer Use app rules**, set default app access to **Allow** or **Block**, then add rules for individual applications. The default applies when no app rule matches. If multiple rules match, Block takes precedence.

Add a rule using the identifier for the application’s platform and type:

* **macOS:** The application’s bundle identifier.
* **Packaged Windows apps:** The Application User Model ID, or AUMID.
* **Other Windows apps:** The executable’s verified publisher and product details, with an optional binary name.

An executable rule identifies the signed application; a filename alone is not enough. Add separate rules for the macOS and Windows applications your members need.

Use **Save app approvals** to control whether members can save **Always allow** approvals for applications.

On macOS, you can prevent members from enabling locked computer use. This restriction does not stop locked computer use that was already enabled.

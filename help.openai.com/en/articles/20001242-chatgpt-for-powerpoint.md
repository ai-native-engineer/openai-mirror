<!-- source: https://help.openai.com/en/articles/20001242-chatgpt-for-powerpoint -->

# ChatGPT for PowerPoint

Use ChatGPT in PowerPoint to create, edit, understand, and polish presentations.

Updated: 17 days ago

# What it is

ChatGPT for PowerPoint is a PowerPoint-native AI experience that lives in a sidebar inside Microsoft PowerPoint. It can help you create, edit, understand, and polish presentations directly, while preserving editable slide structure.

You can use ChatGPT for PowerPoint to create a first draft from source material, add or revise slides in an existing deck, ask questions about a presentation’s story and structure, and improve a deck for a specific audience.

# Who it’s for

It is useful for presentation-heavy work and projects like:

* Building board updates, business reviews, and strategy decks from notes, documents, spreadsheets, or other source material

* Adding or revising slides in an existing presentation

* Tightening a deck for an executive, customer, or internal audience

* Turning long-form content into a clearer presentation structure

* Reviewing a deck’s story, gaps, and likely audience questions

* Applying repeatable presentation workflows through Skills, templates, and connected apps where available

# How to install

You can find ChatGPT for PowerPoint in [Microsoft Marketplace](https://marketplace.microsoft.com/en-us/product/office/WA200010215):

1. Open Microsoft PowerPoint.
2. Go to **Home**.
3. Go to **Add-ins**.
4. Search for ChatGPT.
5. Add it, then open ChatGPT from the ribbon.
6. Sign in with the ChatGPT account that has access.

If your organization can't access the Microsoft Store for this add-in, a Microsoft 365 admin can deploy it internally using the [manifest XML file](https://bps.openai.com/basispoints/api/office/manifest.xml). To download the manifest file, open the link, right-click it, and select Save As, depending on your browser.

Then, in the Microsoft 365 admin center:

1. Go to **Integrated apps**.
2. Select **Deploy Add-in**.
3. Select **Upload custom apps**.
4. Upload the manifest file.
5. Assign it to the appropriate users or groups.

If your organization uses role-based access control (RBAC), an admin may need to enable the add-in.

ChatGPT can make mistakes, including when editing or deleting presentation content. Review outputs before sharing or relying on them.

## How to use it well

* Be specific about what you want changed, what to preserve, and where the edit should happen.

* Example: “Add a risks slide after the market overview. Match this deck’s style and do not change the surrounding slides.”

* Ask for a plan first when you are making larger edits.

* Example: “Before editing, outline which slides you would change and why.”

* Use source material when you want ChatGPT to build or revise a presentation from existing context.

* Review important claims, numbers, and edits before sharing the deck.

## Prompts to try

* “Build a 10-slide board update from these notes and KPIs.”

* “Add a risks slide after the market overview.”

* “Tighten this deck for an executive audience.”

* “Turn this memo into 5 slides.”

* “Make these slides match our house style.”

* “What is the story of this deck?”

## Current limitations

* Template adherence: The product is designed to work within existing presentation templates where possible, but generated or edited slides may not always match a preferred style perfectly.

* Advanced presentation edits: Some advanced PowerPoint editing, chart, shape, formatting, and slide-management capabilities may be limited or still in development.

* Review outputs before relying on them: Outputs may be incomplete or incorrect. Review claims, numbers, citations where available, and slide changes before sharing or relying on them. For important work, duplicate the file first so you can revert if needed.

# Using plugins, skills, and apps with ChatGPT for PowerPoint

Where supported, ChatGPT for PowerPoint can use plugins. A plugin can include skills, apps, and other workflow capabilities. Availability depends on your plan, workspace, and rollout.

Apps connect ChatGPT to approved data sources and actions. Only apps available in the PowerPoint surface and allowed by your workspace and data-source permissions can be used.

# For users

* Open ChatGPT for PowerPoint.

* Click + to access Skills and apps.

* Select a Skill or use @ to invoke it in your prompt.

* Open apps to browse the apps available from your ChatGPT account.

* If an app is not available, check whether it has been enabled by your workspace admin.

* Ask ChatGPT to create, edit, explain, or summarize your presentation.

* Review important claims, citations where available, and slide changes before relying on the output.

# For admins

* Admins can enable ChatGPT for PowerPoint in workspace settings.

* Admins can enable apps in the admin portal and control access to individual apps, where supported.

* App availability may depend on user entitlements, admin settings, and connected data-source permissions.

# Availability and pricing

ChatGPT for PowerPoint is available globally to Free, Go, Plus, Pro, Business, Enterprise, ChatGPT Edu, and K-12 users. Free and Go include limited usage access. Plus, Pro, and Business include access subject to your plan's agentic usage limit.

Agentic usage limits are shared with other agentic features once pricing for those features is effective. ChatGPT for PowerPoint uses the same token-based rates as ChatGPT for Excel/Sheets. For Business, Enterprise, and Edu, usage consumes credits from the workspace credit pool once flexible pricing is effective. For effective dates and plan-specific pricing, see [Using Credits for Flexible Usage in ChatGPT](/en/articles/12642688) for Free, Go, Plus, and Pro, or the [ChatGPT Rate Card](/en/articles/11481834) for Business, Enterprise, and Edu.

Usage may depend on the size and complexity of the presentation task. Larger decks, multi-step edits, and more complex source-grounded requests may use more of your plan’s available usage.

# For enterprise admins and security teams

ChatGPT for PowerPoint is designed to support workspace-level enterprise controls, including policy enforcement, scoped access to authorized files and sources, and secure handling of product state where required.

Enterprise logging and compliance coverage depends on your workspace and current product support. Check the Compliance API documentation for the events available to your organization.

# Privacy, security, and data handling

ChatGPT for PowerPoint runs in Microsoft PowerPoint. Your use of PowerPoint is governed by your agreements with Microsoft.

As part of Microsoft's Add In Marketplace [Terms of Service](https://learn.microsoft.com/en-us/legal/marketplace/marketplace-terms), Microsoft may have the ability to read the content of your PowerPoint files.

To respond, ChatGPT processes your prompt, presentation content you make available, attachments, and relevant connected context. Data handling follows your ChatGPT plan and workspace settings, plus Microsoft's terms for the PowerPoint add-in.

# FAQ

## Can it connect to my other apps or internal systems?

Where apps are supported, availability depends on your ChatGPT plan, admin settings, user permissions, and data-source entitlements. If an app is not available, check with your workspace admin.

## Does it involve Microsoft?

Yes. ChatGPT for PowerPoint runs in Microsoft PowerPoint. Your use of PowerPoint is governed by your agreements with Microsoft.

## What are Skills in ChatGPT for PowerPoint?

Skills are reusable playbooks for presentation work. They can encode workflows, style rules, formatting expectations, and output structures so users do not have to rebuild the same prompt each time.

## How do I use a Skill?

Open ChatGPT in PowerPoint, click + to browse Skills, then select a Skill or invoke it with @ in your prompt.

## What are apps in ChatGPT for PowerPoint?

Apps let ChatGPT for PowerPoint use approved files, systems, and data sources from your ChatGPT account so it can produce more contextual presentation outputs.

## Are all ChatGPT apps available in ChatGPT for PowerPoint?

Only apps available in the PowerPoint surface and allowed by admin controls, user permissions, and data-source entitlements appear.

## Can admins control app access?

Yes. Admins can enable the apps feature and control access to individual apps, where supported.

## Does ChatGPT for PowerPoint support EU Data Residency, EU Inference Residency, and Enterprise Key Management?

Enterprise security and data-residency capabilities depend on the current rollout and your workspace configuration. Admins should confirm the controls shown for their workspace or contact their OpenAI representative.

For Data Residency and Inference Residency availability by region, please refer to our [OpenAI Data Residency and Inference Residency documentation](/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt?utm_source=chatgpt.com).

## Why does the Excel Office Add-in show “add-in could not be started” error during SSO?

Some customers may see:

ADD-IN ERROR

This add-in could not be started. Close this dialog to ignore the problem or click “Restart” to try again.

This can happen during the SSO callback when an older SSO callback URL redirects to OpenAI’s current SSO endpoint. Browser sign-in may still work, but the Windows Office add-in may not complete this redirect reliably.

A Global admin for your tenant should retrieve the ACS URL from [OpenAI Admin Portal](https://admin.openai.com) > Identity > SSO > Manage SSO, then update the OpenAI Enterprise Application in the Identity Provider and make this new URL the default.

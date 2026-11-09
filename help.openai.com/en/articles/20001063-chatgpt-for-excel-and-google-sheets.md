<!-- source: https://help.openai.com/en/articles/20001063-chatgpt-for-excel-and-google-sheets -->

# ChatGPT for Excel and Google Sheets

Use ChatGPT in Excel and Google Sheets to build, update, and understand spreadsheets, and learn how setup works for your plan.

Updated: 10 days ago

Use ChatGPT in Excel and Google Sheets to build, update, and understand spreadsheets, and learn how setup works for your plan.

This feature is available globally to Business, Enterprise, Edu, and K-12 users, and to ChatGPT Free, Go, Pro, and Plus users.

## What it is

ChatGPT for Excel and Google Sheets is a spreadsheet-native AI experience that lives in a sidebar inside your Excel and Google Sheets spreadsheets. It can help you build, update, and explain spreadsheets directly, including large, multi-tab files with formulas, references, and assumptions.

ChatGPT for Excel and ChatGPT for Google Sheets are separate spreadsheet experiences, but they support similar workflows: creating spreadsheets from scratch, asking questions about existing spreadsheets, and making updates using natural language.

# Use ChatGPT for Excel with Codex in the desktop app

You can also use Codex in the [ChatGPT desktop app](https://help.openai.com/articles/20001276) to work directly with an open Microsoft Excel workbook through the ChatGPT for Excel add-in. Codex can inspect and update sheets, formulas, values, formatting, and charts in the workbook. It can also use code and local files you provide as part of the task. This workflow is currently available for Microsoft Excel only.

To get started:

1. Install ChatGPT for Excel using the steps below and sign in to the add-in with the same ChatGPT account you use in Codex. If you use a workspace, select the same one in both.
2. Open an existing workbook or start a new workbook in Microsoft Excel.
3. Open the ChatGPT desktop app and select Codex.
4. Mention **@Microsoft Excel** or ask Codex to work with the open workbook.
5. Review the workbook changes before saving or sharing.

Computer Use is optional. Where available, Codex can use it to open Microsoft Excel and start the add-in. Otherwise, open the workbook and add-in yourself, then continue in Codex.

Direct Excel control may not be used for every spreadsheet request.

## If Codex can’t find your open workbook

1. Check that the add-in and Codex are signed in to the same ChatGPT account. If the accounts differ, select **Log out** in the add-in’s settings menu and sign in with the account you use in Codex. If you use a workspace, select the same one in both.
2. Open the more options menu (•••) in the Excel add-in and make sure **Allow Codex control** is turned on.
3. Keep the workbook and add-in pane open, then ask Codex to find the open workbook again.

# Who it's for

It's great for spreadsheet-heavy work and projects like:

* Building trackers, budgets, plans, and templates from scratch
* Cleaning up messy sheets, including formatting, labels, duplicates, and broken formulas
* Understanding an unfamiliar spreadsheet, including assumptions, drivers, and key formulas
* Updating a model when inputs change and summarizing what changed
* Running scenarios and sensitivity tables
* Reviewing reporting, KPI, planning, and forecasting work

# Install ChatGPT for Excel and Google Sheets

## Excel

You can find ChatGPT for Excel in the [Microsoft Marketplace](https://marketplace.microsoft.com/en-us/product/office/WA200010215):

1. Open Microsoft Excel (desktop or web).
2. Go to **Home**
3. Go to **Add-ins**
4. Search for **ChatGPT**.
5. Add it, then open ChatGPT from the ribbon.
6. Sign in with the ChatGPT account that has your supported plan.

If your organization can't access the Microsoft Store for this add-in, a Microsoft 365 admin can deploy it internally using the [manifest XML file](https://bps.openai.com/basispoints/api/office/manifest.xml). To download the manifest file, open the link, right-click it, and select **Save As**, depending on your browser.

Then, in the Microsoft 365 admin center:

1. Go to **Integrated apps**.
2. Select **Deploy Add-in.**
3. Select **Upload custom apps**.
4. Upload the manifest file
5. Assign it to the appropriate users or groups.

## Google Sheets

* Install ChatGPT from the [Google Workspace Marketplace](https://workspace.google.com/marketplace/app/chatgpt/870214997678).
* Open Google Sheets.
* Open ChatGPT from the Google Sheets Extensions menu.
* Sign in with the ChatGPT account that has your supported plan.

If your organization uses role-based access control (RBAC), an admin may need to enable the add-in.

1. Go to **Workspace settings**.
2. Select **Permissions & roles**.
3. Select **ChatGPT for Excel and Google Sheets**.
4. Select **Enable ChatGPT for Excel and Sheets**.

Please note that this applies to **both** Excel and Google Sheets.

Keep in mind, ChatGPT is not a financial, legal, or tax advisor and any outputs should not be considered advice. AI can also make mistakes, so verify the outputs.

# Use it well

* Be specific about what you want changed (what to preserve, what to overwrite, and where).
* Example: "Update assumptions on the Inputs tab only. Don't change formatting. Summarize changes."
* Ask for a plan first when you're making big edits.
* Example: "Before editing, outline exactly which tabs/ranges you'll modify."
* You can @ mention select sheets in your workbook to focus the prompt.
* ChatGPT for Excel and Google Sheets can search the web for information to pull into your workbook.

## Prompts to try

* "Build a formatted monthly budget with categories, totals, and charts."
* "Why am I getting an error in cell B145? Explain the formula chain and propose a fix."
* "Summarize trends across these three tabs and call out anything unusual."
* "Clean up this sheet: standardize formatting, fix inconsistent labels, and remove duplicates."
* "Update this table to reflect the new assumptions and then list exactly what changed."
* "Create a new scenario tab that compares base, upside, and downside cases."

# Current limitations

* **Separate experience:** Spreadsheet chats operate separately from your main ChatGPT chat history. Conversations and spreadsheet data do not sync between experiences.
* **Limited memory support:** Spreadsheet chats do not have access to ChatGPT memory.
* **Advanced spreadsheet features:** Features such as VBA and macros may not be fully supported.
* **Review outputs before relying on them:** Outputs may be incomplete or incorrect. Review formulas, calculations, citations, and changed cells before sharing or relying on them. For important work, duplicate the file first so you can revert if needed.

# Use Skills and apps with ChatGPT for Excel and Google Sheets

ChatGPT for Excel and Google Sheets support Skills and apps. Skills are reusable playbooks that teach ChatGPT how to handle specific spreadsheet workflows, formats, and review steps.

Apps let ChatGPT for Excel and Google Sheets work with connected data sources so spreadsheet work can be grounded in the right context.

## For users

* Open ChatGPT for Excel or Google Sheets.
* Select + to access Skills and apps.
* Select a Skill or use @ to invoke it in your prompt.
* Open apps to browse the apps available from your ChatGPT account.
* If an app is not available, check whether it has been enabled by your workspace admin.
* Ask ChatGPT to build, update, explain, or summarize your workbook.
* Review formulas, citations, and changed cells before relying on the output.

## For admins

* Admins can enable ChatGPT for Excel and Sheets in workspace settings.
* Admins can enable apps in the admin portal and control access to individual apps, where supported.
* App availability may depend on user entitlements, admin settings, and connected data-source permissions.

# Availability and pricing

ChatGPT for Excel and Google Sheets are available globally to Free, Go, Plus, Pro, Business, Enterprise, ChatGPT Edu, and K-12 users. Free and Go include limited usage access. Plus and Pro include access subject to your plan's agentic usage limit.

Business, Enterprise, Edu, and K-12 customers have a free preview through June 2, 2026; after that, usage follows each plan's credits and usage terms.

Agentic usage limits are shared with other agentic features once pricing for those features is effective. For effective dates and feature-specific pricing, see [Using Credits for Flexible Usage in ChatGPT](https://help.openai.com/articles/12642688) for Plus and Pro or the [ChatGPT Rate Card](https://help.openai.com/articles/11481834) for Business and Enterprise.

Usage depends on the size and complexity of the spreadsheet task. Larger workbooks, multi-step edits, and more complex analysis may use more of your agentic usage limit. Business and Enterprise admins can monitor usage and purchase credits for additional access.

# For enterprise admins and security teams

ChatGPT for Excel and Google Sheets supports workspace-level enterprise controls including data and inference residency where available, Enterprise Key Management, and role based access controls.

Prompts and responses are available in the Compliance API. For technical details, please see the [Compliance API reference](https://chatgpt.com/admin/api-reference#tag/Projects).

# Privacy, security, and data handling

ChatGPT for Excel runs in Microsoft Excel. ChatGPT for Google Sheets runs in Google Sheets. Your use of those products is governed by your agreements with Microsoft or Google, respectively.

As part of Microsoft's Add In Marketplace [Terms of Service](https://learn.microsoft.com/en-us/legal/marketplace/marketplace-terms), Microsoft may have the ability to read the content of your Excel workbook, attachments, and prompts.

What gets processed: To respond, ChatGPT processes your prompt, attachments, and relevant spreadsheet context so it can update your workbook and send you an analysis. Your data is stored locally in the product, and you can delete or download your data directly in the Settings. Some of your data logs may be stored with OpenAI for 30 days for safety and integrity purposes.

# FAQ

## Is this available worldwide?

ChatGPT for Excel and Google Sheets is available globally to Business, Enterprise, Edu, and K-12 users, and to ChatGPT Free, Go, Pro, and Plus users.

## Can it connect to my other apps or internal systems?

Yes. Where apps are supported, availability depends on your ChatGPT plan, admin settings, user permissions, and data-source entitlements. If an app is not available, check with your workspace admin.

## Does it involve Microsoft or Google?

Yes. ChatGPT for Excel runs in Microsoft Excel, and ChatGPT for Google Sheets runs in Google Sheets. Your use of those products is governed by your agreements with Microsoft or Google, respectively.

## What are Skills in ChatGPT for Excel and Google Sheets?

[Skills](https://help.openai.com/articles/20001066) are reusable playbooks for spreadsheet work. They can encode workflows, standards, formatting rules, and output structures so users do not have to rebuild the same prompt each time.

## What Skills are included by default?

ChatGPT for Excel and Google Sheets include default Skills for financial modeling and corporate finance formatting. More Skills may be added over time.

## How do I use a Skill?

Open ChatGPT in Excel and Google Sheets, select + to browse Skills, then select a Skill or invoke it with @ in your prompt.

## What are apps in ChatGPT for Excel and Google Sheets?

[Apps](https://help.openai.com/articles/11487775) let ChatGPT for Excel and Google Sheets use approved files, systems, and data sources from your ChatGPT account so it can produce more contextual spreadsheet outputs.

## Are all ChatGPT apps available in ChatGPT for Excel and Google Sheets?

Apps from a user's ChatGPT account can carry over to ChatGPT for Excel and Google Sheets, subject to admin controls, user permissions, and data-source entitlements.

For MCP apps, tools intended for use in ChatGPT for Excel and Google Sheets should be accurately annotated as read-only and non-destructive. Tools without explicit annotations may be handled conservatively and may not appear in these surfaces.

## Why does the Excel Office Add-in show add-in could not be started error during SSO?

Some customers may see:

> ADD-IN ERROR This add-in could not be started. Close this dialog to ignore the problem or click “Restart” to try again.

This can happen during the SSO callback when an older SSO callback URL redirects to OpenAI’s current SSO endpoint. Browser sign-in may still work, but the Windows Office add-in may not complete this redirect reliably.

A Global admin for your tenant should retrieve the ACS URL from:

1. Go to [**OpenAI Admin Portal**](https://admin.openai.com).
2. Select **Identity**.
3. Select **SSO**.
4. Select **Manage SSO**.

Then update the OpenAI Enterprise Application in the Identity Provider and make this new URL the default.

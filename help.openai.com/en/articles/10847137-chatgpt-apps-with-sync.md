<!-- source: https://help.openai.com/en/articles/10847137-chatgpt-apps-with-sync -->

# ChatGPT apps with sync

Index select knowledge sources in advance, to speed up and help improve ChatGPT’s answers.

Updated: 2 days ago

***Note****: apps with sync are solely available for select paid plans. To check your plan's eligibility, please refer to this article:* [*Apps in ChatGPT*](/en/articles/11487775)

*As of December 17, 2025, we are renaming connectors to apps to present a more unified experience. The term now includes both apps that feature interactive UI and connectors that help you search and reference your information in ChatGPT. We are not removing any existing functionality; previously enabled connectors and company knowledge will continue to work as before.*

## Overview

Apps with the sync capability enable you to find answers faster, reduce context-switching between tools, and make more informed decisions by bringing the most relevant internal information from connected apps into ChatGPT’s response.  
  
Note that if you are an Enterprise or Edu customer with [Enterprise Key Management (EKM)](https://help.openai.com/articles/20000943) enabled, apps with the Sync capability will become **unavailable**.

***Note:*** *Connectors establish a connection to third-party services, and by using them you are also subject to the applicable terms of use of those services. Workspace administrators may determine which connectors are available within your workspace.*

## Using apps with sync

ChatGPT can automatically decide when to use an app with sync to answer your questions, like “Find the deck from our last quarterly review” or “Summarize our 2024 go-to-market strategy.”  
  
You can also explicitly ask ChatGPT to search your app by using an @ mention, or adding it from the **tools menu (+)**.  
  
If you'd prefer ChatGPT not access your app with sync for a particular question, you can include a prompt like “don’t search internally.”  
  
For general instructions to connect apps to your workspace, see: [Apps in ChatGPT](/en/articles/11487775).

## Upgrading apps with sync

Some apps may offer app upgrades over time - for example, adding features, built using MCP, that allow you to take approved actions to complete work from within ChatGPT. You can update the app to take advantage of the new sections, while still preserving previous sync functionality.

* When upgrades are available, Enterprise/Edu admins/owners must first enable the upgraded app from **Workspace settings > Apps > Directory** and clicking **Enable.**

  + Admins/owners can choose to enable or disable sync when re-enabling the app.
* Note that the previous version of the app will continue to function as normal - re-enabling only allows the latest tools/actions to be made available to users.
* For other plans, no workspace configuration is necessary. If you have previously connected the app you'll see an **Upgrade** option on the app's directory page.
* If you choose to upgrade, you may be asked to sign in again. Your existing synced data stays connected.
* After upgrading, you can use both the previous sync functionality and any new actions available from the app (subject to any admin/owner restrictions active in your workspace).

# Data use and controls

## How ChatGPT uses synced data

ChatGPT uses synced app data to help generate responses and to proactively provide helpful suggestions based on your connected information. You have controls in your connector settings.

## Training

* For Business, Enterprise, and Edu workspaces: we do not train generalized models on your workspace data by default.
* For consumer plans: we do not train generalized models on data synced from connected apps or derivations of that data **unless** it becomes part of your ChatGPT conversations (for example, in a response) and your “Improve the model for everyone” setting is on, or if you choose to submit it as feedback.

## Memory

* If you have Memory enabled, ChatGPT may save and use relevant information it has accessed, including from connected apps, to interact with you and provide more relevant and useful responses. You can turn Memory off or manage saved memories in your settings, which can be accessed by going to **Settings > Personalization**.

## Deleting and disconnecting

* **Delete a chat:** Deleting a conversation deletes any synced app data retained in that conversation.
* **Disconnect an app:** Disconnecting stops future syncing and access to that app, but does not delete existing conversations that already used that data.

To remove connected data from your account, delete the conversations where it was used and related saved memories.

# FAQ

## Why use an app with sync?

Syncing can improve response speed and quality, especially for knowledge-heavy prompts like strategy summaries or policy lookups.

## Why can’t I connect to apps?

There are a few reasons why you might not be able to connect to an app:

* **Admin settings:** Workspace owners can control which apps are enabled in your workspace. If an app is not turned on, you won’t be able to connect to it.
* **Outdated app version:** On mobile, make sure you’re using the latest version of the ChatGPT app. Apps require an up-to-date build to appear.

If you’ve confirmed all of the above and still can’t connect to an app, try checking again in a few days or contact your workspace admin.

## How are permissions respected?

Existing permissions are fully respected and kept regularly up to date. Apps are designed to enable users to only discover content via ChatGPT that they can already access in the respective sites.  
  
For Business and Enterprise/Edu plans, this means each employee may receive different responses for the same prompt.  
  
ChatGPT keeps up to date on both changes to files/channels as well as users' access to them. The exact mechanism of this differs depending on how you connect — either we directly record whether a user has access to a file or we sync the permissions for the file itself and associated directory information in order to resolve group membership.

## How does syncing work?

Apps with sync require a one-time initial syncing of files; this will take some time as we index all data from this source, enabling real-time retrieval in context of your ChatGPT queries while respecting all existing file permissions. After the initial sync, files and permissions are updated frequently and typically reflect changes quickly. Note that some changes may take a short time to appear.  
  
Initial syncing can vary depending on how many files you have access to, but happens in a few stages once you connect a source:

|  |  |  |
| --- | --- | --- |
| Sync Initiation | **We’ve initiated the indexing for this source.** | It isn’t yet available in ChatGPT as context, but we’re working on it. Depending on the size of your organization, the full sync may take up to a few days. |
| Partial Sync | **Your most recent data is now available and ready to search** | We’re still completing the full sync in the background, so some results may be missing for now but we’ve synced your most recent data (approximately past 30 days but may vary)**.** Depending on the size of your organization, this process may take up to a few days. |
| Complete Sync | **Your data is fully synced!** | All information from this source is now available as context within ChatGPT. From here on, it will be regularly refreshed to keep things as close to real time as possible. |

## Are there any limits to content retrieval effectiveness or accuracy?

Apps with sync are initially designed to work best for Q&A and search related queries. The most relevant data is sent to the model based on query intent, limiting performance in scenarios requiring aggregation from numerous sources or very complex queries, such as financial data aggregations.

## Can I rename my app connection?

Currently, names for apps with sync cannot be updated.

## Can I use apps with sync on my desktop apps (Windows/macOS) or mobile apps (iOS/Android)?

Currently, only the Windows app has parity with the full experience on ChatGPT.com. We are working toward bringing the full app experience to the rest of our product surfaces - please stay tuned!

## Can I paste Google Drive links to reference them?

Yes, the Google Drive app with sync allows you to reference Google Drive links, e.g. "summarize this [Google Doc link]" as long as the Google Doc is synced and the user has permission to access it.

## Where are apps with sync supported for data residency?

All apps with sync are supported for workspaces with data residency in the United States, Europe (EEA + Switzerland), and Japan. Google Drive and GitHub apps with sync are also supported in all currently supported [data residency regions](/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt).

## I already have the sync version of the app connected — do I need to upgrade an app, if upgrades are available?

No. If you already use the app with sync, it will keep working exactly as it does today. If you want new app capabilities (for example write actions), you can choose to upgrade. Nothing breaks if you don’t upgrade.

## What happens when I “upgrade”?

You may be asked to re-authenticate (OAuth), even if you already had sync enabled. This is required to allow real-time calls to the partner app. Your existing synced data stays intact.

## What other apps will be available in the future?

We’re working on connecting ChatGPT to more tools teams rely on every day—from docs and collaboration to data, CRM, and more, see: [ChatGPT app directory.](https://chatgpt.com/apps)

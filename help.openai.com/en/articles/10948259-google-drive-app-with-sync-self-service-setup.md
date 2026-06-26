<!-- source: https://help.openai.com/en/articles/10948259-google-drive-app-with-sync-self-service-setup -->

# Google Drive app with sync - Self-Service Setup

Learn how ChatGPT Pro users, as well as Enterprise and Business admins can configure this experience for their workspace.

Updated: 2 days ago

# Overview

ChatGPT Pro users, as well as Enterprise and Business workspace owners and admins can set up [Google Drive](/en/articles/10847137-chatgpt-synced-connectors-faq) app with sync in their [ChatGPT Admin Apps settings](https://chatgpt.com/admin/ca), which enables workspace members to use ChatGPT to use up-to-date information from their internal sources. Connections can be created, deleted, or modified at any time.  
  
Below outlines steps for each user type to connect the Google Drive app with sync to their ChatGPT account.

***Note:*** *Google Docs, Sheets, and Slides actions are now available as* ***Google Drive actions****. This unifies all actions into the Google drive app - simplifying Google app usage. Standalone Google Docs, Sheets, and Slides apps rare no longer available on the ChatGPT app directory, and users should connect to the Google Drive app for Docs, Sheets and Slides access.*   
  
*For ChatGPT Enterprise/Edu, these new unified Google Drive actions are* ***off by default*** *until a workspace admin enables them. For ChatGPT Business,* ***they are on by default****. After enablement, Google Workspace admins may need to re-authorize updated Google Drive scopes before users can use these actions, or new users can connect. If you receive complaints from your users that they are unable to connect to Google Drive, please check your Google workspace scope authorizations for Google Drive, Docs, Sheets and Slides, and confirm that all actions in the app have scopes that have been authorized, or turn off actions that you do not want to authorize.*   
  
*Note that the sync feature remains unaffected with this change.*

# Pro

Start by selecting your **Profile Icon** -> **Settings** -> **Apps.** Access the ChatGPT app directory, find Google Drive, and click Connect.  
  
Select the **Sync** option.  
  
You will be redirected to log in to Google Drive, as well as authorize ChatGPT to see and download all your Google Drive files.  
  
Once completed, files will start syncing to your ChatGPT account. Note that it may take some time for the sync to fully complete.

# Business and Enterprise

ChatGPT Workspace Admins can configure apps with sync with one of the following methods:

|  |  |
| --- | --- |
| Self-service | Ideal for flexible deployments where admins want users to connect their own Google accounts quickly without managing service accounts.   **Setup:** Admin enables the app.  Admins can choose to enable for all users by selecting **Deploy to my team**, or allow specific users.  Individual users then connect their Google accounts via OAuth (sign in with Google). |
| Admin-managed (Deploy to my team) | Ideal if admins prefer centralized authentication via service accounts.   **Setup:** Admin sets up service account, so that individual users don’t need to authenticate individually.  Google Workspace admins will need to create a Google service account and an admin account configured with read-only access to Google Drive. ChatGPT then syncs files and existing permissions automatically for all users who are enabled.  After admin configuration is complete, this works automatically for end users (no action required). |

When using **Deploy to Your Team**, ChatGPT Workspace Admins have three options for managing shared drives:

* Include all shared drives: Default selection with no exclusions.
* Include most shared drives (exclude specific ones): Include by default and specify IDs for drives to exclude.
* Exclude most shared drives (include specific ones): Exclude by default and specify IDs for drives to include.

Start by selecting **Workspace settings** -> **Apps** -> **Enabled -> Enable sync**  
  
Note that for Enterprise/Edu workspaces, the Google Drive app with sync supports in-region data residency in supported regions. [Learn more about data residency.](/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)

## Connecting Google Drive to your workspace

To begin set up, Click on **Connect** for Google Drive:  
  
We strongly recommend **Quick setup** for ChatGPT workspaces with ten or fewer users - this option requires minimal admin setup.

For an **Admin-controlled access** set up, a Google Workspace admin will create a Google service account and an admin account. These will be configured with read-only access to your organization’s Google Drive. ChatGPT will then sync files and permissions on behalf of the users you enable the app for. After you’ve completed the setup no action is needed by users of your workspaces. [Please follow these steps for admin-managed setup.](/en/articles/10929079)

![Google Drive setup step to enter a Google Workspace domain, with dolores-lab.com filled in](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-6861bd898bfb5d47f2c29387/4d4e07491e3b8fd44a91300ec3d68e56/image.png)

You’ll be prompted to enter the domain name, usually the one that belongs to your work email address. If not everyone at your company has the same email domain, then you’ll need to provide the primary domain — see [this Google help article](https://support.google.com/cloudidentity/answer/182080) for details.  
  
Please note that this must be a Google Workspace domain: **gmail.com** and **googlemail.com** are not supported.

![Google Drive app permissions dialog selecting workspace members and Enable for everyone](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-242ae5d5edf269d532c21c2e/a91db8cabb91c5156443e724c049ac88/image.png)

**New ChatGPT users will not automatically have access** toGoogle Drive synced connectors**.**

If you add new users to your ChatGPT workspace and want them to use this connection, you will need to also add them as a user of this connection.

Click **Next** to review the creation of this connection:

![Review step for connecting Google Drive in ChatGPT with a Start syncing button](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-6339e3281bb4d0bf19cef98a/78af8c92ce9c561916f7357236672ea2/AD_4nXf8PSteK199baU1nUvqeIs92RmZNx5kdiQDerg8dVWc5NH0xPi0zIWwCsUyNsNn88kFCqUtNvuWHkavEGsMVcIxiayAi66mYc8xmDxxcUABVf_14q5ed-eehvln)

Once you select **Start syncing**, the connection will appear in the admin console:

![Google Drive app details with Self-service connection type configured for dolores-lab.com](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-895393cd867dbccc1031f4ff/8481ca82a83ce32c96dbaccbebc7e3db/AD_4nXfcWLSjiYxHz8tWxQ1cSeU1-LKFf7Z20RQBa5GJmzhu9S-znbFEPF3J-PvGFTzHHW-BP69Av1C9jVPLdXE5AQOP7-GOaABHU2kGufQ6Fpfh6aj1OBWH2idbNrgC)

At this point in time, files in your company’s Google Drive have not yet started syncing to ChatGPT. This will begin as soon as each user goes through the self-service flow.

If using Oauth(self-service set up); each individual workspace member is required to follow the steps below to use the GDrive connector.

Each workspace member can now enable a connection to Google Drive. On [ChatGPT](https://chatgpt.com/), Google Drive is now available for connecting (you can do this in the composer, the settings page, or via a banner on the home screen):

![Connector picker with Google Drive listed and a Connect action](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-84fed514389c38364e356fea/abf9c229b1d74533dd4f90553d84ca9c/AD_4nXdk6vSgraEo0zREbZzvfkgbq1wuOhldiyTYY4ctrVODgqXtmtzWa_XvZpMQ6pAS_U-kNkIQ3KkDLcoQkogEGaYwdcowAYzdgw9RGug0aXTu94je9LPPLNt05Svr)

Users can also enable this connection in the ChatGPT settings, which can be found by clicking on **your profile icon** > **Settings > Apps,** then finding the Google drive app in the app directory.  
  
Each user will need to click **Connect**. A modal will appear explaining that their files will be synced and if they choose Continue then they’ll be directed to Google to complete the flow.  
  
If employees are signed into more than one Google account, they should choose the one they use for work. To prevent accidentally connecting the wrong account, we will ensure the chosen account’s domain matches what you provided when creating the connection.  
  
Upon choosing the account to connect, Google will ask the user to **Continue.**

![Google Sign in to ChatGPT confirmation page with selected account and Continue button](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-75cf49c2c43835f32fa9815f/84ef4074798e9f731c11522cb8cf4c33/AD_4nXdAWetxWHFRICpuJ1Z6F3Qu0e5F94jnKELZAgiX0Rd12mdixH3ZejLE1lL2PrlSshOmgemtzrkn6wl4d8xX3B_QKWz3jsqb3I9Sg1QxhkYdfPxG6awXgYfUgOjk)

When Google asks what ChatGPT can access, select 'See and download all your Google Drive files' before continuing. If this permission is not granted, sync setup will fail due to missing OAuth permissions, and you'll need to disconnect and reconnect Google Drive from ChatGPT, granting all requested permissions.

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-c14945c7c7118ce1c921684f/b543325618f4ad783bb28e0582aec264/AD_4nXdmO50pRUa2so5BKLviVHFLxmCEYX4mXt1cf6JXYU9dpaoZ09N2b3L62KDr8c4WPYzeNoXEiDHb8MDICJcKqs0pRI6pv-nemBfblkxFJMOCRGJZ_CA8b8QUu-OV)

Ensure the first check box is checked before clicking **Continue**:

![Google consent screen for ChatGPT access to Google Drive files with Continue button](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-ed27efffaa95ad712fd12f37/9ae8d2fac017f49275f3469f65e87e00/AD_4nXfoM2jJSJ8tMMaz1bGa8-OYpuPWk30Ggc9WHqaDfXjK4bx16z0yMRVHhOLkxTqsRNEVHZVr5R-vaKgu6bIygGImNJpB-fl3agP5WWAWyqKlxSM5AhC99pX9Jirp)

# Syncing in progress

Once you complete the connection flow, Google Drive will begin syncing.

![ChatGPT Add sources menu with Google Drive already syncing](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-9e886991e8e7d68714dbd698/db55f6529c3158e30913d2fcbfbdd0ff/AD_4nXdjGMq4fZNZz2163Gmr1dIw37kvkXMLF6Ll-HLQgck8gcob-oNFOy2K5Dm5swBKAWoWY5yfInApO_asSrQYHBcrYipJqrEVWDQnnqR-YwtdwXUXjqnSk7g7EfY5)

As your Drive is indexed, you'll see real-time progress here. A partial sync allows you to search recently synced files while the rest continues syncing. Depending on the number of files, full indexing may take anywhere from a few hours to a few days (especially for larger organizations).

![Google Drive sync toggle enabled with tooltip stating Last 30 days synced](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-2f80da6925a4e60780464912/1434344b93614f9b0e0c341dd08e4292/AD_4nXdt48Zs3oIGhtnLYb4yZPqxDDDp1K-ff_XwCHQRG8ljnYPcIyvM49A9pfdBHZlvR6fQzsTHdwzlEkXVvk0bPn-ZqRClpl8SQMLhKUdSPy3Vvy6X_VydQhTIPiSX)

When the progress marker disappears, syncing is complete. From that point forward, ChatGPT will continuously sync any new changes or additions to your Google Drive.

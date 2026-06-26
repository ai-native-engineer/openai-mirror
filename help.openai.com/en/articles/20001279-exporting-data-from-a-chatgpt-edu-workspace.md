<!-- source: https://help.openai.com/en/articles/20001279-exporting-data-from-a-chatgpt-edu-workspace -->

# Exporting data from a ChatGPT Edu workspace

Learn when ChatGPT Edu data export is available, how admins enable it, and how members can keep exported conversations as reference in a personal account.

Updated: 2 days ago

# Overview

ChatGPT Edu workspace members can export their workspace data when both of these conditions are met:

* The workspace has no data residency configuration.
* A workspace admin has enabled data export.

Data export is off by default. When an admin enables it, the setting applies to everyone in the workspace. It cannot be enabled for only certain members, roles, or groups.  
  
Admins can enable or disable whether members can request exports. Members request and download their own exports from their own accounts. Each member can export only their own data.  
  
Workspaces with any data residency configuration are not eligible for this feature.

# Enable data export for your workspace

Workspace admins can enable data export from Workspace settings > Permissions & roles > Workspace.

1. Open your profile menu, then select Workspace settings.
2. Select Permissions & roles, then select Workspace.
3. Under Data export, turn on Allow members to export their own data.

After the setting is enabled, members can request an export from their own ChatGPT settings. Each member can export only their own data.

# Export data from your Edu workspace

1. Sign in to the ChatGPT Edu workspace that contains the data you want to export.
2. Open **Settings**.
3. Select **Data controls**.
4. Under **Export data**, select **Export**.
5. If you are asked to verify your account by email, complete verification, return to ChatGPT, and start the export again.
6. Select **Confirm export**.

You will receive an email when the export is ready. Processing can take up to 7 days. Download the export while you are signed in to the same account that requested it.  
  
The downloaded ZIP file can include:

* `conversations.json`, or numbered conversation JSON files for larger exports
* files and other assets used in conversations
* account and conversation metadata

# Use exported conversations as reference in a personal account

This process is not a full account migration or account rehydration. Uploading the JSON file does not recreate your old chats as separate conversations or restore the original chat sidebar.  
  
You can keep the exported conversations as reference in a personal ChatGPT account:

1. Extract the downloaded ZIP file.
2. Find `conversations.json`. Larger exports may contain numbered conversation JSON files instead.
3. Sign in to the personal ChatGPT account you want to keep using.
4. Start a new conversation.
5. Upload the conversation JSON file. If the file is too large, upload the numbered files separately or split the JSON into smaller files.

The uploaded file is available as reference in that conversation.

# Limitations

* Workspaces with any data residency configuration are not eligible for this feature.
* The admin setting applies to the entire workspace and cannot be limited to selected members.
* This feature does not change the Privacy Portal or privacy-request process.

# Troubleshooting

If an admin does not see **Data export**, confirm that the workspace is a ChatGPT Edu workspace with no data residency configuration.  
  
If a member does not see **Export data**, ask a workspace admin whether data export has been enabled.  
  
For help requesting or downloading an export, see: [How do I export my ChatGPT history and data?](https://help.openai.com/articles/7260999).  
  
For more information about using the exported JSON in another account, see: [Transferring conversations between ChatGPT accounts](https://help.openai.com/articles/9106926).

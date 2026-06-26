<!-- source: https://help.openai.com/en/articles/9106926-transfer-exported-conversations-between-chatgpt-accounts -->

# Transfer exported conversations between ChatGPT accounts

Learn how to upload exported conversation files to another personal ChatGPT account so ChatGPT can use them as reference.

Updated: 3 days ago

## Overview

ChatGPT does not support fully merging accounts or moving conversations from one account’s chat history into another account’s chat history.  
  
You can export conversations from one eligible ChatGPT account, then upload the exported conversation file to a new conversation in another personal ChatGPT account. ChatGPT can use the uploaded file as reference in that conversation.  
  
This is not a full account migration. Uploading exported conversations does not:

* Merge two ChatGPT accounts.
* Recreate previous conversations as separate chats.
* Restore your original chat sidebar.
* Move subscriptions, settings, memories, GPTs, files, or workspace access to another account.

## Availability

You can use this process with exported conversation files from:

* A personal ChatGPT account.
* An eligible ChatGPT Edu workspace, when a workspace admin has enabled data export.

You cannot export data from ChatGPT Business or Enterprise workspaces through ChatGPT settings.  
  
For ChatGPT Edu export eligibility and admin setup, see: [Exporting data from a ChatGPT Edu workspace](https://help.openai.com/articles/20001279).

## Before you begin

Before uploading exported conversations to another account:

* Make sure you can sign in to the account or workspace that contains the conversations you want to export.
* Decide which personal ChatGPT account you want to keep using.
* Review any active Plus or Pro subscriptions across your accounts so you do not keep a subscription you no longer need.

## Export conversations from the original account

To export your conversations, follow the steps in [Exporting your ChatGPT history and data](https://help.openai.com/articles/7260999).  
  
When your export is ready, download the ZIP file while you are signed in to the same account that requested it.

## Upload exported conversations to another account

1. Extract the downloaded ZIP file.
2. Find `conversations.json`. Larger exports may contain numbered conversation JSON files instead.
3. Sign in to the personal ChatGPT account you want to keep using.
4. Start a new conversation.
5. Upload the conversation JSON file.

The uploaded file is available as reference in that conversation.

## If the exported file is too large

If the conversation JSON file is too large to upload, try one of these options:

* Upload the numbered conversation JSON files separately, if your export includes them.
* Split the JSON file into smaller files before uploading.
* Upload only the conversations you need to reference.

## Limitations

This process lets ChatGPT reference exported conversation data in a new conversation. It does not recreate your previous ChatGPT account experience.  
  
Uploading exported conversations does not:

* Add old conversations to your chat history.
* Create separate chats for each exported conversation.
* Restore your original sidebar.
* Combine two accounts.
* Transfer a Plus or Pro subscription.
* Transfer workspace membership.
* Transfer custom instructions, memories, GPTs, or other account settings.

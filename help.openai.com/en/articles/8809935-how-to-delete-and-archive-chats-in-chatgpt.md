<!-- source: https://help.openai.com/en/articles/8809935-how-to-delete-and-archive-chats-in-chatgpt -->

# How to Delete and Archive Chats in ChatGPT

Manage your ChatGPT conversation history by either deleting or archiving chats. Here’s how each option works and what to expect.

Updated: 10 days ago

*Note*: Data retention for certain services may be affected by recent legal developments – please see our [blog post](https://openai.com/index/response-to-nyt-data-demands/) for more details.

# Deleting Chats

### How to delete a chat

1. Go to your ChatGPT chat history sidebar.
2. Hover over the conversation you want to delete.
3. Click the **three dots** (`⋯`) next to the chat title.
4. Select **Delete** from the menu.
5. Confirm your deletion when prompted.

![ChatGPT chat options menu with Archive and Delete actions for a conversation](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-c5a676f63cbc58934abdd6bd/c259b9d9f5056a4a0eaaf37e688b4469/image.png)

### What happens when you delete a chat?

* The chat is **immediately removed** from your chat history view.
* It is **scheduled for permanent deletion** from OpenAI's systems within **30 days**, unless:

  + It has already been **de-identified** and disassociated from your account, or
  + OpenAI must retain it for **security** or **legal** obligations.
* **You cannot recover a chat once it’s deleted.** Deleted chats are not retrievable through the UI, APIs, or support.

# Archiving Chats

### How to archive a chat

1. Go to your ChatGPT chat history sidebar.
2. Hover over the conversation you want to delete.
3. Click the **three dots** (`⋯`) next to the chat title.
4. Select **Archive** from the menu. No confirmation is required.

![ChatGPT chat options menu with Archive selected for a conversation](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-3b8022bffe4081877a61edf5/7a00c36992e4cbebf9a4d4a29065873c/image.png)

### How to manage archived chats

1. Go to **Settings** > **Data controls**, then click the the **Manage** button to the right of **Archived Chats**.
2. From there, you can:

   * **Unarchive** a chat (return it to your active history).
   * **Delete** an archived chat (permanently schedule it for deletion).

![Archived Chats list with an Unarchive conversation tooltip for a saved chat](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-976cd676294a366e12047002/fd6c06838929e2d94b2fb0dbd734f422/image.png)

**Tip:** Archiving is ideal when you want to **hide clutter** without losing important conversations.

# Options for deleting or archiving all chats

**Settings > Data controls** contains options to archive or delete **all** chats at one time.

![ChatGPT settings options to Archive all chats or Delete all chats](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-01ed15d6ba88f6c7f761b8dc/e820362ee07d266bc0c02340f5791b3a/image.png)

Note that these actions will apply to **all** conversations, including those contained within projects.

# Retention Overview

* Chats you keep (unarchived or archived) are saved in your account until you delete them.
* Deleted chats are removed from your view immediately and permanently deleted from OpenAI’s systems within 30 days, unless de-identification or legal exceptions apply.
* Archived chats remain in your account under your standard retention settings — archiving does not delete them.

If you archive a conversation that used connected app data:

* The conversation remains stored in your account.
* Any connected app data referenced in that conversation also remains stored.

To remove both the conversation and any connected app data used within it, you must delete the conversation.  
  
Disconnecting an app will stop future access to that data, but does not delete conversations that already used it.  
  
📚 For a detailed explanation of chat and file retention policies, see [Chat and File Retention Policies in ChatGPT](/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt)

### What happens to connected app data when I delete a chat?

If you’ve connected apps such as Google Drive, Gmail, or Calendar, ChatGPT may use synced app data to help generate responses in your conversations and provide helpful information to you.  
  
Deleting a chat removes both:

* the conversation itself, and
* any synced app data retained within that conversation

from your account, subject to our standard retention and legal obligations.

### Does deleting a chat delete synced data from connected apps?

Deleting a conversation deletes any connected app data that was retained within that conversation.  
  
Disconnecting an app:

* prevents ChatGPT from accessing new data from that app,
* but does not delete past conversations that used that data.

To remove connected app data from your account, delete any conversations that referenced it.

# Troubleshooting missing chats

If your chat history appears empty or conversations are missing, the steps below resolve most issues before you need to contact Support.

* Make sure you’re signed into the correct OpenAI account or workspace (including the right email, SSO method, or team).
* Open **Settings** > **Data controls** and check **Archived Chats** — the conversation may have been archived rather than deleted.
* Confirm the **Chat history & training** toggle in Settings is turned **on**.
* Refresh the page or sign out and back in to reload your history.
* Check [status.openai.com](https://status.openai.com/) for any active incidents that might hide chat history.
* Request a data export via **Settings** > **Data controls** to confirm which chats are still stored in your account.

Deleted chats (including those removed with **Delete all chats**) **cannot be restored.**  
  
When you contact Support, include your account email and sign-in method, workspace or organization name (if applicable), approximate time frames of the missing conversations, and confirm which of the above checks you’ve already completed.

<!-- source: https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt -->

# Chat and File Retention Policies in ChatGPT

Understand how your chats and files are stored, how long they are retained, and how you can manage or delete them when needed.

Updated: 3 days ago

**Note**: Data retention for certain services may be affected by recent legal developments – please see our [**blog post**](https://openai.com/index/response-to-nyt-data-demands/) for more details

# Chats

**Chats** are saved to your account until you delete them manually.

* When you delete a chat (or your account), the chat is **removed from your account immediately** and scheduled for permanent deletion from OpenAI systems within 30 days, unless:

  + The chat has already been de-identified and disassociated from you, or
  + OpenAI must retain it longer for security or legal obligations.
* Once you delete a chat, **you cannot recover it**. Deleting a chat removes it both from your visible chat history and the system after the retention window.

**Archiving vs Deleting:**

* If you simply want to hide a chat from your sidebar (but keep it in your account), you can **archive** it instead of deleting it.
* Archived chats follow the same retention rules as unarchived chats and can be managed in your ChatGPT Settings.
* For additional instructions on how to delete and archive chats, please visit here:

  + [How to archive and delete chats in ChatGPT](/en/articles/8809935-how-to-delete-and-archive-chats-in-chatgpt)

**Temporary Chats:**

* When using Temporary Chat mode, your chats are automatically deleted from OpenAI systems within **30 days**, even without manual deletion.
* Learn more about Temporary Chats here: [Temporary Chat FAQ](/en/articles/8914046-temporary-chat-faq)

**See also:** [How your data is used to improve model performance](/en/articles/5722486-how-your-data-is-used-to-improve-model-performance)

# Files

Files uploaded during a conversation (for example, documents or images) are saved to your Library when Library is available for your account or workspace. Chats and Library files are managed separately: deleting a chat does not delete files saved to Library. You can view and delete saved files from Library.

For Enterprise, Edu, and Healthcare workspaces, files saved to Library are retained according to the workspace’s retention policy. Files that are not saved to Library, such as unsupported or transient upload flows, may expire separately from chat retention settings.

## Custom GPTs and projects

Files uploaded to to a custom GPT or project (including shared projects) are retained until the GPT or project is deleted. Once deleted, the file is removed within 30 days unless legal/security exceptions apply.

# Compliance API Considerations (Enterprise Only)

* **Files saved to Library:** Files uploaded into conversations and saved to Library follow the workspace’s retention policy. They are available through the Library-specific Compliance API endpoints while active.**Files not saved to Library**: Files that are not saved to Library, such as unsupported or transient upload flows, may expire independently of chat retention settings. For Enterprise users, these files expire after 48 hours unless a different retention period applies.
* After a Library file is deleted, expires under the workspace retention policy, or is otherwise no longer active, it becomes unavailable via the Compliance API immediately. OpenAI’s internal backups may retain it for up to 30 additional days, unless OpenAI must retain it longer for security or legal obligations.
* If a file is no longer active, requests to access or delete it through the applicable Compliance API endpoint may return an error such as:

```
{  
  "error":   
    {  
     "message": "File not found in workspace.",  
     "type": "invalid_request_error"  
    }  
}
```

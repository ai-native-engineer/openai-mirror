<!-- source: https://help.openai.com/en/articles/12368225-box-app-with-sync -->

# Box - app with sync

Updated: 10 days ago

## Overview

The Box app with sync lets ChatGPT securely use your Box content to answer questions. You can connect, disconnect, or update the connection at any time. Once enabled, ChatGPT will automatically reference your Box files when relevant.  
  
  
**Type:** app with sync  
  
  
**Where you can use it:** Chat  
  
Learn about [how to connect a new app](/en/articles/11487775-connectors-in-chatgpt#h_615184a466).  
  
  
**Example prompts**

* “Consolidate all the Box documents on [project] into a one-page guide for new hires.”
* “Find and critique our quarterly planning documents for next quarter in Box.”

[Learn more about app use cases and prompts.](/en/articles/12084614-connector-use-cases-and-prompts)

# Capabilities and Permissions

#### What it can access

* **Supported:** .pdf, .docx, .pptx, .xlsx
* **Not indexed:** .zip, .psd, images such as .png, .jpeg. Non-document content like images and videos is not indexed.

#### What it can do

* Read content and metadata for files and folders you can access in Box
* Respect Box permissions, including items shared with you
* Supports Box write actions where available

**Permission requested (scopes):**

* `root_readwrite`
* `ai.readwrite`
* `docgen.readwrite`

**Known limitations**

* Sync time depends on file volume and can take minutes to hours
* Box enforces strict rate limits; syncing may take longer than other providers
* Polling frequency for incremental updates is reduced to respect Box limits
* Admins must enable access for users or groups via role-based access controls (RBAC)

# FAQ

## Can admins control who has access to the app with sync?

Yes, [you can further configure access to users settings with RBAC.](/en/articles/11750701-rbac)

## Can I ask ChatGPT about my Box files right after enabling sync?

Yes—but until syncing has started or completed, ChatGPT will continue to use results from the older Box file search app.  
  
Once the sync status shows as partially complete or fully complete, you’ll start seeing synced results.  
  
Syncing may take anywhere from a few minutes to several hours, depending on how many files you can access.

## When will new or updated files be reflected?

New and updated files are typically reflected within a few days.

## Are file permissions respected by ChatGPT?

File permissions are always respected. Users only have access to their own files and to files that others have shared with them.

<!-- source: https://help.openai.com/en/articles/12364275-dropbox-app-with-sync -->

# Dropbox - app with sync

Updated: 2 days ago

## Overview

The Dropbox app with sync lets ChatGPT securely use your Dropbox content to answer questions. You can connect, disconnect, or update the connection at any time. Once enabled, ChatGPT will automatically reference your Dropbox files when relevant.  
  
  
**Type:** app with sync  
  
  
**Available in:** Chat  
  
Learn about [how to connect a new app](/en/articles/11487775-connectors-in-chatgpt#h_615184a466).

#### Example prompts

* “Consolidate all the Dropbox documents on [project] into a one-page guide for new hires.”
* “Find and critique our quarterly planning documents for next quarter in Dropbox.”

[Learn more about app use cases and prompts.](/en/articles/12084614-connector-use-cases-and-prompts)

## Capabilities and permissions

#### What it can access

* Supported document types: .pdf, .docx, .pptx, .xlsx
* Not indexed: images and videos (e.g., .png, .jpeg, .mp4), archives and design files (e.g., .zip, .psd)

#### What it can do

* Read content and metadata from your Dropbox files and folders
* View sharing settings and collaborators
* Use files directly shared with you (respecting your permissions)
* Supports Dropbox write actions where available

**Permissions requested (OAuth scopes)**

* `openid`
* `email`
* `files.content.read`
* `files.content.write`
* `sharing.write`
* `files.metadata.read`
* `account_info.read`

## Known limitations

* Sync time depends on file volume. It can take minutes to hours.
* Non-document content (e.g., images and videos) is not indexed.
* Admins control access with RBAC. End users must still connect Dropbox and enable sync.

# FAQ

## Can admins control who has access to the app with sync?

Yes, [you can further configure access to users settings with RBAC.](/en/articles/11750701-rbac)

## Can I ask ChatGPT about my Dropbox files right after enabling sync?

Yes—but until syncing has started or completed, ChatGPT will continue to use results from the non-sync app.  
  
Once the sync status shows as partially complete or fully complete, you’ll start seeing synced results.  
  
Syncing may take anywhere from a few minutes to several hours, depending on how many files you can access.

## When will new or updated files be reflected?

New and updated files are typically reflected within a few minutes to about an hour.

## Are file permissions respected by ChatGPT?

File permissions are always respected. Users only have access to their own files and to files that others have shared with them.

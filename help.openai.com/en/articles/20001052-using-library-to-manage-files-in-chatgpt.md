<!-- source: https://help.openai.com/en/articles/20001052-using-library-to-manage-files-in-chatgpt -->

# Using Library to manage files in ChatGPT

Learn how to find, reuse, download, delete, and manage saved or connected files in Library.

Updated: 4 days ago

Library lets you find and reuse files that you upload to or create in ChatGPT. You can browse, search, download, and delete saved files, then add them to other conversations.

When available, Library can also show files and folders from connected Google Drive, Box, Dropbox, and SharePoint accounts. Connected files remain associated with their original service.

## Availability

Library is available to ChatGPT Free, Go, Plus, Pro, and Business users and to Enterprise, Edu, and Healthcare workspaces, including accounts in the European Economic Area, Switzerland, and the United Kingdom.

The full Library experience is available on web. Recent files in the composer and file search are also available on iOS and Android.

Google Drive in Library supports Plus, Pro, Business, Enterprise, Edu, and Healthcare accounts on web, in both the **Chat** and **Work** toggles.

Connected sources, file availability, and workspace controls can vary by account, plan, region, and permissions.

# Understand which files appear in Library

ChatGPT can save uploaded and generated files, including documents, spreadsheets, presentations, PDFs, and images. Generated images also appear in **Images**.

Some files are handled differently:

* Files uploaded in temporary chat aren’t saved to Library while the chat remains temporary. If you save the chat to your history, eligible files may also be saved to Library, subject to availability and storage limits.
* Files uploaded in ChatGPT Health are not saved to Library.
* Files from a connected Google Drive account remain connected to Google Drive.

# Find files in Library

1. Open **Library** from the ChatGPT sidebar.
2. Browse your available files or enter a filename in the search field.
3. Use the available filters to narrow your results.
4. Select the file you want to open.

Available filters can include whether a file was uploaded or generated and its file type. When available, select Show all file types to include files whose names start with a period.

Sidebar search can also show eligible Library files alongside chats and projects. For more information, see: [Finding your chats, projects, and files in ChatGPT](https://help.openai.com/articles/10056348).

# Upload a file

1. Open **Library**.
2. Select **Upload** or drag a file into Library.
3. Choose the file you want to add.

Select **Storage** to review your storage usage, remaining space, and applicable limits.

# Add a Library file to a chat

1. Open a conversation.
2. Select the composer menu.
3. Select **Add from library**.
4. Select the file you want to use.

A file added from Library stays in Library unless you delete it separately.

# Browse connected Google Drive files

Connect the Google Drive app in ChatGPT with the permissions needed to browse files and folders. In a workspace, your admin must also keep the required public actions enabled. Library includes files and folders in My Drive and items shared directly with you. Shared Drives aren’t included.

ChatGPT follows the permissions of the Google account you connected. Drive files stay connected to their original source.

You can add a Drive file to a conversation from Library, from the composer, or with an @mention. You can also select a folder in Library and ask ChatGPT to work across the files it contains.

You can keep Google Docs, Sheets, or Slides open beside your conversation while ChatGPT summarizes, analyzes, or compares their contents. Where supported and authorized, ChatGPT can update the source file directly. Open the original file in Google Drive for editing or collaboration features that aren’t supported in ChatGPT.

For more information about connected apps and permissions, see: [Apps in ChatGPT](https://help.openai.com/articles/11487775).

# Manage connected-app access

To browse files and folders from Google Drive, Box, Dropbox, or SharePoint in Library, your app connection needs the required permissions. In a workspace, your admin must also keep the required public actions enabled.

## Reconnect an app

If you need to update an app’s permissions for Library:

1. Open Settings.
2. Select Apps.
3. Select the connected app.
4. Select Reconnect.
5. Sign in and approve the requested permissions.

Reconnecting updates the app’s permissions. It does not delete files or folders from the original service. If your organization requires admin approval for new permissions, contact your workspace or IT administrator.

## Workspace controls

Workspace admins can enable or disable public actions for supported apps. If an action required by Library is disabled, the provider or affected Library features may be unavailable until the action is enabled again.

Private upload and write actions are not required to browse connected folders. Members in read-only workspaces may still be able to browse files, but uploads and changes can fail.

# Download a file

1. Open **Library**.
2. Select one or more files.
3. Select **Download**.

# Delete a file

These steps apply to files uploaded to or created in ChatGPT. Connected Google Drive files and folders can’t be deleted from ChatGPT. To delete or manage them, open the original item in Google Drive.

1. Open **Library**.
2. Select the file you want to remove.
3. Select **Delete**.

If **Recently deleted** is available, you may be able to restore the file before it is permanently deleted. Select **Delete forever** to remove one file or **Delete all** to remove all eligible files sooner.

OpenAI schedules deleted files for permanent deletion within 30 days, unless the file was already de-identified and disassociated from your account or OpenAI must retain it longer for security or legal obligations.

Deleting a chat does not delete a file that remains saved separately in Library. For more information, see: [Chat and file retention in ChatGPT](https://help.openai.com/articles/8983778).

# Share files and folders

Where Library sharing is available, you can share files and folders with specific people or across your workspace. Choose an available access level, such as Viewer or Editor, and manage access from the sharing dialog. Recipients can find shared content in Shared with me.

# Manage automatic Library search

When the **Library search** setting is available, it controls whether ChatGPT can automatically search eligible Library files when answering your questions.

To update the setting:

1. Open **Settings**.
2. Select **Personalization**.
3. Expand **Advanced**.
4. Turn **Library search** on or off.

Turning off **Library search** does not prevent you from browsing Library, searching manually, opening files, or attaching files yourself. Workspace administrators may control whether automatic file referencing is available.

# Review file and storage limits

## File size limits

* Files uploaded to a GPT or conversation are limited to 512 MB per file.
* Text and document files are limited to 2 million tokens per file. This token limit does not apply to spreadsheets.
* CSV and spreadsheet files are limited to approximately 50 MB, depending on row size.
* Images are limited to 20 MB per image.

## Library storage limits

* Free: 500 MB.
* Go: 4 GB.
* Plus and Business: 20 GB.
* Pro: 100 GB.

Library storage is separate from daily chat and attachment limits. Workspace storage and retention can differ from individual-plan limits.

# Understand memory, model improvement, and privacy

When memory is enabled, ChatGPT may use relevant files to personalize responses where that feature is available.

For individual services, OpenAI may use eligible files and chats to improve models when **Improve the model for everyone** is on. You can manage this setting in **Data controls**.

By default, OpenAI does not use content from ChatGPT Business, Enterprise, Edu, or ChatGPT for Healthcare workspaces to train its models.

For information about data from connected Google Drive files and folders, see: [Google app data controls](https://help.openai.com/articles/10408842).

For more information, see: [Memory in ChatGPT](https://help.openai.com/articles/8590148), [Data controls in ChatGPT](https://help.openai.com/articles/7730893), and [How your data is used to improve model performance](https://help.openai.com/articles/5722486).

# Manage Library in an organization

Files saved to Library follow the applicable workspace retention policy. Workspace owners may control whether ChatGPT automatically references Library files when responding. Turning off automatic referencing does not remove Library or prevent members from browsing, searching, opening, or attaching files themselves.

Automatic referencing is off by default for ChatGPT for Healthcare workspaces.

Authorized users with the required Compliance API permissions may be able to export or delete Library files through supported Library-specific endpoints.

For more information, see: [OpenAI Compliance Platform for Enterprise and Edu customers](https://help.openai.com/articles/9261474).

<!-- source: https://help.openai.com/en/articles/8724843-file-storage-quota-errors-for-api-users -->

# File storage quota errors for API users

What to do when you encounter an error about reaching your file storage quota for assistants.

Updated: 14 days ago

As of May 21 2025, we’ve added new built-in tools to the Responses API—[remote MCP servers](https://platform.openai.com/docs/guides/tools-remote-mcp), Image Generation, Code Interpreter, and an upgraded File Search—along with background mode and encrypted content, so you can build agents that pull richer context and run more reliably. For details, see our [Responses API](https://platform.openai.com/docs/quickstart?api-mode=responses) docs.

OpenAI currently supports a file storage quota of 2.5 TB of files per project. If this quota is breached, you will see the following error:

```
You have exceeded your file storage quota. Projects are limited to 2.5 TB of files. Please reduce the file size or contact support.
```

We recommend\* deleting unused files\* stored on your account. Some customers implement regular cleanup jobs for unused files to avoid this issue, since raising the storage quotas can only be done in rare circumstances. You can [view and list files with](https://platform.openai.com/docs/api-reference/files/list) the API. If you still need your file storage quota raised, please let us know by starting a conversation on [help.openai.com](https://help.openai.com/) with our help bot.

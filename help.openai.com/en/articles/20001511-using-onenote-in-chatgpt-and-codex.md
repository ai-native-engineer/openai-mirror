<!-- source: https://help.openai.com/en/articles/20001511-using-onenote-in-chatgpt-and-codex -->

# Using OneNote in ChatGPT and Codex

Learn how to work with notes through the OneNote plugin and understand notebook access limits.

Updated: 2 days ago

**Note:** The plugin may not be available for all workspaces

The OneNote plugin can help you find and summarize notes, collect decisions and action items, and create or update notes through supported actions. Available capabilities depend on your account, workspace, product surface and Microsoft permissions.

# Connect OneNote

Find the OpenAI-developed plugin in Plugins and follow the connection prompts. Sign in to the Microsoft account that owns or has the supported access to the notes you want to use. A managed workspace or Microsoft organization may require administrator approval.

For general installation and selection instructions, see [Plugins in ChatGPT and Codex](https://help.openai.com/articles/20001256). Connecting OneNote does not expand your Microsoft permissions.

## Find and summarize notes

Give the notebook, section or page name and describe the information you need. For example:

Find the decisions and open questions in my Project Apollo notes. Include links to the source pages.

A specific notebook, section and date range helps narrow the request. Some searches cover a bounded set of pages. If the result is incomplete, narrow the request or ask to continue the search before assuming that the information is absent.

## Understand notebook access

Personal notebook operations are limited to notebooks owned by the connected Microsoft account. A personal notebook shared with you by someone else may not appear in that workflow.

Microsoft 365 group and SharePoint site notebooks use separate supported shared-notebook workflows. Identify the group or site and intended notebook when requesting those notes. Access to a notebook in Microsoft's product does not mean every OneNote plugin operation supports that notebook type.

## Create or update a note

Specify the destination notebook, section and page and the change you want. For example:

Append these meeting decisions to the Project Apollo launch page. Keep the existing notes unchanged.

Review the target and proposed change before authorizing an action. A connection that can read notes may not have permission to create or edit them. Workspace policy, Microsoft permissions and approval requirements still apply.

## Copy a page

If the supported workflow copies a page, allow the copy operation to finish and check the destination before starting another copy. An accepted request is not the same as a completed copy. If the outcome is unclear, avoid repeating the request until its status is resolved.

## Troubleshooting

### OneNote is missing or disabled

Check that you are using the intended account and workspace. In a managed workspace, ask the administrator to review the plugin and its required app settings. Availability can vary by rollout and surface.

### Microsoft asks for administrator approval

Ask your Microsoft administrator to review the requested permissions for the connection. Follow the approval flow shown; do not share passwords, tokens or client secrets with support.

### A notebook or page is missing

Confirm the connected Microsoft account and whether the notebook is personally owned, shared with you, or stored in a group or SharePoint site. Check the supported workflow for that notebook type. Narrow the search to the intended notebook or section and check whether the result was incomplete.

### A write or copy fails

Check that the same Microsoft account can perform the intended change directly and that your workspace allows the action. Note the exact target, error and time. If a copy outcome is unknown, check the destination and existing operation status before trying again.

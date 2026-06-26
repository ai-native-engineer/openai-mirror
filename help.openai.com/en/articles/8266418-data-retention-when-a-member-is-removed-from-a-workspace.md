<!-- source: https://help.openai.com/en/articles/8266418-data-retention-when-a-member-is-removed-from-a-workspace -->

# Data retention when a member is removed from a workspace

Learn what happens to a user's conversations and data if they are removed from a workspace.

Updated: 3 days ago

# Overview

When a member is removed from a ChatGPT workspace, their access to that workspace is revoked immediately. Whether their conversations and data are retained or restored later depends on the plan, feature, and the respective workspace’s retention policy.

## User Removal vs. Content Deletion

This article outlines data retention behavior when a **user is removed** from a ChatGPT workspace. If a user **deletes content themselves** through the ChatGPT UI, or content is deleted by Compliance API (for Enterprises), it follows the policies outlined in [Chat and File Retention Policies](https://help.openai.com/articles/8983778).

# Data retention by workspace type

## Enterprise and Edu workspaces

Removing or deprovisioning a member, either manually or via SCIM, follows the workspace’s configured **data‑retention policy**.

* **If retention is indefinite:** The removed member’s chats, files, and canvas documents persist indefinitely. If they are re‑added, their content is restored.
* **If retention is time‑bound:** Content is retained only for the configured duration (90 days, 180 days, etc). After that window, data will no longer be available.

## Business workspaces

* **Retention:** Chats, files, and canvas documents are retained **indefinitely**.
* **Restoration on re‑add:** If the member is re‑added, their content is restored.

# Data retention by feature

For all features, if a member is re-added to the workspace before the associated data is deleted, access to the relevant content is restored.

## Conversations and files

Conversations and files are flagged for deletion in accordance with the workspace's data-retention policy.

## Canvas documents

Canvas documents are flagged for deletion in accordance with the workspace's data-retention policy.

## Projects and GPTs

On removal, a member’s projects and GPTs are reassigned to a workspace owner, and are **not** flagged for deletion. If the member rejoins the workspace, projects and GPT ownership is transferred back to the member.  
  
Conversations held within projects and GPTs are flagged for deletion in accordance with the workspace's data-retention policy.  
  
  
**Privacy note:** When projects or GPTs are reassigned to a workspace owner, only ownership of the project or GPT changes. Conversations and files created by the removed member are not transferred, and are not visible to the workspace owner.

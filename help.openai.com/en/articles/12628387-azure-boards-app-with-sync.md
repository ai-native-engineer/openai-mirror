<!-- source: https://help.openai.com/en/articles/12628387-azure-boards-app-with-sync -->

# Azure Boards — app with sync

Updated: 9 days ago

## Overview

The Azure DevOps app with sync lets ChatGPT securely access your team’s Azure DevOps projects and teams, work items and comments to answer questions. You can connect, disconnect, or update the connection at any time. Once enabled, ChatGPT will automatically reference content in Azure DevOps when relevant.  
  
  
**Type:** app with sync  
  
  
**Where you can use it:** chat, deep research  
  
  
[**Learn more about connecting a new app**](/en/articles/11487775-connectors-in-chatgpt#h_615184a466).

## Example prompts

* “List Azure DevOps work items assigned to me due this week”
* “Summarize comments on bugs in Sprint 10”
* “Find work items tagged 'blocked' across projects”

[**Learn more about app use cases and prompts.**](/en/articles/12084614-connector-use-cases-and-prompts)

## Capabilities and permissions

## What it can access

* Projects and teams

**Accessing Items below require sync to be enabled:**

* Work items (user stories, tasks, bugs) and comments
* Areas, iterations, states, tags
* Attachment metadata (names, links)

## Not indexed

* Large binary attachments (e.g., videos), embedded media, and unsupported file types
* Items outside your permission scope
* System-generated or ephemeral metadata not exposed via the API

## Permissions (scope)

```
vso.profile  
vso.project  
vso.work  
offline_access
```

## Known limitations

* Initial sync time depends on data volume (minutes to hours)
* API rate limits and provider throttling may delay syncs
* Permission or configuration changes are applied on the next sync cycle
* Some attachment binaries or non-text content may be excluded
* If you have multiple Azure domains configured, ChatGPT picks the first domain for the connection.

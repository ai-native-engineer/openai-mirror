<!-- source: https://help.openai.com/en/articles/12628397-clickup-app-with-sync -->

# ClickUp — app with sync

Updated: 10 days ago

## Overview

The ClickUp app with sync lets ChatGPT securely access your team’s ClickUp spaces, folders, lists, tasks and subtasks to answer questions. You can connect, disconnect, or update the connection at any time. Once enabled, ChatGPT will automatically reference content in ClickUp when relevant.  
  
  
**Type:** app with sync  
  
  
**Where you can use it:** Chat, deep research  
  
  
[**Learn more about connecting a new app**](/en/articles/11487775).

## Example prompts

* “List ClickUp tasks due today across all spaces”
* “Summarize comments on tasks tagged 'urgent'”
* “Find blocked tasks in the 'Onboarding' list”

[Learn more about app use cases.](/en/articles/12084614)

## Capabilities and permissions

## What it can access

* Spaces, folders, lists
* Tasks and subtasks
* Comments and checklists
* Custom fields, tags, assignees, due dates
* Attachment metadata (names, links)

## Not indexed

* Large binary attachments (e.g., videos), embedded media, and unsupported file types
* Items outside your permission scope
* System-generated or ephemeral metadata not exposed via the API

## Permissions (scope)

* read

## Known limitations

* Initial sync time depends on data volume (minutes to hours)
* API rate limits and provider throttling may delay syncs
* Permission or configuration changes are applied on the next sync cycle
* Some attachment binaries or non-text content may be excluded

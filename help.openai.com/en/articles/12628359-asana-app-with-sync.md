<!-- source: https://help.openai.com/en/articles/12628359-asana-app-with-sync -->

# Asana — app with sync

Updated: 10 days ago

## Overview

The Asana app with sync lets ChatGPT securely access your team’s Asana projects, tasks, and comments to answer questions. You can connect, disconnect, or update the connection at any time. Once enabled, ChatGPT will automatically reference content in Asana when relevant.  
  
Find this app in the [app directory](https://chatgpt.com/apps), or from Settings > Apps.  
  
The Asana app has been upgraded and now offers new MCP actions, including write actions. Existing sync behavior is unaffected. If you have previously connected the Asana app and want to use newly available actions, navigate to the ChatGPT [app directory](https://chatgpt.com/apps), locate the Asana app, and click upgrade (note - may require workspace admin/owner approval).  
  
  
**Type:** app with sync  
  
  
**Where you can use it:** chat, deep research  
  
  
[**Learn more about setting up apps in ChatGPT.**](/en/articles/11487775)

## Example prompts

* “Summarize overdue Asana tasks by project”
* “Find tasks assigned to me due this week”
* “Draft a status update from recent task comments”

[**Learn more about app use cases and prompts.**](/en/articles/12084614)

## Capabilities and permissions

### What it can access

* Projects and sections
* Tasks and subtasks
* Comments and activity notes
* Tags, custom fields, assignees, due dates
* Attachment metadata (names, links)

### Not indexed

* Large binary attachments (e.g., videos), embedded media, and unsupported file types
* Items outside your permission scope
* System-generated or ephemeral metadata not exposed via the API

### Permissions (scope)

* default
* `Full Permissions` are required to sync project sections and tasks data that currently don't have a read-only scope defined.

### Known limitations

* Initial sync time depends on data volume (minutes to hours)
* API rate limits and provider throttling may delay syncs
* Permission or configuration changes are applied on the next sync cycle
* Some attachment binaries or non-text content may be excluded

<!-- source: https://help.openai.com/en/articles/20001041-pipedrive-app-with-sync -->

# Pipedrive - app with sync

Updated: 14 days ago

## Overview

The Pipedrive app with sync lets ChatGPT securely access your team’s Pipedrive CRM data—such as deals, contacts, and activities—to help answer questions, generate summaries, and draft updates. You can connect, disconnect, or update the connection at any time. Once enabled, ChatGPT will automatically reference relevant Pipedrive data when it’s helpful.  
  
Find this app in the [app directory](https://chatgpt.com/apps), or from **Settings → Apps**.  
  
  
**Type:** app with sync **Where you can use it:** chat, deep research  
  
  
[Learn more about setting up apps in ChatGPT.](/en/articles/11487775)

## Example prompts

* “Summarize my open deals by stage and expected close date”
* “Find deals assigned to me that haven’t had activity in the last 14 days”
* “Draft a follow-up email based on the latest notes from this deal”
* “Create a weekly pipeline summary from recent deal updates”

[Learn more about app use cases and prompts.](/en/articles/12084614)

## Capabilities and permissions

### What it can access

* Deals and pipelines
* Contacts (people and organizations)
* Activities and reminders
* Notes and comments
* Owners, stages, statuses, and close dates
* Attachment metadata (names and links)

### Not indexed

* Large binary attachments (e.g., videos), embedded media, and unsupported file types
* Items outside your permission scope
* System-generated or ephemeral metadata not exposed via the API

### Permissions (scope)

**default**  
  
Read access is required to sync CRM data such as deals, contacts, and activities. The app respects your existing Pipedrive permissions and only accesses data you are allowed to view or edit.

## Known limitations

* Initial sync time depends on data volume (minutes to hours)
* API rate limits and provider throttling may delay syncs
* Permission or configuration changes are applied on the next sync cycle
* Some attachment binaries or non-text content may be excluded

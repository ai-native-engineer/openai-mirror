<!-- source: https://help.openai.com/en/articles/12628389-basecamp-app-with-sync -->

# Basecamp — app with sync

Updated: 10 days ago

## Overview

The Basecamp app with sync lets ChatGPT securely access your team’s Basecamp projects and message boards, to‑dos and to‑do lists to answer questions. You can connect, disconnect, or update the connection at any time. Once enabled, ChatGPT will automatically reference content in Basecamp when relevant.  
  
  
**Type:** app with sync  
  
  
**Where you can use it:** Chat, deep research  
  
  
[**Learn more about connecting a new app**](/en/articles/11487775-connectors-in-chatgpt#h_615184a466).

## Example prompts

* “Summarize recent Basecamp to‑dos completed in Project A”
* “List overdue to‑dos assigned to me”
* “Draft a status update from message board activity”

[**Learn more about app use cases and prompts.**](/en/articles/12084614-connector-use-cases-and-prompts)

## Capabilities and permissions

## What it can access

* Projects and message boards
* To‑dos and to‑do lists
* Messages and comments
* Docs and files metadata
* Schedule/events metadata

## Not indexed

* Large binary attachments (e.g., videos), embedded media, and unsupported file types
* Items outside your permission scope
* System-generated or ephemeral metadata not exposed via the API

## Permissions (scope)

```
read
```

## Known limitations

* Initial sync time depends on data volume (minutes to hours)
* API rate limits and provider throttling may delay syncs
* Permission or configuration changes are applied on the next sync cycle
* Some attachment binaries or non-text content may be excluded
* If you have multiple Basecamp domains configured, ChatGPT picks the first domain for the connection.

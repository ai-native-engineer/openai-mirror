<!-- source: https://help.openai.com/en/articles/12628448-zoho-desk-app-with-sync -->

# Zoho Desk — app with sync

Updated: 10 days ago

## Overview

The Zoho Desk app with sync lets ChatGPT securely access your team’s Zoho Desk tickets and threads, contacts and accounts to answer questions. You can connect, disconnect, or update the connection at any time. Once enabled, ChatGPT will automatically reference content in Zoho Desk when relevant. Manage this app in Settings > Apps. Find Zoho Desk in the [app directory](https://chatgpt.com/apps) in ChatGPT.  
  
  
**Type:** app with sync  
  
  
**Where you can use it:** Chat, deep research  
  
  
[**Learn more about setting up apps in ChatGPT.**](/en/articles/11487775)

## Example prompts

* “Summarize Zoho Desk tickets created this week”
* “List high‑priority tickets awaiting agent response”
* “Draft a response for a customer follow‑up”

[**Learn more about app use cases and prompts.**](/en/articles/12084614)

## Capabilities and permissions

### What it can access

* Tickets and threads
* Contacts and accounts
* Ticket fields, status, priorities, tags

### Not indexed

* Large binary attachments (e.g., videos), embedded media, and unsupported file types
* Items outside your permission scope
* System-generated or ephemeral metadata not exposed via the API

### Permissions (scope)

* Desk.tickets.READ
* Desk.basic.READ
* Desk.events.READ
* Desk.contacts.READ
* Desk.tasks.READ

### Known limitations

* Initial sync time depends on data volume (minutes to hours)
* API rate limits and provider throttling may delay syncs
* Permission or configuration changes are applied on the next sync cycle
* Some attachment binaries or non-text content may be excluded

<!-- source: https://help.openai.com/en/articles/12628380-aha-app-with-sync -->

# Aha! — app with sync

Updated: last month

## Overview

The Aha! app with sync lets ChatGPT securely access your team’s Aha! products and releases, epics, features, and requirements to answer questions. You can connect, disconnect, or update the connection at any time. Once enabled, ChatGPT will automatically reference content in Aha! when relevant.  
  
  
**Type:** app with sync  
  
  
**Where you can use it:** Chat, deep research  
  
  
[**Learn more about connecting a new app**](/en/articles/11487775-connectors-in-chatgpt#h_615184a466)

## Example prompts

* “Summarize Aha! features planned for the next release”
* “Draft release notes from recent feature updates”

[**Learn more about app use cases and prompts.**](/en/articles/12084614-connector-use-cases-and-prompts)

## Capabilities and permissions

## What it can access

* Products and releases
* Epics, features, requirements
* Comments and status
* Fields and metadata

## Not indexed

* Large binary attachments (e.g., videos), embedded media, and unsupported file types
* Items outside your permission scope
* System-generated or ephemeral metadata not exposed via the API
* Ideas and votes

## Permissions (scope)

* Default

## Known limitations

* Initial sync time depends on data volume (minutes to hours)
* API rate limits and provider throttling may delay syncs
* Permission or configuration changes are applied on the next sync cycle
* Some attachment binaries or non-text content may be excluded

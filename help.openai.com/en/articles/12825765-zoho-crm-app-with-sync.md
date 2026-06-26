<!-- source: https://help.openai.com/en/articles/12825765-zoho-crm-app-with-sync -->

# Zoho CRM - app with sync

Updated: 15 days ago

## Overview

The Zoho CRM app with sync lets ChatGPT securely access your Zoho CRM leads, contacts, accounts, deals, and activities to answer questions. You can connect, disconnect, or update the connection at any time. Once enabled, ChatGPT will automatically reference your Zoho CRM content when relevant.  
  
  
**Type:** app with sync  
  
  
**Where you can use it:** chat, deep research  
  
  
[**Learn more about connecting a new app**](/en/articles/11487775-connectors-in-chatgpt#h_615184a466).

## Example prompts

* Pull my open deals closing this month in Zoho CRM.
* Find the contact details for 'Acme Corp' and summarize recent activity.
* Create a new lead named Jane Doe with email [jane@test.com](mailto:jane@acme.com).

[**Learn more about app use cases and prompts.**](/en/articles/12084614-connector-use-cases-and-prompts)

## Capabilities and permissions

## What it can do

* Leads, contacts, accounts (companies), and deals with core fields and metadata
* Activities (tasks, calls, events) and notes when accessible
* Owner, stage/status, and timestamp metadata for CRM records

## Not indexed

* Large binary attachments or unsupported file types (e.g., videos)

## Permissions (scope)

```
ZohoCRM.modules.ALL  
ZohoCRM.users.ALL  
ZohoCRM.org.ALL  
ZohoCRM.settings.ALL
```

## Known limitations

* At minimum, the following standard modules must be available to activate the connector:

  + Accounts
  + Contacts
  + Deals
* Initial sync time scales with CRM data volume across modules.
* API limits and quotas from Zoho may throttle sync frequency.
* Field- and module-level permissions in Zoho CRM determine visibility; restricted records are not indexed.
* Large attachments may be skipped or partially indexed.
* We do not currently support custom modules.

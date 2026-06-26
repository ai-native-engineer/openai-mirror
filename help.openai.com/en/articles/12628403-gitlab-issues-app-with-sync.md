<!-- source: https://help.openai.com/en/articles/12628403-gitlab-issues-app-with-sync -->

# GitLab Issues — app with sync

Updated: 10 days ago

## Overview

The GitLab Issues app with sync lets ChatGPT securely access your team’s GitLab Issues projects and groups, issues and merge requests to answer questions. You can connect, disconnect, or update the connection at any time. Once enabled, ChatGPT will automatically reference content in GitLab Issues when relevant.  
  
  
**Type:** app with sync  
  
  
**Where you can use it:** Chat, deep research  
  
  
[**Learn more about connecting a new app**](/en/articles/11487775)

## Example prompts

* “Summarize open GitLab Issues labeled 'P1'”
* “Find merge requests awaiting my review in Project X”
* “Draft release notes from recent issue and MR activity”

[**Learn more about app use cases and prompts.**](/en/articles/12084614)

## Capabilities and permissions

## What it can access

* Projects and groups
* Issues and merge requests
* Comments/notes and timelines
* Labels, milestones, assignees

## Not indexed

* Large binary attachments (e.g., videos), embedded media, and unsupported file types
* Items outside your permission scope
* System-generated or ephemeral metadata not exposed via the API

## Permissions (scope)

* read\_api
* read\_user

## Known limitations

* Initial sync time depends on data volume (minutes to hours)
* API rate limits and provider throttling may delay syncs
* Permission or configuration changes are applied on the next sync cycle
* Some attachment binaries or non-text content may be excluded

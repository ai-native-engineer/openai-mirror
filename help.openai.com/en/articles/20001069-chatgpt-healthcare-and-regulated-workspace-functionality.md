<!-- source: https://help.openai.com/en/articles/20001069-chatgpt-healthcare-and-regulated-workspace-functionality -->

# ChatGPT Healthcare and Regulated Workspace functionality

Understanding the functionality available to HIPAA compliant workspaces.

Updated: 2 days ago

# Overview

ChatGPT for Healthcare and Regulated Workspaces are preconfigured ChatGPT Enterprise workspaces where certain features are turned off by default. These workspaces also make certain features safer for use with PHI.

# Functionality covered under BAA

ChatGPT for Healthcare and Regulated workspaces include the following functionality that support HIPAA compliance and are covered by the OpenAI Business Associate and Healthcare Addendum (the “BAA”):

* Admin features
* SSO
* Compliance API
* RBAC
* Chat with files
* Chat Sharing
* Voice (Speech to text/Advanced voice mode)
* Python Tool & File Download
* Web Search & Deep Research (*Offline web search only, using OpenAI"s internal search index*)
* Canvas & Canvas Code Execution
* ImageGen
* Memory
* Projects
* Notifications
* Apps / Connectors
* GPTs
* Desktop Clients: MacOS and Windows
* Mobile App
* Record
* Work with Apps
* Study Mode
* ChatGPT for Excel and Sheets
* Workspace Agents
* Trusted Clinical Search (*ChatGPT for Healthcare only*)
* Codex Local\* for data processed by OpenAI *(incl. use through CLI, IDE and Desktop App when signed in with a ChatGPT Enterprise account)*

\**Please contact your Account Director to enable Codex HIPAA support for your workspace.*

# Access to Functionality not covered under BAA

A customer may, in its sole discretion, enable access to additional ChatGPT functionality that is not covered under BAA. These additional features are disabled by default. Workplace administrators can enable access to these features through RBAC groups; [see this article](/en/articles/11750701) for more information on how to configure RBAC roles and groups. *This access is intended only for uses that do not involve transmission, storage, or processing of PHI*.

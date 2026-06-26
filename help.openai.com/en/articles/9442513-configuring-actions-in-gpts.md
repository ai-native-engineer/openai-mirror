<!-- source: https://help.openai.com/en/articles/9442513-configuring-actions-in-gpts -->

# Configuring actions in GPTs

How to connect your GPT to external APIs using actions, including setup, authentication, and schema configuration.

Updated: 10 days ago

# Overview

This article explains how to configure actions in a GPT, including how to connect to external APIs, define what the GPT can do, and manage authentication, schemas, and workspace restrictions.  
  
To configure an action, you’ll need the API details for the service you want to connect, including authentication information and an OpenAPI schema. A GPT can use either apps or actions, but not both at the same time.  
  
Each action is defined by two main components: how the GPT authenticates with the API, and a schema that defines what the API can do.

## Limitations

If your workspace allows zero action domains, GPT custom actions cannot execute because no action domain can pass allowlist checks. This does not necessarily mean all GPT visibility or access is blocked.  
  
Actions are not available for Pro mode. When you create or edit a GPT with custom actions, the model selector shows only non-Pro models that support actions.

# Create an action

In the GPT editor, navigate to the **Actions** section and select **Create new action**.  
  
You’ll then configure how your GPT connects to and uses an external API.  
  
After configuring an action, test it in **Preview** to confirm it behaves as expected.

# Authentication

Authentication controls how your GPT connects to an external API.  
  
Available options:

* **None:** No authentication required
* **API key:** Uses a secret key to authorize requests
* **OAuth:** Uses user sign-in for account-based access

## API key

Use API key authentication for server-to-server access. It can be configured as:

* **Basic**
* **Bearer**
* **Custom header**

## OAuth

Use OAuth when actions require user accounts. OAuth requires:

* **Client ID** and **Client Secret**
* **Authorization URL** and **Token URL**
* **Scope** and token exchange method

The editor provides a callback URL for completing the OAuth flow.

# Schema

The schema defines what your API can do. It tells ChatGPT:

* Which server to call
* What endpoints are available
* What parameters they accept
* How each action is identified (operation IDs)

The schema must be provided as an OpenAPI specification in JSON or YAML.

## Add a schema

You can add a schema in three ways:

* Paste it directly into the editor
* Import it from a URL
* Start from a built-in example:

  + Weather (JSON)
  + Pet Store (YAML)
  + Blank template

If the schema is valid, the editor shows detected actions. If it is invalid, validation errors are displayed.

# Workspace restrictions (Enterprise and Edu)

If you see the message:  
  
  
**“No domains are allowed by your workspace’s settings.”**  
  
This means actions are restricted by your workspace settings.

* Admins can allow all domains or restrict actions to approved domains.
* If no domains are allowed, you cannot use actions.

For workspace-level controls on actions and domain restrictions, see: [Managing GPT access in Enterprise and Edu workspaces](https://help.openai.com/articles/8555535).

# Privacy and user controls

* Each action can include a Privacy Policy URL.
* Public GPTs (link or GPT Store) with actions must include a valid privacy policy URL.
* Users may be asked to approve actions before they run.
* For OAuth actions, users can review and manage connected accounts.

# Additional help

For help writing or debugging actions, use the official [ActionsGPT](https://chatgpt.com/g/g-TYEliDU6A-actionsgpt).

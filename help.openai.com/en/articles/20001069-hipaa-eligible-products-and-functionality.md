<!-- source: https://help.openai.com/en/articles/20001069-hipaa-eligible-products-and-functionality -->

# HIPAA Eligible Products and Functionality

Understanding the HIPAA eligible OpenAI products and functionality.

Updated: 11 hours ago

This page provides an overview of OpenAI HIPAA eligible products and functionality. For details on the use and configuration of these products see the [HIPAA Guide](https://cdn.openai.com/osa/hipaa-guide.pdf) referenced in your BAA.

# HIPAA Eligible Products

OpenAI makes the following HIPAA eligible products available with a Business Associates Agreement (BAA):

* ChatGPT for Healthcare
* ChatGPT for Enterprise with Regulated Workspace
* ChatGPT FedRAMP
* ChatGPT for Clinicians
* API with Modified Retention
* API FedRAMP with Modified Retention

# ChatGPT functionality covered under BAA

HIPAA Eligible ChatGPT products  include the following functionality that support HIPAA compliance and are covered by the OpenAI Business Associate and Healthcare Addendum (the “BAA”):

* Admin features
* SSO
* Compliance API
* RBAC
* Chat with files
* Chat Sharing
* Voice (Speech to text/Advanced voice mode)
* Python Tool & File Download
* Web Search & Deep Research (See below for details)
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
* ChatGPT for Excel and Sheets
* ChatGPT for PowerPoint
* Workspace Agents
* Library
* Codex Local (See below for details)
* Study Mode (Available in ChatGPT for Edu only)
* Trusted Clinical Search (Available in ChatGPT for Healthcare only)

## Codex Local (Sign-in with ChatGPT)

Codex Local involves the installation of Codex Local Client on a local workstation. The HIPAA eligible local clients include CLI, IDE and Desktop App when signed in with a [HIPAA eligible](/en/articles/20001069-hipaa-eligible-products-and-functionality#hipaa-eligible-products) ChatGPT account. When the Codex Local Client transmits PHI to OpenAI for processing, OpenAI will protect the Customer PHI consistent with the BAA.

The OpenAI BAA does not apply to the execution of the Codex Local Client on Customer’s client machines or to any Third-Party Services accessed by the Codex Local Client due to Customer’s use or instructions. Customer is responsible for evaluating the Codex Local Client installation, its operating environment, and establishing a managed configuration that meets their requirements for use with PHI.

For more information on deploying Codex in your organization see the [Admin rollout guide](https://learn.chatgpt.com/docs/enterprise/admin-setup).

For Codex Local configuration options see [Managed Configuration](https://learn.chatgpt.com/docs/enterprise/managed-configuration) and the [Codex HIPAA Implementation Guide](https://developers.openai.com/codex/hipaa-configuration).

## Web Search & Deep Research

OpenAI configures HIPAA eligible ChatGPT workspaces to use OpenAI's search index. When users enable the Web Search or Deep Research tool or when the model retrieves information from the web, it uses information in OpenAI's index. OpenAI does not send queries to third-party search providers (e.g., Bing) when using a HIPAA eligible workspace.

## Access to ChatGPT Functionality not covered under BAA

A customer may, in its sole discretion, enable access to additional ChatGPT functionality that is not covered under BAA. These additional features are disabled by default. Workplace administrators can enable access to these features through RBAC groups; [see this article](/en/articles/11750701) for more information on how to configure RBAC roles and groups. This access is intended only for uses that do not involve transmission, storage, or processing of PHI.

# API Functionality covered under BAA

HIPAA eligibility for the OpenAI API is contingent on Customer’s account being provisioned with Modified Retention, unless otherwise specified by OpenAI. Once your org ID is provisioned with Modified Retention, the endpoints listed below can be used for processing PHI, even if data is retained, upon execution of the OpenAI BAA.

## HIPAA-Eligible Endpoints

/v1/chat/completions

/v1/responses

/v1/assistants

/v1/threads

/v1/threads/messages

/v1/threads/runs

/v1/vector\_stores

/v1/threads/runs/steps

 /v1/images/generations

/v1/images/edits

/v1/images/variations

/v1/embeddings

/v1/audio/transcriptions

/v1/audio/translations

/v1/audio/speech

/v1/files

/v1/fine\_tuning/jobs

/v1/batches

 /v1/moderations

/v1/completions

/v1/realtime

## Codex Local (API Key)

Use of Codex Local with a Customer-provided OpenAI API key for the OpenAI API Services will be covered by the BAA for data processed by OpenAI only if Customer has entered into a BAA with OpenAI that includes the API Services with Modified Retention as an Eligible Service. See the Codex Local ([Sign-In with ChatGPT](https://docs.google.com/document/d/1k3l1gTSm6mbP8tbpeovK-0lL4hCwwHpW5f5sddziJrc/edit?tab=t.0#heading=h.l5nlvcegwdzz)) section above for more information on BAA coverage and Customer Responsibilities.

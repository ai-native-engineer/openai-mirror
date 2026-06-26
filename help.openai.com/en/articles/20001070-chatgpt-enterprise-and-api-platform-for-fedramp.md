<!-- source: https://help.openai.com/en/articles/20001070-chatgpt-enterprise-and-api-platform-for-fedramp -->

# ChatGPT Enterprise and API Platform for FedRAMP

Learn about supported features and functionality for ChatGPT and the API with FedRAMP compliance.

Updated: 2 days ago

# Overview

ChatGPT and the API for FedRAMP are versions of ChatGPT Enterprise and the API platform that have achieved [Federal Risk and Authorization Management Program (FedRAMP) Moderate accreditation](https://www.fedramp.gov/marketplace/products/FR2533155773/) through the FedRAMP 20x program.

# Feature availability

ChatGPT and API for FedRAMP do not initially include all features available in the commercial platforms. Over time, our goal is to bring feature parity as close as possible to the commercial ChatGPT Enterprise and API platforms while maintaining FedRAMP compliance.  
  
The sections below list the features currently available.

## ChatGPT

### Core features

* Latest instant model
* [Code Interpreter & Data Analysis](https://help.openai.com/articles/9213685)
* [Company knowledge](https://help.openai.com/articles/12628342)
* [GPTs](https://help.openai.com/articles/8554407)
* Notifications for supported categories. Task and group chat notification settings are not available in FedRAMP workspaces.
* [Projects](https://help.openai.com/articles/10169521)
* Real-time [apps](https://help.openai.com/articles/11487775)

  + Synced apps are currently not supported
* Web search ([regular](https://help.openai.com/articles/10093903) and [offline](https://help.openai.com/articles/20001203))

### Advanced features

* Latest Thinking and Pro models

## API

***Note:*** *FedRAMP compliance requires that all API requests use the designated* **gov.api.openai.com** *endpoint for all supported methods and models.*

### Methods

The following API methods are currently available:

```
/v1/chat/completions  
/v1/completions  
/v1/conversations  
/v1/files  
/v1/moderations  
/v1/responses  
/v1/uploads
```

For more information about using these methods, see: [API reference documentation](https://developers.openai.com/api/reference/overview).

### Models

The latest model family is generally available to use in the FedRAMP API, including mini and nano variants if applicable. Model snapshots are also available as they are released.  
  
Legacy models are not available.

## Codex

FedRAMP customers can use local Codex with FedRAMP ChatGPT sign-in or FedRAMP API-key sign-in, and Codex local will respect FedRAMP boundaries any time that it is communicating with OpenAI.  
  
Please note that local downloadable products like the Codex app or CLI are outside of the FedRAMP boundary, and should be carefully reviewed by your Authorizing Official.  
  
Codex Cloud is not currently supported in FedRAMP workspaces.

### Codex with ChatGPT sign-in

To use local Codex with a FedRAMP workspace, do all of the following:

1. Sign in to local Codex with ChatGPT.
2. Select a FedRAMP workspace.
3. Use Codex v0.122.0 or later.

### Codex with API key sign-in

To use local Codex with a FedRAMP API organization, do all of the following:

1. Use an API key generated from a FedRAMP-enabled API organization.
2. Use Codex v0.122.0 or later.
3. Run this command in Terminal to configure Codex to use the FedRAMP API endpoint:

```
codex config set openai_base_url https://gov.api.openai.com/v1
```

### Available models in Codex

In local Codex, FedRAMP customers have access only to models available in FedRAMP environments.

# Privacy and security

ChatGPT and API FedRAMP are designed for strict FedRAMP compliance and are operated with additional access restrictions and feature controls compared to standard ChatGPT Enterprise environments. Key Enterprise privacy measures are still in place:

* No model training on customer data
* Identical retention policies to ChatGT Enterprise, including availability of the [Compliance API](/en/articles/9261474-compliance-api-for-enterprise-customers)

# FAQ

## How is ChatGPT FedRAMP different from ChatGPT Gov?

ChatGPT FedRAMP is a SaaS product that OpenAI owns and manages for the customer. It is a configuration of ChatGPT Enterprise with additional accredited compliance. [ChatGPT Gov](https://openai.com/global-affairs/introducing-chatgpt-gov/) is a containerized frontend application that customers install and manage in their own Microsoft Azure environment.

## Can I convert my existing ChatGPT Enterprise workspace to FedRAMP?

No. Existing ChatGPT Enterprise workspaces cannot be converted to FedRAMP.  
  
However, OpenAI can support a one-time migration of users to a newly provisioned FedRAMP workspace, including ChatGPT conversations and tenant-level SSO settings. Workspace settings will need to be configured again in the new environment. For assistance, contact your account team.

## Can I convert my existing API organization to FedRAMP?

Yes. Existing API organizations can be converted to FedRAMP.  
  
Once converted, customers must use the designated **gov.api.openai.com** endpoint.

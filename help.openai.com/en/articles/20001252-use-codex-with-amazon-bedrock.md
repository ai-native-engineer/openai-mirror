<!-- source: https://help.openai.com/en/articles/20001252-use-codex-with-amazon-bedrock -->

# Use Codex with Amazon Bedrock

Learn how Codex uses OpenAI models on Amazon Bedrock and which local workflows and features are supported.

Updated: 10 hours ago

Codex can be configured to use OpenAI models available through Amazon Bedrock.

In this configuration, Codex runs locally in the Codex CLI, Codex desktop app, or Codex IDE extension, while model requests are sent to Amazon Bedrock. Codex uses Bedrock-supported authentication, and customers manage access, governance, billing, quotas, Regions, and request handling through their AWS account and applicable Amazon Bedrock controls.

This article provides a general overview. For setup instructions, see **Configure Codex with Amazon Bedrock.**

## How it works

When Codex is configured to use Amazon Bedrock:

* Codex runs locally in the CLI, desktop app, or IDE extension.
* Amazon Bedrock is configured as the model provider.
* Authentication uses AWS credentials or another Bedrock-supported authentication method.
* Inference requests are processed through Amazon Bedrock.
* Amazon Bedrock provides an OpenAI-compatible Responses API implementation for supported OpenAI models.

The OpenAI-hosted Responses API is not in the request path.

## What is supported

This configuration supports local Codex workflows, including:

* Codex CLI local workflows
* Codex desktop app local workflows
* Codex IDE extension local workflows
* Bedrock-backed inference using supported OpenAI models
* AWS-managed access through IAM, model access controls, billing, quotas, Regions, and applicable Bedrock controls

## What is not currently available

Some Codex features that depend on OpenAI-hosted cloud services, hosted tools, or cloud-managed tool discovery are not currently available when using Amazon Bedrock.

The following features are not currently available in this configuration:

* Image generation
* Voice transcription for input
* Cloud plugin store
* Cloud configuration and policy management
* Codex cloud agents, including review, security, and web agents

Because MCP namespace tools and tool search are not currently available, MCP and tool discovery functionality may be limited in this configuration.

Feature availability may differ between Codex with ChatGPT sign-in, Codex with an OpenAI API key, and Codex with an Amazon Bedrock API key.

## Compatibility notes

Codex on Amazon Bedrock is designed to provide a Codex local development experience using OpenAI models available through Amazon Bedrock. It should not be assumed to have identical feature availability or behavior to Codex backed by OpenAI’s API Platform.

Feature support may vary by:

* Model
* AWS Region
* API surface
* AWS account configuration
* AWS release status

## Support boundaries

For Codex client setup, configuration, CLI behavior, desktop app behavior, IDE extension behavior, or local Codex product experience, contact OpenAI Support.

For AWS credentials, IAM permissions, Bedrock model access, quotas, billing, regional availability, Bedrock request failures, AWS backend logs, or Bedrock service behavior, contact your AWS administrator or AWS Support.

## Related documentation

* Configure Codex with Amazon Bedrock.
* [OpenAI Codex CLI documentation](https://developers.openai.com/codex/cli)
* [Amazon Bedrock documentation for OpenAI-compatible APIs](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-mantle.html)
* [AWS documentation for Bedrock authentication and model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-openai.html)

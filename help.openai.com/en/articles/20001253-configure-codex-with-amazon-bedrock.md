<!-- source: https://help.openai.com/en/articles/20001253-configure-codex-with-amazon-bedrock -->

# Configure Codex with Amazon Bedrock

Configure Codex with Amazon Bedrock, including supported models, AWS credentials, and local client settings.

Updated: 10 hours ago

Use this guide to configure Codex to use OpenAI models available through Amazon Bedrock.

In this configuration, Codex uses Amazon Bedrock credentials and sends model requests through Bedrock’s implementation of the Responses API. The OpenAI-hosted API is not in the request path.

This setup supports local Codex workflows in:

* Codex CLI
* Codex desktop app
* Codex VS Code extension

This article does not apply to Codex configured with ChatGPT sign-in or an OpenAI API key.

## Before you start

Make sure you have:

* Codex CLI version 0.128.0 or later
* Codex desktop app or VS Code extension version 26.429.30905 or later
* Access to supported OpenAI models in Amazon Bedrock
* An AWS Region where the selected model is available
* Bedrock-supported authentication configured for your AWS account

## Supported models

Use one of these exact model IDs:

`openai.gpt-5.6-sol`

`openai.gpt-5.6-terra`

`openai.gpt-5.6-luna`

`openai.gpt-5.5`

`openai.gpt-5.4`

Recommended default:

`openai.gpt-5.6-sol`

## Configure Codex

Add the following to:

`~/.codex/config.toml`

`model = "openai.gpt-5.6-sol"`

`model_provider = "amazon-bedrock"`

`[model_providers.amazon-bedrock.aws]`

`region = "us-west-2"`

`wire_api = "responses"`

`# Optional for AWS SDK auth. If omitted, the AWS SDK uses AWS_PROFILE or the default profile.`

`# profile = "codex-bedrock"`

Replace `us-west-2` with the AWS Region where your selected model is available.

## Authentication options

Codex supports two Amazon Bedrock authentication paths:

1. Bedrock API key using `AWS_BEARER_TOKEN_BEDROCK`
2. AWS SDK credential chain for IAM-signed requests

Codex checks authentication in this order:

1. `AWS_BEARER_TOKEN_BEDROCK`
2. AWS SDK credential chain

If `AWS_BEARER_TOKEN_BEDROCK` is set, Codex uses it first. Otherwise, Codex falls back to the AWS SDK credential chain.

Do not use `OPENAI_API_KEY` for this configuration. Codex uses Amazon Bedrock credentials when `model_provider` is set to `amazon-bedrock`.

Use a Bedrock API key if your AWS account supports Bedrock API keys. Use AWS SDK credentials if your organization manages Bedrock access through IAM, AWS SSO, named profiles, or federated identity.

## Option 1: Use a Bedrock API key

Set your Bedrock API key in the environment Codex will read:

`export AWS_BEARER_TOKEN_BEDROCK=<your-bedrock-api-key>`

Then make sure your Codex config includes a Bedrock Region:

`model = "openai.gpt-5.6-sol"`

`model_provider = "amazon-bedrock"`

`[model_providers.amazon-bedrock.aws]`

`wire_api = "responses"`

`region = "us-west-2"`

The Region is required when using Bedrock API-key authentication.

## Option 2: Use AWS SDK credentials

Use this path when you want Codex to authenticate with AWS IAM credentials.

Codex uses the AWS SDK credential chain, so standard AWS credential setups can work, including shared AWS config files, environment variables, AWS SSO, and named profiles.

### Shared AWS credentials

`aws configure`

### Environment variables

`export AWS_ACCESS_KEY_ID=<your-access-key-id>`

`export AWS_SECRET_ACCESS_KEY=<your-secret-access-key>`

`export AWS_SESSION_TOKEN=<your-session-token>`

### AWS Management Console credentials

`aws login`

### AWS SSO or named profile

`aws sso login --profile <profile-name>`

`export AWS_PROFILE=<profile-name>`

You can also set the profile directly in ~/.codex/config.toml:

`model = "openai.gpt-5.6-sol"`

`model_provider = "amazon-bedrock"`

`[model_providers.amazon-bedrock.aws]`

`profile = "codex-bedrock"`

`wire_api = "responses"`

`region = "us-west-2"`

Codex first uses `model_providers.amazon-bedrock.aws.region` when set. Otherwise, for SDK authentication, Codex delegates Region resolution to the AWS SDK default config chain, including `AWS_REGION`, `AWS_DEFAULT_REGION`, and the selected AWS profile.

* `~/.codex/config.toml`
* `AWS_REGION`
* `AWS_DEFAULT_REGION`
* The selected AWS profile

Setting the Region in ~/.codex/config.toml is the most explicit option.

## Federated identity with credential\_process

For corporate SSO or OIDC federation, configure the AWS profile outside Codex and let the AWS SDK resolve credentials.

Example `~/.aws/config` entry:

`[profile codex-bedrock]`

`region = us-west-2`

`credential_process = /path/to/your/idp-helper --profile codex-bedrock`

Then point Codex at that profile in ~/.codex/config.toml:

`model = "openai.gpt-5.6-sol"`

`model_provider = "amazon-bedrock"`

`[model_providers.amazon-bedrock.aws]`

`profile = "codex-bedrock" wire_api = "responses"`

`region = "us-west-2"`

## Desktop app and VS Code extension

Desktop apps and IDE extensions may not inherit environment variables from your shell.

If Codex needs environment variables such as AWS\_BEARER\_TOKEN\_BEDROCK, add them to:

`~/.codex/.env`

Example:

`AWS_BEARER_TOKEN_BEDROCK=<your-bedrock-api-key>`

`AWS_REGION=us-west-2`

After changing `~/.codex/config.toml` or `~/.codex/.env`, restart the Codex desktop app or VS Code extension.

## Verify setup

After configuration:

* In Codex CLI, open `/status` and confirm Codex is using the `amazon-bedrock` model provider.
* In the Codex desktop app or VS Code extension, start a new session after restarting the app.

## Known limitations

The following features are not currently available in this configuration:

* Image generation
* Voice transcription for input
* Cloud plugin store
* Cloud configuration and policies
* Cloud agents, including review, security, and web agents

Feature availability may differ between Codex with ChatGPT sign-in, Codex with an OpenAI API key, and Codex with an Amazon Bedrock API key.

## Troubleshooting

If setup fails, check the following:

* Your Codex version meets the minimum requirement.
* Your model ID exactly matches a supported model.
* Your AWS Region is set and the selected model is available in that Region.
* Your AWS credentials or Bedrock API key are valid and not expired.
* Your AWS identity has permission to access the selected Bedrock model.
* `AWS_BEARER_TOKEN_BEDROCK` is not set to an expired or unintended key.
* If using AWS SDK credentials, your selected AWS profile is valid.
* For desktop app or VS Code extension usage, required environment variables are present in `~/.codex/.env`.
* You restarted the app or extension after changing config or environment files.

For AWS credentials, IAM permissions, Bedrock model access, quotas, billing, regional availability, or Bedrock service errors, contact your AWS administrator or AWS Support.

OpenAI Support can help with Codex client setup, configuration, and local Codex behavior.

<!-- source: https://help.openai.com/en/articles/20001254-responses-api-support-on-amazon-bedrock -->

# Responses API support on Amazon Bedrock

Learn how AWS operates an OpenAI-compatible Responses API implementation for supported OpenAI models on Amazon Bedrock.

Updated: 1 hour ago

Amazon Bedrock provides an OpenAI-compatible implementation of the Responses API for supported OpenAI models. This implementation is provided and operated by AWS, and is separate from OpenAI’s hosted Responses API.

The goal is compatibility with the OpenAI Responses API, but feature availability, behavior, model support, and release timing may differ. Availability can vary by model, AWS Region, account configuration, and AWS release status.

## How it works

Requests are sent to Amazon Bedrock and authenticated using Bedrock-supported authentication methods. The OpenAI-hosted Responses API is not in the request path.

Customers manage access through their AWS account, including IAM permissions, model access, quotas, billing, regional availability, and applicable Bedrock controls.

## Supported capabilities

A subset of Response API capabilities are supported through Amazon Bedrock. See the [Responses API feature availability](https://developers.openai.com/api/docs/guides/amazon-bedrock#responses-api-feature-availability) article for a detailed table on current feature availability.

## Troubleshooting

If a request fails, first confirm:

* The selected OpenAI model is available in the AWS Region being used
* The AWS account has access to the model in Amazon Bedrock
* The AWS identity has the required IAM permissions
* Quotas and rate limits are sufficient for the request
* The request uses a capability currently supported by Amazon Bedrock
* The request is being sent to the Amazon Bedrock endpoint, not the OpenAI-hosted API endpoint

## Support

For issues related to AWS authentication, IAM permissions, Bedrock model access, quotas, billing, regional availability, Bedrock request failures, AWS backend logs, or Bedrock service behavior, contact AWS Support.

For information about OpenAI’s hosted Responses API, see OpenAI’s API documentation. OpenAI’s hosted API documentation describes OpenAI Platform behavior and may include capabilities that are not available in the Amazon Bedrock implementation.

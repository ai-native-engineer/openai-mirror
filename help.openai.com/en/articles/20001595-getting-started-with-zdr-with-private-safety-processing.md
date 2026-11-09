<!-- source: https://help.openai.com/en/articles/20001595-getting-started-with-zdr-with-private-safety-processing -->

# Getting started with ZDR with Private Safety Processing

Set up ZDR with PSP, validate your storage, and resolve onboarding issues.

Updated: 10 days ago

Zero Data Retention with Private Safety Processing (ZDR with PSP) enables offline, automated safety review without OpenAI retaining customer prompts or responses. Read the [PSP developer guide](https://developers.openai.com/api/docs/guides/private-safety-processing) to learn how PSP protects your data and what setup requires, and [API data controls](https://developers.openai.com/api/docs/guides/your-data) for eligibility and endpoint limitations.

# Start setup

Ask an organization administrator to follow the setup and verification instructions for your storage provider. The guide covers cloud configuration, storage registration, and validation for the intended OpenAI project.

[Open the PSP setup guide](https://developers.openai.com/api/docs/guides/private-safety-processing#set-up-and-verify-customer-storage)

# Check your setup

Confirm that your project shows **Validated** for the storage connection and **Zero Data Retention with Private Safety Processing** as its retention policy. Storage registration alone does not finish setup.

If setup or validation fails, check the selected organization and project, review the reported error, and follow the guide’s troubleshooting instructions.

[Open PSP troubleshooting](https://developers.openai.com/api/docs/guides/private-safety-processing#check-storage-status)

# Get onboarding help

If an OpenAI account team is helping you onboard, contact that team. Otherwise you can [contact support](https://help.openai.com/articles/6614161) for additional assistance.

To help us troubleshoot, include:

* Your account email and OpenAI organization and project IDs.
* Your storage provider and region, the setup step that failed, and the error or status shown.
* The time of the failure, including time zone, and a request ID if available.

Do not include API keys, cloud credentials, prompts, responses, or decrypted customer records. Remove sensitive information from screenshots and error details before sharing.

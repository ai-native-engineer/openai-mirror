<!-- source: https://help.openai.com/en/articles/20000957-ekm-kms-key-lifecycle -->

# EKM KMS key lifecycle

End-to-end KMS key lifecycle guidance, from setup checks to post-revocation cleanup

Updated: 3 days ago

# Prerequisites

This assumes you have already registered your external KMS key with OpenAI, following one of these guides

* [OpenAI / AWS EKM Integration Instructions](/en/articles/20000947)
* [OpenAI / GCP EKM Integration Instructions](/en/articles/20000949)
* [OpenAI / Azure EKM Integration Instructions](/en/articles/20000951)

# Key Terms

Key **rotation** and key **revocation** serve different purposes. Make sure to choose the correct action for your use case.

* **Key Rotation**: Generate new cryptographic material for encryption of new data, while allowing decryption of older data encrypted with previous keys

  + **Key Rotation** does not affect access to OpenAI data
* **Key Revocation**: Revoke access to all data encrypted with previous keys.

  + **Key Revocation** revokes access to OpenAI data

# How to verify that your KMS key is being used

Your cloud provider should have logs:

* AWS - <https://docs.aws.amazon.com/kms/latest/developerguide/security-logging-monitoring.html>
* GCP - <https://cloud.google.com/kms/docs/audit-logging>
* Azure - <https://learn.microsoft.com/en-us/azure/key-vault/general/howto-logging>

# How to rotate your key

You can set up automatic key rotation

* AWS - <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>
* GCP - <https://cloud.google.com/kms/docs/rotate-key#automatic>
* Azure - <https://learn.microsoft.com/en-us/azure/key-vault/keys/how-to-configure-key-rotation>

To test: your access to OpenAI data will be unaffected by this change

# How to revoke your key

There are many ways to revoke OpenAI's access to your key - any disruption in the auth flow:

* If you revoke access from OpenAI's role to the KMS key
* If you remove the encrypt/decrypt permissions on the KMS key
* If you are using an AWS key alias (not recommended), if you switch the underlying KMS ARN. This action is sometimes confused with key rotation but is really a key revocation, so it is not recommended unless you are sure you want this.
* If you request for OpenAI to update the KMS ARN used for your ChatGPT Enterprise workspace

To validate your key revocation:

* **Wait one hour** for all cache entries to expire on OpenAI's end, then test revocation

  + If you are using **ChatGPT Enterprise**, you will no longer be able to read previous conversations, conversation search will not show results from previous conversations, and you will not be able to access previous custom GPTs.
  + If you are using the **API**, you will no longer be able to download previous batch files, use previous fine-tuned models, or reference previous responses created using the Responses API.
* If you are using the **API**, you can also test immediately that your key revocation has been processed by OpenAI and will take effect within one hour

  + Create an **Admin API key** (not a normal API key):
  + Get the OpenAI external key id (**extkey\_xxx**) associated with your workspace or project by calling curl -X GET -H "Authorization: Bearer $ADMIN\_API\_KEY" <https://api.openai.com/v1/organization/external_keys>
  + Now call curl -X POST -H "Authorization: Bearer $ADMIN\_API\_KEY" "https://api.openai.com/v1/organization/external\_keys/**extkey\_xxx**/validate"

## Best practices with key revocation

If you are using the API

* **Archive the API project whose data you have made inaccessible**. Then, set up a new KMS key, and create a new API project associated with the new KMS key.
* **Note that you cannot swap the KMS key associated with the old API project where you have executed the key revocation** - you must archive the old project. A project where a key revocation has been issued should not stay in use. The API makes it very easy to create new projects, so use that feature.

If you are using ChatGPT Enterprise

* Reach out to OpenAI support after you have executed a key revocation.
* We will work with you to spin up a **new workspace**. We will not reuse the old workspace by trying to update it to use a new KMS key. This is because when key revocation works as designed, previous data encrypted with the revoked key becomes inaccessible.

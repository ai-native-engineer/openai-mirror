<!-- source: https://help.openai.com/en/articles/20000947-openai-aws-ekm-integration-instructions -->

# OpenAI / AWS EKM Integration Instructions

Step-by-step instructions to provision AWS and activate EKM

Updated: 3 days ago

# Overview

Enterprise Key Management (EKM) allows OpenAI to encrypt data using a master key that you control. This document shows how to set up your AWS account to give OpenAI limited permissions on your KMS.

![AWS EKM integration flow between OpenAI EKM Service, your STS, your KMS, and your master KEK](https://images.ctfassets.net/j22is2dtoxu1/42QMP7ByOzgg2A9OcUm5uk/7393cda12397a475092ebf9e9f899d2d/Screenshot_2025-10-13_at_11.15.44â__AM.png)

# Steps

## 1. Create a **new KMS key**

1. Go to **KMS -> Customer managed keys**, then click **Create Key**.
2. Select a symmetric encryption algorithm.
3. After your key is created, note its **ARN**. Supported formats include `arn:aws:kms:<region>:<account_number>:key/<uuid>`, `...:key/mrk-*`, or `...:alias/<alias_name>`.

![AWS KMS customer managed key details page with key ID and ARN for test-kms](https://images.ctfassets.net/j22is2dtoxu1/eYNfROzIA48sxQq6MzhSs/8e6b635deebcf75d7f28a3cfd5c06aa9/Screenshot_2025-10-13_at_11.19.04â__AM.png)

## 2. Create a **custom policy** for limited access to the KMS key

1. Go to **IAM -> Policies**, then click Create Policy.
2. In the **Specify permissions** step, select **JSON** and enter the following to give the policy KMS access actions. Make sure you replace **YOUR\_KMS\_ARN** with the ARN of the Key you created.

![AWS IAM Create policy page with Specify permissions open and the JSON policy editor selected](https://images.ctfassets.net/j22is2dtoxu1/6TE2cPS6r3Vgtf9b11qUlI/607fc45b3d8ff8627869004ae3f6400d/Screenshot_2025-10-13_at_11.21.44â__AM.png)

```
{  
    "Version": "2012-10-17",  
    "Statement": [  
        {  
            "Sid": "AllowEncryptDecrypt",  
            "Effect": "Allow",  
            "Action": [  
  
                "kms:Decrypt",  
                "kms:Encrypt"  
  
            ],  
            "Resource": <YOUR_KMS_ARN>  
        }  
    ]  
}
```

## 3. Create an **IAM Role** for OpenAI to assume, and assign it to the policy with limited access to your KMS

OpenAI will call `AssumeRole` from an OpenAI-owned AWS account. This step lets OpenAI's AWS principal assume the limited role for accessing your KMS.

1. Go to **IAM -> Roles**, then click **Create Role**.
2. In the **Select trusted entity** step, select **Custom trust policy**.

![AWS IAM Select trusted entity screen with Custom trust policy selected](https://images.ctfassets.net/j22is2dtoxu1/CQJFADOrECGXJ06X8Krb4/2675e81e73bc274fe676f7e4db98c2fb/Screenshot_2025-10-13_at_11.23.36â__AM.png)

Next, enter the following in the **Custom trust policy** to allow access to OpenAI's AWS principal.

* The principal is OpenAI's AWS principal: `arn:aws:iam::790389265272:role/EnterpriseKeyManagement`.
* Indicate which **ExternalId** OpenAI should pass during the `AssumeRole` process.

  + For ChatGPT or API, use the **organization ID (org-xxx)** associated with your workspace: <https://platform.api.openai.org/settings/organization/general>.
  + For API, you can use a specific **API project ID** for more granularity.

```
{  
    "Version": "2012-10-17",  
    "Statement": [  
        {  
            "Effect": "Allow",  
            "Principal": {  
                "AWS": "arn:aws:iam::790389265272:role/EnterpriseKeyManagement"  
            },  
            "Action": "sts:AssumeRole",  
            "Condition": {  
                "StringEquals": {  
                    "sts:ExternalId": [  
                         <YOUR_OPENAI_ORGANIZATION_ID>,  
                     ]  
                }  
            }  
        }  
    ]  
}
```

Then, in the **Add permissions** step, search for the policy name of the IAM policy you created in the previous step. Click the **checkbox** next to the policy name, then click **Next**.

![AWS IAM Add permissions page filtered to customer managed KMS policies with test-allow-kms-access selected](https://images.ctfassets.net/j22is2dtoxu1/Q4AktT8thE6fSQloDkA5L/1320696eb04aa2ab283c02cd48429052/Screenshot_2025-10-13_at_11.29.43â__AM.png)

Finally, in the **Name, review, and create** section, select any role name.

## 4. Apply any additional restrictions in line with your own security practices

Above is the *minimum required information* OpenAI needs to set up EKM. You are free to apply additional key policies or restrictions in line with your own internal security practices, as long as OpenAI is able to call encrypt and decrypt operations on your KMS. When you call the key registration endpoint with OpenAI that's described below, we will validate your setup.

# After completing the above steps

## ChatGPT Enterprise

Please reach out to your OpenAI contact and share the following:

* `"role_arn": "arn:aws:iam::<YOUR_AWS_ACCOUNT_NUMBER>:role/<YOUR_ROLE>"`

  + The Role ARN that OpenAI will assume in your cloud.
* `"kms_arn": "arn:aws:kms:<REGION>:<YOUR_AWS_ACCOUNT_NUMBER>:key/<UUID>"`

  + The Key Management System ARN for the master key you manage.

We will enable EKM for your ChatGPT organization/workspace.

## API

## Register your external key with OpenAI

Follow the instructions in this API reference: [External Keys in the Management API](/en/articles/20000953).

1. First, register your external key at the OpenAI organization level, which will generate an external key ID.
2. In this step, we will validate that your input is valid and that we can authenticate to your KMS.
3. This won't add EKM to your OpenAI project yet.

```
curl -X POST \  
-H "Content-type: application/json" \  
-H "Authorization: Bearer $TOKEN" \  
  
"https://api.openai.com/v1/organization/external_keys" \  
-d '{  
  "type": "aws",  
  "name": "AWS EKM Config",  
  "role_arn": "arn:aws:iam::<YOUR_AWS_ACCOUNT_NUMBER>:role/<YOUR_ROLE>",  
  "kms_arn": "arn:aws:kms:<REGION>:<YOUR_AWS_ACCOUNT_NUMBER>:key/<UUID>",  
  "external_id": <your org id or project id>  
}'
```

Then, create an OpenAI project associated with the external key. After this, EKM is activated on your project. The response body of this API call will give you the project ID **(proj\_xxx)**.

```
curl -X POST \  
-H "Content-type: application/json" \  
-H "Authorization: Bearer $TOKEN" \  
"https://api.openai.com/v1/organization/projects" \  
-d '{  
   "name": "Some Project",  
  
   "external_key_id": "extkey_xxxx"  
}'
```

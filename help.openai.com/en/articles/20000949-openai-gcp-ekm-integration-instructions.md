<!-- source: https://help.openai.com/en/articles/20000949-openai-gcp-ekm-integration-instructions -->

# OpenAI / GCP EKM Integration Instructions

Step-by-step instructions to provision GCP and activate EKM

Updated: 3 days ago

# Overview

Enterprise Key Management (EKM) allows OpenAI to encrypt data using a master key that you control. This document shows how to set up your GCP account to give OpenAI limited permissions on your KMS.

![Diagram of OpenAI GCP EKM integration flow using STS token exchange and KMS encrypt or decrypt requests](https://images.ctfassets.net/j22is2dtoxu1/3vn2AFbQkTHhInTd1EyHlR/1d15277f1f2ad69917331bc4975c8cb7/Screenshot_2025-10-15_at_4.19.43â__PM.png)

# Steps

## 1. Create a federated identity for OpenAI

OpenAI will be issuing an identity token from an OpenAI-owned GCP account that looks something like this.

* The azp and sub are OpenAI's service account ID in GCP
* The aud is your OpenAI organization ID. You can also pick another audience such as your OpenAI project ID - see the instructions below

```
{  
  "aud": "org-xxxx",  
  "azp": "105900137572174660365",  
  "exp": 1747876928,  
  "iat": 1747873328,  
  "iss": "https://accounts.google.com",  
  "sub": "105900137572174660365"  
}
```

This step recognizes the claims made by that identity token and enables your GCP STS to issue an access token when that identity token is supplied.

1. Go to **IAM & Admin -> Workload Identity Federation** and click on **Create Pool**

![GCP IAM & Admin with Workload Identity Federation selected](https://images.ctfassets.net/j22is2dtoxu1/kEspFsoaYgFNxfpeZJAqu/3d9aefa162fedf7f714bfbe74985b8ff/Screenshot_2025-10-15_at_4.22.48â__PM.png)

1. In the step **Create an identity pool,** enter anything for the **pool name.**

1. In the step **Add a provider to pool**:

1. In Select a provider, select **OpenID Connect (OIDC)**
2. Enter anything for the **provider name**.
3. In the **Issuer (URL)** section, enter **https://accounts.google.com**
4. In the **Audiences** section

1. Select **Allowed audiences**
2. Enter the audience that OpenAI should indicate when we pass you a token.

1. For ChatGPT or API: You can put the **OpenAI API organization ID** (**org-xxx**)
2. For API: you can put a specific **API project id** for more granularity.

![GCP Workload Identity Provider edit page with Allowed audiences selected and Audience 1 entered](https://images.ctfassets.net/j22is2dtoxu1/4E69gyKsUYU79lWgefX0lh/a9c65e4af13f8deef3f8518f53e38f66/Screenshot_2025-10-15_at_4.29.20â__PM.png)

1. In the **Attribute mapping** section

1. for **google.subject** enter **assertion.sub**

![Google Cloud attribute mapping with Google 1 google.subject mapped to OIDC 1 assertion.sub](https://images.ctfassets.net/j22is2dtoxu1/3Q9rXTV0SK33ZbqwRzI04f/8d67a8f9882d4ff37c1c9ee07e3a9f22/Screenshot_2025-10-15_at_4.30.57â__PM.png)

1. In the **Attribute conditions** section

1. Now you should see your **workload identity pool** and **workload identity provider** listed in the <https://console.cloud.google.com/iam-admin/workload-identity-pools> page

1. **Workload identity pool id**

![GCP Workload Identity Pools page highlighting the provider ID value needed for OpenAI EKM setup](https://images.ctfassets.net/j22is2dtoxu1/1XD2dMRWpkp6B2OPh5lY6S/fb73bfb9068f6871ebd02cdbd1719241/Screenshot_2025-10-15_at_4.32.40â__PM.png)

1. **Workload identity provider ID**

![GCP Workload Identity Provider edit page with the provider ID field highlighted](https://images.ctfassets.net/j22is2dtoxu1/78J8kqO2nDMdG60aBxsZv4/006c4db4450953cef6225f16195b3d64/Screenshot_2025-10-15_at_4.33.34â__PM.png)

## 2. Ensure KMS is enabled

Go to <https://console.developers.google.com/apis/api/cloudkms.googleapis.com/overview> to enable KMS. You are not required to create your KMS in the same GCP project where you recognized OpenAI's federated identity; however, if the projects differ, the KMS product must at least be *enabled* in both projects.

## 3. Create a new KMS Key

1. Go to **Security -> Data Protection > Key Management**
2. Under the **Overview** tab click on **Create key ring**

1. Choose any name for your key ring
2. For Purpose and algorithm, select **Symmetric encrypt/decrypt**

![GCP Key Management Overview page with the Create Key Ring button highlighted](https://images.ctfassets.net/j22is2dtoxu1/5Yao654DYTPw1AHvZWm1mZ/3db09388e9c68852d7cd57ff8e63eafe/Screenshot_2025-10-15_at_4.36.15â__PM.png)

1. Once you’ve created a key ring, it should be listed in the **Key Rings** tab. Click on the key ring.
2. In the key ring details, click on **Create Key**

1. Choose any name for your key

## 4. Create a limited role for encrypt/decrypt operations on the KMS

1. Go to IAM & Admin -> Roles -> Create role
2. Enter anything for the role title and ID
3. Click Add Permissions, then add the following

1. **cloudkms.cryptoKeyVersions.useToDecrypt**
2. **cloudkms.cryptoKeyVersions.useToEncrypt**

## 5. Assign OpenAI’s federated identity to the limited KMS role for encrypt/decrypt operations

1. Go to **Security -> Data Protection > Key Management**
2. Click on your **key ring** name, then click on your **key name** to get to your key details page.

1. Click on the **Permissions** tab, then click the button **Grant Access**

![Google Cloud KMS key details page with Permissions tab open and Grant Access highlighted](https://images.ctfassets.net/j22is2dtoxu1/7fDg1nMyPBIL4oRhhmgQJp/525dfe9da133e2e419800b4b2a24de4e/Screenshot_2025-10-15_at_4.39.33â__PM.png)

1. Assign the OpenAI federated identity to the custom role you previously created

1. For the **Add principals** section, enter principal://iam.googleapis.com/projects/**<YOUR\_GCP\_PROJECT\_NUMBER>**/locations/global/workloadIdentityPools/**<YOUR\_GCP\_WORKLOAD\_IDENTITY\_POOL>**/subject/**105900137572174660365**

1. In the **Assign roles** section, select the custom role you created in the previous step for limited EKM permissions

## 6. Apply any additional restrictions in line with your own security practices

Above is the *minimum required information* OpenAI needs to set up EKM. You are free to apply additional key policies or restrictions in line with your own internal security practices, as long as OpenAI is able to call encrypt and decrypt operations on your KMS. When you call the key registration endpoint with OpenAI that's described below, we will validate your setup.

# After completing the above steps

## ChatGPT Enterprise

Please reach out to your OpenAI contact and share the following:

* "workload\_identity\_project\_number": "123456789012",

* "workload\_identity\_pool\_id": "openai-azure",

* "workload\_identity\_provider\_id": "openai-ekm-service-role",

* "kms\_project\_id": "adjective-noun-12345",

* "kms\_key\_name": "openai-kms-key",

* "kms\_key\_ring\_name": "openai-kms-key-ring",

* "kms\_key\_location": "us-east1"

* The region where your Key Management System master key is located

We will enable EKM for your ChatGPT organization/workspace.

## API

## Register your external key with OpenAI

Follow the instructions in this API reference [External Keys in the Management API](/en/articles/20000953)

* First, register your external key **at the OpenAI organization level,** which will generate an external key id.
* In this step, we will validate your setup on GCP by checking that we can auth to your KMS.
* This won't add EKM to your OpenAI project yet.

```
curl -X POST \  
-H "Content-type: application/json" \  
-H "Authorization: Bearer $TOKEN" \  
"https://api.openai.com/v1/organization/external_keys" \  
-d '{  
   "type": "gcp",  
   "name": "GCP EKM Config",  
   "workload_identity_project_number": "123456789012",  
   "workload_identity_pool_id": "openai-azure",  
   "workload_identity_provider_id": "openai-ekm-service-role",  
   "audience": <your org id or project id>,  
   "kms_project_id": "adjective-noun-12345",  
   "kms_key_name": "openai-kms-key",  
   "kms_key_ring_name": "openai-kms-key-ring",  
   "kms_key_location": "us-east1"  
}'
```

Then, create an OpenAI project associated with the external key. After this, EKM is activated on your project.

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

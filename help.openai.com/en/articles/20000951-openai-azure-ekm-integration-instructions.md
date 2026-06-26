<!-- source: https://help.openai.com/en/articles/20000951-openai-azure-ekm-integration-instructions -->

# OpenAI / Azure EKM Integration Instructions

Step-by-step instructions to provision Azure and activate EKM

Updated: 3 days ago

# Overview

Enterprise Key Management (EKM) allows OpenAI to encrypt data using a master key that you control. In order for OpenAI to call encrypt/decrypt operations on your Key Vault, we’ll need to be granted access. This document shows how to set up your Azure account so OpenAI can assume a role with Key Vault permissions.

![Azure EKM flow where OpenAI EKM uses Microsoft Entra ID to access your Key Vault and master KEK](https://images.ctfassets.net/j22is2dtoxu1/2Y1uRmMfU4RFYP17Y19DOO/65e7ca16e8b05629aa23bc1f0fbdbedb/Screenshot_2025-10-13_at_11.44.47â__AM.png)

# Steps

## 1. Create a service principal for OpenAI in your account

1. Get an access token

```
az account get-access-token --resource https://graph.microsoft.com  
--tenant YOUR_TENANT_ID
```

1. Create the service principal - the **appId** in the request below is OpenAI’s application client id. This will create a principal with the display name “**EKM - OpenAI Azure**” - remember this for later steps.

OpenAI / Azure EKM Integration Instructions - Create service principal

```
curl -X POST https://graph.microsoft.com/v1.0/servicePrincipals \  
-H "Authorization: Bearer $TOKEN_FROM_ABOVE" \  
-H "Content-Type: application/json" \  
–d '{"appId": "20a14814-5ab7-4612-a671-1382b412bf93"}'
```

## 2. Create a custom role for limited KMS access

1. Go to **Subscriptions -> Access Control (IAM)**
2. Under the **+ Add** dropdown, select **Add custom role**
3. Go to the **JSON** tab, click Edit, and add the following:

   1. Any role name - remember the name you selected
   2. The following permissions in **dataActions**:

      1. `Microsoft.KeyVault/vaults/keys/encrypt/action`
      2. `Microsoft.KeyVault/vaults/keys/decrypt/action`
      3. `Microsoft.KeyVault/vaults/keys/read`

![OpenAI / Azure EKM Integration Instructions Custom Role](https://images.ctfassets.net/j22is2dtoxu1/1hEkG4XEtxavIrFHfw337B/12af98657dbde768567a07255d9dbdb8/Screenshot_2025-10-13_at_11.49.25â__AM.png)

## 3. Create a Key Vault + Key

If you don't have one already, create a **new Key Vault** in the **same subscription** where you just created your custom role.  
  
In that Key Vault, create a new Key:

1. Go to **Key Vault -> Objects -> Keys**, then click on Generate/Import
2. Under Options select **Generate**

![Azure Key Vault Keys page with Generate/Import highlighted to add a key](https://images.ctfassets.net/j22is2dtoxu1/1P5aJCVVZd4keFkAxA9Aia/d7fa053ebd5fb5363d1cde6ac345c15b/Screenshot_2025-10-13_at_11.51.13â__AM.png)

1. Select **RSA** for encryption algorithm.
2. You can select any RSA key size
3. Provide a **key name** with the following format: `<org-xxx>--<any_name>` where `org-xxx` is your OpenAI organization ID that you can find at https://platform.openai.com/settings/organization/general

![Azure Key Vault key generation form with RSA selected and key name org-abcdefg--test-keyvault-key](https://images.ctfassets.net/j22is2dtoxu1/4WhTX8joU6AxveyGV7b1uv/ac07ec977793f99fbffb4e0b0137312e/Screenshot_2025-10-13_at_11.52.48â__AM.png)

If you are unable to view or create a key, make sure that you have the role **Key Vault Administrator**. This is needed even if you have the Owner role. To be assigned the role:

1. Go to **Key Vault -> Access Control (IAM)**
2. Click on **Add -> Add role assignment**

![Azure Key Vault Access control (IAM) page with Add menu open to Add role assignment](https://images.ctfassets.net/j22is2dtoxu1/19I33ernqpIWOnrwIAwZaj/231dd1bfb413bf0ccb99c4f469af42f7/Screenshot_2025-10-13_at_11.54.55â__AM.png)

## 4. Create a role assignment for OpenAI service principal + new custom KMS + new key

1. Go to **Key Vault -> Objects -> Keys** then click on the row for the key you created
2. Go to **Access control (IAM)** for your **key** you just clicked on (**not your key vault**).
3. Under the **+ Add** dropdown, select **Add role assignment**

![Azure Key Vault Access control (IAM) page with Add menu open to Add role assignment](https://images.ctfassets.net/j22is2dtoxu1/7qV1Uaw75QknRBfnL6Adn8/8bca7e0257fedeb862fb59eb197a0b06/Screenshot_2025-10-13_at_11.56.53â__AM.png)

1. In the **Role** tab, select the name of the custom role you just created.

![Azure role list filtered for openai- with the openai-azure-kms-role entry](https://images.ctfassets.net/j22is2dtoxu1/4eLA9mvXz8DmJRDFsd9oE5/1306b6b0da8469e67afab815b24fdb8a/Screenshot_2025-10-13_at_11.59.23â__AM.png)

1. In the **Members** tab:

   1. Click on “+ Select members”
   2. Type **“ekm -”** in the search bar, then the OpenAI service principal that you created in Step 1 should load

![Azure role assignment Members step with EKM - OpenAI Azure Application selected as a member](https://images.ctfassets.net/j22is2dtoxu1/usWcbmZVt8CsI2HsmymJU/1880100bbdf4299819118e6b594987bf/Screenshot_2025-10-13_at_12.00.59â__PM.png)

## 5. Apply any additional restrictions in line with your own security practices

Above is the minimum required information OpenAI needs to set up EKM. You are free to apply additional key policies or restrictions in line with your own internal security practices, as long as OpenAI is able to call encrypt and decrypt operations on your KMS. When you call the key registration endpoint with OpenAI that's described below, we will validate your setup.

# After completing the above steps

## ChatGPT Enterprise

Please reach out to your OpenAI contact and share the following:

* "tenant\_id": "<YOUR\_AZURE\_TENANT\_UUID>"

* "vault\_uri": "https://<YOUR\_KEYVAULT\_NAME>.vault.azure.net/"

* "key\_name": "<YOUR\_KEY\_NAME>"

* The name of the Azure Key Vault master key that you manage
* The key name must have the form <org-xxx>--<any\_name> where org-xxx is your OpenAI organization ID that you can find at https://platform.openai.com/settings/organization/general

We will enable EKM for your ChatGPT organization/workspace.

## API

## Register your external key with OpenAI

Follow the instructions in this API reference [External Keys in the Management API](/en/articles/20000953)

* First, register your external key at the OpenAI organization level, which will generate an external key id of the form **extkey\_xxx**
* In this step, we will validate that your input is valid and that we can authenticate to your KMS.
* This won't add EKM to your OpenAI project yet.

```
# This generates an external key ID of the form extkey_xxx  
curl -X POST \  
-H "Content-type: application/json" \  
-H "Authorization: Bearer $TOKEN" \  
"https://api.openai.com/v1/organization/external_keys" \  
-d '{  
  "type": "azure",  
  "name": "<ANY_FRIENDLY_NAME>",  
  "tenant_id": "<YOUR_AZURE_TENANT_UUID>",  
  "vault_uri": "https://<YOUR_KEYVAULT_NAME>.vault.azure.net/",  
  "key_name": "<YOUR_KEY_NAME>"  
}'
```

* Then, create an OpenAI project associated with the external key. After this, EKM is activated on your project.
* The response body of this API call will give you the project ID **(proj\_xxx)**

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

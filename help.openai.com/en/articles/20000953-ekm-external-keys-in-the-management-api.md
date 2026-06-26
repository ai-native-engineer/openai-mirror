<!-- source: https://help.openai.com/en/articles/20000953-ekm-external-keys-in-the-management-api -->

# EKM (External Keys) in the Management API

Manage external keys for EKM using the Management API

Updated: 2 days ago

# Summary

## Access

* EKM endpoints are accessible in the **Management API** via an **Admin API Key**. [**https://platform.openai.com/settings/organization/admin-keys**](https://platform.openai.com/settings/organization/admin-keys) (do not use a normal API key). Admin API keys are available to **organization owners**.
* Use `api.external_keys.write` to create or delete external keys, and `api.external_keys.read` to list or validate external keys. A single key needs both scopes only if it must perform both read and write operations.
* We currently need to feature flag your organization into these endpoints. You know you have the feature flag if you see **external\_key\_id** returned from the existing List Projects endpoint: <https://api.openai.com/v1/organization/projects>

## Usage

* Your EKM config is **registered** at the **organization** level via a new endpoint <https://api.openai.com/v1/organization/external_keys>
* Registering your EKM config returns an external\_key\_id in the form **extkey\_xxxx**
* EKM configs are **activated** at the **project** level by passing in an external\_key\_id in the body of the existing Create Project <https://api.openai.com/v1/organization/projects> endpoint

## Restrictions

* You must first test EKM on a **new project** via the Management API.
* **We recommend spinning up new projects for your EKM workloads.** However, if you want EKM on an existing project, we can add you to the feature flag. Please note the following best practices before you roll out EKM to your existing production projects.

  + Test all API features that you use in production in your test EKM API project first
  + Apply a gradual rollout instead of populating EKM on all production API projects at once

# Organization-level endpoints

## Register an external key on your organization

### AWS

#### Sample Request

* **type**: string -  always “aws”
* **name**: string -  A friendly name for your config
* **role\_arn**: string - The Role ARN that OpenAI will assume in your cloud
* **kms\_arn**: string - The Key Management System ARN for the master key you manage
* **external\_id**: string - Your organization id or API project id

```
curl -X POST \  
-H "Content-type: application/json" \  
-H "Authorization: Bearer $TOKEN" \  
"https://api.openai.com/v1/organization/external_keys" \  
-d '{  
  "type": "aws",  
  "name": "AWS EKM Config",  
  "role_arn": "arn:aws:iam::<12_DIGIT_ACCOUNT_NUMBER>:role/<ROLE>",  
  "kms_arn": "arn:aws:kms:<REGION>:<ACCOUNT_NUMBER>:key/<UUID>",  
  "external_id": <your org id or project id>  
}'
```

#### Sample Response

```
{  
  "id": "extkey_xxxx",  
  "object": "organization.external_key",  
  "created_at": 1746175499,  
  "api_project_ids": [],  
  "type": "aws",  
  "name": "AWS EKM Config",  
  "role_arn": "arn:aws:iam::<ACCOUNT_NUMBER>:role/<ROLE>",  
  "kms_arn": "arn:aws:kms:<REGION>:<ACCOUNT_NUMBER>:key/<UUID>",  
  "external_id": <your org id or project id>  
}  
```

### GCP

#### Sample Request

* **type**: string - always  "gcp",
* **name**: string - A friendly name for your config
* **workload\_identity\_project\_number**: string - The 12-digit GCP project number where you registered OpenAI's workload identity
* **workload\_identity\_pool\_id**: string - The pool containing the Workload Identity provider that you registered for OpenAI
* **workload\_identity\_provider\_id**: string - The Workload Identity provider that you registered for OpenAI
* **audience:** string - The audience that OpenAI should pass in the token when we assume a role through your GCP STS
* **kms\_project\_id:** string - The name of the GCP project where your KMS lives
* **kms\_key\_ring\_name**: string - The Key Management System key ring containing the master key you manage
* **kms\_key\_name**: string - The name of the Key Management System master key
* **kms\_key\_location**: string - The region where your Key Management System master key is located

If your KMS lives in a different GCP project from the one where you registered OpenAI's Workload Identity, make sure that the project containing OpenAI's Workload Identity at least has KMS enabled by going to <https://console.developers.google.com/apis/api/cloudkms.googleapis.com/overview>

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

#### Sample Response

```
{  
  "id": "extkey_xxxxxx",  
  "object": "organization.external_key",  
  "created_at": 1746174349,  
  "api_project_ids": [],  
  "type": "gcp",  
  "name": "GCP EKM Config",  
  "workload_identity_project_number": "123456789012",  
  "kms_key_ring_name": "openai-kms-key-ring",  
  "kms_key_name": "openai-kms-key",  
  "kms_key_location": "us-east1",  
  "audience": <your org id or project id>,  
  "kms_project_id": "adjective-noun-12345",  
  "workload_identity_pool_id": "openai-azure",  
  "workload_identity_provider_id": "openai-ekm-service-role"  
}
```

### Azure

#### Sample Request

* **type**: string - always  "azure",
* **name**: string - A friendly name for your config
* **tenant\_id**: string - Your Azure tenant UUID
* **vault\_uri**: string - The URI of the Azure vault containing the master key you manage
* **key\_name**: string - The name of the Azure Key Vault master key that you manage.

  + It must have the form **<org-xxx>--<any\_name>**
  + where **org-xxx** is your OpenAI organization ID that you can find at <https://platform.openai.com/settings/organization/general>

```
curl -X POST \  
-H "Content-type: application/json" \  
-H "Authorization: Bearer $TOKEN" \  
"https://api.openai.com/v1/organization/external_keys" \  
-d '{  
  "type": "azure",  
  "name": "Azure EKM Config",  
  "tenant_id": "<UUID>",  
  "vault_uri": "https://<VAULT_NAME>.vault.azure.net/",  
  "key_name": "org-xxx--some-key"  
}'
```

#### Sample Response

```
{  
  "id": "extkey_xxxx",  
  "object": "organization.external_key",  
  "created_at": 1746174377,  
  "api_project_ids": [],  
  "type": "azure",  
  "name": "Azure EKM Config",  
  "tenant_id": "<UUID>",  
  "vault_uri": "https://<VAULT_NAME>.vault.azure.net/",  
  "key_name": "org-xxx--some-key"  
}
```

## Delete an external key registered on your organization

**Note:** You can only delete an external key if it is not associated with any active API projects or workspace. If it is associated with an active API project, archive that project first. If it is associated with a workspace, the key cannot be deleted.

### Sample Request

```
curl -X DELETE \  
-H "Authorization: Bearer $TOKEN" \  
"https://api.openai.com/v1/organization/external_keys/extkey_xxxx"
```

### Sample Response

```
{  
  "id": "extkey_xxxxx",  
  "object": "organization.external_key.deleted",  
  "created_at": 1746127808,  
  "api_project_ids": [],  
  "type": "aws",  
  "account_number": "123456789012",  
  "kms_arn": "arn:aws:kms:<REGION>:<ACCOUNT_NUMBER>:key/<UUID>",  
  "name": "AWS EKM Config",  
  "role_arn": "arn:aws:iam::<ACCOUNT_NUMBER>:role/<ROLE>"  
}
```

## Get the external keys registered on your organization

### Sample Request

```
curl -X GET \  
-H "Authorization: Bearer $TOKEN" \  
"https://api.openai.com/v1/organization/external_keys"
```

### Sample Response

```
{  
  "object": "list",  
  "data": [  
    {  
      "id": "extkey_xxxx",  
      "object": "organization.external_key",  
      "created_at": 1746127808,  
      "api_project_ids": [],  
      "type": "aws",  
      "name": "AWS EKM Config",  
      "account_number": "123456789012",  
      "kms_arn": "arn:aws:kms:<REGION>:<ACCOUNT_NUMBER>:key/<UUID>",  
  	role_arn": "arn:aws:iam::<ACCOUNT_NUMBER>:role/<ROLE>"  
    }  
  ],  
  "first_id": "extkey_xxxx",  
  "has_more": false,  
  "last_id": "extkey_xxxx"  
}
```

## Validate an external key

You can use this endpoint to check several things

* Your external cloud configuration remains valid with OpenAI after you have made changes (you'll see a success response)
* Your key revocation is done correctly, is being processed by OpenAI, and will take effect after the 1 hour cache TTLs have expired (you'll see an error response)

### Sample Request

```
curl -X POST -H "Authorization: Bearer $TOKEN"  
"https://api.openai.com/v1/organization/external_keys/extkey_xxx/validate"
```

### Sample Response

```
{  
 "status": "success"  
}
```

Or, an error surfaced from the cloud provider.

# Project-level endpoints

## Create a new project with an external key ID

This is the same as the existing Create Project endpoint, with the addition of the **external\_key\_id** parameter in the request and response.

### Sample Request

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

### Sample Response

```
{  
  "object": "project",  
  "id": "proj_xxxxx",  
  "title": "Some Project",  
  "external_key_id": "extkey_xxxxx",  
  "created": 1740012721,  
  "organization_id": "org-xxxxx",  
  "is_initial": false,  
  "geography": null,  
  "scale_tier_enabled": false,  
  "disable_user_api_keys": false,  
  "zdr_type": null,  
}
```

## [Restricted] Update an existing project with an external key ID

This is the same as the existing Update Project endpoint, with the addition of the **external\_key\_id** parameter in the request and response.  
  
  
**We recommend spinning up new API projects for your EKM workloads.** If you want EKM on all your existing API projects, ask your account director and we will add you to the feature flag. Please note the following best practices before you roll out EKM to your existing production projects.

* Test all API features that you use in production in your test EKM API project first
* Apply a gradual rollout instead of populating EKM on all production API projects at once

### Sample Request

```
curl -X POST \  
-H "Content-type: application/json" \  
-H "Authorization: Bearer $TOKEN" \  
"https://api.openai.com/v1/organization/projects/proj_xxx" \  
-d '{  
   "external_key_id": "extkey_xxxx"  
}'
```

## List all the projects on your organization

This is the same as the existing endpoint but with the addition of **external\_key\_id** in the API response

### Sample Request

```
curl -X GET \  
-H "Authorization: Bearer $TOKEN" \  
"https://api.openai.com/v1/organization/projects"
```

### Sample Response

```
{  
  "object": "list",  
  "data": [  
    {  
      "object": "organization.project",  
      "id": "proj_xxxx",  
      "name": "Project Name",  
      "external_key_id": "extkey_xxxx",  
      "created_at": 1717798982,  
      "archived_at": null,  
      "status": "active"  
    }  
  ],  
  "first_id": "proj_xxxx",  
  "last_id": "proj_xxxx",  
  "has_more": true  
}
```

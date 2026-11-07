<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/external_keys/ -->

# External Keys

## Add an external key config for an organization

`admin.organization.external_keys.create(ExternalKeyCreateParams**kwargs)  -> ExternalKey`

**post** `/organization/external_keys`

Add an external key config for an organization

### Parameters

- `external_id: str`

  The ExternalID that OpenAI will pass in the AssumeRole call for the customer's AWS account. This must be the OpenAI organization ID or an API project ID that belongs to the organization.

- `kms_arn: str`

  The Key Management System ARN for the master key you manage

- `name: str`

  A friendly name to identify this config

- `role_arn: str`

  The Role ARN that OpenAI will assume to call your KMS

- `type: Literal["aws"]`

  - `"aws"`

- `purpose: Optional[Literal["ekm", "psp_decryption"]]`

  - `"ekm"`

  - `"psp_decryption"`

### Returns

- `class ExternalKey: …`

  - `id: str`

  - `api_project_ids: List[str]`

  - `created_at: int`

  - `name: str`

  - `object: str`

  - `type: str`

  - `workspace_id: str`

  - `audience: Optional[str]`

  - `external_id: Optional[str]`

  - `key_name: Optional[str]`

  - `key_version: Optional[str]`

  - `kms_arn: Optional[str]`

  - `kms_key_location: Optional[str]`

  - `kms_key_name: Optional[str]`

  - `kms_key_ring_name: Optional[str]`

  - `kms_key_version: Optional[str]`

  - `kms_project_id: Optional[str]`

  - `purpose: Optional[Literal["ekm", "psp_decryption"]]`

    - `"ekm"`

    - `"psp_decryption"`

  - `role_arn: Optional[str]`

  - `tenant_id: Optional[str]`

  - `vault_uri: Optional[str]`

  - `workload_identity_pool_id: Optional[str]`

  - `workload_identity_project_number: Optional[str]`

  - `workload_identity_provider_id: Optional[str]`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
external_key = client.admin.organization.external_keys.create(
    external_id="external_id",
    kms_arn="kms_arn",
    name="name",
    role_arn="arn:aws:iam::123456789012:role/example-role",
    type="aws",
)
print(external_key.id)
```

#### 200 — Example

```json
{
  "id": "id",
  "api_project_ids": [
    "string"
  ],
  "created_at": 0,
  "name": "name",
  "object": "object",
  "type": "type",
  "workspace_id": "workspace_id",
  "audience": "audience",
  "external_id": "external_id",
  "key_name": "key_name",
  "key_version": "key_version",
  "kms_arn": "kms_arn",
  "kms_key_location": "kms_key_location",
  "kms_key_name": "kms_key_name",
  "kms_key_ring_name": "kms_key_ring_name",
  "kms_key_version": "kms_key_version",
  "kms_project_id": "kms_project_id",
  "purpose": "ekm",
  "role_arn": "role_arn",
  "tenant_id": "tenant_id",
  "vault_uri": "vault_uri",
  "workload_identity_pool_id": "workload_identity_pool_id",
  "workload_identity_project_number": "workload_identity_project_number",
  "workload_identity_provider_id": "workload_identity_provider_id"
}
```

## Delete an external key config for the user's organization

`admin.organization.external_keys.delete(strexternal_key_id)  -> ExternalKey`

**delete** `/organization/external_keys/{external_key_id}`

Delete an external key config for the user's organization

### Parameters

- `external_key_id: str`

### Returns

- `class ExternalKey: …`

  - `id: str`

  - `api_project_ids: List[str]`

  - `created_at: int`

  - `name: str`

  - `object: str`

  - `type: str`

  - `workspace_id: str`

  - `audience: Optional[str]`

  - `external_id: Optional[str]`

  - `key_name: Optional[str]`

  - `key_version: Optional[str]`

  - `kms_arn: Optional[str]`

  - `kms_key_location: Optional[str]`

  - `kms_key_name: Optional[str]`

  - `kms_key_ring_name: Optional[str]`

  - `kms_key_version: Optional[str]`

  - `kms_project_id: Optional[str]`

  - `purpose: Optional[Literal["ekm", "psp_decryption"]]`

    - `"ekm"`

    - `"psp_decryption"`

  - `role_arn: Optional[str]`

  - `tenant_id: Optional[str]`

  - `vault_uri: Optional[str]`

  - `workload_identity_pool_id: Optional[str]`

  - `workload_identity_project_number: Optional[str]`

  - `workload_identity_provider_id: Optional[str]`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
external_key = client.admin.organization.external_keys.delete(
    "external_key_id",
)
print(external_key.id)
```

#### 200 — Example

```json
{
  "id": "id",
  "api_project_ids": [
    "string"
  ],
  "created_at": 0,
  "name": "name",
  "object": "object",
  "type": "type",
  "workspace_id": "workspace_id",
  "audience": "audience",
  "external_id": "external_id",
  "key_name": "key_name",
  "key_version": "key_version",
  "kms_arn": "kms_arn",
  "kms_key_location": "kms_key_location",
  "kms_key_name": "kms_key_name",
  "kms_key_ring_name": "kms_key_ring_name",
  "kms_key_version": "kms_key_version",
  "kms_project_id": "kms_project_id",
  "purpose": "ekm",
  "role_arn": "role_arn",
  "tenant_id": "tenant_id",
  "vault_uri": "vault_uri",
  "workload_identity_pool_id": "workload_identity_pool_id",
  "workload_identity_project_number": "workload_identity_project_number",
  "workload_identity_provider_id": "workload_identity_provider_id"
}
```

## List the external key configs registered on the user's organization

`admin.organization.external_keys.list(ExternalKeyListParams**kwargs)  -> SyncCursorPage[ExternalKey]`

**get** `/organization/external_keys`

List the external key configs registered on the user's organization

### Parameters

- `after: Optional[str]`

- `limit: Optional[int]`

  `minimum: 0`, `maximum: 100`

- `order: Optional[Literal["asc", "desc"]]`

  - `"asc"`

  - `"desc"`

- `purpose: Optional[Literal["ekm", "psp_decryption"]]`

  Filter by key purpose. When omitted, returns keys of all purposes.

  - `"ekm"`

  - `"psp_decryption"`

### Returns

- `class ExternalKey: …`

  - `id: str`

  - `api_project_ids: List[str]`

  - `created_at: int`

  - `name: str`

  - `object: str`

  - `type: str`

  - `workspace_id: str`

  - `audience: Optional[str]`

  - `external_id: Optional[str]`

  - `key_name: Optional[str]`

  - `key_version: Optional[str]`

  - `kms_arn: Optional[str]`

  - `kms_key_location: Optional[str]`

  - `kms_key_name: Optional[str]`

  - `kms_key_ring_name: Optional[str]`

  - `kms_key_version: Optional[str]`

  - `kms_project_id: Optional[str]`

  - `purpose: Optional[Literal["ekm", "psp_decryption"]]`

    - `"ekm"`

    - `"psp_decryption"`

  - `role_arn: Optional[str]`

  - `tenant_id: Optional[str]`

  - `vault_uri: Optional[str]`

  - `workload_identity_pool_id: Optional[str]`

  - `workload_identity_project_number: Optional[str]`

  - `workload_identity_provider_id: Optional[str]`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
page = client.admin.organization.external_keys.list()
page = page.data[0]
print(page.id)
```

#### 200 — Example

```json
{
  "data": [
    {
      "id": "id",
      "api_project_ids": [
        "string"
      ],
      "created_at": 0,
      "name": "name",
      "object": "object",
      "type": "type",
      "workspace_id": "workspace_id",
      "audience": "audience",
      "external_id": "external_id",
      "key_name": "key_name",
      "key_version": "key_version",
      "kms_arn": "kms_arn",
      "kms_key_location": "kms_key_location",
      "kms_key_name": "kms_key_name",
      "kms_key_ring_name": "kms_key_ring_name",
      "kms_key_version": "kms_key_version",
      "kms_project_id": "kms_project_id",
      "purpose": "ekm",
      "role_arn": "role_arn",
      "tenant_id": "tenant_id",
      "vault_uri": "vault_uri",
      "workload_identity_pool_id": "workload_identity_pool_id",
      "workload_identity_project_number": "workload_identity_project_number",
      "workload_identity_provider_id": "workload_identity_provider_id"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve an external key registration

`admin.organization.external_keys.retrieve(strexternal_key_id)  -> ExternalKey`

**get** `/organization/external_keys/{external_key_id}`

Retrieve a stored external key registration for the user's organization.

### Parameters

- `external_key_id: str`

### Returns

- `class ExternalKey: …`

  - `id: str`

  - `api_project_ids: List[str]`

  - `created_at: int`

  - `name: str`

  - `object: str`

  - `type: str`

  - `workspace_id: str`

  - `audience: Optional[str]`

  - `external_id: Optional[str]`

  - `key_name: Optional[str]`

  - `key_version: Optional[str]`

  - `kms_arn: Optional[str]`

  - `kms_key_location: Optional[str]`

  - `kms_key_name: Optional[str]`

  - `kms_key_ring_name: Optional[str]`

  - `kms_key_version: Optional[str]`

  - `kms_project_id: Optional[str]`

  - `purpose: Optional[Literal["ekm", "psp_decryption"]]`

    - `"ekm"`

    - `"psp_decryption"`

  - `role_arn: Optional[str]`

  - `tenant_id: Optional[str]`

  - `vault_uri: Optional[str]`

  - `workload_identity_pool_id: Optional[str]`

  - `workload_identity_project_number: Optional[str]`

  - `workload_identity_provider_id: Optional[str]`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
external_key = client.admin.organization.external_keys.retrieve(
    "external_key_id",
)
print(external_key.id)
```

#### 200 — Example

```json
{
  "id": "id",
  "api_project_ids": [
    "string"
  ],
  "created_at": 0,
  "name": "name",
  "object": "object",
  "type": "type",
  "workspace_id": "workspace_id",
  "audience": "audience",
  "external_id": "external_id",
  "key_name": "key_name",
  "key_version": "key_version",
  "kms_arn": "kms_arn",
  "kms_key_location": "kms_key_location",
  "kms_key_name": "kms_key_name",
  "kms_key_ring_name": "kms_key_ring_name",
  "kms_key_version": "kms_key_version",
  "kms_project_id": "kms_project_id",
  "purpose": "ekm",
  "role_arn": "role_arn",
  "tenant_id": "tenant_id",
  "vault_uri": "vault_uri",
  "workload_identity_pool_id": "workload_identity_pool_id",
  "workload_identity_project_number": "workload_identity_project_number",
  "workload_identity_provider_id": "workload_identity_provider_id"
}
```

## Validate an external key config for the user's organization

`admin.organization.external_keys.validate(strexternal_key_id)  -> ExternalKeyValidateResponse`

**post** `/organization/external_keys/{external_key_id}/validate`

Validate an external key config for the user's organization

### Parameters

- `external_key_id: str`

### Returns

- `class ExternalKeyValidateResponse: …`

  - `status: str`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
response = client.admin.organization.external_keys.validate(
    "external_key_id",
)
print(response.status)
```

#### 200 — Example

```json
{
  "status": "status"
}
```

## Domain Types

### External Key

- `class ExternalKey: …`

  - `id: str`

  - `api_project_ids: List[str]`

  - `created_at: int`

  - `name: str`

  - `object: str`

  - `type: str`

  - `workspace_id: str`

  - `audience: Optional[str]`

  - `external_id: Optional[str]`

  - `key_name: Optional[str]`

  - `key_version: Optional[str]`

  - `kms_arn: Optional[str]`

  - `kms_key_location: Optional[str]`

  - `kms_key_name: Optional[str]`

  - `kms_key_ring_name: Optional[str]`

  - `kms_key_version: Optional[str]`

  - `kms_project_id: Optional[str]`

  - `purpose: Optional[Literal["ekm", "psp_decryption"]]`

    - `"ekm"`

    - `"psp_decryption"`

  - `role_arn: Optional[str]`

  - `tenant_id: Optional[str]`

  - `vault_uri: Optional[str]`

  - `workload_identity_pool_id: Optional[str]`

  - `workload_identity_project_number: Optional[str]`

  - `workload_identity_provider_id: Optional[str]`

### External Key Validate Response

- `class ExternalKeyValidateResponse: …`

  - `status: str`

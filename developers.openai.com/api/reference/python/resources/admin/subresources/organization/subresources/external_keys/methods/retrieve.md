<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/external_keys/methods/retrieve/ -->

## Retrieve an external key registration

`admin.organization.external_keys.retrieve(strexternal_key_id)  -> ExternalKey`

**get** `/organization/external_keys/{external_key_id}`

Retrieve a stored external key registration for the user's organization.

- `external_key_id: str`

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

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
external_key = client.admin.organization.external_keys.retrieve(
    "external_key_id",
print(external_key.id)

  "api_project_ids": [
    "string"
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

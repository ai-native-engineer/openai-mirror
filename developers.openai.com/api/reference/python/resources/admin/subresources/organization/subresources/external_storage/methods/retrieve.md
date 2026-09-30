<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/external_storage/methods/retrieve/ -->

## Get an external storage configuration

`admin.organization.external_storage.retrieve(strexternal_storage_id)  -> ExternalStorageConfiguration`

**get** `/organization/external_storage/{external_storage_id}`

Get one customer-managed external storage configuration.

- `external_storage_id: str`

- `class ExternalStorageConfiguration: …`

  - `id: str`

  - `created_at: int`

  - `geography: str`

  - `object: Literal["organization.external_storage"]`

    - `"organization.external_storage"`

  - `project_id: str`

  - `provider: Provider`

    - `class AwsExternalStorageProvider: …`

      - `account_id: str`

      - `bucket: str`

      - `external_id: str`

      - `region: str`

      - `role_arn: str`

      - `type: Literal["aws"]`

        - `"aws"`

    - `class AzureExternalStorageProvider: …`

      - `account_name: str`

      - `container: str`

      - `region: str`

      - `resource_group: str`

      - `subscription_id: str`

      - `tenant_id: str`

      - `type: Literal["azure"]`

        - `"azure"`

    - `class GcpExternalStorageProvider: …`

      - `audience: str`

      - `bucket: str`

      - `region: str`

      - `type: Literal["gcp"]`

        - `"gcp"`

      - `workload_identity_pool_id: str`

      - `workload_identity_project_number: str`

      - `workload_identity_provider_id: str`

  - `status: Literal["pending", "validated", "unhealthy"]`

    - `"pending"`

    - `"validated"`

    - `"unhealthy"`

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
external_storage_configuration = client.admin.organization.external_storage.retrieve(
    "extstorage_123",
print(external_storage_configuration.id)

  "geography": "geography",
  "object": "organization.external_storage",
  "project_id": "project_id",
  "provider": {
    "account_id": "account_id",
    "bucket": "bucket",
    "external_id": "external_id",
    "region": "region",
    "role_arn": "role_arn",
    "type": "aws"
  "status": "pending"

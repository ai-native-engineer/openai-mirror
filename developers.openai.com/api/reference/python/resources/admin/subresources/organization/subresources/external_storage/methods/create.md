<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/external_storage/methods/create/ -->

## Create an external storage configuration

`admin.organization.external_storage.create(ExternalStorageCreateParams**kwargs)  -> ExternalStorageConfiguration`

**post** `/organization/external_storage`

Register one customer-managed external storage configuration.

- `project_id: str`

- `provider: Provider`

  - `class ProviderAws: …`

    - `bucket: str`

    - `role_arn: str`

    - `type: Literal["aws"]`

      - `"aws"`

  - `class ProviderAzure: …`

    - `account_name: str`

    - `container: str`

    - `resource_group: str`

    - `subscription_id: str`

    - `tenant_id: str`

    - `type: Literal["azure"]`

      - `"azure"`

  - `class ProviderGcp: …`

    - `bucket: str`

    - `type: Literal["gcp"]`

      - `"gcp"`

    - `workload_identity_pool_id: str`

    - `workload_identity_project_number: str`

    - `workload_identity_provider_id: str`

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
external_storage_configuration = client.admin.organization.external_storage.create(
    project_id="proj_123",
    provider={
        "bucket": "bucket",
        "role_arn": "role_arn",
        "type": "aws",
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

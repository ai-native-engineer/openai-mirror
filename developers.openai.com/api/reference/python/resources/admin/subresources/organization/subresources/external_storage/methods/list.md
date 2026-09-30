<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/external_storage/methods/list/ -->

## List external storage configurations

`admin.organization.external_storage.list(ExternalStorageListParams**kwargs)  -> SyncCursorPage[ExternalStorageConfiguration]`

**get** `/organization/external_storage`

List the organization's customer-managed external storage configurations.

- `after: Optional[str]`

  Return external storage configurations after this ID.

- `limit: Optional[int]`

- `order: Optional[Literal["asc", "desc"]]`

  - `"asc"`

  - `"desc"`

- `project_id: Optional[str]`

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
page = client.admin.organization.external_storage.list()
page = page.data[0]
print(page.id)

  "data": [
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
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/external_storage/ -->

# External Storage

## Create an external storage configuration

`admin.organization.external_storage.create(ExternalStorageCreateParams**kwargs)  -> ExternalStorageConfiguration`

**post** `/organization/external_storage`

Register one customer-managed external storage configuration.

### Parameters

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

### Returns

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

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
external_storage_configuration = client.admin.organization.external_storage.create(
    project_id="proj_123",
    provider={
        "bucket": "bucket",
        "role_arn": "role_arn",
        "type": "aws",
    },
)
print(external_storage_configuration.id)
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
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
  },
  "status": "pending"
}
```

## Delete an external storage configuration

`admin.organization.external_storage.delete(strexternal_storage_id)  -> ExternalStorageDeleted`

**delete** `/organization/external_storage/{external_storage_id}`

Disconnect a customer-managed external storage configuration. Removing the project's last configuration restores organization-default retention if customer-managed retention was active. Repeating a deletion also completes any interrupted retention update. Cloud storage is unchanged.

### Parameters

- `external_storage_id: str`

### Returns

- `class ExternalStorageDeleted: …`

  - `id: str`

  - `deleted: bool`

  - `object: Literal["organization.external_storage.deleted"]`

    - `"organization.external_storage.deleted"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
external_storage_deleted = client.admin.organization.external_storage.delete(
    "extstorage_123",
)
print(external_storage_deleted.id)
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "organization.external_storage.deleted"
}
```

## List external storage configurations

`admin.organization.external_storage.list(ExternalStorageListParams**kwargs)  -> SyncCursorPage[ExternalStorageConfiguration]`

**get** `/organization/external_storage`

List the organization's customer-managed external storage configurations.

### Parameters

- `after: Optional[str]`

  Return external storage configurations after this ID.

- `limit: Optional[int]`

- `order: Optional[Literal["asc", "desc"]]`

  - `"asc"`

  - `"desc"`

- `project_id: Optional[str]`

### Returns

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

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
page = client.admin.organization.external_storage.list()
page = page.data[0]
print(page.id)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": 0,
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
      },
      "status": "pending"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Get an external storage configuration

`admin.organization.external_storage.retrieve(strexternal_storage_id)  -> ExternalStorageConfiguration`

**get** `/organization/external_storage/{external_storage_id}`

Get one customer-managed external storage configuration.

### Parameters

- `external_storage_id: str`

### Returns

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

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
external_storage_configuration = client.admin.organization.external_storage.retrieve(
    "extstorage_123",
)
print(external_storage_configuration.id)
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
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
  },
  "status": "pending"
}
```

## Validate an external storage configuration

`admin.organization.external_storage.validate(strexternal_storage_id)  -> ExternalStorageConfiguration`

**post** `/organization/external_storage/{external_storage_id}/validate`

Validate one customer-managed external storage configuration.

### Parameters

- `external_storage_id: str`

### Returns

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

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
external_storage_configuration = client.admin.organization.external_storage.validate(
    "extstorage_123",
)
print(external_storage_configuration.id)
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
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
  },
  "status": "pending"
}
```

## Domain Types

### Aws External Storage Provider

- `class AwsExternalStorageProvider: …`

  - `account_id: str`

  - `bucket: str`

  - `external_id: str`

  - `region: str`

  - `role_arn: str`

  - `type: Literal["aws"]`

    - `"aws"`

### Azure External Storage Provider

- `class AzureExternalStorageProvider: …`

  - `account_name: str`

  - `container: str`

  - `region: str`

  - `resource_group: str`

  - `subscription_id: str`

  - `tenant_id: str`

  - `type: Literal["azure"]`

    - `"azure"`

### External Storage Configuration

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

### External Storage Deleted

- `class ExternalStorageDeleted: …`

  - `id: str`

  - `deleted: bool`

  - `object: Literal["organization.external_storage.deleted"]`

    - `"organization.external_storage.deleted"`

### Gcp External Storage Provider

- `class GcpExternalStorageProvider: …`

  - `audience: str`

  - `bucket: str`

  - `region: str`

  - `type: Literal["gcp"]`

    - `"gcp"`

  - `workload_identity_pool_id: str`

  - `workload_identity_project_number: str`

  - `workload_identity_provider_id: str`

<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/external_storage/methods/delete/ -->

## Delete an external storage configuration

`admin.organization.external_storage.delete(strexternal_storage_id)  -> ExternalStorageDeleted`

**delete** `/organization/external_storage/{external_storage_id}`

Disconnect a customer-managed external storage configuration. Removing the project's last configuration restores organization-default retention if customer-managed retention was active. Repeating a deletion also completes any interrupted retention update. Cloud storage is unchanged.

- `external_storage_id: str`

- `class ExternalStorageDeleted: …`

  - `id: str`

  - `deleted: bool`

  - `object: Literal["organization.external_storage.deleted"]`

    - `"organization.external_storage.deleted"`

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
external_storage_deleted = client.admin.organization.external_storage.delete(
    "extstorage_123",
print(external_storage_deleted.id)

  "deleted": true,
  "object": "organization.external_storage.deleted"

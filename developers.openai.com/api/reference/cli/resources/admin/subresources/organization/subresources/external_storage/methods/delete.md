<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/external_storage/methods/delete/ -->

## Delete an external storage configuration

`$ openai admin:organization:external-storage delete`

**delete** `/organization/external_storage/{external_storage_id}`

Disconnect a customer-managed external storage configuration. Removing the project's last configuration restores organization-default retention if customer-managed retention was active. Repeating a deletion also completes any interrupted retention update. Cloud storage is unchanged.

- `--external-storage-id: string`

- `external_storage_deleted: object { id, deleted, object }`

  - `id: string`

  - `deleted: boolean`

  - `object: "organization.external_storage.deleted"`

```cli
openai admin:organization:external-storage delete \
  --admin-api-key 'My Admin API Key' \
  --external-storage-id extstorage_123

  "deleted": true,
  "object": "organization.external_storage.deleted"

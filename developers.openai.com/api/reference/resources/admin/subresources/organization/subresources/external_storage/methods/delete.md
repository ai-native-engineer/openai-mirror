<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/external_storage/methods/delete/ -->

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[External Storage](/api/reference/resources/admin/subresources/organization/subresources/external_storage)

# Delete an external storage configuration

DELETE/organization/external\_storage/{external\_storage\_id}

Disconnect a customer-managed external storage configuration. Removing the project’s last configuration restores organization-default retention if customer-managed retention was active. Repeating a deletion also completes any interrupted retention update. Cloud storage is unchanged.

external\_storage\_id: string

ExternalStorageDeleted object { id, deleted, object }

deleted: boolean

object: "organization.external\_storage.deleted"

### Delete an external storage configuration

curl -X DELETE https://api.openai.com/v1/organization/external_storage/extstorage_abc123 \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

  "object": "organization.external_storage.deleted",
  "id": "extstorage_abc123",
  "deleted": true

  "object": "organization.external_storage.deleted",
  "id": "extstorage_abc123",
  "deleted": true

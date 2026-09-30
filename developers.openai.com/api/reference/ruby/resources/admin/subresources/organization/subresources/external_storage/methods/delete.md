<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/external_storage/methods/delete/ -->

## Delete an external storage configuration

`admin.organization.external_storage.delete(external_storage_id) -> ExternalStorageDeleted`

**delete** `/organization/external_storage/{external_storage_id}`

Disconnect a customer-managed external storage configuration. Removing the project's last configuration restores organization-default retention if customer-managed retention was active. Repeating a deletion also completes any interrupted retention update. Cloud storage is unchanged.

- `external_storage_id: String`

- `class ExternalStorageDeleted`

  - `id: String`

  - `deleted: bool`

  - `object: :"organization.external_storage.deleted"`

    - `:"organization.external_storage.deleted"`

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

external_storage_deleted = openai.admin.organization.external_storage.delete("extstorage_123")

puts(external_storage_deleted)

  "deleted": true,
  "object": "organization.external_storage.deleted"

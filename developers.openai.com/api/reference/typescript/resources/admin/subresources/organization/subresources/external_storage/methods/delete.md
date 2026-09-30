<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/external_storage/methods/delete/ -->

## Delete an external storage configuration

`client.admin.organization.externalStorage.delete(stringexternalStorageID, RequestOptionsoptions?): ExternalStorageDeleted`

**delete** `/organization/external_storage/{external_storage_id}`

Disconnect a customer-managed external storage configuration. Removing the project's last configuration restores organization-default retention if customer-managed retention was active. Repeating a deletion also completes any interrupted retention update. Cloud storage is unchanged.

- `externalStorageID: string`

- `ExternalStorageDeleted`

  - `id: string`

  - `deleted: boolean`

  - `object: "organization.external_storage.deleted"`

    - `"organization.external_storage.deleted"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const externalStorageDeleted = await client.admin.organization.externalStorage.delete(
  'extstorage_123',
);

console.log(externalStorageDeleted.id);

  "deleted": true,
  "object": "organization.external_storage.deleted"

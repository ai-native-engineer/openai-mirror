<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/external_keys/methods/validate/ -->

## Validate an external key config for the user's organization

`client.admin.organization.externalKeys.validate(stringexternalKeyID, RequestOptionsoptions?): ExternalKeyValidateResponse`

**post** `/organization/external_keys/{external_key_id}/validate`

Validate an external key config for the user's organization

- `externalKeyID: string`

- `ExternalKeyValidateResponse`

  - `status: string`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const response = await client.admin.organization.externalKeys.validate('external_key_id');

console.log(response.status);

  "status": "status"

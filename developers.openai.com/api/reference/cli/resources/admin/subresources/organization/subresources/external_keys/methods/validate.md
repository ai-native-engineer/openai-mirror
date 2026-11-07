<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/external_keys/methods/validate/ -->

## Validate an external key config for the user's organization

`$ openai admin:organization:external-keys validate`

**post** `/organization/external_keys/{external_key_id}/validate`

Validate an external key config for the user's organization

- `--external-key-id: string`

- `AdminOrganizationExternalKeyValidateResponse: object { status }`

  - `status: string`

```cli
openai admin:organization:external-keys validate \
  --admin-api-key 'My Admin API Key' \
  --external-key-id external_key_id

  "status": "status"

<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/delete/ -->

## Delete Platform workload identity provider

`$ openai admin:organization:workload-identity-providers delete`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Delete a provider after deleting all its federation rules.

- `--workload-identity-provider-id: string`

  `minLength: 1`

- `workload_identity_provider_deleted: object { id, deleted, object }`

  - `id: string`

  - `deleted: boolean`

  - `object: "organization.workload_identity_provider.deleted"`

```cli
openai admin:organization:workload-identity-providers delete \
  --admin-api-key 'My Admin API Key' \
  --workload-identity-provider-id x

  "deleted": true,
  "object": "organization.workload_identity_provider.deleted"

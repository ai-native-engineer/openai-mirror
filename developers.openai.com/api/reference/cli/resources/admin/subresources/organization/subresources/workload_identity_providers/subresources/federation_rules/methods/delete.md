<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/delete/ -->

## Delete Platform workload identity federation rule

`$ openai admin:organization:workload-identity-providers:federation-rules delete`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Delete a federation rule to a project service account.

- `--workload-identity-provider-id: string`

  `minLength: 1`

- `--workload-identity-federation-rule-id: string`

  `minLength: 1`

- `federation_rule_deleted: object { id, deleted, object }`

  - `id: string`

  - `deleted: boolean`

  - `object: "organization.workload_identity_federation_rule.deleted"`

```cli
openai admin:organization:workload-identity-providers:federation-rules delete \
  --admin-api-key 'My Admin API Key' \
  --workload-identity-provider-id x \
  --workload-identity-federation-rule-id x

  "deleted": true,
  "object": "organization.workload_identity_federation_rule.deleted"

<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/create/ -->

## Create Platform workload identity federation rule

`$ openai admin:organization:workload-identity-providers:federation-rules create`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

Bind verified token attributes to an existing project service account.

- `--workload-identity-provider-id: string`

  `minLength: 1`

- `--attribute-matchers: map[string or boolean or number or number]`

- `--project-id: string`

  `minLength: 1`

- `--service-account-id: string`

  `minLength: 1`

- `--description: optional string`

- `--enabled: optional boolean`

- `--name: optional string`

- `--permissions: optional object { type }  or object { scopes, type }`

- `federation_rule: object { id, attribute_matchers, created_at, 9 more }`

  - `id: string`

  - `attribute_matchers: map[string or boolean or number or number]`

    - `union_member_0: string`

    - `union_member_1: boolean`

    - `union_member_2: number or number`

      - `union_member_0: number`

      - `union_member_1: number`

  - `created_at: number`

  - `description: string`

  - `enabled: boolean`

  - `name: string`

  - `object: "organization.workload_identity_federation_rule"`

  - `permissions: object { type }  or object { scopes, type }`

    - `service_account_default: object { type }`

    - `restricted: object { scopes, type }`

      - `scopes: array of string`

      - `type: "restricted"`

  - `project_id: string`

  - `service_account_id: string`

  - `updated_at: number`

  - `workload_identity_provider_id: string`

```cli
openai admin:organization:workload-identity-providers:federation-rules create \
  --admin-api-key 'My Admin API Key' \
  --workload-identity-provider-id x \
  --attribute-matchers '{foo: string}' \
  --project-id x \
  --service-account-id x

  "attribute_matchers": {
    "foo": "string"
  "enabled": true,
  "object": "organization.workload_identity_federation_rule",
  "permissions": {
    "type": "service_account_default"
  "project_id": "project_id",
  "service_account_id": "service_account_id",
  "updated_at": 0,
  "workload_identity_provider_id": "workload_identity_provider_id"

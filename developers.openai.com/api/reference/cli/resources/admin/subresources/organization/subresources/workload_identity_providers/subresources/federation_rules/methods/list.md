<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/list/ -->

## List Platform workload identity federation rules

`$ openai admin:organization:workload-identity-providers:federation-rules list`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

List the provider's federation rules to project service accounts.

- `--workload-identity-provider-id: string`

  `minLength: 1`

- `--after: optional string`

  `minLength: 1`

- `--limit: optional number`

  `minimum: 1`, `maximum: 100`

- `--order: optional "asc" or "desc"`

- `--service-account-id: optional string`

  `minLength: 1`

- `PlatformFederationRuleListResource: object { data, first_id, has_more, 2 more }`

  - `data: array of FederationRule`

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

  - `first_id: string`

  - `has_more: boolean`

  - `last_id: string`

  - `object: "list"`

```cli
openai admin:organization:workload-identity-providers:federation-rules list \
  --admin-api-key 'My Admin API Key' \
  --workload-identity-provider-id x

  "data": [
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
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

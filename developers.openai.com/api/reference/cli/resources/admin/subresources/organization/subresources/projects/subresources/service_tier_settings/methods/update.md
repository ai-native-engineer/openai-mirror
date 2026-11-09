<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_tier_settings/methods/update/ -->

## Update project service tier settings

`$ openai admin:organization:projects:service-tier-settings update`

**post** `/organization/projects/{project_id}/service_tier_settings`

Update the default or enabled service tiers atomically. Supply at least one field. Omitted fields keep their current values.

- `--project-id: string`

  The ID of the project

- `--default: optional "standard" or "fast" or "scale"`

  Default tier for requests that omit service_tier or use auto.

- `--enabled-tiers: optional "all" or array of ProjectOptionalServiceTier`

  Additional service tiers enabled for this project. "all" includes future tiers. An empty array allows only Standard. Organization policy and eligibility still apply.

- `project_service_tier_settings: object { default, enabled_tiers, object }`

  - `default: "standard" or "fast" or "scale"`

    Default tier for requests that omit service_tier or use auto.

    - `"standard"`

    - `"fast"`

    - `"scale"`

  - `enabled_tiers: "all" or array of ProjectOptionalServiceTier`

    Additional service tiers enabled for this project. "all" includes future tiers. An empty array allows only Standard. Organization policy and eligibility still apply.

    - `union_member_0: "all"`

    - `union_member_1: array of ProjectOptionalServiceTier`

      - `"flex"`

      - `"fast"`

      - `"ultrafast"`

  - `object: "project.service_tier_settings"`

```cli
openai admin:organization:projects:service-tier-settings update \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id \
  --default standard

  "default": "standard",
  "enabled_tiers": "all",
  "object": "project.service_tier_settings"

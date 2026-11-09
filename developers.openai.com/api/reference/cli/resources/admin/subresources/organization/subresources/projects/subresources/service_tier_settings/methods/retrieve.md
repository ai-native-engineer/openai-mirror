<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_tier_settings/methods/retrieve/ -->

## Retrieve project service tier settings

`$ openai admin:organization:projects:service-tier-settings retrieve`

**get** `/organization/projects/{project_id}/service_tier_settings`

Retrieve the configured default and enabled service tiers for a project.

- `--project-id: string`

  The ID of the project

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
openai admin:organization:projects:service-tier-settings retrieve \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id

  "default": "standard",
  "enabled_tiers": "all",
  "object": "project.service_tier_settings"

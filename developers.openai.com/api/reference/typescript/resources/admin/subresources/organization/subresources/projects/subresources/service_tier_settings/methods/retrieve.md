<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_tier_settings/methods/retrieve/ -->

## Retrieve project service tier settings

`client.admin.organization.projects.serviceTierSettings.retrieve(stringprojectID, RequestOptionsoptions?): ProjectServiceTierSettings`

**get** `/organization/projects/{project_id}/service_tier_settings`

Retrieve the configured default and enabled service tiers for a project.

- `projectID: string`

  The ID of the project

- `ProjectServiceTierSettings`

  - `default: "standard" | "fast" | "scale"`

    Default tier for requests that omit service_tier or use auto.

    - `"standard"`

    - `"fast"`

    - `"scale"`

  - `enabled_tiers: "all" | Array<ProjectOptionalServiceTier>`

    Additional service tiers enabled for this project. "all" includes future tiers. An empty array allows only Standard. Organization policy and eligibility still apply.

    - `"all"`

      - `"all"`

    - `Array<ProjectOptionalServiceTier>`

      - `"flex"`

      - `"fast"`

      - `"ultrafast"`

  - `object: "project.service_tier_settings"`

    - `"project.service_tier_settings"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const projectServiceTierSettings =
  await client.admin.organization.projects.serviceTierSettings.retrieve('project_id');

console.log(projectServiceTierSettings.default);

  "default": "standard",
  "enabled_tiers": "all",
  "object": "project.service_tier_settings"

<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_tier_settings/methods/retrieve/ -->

## Retrieve project service tier settings

`admin.organization.projects.service_tier_settings.retrieve(strproject_id)  -> ProjectServiceTierSettings`

**get** `/organization/projects/{project_id}/service_tier_settings`

Retrieve the configured default and enabled service tiers for a project.

- `project_id: str`

  The ID of the project

- `class ProjectServiceTierSettings: …`

  - `default: Literal["standard", "fast", "scale"]`

    Default tier for requests that omit service_tier or use auto.

    - `"standard"`

    - `"fast"`

    - `"scale"`

  - `enabled_tiers: Union[Literal["all"], List[ProjectOptionalServiceTier]]`

    Additional service tiers enabled for this project. "all" includes future tiers. An empty array allows only Standard. Organization policy and eligibility still apply.

    - `Literal["all"]`

      - `"all"`

    - `List[ProjectOptionalServiceTier]`

      - `"flex"`

      - `"fast"`

      - `"ultrafast"`

  - `object: Literal["project.service_tier_settings"]`

    - `"project.service_tier_settings"`

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
project_service_tier_settings = client.admin.organization.projects.service_tier_settings.retrieve(
    "project_id",
print(project_service_tier_settings.default)

  "default": "standard",
  "enabled_tiers": "all",
  "object": "project.service_tier_settings"

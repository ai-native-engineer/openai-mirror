<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_tier_settings/methods/update/ -->

## Update project service tier settings

`admin.organization.projects.service_tier_settings.update(strproject_id, ServiceTierSettingUpdateParams**kwargs)  -> ProjectServiceTierSettings`

**post** `/organization/projects/{project_id}/service_tier_settings`

Update the default or enabled service tiers atomically. Supply at least one field. Omitted fields keep their current values.

- `project_id: str`

  The ID of the project

- `default: Optional[Literal["standard", "fast", "scale"]]`

  Default tier for requests that omit service_tier or use auto.

  - `"standard"`

  - `"fast"`

  - `"scale"`

- `enabled_tiers: Optional[Union[Literal["all"], List[ProjectOptionalServiceTier]]]`

  Additional service tiers enabled for this project. "all" includes future tiers. An empty array allows only Standard. Organization policy and eligibility still apply.

  - `Literal["all"]`

    - `"all"`

  - `List[ProjectOptionalServiceTier]`

    - `"flex"`

    - `"fast"`

    - `"ultrafast"`

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
project_service_tier_settings = client.admin.organization.projects.service_tier_settings.update(
    project_id="project_id",
    default="standard",
print(project_service_tier_settings.default)

  "default": "standard",
  "enabled_tiers": "all",
  "object": "project.service_tier_settings"

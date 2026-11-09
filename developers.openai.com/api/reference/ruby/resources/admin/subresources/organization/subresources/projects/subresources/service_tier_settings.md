<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/service_tier_settings/ -->

# Service Tier Settings

## Retrieve project service tier settings

`admin.organization.projects.service_tier_settings.retrieve(project_id) -> ProjectServiceTierSettings`

**get** `/organization/projects/{project_id}/service_tier_settings`

Retrieve the configured default and enabled service tiers for a project.

### Parameters

- `project_id: String`

  The ID of the project

### Returns

- `class ProjectServiceTierSettings`

  - `default: :standard | :fast | :scale`

    Default tier for requests that omit service_tier or use auto.

    - `:standard`

    - `:fast`

    - `:scale`

  - `enabled_tiers: :all | Array[ProjectOptionalServiceTier]`

    Additional service tiers enabled for this project. "all" includes future tiers. An empty array allows only Standard. Organization policy and eligibility still apply.

    - `EnabledTiers = :all`

      - `:all`

    - `UnionMember1 = Array[ProjectOptionalServiceTier]`

      - `:flex`

      - `:fast`

      - `:ultrafast`

  - `object: :"project.service_tier_settings"`

    - `:"project.service_tier_settings"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

project_service_tier_settings = openai.admin.organization.projects.service_tier_settings.retrieve("project_id")

puts(project_service_tier_settings)
```

#### 200 — Example

```json
{
  "default": "standard",
  "enabled_tiers": "all",
  "object": "project.service_tier_settings"
}
```

## Update project service tier settings

`admin.organization.projects.service_tier_settings.update(project_id, **kwargs) -> ProjectServiceTierSettings`

**post** `/organization/projects/{project_id}/service_tier_settings`

Update the default or enabled service tiers atomically. Supply at least one field. Omitted fields keep their current values.

### Parameters

- `project_id: String`

  The ID of the project

- `default: :standard | :fast | :scale`

  Default tier for requests that omit service_tier or use auto.

  - `:standard`

  - `:fast`

  - `:scale`

- `enabled_tiers: :all | Array[ProjectOptionalServiceTier]`

  Additional service tiers enabled for this project. "all" includes future tiers. An empty array allows only Standard. Organization policy and eligibility still apply.

  - `EnabledTiers = :all`

    - `:all`

  - `UnionMember1 = Array[ProjectOptionalServiceTier]`

    - `:flex`

    - `:fast`

    - `:ultrafast`

### Returns

- `class ProjectServiceTierSettings`

  - `default: :standard | :fast | :scale`

    Default tier for requests that omit service_tier or use auto.

    - `:standard`

    - `:fast`

    - `:scale`

  - `enabled_tiers: :all | Array[ProjectOptionalServiceTier]`

    Additional service tiers enabled for this project. "all" includes future tiers. An empty array allows only Standard. Organization policy and eligibility still apply.

    - `EnabledTiers = :all`

      - `:all`

    - `UnionMember1 = Array[ProjectOptionalServiceTier]`

      - `:flex`

      - `:fast`

      - `:ultrafast`

  - `object: :"project.service_tier_settings"`

    - `:"project.service_tier_settings"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

project_service_tier_settings = openai.admin.organization.projects.service_tier_settings.update("project_id", default: :standard)

puts(project_service_tier_settings)
```

#### 200 — Example

```json
{
  "default": "standard",
  "enabled_tiers": "all",
  "object": "project.service_tier_settings"
}
```

## Domain Types

### Project Optional Service Tier

- `ProjectOptionalServiceTier = :flex | :fast | :ultrafast`

  - `:flex`

  - `:fast`

  - `:ultrafast`

### Project Service Tier Settings

- `class ProjectServiceTierSettings`

  - `default: :standard | :fast | :scale`

    Default tier for requests that omit service_tier or use auto.

    - `:standard`

    - `:fast`

    - `:scale`

  - `enabled_tiers: :all | Array[ProjectOptionalServiceTier]`

    Additional service tiers enabled for this project. "all" includes future tiers. An empty array allows only Standard. Organization policy and eligibility still apply.

    - `EnabledTiers = :all`

      - `:all`

    - `UnionMember1 = Array[ProjectOptionalServiceTier]`

      - `:flex`

      - `:fast`

      - `:ultrafast`

  - `object: :"project.service_tier_settings"`

    - `:"project.service_tier_settings"`

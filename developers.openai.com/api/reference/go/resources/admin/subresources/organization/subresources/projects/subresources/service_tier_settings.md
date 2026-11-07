<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_tier_settings/ -->

# Service Tier Settings

## Retrieve project service tier settings

`client.Admin.Organization.Projects.ServiceTierSettings.Get(ctx, projectID) (*ProjectServiceTierSettings, error)`

**get** `/organization/projects/{project_id}/service_tier_settings`

Retrieve the configured default and enabled service tiers for a project.

### Parameters

- `projectID string`

  The ID of the project

### Returns

- `type ProjectServiceTierSettings struct{…}`

  - `Default ProjectServiceTierSettingsDefault`

    Default tier for requests that omit service_tier or use auto.

    - `const ProjectServiceTierSettingsDefaultStandard ProjectServiceTierSettingsDefault = "standard"`

    - `const ProjectServiceTierSettingsDefaultFast ProjectServiceTierSettingsDefault = "fast"`

    - `const ProjectServiceTierSettingsDefaultScale ProjectServiceTierSettingsDefault = "scale"`

  - `EnabledTiers ProjectServiceTierSettingsEnabledTiersUnion`

    Additional service tiers enabled for this project. "all" includes future tiers. An empty array allows only Standard. Organization policy and eligibility still apply.

    - `type All string`

      - `const AllAll All = "all"`

    - `type ProjectServiceTierSettingsEnabledTiers []ProjectOptionalServiceTier`

      - `const ProjectOptionalServiceTierFlex ProjectOptionalServiceTier = "flex"`

      - `const ProjectOptionalServiceTierFast ProjectOptionalServiceTier = "fast"`

      - `const ProjectOptionalServiceTierUltrafast ProjectOptionalServiceTier = "ultrafast"`

  - `Object ProjectServiceTierSettings`

    - `const ProjectServiceTierSettingsProjectServiceTierSettings ProjectServiceTierSettings = "project.service_tier_settings"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  )
  projectServiceTierSettings, err := client.Admin.Organization.Projects.ServiceTierSettings.Get(context.TODO(), "project_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", projectServiceTierSettings.Default)
}
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

`client.Admin.Organization.Projects.ServiceTierSettings.Update(ctx, projectID, body) (*ProjectServiceTierSettings, error)`

**post** `/organization/projects/{project_id}/service_tier_settings`

Update the default or enabled service tiers atomically. Supply at least one field. Omitted fields keep their current values.

### Parameters

- `projectID string`

  The ID of the project

- `body AdminOrganizationProjectServiceTierSettingUpdateParams`

  - `Default param.Field[AdminOrganizationProjectServiceTierSettingUpdateParamsDefault]`

    Default tier for requests that omit service_tier or use auto.

    - `const AdminOrganizationProjectServiceTierSettingUpdateParamsDefaultStandard AdminOrganizationProjectServiceTierSettingUpdateParamsDefault = "standard"`

    - `const AdminOrganizationProjectServiceTierSettingUpdateParamsDefaultFast AdminOrganizationProjectServiceTierSettingUpdateParamsDefault = "fast"`

    - `const AdminOrganizationProjectServiceTierSettingUpdateParamsDefaultScale AdminOrganizationProjectServiceTierSettingUpdateParamsDefault = "scale"`

  - `EnabledTiers param.Field[AdminOrganizationProjectServiceTierSettingUpdateParamsEnabledTiersUnion]`

    Additional service tiers enabled for this project. "all" includes future tiers. An empty array allows only Standard. Organization policy and eligibility still apply.

    - `type All string`

      - `const AllAll All = "all"`

    - `type AdminOrganizationProjectServiceTierSettingUpdateParamsEnabledTiers []ProjectOptionalServiceTier`

      - `const ProjectOptionalServiceTierFlex ProjectOptionalServiceTier = "flex"`

      - `const ProjectOptionalServiceTierFast ProjectOptionalServiceTier = "fast"`

      - `const ProjectOptionalServiceTierUltrafast ProjectOptionalServiceTier = "ultrafast"`

### Returns

- `type ProjectServiceTierSettings struct{…}`

  - `Default ProjectServiceTierSettingsDefault`

    Default tier for requests that omit service_tier or use auto.

    - `const ProjectServiceTierSettingsDefaultStandard ProjectServiceTierSettingsDefault = "standard"`

    - `const ProjectServiceTierSettingsDefaultFast ProjectServiceTierSettingsDefault = "fast"`

    - `const ProjectServiceTierSettingsDefaultScale ProjectServiceTierSettingsDefault = "scale"`

  - `EnabledTiers ProjectServiceTierSettingsEnabledTiersUnion`

    Additional service tiers enabled for this project. "all" includes future tiers. An empty array allows only Standard. Organization policy and eligibility still apply.

    - `type All string`

      - `const AllAll All = "all"`

    - `type ProjectServiceTierSettingsEnabledTiers []ProjectOptionalServiceTier`

      - `const ProjectOptionalServiceTierFlex ProjectOptionalServiceTier = "flex"`

      - `const ProjectOptionalServiceTierFast ProjectOptionalServiceTier = "fast"`

      - `const ProjectOptionalServiceTierUltrafast ProjectOptionalServiceTier = "ultrafast"`

  - `Object ProjectServiceTierSettings`

    - `const ProjectServiceTierSettingsProjectServiceTierSettings ProjectServiceTierSettings = "project.service_tier_settings"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  )
  projectServiceTierSettings, err := client.Admin.Organization.Projects.ServiceTierSettings.Update(
    context.TODO(),
    "project_id",
    openai.AdminOrganizationProjectServiceTierSettingUpdateParams{
      Default: openai.AdminOrganizationProjectServiceTierSettingUpdateParamsDefaultStandard,
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", projectServiceTierSettings.Default)
}
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

- `type ProjectOptionalServiceTier string`

  - `const ProjectOptionalServiceTierFlex ProjectOptionalServiceTier = "flex"`

  - `const ProjectOptionalServiceTierFast ProjectOptionalServiceTier = "fast"`

  - `const ProjectOptionalServiceTierUltrafast ProjectOptionalServiceTier = "ultrafast"`

### Project Service Tier Settings

- `type ProjectServiceTierSettings struct{…}`

  - `Default ProjectServiceTierSettingsDefault`

    Default tier for requests that omit service_tier or use auto.

    - `const ProjectServiceTierSettingsDefaultStandard ProjectServiceTierSettingsDefault = "standard"`

    - `const ProjectServiceTierSettingsDefaultFast ProjectServiceTierSettingsDefault = "fast"`

    - `const ProjectServiceTierSettingsDefaultScale ProjectServiceTierSettingsDefault = "scale"`

  - `EnabledTiers ProjectServiceTierSettingsEnabledTiersUnion`

    Additional service tiers enabled for this project. "all" includes future tiers. An empty array allows only Standard. Organization policy and eligibility still apply.

    - `type All string`

      - `const AllAll All = "all"`

    - `type ProjectServiceTierSettingsEnabledTiers []ProjectOptionalServiceTier`

      - `const ProjectOptionalServiceTierFlex ProjectOptionalServiceTier = "flex"`

      - `const ProjectOptionalServiceTierFast ProjectOptionalServiceTier = "fast"`

      - `const ProjectOptionalServiceTierUltrafast ProjectOptionalServiceTier = "ultrafast"`

  - `Object ProjectServiceTierSettings`

    - `const ProjectServiceTierSettingsProjectServiceTierSettings ProjectServiceTierSettings = "project.service_tier_settings"`

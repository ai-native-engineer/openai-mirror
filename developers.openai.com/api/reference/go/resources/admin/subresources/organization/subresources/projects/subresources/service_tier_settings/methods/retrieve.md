<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_tier_settings/methods/retrieve/ -->

## Retrieve project service tier settings

`client.Admin.Organization.Projects.ServiceTierSettings.Get(ctx, projectID) (*ProjectServiceTierSettings, error)`

**get** `/organization/projects/{project_id}/service_tier_settings`

Retrieve the configured default and enabled service tiers for a project.

- `projectID string`

  The ID of the project

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

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  projectServiceTierSettings, err := client.Admin.Organization.Projects.ServiceTierSettings.Get(context.TODO(), "project_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectServiceTierSettings.Default)

  "default": "standard",
  "enabled_tiers": "all",
  "object": "project.service_tier_settings"

<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_tier_settings/methods/update/ -->

## Update project service tier settings

`ProjectServiceTierSettings admin().organization().projects().serviceTierSettings().update(ServiceTierSettingUpdateParamsparams = ServiceTierSettingUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/organization/projects/{project_id}/service_tier_settings`

Update the default or enabled service tiers atomically. Supply at least one field. Omitted fields keep their current values.

- `ServiceTierSettingUpdateParams params`

  - `Optional<String> projectId`

    The ID of the project

  - `Optional<Default> default_`

    Default tier for requests that omit service_tier or use auto.

    - `STANDARD("standard")`

    - `FAST("fast")`

    - `SCALE("scale")`

  - `Optional<EnabledTiers> enabledTiers`

    Additional service tiers enabled for this project. "all" includes future tiers. An empty array allows only Standard. Organization policy and eligibility still apply.

    - `JsonValue;`

      - `ALL("all")`

    - `List<ProjectOptionalServiceTier>`

      - `FLEX("flex")`

      - `FAST("fast")`

      - `ULTRAFAST("ultrafast")`

- `class ProjectServiceTierSettings:`

  - `Default default_`

    Default tier for requests that omit service_tier or use auto.

    - `STANDARD("standard")`

    - `FAST("fast")`

    - `SCALE("scale")`

  - `EnabledTiers enabledTiers`

    Additional service tiers enabled for this project. "all" includes future tiers. An empty array allows only Standard. Organization policy and eligibility still apply.

    - `JsonValue;`

      - `ALL("all")`

    - `List<ProjectOptionalServiceTier>`

      - `FLEX("flex")`

      - `FAST("fast")`

      - `ULTRAFAST("ultrafast")`

  - `JsonValue; object_ "project.service_tier_settings"constant`

    - `PROJECT_SERVICE_TIER_SETTINGS("project.service_tier_settings")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.projects.servicetiersettings.ProjectServiceTierSettings;
import com.openai.models.admin.organization.projects.servicetiersettings.ServiceTierSettingUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ServiceTierSettingUpdateParams params = ServiceTierSettingUpdateParams.builder()
            .default_(ServiceTierSettingUpdateParams.Default.STANDARD)
            .build();
        ProjectServiceTierSettings projectServiceTierSettings = client.admin().organization().projects().serviceTierSettings().update(
          "project_id", params
        );

  "default": "standard",
  "enabled_tiers": "all",
  "object": "project.service_tier_settings"

<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_tier_settings/methods/retrieve/ -->

## Retrieve project service tier settings

`ProjectServiceTierSettings admin().organization().projects().serviceTierSettings().retrieve(ServiceTierSettingRetrieveParamsparams = ServiceTierSettingRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/organization/projects/{project_id}/service_tier_settings`

Retrieve the configured default and enabled service tiers for a project.

- `ServiceTierSettingRetrieveParams params`

  - `Optional<String> projectId`

    The ID of the project

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
import com.openai.models.admin.organization.projects.servicetiersettings.ServiceTierSettingRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ProjectServiceTierSettings projectServiceTierSettings = client.admin().organization().projects().serviceTierSettings().retrieve("project_id");

  "default": "standard",
  "enabled_tiers": "all",
  "object": "project.service_tier_settings"

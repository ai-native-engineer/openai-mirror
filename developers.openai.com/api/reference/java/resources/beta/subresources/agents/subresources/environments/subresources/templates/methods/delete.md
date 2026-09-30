<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/delete/ -->

## Delete an agent environment template

`EnvironmentTemplateDeleted beta().agents().environments().templates().delete(TemplateDeleteParamsparams = TemplateDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/agents/environments/templates/{environment_template_id}`

Deletes reusable environment configuration and all confidential template inputs. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

- `TemplateDeleteParams params`

  - `Optional<String> environmentTemplateId`

- `class EnvironmentTemplateDeleted:`

  A deleted reusable environment template.

  - `String id`

    The ID of the deleted environment template.

  - `boolean deleted`

    Whether the environment template was deleted. Always `true`.

  - `JsonValue; object_ "agent.environment.template.deleted"constant`

    The object type. Always `agent.environment.template.deleted`.

    - `AGENT_ENVIRONMENT_TEMPLATE_DELETED("agent.environment.template.deleted")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.environments.templates.EnvironmentTemplateDeleted;
import com.openai.models.beta.agents.environments.templates.TemplateDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EnvironmentTemplateDeleted environmentTemplateDeleted = client.beta().agents().environments().templates().delete("environment_template_id");

  "deleted": true,
  "object": "agent.environment.template.deleted"

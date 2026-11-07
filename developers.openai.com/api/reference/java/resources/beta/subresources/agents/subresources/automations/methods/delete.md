<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/automations/methods/delete/ -->

## Delete an automation

`AutomationDeleted beta().agents().automations().delete(AutomationDeleteParamsparams = AutomationDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/agents/automations/{automation_id}`

Deletes the automation and prevents future invocations without deleting its target session.

- `AutomationDeleteParams params`

  - `Optional<String> automationId`

    `minLength: 0`, `maxLength: 1048576`

- `class AutomationDeleted:`

  - `String id`

    The deleted automation ID.

    `minLength: 0`

  - `boolean deleted`

    Always true.

  - `JsonValue; object_ "agent.automation.deleted"constant`

    Always `agent.automation.deleted`.

    - `AGENT_AUTOMATION_DELETED("agent.automation.deleted")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.automations.AutomationDeleteParams;
import com.openai.models.beta.agents.automations.AutomationDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AutomationDeleted automationDeleted = client.beta().agents().automations().delete("automation_id");

  "deleted": true,
  "object": "agent.automation.deleted"

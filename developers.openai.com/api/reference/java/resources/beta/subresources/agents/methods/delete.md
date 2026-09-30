<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/methods/delete/ -->

## Delete an agent

`AgentDeleted beta().agents().delete(AgentDeleteParamsparams = AgentDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/agents/{agent_id}`

Deletes a reusable agent. See [agent configuration](/api/docs/guides/agents-api/configuration).

- `AgentDeleteParams params`

  - `Optional<String> agentId`

- `class AgentDeleted:`

  A deleted reusable agent.

  - `String id`

    The ID of the deleted agent.

  - `boolean deleted`

    Whether the agent was deleted. Always `true`.

  - `JsonValue; object_ "agent.deleted"constant`

    The object type. Always `agent.deleted`.

    - `AGENT_DELETED("agent.deleted")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.AgentDeleteParams;
import com.openai.models.beta.agents.AgentDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AgentDeleted agentDeleted = client.beta().agents().delete("agent_id");

  "deleted": true,
  "object": "agent.deleted"

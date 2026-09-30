<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/sessions/methods/delete/ -->

## Delete an agent session

`AgentSessionDeleted beta().agents().sessions().delete(SessionDeleteParamsparams = SessionDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/agents/sessions/{session_id}`

Removes a managed agent session from the public API and returns a deletion confirmation. If backend execution has ended, deletion can cancel a still-open public turn and abandon unpublished outputs. Running execution must be cancelled first. Physical cleanup may continue asynchronously. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

- `SessionDeleteParams params`

  - `Optional<String> sessionId`

- `class AgentSessionDeleted:`

  A Managed Agents session removed from the public API. Physical cleanup may continue asynchronously.

  - `String id`

    The ID of the deleted session.

  - `boolean deleted`

    Whether the session has been removed from the public API. Always `true`. Physical cleanup may still be in progress.

  - `JsonValue; object_ "agent.session.deleted"constant`

    The object type. Always `agent.session.deleted`.

    - `AGENT_SESSION_DELETED("agent.session.deleted")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.AgentSessionDeleted;
import com.openai.models.beta.agents.sessions.SessionDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AgentSessionDeleted agentSessionDeleted = client.beta().agents().sessions().delete("session_id");

  "deleted": true,
  "object": "agent.session.deleted"

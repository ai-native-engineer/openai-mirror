<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/methods/retrieve/ -->

## Retrieve a session subagent

`Subagent beta().agents().sessions().subagents().retrieve(SubagentRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}`

Retrieves a subagent belonging to this session. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

- `SubagentRetrieveParams params`

  - `String sessionId`

  - `Optional<String> subagentId`

- `class Subagent:`

  A subagent created within a session.

  - `String id`

    The ID of the subagent.

  - `Optional<Long> closedAt`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `Optional<List<AgentContent>> instructions`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `class OutputText:`

      A text content part produced by the agent.

      - `String text`

        The text produced by the agent.

      - `JsonValue; type "output_text"constant`

        The content type. Always `output_text`.

        - `OUTPUT_TEXT("output_text")`

    - `EncryptedContent`

      - `String encryptedContent`

        The encrypted content payload.

      - `JsonValue; type "encrypted_content"constant`

        The content type. Always `encrypted_content`.

        - `ENCRYPTED_CONTENT("encrypted_content")`

  - `Optional<String> name`

    The runner-assigned nickname, or null when unavailable.

  - `Object object_`

    The object type. Always `agent.session.subagent`.

    - `AGENT_SESSION_SUBAGENT("agent.session.subagent")`

  - `long openedAt`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `String parentAgentId`

    The ID of the agent that created this subagent.

  - `String sessionId`

    The ID of the session that owns the subagent.

  - `Status status`

    The current status of the subagent.

    - `ACTIVE("active")`

      The subagent remains available, including while idle between turns.

    - `CLOSED("closed")`

      The subagent is closed.

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.Subagent;
import com.openai.models.beta.agents.sessions.subagents.SubagentRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SubagentRetrieveParams params = SubagentRetrieveParams.builder()
            .sessionId("session_id")
            .subagentId("subagent_id")
            .build();
        Subagent subagent = client.beta().agents().sessions().subagents().retrieve(params);

  "closed_at": 0,
  "instructions": [
      "text": "text",
      "type": "output_text"
  "object": "agent.session.subagent",
  "opened_at": 0,
  "parent_agent_id": "parent_agent_id",
  "session_id": "session_id",
  "status": "active"

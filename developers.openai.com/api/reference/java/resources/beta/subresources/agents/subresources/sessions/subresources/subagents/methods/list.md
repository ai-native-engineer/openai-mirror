<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/methods/list/ -->

## List session subagents

`SubagentListPage beta().agents().sessions().subagents().list(SubagentListParamsparams = SubagentListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/subagents`

Lists subagents in a session, including nested and closed subagents. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

- `SubagentListParams params`

  - `Optional<String> sessionId`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

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
import com.openai.models.beta.agents.sessions.subagents.SubagentListPage;
import com.openai.models.beta.agents.sessions.subagents.SubagentListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SubagentListPage page = client.beta().agents().sessions().subagents().list("session_id");

  "data": [
      "closed_at": 0,
      "instructions": [
          "text": "text",
          "type": "output_text"
      "object": "agent.session.subagent",
      "opened_at": 0,
      "parent_agent_id": "parent_agent_id",
      "session_id": "session_id",
      "status": "active"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

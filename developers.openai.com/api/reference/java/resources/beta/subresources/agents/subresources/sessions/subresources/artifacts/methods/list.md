<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/list/ -->

## List agent session artifacts

`ArtifactListPage beta().agents().sessions().artifacts().list(ArtifactListParamsparams = ArtifactListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/artifacts`

Lists immutable artifacts published by completed hosted session turns. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `ArtifactListParams params`

  - `Optional<String> sessionId`

  - `Optional<String> after`

    Return artifacts after this immutable artifact ID.

  - `Optional<String> environmentId`

    Restrict the listing to artifacts produced by this environment.

  - `Optional<Long> limit`

    The maximum number of artifacts to return, between 1 and 100.

  - `Optional<Order> order`

    Sort by creation time and ID. Defaults to descending.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

- `class SessionArtifact:`

  An immutable file published by a completed hosted session turn.

  - `String id`

    The immutable artifact ID.

  - `long createdAt`

    The Unix timestamp, in seconds, when the artifact was published.

  - `String environmentId`

    The ID of the environment that produced the artifact.

  - `JsonValue; object_ "agent.session.artifact"constant`

    The object type. Always `agent.session.artifact`.

    - `AGENT_SESSION_ARTIFACT("agent.session.artifact")`

  - `String path`

    The original absolute file path in the execution environment.

  - `String sessionId`

    The ID of the session that owns the artifact.

  - `long sizeBytes`

    The immutable artifact size in bytes.

  - `String turnId`

    The ID of the completed turn that published the artifact.

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.artifacts.ArtifactListPage;
import com.openai.models.beta.agents.sessions.artifacts.ArtifactListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ArtifactListPage page = client.beta().agents().sessions().artifacts().list("session_id");

  "data": [
      "environment_id": "environment_id",
      "object": "agent.session.artifact",
      "path": "path",
      "session_id": "session_id",
      "size_bytes": 0,
      "turn_id": "turn_id"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

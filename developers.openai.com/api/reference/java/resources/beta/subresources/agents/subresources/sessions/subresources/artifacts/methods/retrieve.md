<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/retrieve/ -->

## Retrieve an agent session artifact

`SessionArtifact beta().agents().sessions().artifacts().retrieve(ArtifactRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Retrieves immutable metadata for one durable session artifact. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `ArtifactRetrieveParams params`

  - `String sessionId`

  - `Optional<String> artifactId`

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
import com.openai.models.beta.agents.sessions.artifacts.ArtifactRetrieveParams;
import com.openai.models.beta.agents.sessions.artifacts.SessionArtifact;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ArtifactRetrieveParams params = ArtifactRetrieveParams.builder()
            .sessionId("session_id")
            .artifactId("artifact_id")
            .build();
        SessionArtifact sessionArtifact = client.beta().agents().sessions().artifacts().retrieve(params);

  "environment_id": "environment_id",
  "object": "agent.session.artifact",
  "path": "path",
  "session_id": "session_id",
  "size_bytes": 0,
  "turn_id": "turn_id"

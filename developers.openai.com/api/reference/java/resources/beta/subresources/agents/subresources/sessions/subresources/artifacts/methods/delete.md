<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/delete/ -->

## Delete an agent session artifact

`SessionArtifactDeleted beta().agents().sessions().artifacts().delete(ArtifactDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Deletes an immutable session artifact without deleting its live environment file or original Files API object. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `ArtifactDeleteParams params`

  - `String sessionId`

  - `Optional<String> artifactId`

- `class SessionArtifactDeleted:`

  Confirmation that an immutable session artifact was deleted.

  - `String id`

    The ID of the deleted session artifact.

  - `boolean deleted`

    Whether the session artifact was deleted. Always `true`.

  - `JsonValue; object_ "agent.session.artifact.deleted"constant`

    The object type. Always `agent.session.artifact.deleted`.

    - `AGENT_SESSION_ARTIFACT_DELETED("agent.session.artifact.deleted")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.artifacts.ArtifactDeleteParams;
import com.openai.models.beta.agents.sessions.artifacts.SessionArtifactDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ArtifactDeleteParams params = ArtifactDeleteParams.builder()
            .sessionId("session_id")
            .artifactId("artifact_id")
            .build();
        SessionArtifactDeleted sessionArtifactDeleted = client.beta().agents().sessions().artifacts().delete(params);

  "deleted": true,
  "object": "agent.session.artifact.deleted"

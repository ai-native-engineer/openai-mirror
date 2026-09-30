<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/ -->

# Artifacts

## Retrieve agent session artifact content

`HttpResponse beta().agents().sessions().artifacts().content(ArtifactContentParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}/content`

Downloads immutable session artifact bytes after the execution environment expires. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `ArtifactContentParams params`

  - `String sessionId`

  - `Optional<String> artifactId`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.http.HttpResponse;
import com.openai.models.beta.agents.sessions.artifacts.ArtifactContentParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ArtifactContentParams params = ArtifactContentParams.builder()
            .sessionId("session_id")
            .artifactId("artifact_id")
            .build();
        HttpResponse response = client.beta().agents().sessions().artifacts().content(params);
    }
}
```

## Delete an agent session artifact

`SessionArtifactDeleted beta().agents().sessions().artifacts().delete(ArtifactDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Deletes an immutable session artifact without deleting its live environment file or original Files API object. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `ArtifactDeleteParams params`

  - `String sessionId`

  - `Optional<String> artifactId`

### Returns

- `class SessionArtifactDeleted:`

  Confirmation that an immutable session artifact was deleted.

  - `String id`

    The ID of the deleted session artifact.

  - `boolean deleted`

    Whether the session artifact was deleted. Always `true`.

  - `JsonValue; object_ "agent.session.artifact.deleted"constant`

    The object type. Always `agent.session.artifact.deleted`.

    - `AGENT_SESSION_ARTIFACT_DELETED("agent.session.artifact.deleted")`

### Example

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
    }
}
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "agent.session.artifact.deleted"
}
```

## List agent session artifacts

`ArtifactListPage beta().agents().sessions().artifacts().list(ArtifactListParamsparams = ArtifactListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/artifacts`

Lists immutable artifacts published by completed hosted session turns. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

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

### Returns

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

### Example

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
    }
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": 0,
      "environment_id": "environment_id",
      "object": "agent.session.artifact",
      "path": "path",
      "session_id": "session_id",
      "size_bytes": 0,
      "turn_id": "turn_id"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve an agent session artifact

`SessionArtifact beta().agents().sessions().artifacts().retrieve(ArtifactRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Retrieves immutable metadata for one durable session artifact. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `ArtifactRetrieveParams params`

  - `String sessionId`

  - `Optional<String> artifactId`

### Returns

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

### Example

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
    }
}
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "environment_id": "environment_id",
  "object": "agent.session.artifact",
  "path": "path",
  "session_id": "session_id",
  "size_bytes": 0,
  "turn_id": "turn_id"
}
```

## Domain Types

### Session Artifact

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

### Session Artifact Deleted

- `class SessionArtifactDeleted:`

  Confirmation that an immutable session artifact was deleted.

  - `String id`

    The ID of the deleted session artifact.

  - `boolean deleted`

    Whether the session artifact was deleted. Always `true`.

  - `JsonValue; object_ "agent.session.artifact.deleted"constant`

    The object type. Always `agent.session.artifact.deleted`.

    - `AGENT_SESSION_ARTIFACT_DELETED("agent.session.artifact.deleted")`

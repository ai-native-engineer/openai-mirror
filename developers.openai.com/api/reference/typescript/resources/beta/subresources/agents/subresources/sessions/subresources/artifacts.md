<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/ -->

# Artifacts

## Retrieve agent session artifact content

`client.beta.agents.sessions.artifacts.content(stringartifactID, ArtifactContentParamsparams, RequestOptionsoptions?): Response`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}/content`

Downloads immutable session artifact bytes after the execution environment expires. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `artifactID: string`

- `params: ArtifactContentParams`

  - `session_id: string`

    The ID of the session that owns the artifact.

### Returns

- `unnamed_schema_2 = Response`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.agents.sessions.artifacts.content('artifact_id', {
  session_id: 'session_id',
});

console.log(response);

const content = await response.blob();
console.log(content);
```

## Delete an agent session artifact

`client.beta.agents.sessions.artifacts.delete(stringartifactID, ArtifactDeleteParamsparams, RequestOptionsoptions?): SessionArtifactDeleted`

**delete** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Deletes an immutable session artifact without deleting its live environment file or original Files API object. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `artifactID: string`

- `params: ArtifactDeleteParams`

  - `session_id: string`

    The ID of the session that owns the artifact.

### Returns

- `SessionArtifactDeleted`

  Confirmation that an immutable session artifact was deleted.

  - `id: string`

    The ID of the deleted session artifact.

  - `deleted: boolean`

    Whether the session artifact was deleted. Always `true`.

  - `object: "agent.session.artifact.deleted"`

    The object type. Always `agent.session.artifact.deleted`.

    - `"agent.session.artifact.deleted"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const sessionArtifactDeleted = await client.beta.agents.sessions.artifacts.delete('artifact_id', {
  session_id: 'session_id',
});

console.log(sessionArtifactDeleted.id);
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

`client.beta.agents.sessions.artifacts.list(stringsessionID, ArtifactListParamsquery?, RequestOptionsoptions?): CursorPage<SessionArtifact>`

**get** `/agents/sessions/{session_id}/artifacts`

Lists immutable artifacts published by completed hosted session turns. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `sessionID: string`

- `query: ArtifactListParams`

  - `after?: string | null`

    Return artifacts after this immutable artifact ID.

  - `environment_id?: string | null`

    Restrict the listing to artifacts produced by this environment.

  - `limit?: number | null`

    The maximum number of artifacts to return, between 1 and 100.

  - `order?: "asc" | "desc"`

    Sort by creation time and ID. Defaults to descending.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

### Returns

- `SessionArtifact`

  An immutable file published by a completed hosted session turn.

  - `id: string`

    The immutable artifact ID.

  - `created_at: number`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: string`

    The ID of the environment that produced the artifact.

  - `object: "agent.session.artifact"`

    The object type. Always `agent.session.artifact`.

    - `"agent.session.artifact"`

  - `path: string`

    The original absolute file path in the execution environment.

  - `session_id: string`

    The ID of the session that owns the artifact.

  - `size_bytes: number`

    The immutable artifact size in bytes.

  - `turn_id: string`

    The ID of the completed turn that published the artifact.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const sessionArtifact of client.beta.agents.sessions.artifacts.list('session_id')) {
  console.log(sessionArtifact.id);
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

`client.beta.agents.sessions.artifacts.retrieve(stringartifactID, ArtifactRetrieveParamsparams, RequestOptionsoptions?): SessionArtifact`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Retrieves immutable metadata for one durable session artifact. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `artifactID: string`

- `params: ArtifactRetrieveParams`

  - `session_id: string`

    The ID of the session that owns the artifact.

### Returns

- `SessionArtifact`

  An immutable file published by a completed hosted session turn.

  - `id: string`

    The immutable artifact ID.

  - `created_at: number`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: string`

    The ID of the environment that produced the artifact.

  - `object: "agent.session.artifact"`

    The object type. Always `agent.session.artifact`.

    - `"agent.session.artifact"`

  - `path: string`

    The original absolute file path in the execution environment.

  - `session_id: string`

    The ID of the session that owns the artifact.

  - `size_bytes: number`

    The immutable artifact size in bytes.

  - `turn_id: string`

    The ID of the completed turn that published the artifact.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const sessionArtifact = await client.beta.agents.sessions.artifacts.retrieve('artifact_id', {
  session_id: 'session_id',
});

console.log(sessionArtifact.id);
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

- `SessionArtifact`

  An immutable file published by a completed hosted session turn.

  - `id: string`

    The immutable artifact ID.

  - `created_at: number`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: string`

    The ID of the environment that produced the artifact.

  - `object: "agent.session.artifact"`

    The object type. Always `agent.session.artifact`.

    - `"agent.session.artifact"`

  - `path: string`

    The original absolute file path in the execution environment.

  - `session_id: string`

    The ID of the session that owns the artifact.

  - `size_bytes: number`

    The immutable artifact size in bytes.

  - `turn_id: string`

    The ID of the completed turn that published the artifact.

### Session Artifact Deleted

- `SessionArtifactDeleted`

  Confirmation that an immutable session artifact was deleted.

  - `id: string`

    The ID of the deleted session artifact.

  - `deleted: boolean`

    Whether the session artifact was deleted. Always `true`.

  - `object: "agent.session.artifact.deleted"`

    The object type. Always `agent.session.artifact.deleted`.

    - `"agent.session.artifact.deleted"`

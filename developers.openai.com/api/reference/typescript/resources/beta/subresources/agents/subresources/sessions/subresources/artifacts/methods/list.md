<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/list/ -->

## List agent session artifacts

`client.beta.agents.sessions.artifacts.list(stringsessionID, ArtifactListParamsquery?, RequestOptionsoptions?): CursorPage<SessionArtifact>`

**get** `/agents/sessions/{session_id}/artifacts`

Lists immutable artifacts published by completed hosted session turns. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

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

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const sessionArtifact of client.beta.agents.sessions.artifacts.list('session_id')) {
  console.log(sessionArtifact.id);

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

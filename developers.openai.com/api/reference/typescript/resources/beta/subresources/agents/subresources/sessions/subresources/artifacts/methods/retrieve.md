<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/retrieve/ -->

## Retrieve an agent session artifact

`client.beta.agents.sessions.artifacts.retrieve(stringartifactID, ArtifactRetrieveParamsparams, RequestOptionsoptions?): SessionArtifact`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Retrieves immutable metadata for one durable session artifact. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `artifactID: string`

- `params: ArtifactRetrieveParams`

  - `session_id: string`

    The ID of the session that owns the artifact.

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

const sessionArtifact = await client.beta.agents.sessions.artifacts.retrieve('artifact_id', {
  session_id: 'session_id',
});

console.log(sessionArtifact.id);

  "environment_id": "environment_id",
  "object": "agent.session.artifact",
  "path": "path",
  "session_id": "session_id",
  "size_bytes": 0,
  "turn_id": "turn_id"

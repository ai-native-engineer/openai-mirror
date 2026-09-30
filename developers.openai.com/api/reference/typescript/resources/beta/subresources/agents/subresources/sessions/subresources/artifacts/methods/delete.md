<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/delete/ -->

## Delete an agent session artifact

`client.beta.agents.sessions.artifacts.delete(stringartifactID, ArtifactDeleteParamsparams, RequestOptionsoptions?): SessionArtifactDeleted`

**delete** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Deletes an immutable session artifact without deleting its live environment file or original Files API object. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `artifactID: string`

- `params: ArtifactDeleteParams`

  - `session_id: string`

    The ID of the session that owns the artifact.

- `SessionArtifactDeleted`

  Confirmation that an immutable session artifact was deleted.

  - `id: string`

    The ID of the deleted session artifact.

  - `deleted: boolean`

    Whether the session artifact was deleted. Always `true`.

  - `object: "agent.session.artifact.deleted"`

    The object type. Always `agent.session.artifact.deleted`.

    - `"agent.session.artifact.deleted"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const sessionArtifactDeleted = await client.beta.agents.sessions.artifacts.delete('artifact_id', {
  session_id: 'session_id',
});

console.log(sessionArtifactDeleted.id);

  "deleted": true,
  "object": "agent.session.artifact.deleted"

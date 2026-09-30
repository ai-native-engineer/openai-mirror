<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/content/ -->

## Retrieve agent session artifact content

`client.beta.agents.sessions.artifacts.content(stringartifactID, ArtifactContentParamsparams, RequestOptionsoptions?): Response`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}/content`

Downloads immutable session artifact bytes after the execution environment expires. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `artifactID: string`

- `params: ArtifactContentParams`

  - `session_id: string`

    The ID of the session that owns the artifact.

- `unnamed_schema_2 = Response`

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

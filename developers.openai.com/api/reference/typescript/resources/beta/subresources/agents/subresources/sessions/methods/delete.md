<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/sessions/methods/delete/ -->

## Delete an agent session

`client.beta.agents.sessions.delete(stringsessionID, RequestOptionsoptions?): AgentSessionDeleted`

**delete** `/agents/sessions/{session_id}`

Removes a managed agent session from the public API and returns a deletion confirmation. If backend execution has ended, deletion can cancel a still-open public turn and abandon unpublished outputs. Running execution must be cancelled first. Physical cleanup may continue asynchronously. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

- `sessionID: string`

- `AgentSessionDeleted`

  A Managed Agents session removed from the public API. Physical cleanup may continue asynchronously.

  - `id: string`

    The ID of the deleted session.

  - `deleted: boolean`

    Whether the session has been removed from the public API. Always `true`. Physical cleanup may still be in progress.

  - `object: "agent.session.deleted"`

    The object type. Always `agent.session.deleted`.

    - `"agent.session.deleted"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const agentSessionDeleted = await client.beta.agents.sessions.delete('session_id');

console.log(agentSessionDeleted.id);

  "deleted": true,
  "object": "agent.session.deleted"

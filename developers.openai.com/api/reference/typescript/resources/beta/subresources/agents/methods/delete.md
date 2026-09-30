<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/methods/delete/ -->

## Delete an agent

`client.beta.agents.delete(stringagentID, RequestOptionsoptions?): AgentDeleted`

**delete** `/agents/{agent_id}`

Deletes a reusable agent. See [agent configuration](/api/docs/guides/agents-api/configuration).

- `agentID: string`

- `AgentDeleted`

  A deleted reusable agent.

  - `id: string`

    The ID of the deleted agent.

  - `deleted: boolean`

    Whether the agent was deleted. Always `true`.

  - `object: "agent.deleted"`

    The object type. Always `agent.deleted`.

    - `"agent.deleted"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const agentDeleted = await client.beta.agents.delete('agent_id');

console.log(agentDeleted.id);

  "deleted": true,
  "object": "agent.deleted"

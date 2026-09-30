<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/methods/retrieve/ -->

## Retrieve a session subagent

`client.beta.agents.sessions.subagents.retrieve(stringsubagentID, SubagentRetrieveParamsparams, RequestOptionsoptions?): Subagent`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}`

Retrieves a subagent belonging to this session. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

- `subagentID: string`

- `params: SubagentRetrieveParams`

  - `session_id: string`

    The ID of the session.

- `Subagent`

  A subagent created within a session.

  - `id: string`

    The ID of the subagent.

  - `closed_at: number | null`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `instructions: Array<AgentContent> | null`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `OutputText`

      A text content part produced by the agent.

      - `text: string`

        The text produced by the agent.

      - `type: "output_text"`

        The content type. Always `output_text`.

        - `"output_text"`

    - `EncryptedContentResource`

      Encrypted content exchanged between agents.

      - `encrypted_content: string`

        The encrypted content payload.

      - `type: "encrypted_content"`

        The content type. Always `encrypted_content`.

        - `"encrypted_content"`

  - `name: string | null`

    The runner-assigned nickname, or null when unavailable.

  - `object: "agent.session.subagent"`

    The object type. Always `agent.session.subagent`.

    - `"agent.session.subagent"`

  - `opened_at: number`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `parent_agent_id: string`

    The ID of the agent that created this subagent.

  - `session_id: string`

    The ID of the session that owns the subagent.

  - `status: "active" | "closed"`

    The current status of the subagent.

    - `"active"`

      The subagent remains available, including while idle between turns.

    - `"closed"`

      The subagent is closed.

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const subagent = await client.beta.agents.sessions.subagents.retrieve('subagent_id', {
  session_id: 'session_id',
});

console.log(subagent.id);

  "closed_at": 0,
  "instructions": [
      "text": "text",
      "type": "output_text"
  "object": "agent.session.subagent",
  "opened_at": 0,
  "parent_agent_id": "parent_agent_id",
  "session_id": "session_id",
  "status": "active"

<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/methods/retrieve/ -->

## Retrieve a session subagent

`beta.agents.sessions.subagents.retrieve(strsubagent_id, SubagentRetrieveParams**kwargs)  -> Subagent`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}`

Retrieves a subagent belonging to this session. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

- `session_id: str`

- `subagent_id: str`

- `class Subagent: …`

  A subagent created within a session.

  - `id: str`

    The ID of the subagent.

  - `closed_at: Optional[int]`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `instructions: Optional[List[AgentContent]]`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `class OutputText: …`

      A text content part produced by the agent.

      - `text: str`

        The text produced by the agent.

      - `type: Literal["output_text"]`

        The content type. Always `output_text`.

        - `"output_text"`

    - `class EncryptedContentResource: …`

      Encrypted content exchanged between agents.

      - `encrypted_content: str`

        The encrypted content payload.

      - `type: Literal["encrypted_content"]`

        The content type. Always `encrypted_content`.

        - `"encrypted_content"`

  - `name: Optional[str]`

    The runner-assigned nickname, or null when unavailable.

  - `object: Literal["agent.session.subagent"]`

    The object type. Always `agent.session.subagent`.

    - `"agent.session.subagent"`

  - `opened_at: int`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `parent_agent_id: str`

    The ID of the agent that created this subagent.

  - `session_id: str`

    The ID of the session that owns the subagent.

  - `status: Literal["active", "closed"]`

    The current status of the subagent.

    - `"active"`

      The subagent remains available, including while idle between turns.

    - `"closed"`

      The subagent is closed.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
subagent = client.beta.agents.sessions.subagents.retrieve(
    subagent_id="subagent_id",
    session_id="session_id",
print(subagent.id)

  "closed_at": 0,
  "instructions": [
      "text": "text",
      "type": "output_text"
  "object": "agent.session.subagent",
  "opened_at": 0,
  "parent_agent_id": "parent_agent_id",
  "session_id": "session_id",
  "status": "active"

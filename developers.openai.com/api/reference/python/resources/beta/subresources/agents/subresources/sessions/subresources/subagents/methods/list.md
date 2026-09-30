<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/methods/list/ -->

## List session subagents

`beta.agents.sessions.subagents.list(strsession_id, SubagentListParams**kwargs)  -> SyncCursorPage[Subagent]`

**get** `/agents/sessions/{session_id}/subagents`

Lists subagents in a session, including nested and closed subagents. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

- `session_id: str`

- `after: Optional[str]`

  Return resources after this resource ID in the selected order.

- `limit: Optional[int]`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: Optional[Literal["asc", "desc"]]`

  The order in which resources are returned. Defaults to `desc`.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

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
page = client.beta.agents.sessions.subagents.list(
    session_id="session_id",
page = page.data[0]
print(page.id)

  "data": [
      "closed_at": 0,
      "instructions": [
          "text": "text",
          "type": "output_text"
      "object": "agent.session.subagent",
      "opened_at": 0,
      "parent_agent_id": "parent_agent_id",
      "session_id": "session_id",
      "status": "active"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/methods/delete/ -->

## Delete an agent

`beta.agents.delete(stragent_id)  -> AgentDeleted`

**delete** `/agents/{agent_id}`

Deletes a reusable agent. See [agent configuration](/api/docs/guides/agents-api/configuration).

- `agent_id: str`

- `class AgentDeleted: …`

  A deleted reusable agent.

  - `id: str`

    The ID of the deleted agent.

  - `deleted: bool`

    Whether the agent was deleted. Always `true`.

  - `object: Literal["agent.deleted"]`

    The object type. Always `agent.deleted`.

    - `"agent.deleted"`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
agent_deleted = client.beta.agents.delete(
    "agent_id",
print(agent_deleted.id)

  "deleted": true,
  "object": "agent.deleted"

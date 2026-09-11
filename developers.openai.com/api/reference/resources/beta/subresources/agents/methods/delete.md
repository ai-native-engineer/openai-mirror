<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/methods/delete/ -->

# Delete an agent

DELETE/agents/{agent\_id}

Deletes a reusable agent. See [agent configuration](/api/docs/guides/agents-api/configuration).

agent\_id: string

AgentDeleted object { id, deleted, object }

A deleted reusable agent.

The ID of the deleted agent.

deleted: boolean

Whether the agent was deleted. Always `true`.

object: "agent.deleted"

The object type. Always `agent.deleted`.

### Delete an agent

curl https://api.openai.com/v1/agents/$AGENT_ID \
    -X DELETE \

  "deleted": true,
  "object": "agent.deleted"

  "deleted": true,
  "object": "agent.deleted"

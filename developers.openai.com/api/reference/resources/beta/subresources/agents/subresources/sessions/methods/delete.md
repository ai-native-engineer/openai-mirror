<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions/methods/delete/ -->

[Sessions](/api/reference/resources/beta/subresources/agents/subresources/sessions)

# Delete an agent session

DELETE/agents/sessions/{session\_id}

Removes a managed agent session from the public API and returns a deletion confirmation. Physical cleanup may continue asynchronously. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

session\_id: string

AgentSessionDeleted object { id, deleted, object }

A Managed Agents session removed from the public API. Physical cleanup may continue asynchronously.

The ID of the deleted session.

deleted: boolean

Whether the session has been removed from the public API. Always `true`. Physical cleanup may still be in progress.

object: "agent.session.deleted"

The object type. Always `agent.session.deleted`.

### Delete an agent session

curl https://api.openai.com/v1/agents/sessions/$SESSION_ID \
    -X DELETE \

  "deleted": true,
  "object": "agent.session.deleted"

  "deleted": true,
  "object": "agent.session.deleted"

<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/sessions/methods/delete/ -->

## Delete an agent session

`beta.agents.sessions.delete(session_id) -> AgentSessionDeleted`

**delete** `/agents/sessions/{session_id}`

Removes a managed agent session from the public API and returns a deletion confirmation. If backend execution has ended, deletion can cancel a still-open public turn and abandon unpublished outputs. Running execution must be cancelled first. Physical cleanup may continue asynchronously. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

- `session_id: String`

- `class AgentSessionDeleted`

  A Managed Agents session removed from the public API. Physical cleanup may continue asynchronously.

  - `id: String`

    The ID of the deleted session.

  - `deleted: bool`

    Whether the session has been removed from the public API. Always `true`. Physical cleanup may still be in progress.

  - `object: :"agent.session.deleted"`

    The object type. Always `agent.session.deleted`.

    - `:"agent.session.deleted"`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

agent_session_deleted = openai.beta.agents.sessions.delete("session_id")

puts(agent_session_deleted)

  "deleted": true,
  "object": "agent.session.deleted"

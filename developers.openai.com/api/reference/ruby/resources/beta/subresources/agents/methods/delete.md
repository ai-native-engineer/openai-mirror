<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/methods/delete/ -->

## Delete an agent

`beta.agents.delete(agent_id) -> AgentDeleted`

**delete** `/agents/{agent_id}`

Deletes a reusable agent. See [agent configuration](/api/docs/guides/agents-api/configuration).

- `agent_id: String`

- `class AgentDeleted`

  A deleted reusable agent.

  - `id: String`

    The ID of the deleted agent.

  - `deleted: bool`

    Whether the agent was deleted. Always `true`.

  - `object: :"agent.deleted"`

    The object type. Always `agent.deleted`.

    - `:"agent.deleted"`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

agent_deleted = openai.beta.agents.delete("agent_id")

puts(agent_deleted)

  "deleted": true,
  "object": "agent.deleted"

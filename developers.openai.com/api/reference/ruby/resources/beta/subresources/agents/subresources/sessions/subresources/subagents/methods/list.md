<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/methods/list/ -->

## List session subagents

`beta.agents.sessions.subagents.list(session_id, **kwargs) -> CursorPage<Subagent>`

**get** `/agents/sessions/{session_id}/subagents`

Lists subagents in a session, including nested and closed subagents. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

- `session_id: String`

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

- `class Subagent`

  A subagent created within a session.

  - `id: String`

    The ID of the subagent.

  - `closed_at: Integer`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `instructions: Array[AgentContent]`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `class OutputText`

      A text content part produced by the agent.

      - `text: String`

        The text produced by the agent.

      - `type: :output_text`

        The content type. Always `output_text`.

        - `:output_text`

    - `class EncryptedContent`

      Encrypted content exchanged between agents.

      - `encrypted_content: String`

        The encrypted content payload.

      - `type: :encrypted_content`

        The content type. Always `encrypted_content`.

        - `:encrypted_content`

  - `name: String`

    The runner-assigned nickname, or null when unavailable.

  - `object: :"agent.session.subagent"`

    The object type. Always `agent.session.subagent`.

    - `:"agent.session.subagent"`

  - `opened_at: Integer`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `parent_agent_id: String`

    The ID of the agent that created this subagent.

  - `session_id: String`

    The ID of the session that owns the subagent.

  - `status: :active | :closed`

    The current status of the subagent.

    - `:active`

      The subagent remains available, including while idle between turns.

    - `:closed`

      The subagent is closed.

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.subagents.list("session_id")

puts(page)

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

<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/methods/retrieve/ -->

## Retrieve a session subagent

`beta.agents.sessions.subagents.retrieve(subagent_id, **kwargs) -> Subagent`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}`

Retrieves a subagent belonging to this session. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

- `session_id: String`

- `subagent_id: String`

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

subagent = openai.beta.agents.sessions.subagents.retrieve("subagent_id", session_id: "session_id")

puts(subagent)

  "closed_at": 0,
  "instructions": [
      "text": "text",
      "type": "output_text"
  "object": "agent.session.subagent",
  "opened_at": 0,
  "parent_agent_id": "parent_agent_id",
  "session_id": "session_id",
  "status": "active"

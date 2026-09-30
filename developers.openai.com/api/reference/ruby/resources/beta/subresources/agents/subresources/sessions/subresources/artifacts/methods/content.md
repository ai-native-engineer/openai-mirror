<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/content/ -->

## Retrieve agent session artifact content

`beta.agents.sessions.artifacts.content(artifact_id, **kwargs) -> StringIO`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}/content`

Downloads immutable session artifact bytes after the execution environment expires. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `session_id: String`

- `artifact_id: String`

- `StringIO`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

response = openai.beta.agents.sessions.artifacts.content("artifact_id", session_id: "session_id")

puts(response)

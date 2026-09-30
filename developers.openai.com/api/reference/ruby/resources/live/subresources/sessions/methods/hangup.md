<!-- source: https://developers.openai.com/api/reference/ruby/resources/live/subresources/sessions/methods/hangup/ -->

## Hang up session

`live.sessions.hangup(session_id) -> void`

**post** `/live/sessions/{session_id}/hangup`

End a SIP call identified by session_id.

- `session_id: String`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

result = openai.live.sessions.hangup("session_id")

puts(result)

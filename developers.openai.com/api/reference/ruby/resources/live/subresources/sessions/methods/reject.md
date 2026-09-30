<!-- source: https://developers.openai.com/api/reference/ruby/resources/live/subresources/sessions/methods/reject/ -->

## Reject call

`live.sessions.reject(session_id, **kwargs) -> void`

**post** `/live/sessions/{session_id}/reject`

Reject an incoming SIP call. Send a required SIP rejection status_code between 300 and 699.

- `session_id: String`

- `status_code: Integer`

  SIP rejection status sent to the caller. This field is required.

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

result = openai.live.sessions.reject("session_id", status_code: 486)

puts(result)

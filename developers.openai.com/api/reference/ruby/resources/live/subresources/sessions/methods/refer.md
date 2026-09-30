<!-- source: https://developers.openai.com/api/reference/ruby/resources/live/subresources/sessions/methods/refer/ -->

## Transfer call

`live.sessions.refer(session_id, **kwargs) -> void`

**post** `/live/sessions/{session_id}/refer`

Transfer a SIP call to another destination. Supply a nonblank target_uri for the SIP Refer-To header.

- `session_id: String`

- `target_uri: String`

  Nonblank URI for the SIP Refer-To header, such as tel:+14155550123 or sip:agent@example.com.

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

result = openai.live.sessions.refer("session_id", target_uri: "tel:+14155550123")

puts(result)

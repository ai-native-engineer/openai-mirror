<!-- source: https://developers.openai.com/api/reference/ruby/resources/live/subresources/sessions/methods/download_recording/ -->

## Download recording

`live.sessions.download_recording(session_id) -> StringIO`

**get** `/live/sessions/{session_id}/content`

Get Live session content

- `session_id: String`

  The ID of the stored Live session to download. Use the session ID returned when the session started with storage enabled.

- `StringIO`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

response = openai.live.sessions.download_recording("live_SQ")

puts(response)

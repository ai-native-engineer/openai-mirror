<!-- source: https://developers.openai.com/api/reference/ruby/resources/realtime/subresources/translations/methods/connect/ -->

## Connect

Open a Realtime translation session. The WebSocket URL requires a `model` query parameter.

**WebSocket** `wss://api.openai.com/v1/realtime/translations`

```ruby
require "openai"
require "async"
require "base64"

# input.pcm: a short recording of raw 24 kHz mono PCM16 little-endian audio.
Sync do |task|
  task.with_timeout(60) do
    client = OpenAI::Client.new
    client.realtime.connect_translation(model: "gpt-realtime-translate") do |connection|
      connection.send_event(
        type: "session.update", session: { audio: { output: { language: "es" } } }
      # Wait for the new language before sending audio.
      loop do
        event = connection.receive
        raise "WebSocket closed before session.updated" unless event
        raise "Translation error: #{event.error.message}" if event.type.to_s == "error"
        raise "Translation closed before session.updated" if event.type.to_s == "session.closed"
        break if event.type.to_s == "session.updated"
      end
      File.open("input.pcm", "rb") do |audio|
        while (chunk = audio.read(9600)) # 200 ms of PCM16
          connection.send_event(
            type: "session.input_audio_buffer.append",
            audio: Base64.strict_encode64(chunk)
        end
      end
      # finish sends session.close and yields trailing text until session.closed.
      connection.finish(timeout: 10) do |event|
        case event.type.to_s
        when "session.output_transcript.delta"
          print event.delta
        when "error"
          raise "Translation error: #{event.error.message}"
        end
      end
    end
  end
end

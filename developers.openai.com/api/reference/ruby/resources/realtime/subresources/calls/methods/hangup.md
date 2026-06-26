<!-- source: https://developers.openai.com/api/reference/ruby/resources/realtime/subresources/calls/methods/hangup/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Realtime](/api/reference/ruby/resources/realtime)

[Calls](/api/reference/ruby/resources/realtime/subresources/calls)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Hang up call

realtime.calls.hangup(call\_id) -> void

POST/realtime/calls/{call\_id}/hangup

End an active Realtime API call, whether it was initiated over SIP or
WebRTC.

##### ParametersExpand Collapse

call\_id: String

### Hang up call

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

result = openai.realtime.calls.hangup("call_id")

puts(result)

##### Returns Examples

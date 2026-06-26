<!-- source: https://developers.openai.com/api/reference/ruby/resources/realtime/subresources/calls/methods/refer/ -->

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

# Refer call

realtime.calls.refer(call\_id, \*\*kwargs) -> void

POST/realtime/calls/{call\_id}/refer

Transfer an active SIP call to a new destination using the SIP REFER verb.

##### ParametersExpand Collapse

call\_id: String

target\_uri: String

URI that should appear in the SIP Refer-To header. Supports values like
`tel:+14155550123` or `sip:agent@example.com`.

### Refer call

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

result = openai.realtime.calls.refer("call_id", target_uri: "tel:+14155550123")

puts(result)

##### Returns Examples

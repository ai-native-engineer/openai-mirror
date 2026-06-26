<!-- source: https://developers.openai.com/api/reference/ruby/resources/realtime/subresources/calls/methods/reject/ -->

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

# Reject call

realtime.calls.reject(call\_id, \*\*kwargs) -> void

POST/realtime/calls/{call\_id}/reject

Decline an incoming SIP call by returning a SIP status code to the caller.

##### ParametersExpand Collapse

call\_id: String

status\_code: Integer

SIP response code to send back to the caller. Defaults to `603` (Decline)
when omitted.

### Reject call

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

result = openai.realtime.calls.reject("call_id")

puts(result)

##### Returns Examples

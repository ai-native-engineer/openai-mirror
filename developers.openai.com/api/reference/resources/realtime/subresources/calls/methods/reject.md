<!-- source: https://developers.openai.com/api/reference/resources/realtime/subresources/calls/methods/reject/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Realtime](/api/reference/resources/realtime)

[Calls](/api/reference/resources/realtime/subresources/calls)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Reject call

POST/realtime/calls/{call\_id}/reject

Decline an incoming SIP call by returning a SIP status code to the caller.

##### Path ParametersExpand Collapse

call\_id: string

##### Body ParametersJSONExpand Collapse

status\_code: optional number

SIP response code to send back to the caller. Defaults to `603` (Decline)
when omitted.

### Reject call

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X POST https://api.openai.com/v1/realtime/calls/$CALL_ID/reject \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"status_code": 486}'

##### Returns Examples

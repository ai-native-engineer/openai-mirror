<!-- source: https://developers.openai.com/api/reference/cli/resources/realtime/subresources/calls/methods/reject/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Realtime](/api/reference/cli/resources/realtime)

[Calls](/api/reference/cli/resources/realtime/subresources/calls)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Reject call

$ openai realtime:calls reject

POST/realtime/calls/{call\_id}/reject

Decline an incoming SIP call by returning a SIP status code to the caller.

##### ParametersExpand Collapse

--call-id: string

The identifier for the call provided in the
[`realtime.call.incoming`](https://platform.openai.com/docs/api-reference/webhook-events/realtime/call/incoming)
webhook.

--status-code: optional number

SIP response code to send back to the caller. Defaults to `603` (Decline)
when omitted.

### Reject call

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai realtime:calls reject \
  --api-key 'My API Key' \
  --call-id call_id

##### Returns Examples

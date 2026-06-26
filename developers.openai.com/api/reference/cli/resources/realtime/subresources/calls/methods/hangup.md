<!-- source: https://developers.openai.com/api/reference/cli/resources/realtime/subresources/calls/methods/hangup/ -->

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

# Hang up call

$ openai realtime:calls hangup

POST/realtime/calls/{call\_id}/hangup

End an active Realtime API call, whether it was initiated over SIP or
WebRTC.

##### ParametersExpand Collapse

--call-id: string

The identifier for the call. For SIP calls, use the value provided in the
[`realtime.call.incoming`](https://platform.openai.com/docs/api-reference/webhook-events/realtime/call/incoming)
webhook. For WebRTC sessions, reuse the call ID returned in the `Location`
header when creating the call with
[`POST /v1/realtime/calls`](https://platform.openai.com/docs/api-reference/realtime/create-call).

### Hang up call

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai realtime:calls hangup \
  --api-key 'My API Key' \
  --call-id call_id

##### Returns Examples

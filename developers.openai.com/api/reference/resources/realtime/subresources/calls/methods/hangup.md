<!-- source: https://developers.openai.com/api/reference/resources/realtime/subresources/calls/methods/hangup/ -->

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

# Hang up call

POST/realtime/calls/{call\_id}/hangup

End an active Realtime API call, whether it was initiated over SIP or
WebRTC.

##### Path ParametersExpand Collapse

call\_id: string

### Hang up call

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X POST https://api.openai.com/v1/realtime/calls/$CALL_ID/hangup \
  -H "Authorization: Bearer $OPENAI_API_KEY"

##### Returns Examples

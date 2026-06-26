<!-- source: https://developers.openai.com/api/reference/resources/realtime/subresources/calls/methods/refer/ -->

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

# Refer call

POST/realtime/calls/{call\_id}/refer

Transfer an active SIP call to a new destination using the SIP REFER verb.

##### Path ParametersExpand Collapse

call\_id: string

##### Body ParametersJSONExpand Collapse

target\_uri: string

URI that should appear in the SIP Refer-To header. Supports values like
`tel:+14155550123` or `sip:agent@example.com`.

### Refer call

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X POST https://api.openai.com/v1/realtime/calls/$CALL_ID/refer \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target_uri": "tel:+14155550123"}'

##### Returns Examples

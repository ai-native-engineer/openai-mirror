<!-- source: https://developers.openai.com/api/reference/cli/resources/realtime/subresources/calls/methods/refer/ -->

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

# Refer call

$ openai realtime:calls refer

POST/realtime/calls/{call\_id}/refer

Transfer an active SIP call to a new destination using the SIP REFER verb.

##### ParametersExpand Collapse

--call-id: string

The identifier for the call provided in the
[`realtime.call.incoming`](https://platform.openai.com/docs/api-reference/webhook-events/realtime/call/incoming)
webhook.

--target-uri: string

URI that should appear in the SIP Refer-To header. Supports values like
`tel:+14155550123` or `sip:agent@example.com`.

### Refer call

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai realtime:calls refer \
  --api-key 'My API Key' \
  --call-id call_id \
  --target-uri tel:+14155550123

##### Returns Examples

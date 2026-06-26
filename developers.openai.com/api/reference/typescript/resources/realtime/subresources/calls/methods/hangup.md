<!-- source: https://developers.openai.com/api/reference/typescript/resources/realtime/subresources/calls/methods/hangup/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Realtime](/api/reference/typescript/resources/realtime)

[Calls](/api/reference/typescript/resources/realtime/subresources/calls)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Hang up call

client.realtime.calls.hangup(stringcallID, RequestOptionsoptions?): void

POST/realtime/calls/{call\_id}/hangup

End an active Realtime API call, whether it was initiated over SIP or
WebRTC.

##### ParametersExpand Collapse

callID: string

### Hang up call

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted

await client.realtime.calls.hangup('call_id');

##### Returns Examples

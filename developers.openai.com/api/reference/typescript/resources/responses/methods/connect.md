<!-- source: https://developers.openai.com/api/reference/typescript/resources/responses/methods/connect/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Responses](/api/reference/typescript/resources/responses)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Connect

client.responses.connect(RequestOptionsoptions?): void

Function

Connect to a persistent Responses API WebSocket. Send `response.create` events and receive response stream events over the socket.

### Connect

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

await client.responses.connect();

##### Returns Examples

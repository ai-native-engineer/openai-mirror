<!-- source: https://developers.openai.com/api/reference/python/resources/responses/methods/connect/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Responses](/api/reference/python/resources/responses)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Connect

responses.connect()

Function

Connect to a persistent Responses API WebSocket. Send `response.create` events and receive response stream events over the socket.

### Connect

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
client.responses.connect()

##### Returns Examples

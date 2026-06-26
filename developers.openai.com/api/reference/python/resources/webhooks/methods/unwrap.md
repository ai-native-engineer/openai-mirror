<!-- source: https://developers.openai.com/api/reference/python/resources/webhooks/methods/unwrap/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Webhooks](/api/reference/python/resources/webhooks)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Unwrap

webhooks.unwrap()

Function

Validates that the given payload was sent by OpenAI and parses the payload.

### Unwrap

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
client.webhooks.unwrap()

##### Returns Examples

<!-- source: https://developers.openai.com/api/reference/python/resources/realtime/subresources/calls/methods/reject/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Realtime](/api/reference/python/resources/realtime)

[Calls](/api/reference/python/resources/realtime/subresources/calls)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Reject call

realtime.calls.reject(strcall\_id, CallRejectParams\*\*kwargs)

POST/realtime/calls/{call\_id}/reject

Decline an incoming SIP call by returning a SIP status code to the caller.

##### ParametersExpand Collapse

call\_id: str

status\_code: Optional[int]

SIP response code to send back to the caller. Defaults to `603` (Decline)
when omitted.

### Reject call

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
client.realtime.calls.reject(
    call_id="call_id",

##### Returns Examples

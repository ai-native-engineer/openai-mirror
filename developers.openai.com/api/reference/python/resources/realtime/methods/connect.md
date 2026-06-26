<!-- source: https://developers.openai.com/api/reference/python/resources/realtime/methods/connect/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Realtime](/api/reference/python/resources/realtime)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Connect

realtime.connect(RealtimeConnectParams\*\*kwargs)

Function

The Realtime API enables you to build low-latency, multi-modal conversational experiences. It currently supports text and audio as both input and output, as well as function calling.

Some notable benefits of the API include:

* Native speech-to-speech: Skipping an intermediate text format means low latency and nuanced output.
* Natural, steerable voices: The models have natural inflection and can laugh, whisper, and adhere to tone direction.
* Simultaneous multimodal output: Text is useful for moderation; faster-than-realtime audio ensures stable playback.

The Realtime API is a stateful, event-based API that communicates over a WebSocket.

##### ParametersExpand Collapse

call\_id: Optional[str]

model: Optional[str]

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
client.realtime.connect()

##### Returns Examples

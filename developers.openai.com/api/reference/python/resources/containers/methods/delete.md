<!-- source: https://developers.openai.com/api/reference/python/resources/containers/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Containers](/api/reference/python/resources/containers)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a container

containers.delete(strcontainer\_id)

DELETE/containers/{container\_id}

Delete Container

##### ParametersExpand Collapse

container\_id: str

### Delete a container

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
client.containers.delete(
    "container_id",

    "id": "cntr_682dfebaacac8198bbfe9c2474fb6f4a085685cbe3cb5863",
    "object": "container.deleted",
    "deleted": true

##### Returns Examples

    "id": "cntr_682dfebaacac8198bbfe9c2474fb6f4a085685cbe3cb5863",
    "object": "container.deleted",
    "deleted": true

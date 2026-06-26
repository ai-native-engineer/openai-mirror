<!-- source: https://developers.openai.com/api/reference/python/resources/containers/subresources/files/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Containers](/api/reference/python/resources/containers)

[Files](/api/reference/python/resources/containers/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a container file

containers.files.delete(strfile\_id, FileDeleteParams\*\*kwargs)

DELETE/containers/{container\_id}/files/{file\_id}

Delete Container File

##### ParametersExpand Collapse

container\_id: str

file\_id: str

### Delete a container file

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
client.containers.files.delete(
    file_id="file_id",
    container_id="container_id",

    "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "object": "container.file.deleted",
    "deleted": true

##### Returns Examples

    "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "object": "container.file.deleted",
    "deleted": true

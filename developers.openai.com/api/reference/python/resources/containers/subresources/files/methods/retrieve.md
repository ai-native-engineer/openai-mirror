<!-- source: https://developers.openai.com/api/reference/python/resources/containers/subresources/files/methods/retrieve/ -->

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

# Retrieve container file

containers.files.retrieve(strfile\_id, FileRetrieveParams\*\*kwargs)  -> [FileRetrieveResponse](/api/reference/python/resources/containers#(resource)%20containers.files%20%3E%20(model)%20file_retrieve_response%20%3E%20(schema))

GET/containers/{container\_id}/files/{file\_id}

Retrieve Container File

##### ParametersExpand Collapse

container\_id: str

file\_id: str

##### ReturnsExpand Collapse

class FileRetrieveResponse: …

id: str

Unique identifier for the file.

bytes: int

Size of the file in bytes.

container\_id: str

The container this file belongs to.

created\_at: int

Unix timestamp (in seconds) when the file was created.

formatunixtime

object: Literal["container.file"]

The type of this object (`container.file`).

path: str

Path of the file in the container.

source: str

Source of the file (e.g., `user`, `assistant`).

### Retrieve container file

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
file = client.containers.files.retrieve(
    file_id="file_id",
    container_id="container_id",
print(file.id)

    "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "object": "container.file",
    "created_at": 1747848842,
    "bytes": 880,
    "container_id": "cntr_682e0e7318108198aa783fd921ff305e08e78805b9fdbb04",
    "path": "/mnt/data/88e12fa445d32636f190a0b33daed6cb-tsconfig.json",
    "source": "user"

##### Returns Examples

    "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "object": "container.file",
    "created_at": 1747848842,
    "bytes": 880,
    "container_id": "cntr_682e0e7318108198aa783fd921ff305e08e78805b9fdbb04",
    "path": "/mnt/data/88e12fa445d32636f190a0b33daed6cb-tsconfig.json",
    "source": "user"

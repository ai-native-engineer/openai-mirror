<!-- source: https://developers.openai.com/api/reference/python/resources/containers/subresources/files/methods/list/ -->

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

# List container files

containers.files.list(strcontainer\_id, FileListParams\*\*kwargs)  -> SyncCursorPage[[FileListResponse](/api/reference/python/resources/containers#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema))]

GET/containers/{container\_id}/files

List Container files

##### ParametersExpand Collapse

container\_id: str

after: Optional[str]

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

limit: Optional[int]

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

order: Optional[Literal["asc", "desc"]]

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

class FileListResponse: …

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

### List container files

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
page = client.containers.files.list(
    container_id="container_id",
page = page.data[0]
print(page.id)

    "object": "list",
    "data": [
            "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
            "object": "container.file",
            "created_at": 1747848842,
            "bytes": 880,
            "container_id": "cntr_682e0e7318108198aa783fd921ff305e08e78805b9fdbb04",
            "path": "/mnt/data/88e12fa445d32636f190a0b33daed6cb-tsconfig.json",
            "source": "user"
    ],
    "first_id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "has_more": false,
    "last_id": "cfile_682e0e8a43c88191a7978f477a09bdf5"

##### Returns Examples

    "object": "list",
    "data": [
            "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
            "object": "container.file",
            "created_at": 1747848842,
            "bytes": 880,
            "container_id": "cntr_682e0e7318108198aa783fd921ff305e08e78805b9fdbb04",
            "path": "/mnt/data/88e12fa445d32636f190a0b33daed6cb-tsconfig.json",
            "source": "user"
    ],
    "first_id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "has_more": false,
    "last_id": "cfile_682e0e8a43c88191a7978f477a09bdf5"

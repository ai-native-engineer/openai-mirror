<!-- source: https://developers.openai.com/api/reference/ruby/resources/containers/subresources/files/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Containers](/api/reference/ruby/resources/containers)

[Files](/api/reference/ruby/resources/containers/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List container files

containers.files.list(container\_id, \*\*kwargs) -> CursorPage<[FileListResponse](/api/reference/ruby/resources/containers#(resource)%20containers.files%20%3E%20(model)%20file_list_response%20%3E%20(schema)) { id, bytes, container\_id, 4 more } >

GET/containers/{container\_id}/files

List Container files

##### ParametersExpand Collapse

container\_id: String

after: String

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

limit: Integer

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

order: :asc | :desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

One of the following:

:asc

:desc

##### ReturnsExpand Collapse

class FileListResponse { id, bytes, container\_id, 4 more }

id: String

Unique identifier for the file.

bytes: Integer

Size of the file in bytes.

container\_id: String

The container this file belongs to.

created\_at: Integer

Unix timestamp (in seconds) when the file was created.

formatunixtime

object: :"container.file"

The type of this object (`container.file`).

path: String

Path of the file in the container.

source: String

Source of the file (e.g., `user`, `assistant`).

### List container files

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.containers.files.list("container_id")

puts(page)

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

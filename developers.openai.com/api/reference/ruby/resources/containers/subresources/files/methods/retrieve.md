<!-- source: https://developers.openai.com/api/reference/ruby/resources/containers/subresources/files/methods/retrieve/ -->

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

# Retrieve container file

containers.files.retrieve(file\_id, \*\*kwargs) -> [FileRetrieveResponse](/api/reference/ruby/resources/containers#(resource)%20containers.files%20%3E%20(model)%20file_retrieve_response%20%3E%20(schema)) { id, bytes, container\_id, 4 more }

GET/containers/{container\_id}/files/{file\_id}

Retrieve Container File

##### ParametersExpand Collapse

container\_id: String

file\_id: String

##### ReturnsExpand Collapse

class FileRetrieveResponse { id, bytes, container\_id, 4 more }

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

### Retrieve container file

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

file = openai.containers.files.retrieve("file_id", container_id: "container_id")

puts(file)

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

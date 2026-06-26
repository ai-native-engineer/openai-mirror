<!-- source: https://developers.openai.com/api/reference/cli/resources/containers/subresources/files/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Containers](/api/reference/cli/resources/containers)

[Files](/api/reference/cli/resources/containers/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create container file

$ openai containers:files create

POST/containers/{container\_id}/files

Create a Container File

You can send either a multipart/form-data request with the raw file content, or a JSON request with a file ID.

##### ParametersExpand Collapse

--container-id: string

--file: optional file path

The File object (not file name) to be uploaded.

--file-id: optional string

Name of the file to create.

##### ReturnsExpand Collapse

ContainerFileNewResponse: object { id, bytes, container\_id, 4 more }

id: string

Unique identifier for the file.

bytes: number

Size of the file in bytes.

container\_id: string

The container this file belongs to.

created\_at: number

Unix timestamp (in seconds) when the file was created.

object: "container.file"

The type of this object (`container.file`).

path: string

Path of the file in the container.

source: string

Source of the file (e.g., `user`, `assistant`).

### Create container file

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai containers:files create \
  --api-key 'My API Key' \
  --container-id container_id

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

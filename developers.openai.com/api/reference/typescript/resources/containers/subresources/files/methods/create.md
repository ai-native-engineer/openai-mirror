<!-- source: https://developers.openai.com/api/reference/typescript/resources/containers/subresources/files/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Containers](/api/reference/typescript/resources/containers)

[Files](/api/reference/typescript/resources/containers/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create container file

client.containers.files.create(stringcontainerID, FileCreateParams { file, file\_id } body, RequestOptionsoptions?): [FileCreateResponse](/api/reference/typescript/resources/containers#(resource)%20containers.files%20%3E%20(model)%20file_create_response%20%3E%20(schema)) { id, bytes, container\_id, 4 more }

POST/containers/{container\_id}/files

Create a Container File

You can send either a multipart/form-data request with the raw file content, or a JSON request with a file ID.

##### ParametersExpand Collapse

containerID: string

body: FileCreateParams { file, file\_id }

file?: [Uploadable](/api/reference/typescript/resources/containers/subresources/files/methods/create#(resource)%20containers.files%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20file%20%3E%20(schema))

The File object (not file name) to be uploaded.

file\_id?: string

Name of the file to create.

##### ReturnsExpand Collapse

FileCreateResponse { id, bytes, container\_id, 4 more }

id: string

Unique identifier for the file.

bytes: number

Size of the file in bytes.

container\_id: string

The container this file belongs to.

created\_at: number

Unix timestamp (in seconds) when the file was created.

formatunixtime

object: "container.file"

The type of this object (`container.file`).

path: string

Path of the file in the container.

source: string

Source of the file (e.g., `user`, `assistant`).

### Create container file

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import fs from 'fs';
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted

const file = await client.containers.files.create('container_id');

console.log(file.id);

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

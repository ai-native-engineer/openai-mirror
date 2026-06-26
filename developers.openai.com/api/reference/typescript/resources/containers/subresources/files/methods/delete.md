<!-- source: https://developers.openai.com/api/reference/typescript/resources/containers/subresources/files/methods/delete/ -->

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

# Delete a container file

client.containers.files.delete(stringfileID, FileDeleteParams { container\_id } params, RequestOptionsoptions?): void

DELETE/containers/{container\_id}/files/{file\_id}

Delete Container File

##### ParametersExpand Collapse

fileID: string

params: FileDeleteParams { container\_id }

container\_id: string

### Delete a container file

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted

await client.containers.files.delete('file_id', { container_id: 'container_id' });

    "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "object": "container.file.deleted",
    "deleted": true

##### Returns Examples

    "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "object": "container.file.deleted",
    "deleted": true

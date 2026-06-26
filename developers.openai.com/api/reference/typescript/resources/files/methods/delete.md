<!-- source: https://developers.openai.com/api/reference/typescript/resources/files/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Files](/api/reference/typescript/resources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete file

client.files.delete(stringfileID, RequestOptionsoptions?): [FileDeleted](/api/reference/typescript/resources/files#(resource)%20files%20%3E%20(model)%20file_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/files/{file\_id}

Delete a file and remove it from all vector stores.

##### ParametersExpand Collapse

fileID: string

##### ReturnsExpand Collapse

FileDeleted { id, deleted, object }

id: string

deleted: boolean

object: "file"

### Delete file

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const file = await openai.files.delete("file-abc123");

  console.log(file);

main();

  "id": "file-abc123",
  "object": "file",
  "deleted": true

##### Returns Examples

  "id": "file-abc123",
  "object": "file",
  "deleted": true

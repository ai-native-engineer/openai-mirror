<!-- source: https://developers.openai.com/api/reference/typescript/resources/vector_stores/subresources/files/methods/content/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Vector Stores](/api/reference/typescript/resources/vector_stores)

[Files](/api/reference/typescript/resources/vector_stores/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve vector store file content

client.vectorStores.files.content(stringfileID, FileContentParams { vector\_store\_id } params, RequestOptionsoptions?): Page<[FileContentResponse](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20file_content_response%20%3E%20(schema)) { text, type } >

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}/content

Retrieve the parsed contents of a vector store file.

##### ParametersExpand Collapse

fileID: string

params: FileContentParams { vector\_store\_id }

vector\_store\_id: string

The ID of the vector store.

##### ReturnsExpand Collapse

FileContentResponse { text, type }

text?: string

The text content

type?: string

The content type (currently only `"text"`)

### Retrieve vector store file content

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

// Automatically fetches more pages as needed.
for await (const fileContentResponse of client.vectorStores.files.content('file-abc123', {
  vector_store_id: 'vs_abc123',
})) {
  console.log(fileContentResponse.text);

  "file_id": "file-abc123",
  "filename": "example.txt",
  "attributes": {"key": "value"},
  "content": [
    {"type": "text", "text": "..."},
    ...
  ]

##### Returns Examples

  "file_id": "file-abc123",
  "filename": "example.txt",
  "attributes": {"key": "value"},
  "content": [
    {"type": "text", "text": "..."},
    ...
  ]

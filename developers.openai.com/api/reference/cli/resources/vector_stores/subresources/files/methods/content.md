<!-- source: https://developers.openai.com/api/reference/cli/resources/vector_stores/subresources/files/methods/content/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Vector Stores](/api/reference/cli/resources/vector_stores)

[Files](/api/reference/cli/resources/vector_stores/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve vector store file content

$ openai vector-stores:files content

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}/content

Retrieve the parsed contents of a vector store file.

##### ParametersExpand Collapse

--vector-store-id: string

The ID of the vector store.

--file-id: string

The ID of the file within the vector store.

##### ReturnsExpand Collapse

VectorStoreFileContentResponse: object { data, has\_more, next\_page, object }

Represents the parsed content of a vector store file.

data: array of object { text, type }

Parsed content of the file.

text: optional string

The text content

type: optional string

The content type (currently only `"text"`)

has\_more: boolean

Indicates if there are more content pages to fetch.

next\_page: string

The token for the next page, if any.

object: "vector\_store.file\_content.page"

The object type, which is always `vector_store.file_content.page`

### Retrieve vector store file content

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai vector-stores:files content \
  --api-key 'My API Key' \
  --vector-store-id vs_abc123 \
  --file-id file-abc123

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

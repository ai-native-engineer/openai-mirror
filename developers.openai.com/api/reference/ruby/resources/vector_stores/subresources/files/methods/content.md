<!-- source: https://developers.openai.com/api/reference/ruby/resources/vector_stores/subresources/files/methods/content/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Vector Stores](/api/reference/ruby/resources/vector_stores)

[Files](/api/reference/ruby/resources/vector_stores/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve vector store file content

vector\_stores.files.content(file\_id, \*\*kwargs) -> Page<[FileContentResponse](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20file_content_response%20%3E%20(schema)) { text, type } >

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}/content

Retrieve the parsed contents of a vector store file.

##### ParametersExpand Collapse

vector\_store\_id: String

file\_id: String

##### ReturnsExpand Collapse

class FileContentResponse { text, type }

text: String

The text content

type: String

The content type (currently only `"text"`)

### Retrieve vector store file content

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

page = openai.vector_stores.files.content("file-abc123", vector_store_id: "vs_abc123")

puts(page)

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

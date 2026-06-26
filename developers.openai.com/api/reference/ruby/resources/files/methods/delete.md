<!-- source: https://developers.openai.com/api/reference/ruby/resources/files/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Files](/api/reference/ruby/resources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete file

files.delete(file\_id) -> [FileDeleted](/api/reference/ruby/resources/files#(resource)%20files%20%3E%20(model)%20file_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/files/{file\_id}

Delete a file and remove it from all vector stores.

##### ParametersExpand Collapse

file\_id: String

##### ReturnsExpand Collapse

class FileDeleted { id, deleted, object }

id: String

deleted: bool

object: :file

### Delete file

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

file_deleted = openai.files.delete("file_id")

puts(file_deleted)

  "id": "file-abc123",
  "object": "file",
  "deleted": true

##### Returns Examples

  "id": "file-abc123",
  "object": "file",
  "deleted": true

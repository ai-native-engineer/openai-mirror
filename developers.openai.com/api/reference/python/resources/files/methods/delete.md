<!-- source: https://developers.openai.com/api/reference/python/resources/files/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Files](/api/reference/python/resources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete file

files.delete(strfile\_id)  -> [FileDeleted](/api/reference/python/resources/files#(resource)%20files%20%3E%20(model)%20file_deleted%20%3E%20(schema))

DELETE/files/{file\_id}

Delete a file and remove it from all vector stores.

##### ParametersExpand Collapse

file\_id: str

##### ReturnsExpand Collapse

class FileDeleted: …

id: str

deleted: bool

object: Literal["file"]

### Delete file

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI
client = OpenAI()

client.files.delete("file-abc123")

  "id": "file-abc123",
  "object": "file",
  "deleted": true

##### Returns Examples

  "id": "file-abc123",
  "object": "file",
  "deleted": true

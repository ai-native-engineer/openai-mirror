<!-- source: https://developers.openai.com/api/reference/resources/files/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Files](/api/reference/resources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete file

DELETE/files/{file\_id}

Delete a file and remove it from all vector stores.

##### Path ParametersExpand Collapse

file\_id: string

##### ReturnsExpand Collapse

FileDeleted object { id, deleted, object }

id: string

deleted: boolean

object: "file"

### Delete file

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/files/file-abc123 \
  -X DELETE \
  -H "Authorization: Bearer $OPENAI_API_KEY"

  "id": "file-abc123",
  "object": "file",
  "deleted": true

##### Returns Examples

  "id": "file-abc123",
  "object": "file",
  "deleted": true

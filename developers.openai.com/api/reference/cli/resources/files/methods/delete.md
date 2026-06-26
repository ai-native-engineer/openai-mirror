<!-- source: https://developers.openai.com/api/reference/cli/resources/files/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Files](/api/reference/cli/resources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete file

$ openai files delete

DELETE/files/{file\_id}

Delete a file and remove it from all vector stores.

##### ParametersExpand Collapse

--file-id: string

The ID of the file to use for this request.

##### ReturnsExpand Collapse

file\_deleted: object { id, deleted, object }

id: string

deleted: boolean

object: "file"

### Delete file

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai files delete \
  --api-key 'My API Key' \
  --file-id file_id

  "id": "file-abc123",
  "object": "file",
  "deleted": true

##### Returns Examples

  "id": "file-abc123",
  "object": "file",
  "deleted": true

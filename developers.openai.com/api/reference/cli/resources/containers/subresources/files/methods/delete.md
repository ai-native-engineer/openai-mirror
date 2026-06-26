<!-- source: https://developers.openai.com/api/reference/cli/resources/containers/subresources/files/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Containers](/api/reference/cli/resources/containers)

[Files](/api/reference/cli/resources/containers/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a container file

$ openai containers:files delete

DELETE/containers/{container\_id}/files/{file\_id}

Delete Container File

##### ParametersExpand Collapse

--container-id: string

--file-id: string

### Delete a container file

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai containers:files delete \
  --api-key 'My API Key' \
  --container-id container_id \
  --file-id file_id

    "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "object": "container.file.deleted",
    "deleted": true

##### Returns Examples

    "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "object": "container.file.deleted",
    "deleted": true

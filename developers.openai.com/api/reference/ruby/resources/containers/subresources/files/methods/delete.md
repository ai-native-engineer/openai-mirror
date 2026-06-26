<!-- source: https://developers.openai.com/api/reference/ruby/resources/containers/subresources/files/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Containers](/api/reference/ruby/resources/containers)

[Files](/api/reference/ruby/resources/containers/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a container file

containers.files.delete(file\_id, \*\*kwargs) -> void

DELETE/containers/{container\_id}/files/{file\_id}

Delete Container File

##### ParametersExpand Collapse

container\_id: String

file\_id: String

### Delete a container file

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

result = openai.containers.files.delete("file_id", container_id: "container_id")

puts(result)

    "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "object": "container.file.deleted",
    "deleted": true

##### Returns Examples

    "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "object": "container.file.deleted",
    "deleted": true

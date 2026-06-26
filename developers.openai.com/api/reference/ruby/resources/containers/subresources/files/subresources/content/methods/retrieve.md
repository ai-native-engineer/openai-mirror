<!-- source: https://developers.openai.com/api/reference/ruby/resources/containers/subresources/files/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Containers](/api/reference/ruby/resources/containers)

[Files](/api/reference/ruby/resources/containers/subresources/files)

[Content](/api/reference/ruby/resources/containers/subresources/files/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve container file content

containers.files.content.retrieve(file\_id, \*\*kwargs) -> StringIO

GET/containers/{container\_id}/files/{file\_id}/content

Retrieve Container File Content

##### ParametersExpand Collapse

container\_id: String

file\_id: String

##### ReturnsExpand Collapse

StringIO

### Retrieve container file content

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

content = openai.containers.files.content.retrieve("file_id", container_id: "container_id")

puts(content)

<binary content of the file>

##### Returns Examples

<binary content of the file>

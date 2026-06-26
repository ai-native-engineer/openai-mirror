<!-- source: https://developers.openai.com/api/reference/ruby/resources/files/methods/content/ -->

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

# Retrieve file content

files.content(file\_id) -> StringIO

GET/files/{file\_id}/content

Returns the contents of the specified file.

##### ParametersExpand Collapse

file\_id: String

##### ReturnsExpand Collapse

StringIO

### Retrieve file content

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

response = openai.files.content("file_id")

puts(response)

##### Returns Examples

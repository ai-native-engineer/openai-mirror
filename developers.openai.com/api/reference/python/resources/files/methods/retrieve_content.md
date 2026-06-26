<!-- source: https://developers.openai.com/api/reference/python/resources/files/methods/retrieve_content/ -->

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

# Retrieve file content

Deprecated: The `.content()` method should be used instead

files.retrieve\_content(strfile\_id)  -> [FileContent](/api/reference/python/resources/files#(resource)%20files%20%3E%20(model)%20file_content%20%3E%20(schema))

GET/files/{file\_id}/content

Returns the contents of the specified file.

##### ParametersExpand Collapse

file\_id: str

##### ReturnsExpand Collapse

str

### Retrieve file content

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

content = client.files.content("file-abc123")

200 example

"string"

##### Returns Examples

200 example

"string"

<!-- source: https://developers.openai.com/api/reference/python/resources/files/methods/content/ -->

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

files.content(strfile\_id)  -> BinaryResponseContent

GET/files/{file\_id}/content

Returns the contents of the specified file.

##### ParametersExpand Collapse

file\_id: str

##### ReturnsExpand Collapse

BinaryResponseContent

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

##### Returns Examples

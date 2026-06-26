<!-- source: https://developers.openai.com/api/reference/python/resources/containers/subresources/files/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Containers](/api/reference/python/resources/containers)

[Files](/api/reference/python/resources/containers/subresources/files)

[Content](/api/reference/python/resources/containers/subresources/files/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve container file content

containers.files.content.retrieve(strfile\_id, ContentRetrieveParams\*\*kwargs)  -> BinaryResponseContent

GET/containers/{container\_id}/files/{file\_id}/content

Retrieve Container File Content

##### ParametersExpand Collapse

container\_id: str

file\_id: str

##### ReturnsExpand Collapse

BinaryResponseContent

### Retrieve container file content

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
content = client.containers.files.content.retrieve(
    file_id="file_id",
    container_id="container_id",
print(content)
data = content.read()
print(data)

<binary content of the file>

##### Returns Examples

<binary content of the file>

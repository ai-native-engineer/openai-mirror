<!-- source: https://developers.openai.com/api/reference/cli/resources/containers/subresources/files/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Containers](/api/reference/cli/resources/containers)

[Files](/api/reference/cli/resources/containers/subresources/files)

[Content](/api/reference/cli/resources/containers/subresources/files/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve container file content

$ openai containers:files:content retrieve

GET/containers/{container\_id}/files/{file\_id}/content

Retrieve Container File Content

##### ParametersExpand Collapse

--container-id: string

--file-id: string

##### ReturnsExpand Collapse

unnamed\_schema\_3: file path

### Retrieve container file content

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai containers:files:content retrieve \
  --api-key 'My API Key' \
  --container-id container_id \
  --file-id file_id

<binary content of the file>

##### Returns Examples

<binary content of the file>

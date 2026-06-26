<!-- source: https://developers.openai.com/api/reference/typescript/resources/containers/subresources/files/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Containers](/api/reference/typescript/resources/containers)

[Files](/api/reference/typescript/resources/containers/subresources/files)

[Content](/api/reference/typescript/resources/containers/subresources/files/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve container file content

client.containers.files.content.retrieve(stringfileID, ContentRetrieveParams { container\_id } params, RequestOptionsoptions?): Response

GET/containers/{container\_id}/files/{file\_id}/content

Retrieve Container File Content

##### ParametersExpand Collapse

fileID: string

params: ContentRetrieveParams { container\_id }

container\_id: string

##### ReturnsExpand Collapse

unnamed\_schema\_9 = Response

### Retrieve container file content

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted

const content = await client.containers.files.content.retrieve('file_id', {
  container_id: 'container_id',

console.log(content);

const data = await content.blob();
console.log(data);

<binary content of the file>

##### Returns Examples

<binary content of the file>

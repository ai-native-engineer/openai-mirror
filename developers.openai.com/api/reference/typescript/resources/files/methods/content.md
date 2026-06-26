<!-- source: https://developers.openai.com/api/reference/typescript/resources/files/methods/content/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Files](/api/reference/typescript/resources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve file content

client.files.content(stringfileID, RequestOptionsoptions?): Response

GET/files/{file\_id}/content

Returns the contents of the specified file.

##### ParametersExpand Collapse

fileID: string

##### ReturnsExpand Collapse

unnamed\_schema\_7 = Response

### Retrieve file content

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const file = await openai.files.content("file-abc123");

  console.log(file);

main();

##### Returns Examples

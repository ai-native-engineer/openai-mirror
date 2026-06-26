<!-- source: https://developers.openai.com/api/reference/typescript/resources/skills/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Skills](/api/reference/typescript/resources/skills)

[Content](/api/reference/typescript/resources/skills/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Download a skill zip bundle by its ID.

client.skills.content.retrieve(stringskillID, RequestOptionsoptions?): Response

GET/skills/{skill\_id}/content

Download a skill zip bundle by its ID.

##### ParametersExpand Collapse

skillID: string

##### ReturnsExpand Collapse

unnamed\_schema\_10 = Response

### Download a skill zip bundle by its ID.

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

const content = await client.skills.content.retrieve('skill_123');

console.log(content);

const data = await content.blob();
console.log(data);

##### Returns Examples

<!-- source: https://developers.openai.com/api/reference/typescript/resources/skills/subresources/versions/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Skills](/api/reference/typescript/resources/skills)

[Versions](/api/reference/typescript/resources/skills/subresources/versions)

[Content](/api/reference/typescript/resources/skills/subresources/versions/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Download a skill version zip bundle.

client.skills.versions.content.retrieve(stringversion, ContentRetrieveParams { skill\_id } params, RequestOptionsoptions?): Response

GET/skills/{skill\_id}/versions/{version}/content

Download a skill version zip bundle.

##### ParametersExpand Collapse

version: string

The skill version number.

params: ContentRetrieveParams { skill\_id }

skill\_id: string

The identifier of the skill.

##### ReturnsExpand Collapse

unnamed\_schema\_11 = Response

### Download a skill version zip bundle.

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

const content = await client.skills.versions.content.retrieve('version', { skill_id: 'skill_123' });

console.log(content);

const data = await content.blob();
console.log(data);

##### Returns Examples

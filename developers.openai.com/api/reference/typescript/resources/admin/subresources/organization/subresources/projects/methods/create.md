<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create project

client.admin.organization.projects.create(ProjectCreateParams { name, external\_key\_id, geography } body, RequestOptionsoptions?): [Project](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) { id, created\_at, object, 4 more }

POST/organization/projects

Create a new project in the organization. Projects can be created and archived, but cannot be deleted.

##### ParametersExpand Collapse

body: ProjectCreateParams { name, external\_key\_id, geography }

name: string

The friendly name of the project, this name appears in reports.

external\_key\_id?: string | null

External key ID to associate with the project.

geography?: string | null

Create the project with the specified data residency region. Your organization must have access to Data residency functionality in order to use. See [data residency controls](https://platform.openai.com/docs/guides/your-data#data-residency-controls) to review the functionality and limitations of setting this field.

##### ReturnsExpand Collapse

Project { id, created\_at, object, 4 more }

Represents an individual project.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the project was created.

formatunixtime

object: "organization.project"

The object type, which is always `organization.project`

archived\_at?: number | null

The Unix timestamp (in seconds) of when the project was archived or `null`.

formatunixtime

external\_key\_id?: string | null

The external key associated with the project.

name?: string | null

The name of the project. This appears in reporting.

status?: string | null

`active` or `archived`

### Create project

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
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted

const project = await client.admin.organization.projects.create({ name: 'name' });

console.log(project.id);

    "id": "proj_abc",
    "object": "organization.project",
    "name": "Project ABC",
    "created_at": 1711471533,
    "archived_at": null,
    "status": "active"

##### Returns Examples

    "id": "proj_abc",
    "object": "organization.project",
    "name": "Project ABC",
    "created_at": 1711471533,
    "archived_at": null,
    "status": "active"

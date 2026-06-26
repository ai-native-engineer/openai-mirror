<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

[Data Retention](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/data_retention)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project data retention

client.admin.organization.projects.dataRetention.retrieve(stringprojectID, RequestOptionsoptions?): [ProjectDataRetention](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)) { object, type }

GET/organization/projects/{project\_id}/data\_retention

Retrieves project data retention controls.

##### ParametersExpand Collapse

projectID: string

##### ReturnsExpand Collapse

ProjectDataRetention { object, type }

Represents a project’s data retention control setting.

object: "project.data\_retention"

The object type, which is always `project.data_retention`.

type: "organization\_default" | "none" | "zero\_data\_retention" | 3 more

The configured project data retention type.

One of the following:

"organization\_default"

"none"

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

### Retrieve project data retention

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

const projectDataRetention = await client.admin.organization.projects.dataRetention.retrieve(
  'project_id',
);

console.log(projectDataRetention.object);

    "object": "project.data_retention",
    "type": "organization_default"

##### Returns Examples

    "object": "project.data_retention",
    "type": "organization_default"

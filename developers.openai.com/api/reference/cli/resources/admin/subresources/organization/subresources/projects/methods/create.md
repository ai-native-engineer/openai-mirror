<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create project

$ openai admin:organization:projects create

POST/organization/projects

Create a new project in the organization. Projects can be created and archived, but cannot be deleted.

##### ParametersExpand Collapse

--name: string

The friendly name of the project, this name appears in reports.

--external-key-id: optional string

External key ID to associate with the project.

--geography: optional string

Create the project with the specified data residency region. Your organization must have access to Data residency functionality in order to use. See [data residency controls](https://platform.openai.com/docs/guides/your-data#data-residency-controls) to review the functionality and limitations of setting this field.

##### ReturnsExpand Collapse

project: object { id, created\_at, object, 4 more }

Represents an individual project.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the project was created.

object: "organization.project"

The object type, which is always `organization.project`

archived\_at: optional number

The Unix timestamp (in seconds) of when the project was archived or `null`.

external\_key\_id: optional string

The external key associated with the project.

name: optional string

The name of the project. This appears in reporting.

status: optional string

`active` or `archived`

### Create project

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects create \
  --admin-api-key 'My Admin API Key' \
  --name name

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

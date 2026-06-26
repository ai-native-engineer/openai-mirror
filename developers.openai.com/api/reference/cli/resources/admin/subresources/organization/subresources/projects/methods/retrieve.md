<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/methods/retrieve/ -->

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

# Retrieve project

$ openai admin:organization:projects retrieve

GET/organization/projects/{project\_id}

Retrieves a project.

##### ParametersExpand Collapse

--project-id: string

The ID of the project.

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

### Retrieve project

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects retrieve \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id

    "id": "proj_abc",
    "object": "organization.project",
    "name": "Project example",
    "created_at": 1711471533,
    "archived_at": null,
    "status": "active"

##### Returns Examples

    "id": "proj_abc",
    "object": "organization.project",
    "name": "Project example",
    "created_at": 1711471533,
    "archived_at": null,
    "status": "active"

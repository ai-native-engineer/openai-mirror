<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Roles](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List project roles

$ openai admin:organization:projects:roles list

GET/projects/{project\_id}/roles

Lists the roles configured for a project.

##### ParametersExpand Collapse

--project-id: string

The ID of the project to inspect.

--after: optional string

Cursor for pagination. Provide the value from the previous response’s `next` field to continue listing roles.

--limit: optional number

A limit on the number of roles to return. Defaults to 1000.

--order: optional "asc" or "desc"

Sort order for the returned roles.

##### ReturnsExpand Collapse

PublicRoleListResource: object { data, has\_more, next, object }

Paginated list of roles available on an organization or project.

data: array of [Role](/api/reference/cli/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

Roles returned in the current page.

id: string

Identifier for the role.

description: string

Optional description of the role.

name: string

Unique name for the role.

object: "role"

Always `role`.

permissions: array of string

Permissions granted by the role.

predefined\_role: boolean

Whether the role is predefined and managed by OpenAI.

resource\_type: string

Resource type the role is bound to (for example `api.organization` or `api.project`).

has\_more: boolean

Whether more roles are available when paginating.

next: string

Cursor to fetch the next page of results, or `null` when there are no additional roles.

object: "list"

Always `list`.

### List project roles

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:roles list \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id

    "object": "list",
    "data": [
            "object": "role",
            "id": "role_01J1F8PROJ",
            "name": "API Project Key Manager",
            "description": "Allows managing API keys for the project",
            "permissions": [
                "api.organization.projects.api_keys.read",
                "api.organization.projects.api_keys.write"
            ],
            "resource_type": "api.project",
            "predefined_role": false
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
            "object": "role",
            "id": "role_01J1F8PROJ",
            "name": "API Project Key Manager",
            "description": "Allows managing API keys for the project",
            "permissions": [
                "api.organization.projects.api_keys.read",
                "api.organization.projects.api_keys.write"
            ],
            "resource_type": "api.project",
            "predefined_role": false
    ],
    "has_more": false,
    "next": null

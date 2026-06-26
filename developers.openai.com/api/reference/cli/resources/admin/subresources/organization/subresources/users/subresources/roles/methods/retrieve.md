<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Users](/api/reference/cli/resources/admin/subresources/organization/subresources/users)

[Roles](/api/reference/cli/resources/admin/subresources/organization/subresources/users/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve user organization role

$ openai admin:organization:users:roles retrieve

GET/organization/users/{user\_id}/roles/{role\_id}

Retrieves an organization role assigned to a user.

##### ParametersExpand Collapse

--user-id: string

The ID of the user to inspect.

--role-id: string

The ID of the organization role to retrieve for the user.

##### ReturnsExpand Collapse

AdminOrganizationUserRoleGetResponse: object { id, assignment\_sources, created\_at, 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id: string

Identifier for the role.

assignment\_sources: array of object { principal\_id, principal\_type }

Principals from which the role assignment is inherited, when available.

principal\_id: string

principal\_type: string

created\_at: number

When the role was created.

created\_by: string

Identifier of the actor who created the role.

created\_by\_user\_obj: map[unknown]

User details for the actor that created the role, when available.

description: string

Description of the role.

metadata: map[unknown]

Arbitrary metadata stored on the role.

name: string

Name of the role.

permissions: array of string

Permissions associated with the role.

predefined\_role: boolean

Whether the role is predefined by OpenAI.

resource\_type: string

Resource type the role applies to.

updated\_at: number

When the role was last updated.

### Retrieve user organization role

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:users:roles retrieve \
  --admin-api-key 'My Admin API Key' \
  --user-id user_id \
  --role-id role_id

    "id": "role_01J1F8ROLE01",
    "name": "API Group Manager",
    "permissions": [
        "api.groups.read",
        "api.groups.write"
    ],
    "resource_type": "api.organization",
    "predefined_role": false,
    "description": "Allows managing organization groups",
    "created_at": 1711471533,
    "updated_at": 1711472599,
    "created_by": "user_abc123",
    "created_by_user_obj": null,
    "metadata": {},
    "assignment_sources": null

##### Returns Examples

    "id": "role_01J1F8ROLE01",
    "name": "API Group Manager",
    "permissions": [
        "api.groups.read",
        "api.groups.write"
    ],
    "resource_type": "api.organization",
    "predefined_role": false,
    "description": "Allows managing organization groups",
    "created_at": 1711471533,
    "updated_at": 1711472599,
    "created_by": "user_abc123",
    "created_by_user_obj": null,
    "metadata": {},
    "assignment_sources": null

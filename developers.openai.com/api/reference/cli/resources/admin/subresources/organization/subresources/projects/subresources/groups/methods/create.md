<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Add project group

$ openai admin:organization:projects:groups create

POST/organization/projects/{project\_id}/groups

Grants a group access to a project.

##### ParametersExpand Collapse

--project-id: string

The ID of the project to update.

--group-id: string

Identifier of the group to add to the project.

--role: string

Identifier of the project role to grant to the group.

##### ReturnsExpand Collapse

project\_group: object { created\_at, group\_id, group\_name, 3 more }

Details about a group’s membership in a project.

created\_at: number

Unix timestamp (in seconds) when the group was granted project access.

group\_id: string

Identifier of the group that has access to the project.

group\_name: string

Display name of the group.

group\_type: "group" or "tenant\_group"

The type of the group.

"group"

"tenant\_group"

object: "project.group"

Always `project.group`.

project\_id: string

Identifier of the project.

### Add project group

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:groups create \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id \
  --group-id group_id \
  --role role

    "object": "project.group",
    "project_id": "proj_abc123",
    "group_id": "group_01J1F8ABCDXYZ",
    "group_name": "Support Team",
    "created_at": 1711471533

##### Returns Examples

    "object": "project.group",
    "project_id": "proj_abc123",
    "group_id": "group_01J1F8ABCDXYZ",
    "group_name": "Support Team",
    "created_at": 1711471533

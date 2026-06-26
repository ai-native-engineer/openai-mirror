<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project group

admin.organization.projects.groups.retrieve(group\_id, \*\*kwargs) -> [ProjectGroup](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)) { created\_at, group\_id, group\_name, 3 more }

GET/organization/projects/{project\_id}/groups/{group\_id}

Retrieves a project’s group.

##### ParametersExpand Collapse

project\_id: String

group\_id: String

group\_type: :group | :tenant\_group

The type of group to retrieve.

One of the following:

:group

:tenant\_group

##### ReturnsExpand Collapse

class ProjectGroup { created\_at, group\_id, group\_name, 3 more }

Details about a group’s membership in a project.

created\_at: Integer

Unix timestamp (in seconds) when the group was granted project access.

formatunixtime

group\_id: String

Identifier of the group that has access to the project.

group\_name: String

Display name of the group.

group\_type: :group | :tenant\_group

The type of the group.

One of the following:

:group

:tenant\_group

object: :"project.group"

Always `project.group`.

project\_id: String

Identifier of the project.

### Retrieve project group

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

project_group = openai.admin.organization.projects.groups.retrieve("group_id", project_id: "project_id")

puts(project_group)

    "object": "project.group",
    "project_id": "proj_abc123",
    "group_id": "group_01J1F8ABCDXYZ",
    "group_name": "Support Team",
    "group_type": "group",
    "created_at": 1711471533

##### Returns Examples

    "object": "project.group",
    "project_id": "proj_abc123",
    "group_id": "group_01J1F8ABCDXYZ",
    "group_name": "Support Team",
    "group_type": "group",
    "created_at": 1711471533

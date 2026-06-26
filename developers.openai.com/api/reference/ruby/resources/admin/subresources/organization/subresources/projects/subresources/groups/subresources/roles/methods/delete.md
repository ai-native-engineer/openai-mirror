<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/groups)

[Roles](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Unassign project role from group

admin.organization.projects.groups.roles.delete(role\_id, \*\*kwargs) -> [RoleDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

Unassigns a project role from a group within a project.

##### ParametersExpand Collapse

project\_id: String

group\_id: String

role\_id: String

##### ReturnsExpand Collapse

class RoleDeleteResponse { deleted, object }

Confirmation payload returned after unassigning a role.

deleted: bool

Whether the assignment was removed.

object: String

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

### Unassign project role from group

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

role = openai.admin.organization.projects.groups.roles.delete(
  "role_id",
  project_id: "project_id",
  group_id: "group_id"

puts(role)

    "object": "group.role.deleted",
    "deleted": true

##### Returns Examples

    "object": "group.role.deleted",
    "deleted": true

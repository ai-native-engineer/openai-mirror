<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Users](/api/reference/ruby/resources/admin/subresources/organization/subresources/users)

[Roles](/api/reference/ruby/resources/admin/subresources/organization/subresources/users/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Unassign organization role from user

admin.organization.users.roles.delete(role\_id, \*\*kwargs) -> [RoleDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/organization/users/{user\_id}/roles/{role\_id}

Unassigns an organization role from a user within the organization.

##### ParametersExpand Collapse

user\_id: String

role\_id: String

##### ReturnsExpand Collapse

class RoleDeleteResponse { deleted, object }

Confirmation payload returned after unassigning a role.

deleted: bool

Whether the assignment was removed.

object: String

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

### Unassign organization role from user

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

role = openai.admin.organization.users.roles.delete("role_id", user_id: "user_id")

puts(role)

    "object": "user.role.deleted",
    "deleted": true

##### Returns Examples

    "object": "user.role.deleted",
    "deleted": true

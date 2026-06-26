<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Roles](/api/reference/ruby/resources/admin/subresources/organization/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete organization role

admin.organization.roles.delete(role\_id) -> [RoleDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/roles/{role\_id}

Deletes a custom role from the organization.

##### ParametersExpand Collapse

role\_id: String

##### ReturnsExpand Collapse

class RoleDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a role.

id: String

Identifier of the deleted role.

deleted: bool

Whether the role was deleted.

object: :"role.deleted"

Always `role.deleted`.

### Delete organization role

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

role = openai.admin.organization.roles.delete("role_id")

puts(role)

    "object": "role.deleted",
    "id": "role_01J1F8ROLE01",
    "deleted": true

##### Returns Examples

    "object": "role.deleted",
    "id": "role_01J1F8ROLE01",
    "deleted": true

<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Groups](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete group

admin.organization.groups.delete(group\_id) -> [GroupDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/groups/{group\_id}

Deletes a group from the organization.

##### ParametersExpand Collapse

group\_id: String

##### ReturnsExpand Collapse

class GroupDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a group.

id: String

Identifier of the deleted group.

deleted: bool

Whether the group was deleted.

object: :"group.deleted"

Always `group.deleted`.

### Delete group

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

group = openai.admin.organization.groups.delete("group_id")

puts(group)

    "object": "group.deleted",
    "id": "group_01J1F8ABCDXYZ",
    "deleted": true

##### Returns Examples

    "object": "group.deleted",
    "id": "group_01J1F8ABCDXYZ",
    "deleted": true

<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/methods/update/ -->

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

# Update group

admin.organization.groups.update(group\_id, \*\*kwargs) -> [GroupUpdateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema)) { id, created\_at, is\_scim\_managed, name }

POST/organization/groups/{group\_id}

Updates a group’s information.

##### ParametersExpand Collapse

group\_id: String

name: String

New display name for the group.

minLength1

maxLength255

##### ReturnsExpand Collapse

class GroupUpdateResponse { id, created\_at, is\_scim\_managed, name }

Response returned after updating a group.

id: String

Identifier for the group.

created\_at: Integer

Unix timestamp (in seconds) when the group was created.

formatunixtime

is\_scim\_managed: bool

Whether the group is managed through SCIM and controlled by your identity provider.

name: String

Updated display name for the group.

### Update group

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

group = openai.admin.organization.groups.update("group_id", name: "x")

puts(group)

    "id": "group_01J1F8ABCDXYZ",
    "name": "Escalations",
    "created_at": 1711471533,
    "is_scim_managed": false

##### Returns Examples

    "id": "group_01J1F8ABCDXYZ",
    "name": "Escalations",
    "created_at": 1711471533,
    "is_scim_managed": false

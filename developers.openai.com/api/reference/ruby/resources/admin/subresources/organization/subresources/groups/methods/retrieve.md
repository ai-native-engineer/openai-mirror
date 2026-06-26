<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/methods/retrieve/ -->

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

# Retrieve group

admin.organization.groups.retrieve(group\_id) -> [Group](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id, created\_at, group\_type, 2 more }

GET/organization/groups/{group\_id}

Retrieves a group.

##### ParametersExpand Collapse

group\_id: String

##### ReturnsExpand Collapse

class Group { id, created\_at, group\_type, 2 more }

Details about an organization group.

id: String

Identifier for the group.

created\_at: Integer

Unix timestamp (in seconds) when the group was created.

formatunixtime

group\_type: :group | :tenant\_group

The type of the group.

One of the following:

:group

:tenant\_group

is\_scim\_managed: bool

Whether the group is managed through SCIM and controlled by your identity provider.

name: String

Display name of the group.

### Retrieve group

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

group = openai.admin.organization.groups.retrieve("group_id")

puts(group)

    "id": "group_01J1F8ABCDXYZ",
    "name": "Support Team",
    "created_at": 1711471533,
    "is_scim_managed": false,
    "group_type": "group"

##### Returns Examples

    "id": "group_01J1F8ABCDXYZ",
    "name": "Support Team",
    "created_at": 1711471533,
    "is_scim_managed": false,
    "group_type": "group"

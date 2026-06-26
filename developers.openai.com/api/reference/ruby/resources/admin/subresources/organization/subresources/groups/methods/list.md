<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/methods/list/ -->

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

# List groups

admin.organization.groups.list(\*\*kwargs) -> NextCursorPage<[Group](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id, created\_at, group\_type, 2 more } >

GET/organization/groups

Lists all groups in the organization.

##### ParametersExpand Collapse

after: String

A cursor for use in pagination. `after` is a group ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with group\_abc, your subsequent call can include `after=group_abc` in order to fetch the next page of the list.

limit: Integer

A limit on the number of groups to be returned. Limit can range between 0 and 1000, and the default is 100.

minimum0

maximum1000

order: :asc | :desc

Specifies the sort order of the returned groups.

One of the following:

:asc

:desc

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

### List groups

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

page = openai.admin.organization.groups.list

puts(page)

    "object": "list",
    "data": [
            "object": "group",
            "id": "group_01J1F8ABCDXYZ",
            "name": "Support Team",
            "created_at": 1711471533,
            "is_scim_managed": false
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
            "object": "group",
            "id": "group_01J1F8ABCDXYZ",
            "name": "Support Team",
            "created_at": 1711471533,
            "is_scim_managed": false
    ],
    "has_more": false,
    "next": null

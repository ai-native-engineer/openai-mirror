<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/groups/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List groups

GET/organization/groups

Lists all groups in the organization.

##### Query ParametersExpand Collapse

after: optional string

A cursor for use in pagination. `after` is a group ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with group\_abc, your subsequent call can include `after=group_abc` in order to fetch the next page of the list.

limit: optional number

A limit on the number of groups to be returned. Limit can range between 0 and 1000, and the default is 100.

minimum0

maximum1000

order: optional "asc" or "desc"

Specifies the sort order of the returned groups.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

data: array of [Group](/api/reference/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id, created\_at, group\_type, 2 more }

Groups returned in the current page.

id: string

Identifier for the group.

created\_at: number

Unix timestamp (in seconds) when the group was created.

formatunixtime

group\_type: "group" or "tenant\_group"

The type of the group.

One of the following:

"group"

"tenant\_group"

is\_scim\_managed: boolean

Whether the group is managed through SCIM and controlled by your identity provider.

name: string

Display name of the group.

has\_more: boolean

Whether additional groups are available when paginating.

next: string

Cursor to fetch the next page of results, or `null` if there are no more results.

object: "list"

Always `list`.

### List groups

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/organization/groups?limit=20&order=asc \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

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

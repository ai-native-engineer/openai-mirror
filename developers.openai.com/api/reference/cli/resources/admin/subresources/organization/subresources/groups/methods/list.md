<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/groups/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Groups](/api/reference/cli/resources/admin/subresources/organization/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List groups

$ openai admin:organization:groups list

GET/organization/groups

Lists all groups in the organization.

##### ParametersExpand Collapse

--after: optional string

A cursor for use in pagination. `after` is a group ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with group\_abc, your subsequent call can include `after=group_abc` in order to fetch the next page of the list.

--limit: optional number

A limit on the number of groups to be returned. Limit can range between 0 and 1000, and the default is 100.

--order: optional "asc" or "desc"

Specifies the sort order of the returned groups.

##### ReturnsExpand Collapse

GroupListResource: object { data, has\_more, next, object }

Paginated list of organization groups.

data: array of [Group](/api/reference/cli/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id, created\_at, group\_type, 2 more }

Groups returned in the current page.

id: string

Identifier for the group.

created\_at: number

Unix timestamp (in seconds) when the group was created.

group\_type: "group" or "tenant\_group"

The type of the group.

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

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:groups list \
  --admin-api-key 'My Admin API Key'

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

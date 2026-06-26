<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Groups](/api/reference/cli/resources/admin/subresources/organization/subresources/groups)

[Users](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List group users

$ openai admin:organization:groups:users list

GET/organization/groups/{group\_id}/users

Lists the users assigned to a group.

##### ParametersExpand Collapse

--group-id: string

The ID of the group to inspect.

--after: optional string

A cursor for use in pagination. Provide the ID of the last user from the previous list response to retrieve the next page.

--limit: optional number

A limit on the number of users to be returned. Limit can range between 0 and 1000, and the default is 100.

--order: optional "asc" or "desc"

Specifies the sort order of users in the list.

##### ReturnsExpand Collapse

UserListResource: object { data, has\_more, next, object }

Paginated list of user objects returned when inspecting group membership.

data: array of [OrganizationGroupUser](/api/reference/cli/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema)) { id, email, name }

Users in the current page.

id: string

The identifier, which can be referenced in API endpoints

email: string

The email address of the user.

name: string

The name of the user.

has\_more: boolean

Whether more users are available when paginating.

next: string

Cursor to fetch the next page of results, or `null` when no further users are available.

object: "list"

Always `list`.

### List group users

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:groups:users list \
  --admin-api-key 'My Admin API Key' \
  --group-id group_id

    "object": "list",
    "data": [
            "id": "user_abc123",
            "name": "Ada Lovelace",
            "email": "ada@example.com"
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
            "id": "user_abc123",
            "name": "Ada Lovelace",
            "email": "ada@example.com"
    ],
    "has_more": false,
    "next": null

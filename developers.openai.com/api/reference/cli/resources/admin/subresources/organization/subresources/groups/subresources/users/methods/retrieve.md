<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve/ -->

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

# Retrieve group user

$ openai admin:organization:groups:users retrieve

GET/organization/groups/{group\_id}/users/{user\_id}

Retrieves a user in a group.

##### ParametersExpand Collapse

--group-id: string

The ID of the group to inspect.

--user-id: string

The ID of the user to retrieve from the group.

##### ReturnsExpand Collapse

AdminOrganizationGroupUserGetResponse: object { id, email, is\_service\_account, 3 more }

Details about a user returned from an organization group membership lookup.

id: string

Identifier for the user.

email: string

Email address of the user, or `null` for users without an email.

is\_service\_account: boolean

Whether the user is a service account.

name: string

Display name of the user.

picture: string

URL of the user’s profile picture, if available.

user\_type: "user" or "tenant\_user"

The type of user.

"user"

"tenant\_user"

### Retrieve group user

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:groups:users retrieve \
  --admin-api-key 'My Admin API Key' \
  --group-id group_id \
  --user-id user_id

    "id": "user_abc123",
    "name": "Ada Lovelace",
    "email": "ada@example.com",
    "picture": null,
    "is_service_account": false,
    "user_type": "user"

##### Returns Examples

    "id": "user_abc123",
    "name": "Ada Lovelace",
    "email": "ada@example.com",
    "picture": null,
    "is_service_account": false,
    "user_type": "user"

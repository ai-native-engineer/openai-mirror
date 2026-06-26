<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/users/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Users](/api/reference/resources/admin/subresources/organization/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List users

GET/organization/users

Lists all of the users in the organization.

##### Query ParametersExpand Collapse

after: optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

emails: optional array of string

Filter by the email address of users.

limit: optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

##### ReturnsExpand Collapse

data: array of [OrganizationUser](/api/reference/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more }

id: string

The identifier, which can be referenced in API endpoints

added\_at: number

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

object: "organization.user"

The object type, which is always `organization.user`

api\_key\_last\_used\_at: optional number

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

created: optional number

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

developer\_persona: optional string

The developer persona metadata for the user.

email: optional string

The email address of the user

is\_default: optional boolean

Whether this is the organization’s default user.

is\_scale\_tier\_authorized\_purchaser: optional boolean

Whether the user is an authorized purchaser for Scale Tier.

is\_scim\_managed: optional boolean

Whether the user is managed through SCIM.

is\_service\_account: optional boolean

Whether the user is a service account.

name: optional string

The name of the user

projects: optional object { data, object }

Projects associated with the user, if included.

data: array of object { id, name, role }

id: optional string

name: optional string

role: optional string

object: "list"

role: optional string

`owner` or `reader`

technical\_level: optional string

The technical level metadata for the user.

user: optional object { id, object, banned, 5 more }

Nested user details.

id: string

object: "user"

banned: optional boolean

banned\_at: optional number

formatunixtime

email: optional string

enabled: optional boolean

name: optional string

picture: optional string

has\_more: boolean

object: "list"

first\_id: optional string

last\_id: optional string

### List users

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/organization/users?after=user_abc&limit=20 \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

    "object": "list",
    "data": [
            "object": "organization.user",
            "id": "user_abc",
            "name": "First Last",
            "email": "user@example.com",
            "role": "owner",
            "added_at": 1711471533
    ],
    "first_id": "user-abc",
    "last_id": "user-xyz",
    "has_more": false

##### Returns Examples

    "object": "list",
    "data": [
            "object": "organization.user",
            "id": "user_abc",
            "name": "First Last",
            "email": "user@example.com",
            "role": "owner",
            "added_at": 1711471533
    ],
    "first_id": "user-abc",
    "last_id": "user-xyz",
    "has_more": false

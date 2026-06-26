<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/users/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Users

##### [List users](/api/reference/cli/resources/admin/subresources/organization/subresources/users/methods/list)

$ openai admin:organization:users list

GET/organization/users

##### [Retrieve user](/api/reference/cli/resources/admin/subresources/organization/subresources/users/methods/retrieve)

$ openai admin:organization:users retrieve

GET/organization/users/{user\_id}

##### [Modify user](/api/reference/cli/resources/admin/subresources/organization/subresources/users/methods/update)

$ openai admin:organization:users update

POST/organization/users/{user\_id}

##### [Delete user](/api/reference/cli/resources/admin/subresources/organization/subresources/users/methods/delete)

$ openai admin:organization:users delete

DELETE/organization/users/{user\_id}

##### ModelsExpand Collapse

organization\_user: object { id, added\_at, object, 13 more }

Represents an individual `user` within an organization.

id: string

The identifier, which can be referenced in API endpoints

added\_at: number

The Unix timestamp (in seconds) of when the user was added.

object: "organization.user"

The object type, which is always `organization.user`

api\_key\_last\_used\_at: optional number

The Unix timestamp (in seconds) of the user’s last API key usage.

created: optional number

The Unix timestamp (in seconds) of when the user was created.

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

email: optional string

enabled: optional boolean

name: optional string

picture: optional string

#### UsersRoles

##### [List user organization role assignments](/api/reference/cli/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/list)

$ openai admin:organization:users:roles list

GET/organization/users/{user\_id}/roles

##### [Assign organization role to user](/api/reference/cli/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/create)

$ openai admin:organization:users:roles create

POST/organization/users/{user\_id}/roles

##### [Retrieve user organization role](/api/reference/cli/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve)

$ openai admin:organization:users:roles retrieve

GET/organization/users/{user\_id}/roles/{role\_id}

##### [Unassign organization role from user](/api/reference/cli/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/delete)

$ openai admin:organization:users:roles delete

DELETE/organization/users/{user\_id}/roles/{role\_id}

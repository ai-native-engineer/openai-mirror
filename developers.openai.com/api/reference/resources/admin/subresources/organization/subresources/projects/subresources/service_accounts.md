<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Service Accounts

##### [List project service accounts](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/list)

GET/organization/projects/{project\_id}/service\_accounts

##### [Create project service account](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create)

POST/organization/projects/{project\_id}/service\_accounts

##### [Retrieve project service account](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/retrieve)

GET/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Update project service account](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update)

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Delete project service account](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete)

DELETE/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### ModelsExpand Collapse

ProjectServiceAccount object { id, created\_at, name, 2 more }

Represents an individual service account in a project.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the service account was created

formatunixtime

name: string

The name of the service account

object: "organization.project.service\_account"

The object type, which is always `organization.project.service_account`

role: "owner" or "member"

`owner` or `member`

One of the following:

"owner"

"member"

ServiceAccountCreateResponse object { id, api\_key, created\_at, 3 more }

id: string

api\_key: object { id, created\_at, name, 2 more }

id: string

created\_at: number

formatunixtime

name: string

object: "organization.project.service\_account.api\_key"

The object type, which is always `organization.project.service_account.api_key`

value: string

created\_at: number

formatunixtime

name: string

object: "organization.project.service\_account"

role: "member"

Service accounts can only have one role of type `member`

ServiceAccountDeleteResponse object { id, deleted, object }

id: string

deleted: boolean

object: "organization.project.service\_account.deleted"

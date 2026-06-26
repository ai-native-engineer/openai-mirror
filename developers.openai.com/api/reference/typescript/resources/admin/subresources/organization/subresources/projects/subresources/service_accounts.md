<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Service Accounts

##### [List project service accounts](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/list)

client.admin.organization.projects.serviceAccounts.list(stringprojectID, ServiceAccountListParams { after, limit } query?, RequestOptionsoptions?): ConversationCursorPage<[ProjectServiceAccount](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)) { id, created\_at, name, 2 more } >

GET/organization/projects/{project\_id}/service\_accounts

##### [Create project service account](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create)

client.admin.organization.projects.serviceAccounts.create(stringprojectID, ServiceAccountCreateParams { name } body, RequestOptionsoptions?): [ServiceAccountCreateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)) { id, api\_key, created\_at, 3 more }

POST/organization/projects/{project\_id}/service\_accounts

##### [Retrieve project service account](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/retrieve)

client.admin.organization.projects.serviceAccounts.retrieve(stringserviceAccountID, ServiceAccountRetrieveParams { project\_id } params, RequestOptionsoptions?): [ProjectServiceAccount](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)) { id, created\_at, name, 2 more }

GET/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Update project service account](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update)

client.admin.organization.projects.serviceAccounts.update(stringserviceAccountID, ServiceAccountUpdateParams { project\_id, name, role } params, RequestOptionsoptions?): [ProjectServiceAccount](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)) { id, created\_at, name, 2 more }

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Delete project service account](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete)

client.admin.organization.projects.serviceAccounts.delete(stringserviceAccountID, ServiceAccountDeleteParams { project\_id } params, RequestOptionsoptions?): [ServiceAccountDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### ModelsExpand Collapse

ProjectServiceAccount { id, created\_at, name, 2 more }

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

role: "owner" | "member"

`owner` or `member`

One of the following:

"owner"

"member"

ServiceAccountCreateResponse { id, api\_key, created\_at, 3 more }

id: string

api\_key: APIKey | null

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

ServiceAccountDeleteResponse { id, deleted, object }

id: string

deleted: boolean

object: "organization.project.service\_account.deleted"

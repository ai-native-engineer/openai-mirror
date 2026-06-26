<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Service Accounts

##### [List project service accounts](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/list)

$ openai admin:organization:projects:service-accounts list

GET/organization/projects/{project\_id}/service\_accounts

##### [Create project service account](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create)

$ openai admin:organization:projects:service-accounts create

POST/organization/projects/{project\_id}/service\_accounts

##### [Retrieve project service account](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/retrieve)

$ openai admin:organization:projects:service-accounts retrieve

GET/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Update project service account](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update)

$ openai admin:organization:projects:service-accounts update

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Delete project service account](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete)

$ openai admin:organization:projects:service-accounts delete

DELETE/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### ModelsExpand Collapse

project\_service\_account: object { id, created\_at, name, 2 more }

Represents an individual service account in a project.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the service account was created

name: string

The name of the service account

object: "organization.project.service\_account"

The object type, which is always `organization.project.service_account`

role: "owner" or "member"

`owner` or `member`

"owner"

"member"

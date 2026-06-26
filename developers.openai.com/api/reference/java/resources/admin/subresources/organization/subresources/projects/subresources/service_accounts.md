<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Service Accounts

##### [List project service accounts](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/list)

ServiceAccountListPage admin().organization().projects().serviceAccounts().list(ServiceAccountListParamsparams = ServiceAccountListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/service\_accounts

##### [Create project service account](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create)

[ServiceAccountCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20ServiceAccountCreateResponse%20%3E%20(schema)) admin().organization().projects().serviceAccounts().create(ServiceAccountCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/service\_accounts

##### [Retrieve project service account](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/retrieve)

[ProjectServiceAccount](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)) admin().organization().projects().serviceAccounts().retrieve(ServiceAccountRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Update project service account](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update)

[ProjectServiceAccount](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)) admin().organization().projects().serviceAccounts().update(ServiceAccountUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Delete project service account](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete)

[ServiceAccountDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20ServiceAccountDeleteResponse%20%3E%20(schema)) admin().organization().projects().serviceAccounts().delete(ServiceAccountDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### ModelsExpand Collapse

class ProjectServiceAccount:

Represents an individual service account in a project.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the service account was created

formatunixtime

String name

The name of the service account

JsonValue; object\_ "organization.project.service\_account"constant"organization.project.service\_account"constant

The object type, which is always `organization.project.service_account`

Role role

`owner` or `member`

One of the following:

OWNER("owner")

MEMBER("member")

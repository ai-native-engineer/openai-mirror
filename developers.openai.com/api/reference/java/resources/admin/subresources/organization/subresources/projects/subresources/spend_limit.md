<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/ -->

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

# Spend Limit

##### [Retrieve project spend limit](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/retrieve)

[ProjectSpendLimit](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)) admin().organization().projects().spendLimit().retrieve(SpendLimitRetrieveParamsparams = SpendLimitRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/spend\_limit

##### [Update project spend limit](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/update)

[ProjectSpendLimit](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)) admin().organization().projects().spendLimit().update(SpendLimitUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/spend\_limit

##### [Delete project spend limit](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/delete)

[ProjectSpendLimitDeleted](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit_deleted%20%3E%20(schema)) admin().organization().projects().spendLimit().delete(SpendLimitDeleteParamsparams = SpendLimitDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/spend\_limit

##### ModelsExpand Collapse

class ProjectSpendLimit:

Represents a hard spend limit configured at the project level.

Currency currency

USD("USD")

Enforcement enforcement

Status status

INACTIVE("inactive")

ENFORCING("enforcing")

Interval interval

MONTH("month")

JsonValue; object\_ "project.spend\_limit"constant"project.spend\_limit"constant

The object type, which is always `project.spend_limit`.

long thresholdAmount

class ProjectSpendLimitDeleted:

Confirmation payload returned after deleting a project hard spend limit.

boolean deleted

Whether the hard spend limit was deleted.

JsonValue; object\_ "project.spend\_limit.deleted"constant"project.spend\_limit.deleted"constant

The object type, which is always `project.spend_limit.deleted`.

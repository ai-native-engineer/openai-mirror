<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/spend_limit/ -->

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

# Spend Limit

##### [Retrieve organization spend limit](/api/reference/java/resources/admin/subresources/organization/subresources/spend_limit/methods/retrieve)

[OrganizationSpendLimit](/api/reference/java/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit%20%3E%20(schema)) admin().organization().spendLimit().retrieve(SpendLimitRetrieveParamsparams = SpendLimitRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/spend\_limit

##### [Update organization spend limit](/api/reference/java/resources/admin/subresources/organization/subresources/spend_limit/methods/update)

[OrganizationSpendLimit](/api/reference/java/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit%20%3E%20(schema)) admin().organization().spendLimit().update(SpendLimitUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/spend\_limit

##### [Delete organization spend limit](/api/reference/java/resources/admin/subresources/organization/subresources/spend_limit/methods/delete)

[OrganizationSpendLimitDeleted](/api/reference/java/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit_deleted%20%3E%20(schema)) admin().organization().spendLimit().delete(SpendLimitDeleteParamsparams = SpendLimitDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/spend\_limit

##### ModelsExpand Collapse

class OrganizationSpendLimit:

Represents a hard spend limit configured at the organization level.

Currency currency

USD("USD")

Enforcement enforcement

Status status

INACTIVE("inactive")

ENFORCING("enforcing")

Interval interval

MONTH("month")

JsonValue; object\_ "organization.spend\_limit"constant"organization.spend\_limit"constant

The object type, which is always `organization.spend_limit`.

long thresholdAmount

class OrganizationSpendLimitDeleted:

Confirmation payload returned after deleting an organization hard spend limit.

boolean deleted

Whether the hard spend limit was deleted.

JsonValue; object\_ "organization.spend\_limit.deleted"constant"organization.spend\_limit.deleted"constant

The object type, which is always `organization.spend_limit.deleted`.

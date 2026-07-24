<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/spend_limit/ -->

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

# Spend Limit

##### [Retrieve organization spend limit](/api/reference/python/resources/admin/subresources/organization/subresources/spend_limit/methods/retrieve)

admin.organization.spend\_limit.retrieve()  -> [OrganizationSpendLimit](/api/reference/python/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit%20%3E%20(schema))

GET/organization/spend\_limit

##### [Update organization spend limit](/api/reference/python/resources/admin/subresources/organization/subresources/spend_limit/methods/update)

admin.organization.spend\_limit.update(SpendLimitUpdateParams\*\*kwargs)  -> [OrganizationSpendLimit](/api/reference/python/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit%20%3E%20(schema))

POST/organization/spend\_limit

##### [Delete organization spend limit](/api/reference/python/resources/admin/subresources/organization/subresources/spend_limit/methods/delete)

admin.organization.spend\_limit.delete()  -> [OrganizationSpendLimitDeleted](/api/reference/python/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit_deleted%20%3E%20(schema))

DELETE/organization/spend\_limit

##### ModelsExpand Collapse

class OrganizationSpendLimit: …

Represents a hard spend limit configured at the organization level.

currency: Union[str, Literal["USD"]]

str

Literal["USD"]

enforcement: Enforcement

status: Union[str, Literal["inactive", "enforcing"]]

str

Literal["inactive", "enforcing"]

"inactive"

"enforcing"

interval: Union[str, Literal["month"]]

str

Literal["month"]

object: Literal["organization.spend\_limit"]

The object type, which is always `organization.spend_limit`.

threshold\_amount: int

class OrganizationSpendLimitDeleted: …

Confirmation payload returned after deleting an organization hard spend limit.

deleted: bool

Whether the hard spend limit was deleted.

object: Literal["organization.spend\_limit.deleted"]

The object type, which is always `organization.spend_limit.deleted`.

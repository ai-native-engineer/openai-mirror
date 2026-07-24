<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_limit/ -->

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

# Spend Limit

##### [Retrieve organization spend limit](/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_limit/methods/retrieve)

admin.organization.spend\_limit.retrieve() -> [OrganizationSpendLimit](/api/reference/ruby/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit%20%3E%20(schema)) { currency, enforcement, interval, 2 more }

GET/organization/spend\_limit

##### [Update organization spend limit](/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_limit/methods/update)

admin.organization.spend\_limit.update(\*\*kwargs) -> [OrganizationSpendLimit](/api/reference/ruby/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit%20%3E%20(schema)) { currency, enforcement, interval, 2 more }

POST/organization/spend\_limit

##### [Delete organization spend limit](/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_limit/methods/delete)

admin.organization.spend\_limit.delete() -> [OrganizationSpendLimitDeleted](/api/reference/ruby/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit_deleted%20%3E%20(schema)) { deleted, object }

DELETE/organization/spend\_limit

##### ModelsExpand Collapse

class OrganizationSpendLimit { currency, enforcement, interval, 2 more }

Represents a hard spend limit configured at the organization level.

currency: String | :USD

String = String

Currency = :USD

enforcement: Enforcement{ status}

status: String | :inactive | :enforcing

String = String

Status = :inactive | :enforcing

:inactive

:enforcing

interval: String | :month

String = String

Interval = :month

object: :"organization.spend\_limit"

The object type, which is always `organization.spend_limit`.

threshold\_amount: Integer

class OrganizationSpendLimitDeleted { deleted, object }

Confirmation payload returned after deleting an organization hard spend limit.

deleted: bool

Whether the hard spend limit was deleted.

object: :"organization.spend\_limit.deleted"

The object type, which is always `organization.spend_limit.deleted`.

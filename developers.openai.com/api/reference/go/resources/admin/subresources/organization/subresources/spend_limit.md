<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/spend_limit/ -->

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

# Spend Limit

##### [Retrieve organization spend limit](/api/reference/go/resources/admin/subresources/organization/subresources/spend_limit/methods/retrieve)

client.Admin.Organization.SpendLimit.Get(ctx) (\*[OrganizationSpendLimit](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit%20%3E%20(schema)), error)

GET/organization/spend\_limit

##### [Update organization spend limit](/api/reference/go/resources/admin/subresources/organization/subresources/spend_limit/methods/update)

client.Admin.Organization.SpendLimit.Update(ctx, body) (\*[OrganizationSpendLimit](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit%20%3E%20(schema)), error)

POST/organization/spend\_limit

##### [Delete organization spend limit](/api/reference/go/resources/admin/subresources/organization/subresources/spend_limit/methods/delete)

client.Admin.Organization.SpendLimit.Delete(ctx) (\*[OrganizationSpendLimitDeleted](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit_deleted%20%3E%20(schema)), error)

DELETE/organization/spend\_limit

##### ModelsExpand Collapse

type OrganizationSpendLimit struct{…}

Represents a hard spend limit configured at the organization level.

Currency OrganizationSpendLimitCurrency

string

type OrganizationSpendLimitCurrency string

Enforcement OrganizationSpendLimitEnforcement

Status string

string

string

const OrganizationSpendLimitEnforcementStatusInactive OrganizationSpendLimitEnforcementStatus = "inactive"

const OrganizationSpendLimitEnforcementStatusEnforcing OrganizationSpendLimitEnforcementStatus = "enforcing"

Interval OrganizationSpendLimitInterval

string

type OrganizationSpendLimitInterval string

Object OrganizationSpendLimit

The object type, which is always `organization.spend_limit`.

ThresholdAmount int64

type OrganizationSpendLimitDeleted struct{…}

Confirmation payload returned after deleting an organization hard spend limit.

Deleted bool

Whether the hard spend limit was deleted.

Object OrganizationSpendLimitDeleted

The object type, which is always `organization.spend_limit.deleted`.

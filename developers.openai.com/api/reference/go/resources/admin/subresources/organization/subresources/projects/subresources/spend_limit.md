<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/ -->

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

# Spend Limit

##### [Retrieve project spend limit](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/retrieve)

client.Admin.Organization.Projects.SpendLimit.Get(ctx, projectID) (\*[ProjectSpendLimit](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/spend\_limit

##### [Update project spend limit](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/update)

client.Admin.Organization.Projects.SpendLimit.Update(ctx, projectID, body) (\*[ProjectSpendLimit](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/spend\_limit

##### [Delete project spend limit](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/delete)

client.Admin.Organization.Projects.SpendLimit.Delete(ctx, projectID) (\*[ProjectSpendLimitDeleted](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit_deleted%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/spend\_limit

##### ModelsExpand Collapse

type ProjectSpendLimit struct{…}

Represents a hard spend limit configured at the project level.

Currency ProjectSpendLimitCurrency

string

type ProjectSpendLimitCurrency string

Enforcement ProjectSpendLimitEnforcement

Status string

string

string

const ProjectSpendLimitEnforcementStatusInactive ProjectSpendLimitEnforcementStatus = "inactive"

const ProjectSpendLimitEnforcementStatusEnforcing ProjectSpendLimitEnforcementStatus = "enforcing"

Interval ProjectSpendLimitInterval

string

type ProjectSpendLimitInterval string

Object ProjectSpendLimit

The object type, which is always `project.spend_limit`.

ThresholdAmount int64

type ProjectSpendLimitDeleted struct{…}

Confirmation payload returned after deleting a project hard spend limit.

Deleted bool

Whether the hard spend limit was deleted.

Object ProjectSpendLimitDeleted

The object type, which is always `project.spend_limit.deleted`.

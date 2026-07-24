<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/retrieve/ -->

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Spend Limit](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit)

# Retrieve project spend limit

$ openai admin:organization:projects:spend-limit retrieve

GET/organization/projects/{project\_id}/spend\_limit

Get a project’s hard spend limit.

##### ParametersExpand Collapse

--project-id: string

The ID of the project whose hard spend limit is being managed.

project\_spend\_limit: object { currency, enforcement, interval, 2 more }

Represents a hard spend limit configured at the project level.

currency: string or "USD"

"USD"

enforcement: object { status }

status: string or "inactive" or "enforcing"

"inactive"

"enforcing"

interval: string or "month"

"month"

object: "project.spend\_limit"

The object type, which is always `project.spend_limit`.

threshold\_amount: number

### Retrieve project spend limit

CLI Tool

openai admin:organization:projects:spend-limit retrieve \
  --admin-api-key 'My Admin API Key' \
  --project-id proj_123

    "object": "project.spend_limit",
    "threshold_amount": 10000,
    "currency": "USD",
    "interval": "month",
    "enforcement": {
        "status": "enforcing"

    "object": "project.spend_limit",
    "threshold_amount": 10000,
    "currency": "USD",
    "interval": "month",
    "enforcement": {
        "status": "enforcing"

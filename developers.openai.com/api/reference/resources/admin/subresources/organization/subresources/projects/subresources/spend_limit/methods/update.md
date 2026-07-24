<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/update/ -->

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Spend Limit](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit)

# Update project spend limit

POST/organization/projects/{project\_id}/spend\_limit

Create or replace a project’s hard spend limit.

##### Path ParametersExpand Collapse

project\_id: string

##### Body ParametersJSONExpand Collapse

currency: "USD"

interval: "month"

threshold\_amount: number

minimum1

ProjectSpendLimit object { currency, enforcement, interval, 2 more }

Represents a hard spend limit configured at the project level.

currency: string or "USD"

string

"USD"

enforcement: object { status }

status: string or "inactive" or "enforcing"

string

"inactive" or "enforcing"

"inactive"

"enforcing"

interval: string or "month"

string

"month"

object: "project.spend\_limit"

The object type, which is always `project.spend_limit`.

threshold\_amount: number

### Update project spend limit

HTTP

curl -X POST https://api.openai.com/v1/organization/projects/proj_abc/spend_limit \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "threshold_amount": 10000,
      "currency": "USD",
      "interval": "month"
  }'

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

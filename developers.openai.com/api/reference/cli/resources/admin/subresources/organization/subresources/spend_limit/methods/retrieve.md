<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/spend_limit/methods/retrieve/ -->

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Spend Limit](/api/reference/cli/resources/admin/subresources/organization/subresources/spend_limit)

# Retrieve organization spend limit

$ openai admin:organization:spend-limit retrieve

GET/organization/spend\_limit

Get the organization’s hard spend limit.

organization\_spend\_limit: object { currency, enforcement, interval, 2 more }

Represents a hard spend limit configured at the organization level.

currency: string or "USD"

"USD"

enforcement: object { status }

status: string or "inactive" or "enforcing"

"inactive"

"enforcing"

interval: string or "month"

"month"

object: "organization.spend\_limit"

The object type, which is always `organization.spend_limit`.

threshold\_amount: number

### Retrieve organization spend limit

CLI Tool

openai admin:organization:spend-limit retrieve \
  --admin-api-key 'My Admin API Key'

    "object": "organization.spend_limit",
    "threshold_amount": 10000,
    "currency": "USD",
    "interval": "month",
    "enforcement": {
        "status": "enforcing"

    "object": "organization.spend_limit",
    "threshold_amount": 10000,
    "currency": "USD",
    "interval": "month",
    "enforcement": {
        "status": "enforcing"

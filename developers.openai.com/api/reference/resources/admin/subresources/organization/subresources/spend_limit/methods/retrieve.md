<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/spend_limit/methods/retrieve/ -->

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Spend Limit](/api/reference/resources/admin/subresources/organization/subresources/spend_limit)

# Retrieve organization spend limit

GET/organization/spend\_limit

Get the organization’s hard spend limit.

OrganizationSpendLimit object { currency, enforcement, interval, 2 more }

Represents a hard spend limit configured at the organization level.

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

object: "organization.spend\_limit"

The object type, which is always `organization.spend_limit`.

threshold\_amount: number

### Retrieve organization spend limit

HTTP

curl https://api.openai.com/v1/organization/spend_limit \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

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

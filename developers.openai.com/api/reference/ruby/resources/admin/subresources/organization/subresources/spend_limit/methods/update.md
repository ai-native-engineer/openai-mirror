<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_limit/methods/update/ -->

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Spend Limit](/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_limit)

# Update organization spend limit

admin.organization.spend\_limit.update(\*\*kwargs) -> [OrganizationSpendLimit](/api/reference/ruby/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit%20%3E%20(schema)) { currency, enforcement, interval, 2 more }

POST/organization/spend\_limit

Create or replace the organization’s hard spend limit.

##### ParametersExpand Collapse

currency: :USD

interval: :month

threshold\_amount: Integer

minimum1

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

### Update organization spend limit

Ruby

require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

organization_spend_limit = openai.admin.organization.spend_limit.update(currency: :USD, interval: :month, threshold_amount: 1)

puts(organization_spend_limit)

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

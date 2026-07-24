<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_limit/methods/update/ -->

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Spend Limit](/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_limit)

# Update organization spend limit

client.admin.organization.spendLimit.update(SpendLimitUpdateParams { currency, interval, threshold\_amount } body, RequestOptionsoptions?): [OrganizationSpendLimit](/api/reference/typescript/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit%20%3E%20(schema)) { currency, enforcement, interval, 2 more }

POST/organization/spend\_limit

Create or replace the organization’s hard spend limit.

##### ParametersExpand Collapse

body: SpendLimitUpdateParams { currency, interval, threshold\_amount }

currency: "USD"

interval: "month"

threshold\_amount: number

minimum1

OrganizationSpendLimit { currency, enforcement, interval, 2 more }

Represents a hard spend limit configured at the organization level.

currency: (string & {}) | "USD"

(string & {})

"USD"

"USD"

enforcement: Enforcement { status }

status: (string & {}) | "inactive" | "enforcing"

(string & {})

"inactive" | "enforcing"

"inactive"

"enforcing"

interval: (string & {}) | "month"

(string & {})

"month"

"month"

object: "organization.spend\_limit"

The object type, which is always `organization.spend_limit`.

threshold\_amount: number

### Update organization spend limit

TypeScript

import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const organizationSpendLimit = await client.admin.organization.spendLimit.update({
  currency: 'USD',
  interval: 'month',
  threshold_amount: 1,
});

console.log(organizationSpendLimit.currency);

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

<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/update/ -->

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

[Spend Limit](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit)

# Update project spend limit

client.admin.organization.projects.spendLimit.update(stringprojectID, SpendLimitUpdateParams { currency, interval, threshold\_amount } body, RequestOptionsoptions?): [ProjectSpendLimit](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)) { currency, enforcement, interval, 2 more }

POST/organization/projects/{project\_id}/spend\_limit

Create or replace a project’s hard spend limit.

##### ParametersExpand Collapse

projectID: string

body: SpendLimitUpdateParams { currency, interval, threshold\_amount }

currency: "USD"

interval: "month"

threshold\_amount: number

minimum1

ProjectSpendLimit { currency, enforcement, interval, 2 more }

Represents a hard spend limit configured at the project level.

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

object: "project.spend\_limit"

The object type, which is always `project.spend_limit`.

threshold\_amount: number

### Update project spend limit

TypeScript

import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const projectSpendLimit = await client.admin.organization.projects.spendLimit.update('proj_123', {
  currency: 'USD',
  interval: 'month',
  threshold_amount: 1,
});

console.log(projectSpendLimit.currency);

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

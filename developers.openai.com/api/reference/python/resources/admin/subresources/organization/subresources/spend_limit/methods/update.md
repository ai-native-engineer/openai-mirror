<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/spend_limit/methods/update/ -->

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Spend Limit](/api/reference/python/resources/admin/subresources/organization/subresources/spend_limit)

# Update organization spend limit

admin.organization.spend\_limit.update(SpendLimitUpdateParams\*\*kwargs)  -> [OrganizationSpendLimit](/api/reference/python/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit%20%3E%20(schema))

POST/organization/spend\_limit

Create or replace the organization’s hard spend limit.

##### ParametersExpand Collapse

currency: Literal["USD"]

interval: Literal["month"]

threshold\_amount: int

minimum1

class OrganizationSpendLimit: …

Represents a hard spend limit configured at the organization level.

currency: Union[str, Literal["USD"]]

str

Literal["USD"]

enforcement: Enforcement

status: Union[str, Literal["inactive", "enforcing"]]

str

Literal["inactive", "enforcing"]

"inactive"

"enforcing"

interval: Union[str, Literal["month"]]

str

Literal["month"]

object: Literal["organization.spend\_limit"]

The object type, which is always `organization.spend_limit`.

threshold\_amount: int

### Update organization spend limit

Python

import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
organization_spend_limit = client.admin.organization.spend_limit.update(
    currency="USD",
    interval="month",
    threshold_amount=1,
)
print(organization_spend_limit.currency)

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

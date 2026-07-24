<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/update/ -->

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

[Spend Limit](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit)

# Update project spend limit

admin.organization.projects.spend\_limit.update(strproject\_id, SpendLimitUpdateParams\*\*kwargs)  -> [ProjectSpendLimit](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema))

POST/organization/projects/{project\_id}/spend\_limit

Create or replace a project’s hard spend limit.

##### ParametersExpand Collapse

project\_id: str

currency: Literal["USD"]

interval: Literal["month"]

threshold\_amount: int

minimum1

class ProjectSpendLimit: …

Represents a hard spend limit configured at the project level.

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

object: Literal["project.spend\_limit"]

The object type, which is always `project.spend_limit`.

threshold\_amount: int

### Update project spend limit

Python

import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
project_spend_limit = client.admin.organization.projects.spend_limit.update(
    project_id="proj_123",
    currency="USD",
    interval="month",
    threshold_amount=1,
)
print(project_spend_limit.currency)

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

<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/retrieve/ -->

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

[Spend Limit](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit)

# Retrieve project spend limit

admin.organization.projects.spend\_limit.retrieve(project\_id) -> [ProjectSpendLimit](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)) { currency, enforcement, interval, 2 more }

GET/organization/projects/{project\_id}/spend\_limit

Get a project’s hard spend limit.

##### ParametersExpand Collapse

project\_id: String

class ProjectSpendLimit { currency, enforcement, interval, 2 more }

Represents a hard spend limit configured at the project level.

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

object: :"project.spend\_limit"

The object type, which is always `project.spend_limit`.

threshold\_amount: Integer

### Retrieve project spend limit

Ruby

require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

project_spend_limit = openai.admin.organization.projects.spend_limit.retrieve("proj_123")

puts(project_spend_limit)

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

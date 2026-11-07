<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/automations/methods/delete/ -->

## Delete an automation

`beta.agents.automations.delete(automation_id) -> AutomationDeleted`

**delete** `/agents/automations/{automation_id}`

Deletes the automation and prevents future invocations without deleting its target session.

- `automation_id: String`

  `minLength: 0`, `maxLength: 1048576`

- `class AutomationDeleted`

  - `id: String`

    The deleted automation ID.

    `minLength: 0`

  - `deleted: bool`

    Always true.

  - `object: :"agent.automation.deleted"`

    Always `agent.automation.deleted`.

    - `:"agent.automation.deleted"`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

automation_deleted = openai.beta.agents.automations.delete("automation_id")

puts(automation_deleted)

  "deleted": true,
  "object": "agent.automation.deleted"

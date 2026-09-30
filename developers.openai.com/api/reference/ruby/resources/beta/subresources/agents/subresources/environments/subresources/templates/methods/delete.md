<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/delete/ -->

## Delete an agent environment template

`beta.agents.environments.templates.delete(environment_template_id) -> EnvironmentTemplateDeleted`

**delete** `/agents/environments/templates/{environment_template_id}`

Deletes reusable environment configuration and all confidential template inputs. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

- `environment_template_id: String`

- `class EnvironmentTemplateDeleted`

  A deleted reusable environment template.

  - `id: String`

    The ID of the deleted environment template.

  - `deleted: bool`

    Whether the environment template was deleted. Always `true`.

  - `object: :"agent.environment.template.deleted"`

    The object type. Always `agent.environment.template.deleted`.

    - `:"agent.environment.template.deleted"`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

environment_template_deleted = openai.beta.agents.environments.templates.delete("environment_template_id")

puts(environment_template_deleted)

  "deleted": true,
  "object": "agent.environment.template.deleted"

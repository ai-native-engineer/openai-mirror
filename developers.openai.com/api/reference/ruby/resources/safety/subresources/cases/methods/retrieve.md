<!-- source: https://developers.openai.com/api/reference/ruby/resources/safety/subresources/cases/methods/retrieve/ -->

## Get safety case

`safety.cases.retrieve(id) -> SafetyCase`

**get** `/safety/cases/{id}`

Get a safety case by ID.

- `id: String`

  Safety case ID

- `class SafetyCase`

  - `id: String`

  - `created_at: Integer`

  - `entity_identifier: String`

  - `notice: Notice{ type}`

    - `type: :warning | :deactivation`

      - `:warning`

      - `:deactivation`

  - `object: :"safety.case"`

    - `:"safety.case"`

  - `reason: String`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

safety_case = openai.safety.cases.retrieve("id")

puts(safety_case)

  "entity_identifier": "entity_identifier",
  "notice": {
    "type": "warning"
  "object": "safety.case",
  "reason": "reason"

<!-- source: https://developers.openai.com/api/reference/ruby/resources/safety/subresources/cases/ -->

# Cases

## Get safety case

`safety.cases.retrieve(id) -> SafetyCase`

**get** `/safety/cases/{id}`

Get a safety case by ID.

### Parameters

- `id: String`

  Safety case ID

### Returns

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

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

safety_case = openai.safety.cases.retrieve("id")

puts(safety_case)
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "entity_identifier": "entity_identifier",
  "notice": {
    "type": "warning"
  },
  "object": "safety.case",
  "reason": "reason"
}
```

## Domain Types

### Safety Case

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

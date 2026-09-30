<!-- source: https://developers.openai.com/api/reference/ruby/resources/safety/ -->

# Safety

# Alerts

## Get project safety alert

`safety.alerts.retrieve(id) -> SafetyAlert`

**get** `/safety/alerts/{id}`

Get a safety alert belonging to the authenticated API project.

### Parameters

- `id: String`

  Project safety alert ID

### Returns

- `class SafetyAlert`

  - `id: String`

  - `created_at: Integer`

  - `error_type: :potentially_unintended_data_transfer | :potentially_unintended_data_access | :potentially_unintended_destructive_activity | :other`

    - `:potentially_unintended_data_transfer`

    - `:potentially_unintended_data_access`

    - `:potentially_unintended_destructive_activity`

    - `:other`

  - `model: String`

  - `object: :"safety.alert"`

    - `:"safety.alert"`

  - `reason: String`

    A customer-safe description derived from error_type, or null for zero data retention requests.

  - `request_id: String`

  - `request_paused: bool`

    Whether block registration succeeded for this request. This does not confirm that response execution stopped.

  - `response_id: String`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

safety_alert = openai.safety.alerts.retrieve("id")

puts(safety_alert)
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "error_type": "potentially_unintended_data_transfer",
  "model": "model",
  "object": "safety.alert",
  "reason": "reason",
  "request_id": "request_id",
  "request_paused": true,
  "response_id": "response_id"
}
```

## Domain Types

### Safety Alert

- `class SafetyAlert`

  - `id: String`

  - `created_at: Integer`

  - `error_type: :potentially_unintended_data_transfer | :potentially_unintended_data_access | :potentially_unintended_destructive_activity | :other`

    - `:potentially_unintended_data_transfer`

    - `:potentially_unintended_data_access`

    - `:potentially_unintended_destructive_activity`

    - `:other`

  - `model: String`

  - `object: :"safety.alert"`

    - `:"safety.alert"`

  - `reason: String`

    A customer-safe description derived from error_type, or null for zero data retention requests.

  - `request_id: String`

  - `request_paused: bool`

    Whether block registration succeeded for this request. This does not confirm that response execution stopped.

  - `response_id: String`

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

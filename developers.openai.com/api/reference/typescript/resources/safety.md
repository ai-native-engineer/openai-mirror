<!-- source: https://developers.openai.com/api/reference/typescript/resources/safety/ -->

# Safety

# Alerts

## Get project safety alert

`client.safety.alerts.retrieve(stringid, RequestOptionsoptions?): SafetyAlert`

**get** `/safety/alerts/{id}`

Get a safety alert belonging to the authenticated API project.

### Parameters

- `id: string`

  Project safety alert ID

### Returns

- `SafetyAlert`

  - `id: string`

  - `created_at: number`

  - `error_type: "potentially_unintended_data_transfer" | "potentially_unintended_data_access" | "potentially_unintended_destructive_activity" | "other"`

    - `"potentially_unintended_data_transfer"`

    - `"potentially_unintended_data_access"`

    - `"potentially_unintended_destructive_activity"`

    - `"other"`

  - `model: string`

  - `object: "safety.alert"`

    - `"safety.alert"`

  - `reason: string | null`

    A customer-safe description derived from error_type, or null for zero data retention requests.

  - `request_id: string`

  - `request_paused: boolean`

    Whether block registration succeeded for this request. This does not confirm that response execution stopped.

  - `response_id: string`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const safetyAlert = await client.safety.alerts.retrieve('id');

console.log(safetyAlert.id);
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

- `SafetyAlert`

  - `id: string`

  - `created_at: number`

  - `error_type: "potentially_unintended_data_transfer" | "potentially_unintended_data_access" | "potentially_unintended_destructive_activity" | "other"`

    - `"potentially_unintended_data_transfer"`

    - `"potentially_unintended_data_access"`

    - `"potentially_unintended_destructive_activity"`

    - `"other"`

  - `model: string`

  - `object: "safety.alert"`

    - `"safety.alert"`

  - `reason: string | null`

    A customer-safe description derived from error_type, or null for zero data retention requests.

  - `request_id: string`

  - `request_paused: boolean`

    Whether block registration succeeded for this request. This does not confirm that response execution stopped.

  - `response_id: string`

# Cases

## Get safety case

`client.safety.cases.retrieve(stringid, RequestOptionsoptions?): SafetyCase`

**get** `/safety/cases/{id}`

Get a safety case by ID.

### Parameters

- `id: string`

  Safety case ID

### Returns

- `SafetyCase`

  - `id: string`

  - `created_at: number`

  - `entity_identifier: string`

  - `notice: Notice`

    - `type: "warning" | "deactivation"`

      - `"warning"`

      - `"deactivation"`

  - `object: "safety.case"`

    - `"safety.case"`

  - `reason: string | null`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const safetyCase = await client.safety.cases.retrieve('id');

console.log(safetyCase.id);
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

- `SafetyCase`

  - `id: string`

  - `created_at: number`

  - `entity_identifier: string`

  - `notice: Notice`

    - `type: "warning" | "deactivation"`

      - `"warning"`

      - `"deactivation"`

  - `object: "safety.case"`

    - `"safety.case"`

  - `reason: string | null`

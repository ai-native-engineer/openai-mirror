<!-- source: https://developers.openai.com/api/reference/typescript/resources/safety/subresources/alerts/methods/retrieve/ -->

## Get project safety alert

`client.safety.alerts.retrieve(stringid, RequestOptionsoptions?): SafetyAlert`

**get** `/safety/alerts/{id}`

Get a safety alert belonging to the authenticated API project.

- `id: string`

  Project safety alert ID

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

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const safetyAlert = await client.safety.alerts.retrieve('id');

console.log(safetyAlert.id);

  "error_type": "potentially_unintended_data_transfer",
  "model": "model",
  "object": "safety.alert",
  "reason": "reason",
  "request_id": "request_id",
  "request_paused": true,
  "response_id": "response_id"

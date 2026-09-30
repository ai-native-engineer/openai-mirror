<!-- source: https://developers.openai.com/api/reference/cli/resources/safety/subresources/alerts/methods/retrieve/ -->

## Get project safety alert

`$ openai safety:alerts retrieve`

**get** `/safety/alerts/{id}`

Get a safety alert belonging to the authenticated API project.

- `--id: string`

  Project safety alert ID

- `safety_alert: object { id, created_at, error_type, 6 more }`

  - `id: string`

  - `created_at: number`

  - `error_type: "potentially_unintended_data_transfer" or "potentially_unintended_data_access" or "potentially_unintended_destructive_activity" or "other"`

    - `"potentially_unintended_data_transfer"`

    - `"potentially_unintended_data_access"`

    - `"potentially_unintended_destructive_activity"`

    - `"other"`

  - `model: string`

  - `object: "safety.alert"`

  - `reason: string`

    A customer-safe description derived from error_type, or null for zero data retention requests.

  - `request_id: string`

  - `request_paused: boolean`

    Whether block registration succeeded for this request. This does not confirm that response execution stopped.

  - `response_id: string`

```cli
openai safety:alerts retrieve \
  --api-key 'My API Key' \
  --id id

  "error_type": "potentially_unintended_data_transfer",
  "model": "model",
  "object": "safety.alert",
  "reason": "reason",
  "request_id": "request_id",
  "request_paused": true,
  "response_id": "response_id"

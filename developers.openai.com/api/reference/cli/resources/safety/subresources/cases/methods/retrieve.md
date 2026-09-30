<!-- source: https://developers.openai.com/api/reference/cli/resources/safety/subresources/cases/methods/retrieve/ -->

## Get safety case

`$ openai safety:cases retrieve`

**get** `/safety/cases/{id}`

Get a safety case by ID.

- `--id: string`

  Safety case ID

- `safety_case: object { id, created_at, entity_identifier, 3 more }`

  - `id: string`

  - `created_at: number`

  - `entity_identifier: string`

  - `notice: object { type }`

    - `type: "warning" or "deactivation"`

      - `"warning"`

      - `"deactivation"`

  - `object: "safety.case"`

  - `reason: string`

```cli
openai safety:cases retrieve \
  --api-key 'My API Key' \
  --id id

  "entity_identifier": "entity_identifier",
  "notice": {
    "type": "warning"
  "object": "safety.case",
  "reason": "reason"

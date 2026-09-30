<!-- source: https://developers.openai.com/api/reference/cli/resources/safety/subresources/cases/ -->

# Cases

## Get safety case

`$ openai safety:cases retrieve`

**get** `/safety/cases/{id}`

Get a safety case by ID.

### Parameters

- `--id: string`

  Safety case ID

### Returns

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

### Example

```cli
openai safety:cases retrieve \
  --api-key 'My API Key' \
  --id id
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

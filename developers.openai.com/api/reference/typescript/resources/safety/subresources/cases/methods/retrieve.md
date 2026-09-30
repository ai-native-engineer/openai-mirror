<!-- source: https://developers.openai.com/api/reference/typescript/resources/safety/subresources/cases/methods/retrieve/ -->

## Get safety case

`client.safety.cases.retrieve(stringid, RequestOptionsoptions?): SafetyCase`

**get** `/safety/cases/{id}`

Get a safety case by ID.

- `id: string`

  Safety case ID

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

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const safetyCase = await client.safety.cases.retrieve('id');

console.log(safetyCase.id);

  "entity_identifier": "entity_identifier",
  "notice": {
    "type": "warning"
  "object": "safety.case",
  "reason": "reason"

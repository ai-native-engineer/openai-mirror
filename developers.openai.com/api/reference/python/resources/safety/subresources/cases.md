<!-- source: https://developers.openai.com/api/reference/python/resources/safety/subresources/cases/ -->

# Cases

## Get safety case

`safety.cases.retrieve(strid)  -> SafetyCase`

**get** `/safety/cases/{id}`

Get a safety case by ID.

### Parameters

- `id: str`

  Safety case ID

### Returns

- `class SafetyCase: …`

  - `id: str`

  - `created_at: int`

  - `entity_identifier: str`

  - `notice: Notice`

    - `type: Literal["warning", "deactivation"]`

      - `"warning"`

      - `"deactivation"`

  - `object: Literal["safety.case"]`

    - `"safety.case"`

  - `reason: Optional[str]`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
safety_case = client.safety.cases.retrieve(
    "id",
)
print(safety_case.id)
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

- `class SafetyCase: …`

  - `id: str`

  - `created_at: int`

  - `entity_identifier: str`

  - `notice: Notice`

    - `type: Literal["warning", "deactivation"]`

      - `"warning"`

      - `"deactivation"`

  - `object: Literal["safety.case"]`

    - `"safety.case"`

  - `reason: Optional[str]`

<!-- source: https://developers.openai.com/api/reference/resources/safety/subresources/cases/methods/retrieve/ -->

[Safety](/api/reference/resources/safety)

[Cases](/api/reference/resources/safety/subresources/cases)

# Get safety case

GET/safety/cases/{id}

Get a safety case by ID.

Safety case ID

maxLength128

SafetyCase object { id, created\_at, entity\_identifier, 3 more }

entity\_identifier: string

notice: object { type }

type: "warning" or "deactivation"

"warning"

"deactivation"

object: "safety.case"

reason: string or null

### Get safety case

curl https://api.openai.com/v1/safety/cases/C-abc123 \

  "id": "C-abc123",
  "object": "safety.case",
  "created_at": 1787659200,
  "entity_identifier": "safety-id-123",
  "reason": "cyber_abuse",
  "notice": {"type": "warning"}

  "id": "C-abc123",
  "object": "safety.case",
  "created_at": 1787659200,
  "entity_identifier": "safety-id-123",
  "reason": "cyber_abuse",
  "notice": {"type": "warning"}

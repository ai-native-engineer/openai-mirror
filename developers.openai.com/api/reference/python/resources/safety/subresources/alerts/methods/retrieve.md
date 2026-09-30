<!-- source: https://developers.openai.com/api/reference/python/resources/safety/subresources/alerts/methods/retrieve/ -->

## Get project safety alert

`safety.alerts.retrieve(strid)  -> SafetyAlert`

**get** `/safety/alerts/{id}`

Get a safety alert belonging to the authenticated API project.

- `id: str`

  Project safety alert ID

- `class SafetyAlert: …`

  - `id: str`

  - `created_at: int`

  - `error_type: Literal["potentially_unintended_data_transfer", "potentially_unintended_data_access", "potentially_unintended_destructive_activity", "other"]`

    - `"potentially_unintended_data_transfer"`

    - `"potentially_unintended_data_access"`

    - `"potentially_unintended_destructive_activity"`

    - `"other"`

  - `model: str`

  - `object: Literal["safety.alert"]`

    - `"safety.alert"`

  - `reason: Optional[str]`

    A customer-safe description derived from error_type, or null for zero data retention requests.

  - `request_id: str`

  - `request_paused: bool`

    Whether block registration succeeded for this request. This does not confirm that response execution stopped.

  - `response_id: str`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
safety_alert = client.safety.alerts.retrieve(
    "id",
print(safety_alert.id)

  "error_type": "potentially_unintended_data_transfer",
  "model": "model",
  "object": "safety.alert",
  "reason": "reason",
  "request_id": "request_id",
  "request_paused": true,
  "response_id": "response_id"

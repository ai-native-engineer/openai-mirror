<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/automations/methods/delete/ -->

## Delete an automation

`beta.agents.automations.delete(strautomation_id)  -> AutomationDeleted`

**delete** `/agents/automations/{automation_id}`

Deletes the automation and prevents future invocations without deleting its target session.

- `automation_id: str`

  `minLength: 0`, `maxLength: 1048576`

- `class AutomationDeleted: …`

  - `id: str`

    The deleted automation ID.

    `minLength: 0`

  - `deleted: bool`

    Always true.

  - `object: Literal["agent.automation.deleted"]`

    Always `agent.automation.deleted`.

    - `"agent.automation.deleted"`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
automation_deleted = client.beta.agents.automations.delete(
    "automation_id",
print(automation_deleted.id)

  "deleted": true,
  "object": "agent.automation.deleted"

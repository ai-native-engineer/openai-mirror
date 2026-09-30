<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/delete/ -->

## Delete an agent environment template

`beta.agents.environments.templates.delete(strenvironment_template_id)  -> EnvironmentTemplateDeleted`

**delete** `/agents/environments/templates/{environment_template_id}`

Deletes reusable environment configuration and all confidential template inputs. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

- `environment_template_id: str`

- `class EnvironmentTemplateDeleted: …`

  A deleted reusable environment template.

  - `id: str`

    The ID of the deleted environment template.

  - `deleted: bool`

    Whether the environment template was deleted. Always `true`.

  - `object: Literal["agent.environment.template.deleted"]`

    The object type. Always `agent.environment.template.deleted`.

    - `"agent.environment.template.deleted"`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
environment_template_deleted = client.beta.agents.environments.templates.delete(
    "environment_template_id",
print(environment_template_deleted.id)

  "deleted": true,
  "object": "agent.environment.template.deleted"

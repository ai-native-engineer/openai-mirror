<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/delete/ -->

## Delete an agent environment template

`client.beta.agents.environments.templates.delete(stringenvironmentTemplateID, RequestOptionsoptions?): EnvironmentTemplateDeleted`

**delete** `/agents/environments/templates/{environment_template_id}`

Deletes reusable environment configuration and all confidential template inputs. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

- `environmentTemplateID: string`

- `EnvironmentTemplateDeleted`

  A deleted reusable environment template.

  - `id: string`

    The ID of the deleted environment template.

  - `deleted: boolean`

    Whether the environment template was deleted. Always `true`.

  - `object: "agent.environment.template.deleted"`

    The object type. Always `agent.environment.template.deleted`.

    - `"agent.environment.template.deleted"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const environmentTemplateDeleted = await client.beta.agents.environments.templates.delete(
  'environment_template_id',
);

console.log(environmentTemplateDeleted.id);

  "deleted": true,
  "object": "agent.environment.template.deleted"

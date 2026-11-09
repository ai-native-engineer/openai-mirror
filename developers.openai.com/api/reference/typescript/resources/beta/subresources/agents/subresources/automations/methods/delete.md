<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/automations/methods/delete/ -->

## Delete an automation

`client.beta.agents.automations.delete(stringautomationID, RequestOptionsoptions?): AutomationDeleted`

**delete** `/agents/automations/{automation_id}`

Deletes the automation and prevents future invocations without deleting its target session.

- `automationID: string`

  `minLength: 0`, `maxLength: 1048576`

- `AutomationDeleted`

  - `id: string`

    The deleted automation ID.

    `minLength: 0`

  - `deleted: boolean`

    Always true.

  - `object: "agent.automation.deleted"`

    Always `agent.automation.deleted`.

    - `"agent.automation.deleted"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const automationDeleted = await client.beta.agents.automations.delete('automation_id');

console.log(automationDeleted.id);

  "deleted": true,
  "object": "agent.automation.deleted"

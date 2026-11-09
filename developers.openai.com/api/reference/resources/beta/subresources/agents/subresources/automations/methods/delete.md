<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/automations/methods/delete/ -->

> For the complete documentation index, see [llms.txt](/llms.txt). Markdown versions of documentation pages are available by appending `.md` to the page URL.

## Delete an automation

**delete** `/agents/automations/{automation_id}`

Deletes the automation and prevents future invocations without deleting its target session.

### Path Parameters

- `automation_id: string`

  `minLength: 0`, `maxLength: 1048576`

- `AutomationDeleted object { id, deleted, object }`

  - `id: string`

    The deleted automation ID.

    `minLength: 0`

  - `deleted: boolean`

    Always true.

  - `object: "agent.automation.deleted" (default: "agent.automation.deleted")`

    Always `agent.automation.deleted`.

    - `"agent.automation.deleted"`

```http
curl https://api.openai.com/v1/agents/automations/$AUTOMATION_ID \
    -X DELETE \
    -H 'OpenAI-Beta: agents=v1' \
    -H "Authorization: Bearer $OPENAI_API_KEY"

  "deleted": true,
  "object": "agent.automation.deleted"

<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/delete/ -->

[Environments](/api/reference/resources/beta/subresources/agents/subresources/environments)

[Templates](/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/templates)

# Delete an agent environment template

DELETE/agents/environments/templates/{environment\_template\_id}

Deletes reusable environment configuration and all confidential template inputs. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

environment\_template\_id: string

EnvironmentTemplateDeleted object { id, deleted, object }

A deleted reusable environment template.

The ID of the deleted environment template.

deleted: boolean

Whether the environment template was deleted. Always `true`.

object: "agent.environment.template.deleted"

The object type. Always `agent.environment.template.deleted`.

### Delete an agent environment template

curl https://api.openai.com/v1/agents/environments/templates/$ENVIRONMENT_TEMPLATE_ID \
    -X DELETE \

  "deleted": true,
  "object": "agent.environment.template.deleted"

  "deleted": true,
  "object": "agent.environment.template.deleted"

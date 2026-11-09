<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/delete/ -->

## Delete Platform workload identity federation rule

`admin.organization.workload_identity_providers.federation_rules.delete(strworkload_identity_federation_rule_id, FederationRuleDeleteParams**kwargs)  -> FederationRuleDeleted`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Delete a federation rule to a project service account.

- `workload_identity_provider_id: str`

  `minLength: 1`

- `workload_identity_federation_rule_id: str`

  `minLength: 1`

- `class FederationRuleDeleted: …`

  - `id: str`

  - `deleted: bool`

  - `object: Literal["organization.workload_identity_federation_rule.deleted"]`

    - `"organization.workload_identity_federation_rule.deleted"`

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
federation_rule_deleted = client.admin.organization.workload_identity_providers.federation_rules.delete(
    workload_identity_federation_rule_id="x",
    workload_identity_provider_id="x",
print(federation_rule_deleted.id)

  "deleted": true,
  "object": "organization.workload_identity_federation_rule.deleted"

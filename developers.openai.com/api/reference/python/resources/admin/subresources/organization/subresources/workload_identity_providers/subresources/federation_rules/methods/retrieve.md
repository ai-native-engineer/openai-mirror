<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/retrieve/ -->

## Retrieve Platform workload identity federation rule

`admin.organization.workload_identity_providers.federation_rules.retrieve(strworkload_identity_federation_rule_id, FederationRuleRetrieveParams**kwargs)  -> FederationRule`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Retrieve a federation rule owned by the authenticated organization and provider.

- `workload_identity_provider_id: str`

  `minLength: 1`

- `workload_identity_federation_rule_id: str`

  `minLength: 1`

- `class FederationRule: …`

  - `id: str`

  - `attribute_matchers: Dict[str, Union[str, bool, Union[int, float]]]`

    - `str`

    - `bool`

    - `Union[int, float]`

      - `int`

      - `float`

  - `created_at: int`

  - `description: Optional[str]`

  - `enabled: bool`

  - `name: Optional[str]`

  - `object: Literal["organization.workload_identity_federation_rule"]`

    - `"organization.workload_identity_federation_rule"`

  - `permissions: Permissions`

    - `class PermissionsServiceAccountDefault: …`

      - `type: Literal["service_account_default"]`

        - `"service_account_default"`

    - `class PermissionsRestricted: …`

      - `scopes: List[str]`

      - `type: Literal["restricted"]`

        - `"restricted"`

  - `project_id: str`

  - `service_account_id: str`

  - `updated_at: int`

  - `workload_identity_provider_id: str`

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
federation_rule = client.admin.organization.workload_identity_providers.federation_rules.retrieve(
    workload_identity_federation_rule_id="x",
    workload_identity_provider_id="x",
print(federation_rule.id)

  "attribute_matchers": {
    "foo": "string"
  "enabled": true,
  "object": "organization.workload_identity_federation_rule",
  "permissions": {
    "type": "service_account_default"
  "project_id": "project_id",
  "service_account_id": "service_account_id",
  "updated_at": 0,
  "workload_identity_provider_id": "workload_identity_provider_id"

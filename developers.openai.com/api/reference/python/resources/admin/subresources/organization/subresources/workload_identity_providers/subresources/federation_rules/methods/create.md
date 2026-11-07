<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/create/ -->

## Create Platform workload identity federation rule

`admin.organization.workload_identity_providers.federation_rules.create(strworkload_identity_provider_id, FederationRuleCreateParams**kwargs)  -> FederationRule`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

Bind verified token attributes to an existing project service account.

- `workload_identity_provider_id: str`

  `minLength: 1`

- `attribute_matchers: Dict[str, Union[str, bool, Union[int, float]]]`

  - `str`

  - `bool`

  - `Union[int, float]`

    - `int`

    - `float`

- `project_id: str`

  `minLength: 1`

- `service_account_id: str`

  `minLength: 1`

- `description: Optional[str]`

- `enabled: Optional[bool]`

- `name: Optional[str]`

- `permissions: Optional[Permissions]`

  - `class PermissionsServiceAccountDefault: …`

    - `type: Literal["service_account_default"]`

      - `"service_account_default"`

  - `class PermissionsRestricted: …`

    - `scopes: Sequence[str]`

      `minItems: 1`

    - `type: Literal["restricted"]`

      - `"restricted"`

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
federation_rule = client.admin.organization.workload_identity_providers.federation_rules.create(
    workload_identity_provider_id="x",
    attribute_matchers={
        "foo": "string"
    project_id="x",
    service_account_id="x",
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

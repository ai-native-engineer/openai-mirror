<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/list/ -->

## List Platform workload identity federation rules

`admin.organization.workload_identity_providers.federation_rules.list(strworkload_identity_provider_id, FederationRuleListParams**kwargs)  -> SyncCursorPage[FederationRule]`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

List the provider's federation rules to project service accounts.

- `workload_identity_provider_id: str`

  `minLength: 1`

- `after: Optional[str]`

  `minLength: 1`

- `limit: Optional[int]`

  `minimum: 1`, `maximum: 100`

- `order: Optional[Union[Literal["asc", "desc"]]]`

  - `Literal["asc", "desc"]`

    - `"asc"`

    - `"desc"`

- `service_account_id: Optional[str]`

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
page = client.admin.organization.workload_identity_providers.federation_rules.list(
    workload_identity_provider_id="x",
page = page.data[0]
print(page.id)

  "data": [
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
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

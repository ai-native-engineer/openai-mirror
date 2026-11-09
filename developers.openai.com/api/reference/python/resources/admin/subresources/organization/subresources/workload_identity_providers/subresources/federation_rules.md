<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/ -->

# Federation Rules

## Create Platform workload identity federation rule

`admin.organization.workload_identity_providers.federation_rules.create(strworkload_identity_provider_id, FederationRuleCreateParams**kwargs)  -> FederationRule`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

Bind verified token attributes to an existing project service account.

### Parameters

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

### Returns

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

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
federation_rule = client.admin.organization.workload_identity_providers.federation_rules.create(
    workload_identity_provider_id="x",
    attribute_matchers={
        "foo": "string"
    },
    project_id="x",
    service_account_id="x",
)
print(federation_rule.id)
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_matchers": {
    "foo": "string"
  },
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "name": "name",
  "object": "organization.workload_identity_federation_rule",
  "permissions": {
    "type": "service_account_default"
  },
  "project_id": "project_id",
  "service_account_id": "service_account_id",
  "updated_at": 0,
  "workload_identity_provider_id": "workload_identity_provider_id"
}
```

## Delete Platform workload identity federation rule

`admin.organization.workload_identity_providers.federation_rules.delete(strworkload_identity_federation_rule_id, FederationRuleDeleteParams**kwargs)  -> FederationRuleDeleted`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Delete a federation rule to a project service account.

### Parameters

- `workload_identity_provider_id: str`

  `minLength: 1`

- `workload_identity_federation_rule_id: str`

  `minLength: 1`

### Returns

- `class FederationRuleDeleted: …`

  - `id: str`

  - `deleted: bool`

  - `object: Literal["organization.workload_identity_federation_rule.deleted"]`

    - `"organization.workload_identity_federation_rule.deleted"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
federation_rule_deleted = client.admin.organization.workload_identity_providers.federation_rules.delete(
    workload_identity_federation_rule_id="x",
    workload_identity_provider_id="x",
)
print(federation_rule_deleted.id)
```

#### 200 — Example

```json
{
  "id": "id",
  "deleted": true,
  "object": "organization.workload_identity_federation_rule.deleted"
}
```

## List Platform workload identity federation rules

`admin.organization.workload_identity_providers.federation_rules.list(strworkload_identity_provider_id, FederationRuleListParams**kwargs)  -> SyncCursorPage[FederationRule]`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

List the provider's federation rules to project service accounts.

### Parameters

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

### Returns

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

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
page = client.admin.organization.workload_identity_providers.federation_rules.list(
    workload_identity_provider_id="x",
)
page = page.data[0]
print(page.id)
```

#### 200 — Example

```json
{
  "data": [
    {
      "id": "id",
      "attribute_matchers": {
        "foo": "string"
      },
      "created_at": 0,
      "description": "description",
      "enabled": true,
      "name": "name",
      "object": "organization.workload_identity_federation_rule",
      "permissions": {
        "type": "service_account_default"
      },
      "project_id": "project_id",
      "service_account_id": "service_account_id",
      "updated_at": 0,
      "workload_identity_provider_id": "workload_identity_provider_id"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve Platform workload identity federation rule

`admin.organization.workload_identity_providers.federation_rules.retrieve(strworkload_identity_federation_rule_id, FederationRuleRetrieveParams**kwargs)  -> FederationRule`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Retrieve a federation rule owned by the authenticated organization and provider.

### Parameters

- `workload_identity_provider_id: str`

  `minLength: 1`

- `workload_identity_federation_rule_id: str`

  `minLength: 1`

### Returns

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

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
federation_rule = client.admin.organization.workload_identity_providers.federation_rules.retrieve(
    workload_identity_federation_rule_id="x",
    workload_identity_provider_id="x",
)
print(federation_rule.id)
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_matchers": {
    "foo": "string"
  },
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "name": "name",
  "object": "organization.workload_identity_federation_rule",
  "permissions": {
    "type": "service_account_default"
  },
  "project_id": "project_id",
  "service_account_id": "service_account_id",
  "updated_at": 0,
  "workload_identity_provider_id": "workload_identity_provider_id"
}
```

## Update Platform workload identity federation rule

`admin.organization.workload_identity_providers.federation_rules.update(strworkload_identity_federation_rule_id, FederationRuleUpdateParams**kwargs)  -> FederationRule`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Update supplied matcher, permission, metadata, or enabled fields.

### Parameters

- `workload_identity_provider_id: str`

  `minLength: 1`

- `workload_identity_federation_rule_id: str`

  `minLength: 1`

- `attribute_matchers: Optional[Dict[str, Union[str, bool, Union[int, float]]]]`

  - `str`

  - `bool`

  - `Union[int, float]`

    - `int`

    - `float`

- `description: Optional[str]`

- `enabled: Optional[bool]`

- `name: Optional[str]`

- `permissions: Optional[Permissions]`

  - `class PermissionsDefaultPermissionsParam: …`

    - `type: Literal["service_account_default"]`

      - `"service_account_default"`

  - `class PermissionsRestrictedPermissionsParam: …`

    - `scopes: Sequence[str]`

      `minItems: 1`

    - `type: Literal["restricted"]`

      - `"restricted"`

### Returns

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

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
federation_rule = client.admin.organization.workload_identity_providers.federation_rules.update(
    workload_identity_federation_rule_id="x",
    workload_identity_provider_id="x",
)
print(federation_rule.id)
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_matchers": {
    "foo": "string"
  },
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "name": "name",
  "object": "organization.workload_identity_federation_rule",
  "permissions": {
    "type": "service_account_default"
  },
  "project_id": "project_id",
  "service_account_id": "service_account_id",
  "updated_at": 0,
  "workload_identity_provider_id": "workload_identity_provider_id"
}
```

## Domain Types

### Federation Rule

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

### Federation Rule Deleted

- `class FederationRuleDeleted: …`

  - `id: str`

  - `deleted: bool`

  - `object: Literal["organization.workload_identity_federation_rule.deleted"]`

    - `"organization.workload_identity_federation_rule.deleted"`

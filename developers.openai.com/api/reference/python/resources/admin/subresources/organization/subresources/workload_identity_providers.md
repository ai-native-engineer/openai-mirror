<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/workload_identity_providers/ -->

# Workload Identity Providers

## Create Platform workload identity provider

`admin.organization.workload_identity_providers.create(WorkloadIdentityProviderCreateParams**kwargs)  -> WorkloadIdentityProvider`

**post** `/organization/workload_identity_providers`

Register an OIDC provider for keyless project service-account authentication.

### Parameters

- `audience: str`

  `minLength: 1`

- `issuer: str`

  `minLength: 1`

- `name: str`

  `minLength: 1`

- `type: Literal["oidc"]`

  - `"oidc"`

- `attribute_transformations: Optional[Iterable[AttributeTransformation]]`

  `maxItems: 20`

  - `attribute: str`

    `minLength: 1`, `maxLength: 256`

  - `expression: str`

    `minLength: 1`, `maxLength: 4096`

- `description: Optional[str]`

- `enabled: Optional[bool]`

- `verification: Optional[Verification]`

  - `class VerificationDiscovery: …`

    - `discovery_url: Optional[str]`

    - `type: Literal["discovery"]`

      - `"discovery"`

  - `class VerificationUploadedJwks: …`

    - `jwks: Dict[str, object]`

    - `type: Literal["uploaded_jwks"]`

      - `"uploaded_jwks"`

### Returns

- `class WorkloadIdentityProvider: …`

  - `id: str`

  - `attribute_transformations: List[AttributeTransformation]`

    - `attribute: str`

    - `expression: str`

  - `audience: str`

  - `created_at: int`

  - `description: Optional[str]`

  - `enabled: bool`

  - `issuer: str`

  - `name: str`

  - `object: Literal["organization.workload_identity_provider"]`

    - `"organization.workload_identity_provider"`

  - `type: Literal["oidc"]`

    - `"oidc"`

  - `updated_at: int`

  - `verification: Verification`

    - `class VerificationDiscovery: …`

      - `discovery_url: Optional[str]`

      - `type: Literal["discovery"]`

        - `"discovery"`

    - `class VerificationUploadedJwks: …`

      - `jwks: Dict[str, object]`

      - `type: Literal["uploaded_jwks"]`

        - `"uploaded_jwks"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
workload_identity_provider = client.admin.organization.workload_identity_providers.create(
    audience="x",
    issuer="x",
    name="x",
    type="oidc",
)
print(workload_identity_provider.id)
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_transformations": [
    {
      "attribute": "attribute",
      "expression": "expression"
    }
  ],
  "audience": "audience",
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "issuer": "issuer",
  "name": "name",
  "object": "organization.workload_identity_provider",
  "type": "oidc",
  "updated_at": 0,
  "verification": {
    "discovery_url": "discovery_url",
    "type": "discovery"
  }
}
```

## Delete Platform workload identity provider

`admin.organization.workload_identity_providers.delete(strworkload_identity_provider_id)  -> WorkloadIdentityProviderDeleted`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Delete a provider after deleting all its federation rules.

### Parameters

- `workload_identity_provider_id: str`

  `minLength: 1`

### Returns

- `class WorkloadIdentityProviderDeleted: …`

  - `id: str`

  - `deleted: bool`

  - `object: Literal["organization.workload_identity_provider.deleted"]`

    - `"organization.workload_identity_provider.deleted"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
workload_identity_provider_deleted = client.admin.organization.workload_identity_providers.delete(
    "x",
)
print(workload_identity_provider_deleted.id)
```

#### 200 — Example

```json
{
  "id": "id",
  "deleted": true,
  "object": "organization.workload_identity_provider.deleted"
}
```

## List Platform workload identity providers

`admin.organization.workload_identity_providers.list(WorkloadIdentityProviderListParams**kwargs)  -> SyncCursorPage[WorkloadIdentityProvider]`

**get** `/organization/workload_identity_providers`

List OIDC providers in the authenticated Admin API key's organization.

### Parameters

- `after: Optional[str]`

  `minLength: 1`

- `limit: Optional[int]`

  `minimum: 1`, `maximum: 100`

- `order: Optional[Union[Literal["asc", "desc"]]]`

  - `Literal["asc", "desc"]`

    - `"asc"`

    - `"desc"`

### Returns

- `class WorkloadIdentityProvider: …`

  - `id: str`

  - `attribute_transformations: List[AttributeTransformation]`

    - `attribute: str`

    - `expression: str`

  - `audience: str`

  - `created_at: int`

  - `description: Optional[str]`

  - `enabled: bool`

  - `issuer: str`

  - `name: str`

  - `object: Literal["organization.workload_identity_provider"]`

    - `"organization.workload_identity_provider"`

  - `type: Literal["oidc"]`

    - `"oidc"`

  - `updated_at: int`

  - `verification: Verification`

    - `class VerificationDiscovery: …`

      - `discovery_url: Optional[str]`

      - `type: Literal["discovery"]`

        - `"discovery"`

    - `class VerificationUploadedJwks: …`

      - `jwks: Dict[str, object]`

      - `type: Literal["uploaded_jwks"]`

        - `"uploaded_jwks"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
page = client.admin.organization.workload_identity_providers.list()
page = page.data[0]
print(page.id)
```

#### 200 — Example

```json
{
  "data": [
    {
      "id": "id",
      "attribute_transformations": [
        {
          "attribute": "attribute",
          "expression": "expression"
        }
      ],
      "audience": "audience",
      "created_at": 0,
      "description": "description",
      "enabled": true,
      "issuer": "issuer",
      "name": "name",
      "object": "organization.workload_identity_provider",
      "type": "oidc",
      "updated_at": 0,
      "verification": {
        "discovery_url": "discovery_url",
        "type": "discovery"
      }
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve Platform workload identity provider

`admin.organization.workload_identity_providers.retrieve(strworkload_identity_provider_id)  -> WorkloadIdentityProvider`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Retrieve an OIDC provider in the authenticated organization.

### Parameters

- `workload_identity_provider_id: str`

  `minLength: 1`

### Returns

- `class WorkloadIdentityProvider: …`

  - `id: str`

  - `attribute_transformations: List[AttributeTransformation]`

    - `attribute: str`

    - `expression: str`

  - `audience: str`

  - `created_at: int`

  - `description: Optional[str]`

  - `enabled: bool`

  - `issuer: str`

  - `name: str`

  - `object: Literal["organization.workload_identity_provider"]`

    - `"organization.workload_identity_provider"`

  - `type: Literal["oidc"]`

    - `"oidc"`

  - `updated_at: int`

  - `verification: Verification`

    - `class VerificationDiscovery: …`

      - `discovery_url: Optional[str]`

      - `type: Literal["discovery"]`

        - `"discovery"`

    - `class VerificationUploadedJwks: …`

      - `jwks: Dict[str, object]`

      - `type: Literal["uploaded_jwks"]`

        - `"uploaded_jwks"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
workload_identity_provider = client.admin.organization.workload_identity_providers.retrieve(
    "x",
)
print(workload_identity_provider.id)
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_transformations": [
    {
      "attribute": "attribute",
      "expression": "expression"
    }
  ],
  "audience": "audience",
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "issuer": "issuer",
  "name": "name",
  "object": "organization.workload_identity_provider",
  "type": "oidc",
  "updated_at": 0,
  "verification": {
    "discovery_url": "discovery_url",
    "type": "discovery"
  }
}
```

## Update Platform workload identity provider

`admin.organization.workload_identity_providers.update(strworkload_identity_provider_id, WorkloadIdentityProviderUpdateParams**kwargs)  -> WorkloadIdentityProvider`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Update supplied provider fields, preserving omitted fields.

### Parameters

- `workload_identity_provider_id: str`

  `minLength: 1`

- `attribute_transformations: Optional[Iterable[AttributeTransformation]]`

  `maxItems: 20`

  - `attribute: str`

    `minLength: 1`, `maxLength: 256`

  - `expression: str`

    `minLength: 1`, `maxLength: 4096`

- `audience: Optional[str]`

  `minLength: 1`

- `description: Optional[str]`

- `enabled: Optional[bool]`

- `issuer: Optional[str]`

  `minLength: 1`

- `name: Optional[str]`

  `minLength: 1`

- `verification: Optional[Verification]`

  - `class VerificationDiscoveryVerificationParam: …`

    - `discovery_url: Optional[str]`

    - `type: Literal["discovery"]`

      - `"discovery"`

  - `class VerificationUploadedJwksVerificationParam: …`

    - `jwks: Dict[str, object]`

    - `type: Literal["uploaded_jwks"]`

      - `"uploaded_jwks"`

### Returns

- `class WorkloadIdentityProvider: …`

  - `id: str`

  - `attribute_transformations: List[AttributeTransformation]`

    - `attribute: str`

    - `expression: str`

  - `audience: str`

  - `created_at: int`

  - `description: Optional[str]`

  - `enabled: bool`

  - `issuer: str`

  - `name: str`

  - `object: Literal["organization.workload_identity_provider"]`

    - `"organization.workload_identity_provider"`

  - `type: Literal["oidc"]`

    - `"oidc"`

  - `updated_at: int`

  - `verification: Verification`

    - `class VerificationDiscovery: …`

      - `discovery_url: Optional[str]`

      - `type: Literal["discovery"]`

        - `"discovery"`

    - `class VerificationUploadedJwks: …`

      - `jwks: Dict[str, object]`

      - `type: Literal["uploaded_jwks"]`

        - `"uploaded_jwks"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
workload_identity_provider = client.admin.organization.workload_identity_providers.update(
    workload_identity_provider_id="x",
)
print(workload_identity_provider.id)
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_transformations": [
    {
      "attribute": "attribute",
      "expression": "expression"
    }
  ],
  "audience": "audience",
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "issuer": "issuer",
  "name": "name",
  "object": "organization.workload_identity_provider",
  "type": "oidc",
  "updated_at": 0,
  "verification": {
    "discovery_url": "discovery_url",
    "type": "discovery"
  }
}
```

## Domain Types

### Workload Identity Provider

- `class WorkloadIdentityProvider: …`

  - `id: str`

  - `attribute_transformations: List[AttributeTransformation]`

    - `attribute: str`

    - `expression: str`

  - `audience: str`

  - `created_at: int`

  - `description: Optional[str]`

  - `enabled: bool`

  - `issuer: str`

  - `name: str`

  - `object: Literal["organization.workload_identity_provider"]`

    - `"organization.workload_identity_provider"`

  - `type: Literal["oidc"]`

    - `"oidc"`

  - `updated_at: int`

  - `verification: Verification`

    - `class VerificationDiscovery: …`

      - `discovery_url: Optional[str]`

      - `type: Literal["discovery"]`

        - `"discovery"`

    - `class VerificationUploadedJwks: …`

      - `jwks: Dict[str, object]`

      - `type: Literal["uploaded_jwks"]`

        - `"uploaded_jwks"`

### Workload Identity Provider Deleted

- `class WorkloadIdentityProviderDeleted: …`

  - `id: str`

  - `deleted: bool`

  - `object: Literal["organization.workload_identity_provider.deleted"]`

    - `"organization.workload_identity_provider.deleted"`

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

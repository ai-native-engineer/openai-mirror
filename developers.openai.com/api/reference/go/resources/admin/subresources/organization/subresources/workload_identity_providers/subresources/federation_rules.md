<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/ -->

# Federation Rules

## Create Platform workload identity federation rule

`client.Admin.Organization.WorkloadIdentityProviders.FederationRules.New(ctx, workloadIdentityProviderID, body) (*FederationRule, error)`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

Bind verified token attributes to an existing project service account.

### Parameters

- `workloadIdentityProviderID string`

  `minLength: 1`

- `body AdminOrganizationWorkloadIdentityProviderFederationRuleNewParams`

  - `AttributeMatchers param.Field[map[string, AdminOrganizationWorkloadIdentityProviderFederationRuleNewParamsAttributeMatcherUnion]]`

    - `string`

    - `bool`

    - `type UnionMember2 interface{…}`

      - `int64`

      - `float64`

  - `ProjectID param.Field[string]`

    `minLength: 1`

  - `ServiceAccountID param.Field[string]`

    `minLength: 1`

  - `Description param.Field[string]`

  - `Enabled param.Field[bool]`

  - `Name param.Field[string]`

  - `Permissions param.Field[AdminOrganizationWorkloadIdentityProviderFederationRuleNewParamsPermissionsUnion]`

    - `type AdminOrganizationWorkloadIdentityProviderFederationRuleNewParamsPermissionsServiceAccountDefault struct{…}`

      - `Type ServiceAccountDefault`

        - `const ServiceAccountDefaultServiceAccountDefault ServiceAccountDefault = "service_account_default"`

    - `type AdminOrganizationWorkloadIdentityProviderFederationRuleNewParamsPermissionsRestricted struct{…}`

      - `Scopes []string`

        `minItems: 1`

      - `Type Restricted`

        - `const RestrictedRestricted Restricted = "restricted"`

### Returns

- `type FederationRule struct{…}`

  - `ID string`

  - `AttributeMatchers map[string, FederationRuleAttributeMatcherUnion]`

    - `string`

    - `bool`

    - `type UnionMember2 interface{…}`

      - `int64`

      - `float64`

  - `CreatedAt int64`

  - `Description string`

  - `Enabled bool`

  - `Name string`

  - `Object OrganizationWorkloadIdentityFederationRule`

    - `const OrganizationWorkloadIdentityFederationRuleOrganizationWorkloadIdentityFederationRule OrganizationWorkloadIdentityFederationRule = "organization.workload_identity_federation_rule"`

  - `Permissions FederationRulePermissionsUnion`

    - `type FederationRulePermissionsServiceAccountDefault struct{…}`

      - `Type ServiceAccountDefault`

        - `const ServiceAccountDefaultServiceAccountDefault ServiceAccountDefault = "service_account_default"`

    - `type FederationRulePermissionsRestricted struct{…}`

      - `Scopes []string`

      - `Type Restricted`

        - `const RestrictedRestricted Restricted = "restricted"`

  - `ProjectID string`

  - `ServiceAccountID string`

  - `UpdatedAt int64`

  - `WorkloadIdentityProviderID string`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  )
  federationRule, err := client.Admin.Organization.WorkloadIdentityProviders.FederationRules.New(
    context.TODO(),
    "x",
    openai.AdminOrganizationWorkloadIdentityProviderFederationRuleNewParams{
      AttributeMatchers: map[string]openai.AdminOrganizationWorkloadIdentityProviderFederationRuleNewParamsAttributeMatcherUnion{
      "foo": {
        OfString: openai.String("string"),
      },
      },
      ProjectID: "x",
      ServiceAccountID: "x",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", federationRule.ID)
}
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

`client.Admin.Organization.WorkloadIdentityProviders.FederationRules.Delete(ctx, workloadIdentityProviderID, workloadIdentityFederationRuleID) (*FederationRuleDeleted, error)`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Delete a federation rule to a project service account.

### Parameters

- `workloadIdentityProviderID string`

  `minLength: 1`

- `workloadIdentityFederationRuleID string`

  `minLength: 1`

### Returns

- `type FederationRuleDeleted struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object OrganizationWorkloadIdentityFederationRuleDeleted`

    - `const OrganizationWorkloadIdentityFederationRuleDeletedOrganizationWorkloadIdentityFederationRuleDeleted OrganizationWorkloadIdentityFederationRuleDeleted = "organization.workload_identity_federation_rule.deleted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  )
  federationRuleDeleted, err := client.Admin.Organization.WorkloadIdentityProviders.FederationRules.Delete(
    context.TODO(),
    "x",
    "x",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", federationRuleDeleted.ID)
}
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

`client.Admin.Organization.WorkloadIdentityProviders.FederationRules.List(ctx, workloadIdentityProviderID, query) (*CursorPage[FederationRule], error)`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

List the provider's federation rules to project service accounts.

### Parameters

- `workloadIdentityProviderID string`

  `minLength: 1`

- `query AdminOrganizationWorkloadIdentityProviderFederationRuleListParams`

  - `After param.Field[string]`

    `minLength: 1`

  - `Limit param.Field[int64]`

    `minimum: 1`, `maximum: 100`

  - `Order param.Field[AdminOrganizationWorkloadIdentityProviderFederationRuleListParamsOrderString]`

    - `type AdminOrganizationWorkloadIdentityProviderFederationRuleListParamsOrderString string`

      - `const AdminOrganizationWorkloadIdentityProviderFederationRuleListParamsOrderStringAsc AdminOrganizationWorkloadIdentityProviderFederationRuleListParamsOrderString = "asc"`

      - `const AdminOrganizationWorkloadIdentityProviderFederationRuleListParamsOrderStringDesc AdminOrganizationWorkloadIdentityProviderFederationRuleListParamsOrderString = "desc"`

  - `ServiceAccountID param.Field[string]`

    `minLength: 1`

### Returns

- `type FederationRule struct{…}`

  - `ID string`

  - `AttributeMatchers map[string, FederationRuleAttributeMatcherUnion]`

    - `string`

    - `bool`

    - `type UnionMember2 interface{…}`

      - `int64`

      - `float64`

  - `CreatedAt int64`

  - `Description string`

  - `Enabled bool`

  - `Name string`

  - `Object OrganizationWorkloadIdentityFederationRule`

    - `const OrganizationWorkloadIdentityFederationRuleOrganizationWorkloadIdentityFederationRule OrganizationWorkloadIdentityFederationRule = "organization.workload_identity_federation_rule"`

  - `Permissions FederationRulePermissionsUnion`

    - `type FederationRulePermissionsServiceAccountDefault struct{…}`

      - `Type ServiceAccountDefault`

        - `const ServiceAccountDefaultServiceAccountDefault ServiceAccountDefault = "service_account_default"`

    - `type FederationRulePermissionsRestricted struct{…}`

      - `Scopes []string`

      - `Type Restricted`

        - `const RestrictedRestricted Restricted = "restricted"`

  - `ProjectID string`

  - `ServiceAccountID string`

  - `UpdatedAt int64`

  - `WorkloadIdentityProviderID string`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  )
  page, err := client.Admin.Organization.WorkloadIdentityProviders.FederationRules.List(
    context.TODO(),
    "x",
    openai.AdminOrganizationWorkloadIdentityProviderFederationRuleListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
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

`client.Admin.Organization.WorkloadIdentityProviders.FederationRules.Get(ctx, workloadIdentityProviderID, workloadIdentityFederationRuleID) (*FederationRule, error)`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Retrieve a federation rule owned by the authenticated organization and provider.

### Parameters

- `workloadIdentityProviderID string`

  `minLength: 1`

- `workloadIdentityFederationRuleID string`

  `minLength: 1`

### Returns

- `type FederationRule struct{…}`

  - `ID string`

  - `AttributeMatchers map[string, FederationRuleAttributeMatcherUnion]`

    - `string`

    - `bool`

    - `type UnionMember2 interface{…}`

      - `int64`

      - `float64`

  - `CreatedAt int64`

  - `Description string`

  - `Enabled bool`

  - `Name string`

  - `Object OrganizationWorkloadIdentityFederationRule`

    - `const OrganizationWorkloadIdentityFederationRuleOrganizationWorkloadIdentityFederationRule OrganizationWorkloadIdentityFederationRule = "organization.workload_identity_federation_rule"`

  - `Permissions FederationRulePermissionsUnion`

    - `type FederationRulePermissionsServiceAccountDefault struct{…}`

      - `Type ServiceAccountDefault`

        - `const ServiceAccountDefaultServiceAccountDefault ServiceAccountDefault = "service_account_default"`

    - `type FederationRulePermissionsRestricted struct{…}`

      - `Scopes []string`

      - `Type Restricted`

        - `const RestrictedRestricted Restricted = "restricted"`

  - `ProjectID string`

  - `ServiceAccountID string`

  - `UpdatedAt int64`

  - `WorkloadIdentityProviderID string`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  )
  federationRule, err := client.Admin.Organization.WorkloadIdentityProviders.FederationRules.Get(
    context.TODO(),
    "x",
    "x",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", federationRule.ID)
}
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

`client.Admin.Organization.WorkloadIdentityProviders.FederationRules.Update(ctx, workloadIdentityProviderID, workloadIdentityFederationRuleID, body) (*FederationRule, error)`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Update supplied matcher, permission, metadata, or enabled fields.

### Parameters

- `workloadIdentityProviderID string`

  `minLength: 1`

- `workloadIdentityFederationRuleID string`

  `minLength: 1`

- `body AdminOrganizationWorkloadIdentityProviderFederationRuleUpdateParams`

  - `AttributeMatchers param.Field[map[string, AdminOrganizationWorkloadIdentityProviderFederationRuleUpdateParamsAttributeMatcherUnion]]`

    - `string`

    - `bool`

    - `type UnionMember2 interface{…}`

      - `int64`

      - `float64`

  - `Description param.Field[string]`

  - `Enabled param.Field[bool]`

  - `Name param.Field[string]`

  - `Permissions param.Field[AdminOrganizationWorkloadIdentityProviderFederationRuleUpdateParamsPermissionsUnion]`

    - `type AdminOrganizationWorkloadIdentityProviderFederationRuleUpdateParamsPermissionsDefaultPermissionsParam struct{…}`

      - `Type ServiceAccountDefault`

        - `const ServiceAccountDefaultServiceAccountDefault ServiceAccountDefault = "service_account_default"`

    - `type AdminOrganizationWorkloadIdentityProviderFederationRuleUpdateParamsPermissionsRestrictedPermissionsParam struct{…}`

      - `Scopes []string`

        `minItems: 1`

      - `Type Restricted`

        - `const RestrictedRestricted Restricted = "restricted"`

### Returns

- `type FederationRule struct{…}`

  - `ID string`

  - `AttributeMatchers map[string, FederationRuleAttributeMatcherUnion]`

    - `string`

    - `bool`

    - `type UnionMember2 interface{…}`

      - `int64`

      - `float64`

  - `CreatedAt int64`

  - `Description string`

  - `Enabled bool`

  - `Name string`

  - `Object OrganizationWorkloadIdentityFederationRule`

    - `const OrganizationWorkloadIdentityFederationRuleOrganizationWorkloadIdentityFederationRule OrganizationWorkloadIdentityFederationRule = "organization.workload_identity_federation_rule"`

  - `Permissions FederationRulePermissionsUnion`

    - `type FederationRulePermissionsServiceAccountDefault struct{…}`

      - `Type ServiceAccountDefault`

        - `const ServiceAccountDefaultServiceAccountDefault ServiceAccountDefault = "service_account_default"`

    - `type FederationRulePermissionsRestricted struct{…}`

      - `Scopes []string`

      - `Type Restricted`

        - `const RestrictedRestricted Restricted = "restricted"`

  - `ProjectID string`

  - `ServiceAccountID string`

  - `UpdatedAt int64`

  - `WorkloadIdentityProviderID string`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  )
  federationRule, err := client.Admin.Organization.WorkloadIdentityProviders.FederationRules.Update(
    context.TODO(),
    "x",
    "x",
    openai.AdminOrganizationWorkloadIdentityProviderFederationRuleUpdateParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", federationRule.ID)
}
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

- `type FederationRule struct{…}`

  - `ID string`

  - `AttributeMatchers map[string, FederationRuleAttributeMatcherUnion]`

    - `string`

    - `bool`

    - `type UnionMember2 interface{…}`

      - `int64`

      - `float64`

  - `CreatedAt int64`

  - `Description string`

  - `Enabled bool`

  - `Name string`

  - `Object OrganizationWorkloadIdentityFederationRule`

    - `const OrganizationWorkloadIdentityFederationRuleOrganizationWorkloadIdentityFederationRule OrganizationWorkloadIdentityFederationRule = "organization.workload_identity_federation_rule"`

  - `Permissions FederationRulePermissionsUnion`

    - `type FederationRulePermissionsServiceAccountDefault struct{…}`

      - `Type ServiceAccountDefault`

        - `const ServiceAccountDefaultServiceAccountDefault ServiceAccountDefault = "service_account_default"`

    - `type FederationRulePermissionsRestricted struct{…}`

      - `Scopes []string`

      - `Type Restricted`

        - `const RestrictedRestricted Restricted = "restricted"`

  - `ProjectID string`

  - `ServiceAccountID string`

  - `UpdatedAt int64`

  - `WorkloadIdentityProviderID string`

### Federation Rule Deleted

- `type FederationRuleDeleted struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object OrganizationWorkloadIdentityFederationRuleDeleted`

    - `const OrganizationWorkloadIdentityFederationRuleDeletedOrganizationWorkloadIdentityFederationRuleDeleted OrganizationWorkloadIdentityFederationRuleDeleted = "organization.workload_identity_federation_rule.deleted"`

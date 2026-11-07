<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/workload_identity_providers/ -->

# Workload Identity Providers

## Create Platform workload identity provider

`client.Admin.Organization.WorkloadIdentityProviders.New(ctx, body) (*WorkloadIdentityProvider, error)`

**post** `/organization/workload_identity_providers`

Register an OIDC provider for keyless project service-account authentication.

### Parameters

- `body AdminOrganizationWorkloadIdentityProviderNewParams`

  - `Audience param.Field[string]`

    `minLength: 1`

  - `Issuer param.Field[string]`

    `minLength: 1`

  - `Name param.Field[string]`

    `minLength: 1`

  - `Type param.Field[Oidc]`

    - `const OidcOidc Oidc = "oidc"`

  - `AttributeTransformations param.Field[[]AdminOrganizationWorkloadIdentityProviderNewParamsAttributeTransformation]`

    `maxItems: 20`

    - `Attribute string`

      `minLength: 1`, `maxLength: 256`

    - `Expression string`

      `minLength: 1`, `maxLength: 4096`

  - `Description param.Field[string]`

  - `Enabled param.Field[bool]`

  - `Verification param.Field[AdminOrganizationWorkloadIdentityProviderNewParamsVerificationUnion]`

    - `type AdminOrganizationWorkloadIdentityProviderNewParamsVerificationDiscovery struct{…}`

      - `DiscoveryURL string`

      - `Type Discovery`

        - `const DiscoveryDiscovery Discovery = "discovery"`

    - `type AdminOrganizationWorkloadIdentityProviderNewParamsVerificationUploadedJwks struct{…}`

      - `Jwks map[string, any]`

      - `Type UploadedJwks`

        - `const UploadedJwksUploadedJwks UploadedJwks = "uploaded_jwks"`

### Returns

- `type WorkloadIdentityProvider struct{…}`

  - `ID string`

  - `AttributeTransformations []WorkloadIdentityProviderAttributeTransformation`

    - `Attribute string`

    - `Expression string`

  - `Audience string`

  - `CreatedAt int64`

  - `Description string`

  - `Enabled bool`

  - `Issuer string`

  - `Name string`

  - `Object OrganizationWorkloadIdentityProvider`

    - `const OrganizationWorkloadIdentityProviderOrganizationWorkloadIdentityProvider OrganizationWorkloadIdentityProvider = "organization.workload_identity_provider"`

  - `Type Oidc`

    - `const OidcOidc Oidc = "oidc"`

  - `UpdatedAt int64`

  - `Verification WorkloadIdentityProviderVerificationUnion`

    - `type WorkloadIdentityProviderVerificationDiscovery struct{…}`

      - `DiscoveryURL string`

      - `Type Discovery`

        - `const DiscoveryDiscovery Discovery = "discovery"`

    - `type WorkloadIdentityProviderVerificationUploadedJwks struct{…}`

      - `Jwks map[string, any]`

      - `Type UploadedJwks`

        - `const UploadedJwksUploadedJwks UploadedJwks = "uploaded_jwks"`

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
  workloadIdentityProvider, err := client.Admin.Organization.WorkloadIdentityProviders.New(context.TODO(), openai.AdminOrganizationWorkloadIdentityProviderNewParams{
    Audience: "x",
    Issuer: "x",
    Name: "x",
    Type: "oidc",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", workloadIdentityProvider.ID)
}
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

`client.Admin.Organization.WorkloadIdentityProviders.Delete(ctx, workloadIdentityProviderID) (*WorkloadIdentityProviderDeleted, error)`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Delete a provider after deleting all its federation rules.

### Parameters

- `workloadIdentityProviderID string`

  `minLength: 1`

### Returns

- `type WorkloadIdentityProviderDeleted struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object OrganizationWorkloadIdentityProviderDeleted`

    - `const OrganizationWorkloadIdentityProviderDeletedOrganizationWorkloadIdentityProviderDeleted OrganizationWorkloadIdentityProviderDeleted = "organization.workload_identity_provider.deleted"`

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
  workloadIdentityProviderDeleted, err := client.Admin.Organization.WorkloadIdentityProviders.Delete(context.TODO(), "x")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", workloadIdentityProviderDeleted.ID)
}
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

`client.Admin.Organization.WorkloadIdentityProviders.List(ctx, query) (*CursorPage[WorkloadIdentityProvider], error)`

**get** `/organization/workload_identity_providers`

List OIDC providers in the authenticated Admin API key's organization.

### Parameters

- `query AdminOrganizationWorkloadIdentityProviderListParams`

  - `After param.Field[string]`

    `minLength: 1`

  - `Limit param.Field[int64]`

    `minimum: 1`, `maximum: 100`

  - `Order param.Field[AdminOrganizationWorkloadIdentityProviderListParamsOrderString]`

    - `type AdminOrganizationWorkloadIdentityProviderListParamsOrderString string`

      - `const AdminOrganizationWorkloadIdentityProviderListParamsOrderStringAsc AdminOrganizationWorkloadIdentityProviderListParamsOrderString = "asc"`

      - `const AdminOrganizationWorkloadIdentityProviderListParamsOrderStringDesc AdminOrganizationWorkloadIdentityProviderListParamsOrderString = "desc"`

### Returns

- `type WorkloadIdentityProvider struct{…}`

  - `ID string`

  - `AttributeTransformations []WorkloadIdentityProviderAttributeTransformation`

    - `Attribute string`

    - `Expression string`

  - `Audience string`

  - `CreatedAt int64`

  - `Description string`

  - `Enabled bool`

  - `Issuer string`

  - `Name string`

  - `Object OrganizationWorkloadIdentityProvider`

    - `const OrganizationWorkloadIdentityProviderOrganizationWorkloadIdentityProvider OrganizationWorkloadIdentityProvider = "organization.workload_identity_provider"`

  - `Type Oidc`

    - `const OidcOidc Oidc = "oidc"`

  - `UpdatedAt int64`

  - `Verification WorkloadIdentityProviderVerificationUnion`

    - `type WorkloadIdentityProviderVerificationDiscovery struct{…}`

      - `DiscoveryURL string`

      - `Type Discovery`

        - `const DiscoveryDiscovery Discovery = "discovery"`

    - `type WorkloadIdentityProviderVerificationUploadedJwks struct{…}`

      - `Jwks map[string, any]`

      - `Type UploadedJwks`

        - `const UploadedJwksUploadedJwks UploadedJwks = "uploaded_jwks"`

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
  page, err := client.Admin.Organization.WorkloadIdentityProviders.List(context.TODO(), openai.AdminOrganizationWorkloadIdentityProviderListParams{

  })
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

`client.Admin.Organization.WorkloadIdentityProviders.Get(ctx, workloadIdentityProviderID) (*WorkloadIdentityProvider, error)`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Retrieve an OIDC provider in the authenticated organization.

### Parameters

- `workloadIdentityProviderID string`

  `minLength: 1`

### Returns

- `type WorkloadIdentityProvider struct{…}`

  - `ID string`

  - `AttributeTransformations []WorkloadIdentityProviderAttributeTransformation`

    - `Attribute string`

    - `Expression string`

  - `Audience string`

  - `CreatedAt int64`

  - `Description string`

  - `Enabled bool`

  - `Issuer string`

  - `Name string`

  - `Object OrganizationWorkloadIdentityProvider`

    - `const OrganizationWorkloadIdentityProviderOrganizationWorkloadIdentityProvider OrganizationWorkloadIdentityProvider = "organization.workload_identity_provider"`

  - `Type Oidc`

    - `const OidcOidc Oidc = "oidc"`

  - `UpdatedAt int64`

  - `Verification WorkloadIdentityProviderVerificationUnion`

    - `type WorkloadIdentityProviderVerificationDiscovery struct{…}`

      - `DiscoveryURL string`

      - `Type Discovery`

        - `const DiscoveryDiscovery Discovery = "discovery"`

    - `type WorkloadIdentityProviderVerificationUploadedJwks struct{…}`

      - `Jwks map[string, any]`

      - `Type UploadedJwks`

        - `const UploadedJwksUploadedJwks UploadedJwks = "uploaded_jwks"`

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
  workloadIdentityProvider, err := client.Admin.Organization.WorkloadIdentityProviders.Get(context.TODO(), "x")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", workloadIdentityProvider.ID)
}
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

`client.Admin.Organization.WorkloadIdentityProviders.Update(ctx, workloadIdentityProviderID, body) (*WorkloadIdentityProvider, error)`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Update supplied provider fields, preserving omitted fields.

### Parameters

- `workloadIdentityProviderID string`

  `minLength: 1`

- `body AdminOrganizationWorkloadIdentityProviderUpdateParams`

  - `AttributeTransformations param.Field[[]AdminOrganizationWorkloadIdentityProviderUpdateParamsAttributeTransformation]`

    `maxItems: 20`

    - `Attribute string`

      `minLength: 1`, `maxLength: 256`

    - `Expression string`

      `minLength: 1`, `maxLength: 4096`

  - `Audience param.Field[string]`

    `minLength: 1`

  - `Description param.Field[string]`

  - `Enabled param.Field[bool]`

  - `Issuer param.Field[string]`

    `minLength: 1`

  - `Name param.Field[string]`

    `minLength: 1`

  - `Verification param.Field[AdminOrganizationWorkloadIdentityProviderUpdateParamsVerificationUnion]`

    - `type AdminOrganizationWorkloadIdentityProviderUpdateParamsVerificationDiscoveryVerificationParam struct{…}`

      - `DiscoveryURL string`

      - `Type Discovery`

        - `const DiscoveryDiscovery Discovery = "discovery"`

    - `type AdminOrganizationWorkloadIdentityProviderUpdateParamsVerificationUploadedJwksVerificationParam struct{…}`

      - `Jwks map[string, any]`

      - `Type UploadedJwks`

        - `const UploadedJwksUploadedJwks UploadedJwks = "uploaded_jwks"`

### Returns

- `type WorkloadIdentityProvider struct{…}`

  - `ID string`

  - `AttributeTransformations []WorkloadIdentityProviderAttributeTransformation`

    - `Attribute string`

    - `Expression string`

  - `Audience string`

  - `CreatedAt int64`

  - `Description string`

  - `Enabled bool`

  - `Issuer string`

  - `Name string`

  - `Object OrganizationWorkloadIdentityProvider`

    - `const OrganizationWorkloadIdentityProviderOrganizationWorkloadIdentityProvider OrganizationWorkloadIdentityProvider = "organization.workload_identity_provider"`

  - `Type Oidc`

    - `const OidcOidc Oidc = "oidc"`

  - `UpdatedAt int64`

  - `Verification WorkloadIdentityProviderVerificationUnion`

    - `type WorkloadIdentityProviderVerificationDiscovery struct{…}`

      - `DiscoveryURL string`

      - `Type Discovery`

        - `const DiscoveryDiscovery Discovery = "discovery"`

    - `type WorkloadIdentityProviderVerificationUploadedJwks struct{…}`

      - `Jwks map[string, any]`

      - `Type UploadedJwks`

        - `const UploadedJwksUploadedJwks UploadedJwks = "uploaded_jwks"`

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
  workloadIdentityProvider, err := client.Admin.Organization.WorkloadIdentityProviders.Update(
    context.TODO(),
    "x",
    openai.AdminOrganizationWorkloadIdentityProviderUpdateParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", workloadIdentityProvider.ID)
}
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

- `type WorkloadIdentityProvider struct{…}`

  - `ID string`

  - `AttributeTransformations []WorkloadIdentityProviderAttributeTransformation`

    - `Attribute string`

    - `Expression string`

  - `Audience string`

  - `CreatedAt int64`

  - `Description string`

  - `Enabled bool`

  - `Issuer string`

  - `Name string`

  - `Object OrganizationWorkloadIdentityProvider`

    - `const OrganizationWorkloadIdentityProviderOrganizationWorkloadIdentityProvider OrganizationWorkloadIdentityProvider = "organization.workload_identity_provider"`

  - `Type Oidc`

    - `const OidcOidc Oidc = "oidc"`

  - `UpdatedAt int64`

  - `Verification WorkloadIdentityProviderVerificationUnion`

    - `type WorkloadIdentityProviderVerificationDiscovery struct{…}`

      - `DiscoveryURL string`

      - `Type Discovery`

        - `const DiscoveryDiscovery Discovery = "discovery"`

    - `type WorkloadIdentityProviderVerificationUploadedJwks struct{…}`

      - `Jwks map[string, any]`

      - `Type UploadedJwks`

        - `const UploadedJwksUploadedJwks UploadedJwks = "uploaded_jwks"`

### Workload Identity Provider Deleted

- `type WorkloadIdentityProviderDeleted struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object OrganizationWorkloadIdentityProviderDeleted`

    - `const OrganizationWorkloadIdentityProviderDeletedOrganizationWorkloadIdentityProviderDeleted OrganizationWorkloadIdentityProviderDeleted = "organization.workload_identity_provider.deleted"`

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

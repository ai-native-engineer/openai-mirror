<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/create/ -->

## Create Platform workload identity provider

`client.Admin.Organization.WorkloadIdentityProviders.New(ctx, body) (*WorkloadIdentityProvider, error)`

**post** `/organization/workload_identity_providers`

Register an OIDC provider for keyless project service-account authentication.

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

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  workloadIdentityProvider, err := client.Admin.Organization.WorkloadIdentityProviders.New(context.TODO(), openai.AdminOrganizationWorkloadIdentityProviderNewParams{
    Audience: "x",
    Issuer: "x",
    Name: "x",
    Type: "oidc",
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", workloadIdentityProvider.ID)

  "attribute_transformations": [
      "attribute": "attribute",
      "expression": "expression"
  "audience": "audience",
  "enabled": true,
  "issuer": "issuer",
  "object": "organization.workload_identity_provider",
  "type": "oidc",
  "updated_at": 0,
  "verification": {
    "discovery_url": "discovery_url",
    "type": "discovery"

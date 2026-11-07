<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/retrieve/ -->

## Retrieve Platform workload identity provider

`client.Admin.Organization.WorkloadIdentityProviders.Get(ctx, workloadIdentityProviderID) (*WorkloadIdentityProvider, error)`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Retrieve an OIDC provider in the authenticated organization.

- `workloadIdentityProviderID string`

  `minLength: 1`

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
  workloadIdentityProvider, err := client.Admin.Organization.WorkloadIdentityProviders.Get(context.TODO(), "x")
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

<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/list/ -->

## List Platform workload identity providers

`client.Admin.Organization.WorkloadIdentityProviders.List(ctx, query) (*CursorPage[WorkloadIdentityProvider], error)`

**get** `/organization/workload_identity_providers`

List OIDC providers in the authenticated Admin API key's organization.

- `query AdminOrganizationWorkloadIdentityProviderListParams`

  - `After param.Field[string]`

    `minLength: 1`

  - `Limit param.Field[int64]`

    `minimum: 1`, `maximum: 100`

  - `Order param.Field[AdminOrganizationWorkloadIdentityProviderListParamsOrderString]`

    - `type AdminOrganizationWorkloadIdentityProviderListParamsOrderString string`

      - `const AdminOrganizationWorkloadIdentityProviderListParamsOrderStringAsc AdminOrganizationWorkloadIdentityProviderListParamsOrderString = "asc"`

      - `const AdminOrganizationWorkloadIdentityProviderListParamsOrderStringDesc AdminOrganizationWorkloadIdentityProviderListParamsOrderString = "desc"`

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
  page, err := client.Admin.Organization.WorkloadIdentityProviders.List(context.TODO(), openai.AdminOrganizationWorkloadIdentityProviderListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "data": [
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
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

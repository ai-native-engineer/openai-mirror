<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/external_keys/methods/list/ -->

## List the external key configs registered on the user's organization

`client.Admin.Organization.ExternalKeys.List(ctx, query) (*CursorPage[ExternalKey], error)`

**get** `/organization/external_keys`

List the external key configs registered on the user's organization

- `query AdminOrganizationExternalKeyListParams`

  - `After param.Field[string]`

  - `Limit param.Field[int64]`

    `minimum: 0`, `maximum: 100`

  - `Order param.Field[AdminOrganizationExternalKeyListParamsOrder]`

    - `const AdminOrganizationExternalKeyListParamsOrderAsc AdminOrganizationExternalKeyListParamsOrder = "asc"`

    - `const AdminOrganizationExternalKeyListParamsOrderDesc AdminOrganizationExternalKeyListParamsOrder = "desc"`

  - `Purpose param.Field[AdminOrganizationExternalKeyListParamsPurpose]`

    Filter by key purpose. When omitted, returns keys of all purposes.

    - `const AdminOrganizationExternalKeyListParamsPurposeEkm AdminOrganizationExternalKeyListParamsPurpose = "ekm"`

    - `const AdminOrganizationExternalKeyListParamsPurposePspDecryption AdminOrganizationExternalKeyListParamsPurpose = "psp_decryption"`

- `type ExternalKey struct{…}`

  - `ID string`

  - `APIProjectIDs []string`

  - `CreatedAt int64`

  - `Name string`

  - `Object string`

  - `Type string`

  - `WorkspaceID string`

  - `Audience string`

  - `ExternalID string`

  - `KeyName string`

  - `KeyVersion string`

  - `KmsArn string`

  - `KmsKeyLocation string`

  - `KmsKeyName string`

  - `KmsKeyRingName string`

  - `KmsKeyVersion string`

  - `KmsProjectID string`

  - `Purpose ExternalKeyPurpose`

    - `const ExternalKeyPurposeEkm ExternalKeyPurpose = "ekm"`

    - `const ExternalKeyPurposePspDecryption ExternalKeyPurpose = "psp_decryption"`

  - `RoleArn string`

  - `TenantID string`

  - `VaultUri string`

  - `WorkloadIdentityPoolID string`

  - `WorkloadIdentityProjectNumber string`

  - `WorkloadIdentityProviderID string`

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
  page, err := client.Admin.Organization.ExternalKeys.List(context.TODO(), openai.AdminOrganizationExternalKeyListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "data": [
      "api_project_ids": [
        "string"
      "object": "object",
      "type": "type",
      "workspace_id": "workspace_id",
      "audience": "audience",
      "external_id": "external_id",
      "key_name": "key_name",
      "key_version": "key_version",
      "kms_arn": "kms_arn",
      "kms_key_location": "kms_key_location",
      "kms_key_name": "kms_key_name",
      "kms_key_ring_name": "kms_key_ring_name",
      "kms_key_version": "kms_key_version",
      "kms_project_id": "kms_project_id",
      "purpose": "ekm",
      "role_arn": "role_arn",
      "tenant_id": "tenant_id",
      "vault_uri": "vault_uri",
      "workload_identity_pool_id": "workload_identity_pool_id",
      "workload_identity_project_number": "workload_identity_project_number",
      "workload_identity_provider_id": "workload_identity_provider_id"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

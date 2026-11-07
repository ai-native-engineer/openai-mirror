<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/external_keys/methods/retrieve/ -->

## Retrieve an external key registration

`client.Admin.Organization.ExternalKeys.Get(ctx, externalKeyID) (*ExternalKey, error)`

**get** `/organization/external_keys/{external_key_id}`

Retrieve a stored external key registration for the user's organization.

- `externalKeyID string`

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
  externalKey, err := client.Admin.Organization.ExternalKeys.Get(context.TODO(), "external_key_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", externalKey.ID)

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

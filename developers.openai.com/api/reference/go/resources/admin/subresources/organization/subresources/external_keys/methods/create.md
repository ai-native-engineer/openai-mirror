<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/external_keys/methods/create/ -->

## Add an external key config for an organization

`client.Admin.Organization.ExternalKeys.New(ctx, body) (*ExternalKey, error)`

**post** `/organization/external_keys`

Add an external key config for an organization

- `body AdminOrganizationExternalKeyNewParams`

  - `ExternalID param.Field[string]`

    The ExternalID that OpenAI will pass in the AssumeRole call for the customer's AWS account. This must be the OpenAI organization ID or an API project ID that belongs to the organization.

  - `KmsArn param.Field[string]`

    The Key Management System ARN for the master key you manage

  - `Name param.Field[string]`

    A friendly name to identify this config

  - `RoleArn param.Field[string]`

    The Role ARN that OpenAI will assume to call your KMS

  - `Type param.Field[AdminOrganizationExternalKeyNewParamsType]`

    - `const AdminOrganizationExternalKeyNewParamsTypeAws AdminOrganizationExternalKeyNewParamsType = "aws"`

  - `Purpose param.Field[AdminOrganizationExternalKeyNewParamsPurpose]`

    - `const AdminOrganizationExternalKeyNewParamsPurposeEkm AdminOrganizationExternalKeyNewParamsPurpose = "ekm"`

    - `const AdminOrganizationExternalKeyNewParamsPurposePspDecryption AdminOrganizationExternalKeyNewParamsPurpose = "psp_decryption"`

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
  externalKey, err := client.Admin.Organization.ExternalKeys.New(context.TODO(), openai.AdminOrganizationExternalKeyNewParams{
    ExternalID: "external_id",
    KmsArn: "kms_arn",
    Name: "name",
    RoleArn: "arn:aws:iam::123456789012:role/example-role",
    Type: "aws",
  })
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

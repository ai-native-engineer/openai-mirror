<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/external_keys/ -->

# External Keys

## Add an external key config for an organization

`client.Admin.Organization.ExternalKeys.New(ctx, body) (*ExternalKey, error)`

**post** `/organization/external_keys`

Add an external key config for an organization

### Parameters

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

### Returns

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
  externalKey, err := client.Admin.Organization.ExternalKeys.New(context.TODO(), openai.AdminOrganizationExternalKeyNewParams{
    ExternalID: "external_id",
    KmsArn: "kms_arn",
    Name: "name",
    RoleArn: "arn:aws:iam::123456789012:role/example-role",
    Type: "aws",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", externalKey.ID)
}
```

#### 200 — Example

```json
{
  "id": "id",
  "api_project_ids": [
    "string"
  ],
  "created_at": 0,
  "name": "name",
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
}
```

## Delete an external key config for the user's organization

`client.Admin.Organization.ExternalKeys.Delete(ctx, externalKeyID) (*ExternalKey, error)`

**delete** `/organization/external_keys/{external_key_id}`

Delete an external key config for the user's organization

### Parameters

- `externalKeyID string`

### Returns

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
  externalKey, err := client.Admin.Organization.ExternalKeys.Delete(context.TODO(), "external_key_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", externalKey.ID)
}
```

#### 200 — Example

```json
{
  "id": "id",
  "api_project_ids": [
    "string"
  ],
  "created_at": 0,
  "name": "name",
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
}
```

## List the external key configs registered on the user's organization

`client.Admin.Organization.ExternalKeys.List(ctx, query) (*CursorPage[ExternalKey], error)`

**get** `/organization/external_keys`

List the external key configs registered on the user's organization

### Parameters

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

### Returns

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
  page, err := client.Admin.Organization.ExternalKeys.List(context.TODO(), openai.AdminOrganizationExternalKeyListParams{

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
      "api_project_ids": [
        "string"
      ],
      "created_at": 0,
      "name": "name",
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
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve an external key registration

`client.Admin.Organization.ExternalKeys.Get(ctx, externalKeyID) (*ExternalKey, error)`

**get** `/organization/external_keys/{external_key_id}`

Retrieve a stored external key registration for the user's organization.

### Parameters

- `externalKeyID string`

### Returns

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
  externalKey, err := client.Admin.Organization.ExternalKeys.Get(context.TODO(), "external_key_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", externalKey.ID)
}
```

#### 200 — Example

```json
{
  "id": "id",
  "api_project_ids": [
    "string"
  ],
  "created_at": 0,
  "name": "name",
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
}
```

## Validate an external key config for the user's organization

`client.Admin.Organization.ExternalKeys.Validate(ctx, externalKeyID) (*AdminOrganizationExternalKeyValidateResponse, error)`

**post** `/organization/external_keys/{external_key_id}/validate`

Validate an external key config for the user's organization

### Parameters

- `externalKeyID string`

### Returns

- `type AdminOrganizationExternalKeyValidateResponse struct{…}`

  - `Status string`

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
  response, err := client.Admin.Organization.ExternalKeys.Validate(context.TODO(), "external_key_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.Status)
}
```

#### 200 — Example

```json
{
  "status": "status"
}
```

## Domain Types

### External Key

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

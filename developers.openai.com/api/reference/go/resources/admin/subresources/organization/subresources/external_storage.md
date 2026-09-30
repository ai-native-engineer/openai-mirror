<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/external_storage/ -->

# External Storage

## Create an external storage configuration

`client.Admin.Organization.ExternalStorage.New(ctx, body) (*ExternalStorageConfiguration, error)`

**post** `/organization/external_storage`

Register one customer-managed external storage configuration.

### Parameters

- `body AdminOrganizationExternalStorageNewParams`

  - `ProjectID param.Field[string]`

  - `Provider param.Field[AdminOrganizationExternalStorageNewParamsProviderUnion]`

    - `type AdminOrganizationExternalStorageNewParamsProviderAws struct{…}`

      - `Bucket string`

      - `RoleArn string`

      - `Type Aws`

        - `const AwsAws Aws = "aws"`

    - `type AdminOrganizationExternalStorageNewParamsProviderAzure struct{…}`

      - `AccountName string`

      - `Container string`

      - `ResourceGroup string`

      - `SubscriptionID string`

      - `TenantID string`

      - `Type Azure`

        - `const AzureAzure Azure = "azure"`

    - `type AdminOrganizationExternalStorageNewParamsProviderGcp struct{…}`

      - `Bucket string`

      - `Type Gcp`

        - `const GcpGcp Gcp = "gcp"`

      - `WorkloadIdentityPoolID string`

      - `WorkloadIdentityProjectNumber string`

      - `WorkloadIdentityProviderID string`

### Returns

- `type ExternalStorageConfiguration struct{…}`

  - `ID string`

  - `CreatedAt int64`

  - `Geography string`

  - `Object OrganizationExternalStorage`

    - `const OrganizationExternalStorageOrganizationExternalStorage OrganizationExternalStorage = "organization.external_storage"`

  - `ProjectID string`

  - `Provider ExternalStorageConfigurationProviderUnion`

    - `type AwsExternalStorageProvider struct{…}`

      - `AccountID string`

      - `Bucket string`

      - `ExternalID string`

      - `Region string`

      - `RoleArn string`

      - `Type Aws`

        - `const AwsAws Aws = "aws"`

    - `type AzureExternalStorageProvider struct{…}`

      - `AccountName string`

      - `Container string`

      - `Region string`

      - `ResourceGroup string`

      - `SubscriptionID string`

      - `TenantID string`

      - `Type Azure`

        - `const AzureAzure Azure = "azure"`

    - `type GcpExternalStorageProvider struct{…}`

      - `Audience string`

      - `Bucket string`

      - `Region string`

      - `Type Gcp`

        - `const GcpGcp Gcp = "gcp"`

      - `WorkloadIdentityPoolID string`

      - `WorkloadIdentityProjectNumber string`

      - `WorkloadIdentityProviderID string`

  - `Status ExternalStorageConfigurationStatus`

    - `const ExternalStorageConfigurationStatusPending ExternalStorageConfigurationStatus = "pending"`

    - `const ExternalStorageConfigurationStatusValidated ExternalStorageConfigurationStatus = "validated"`

    - `const ExternalStorageConfigurationStatusUnhealthy ExternalStorageConfigurationStatus = "unhealthy"`

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
  externalStorageConfiguration, err := client.Admin.Organization.ExternalStorage.New(context.TODO(), openai.AdminOrganizationExternalStorageNewParams{
    ProjectID: "proj_123",
    Provider: openai.AdminOrganizationExternalStorageNewParamsProviderUnion{
      OfAws: &openai.AdminOrganizationExternalStorageNewParamsProviderAws{
        Bucket: "bucket",
        RoleArn: "role_arn",
      },
    },
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", externalStorageConfiguration.ID)
}
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "geography": "geography",
  "object": "organization.external_storage",
  "project_id": "project_id",
  "provider": {
    "account_id": "account_id",
    "bucket": "bucket",
    "external_id": "external_id",
    "region": "region",
    "role_arn": "role_arn",
    "type": "aws"
  },
  "status": "pending"
}
```

## Delete an external storage configuration

`client.Admin.Organization.ExternalStorage.Delete(ctx, externalStorageID) (*ExternalStorageDeleted, error)`

**delete** `/organization/external_storage/{external_storage_id}`

Disconnect a customer-managed external storage configuration. Removing the project's last configuration restores organization-default retention if customer-managed retention was active. Repeating a deletion also completes any interrupted retention update. Cloud storage is unchanged.

### Parameters

- `externalStorageID string`

### Returns

- `type ExternalStorageDeleted struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object OrganizationExternalStorageDeleted`

    - `const OrganizationExternalStorageDeletedOrganizationExternalStorageDeleted OrganizationExternalStorageDeleted = "organization.external_storage.deleted"`

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
  externalStorageDeleted, err := client.Admin.Organization.ExternalStorage.Delete(context.TODO(), "extstorage_123")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", externalStorageDeleted.ID)
}
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "organization.external_storage.deleted"
}
```

## List external storage configurations

`client.Admin.Organization.ExternalStorage.List(ctx, query) (*CursorPage[ExternalStorageConfiguration], error)`

**get** `/organization/external_storage`

List the organization's customer-managed external storage configurations.

### Parameters

- `query AdminOrganizationExternalStorageListParams`

  - `After param.Field[string]`

    Return external storage configurations after this ID.

  - `Limit param.Field[int64]`

  - `Order param.Field[AdminOrganizationExternalStorageListParamsOrder]`

    - `const AdminOrganizationExternalStorageListParamsOrderAsc AdminOrganizationExternalStorageListParamsOrder = "asc"`

    - `const AdminOrganizationExternalStorageListParamsOrderDesc AdminOrganizationExternalStorageListParamsOrder = "desc"`

  - `ProjectID param.Field[string]`

### Returns

- `type ExternalStorageConfiguration struct{…}`

  - `ID string`

  - `CreatedAt int64`

  - `Geography string`

  - `Object OrganizationExternalStorage`

    - `const OrganizationExternalStorageOrganizationExternalStorage OrganizationExternalStorage = "organization.external_storage"`

  - `ProjectID string`

  - `Provider ExternalStorageConfigurationProviderUnion`

    - `type AwsExternalStorageProvider struct{…}`

      - `AccountID string`

      - `Bucket string`

      - `ExternalID string`

      - `Region string`

      - `RoleArn string`

      - `Type Aws`

        - `const AwsAws Aws = "aws"`

    - `type AzureExternalStorageProvider struct{…}`

      - `AccountName string`

      - `Container string`

      - `Region string`

      - `ResourceGroup string`

      - `SubscriptionID string`

      - `TenantID string`

      - `Type Azure`

        - `const AzureAzure Azure = "azure"`

    - `type GcpExternalStorageProvider struct{…}`

      - `Audience string`

      - `Bucket string`

      - `Region string`

      - `Type Gcp`

        - `const GcpGcp Gcp = "gcp"`

      - `WorkloadIdentityPoolID string`

      - `WorkloadIdentityProjectNumber string`

      - `WorkloadIdentityProviderID string`

  - `Status ExternalStorageConfigurationStatus`

    - `const ExternalStorageConfigurationStatusPending ExternalStorageConfigurationStatus = "pending"`

    - `const ExternalStorageConfigurationStatusValidated ExternalStorageConfigurationStatus = "validated"`

    - `const ExternalStorageConfigurationStatusUnhealthy ExternalStorageConfigurationStatus = "unhealthy"`

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
  page, err := client.Admin.Organization.ExternalStorage.List(context.TODO(), openai.AdminOrganizationExternalStorageListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": 0,
      "geography": "geography",
      "object": "organization.external_storage",
      "project_id": "project_id",
      "provider": {
        "account_id": "account_id",
        "bucket": "bucket",
        "external_id": "external_id",
        "region": "region",
        "role_arn": "role_arn",
        "type": "aws"
      },
      "status": "pending"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Get an external storage configuration

`client.Admin.Organization.ExternalStorage.Get(ctx, externalStorageID) (*ExternalStorageConfiguration, error)`

**get** `/organization/external_storage/{external_storage_id}`

Get one customer-managed external storage configuration.

### Parameters

- `externalStorageID string`

### Returns

- `type ExternalStorageConfiguration struct{…}`

  - `ID string`

  - `CreatedAt int64`

  - `Geography string`

  - `Object OrganizationExternalStorage`

    - `const OrganizationExternalStorageOrganizationExternalStorage OrganizationExternalStorage = "organization.external_storage"`

  - `ProjectID string`

  - `Provider ExternalStorageConfigurationProviderUnion`

    - `type AwsExternalStorageProvider struct{…}`

      - `AccountID string`

      - `Bucket string`

      - `ExternalID string`

      - `Region string`

      - `RoleArn string`

      - `Type Aws`

        - `const AwsAws Aws = "aws"`

    - `type AzureExternalStorageProvider struct{…}`

      - `AccountName string`

      - `Container string`

      - `Region string`

      - `ResourceGroup string`

      - `SubscriptionID string`

      - `TenantID string`

      - `Type Azure`

        - `const AzureAzure Azure = "azure"`

    - `type GcpExternalStorageProvider struct{…}`

      - `Audience string`

      - `Bucket string`

      - `Region string`

      - `Type Gcp`

        - `const GcpGcp Gcp = "gcp"`

      - `WorkloadIdentityPoolID string`

      - `WorkloadIdentityProjectNumber string`

      - `WorkloadIdentityProviderID string`

  - `Status ExternalStorageConfigurationStatus`

    - `const ExternalStorageConfigurationStatusPending ExternalStorageConfigurationStatus = "pending"`

    - `const ExternalStorageConfigurationStatusValidated ExternalStorageConfigurationStatus = "validated"`

    - `const ExternalStorageConfigurationStatusUnhealthy ExternalStorageConfigurationStatus = "unhealthy"`

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
  externalStorageConfiguration, err := client.Admin.Organization.ExternalStorage.Get(context.TODO(), "extstorage_123")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", externalStorageConfiguration.ID)
}
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "geography": "geography",
  "object": "organization.external_storage",
  "project_id": "project_id",
  "provider": {
    "account_id": "account_id",
    "bucket": "bucket",
    "external_id": "external_id",
    "region": "region",
    "role_arn": "role_arn",
    "type": "aws"
  },
  "status": "pending"
}
```

## Validate an external storage configuration

`client.Admin.Organization.ExternalStorage.Validate(ctx, externalStorageID) (*ExternalStorageConfiguration, error)`

**post** `/organization/external_storage/{external_storage_id}/validate`

Validate one customer-managed external storage configuration.

### Parameters

- `externalStorageID string`

### Returns

- `type ExternalStorageConfiguration struct{…}`

  - `ID string`

  - `CreatedAt int64`

  - `Geography string`

  - `Object OrganizationExternalStorage`

    - `const OrganizationExternalStorageOrganizationExternalStorage OrganizationExternalStorage = "organization.external_storage"`

  - `ProjectID string`

  - `Provider ExternalStorageConfigurationProviderUnion`

    - `type AwsExternalStorageProvider struct{…}`

      - `AccountID string`

      - `Bucket string`

      - `ExternalID string`

      - `Region string`

      - `RoleArn string`

      - `Type Aws`

        - `const AwsAws Aws = "aws"`

    - `type AzureExternalStorageProvider struct{…}`

      - `AccountName string`

      - `Container string`

      - `Region string`

      - `ResourceGroup string`

      - `SubscriptionID string`

      - `TenantID string`

      - `Type Azure`

        - `const AzureAzure Azure = "azure"`

    - `type GcpExternalStorageProvider struct{…}`

      - `Audience string`

      - `Bucket string`

      - `Region string`

      - `Type Gcp`

        - `const GcpGcp Gcp = "gcp"`

      - `WorkloadIdentityPoolID string`

      - `WorkloadIdentityProjectNumber string`

      - `WorkloadIdentityProviderID string`

  - `Status ExternalStorageConfigurationStatus`

    - `const ExternalStorageConfigurationStatusPending ExternalStorageConfigurationStatus = "pending"`

    - `const ExternalStorageConfigurationStatusValidated ExternalStorageConfigurationStatus = "validated"`

    - `const ExternalStorageConfigurationStatusUnhealthy ExternalStorageConfigurationStatus = "unhealthy"`

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
  externalStorageConfiguration, err := client.Admin.Organization.ExternalStorage.Validate(context.TODO(), "extstorage_123")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", externalStorageConfiguration.ID)
}
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "geography": "geography",
  "object": "organization.external_storage",
  "project_id": "project_id",
  "provider": {
    "account_id": "account_id",
    "bucket": "bucket",
    "external_id": "external_id",
    "region": "region",
    "role_arn": "role_arn",
    "type": "aws"
  },
  "status": "pending"
}
```

## Domain Types

### Aws External Storage Provider

- `type AwsExternalStorageProvider struct{…}`

  - `AccountID string`

  - `Bucket string`

  - `ExternalID string`

  - `Region string`

  - `RoleArn string`

  - `Type Aws`

    - `const AwsAws Aws = "aws"`

### Azure External Storage Provider

- `type AzureExternalStorageProvider struct{…}`

  - `AccountName string`

  - `Container string`

  - `Region string`

  - `ResourceGroup string`

  - `SubscriptionID string`

  - `TenantID string`

  - `Type Azure`

    - `const AzureAzure Azure = "azure"`

### External Storage Configuration

- `type ExternalStorageConfiguration struct{…}`

  - `ID string`

  - `CreatedAt int64`

  - `Geography string`

  - `Object OrganizationExternalStorage`

    - `const OrganizationExternalStorageOrganizationExternalStorage OrganizationExternalStorage = "organization.external_storage"`

  - `ProjectID string`

  - `Provider ExternalStorageConfigurationProviderUnion`

    - `type AwsExternalStorageProvider struct{…}`

      - `AccountID string`

      - `Bucket string`

      - `ExternalID string`

      - `Region string`

      - `RoleArn string`

      - `Type Aws`

        - `const AwsAws Aws = "aws"`

    - `type AzureExternalStorageProvider struct{…}`

      - `AccountName string`

      - `Container string`

      - `Region string`

      - `ResourceGroup string`

      - `SubscriptionID string`

      - `TenantID string`

      - `Type Azure`

        - `const AzureAzure Azure = "azure"`

    - `type GcpExternalStorageProvider struct{…}`

      - `Audience string`

      - `Bucket string`

      - `Region string`

      - `Type Gcp`

        - `const GcpGcp Gcp = "gcp"`

      - `WorkloadIdentityPoolID string`

      - `WorkloadIdentityProjectNumber string`

      - `WorkloadIdentityProviderID string`

  - `Status ExternalStorageConfigurationStatus`

    - `const ExternalStorageConfigurationStatusPending ExternalStorageConfigurationStatus = "pending"`

    - `const ExternalStorageConfigurationStatusValidated ExternalStorageConfigurationStatus = "validated"`

    - `const ExternalStorageConfigurationStatusUnhealthy ExternalStorageConfigurationStatus = "unhealthy"`

### External Storage Deleted

- `type ExternalStorageDeleted struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object OrganizationExternalStorageDeleted`

    - `const OrganizationExternalStorageDeletedOrganizationExternalStorageDeleted OrganizationExternalStorageDeleted = "organization.external_storage.deleted"`

### Gcp External Storage Provider

- `type GcpExternalStorageProvider struct{…}`

  - `Audience string`

  - `Bucket string`

  - `Region string`

  - `Type Gcp`

    - `const GcpGcp Gcp = "gcp"`

  - `WorkloadIdentityPoolID string`

  - `WorkloadIdentityProjectNumber string`

  - `WorkloadIdentityProviderID string`

<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/external_storage/methods/list/ -->

## List external storage configurations

`client.Admin.Organization.ExternalStorage.List(ctx, query) (*CursorPage[ExternalStorageConfiguration], error)`

**get** `/organization/external_storage`

List the organization's customer-managed external storage configurations.

- `query AdminOrganizationExternalStorageListParams`

  - `After param.Field[string]`

    Return external storage configurations after this ID.

  - `Limit param.Field[int64]`

  - `Order param.Field[AdminOrganizationExternalStorageListParamsOrder]`

    - `const AdminOrganizationExternalStorageListParamsOrderAsc AdminOrganizationExternalStorageListParamsOrder = "asc"`

    - `const AdminOrganizationExternalStorageListParamsOrderDesc AdminOrganizationExternalStorageListParamsOrder = "desc"`

  - `ProjectID param.Field[string]`

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
  page, err := client.Admin.Organization.ExternalStorage.List(context.TODO(), openai.AdminOrganizationExternalStorageListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "data": [
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
      "status": "pending"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

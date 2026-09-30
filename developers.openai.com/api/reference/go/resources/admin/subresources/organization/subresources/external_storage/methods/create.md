<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/external_storage/methods/create/ -->

## Create an external storage configuration

`client.Admin.Organization.ExternalStorage.New(ctx, body) (*ExternalStorageConfiguration, error)`

**post** `/organization/external_storage`

Register one customer-managed external storage configuration.

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
  externalStorageConfiguration, err := client.Admin.Organization.ExternalStorage.New(context.TODO(), openai.AdminOrganizationExternalStorageNewParams{
    ProjectID: "proj_123",
    Provider: openai.AdminOrganizationExternalStorageNewParamsProviderUnion{
      OfAws: &openai.AdminOrganizationExternalStorageNewParamsProviderAws{
        Bucket: "bucket",
        RoleArn: "role_arn",
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", externalStorageConfiguration.ID)

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

<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/external_storage/methods/delete/ -->

## Delete an external storage configuration

`client.Admin.Organization.ExternalStorage.Delete(ctx, externalStorageID) (*ExternalStorageDeleted, error)`

**delete** `/organization/external_storage/{external_storage_id}`

Disconnect a customer-managed external storage configuration. Removing the project's last configuration restores organization-default retention if customer-managed retention was active. Repeating a deletion also completes any interrupted retention update. Cloud storage is unchanged.

- `externalStorageID string`

- `type ExternalStorageDeleted struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object OrganizationExternalStorageDeleted`

    - `const OrganizationExternalStorageDeletedOrganizationExternalStorageDeleted OrganizationExternalStorageDeleted = "organization.external_storage.deleted"`

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
  externalStorageDeleted, err := client.Admin.Organization.ExternalStorage.Delete(context.TODO(), "extstorage_123")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", externalStorageDeleted.ID)

  "deleted": true,
  "object": "organization.external_storage.deleted"

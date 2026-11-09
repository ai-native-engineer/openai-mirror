<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/external_keys/methods/validate/ -->

## Validate an external key config for the user's organization

`client.Admin.Organization.ExternalKeys.Validate(ctx, externalKeyID) (*AdminOrganizationExternalKeyValidateResponse, error)`

**post** `/organization/external_keys/{external_key_id}/validate`

Validate an external key config for the user's organization

- `externalKeyID string`

- `type AdminOrganizationExternalKeyValidateResponse struct{…}`

  - `Status string`

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
  response, err := client.Admin.Organization.ExternalKeys.Validate(context.TODO(), "external_key_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", response.Status)

  "status": "status"

<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/delete/ -->

## Delete Platform workload identity provider

`client.Admin.Organization.WorkloadIdentityProviders.Delete(ctx, workloadIdentityProviderID) (*WorkloadIdentityProviderDeleted, error)`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Delete a provider after deleting all its federation rules.

- `workloadIdentityProviderID string`

  `minLength: 1`

- `type WorkloadIdentityProviderDeleted struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object OrganizationWorkloadIdentityProviderDeleted`

    - `const OrganizationWorkloadIdentityProviderDeletedOrganizationWorkloadIdentityProviderDeleted OrganizationWorkloadIdentityProviderDeleted = "organization.workload_identity_provider.deleted"`

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
  workloadIdentityProviderDeleted, err := client.Admin.Organization.WorkloadIdentityProviders.Delete(context.TODO(), "x")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", workloadIdentityProviderDeleted.ID)

  "deleted": true,
  "object": "organization.workload_identity_provider.deleted"

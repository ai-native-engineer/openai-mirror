<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/spend_limit/methods/delete/ -->

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Spend Limit](/api/reference/go/resources/admin/subresources/organization/subresources/spend_limit)

# Delete organization spend limit

client.Admin.Organization.SpendLimit.Delete(ctx) (\*[OrganizationSpendLimitDeleted](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit_deleted%20%3E%20(schema)), error)

DELETE/organization/spend\_limit

Delete the organization’s hard spend limit.

type OrganizationSpendLimitDeleted struct{…}

Confirmation payload returned after deleting an organization hard spend limit.

Deleted bool

Whether the hard spend limit was deleted.

Object OrganizationSpendLimitDeleted

The object type, which is always `organization.spend_limit.deleted`.

### Delete organization spend limit

Go

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
  organizationSpendLimitDeleted, err := client.Admin.Organization.SpendLimit.Delete(context.TODO())
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", organizationSpendLimitDeleted.Deleted)

    "object": "organization.spend_limit.deleted",
    "deleted": true

    "object": "organization.spend_limit.deleted",
    "deleted": true

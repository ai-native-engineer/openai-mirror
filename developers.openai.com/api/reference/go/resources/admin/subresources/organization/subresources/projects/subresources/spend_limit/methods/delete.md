<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/delete/ -->

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Spend Limit](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit)

# Delete project spend limit

client.Admin.Organization.Projects.SpendLimit.Delete(ctx, projectID) (\*[ProjectSpendLimitDeleted](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit_deleted%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/spend\_limit

Delete a project’s hard spend limit.

##### ParametersExpand Collapse

projectID string

type ProjectSpendLimitDeleted struct{…}

Confirmation payload returned after deleting a project hard spend limit.

Deleted bool

Whether the hard spend limit was deleted.

Object ProjectSpendLimitDeleted

The object type, which is always `project.spend_limit.deleted`.

### Delete project spend limit

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
  projectSpendLimitDeleted, err := client.Admin.Organization.Projects.SpendLimit.Delete(context.TODO(), "proj_123")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectSpendLimitDeleted.Deleted)

    "object": "project.spend_limit.deleted",
    "deleted": true

    "object": "project.spend_limit.deleted",
    "deleted": true

<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/update/ -->

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Spend Limit](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit)

# Update project spend limit

client.Admin.Organization.Projects.SpendLimit.Update(ctx, projectID, body) (\*[ProjectSpendLimit](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/spend\_limit

Create or replace a project’s hard spend limit.

##### ParametersExpand Collapse

projectID string

body AdminOrganizationProjectSpendLimitUpdateParams

Currency param.Field[[AdminOrganizationProjectSpendLimitUpdateParamsCurrency](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/update#(resource)%20admin.organization.projects.spend_limit%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20currency%20%3E%20(schema))]

const AdminOrganizationProjectSpendLimitUpdateParamsCurrencyUsd [AdminOrganizationProjectSpendLimitUpdateParamsCurrency](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/update#(resource)%20admin.organization.projects.spend_limit%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20currency%20%3E%20(schema)) = "USD"

Interval param.Field[[AdminOrganizationProjectSpendLimitUpdateParamsInterval](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/update#(resource)%20admin.organization.projects.spend_limit%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20interval%20%3E%20(schema))]

const AdminOrganizationProjectSpendLimitUpdateParamsIntervalMonth [AdminOrganizationProjectSpendLimitUpdateParamsInterval](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/update#(resource)%20admin.organization.projects.spend_limit%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20interval%20%3E%20(schema)) = "month"

ThresholdAmount param.Field[int64]

minimum1

type ProjectSpendLimit struct{…}

Represents a hard spend limit configured at the project level.

Currency ProjectSpendLimitCurrency

string

type ProjectSpendLimitCurrency string

Enforcement ProjectSpendLimitEnforcement

Status string

string

string

const ProjectSpendLimitEnforcementStatusInactive ProjectSpendLimitEnforcementStatus = "inactive"

const ProjectSpendLimitEnforcementStatusEnforcing ProjectSpendLimitEnforcementStatus = "enforcing"

Interval ProjectSpendLimitInterval

string

type ProjectSpendLimitInterval string

Object ProjectSpendLimit

The object type, which is always `project.spend_limit`.

ThresholdAmount int64

### Update project spend limit

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
  projectSpendLimit, err := client.Admin.Organization.Projects.SpendLimit.Update(
    context.TODO(),
    "proj_123",
    openai.AdminOrganizationProjectSpendLimitUpdateParams{
      Currency: openai.AdminOrganizationProjectSpendLimitUpdateParamsCurrencyUsd,
      Interval: openai.AdminOrganizationProjectSpendLimitUpdateParamsIntervalMonth,
      ThresholdAmount: 1,
    },
  )
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectSpendLimit.Currency)

    "object": "project.spend_limit",
    "threshold_amount": 10000,
    "currency": "USD",
    "interval": "month",
    "enforcement": {
        "status": "enforcing"

    "object": "project.spend_limit",
    "threshold_amount": 10000,
    "currency": "USD",
    "interval": "month",
    "enforcement": {
        "status": "enforcing"

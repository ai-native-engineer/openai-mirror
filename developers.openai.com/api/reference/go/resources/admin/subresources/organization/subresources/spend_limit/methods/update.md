<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/spend_limit/methods/update/ -->

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Spend Limit](/api/reference/go/resources/admin/subresources/organization/subresources/spend_limit)

# Update organization spend limit

client.Admin.Organization.SpendLimit.Update(ctx, body) (\*[OrganizationSpendLimit](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit%20%3E%20(schema)), error)

POST/organization/spend\_limit

Create or replace the organization’s hard spend limit.

##### ParametersExpand Collapse

body AdminOrganizationSpendLimitUpdateParams

Currency param.Field[[AdminOrganizationSpendLimitUpdateParamsCurrency](/api/reference/go/resources/admin/subresources/organization/subresources/spend_limit/methods/update#(resource)%20admin.organization.spend_limit%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20currency%20%3E%20(schema))]

const AdminOrganizationSpendLimitUpdateParamsCurrencyUsd [AdminOrganizationSpendLimitUpdateParamsCurrency](/api/reference/go/resources/admin/subresources/organization/subresources/spend_limit/methods/update#(resource)%20admin.organization.spend_limit%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20currency%20%3E%20(schema)) = "USD"

Interval param.Field[[AdminOrganizationSpendLimitUpdateParamsInterval](/api/reference/go/resources/admin/subresources/organization/subresources/spend_limit/methods/update#(resource)%20admin.organization.spend_limit%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20interval%20%3E%20(schema))]

const AdminOrganizationSpendLimitUpdateParamsIntervalMonth [AdminOrganizationSpendLimitUpdateParamsInterval](/api/reference/go/resources/admin/subresources/organization/subresources/spend_limit/methods/update#(resource)%20admin.organization.spend_limit%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20interval%20%3E%20(schema)) = "month"

ThresholdAmount param.Field[int64]

minimum1

type OrganizationSpendLimit struct{…}

Represents a hard spend limit configured at the organization level.

Currency OrganizationSpendLimitCurrency

string

type OrganizationSpendLimitCurrency string

Enforcement OrganizationSpendLimitEnforcement

Status string

string

string

const OrganizationSpendLimitEnforcementStatusInactive OrganizationSpendLimitEnforcementStatus = "inactive"

const OrganizationSpendLimitEnforcementStatusEnforcing OrganizationSpendLimitEnforcementStatus = "enforcing"

Interval OrganizationSpendLimitInterval

string

type OrganizationSpendLimitInterval string

Object OrganizationSpendLimit

The object type, which is always `organization.spend_limit`.

ThresholdAmount int64

### Update organization spend limit

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
  organizationSpendLimit, err := client.Admin.Organization.SpendLimit.Update(context.TODO(), openai.AdminOrganizationSpendLimitUpdateParams{
    Currency: openai.AdminOrganizationSpendLimitUpdateParamsCurrencyUsd,
    Interval: openai.AdminOrganizationSpendLimitUpdateParamsIntervalMonth,
    ThresholdAmount: 1,
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", organizationSpendLimit.Currency)

    "object": "organization.spend_limit",
    "threshold_amount": 10000,
    "currency": "USD",
    "interval": "month",
    "enforcement": {
        "status": "enforcing"

    "object": "organization.spend_limit",
    "threshold_amount": 10000,
    "currency": "USD",
    "interval": "month",
    "enforcement": {
        "status": "enforcing"

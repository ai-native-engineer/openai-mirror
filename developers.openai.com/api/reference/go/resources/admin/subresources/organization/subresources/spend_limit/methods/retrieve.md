<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/spend_limit/methods/retrieve/ -->

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Spend Limit](/api/reference/go/resources/admin/subresources/organization/subresources/spend_limit)

# Retrieve organization spend limit

client.Admin.Organization.SpendLimit.Get(ctx) (\*[OrganizationSpendLimit](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit%20%3E%20(schema)), error)

GET/organization/spend\_limit

Get the organization’s hard spend limit.

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

### Retrieve organization spend limit

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
  organizationSpendLimit, err := client.Admin.Organization.SpendLimit.Get(context.TODO())
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

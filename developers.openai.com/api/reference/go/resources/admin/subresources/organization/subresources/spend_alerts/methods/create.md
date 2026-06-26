<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Spend Alerts](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create organization spend alert

client.Admin.Organization.SpendAlerts.New(ctx, body) (\*[OrganizationSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)), error)

POST/organization/spend\_alerts

Creates an organization spend alert.

##### ParametersExpand Collapse

body AdminOrganizationSpendAlertNewParams

Currency param.Field[[AdminOrganizationSpendAlertNewParamsCurrency](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/create#(resource)%20admin.organization.spend_alerts%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20currency%20%3E%20(schema))]

The currency for the threshold amount.

const AdminOrganizationSpendAlertNewParamsCurrencyUsd [AdminOrganizationSpendAlertNewParamsCurrency](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/create#(resource)%20admin.organization.spend_alerts%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20currency%20%3E%20(schema)) = "USD"

Interval param.Field[[AdminOrganizationSpendAlertNewParamsInterval](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/create#(resource)%20admin.organization.spend_alerts%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20interval%20%3E%20(schema))]

The time interval for evaluating spend against the threshold.

const AdminOrganizationSpendAlertNewParamsIntervalMonth [AdminOrganizationSpendAlertNewParamsInterval](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/create#(resource)%20admin.organization.spend_alerts%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20interval%20%3E%20(schema)) = "month"

NotificationChannel param.Field[[AdminOrganizationSpendAlertNewParamsNotificationChannel](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/create#(resource)%20admin.organization.spend_alerts%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20notification_channel%20%3E%20(schema))]

Email notification settings for a spend alert.

Recipients []string

Email addresses that receive the spend alert notification.

Type Email

The notification channel type. Currently only `email` is supported.

SubjectPrefix stringOptional

Optional subject prefix for alert emails.

ThresholdAmount param.Field[int64]

The alert threshold amount, in cents.

minimum0

##### ReturnsExpand Collapse

type OrganizationSpendAlert struct{…}

Represents a spend alert configured at the organization level.

ID string

The identifier, which can be referenced in API endpoints.

Currency OrganizationSpendAlertCurrency

The currency for the threshold amount.

Interval OrganizationSpendAlertInterval

The time interval for evaluating spend against the threshold.

NotificationChannel OrganizationSpendAlertNotificationChannel

Email notification settings for a spend alert.

Recipients []string

Email addresses that receive the spend alert notification.

Type Email

The notification channel type. Currently only `email` is supported.

SubjectPrefix stringOptional

Optional subject prefix for alert emails.

Object OrganizationSpendAlert

The object type, which is always `organization.spend_alert`.

ThresholdAmount int64

The alert threshold amount, in cents.

### Create organization spend alert

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  organizationSpendAlert, err := client.Admin.Organization.SpendAlerts.New(context.TODO(), openai.AdminOrganizationSpendAlertNewParams{
    Currency: openai.AdminOrganizationSpendAlertNewParamsCurrencyUsd,
    Interval: openai.AdminOrganizationSpendAlertNewParamsIntervalMonth,
    NotificationChannel: openai.AdminOrganizationSpendAlertNewParamsNotificationChannel{
      Recipients: []string{"string"},
    ThresholdAmount: 0,
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", organizationSpendAlert.ID)

    "id": "alert_abc123",
    "object": "organization.spend_alert",
    "threshold_amount": 100000,
    "currency": "USD",
    "interval": "month",
    "notification_channel": {
        "type": "email",
        "recipients": ["finance@example.com"],
        "subject_prefix": "OpenAI spend alert"

##### Returns Examples

    "id": "alert_abc123",
    "object": "organization.spend_alert",
    "threshold_amount": 100000,
    "currency": "USD",
    "interval": "month",
    "notification_channel": {
        "type": "email",
        "recipients": ["finance@example.com"],
        "subject_prefix": "OpenAI spend alert"

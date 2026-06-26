<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/list/ -->

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

# List organization spend alerts

client.Admin.Organization.SpendAlerts.List(ctx, query) (\*ConversationCursorPage[[OrganizationSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema))], error)

GET/organization/spend\_alerts

Lists organization spend alerts.

##### ParametersExpand Collapse

query AdminOrganizationSpendAlertListParams

After param.Field[string]Optional

Cursor for pagination. Provide the ID of the last spend alert from the previous response to fetch the next page.

Before param.Field[string]Optional

Cursor for pagination. Provide the ID of the first spend alert from the previous response to fetch the previous page.

Limit param.Field[int64]Optional

A limit on the number of spend alerts to return. Defaults to 20.

minimum0

maximum100

Order param.Field[[AdminOrganizationSpendAlertListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/list#(resource)%20admin.organization.spend_alerts%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order for the returned spend alerts.

const AdminOrganizationSpendAlertListParamsOrderAsc [AdminOrganizationSpendAlertListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/list#(resource)%20admin.organization.spend_alerts%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const AdminOrganizationSpendAlertListParamsOrderDesc [AdminOrganizationSpendAlertListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/list#(resource)%20admin.organization.spend_alerts%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

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

### List organization spend alerts

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
  page, err := client.Admin.Organization.SpendAlerts.List(context.TODO(), openai.AdminOrganizationSpendAlertListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

    "object": "list",
    "data": [
            "id": "alert_abc123",
            "object": "organization.spend_alert",
            "threshold_amount": 100000,
            "currency": "USD",
            "interval": "month",
            "notification_channel": {
                "type": "email",
                "recipients": ["finance@example.com"],
                "subject_prefix": "OpenAI spend alert"
    ],
    "first_id": "alert_abc123",
    "last_id": "alert_abc123",
    "has_more": false

##### Returns Examples

    "object": "list",
    "data": [
            "id": "alert_abc123",
            "object": "organization.spend_alert",
            "threshold_amount": 100000,
            "currency": "USD",
            "interval": "month",
            "notification_channel": {
                "type": "email",
                "recipients": ["finance@example.com"],
                "subject_prefix": "OpenAI spend alert"
    ],
    "first_id": "alert_abc123",
    "last_id": "alert_abc123",
    "has_more": false

<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Spend Alerts](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List project spend alerts

client.Admin.Organization.Projects.SpendAlerts.List(ctx, projectID, query) (\*ConversationCursorPage[[ProjectSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema))], error)

GET/organization/projects/{project\_id}/spend\_alerts

Lists project spend alerts.

##### ParametersExpand Collapse

projectID string

query AdminOrganizationProjectSpendAlertListParams

After param.Field[string]Optional

Cursor for pagination. Provide the ID of the last spend alert from the previous response to fetch the next page.

Before param.Field[string]Optional

Cursor for pagination. Provide the ID of the first spend alert from the previous response to fetch the previous page.

Limit param.Field[int64]Optional

A limit on the number of spend alerts to return. Defaults to 20.

minimum0

maximum100

Order param.Field[[AdminOrganizationProjectSpendAlertListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order for the returned spend alerts.

const AdminOrganizationProjectSpendAlertListParamsOrderAsc [AdminOrganizationProjectSpendAlertListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const AdminOrganizationProjectSpendAlertListParamsOrderDesc [AdminOrganizationProjectSpendAlertListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

##### ReturnsExpand Collapse

type ProjectSpendAlert struct{…}

Represents a spend alert configured at the project level.

ID string

The identifier, which can be referenced in API endpoints.

Currency ProjectSpendAlertCurrency

The currency for the threshold amount.

Interval ProjectSpendAlertInterval

The time interval for evaluating spend against the threshold.

NotificationChannel ProjectSpendAlertNotificationChannel

Email notification settings for a spend alert.

Recipients []string

Email addresses that receive the spend alert notification.

Type Email

The notification channel type. Currently only `email` is supported.

SubjectPrefix stringOptional

Optional subject prefix for alert emails.

Object ProjectSpendAlert

The object type, which is always `project.spend_alert`.

ThresholdAmount int64

The alert threshold amount, in cents.

### List project spend alerts

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
  page, err := client.Admin.Organization.Projects.SpendAlerts.List(
    context.TODO(),
    "project_id",
    openai.AdminOrganizationProjectSpendAlertListParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

    "object": "list",
    "data": [
            "id": "alert_abc123",
            "object": "project.spend_alert",
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
            "object": "project.spend_alert",
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

<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/retrieve/ -->

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

# Retrieve project spend alert

client.Admin.Organization.Projects.SpendAlerts.Get(ctx, projectID, alertID) (\*[ProjectSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

Retrieves a project spend alert.

##### ParametersExpand Collapse

projectID string

alertID string

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

### Retrieve project spend alert

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
  projectSpendAlert, err := client.Admin.Organization.Projects.SpendAlerts.Get(
    context.TODO(),
    "project_id",
    "alert_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectSpendAlert.ID)

    "id": "alert_abc123",
    "object": "project.spend_alert",
    "threshold_amount": 150000,
    "currency": "USD",
    "interval": "month",
    "notification_channel": {
        "type": "email",
        "recipients": ["finance@example.com"],
        "subject_prefix": "OpenAI spend alert"

##### Returns Examples

    "id": "alert_abc123",
    "object": "project.spend_alert",
    "threshold_amount": 150000,
    "currency": "USD",
    "interval": "month",
    "notification_channel": {
        "type": "email",
        "recipients": ["finance@example.com"],
        "subject_prefix": "OpenAI spend alert"

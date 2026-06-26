<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete/ -->

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

# Delete organization spend alert

client.Admin.Organization.SpendAlerts.Delete(ctx, alertID) (\*[OrganizationSpendAlertDeleted](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert_deleted%20%3E%20(schema)), error)

DELETE/organization/spend\_alerts/{alert\_id}

Deletes an organization spend alert.

##### ParametersExpand Collapse

alertID string

##### ReturnsExpand Collapse

type OrganizationSpendAlertDeleted struct{…}

Confirmation payload returned after deleting an organization spend alert.

ID string

The deleted spend alert ID.

Deleted bool

Whether the spend alert was deleted.

Object OrganizationSpendAlertDeleted

Always `organization.spend_alert.deleted`.

### Delete organization spend alert

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
  organizationSpendAlertDeleted, err := client.Admin.Organization.SpendAlerts.Delete(context.TODO(), "alert_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", organizationSpendAlertDeleted.ID)

    "id": "alert_abc123",
    "object": "organization.spend_alert.deleted",
    "deleted": true

##### Returns Examples

    "id": "alert_abc123",
    "object": "organization.spend_alert.deleted",
    "deleted": true

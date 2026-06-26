<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete/ -->

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

# Delete project spend alert

client.Admin.Organization.Projects.SpendAlerts.Delete(ctx, projectID, alertID) (\*[ProjectSpendAlertDeleted](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

Deletes a project spend alert.

##### ParametersExpand Collapse

projectID string

alertID string

##### ReturnsExpand Collapse

type ProjectSpendAlertDeleted struct{…}

Confirmation payload returned after deleting a project spend alert.

ID string

The deleted spend alert ID.

Deleted bool

Whether the spend alert was deleted.

Object ProjectSpendAlertDeleted

Always `project.spend_alert.deleted`.

### Delete project spend alert

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
  projectSpendAlertDeleted, err := client.Admin.Organization.Projects.SpendAlerts.Delete(
    context.TODO(),
    "project_id",
    "alert_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectSpendAlertDeleted.ID)

    "id": "alert_abc123",
    "object": "project.spend_alert.deleted",
    "deleted": true

##### Returns Examples

    "id": "alert_abc123",
    "object": "project.spend_alert.deleted",
    "deleted": true

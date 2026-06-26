<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[Spend Alerts](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete project spend alert

[ProjectSpendAlertDeleted](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema)) admin().organization().projects().spendAlerts().delete(SpendAlertDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

Deletes a project spend alert.

##### ParametersExpand Collapse

SpendAlertDeleteParams params

String projectId

Optional<String> alertId

##### ReturnsExpand Collapse

class ProjectSpendAlertDeleted:

Confirmation payload returned after deleting a project spend alert.

String id

The deleted spend alert ID.

boolean deleted

Whether the spend alert was deleted.

JsonValue; object\_ "project.spend\_alert.deleted"constant"project.spend\_alert.deleted"constant

Always `project.spend_alert.deleted`.

### Delete project spend alert

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.projects.spendalerts.ProjectSpendAlertDeleted;
import com.openai.models.admin.organization.projects.spendalerts.SpendAlertDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SpendAlertDeleteParams params = SpendAlertDeleteParams.builder()
            .projectId("project_id")
            .alertId("alert_id")
            .build();
        ProjectSpendAlertDeleted projectSpendAlertDeleted = client.admin().organization().projects().spendAlerts().delete(params);

    "id": "alert_abc123",
    "object": "project.spend_alert.deleted",
    "deleted": true

##### Returns Examples

    "id": "alert_abc123",
    "object": "project.spend_alert.deleted",
    "deleted": true

<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Spend Alerts](/api/reference/java/resources/admin/subresources/organization/subresources/spend_alerts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete organization spend alert

[OrganizationSpendAlertDeleted](/api/reference/java/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert_deleted%20%3E%20(schema)) admin().organization().spendAlerts().delete(SpendAlertDeleteParamsparams = SpendAlertDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/spend\_alerts/{alert\_id}

Deletes an organization spend alert.

##### ParametersExpand Collapse

SpendAlertDeleteParams params

Optional<String> alertId

##### ReturnsExpand Collapse

class OrganizationSpendAlertDeleted:

Confirmation payload returned after deleting an organization spend alert.

String id

The deleted spend alert ID.

boolean deleted

Whether the spend alert was deleted.

JsonValue; object\_ "organization.spend\_alert.deleted"constant"organization.spend\_alert.deleted"constant

Always `organization.spend_alert.deleted`.

### Delete organization spend alert

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
import com.openai.models.admin.organization.spendalerts.OrganizationSpendAlertDeleted;
import com.openai.models.admin.organization.spendalerts.SpendAlertDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        OrganizationSpendAlertDeleted organizationSpendAlertDeleted = client.admin().organization().spendAlerts().delete("alert_id");

    "id": "alert_abc123",
    "object": "organization.spend_alert.deleted",
    "deleted": true

##### Returns Examples

    "id": "alert_abc123",
    "object": "organization.spend_alert.deleted",
    "deleted": true

<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list/ -->

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

# List project spend alerts

SpendAlertListPage admin().organization().projects().spendAlerts().list(SpendAlertListParamsparams = SpendAlertListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/spend\_alerts

Lists project spend alerts.

##### ParametersExpand Collapse

SpendAlertListParams params

Optional<String> projectId

Optional<String> after

Cursor for pagination. Provide the ID of the last spend alert from the previous response to fetch the next page.

Optional<String> before

Cursor for pagination. Provide the ID of the first spend alert from the previous response to fetch the previous page.

Optional<Long> limit

A limit on the number of spend alerts to return. Defaults to 20.

minimum0

maximum100

Optional<[Order](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Sort order for the returned spend alerts.

ASC("asc")

DESC("desc")

##### ReturnsExpand Collapse

class ProjectSpendAlert:

Represents a spend alert configured at the project level.

String id

The identifier, which can be referenced in API endpoints.

Currency currency

The currency for the threshold amount.

Interval interval

The time interval for evaluating spend against the threshold.

NotificationChannel notificationChannel

Email notification settings for a spend alert.

List<String> recipients

Email addresses that receive the spend alert notification.

JsonValue; type "email"constant"email"constant

The notification channel type. Currently only `email` is supported.

Optional<String> subjectPrefix

Optional subject prefix for alert emails.

JsonValue; object\_ "project.spend\_alert"constant"project.spend\_alert"constant

The object type, which is always `project.spend_alert`.

long thresholdAmount

The alert threshold amount, in cents.

### List project spend alerts

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
import com.openai.models.admin.organization.projects.spendalerts.SpendAlertListPage;
import com.openai.models.admin.organization.projects.spendalerts.SpendAlertListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SpendAlertListPage page = client.admin().organization().projects().spendAlerts().list("project_id");

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

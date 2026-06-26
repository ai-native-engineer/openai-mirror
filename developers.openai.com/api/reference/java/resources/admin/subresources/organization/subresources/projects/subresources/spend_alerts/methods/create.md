<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/create/ -->

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

# Create project spend alert

[ProjectSpendAlert](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) admin().organization().projects().spendAlerts().create(SpendAlertCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/spend\_alerts

Creates a project spend alert.

##### ParametersExpand Collapse

SpendAlertCreateParams params

Optional<String> projectId

Currency currency

The currency for the threshold amount.

USD("USD")

Interval interval

The time interval for evaluating spend against the threshold.

MONTH("month")

NotificationChannel notificationChannel

Email notification settings for a spend alert.

List<String> recipients

Email addresses that receive the spend alert notification.

JsonValue; type "email"constant"email"constant

The notification channel type. Currently only `email` is supported.

Optional<String> subjectPrefix

Optional subject prefix for alert emails.

long thresholdAmount

The alert threshold amount, in cents.

minimum0

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

### Create project spend alert

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
import com.openai.models.admin.organization.projects.spendalerts.ProjectSpendAlert;
import com.openai.models.admin.organization.projects.spendalerts.SpendAlertCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SpendAlertCreateParams params = SpendAlertCreateParams.builder()
            .projectId("project_id")
            .currency(SpendAlertCreateParams.Currency.USD)
            .interval(SpendAlertCreateParams.Interval.MONTH)
            .notificationChannel(SpendAlertCreateParams.NotificationChannel.builder()
                .addRecipient("string")
                .build())
            .thresholdAmount(0L)
            .build();
        ProjectSpendAlert projectSpendAlert = client.admin().organization().projects().spendAlerts().create(params);

    "id": "alert_abc123",
    "object": "project.spend_alert",
    "threshold_amount": 100000,
    "currency": "USD",
    "interval": "month",
    "notification_channel": {
        "type": "email",
        "recipients": ["finance@example.com"],
        "subject_prefix": "OpenAI spend alert"

##### Returns Examples

    "id": "alert_abc123",
    "object": "project.spend_alert",
    "threshold_amount": 100000,
    "currency": "USD",
    "interval": "month",
    "notification_channel": {
        "type": "email",
        "recipients": ["finance@example.com"],
        "subject_prefix": "OpenAI spend alert"

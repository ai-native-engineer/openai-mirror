<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/spend_alerts/methods/create/ -->

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

# Create organization spend alert

[OrganizationSpendAlert](/api/reference/java/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) admin().organization().spendAlerts().create(SpendAlertCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/spend\_alerts

Creates an organization spend alert.

##### ParametersExpand Collapse

SpendAlertCreateParams params

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

class OrganizationSpendAlert:

Represents a spend alert configured at the organization level.

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

JsonValue; object\_ "organization.spend\_alert"constant"organization.spend\_alert"constant

The object type, which is always `organization.spend_alert`.

long thresholdAmount

The alert threshold amount, in cents.

### Create organization spend alert

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
import com.openai.models.admin.organization.spendalerts.OrganizationSpendAlert;
import com.openai.models.admin.organization.spendalerts.SpendAlertCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SpendAlertCreateParams params = SpendAlertCreateParams.builder()
            .currency(SpendAlertCreateParams.Currency.USD)
            .interval(SpendAlertCreateParams.Interval.MONTH)
            .notificationChannel(SpendAlertCreateParams.NotificationChannel.builder()
                .addRecipient("string")
                .build())
            .thresholdAmount(0L)
            .build();
        OrganizationSpendAlert organizationSpendAlert = client.admin().organization().spendAlerts().create(params);

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

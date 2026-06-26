<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/spend_alerts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Spend Alerts

##### [List organization spend alerts](/api/reference/java/resources/admin/subresources/organization/subresources/spend_alerts/methods/list)

SpendAlertListPage admin().organization().spendAlerts().list(SpendAlertListParamsparams = SpendAlertListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/spend\_alerts

##### [Create organization spend alert](/api/reference/java/resources/admin/subresources/organization/subresources/spend_alerts/methods/create)

[OrganizationSpendAlert](/api/reference/java/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) admin().organization().spendAlerts().create(SpendAlertCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/spend\_alerts

##### [Retrieve organization spend alert](/api/reference/java/resources/admin/subresources/organization/subresources/spend_alerts/methods/retrieve)

[OrganizationSpendAlert](/api/reference/java/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) admin().organization().spendAlerts().retrieve(SpendAlertRetrieveParamsparams = SpendAlertRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/spend\_alerts/{alert\_id}

##### [Update organization spend alert](/api/reference/java/resources/admin/subresources/organization/subresources/spend_alerts/methods/update)

[OrganizationSpendAlert](/api/reference/java/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) admin().organization().spendAlerts().update(SpendAlertUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/spend\_alerts/{alert\_id}

##### [Delete organization spend alert](/api/reference/java/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete)

[OrganizationSpendAlertDeleted](/api/reference/java/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert_deleted%20%3E%20(schema)) admin().organization().spendAlerts().delete(SpendAlertDeleteParamsparams = SpendAlertDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

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

class OrganizationSpendAlertDeleted:

Confirmation payload returned after deleting an organization spend alert.

String id

The deleted spend alert ID.

boolean deleted

Whether the spend alert was deleted.

JsonValue; object\_ "organization.spend\_alert.deleted"constant"organization.spend\_alert.deleted"constant

Always `organization.spend_alert.deleted`.

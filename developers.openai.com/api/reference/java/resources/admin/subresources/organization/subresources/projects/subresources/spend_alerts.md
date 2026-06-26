<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Spend Alerts

##### [List project spend alerts](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list)

SpendAlertListPage admin().organization().projects().spendAlerts().list(SpendAlertListParamsparams = SpendAlertListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/spend\_alerts

##### [Create project spend alert](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/create)

[ProjectSpendAlert](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) admin().organization().projects().spendAlerts().create(SpendAlertCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/spend\_alerts

##### [Retrieve project spend alert](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/retrieve)

[ProjectSpendAlert](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) admin().organization().projects().spendAlerts().retrieve(SpendAlertRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Update project spend alert](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/update)

[ProjectSpendAlert](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) admin().organization().projects().spendAlerts().update(SpendAlertUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Delete project spend alert](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete)

[ProjectSpendAlertDeleted](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema)) admin().organization().projects().spendAlerts().delete(SpendAlertDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

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

class ProjectSpendAlertDeleted:

Confirmation payload returned after deleting a project spend alert.

String id

The deleted spend alert ID.

boolean deleted

Whether the spend alert was deleted.

JsonValue; object\_ "project.spend\_alert.deleted"constant"project.spend\_alert.deleted"constant

Always `project.spend_alert.deleted`.

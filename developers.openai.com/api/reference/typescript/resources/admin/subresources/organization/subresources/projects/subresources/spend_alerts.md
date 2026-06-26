<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Spend Alerts

##### [List project spend alerts](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list)

client.admin.organization.projects.spendAlerts.list(stringprojectID, SpendAlertListParams { after, before, limit, order } query?, RequestOptionsoptions?): ConversationCursorPage<[ProjectSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more } >

GET/organization/projects/{project\_id}/spend\_alerts

##### [Create project spend alert](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/create)

client.admin.organization.projects.spendAlerts.create(stringprojectID, SpendAlertCreateParams { currency, interval, notification\_channel, threshold\_amount } body, RequestOptionsoptions?): [ProjectSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/projects/{project\_id}/spend\_alerts

##### [Retrieve project spend alert](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/retrieve)

client.admin.organization.projects.spendAlerts.retrieve(stringalertID, SpendAlertRetrieveParams { project\_id } params, RequestOptionsoptions?): [ProjectSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

GET/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Update project spend alert](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/update)

client.admin.organization.projects.spendAlerts.update(stringalertID, SpendAlertUpdateParams { project\_id, currency, interval, 2 more } params, RequestOptionsoptions?): [ProjectSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Delete project spend alert](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete)

client.admin.organization.projects.spendAlerts.delete(stringalertID, SpendAlertDeleteParams { project\_id } params, RequestOptionsoptions?): [ProjectSpendAlertDeleted](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

ProjectSpendAlert { id, currency, interval, 3 more }

Represents a spend alert configured at the project level.

id: string

The identifier, which can be referenced in API endpoints.

currency: "USD"

The currency for the threshold amount.

interval: "month"

The time interval for evaluating spend against the threshold.

notification\_channel: NotificationChannel { recipients, type, subject\_prefix }

Email notification settings for a spend alert.

recipients: Array<string>

Email addresses that receive the spend alert notification.

type: "email"

The notification channel type. Currently only `email` is supported.

subject\_prefix?: string | null

Optional subject prefix for alert emails.

object: "project.spend\_alert"

The object type, which is always `project.spend_alert`.

threshold\_amount: number

The alert threshold amount, in cents.

ProjectSpendAlertDeleted { id, deleted, object }

Confirmation payload returned after deleting a project spend alert.

id: string

The deleted spend alert ID.

deleted: boolean

Whether the spend alert was deleted.

object: "project.spend\_alert.deleted"

Always `project.spend_alert.deleted`.

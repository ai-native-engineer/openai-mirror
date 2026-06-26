<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Spend Alerts

##### [List project spend alerts](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list)

admin.organization.projects.spend\_alerts.list(project\_id, \*\*kwargs) -> ConversationCursorPage<[ProjectSpendAlert](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more } >

GET/organization/projects/{project\_id}/spend\_alerts

##### [Create project spend alert](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/create)

admin.organization.projects.spend\_alerts.create(project\_id, \*\*kwargs) -> [ProjectSpendAlert](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/projects/{project\_id}/spend\_alerts

##### [Retrieve project spend alert](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/retrieve)

admin.organization.projects.spend\_alerts.retrieve(alert\_id, \*\*kwargs) -> [ProjectSpendAlert](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

GET/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Update project spend alert](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/update)

admin.organization.projects.spend\_alerts.update(alert\_id, \*\*kwargs) -> [ProjectSpendAlert](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Delete project spend alert](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete)

admin.organization.projects.spend\_alerts.delete(alert\_id, \*\*kwargs) -> [ProjectSpendAlertDeleted](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

class ProjectSpendAlert { id, currency, interval, 3 more }

Represents a spend alert configured at the project level.

id: String

The identifier, which can be referenced in API endpoints.

currency: :USD

The currency for the threshold amount.

interval: :month

The time interval for evaluating spend against the threshold.

notification\_channel: NotificationChannel{ recipients, type, subject\_prefix}

Email notification settings for a spend alert.

recipients: Array[String]

Email addresses that receive the spend alert notification.

type: :email

The notification channel type. Currently only `email` is supported.

subject\_prefix: String

Optional subject prefix for alert emails.

object: :"project.spend\_alert"

The object type, which is always `project.spend_alert`.

threshold\_amount: Integer

The alert threshold amount, in cents.

class ProjectSpendAlertDeleted { id, deleted, object }

Confirmation payload returned after deleting a project spend alert.

id: String

The deleted spend alert ID.

deleted: bool

Whether the spend alert was deleted.

object: :"project.spend\_alert.deleted"

Always `project.spend_alert.deleted`.

<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_alerts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Spend Alerts

##### [List organization spend alerts](/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_alerts/methods/list)

admin.organization.spend\_alerts.list(\*\*kwargs) -> ConversationCursorPage<[OrganizationSpendAlert](/api/reference/ruby/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more } >

GET/organization/spend\_alerts

##### [Create organization spend alert](/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_alerts/methods/create)

admin.organization.spend\_alerts.create(\*\*kwargs) -> [OrganizationSpendAlert](/api/reference/ruby/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/spend\_alerts

##### [Retrieve organization spend alert](/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_alerts/methods/retrieve)

admin.organization.spend\_alerts.retrieve(alert\_id) -> [OrganizationSpendAlert](/api/reference/ruby/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

GET/organization/spend\_alerts/{alert\_id}

##### [Update organization spend alert](/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_alerts/methods/update)

admin.organization.spend\_alerts.update(alert\_id, \*\*kwargs) -> [OrganizationSpendAlert](/api/reference/ruby/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/spend\_alerts/{alert\_id}

##### [Delete organization spend alert](/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete)

admin.organization.spend\_alerts.delete(alert\_id) -> [OrganizationSpendAlertDeleted](/api/reference/ruby/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

class OrganizationSpendAlert { id, currency, interval, 3 more }

Represents a spend alert configured at the organization level.

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

object: :"organization.spend\_alert"

The object type, which is always `organization.spend_alert`.

threshold\_amount: Integer

The alert threshold amount, in cents.

class OrganizationSpendAlertDeleted { id, deleted, object }

Confirmation payload returned after deleting an organization spend alert.

id: String

The deleted spend alert ID.

deleted: bool

Whether the spend alert was deleted.

object: :"organization.spend\_alert.deleted"

Always `organization.spend_alert.deleted`.

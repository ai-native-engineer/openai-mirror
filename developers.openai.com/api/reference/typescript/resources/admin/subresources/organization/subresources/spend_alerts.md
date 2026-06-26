<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_alerts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Spend Alerts

##### [List organization spend alerts](/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_alerts/methods/list)

client.admin.organization.spendAlerts.list(SpendAlertListParams { after, before, limit, order } query?, RequestOptionsoptions?): ConversationCursorPage<[OrganizationSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more } >

GET/organization/spend\_alerts

##### [Create organization spend alert](/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_alerts/methods/create)

client.admin.organization.spendAlerts.create(SpendAlertCreateParams { currency, interval, notification\_channel, threshold\_amount } body, RequestOptionsoptions?): [OrganizationSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/spend\_alerts

##### [Retrieve organization spend alert](/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_alerts/methods/retrieve)

client.admin.organization.spendAlerts.retrieve(stringalertID, RequestOptionsoptions?): [OrganizationSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

GET/organization/spend\_alerts/{alert\_id}

##### [Update organization spend alert](/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_alerts/methods/update)

client.admin.organization.spendAlerts.update(stringalertID, SpendAlertUpdateParams { currency, interval, notification\_channel, threshold\_amount } body, RequestOptionsoptions?): [OrganizationSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/spend\_alerts/{alert\_id}

##### [Delete organization spend alert](/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete)

client.admin.organization.spendAlerts.delete(stringalertID, RequestOptionsoptions?): [OrganizationSpendAlertDeleted](/api/reference/typescript/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

OrganizationSpendAlert { id, currency, interval, 3 more }

Represents a spend alert configured at the organization level.

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

object: "organization.spend\_alert"

The object type, which is always `organization.spend_alert`.

threshold\_amount: number

The alert threshold amount, in cents.

OrganizationSpendAlertDeleted { id, deleted, object }

Confirmation payload returned after deleting an organization spend alert.

id: string

The deleted spend alert ID.

deleted: boolean

Whether the spend alert was deleted.

object: "organization.spend\_alert.deleted"

Always `organization.spend_alert.deleted`.

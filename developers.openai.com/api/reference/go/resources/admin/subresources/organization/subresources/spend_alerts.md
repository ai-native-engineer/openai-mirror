<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Spend Alerts

##### [List organization spend alerts](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/list)

client.Admin.Organization.SpendAlerts.List(ctx, query) (\*ConversationCursorPage[[OrganizationSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema))], error)

GET/organization/spend\_alerts

##### [Create organization spend alert](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/create)

client.Admin.Organization.SpendAlerts.New(ctx, body) (\*[OrganizationSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)), error)

POST/organization/spend\_alerts

##### [Retrieve organization spend alert](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/retrieve)

client.Admin.Organization.SpendAlerts.Get(ctx, alertID) (\*[OrganizationSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)), error)

GET/organization/spend\_alerts/{alert\_id}

##### [Update organization spend alert](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/update)

client.Admin.Organization.SpendAlerts.Update(ctx, alertID, body) (\*[OrganizationSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)), error)

POST/organization/spend\_alerts/{alert\_id}

##### [Delete organization spend alert](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete)

client.Admin.Organization.SpendAlerts.Delete(ctx, alertID) (\*[OrganizationSpendAlertDeleted](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert_deleted%20%3E%20(schema)), error)

DELETE/organization/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

type OrganizationSpendAlert struct{…}

Represents a spend alert configured at the organization level.

ID string

The identifier, which can be referenced in API endpoints.

Currency OrganizationSpendAlertCurrency

The currency for the threshold amount.

Interval OrganizationSpendAlertInterval

The time interval for evaluating spend against the threshold.

NotificationChannel OrganizationSpendAlertNotificationChannel

Email notification settings for a spend alert.

Recipients []string

Email addresses that receive the spend alert notification.

Type Email

The notification channel type. Currently only `email` is supported.

SubjectPrefix stringOptional

Optional subject prefix for alert emails.

Object OrganizationSpendAlert

The object type, which is always `organization.spend_alert`.

ThresholdAmount int64

The alert threshold amount, in cents.

type OrganizationSpendAlertDeleted struct{…}

Confirmation payload returned after deleting an organization spend alert.

ID string

The deleted spend alert ID.

Deleted bool

Whether the spend alert was deleted.

Object OrganizationSpendAlertDeleted

Always `organization.spend_alert.deleted`.

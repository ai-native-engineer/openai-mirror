<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/spend_alerts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Spend Alerts

##### [List organization spend alerts](/api/reference/python/resources/admin/subresources/organization/subresources/spend_alerts/methods/list)

admin.organization.spend\_alerts.list(SpendAlertListParams\*\*kwargs)  -> SyncConversationCursorPage[[OrganizationSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema))]

GET/organization/spend\_alerts

##### [Create organization spend alert](/api/reference/python/resources/admin/subresources/organization/subresources/spend_alerts/methods/create)

admin.organization.spend\_alerts.create(SpendAlertCreateParams\*\*kwargs)  -> [OrganizationSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema))

POST/organization/spend\_alerts

##### [Retrieve organization spend alert](/api/reference/python/resources/admin/subresources/organization/subresources/spend_alerts/methods/retrieve)

admin.organization.spend\_alerts.retrieve(stralert\_id)  -> [OrganizationSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema))

GET/organization/spend\_alerts/{alert\_id}

##### [Update organization spend alert](/api/reference/python/resources/admin/subresources/organization/subresources/spend_alerts/methods/update)

admin.organization.spend\_alerts.update(stralert\_id, SpendAlertUpdateParams\*\*kwargs)  -> [OrganizationSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema))

POST/organization/spend\_alerts/{alert\_id}

##### [Delete organization spend alert](/api/reference/python/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete)

admin.organization.spend\_alerts.delete(stralert\_id)  -> [OrganizationSpendAlertDeleted](/api/reference/python/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert_deleted%20%3E%20(schema))

DELETE/organization/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

class OrganizationSpendAlert: …

Represents a spend alert configured at the organization level.

id: str

The identifier, which can be referenced in API endpoints.

currency: Literal["USD"]

The currency for the threshold amount.

interval: Literal["month"]

The time interval for evaluating spend against the threshold.

notification\_channel: NotificationChannel

Email notification settings for a spend alert.

recipients: List[str]

Email addresses that receive the spend alert notification.

type: Literal["email"]

The notification channel type. Currently only `email` is supported.

subject\_prefix: Optional[str]

Optional subject prefix for alert emails.

object: Literal["organization.spend\_alert"]

The object type, which is always `organization.spend_alert`.

threshold\_amount: int

The alert threshold amount, in cents.

class OrganizationSpendAlertDeleted: …

Confirmation payload returned after deleting an organization spend alert.

id: str

The deleted spend alert ID.

deleted: bool

Whether the spend alert was deleted.

object: Literal["organization.spend\_alert.deleted"]

Always `organization.spend_alert.deleted`.

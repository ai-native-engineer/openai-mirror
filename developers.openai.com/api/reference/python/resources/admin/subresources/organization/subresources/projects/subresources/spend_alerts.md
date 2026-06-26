<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Spend Alerts

##### [List project spend alerts](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list)

admin.organization.projects.spend\_alerts.list(strproject\_id, SpendAlertListParams\*\*kwargs)  -> SyncConversationCursorPage[[ProjectSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema))]

GET/organization/projects/{project\_id}/spend\_alerts

##### [Create project spend alert](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/create)

admin.organization.projects.spend\_alerts.create(strproject\_id, SpendAlertCreateParams\*\*kwargs)  -> [ProjectSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema))

POST/organization/projects/{project\_id}/spend\_alerts

##### [Retrieve project spend alert](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/retrieve)

admin.organization.projects.spend\_alerts.retrieve(stralert\_id, SpendAlertRetrieveParams\*\*kwargs)  -> [ProjectSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema))

GET/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Update project spend alert](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/update)

admin.organization.projects.spend\_alerts.update(stralert\_id, SpendAlertUpdateParams\*\*kwargs)  -> [ProjectSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema))

POST/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Delete project spend alert](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete)

admin.organization.projects.spend\_alerts.delete(stralert\_id, SpendAlertDeleteParams\*\*kwargs)  -> [ProjectSpendAlertDeleted](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema))

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

class ProjectSpendAlert: …

Represents a spend alert configured at the project level.

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

object: Literal["project.spend\_alert"]

The object type, which is always `project.spend_alert`.

threshold\_amount: int

The alert threshold amount, in cents.

class ProjectSpendAlertDeleted: …

Confirmation payload returned after deleting a project spend alert.

id: str

The deleted spend alert ID.

deleted: bool

Whether the spend alert was deleted.

object: Literal["project.spend\_alert.deleted"]

Always `project.spend_alert.deleted`.

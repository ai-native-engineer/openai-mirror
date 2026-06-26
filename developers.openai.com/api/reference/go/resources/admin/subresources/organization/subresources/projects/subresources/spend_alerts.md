<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Spend Alerts

##### [List project spend alerts](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list)

client.Admin.Organization.Projects.SpendAlerts.List(ctx, projectID, query) (\*ConversationCursorPage[[ProjectSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema))], error)

GET/organization/projects/{project\_id}/spend\_alerts

##### [Create project spend alert](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/create)

client.Admin.Organization.Projects.SpendAlerts.New(ctx, projectID, body) (\*[ProjectSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/spend\_alerts

##### [Retrieve project spend alert](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/retrieve)

client.Admin.Organization.Projects.SpendAlerts.Get(ctx, projectID, alertID) (\*[ProjectSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Update project spend alert](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/update)

client.Admin.Organization.Projects.SpendAlerts.Update(ctx, projectID, alertID, body) (\*[ProjectSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Delete project spend alert](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete)

client.Admin.Organization.Projects.SpendAlerts.Delete(ctx, projectID, alertID) (\*[ProjectSpendAlertDeleted](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

type ProjectSpendAlert struct{…}

Represents a spend alert configured at the project level.

ID string

The identifier, which can be referenced in API endpoints.

Currency ProjectSpendAlertCurrency

The currency for the threshold amount.

Interval ProjectSpendAlertInterval

The time interval for evaluating spend against the threshold.

NotificationChannel ProjectSpendAlertNotificationChannel

Email notification settings for a spend alert.

Recipients []string

Email addresses that receive the spend alert notification.

Type Email

The notification channel type. Currently only `email` is supported.

SubjectPrefix stringOptional

Optional subject prefix for alert emails.

Object ProjectSpendAlert

The object type, which is always `project.spend_alert`.

ThresholdAmount int64

The alert threshold amount, in cents.

type ProjectSpendAlertDeleted struct{…}

Confirmation payload returned after deleting a project spend alert.

ID string

The deleted spend alert ID.

Deleted bool

Whether the spend alert was deleted.

Object ProjectSpendAlertDeleted

Always `project.spend_alert.deleted`.

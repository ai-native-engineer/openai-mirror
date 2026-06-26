<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Spend Alerts

##### [List project spend alerts](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list)

$ openai admin:organization:projects:spend-alerts list

GET/organization/projects/{project\_id}/spend\_alerts

##### [Create project spend alert](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/create)

$ openai admin:organization:projects:spend-alerts create

POST/organization/projects/{project\_id}/spend\_alerts

##### [Retrieve project spend alert](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/retrieve)

$ openai admin:organization:projects:spend-alerts retrieve

GET/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Update project spend alert](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/update)

$ openai admin:organization:projects:spend-alerts update

POST/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Delete project spend alert](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete)

$ openai admin:organization:projects:spend-alerts delete

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

project\_spend\_alert: object { id, currency, interval, 3 more }

Represents a spend alert configured at the project level.

id: string

The identifier, which can be referenced in API endpoints.

currency: "USD"

The currency for the threshold amount.

"USD"

interval: "month"

The time interval for evaluating spend against the threshold.

"month"

notification\_channel: object { recipients, type, subject\_prefix }

Email notification settings for a spend alert.

recipients: array of string

Email addresses that receive the spend alert notification.

type: "email"

The notification channel type. Currently only `email` is supported.

subject\_prefix: optional string

Optional subject prefix for alert emails.

object: "project.spend\_alert"

The object type, which is always `project.spend_alert`.

threshold\_amount: number

The alert threshold amount, in cents.

project\_spend\_alert\_deleted: object { id, deleted, object }

Confirmation payload returned after deleting a project spend alert.

id: string

The deleted spend alert ID.

deleted: boolean

Whether the spend alert was deleted.

object: "project.spend\_alert.deleted"

Always `project.spend_alert.deleted`.

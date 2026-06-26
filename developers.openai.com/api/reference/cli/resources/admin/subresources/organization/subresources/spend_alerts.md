<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/spend_alerts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Spend Alerts

##### [List organization spend alerts](/api/reference/cli/resources/admin/subresources/organization/subresources/spend_alerts/methods/list)

$ openai admin:organization:spend-alerts list

GET/organization/spend\_alerts

##### [Create organization spend alert](/api/reference/cli/resources/admin/subresources/organization/subresources/spend_alerts/methods/create)

$ openai admin:organization:spend-alerts create

POST/organization/spend\_alerts

##### [Retrieve organization spend alert](/api/reference/cli/resources/admin/subresources/organization/subresources/spend_alerts/methods/retrieve)

$ openai admin:organization:spend-alerts retrieve

GET/organization/spend\_alerts/{alert\_id}

##### [Update organization spend alert](/api/reference/cli/resources/admin/subresources/organization/subresources/spend_alerts/methods/update)

$ openai admin:organization:spend-alerts update

POST/organization/spend\_alerts/{alert\_id}

##### [Delete organization spend alert](/api/reference/cli/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete)

$ openai admin:organization:spend-alerts delete

DELETE/organization/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

organization\_spend\_alert: object { id, currency, interval, 3 more }

Represents a spend alert configured at the organization level.

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

object: "organization.spend\_alert"

The object type, which is always `organization.spend_alert`.

threshold\_amount: number

The alert threshold amount, in cents.

organization\_spend\_alert\_deleted: object { id, deleted, object }

Confirmation payload returned after deleting an organization spend alert.

id: string

The deleted spend alert ID.

deleted: boolean

Whether the spend alert was deleted.

object: "organization.spend\_alert.deleted"

Always `organization.spend_alert.deleted`.

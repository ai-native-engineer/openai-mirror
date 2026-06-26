<!-- source: https://help.openai.com/en/articles/9687866-admin-and-audit-logs-api-for-the-api-platform -->

# Admin and Audit Logs API for the API Platform

Obtain audit logs and perform admin actions in your API Platform organization.

Updated: 3 days ago

# Admin API capabilities

The Admin API enables Organization Owners and Security Teams to programmatically manage their OpenAI Organizations to enforce existing identity and access management policies to improve security and meet compliance requirements.  
  
With the Admin API, they can:

* List, create, retrieve, delete Invites in an Organization.
* List, create, update, retrieve, and delete Users in an Organization.

  + Update the roles of existing Users in an Organization.
* List, add, update, retrieve, and archive Projects in an Organization.
* List, add, retrieve, and remove Users in a Project.
* List, create, retrieve, and delete Service Accounts from a Project.
* List, retrieve, and delete API Keys in a Project.

* List, create, retrieve, and delete Admin API keys in an Organization.

[Visit our Admin API documentation to learn more.](https://developers.openai.com/api/reference/administration/overview)

## How do I create an Admin API key for my organization?

Organization Owners can create Admin API Keys in their [API Platform dashboard](https://platform.openai.com/) by selecting [Admin keys](https://platform.openai.com/organization/admin-keys) on the left-hand panel, and selecting Create new admin key on the top-left of the page.  
  
  
[Visit our Admin API documentation to learn more.](https://developers.openai.com/api/reference/administration/overview)

![Admin keys page listing organization admin API keys with a Create new admin key button](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-27c26187c74a7bf4c69c72d6/3731d04147a9cdd44b5715120f9e7161/AD_4nXdi5YCOn8zoMMzKy1ex3PIs_PWbjSlBUWrXQd1QLDHNtNV0iDtjLxpnKQQTeEXi-p5NwJWPdiii7dO2Rq_HfHKJohEnwIgDmdsWb69R9HLRD1Md-qHGRNUkpyN1)

## Who can use Admin API keys?

Only Organization Owners can create Admin API keys. Admin API keys can be used to authenticate Admin API requests with the required management scopes.

[Learn more about user roles in API Platform organizations.](/en/articles/9186755-managing-your-work-in-the-api-platform-with-projects#h_962ddad85d)

## Can I recover data I deleted with the Admin API?

Deleted data is not recoverable. This API does not provide the capability for deleting any data logged for audit or security within OpenAI. All authenticated requests to this API are logged for security and compliance purposes. When an item is deleted using this API, it is also removed from all internal search and retrieval indexes.

## How long does OpenAI retain my data for once I delete it with the Admin API?

Data is retained internally for no greater than 30 days following a deletion request.

## I lost my Admin API key - how do I recover it?

If an API key is lost, it cannot be recovered. We suggest deleting the previous key from your Admin Keys and creating a new one.

# Audit logging capabilities

The Audit Log API provides Security Teams with complete visibility into the state of their OpenAI Organizations by providing an immutable, auditable log of events that can help identify security issues, compliance risks, and gaps in operational procedures. With the Audit Logs API, they can track:

* The lifecycle of API Keys — creation, updates, and deletion.
* Account invitations — when the invitation was sent, accepted or deleted.
* The lifecycle of Users and Service Accounts — creation, updates, deletions, role assignment and changes.
* Login and logout failures.
* Updates to the Organization configuration.
* The lifecycle of Projects — creation, updates, and archival.

[Visit our Audit logging documentation to learn more.](https://platform.openai.com/docs/api-reference/audit-logs)

## How do I enable Audit logging for my organization?

> Please note: Once audit logging is enabled for your API Platform organization, it cannot be disabled. Only Organization owners can contact support to disable audit logging.

Organization Owners can enable audit logging by going to their [Organization setting -> Data controls -> Data retention](https://platform.openai.com/settings/organization/data-controls/data-retention) and turning on the Enable under Audit logging at the bottom. Once you save your selection, Audit logging will be enabled for your API Platform organization  
  
  
[Visit our Audit logging documentation to learn more.](https://developers.openai.com/api/reference/administration/overview)

![Data controls Data retention tab with API call logging set to Enabled per call](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-d23d04a194ef069a8b57a4cc/80667c5b4bd0ec4f979ef0e188797570/Screenshot_2025-03-11_at_12_42_10.png)

## Who can use Audit log API keys?

Only Organization Owners can create and use Admin API keys for the purposes of accessing Audit Logs. Please note that Audit logging will need to be enabled to receive Audit log data.  
  
  
[Learn more about user roles in API Platform organizations.](/en/articles/9186755-managing-your-work-in-the-api-platform-with-projects#h_962ddad85d)

## How long are API Platform audit logs retained?

API Platform audit logs do not currently have a fixed retention period or configured TTL. OpenAI retains these audit logs on a best-effort basis for as long as they remain available, but does not guarantee permanent availability.  
  
Because audit logs can be useful for long-term security, compliance, and administrative review, OpenAI does not automatically delete them after a short fixed window. Customers that need audit logs for their own retention, compliance, or eDiscovery policies should export and store copies in their own systems.  
  
API Platform audit logs record administrative and organization-configuration events, such as changes to users, projects, API keys, service accounts, and organization settings. They are separate from API request and response customer content.

## Does Zero Data Retention affect API Platform audit logs?

No. Zero Data Retention does not change the availability, retention behavior, or event contents of API Platform audit logs.  
  
Zero Data Retention applies to customer content retention for API usage and abuse-monitoring controls. API Platform audit logs are administrative/configuration metadata about the organization and are available independently of whether Zero Data Retention is enabled.

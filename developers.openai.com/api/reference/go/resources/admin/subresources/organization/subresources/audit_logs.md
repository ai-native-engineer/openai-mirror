<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/audit_logs/ -->

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

# Audit Logs

List user actions and configuration changes within this organization.

##### [List audit logs](/api/reference/go/resources/admin/subresources/organization/subresources/audit_logs/methods/list)

client.Admin.Organization.AuditLogs.List(ctx, query) (\*ConversationCursorPage[[AdminOrganizationAuditLogListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20AdminOrganizationAuditLogListResponse%20%3E%20(schema))], error)

GET/organization/audit\_logs

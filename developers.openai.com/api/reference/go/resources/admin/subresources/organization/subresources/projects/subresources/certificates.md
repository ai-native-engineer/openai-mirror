<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/certificates/ -->

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

# Certificates

##### [List project certificates](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list)

client.Admin.Organization.Projects.Certificates.List(ctx, projectID, query) (\*ConversationCursorPage[[AdminOrganizationProjectCertificateListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20AdminOrganizationProjectCertificateListResponse%20%3E%20(schema))], error)

GET/organization/projects/{project\_id}/certificates

##### [Activate certificates for project](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/activate)

client.Admin.Organization.Projects.Certificates.Activate(ctx, projectID, body) (\*Page[[AdminOrganizationProjectCertificateActivateResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20AdminOrganizationProjectCertificateActivateResponse%20%3E%20(schema))], error)

POST/organization/projects/{project\_id}/certificates/activate

##### [Deactivate certificates for project](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/deactivate)

client.Admin.Organization.Projects.Certificates.Deactivate(ctx, projectID, body) (\*Page[[AdminOrganizationProjectCertificateDeactivateResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20AdminOrganizationProjectCertificateDeactivateResponse%20%3E%20(schema))], error)

POST/organization/projects/{project\_id}/certificates/deactivate

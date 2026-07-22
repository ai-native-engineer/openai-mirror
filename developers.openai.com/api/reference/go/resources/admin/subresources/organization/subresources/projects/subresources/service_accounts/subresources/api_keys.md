<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/ -->

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

# API Keys

##### [Create project service account API key](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/methods/create)

client.Admin.Organization.Projects.ServiceAccounts.APIKeys.New(ctx, projectID, serviceAccountID, body) (\*[AdminOrganizationProjectServiceAccountAPIKeyNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20AdminOrganizationProjectServiceAccountAPIKeyNewResponse%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}/api\_keys

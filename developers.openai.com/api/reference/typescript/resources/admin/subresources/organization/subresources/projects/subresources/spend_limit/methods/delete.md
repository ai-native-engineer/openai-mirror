<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/delete/ -->

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

[Spend Limit](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit)

# Delete project spend limit

client.admin.organization.projects.spendLimit.delete(stringprojectID, RequestOptionsoptions?): [ProjectSpendLimitDeleted](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit_deleted%20%3E%20(schema)) { deleted, object }

DELETE/organization/projects/{project\_id}/spend\_limit

Delete a project’s hard spend limit.

##### ParametersExpand Collapse

projectID: string

ProjectSpendLimitDeleted { deleted, object }

Confirmation payload returned after deleting a project hard spend limit.

deleted: boolean

Whether the hard spend limit was deleted.

object: "project.spend\_limit.deleted"

The object type, which is always `project.spend_limit.deleted`.

### Delete project spend limit

TypeScript

import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const projectSpendLimitDeleted = await client.admin.organization.projects.spendLimit.delete(
  'proj_123',
);

console.log(projectSpendLimitDeleted.deleted);

    "object": "project.spend_limit.deleted",
    "deleted": true

    "object": "project.spend_limit.deleted",
    "deleted": true

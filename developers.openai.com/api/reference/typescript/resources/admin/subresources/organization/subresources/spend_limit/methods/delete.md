<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_limit/methods/delete/ -->

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Spend Limit](/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_limit)

# Delete organization spend limit

client.admin.organization.spendLimit.delete(RequestOptionsoptions?): [OrganizationSpendLimitDeleted](/api/reference/typescript/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit_deleted%20%3E%20(schema)) { deleted, object }

DELETE/organization/spend\_limit

Delete the organization’s hard spend limit.

OrganizationSpendLimitDeleted { deleted, object }

Confirmation payload returned after deleting an organization hard spend limit.

deleted: boolean

Whether the hard spend limit was deleted.

object: "organization.spend\_limit.deleted"

The object type, which is always `organization.spend_limit.deleted`.

### Delete organization spend limit

TypeScript

import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const organizationSpendLimitDeleted = await client.admin.organization.spendLimit.delete();

console.log(organizationSpendLimitDeleted.deleted);

    "object": "organization.spend_limit.deleted",
    "deleted": true

    "object": "organization.spend_limit.deleted",
    "deleted": true

<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/spend_limit/methods/delete/ -->

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Spend Limit](/api/reference/python/resources/admin/subresources/organization/subresources/spend_limit)

# Delete organization spend limit

admin.organization.spend\_limit.delete()  -> [OrganizationSpendLimitDeleted](/api/reference/python/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit_deleted%20%3E%20(schema))

DELETE/organization/spend\_limit

Delete the organization’s hard spend limit.

class OrganizationSpendLimitDeleted: …

Confirmation payload returned after deleting an organization hard spend limit.

deleted: bool

Whether the hard spend limit was deleted.

object: Literal["organization.spend\_limit.deleted"]

The object type, which is always `organization.spend_limit.deleted`.

### Delete organization spend limit

Python

import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
organization_spend_limit_deleted = client.admin.organization.spend_limit.delete()
print(organization_spend_limit_deleted.deleted)

    "object": "organization.spend_limit.deleted",
    "deleted": true

    "object": "organization.spend_limit.deleted",
    "deleted": true

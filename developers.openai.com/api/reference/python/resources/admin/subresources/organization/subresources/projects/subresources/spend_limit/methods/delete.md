<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/delete/ -->

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

[Spend Limit](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit)

# Delete project spend limit

admin.organization.projects.spend\_limit.delete(strproject\_id)  -> [ProjectSpendLimitDeleted](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit_deleted%20%3E%20(schema))

DELETE/organization/projects/{project\_id}/spend\_limit

Delete a project’s hard spend limit.

##### ParametersExpand Collapse

project\_id: str

class ProjectSpendLimitDeleted: …

Confirmation payload returned after deleting a project hard spend limit.

deleted: bool

Whether the hard spend limit was deleted.

object: Literal["project.spend\_limit.deleted"]

The object type, which is always `project.spend_limit.deleted`.

### Delete project spend limit

Python

import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
project_spend_limit_deleted = client.admin.organization.projects.spend_limit.delete(
    "proj_123",
)
print(project_spend_limit_deleted.deleted)

    "object": "project.spend_limit.deleted",
    "deleted": true

    "object": "project.spend_limit.deleted",
    "deleted": true

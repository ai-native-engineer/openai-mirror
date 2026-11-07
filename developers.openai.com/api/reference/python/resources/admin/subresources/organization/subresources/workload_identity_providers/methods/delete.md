<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/delete/ -->

## Delete Platform workload identity provider

`admin.organization.workload_identity_providers.delete(strworkload_identity_provider_id)  -> WorkloadIdentityProviderDeleted`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Delete a provider after deleting all its federation rules.

- `workload_identity_provider_id: str`

  `minLength: 1`

- `class WorkloadIdentityProviderDeleted: …`

  - `id: str`

  - `deleted: bool`

  - `object: Literal["organization.workload_identity_provider.deleted"]`

    - `"organization.workload_identity_provider.deleted"`

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
workload_identity_provider_deleted = client.admin.organization.workload_identity_providers.delete(
    "x",
print(workload_identity_provider_deleted.id)

  "deleted": true,
  "object": "organization.workload_identity_provider.deleted"

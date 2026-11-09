<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/external_keys/methods/validate/ -->

## Validate an external key config for the user's organization

`admin.organization.external_keys.validate(strexternal_key_id)  -> ExternalKeyValidateResponse`

**post** `/organization/external_keys/{external_key_id}/validate`

Validate an external key config for the user's organization

- `external_key_id: str`

- `class ExternalKeyValidateResponse: …`

  - `status: str`

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
response = client.admin.organization.external_keys.validate(
    "external_key_id",
print(response.status)

  "status": "status"

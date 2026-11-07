<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/list/ -->

## List Platform workload identity providers

`admin.organization.workload_identity_providers.list(WorkloadIdentityProviderListParams**kwargs)  -> SyncCursorPage[WorkloadIdentityProvider]`

**get** `/organization/workload_identity_providers`

List OIDC providers in the authenticated Admin API key's organization.

- `after: Optional[str]`

  `minLength: 1`

- `limit: Optional[int]`

  `minimum: 1`, `maximum: 100`

- `order: Optional[Union[Literal["asc", "desc"]]]`

  - `Literal["asc", "desc"]`

    - `"asc"`

    - `"desc"`

- `class WorkloadIdentityProvider: …`

  - `id: str`

  - `attribute_transformations: List[AttributeTransformation]`

    - `attribute: str`

    - `expression: str`

  - `audience: str`

  - `created_at: int`

  - `description: Optional[str]`

  - `enabled: bool`

  - `issuer: str`

  - `name: str`

  - `object: Literal["organization.workload_identity_provider"]`

    - `"organization.workload_identity_provider"`

  - `type: Literal["oidc"]`

    - `"oidc"`

  - `updated_at: int`

  - `verification: Verification`

    - `class VerificationDiscovery: …`

      - `discovery_url: Optional[str]`

      - `type: Literal["discovery"]`

        - `"discovery"`

    - `class VerificationUploadedJwks: …`

      - `jwks: Dict[str, object]`

      - `type: Literal["uploaded_jwks"]`

        - `"uploaded_jwks"`

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
page = client.admin.organization.workload_identity_providers.list()
page = page.data[0]
print(page.id)

  "data": [
      "attribute_transformations": [
          "attribute": "attribute",
          "expression": "expression"
      "audience": "audience",
      "enabled": true,
      "issuer": "issuer",
      "object": "organization.workload_identity_provider",
      "type": "oidc",
      "updated_at": 0,
      "verification": {
        "discovery_url": "discovery_url",
        "type": "discovery"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

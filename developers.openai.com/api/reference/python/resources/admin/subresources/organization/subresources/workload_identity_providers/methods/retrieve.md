<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/retrieve/ -->

## Retrieve Platform workload identity provider

`admin.organization.workload_identity_providers.retrieve(strworkload_identity_provider_id)  -> WorkloadIdentityProvider`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Retrieve an OIDC provider in the authenticated organization.

- `workload_identity_provider_id: str`

  `minLength: 1`

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
workload_identity_provider = client.admin.organization.workload_identity_providers.retrieve(
    "x",
print(workload_identity_provider.id)

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

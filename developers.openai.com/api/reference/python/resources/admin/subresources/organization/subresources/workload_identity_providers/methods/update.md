<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/update/ -->

## Update Platform workload identity provider

`admin.organization.workload_identity_providers.update(strworkload_identity_provider_id, WorkloadIdentityProviderUpdateParams**kwargs)  -> WorkloadIdentityProvider`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Update supplied provider fields, preserving omitted fields.

- `workload_identity_provider_id: str`

  `minLength: 1`

- `attribute_transformations: Optional[Iterable[AttributeTransformation]]`

  `maxItems: 20`

  - `attribute: str`

    `minLength: 1`, `maxLength: 256`

  - `expression: str`

    `minLength: 1`, `maxLength: 4096`

- `audience: Optional[str]`

  `minLength: 1`

- `description: Optional[str]`

- `enabled: Optional[bool]`

- `issuer: Optional[str]`

  `minLength: 1`

- `name: Optional[str]`

  `minLength: 1`

- `verification: Optional[Verification]`

  - `class VerificationDiscoveryVerificationParam: …`

    - `discovery_url: Optional[str]`

    - `type: Literal["discovery"]`

      - `"discovery"`

  - `class VerificationUploadedJwksVerificationParam: …`

    - `jwks: Dict[str, object]`

    - `type: Literal["uploaded_jwks"]`

      - `"uploaded_jwks"`

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
workload_identity_provider = client.admin.organization.workload_identity_providers.update(
    workload_identity_provider_id="x",
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

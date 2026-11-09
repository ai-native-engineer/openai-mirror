<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/external_keys/ -->

# External Keys

## Add an external key config for an organization

`admin.organization.external_keys.create(**kwargs) -> ExternalKey`

**post** `/organization/external_keys`

Add an external key config for an organization

### Parameters

- `body: Aws{ external_id, kms_arn, name, 3 more} | Gcp{ audience, kms_key_location, kms_key_name, 9 more} | Azure{ key_name, name, tenant_id, 4 more}`

  - `class Aws`

    - `external_id: String`

      The ExternalID that OpenAI will pass in the AssumeRole call for the customer's AWS account. This must be the OpenAI organization ID or an API project ID that belongs to the organization.

    - `kms_arn: String`

      The Key Management System ARN for the master key you manage

    - `name: String`

      A friendly name to identify this config

    - `role_arn: String`

      The Role ARN that OpenAI will assume to call your KMS

    - `type: :aws`

      - `:aws`

    - `purpose: :ekm | :psp_decryption`

      - `:ekm`

      - `:psp_decryption`

  - `class Gcp`

    - `audience: String`

      The aud field in the identity token OpenAI will pass in the call to the customer's GCP STS. This must be the OpenAI organization ID or an API project ID that belongs to the organization.

    - `kms_key_location: String`

      The region where your Key Management System master key is located

    - `kms_key_name: String`

      The name of the Key Management System master key you manage

    - `kms_key_ring_name: String`

      The Key Management System key ring for the master key you manage

    - `kms_project_id: String`

      The string GCP project name where your KMS resides

    - `name: String`

      A friendly name to identify this config

    - `type: :gcp`

      - `:gcp`

    - `workload_identity_pool_id: String`

      The pool containing the Workload Identity provider that you registered for OpenAI

    - `workload_identity_project_number: String`

      The numeric GCP project number where you registered OpenAI's workload identity

    - `workload_identity_provider_id: String`

      The Workload Identity provider that you registered for OpenAI

    - `kms_key_version: String`

      An exact CryptoKeyVersion number. Required for PSP decryption; not accepted for EKM.

    - `purpose: :ekm | :psp_decryption`

      - `:ekm`

      - `:psp_decryption`

  - `class Azure`

    - `key_name: String`

      The name of the Azure Key Vault master key that you manage

      `maxLength: 127`

    - `name: String`

      A friendly name to identify this config

    - `tenant_id: String`

      Your Azure tenant UUID

    - `type: :azure`

      - `:azure`

    - `vault_uri: String`

      The URI of the Azure vault containing the master key you manage

    - `key_version: String`

      An exact Azure Key Vault key version. Required for PSP decryption; not accepted for EKM.

    - `purpose: :ekm | :psp_decryption`

      - `:ekm`

      - `:psp_decryption`

### Returns

- `class ExternalKey`

  - `id: String`

  - `api_project_ids: Array[String]`

  - `created_at: Integer`

  - `name: String`

  - `object: String`

  - `type: String`

  - `workspace_id: String`

  - `audience: String`

  - `external_id: String`

  - `key_name: String`

  - `key_version: String`

  - `kms_arn: String`

  - `kms_key_location: String`

  - `kms_key_name: String`

  - `kms_key_ring_name: String`

  - `kms_key_version: String`

  - `kms_project_id: String`

  - `purpose: :ekm | :psp_decryption`

    - `:ekm`

    - `:psp_decryption`

  - `role_arn: String`

  - `tenant_id: String`

  - `vault_uri: String`

  - `workload_identity_pool_id: String`

  - `workload_identity_project_number: String`

  - `workload_identity_provider_id: String`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

external_key = openai.admin.organization.external_keys.create(
  body: {external_id: "external_id", kms_arn: "kms_arn", name: "name", role_arn: "arn:aws:iam::123456789012:role/example-role", type: :aws}
)

puts(external_key)
```

#### 200 — Example

```json
{
  "id": "id",
  "api_project_ids": [
    "string"
  ],
  "created_at": 0,
  "name": "name",
  "object": "object",
  "type": "type",
  "workspace_id": "workspace_id",
  "audience": "audience",
  "external_id": "external_id",
  "key_name": "key_name",
  "key_version": "key_version",
  "kms_arn": "kms_arn",
  "kms_key_location": "kms_key_location",
  "kms_key_name": "kms_key_name",
  "kms_key_ring_name": "kms_key_ring_name",
  "kms_key_version": "kms_key_version",
  "kms_project_id": "kms_project_id",
  "purpose": "ekm",
  "role_arn": "role_arn",
  "tenant_id": "tenant_id",
  "vault_uri": "vault_uri",
  "workload_identity_pool_id": "workload_identity_pool_id",
  "workload_identity_project_number": "workload_identity_project_number",
  "workload_identity_provider_id": "workload_identity_provider_id"
}
```

## Delete an external key config for the user's organization

`admin.organization.external_keys.delete(external_key_id) -> ExternalKey`

**delete** `/organization/external_keys/{external_key_id}`

Delete an external key config for the user's organization

### Parameters

- `external_key_id: String`

### Returns

- `class ExternalKey`

  - `id: String`

  - `api_project_ids: Array[String]`

  - `created_at: Integer`

  - `name: String`

  - `object: String`

  - `type: String`

  - `workspace_id: String`

  - `audience: String`

  - `external_id: String`

  - `key_name: String`

  - `key_version: String`

  - `kms_arn: String`

  - `kms_key_location: String`

  - `kms_key_name: String`

  - `kms_key_ring_name: String`

  - `kms_key_version: String`

  - `kms_project_id: String`

  - `purpose: :ekm | :psp_decryption`

    - `:ekm`

    - `:psp_decryption`

  - `role_arn: String`

  - `tenant_id: String`

  - `vault_uri: String`

  - `workload_identity_pool_id: String`

  - `workload_identity_project_number: String`

  - `workload_identity_provider_id: String`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

external_key = openai.admin.organization.external_keys.delete("external_key_id")

puts(external_key)
```

#### 200 — Example

```json
{
  "id": "id",
  "api_project_ids": [
    "string"
  ],
  "created_at": 0,
  "name": "name",
  "object": "object",
  "type": "type",
  "workspace_id": "workspace_id",
  "audience": "audience",
  "external_id": "external_id",
  "key_name": "key_name",
  "key_version": "key_version",
  "kms_arn": "kms_arn",
  "kms_key_location": "kms_key_location",
  "kms_key_name": "kms_key_name",
  "kms_key_ring_name": "kms_key_ring_name",
  "kms_key_version": "kms_key_version",
  "kms_project_id": "kms_project_id",
  "purpose": "ekm",
  "role_arn": "role_arn",
  "tenant_id": "tenant_id",
  "vault_uri": "vault_uri",
  "workload_identity_pool_id": "workload_identity_pool_id",
  "workload_identity_project_number": "workload_identity_project_number",
  "workload_identity_provider_id": "workload_identity_provider_id"
}
```

## List the external key configs registered on the user's organization

`admin.organization.external_keys.list(**kwargs) -> CursorPage<ExternalKey>`

**get** `/organization/external_keys`

List the external key configs registered on the user's organization

### Parameters

- `after: String`

- `limit: Integer`

  `minimum: 0`, `maximum: 100`

- `order: :asc | :desc`

  - `:asc`

  - `:desc`

- `purpose: :ekm | :psp_decryption`

  Filter by key purpose. When omitted, returns keys of all purposes.

  - `:ekm`

  - `:psp_decryption`

### Returns

- `class ExternalKey`

  - `id: String`

  - `api_project_ids: Array[String]`

  - `created_at: Integer`

  - `name: String`

  - `object: String`

  - `type: String`

  - `workspace_id: String`

  - `audience: String`

  - `external_id: String`

  - `key_name: String`

  - `key_version: String`

  - `kms_arn: String`

  - `kms_key_location: String`

  - `kms_key_name: String`

  - `kms_key_ring_name: String`

  - `kms_key_version: String`

  - `kms_project_id: String`

  - `purpose: :ekm | :psp_decryption`

    - `:ekm`

    - `:psp_decryption`

  - `role_arn: String`

  - `tenant_id: String`

  - `vault_uri: String`

  - `workload_identity_pool_id: String`

  - `workload_identity_project_number: String`

  - `workload_identity_provider_id: String`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

page = openai.admin.organization.external_keys.list

puts(page)
```

#### 200 — Example

```json
{
  "data": [
    {
      "id": "id",
      "api_project_ids": [
        "string"
      ],
      "created_at": 0,
      "name": "name",
      "object": "object",
      "type": "type",
      "workspace_id": "workspace_id",
      "audience": "audience",
      "external_id": "external_id",
      "key_name": "key_name",
      "key_version": "key_version",
      "kms_arn": "kms_arn",
      "kms_key_location": "kms_key_location",
      "kms_key_name": "kms_key_name",
      "kms_key_ring_name": "kms_key_ring_name",
      "kms_key_version": "kms_key_version",
      "kms_project_id": "kms_project_id",
      "purpose": "ekm",
      "role_arn": "role_arn",
      "tenant_id": "tenant_id",
      "vault_uri": "vault_uri",
      "workload_identity_pool_id": "workload_identity_pool_id",
      "workload_identity_project_number": "workload_identity_project_number",
      "workload_identity_provider_id": "workload_identity_provider_id"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve an external key registration

`admin.organization.external_keys.retrieve(external_key_id) -> ExternalKey`

**get** `/organization/external_keys/{external_key_id}`

Retrieve a stored external key registration for the user's organization.

### Parameters

- `external_key_id: String`

### Returns

- `class ExternalKey`

  - `id: String`

  - `api_project_ids: Array[String]`

  - `created_at: Integer`

  - `name: String`

  - `object: String`

  - `type: String`

  - `workspace_id: String`

  - `audience: String`

  - `external_id: String`

  - `key_name: String`

  - `key_version: String`

  - `kms_arn: String`

  - `kms_key_location: String`

  - `kms_key_name: String`

  - `kms_key_ring_name: String`

  - `kms_key_version: String`

  - `kms_project_id: String`

  - `purpose: :ekm | :psp_decryption`

    - `:ekm`

    - `:psp_decryption`

  - `role_arn: String`

  - `tenant_id: String`

  - `vault_uri: String`

  - `workload_identity_pool_id: String`

  - `workload_identity_project_number: String`

  - `workload_identity_provider_id: String`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

external_key = openai.admin.organization.external_keys.retrieve("external_key_id")

puts(external_key)
```

#### 200 — Example

```json
{
  "id": "id",
  "api_project_ids": [
    "string"
  ],
  "created_at": 0,
  "name": "name",
  "object": "object",
  "type": "type",
  "workspace_id": "workspace_id",
  "audience": "audience",
  "external_id": "external_id",
  "key_name": "key_name",
  "key_version": "key_version",
  "kms_arn": "kms_arn",
  "kms_key_location": "kms_key_location",
  "kms_key_name": "kms_key_name",
  "kms_key_ring_name": "kms_key_ring_name",
  "kms_key_version": "kms_key_version",
  "kms_project_id": "kms_project_id",
  "purpose": "ekm",
  "role_arn": "role_arn",
  "tenant_id": "tenant_id",
  "vault_uri": "vault_uri",
  "workload_identity_pool_id": "workload_identity_pool_id",
  "workload_identity_project_number": "workload_identity_project_number",
  "workload_identity_provider_id": "workload_identity_provider_id"
}
```

## Validate an external key config for the user's organization

`admin.organization.external_keys.validate(external_key_id) -> ExternalKeyValidateResponse`

**post** `/organization/external_keys/{external_key_id}/validate`

Validate an external key config for the user's organization

### Parameters

- `external_key_id: String`

### Returns

- `class ExternalKeyValidateResponse`

  - `status: String`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

response = openai.admin.organization.external_keys.validate("external_key_id")

puts(response)
```

#### 200 — Example

```json
{
  "status": "status"
}
```

## Domain Types

### External Key

- `class ExternalKey`

  - `id: String`

  - `api_project_ids: Array[String]`

  - `created_at: Integer`

  - `name: String`

  - `object: String`

  - `type: String`

  - `workspace_id: String`

  - `audience: String`

  - `external_id: String`

  - `key_name: String`

  - `key_version: String`

  - `kms_arn: String`

  - `kms_key_location: String`

  - `kms_key_name: String`

  - `kms_key_ring_name: String`

  - `kms_key_version: String`

  - `kms_project_id: String`

  - `purpose: :ekm | :psp_decryption`

    - `:ekm`

    - `:psp_decryption`

  - `role_arn: String`

  - `tenant_id: String`

  - `vault_uri: String`

  - `workload_identity_pool_id: String`

  - `workload_identity_project_number: String`

  - `workload_identity_provider_id: String`

### External Key Validate Response

- `class ExternalKeyValidateResponse`

  - `status: String`

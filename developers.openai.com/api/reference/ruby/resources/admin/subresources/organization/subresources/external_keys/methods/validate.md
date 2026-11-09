<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/external_keys/methods/validate/ -->

## Validate an external key config for the user's organization

`admin.organization.external_keys.validate(external_key_id) -> ExternalKeyValidateResponse`

**post** `/organization/external_keys/{external_key_id}/validate`

Validate an external key config for the user's organization

- `external_key_id: String`

- `class ExternalKeyValidateResponse`

  - `status: String`

```ruby
require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

response = openai.admin.organization.external_keys.validate("external_key_id")

puts(response)

  "status": "status"

<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Admin API Keys](/api/reference/cli/resources/admin/subresources/organization/subresources/admin_api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete admin API key

$ openai admin:organization:admin-api-keys delete

DELETE/organization/admin\_api\_keys/{key\_id}

Delete an organization admin API key

##### ParametersExpand Collapse

--key-id: string

The ID of the API key to be deleted.

##### ReturnsExpand Collapse

AdminOrganizationAdminAPIKeyDeleteResponse: object { id, deleted, object }

id: string

deleted: boolean

object: "organization.admin\_api\_key.deleted"

### Delete admin API key

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:admin-api-keys delete \
  --admin-api-key 'My Admin API Key' \
  --key-id key_id

  "id": "key_abc",
  "object": "organization.admin_api_key.deleted",
  "deleted": true

##### Returns Examples

  "id": "key_abc",
  "object": "organization.admin_api_key.deleted",
  "deleted": true

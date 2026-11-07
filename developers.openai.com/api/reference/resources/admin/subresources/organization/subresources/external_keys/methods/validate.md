<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/external_keys/methods/validate/ -->

> For the complete documentation index, see [llms.txt](/llms.txt). Markdown versions of documentation pages are available by appending `.md` to the page URL.

## Validate an external key config for the user's organization

**post** `/organization/external_keys/{external_key_id}/validate`

Validate an external key config for the user's organization

### Path Parameters

- `external_key_id: string`

- `status: string`

```http
curl https://api.openai.com/v1/organization/external_keys/$EXTERNAL_KEY_ID/validate \
    -X POST \
    -H "Authorization: Bearer $OPENAI_ADMIN_KEY"

  "status": "status"

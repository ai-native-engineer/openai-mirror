<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/data_retention/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Data Retention](/api/reference/resources/admin/subresources/organization/subresources/data_retention)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update organization data retention

POST/organization/data\_retention

Updates organization data retention controls.

##### Body ParametersJSONExpand Collapse

retention\_type: "zero\_data\_retention" or "modified\_abuse\_monitoring" or "enhanced\_zero\_data\_retention" or "enhanced\_modified\_abuse\_monitoring"

The desired organization data retention type.

One of the following:

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

##### ReturnsExpand Collapse

OrganizationDataRetention object { object, type }

Represents the organization’s data retention control setting.

object: "organization.data\_retention"

The object type, which is always `organization.data_retention`.

type: "zero\_data\_retention" or "modified\_abuse\_monitoring" or "enhanced\_zero\_data\_retention" or "enhanced\_modified\_abuse\_monitoring"

The configured organization data retention type.

One of the following:

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

### Update organization data retention

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X POST https://api.openai.com/v1/organization/data_retention \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "retention_type": "modified_abuse_monitoring"
  }'

    "object": "organization.data_retention",
    "type": "modified_abuse_monitoring"

##### Returns Examples

    "object": "organization.data_retention",
    "type": "modified_abuse_monitoring"

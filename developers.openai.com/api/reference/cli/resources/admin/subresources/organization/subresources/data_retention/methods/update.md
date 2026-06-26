<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/data_retention/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Data Retention](/api/reference/cli/resources/admin/subresources/organization/subresources/data_retention)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update organization data retention

$ openai admin:organization:data-retention update

POST/organization/data\_retention

Updates organization data retention controls.

##### ParametersExpand Collapse

--retention-type: "zero\_data\_retention" or "modified\_abuse\_monitoring" or "enhanced\_zero\_data\_retention" or "enhanced\_modified\_abuse\_monitoring"

The desired organization data retention type.

##### ReturnsExpand Collapse

organization\_data\_retention: object { object, type }

Represents the organization’s data retention control setting.

object: "organization.data\_retention"

The object type, which is always `organization.data_retention`.

type: "zero\_data\_retention" or "modified\_abuse\_monitoring" or "enhanced\_zero\_data\_retention" or "enhanced\_modified\_abuse\_monitoring"

The configured organization data retention type.

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

### Update organization data retention

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:data-retention update \
  --admin-api-key 'My Admin API Key' \
  --retention-type zero_data_retention

    "object": "organization.data_retention",
    "type": "modified_abuse_monitoring"

##### Returns Examples

    "object": "organization.data_retention",
    "type": "modified_abuse_monitoring"

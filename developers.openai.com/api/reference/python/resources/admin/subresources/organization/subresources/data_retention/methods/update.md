<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/data_retention/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Data Retention](/api/reference/python/resources/admin/subresources/organization/subresources/data_retention)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update organization data retention

admin.organization.data\_retention.update(DataRetentionUpdateParams\*\*kwargs)  -> [OrganizationDataRetention](/api/reference/python/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema))

POST/organization/data\_retention

Updates organization data retention controls.

##### ParametersExpand Collapse

retention\_type: Literal["zero\_data\_retention", "modified\_abuse\_monitoring", "enhanced\_zero\_data\_retention", "enhanced\_modified\_abuse\_monitoring"]

The desired organization data retention type.

One of the following:

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

##### ReturnsExpand Collapse

class OrganizationDataRetention: …

Represents the organization’s data retention control setting.

object: Literal["organization.data\_retention"]

The object type, which is always `organization.data_retention`.

type: Literal["zero\_data\_retention", "modified\_abuse\_monitoring", "enhanced\_zero\_data\_retention", "enhanced\_modified\_abuse\_monitoring"]

The configured organization data retention type.

One of the following:

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

### Update organization data retention

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
organization_data_retention = client.admin.organization.data_retention.update(
    retention_type="zero_data_retention",
print(organization_data_retention.object)

    "object": "organization.data_retention",
    "type": "modified_abuse_monitoring"

##### Returns Examples

    "object": "organization.data_retention",
    "type": "modified_abuse_monitoring"

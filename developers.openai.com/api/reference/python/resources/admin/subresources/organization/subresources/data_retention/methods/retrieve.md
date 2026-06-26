<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/data_retention/methods/retrieve/ -->

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

# Retrieve organization data retention

admin.organization.data\_retention.retrieve()  -> [OrganizationDataRetention](/api/reference/python/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema))

GET/organization/data\_retention

Retrieves organization data retention controls.

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

### Retrieve organization data retention

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
organization_data_retention = client.admin.organization.data_retention.retrieve()
print(organization_data_retention.object)

    "object": "organization.data_retention",
    "type": "modified_abuse_monitoring"

##### Returns Examples

    "object": "organization.data_retention",
    "type": "modified_abuse_monitoring"

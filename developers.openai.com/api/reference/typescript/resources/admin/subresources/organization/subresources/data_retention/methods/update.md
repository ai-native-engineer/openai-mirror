<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/data_retention/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Data Retention](/api/reference/typescript/resources/admin/subresources/organization/subresources/data_retention)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update organization data retention

client.admin.organization.dataRetention.update(DataRetentionUpdateParams { retention\_type } body, RequestOptionsoptions?): [OrganizationDataRetention](/api/reference/typescript/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema)) { object, type }

POST/organization/data\_retention

Updates organization data retention controls.

##### ParametersExpand Collapse

body: DataRetentionUpdateParams { retention\_type }

retention\_type: "zero\_data\_retention" | "modified\_abuse\_monitoring" | "enhanced\_zero\_data\_retention" | "enhanced\_modified\_abuse\_monitoring"

The desired organization data retention type.

One of the following:

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

##### ReturnsExpand Collapse

OrganizationDataRetention { object, type }

Represents the organization’s data retention control setting.

object: "organization.data\_retention"

The object type, which is always `organization.data_retention`.

type: "zero\_data\_retention" | "modified\_abuse\_monitoring" | "enhanced\_zero\_data\_retention" | "enhanced\_modified\_abuse\_monitoring"

The configured organization data retention type.

One of the following:

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

### Update organization data retention

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted

const organizationDataRetention = await client.admin.organization.dataRetention.update({
  retention_type: 'zero_data_retention',

console.log(organizationDataRetention.object);

    "object": "organization.data_retention",
    "type": "modified_abuse_monitoring"

##### Returns Examples

    "object": "organization.data_retention",
    "type": "modified_abuse_monitoring"

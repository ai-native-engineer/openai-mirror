<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/data_retention/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Data Retention

##### [Retrieve organization data retention](/api/reference/cli/resources/admin/subresources/organization/subresources/data_retention/methods/retrieve)

$ openai admin:organization:data-retention retrieve

GET/organization/data\_retention

##### [Update organization data retention](/api/reference/cli/resources/admin/subresources/organization/subresources/data_retention/methods/update)

$ openai admin:organization:data-retention update

POST/organization/data\_retention

##### ModelsExpand Collapse

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

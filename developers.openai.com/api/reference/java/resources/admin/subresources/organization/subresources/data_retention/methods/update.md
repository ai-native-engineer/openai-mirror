<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/data_retention/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Data Retention](/api/reference/java/resources/admin/subresources/organization/subresources/data_retention)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update organization data retention

[OrganizationDataRetention](/api/reference/java/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema)) admin().organization().dataRetention().update(DataRetentionUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/data\_retention

Updates organization data retention controls.

##### ParametersExpand Collapse

DataRetentionUpdateParams params

RetentionType retentionType

The desired organization data retention type.

ZERO\_DATA\_RETENTION("zero\_data\_retention")

MODIFIED\_ABUSE\_MONITORING("modified\_abuse\_monitoring")

ENHANCED\_ZERO\_DATA\_RETENTION("enhanced\_zero\_data\_retention")

ENHANCED\_MODIFIED\_ABUSE\_MONITORING("enhanced\_modified\_abuse\_monitoring")

##### ReturnsExpand Collapse

class OrganizationDataRetention:

Represents the organization’s data retention control setting.

JsonValue; object\_ "organization.data\_retention"constant"organization.data\_retention"constant

The object type, which is always `organization.data_retention`.

Type type

The configured organization data retention type.

One of the following:

ZERO\_DATA\_RETENTION("zero\_data\_retention")

MODIFIED\_ABUSE\_MONITORING("modified\_abuse\_monitoring")

ENHANCED\_ZERO\_DATA\_RETENTION("enhanced\_zero\_data\_retention")

ENHANCED\_MODIFIED\_ABUSE\_MONITORING("enhanced\_modified\_abuse\_monitoring")

### Update organization data retention

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.dataretention.DataRetentionUpdateParams;
import com.openai.models.admin.organization.dataretention.OrganizationDataRetention;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        DataRetentionUpdateParams params = DataRetentionUpdateParams.builder()
            .retentionType(DataRetentionUpdateParams.RetentionType.ZERO_DATA_RETENTION)
            .build();
        OrganizationDataRetention organizationDataRetention = client.admin().organization().dataRetention().update(params);

    "object": "organization.data_retention",
    "type": "modified_abuse_monitoring"

##### Returns Examples

    "object": "organization.data_retention",
    "type": "modified_abuse_monitoring"

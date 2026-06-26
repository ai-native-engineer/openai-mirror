<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[Data Retention](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/data_retention)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update project data retention

[ProjectDataRetention](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)) admin().organization().projects().dataRetention().update(DataRetentionUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/data\_retention

Updates project data retention controls.

##### ParametersExpand Collapse

DataRetentionUpdateParams params

Optional<String> projectId

RetentionType retentionType

The desired project data retention type.

ORGANIZATION\_DEFAULT("organization\_default")

NONE("none")

ZERO\_DATA\_RETENTION("zero\_data\_retention")

MODIFIED\_ABUSE\_MONITORING("modified\_abuse\_monitoring")

ENHANCED\_ZERO\_DATA\_RETENTION("enhanced\_zero\_data\_retention")

ENHANCED\_MODIFIED\_ABUSE\_MONITORING("enhanced\_modified\_abuse\_monitoring")

##### ReturnsExpand Collapse

class ProjectDataRetention:

Represents a project’s data retention control setting.

JsonValue; object\_ "project.data\_retention"constant"project.data\_retention"constant

The object type, which is always `project.data_retention`.

Type type

The configured project data retention type.

One of the following:

ORGANIZATION\_DEFAULT("organization\_default")

NONE("none")

ZERO\_DATA\_RETENTION("zero\_data\_retention")

MODIFIED\_ABUSE\_MONITORING("modified\_abuse\_monitoring")

ENHANCED\_ZERO\_DATA\_RETENTION("enhanced\_zero\_data\_retention")

ENHANCED\_MODIFIED\_ABUSE\_MONITORING("enhanced\_modified\_abuse\_monitoring")

### Update project data retention

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
import com.openai.models.admin.organization.projects.dataretention.DataRetentionUpdateParams;
import com.openai.models.admin.organization.projects.dataretention.ProjectDataRetention;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        DataRetentionUpdateParams params = DataRetentionUpdateParams.builder()
            .projectId("project_id")
            .retentionType(DataRetentionUpdateParams.RetentionType.ORGANIZATION_DEFAULT)
            .build();
        ProjectDataRetention projectDataRetention = client.admin().organization().projects().dataRetention().update(params);

    "object": "project.data_retention",
    "type": "modified_abuse_monitoring"

##### Returns Examples

    "object": "project.data_retention",
    "type": "modified_abuse_monitoring"

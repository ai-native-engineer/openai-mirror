<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project

[Project](/api/reference/java/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) admin().organization().projects().retrieve(ProjectRetrieveParamsparams = ProjectRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}

Retrieves a project.

##### ParametersExpand Collapse

ProjectRetrieveParams params

Optional<String> projectId

##### ReturnsExpand Collapse

class Project:

Represents an individual project.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the project was created.

formatunixtime

JsonValue; object\_ "organization.project"constant"organization.project"constant

The object type, which is always `organization.project`

Optional<Long> archivedAt

The Unix timestamp (in seconds) of when the project was archived or `null`.

formatunixtime

Optional<String> externalKeyId

The external key associated with the project.

Optional<String> name

The name of the project. This appears in reporting.

Optional<String> status

`active` or `archived`

### Retrieve project

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
import com.openai.models.admin.organization.projects.Project;
import com.openai.models.admin.organization.projects.ProjectRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Project project = client.admin().organization().projects().retrieve("project_id");

    "id": "proj_abc",
    "object": "organization.project",
    "name": "Project example",
    "created_at": 1711471533,
    "archived_at": null,
    "status": "active"

##### Returns Examples

    "id": "proj_abc",
    "object": "organization.project",
    "name": "Project example",
    "created_at": 1711471533,
    "archived_at": null,
    "status": "active"

<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/methods/update/ -->

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

# Modify project

[Project](/api/reference/java/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) admin().organization().projects().update(ProjectUpdateParamsparams = ProjectUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}

Modifies a project in the organization.

##### ParametersExpand Collapse

ProjectUpdateParams params

Optional<String> projectId

Optional<String> externalKeyId

External key ID to associate with the project.

Optional<String> geography

Geography for the project.

Optional<String> name

The updated name of the project, this name appears in reports.

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

### Modify project

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
import com.openai.models.admin.organization.projects.ProjectUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Project project = client.admin().organization().projects().update("project_id");

200 example

  "id": "id",
  "created_at": 0,
  "object": "organization.project",
  "archived_at": 0,
  "external_key_id": "external_key_id",
  "name": "name",
  "status": "status"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "object": "organization.project",
  "archived_at": 0,
  "external_key_id": "external_key_id",
  "name": "name",
  "status": "status"

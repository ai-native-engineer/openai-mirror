<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/methods/list/ -->

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

# List projects

ProjectListPage admin().organization().projects().list(ProjectListParamsparams = ProjectListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects

Returns a list of projects.

##### ParametersExpand Collapse

ProjectListParams params

Optional<String> after

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Optional<Boolean> includeArchived

If `true` returns all projects including those that have been `archived`. Archived projects are not included by default.

Optional<Long> limit

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

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

### List projects

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
import com.openai.models.admin.organization.projects.ProjectListPage;
import com.openai.models.admin.organization.projects.ProjectListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ProjectListPage page = client.admin().organization().projects().list();

    "object": "list",
    "data": [
            "id": "proj_abc",
            "object": "organization.project",
            "name": "Project example",
            "created_at": 1711471533,
            "archived_at": null,
            "status": "active"
    ],
    "first_id": "proj-abc",
    "last_id": "proj-xyz",
    "has_more": false

##### Returns Examples

    "object": "list",
    "data": [
            "id": "proj_abc",
            "object": "organization.project",
            "name": "Project example",
            "created_at": 1711471533,
            "archived_at": null,
            "status": "active"
    ],
    "first_id": "proj-abc",
    "last_id": "proj-xyz",
    "has_more": false

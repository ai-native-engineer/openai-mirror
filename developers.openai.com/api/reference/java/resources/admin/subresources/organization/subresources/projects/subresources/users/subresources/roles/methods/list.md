<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users)

[Roles](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List project user role assignments

RoleListPage admin().organization().projects().users().roles().list(RoleListParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/projects/{project\_id}/users/{user\_id}/roles

Lists the project roles assigned to a user within a project.

##### ParametersExpand Collapse

RoleListParams params

String projectId

Optional<String> userId

Optional<String> after

Cursor for pagination. Provide the value from the previous response’s `next` field to continue listing project roles.

Optional<Long> limit

A limit on the number of project role assignments to return.

minimum0

maximum1000

Optional<[Order](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/list#(resource)%20admin.organization.projects.users.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Sort order for the returned project roles.

ASC("asc")

DESC("desc")

##### ReturnsExpand Collapse

class RoleListResponse:

Detailed information about a role assignment entry returned when listing assignments.

String id

Identifier for the role.

Optional<List<AssignmentSource>> assignmentSources

Principals from which the role assignment is inherited, when available.

String principalId

String principalType

Optional<Long> createdAt

When the role was created.

formatunixtime

Optional<String> createdBy

Identifier of the actor who created the role.

Optional<CreatedByUserObj> createdByUserObj

User details for the actor that created the role, when available.

Optional<String> description

Description of the role.

Optional<Metadata> metadata

Arbitrary metadata stored on the role.

String name

Name of the role.

List<String> permissions

Permissions associated with the role.

boolean predefinedRole

Whether the role is predefined by OpenAI.

String resourceType

Resource type the role applies to.

Optional<Long> updatedAt

When the role was last updated.

formatunixtime

### List project user role assignments

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
import com.openai.models.admin.organization.projects.users.roles.RoleListPage;
import com.openai.models.admin.organization.projects.users.roles.RoleListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RoleListParams params = RoleListParams.builder()
            .projectId("project_id")
            .userId("user_id")
            .build();
        RoleListPage page = client.admin().organization().projects().users().roles().list(params);

    "object": "list",
    "data": [
            "id": "role_01J1F8PROJ",
            "name": "API Project Key Manager",
            "permissions": [
                "api.organization.projects.api_keys.read",
                "api.organization.projects.api_keys.write"
            ],
            "resource_type": "api.project",
            "predefined_role": false,
            "description": "Allows managing API keys for the project",
            "created_at": 1711471533,
            "updated_at": 1711472599,
            "created_by": "user_abc123",
            "created_by_user_obj": {
                "id": "user_abc123",
                "name": "Ada Lovelace",
                "email": "ada@example.com"
            "metadata": {}
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
            "id": "role_01J1F8PROJ",
            "name": "API Project Key Manager",
            "permissions": [
                "api.organization.projects.api_keys.read",
                "api.organization.projects.api_keys.write"
            ],
            "resource_type": "api.project",
            "predefined_role": false,
            "description": "Allows managing API keys for the project",
            "created_at": 1711471533,
            "updated_at": 1711472599,
            "created_by": "user_abc123",
            "created_by_user_obj": {
                "id": "user_abc123",
                "name": "Ada Lovelace",
                "email": "ada@example.com"
            "metadata": {}
    ],
    "has_more": false,
    "next": null

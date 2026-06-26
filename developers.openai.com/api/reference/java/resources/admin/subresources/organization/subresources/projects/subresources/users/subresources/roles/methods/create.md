<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/create/ -->

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

# Assign project role to user

[RoleCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20RoleCreateResponse%20%3E%20(schema)) admin().organization().projects().users().roles().create(RoleCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/projects/{project\_id}/users/{user\_id}/roles

Assigns a project role to a user within a project.

##### ParametersExpand Collapse

RoleCreateParams params

String projectId

Optional<String> userId

String roleId

Identifier of the role to assign.

##### ReturnsExpand Collapse

class RoleCreateResponse:

Role assignment linking a user to a role.

JsonValue; object\_ "user.role"constant"user.role"constant

Always `user.role`.

[Role](/api/reference/java/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) role

Details about a role that can be assigned through the public Roles API.

String id

Identifier for the role.

Optional<String> description

Optional description of the role.

String name

Unique name for the role.

JsonValue; object\_ "role"constant"role"constant

Always `role`.

List<String> permissions

Permissions granted by the role.

boolean predefinedRole

Whether the role is predefined and managed by OpenAI.

String resourceType

Resource type the role is bound to (for example `api.organization` or `api.project`).

[OrganizationUser](/api/reference/java/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) user

Represents an individual `user` within an organization.

String id

The identifier, which can be referenced in API endpoints

long addedAt

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

JsonValue; object\_ "organization.user"constant"organization.user"constant

The object type, which is always `organization.user`

Optional<Long> apiKeyLastUsedAt

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

Optional<Long> created

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

Optional<String> developerPersona

The developer persona metadata for the user.

Optional<String> email

The email address of the user

Optional<Boolean> isDefault

Whether this is the organization’s default user.

Optional<Boolean> isScaleTierAuthorizedPurchaser

Whether the user is an authorized purchaser for Scale Tier.

Optional<Boolean> isScimManaged

Whether the user is managed through SCIM.

Optional<Boolean> isServiceAccount

Whether the user is a service account.

Optional<String> name

The name of the user

Optional<Projects> projects

Projects associated with the user, if included.

List<Data> data

Optional<String> id

Optional<String> name

Optional<String> role

JsonValue; object\_ "list"constant"list"constant

Optional<String> role

`owner` or `reader`

Optional<String> technicalLevel

The technical level metadata for the user.

Optional<User> user

Nested user details.

String id

JsonValue; object\_ "user"constant"user"constant

Optional<Boolean> banned

Optional<Long> bannedAt

formatunixtime

Optional<String> email

Optional<Boolean> enabled

Optional<String> name

Optional<String> picture

### Assign project role to user

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
import com.openai.models.admin.organization.projects.users.roles.RoleCreateParams;
import com.openai.models.admin.organization.projects.users.roles.RoleCreateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RoleCreateParams params = RoleCreateParams.builder()
            .projectId("project_id")
            .userId("user_id")
            .roleId("role_id")
            .build();
        RoleCreateResponse role = client.admin().organization().projects().users().roles().create(params);

    "object": "user.role",
    "user": {
        "object": "organization.user",
        "id": "user_abc123",
        "name": "Ada Lovelace",
        "email": "ada@example.com",
        "role": "owner",
        "added_at": 1711470000
    "role": {
        "object": "role",
        "id": "role_01J1F8PROJ",
        "name": "API Project Key Manager",
        "description": "Allows managing API keys for the project",
        "permissions": [
            "api.organization.projects.api_keys.read",
            "api.organization.projects.api_keys.write"
        ],
        "resource_type": "api.project",
        "predefined_role": false

##### Returns Examples

    "object": "user.role",
    "user": {
        "object": "organization.user",
        "id": "user_abc123",
        "name": "Ada Lovelace",
        "email": "ada@example.com",
        "role": "owner",
        "added_at": 1711470000
    "role": {
        "object": "role",
        "id": "role_01J1F8PROJ",
        "name": "API Project Key Manager",
        "description": "Allows managing API keys for the project",
        "permissions": [
            "api.organization.projects.api_keys.read",
            "api.organization.projects.api_keys.write"
        ],
        "resource_type": "api.project",
        "predefined_role": false

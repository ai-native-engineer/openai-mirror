<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Users](/api/reference/java/resources/admin/subresources/organization/subresources/users)

[Roles](/api/reference/java/resources/admin/subresources/organization/subresources/users/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve user organization role

[RoleRetrieveResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20RoleRetrieveResponse%20%3E%20(schema)) admin().organization().users().roles().retrieve(RoleRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/users/{user\_id}/roles/{role\_id}

Retrieves an organization role assigned to a user.

##### ParametersExpand Collapse

RoleRetrieveParams params

String userId

Optional<String> roleId

##### ReturnsExpand Collapse

class RoleRetrieveResponse:

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

### Retrieve user organization role

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
import com.openai.models.admin.organization.users.roles.RoleRetrieveParams;
import com.openai.models.admin.organization.users.roles.RoleRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RoleRetrieveParams params = RoleRetrieveParams.builder()
            .userId("user_id")
            .roleId("role_id")
            .build();
        RoleRetrieveResponse role = client.admin().organization().users().roles().retrieve(params);

    "id": "role_01J1F8ROLE01",
    "name": "API Group Manager",
    "permissions": [
        "api.groups.read",
        "api.groups.write"
    ],
    "resource_type": "api.organization",
    "predefined_role": false,
    "description": "Allows managing organization groups",
    "created_at": 1711471533,
    "updated_at": 1711472599,
    "created_by": "user_abc123",
    "created_by_user_obj": null,
    "metadata": {},
    "assignment_sources": null

##### Returns Examples

    "id": "role_01J1F8ROLE01",
    "name": "API Group Manager",
    "permissions": [
        "api.groups.read",
        "api.groups.write"
    ],
    "resource_type": "api.organization",
    "predefined_role": false,
    "description": "Allows managing organization groups",
    "created_at": 1711471533,
    "updated_at": 1711472599,
    "created_by": "user_abc123",
    "created_by_user_obj": null,
    "metadata": {},
    "assignment_sources": null

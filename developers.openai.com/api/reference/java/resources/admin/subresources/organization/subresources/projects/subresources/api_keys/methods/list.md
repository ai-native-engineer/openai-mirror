<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[API Keys](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List project API keys

ApiKeyListPage admin().organization().projects().apiKeys().list(ApiKeyListParamsparams = ApiKeyListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/api\_keys

Returns a list of API keys in the project.

##### ParametersExpand Collapse

ApiKeyListParams params

Optional<String> projectId

Optional<String> after

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Optional<Long> limit

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

##### ReturnsExpand Collapse

class ProjectApiKey:

Represents an individual API key in a project.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

Optional<Long> lastUsedAt

The Unix timestamp (in seconds) of when the API key was last used.

formatunixtime

String name

The name of the API key

JsonValue; object\_ "organization.project.api\_key"constant"organization.project.api\_key"constant

The object type, which is always `organization.project.api_key`

Owner owner

Optional<ServiceAccount> serviceAccount

The service account that owns a project API key.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the service account was created.

formatunixtime

String name

The name of the service account.

String role

The service account’s project role.

Optional<Type> type

`user` or `service_account`

One of the following:

USER("user")

SERVICE\_ACCOUNT("service\_account")

Optional<User> user

The user that owns a project API key.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

String email

The email address of the user.

String name

The name of the user.

String role

The user’s project role.

String redactedValue

The redacted value of the API key

### List project API keys

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
import com.openai.models.admin.organization.projects.apikeys.ApiKeyListPage;
import com.openai.models.admin.organization.projects.apikeys.ApiKeyListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ApiKeyListPage page = client.admin().organization().projects().apiKeys().list("project_id");

    "object": "list",
    "data": [
            "object": "organization.project.api_key",
            "redacted_value": "sk-abc...def",
            "name": "My API Key",
            "created_at": 1711471533,
            "last_used_at": 1711471534,
            "id": "key_abc",
            "owner": {
                "type": "user",
                "user": {
                    "id": "user_abc",
                    "name": "First Last",
                    "email": "user@example.com",
                    "role": "owner",
                    "created_at": 1711471533
    ],
    "first_id": "key_abc",
    "last_id": "key_xyz",
    "has_more": false

##### Returns Examples

    "object": "list",
    "data": [
            "object": "organization.project.api_key",
            "redacted_value": "sk-abc...def",
            "name": "My API Key",
            "created_at": 1711471533,
            "last_used_at": 1711471534,
            "id": "key_abc",
            "owner": {
                "type": "user",
                "user": {
                    "id": "user_abc",
                    "name": "First Last",
                    "email": "user@example.com",
                    "role": "owner",
                    "created_at": 1711471533
    ],
    "first_id": "key_abc",
    "last_id": "key_xyz",
    "has_more": false

<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/users/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Users](/api/reference/java/resources/admin/subresources/organization/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List users

UserListPage admin().organization().users().list(UserListParamsparams = UserListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/users

Lists all of the users in the organization.

##### ParametersExpand Collapse

UserListParams params

Optional<String> after

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Optional<List<String>> emails

Filter by the email address of users.

Optional<Long> limit

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

##### ReturnsExpand Collapse

class OrganizationUser:

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

### List users

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
import com.openai.models.admin.organization.users.UserListPage;
import com.openai.models.admin.organization.users.UserListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        UserListPage page = client.admin().organization().users().list();

    "object": "list",
    "data": [
            "object": "organization.user",
            "id": "user_abc",
            "name": "First Last",
            "email": "user@example.com",
            "role": "owner",
            "added_at": 1711471533
    ],
    "first_id": "user-abc",
    "last_id": "user-xyz",
    "has_more": false

##### Returns Examples

    "object": "list",
    "data": [
            "object": "organization.user",
            "id": "user_abc",
            "name": "First Last",
            "email": "user@example.com",
            "role": "owner",
            "added_at": 1711471533
    ],
    "first_id": "user-abc",
    "last_id": "user-xyz",
    "has_more": false

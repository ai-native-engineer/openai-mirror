<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/invites/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Invites](/api/reference/java/resources/admin/subresources/organization/subresources/invites)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List invites

InviteListPage admin().organization().invites().list(InviteListParamsparams = InviteListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/invites

Returns a list of invites in the organization.

##### ParametersExpand Collapse

InviteListParams params

Optional<String> after

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Optional<Long> limit

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

##### ReturnsExpand Collapse

class Invite:

Represents an individual `invite` to the organization.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the invite was sent.

formatunixtime

String email

The email address of the individual to whom the invite was sent

JsonValue; object\_ "organization.invite"constant"organization.invite"constant

The object type, which is always `organization.invite`

List<Project> projects

The projects that were granted membership upon acceptance of the invite.

String id

Project’s public ID

Role role

Project membership role

One of the following:

MEMBER("member")

OWNER("owner")

Role role

`owner` or `reader`

One of the following:

OWNER("owner")

READER("reader")

Status status

`accepted`,`expired`, or `pending`

One of the following:

ACCEPTED("accepted")

EXPIRED("expired")

PENDING("pending")

Optional<Long> acceptedAt

The Unix timestamp (in seconds) of when the invite was accepted.

formatunixtime

Optional<Long> expiresAt

The Unix timestamp (in seconds) of when the invite expires.

formatunixtime

### List invites

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
import com.openai.models.admin.organization.invites.InviteListPage;
import com.openai.models.admin.organization.invites.InviteListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        InviteListPage page = client.admin().organization().invites().list();

  "object": "list",
  "data": [
      "object": "organization.invite",
      "id": "invite-abc",
      "email": "user@example.com",
      "role": "owner",
      "status": "accepted",
      "created_at": 1711471533,
      "expires_at": 1711471533,
      "accepted_at": 1711471533
  ],
  "first_id": "invite-abc",
  "last_id": "invite-abc",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "object": "organization.invite",
      "id": "invite-abc",
      "email": "user@example.com",
      "role": "owner",
      "status": "accepted",
      "created_at": 1711471533,
      "expires_at": 1711471533,
      "accepted_at": 1711471533
  ],
  "first_id": "invite-abc",
  "last_id": "invite-abc",
  "has_more": false

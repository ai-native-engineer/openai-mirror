<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/invites/methods/create/ -->

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

# Create invite

[Invite](/api/reference/java/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) admin().organization().invites().create(InviteCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/invites

Create an invite for a user to the organization. The invite must be accepted by the user before they have access to the organization.

##### ParametersExpand Collapse

InviteCreateParams params

String email

Send an email to this address

Role role

`owner` or `reader`

READER("reader")

OWNER("owner")

Optional<List<Project>> projects

An array of projects to which membership is granted at the same time the org invite is accepted. If omitted, the user will be invited to the default project for compatibility with legacy behavior. If empty list is passed, the user will not be invited to any projects, including the default one.

String id

Project’s public ID

Role role

Project membership role

One of the following:

MEMBER("member")

OWNER("owner")

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

### Create invite

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
import com.openai.models.admin.organization.invites.Invite;
import com.openai.models.admin.organization.invites.InviteCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        InviteCreateParams params = InviteCreateParams.builder()
            .email("email")
            .role(InviteCreateParams.Role.READER)
            .build();
        Invite invite = client.admin().organization().invites().create(params);

  "object": "organization.invite",
  "id": "invite-def",
  "email": "anotheruser@example.com",
  "role": "reader",
  "status": "pending",
  "created_at": 1711471533,
  "expires_at": 1711471533,
  "accepted_at": null,
  "projects": [
      "id": "project-xyz",
      "role": "member"
      "id": "project-abc",
      "role": "owner"
  ]

##### Returns Examples

  "object": "organization.invite",
  "id": "invite-def",
  "email": "anotheruser@example.com",
  "role": "reader",
  "status": "pending",
  "created_at": 1711471533,
  "expires_at": 1711471533,
  "accepted_at": null,
  "projects": [
      "id": "project-xyz",
      "role": "member"
      "id": "project-abc",
      "role": "owner"
  ]

<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/invites/methods/retrieve/ -->

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

# Retrieve invite

[Invite](/api/reference/java/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) admin().organization().invites().retrieve(InviteRetrieveParamsparams = InviteRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/invites/{invite\_id}

Retrieves an invite.

##### ParametersExpand Collapse

InviteRetrieveParams params

Optional<String> inviteId

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

### Retrieve invite

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
import com.openai.models.admin.organization.invites.InviteRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Invite invite = client.admin().organization().invites().retrieve("invite_id");

    "object": "organization.invite",
    "id": "invite-abc",
    "email": "user@example.com",
    "role": "owner",
    "status": "accepted",
    "created_at": 1711471533,
    "expires_at": 1711471533,
    "accepted_at": 1711471533

##### Returns Examples

    "object": "organization.invite",
    "id": "invite-abc",
    "email": "user@example.com",
    "role": "owner",
    "status": "accepted",
    "created_at": 1711471533,
    "expires_at": 1711471533,
    "accepted_at": 1711471533

<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/invites/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Invites

##### [List invites](/api/reference/java/resources/admin/subresources/organization/subresources/invites/methods/list)

InviteListPage admin().organization().invites().list(InviteListParamsparams = InviteListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/invites

##### [Create invite](/api/reference/java/resources/admin/subresources/organization/subresources/invites/methods/create)

[Invite](/api/reference/java/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) admin().organization().invites().create(InviteCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/invites

##### [Retrieve invite](/api/reference/java/resources/admin/subresources/organization/subresources/invites/methods/retrieve)

[Invite](/api/reference/java/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) admin().organization().invites().retrieve(InviteRetrieveParamsparams = InviteRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/invites/{invite\_id}

##### [Delete invite](/api/reference/java/resources/admin/subresources/organization/subresources/invites/methods/delete)

[InviteDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20InviteDeleteResponse%20%3E%20(schema)) admin().organization().invites().delete(InviteDeleteParamsparams = InviteDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/invites/{invite\_id}

##### ModelsExpand Collapse

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

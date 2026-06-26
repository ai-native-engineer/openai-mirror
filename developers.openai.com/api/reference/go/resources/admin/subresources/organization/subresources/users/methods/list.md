<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/users/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Users](/api/reference/go/resources/admin/subresources/organization/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List users

client.Admin.Organization.Users.List(ctx, query) (\*ConversationCursorPage[[OrganizationUser](/api/reference/go/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema))], error)

GET/organization/users

Lists all of the users in the organization.

##### ParametersExpand Collapse

query AdminOrganizationUserListParams

After param.Field[string]Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Emails param.Field[[]string]Optional

Filter by the email address of users.

Limit param.Field[int64]Optional

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

##### ReturnsExpand Collapse

type OrganizationUser struct{…}

Represents an individual `user` within an organization.

ID string

The identifier, which can be referenced in API endpoints

AddedAt int64

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

Object OrganizationUser

The object type, which is always `organization.user`

APIKeyLastUsedAt int64Optional

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

Created int64Optional

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

DeveloperPersona stringOptional

The developer persona metadata for the user.

Email stringOptional

The email address of the user

IsDefault boolOptional

Whether this is the organization’s default user.

IsScaleTierAuthorizedPurchaser boolOptional

Whether the user is an authorized purchaser for Scale Tier.

IsScimManaged boolOptional

Whether the user is managed through SCIM.

IsServiceAccount boolOptional

Whether the user is a service account.

Name stringOptional

The name of the user

Projects OrganizationUserProjectsOptional

Projects associated with the user, if included.

Data []OrganizationUserProjectsData

ID stringOptional

Name stringOptional

Role stringOptional

Object List

Role stringOptional

`owner` or `reader`

TechnicalLevel stringOptional

The technical level metadata for the user.

User OrganizationUserUserOptional

Nested user details.

ID string

Object User

Banned boolOptional

BannedAt int64Optional

formatunixtime

Email stringOptional

Enabled boolOptional

Name stringOptional

Picture stringOptional

### List users

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  page, err := client.Admin.Organization.Users.List(context.TODO(), openai.AdminOrganizationUserListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

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

<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/spend_limit/methods/delete/ -->

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Spend Limit](/api/reference/java/resources/admin/subresources/organization/subresources/spend_limit)

# Delete organization spend limit

[OrganizationSpendLimitDeleted](/api/reference/java/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit_deleted%20%3E%20(schema)) admin().organization().spendLimit().delete(SpendLimitDeleteParamsparams = SpendLimitDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/spend\_limit

Delete the organization’s hard spend limit.

##### ParametersExpand Collapse

SpendLimitDeleteParams params

class OrganizationSpendLimitDeleted:

Confirmation payload returned after deleting an organization hard spend limit.

boolean deleted

Whether the hard spend limit was deleted.

JsonValue; object\_ "organization.spend\_limit.deleted"constant"organization.spend\_limit.deleted"constant

The object type, which is always `organization.spend_limit.deleted`.

### Delete organization spend limit

Java

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.spendlimit.OrganizationSpendLimitDeleted;
import com.openai.models.admin.organization.spendlimit.SpendLimitDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        OrganizationSpendLimitDeleted organizationSpendLimitDeleted = client.admin().organization().spendLimit().delete();

    "object": "organization.spend_limit.deleted",
    "deleted": true

    "object": "organization.spend_limit.deleted",
    "deleted": true

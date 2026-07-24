<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/delete/ -->

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[Spend Limit](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit)

# Delete project spend limit

[ProjectSpendLimitDeleted](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit_deleted%20%3E%20(schema)) admin().organization().projects().spendLimit().delete(SpendLimitDeleteParamsparams = SpendLimitDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/spend\_limit

Delete a project’s hard spend limit.

##### ParametersExpand Collapse

SpendLimitDeleteParams params

Optional<String> projectId

class ProjectSpendLimitDeleted:

Confirmation payload returned after deleting a project hard spend limit.

boolean deleted

Whether the hard spend limit was deleted.

JsonValue; object\_ "project.spend\_limit.deleted"constant"project.spend\_limit.deleted"constant

The object type, which is always `project.spend_limit.deleted`.

### Delete project spend limit

Java

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.projects.spendlimit.ProjectSpendLimitDeleted;
import com.openai.models.admin.organization.projects.spendlimit.SpendLimitDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ProjectSpendLimitDeleted projectSpendLimitDeleted = client.admin().organization().projects().spendLimit().delete("proj_123");

    "object": "project.spend_limit.deleted",
    "deleted": true

    "object": "project.spend_limit.deleted",
    "deleted": true

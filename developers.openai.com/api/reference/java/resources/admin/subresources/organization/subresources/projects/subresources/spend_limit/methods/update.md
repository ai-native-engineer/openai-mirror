<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/update/ -->

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[Spend Limit](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit)

# Update project spend limit

[ProjectSpendLimit](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.spend_limit%20%3E%20(model)%20project_spend_limit%20%3E%20(schema)) admin().organization().projects().spendLimit().update(SpendLimitUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/spend\_limit

Create or replace a project’s hard spend limit.

##### ParametersExpand Collapse

SpendLimitUpdateParams params

Optional<String> projectId

Currency currency

USD("USD")

Interval interval

MONTH("month")

long thresholdAmount

minimum1

class ProjectSpendLimit:

Represents a hard spend limit configured at the project level.

Currency currency

USD("USD")

Enforcement enforcement

Status status

INACTIVE("inactive")

ENFORCING("enforcing")

Interval interval

MONTH("month")

JsonValue; object\_ "project.spend\_limit"constant"project.spend\_limit"constant

The object type, which is always `project.spend_limit`.

long thresholdAmount

### Update project spend limit

Java

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.projects.spendlimit.ProjectSpendLimit;
import com.openai.models.admin.organization.projects.spendlimit.SpendLimitUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SpendLimitUpdateParams params = SpendLimitUpdateParams.builder()
            .projectId("proj_123")
            .currency(SpendLimitUpdateParams.Currency.USD)
            .interval(SpendLimitUpdateParams.Interval.MONTH)
            .thresholdAmount(1L)
            .build();
        ProjectSpendLimit projectSpendLimit = client.admin().organization().projects().spendLimit().update(params);

    "object": "project.spend_limit",
    "threshold_amount": 10000,
    "currency": "USD",
    "interval": "month",
    "enforcement": {
        "status": "enforcing"

    "object": "project.spend_limit",
    "threshold_amount": 10000,
    "currency": "USD",
    "interval": "month",
    "enforcement": {
        "status": "enforcing"

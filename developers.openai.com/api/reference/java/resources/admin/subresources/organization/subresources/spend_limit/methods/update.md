<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/spend_limit/methods/update/ -->

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Spend Limit](/api/reference/java/resources/admin/subresources/organization/subresources/spend_limit)

# Update organization spend limit

[OrganizationSpendLimit](/api/reference/java/resources/admin#(resource)%20admin.organization.spend_limit%20%3E%20(model)%20organization_spend_limit%20%3E%20(schema)) admin().organization().spendLimit().update(SpendLimitUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/spend\_limit

Create or replace the organization’s hard spend limit.

##### ParametersExpand Collapse

SpendLimitUpdateParams params

Currency currency

USD("USD")

Interval interval

MONTH("month")

long thresholdAmount

minimum1

class OrganizationSpendLimit:

Represents a hard spend limit configured at the organization level.

Currency currency

USD("USD")

Enforcement enforcement

Status status

INACTIVE("inactive")

ENFORCING("enforcing")

Interval interval

MONTH("month")

JsonValue; object\_ "organization.spend\_limit"constant"organization.spend\_limit"constant

The object type, which is always `organization.spend_limit`.

long thresholdAmount

### Update organization spend limit

Java

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.spendlimit.OrganizationSpendLimit;
import com.openai.models.admin.organization.spendlimit.SpendLimitUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SpendLimitUpdateParams params = SpendLimitUpdateParams.builder()
            .currency(SpendLimitUpdateParams.Currency.USD)
            .interval(SpendLimitUpdateParams.Interval.MONTH)
            .thresholdAmount(1L)
            .build();
        OrganizationSpendLimit organizationSpendLimit = client.admin().organization().spendLimit().update(params);

    "object": "organization.spend_limit",
    "threshold_amount": 10000,
    "currency": "USD",
    "interval": "month",
    "enforcement": {
        "status": "enforcing"

    "object": "organization.spend_limit",
    "threshold_amount": 10000,
    "currency": "USD",
    "interval": "month",
    "enforcement": {
        "status": "enforcing"

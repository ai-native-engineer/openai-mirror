<!-- source: https://help.openai.com/en/articles/10478918-reviewing-api-usage-and-costs -->

# Reviewing API usage and costs

Review API activity in the Usage Dashboard, check token counts in API responses, and understand project filters, exports, and Scale Tier costs.

Updated: 12 hours ago

You can review API usage in two ways:

* Use the [Usage Dashboard](https://platform.openai.com/usage) to review activity across current and past billing periods.
* Read the usage information in an API response to check an individual request.

Playground uses the same API calls as your applications. Its tokens count toward your account’s API usage and follow the same usage rules and pricing.

## Dashboard access

You must be an organization owner or have the **Usage Dashboard** permission to access the Usage Dashboard.

# Review usage in the dashboard

Open the [Usage Dashboard](https://platform.openai.com/usage), select the organization you want to review, and choose the relevant reporting period.

Dashboard data is displayed in UTC. Keep that time zone in mind when comparing dashboard activity with your application logs.

## Select projects

The dashboard has its own project selector. It works independently of the project selected elsewhere in the API Platform.

Use the dashboard’s selector to review one project, several projects, or all projects. To see overall organization data, clear the selected projects. With no projects selected, the dashboard shows all project data.

## Review an individual user’s usage

To review one user’s Responses and Chat Completions usage:

1. In the Usage Dashboard, go to **API capabilities > Responses and Chat Completions**.
2. Select **Filter by**.
3. Under **Users**, select the user, then select **Apply filters**.

## View tokens per minute

Usage detail pages support interval selection. Select a 1-minute interval to examine tokens per minute (TPM).

This interval applies to usage data, not billing data.

# Export usage data

There is no limit on the export date range. Exports covering a long period may be split into multiple files.

For monthly invoice reconciliation and line-item exports, see: [Exporting monthly usage details](https://help.openai.com/articles/20001072).

# View credit grants

Credit-grant details are available on your organization’s [Billing page](https://platform.openai.com/settings/organization/billing/credit-grants).

Credit grants and API usage answer different questions: credit grants show the credits associated with your organization, while usage shows its API activity.

# Review Scale Tier usage and costs

If your organization has Scale Tier enabled and you have the required access, open the [Scale Tier usage page](https://platform.openai.com/usage/scale-tier) for detailed usage.

Scale Tier bundle costs are attributed to the organization, not to individual projects.

## Usage is greater than zero, but project spend is zero

Check whether the model’s usage is covered by your Scale Tier allocation. If all usage for that model is within the Scale Tier TPM allocation, the project can show usage without additional model spend.

The Scale Tier subscription cost remains at the organization level. To review it:

1. Clear the project filter in the Usage Dashboard.
2. Select **Spend categories**.

# Review multiple organizations

The Usage Dashboard does not combine cost or usage data across organizations. Each organization, including a sub-organization, is treated separately.

To view a sub-organization, select it in the organization selector.

If you need combined reporting, consider using projects within one organization instead of separate sub-organizations, or use the [Usage API](https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/usage) for custom analysis.

# Check token usage in an API response

Token-usage field names depend on the endpoint.

|  |  |  |
| --- | --- | --- |
| **Token count** | **Chat Completions** | **Responses** |
| Input tokens | usage.prompt\_tokens | usage.input\_tokens |
| Output tokens | usage.completion\_tokens | usage.output\_tokens |
| Total tokens | usage.total\_tokens | usage.total\_tokens |

For example, a Chat Completions response can include:

|  |
| --- |
| { "usage": { "prompt\_tokens": 13, "completion\_tokens": 7, "total\_tokens": 20 }} |

Depending on the endpoint and model, usage details can also include cached-input and reasoning-token counts. These help explain why the visible length of a response does not show its full token usage.

For an explanation of the different token categories, see: [Understanding and counting tokens](https://help.openai.com/articles/4936856).

## Get usage from streamed Chat Completions

For a streaming Chat Completions request, include:

|  |
| --- |
| { "stream": true, "stream\_options": { "include\_usage": true }} |

With include\_usage enabled, an additional chunk before data: [DONE] contains the usage for the entire request. Its choices array is empty. Other chunks have a null usage value.

If the stream is interrupted, you may not receive that final usage chunk. A missing final chunk does not establish that the request used no tokens.

This configuration is specific to Chat Completions. For details, see the [Chat Completions API reference](https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create).

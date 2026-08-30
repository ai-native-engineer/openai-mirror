<!-- source: https://help.openai.com/en/articles/5955604-troubleshooting-api-rate-limits-and-429-errors -->

# Troubleshooting API rate limits and 429 errors

Identify the cause of an API 429 error, reduce request bursts, and choose the right next step for rate, credit, or usage limits.

Updated: 14 hours ago

API usage is subject to rate limits. These limits restrict requests, tokens, or other usage over a specified period.

A 429 response can indicate a temporary rate limit, an exhausted prepaid balance, or a spending or usage limit. Check the error details before retrying or changing your billing settings.

# Identify the cause

Read the error message and error.code, when provided. Billing-related errors can still use the broader error.type value insufficient\_quota.

|  |  |  |
| --- | --- | --- |
| **Error or code** | **What it means** | **What to do** |
| Rate limit reached for requests or tokens | Requests are exceeding an applicable rate limit. | Pace requests and follow the retry guidance below. |
| credit\_balance\_exhausted | The organization has no prepaid credits remaining. | Add credits in your API billing settings. |
| organization\_usage\_limit\_exceeded | The organization reached its OpenAI-assigned usage limit. | Request a higher approved usage limit. |
| organization\_spend\_limit\_exceeded | The organization reached its enforced spend limit. | Increase or remove the limit, or wait for the monthly reset. |
| project\_spend\_limit\_exceeded | The project reached its enforced spend limit. | Increase or remove the project limit, or wait for the monthly reset. |

Retrying a billing, spending, or quota error does not restore access. Address the reported balance or limit first. Changes to enforced spend limits can take time to apply.

Changing a spend limit requires permission to manage the relevant organization or project settings. If you don’t have access, ask the person who manages those settings.

For prepaid credit purchases, see: [Setting up and managing prepaid API billing](https://help.openai.com/articles/8264644).

For the different spending controls, see the [API spend-limit guide](https://developers.openai.com/api/docs/guides/spend-limits).

# Check the applicable rate limits

Go to your organization’s [**Limits** page](https://platform.openai.com/settings/organization/limits) to review its current usage tier and limits.

Rate limits can apply at the organization and project levels. They are not individual user allowances. Limits also vary by model, and some model families share a limit.

Check which limit the error identifies. For example, requests per minute and tokens per minute are separate limits. You can reach one while remaining below the other.

## Confirm the organization used by your request

If you belong to multiple organizations, confirm that your requests use the intended organization and project.

When your API key uses a default organization, check your [default organization setting](https://platform.openai.com/settings/profile/user). Different organizations can have different billing arrangements and usage tiers.

# Reduce temporary rate-limit errors

## Pace requests and avoid bursts

Spread requests over time instead of sending a large number at once.

Rate limits can be enforced over shorter periods than the displayed interval. For example, a limit of 60 requests per minute may also be enforced over 1-second periods. A short burst can therefore trigger an error even if your average usage appears below the per-minute limit.

Long prompts and unnecessarily large output-token allowances can also contribute to token-rate errors.

## Retry with a delay

For temporary rate-limit errors:

1. Check for a Retry-After response header.
2. If the header contains a valid delay, wait at least that long before retrying.
3. If the header is missing or invalid, use exponential backoff with jitter: increase the delay after each unsuccessful attempt and add a small random delay.
4. Limit both the number of retries and the total time spent retrying.

Official OpenAI SDKs already retry eligible rate-limit errors and honor Retry-After when it is present. Account for those retries before adding another retry loop.

Unsuccessful requests contribute to per-minute limits. Continuously resending the same request can prolong the problem.

For implementation guidance and examples, see the [API rate-limit guide](https://developers.openai.com/api/docs/guides/rate-limits). Review any third-party retry library before using it in your application.

## Review prompt and output size

Remove unnecessary instructions, repeated context, and examples from your prompts. Test the revised prompt to confirm that it still produces the result you need.

Use the output-token parameter supported by your endpoint and model:

* Chat Completions uses max\_completion\_tokens.
* Responses uses max\_output\_tokens.

Avoid setting a much larger allowance than the request needs. These parameters include reasoning tokens as well as visible output, so allow for both when using a reasoning model.

# Review your usage tier

If errors continue after you reduce bursts and review token usage, check your [**Limits** page](https://platform.openai.com/settings/organization/limits) for the available ways to increase your limits.

As API spending increases, OpenAI can automatically graduate an organization to a higher usage tier. This usually increases rate limits across most models.

Your approved monthly usage limit is separate from request and token rate limits. Increasing one should not be treated as confirmation that the other has changed.

# If the issue continues

## Before escalating

Keep the exact error message, any error code, relevant request IDs, the time of the error with your time zone, and the relevant limit shown in your account available. Note the steps you have already tried.

## Contact OpenAI Support

Contact OpenAI Support through the Help Center if you cannot resolve the issue after checking the reported limit. Do not include API keys or other authentication secrets.

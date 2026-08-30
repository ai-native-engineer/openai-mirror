<!-- source: https://help.openai.com/en/articles/6614457-troubleshooting-api-usage-and-spend-limits -->

# Troubleshooting API usage and spend limits

Identify the limit or credit balance affecting your API requests and find the right next step.

Updated: 2 hours ago

An API billing or quota error can mean that you’ve reached an approved usage limit, reached a configured spend limit, or used your prepaid credits. Check the error before changing your settings.

# Identify the error

Check error.code in the API response. A billing-related error may still use the broader error.type value insufficient\_quota.

|  |  |  |
| --- | --- | --- |
| **Error code** | **What it means** | **Next step** |
| organization\_usage\_limit\_exceeded | Your organization reached its OpenAI-assigned usage limit. | Review your approved limit and options for an increase. |
| organization\_spend\_limit\_exceeded | Your organization reached a configured hard spend limit. | Review the organization’s spend controls. |
| project\_spend\_limit\_exceeded | Your project reached a configured hard spend limit. | Review that project’s spend controls. |
| credit\_balance\_exhausted | Your organization has no prepaid credits remaining. | Add credits to your API balance. |

Retrying these errors won’t restore access without addressing the relevant credits or limits. For details, see the [API error codes guide](https://developers.openai.com/api/docs/guides/error-codes).

# Review your approved usage limit

Go to your organization’s [**Limits** page](https://platform.openai.com/account/limits) to check its current approved monthly usage limit and usage tier.

As your API spend increases, OpenAI automatically moves your organization to higher usage tiers. This usually increases rate limits across most models. Use the limits shown for your organization rather than assuming that every account has the same monthly allowance.

For tier details, see the [API rate limits guide](https://developers.openai.com/api/docs/guides/rate-limits).

# Check configured spend controls

Spend alerts send notifications without stopping API traffic. Hard spend limits can stop affected requests when tracked spend reaches the configured amount.

Both organization and project limits can apply. An organization limit covers its projects; a project limit covers traffic billed to that project. These controls are separate from your OpenAI-approved usage limit.

If a hard limit caused the error, someone with permission to manage the relevant settings can raise or remove it if spending should continue. Otherwise, it resets with the next monthly cycle. Changes and enforcement aren’t instantaneous, so recorded spend can slightly exceed the configured amount.

For settings and instructions, see the [API spend limits guide](https://developers.openai.com/api/docs/guides/spend-limits).

# Check your prepaid balance

If you’ve used your prepaid credits, go to the [API billing portal](https://platform.openai.com/account/billing) and select **Buy credits** or **Add to credit balance**, whichever appears, to purchase more. Your updated balance may take a few minutes to appear.

For setup and recharge guidance, see: [Setting up prepaid billing](https://help.openai.com/articles/8264644).

# Check whether the error is a rate limit

Request and token rate limits control how quickly you can use the API. They’re different from monthly usage limits, spend controls, and your prepaid balance.

For request or token rate-limit errors, see: [Troubleshooting API rate-limit errors](https://help.openai.com/articles/5955604).

# If the issue continues

## Before escalating

Have the error message and code, the time of the error with your time zone, and any relevant request IDs ready. Remove sensitive information from screenshots or code you share.

## Contact OpenAI Support

If your needs exceed the limits available to your organization, you have a unique use case, or the error continues after you address its cause, [contact OpenAI Support](/en/articles/6614161) using the chat widget in the Help Center.

For contact instructions and the information to include, see: [Contacting Support](https://help.openai.com/articles/6614161).

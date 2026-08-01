<!-- source: https://openai.com/index/disrupting-malicious-uses-of-ai-iuvm/ -->

May 1, 2024

# IUVM: Iran-linked influence content network

OpenAI banned accounts associated with the Iran-origin operation "IUVM", using AI to generate and translate pro-Iran, anti-Israel and anti-US website content.

*This case study was originally published in OpenAI’s* [*May 2024*⁠(opens in a new window)](https://cdn.openai.com/threat-intelligence-reports/threat-intel-report-may-2024.pdf) *report.*

We banned a small number of accounts linked to people associated with the [International Union of Virtual Media (IUVM)⁠(opens in a new window)](https://www.reuters.com/article/idUSKCN1LD2R7/), an Iranian entity that has been studied by the open-source community since 2018.

This campaign targeted global audiences and focused on content generation in English and French. It used our models to generate and proofread [article⁠(opens in a new window)](https://web.archive.org/web/20240428105313/https://iuvmpress.co/irans-missile-export-to-russia-understanding-irans-ballistic-diplomacy)s, headlines and website tags. This content was then published on IUVM’s current website, iuvmpress.co (earlier IUVM domains were [seized by the FBI in 2020⁠(opens in a new window)](https://home.treasury.gov/news/press-releases/sm1158)).

The articles were typically created the day before they were published; the website tags were created immediately before publication and were likely automated. On one occasion, we identified a set of website tags that included our model’s response message, suggestive of automation (or poor proofreading).

![Tags on an article published by iuvmpress.co. Note the first two tags, which include our model’s response.](https://images.ctfassets.net/kftzwdyauwt9/7mX9pFEgiV9UgQ2CnyS9Wz/06fb1525f10daba75071759a311d95a4/may-2024-international-union-of-virtual-media-iuvm-p29-fig1.png?w=3840&q=90&fm=webp)

*Tags on an article published by iuvmpress.co. Note the first two tags, which include our model’s response.*

## Content

The content that this network generated consisted of long-form articles, headlines and website tags. This content was typically anti-US and anti-Israel and praised the Palestinians, Iran, and the “Axis of Resistance”.

## Impact assessment

IUVM’s online presence has been reduced by repeated [social media takedowns⁠(opens in a new window)](https://medium.com/dfrlab/trolltracker-twitters-troll-farm-archives-17a6d5f13635) and the [FBI’s seizure of its domains⁠(opens in a new window)](https://home.treasury.gov/news/press-releases/sm1158). Beyond its website, as of May 23, 2024, we identified IUVM-branded accounts on TikTok, VKontakte and Odnoklassniki. These social media accounts had, respectively, 10, 76 and 274 followers or subscribers.

Using the [Breakout Scale⁠(opens in a new window)](https://www.brookings.edu/articles/the-breakout-scale-measuring-the-impact-of-influence-operations/) to assess the impact of IO, which rates them on a scale of 1 (lowest) to 6 (highest), we would assess this as a Category 2 operation, marked by posting activity on multiple platforms, but with no breakout or significant audience engagement in any of them.

## Indicators

We identified the following domains as being associated with this campaign.

* iuvmpress.co
* iuvmarchive.org

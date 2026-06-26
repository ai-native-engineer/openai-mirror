<!-- source: https://help.openai.com/en/articles/20001243-advertiser-guidance-for-allowing-openai-web-crawlers -->

# Advertiser Guidance for Allowing OpenAI Web Crawlers

Learn how to make your ad landing pages accessible to OpenAI and troubleshoot common access issues.

Updated: 2 days ago

## Why does OpenAI use web crawlers?

We use [crawlers](https://developers.openai.com/api/docs/bots) to validate the safety of web pages submitted as ads on ChatGPT. When you submit an ad, OpenAI may visit the landing page to ensure it complies with our policies. We may also use content from the landing page to determine when it's most relevant to show the ad to users.

## Which OpenAI crawlers should you allow?

You must allow OAI-AdsBot. We recommend allowing both OAI-AdsBot and OAI-SearchBot.

## OpenAI crawlers fail to crawl my website. What should I do?

Most websites have multiple layers of protection before a crawler can successfully access a webpage. Work with your engineering or security team to validate that OpenAI crawlers can pass through each of the following layers.

### 1. robots.txt

The robots.txt file tells crawlers whether they are permitted to access certain parts of your website. OpenAI crawlers respect these rules. If access is disallowed in robots.txt, crawling will stop immediately.

Review your robots.txt configuration and confirm that OpenAI crawlers are explicitly allowed to access the relevant pages and paths. For example: User-agent: OAI-SearchBot Allow: / User-agent: OAI-AdsBot Allow: /

### 2. Web protection and bot mitigation

Many websites use services such as Cloudflare, Akamai, or other web protection providers to defend against DDoS attacks, scraping, and unauthorized traffic. These systems can mistakenly block legitimate crawlers, often returning 403 Forbidden errors. Because OpenAI crawlers can resemble automated traffic patterns, they may be denied unless specifically allowlisted.

Review your web protection or firewall configuration and allowlist OpenAI crawler traffic where possible, ideally based on our crawler user agents. Your engineering or infrastructure team should also inspect any automated bot mitigation rules that could be triggering false positives.

### 3. Human verification and anti-bot logic

Some websites implement additional application-level checks to verify that a visitor is human, such as CAPTCHAs, JavaScript challenges, behavioral analysis, or session validation. Since OpenAI crawlers are automated systems, these checks may block access even if the crawler successfully passes earlier layers.

Review any human-verification or anti-automation logic implemented within your application and ensure OpenAI crawlers are exempted where appropriate, ideally by allowlisting our crawler user agents.

## A note on stable IP ranges

Some security systems require crawler traffic to originate from stable, publicly documented IP ranges before traffic can be reliably allowlisted. Because crawler infrastructure may evolve over time, your engineering team should avoid relying solely on short-term IP observations from logs. Instead, validate traffic through a combination of user-agent identification, verified bot programs where supported, firewall allowlists, robots.txt behavior, and provider-level bot verification systems.

If you must allow a stable list of IP ranges, reference <https://openai.com/searchbot.json> and <https://openai.com/adsbot.json>.

## A note on rate limiting

Large batch uploads or sudden spikes in crawler traffic can sometimes trigger automated rate limiting or bot protection systems.

If you suspect rate limiting is occurring, ask your engineering team to review HTTP response codes, especially 429 Too Many Requests, firewall or CDN logs, bot mitigation events, request throttling rules, and traffic analytics around the time the crawler attempted access. This can help identify whether requests are being intentionally slowed or blocked by infrastructure protections.

You may also consider uploading ads across more time in smaller batches.

## A note on Cloudflare

OAI-AdsBot is officially verified and allowlisted by Cloudflare.

## Crawler and landing page FAQ

### Which crawler is required for ads review?

OAI-AdsBot is required for ChatGPT Ads landing page validation and review. OAI-SearchBot is recommended because it may help OpenAI understand public web content, but OAI-AdsBot is the crawler advertisers should prioritize for ads readiness.

### Can support manually bypass crawler validation?

Do not rely on a manual bypass. Make the landing page crawlable for OAI-AdsBot by fixing robots.txt, WAF, CDN, bot mitigation, authentication, and rate-limiting blocks. Ads may need to be re-uploaded or resubmitted for review after the landing page becomes accessible.

### What should my engineering team check first?

Check whether the landing page returns a successful HTTP response to OAI-AdsBot, whether robots.txt allows the relevant path, and whether WAF, CDN, bot mitigation, JavaScript challenges, CAPTCHAs, authentication, or geo rules block automated access.

### Are app-store links, deep links, or non-web destinations supported as landing pages?

Use a directly reachable web landing page whenever possible. App-store links, deep links, documents, or destinations that require an app, login, region-specific access, or unsupported redirects may not provide enough crawlable content for validation or review.

### When should I re-upload or request review again?

After fixing crawler access, re-upload or resubmit affected ads if the status does not update on its own. For bulk-uploaded ads, smaller batches can reduce rate-limit or bot-protection triggers while your team validates the fix.

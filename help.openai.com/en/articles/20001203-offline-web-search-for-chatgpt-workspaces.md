<!-- source: https://help.openai.com/en/articles/20001203-offline-web-search-for-chatgpt-workspaces -->

# Offline web search for ChatGPT workspaces

Learn how offline web search uses OpenAI’s indexed and cached web content for eligible ChatGPT workspaces.

Updated: 2 days ago

# Overview

Offline web search is a web search configuration for eligible ChatGPT workspaces. It allows ChatGPT to use OpenAI’s indexed and cached web content instead of using live web search at the time of each request.  
  
Offline web search is intended for organizations with stricter governance, compliance, or data-handling requirements. It can help support workflows that need web search while limiting live external search provider use, depending on workspace configuration.

## Availability

Offline web search is available for eligible ChatGPT workspaces, including certain Enterprise, Edu, Healthcare, Teachers, regulated, and federal workspace configurations.  
  
Availability depends on your plan, contract, workspace configuration, and admin settings. Some regulated workspace configurations may have offline web search enabled by default. Other eligible workspaces may need OpenAI to configure it for the workspace or may use it as part of [Lockdown Mode](https://help.openai.com/articles/20001061).  
  
Offline web search applies to ChatGPT web search behavior. It does not describe API platform behavior.

# How it works

When offline web search is enabled, ChatGPT uses OpenAI’s indexed and cached web content for web search. This means ChatGPT can return information from pages that are already available in the OpenAI index or cache.  
  
Coverage and freshness can vary by site, page, language, region, and content type.  
  
If a page or URL is not available in the index or cache, ChatGPT will not not be able to retrieve it through offline web search. In those cases, users may need to provide the source material directly or use live web search if their workspace permits it.

# Decide whether offline web search fits your workflow

Offline web search is a better fit for stable web research than for workflows that require real-time freshness, guaranteed URL availability, or audit-grade evidence.  
  
Use this table to decide whether offline web search is appropriate for a workflow.

| Workflow need | What to expect with offline web search | Recommended path |
| --- | --- | --- |
| General research from public web pages | ChatGPT can use OpenAI’s indexed and cached web content when relevant content is available. | Use offline web search when exact real-time freshness is not required. |
| Use one specific URL as the source | ChatGPT can use the URL only if that page is available in the index or cache. If the page is unavailable, ChatGPT may fail to retrieve it or say it cannot access the page. | Upload the source material, paste the relevant text, provide another URL, or use live web search if your workspace permits it. |
| Confirm what a page said at a specific time | Offline web search results may not include the exact time when a page was indexed or cached. | Use an official source, uploaded file, archived record, or another approved source-of-record process. |
| Research the latest information | Results may be older than the live web version. Freshness varies by page and site. | Use live web search if permitted, or provide current source material directly. |
| Search long-tail or niche sites | Some pages may be missing, stale, or only partially represented. | Cross-check with additional sources, upload the material, or use live web search if permitted. |
| Analyze dynamic, personalized, or login-gated content | Content that depends on scripts, personalization, accounts, or frequent updates may be incomplete or unavailable. | Use stable documents, PDFs, exports, approved connectors, or uploaded files. |
| Review a page in detail | Offline web search may retrieve cached or indexed content, but deeper navigation can be limited to pages that are already indexed or cached. | Ask targeted follow-up questions, provide the relevant page content, or use live web search if permitted. |

# Setup requirements

Offline web search can be configured in different ways depending on your workspace.  
  
For some eligible workspaces, admins can make offline web search available by assigning members to a custom role with [Lockdown Mode](https://help.openai.com/articles/20001061) enabled. If offline web search is enabled through a Lockdown Mode role, other Lockdown Mode restrictions may also apply.  
  
For other eligible workspaces, offline web search may be applied as a workspace-level configuration by OpenAI. Some regulated workspace configurations may use offline web search by default.  
  
Before rolling out offline web search, admins should confirm:

* Whether offline web search is available for the workspace.
* Whether the configuration applies workspace-wide, by role, or both.
* Whether Lockdown Mode is required for the intended setup.
* Which related workspace features or role permissions may change.
* Which user groups should use offline web search.

If you do not see a relevant setting in your workspace, contact your OpenAI account team or OpenAI Support to confirm whether offline web search is available and how it can be configured.

# Enable offline web search

Eligible workspace admins may be able to enable offline web search in one of these ways:

* Assign members to a custom role with Lockdown Mode enabled.
* Have OpenAI configure web search restrictions for the workspace.
* Use a regulated workspace configuration where cached or indexed web access is enabled by default.

The available setup path depends on your workspace configuration and contract. Contact your OpenAI account representative for more information.

# Search coverage and freshness

Offline web search does not guarantee coverage of the entire public web. Pages may be missing, unavailable, incomplete, or older than the live version.  
  
OpenAI’s systems may update some indexed content quickly, but there is no refresh SLA for a specific URL. A particular page may be refreshed on a different schedule depending on the site, crawl access, caching, popularity, and other technical factors.  
  
Common reasons content may be missing or stale include:

* The site blocks crawling through robots.txt or similar controls.
* The site uses CDN or bot-blocking behavior.
* The page requires login or personalization.
* The content depends heavily on scripts or dynamic loading.
* The page is new, rarely accessed, or low-signal.
* The site structure makes deeper pages harder to discover.

# Specific URL behavior

If a user asks ChatGPT to use a specific URL, offline web search can use that URL only if the page is available in the index or cache.  
  
If the URL is not available, ChatGPT may fail to retrieve it or say it cannot access the page. Offline web search should not be treated as a guarantee that every public URL can be fetched.  
  
If a specific URL is important, use one of these alternatives:

* Provide another URL.
* Upload the source material directly.
* Paste the relevant text into ChatGPT.
* Use live web search if your workspace permits it.

# Source timestamps

Offline web search results may not include the exact time when a page was indexed or cached.  
  
Do not use offline web search when your workflow requires a guaranteed citation timestamp, audit-grade evidence of a page at a specific moment, or proof that a source was current at the time of response. For those workflows, use customer-provided materials, official documents, or another approved source-of-record process.

# Security

Offline web search is designed to support stricter web access controls. It limits web search to OpenAI’s indexed and cached web content instead of using live external web search at request time.  
  
This is designed to help organizations reduce the chance that web search queries are sent to a live external search provider at request time, depending on workspace configuration.  
  
Offline web search does not eliminate all risk. Indexed or cached web content can still contain inaccurate information, incomplete information, outdated information, or malicious instructions. Users should review cited sources and follow their organization’s data-handling policies.

# Relationship to Lockdown Mode and other features

Offline web search only describes how ChatGPT performs web search.  
  
Some workspaces use offline web search as part of a broader security configuration, such as [Lockdown Mode](https://help.openai.com/articles/20001061) or a regulated workspace setup. In those configurations, other features may also be limited or disabled. Those restrictions come from the broader security configuration, not from offline web search alone.  
  
If offline web search is enabled through a Lockdown Mode role, other Lockdown Mode restrictions may also apply.  
  
If offline web search is enabled without a broader security mode, most ChatGPT features should not change solely because search uses OpenAI's indexed and cached web content. However, any feature that depends only on live external web search may not work the same way in offline web search.  
  
Feature availability depends on your workspace settings, role permissions, and plan.

# FAQ

## How can I confirm offline web search is enabled?

There may not be a separate user-facing indicator labeled “offline web search.”  
  
When offline web search is enabled, users may notice that ChatGPT can still search the web, but results come from OpenAI’s indexed and cached web content instead of a live external search provider at request time.  
  
Users may also notice that:

* Some specific URLs cannot be retrieved.
* Some results are older than the live web version.
* ChatGPT may ask for the source material to be uploaded or pasted when a page is not available.

If you need to confirm the exact configuration for your workspace, contact your OpenAI account team or OpenAI Support.

## Does offline web search cover all public websites?

No. Offline web search is broad, but coverage is not guaranteed. Some pages may be unavailable because of crawl restrictions, site configuration, dynamic content, or indexing limitations.

## Does offline web search support all languages and regions?

Offline web search is not limited to a single language or region, but coverage and freshness can vary by site, region, language, and page.

## Is offline web search real time?

No. Offline web search uses indexed and cached content. Some content may be recent, but specific pages may be older than the live web version.

## Can ChatGPT show when a page was cached?

Not always. If your workflow requires a reliable timestamp, use uploaded source material, official documents, or another approved source-of-record process.

## Does offline web search replace live web search?

For eligible workspaces, offline web search can be used instead of live web search for workflows that do not require real-time freshness, guaranteed URL availability, or audit-grade evidence. It is not a full substitute for live web search.

## Does offline web search affect apps or connectors?

Offline web search does not automatically determine app or connector availability. Apps, connectors, and related actions are controlled by your workspace settings, role permissions, and security configuration.  
  
If offline web search is enabled as part of [Lockdown Mode](https://help.openai.com/articles/20001061) or a regulated workspace configuration, some apps or live capabilities may also be restricted.

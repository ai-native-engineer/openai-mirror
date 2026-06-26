<!-- source: https://help.openai.com/en/articles/11845367-chatgpt-agent-allowlisting -->

# ChatGPT agent allowlisting

Allow ChatGPT agent traffic to reach your site securely and reliably

Updated: 2 days ago

# Overview

ChatGPT agent signs every outbound HTTP request so you can confidently identify authentic traffic from ChatGPT. By allowlisting the agent in your CDN or firewall, you avoid false positives and ensure a smooth experience for your site visitors.

# How message signatures work

ChatGPT agent uses the HTTP Message Signatures standard ([RFC 9421](https://datatracker.ietf.org/doc/html/rfc9421)). Each request includes a `Signature` and `Signature-Input` set of headers and a companion Signature-Agent header set to `"https://chatgpt.com"`.

Additionally, we implement this [draft RFC](https://datatracker.ietf.org/doc/html/draft-meunier-web-bot-auth-architecture) to facilitate public key discoverability at this URL:

* <https://chatgpt.com/.well-known/http-message-signatures-directory>

Your edge service can retrieve the key, validate the signature, and confirm that the request is genuine.

# Allowlisting with Akamai

ChatGPT agent is categorized under the Artificial Intelligence (AI) bots category in the Akamai-validated bots list. To explicitly allow ChatGPT Agent:

1. In your Akamai Security Configuration, open the relevant Security Policy and select **Bot management**, then click **Custom Bot Categories**, and under settings, select **Manage Bot Categories**.
2. Add a new bot category and, within it, create a new bot, selecting Type: **Akamai-Defined** and Bot name: **ChatGPT Agent**.
3. Return to Custom Bot Categories and set the action of the new bot category to **Allow.**

***Note:*** *No custom signature verification is required. Akamai performs this verification for you.*

# Allowlisting with Cloudflare

ChatGPT agent is a **signed agent** in Cloudflare's Bots and Agents directory (tag `chatgpt-agent`, detection ID `129220581`).

1. In the Cloudflare dashboard, open **Security → WAF** and create a new custom rule.
2. Set expression to **Bot Detection ID equals** and search for "**ChatGPT Operator"** to find detection ID `129220581`
3. Save and deploy the rule.

***Note:*** *The rule should skip or allow requests when bot detection ID equals* `129220581`*. No custom signature verification is required if using this method—Cloudflare performs this validation for you. These steps alone are sufficient to allowlist ChatGPT agent traffic.*

# Allowlisting with HUMAN

## HUMAN Sightline

ChatGPT agent is a trusted AI Agent in HUMAN’s *Known Bots & Crawlers*. To allow it:

1. In your Sightline or BD console, go to **Policies → Traffic Policy Settings → Known bots & Crawlers**.
2. Search for **ChatGPT Agent**.
3. Change the rule to **ON** and set the rule response to **Allow**.

## HUMAN AgenticTrust

ChatGPT agent is a trusted AI Agent in HUMAN’s AgenticTrust. It is cryptographically verified, and its intent is monitored in every session. By default, it is permitted to read, log in, and make purchases. To modify this configuration:

1. In your Sightline console, open **Policies → AI Agents Permissions**.
2. Search for **ChatGPT Agent**.
3. Grant or revoke specific permissions as needed.

***Note:*** *No custom signature verification is required—HUMAN performs this verification for you.*

# Allowlisting with Vercel

If your site is hosted on Vercel, **no additional configuration is required** to allow ChatGPT Agent to access your content. Vercel has added ChatGPT Agent (via **chatgpt-operator**) to their [Verified Bot Directory](https://vercel.com/changelog/vercel-botid-now-leverages-vercels-verified-bot-directory), and their [Bot Verification](https://vercel.com/changelog/vercels-bot-verification-now-supports-web-bot-auth) system automatically permits our requests by default.

# Allowlisting with other CDNs

If you are not using any of the mentioned CDNs, you can still trust ChatGPT agent traffic by checking the request headers:

1. Verify the `Signature-Agent` header exactly matches `"https://chatgpt.com"`, *including* the quotation marks.
2. Fetch the public key associated with the signature from the [well-known endpoint](https://chatgpt.com/.well-known/http-message-signatures-directory).
3. Verify the authenticity of the `Signature` header as defined in RFC 9421.

# Troubleshooting tips

Confirm that the `Signature`, `Signature-Input`, and `Signature-Agent` headers are preserved by any intermediate proxies.

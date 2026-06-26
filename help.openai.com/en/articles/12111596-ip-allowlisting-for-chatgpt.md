<!-- source: https://help.openai.com/en/articles/12111596-ip-allowlisting-for-chatgpt -->

# IP allowlisting for ChatGPT

Ensure only traffic from trusted IPs can reach ChatGPT

Updated: 3 days ago

# Overview

IP Allowlisting is an optional security feature available for **ChatGPT Enterprise and Edu workspaces**. It is intended to help organizations protect their workspaces from unauthorized access.  
  
When IP Allowlisting is enabled, only requests originating from the IP addresses you specify will be allowed. Any request from an IP address **not** on the allowlist is automatically blocked—even if the user has valid credentials.  
  
This feature supports both **ChatGPT Workspaces** and the **Compliance API**, each with separate allowlists to restrict access to approved IPs only.  
  
---

# How to Configure IP Allowlisting

Only workspace owners and admin users will be able to adjust this setting.

1. Go to **Workspace Settings**
2. Navigate to the **Identity & access** tab
3. Select **Access Restrictions**
4. Add one or more IP addresses or IP ranges that should be allowed for either **Workspace** and/or the **Compliance API**.
5. Toggle **Activate IP Allowlist** to enable the feature.

* By default, the toggle is off.
* After enabling, allow 5–15 minutes for changes to take effect.

You can add or remove IPs at any time.

***Note:*** *Users will still be able to sign in and switch between workspaces. However, loading new data will only succeed if the request originates from an allowed IP.*

---

# FAQ

## What happens if we accidentally block ourselves?

Workspace owners and admins can disable the allowlist from **Workspace Settings**. If another user is able to log in from one of the allowed IPs, they can disable allowlisting. Once disabled, all IP restrictions are lifted (changes take 5–15 minutes).  
  
If no users are able to access the workspace, please [contact our support team](/en/articles/6614161-how-can-i-contact-support).

## Does IP Allowlisting apply to all ChatGPT features?

Yes. IP Allowlisting applies across all major ChatGPT endpoints and features, including authenticated file downloads.

## Does this include Compliance API keys?

Yes. Compliance API traffic is also subject to IP Allowlisting. For Compliance API keys, IP Allowlisting is always enforced and cannot be turned off.

## Are internal OpenAI services or system integrations affected?

No. IP Allowlisting applies only to user traffic into ChatGPT, not to OpenAI’s internal systems.

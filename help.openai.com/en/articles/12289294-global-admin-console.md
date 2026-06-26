<!-- source: https://help.openai.com/en/articles/12289294-global-admin-console -->

# Global Admin Console

This document provides an introductory walkthrough of the upcoming Global Admin Console and its features.

Updated: 2 days ago

# Overview

The [global admin console](http://admin.openai.com/) provides a single surface for ChatGPT Business and Enterprise/Edu plans to administer and operationalize OpenAI products - including identity and access, analytics, agents, and governance. It introduces a new level of hierarchy in the organizational structure: **the Tenant**. A single Tenant can contain support the following:

1. One or multiple ChatGPT workspaces
2. One or multiple API Platform organizations
3. Multiple verified domains
4. A single SSO connection
5. One or multiple Tenant Admins

The Global Admin Console also introduces a new, global role: **Global admins.** Global admins are different from Workspace admins and owners. This role is assigned when the first workspace is generated. Global admins are able to:

* Manage (add/remove/verify) domains
* Set up SSO across their ChatGPT workspaces, API Platform organizations, and the Global Admin Console itself
* Add or remove additional users as Global Admins
* Change the name of their Tenant
* This will impact the connection name that their users will see when logging in with SSO

Workspace users may also have access to the global admin console, depending on their role.

|  |  |
| --- | --- |
| **Role** | **Access type** |
| Workspace admins/owners | View, edit & export access (where applicable) limited to the workspace that you are an admin or owner of. |
| Analytics viewers\* | View and export access to the Analytics section for the workspace you are a member of. |
| Members | No access |

\*The analytics viewer role is only available to ChatGPT Enterprise/Edu accounts. Read more about roles in [ChatGPT Enterprise](https://help.openai.com/articles/8266401) and [ChatGPT Business](/en/articles/8542216).

# Navigating the Global Admin Console

In the following sections, we will walk through each of the pages currently available in the Global Admin Console.

## Overview

The **Overview** tab provides a high-level view of the current components of your Tenant. It allows you to see which workspaces and organizations are currently a part of the Tenant and navigate to the additional Tenant settings.

## Access

The **Access** tab is your centralized hub for SSO, domain, and external application access management. The Global Admin Console also includes **External Access** controls for managing whether members can use Sign in with ChatGPT for approved external applications.

### External Access

The [**External Access**](https://admin.openai.com/apps) section lets admins manage whether members can use Sign in with ChatGPT to access external applications, including OpenAI Academy.  
  
Admins can use these controls to:

* Turn **Enable Sign in with ChatGPT for your organization** on or off.
* Turn on **Approved applications** to choose which applications members can access with Sign in with ChatGPT.
* Approve or disable individual applications from the **Approved applications** list.

If **Enable Sign in with ChatGPT for your organization** is off, members cannot use Sign in with ChatGPT for external applications. If **Approved applications** is on, members can only use Sign in with ChatGPT for applications that are approved.

### Domains

The **Domains** section allows you to add and remove verified domains. Please refer to our documentation page [here](/en/articles/10472980-enabling-sso-on-chatgpt#h_97e0923af5) for a walkthrough on verifying a domain.  
  
As mentioned previously, a unique domain can only be verified once. If you attempt to verify a domain and receive a message indicating it is already in-use, please reach out to Support for further assistance.

### Domain Eligibility and Mapping

Domain Mapping allows you to choose which of your verified domains apply to different workspaces and organizations within the Tenant. Mapped domains apply to the following features:

* SSO
* (ChatGPT) Automatic Account Creation
* (ChatGPT) External Invites
* (ChatGPT) Account Merges

In order for SSO to apply to a particular workspace + domain, you ***must*** ensure that the domain is mapped accordingly. If SSO is only enabled for the workspace or organization, but no domains are mapped, then the connection is effectively inactive.

When you first verify a domain, we default it to **Not Mapped** to help ensure that it doesn't immediately apply to your workspaces or organizations and potentially lock out users before you're ready.

![Identity & Access Domains page with tenant.agifeels.com options menu open to Manage Eligibility](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-d202f6440d29ad42332b4da8/c30d42766c4ae9e131a9d5fba35a8ad9/Screenshot_2025-11-05_at_11_25_35_E2_80_AFAM.png)

You can choose between mapping the domain to **All Workspaces/Orgs** or else a subset of workspaces. While mapped domains can be applied on a per-workspace basis, they apply globally across all API orgs (even those outside of the Tenant). This is because API Platform SSO remains entirely domain-based, compared to ChatGPT SSO which is workspace-and-domain-based:

![Manage tenant.agifeels.com dialog with Specific Workspaces/Orgs selected and All API Orgs checked](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-05f99c58fbc0cd3e42f4b7da/a2f2db6de82e67381e38f259537228aa/Screenshot_2025-11-05_at_11_35_39_E2_80_AFAM.png)

Let's take a deeper look into each of the remaining features addressed by domain mapping. Please note that both Automatic Account Creation and External Invites are configured at the workspace level rather than directly from the Global Admin Console.

#### Automatic Account Creation (AAC)

When enabled on a ChatGPT workspace, a new user whose email matches the verified domain(s) will automatically receive an invitation to the Enterprise workspace when they sign up.  
  
If you have mapped a domain to multiple workspaces, the user will automatically receive invitations to each workspace.  
  
We do not recommend enabling AAC if you are using SCIM.

Keep in mind that if AAC is enabled, all users with a matching, verified domain will be forced to merge any preexisting personal accounts into the Enterprise workspace. Review our documentation page [here](/en/articles/10479654-understanding-your-ideal-user-management-setup#h_c3d0c4e6cb) for more information.

#### External Invites

This setting controls whether or not users with non-verified domains can be invited to the workspace. Users from external domains will not be required to log in through SSO, as SSO settings only apply to users belonging to the verified domain(s).

#### Account Merge

Please review our documentation page [here](/en/articles/10479654-understanding-your-ideal-user-management-setup#h_e3027c8b11) to better understand how the Account Merge implementation looks, along with its corresponding logic.

### Single Sign-On (SSO)

The **Single Sign-On** section allows you to establish a single SSO connection which you can then apply to all of your Tenant’s API organizations as well as select ChatGPT workspaces. You can follow our documentation page [here](/en/articles/10472980-enabling-sso-on-chatgpt#h_030507d77f) to establish a new SSO connection, or use the **Manage SSO** button to modify an existing connection.  
  
Once you’ve successfully established an active SSO connection, you must ensure the following to successfully apply it:

1. The SSO connection is enabled on ChatGPT or the API
2. Your verified domains are mapped to the workspace or organization

Both ChatGPT and the API Platform allow for the following SSO settings:

* ***Required***: SSO login method becomes mandatory for all Users in the Workspace, and for all Users under the domain on Platform and in Admin console. For ChatGPT, *Users will not be able to sign into the Company's workspace using any other authentication method, including email/password login. For Platform, Users under the Company's domain will not be able to sign in using non-SSO methods (even if they are not a Member of the Company's Platform Org).*
* ***Optional***: SSO login method can be used, and other methods are also available.
* ***Off***: SSO login cannot be used. When SSO is off, ChatGPT and Platform users can log in with Social Authentication or Password.

***Note:*** *Customized Workspace SSO settings take priority over the general workspace setting. For example, if your Workspace SSO settings are “Required,” then you can still customize an individual workspace to “Optional” and have the latter take precedence.*

#### ChatGPT SSO Settings

You now have the ability to customize the application of your SSO connection across multiple workspaces within the Tenant:

![Global Admin Console Single Sign-On settings with ChatGPT SSO set to Optional](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-3a1275b30774b3e026833c0a/f86d19bcf6f5e0558048a0f6bfa5a6f4/workspace.png)

The custom setting options mirror the options available on ChatGPT itself. As mentioned previously, the custom SSO settings defined on a single workspace take precedence over the global ChatGPT SSO settings:

![Workspace-specific SSO Settings dialog with Required selected and a menu of Required, Optional, and Off](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-543670b464b555b0a4141c87/3afe1d961c9360b6ad70ba9d0a6f588a/Screenshot_2025-11-05_at_3_45_35_E2_80_AFPM.png)

#### Platform SSO Settings

Similar to ChatGPT, you can choose how to apply your SSO connection to your API organization(s). The key difference is that Platform SSO remains domain-based at this time. This means that when SSO is enabled (required or optional), it applies to **all** **Organizations both within your Tenant and outside your Tenant**:

![Global Admin Console Single Sign-On settings with API SSO set to Required](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-bbebf130f86a82ca8920ed66/33d480cc3340f147781aaff64acef106/platform.png)

As a result, we do not allow for customization of SSO on API Platform organizations.

#### Admin Portal SSO Settings

The Admin Portal SSO Settings determine how Tenant Admins log into [admin.openai.com](http://admin.openai.com). The options follow the same logic discussed in the above SSO section.

#### Manage Invites

At this time, the **Manage Invites** section is a work-in-progress and a view of what’s to come. We plan to add support for user provisioning and management (both directly and via SCIM). Thank you for your patience while we work to add support for this functionality.

## People

The **Peopl**e tab shows all of the users across your Tenant’s various workspaces and organizations. From the default view, you can search for specific users by name or by email, and have the ability to promote individual users to be Tenant admins:

![OpenAI Admin People page with a user actions menu open including Make a Tenant Admin](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-3461938fe749fafdceb530bd/8d2bdfc67b34ed798d67713233b1a79d/people1.png)

Additionally, you can view the access that each user has across the different Tenant workspaces and organizations:

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-2dd4c54115d395d639a76da0/4d2647f9b0626385e90cc950f3192fe2/people2.png)

## Analytics

The **Analytics** drop down helps admins review adoption and usage from one place. Admins can compare trends over time, review active-users and message activity, and drill into detailed views for leaderboards,  credits consumed broken down by Codex and ChatGPT uses, ChatGPT analytics, and Codex analytics.   
  
The table below describes the range of historical data available, per analytics category.

|  |  |
| --- | --- |
| ChatGPT & Codex credit analytics | Available from 5/18/2026 |
| Codex usage analytics | Available for the past 90 days |
| ChatGPT usage analytics | Prior 12 months |

Codex and ChatGPT credit data beyond these periods can be obtained from the credit usage report in billing settings. For ChatGPT Business, go to Workspace settings -> [Billing](https://chatgpt.com/admin/billing). For ChatGPT Enterprise, go to the [billing](https://admin.openai.com/billing) tab in the global admin console, and click the export button in the top right.   
  
  
**Note**: The admin console provides an overview of ChatGPT analytics - more details, including usage of projects, skills and GPTs can be found in Workspace settings. Learn more.

Analytics data is typically refreshed at the following timeframes:

|  |  |
| --- | --- |
| ChatGPT & Codex credit analytics | 1-6 hours |
| Codex usage analytics | 1-6 hours |
| ChatGPT usage analytics | Up to 48 hours |

## Overview

The Overview section provides a dashboard of usage, including active users, credits, tokens, and messages for ChatGPT and Codex. Additionally, the view includes user and agent leaderboards, setting date filters, and downloading / exporting data as a csv for a specified date range.

## Leaderboards

The Leaderboards section helps admins compare adoption and activity across users and workspace agents. Admins can identify top usage patterns, understand where adoption is concentrated, and view key metrics such as tokens used, credits consumed and lines of code written.   
  
Clicking on a user provides granular details about consumption - for example, clicking on a user brings up their credit usage breakdown by product type (ChatGPT or Codex), by metered item (e.g. Input, output and cached input tokens by model) and by model (e.g. GPT 5.5).

## Credits

The Credits section helps admins understand how credits are being used across the selected workspace. Admins can review credit consumption trends over time and, where available, break usage down by product area such as ChatGPT or Codex, by metered item such as input tokens, output tokens, or cached input tokens, and by model. This can help identify which products, users, agents, or models are driving credit usage.  
  
Note that some legacy or rate-limit-only plans may not show credit activity, or credit charts.

## ChatGPT

The ChatGPT section gives admins an overview of ChatGPT adoption and activity for the selected workspace. Admins can review trends such as active users, message activity, and ChatGPT-related credit usage, with more detailed breakdowns available where supported.  
  
For deeper ChatGPT reporting, including usage of projects, skills, and GPTs, admins can continue to use the analytics page in Workspace settings.

## Codex

The Codex section gives admins a concise Codex-specific view of usage in the console. It shows Codex adoption and activity, such as active users, credits used, tokens used, messages runs, lines of code generated, plugin calls, skills used, and code review activity where available.

## Billing (ChatGPT Enterprise/Edu only)

Use Billing to review billing details for ChatGPT Enterprise/Edu workspaces.  
  
  
***Note****: this tab replaces the Billing tab formerly available in Workspace settings for ChatGPT Enterprise and Edu accounts. ChatGPT Business owners and admins should continue to manage their billing settings from Workspace settings.*  
  
  
Billing is scoped to the selected workspace. It does not use an all-workspaces view. If you manage more than one workspace, use the workspace selector to choose the workspace you want to review.

Depending on your plan and permissions, Billing may include these tabs:

* Plan.
* Grant activity.
* Invoices (Workspace owners only).

### Plan

The Plan tab shows plan and credit information for the selected workspace.

Depending on your workspace and permissions, you may see:

* License details, such as Enterprise or Edu license information.
* Seat usage.
* Credit balance.
* Unbilled overage
* Credit activity or usage charts.
* Usage alerts.
* Overage limit settings.

Some legacy or rate-limit-only plans may not show credit balances, credit activity, or credit charts.  
  
Admins and owners can use these settings to manage credit usage alerts and set overage limits.

### Grant activity

If Grant activity is available, use it to review credit grants and credit activity for the selected workspace.

### Invoices

If the Invoices tab is available, use it to review invoices for the selected workspace.

Invoice access can be more restricted than general Billing access. If you can view Billing but do not see Invoices, your account may not have permission to view invoice details.

## Agents

The “Agents” area helps admins understand which workspace agents exist across their organization and how they are being used. Admins can open an agent to review details such as its Agent ID, move into the Builder to edit it, inspect recent activity, connected apps, and memory files, manage schedules, and review agent analytics such as unique users and runs over time.

# Adding/Removing Workspaces and Organizations

If you would like to add or remove additional workspaces or organizations from your Tenant, please reach out to [support@openai.com](mailto:support@openai.com) for assistance.

# Troubleshooting Global Admin Console

### "Unable to login / You are not a global admin" error

Membership to the Global Admin Console is separate from membership to workspaces and organizations. It's likely that other workspace and organization owners are global admins and can invite you. If not, please ensure you are an owner of each of your workspaces and organizations, then reach out to support@openai.com with the IDs for each organization and workspace. These identifiers can be found at [platform.openai.com/settings/organization/general](https://platform.openai.com/settings/organization/general) and [chatgpt.com/admin](https://chatgpt.com/admin) respectively.

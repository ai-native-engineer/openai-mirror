<!-- source: https://academy.openai.com/public/clubs/admins-6o6xf/resources/scim -->

[Admins](/en/public/clubs/admins-6o6xf/overview)

[navigation.content](/en/public/clubs/admins-6o6xf/content)

Article

March 11, 2026 · Last updated on May 29, 2026

# Automate provisioning and unlock actionable analytics with SCIM

![Automate provisioning and unlock actionable analytics with SCIM](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Admins-Cover-Images-25--7999bf69-6ca4-4ad0-b763-1111d0e27b5d-1773273301705.jpeg?fit=scale-down&width=1200)

# Leaders & Admins

# Deployment & Adoption

# Personal

## A focused guide for enabling reliable provisioning and better workspace analytics

![Automate provisioning and unlock actionable analytics with SCIM](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Admins-Cover-Images-25--7999bf69-6ca4-4ad0-b763-1111d0e27b5d-1773273301705.jpeg?fit=scale-down&width=1200)

# **SCIM for ChatGPT Enterprise**

*A focused guide for enabling reliable provisioning and better workspace analytics*

SCIM is a standard way to keep SaaS access aligned with your identity provider (IdP): who has access, and which org groups they belong to. If your organization already uses SCIM for tools like Slack, Atlassian, GitHub, ServiceNow or Zoom the setup pattern for ChatGPT will feel familiar: an IdP-managed app integration with a scoped set of users and groups.

For ChatGPT Enterprise, SCIM is useful for several outcomes:

1. **Automating user lifecycle management:** Easily provision and deprovision by managing user association to groups centrally in the IdP. Avoid manual invites as well as stale memberships.

2. **Making workspace analytics actionable:** Segment insights by the organizational units that SCIM groups represent, e.g., department, function, or team to understand how ChatGPT and Codex are (and aren’t) currently used. Infer which successful patterns from one group can be scaled to others and  which groups require additional enablement.

3. **Configure role based access and controls:** Enable role-based access controls (RBAC) by syncing IdP groups via SCIM, allowing administrators to manage permissions, feature access, set spend controls, and test or roll out features to selected user groups.

## **What is SCIM?**

**SCIM (System for Cross-domain Identity Management)** is a protocol that enables organizations to automatically provision, update, and deactivate users, as well as synchronize group memberships from their identity provider (IdP) to downstream applications such as ChatGPT.

SCIM is **distinct from SSO**: SSO handles user authentication (sign-in), while SCIM manages user lifecycle and group synchronization for access control and governance.

See the [OpenAI SCIM integration documentation for configuration details](https://help.openai.com/en/articles/10011769-scim-integration-faq).

## **How SCIM works**

SCIM integrations follows a similar pattern across apps incl. ChatGPT:

|  |  |  |
| --- | --- | --- |
| **Step** | **What happens** | **Owned by** |
| 1. Enable provisioning | Turn on SCIM/directory sync in the Identity and Provision tab for ChatGPT | ChatGPT workspace owner |
| 2. Configure IdP app | Create/configure the SCIM app in Okta/Entra/etc. | IT/IAM |
| 3. Map attributes | Confirm identifiers (usually email assuming they match the user’ OpenAI email addresses) and optional profile fields | IT/IAM |
| 4. Validate | Add/remove a test user; confirm expected behavior | IT/IAM + app admin |
| 5. Operate | Ongoing (de-)provisioning flows and group maintenance | IT/IAM |

## **Recommended group designs**

### **Granularity for analytics insights**

Use organizational units with clear owners that can steer based on the insights provided. The groups should also be of sufficient headcount (at least 10) to show meaningful aggregated trends w/o identifying individual users. Typical aggregation levels include:

|  |  |  |
| --- | --- | --- |
| **Dimension** | **Good starting point** | **Notes** |
| Function / Department | Engineering, Sales, Support, Marketing, Finance | Usually the highest-signal slice |
| Region | NA, EMEA, APAC | Helpful if you run internal programs regionally or for restricting features due to the regional context |
| Business unit | BU\_X, BU\_Y | For companies operating in BUs – enables detailed analyses and comparison across BUs |

### **Naming conventions**

A consistent prefix makes it easier to manage at scale, especially if SCIM groups are used for multiple purposes. We generally recommend [USAGE]\_[DIMENSION]\_[GROUP], e.g.: ANALYTICS\_FUNCTION\_Engineering, ROLLOUT\_REGION\_EMEA, TESTING\_CODEX\_LOCAL – [USAGE] can be left out if there is only one use case initially.

## **Implementation plan**

### **Phase 0: Decide provisioning posture**

Choose one primary provisioning strategy:

1. **SCIM-driven provisioning:** Users are provisioned proactively via IdP groups. When users are assigned to the ChatGPT app or to a synced group in the IdP, they are automatically provisioned and invited to the workspace.

2. **Just-in-time creation:** Users are created reactively when they first sign in to ChatGPT.

Many organizations prefer **SCIM-driven provisioning** because it aligns access with the IdP lifecycle. If you choose SCIM, start with a small scope and expand after validation. See the [OpenAI guidance on user management setups](https://help.openai.com/en/articles/10479654-understanding-your-ideal-user-management-setup).

### **Phase 1: Pilot (1–2 groups)**

1. Select 1-2 stable groups (e.g., FUNCTION\_Engineering, FUNCTION\_Support)

2. Add a small pilot cohort to the IdP group that is assigned to the ChatGPT SCIM app

3. Validate:

* Users appear as expected (managed vs. manual)

* Group sync appears as expected

* Joiner/leaver flow works as intended

* Existing manually invited users become SCIM-managed once their account is matched via email and assigned to a synced IdP group.

### **Phase 2: Expand to Level 1 coverage**

Scale to your 5–15 “Level 1” groups. Hold off on matrixed or highly granular groups until you’ve used the analytics for at least one enablement cycle. Overly granular groups can make provisioning harder to manage and provide little additional insight early in an adoption program.

## **Common questions**

|  |  |
| --- | --- |
| **Concern** | **Clarification** |
| “This is a big, ChatGPT-specific build.” | SCIM is the same IdP app pattern used across SaaS. The main decision is scoping and which groups to sync. |
| “SCIM means everyone gets auto-invited.” | Access is controlled throughIdP app assignment. Only users assigned to the ChatGPT app are provisioned. SCIM groups simply synchronize membership for those users and can be used for analytics, permissions, or feature rollouts. |
| “This exposes employee data.” | SCIM typically syncs identity and allows to control which membership metadata is shared. Analytics is aggregated and access-controlled. |
| “We’ll have to model the entire org chart.” | You only need the minimal group set you want for provisioning and reporting. Start with functions. |

## **Resources to share with your IT teams**

Use this email template to share with your team:

Hi team,

I’d like to request that we enable SCIM provisioning and group sync for our ChatGPT Enterprise workspace.

This would move user provisioning and deprovisioning into our existing IdP workflow, reduce manual access management, and allow organizational groups to sync into the workspace.

With group sync in place, we would also be able to segment Workspace Analytics by department or function and use IdP groups more effectively for access management and feature rollout decisions.

I’m happy to walk [through the documentation](https://help.openai.com/en/articles/10011769-scim-integration-faq) with you and support validation of the configuration once it is set up.

Thanks,
[YOUR NAME]

Table Of Contents

[Empowering and supporting your team](/en/public/clubs/admins-6o6xf/resources/empowering-and-supporting-your-team)

[Communicating about ChatGPT Enterprise to your team](/en/public/clubs/admins-6o6xf/resources/team-communication)

[Inviting and managing your team](/en/public/clubs/admins-6o6xf/resources/inviting-and-managing-your-team)

[Feature controls and integrations with your tools](/en/public/clubs/admins-6o6xf/resources/feature-controls-and-integrations-with-your-tools)

Jul 10th, 2025 • Views 7.1K

[Leading impactful ChatGPT Trainings](/en/public/clubs/admins-6o6xf/resources/leading-impactful-chatgpt-trainings)

Sep 23rd, 2025 • Views 5.5K

[ChatGPT Enterprise workspace analytics guide](/en/public/clubs/admins-6o6xf/resources/chatgpt-enterprise-user-analytics-guide)

Mar 10th, 2026 • Views 9.7K

[Welcome to the For Work Admins Track!](/en/public/clubs/admins-6o6xf/resources/welcome-admins)

Jan 12th, 2026 • Views 10.9K

[Feature controls and integrations with your tools](/en/public/clubs/admins-6o6xf/resources/feature-controls-and-integrations-with-your-tools)

Jul 10th, 2025 • Views 7.1K

[ChatGPT Enterprise workspace analytics guide](/en/public/clubs/admins-6o6xf/resources/chatgpt-enterprise-user-analytics-guide)

Mar 10th, 2026 • Views 9.7K

[Welcome to the For Work Admins Track!](/en/public/clubs/admins-6o6xf/resources/welcome-admins)

Jan 12th, 2026 • Views 10.9K

[Leading impactful ChatGPT Trainings](/en/public/clubs/admins-6o6xf/resources/leading-impactful-chatgpt-trainings)

Sep 23rd, 2025 • Views 5.5K

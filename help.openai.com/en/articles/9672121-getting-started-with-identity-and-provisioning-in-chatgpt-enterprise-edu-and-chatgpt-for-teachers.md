<!-- source: https://help.openai.com/en/articles/9672121-getting-started-with-identity-and-provisioning-in-chatgpt-enterprise-edu-and-chatgpt-for-teachers -->

# Getting started with identity and provisioning in ChatGPT Enterprise, Edu, and ChatGPT for Teachers

Updated: 2 days ago

In order for a user to access a ChatGPT Enterprise or Edu workspace, two things need to happen:

* The user needs to be **provisioned** in the workspace
* The user needs to **authenticate** their identity with OpenAI

# Domain verification

Prior to setting up additional provisioning and authentication options, you must verify ownership of one or more email domains on the Identity & Provisioning page. This associates the email domain with your ChatGPT Enterprise workspace. [Learn more about domain verification for ChatGPT Enterprise and Edu](/en/articles/9534785-provisioning-sso-for-chatgpt-enterprise#h_189aa10033).

# Provisioning

By default, workspace owners and admins provision users by [inviting them through the ChatGPT workspace Members page](/en/articles/8266401-how-do-i-add-change-or-remove-chatgpt-enterprise-members).  
  
To automate the provisioning process, workspace owners can configure the following options on the Identity & Provisioning page:

* **Automatic Account Creation** - grants users access to a workspace automatically based on their email domain when they attempt to log in. [Learn more about Automatic Account Creation](/en/articles/10479654-understanding-your-ideal-user-management-setup#h_c3d0c4e6cb).

* **Directory Sync via SCIM** - automatically invites users into the workspace based on their membership in specified Identity Provider groups. [Learn more about SCIM provisioning](/en/articles/9627404-openai-scim-integration-faq).
* Control whether SCIM-managed groups are discoverable in sharing flows such as GPTs and projects, see: [SCIM Integration FAQ](https://help.openai.com/articles/10011769).

Workspace owners can optionally **disable external domain invites** to limit new invitations to users whose email addresses match verified domains. This restriction applies to new invites only and does not retroactively block existing users or invitations that were already sent.

Note: These features are not currently available to ChatGPT for Teachers users.

## Email invitations and account migrations

When a user is invited into your ChatGPT Workspace, either manually or via SCIM provisioning, OpenAI will send them an invitation email by default (see [this article](/en/articles/9627404-openai-scim-integration-faq) for cases when an email will not be sent). If the user has an email address matching a verified domain, the user will automatically be added to the workspace whether they accept the invite link in their email or log in through chatgpt.com  
  
If an invited user with an email address matching a verified domain has an existing ChatGPT account, they will be prompted to migrate their account to the Enterprise workspace upon accepting the invitation. Users can choose to transfer their existing data to the Enterprise workspace, or to export and delete their data. Paid personal subscriptions are automatically canceled as part of the migration process.

*Note: When a user transfers their personal workspace into a ChatGPT Enterprise or Edu workspace, personal GPTs that were already shared or published, including GPTs shared by link, are converted to workspace-visible GPTs in the destination workspace. GPTs that were private before transfer remain private. Workspace owners can review and update the visibility of transferred GPTs after migration.*

If an invited user has an existing ChatGPT account associated with an email address which *does not* match a verified domain, they will not be prompted to migrate their account and can keep both their personal account and their access to the Enterprise workspace.

![ChatGPT Enterprise invite flow offering transfer of existing chat history and GPTs or export and delete workspace](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-635bd1817a2c2d231850dcf7/ff210261fc0230e0fec35a759407205c/AD_4nXdH4wmPBytnpDjccGmoRSEr77t686C6tJKIiVj3DA5H17OqrtHEN_eYT94Sae8LOBBr9w_VWvZG-d3Vj7XvwM1FXHjQNi1BPU3E-FmHwkCBbrzaTuny4ZEDZHYt)

*Account migration workflow displayed to users in the ChatGPT Enterprise UI.*

---

Enterprise workspaces that have Data Residency enabled, will only be able to avail of the option to export chats and delete Personal workspaces. Data migration is not supported for Data Residency workspaces. Users will be presented with the following modal:

![personal-biz-export-dr-modal](https://images.ctfassets.net/j22is2dtoxu1/0VZE7TXC7Mv4GhgSAG5ju/690bae903bb62f78f7639227a04054b6/export-dr.png)

*Data Export workflow displayed to users in the ChatGPT Enterprise UI for Data Residency Enterprise workspaces.*

***Note:*** *For ChatGPT Business plans upgrading to an Enterprise plan:*

*Users belonging to the ChatGPT Business workspace will* ***not*** *be prompted to migrate their* ***Business*** *workspace into the* ***Enterprise*** *workspace, but will be prompted to migrate their* ***personal*** *workspace.*

# Authentication

By default, users authenticate with OpenAI using an email address and password, or by using Social login (Google, Microsoft, or Apple).  
  
To further secure the authentication process, workspace owners can configure the following **Single Sign-On (SSO)** on the Identity & Provisioning page:

* **Enable** **SSO** - Users who have been provisioned in the workspace and who have an email address associated with a verified domain are able to authenticate via the integrated Identity Provider (IdP). When SSO is enabled but not enforced, users can still choose to authenticate with their username and password or with Social login via Google, Microsoft, and Apple.
* **Enforce SSO** - Has the additional effect of disabling Social login for users who have been provisioned in the workspace and who have an email address associated with a verified domain.

Enabling or enforcing SSO by itself *does not* impact the experience of the following types of users:

* ChatGPT users with an email matching a verified domain who are not provisioned in the workspace. These users can continue to access their personal ChatGPT accounts after SSO is configured.
* ChatGPT users with an email domain which *does not* match a verified email domain but who are provisioned in the workspace. These users can continue to access the ChatGPT Enterprise workspace via password-based or Social login methods.

[Learn more about configuring SSO](/en/articles/9534785-provisioning-sso-for-chatgpt-enterprise).

## Configuring SSO across OpenAI products

Your ChatGPT Enterprise workspace and OpenAI API Platform organizations share a single SSO connection with your IdP. As a result, domain verifications and SAML SSO settings are shared between products. If you have already configured SSO in your API Platform organization, verified domains and SAML SSO settings will be pre-populated in ChatGPT. The reverse is also true.  
  
SSO has to be enabled separately on ChatGPT vs. the API Platform. However, once you've configured it on one, the other's "setup" is largely flipping the switch and adding a bookmark app in your IdP if so desired.

|  | API Platform SSO enabled | API Platform SSO disabled |
| --- | --- | --- |
| ChatGPT SSO enabled | ✅ | ✅ |
| ChatGPT SSO disabled | ✅ | ✅ |

[Learn more about API Platform SSO configuration](/en/articles/9641482-api-platform-single-sign-on-sso-integration-for-existing-enterprise-customers).

# Recommended identity and provisioning patterns

ChatGPT Enterprise gives you the flexibility to mix and match identity and provisioning options. The most common patterns are provided for reference.

|  | **Provisioning** | **Authentication** | **User experience** |
| --- | --- | --- | --- |
| **Opt-in access** Any user who authenticates with an email address associated with a verified domain will be automatically provisioned in your workspace. | Automatic Account Creation | Password or Social | Upon signing up for or logging into a personal account, users will be prompted to migrate their personal account to the Enterprise workspace. |
| **SSO with manual invites** Users who are manually invited to the workspace can authenticate with SSO. | Manual | SSO Enabled or Enforced | Users can continue to sign up for or log into their personal accounts. After being invited into the Enterprise workspace, users will be prompted to migrate their existing personal account. |
| **SSO with Automated Account Creation** Any user who authenticates with an email address associated with a verified domain will be automatically provisioned in your workspace and can subsequently authenticate with SSO. | Automatic Account Creation | SSO Enabled or Enforced | Upon signing up for or logging into their personal account, users will be prompted to migrate their personal account to the Enterprise workspace. Note: users without the ability to authenticate via the IdP will be   **unable to**  log into ChatGPT after migrating to the Enterprise workspace. |
| **SSO with SCIM** Users who are a member of a specified IdP group are automatically invited to workspace and can subsequently authenticate with SSO. | SCIM | SSO Enabled or Enforced | Users can continue to sign up for or log into personal accounts. Upon being added to the specified IdP groups, users receive an invitation email and are prompted to migrate their existing personal account. |

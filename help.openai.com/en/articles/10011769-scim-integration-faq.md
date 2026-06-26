<!-- source: https://help.openai.com/en/articles/10011769-scim-integration-faq -->

# SCIM Integration FAQ

ChatGPT and API Platform SCIM

Updated: 3 days ago

The OpenAI SCIM Integration allows identity providers to exchange user identity data with OpenAI, automating the provisioning of ChatGPT and API Platform invitations and removals of users from ChatGPT workspaces and API Platform organizations. Unlike SSO, SCIM is not shared across ChatGPT workspaces and API organizations.  
  
SCIM integration is only available for API Platform organizations with Custom or Unlimited Billing Plans and ChatGPT Workspaces with Enterprise or EDU plans. SCIM is not available in ChatGPT for Teachers. To learn more about these Billing Plans, please, [contact OpenAI Sales team](https://openai.com/business/).

## Common SCIM Questions

### How do I set up the SCIM integration?

ChatGPT SCIM can be configured in the [Identity and Provisioning](https://chatgpt.com/admin/identity) tab. API Platform SCIM can be configured in the [Identity settings](https://platform.openai.com/settings/organization/identity). Users with Owner access can enable “directory sync”, guiding them through setting up directory sync with your IdP provider via the WorkOS portal. Here’s a view of the WorkOS portal:

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-2b41012a752cacf57c2db9e4/059610012c750364cae885581d56ca48/AD_4nXdEQ1IjbnjWW6PxoRPWVzmqJX1khhiQMAfatOomsxc8uYFb4I417jwsWTuL39sHoKLFJS1AhtUX-X-vTtsdV5gBWF9ShXtwZJTRLzhcAgnokWD8pz7lD3Yutpuv)

### Which IDPs are supported by the SCIM integration?

Supported IdPs include Okta, Entra ID (Azure AD), Google Workspace, PingFederate, OneLogin, Rippling, and more, with options for custom SCIM implementations and an SFTP endpoint for CSV file provisioning.

### What does it mean to be “managed by SCIM”?

“Managed by SCIM” means a user’s account is controlled through automated provisioning and deprovisioning based on synced directory information. Manually added users are not managed by SCIM unless later synced from the directory.

### Can users be manually added in addition to using SCIM?

Yes. ChatGPT users can be added to the workspace manually via the [Members page](https://chatgpt.com/admin/members). API Platform users can be added to the organization manually via the Platform settings [People page](https://platform.openai.com/settings/organization/people/members) or the [Administration API](https://platform.openai.com/docs/api-reference/invite/create). The member lists will indicate which users are managed by SCIM versus those added manually.

### What happens if a user's first name and last name in ChatGPT don't match what is in the IDP?

ChatGPT users can edit their name in our services, but for users managed by SCIM, name changes from your IdP can update the name shown in ChatGPT. SCIM still matches users by email address, so a name mismatch alone should not prevent provisioning or membership changes.

### What happens if a user updates their email in the IDP?

When a user's email changes in the Identity Provider, an event is sent via SCIM to notify OpenAI of the change. If the [administrative email change criteria](/en/articles/4936827-how-to-change-your-email-address#administrative-email-changes) is met, the user's email address will be changed.  
  
If the user's email address fails to change, please review the criteria and contact support@openai.com for assistance as needed.

### How often does the SCIM directory sync?

Most services sync every 30 to 40 minutes (some services sync immediately, such as Okta).

### Is there a way to force directory syncs?

At the moment, there is no way to force a SCIM directory sync. Please contact Support by creating a ticket on the bottom-corner of this Help page if you experience issues with your SCIM directory.

## ChatGPT

### What happens when a ChatGPT user is invited via SCIM?

If the user **is** already in the workspace and becomes SCIM managed, they will not receive an email.  
  
If a user is provisioned with SCIM and the user **is not** already a member of the workspace, the user will be sent an email letting them know they have been invited to the workspace.  
  
The user can accept the invite by using the link in their email invite or by logging in through [chatgpt.com](http://chatgpt.com/). If the user does not accept the invitation, the user will continue to show as a "Pending Invite" in the Members tab.

### How does Automatic Account Creation interact with SCIM?

[Automatic Account Creation](/en/articles/9534785-provisioning-sso-for-chatgpt-enterprise#h_ca54dc1f7a) provisions users *reactively*, at the time they attempt to sign up or log in. This is known as “just-in-time” provisioning. By contrast, SCIM provisions users *proactively*, as soon as they are added to a specified IdP group.  
  
As a best practice, we strongly recommend *against* enabling both Automatic Account Creation and SCIM. Enabling both features on your account may result in provisioning access to unmanaged users. Remember that only those users managed by SCIM can be automatically deactivated in response to changes in IdP group membership.

### How do I enable Groups with my SCIM integration?

When you enable the directory sync with ChatGPT, your existing synced directories will be automatically synced with ChatGPT Groups. Any group you choose to sync with your IdP will be automatically reflected in ChatGPT.  
  
You will still have the ability to manually create groups in your [ChatGPT workspace settings](https://chatgpt.com/admin/settings).

### Can workspace owners control whether SCIM-managed groups appear in sharing flows?

Workspace owners can control whether SCIM-managed groups are discoverable to workspace users in sharing flows such as GPTs and projects.

1. Go to **Workspace settings.**
2. Select **Identity & access**.
3. Review **Discoverable by workspace users**.

Note that this setting does **not** remove the groups from SCIM sync or stop group provisioning. If enabled, SCIM-managed groups will not appear in various sharing functionalities inside ChatGPT.  
  
If a project or GPT is already shared with one or more SCIM-managed groups, those groups will be removed from the sharing list the next time the project or GPT is updated.

### Will the SCIM group overwrite the ChatGPT group?

Yes. If you already have a ChatGPT group with the same name as a group synced from your IdP, the existing ChatGPT group becomes managed by SCIM instead of creating a duplicate group. Its membership is then controlled by your IdP, so review the group in your IdP before enabling sync if the existing ChatGPT group has manually managed members.

### How can I tell which users or groups were added via SCIM?

In the [Members](https://chatgpt.com/admin) [and Groups](https://chatgpt.com/admin/groups) sections of your ChatGPT workspace settings, each user or group will have a badge next to its name to indicate if it was added via SCIM.

### What happens to a user’s data if they are removed and then added back via SCIM?

Removing and re-adding a user via SCIM follows the same data-retention behavior as manual removal, and is handled according to the workspace’s data-retention policy. For full details, please refer to our article: [Data retention when a member is removed from a workspace](https://help.openai.com/articles/8266418)

### Can I temporarily suspend or disable a SCIM-managed user while keeping SCIM enabled?

Not from within ChatGPT alone. For SCIM-managed ChatGPT workspaces, your identity provider (IdP) is the source of truth for user access. If a user remains assigned to the ChatGPT application or to a SCIM-provisioned group in your IdP, manually removing them from the workspace may only be temporary. The user can be added back on a later SCIM sync or manual resync.  
  
To temporarily prevent access while keeping SCIM enabled for the rest of your workspace, update the user’s access in your IdP. The most reliable approach is to remove the user from the ChatGPT app assignment or from the provisioning group that grants access. When you’re ready to restore access, add the user back in your IdP and SCIM will provision them again.  
  
Note: Depending on your IdP, suspending or disabling the user account may not remove the ChatGPT app assignment. If the assignment remains active, the user may still be reprovisioned. A “no permissions” group inside ChatGPT is also not a reliable substitute for suspending access.

## API Platform

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-2b41012a752cacf57c2db9e4/059610012c750364cae885581d56ca48/AD_4nXdEQ1IjbnjWW6PxoRPWVzmqJX1khhiQMAfatOomsxc8uYFb4I417jwsWTuL39sHoKLFJS1AhtUX-X-vTtsdV5gBWF9ShXtwZJTRLzhcAgnokWD8pz7lD3Yutpuv)

### What happens when an API Platform user is invited by SCIM?

When a user is provisioned by SCIM, the user receives an invite to the Platform organization. The provisioned user needs to accept the invitation or log in again to become an organization member. If the user does not accept the invitation, the user will continue to show as a “Pending Invite” in the Members tab.  
  
If a user is provisioned with SCIM and the user isn't already a member of the organization, the user will be sent an email letting them know they have been invited to the organization. If the user is already in the organization and becomes SCIM managed, they will not receive an email.

### How can I tell which users were added via SCIM?

In the [Organization Members](https://platform.openai.com/settings/organization/team) section of your Platform settings, each user or invite will have a badge next to its name to indicate if it was added via SCIM.

### What updates can I make to my users via SCIM?

We currently support syncing name updates from your Identity Provider (IdP). Please note that if a user belongs to multiple organizations, any name changes will be applied across all of them. Users can also manually update their own name at any time.

### Can I enable Groups with my API Platform SCIM integration?

Yes. Groups can be synced from your Identity Provider (IdP) via SCIM, which keeps membership up to date automatically. You can then assign roles to those groups within the OpenAI Platform.

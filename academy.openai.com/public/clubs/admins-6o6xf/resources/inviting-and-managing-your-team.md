<!-- source: https://academy.openai.com/public/clubs/admins-6o6xf/resources/inviting-and-managing-your-team -->

[Admins](/public/clubs/admins-6o6xf/overview)

[Content](/public/clubs/admins-6o6xf/content)

Article

July 8, 2025 · Last updated on September 17, 2026

# Inviting and managing your team

![Inviting and managing your team](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Admins-Cover-Images-10--32d896ee-286a-4cc8-9eeb-5a045412d7ca-1754316122967.jpeg?fit=scale-down&width=1200)

# Leaders & Admins

# Foundations

# Work

# Portfolio Company Dev & IT

# Portfolio Academy Cyber

## Learn how to manage user access.

![Inviting and managing your team](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Admins-Cover-Images-10--32d896ee-286a-4cc8-9eeb-5a045412d7ca-1754316122967.jpeg?fit=scale-down&width=1200)

## **Inviting and managing your team**

### **Roles and permissions**

In both ChatGPT Enterprise and ChatGPT Business, there are three roles: **Owner, Admin, and Member**.

* **Owners** have full control over the workspace, including billing, settings, and identity management. They can invite or assign Admins/Owners, manage all available organization-wide settings, and access billing details.

* **Admins** can manage users (e.g. invite/remove members), as well as manage some organization-wide settings, like Connectors. Enterprise Admins can also organize users into groups and view usage analytics.

* **Members** are end-users who can use ChatGPT. In ChatGPT Business, they can also invite or remove other members -  whereas ChatGPT Enterprise restricts user management to Admins/Owners for tighter control.

See more about roles in  [ChatGPT Enterprise](https://help.openai.com/en/articles/8266431-what-is-the-difference-between-different-roles-on-my-chatgpt-enterprise-workspace) and  [ChatGPT Business](https://help.openai.com/en/articles/8798607-what-roles-are-there-in-a-chatgpt-team-workspace).

### **User access and onboarding strategy**

Decide how employees will be added to the ChatGPT workspace and how they'll log in.
**Enable single sign-on:** Enabling SSO lets users log in with corporate credentials and enforces your organization’s authentication policies.. This simplifies user login and improves security. Decide on this early so you can configure SSO and test before org-wide onboarding.

* ﻿ [Guide: Setting up Single Sign On](https://help.openai.com/en/articles/9534785-configuring-sso-for-chatgpt-enterprise)﻿

* ﻿ [SCIM integration](https://help.openai.com/en/articles/9627404-openai-scim-integration-faq): Automate the provisioning and deprovisioning of user accounts in ChatGPT Enterprise with  [supported IDPs](https://help.openai.com/en/articles/9627404-openai-scim-integration-faq) or custom SCIM implementations.

* Reach out to **[[email protected]](/cdn-cgi/l/email-protection)** with any issues or questions

**Verify your company domain:** Verifying your company’s email domain means only users with that domain can join the workspace, providing an extra layer of access control. See:  [Domain Verification for ChatGPT](https://help.openai.com/en/articles/8871611-domain-verification)﻿

**Bulk user provisioning:** Decide if you will onboard users gradually or all at once. ChatGPT Business allows bulk inviting via CSV, which is useful for initial rollout. Enterprise goes further by supporting  [**SCIM provisioning**](https://help.openai.com/en/articles/9627404-openai-scim-integration-faq) (automated user provisioning/de-provisioning through your identity provider).

**Merging accounts:** If some employees already use ChatGPT (Free/Plus/Pro) with a company email, decide whether to have them merge their account into the new workspace or keep it separate. Learn more about  [migrating accounts to ChatGPT Business workspaces](https://help.openai.com/en/articles/8801890-can-i-migrate-or-merge-my-chatgpt-free-or-plus-workspace-over-to-my-chatgpt-team-workspace) and  [migrating accounts to ChatGPT Enterprise workspaces](https://help.openai.com/en/articles/10479654-understanding-your-ideal-user-management-setup#h_41adf246c2).

**User offboarding:** Plan how you will remove users who leave the company or should no longer have access.

* In ChatGPT Business, any user can remove other users from the workspace.

* In ChatGPT Enterprise, only Admins/Owners can remove users. Decide who will be responsible for periodic audits of the member list and ensure there’s a process to promptly remove departing employees’ access. SCIM can help automate the deprovisioning process.

### **Account security and authentication**

**Enforce strong authentication:** ChatGPT supports multi-factor authentication (MFA) for added login security.  Enterprise SSO will delegate authentication security to your identity provider, so if you have MFA or conditional access policies in your IdP, those will apply. **See:**  [**Enabling or disabling Multi-Factor Authentication (MFA)**](https://help.openai.com/en/articles/7967234-enabling-or-disabling-multi-factor-authentication-mfa).

**Compliance API:** ChatGPT Enterprise also supports audit logging via the [**Compliance API**](https://help.openai.com/en/articles/9261474-compliance-api-for-enterprise-customers) for conversations – consider using this to track logins and usage patterns as part of your security oversight.

[Data governance and compliance](/public/clubs/admins-6o6xf/resources/data-governance-and-compliance)

[Measuring impact and ROI](/public/clubs/admins-6o6xf/resources/measuring-impact-and-roi)

[Automate provisioning and unlock actionable analytics with SCIM](/public/clubs/admins-6o6xf/resources/scim)

[Empowering and supporting your team](/public/clubs/admins-6o6xf/resources/empowering-and-supporting-your-team)

Jul 5th, 2025 • Views 19.4K

[Planning your ChatGPT rollout](/public/clubs/admins-6o6xf/resources/planning-your-chatgpt-rollout)

Jul 11th, 2025 • Views 7K

[Communicating about ChatGPT Enterprise to your team](/public/clubs/admins-6o6xf/resources/team-communication)

Aug 5th, 2025 • Views 13.5K

[Feature controls and integrations with your tools](/public/clubs/admins-6o6xf/resources/feature-controls-and-integrations-with-your-tools)

Jul 10th, 2025 • Views 9.3K

[Empowering and supporting your team](/public/clubs/admins-6o6xf/resources/empowering-and-supporting-your-team)

Jul 5th, 2025 • Views 19.4K

[Communicating about ChatGPT Enterprise to your team](/public/clubs/admins-6o6xf/resources/team-communication)

Aug 5th, 2025 • Views 13.5K

[Feature controls and integrations with your tools](/public/clubs/admins-6o6xf/resources/feature-controls-and-integrations-with-your-tools)

Jul 10th, 2025 • Views 9.3K

[Planning your ChatGPT rollout](/public/clubs/admins-6o6xf/resources/planning-your-chatgpt-rollout)

Jul 11th, 2025 • Views 7K

# Managing your ChatGPT Enterprise Workspace

<!-- vimeo: 1139733700 | track: English (auto-generated) -->

[▶ Watch on Vimeo](https://vimeo.com/1139733700)

<details>
<summary>자막: Managing your ChatGPT Enterprise Workspace</summary>

You'll get to workspace settings by clicking on your name and then workspace settings. You'll first see some more general settings like your workspace name and id, and you can click into the member tab to see who is active in your workspace and what their role is. Take a look at our help center to learn more about the permissions of members, admins and owners as you're assigning them. Moving back into the general section one setting you might wanna customize early in your setup is your workspace policy, which allows you to set a text that pops up for new users when they log into chat GBT for the first time. Know that this doesn't enforce a policy within chat GBT, but it can be a great way to share information about how your users should be using chat, GBT and any specific AI policies that your company has set. You'll also need to decide how people are going to access chat GBT. We have a lot of great resources in the OpenAI help center that walk you through the different identity and provisioning patterns that you might choose to set up for your workspace. So we recommend taking a really careful deep dive into that documentation so that you're setting your users up for success right away. You can also access your billing in this demo example. We don't have billing set up, but this is where you'll see what plan you're on and any past invoices. The members tab is where you'll manage access to your workspace. So here's where you can see all of the users that already have accounts. You can invite new users directly via CSV or via email address. And we also recommend you check your pending invites and clear those out as often as possible. These are users who have been invited to the workspace but haven't accepted the invite yet, so you can either revoke their invite or resend it from this dashboard. It can be helpful to also organize those users into groups. Many customers choose to create groups for each department and groups can be a really great way to do some more department level analytics or to control access to certain features, which we will show in a little bit. Uh, but here's how you would add users to a group and you can also add them in bulk, manage the group by editing or deleting it. And so we recommend really taking some time and thinking about the way that you want to organize users within your workspace. Both admins and owners have access to user analytics for the workspace, so you'll see a general overview and you can also filter by group. So if you've set up those department level groups, this is a great way to show department level analytics. You'll also see a breakdown by users and you can dig into specific features like GPTs or projects. I also love this AI power users. You can see who your real champions and power users are with just that one click. So we recommend taking some time to go through this dashboard and you can also export it as a CSV. So if you want to combine this with any other internal data you have, uh, that's a great option for you. We recommend using chat GBT to do your analysis and summary. You can always dig into more details about what all of the different analytics mean in our help center. Both admins and owners can control access to apps and connectors which allow you to connect chacha BT to other tools. You can also manage access to these via role-based access controls, which we'll show you in a bit. And then the GPTs tab shows all of the GPTs that are active within your organization. And you'll also see some controls around GBT actions and what third party APIs A GBT action can call The permissions enrolls tab is where you will configure the baseline permissions for your workspace. So there are several different features and functionality that you can toggle on or off. Here you'll see the early access period section, and this is where you'll see features that we are releasing early for you to be able to control whether or not they're on for your workspace, but they intend to move out of early access period and into the default experience. So we recommend going through all of these specific settings and determining what permissions you want the default experience for a user of your workspace to have. Each of these will also link to help center articles so you can learn more about the specific feature. So definitely take some time, go through this carefully and understand what you want the experience of a default user to have. Many companies want to have more control over which users have access to which features, so that's where custom roles comes into play. Now let's take a step back and look at the relationship between custom roles users and groups. So this is what the standard experience of Chacha BT looks like. You'll have a set of users, some of them are just general members of the workspace, some of them have admin privileges, and some of them have owner privileges, which allows them to control more workspace wide settings. But all of these people are also users of JGBT. And if you don't do anything to your permissions tab, everybody will have the same default permissions across the workspace. Now, let's say you want to put people into groups, which is going to be critical for role-based access control. So you may choose to put people into groups like marketing, engineering, IT or security, something that delineates them and tells you more about what type of user they are. Again, if you don't do anything, all of these groups will still have the same default permissions. Now, let's say you want some of those groups to have access to certain features and to limit access of those features to other groups. Let's go into the interface and show how to set up role-based access control. I'll start by creating groups. So I've already created these, but I've essentially just put specific users into specific groups so that I can organize them more clearly into roles. And then I'll head over to permissions and roles. Again, these are the default workspace roles, but I can also have custom roles. So I will create a role called technical users, and I might have some description that reminds me what that role can and can't do. Now I am in the technical user's role, which is different than the default experience, and I can set specific permissions just for this role. So I might want this role to have access to codex or access to specific connectors. And if I turn on connector access, I can also configure access to specific connectors. So there's a lot of layers of control that you have with role-based access controls. And I can pop into here and edit the specific connectors that I want this role to have access to. Now, within this custom role, I also need to assign people or groups to this role. So I'll go over to role assignments, and then I'm going to add in those groups that I already created. So remember, a group is made up of members, and then you assign that group to a specific role. So think of roles like what you can do and groups like what type of user you are. And I can always go back and change the role permissions for specific groups if I want to make an an update or if OpenAI releases new functionality that I want to limit or grant access to. So in that example that I just showed you, I want marketing to have the default permission. So I'm not going to assign that group a role, but I want engineering and executives or IT to have access to codex and specific connectors. So I assigned those groups to that technical role. So first step, create groups of users. Second, create a custom role within your roles and permissions tab. Third, go through and update the permissions that you want that role to have. And then lastly, assign groups to that role. You can review the roles and groups a member has been assigned to from your members tab by just clicking on their name. And then you'll see groups and custom roles, and you can click into that roll to see more of the roll permissions. Now you can expect this admin interface to change as the product evolves, so we recommend that you just continue to keep up to date with new features and functionality and ensure that the right people are assigned to the right permissions and roles to be able to use chat GBT the most effectively. If you have any questions or run into any issues, check out our help center or contact our support team and they'll be happy to help.

</details>

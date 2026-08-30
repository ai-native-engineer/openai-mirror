<!-- source: https://help.openai.com/en/articles/10011769-scim-provisioning-and-management -->

# SCIM provisioning and management

Set up directory sync for your OpenAI tenant or eligible products, manage groups and user access, and resolve common provisioning issues.

System for Cross-domain Identity Management (SCIM) synchronizes users and groups from your identity provider. SCIM manages provisioning; single sign-on (SSO) manages how people authenticate. You can configure SCIM independently of SSO.

# Check availability and choose a provisioning scope

Your options depend on your products, plan, existing directory connections, and administrator role.

| **SCIM scope** | **Eligible products or plans** | **Required administrator** | **Where to manage it** |
| --- | --- | --- | --- |
| Tenant-wide | Eligible tenants, including Ads-only tenants; supported product assignments include ChatGPT workspaces and Ads accounts, not API Platform organizations. | global admin | Admin Console. |
| ChatGPT workspace | Eligible ChatGPT Enterprise or Edu workspaces. | workspace owner | The selected workspace. |
| API organization | Eligible API organizations with a supported Custom or Unlimited billing plan. | API organization owner | API Platform. |
| Not available | Standalone ChatGPT Business and ChatGPT for Teachers plans; use another supported onboarding method. | workspace owner or admin | The relevant ChatGPT workspace. |

A standalone ChatGPT Business plan and ChatGPT for Teachers do not include SCIM. Tenant-wide SCIM requires at least one verified domain and an eligible ChatGPT Enterprise workspace, ChatGPT Edu workspace, or Ads account. A Business workspace can be included only when the same tenant also has an eligible ChatGPT Enterprise workspace and the Business workspace is available under Product access. Automatic account creation is separate from SCIM and does not require SSO or synchronize directory users and groups.

For ChatGPT Business workspace setup and plan limits, see: [Setting up single sign-on for ChatGPT Business](https://help.openai.com/articles/11489188).

For employees who already use a personal ChatGPT account, see: [Onboarding employees with existing ChatGPT accounts](https://help.openai.com/articles/10479654).

## Choose tenant-wide or product-level SCIM

Tenant-wide SCIM can provision supported ChatGPT workspaces and Ads accounts. It does not provision API organizations. Existing product-level connections continue to manage one eligible ChatGPT workspace or one eligible API organization.

If your ChatGPT workspace offers a choice:

* **Use SCIM only for this workspace** creates a workspace-specific connection.
* **Keep the option to expand across products** opens tenant-wide setup in Admin Console.

Using Admin Console does not require you to replace an existing product-level SCIM connection. Tenant-wide SCIM cannot be enabled while a linked ChatGPT workspace or API organization has active product-level SCIM. Once tenant-wide SCIM is active, you cannot start a conflicting product-level connection. Coordinate any migration with your OpenAI account team before modifying a working connection. Separate ChatGPT and API product-level connections can coexist when tenant-wide SCIM is not active.

Before changing scopes, review existing users, groups, product assignments, and roles. Coordinate any migration with your OpenAI account team. Do not delete a working connection to clear a setup error.

Tenant-wide SCIM cannot change the email address on an existing OpenAI account, and OpenAI Support cannot make that change manually. If you need to update managed email addresses, use an eligible ChatGPT workspace-level SCIM connection instead. Tenant-wide and workspace-level SCIM cannot be active at the same time, so choose the appropriate setup before enabling directory sync.

# Connect a tenant directory

A global admin can use Admin Console to connect a shared, tenant-wide directory for eligible Enterprise or Edu workspaces and Ads accounts. Before you begin, verify at least one domain for the same tenant. Individual Ads accounts do not have separate SCIM directories. Tenant-wide SCIM cannot change the email address on an existing OpenAI account, and OpenAI Support cannot make that change manually.

1. Sign in to Admin Console as a global admin.
2. Select the correct OpenAI tenant and open **Global settings**.
3. Select **Access**, then open **Directory**.
4. Select **Enable Directory Sync (SCIM)**.
5. Configure the identity-provider application with the values shown for this tenant.
6. Assign one or two clearly named pilot groups or users in your identity provider.
7. Return to **Directory** and confirm that the connection becomes **Active**.

Initial setup can take up to 5 minutes. If setup is incomplete, select **Continue setup**. Select **Cancel setup** only if you intend to discard the unfinished connection.

Review the connection status and recent directory events to check the connection or investigate a missing user or group. To review group assignments, open **Manage directory** and select **Manage product access**.

![Admin Console Directory tab showing an active connection and successful user and group synchronization events, with summaries and processing times.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_W7XB8zTrSryTfbMoy0I4Vw66qS_jwLrpoKxFS-8DBz4/7c7afabd4187b60353c41ba7c207043e/lbas_img_W7XB8zTrSryTfbMoy0I4Vw66qS_jwLrpoKxFS-8DBz4.jpg?q=80&fm=webp&w=1344)

Depending on your identity provider, SSO and SCIM can share one application or require separate applications. Follow the provider-specific instructions, and do not reuse another workspace’s or API organization’s connection values.

Supported integrations can include Okta, Microsoft Entra ID, Google Workspace, PingFederate, OneLogin, and Rippling. Additional custom SCIM or SFTP-based options depend on the integrations available to your tenant.

# Connect a ChatGPT workspace directory

1. Sign in as the workspace owner of an eligible Enterprise or Edu workspace.
2. Open **Workspace settings**, then select **Identity & access**.
3. Find **Directory Sync (SCIM)** and select **Enable Directory Sync**.
4. If a choice appears, select **Use SCIM only for this workspace**.
5. Complete the provider-specific setup and assign the intended users or groups.
6. Confirm that synchronized users or groups appear in the selected workspace.

If the workspace’s directory controls are read-only, select **Cloud Console ↗** when shown and ask a global admin to manage the tenant-wide connection in Admin Console.

# Connect an API organization directory

1. Sign in to the API Platform as an owner of an eligible API organization.
2. Select the correct API organization and open **Identity** settings.
3. Start the available directory-sync setup.
4. Configure the identity-provider application using the values for that API organization.
5. Assign the intended users or groups in your identity provider.
6. Confirm that invited users join the correct API organization.

Manage API organization provisioning in the API Platform. Tenant-wide SCIM in Admin Console does not provision API organizations. If API identity settings are unavailable, ask your API organization owner or OpenAI account team to confirm your eligibility and setup.

API organization members, projects, billing, and API-specific roles remain managed in the API Platform.

API organization SCIM can also synchronize groups from your identity provider. Manage those groups and assign supported API roles in the API Platform.

# Assign synchronized groups and product access

1. In Admin Console, open the tenant’s **Global settings**, then select **Users & groups** > **SCIM** **Groups**.
2. Select the synchronized group.
3. Under **Product access**, select **Configure access** or open the existing assignment.
4. Select a supported ChatGPT workspace or Ads account.
5. Review the resource, existing assignments, and available role information.
6. Select **Save**.
7. Open the selected workspace or Ads account and confirm that the group appears. If a new workspace member is missing, check pending invitations.

Assigning a synchronized group to a ChatGPT workspace creates a corresponding workspace group. If someone is not already a workspace member, OpenAI creates an invitation with the **Member** role.

The person joins the workspace group after accepting the invitation. Depending on workspace settings, the invitation may not generate an email. Existing workspace members keep their current role and seat type.

You can assign the same synchronized group to multiple supported ChatGPT workspaces and Ads accounts. Assign each resource separately; access to one does not grant access to another.

![Admin Console SCIM Groups tab listing synchronized groups, member counts, and product access, with Configure access links for groups without assigned access.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_qPZUjqUJmN034IXx20zTHFgy4vidne4SzZZ1rTGjZ3U/5ccb0729b214ca15906201571615d836/lbas_img_qPZUjqUJmN034IXx20zTHFgy4vidne4SzZZ1rTGjZ3U.jpg?q=80&fm=webp&w=1344)

The **Product access** editor supports ChatGPT workspaces and Ads accounts. It does not assign API organizations, the ChatGPT workspace owner role, or custom ChatGPT workspace roles. Review Ads account roles in the selected advertising account and configure custom roles inside the selected ChatGPT workspace.

![Product access dialog for the Engineering SCIM group, with ChatGPT workspace and Ads account access toggles and Save and Cancel buttons.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_cH5GHiXTDhP5VqZJuX0QIs9I8RVBtNO9-9L9wx5lBFs/142db2ef130727f672682e9c0ddf1b3d/lbas_img_cH5GHiXTDhP5VqZJuX0QIs9I8RVBtNO9-9L9wx5lBFs.jpg?q=80&fm=webp&w=1344)

Review existing permissions before expanding access. A synchronized group may already have access to a ChatGPT workspace or Ads account. Use the least-privileged role required, and ask a global admin to investigate unexpected access.

When you give a synchronized group access to an Ads account through **Product access**, its initial account role is **Member**. Review the account-specific role and use the least-privileged access required.

For Ads-specific permissions, see: [Managing identity and access for Ads Manager](https://help.openai.com/articles/20001273).

# Manage user records, invitations, and groups

A synchronized directory record does not automatically grant access to every ChatGPT workspace, API organization, or Ads account. Product membership, group assignment, sign-in policy, and product-specific roles still apply.

## Match existing users and understand email-change limitations

Provisioning matches an existing OpenAI account using its configured work email. Confirm that the identity-provider email, invitation address, and intended OpenAI account identify the same person. Configure your identity provider to send exactly one primary email address for each user.

Tenant-wide SCIM cannot change the email address on an existing OpenAI account, and OpenAI Support cannot make that change manually. An eligible ChatGPT workspace-level SCIM connection may update an accepted, SCIM-managed member’s email when email changes are enabled for that workspace. Both the old and new email domains must be verified for the same workspace and its tenant, the new address must not be linked to another OpenAI account, and the SSO mapping must use the updated address. Update the existing SCIM user and test one account first.

If a synchronized invitation uses an outdated email address, do not delete the account, remove and recreate the directory record, invite the new address as a replacement, or disconnect the directory. These actions can create a separate OpenAI account and leave existing projects, agents, and conversation history attached to the original account. Confirm the directory configuration and contact OpenAI Support before making changes. OpenAI Support cannot manually change the email address of an account managed through tenant-wide SCIM.

If an existing tenant user or tenant group matches a synchronized directory record, it can become managed by your identity provider. Existing manually created ChatGPT workspace invitations, memberships, and groups do not automatically become SCIM-managed.

An existing workspace member can join a synchronized workspace group without changing their existing membership, role, or seat type. Remove manually granted workspace access separately when offboarding.

## Understand invitations and automatic account creation

A newly provisioned ChatGPT or API user may need to accept an invitation before joining the product. Some SCIM flows create a pending invitation without sending an email. An existing ChatGPT workspace member does not receive another workspace invitation when the matching tenant user becomes SCIM-managed.

Ask a workspace owner to review pending invitations. For a manual invitation, the owner can select **Resend invite**, where available. SCIM-managed invitations cannot be resent directly; an API may return 409 scim\_managed\_resource. If **Invite member** is available, the owner can enter the same email again without changing the existing role or seat type. Contact OpenAI Support if the invitation remains blocked.

Automatic account creation can add eligible ChatGPT users when they sign in with a verified-domain email. It is separate from SCIM and does not require SSO. Avoid enabling automatic account creation and SCIM together. Users created this way may not be SCIM-managed, so removing them from the identity provider may not remove their product access. Review seat use, remove unmanaged users separately, and check every access path during offboarding.

## Manage group ownership, roles, and visibility

Manage synchronized group membership in your identity provider. Workspace admins can maintain separate manually managed groups.

![Groups for Avery Chen dialog listing Engineering and Global admins, with group member counts and a search field.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_1Bd-_Bpc4WqnqrbZTOs3MRd2lIfoA7MVqCSE5dopqYM/bf137b1ee8144bc848e5e66b04135012/lbas_img_1Bd-_Bpc4WqnqrbZTOs3MRd2lIfoA7MVqCSE5dopqYM.jpg?q=80&fm=webp&w=1212)

With tenant-wide SCIM, an existing manually managed ChatGPT workspace group is not adopted when it has the same name as a synchronized group. OpenAI creates a separate synchronized workspace group, so review existing group names before assigning access.

If you rename a synchronized group in your identity provider, its corresponding synchronized workspace group is renamed.

Workspace-level SCIM uses a separate connection. Depending on its configuration, a synchronized group with the same name as a manual workspace group can place that group’s membership under identity-provider control.

Where supported, a workspace owner can use **Permissions & roles** in the selected ChatGPT workspace to assign eligible custom workspace roles. Synchronized groups can also support workspace analytics when available.

Where available, **Discoverable by workspace users** in the workspace’s **Identity & access** settings controls whether SCIM-managed groups appear when people share GPTs or projects. Turning the setting off can hide those groups and remove existing group shares the next time a GPT or project is updated. Changing discoverability does not stop synchronization or remove the group. If the workspace uses tenant-wide SCIM and its identity settings are read-only, this control may be unavailable. Ask your OpenAI account team about supported options.

# Test onboarding and offboarding

1. Add one test user to the intended identity-provider application or assigned group.
2. Wait for a successful synchronization.
3. Confirm that the user appears in the intended tenant or product and receives only the expected role.
4. Remove the user from the provider assignment or provisioning group.
5. Wait for the next successful sync and confirm that group-derived access is removed.
6. Check direct invitations, other groups, and product-specific roles that could preserve separate access.

Removing someone only inside ChatGPT may be temporary if the identity provider still assigns that person. Disabling a user in the provider does not always remove the application assignment. Deprovisioning does not delete the person’s OpenAI account or personal workspace. After a successful sync, confirm that the person is no longer an active workspace member and review the workspace’s seat allocation. If the person remains active, cannot be removed, or cannot regain access after being added back, contact OpenAI Support. Workspace data retention follows the selected workspace’s policy.

# Troubleshoot directory-sync problems

| **Issue** | **What to check** |
| --- | --- |
| Directory setup is missing or blocked | Confirm the plan, administrator role, selected tenant, and whether tenant-wide or product-level SCIM is already active. Coordinate migration before changing a working connection. |
| A user or group does not appear | Check identity-provider application assignments, group-push settings, the selected tenant, recent directory events, and the provider’s normal synchronization interval. |
| A synchronized user cannot access a product | Check the group’s **Product access** assignment, product invitation or membership, required sign-in method, and product-specific role. The editor can assign supported ChatGPT workspaces and Ads accounts; it does not assign API organizations. |
| A removed user still has access | Review the identity-provider assignment, direct invitations, other synchronized or manual groups, and roles in each product. One removed access path does not remove another. If the user is still active after a successful sync and no other access path remains, contact OpenAI Support. Do not disconnect the directory to fix one account. |
| An email update creates an account conflict | If the destination email already belongs to another OpenAI account, stop and contact OpenAI Support. Do not delete either account or create a replacement user. |

Many identity providers synchronize changes every 30 to 40 minutes, while others send updates sooner. There is no general OpenAI control to force an immediate directory sync.

For authentication or sign-in errors, see: [Troubleshooting SSO, workspace access, and domain verification](https://help.openai.com/articles/10489721).

# Remove a directory connection safely

Removing an active tenant-wide directory connection cannot be undone. Existing synchronized users and groups remain in the tenant and become manually managed. Disconnecting does not automatically revoke existing product access.

1. In Admin Console, open the tenant’s **Global settings**.
2. Select **Access**, then open **Directory**.
3. Review the connected provider and affected users, groups, and product assignments.
4. Select **Delete Connection**.
5. Confirm the change only if you intend to stop synchronization.
6. Review the remaining users, groups, product access, and administrator roles.

Removal can take up to 5 minutes. Contact your OpenAI account team before replacing a working connection or moving between product-level and tenant-wide SCIM.

────────────────────────────────────────────────────────────

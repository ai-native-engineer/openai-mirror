<!-- source: https://help.openai.com/en/articles/10479654-onboarding-employees-with-existing-chatgpt-accounts -->

# Onboarding employees with existing ChatGPT accounts

Prepare employees with existing personal, Plus, or Pro ChatGPT accounts to join a company workspace safely.

An employee may already use ChatGPT with the same email address your company plans to invite. Before sending invitations, explain whether joining the workspace could affect that person’s chats, GPTs, or subscription.

# Check existing accounts before sending invitations

Ask whether employees already use a personal, Plus, or Pro ChatGPT account with their company email address. Confirm the exact email address receiving the invitation and the intended company workspace.

Employees should accept the invitation and sign in with that same email address. Creating a replacement account or using a different address can make the expected workspace or existing history appear missing.

If an invitation is missing, ask a workspace owner to check pending invitations and select **Resend invite**, where available. SCIM-managed invitations cannot be resent directly. Verify any unexpected invitation with your IT team before signing in.

One OpenAI account can have separate personal and company workspaces. Joining a company workspace and migrating a personal workspace are different actions.

# Understand what employees will see

![Flowchart of ChatGPT login paths for personal accounts, password sign-in, workspace picker, and SSO redirection](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-7ee9def3fd3b73f5c83a6e66/84de4bc673e17f099dbae65350f27c68/ChatGPT_Login_Flow.png?q=80&fm=webp&w=1302)

The invitation, workspace plan, and sign-in requirements determine whether an employee keeps a separate personal workspace or sees a migration choice.

| **Situation** | **Workspace sign-in** | **Expected experience** |
| --- | --- | --- |
| Invited to an eligible Enterprise or Edu workspace | Single sign-on, when required. | Join the company workspace; an eligible personal account may trigger a migration prompt. |
| Invited to a ChatGPT Business workspace | The workspace’s permitted sign-in method. | Join the Business workspace; admins cannot require a personal workspace to be merged or deleted. |
| No workspace invitation or approved enrollment | The employee’s existing sign-in method. | A personal workspace generally remains separate; sign-in alone does not create workspace membership. |

# Review personal-account migration before continuing

![Screenshot of a ChatGPT Enterprise onboarding flow. The left panel says the user has been added to a ChatGPT Enterprise workspace and offers options to transfer existing chat history and GPTs or export and delete existing chat history. Two callout panels on the right show confirmation dialogs warning that transferring chat history is permanent and cannot be undone, or that deleting chat history is permanent and cannot be undone.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_6nnnkAeaQ6NylO0sGXdv1nvIFi3H4FhbTXSlqsXrcrY/e884da16411405405083a165962c972c/lbas_img_6nnnkAeaQ6NylO0sGXdv1nvIFi3H4FhbTXSlqsXrcrY.png?q=80&fm=webp&w=1344)

When an Enterprise or Edu invitation uses a verified company domain, an employee with an existing personal account under the same email may need to migrate that account before joining. Depending on the available options, the employee can transfer eligible chats and GPTs to the company workspace or export and delete personal data. An invitation using an unverified or external domain generally does not trigger migration.

Changing the email address on a personal account does not necessarily make its previous work email available for a new account or SCIM provisioning. Previous SSO use can also continue to affect access after a verified domain is removed. Contact OpenAI Support before making changes. Do not remove a verified domain or create a replacement account as a workaround.

Where automatic account creation is available for Enterprise or Edu, signing in with a verified company email can trigger the same migration experience. Review affected accounts before enabling it.

Automatic account creation does not reactivate a removed or deactivated workspace membership. If you see “No eligible ChatGPT account found,” ask a workspace owner or admin to confirm your authorization and invite you again.

A user added to the workspace can consume a seat even if their identity-provider access prevents sign-in. If the same verified domain is mapped to multiple workspaces, automatic account creation may invite the person to more than one workspace. Review domain mappings and enabled settings before rollout.

* Chats and data residency: Data-residency requirements may prevent personal chats from transferring to the company workspace. If transfer is unavailable, export important data before starting the migration and confirm that the downloaded file opens. If the export fails, stop and contact OpenAI Support.
* GPTs: Previously shared or published personal GPTs that move into the company workspace can become visible there. A workspace owner can review and update their visibility. GPTs that were private before transfer remain private.
* Subscriptions: An eligible web-billed Plus or Pro subscription may be canceled and refunded through the migration flow shown. A subscription purchased through Apple or Google may require separate cancellation.
* Account history: Confirm which account, chats, and GPTs are affected before accepting a migration prompt.

A completed personal-to-Enterprise account migration **cannot be reversed**. Check the exact account, available choices, and subscription details before proceeding.

After migration, chats and GPTs are subject to the company workspace’s access and retention policies. If an employee leaves or loses workspace access, they may also lose access to that content.

ChatGPT Business admins cannot require someone to merge or delete a personal workspace. If a Business workspace upgrades to Enterprise, the Business workspace itself is not merged; an employee may still receive a separate personal-workspace migration prompt.

# Tell employees what to expect

Before the rollout, tell employees:

* Which email address will receive the invitation.
* Which company workspace to select.
* Which sign-in method to use if the workspace requires SSO.
* Whether a personal-account migration prompt could appear.
* Whom to contact before making decisions about chats, GPTs, or subscriptions.

Do not assume every invitation email, delivery time, or migration prompt can be customized.

# Test your rollout with a small group

Invite a small group that includes employees with existing personal, Plus, or Pro accounts when relevant. Check the invitation, account email, company workspace, sign-in method, migration choices, data-residency restrictions, and subscription guidance before inviting everyone.

For company sign-in, see: [Single sign-on (SSO) setup for OpenAI products](https://help.openai.com/articles/9534785).

For ChatGPT Business workspace sign-in, see: [Setting up single sign-on for ChatGPT Business](https://help.openai.com/articles/11489188).

If you plan to synchronize users from your identity provider, see: [SCIM provisioning and management](https://help.openai.com/articles/10011769).

If a workspace or account history appears missing, see: [Troubleshooting SSO, workspace access, and domain verification](https://help.openai.com/articles/10489721).

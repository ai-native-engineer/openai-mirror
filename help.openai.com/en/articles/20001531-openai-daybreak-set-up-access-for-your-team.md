<!-- source: https://help.openai.com/en/articles/20001531-openai-daybreak-set-up-access-for-your-team -->

# OpenAI Daybreak: Set up access for your team

Enable Daybreak for approved ChatGPT and Codex users and API projects.

Updated: yesterday

Enable Daybreak for approved ChatGPT and Codex users and API projects.

# Before you begin

When OpenAI enables Daybreak access controls for a ChatGPT workspace or API organization, the Daybreak setting is off by default. A workspace owner must configure access for approved groups, and an API organization owner must configure approved projects. This also applies to existing Daybreak workspaces that have opted into migrating to these controls.

Daybreak access is limited to high-trust internal users and authorized internal security work. Do not enable these capabilities for external users, customer-facing products, public-facing automations, or third-party workflows.

Daybreak Blue approval does not include Daybreak Red.

Configure the access path your team uses:

* **ChatGPT and Codex with ChatGPT sign-in:** Manage access through the approved ChatGPT workspace.
* **API and Codex with API-key authentication:** Manage access through the approved API project.

If your team uses both, complete both setups.

# Set up ChatGPT and Codex access

Use a custom role assigned to your approved users or groups. A workspace owner must create and assign roles; see [Managing feature access with role-based access control in ChatGPT](/en/articles/11750701). A workspace owner or administrator can then configure an existing role’s model access through the supported Models control page.

To limit Daybreak access to selected users, keep it off under **Workspace default** and enable it only for the role assigned to those users.

1. In the approved workspace, open [**Admin Console > Models**](https://chatgpt.com/admin/models).
2. Open **Workspace default**. If you want to enable Cybersecurity for all workspace users, skip this step. Otherwise, under **Cybersecurity**, ensure **Daybreak Red** and **Blue** are off if it is enabled.
3. Select **Save changes**.
4. Open **Roles**. For the intended role, choose **Edit override**, or choose **Add role override** to create an override.
5. Under **Cybersecurity**, set **Daybreak Blue** to **On**. Enable **Daybreak Red** only if it is approved for the workspace and users in the selected role are authorized to use it.
6. Select **Save**. Changes may take up to about 10 minutes to take effect.
7. Reopen Workspace default and the role. Check the saved settings and the role’s assigned users or groups.

To check the Daybreak status of a user, in [Admin Console > Models > Test](/en/articles/11165333), search for an approved member by name or email and check their saved model permissions. Check for a member who should and a member who should not have access.. Review all direct and group roles: another role can grant access even if one role is set to **Off**. Then, test the intended access path with the approved user. Saved permissions alone do not verify that a model request will succeed. If actual access differs from the saved settings, also check any separately provisioned access.

# Set up API project access

You must be an API organization owner to configure Daybreak access. Being a project owner alone does not give you permission to change these settings.

1. Open the approved organization in the [API Platform](https://platform.openai.com).
2. Create or select a non-default project for your team’s approved internal cybersecurity work. Default projects cannot enable Daybreak.
3. Open **Project settings > General > Daybreak model access**.
4. Turn on each Daybreak access level approved for this project. **Daybreak Red** is available only if your organization is approved for it.
5. Select **Save**. Changes can take up to about 30 minutes to take effect.
6. Add the approved users to the project.
7. Use an API key from the enabled project for API requests or Codex API-key authentication. If you migrated to another organization or project, create or select a key in the destination project and update the applications or workflows that use it.

![Daybreak Project Settings](https://images.ctfassets.net/j22is2dtoxu1/3o4YyNyeotY55RCkDN98Ng/f6c916bedef86e323ba75a28e0527a78/8398024c-1a6c-4b98-9e95-6caaf0d73ea9.png?q=80&fm=webp&w=1344)

*Example: Daybreak Blue is off in Project settings > General > Daybreak model access.*

Repeat these steps for each project that needs access. Enabling Daybreak in one project does not enable it in other projects or configure ChatGPT/Codex workspace access.

If you migrated from a dedicated Cyber organization, API keys from the dedicated Cyber organization do not transfer to the new Organization. Create keys in the approved destination project and update the applications or workflows that use them.

# Check access after setup

Allow time for saved changes to take effect, then refresh the client. Follow the [access check in Enterprise Daybreak onboarding](/en/articles/20001261-enterprise-daybreak-onboarding) to test the intended workspace or API project with the approved users and models.

If Daybreak controls are missing or access does not work as expected:

* Check that you selected the organization, workspace, or project named in your provisioning or migration confirmation.
* Check the administrator’s role. For ChatGPT, open [Workspace settings > Members](/en/articles/8266401). Workspace owners manage defaults and custom-role assignments. For the API, select the correct organization in [API Platform settings > People > Members > Roles](/en/articles/4936812) and confirm Owner.
* For ChatGPT and Codex sign-in, review the user’s group membership, role assignments, and saved model settings.
* For API-key authentication, check that the key belongs to the enabled project.

If the issue continues, [contact OpenAI Support](/en/articles/6614161-how-can-i-contact-support) with the organization or workspace ID, project ID if applicable, affected product, Daybreak access level, saved settings, and any error message. Do not include API keys.

Daybreak does not remove all safeguards. A refusal alone does not mean access is missing.

<!-- source: https://help.openai.com/en/articles/20001532-openai-daybreak-migration-org-consolidation-guide -->

# OpenAI Daybreak Migration & Org consolidation Guide

Updated: 8 hours ago

## Introducing Daybreak access controls

OpenAI is introducing access controls for Daybreak (formerly known as Trusted Access for Cyber) capabilities across API and Codex. These controls allow admins to decide which projects or users are eligible to use Daybreak, and allow authorized users to decide when Daybreak capabilities are applied to specific API requests or Codex tasks.

For API, Cyber model access can now be scoped at the **project level**. Your org admin can create or select a dedicated project for Cyber work, enable Daybreak for that project, and add only the users who need access. Authorized users can then choose when Daybreak capabilities are applied to a request by passing the optional `access\_programs.cyber` parameter (more details [here](https://developers.openai.com/api/docs/guides/daybreak)). This lets you keep Cyber work separated from other API activity, including external use cases, while still managing it inside your primary org.

For ChatGPT and Codex, OpenAI is also introducing **user-level Cyber model access controls** for both Daybreak Blue and Red. Once available, workspace admins will be able to choose which users in the primary workspace can access different Daybreak tiers, instead of needing to maintain a separate Cyber-only workspace. Authorized users can then choose when Daybreak capabilities are applied by turning on the “Daybreak” toggle in the Advanced model picker.

Together, these controls let you centralize administration, billing, and governance in your primary org while limiting Cyber access to the right projects, users, and use cases. Note that API key authentication for Codex does not support the same user-level controls today - however API keys can still be governed through the API project-level access controls.

## Start using access controls

**If your team currently uses Daybreak capabilities in your** **primary** **API org and ChatGPT/Codex workspace**:

* All users within your org / workspace can continue to have access to Daybreak capabilities on your mainline models (as they do now), but migration steps may be required.
* When you’re ready to move to access controls, please request this from your OpenAI representative or [support@openai.com](mailto:support@openai.com).
* OpenAI will then provision your API org and ChatGPT/Codex workspace with project-level and user-level access controls.
* Note that these controls are provisioned default OFF. Once enabled, projects and users will not have Daybreak access until your admins explicitly configure access. Please request this change only when you’re ready to move Daybreak access to this default-off model.  Detailed instructions are below.

**If your team currently uses Daybreak capabilities in a** **separate** **API org and ChatGPT/Codex workspace,** our team will work with you to migrate towards your primary org (see instructions below). Migrating to your primary org gives you:

* **Stronger access control:** Manage Cyber model access through role-based access controls, including project-level controls for API usage and user-level controls for ChatGPT/Codex.
* **Cleaner billing and spend limits:** Usage can flow through your primary commercial setup instead of being split across multiple invoices, and will allow usage to inherit the same rates, burn down from the same commits, and be subject to API spend limits.
* **Project-based administration:** Admins can use Projects to separate Cyber work from other workstreams while keeping governance centralized within the same API organization.
* **Simpler operations:** Reduce duplicated users, workspaces, billing settings, and admin overhead.

Once migration is complete, your team will use Daybreak capabilities in your primary org, and your previous dedicated Cyber org or workspace will be deactivated. Note that if your primary API org has a chatGPT/Codex workspace associated with it, that workspace will also have Daybreak access - similar to the API org, this will be default OFF until admins configure it for desired users. If you absolutely need to maintain a separate API org and ChatGPT/Codex workspace, please coordinate with your OpenAI team.

## Migration process overview

Migrating to your primary org will require the following steps:

1. **Customer: Confirm your target setup**

   * Identify the primary OpenAI API organization, and if applicable the primary ChatGPT/Codex workspace, where your team should use Daybreak capabilities going forward.
2. **Customer: Complete user and workflow migration**

   * Add the relevant users to the primary org/project and migrate any needed workflows, applications, API keys, or operational dependencies from the dedicated Cyber org. See below for a [migration check list](/en/articles/20001532-openai-daybreak-migration-org-consolidation-guide#migration-check-list) and the [Admin plugin](https://openai.com/index/introducing-admin-plugin/) for automated support with migration.
3. **Customer: Submit the migration request to OpenAI**

   * Once your team has completed the checklist below, notify your OpenAI account team (or [support@openai.com](mailto:support@openai.com)) that you are ready for OpenAI to process the migration. In your migration request, please include the org ID that you would like to configure access controls on, and secondary org IDs that you will be migrating away from.
4. **OpenAI: Configures the primary org**

   * OpenAI will enable the appropriate Cyber model access and project-level controls on your primary org.
5. **Customer: Complete final configuration**

   Your org admin can then enable Cyber access for relevant projects within the primary API organization or users within the ChatGPT/Codex workspace, save the configuration, and add the appropriate users to that project or workspace as needed. Note that a org admin must complete this action, as project admins and users are not able to configure these settings.

   * For the API and API Key Authentication for Codex:

     + Navigate to Project Settings > General > Daybreak model access. Find the Daybreak Blue toggle.  If your org is approved for Daybreak Red, you’ll see an additional toggle. The toggles are off by default, meaning the project does not yet have access. Turn on the toggle for the Daybreak tier you want to enable. Access is isolated per project; enabling or disabling a Daybreak toggle for one project has no effect on any other project. Note that **it may take up to ~15 minutes for the API access change to come into effect once you click Save.**
   * For ChatGPT/Codex:

     + **Switch on access for the full workspace:** Open the intended workspace in Admin Console > Models > Workspace default. In Models > Cybersecurity, turn Daybreak Blue on. Enable Daybreak Red only when intended and eligible.Click Save changes.
     + **Switch on access for a specific user:** Open Models > Roles. For the intended role, open its action menu and choose Edit override. Use Add role override for a new override. In Models > Cybersecurity, select On for Daybreak Blue and, optionally, Daybreak Red. Click Save.“Models” > Save. Note that **it may take up to ~10 minutes for the Codex sign in with ChatGPT access change to come into effect once you click Save.**
   * If you previously requested user access via Codex sign in with ChatGPT, please reconfigure access to these users in the primary ChatGPT/Codex workspace to avoid disruption when we revoke the dedicated workspace in step #7.
6. **Customer: Revoke all API keys in your dedicated Cyber org**

   * Ensure that all API keys have been revoked in your dedicated Cyber org by checking API keys in your organization settings [here](https://platform.openai.com/settings/organization/api-keys?project_id=proj_dziJJKa3H9L91zNKiTTbrDFk) (they should all be inactive). **Note that any non-revoked keys will be archived** when OpenAI deactivates the dedicated Cyber org / workspace.
7. **OpenAI: deactivate the dedicated Cyber org or workspace after a 14-day grace period.**

   * To ensure you have time to migrate and validate workflows in the primary org, OpenAI will wait 14 days and then deactivate the dedicated Cyber org or workspace that was previously provisioned. If you previously requested user access via Codex sign in with ChatGPT and have not yet reconfigured their access within the primary workspace, these users will lose access at this time.  If users were provisioned access on an individual basis, they will lose access upon migrating as well.

## Migration check list

Before asking OpenAI to process the migration, please confirm the following:

* You have identified the **primary API org ID** **and ChatGPT/Codex workspace ID** you want to migrate Daybreak capabilities into.
* You have identified the **dedicated Cyber API org ID and ChatGPT/Codex workspace ID** that should be deactivated after migration.
* You have confirmed that Cyber model access will only be enabled for **approved internal use cases and users** within your primary API org ID and ChatGPT/Codex workspace. External use is allowed on the same org or workspace, but projects with external use and external users cannot have access to Daybreak capabilities.
* You have **migrated required users, workflows, API keys, applications, and operational dependencies** off the dedicated Cyber org. These include:

  + User Accounts
  + GPTs
  + Projects
  + Workspace Admin settings (SCIM, user groups, workspace icon, analytics & metrics).
  + Shared conversations
  + Data retention timings
  + Compliance API logs
  + Canvases
  + Library content
  + Connector config & connector data
  + Codex tasks, history, and configs
  + Workspace agents and Skills
* You have ensured that all **API keys** in your dedicated Cyber org have been properly revoked - once you request migration, **OpenAI will deactivate your dedicated Cyber org and active** **API keys on the org will be revoked**.
* Your org admin is ready to enable **Trusted Access for Cyber** in the approved project after OpenAI completes provisioning.
* You are ready for **OpenAI to deactivate the dedicated Cyber org or workspace.**

Once all items are complete, send your OpenAI account team the relevant org or workspace IDs and confirm that you are ready for OpenAI to process the migration.

## FAQs

### **Why is OpenAI asking us to migrate to our primary org?**

Migrating lets you manage Daybreak access, users, billing, and governance in one place. It also reduces duplicated users, workspaces, billing settings, API keys, and admin overhead.

### **Can we keep Cyber work separate from other API activity?**

Yes. Your org admin can create or select a dedicated project for Cyber work, enable Trusted Access for Cyber for that project, and add only the users who need access.

### **Can we use the same primary org for both internal Cyber work and external use cases?**

Yes, but Daybreak capabilities should only be enabled for approved internal use cases, and cyber models must be used only within projects dedicated for internal cyber use cases. Projects with external use cases, or external users, should not have access to Daybreak capabilities.

### **What are approved internal use cases?**

Daybreak approval extends to personnel employed by or working for the approved customer. Access to Daybreak models and capabilities cannot be extended to third parties. Approved use cases include security research, red-team evaluation, threat analysis, vulnerability assessment, defensive testing, secure code review, incident investigation, and other security work performed by your organization’s internal teams. Daybreak capabilities should not be used for customer-facing products, third-party access, or public-facing automations unless with explicit approval from OpenAI’s Daybreak Partner Program.

### **What happens to our dedicated Cyber org or workspace after migration?**

Once migration is complete, OpenAI will deactivate the dedicated Cyber org or workspace and remove legacy org-level Cyber access.

### **Will OpenAI deactivate our dedicated Cyber org before we are ready?**

No. You should only ask OpenAI to process the migration after you have moved the required users, workflows, API keys, applications, and operational dependencies to your primary org or workspace.

### **Will my existing API keys continue to work?**

API keys created in your dedicated Cyber org will not carry over to your primary org. Before migration, create new API keys in the approved project within your primary org and update any applications, scripts, or workflows that rely on the old keys. Existing API keys in your dedicated cyber API org will need to be revoked as part of this migration. Once the dedicated Cyber org is deactivated, keys from that org will no longer work.

### **What information do we need to send to OpenAI?**

Send your OpenAI account team the primary API org ID and ChatGPT/Codex workspace ID you want to migrate into, plus the dedicated Cyber API org ID or workspace ID that should be deactivated after migration.

### **Who enables Daybreak after OpenAI provisions the org?**

Your org admin will complete the final setup by enabling Daybreak for the desired API project and adding the appropriate users. For ChatGPT/Codex, workspace admins will manage user-level access once those controls are available.

### **Will migration change our billing?**

The goal is to move Cyber usage into your primary commercial setup so usage is no longer split across separate orgs, invoices, or credit pools.

### **What if we still need a separate org or workspace?**

Work with your OpenAI account team if you believe you have a business, regulatory, data residency, or invoicing requirement that requires a separate org or workspace.

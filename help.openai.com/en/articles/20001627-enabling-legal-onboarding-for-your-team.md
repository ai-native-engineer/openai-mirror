<!-- source: https://help.openai.com/en/articles/20001627-enabling-legal-onboarding-for-your-team -->

# Enabling Legal Onboarding for your team

Make the Legal Onboarding plugin available for a custom role, then confirm that members can install and open it in ChatGPT.

Updated: 8 days ago

Legal Onboarding is a plugin that guides in-house legal teams through getting started with legal workflows in ChatGPT Enterprise. It helps members choose a practice area, discover relevant plugins and legal skills, connect approved tools, and try starter tasks in ChatGPT.

These instructions are for ChatGPT Enterprise workspace admins and owners. You’ll make the plugin available for a custom role, then confirm that members assigned to that role can install and open it.

Legal Onboarding and Astra for Law have separate access requirements. Installing Legal Onboarding does not grant access to Astra for Law or partner tools. Astra for Law eligibility, a separate access agreement, workspace activation, and permissions to use Astra for Law still apply. Partner tools retain their own licensing, access, and permission requirements.

Astra for Law is a model configuration for professional legal research, analysis, and writing. To learn about the model configuration, see: [Astra for Law](https://help.openai.com/articles/20001528).

## Before you begin

Choose a custom role assigned to the members who need access. If you need to create a role or assign it to members or groups, ask a workspace owner.

For setup instructions, see: [Managing feature access with role-based access control in ChatGPT](https://help.openai.com/articles/11750701).

# Enable the plugin for the workspace

1. Open the [**Admin Console**](https://admin.openai.com/).
2. In the sidebar, select **Plugins**.

   ![Plugins selected in the Admin Console sidebar.](https://images.ctfassets.net/j22is2dtoxu1/3scpoT2qiO6P0F1EWjP5CG/04d4f00f10a95aa02f501806e6690a29/20001627-image-01.png?q=80&fm=webp&w=506)
3. Search for **Legal Onboarding**. Open the **Availability** menu and select **Customize by role**.

# Enable the plugin for a role

1. Open the [**Admin Console**](https://admin.openai.com/) and select the intended ChatGPT workspace.
2. In the sidebar, select **Plugins**.

   ![Plugins selected in the Admin Console sidebar.](https://images.ctfassets.net/j22is2dtoxu1/3scpoT2qiO6P0F1EWjP5CG/04d4f00f10a95aa02f501806e6690a29/20001627-image-01.png?q=80&fm=webp&w=506)
3. Search for **Legal Onboarding**. Open the **Availability** menu and select **Customize by role**.

   ![Legal Onboarding availability menu with Customize by role highlighted.](https://images.ctfassets.net/j22is2dtoxu1/5I3mNZpNN6HylMq8GAlR6Z/b92079f8197e44b41ff693b2973a61b4/20001627-image-02.png?q=80&fm=webp&w=1344)
4. Under **Change availability for**, select the role you want to update. Set availability to **Available for installation for role**, then save your changes.

   ![Plugin role availability set to Available for installation for role, allowing members to install the plugin.](https://images.ctfassets.net/j22is2dtoxu1/AAghzjAZGa5aJtDd9Idc4/d10d1bbe6fe5d4dc09798ff2988ecd51/role.png?q=80&fm=webp&w=1074)

# Verify access as a member of the updated role

1. Open ChatGPT in the intended workspace as a member assigned to the role you updated. Go to **Plugins**, search for **Legal Onboarding**, and select it.
2. Select **Install plugin** and follow the steps on screen.

   ![Legal Onboarding plugin detail page with the Install plugin button highlighted.](https://images.ctfassets.net/j22is2dtoxu1/6onQ6TNMpygB1nrPjl7kQu/a547018f9cdae5d7fb54fcb51b760e47/install.png?q=80&fm=webp&w=1344)
3. Select [**Open plugin**](https://chatgpt.com/mcp-app/connector_openai_chatgpt_for_law/law.open). The welcome screen confirms that this account can open Legal Onboarding.

   Access to Legal Onboarding does not confirm access to Astra for Law.

   ![Welcome to ChatGPT onboarding for lawyers, with Get started and Skip to starter tasks options.](https://images.ctfassets.net/j22is2dtoxu1/4fF7d50FKRgJdTFL2QhRMJ/66ac3b75b04a63fbe5deca1a252b1229/welcome.png?q=80&fm=webp&w=1212)

# Open the plugin from a chat

In ChatGPT, mention **@Legal Onboarding** and ask it to open the plugin.

# Troubleshooting

If a member cannot find or open the plugin:

* Confirm that the member is in the correct workspace and has the role you updated.
* In [**Admin Console**](https://admin.openai.com)[,](https://admin.openai.com) check that the role’s plugin availability is **Available for installation for role**.
* Allow up to 5 minutes for recent role changes to take effect, then ask the member to refresh and try again.
* If the Legal Onboarding screen shows **Install plugin**, ask the member to select it and follow the steps on screen, then select **Open plugin**. If installation is unavailable or fails, contact OpenAI Support.

If the issue continues, contact OpenAI Support. Include the workspace name or ID, affected account email, failed step, error message, and the date, time, and time zone. Remove confidential client information and other sensitive content from screenshots.

For contact instructions, see: [How can I contact support?](https://help.openai.com/articles/6614161)

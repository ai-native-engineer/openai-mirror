<!-- source: https://help.openai.com/en/articles/20001490-using-the-epic-plugin-with-chatgpt-and-codex -->

# Using the Epic plugin with ChatGPT and Codex

Learn how to set up the Epic plugin, connect an Epic account, and review authorized patient information in ChatGPT and Codex.

Updated: 4 days ago

Epic is a plugin for ChatGPT and Codex that connects an approved organizational workspace to its Epic electronic health record through the required EHR app. Clinicians can review patient information they already have permission to access, including clinical notes, medications, conditions, encounters, and laboratory results.

The connection is currently read-only. It cannot update medical records, place orders, message patients, or override existing patient-chart permissions. Clinicians remain responsible for reviewing the underlying record and making care decisions.

## Availability

Epic is available in ChatGPT and Codex for approved [ChatGPT for Healthcare](https://help.openai.com/articles/20001046) and HIPAA-enabled Enterprise workspaces. Availability depends on your organization’s rollout, workspace settings, and Epic configuration.

Epic is not available with individual [ChatGPT for Clinicians](https://help.openai.com/articles/20001202) accounts. If you do not see the plugin, ask your workspace administrator whether your organization has access.

## Compare Epic and Healthcare Public Data

Epic and Healthcare Public Data are separate plugins available in ChatGPT and Codex. They have different data sources and setup requirements:

* **Epic** retrieves patient information from your organization’s Epic records. It requires the EHR app, organization-specific configuration, and each user’s own Epic sign-in.
* **Healthcare Public Data** searches public healthcare sources, including medical research, clinical trials, medication information, and Medicare data. It does not access patient charts.

For public healthcare sources and setup instructions, see: [Using Healthcare Public Data in ChatGPT and Codex](https://help.openai.com/articles/20001489).

# Set up the Epic plugin for your organization

Setting up the Epic plugin requires configuration specific to your organization’s Epic environment and coordination with your Epic administrator. Before you begin, contact your OpenAI account team. They can guide you through the setup requirements needed to support your organization’s configuration.

Your workspace administrator and Epic administrator will need to configure the required EHR app, including your organization’s connection details, authentication settings, and approved permissions, before users can access patient information. After setup is complete, each user must connect their own Epic account. Installing the plugin does not complete this connection or change the user’s existing Epic permissions.

Configuring the EHR app and installing the plugin do not connect anyone’s Epic account. Each user must connect their own account before accessing patient information, even if an administrator has already installed the plugin for them. The integration uses the access granted to that user’s connected Epic account and does not expand their existing Epic permissions.

## Administrator setup

Follow the steps below if you are a workspace [**owner**](https://help.openai.com/articles/8266431) [or](https://help.openai.com/articles/8266431) [**admin**](https://help.openai.com/articles/8266431) to setup the plugin, once you have contacted your OpenAI contact for any necessary pre-config steps.

The Epic plugin includes the **Epic app template**, which administrators can use to customize EHR apps for their workspace. Administrators must first configure and publish the Epic app template, and set up the plugin for their workspace. Clinicians then install the plugin, and connect their own Epic accounts to start using the plugin.

Read about [apps](https://help.openai.com/articles/11487775), [app templates](https://help.openai.com/articles/20001247), and [plugins](https://help.openai.com/articles/20001256) for background.

### Create, configure, and publish the EHR app

1. Confirm that your organization has been approved for the Epic integration and that your ChatGPT for Healthcare or eligible Enterprise workspace is authorized to handle protected health information under an applicable Business Associate Agreement.
2. Work with your organization’s Epic administrator to register or approve an OAuth application for the appropriate Epic environment. Obtain your organization’s:

   1. FHIR R4 base URL,
   2. OAuth client ID
   3. OAuth client secret.
3. In ChatGPT, go to **Workspace settings > Apps**, and click on **Directory.** Search for **Epic**.
4. Click on **Epic app** template. This leads you to the setup needed for creating a workspace-specific EHR app.
5. In the setup screen that appears, enter your organization’s **FHIR Base URL**. Copy the **Callback URL** displayed during setup and register that exact URL as an authorized redirect URI in your organization’s Epic OAuth application.
6. Enter the **OAuth client ID** and **OAuth client secret**. Review the prepopulated scopes with your Epic administrator and confirm that they match the permissions approved for your organization’s Epic application. Review the common OAuth scopes listed in the section below.
7. Select **Create draft**. Review the app’s configuration, role access, and actions, then select **Publish** to publish the app to your workspace.

### Configure the Epic plugin

1. Go to **Workspace settings > Plugins**, select **Epic**, and choose **Available** or **Installed** for the appropriate users or roles. In either case, each user must connect their own Epic account through the EHR app before accessing patient records. Their existing Epic permissions still apply.

   * **Available**: Choose this if you want users to install the Epic plugin themselves.
   * **Installed**: Choose this if you want the Epic plugin installed automatically for those users.
2. Confirm that each clinician can sign in using their own Epic account and access only the patient records permitted by their existing Epic credentials.
3. See [Connect your Epic account](https://help.openai.com/articles/20001490#connect-your-epic-account), for how clinicians can connect their accounts.

## Common OAuth scopes

The scopes below provide a starting point for configuring sign-in and read-only access to patient information.

`openid`
`fhirUser`
`offline_access`
`user/Patient.read`
`user/Condition.read`
`user/AllergyIntolerance.read`
`user/MedicationRequest.read`
`user/MedicationDispense.read`
`user/Observation.read`
`user/DocumentReference.read`
`user/Binary.read`
`user/DiagnosticReport.read`
`user/Encounter.read`

Additional scopes may be needed for other approved resources, such as appointments, procedures, immunizations, or care plans.

**Note:** The EHR app derives its authorization and token endpoints from the configured FHIR base URL. If your Epic environment uses a nonstandard configuration or sign-in fails, contact your Epic administrator and OpenAI account team.

If ChatGPT displays **Before you continue**, review the healthcare warning and your organization’s requirements. If the integration is approved, select **I understand and accept these risks.** Then select **Continue**. Acknowledging this warning does not establish BAA coverage.

For more information about workspace controls, see: [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

# Connect your Epic account

After your administrator configures access:

1. In ChatGPT or Codex, open the **Plugin directory** and select **Epic**.
2. Select **Install plugin**. If your administrator already installed it for you, continue to the next step.
3. If prompted, select **Connect** next to **Epic EHR**, then sign in with your own Epic account. If Codex directs you to ChatGPT to finish authorization, complete the connection there and return to Codex.
4. In ChatGPT, select **Try in chat** if it appears, or start a new conversation. In Codex, start a new task.

Enter your Epic credentials only in your organization’s sign-in flow. Do not share passwords, OAuth client secrets, or access tokens in a chat or Codex task.

# Work with authorized patient information

After connecting your account, you can ask about patient records you are authorized to access. Examples include:

* Summarize the recent clinical history for patient [authorized MRN or patient full name].
* List recent medications, conditions, and laboratory results for patient [authorized MRN or patient full name].
* What has changed since patient [authorized MRN]’s previous visit?

Available information depends on your organization’s Epic configuration, approved resources, and your existing patient permissions. Review the source record and relevant dates before relying on a response.

# Protect patient information

Patient records may include protected health information (PHI). Before using Epic with PHI, confirm that your organization has an applicable Business Associate Agreement (BAA), appropriate Epic authorization, an approved workspace configuration, approval to handle patient information in the product you’re using, and any other agreements required for your intended use.

An enabled plugin, connected app, or accepted warning does not automatically mean that every product, service, or workflow is covered by your BAA. Use only the patient information needed for the task and follow your organization’s policies.

Do not send patient information, passwords, or access tokens to Support.

For information about eligible products and configurations, see: [HIPAA Eligible Products and Functionality](https://help.openai.com/articles/20001069).

# Resolve access and connection issues

* **Epic plugin is missing:** Ask your workspace administrator whether your organization is approved and whether the plugin is available to your account in ChatGPT or Codex.
* **EHR app is unavailable:** Your administrator may need to configure the required app, enable it, or update your role permissions.
* **Your Epic sign-in fails or expires:** Sign in again with your own Epic account. If the problem continues, contact your organization’s Epic administrator.
* **A patient record is missing:** Check your existing Epic permissions. The plugin cannot provide access to charts you are not already allowed to review.
* **You use ChatGPT for Clinicians:** Epic is not available for individual Clinicians accounts. Eligible users may have access to separate public healthcare apps.

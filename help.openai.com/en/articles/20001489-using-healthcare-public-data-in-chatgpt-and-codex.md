<!-- source: https://help.openai.com/en/articles/20001489-using-healthcare-public-data-in-chatgpt-and-codex -->

# Using Healthcare Public Data in ChatGPT and Codex

Learn how to use Healthcare Public Data in ChatGPT and Codex, connect its apps, and search public healthcare sources safely.

Updated: 4 days ago

Healthcare Public Data is a plugin for ChatGPT and Codex that brings together nine read-only apps for searching official public healthcare sources. Use it to find biomedical research, clinical-trial information, medication labels, FDA safety information, Medicare coverage and payment data, healthcare-facility measures, and provider identification records.

The apps search public information. They do not access patient charts or medical records, and they do not require a separate account with the organization that publishes the data.

## Availability

Healthcare Public Data is available in ChatGPT and Codex for supported [ChatGPT for Healthcare](https://help.openai.com/articles/20001046) and HIPAA-enabled Enterprise workspaces. Workspace administrators can manage access to the plugin and its apps.

Eligible U.S. users of [ChatGPT for Clinicians](https://help.openai.com/articles/20001202) can install the Healthcare Public Data plugin and connect the public healthcare apps available to their account.

## Public healthcare sources

### Research and clinical trials

* PubMed — Biomedical research, citations, abstracts, and eligible full-text articles. Review the underlying research before applying it to a clinical question.
* ClinicalTrials.gov — Clinical-trial listings, study locations, recruitment information, and eligibility criteria. Confirm current openings and eligibility with the study team.

### Medications and safety

* DailyMed — Official medication labels, ingredients, packaging information, and drug identifiers. Medication information still requires clinical interpretation.
* RxNorm — Standardized medication names, identifiers, and related drug concepts. It does not establish appropriate dosing, interchangeability, or formulary coverage.
* openFDA — Public FDA safety and regulatory information, including recalls and aggregate data about reported adverse events. The data does not establish that a product caused an event or how often an event occurs.

### Medicare, healthcare facilities, and providers

* CMS Coverage — National and local Medicare coverage information. A public coverage policy does not determine an individual patient’s benefits.
* CMS Open Data — Selected Medicare Part B, Part D, and inpatient hospital payment, prescribing, and utilization data. This source does not include Open Payments, Medicaid, hospice, or dialysis data.
* Medicare Care Compare — Public healthcare-facility information and quality measures. Compare only measures with compatible definitions and reporting periods.
* NPI Registry — Public provider and organization identification records. An NPI does not establish current licensure, provider quality, or Medicare enrollment.

## Set up the plugin and connect apps

### Manage workspace access

Workspace administrators can manage plugin availability separately from access to each included app.

1. Go to **Workspace settings > Plugins** and select **Healthcare Public Data**.
2. Under **Workspace default** or the plugin’s installation policy, choose **Available** to let eligible members install the plugin, or **Installed** to install it for eligible members.

   1. If your workspace uses role-based access control (RBAC), choose **Available** or **Installed** for each eligible role.
3. Go to **Workspace settings > Apps** and open each healthcare app your organization approves.
4. If an app is disabled, select **Enable** when available. Use **User access** to manage which roles can use the app.
5. If a healthcare warning appears, review your organization’s requirements. Select **I understand and accept these risks.** Then select **Continue**.

A plugin can appear available even when its included apps are disabled. Installing the plugin, including through the **Installed** setting, does not automatically connect its apps.

Accepting a healthcare warning does not make an app suitable for protected health information, change your Business Associate Agreement, or expand the app’s approved use.

For general workspace controls, see [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

### Install the plugin

1. In ChatGPT or Codex, open the [Plugin directory](https://chatgpt.com/plugins) and select **Healthcare Public Data**.
2. Select **Install plugin**. If your administrator has already installed the plugin for your role, continue to the next step.
3. If prompted, select **Connect** for each public healthcare app you want to use. If Codex directs you to ChatGPT to finish setup, complete the connection there and return to Codex. If **Connect all** appears, you can use it for the available apps.
4. In ChatGPT, select **Try in chat** if it appears, or start a new conversation. In Codex, start a new task.
5. Ask your question in ChatGPT or Codex. You can also type **@** in ChatGPT or **$** in Codex to choose a connected app to search a specific source.

Each app keeps its own workspace permissions. If an app is unavailable in an organizational workspace, ask an administrator to check that app’s access settings.

For an overview of how plugins and apps work together, see [Plugins in ChatGPT and Codex](https://help.openai.com/articles/20001256) and [Apps in ChatGPT](https://help.openai.com/articles/11487775).

## Protect patient information

Healthcare Public Data apps send searches to public information sources. Do not include protected health information, patient names, dates of birth, medical record numbers, Medicare or member numbers, contact details, or any other patient-identifying information in those searches.

A Business Associate Agreement for your workspace does not, by itself, determine whether an external service is authorized to receive protected health information. Review the applicable agreements, workspace controls, and connected services before using any app with sensitive information.

Healthcare Public Data does not retrieve patient records. Epic is a separate plugin that connects an approved organizational workspace to Epic patient records through the required Epic EHR app. It requires organization-specific setup, an individual Epic sign-in, and existing patient-chart permissions.

For information about eligible products and configurations, see [HIPAA Eligible Products and Functionality](https://help.openai.com/articles/20001069).

## Enterprise reporting and data governance

### Review reporting and compliance coverage

Conversations that use apps are available in the Compliance API, and all app calls are recorded in Compliance Logs. Organizations with specific audit or export requirements should confirm that the available fields meet their requirements.

For existing app-control and logging guidance, see [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

### Check retention and data residency

Public-data requests can be sent to the organization that operates the source. Review your organization’s requirements and the relevant provider’s policies before assuming that workspace retention, deletion, or data-residency settings apply to information sent to that provider.

## Pricing and usage limits

There is no separate charge for Healthcare Public Data or its public-data apps. Your existing plan and workspace usage terms still apply.

Usage depends on the product and plan you’re using. A public data provider may also impose its own limits or become temporarily unavailable.

## FAQ

### Is Healthcare Public Data the same as Epic?

No. Healthcare Public Data searches public healthcare information and does not access patient records. Epic is a separate plugin that retrieves authorized patient-chart information through the Epic EHR app and requires organization setup and an individual Epic sign-in. For setup and access requirements, see: [Using the Epic plugin with ChatGPT and Codex](https://help.openai.com/articles/20001490).

### Does installing the plugin connect all nine apps?

No. Install the plugin, then connect the individual apps you want to use. **Connect all** appears only when that option is available for your eligible apps.

### Do the public healthcare apps require another account?

No. The apps in the plugin do not require separate accounts.

### Can ChatGPT for Clinicians users install the Healthcare Public Data plugin?

Yes. Eligible U.S. users of ChatGPT for Clinicians can install the Healthcare Public Data plugin and connect the public healthcare apps available to their account.

### Why can I see the plugin but not use an app?

Plugin availability and app access are separate. In an organizational workspace, ask your administrator to verify the individual app’s role permissions and availability.

### Why did my search return no results?

The source may not contain a matching public record, or the provider may be temporarily unavailable or limiting requests. Check the source’s scope, adjust the search without adding patient information, and try again later.

Use public healthcare information for research and reference. It does not replace professional medical judgment, an individual benefit determination, or emergency care.

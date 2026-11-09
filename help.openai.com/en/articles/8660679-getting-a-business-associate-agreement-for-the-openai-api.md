<!-- source: https://help.openai.com/en/articles/8660679-getting-a-business-associate-agreement-for-the-openai-api -->

# Getting a Business Associate Agreement for the OpenAI API

Learn how to accept a Business Associate Agreement and enable HIPAA compliance support for your API organization.

Updated: 6 days ago

To use the OpenAI API with protected health information (PHI), your organization must first enter into a Business Associate Agreement (BAA) with OpenAI.

Eligible organizations can accept the standard BAA in the API Platform. Completing the acceptance flow enables HIPAA compliance support for the selected organization.

## Availability

An enterprise agreement is not required to sign a BAA for API services.

Self-serve enrollment requires an established history of API usage.

If the BAA section shows **Not eligible yet**, your organization does not currently meet the self-serve enrollment requirements.

## Before you begin

You must be an organization admin with permission to manage organization settings and authority to accept the agreement on your organization’s behalf.

Review the covered services and configuration requirements before processing PHI. For details, see: [HIPAA eligible products and functionality](https://help.openai.com/articles/20001069).

Once HIPAA compliance support is enabled for your organization, you cannot disable it in the API Platform settings.

Do not include PHI in support requests, screenshots, or attached documents.

# Accept the standard BAA

1. Sign in to the API Platform and select the organization you want to configure.
2. Open **Settings**, then go to [**Organization > General**.](https://platform.openai.com/settings/organization/general)
3. Under **HIPAA compliance support**, select **Enable**.
4. Download and review the Business Associate and Healthcare Addendum.
5. Review the information about HIPAA coverage, including which API services are eligible for PHI.
6. Confirm that you have authority to accept the agreement and that you have reviewed the agreement and understand its coverage.
7. Confirm the organization name and **Organization ID**, then select **Agree and enable**.

When setup is complete, the **HIPAA compliance support** section shows **Active**.

If setup cannot finish, follow the troubleshooting steps below.

# View your agreement

After accepting the standard BAA through the API Platform, select **View agreement** in the **HIPAA compliance support** section to download the standard agreement.

Agreements arranged outside this self-serve flow, including custom BAAs, are not available to download through this setting.

# Troubleshoot HIPAA compliance support

If the organization’s BAA status cannot load, select **Try again**.

If setup could not finish enabling HIPAA support, select **Agree and enable** again to retry.

If the agreement has changed, select **Reload agreement** if shown, download and review the latest agreement, and complete the confirmations again.

If you are not eligible yet to complete the flow in API Platform, try again in a few days or reach out to [baa@openai.com](mailto:baa@openai.com).

# BAAs for ChatGPT

For a BAA for a sales-managed ChatGPT Enterprise or Edu account, [contact sales](https://openai.com/contact-sales). We do not offer a BAA for ChatGPT Business.

Eligible individual clinicians using ChatGPT for Clinicians have a separate in-product BAA flow. For details, see: [ChatGPT for Clinicians](https://help.openai.com/articles/20001202).

# FAQ

## Does accepting a BAA make my application HIPAA compliant?

Accepting a BAA and enabling HIPAA compliance support do not, by themselves, make your application HIPAA compliant. You are responsible for evaluating your use of the services and meeting your compliance obligations. Review the [HIPAA Implementation and Configuration Guide](https://cdn.openai.com/osa/baa-hipaa-guide.pdf) for the requirements that apply to your use case.

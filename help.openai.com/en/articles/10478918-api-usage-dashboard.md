<!-- source: https://help.openai.com/en/articles/10478918-api-usage-dashboard -->

# API Usage Dashboard

Updated: 2 days ago

## Who can view the Usage Dashboard?

Only **Organization Owners**, or users explicitly granted **Usage Dashboard** permission, can access the **Usage Dashboard**.

## Where can I view my credit grants?

The credit grants details table has been unified in the organization Billing page.  
  
You can access them at <https://platform.openai.com/settings/organization/billing/credit-grants>.

## Can I see Scale Tier data in the Usage Dashboard?

Yes. For organizations with Scale Tier enabled and the required access, the dedicated Scale Tier usage detail page is available at <https://platform.openai.com/usage/scale-tier>.

For Scale tier, note that costs of Scale tier bundles are attributed at the Org level, not project

## Can I use the new Usage Dashboard to view Tokens Per Minute (TPM) data?

Yes. Usage data (non billing data) now provides interval selection. Inside the detail pages (), users will be able to select 1 minute data granularity to view TPM for any of the API capabilities.

![Usage dashboard time range set to 1d with Group by menu visible](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-a0d33ba34f6b5e96ff880743/a7368b279e0aa1d383b46a0cdc074cee/AD_4nXeDuazvVMl1aPOYVAIXJb5WQUEihQmt5oYfl5oEZst_qJegrdebxNFfo5MXGLWyZ7HzzQMI4vzhV1fhv1c7QLPKv_yBH-7e3puqdMIJp97Nr6Q0E2ahPz7MRBkc)

## What timezone does the usage dashboard use?

Data in the usage dashboard are displayed using UTC.

## Why are there two project selection drop-downs?

To allow more flexibility for viewing a single, multiple or all project data, the usage page now has its own project selector that works independently of the current project selected in the top right bar. Use the dropdown from the screenshot

![API Usage Dashboard project filter dropdown with AI Test selected](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-8368a436f492bd2880c7bfa3/8505e4eab387f0d5d689bf85f47f9688/AD_4nXdyhIbkHg8crtqlM_hpEROZkqwVh-k03EGZTOo1dtKa7rfGBZzg60Ok_SrfjimPgnjMlTzHrGKjcUgOeiDRZQnCyU-33ti2ZIQftBo10jhRMK70hAuSNy08fjKk)

## How do I see my overall organization data? (For organizations with projects)

To view overall organization data, use the project selector “x” to clear selection. If no projects are selected, it will default to showing all project data.

![API Dashboard with All projects filter, date selector, and Group by set to All](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-9f454ebb7bd83e329a375155/26f6cf066d35c18e4709d5d4b2f967e7/AD_4nXczkDYAfMqaT9hsig7O_8f6tGALWSXkVgbEKk2ImHI-XR55OYXNcWG54f3UonGLSUgDB5sd0LStfiDzKvmEG8Y3ON_XDigpJDldWvIIrv-lk-Pz_IqL29eNQ8ga)

## How can I see my consolidated organization data? (For organizations with sub-orgs)

The Usage Dashboard does not consolidate cost or usage data across organizations.  
  
If you want to view combined cost data, consider migrating from sub-orgs to projects, or using the Usage API for custom analysis.

## How can I view individual sub org data?

All organizations are treated as self contained entities. To view sub org data, you just need to select it in the org selection dropdown like any other organization.

## How much data can I export?

There's no limit on the export time range, but if they request a long time range it may be broken into multiple files.

## My usage for a certain model is >0, but spend for that model is $0

First check if you’re using Scale Tier. Most often, this is a confusion for how Scale Tier costs are attributed.  
  
If all of your usage for a given model is within your Scale Tier TPM, then no costs will be incurred for that project. The Scale Tier subscription cost is always attributed to the Organization.  
  
To see your Scale Tier subscription cost, make sure you don’t have a project filter set, and then select the Spend Categories tab.

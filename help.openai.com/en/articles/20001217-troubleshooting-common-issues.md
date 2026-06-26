<!-- source: https://help.openai.com/en/articles/20001217-troubleshooting-common-issues -->

# Troubleshooting Common Issues

A guide to resolving common setup, launch, measurement, and payment issues in Ads Manager Beta.

Updated: 9 days ago

Use this guide to troubleshoot common issues in Ads Manager Beta. Start with the issue category that best matches your issue, work through the recommended checks, and contact support if the issue persists.

## 1. Onboarding and account setup

### I cannot access Ads Manager

* **Check for verification first:** Confirm the user is signed in with the OpenAI account tied to the organization the ad account is set up with, and the user has been granted access to the correct Ads Manager Beta account
* **Helpful details for support:** User email, account name, screenshot of the error message

### Billing profile or payment method is missing

* **Check first:** Confirm a billing profile has been created, a payment method has been added, and billing settings are correctly configured
* **Helpful details for support:** Account name, screenshot of the billing page, description of the missing or blocked step

### Don’t have permission to create an ad account

* **Check first:** If your company already has an OpenAI tenant, ask your IT team or admin to grant you the Ads Admin role in the OpenAI admin console at <https://admin.openai.com/>. They can do this by going to Users, selecting your user profile, opening Direct roles, clicking +, and assigning Ads Admin
* **Helpful details for support:** Tenant name, screenshot of the error message

## 2. Uploading and launching campaigns

### My campaign upload had an error

* **Check first:** Review the error message as it typically identifies the exact issue. Compare your file against the [Campaign Structure Checklist](https://help.openai.com/articles/20001218) and fix any issues in the template before uploading again
* **Helpful details for support:** The exact file used, the row or object you believe is failing, the error message or screenshot

### My images won’t upload

* **Check first:** Confirm that images are PNG or JPG, square, no larger than 1200 x 1200. Images must also be publicly accessible and open directly to the image in the browser. Accepted image hosting options include publicly available Google Drive links, AWS-hosted image links such as S3 or CloudFront, and self-hosted image links on the advertiser’s domain or CDN
* **Helpful details for support:** Account name, campaign name, ad title associated with the image, image URL

### My ad was rejected

* **Check first:** In the Ads tab of Ads Manager Beta, review the ad **‘Status’**. If the status is **‘Not serving’**, hover over the ad to view the reason. Common causes include ad copy or landing pages that do not align with our [Ad Policies](https://openai.com/policies/ad-policies/), or landing pages that block [OpenAI user agents](https://developers.openai.com/api/docs/bots) or IP addresses. If this happens, you can edit the ad and resubmit it for review, or request another review if you believe the ad was rejected in error
* **Helpful details for support:** Ad title and copy, disapproval code or message, creative copy, landing URL, and the time you received the notice

## 3. Reporting and measurement

### My campaign launched but is not getting any impressions

* **Check first:** Confirm that billing is fully set up, your payment method is valid, your campaign budget has not been reached, your campaign end date has not passed, and your account has successfully completed verification. Ads that are actively delivering, should show a ‘**Serving’** status. Please allow at least 24 hours after launch before flagging delivery issues, and note that there is typically a delay of up to 7 hours between ad delivery and reporting appearing in Ads Manager Beta.
* **Helpful details for support:** Account name, campaign name, launch date, screenshot showing zero delivery

### Reporting does not match what I expected

* **Check first:** Confirm that the ads included in your reporting are marked as ‘**Serving**’. If you are comparing metrics across table view, CSV downloads, or charts, make sure the same campaigns, filters, and date range are applied across each view. If you’ve confirmed the above and still see discrepancies, please flag the issue to support for further review
* **Helpful details for support:** Report screenshot or export, date range, filters used, short note on what you expected to see

## How to submit a support request

You can submit a support request directly to [ads-support@openai.com](mailto:ads-support@openai.com) or use the support widget in the bottom right of this page.

### How to describe urgency

If the issue looks broader than one campaign or one user, say that clearly. Mention whether it affects multiple campaigns, multiple accounts, or an entire workflow such as reporting or launch. If you suspect a broader incident, include a few concrete examples rather than a general statement that the platform is down.

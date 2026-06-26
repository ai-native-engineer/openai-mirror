<!-- source: https://help.openai.com/en/articles/20001218-bulk-upload-campaign-schema-checklist -->

# Bulk Upload Campaign Schema Checklist

Use this checklist to review your bulk upload file before uploading it in Ads Manager Beta.

Updated: 24 days ago

# Overview

Use this checklist when reviewing your bulk upload schema file before uploading into Ads Manager Beta. It helps catch avoidable file formatting and validation issues before upload.

# Campaigns tab

* All required campaign fields are filled in
* Campaign names are unique
* Campaign objective field is either: ‘Views’ or ‘Clicks’
* Campaign dates are valid and correctly formatted (YYYY-MM-DD)
* Budget fields are completed
* Country field is completed and in JSON format
* No duplicate campaign names
* No more than 5,000 campaigns

# Ad groups tab

* All required ad group fields are filled in
* Ad group names are unique
* Every ad group is linked to the correct campaign
* Campaign names match exactly across tabs (campaign/ ad groups)
* Context hints are in JSON format [“hint1”, “hint2”]
* No duplicate ad group names
* No more than 5,000 ad groups

# Ads tab

* All required ad fields are filled in
* Ad group names match exactly across tabs (ad groups / ads)
* Ad titles are within character limits (16-24 characters recommended; 50 characters maximum)
* Ad copy is within character limits (32–48 characters recommended; 100 characters maximum)
* Landing page URLs are valid and reachable
* Image URLs are publicly accessible and open directly to the image in the browser
* Images are hosted in one of the following methods: Google Drive links, AWS-hosted image links such as S3 or CloudFront, and self-hosted image links on the advertiser’s domain or CDN
* Image assets meet size and format requirements (square, 1200 x 1200 max)
* No more than 5,000 ads

# Formatting checks

* Keep the row with the column names in each template tab. You can add note rows above it, and you can remove or move template instruction or sample rows. Ads Manager ignores template instruction and sample rows when validating your upload.
* Tabs are still named campaigns, adgroups, and ads
* Column headers have not been renamed
* All rows in each tab is a unique campaign, ad group, or ad (no duplicates)
* There are no merged cells
* Campaign and ad group names are consistent everywhere they appear

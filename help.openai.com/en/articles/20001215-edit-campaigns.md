<!-- source: https://help.openai.com/en/articles/20001215-edit-campaigns -->

# Edit Campaigns

Learn how to make updates to campaigns, ad groups, and ads.

Updated: 10 hours ago

There are two primary ways to make changes to campaigns in Ads Manager Beta today.

* In-line edits (for quick updates): make quick changes directly in Ads Manager Beta. Use this for quick updates such as adjusting budgets, updating ad copy, or pausing campaigns.
* Bulk edits (recommended for larger changes): update your campaign data in the ad schema template and re-upload. Use this for structural changes such as updating context hints, ad copy, or landing pages at scale.

## In-line edits

In-line edits are best for quick, one-off updates that do not require editing the campaign schema template.

### Edit existing campaigns, ad groups, or ads

Use this workflow for small updates such as adjusting budgets, updating ad copy, or updating the image of an ad.

1. Hover over the campaign, ad group, or ad.
2. Click the three-dot menu.
3. Select Edit.
4. Make your changes directly.
5. Select Save.

### Create new ad groups or ads

Use this workflow when you want to quickly add new objects within an existing campaign structure.

* To create a new ad group: click into the campaign to access ad groups within that campaign, then click Create and Create ad group.
* To create a new ad: click into the ad group to access ads within that ad group, then click Create and Create ad.

## Bulk updates

Bulk edits are best for making changes across multiple campaigns, ad groups, or ads at once.

### Update existing campaigns, ad groups, or ads

Use this workflow when you want to modify existing campaigns, ad groups, or ads at scale.

1. Select the campaigns, ad groups, or ads you want to update.
2. Click Export for edit. This downloads a file with the selected campaigns, ad groups, or ads for editing.
3. Make updates directly in the exported schema file.
4. In Ads Manager Beta, click Create, then Bulk upload.
5. Select the relevant object type: Campaign, Ad Group, or Ad, and upload the updated file.

After the file is uploaded, your updates will be reflected to the selected campaigns, ad groups, or ads.

### Create new ad groups or ads within existing campaigns

Use this workflow when you want to expand existing campaigns by adding new ad groups or ads.

1. Select the existing ad groups in the campaign where you want to add new ad groups, or select existing ads in the ad group where you want to add new ads.
2. Click Export for edit. This downloads a file that you can add more ad groups or ads to.
3. In the schema file, add new rows with the correct parent IDs and leave the new object ID blank.
4. In Ads Manager Beta, click Create, then Bulk upload.
5. Select the relevant object type: Campaign, Ad Group, or Ad, and upload the updated file.

New ad groups and ads will be created and linked to the existing campaign structure based on the IDs provided.

## Edit and bulk upload FAQ

### Why should I export before editing?

Export for edit gives you the current IDs and field values that Ads Manager needs to update existing campaigns, ad groups, or ads. Start from a fresh export whenever possible, especially if other users may have changed the account since your last file was downloaded.

### Which IDs are required for bulk edits?

To update an existing object, keep that object's ID in the row. To add a new ad group to an existing campaign, copy the existing campaign ID into the new ad group row and leave the ad group ID blank. To add a new ad to an existing ad group, copy the existing ad group ID into the new ad row and leave the ad ID blank.

### Can I add new ad groups and ads in the same upload?

Use the object type and template required by the bulk upload flow. If you are adding multiple object types, follow the Ads Manager upload sequence and make sure new child rows reference an existing parent ID or a parent that has already been created.

### Do context hints get merged or replaced?

When you bulk update an ad group, provide the complete context hints list you want that ad group to use. Treat the uploaded value as the replacement value for that field, not as an additive merge.

### Can I change objective or budget type with an edit?

Some campaign setup choices, such as objective and budget type, are not intended to be changed after creation. If those values are wrong, create a new campaign with the correct setup.

For bulk file validation details, see the [Bulk Upload Campaign Schema Checklist](/en/articles/20001218-bulk-upload-campaign-schema-checklist).

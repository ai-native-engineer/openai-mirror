<!-- source: https://help.openai.com/en/articles/20001346-set-up-custom-audiences-for-your-campaign -->

# Set up Custom Audiences for your Campaign

Understand what custom audiences are and understand how they are set up in Ads Manager.

Updated: 12 hours ago

Custom audiences let you apply your own customer or prospect lists in ChatGPT Ads.

## **How custom audiences work**

Custom audiences are created from lists of customers or prospects, using **email addresses** or **phone numbers**. After you create an audience, you can use it in the ChatGPT Ads in following ways:

* **Campaign-level inclusion**: Use inclusion audiences to limit campaign eligibility to people in one or more selected audiences. This can help you reach known customers, qualified prospects, or audiences you want to target with a specific campaign.
* **Campaign-level exclusion**: Use exclusion audiences to prevent campaign delivery to people in selected audiences. This can help you avoid reaching existing customers, recent purchasers, or audiences that should not see a specific campaign.
* **Ad-group audience bid adjustments**: Use a bid multiplier to increase or decrease an ad group’s maximum bid when the viewer matches a selected custom audience. This can help you bid more competitively for your high-value customers, or bid more selectively for lower-priority audiences.

Note that each custom audience must include at least **25,000** matched users before it can be used. We recommend audiences of at least **100,000** users.

Custom audiences are applied as audience-level controls. Ads Manager does not show individual matched users or let you select specific people from an audience.

**Creating your custom audiences**

### **Preparing your audience file**

* Prepare a **CSV** or **TXT** file up to **500 MB.**
* Uploads can contain up to **5,000,000** identifiers.
* Use **one** identifier type per upload.
* TXT files must include one identifier per line.
* CSV files can include a header row or no header. If you use a header, the columns must be named: email, phone\_number, email\_sha256, or phone\_number\_sha256.
* Custom audiences **cannot** be edited after creation. To change an audience list, create a new audience and archive the old one.

To create a custom audience in Ads Manager:

* Go to **Settings**.
* Open the **Audiences** tab.
* Select **Create custom audience**.
* Enter a name for the audience.
* Choose the identifier type for your upload: email address, phone number, SHA-256 hashed email address, or SHA-256 hashed phone number.
* Upload your audience file.
* Review the details, then select **Create**.

After you create a custom audience, Ads Manager processes the file before the audience can be used. Processing usually takes about **20-30 minutes**, but can vary based on file size.

Note that uploaded rows may differ from the final matched audience size because invalid values, duplicate values, or identifiers that couldn’t be matched do not count toward the matched users.

Audience statuses show whether the audience can be used:

* **Processing** means the file is still being processed and the audience is not ready yet.
* **Ready** means the audience has been processed, meets the minimum matched audience size, and can be used in campaigns or ad groups.
* **Too small** means the audience does not meet the minimum of 25,000 matched users, so it cannot be used.
* **Failed** means the file could not be processed. You may need to retry after checking the file format.

Some intermediate statuses, such as Upload pending, Indexing, or Publishing, mean the audience is still being prepared and cannot be used yet.

## **Use custom audiences in a campaign**

To use custom audiences as campaign-level filters:

* Create or edit a campaign in Ads Manager.
* In the campaign setup, go to the **Custom audiences** section.
* To limit delivery to selected audiences, select **Include audience** and choose one or more ready custom audiences.
* To prevent delivery to selected audiences, select **Exclude audience** and choose one or more ready custom audiences.
* Review the campaign settings, then save the campaign.

Within the same campaign, you can include audience, exclude audience, or both:

* **Inclusion only**: Ads in the campaign are eligible only for people in at least one included audience.
* **Exclusion only**: Ads in the campaign are eligible broadly, except for people in any excluded audience.
* **Inclusion and exclusion together**: Ads in the campaign are eligible only for people in at least one included audience, except anyone who is also in an excluded audience. If you use both included and excluded audiences, the resulting eligible audience after exclusions must still meet the minimum size of 25,000 matched users.

Note that a custom audience cannot be set as both included and excluded in the same campaign.

## **Use audience bid adjustments at ad groups**

To set bid multiplier at the ad group level:

* Create or edit an ad group in Ads Manager.
* Open **Advanced** settings.
* Go to **Audience bid adjustments**.
* Select **Add multiplier**.
* Choose a ready custom audience.
* Enter a multiplier between **0.1x and 10x**.
* Add more multipliers if needed, then save the ad group.

A bid multiplier raises or lowers the ad group’s maximum bid when the viewer belongs to the selected custom audience. For example, you might set a 2x multiplier for high-value customers, a 5x multiplier for people who have previously engaged with your brand, or a 0.5x multiplier for lower-priority audiences.

If a viewer belongs to more than one selected custom audience, the highest matching multiplier is applied. Bid multipliers do not determine who is eligible to see the campaign.

## **Identifier formatting rules**

### Email address

* Use a valid email address with one @.
* Uppercase letters are accepted and normalized to lowercase.
* Leading or trailing spaces are removed.
* Spaces within the email address are not accepted.

### Phone number

* Use E.164 format, including + and country code.
* Spaces, dashes, parentheses, and periods are removed during normalization.
* Phone numbers without a country code are not accepted.

### SHA-256 hashed email address

* Hash the normalized email address: lowercase and trimmed.
* The uploaded value must be a 64-character SHA-256 hex digest.

### SHA-256 hashed phone number

* Hash the normalized E.164 phone number, including + and country code.
* The uploaded value must be a 64-character SHA-256 hex digest.

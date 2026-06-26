<!-- source: https://help.openai.com/en/articles/20001268-create-campaigns-from-product-feeds -->

# Create Campaigns from Product Feeds

Learn how to upload a product feed and create a feed-based campaign in Ads Manager.

Updated: 3 days ago

Product feed campaigns let retail advertisers upload a product feed in Ads Manager and create ads based on that catalog. Product feeds make it easier to bring more of your catalog into ChatGPT ads, create ads at scale, and connect relevant products with users during high-intent conversations. Ads created from product feeds have been among the strongest-performing ads in our program to date.

## **Why create a campaign from product feeds?**

Feed-based campaigns are designed for retail advertisers with broad or frequently changing product catalogs. They can help you:

* Create campaigns from your product catalog at scale with a single feed upload
* Match relevant products to high-intent user conversations
* Keep product details, availability, and metadata used for ads up to date

Advertisers using product feeds have been among the strongest performers on the platform. Because feed ads are built from structured product data, they can make it easier to run larger, more relevant campaigns and scale performance in Ads Manager.

## **Before you begin**

A few things to be aware of:

* Your product feed must comply with our [feed specifications](https://developers.openai.com/commerce/specs/file-upload/overview)
* Feeds must be uploaded through SFTP
* Feeds must contain a minimum of 1,000 products and a maximum of 2 million products
* Products from your feed will only be eligible for use in ads during this beta. They will not appear in organic ChatGPT conversations, though we may offer that capability in the future
* Each ad account is limited to one feed connection
* Ads created from product feeds will use the same format as our current ad units but may evolve in the future. The ad title and description will be pulled directly from your product feed

## **Step 1: Create a product feed**

* In Ads Manager, navigate to the Tools tab
* Select Feeds
* Click Create Feed
* Follow the prompts to create a new product feed

After the feed is created, Ads Manager will generate the SFTP connection details you need to upload your feed.

## **Step 2: Configure your SFTP connection**

* From the feed row, open the three-dot menu
* Select Edit SFTP Connection
* Choose your authentication method: password or SSH key
* Follow the connection guide in Ads Manager to connect to the SFTP server

Use the feed specification when formatting your feed. Feeds created through Ads Manager default products to ads eligible unless an item is explicitly marked false for ads eligibility.

## **Step 3: Upload and validate your feed**

* Upload your product feed through the SFTP connection
* Wait for Ads Manager to process the feed. This can take anywhere from a few minutes to a few hours depending on the size of the feed
* Items are processed gradually. Check the ad group creation modal for # of items ready to serve

## **Step 4: Create a campaign from your feed**

* In Ads Manager, navigate to the Campaigns tab
* Create a new campaign
* In the campaign type dropdown, select Product feed
* Complete the campaign settings

## **Step 5: Create an ad group and choose products**

* Create an ad group for the campaign
* Select the product feed you want to use
* Apply product filters to define which products are eligible for the ad group
* Review the product count shown in Ads Manager to confirm how many uploaded products pass your filters

If the available filters are not enough for how you want to group products, use the ads\_metadata field in your feed. For example, you can add values such as bidding\_tier or product\_line, then use those values to organize products for ad group setup.

## **Step 6: Create an Ad Template**

* Create an ad template for the group
* The ad template is used as the base for advertising products that are eligible based on the filters for the ad group
* The ad template currently only supports making a selection for your image field
* Only one ad template is necessary per ad group
* Review the sample product preview to confirm that titles and descriptions appear as expected

## **Step 7: Review and launch**

Before submitting your campaign, confirm that:

* The correct feed is selected
* The product count matches the intended set of products
* Product titles, descriptions, images, and landing pages appear as expected
* Your ad template previews correctly
* Your campaign, ad group, budget, bid, and targeting settings are complete

Once everything looks correct, submit the campaign for review and launch your feed-based campaign.

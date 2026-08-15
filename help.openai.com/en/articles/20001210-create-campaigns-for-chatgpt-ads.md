<!-- source: https://help.openai.com/en/articles/20001210-create-campaigns-for-chatgpt-ads -->

# Create Campaigns for ChatGPT Ads

Best practices for creating campaigns for ChatGPT

Campaigns define your overall advertising objective and budget in ChatGPT Ads Manager Beta. A good campaign groups together ad groups and ads that support a shared business goal.

Each campaign contains:

* Campaign title
* Objective
* Conversion event (for campaigns with the Conversions objective)
* Budget
* Start and end dates
* Countries to target
* Platforms to target (optional)
* Custom audiences to include or exclude (optional)

## **Choosing a campaign objective**

Your campaign objective determines how your ads are priced and how delivery is optimized. You can currently choose from CPM, CPC, and oCPC objectives. See the table below for more information about each.

|  |  |  |  |
| --- | --- | --- | --- |
|  | **CPM** | **CPC** | **oCPC** |
| Definition | Cost per 1,000 impressions | Cost per click | Conversion-optimized cost per click |
| Marketing Objective | Scale, reach, and awareness | Engagement and traffic | Downstream actions after a click |
| Best for | Maximizing visibility and exposure | Driving users to click through to your website or product | Optimizing toward a specific tracked conversion event after a click |
| How you pay | Per 1,000 impressions | Per valid click | Per valid click, not per conversion |
| System optimization | Broad delivery at scale | Clicks from users likely to engage | Clicks more likely to drive your conversion goal |

For more detail on oCPC campaigns, view our [Create oCPC Campaigns](/en/articles/20001412-create-ocpc-campaigns) guide.

## **Setting your budget**

Your campaign budget controls how much you are willing to spend across all ads within the campaign. When creating a campaign, choose either a campaign-total budget or a daily budget.

When setting your budget:

* Campaign-total budget: Set the total amount you want to spend over the full duration of the campaign. This is the stricter control for total spend.

  Please note: This is a total spending limit, not a pacing control. The budget isn’t distributed evenly across campaign dates, and spend may accumulate quickly depending on how well your ads match eligible conversations and the available opportunities to serve.
* Daily budget: Set the amount you want to spend each day. This is a delivery target, so actual spend may fluctuate above or below the selected amount on an individual day. The current minimum daily budget varies by your ad account’s billing currency. See the [Minimum Campaign Spend table below](/en/articles/20001210-create-campaigns-for-chatgpt#minimum-campaign-spend) for the applicable amount.

Distribute your planned spend across campaigns based on priority, and adjust budget amounts over time as you learn what performs best. If you are new to the platform, we recommend starting with a daily budget so you can monitor delivery and performance before committing to a campaign-total budget.

## **Choosing start and end dates**

Your campaign start and end dates control how long your ads are eligible to run.

When choosing dates:

* Give campaigns enough time to gain traction and gather meaningful performance data. Campaigns can always be paused or adjusted later.
* Consider seasonality, including seasonal products, new launches, promotions, holidays, or other time-sensitive campaigns.
* Align campaign timing with your broader marketing budget and business goals.

## **Choosing countries to target**

Use campaign targeting to control where your ads can deliver. Ads Manager Beta supports campaign-level country targeting and, in the United States, supported state, designated market area (DMA), and ZIP code targeting. Search for a location in the campaign location picker to confirm whether it is currently supported. You can also download the current location catalog as a CSV to see all available locations.

[Download OpenAI Ads locations](https://developers.openai.com/ads/openai-geotargets.csv)

## Choosing platforms to target

Use platform targeting to control which ChatGPT surfaces your campaign can deliver on. In the Campaign dialog, use the Platforms multi-select dropdown to include one or more supported platforms: iOS App, Android App, or Web. Web includes both desktop web and mobile web.

Note: Insights currently group device reporting into Mobile and Desktop, and mobile web is counted under Mobile. More detailed platform reporting is planned.

## Choosing custom audiences to include or exclude

To include or exclude custom audiences from a campaign, see [Set up Custom Audiences for your campaign](/en/articles/20001346-set-up-custom-audiences-for-your-campaign).

## **Best practices**

* Structure campaigns around distinct business goals or initiatives.
* Use separate campaigns for meaningfully different objectives, regions, or product categories.
* Keep campaign naming clear and consistent for easier reporting and management.
* Create multiple ad groups within each campaign to test different themes, value propositions, or messaging approaches.

## **Campaign setup FAQ**

### **Can I change a campaign objective after creation?**

The campaign objective determines pricing and optimization. If you need a different objective, create a new campaign with the objective you want instead of editing an existing campaign into a different objective.

### **Can I change the budget type after creation?**

You can adjust supported budget amounts over time, but some budget type changes are not reversible. For example, if you change a campaign-total budget to a daily budget, you can't change that campaign back to a campaign-total budget. If the budget type is wrong, create a new campaign with the correct setup.

### **Can I target a state, city, DMA, or postal code?**

Yes. In addition to country targeting, you can target supported locations such as states or regions, cities, DMAs, and postal codes where available. Location availability may vary by country. Search for a location during campaign setup to see the options available to you.

### **Why is my campaign not serving?**

Confirm that your ad account verification and billing are complete, the campaign and ads are active, the campaign dates include today, and the ads have completed review. For troubleshooting guidance, see [Troubleshooting](/en/articles/20001217).

## **Next steps**

After creating your campaigns, you can:

* [Create ad groups and add context hints](https://help.openai.com/articles/20001211)
* [Create ads and creative variations](https://help.openai.com/articles/20001212)
* [Launch your campaign and monitor performance](https://help.openai.com/articles/20001209)

## **Minimum Campaign Spend**

| **Country** | **Daily Minimum** |
| --- | --- |
| Australia | 25 AUD |
| Brazil | 40 BRL |
| Canada | 25 CAD |
| Japan | 2,500 JPY |
| Mexico | 150 MXN |
| New Zealand | 25 NZD |
| South Korea | 25,000 KRW |
| United Kingdom | 15 GBP |
| United States | 25 USD |

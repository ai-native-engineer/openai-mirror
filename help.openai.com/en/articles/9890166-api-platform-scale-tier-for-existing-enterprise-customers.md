<!-- source: https://help.openai.com/en/articles/9890166-api-platform-scale-tier-for-existing-enterprise-customers -->

# API Platform - Scale Tier for Existing Enterprise Customers

Updated: 2 days ago

The Scale Tier on the API Platform enables you to purchase a set number of API input and output tokens per minute (known as “token units”) upfront for access to one dedicated model snapshot. Each token unit is purchased for a minimum of 30 days.  
  
Once you’ve signed an order form, you can add and remove token units through your [API Platform account](https://platform.openai.com/settings/organization/scale-tier/overview). Please note that only Organization owners and authorized users may view Scale tier settings and purchase input and output token units.  
  
  
[Learn more about pricing on the Scale Tier.](https://openai.com/api-scale-tier/)

## How can I access my Scale Tier settings?

API Platform Organization owners can access their [Scale tier](https://platform.openai.com/settings/organization/scale-tier/overview) settings by selecting the Settings gear on the top-right of the page and selecting Scale Tier under the "Organization" section in the menu on the left side of the screen.

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-4bcc264d8efc270131c01095/07ef66fee760fca0bc98c33e21bbae75/AD_4nXes1ZT1toitEjivdc9PAFkwT2xe-BAIG_qJkRXrZYkhwunRXjvEcoIIICRAQ7pME8_do422yRXu0d-Ey1x1F9dOxo691y7R6tTvrD1jqSrnNCwgB6IUW0IVFVY5)

The Scale tier setting page enables you to add more capacity, view your input token usage, plan for capacity, view your provisioned tokens, and review your authorized purchasers.

## How can I purchase more capacity?

You can purchase capacity by selecting the Add capacity button on the top-right of your [Scale tier](https://platform.openai.com/settings/organization/scale-tier/overview) page. Please see our [Scale tier main page](https://openai.com/api-scale-tier/) for the latest details on the TPM entitlements per input and output token units.  
  
After selecting the type of tokens you will purchase, you can directly enter an amount or move the slider to select the number of tokens you wish to purchase. The slider enables you to easily view the TPM changes under Summary as you change the tokens. We will also provide a recommendation on the number of units to purchase to cover your last 30 days of traffic.

![Add token capacity dialog for gpt-4o with Input Tokens selected and input limit increasing from 40K to 60K](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-cdb55275195d30d9f8f30f5f/97431912c3f091c3a036ef7cf5f81b37/AD_4nXcoCgOXYcaR5Z80YbZdiCUmFDelGQvnqVM2L5Ex7LLUKZABK3tAIrhFUB484mJbC0ezjUCmwbVCk7JQkwMAJNW8NKfuggfvFCycJb8dIRkU6iPSA-_uSeaVJ1lj)

Once you have finalized your selection, select Checkout to confirm your purchase in the next modal.  
  
Please note that the prices shown in our summary are our standard rates and do not include any discounts negotiated in your organization’s order form. Any applicable discounts will be applied and reflected in the invoice issued to your organization. Any units purchased will be active until the start of the next invoice period, and renew daily after that.

## How do I enable calls to use Scale Tier tokens?

You will need to set the `Scale Tier Enabled` toggle under Project Settings to on.

If you're using the Completions API, please also see our [docs](https://platform.openai.com/docs/api-reference/chat/create#chat-create-service_tier) explaining the [`service_tier`](https://platform.openai.com/docs/api-reference/chat/create#chat-create-service_tier) key, to decide if you should set that manually or rely on the default behavior.

Calls to the Responses API default to service\_tier=auto. If a project has Scale Tier Enabled, requests that omit service\_tier (or use auto) will use Scale Tier by default when Scale Tier quota is available. Requests with service\_tier=default will use shared/PAYG compute.

## How can I view my purchase history and expired tokens?

You can view your Scale tier purchase history in your [Scale tier](https://platform.openai.com/settings/organization/scale-tier/overview) page by selecting a model under Provisioned tokens.

![Provisioned tokens table with active allocations for gpt-4o and gpt-4o-mini](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-e40b1ff7894b6fc47e3d5d11/69e3233d6b95b0e63b924ef6a2f9cd09/AD_4nXehlC5YdDVP57QQhhXHDrTnlEnXMb9itShoGMRM0em5kLHvlWDVgf2gaRM587QBxVtV_Qj82asJe1YsRGrxTxu4PtyiiOHitN7VAGcKq2muDqeeZVfPCL3Zly6H)

Once you select a model, you will be able to view Expired tokens and Prior transactions at the bottom of the page.

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-655e88eb1bb826cbc47519e1/d0f23570424f571bcf850c809fdf8ca5/AD_4nXcXLqUIX4Q0ayyQV-saXnHo0dcJkS8STeeYE9ziUkgy6H0uTmsW8PW7af2eHcd_PFtUtSzevJjO9vxjaThwDyAuLQUzAfQbuTGs4-Lc9amKj3zBHpm4ZKuXclMG)

## How can I edit my token capacity?

You can edit a model’s token capacity by selecting a model under Provisioned tokens in your [Scale tier](https://platform.openai.com/settings/organization/scale-tier/overview) page. Once you select a model, find your purchase under the Active header and select Cancel next to your purchase to edit

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-081538ecc779caa3be874aeb/a5fcb53874771ee3c61cdd5763e8edfb/AD_4nXdC8jHuN4ezoucRcl6eTwoT6KdgcEs14flEF7qkCHUl2dsFgNS8iJIh8qGGXz2Md0Rn_n8zsdKWAq53js6v-yGmN1VDNAO0pYzDPk7cE2ERkkMRPAhU5vt6DNci)

In the modal, you can enter the number of units to cancel directly or use the slider to model the TPM as you make your selection.

![Edit Token Capacity dialog for gpt-4o canceling 1 package and reducing output limit TPM from 2.248M to 2.246M](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-b51ed223d8faeb2b32cfdebc/05d9fa9f857e563aa2b7154d60c0fd4b/AD_4nXeMMjInT6xvF_M9VokdhLfQo9t43luwk4sK_Gab1MNrUE-GygBq5QnDhY9QaiRdggCgYymrKJ_Cz6rCOZ-9YPnTEQlru_8MPRLVzIrUXX2NSQqFgWREZzZR6jRB)

## How can I view my Scale Tier RPM/TPM and usage?

You can view a summary of API usage for your organization in your [Scale tier](https://platform.openai.com/settings/organization/scale-tier/overview) page. All dates and times are UTC-based, and data may be delayed up to 5 minutes.

![Input token usage chart for the last 30 days with several spikes and a peak near 700K](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-08211b3fba8832f7c507f8b2/23bc765f08d1b0d1a09d6e17c7ff9b68/AD_4nXc8gbDSaBnOXh0de_XhZP7o0BuBNiblhocV0DZDJYdrn2b8bLmqw5uGsUxmGVqKCPQv-pO2mZPtxV_JStU2X6n2-sPPwQpDBeR_IAxupNPgdL_vY2JON9Gqpvfz)

You can review your usage in the [Activity Usage Dashboard](https://platform.openai.com/usage/activity) by selecting your Scale tier models in the models drop-down. You can view this data in a 30 day, 1 day, and 15 minute window. Your usage data is stacked to show the amount of usage for the model covered by your Scale tier against the amount of usage covered by your account plan.  
  
Please note that only Organization owners can view the Usage Dashboard.

## When will I see my change in token capacity reflected in the usage dashboard?

It can take up to 24 hours for the changes you make to be reflected. The changes themselves will go into effect near instantaneously.

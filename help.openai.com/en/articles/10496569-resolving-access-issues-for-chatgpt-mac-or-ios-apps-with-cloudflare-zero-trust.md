<!-- source: https://help.openai.com/en/articles/10496569-resolving-access-issues-for-chatgpt-mac-or-ios-apps-with-cloudflare-zero-trust -->

# Resolving Access Issues for ChatGPT Mac or iOS Apps with Cloudflare Zero Trust

Updated: 15 days ago

# General information

## Overview

A recent Cloudflare update has introduced new certificate requirements that may impact access to ChatGPT Mac or iOS apps for Enterprise and Edu customers using Cloudflare Zero Trust with TLS Decryption enabled. If your organization falls into this category, you may experience service disruptions starting Sunday, February 2 unless corrective action is taken.  
  
This article provides step-by-step instructions for Cloudflare administrators to update settings and ensure uninterrupted access.

## Who Is Affected?

You may be impacted if your organization:

* Uses ChatGPT Enterprise or Edu.
* Has Cloudflare Zero Trust enabled.
* Has TLS Decryption turned on.
* Uses the MacOS or iOS native app to access ChatGPT.

**Note**: This issue should not impact ChatGPT web client access, Windows, or Android users.  
  
Without updates, affected users may lose access to the ChatGPT Mac or iOS apps.

## How to Prevent Service Disruptions

To maintain access, Cloudflare Zero Trust administrators must update firewall policies by following these steps:

* **Step 1**: Access the Cloudflare Dashboard -> Go to the Cloudflare Dashboard.

* **Step 2**: Create a New Firewall Policy -> Click **Create Policy**.

* Configure the policy as follows:

* Click **Create policy** to finalize.
* Move this newly created policy to the top of the list to ensure it takes precedence.

If you require further assistance with Cloudflare policy management, contact your Cloudflare administrator or open a support ticket via the [Cloudflare Support Dashboard](https://dash.cloudflare.com/).

## When Will This Change Take Effect?

This update must be applied before Sunday, February 2 to prevent disruptions. After this date, impacted users may no longer be able to access ChatGPT from Mac or iOS until the firewall policy is updated.

# FAQs

## How do I know if my organization is impacted?

There is no proactive way to determine which users will be affected. However, if ChatGPT Mac or iOS access is disrupted, this update should resolve the issue.

## What happens if we do not update our policies?

Users attempting to access ChatGPT via Mac or iOS apps may be unable to connect due to security settings blocking the required traffic, encountering an error such as:

![ChatGPT Mac app error about an untrusted Cloudflare Gateway CA certificate causing a network configuration issue](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-1eeabda0574a9cc27cb17b24/ddaf8be7997dbbd1b40c4e2bf73cf111/AD_4nXfLtB5uoOptbnmGBXiayd55hRhxMn7HxvXYtNFYSezETtIr4ksMv_6DyL6RFkArALG0SVkgySlWWiAboJystaLOaSDqrHJwY4LBYdOQ9y_6BNxKbyxoBTakNoSN)

If you do not update your policies: you will need to use the web client in order to continue accessing ChatGPT.

## Who should implement these changes?

Cloudflare Zero Trust administrators within your organization should follow the steps outlined in this guide.

## Where can I get further support?

If you experience issues after applying these changes, please reach out to:

* Your organization’s IT or security team.
* Cloudflare Support via the Cloudflare Dashboard.
* ChatGPT Support through your Enterprise or Edu account contact.

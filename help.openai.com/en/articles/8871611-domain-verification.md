<!-- source: https://help.openai.com/en/articles/8871611-domain-verification -->

# Domain Verification

Updated: 3 days ago

Domain verification is a process that confirms the ownership of a domain for your GPT experience. It helps prevent fraud and unauthorized access, ensures secure communications, manage access controls, and proves ownership of content created. Within our products, domain verification is required for advanced security features including [single sign-on](/en/articles/8350141-how-to-set-up-debug-sso-for-chatgpt-enterprise) alongside the ability to publish your [custom GPT](/en/articles/8554397-creating-a-gpt) to the GPT store.

## How Domain Verification Works at OpenAI

Currently, domain verification can be required in two places:

* [Single Sign-on (SSO)](/en/articles/10472980-enabling-sso-on-chatgpt#h_7517a41f81)
* [The Custom GPT Builder Profile](/en/articles/8798878-building-and-publishing-a-gpt) for non-Enterprise customers.

To verify your domain, head to [admin.openai.com/identity](admin.openai.com/identity).  
  
Domains are typically verified by adding a specific DNS record (such as a TXT record) to your domain's DNS configuration.  
  
Because domain verification is currently tied to specific OpenAI organizations, once one organization executes the domain verification, no other organizations can verify the same domain. This means that SSO and Builder Profiles should reside in the same organization with domain verification -- otherwise, a verified domain residing in one organization will subsequently block login access or Custom GPT publications in another organization for users who share the same email domain.

# Common Errors

### Your domain could not be verified

![Domain verification error banner stating the domain could not be verified and TXT records may take up to 30 minutes](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-9b889a1a45495a21c2d5b546/86f813d8227f43287321137e24832b13/image.png)

DNS propagation can take up to 24 hours. You can attempt verification as soon as your TXT record is live, and retry if propagation is still in progress.  
  
If you are verifying the domain as part of your Custom GPT Builder Profile, you will need to check with your colleagues if the GPT can be created as part of your company's Enterprise organization. If you are using a different organization for the GPT Builder, you can still create GPTs but cannot publish them in the GPT store.

### "We ran into an issue while signing you in, please take a break and try again soon"

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-a5b3b1635ea1783211e2881a/9178121be0e662180a0925380ed5118c/CleanShot_2024-01-16_at_15.59.54_402x__281_29.png)

This error may happen if your domain was verified in another OpenAI organization, preventing all users from logging in to the OpenAI organization you belong to. You can check if other users are also seeing this same error message.  
  
If the issues do not self-resolve after enough time has passed for the records to be registered, please reach out to Support for further assistance.

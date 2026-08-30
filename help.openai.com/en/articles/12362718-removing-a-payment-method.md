<!-- source: https://help.openai.com/en/articles/12362718-removing-a-payment-method -->

# Removing a payment method

Remove a saved payment method from ChatGPT or the API Platform, or get help when removal is unavailable.

Updated: 3 days ago

You can remove saved payment methods in the billing settings for ChatGPT or the API Platform. Use the steps for the account, workspace, or organization that holds the payment method.

Removing a payment method does not cancel a subscription, erase past invoices, or reverse charges. To stop a ChatGPT subscription from renewing, see: [Canceling your ChatGPT subscription](https://help.openai.com/articles/7232927).

To avoid interrupting paid services, add a replacement payment method before removing the old one.

# Remove a payment method

If Apple or Google bills your subscription, manage the payment method through your Apple Account or Google Play account. The steps below do not change a store payment method.

## ChatGPT on the web

Use these steps for a personal ChatGPT account. A Free account can still have a saved payment method.

1. Go to [**Settings > Billing**](https://chatgpt.com/#settings/Billing) in ChatGPT on the web.
2. Under **Payment methods**, select the card’s more options menu (•••).
3. Select **Remove**. If it is unavailable, follow the troubleshooting steps below.

### If you see Payment in Account settings

Some accounts use a billing portal instead. Follow these steps if **Payment** appears in **Account** settings.

1. Go to [**Settings > Account**](https://chatgpt.com/#settings/Account).
2. Under **Payment**, select **Manage**.

![ChatGPT Account settings with the Payment section and Manage button highlighted](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-d0f838526f9043a4679b742a/9b8db2967830783d83454e6ef1c67010/Payment_details.png?q=80&fm=webp&w=1340)

In the billing portal, select **×** beside the payment method you want to remove.

![Payment method list with American Express ending in 1009 and the remove X icon highlighted](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-de1157c841249dc37bd619a2/baecc692b8e194c858a162d5c30114f2/payment-method-delete.png?q=80&fm=webp&w=942)

## ChatGPT Business

Only workspace owners can manage Business billing.

1. Switch to the Business workspace that uses the payment method.
2. Go to [**Workspace settings**](https://chatgpt.com/admin/billing), then select **Billing > Plan**.
3. Open **Manage plan** and select **Payment method**.

![Billing page Manage plan menu opened to Payment method](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-ef823c574c0f12adc0cf08a6/2d0f91f0884e6986257416ddb11dead3/billing_payment_method.png?q=80&fm=webp&w=1344)

1. In the billing portal, select **×** beside the payment method you want to remove.

![Payment method page with the remove X icon highlighted next to the default American Express card](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-1205dae71ce4ad76b1a634f3/e40ea269acbc59eac1565041f648acdd/payment-method-delete.png?q=80&fm=webp&w=942)

If workspace ownership is changing, coordinate the replacement payment method with the new owner before removing yours.

## API Platform

1. Sign in with an account that has permission to manage the organization’s billing, then select the correct organization.
2. Go to [**Billing > Payment methods**](https://platform.openai.com/settings/organization/billing/payment-methods).
3. On the card you want to remove, select **Delete**.

![Billing Payment methods tab with a red arrow pointing to the Delete link for a saved card](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-04fe705d33fb5995f7a4a3c3/b52e6cd1c790ad7d65ceae4a511b8346/Screenshot_2025-09-22_at_12_10_47_E2_80_AFPM.png?q=80&fm=webp&w=1344)

If **Delete** is unavailable for the default card, add another payment method and select **Set as default** for it, then try deleting the old card again.

# If you cannot remove a payment method

## Only Edit appears for a saved card

If a card is marked **Default** in ChatGPT’s **Billing** settings, its menu may show **Edit** without **Remove**. To replace it, add another payment method, select **Set as default** for the replacement, then try removing the old card.

If you want to remove your only saved card and no removal option is available, [contact Support](https://help.openai.com/articles/6614161).

## The card remains after cancellation

An active subscription or a cancellation that has not taken effect can prevent removal. Check the cancellation status and the end of your current billing period.

If your plan has already ended or your account is on Free, [contact Support](https://help.openai.com/articles/6614161) if no removal option is available.

## The card is used for auto-reload

If ChatGPT says the card is used for auto-reload, select **Manage auto-reload**. Choose another payment method or turn off auto-reload, then try removing the card again.

## There is an unpaid invoice or payment failure

Outstanding charges can block removal. If the charge is expected, pay the invoice or update the payment method as instructed in billing settings. [Contact Support](https://help.openai.com/articles/6614161) if you cannot resolve it.

## You cannot open billing settings

For a Business workspace, ask a workspace owner to manage the payment method. If you are an owner but the workspace is deactivated or billing settings are inaccessible, [contact Support](https://help.openai.com/articles/6614161).

For API billing, check that you have selected the correct organization and have permission to manage its billing. Ask an organization owner to check your access. If you still cannot access billing, [contact Support](https://help.openai.com/articles/6614161).

# Get help

[Contact Support](https://help.openai.com/articles/6614161) if the relevant steps do not resolve the issue. Include:

* The email address you use to sign in.
* Whether the payment method is in personal ChatGPT, a Business workspace, or an API organization, and the workspace or organization name if relevant.
* Your plan or cancellation status, the missing option or exact error, and the steps you tried.
* A screenshot with sensitive details hidden. Do not send a full card number, security code, password, or verification code.

For a charge you do not recognize, see: [Unrecognized ChatGPT or API Credit Purchase Charges](https://help.openai.com/articles/7242625).

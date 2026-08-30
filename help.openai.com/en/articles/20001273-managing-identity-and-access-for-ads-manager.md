<!-- source: https://help.openai.com/en/articles/20001273-managing-identity-and-access-for-ads-manager -->

# Managing identity and access for Ads Manager

Manage Ads sign-in, advertising-account roles, synchronized users, and safe offboarding.

To use Ads Manager, a person needs both a permitted sign-in method and a role for the correct advertising account. Joining an OpenAI tenant, using single sign-on (SSO), or appearing in a synchronized directory does not automatically provide Ads access.

# Understand Ads administrator and account roles

Open Admin Console and select the tenant associated with the advertising account. Your role determines which settings you can manage.

| **Role** | **Scope** | **What it allows** |
| --- | --- | --- |
| global admin | Tenant | Manages tenant-wide domains, identity providers, sign-in policies, and directory connections; can create eligible advertising accounts. |
| Ads admin | Tenant | Creates eligible advertising accounts. Does not manage tenant-wide identity or automatically access existing accounts. |
| ad account admin | One advertising account | Manages the account and supported user or group access. At least one effective account admin must remain. |
| ad account member | One advertising account | Uses and updates supported advertising resources without full account-administration permissions. |
| ad account viewer | One advertising account | Views advertising resources without write or account-administration permissions. |

A person who manages tenant identity, creates an account, and administers that account may need more than one role. A ChatGPT workspace or API Platform organization role does not grant Ads permissions.

Within an advertising account, a person receives the highest role granted directly or through a group: **Admin**, then **Member**, then **Viewer**. Changing or removing a direct role does not reduce access if a group still grants a higher role.

# Check the Ads sign-in policy

In Admin Console, open **Global settings**, then **Access**. Review **Ads SSO settings** for the selected tenant. Activating a shared identity-provider connection or another product’s SSO policy does not automatically enable SSO for Ads.

| **Policy** | **What it means** |
| --- | --- |
| **Required** | SSO is available as a sign-in method. However, someone who is already signed in may be able to access an advertising account with a **Required** policy without signing in again through SSO. |
| **Optional** | Eligible users can use the configured identity provider or another permitted sign-in method. |
| **Off** | SSO is unavailable for the selected product or resource. Users must use another permitted sign-in method. |

Keep SSO **Optional** while testing when that setting is available. Before selecting **Required** or **Off**, confirm that users can access their accounts and that an authorized administrator has a recovery path.

Configure applicable multi-factor authentication (MFA) and conditional-access requirements in your identity provider.

For connection and domain setup, see: [Single sign-on (SSO) setup for OpenAI products](https://help.openai.com/articles/9534785).

# Give someone access to an advertising account

1. In Admin Console, select the correct OpenAI tenant.
2. Select the advertising account.
3. Open **Users & groups**, where available.
4. Find the user or supported account-specific group.
5. Assign the appropriate **Admin**, **Member**, or **Viewer** role.
6. Ask the person to sign in with the work email associated with the tenant.

If the person is missing, confirm that an authorized administrator has invited or synchronized the user. A ChatGPT workspace invitation does not provide advertising-account access.

![Users tab for an Ads account in Admin Console, showing total, active, and invited user counts, user roles and statuses, and an Invite button.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_LI5_WwIBlPC0JHxnB2DNk9Qywgo1jZSVSbuUa0yJv38/20fb3bdcb30fd448d31d6824dfab2cfa/lbas_img_LI5_WwIBlPC0JHxnB2DNk9Qywgo1jZSVSbuUa0yJv38.jpg?q=80&fm=webp&w=1344)

Assign the appropriate role separately for each advertising account a person needs to access.

# Assign the Ads admin role and create the first account

1. Open Admin Console and select the intended tenant.
2. In **Global settings**, open **Users & groups**, select **Users**, and open the person’s profile.
3. Open **Access & roles** or **Direct roles**, depending on which tab is available.
4. Choose the option to add or edit tenant-level access. If you are asked to select a product, select **Cloud Console**.
5. Select **Ads Admin** and save the assignment.

![Admin Console user profile with the Direct roles tab selected, alongside Information, Groups, and Product access.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_h1IjPFPJMN9D0uj2KDEFI3dWdGdViF8JAyuGryJ8mPs/e4288f25ef1c5b19098f569e772e52d0/lbas_img_h1IjPFPJMN9D0uj2KDEFI3dWdGdViF8JAyuGryJ8mPs.png?q=80&fm=webp&w=1344)

A user profile may show **Access & roles**; other configurations show **Direct roles**.

If no advertising account exists, a global admin or Ads admin can create the first account. Account-specific roles may not appear until that account exists.

To create an additional advertising account, start from [Ads Manager](https://ads.openai.com/) with the required permissions. A direct onboarding link can reopen an existing advertising account if you already have an active Ads Manager session.

If **Ads Admin** does not appear, confirm that you selected the correct tenant and, when prompted, **Cloud Console**. Ask a global admin or your OpenAI account team to check your access and Ads eligibility.

# Manage synchronized users and groups

Ads accounts use a tenant-wide SCIM directory, not a separate directory for each advertising account. Eligible tenants, including Ads-only tenants, can synchronize users and groups, but access to each advertising account must still be assigned separately.

Tenant-wide SCIM cannot change the email address on an existing OpenAI account, and OpenAI Support cannot make that change manually.

Manage synchronized users and group membership in your identity provider. You cannot manually add a synchronized user to an advertising-account group or change synchronized group membership in Admin Console.

To give a synchronized group access to an Ads account, open the group’s **Product access** settings, select the account, and save your changes. The initial account role is **Member**. An authorized administrator can change the synchronized group’s advertising-account role without changing its identity-provider membership.

![Groups tab for an Ads account in Admin Console, showing group roles and an open role menu with Admin, Member, and Viewer options.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_EQnQHb8538D5hoZWVfBm0xJDsDBEgHUH7KLdxh6dW7k/22f17e650ab20ecfd700dd56f78ec431/lbas_img_EQnQHb8538D5hoZWVfBm0xJDsDBEgHUH7KLdxh6dW7k.jpg?q=80&fm=webp&w=1344)

For directory eligibility, setup, and troubleshooting, see: [SCIM provisioning and management](https://help.openai.com/articles/10011769).

# Remove or change advertising-account access

Before removing the only effective ad account admin, assign another administrator. Each advertising account must retain at least one effective admin.

1. Select the advertising account and open **Users & groups**.
2. Review the person’s direct role and account-specific group assignments.
3. Remove or change the direct role, or update the relevant group membership.
4. Update synchronized group membership in your identity provider when applicable.
5. Confirm that another account administrator remains and the person’s resulting access matches your intent.

Manage synchronized group membership in your identity provider. For SCIM-managed users, review direct advertising-account roles and synchronized group assignments. For manually managed users, review direct roles and manually managed group assignments. Removing one access path may not remove another, so confirm the person’s remaining access to each advertising account.

# Resolve Ads-specific access problems

If someone cannot open Ads Manager, check:

* The selected OpenAI tenant and advertising account.
* The person’s work email and applicable Ads sign-in policy.
* Whether the person accepted the correct invitation.
* The account-specific role and any direct or group-based access.
* Recent directory changes or identity-provider assignments.
* Whether a global admin or Ads admin must create the first advertising account.

For sign-in errors, see: [Troubleshooting SSO, workspace access, and domain verification](https://help.openai.com/articles/10489721).

────────────────────────────────────────────────────────────

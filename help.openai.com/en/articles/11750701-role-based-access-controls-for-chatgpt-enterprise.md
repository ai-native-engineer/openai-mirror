<!-- source: https://help.openai.com/en/articles/11750701-role-based-access-controls-for-chatgpt-enterprise -->

# Role Based Access Controls for ChatGPT Enterprise

Role-Based Access Controls in your ChatGPT workspace.

Updated: 21 minutes ago

*Note: RBAC is currently available for Enterprise, Edu, ChatGPT for Healthcare, and ChatGPT for Teachers.*

**RBAC** stands for Role-Based Access Controls. It is a security and permissions model used to control access to systems or resources based on a user’s role assignments. With RBAC, you can define permissions against a role and assign these roles to groups within your organization. This simplifies permission management and improves security in your ChatGPT workspace.

Workspace settings provide the default for eligible permissions. A custom role is a reusable set of permissions that owners can assign directly to members or through groups. A member may have more than one custom role.

For eligible permissions, a custom role can use **Default** to inherit the workspace setting, **On** to explicitly allow access, or **Off** to explicitly deny access. ChatGPT evaluates all applicable roles together: at least one role must grant the permission, and an explicit **Off** in any applicable role prevents access. Lockdown Mode is evaluated separately and can further restrict network-enabled capabilities. A member’s seat type, plan, and product eligibility still apply.

## Who can configure RBAC settings and permissions?

[Workspace owners](/en/articles/8266401) can adjust default settings and permissions and use RBAC to create customized settings and permissions. Workspace admins, members and analytics viewers cannot.

**Are there any geography restrictions?**

All supported countries access to this feature.

## Is RBAC configuration available on web, mobile, and desktop?

RBAC configuration is available on web, under Workspace settings -> [Permissions & roles](https://chatgpt.com/admin/permissions).

## What capabilities are included?

Workspace owners can use **Workspace settings > Permissions & roles** to:

* Set the workspace baseline for eligible member permissions.
* Create ordinary custom roles that use **Default**, **On**, and **Off** for eligible permissions.
* Assign one or multiple custom roles to groups.
* Assign roles directly to individual users where available.
* View and manage custom roles in a centralized tab.

## What permissions can I configure with RBAC?

You can control access to key ChatGPT features with RBAC. For a full list of available toggles and options, refer to Workspace settings > [Permissions & roles](https://chatgpt.com/admin/permissions).

Available permission states vary. Eligible ordinary-role permissions use **Default**, **On**, and **Off**. Some permissions, including certain Work and plugin controls, can remain two-state **On** or **Off** controls.

### Lockdown Mode roles

Workspaces that have Lockdown Mode role support can use RBAC to create a custom role for members who need Lockdown Mode. Treat Lockdown Mode as a role-level security configuration, not as a single permission toggle.

When a member is assigned to a Lockdown Mode role, network-enabled capabilities may be limited, including live web search, deep research, agent mode, Canvas networking, and some app, MCP, or connector behavior, depending on workspace settings.

Before assigning a Lockdown Mode role, review which apps and actions the role allows and confirm that members have the permissions they need in each connected source system. App access in ChatGPT does not override permissions in the connected source system.

For more detail about what changes in Lockdown Mode, see **Lockdown Mode**.

We will continue to add features to RBAC permissions over time.

**Note:** You can control access to apps on a per-app basis. An app’s UI cannot be disabled independently.

## What is Member RBAC and how is it different from current roles?

Member RBAC lets workspace owners create custom roles to control end-user access to tools. Existing roles such as Member, Admin, and Owner govern workspace-management rights.

## How do I assign roles to people or groups?

In **Workspace settings > Permissions & roles > Custom roles**, assign roles to individual users or to groups created in **Groups** or synced through SCIM. To assign a role to a specific user, open the user’s profile, go to **Direct roles**, and select **Assign direct role**. Users receive permissions from both direct role assignments and group role assignments.

## Can I create my own roles?

Yes. Use **Add new role** in the **Custom roles** tab to define roles with tailored permissions.

## What is required to enable RBAC for my workspace?

Nothing extra. RBAC is available to eligible workspace owners in the admin dashboard. Create or sync groups, assign roles to groups, or use direct role assignments where available.

## How does RBAC evaluate roles, assignments, and defaults?

Workspace settings provide the baseline for eligible permissions. In an ordinary custom role:

* **Default** inherits the workspace setting.
* **On** explicitly grants the permission.
* **Off** explicitly denies access.

A member can receive multiple ordinary roles through direct and group assignments. ChatGPT evaluates all applicable ordinary roles together. At least one applicable role must grant the permission, and an explicit **Off** in any applicable role prevents access. If all applicable ordinary roles use **Default**, the workspace setting applies.

Lockdown Mode is a separate veto path. A Lockdown assignment can restrict a capability even when an ordinary role grants it. A member’s seat type and other plan or product eligibility requirements also continue to apply.

# How to configure RBAC in your workspace

1. Open **Workspace settings**.
2. Select **Permissions & roles** in the left panel. Only workspace owners can access this area.
3. Open the **Workspace** tab to review the baseline permissions for members.

For eligible permissions, the workspace setting is inherited by a custom role when that role is set to **Default**. A role set to **On** grants the permission through that role. A role set to **Off** explicitly denies access, even if another assigned role is **On**.

![Settings & permissions page with Workspace and Custom roles tabs for configuring baseline and custom access](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-8815c91ffcd421fc102212dd/5afa3bc587345d0ea137aeebc4648fff/AD_4nXekKOHDPNGULcoqmbTxb1_G42yFvcFg6tJql10oSoExd32fk4yZST3g5TuCZup-vDFlEdqTcMkYWaIt7riRrcD-0tmy4QENZBPR0OvYUjmHvE89V1MNRFuuA-Cy)

As you scroll through the page, configure the workspace baseline for eligible permissions.

To create a custom role:

1. Open the **Custom roles** tab.
2. Select **Create role**.
3. Enter a role name and description.
4. Select **Save**.

![Settings & permissions page with Custom roles tab selected and Create role button](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-8926bff2a6d298dec31333d0/11a2769c7300da0db10e9584403a3c59/AD_4nXcmKY6qrkmwhO2lAj8my_OibYUGkNHMBgcSEqqaYO0bEolEhzoLZSlHUa8oVQRFjATceOzlBfYL2dk7v2llQWeBqZBlWKrsOoXudHgdytRwMWaRtdgIRdCv_hZl)

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-b7aa017fe173251960b4afbe/c90faa2ddfda14727c48b6c18a775cfe/AD_4nXfpeCFMRbYlLn5y6G9bifY3s6a6CeDkDFdom3NKrBNpWyICLmYIc6riUWhs-M6FsClNbWtxqsKdj7LwUJvafSaWbs5PgshCETUvyoyMqryridzei24NdxfuQz38)

On the custom role permission page, choose **Default**, **On**, or **Off** for each eligible permission. Two-state permissions continue to use **On** or **Off**.

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-65608794ce387ae22ae5ef7a/11ac910348d8980df28b0819b7b93480/AD_4nXeIL4heybW83untyKxdcKdDs0cp0Sm2Io6bua4M0VgGcamxAu0RuCi62IfQ78LkfrqUzQS78nvyfAhPca0Ol3s-t-I__MpA5jsSSZeZ88hgtIKseSuFFoxTfRJY)

![Workspace Search settings with Web search and Deep research enabled, Agent mode disabled](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-79fc890feedc1e0992624345/4094155546eece572a04bfd8ed214339/image.png)

To assign the role to groups:

1. Open **Role assignments** at the top of the custom-role page.
2. Select **+ Add**.
3. Choose one or more groups.
4. Select **Done**.

![Full GPT Access role assignments tab with no groups found and an Add button](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-1eecb989058dcd87b9ea5088/50003239c491693afbeeb06d5846e3ff/AD_4nXcije-kE6JYKhfRvEDtIKrMz3S1yKWYHbfxmjzWuQCWGKwj4X4JzQMlH7znVi_oaGzj4IL3Pr4kUbbQ5c6LNhOGvy4sFth42LUaISoZg_LBmmI_v_KDA9xf9KwS)

![Assign groups to role dialog with Marketing added and R&D available to add](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-e610acfc4ce7793c8f2d2d75/c672442891cc912573af8d63c85a85b0/AD_4nXckRfff5IOlRopMazwMDZ-wtvBd8SpC7OsGtpi7Lt-0OKEPNbLJJN73qXiwaQnO0w04pBvW5l39HbyZJQhYht5vaVboNTf7U9GXUieg9tebf_AWQUnj2ywiDl7p)

End users in a group with the custom role receive the updated effective permissions after the change takes effect. Changes are not always immediate; confirm the public propagation window before publication.

# Examples

## One ordinary role inherits the workspace setting

If the workspace setting for **Web search** is **On** and a member’s only ordinary custom role uses **Default**, the member inherits **On**.

## One role is Off and another role is On

If one ordinary role sets **Web search** to **Off** and another ordinary role sets it to **On**, access is denied because an explicit **Off** in any applicable role overrides grants.

## Every applicable ordinary role is Off

If all applicable ordinary roles set **Web search** to **Off**, the member does not receive access through ordinary RBAC, even if the workspace baseline is **On**.

## Lockdown Mode applies

If an ordinary role grants a network-enabled capability but the member also has a Lockdown Mode role that restricts it, the Lockdown restriction applies.

# FAQ

## Are groups required for RBAC?

No. Roles can be assigned through groups, and direct role assignments are available where supported. Groups remain the recommended way to manage access at scale.

## How long do RBAC changes take to apply?

Changes are not always immediate. Confirm the public propagation window before publication.

## Does RBAC override a member’s seat type?

No. RBAC controls feature permissions within the access allowed by the member’s seat type and workspace plan.

## What if a permission has only On and Off?

Some controls do not support **Default**. For those controls, configure **On** or **Off** explicitly for the workspace and relevant roles.

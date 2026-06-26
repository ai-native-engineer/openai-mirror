<!-- source: https://help.openai.com/en/articles/12603091-chatgpt-atlas-for-enterprise -->

# ChatGPT Atlas for Enterprise

Updated: 14 days ago

**System requirements**

ChatGPT Atlas supports Macs with Apple silicon (M-series chips) running macOS 14.2 Monterey or later.

Atlas is OpenAI’s new browser. It is generally available for consumers. For Business and Enterprise customers, Atlas is in beta so teams can evaluate it with low-risk data. This page explains who gets access, what protections do and do not apply, and how to run a careful pilot.

## Availability and access

**Business**  
  
Atlas is available by default to all Business workspaces. No admin opt-in is required.  
  
  
**Enterprise**  
  
Enterprise access is off by default.  
  
Workspace owners can enable access to Atlas in their [workspace settings](https://chatgpt.com/admin/permissions) - users can log in with enterprise credentials and access can be managed directly via RBAC.  
  
Until the toggle is enabled, Enterprise users are blocked from signing in with Enterprise credentials. Your OpenAI account team can coordinate an allowlist if needed.

## Enabling and disabling Agent on ChatGPT Atlas

ChatGPT Enterprise admins can enable or disable access to Agent on ChatGPT Atlas in their [workspace’s permission settings](https://chatgpt.com/admin/permissions) by toggling **Agent mode** under the Search header.  
  
Please note that this toggle enables and disables member access to agent mode on both ChatGPT and ChatGPT Atlas. [Learn more about agent mode on ChatGPT.](/en/articles/11752874-chatgpt-agent)

## Security and compliance, at a glance

Atlas for Business and Enterprise is early access. We recommend caution using Atlas in contexts that require heightened compliance and security controls—such as regulated, confidential, or production data. Controls that apply elsewhere in your workspace do not automatically apply to Atlas unless listed on this page.  
  
  
**What is covered today**

* **No training on your data.** Atlas does not use Business or Enterprise content to train OpenAI models.
* **User-level privacy controls.** Individuals can clear their own web browsing data and update privacy settings, including on/off toggles for Memories, model training, and access to usage logs. [Learn more about Privacy controls on ChatGPT Atlas.](/en/articles/12574142)

**What is not covered yet**

* **Certifications and scope.** Atlas is not currently in scope for OpenAI SOC 2 or ISO attestations.
* **Accessibility.** Atlas is not yet fully compliant with WCAG accessibility standards.
* **Data controls.** Some Atlas data types, for example web browsing data, browser memories, and agent activity, may not be covered by Enterprise data retention, storage, segregation, or deletion requirements.
* **Audit and exports.** Atlas does not emit Compliance API logs and does not integrate with SIEM or eDiscovery.
* **Residency.** Atlas-specific data is not region-pinned.
* **Admin and RBAC.** No Atlas-specific RBAC, policy bundles, blocklists, or allowlists beyond the sign-in control above.
* **SSO and lifecycle.** No Atlas-specific SSO enforcement or SCIM provisioning and deprovisioning.
* **Network controls.** No IP allowlists or private egress settings.
* **Managed distribution and updates.** No enterprise update channel or version pinning.
* **Extensions and policy management.** Enterprise extension controls and browser policy management are limited.
* **Search providers.** Atlas may use additional sub-processors for search, which we will document as coverage expands.

If your deployment requires any of the items listed as not covered, treat Atlas as out of scope for now.

## MDM and managed preferences

Atlas supports managed preferences delivered through your own MDM, targeted at the host `com.openai.atlas.web`.

Keys officially supported so far:

* `CookiesAllowedForUrls`
* `ExtensionInstallAllowlist`
* `ExtensionInstallBlocklist`
* `ExtensionInstallForcelist`
* `ExtensionSettings`
* `RemoteDebuggingAllowed`
* `PasswordManagerEnabled`

Many other Chromium-style keys are expected to work, aside from keys that change the Atlas interface. We will expand official support as Atlas becomes generally available.

## Agent in Atlas

Atlas includes agent functionality. When you enable Atlas, agent mode is available within the browser environment. Review this with your security team if agent behavior introduces new risk for your organization.

## How to run a careful pilot

1. **Decide scope.** Choose a small pilot group, use non-sensitive test data, avoid production credentials. Share this page before access begins.
2. **Confirm status.** Align with legal, security, and procurement that Atlas is early access and currently out of scope for SOC 2 and ISO attestations.
3. **Enable access.**

   * **Business:** Atlas is on by default.
   * **Enterprise:** Contact your OpenAI account team about an allowlist.
4. **Apply MDM settings.** Push any managed preferences to com.openai.atlas.web.
5. **Set expectations with users.** Remind users that Atlas does not train on Business or Enterprise content, and that they can clear browsing data in Settings.
6. **Report feedback.** Track issues, missing controls, and policy needs, and share them with your OpenAI account team.

## Legal and compliance notice

Atlas for Business and Enterprise is an early access product. Existing ChatGPT Enterprise security and compliance commitments do not apply to Atlas at this time. If you need formal assurances or certification coverage, wait for those capabilities to be documented here before enabling access.

## FAQ

**Who can access Atlas today?**  
  
All consumers can use Atlas. Business workspaces get Atlas by default. Enterprise workspaces can opt in by enabling the toggle in their [workspace settings](https://chatgpt.com/admin/permissions).  
  
  
**Does Atlas train on our Business or Enterprise content?**  
  
No. Atlas does not use Business or Enterprise content to train OpenAI models.  
  
  
**Can we use Atlas with regulated data such as PHI or payment card data?**  
  
No. Do not use Atlas with regulated, confidential, or production data.  
  
  
**Can we enforce SSO, SCIM, or RBAC for Atlas?**  
  
Yes. The same SSO settings you configure for your ChatGPT Enterprise workspace are applied to Atlas authentication. Atlas access and [browser memories](/en/articles/12625059-web-browsing-settings-on-chatgpt-atlas#h_69e0406b18) can be controlled via workspace RBAC settings.  
  
  
**Can we collect audit logs or export Atlas activity through the Compliance API?**  
  
Not yet. Atlas does not emit Compliance API logs or SIEM and eDiscovery feeds.  
  
  
**Can we control extensions and other browser policies?**  
  
Atlas supports a limited set of managed preferences through your own MDM. See the keys above. More policy coverage will come as we move toward GA.

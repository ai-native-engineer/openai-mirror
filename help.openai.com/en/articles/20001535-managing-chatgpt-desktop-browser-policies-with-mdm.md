<!-- source: https://help.openai.com/en/articles/20001535-managing-chatgpt-desktop-browser-policies-with-mdm -->

# Managing ChatGPT desktop browser policies with MDM

Learn how to deploy and verify Chromium enterprise browser policies for ChatGPT desktop on Windows, macOS, and Linux.

Updated: 10 days ago

**Extension availability.** You can configure extension policies through MDM before your workspace has access to the extension installation and management UI. Deploying these policies does not turn on that UI.

ChatGPT desktop's in-app browser is based on Chromium and inherits its enterprise policy framework. It uses the same policy names and value formats as Chrome. Use the [Chrome Enterprise policy reference](https://chromeenterprise.google/policies/) to find controls and understand their values. Policies apply where the platform, browser version, and affected feature are supported in ChatGPT desktop.

If you already manage Chrome, the deployment process will be familiar. Chrome supports both device-based policy deployment and cloud browser management through Google Admin. ChatGPT desktop currently supports device-based deployment through MDM, Group Policy, or configuration-management tools; cloud management of these browser policies is not yet available.

For a given operating system, the policy contents and formats stay the same. The main change is **where you deploy them on the device**: use ChatGPT desktop's registry keys, preference domain, or policy directory instead of Chrome's.

# Policy locations by platform

| **Platform** | **How policies are read** | **Chrome location** | **ChatGPT desktop location** |
| --- | --- | --- | --- |
| Windows | Registry values and policy subkeys | SOFTWARE\Policies\Google\Chrome | SOFTWARE\Policies\OpenAI\Codex |
| macOS | Managed preferences in a configuration profile | com.google.Chrome | com.openai.codex |
| Linux | JSON files in the mandatory-policy directory | /etc/opt/chrome/policies/managed/ | /etc/opt/codex/policies/managed/ |

The ChatGPT desktop identifiers still contain Codex or codex. Use them exactly as shown.

* **Windows:** Use HKEY\_LOCAL\_MACHINE for all users on a device, or HKEY\_CURRENT\_USER for a specific user. Policy value types and list subkeys follow Chrome's registry format. Chrome's standard administrative templates (ADMX) target Chrome; use custom registry settings for ChatGPT desktop.
* **macOS:** Deploy the policy keys and their plist values as managed preferences under com.openai.codex. A profile targeting Chrome's domain does not target ChatGPT desktop.
* **Linux:** Deploy JSON files directly into /etc/opt/codex/policies/managed/. Use /etc/opt/codex/policies/recommended/ for policies that support defaults users can change.

# Admin guide

## Example policies

The examples below configure two policies:

| **Policy** | **Example value** | **Effect** |
| --- | --- | --- |
| PasswordManagerEnabled | `false` | Prevents saving new passwords. Existing saved passwords are not deleted. |
| CookiesBlockedForUrls | `["https://example.com"]` | Prevents https://example.com from setting cookies. It does not block access to the site. |

Replace these examples with your organization's settings.

## Manage extensions

Deploy these Chromium policy keys at the ChatGPT desktop location above. These policies apply to supported extension features; they do not enable the UI for installing and managing extensions.

* **ExtensionInstallBlocklist** — List of IDs users cannot install; \* blocks all by default. Matching installed extensions are disabled.
* **ExtensionInstallAllowlist** — List of IDs exempt from the blocklist. With a \* blocklist, this permits named signed extensions; it does not install them.
* **ExtensionInstallForcelist** — List of extension IDs, optionally followed by ; and an update-manifest URL. Silently installs them, grants requested permissions, and prevents users from disabling or uninstalling them. It takes precedence over the blocklist.
* **ExtensionSettings** — Dictionary keyed by extension ID or \* for defaults. Sets installation mode (such as blocked, allowed, or force\_installed) and can restrict permissions and host access, require a minimum version, set update behavior, or pin an extension. Per-ID settings can override the list policies.
* **ExtensionAllowedTypes** — List of installable manifest types, such as extension or theme. It also constrains forced installs.
* **ExtensionInstallSources** — URL patterns for the Chromium direct CRX install flow, where available. Both the download URL and the initiating page must match; the blocklist still takes precedence.

On Windows, deploy list policies as numbered REG\_SZ values in policy-named subkeys and ExtensionSettings as JSON in a REG\_SZ value. On macOS, use arrays and a dictionary in the com.openai.codex managed-preferences domain. On Linux, use JSON arrays and an object in a managed-policy file.

Check chrome://policy for deployed values and errors. If a force-installed extension is active, test its behavior in a pilot in-app browser workflow where possible. If the in-app browser UI for installing and managing extensions is available in your workspace, check chrome://extensions/ and test the user install and management flow.

## Windows: Microsoft Intune or Group Policy

For **Microsoft Intune**, save the following as a PowerShell script and add it under **Platform scripts**. It writes mandatory policies for all users on the device:

|  |
| --- |
| $ErrorActionPreference = 'Stop'$policyRoot = 'HKLM:\SOFTWARE\Policies\OpenAI\Codex'if (-not (Test-Path -LiteralPath $policyRoot)) {  New-Item -Path $policyRoot -Force | Out-Null}New-ItemProperty -Path $policyRoot -Name PasswordManagerEnabled -PropertyType DWord -Value 0 -Force | Out-Null$cookieKey = "$policyRoot\CookiesBlockedForUrls"if (-not (Test-Path -LiteralPath $cookieKey)) {  New-Item -Path $cookieKey -Force | Out-Null}New-ItemProperty -Path $cookieKey -Name '1' -PropertyType String -Value 'https://example.com' -Force | Out-Null |

In [Microsoft Intune Platform scripts](https://learn.microsoft.com/en-us/intune/device-management/tools/run-powershell-scripts-windows), set **Run this script using the logged on credentials** to **No** and **Run script in 64-bit PowerShell host** to **Yes**, then assign it to your pilot group. After the script runs, restart ChatGPT desktop and [verify the policies](https://help.openai.com/articles/20001535#verify-the-policies).

For **Group Policy**, create Registry preference items for the same keys, value names, types, and values shown in the script, and apply them to your pilot devices.

Registry value formats:

* **Booleans:** REG\_DWORD, with 0 for false and 1 for true.
* **String lists:** A subkey named after the policy, with numbered REG\_SZ values (1, 2, and so on). When updating a list, remove numbered values that no longer apply.
* **Structured policies:** Follow the policy reference's Windows encoding. For example, ExtensionSettings stores its dictionary as a JSON string in a REG\_SZ value.

For per-user policy, use the same path under HKEY\_CURRENT\_USER and deploy in the intended user's context. A script running as SYSTEM does not write to the signed-in user's HKEY\_CURRENT\_USER. For policies that support recommended defaults, use the Recommended subkey beneath the ChatGPT desktop root.

**Existing Chrome policy:** ChatGPT desktop currently falls back to SOFTWARE\Policies\Google\Chrome separately in each hive if it cannot open that hive's ChatGPT desktop key. A readable ChatGPT desktop key, including an empty one, stops fallback for that hive; missing individual values are not filled from Chrome. To keep both scopes separate from Chrome, provision a readable ChatGPT desktop key in both HKLM and each applicable user's HKCU.

## macOS: Jamf Pro or Microsoft Intune

Create a configuration profile that sets **forced (mandatory) managed preferences** in the com.openai.codex domain. For **Jamf Pro**, first save the following as com.openai.codex.plist:

|  |
| --- |
| <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>PasswordManagerEnabled</key>  <false/>  <key>CookiesBlockedForUrls</key>  <array>    <string>https://example.com</string>  </array></dict></plist> |

* **Jamf Pro:** Use a computer configuration profile's **Application & Custom Settings** payload, upload the plist, and set the preference domain to com.openai.codex. See [Jamf's custom-settings instructions](https://learn.jamf.com/r/en-US/technical-articles/Deploying_Custom_Computer_Configuration_Profiles_Using_the_Application_and_Custom_Settings_Payload).
* **Microsoft Intune:** Create a macOS **Templates > Preference file** profile and set **Preference domain name** to com.openai.codex. For this uploader, save only the key/value contents inside the example's outer <dict>; omit the XML declaration, DOCTYPE, <plist>, and outer <dict> wrappers. Keep the nested <array> intact. See [Intune's preference-file instructions](https://learn.microsoft.com/en-us/intune/device-configuration/templates/configure-preference-file-macos).
* **Other MDM tools:** Use their custom managed-preferences workflow or deploy an equivalent .mobileconfig profile for this domain.

Assign the profile to your pilot devices and confirm installation. Restart ChatGPT desktop and [verify the policies](https://help.openai.com/articles/20001535#verify-the-policies). Use managed preferences: a normal user preference written with defaults write does not make a policy mandatory.

## Linux: configuration management

Use a tool such as **Ansible, Puppet, or Chef** to deliver a JSON policy file to your devices, just as you would for Chrome.

1. Create /etc/opt/codex/policies/managed/ if needed.
2. Deploy a JSON file directly into that directory using your configuration-management tool, package, or device-management agent.
3. Make the directories and file owned by root, readable by ChatGPT desktop users, and writable only by trusted administrators. Typical permissions are 0755 for directories and 0644 for files.
4. Restart ChatGPT desktop and [verify the policies](https://help.openai.com/articles/20001535#verify-the-policies).

Example /etc/opt/codex/policies/managed/browser.json:

|  |
| --- |
| {  "PasswordManagerEnabled": false,  "CookiesBlockedForUrls": ["https://example.com"]} |

Use JSON Booleans, numbers, arrays, and objects as required by each policy. Place files directly in managed/; nested directories are not read. Avoid defining the same policy in multiple files.

# Verify the policies

1. Confirm that your deployment tool delivered the registry values, installed profile, or JSON file to a pilot device.
2. Quit and reopen ChatGPT desktop. Open an in-app browser tab and go to chrome://policy **inside ChatGPT desktop**.
3. Select **Reload policies**. Check each policy's value, source, scope, level, and status. For the mandatory examples, expect source **Platform**, level **Mandatory**, and no policy error.
4. Test the intended behavior in that browser. A policy appearing on this page confirms it was read; it does not by itself prove that the affected feature behaves as intended.

Some policies require a full app restart even after reloading policies. Complete the pilot checks before expanding the deployment.

If a policy is missing, check its spelling, target location, assignment, and read permissions. For an error or ignored policy, check the value type, supported platform and policy level, and any conflicting policy reported on chrome://policy.

To change or remove a policy, update the deployment that supplied it and remove obsolete registry entries or file keys. Unassigning a script alone does not undo values it wrote. Restart ChatGPT desktop and verify again; removing a Windows ChatGPT desktop root can re-enable Chrome fallback.

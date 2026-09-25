<!-- source: https://help.openai.com/en/articles/20001502-managing-sharepoint-site-access-and-sensitivity-label-exclusions -->

# Managing SharePoint site access and sensitivity-label exclusions

Learn how to manage SharePoint site access and exclude supported files with selected sensitivity labels in ChatGPT.

Updated: yesterday

Workspace administrators can use SharePoint controls to allow approved site collections, block selected site collections, and exclude supported files with selected Microsoft Purview sensitivity labels.

A SharePoint site collection, also called an SPSite, can contain multiple sites. A collection rule applies to the entire collection, subject to each user’s existing Microsoft permissions. It does not grant a user access to content they cannot access in Microsoft 365.

Site restrictions apply to supported SharePoint search, browsing, file retrieval, and read/write actions. OneDrive access is managed separately.

Choose the access mode that matches your policy:

* **Allowed sites:** With a nonempty allowlist, users can access only the listed site collections through the app.
* **Blocked sites:** Users can access site collections other than those on the deny list, subject to their Microsoft permissions.

Only one list can contain entries at a time. An empty allowlist does not block all sites. When both lists are empty, SharePoint site restrictions are removed; Microsoft permissions and other configured controls still apply.

## Availability

The controls and workspace Admin API require enablement for your workspace. Available controls include site-collection allowlists, site-collection deny lists, CSV site imports, and sensitivity-label exclusions.

Rules apply to whole site collections. Exact individual-site, folder, or file scoping and **Microsoft Sites.Selected** enforcement are not included in these site-collection controls.

## Before you begin

* Identify the site collections your organization wants to allow or block.
* Obtain each collection’s GUID. A full Microsoft Graph site ID contains the collection GUID as its middle value. The Admin API uses collection GUIDs; the UI CSV importer can also extract them from Graph site-ID triples.
* Enable the SharePoint app’s required Microsoft permissions in both ChatGPT’s permission settings and Microsoft Entra, including `Sites.Read.All` and `Files.Read.All`. These controls filter access on the OpenAI side; they do not replace Microsoft’s delegated permissions.
* For sensitivity-label exclusions, ask your Microsoft 365 or Purview administrator for the immutable GUID of each label without encryption.
* For API administration, obtain your workspace UUID, a ChatGPT workspace Admin key, and a Microsoft Graph token if you need to resolve SharePoint URLs. The two credentials have different purposes.

## About the OpenAI Cookbook

The OpenAI Cookbook is OpenAI’s public collection of example code and guides. This article uses its [SharePoint site-access guide](https://github.com/openai/openai-cookbook/blob/main/examples/chatgpt/sharepoint_site_access/sharepoint_site_access.md) and [Python administration script](https://github.com/openai/openai-cookbook/blob/main/examples/chatgpt/sharepoint_site_access/sharepoint_site_access_admin.py), both hosted on GitHub. You can open these links in your browser to read the files. To run the script, download it and follow the guide’s setup and command instructions.

Throughout this article, “Cookbook” refers to that SharePoint guide, and “Cookbook utility” refers to the linked Python script. Use these references for command examples and API-based allowlist management.

## Set up credentials for API administration

Note: You need to be a workspace administrator to be able to create admin keys. [Read more.](https://help.openai.com/articles/20001407)

### Create a ChatGPT workspace admin key

1. Open the [ChatGPT admin console](https://admin.openai.com) and select the intended workspace.
2. Go to **Credentials** and select **Admin keys**.
3. Create a key with **Restricted** permissions and set **Apps** to **Write**.
4. Store the key securely. This key authorizes reading and changing the SharePoint policy for your workspace.

The required permission is `chatgpt.enterprise.apps.write`. Note that an OpenAI API Platform key and a Microsoft Graph token cannot replace a ChatGPT workspace Admin key.

For more information, see: [Managing Admin keys in the Credentials tab](https://help.openai.com/articles/20001407). For the script’s credential environment variables and secure input example, see the [Cookbook credential instructions](https://github.com/openai/openai-cookbook/blob/main/examples/chatgpt/sharepoint_site_access/sharepoint_site_access.md#create-a-workspace-admin-api-key).

### Obtain a Microsoft Graph token

Use your organization’s approved Microsoft authentication process. For an interactive lookup, if your organization permits Graph Explorer:

1. Open Microsoft Graph Explorer and sign in with a work account in the tenant that contains the SharePoint sites.
2. Select the permissions needed to read the sites, typically `Sites.Read.All`, using **Modify permissions** or **Consent to permissions**. Ask your Microsoft administrator to approve access if your organization requires it.
3. Open the **Access token** tab and copy the token for use with Microsoft Graph.

For the Microsoft instructions, see [Work with Graph Explorer](https://learn.microsoft.com/en-us/graph/graph-explorer/graph-explorer-features).

The Graph token resolves SharePoint URLs into identifiers. The ChatGPT Admin key reads or updates the ChatGPT policy. The Cookbook utility needs the Graph token only for commands that resolve URLs; reading or clearing an existing allowlist requires only the ChatGPT Admin key.

Do not put either credential in source control, shared documents, screenshots, or logs.

## Find a site collection GUID

### Use the SharePoint site URL

1. Open the SharePoint site while signed in to Microsoft with an account that can access it.
2. Append `/_api/site/id` to the site URL. For example, use `https://contoso.sharepoint.com/sites/Finance/_api/site/id`.
3. Copy the GUID returned in the response.

Note: example domains and identifiers in this article are placeholders.

### Use Microsoft Graph

Microsoft Graph returns a site ID with three comma-separated components: the hostname, the site-collection GUID, and the site GUID. Use the middle value for a site-collection rule. Different site URLs can resolve to the same collection GUID.

For the lookup and identifier examples, see [Understand SharePoint site identifiers](https://github.com/openai/openai-cookbook/blob/main/examples/chatgpt/sharepoint_site_access/sharepoint_site_access.md#understand-sharepoint-site-identifiers). To resolve multiple URLs without changing ChatGPT policy, use the [Cookbook inspect instructions](https://github.com/openai/openai-cookbook/blob/main/examples/chatgpt/sharepoint_site_access/sharepoint_site_access.md#inspect-sharepoint-urls) and [Python administration script](https://github.com/openai/openai-cookbook/blob/main/examples/chatgpt/sharepoint_site_access/sharepoint_site_access_admin.py).

For Microsoft’s lookup requirements, see [Get a SharePoint site by path](https://learn.microsoft.com/en-us/graph/api/site-getbypath?view=graph-rest-1.0).

## Manage allowed and blocked site collections

### Use workspace controls

1. Open the SharePoint app’s **Safety & Security Controls** in your workspace.
2. Under **Access mode**, select **Allowed sites** or **Blocked sites**.
3. Add the site collections to the selected list. You can also use the CSV upload described below.
4. Review your changes and select **Save**.
5. Check the saved policy and test your configuration.

Sites added through the Admin API appear in the workspace controls. Sites added in the UI are also available through the API. You can add or remove entries through either surface; the method used to add a site does not lock it to that method.

### Switch between allowed and blocked sites

Only one list can contain entries at a time. Before adding entries in the other mode, clear the existing list and save that change. Then select the other mode, add the intended collections, and save again.

**Clearing the active list changes access immediately when saved.** Clearing an allowlist removes its site restriction; clearing a deny list removes its blocks. Plan the transition with other admins because the interval between clearing one list and saving the other may allow access that your final policy will restrict.

### Upload site collections from CSV

CSV upload supports site collections only. To exclude files by sensitivity label, add the label GUIDs under **Excluded sensitivity labels without encryption**.

1. Open **Safety & Security Controls** and select the intended **Access mode**.
2. Prepare a CSV of site-collection GUIDs or Microsoft Graph site-ID triples. Use one identifier format throughout the file.
3. Select **Upload CSV file** and choose the file.
4. Review the import result and the selected list. Resolve any row errors or warnings before continuing.
5. Select **Save** to apply the changes, then check the saved list.

CSV requirements and behavior:

* Maximum file size: **1 MB**.
* Headers are optional.
* Use one collection GUID per row, or Graph site-ID triples. Triples can be quoted in one field or split across three columns.
* Graph triples are converted to collection GUIDs. Importing a triple does not create an exact-site rule.
* Imports add to the selected list and preserve existing entries. Duplicate collections are deduplicated; the import count reports newly added collections.
* Mixed formats and malformed rows are rejected. An upload containing only site URLs displays a warning and does not add sites. Resolve URLs into collection GUIDs first.
* An upload changes the draft list only. It does not update workspace access until you select **Save**.
* The CSV upload described here manages site collections. Configure sensitivity-label exclusions separately.

If you have a CSV of SharePoint URLs, the [Cookbook utility’s CSV workflow](https://github.com/openai/openai-cookbook/blob/main/examples/chatgpt/sharepoint_site_access/sharepoint_site_access.md#prepare-a-list-of-sites) can resolve them and manage an allowlist through the API. Its `site_url` or `url` input is a different format and workflow from the UI’s identifier upload.

### Understand policy and request limits

The default policy limit is **10,000 site collections**. Higher workspace policy limits, up to 120,000 site collections, require enablement by OpenAI; contact your OpenAI team before planning a larger deployment.

Individual API mutations and the current Cookbook script accept up to **10,000 collection GUIDs per request**. A higher workspace policy limit does not raise this per-request limit. Count unique site collections, not source URLs: multiple URLs can refer to the same collection.

### Use the workspace Admin API

Use your workspace UUID and ChatGPT workspace Admin key with `https://api.chatgpt.com`.

For maintained allowlist commands and request examples, use the Cookbook:

* [Read the existing allowlist](https://github.com/openai/openai-cookbook/blob/main/examples/chatgpt/sharepoint_site_access/sharepoint_site_access.md#read-the-existing-allowlist).
* [Preview and add site collections](https://github.com/openai/openai-cookbook/blob/main/examples/chatgpt/sharepoint_site_access/sharepoint_site_access.md#preview-and-add-site-collections). Additions preserve existing allowed collections.
* [Remove a site collection](https://github.com/openai/openai-cookbook/blob/main/examples/chatgpt/sharepoint_site_access/sharepoint_site_access.md#remove-a-site-collection).
* [Clear the allowlist](https://github.com/openai/openai-cookbook/blob/main/examples/chatgpt/sharepoint_site_access/sharepoint_site_access.md#clear-the-allowlist).

Review the current policy before making changes, then read it again and test the resulting access. Removing the last allowed collection or clearing the allowlist removes that site restriction. Do not send an empty add request unless you intend to remove allowlist restrictions.

The public Cookbook utility currently manages **allowlists only**. It does not manage deny lists or sensitivity-label exclusions. Use the workspace controls described above for those tasks.

## Exclude files with sensitivity labels

### Find the label GUID

Ask your Microsoft 365 or Purview administrator for the intended label’s immutable GUID. Use the GUID, not its display name.

An administrator can list labels through Microsoft Graph. The token needs the applicable `SensitivityLabel.Read` or `SensitivityLabels.Read.All` permission. Match the intended label’s name to its ID and check its protection settings.

For requirements and examples, see [List sensitivity labels](https://learn.microsoft.com/en-us/graph/api/tenantdatasecurityandgovernance-list-sensitivitylabels?view=graph-rest-1.0) and [Sensitivity label properties](https://learn.microsoft.com/en-us/graph/api/resources/security-sensitivitylabel?view=graph-rest-1.0). These label permissions are separate from the site-read permission used to resolve SharePoint URLs.

### Add label exclusions

1. Open the SharePoint app’s **Safety & Security Controls**.
2. Enter each non-encrypted label’s GUID under **Excluded sensitivity labels without encryption**.
3. Save the configuration and test a supported file with the excluded label.

Files with matching supported labels are excluded from SharePoint app results. Files carrying labels that apply encryption are already excluded by default.

## Test your configuration

Use test files and accounts approved by your organization. Before testing, confirm that the same Microsoft account can access each file directly in SharePoint.

1. In **Allowed sites** mode with a nonempty list, check a file in an allowed collection and a file in an unlisted collection. Only the allowed collection should be accessible through the app.
2. In **Blocked sites** mode, check a file in a blocked collection and a file in an unblocked collection. The blocked collection should be unavailable; the unblocked collection remains subject to Microsoft permissions and other controls.
3. Check a supported test file carrying an excluded sensitivity label. It should not appear in the app’s results.
4. After an API change, compare the saved UI list with the policy returned by the API.
5. After a CSV upload, save the changes and reopen the controls to confirm that the intended collections were retained.

If results differ from the intended policy, check the workspace, selected access mode, saved list, collection GUIDs, label GUIDs, supported file type, and the user’s Microsoft permissions. Do not clear a list as a troubleshooting step unless you intend the resulting access change.

For help with missing controls or unexpected access, see: [Contacting OpenAI Support](https://help.openai.com/articles/6614161). Do not include Admin keys or Microsoft Graph tokens in your support request.

## Understand the limitations

* A collection rule covers the entire site collection. It cannot limit access to a particular subsite, folder, or file.
* SharePoint site restrictions do not automatically restrict OneDrive access.
* Sensitivity-label filtering applies only where Microsoft Graph exposes supported label metadata, including supported Office documents, PDF, and MP4 files.
* Unsupported types for sensitivity labels, such as TXT and CSV files, are treated as unlabeled. They remain accessible if otherwise permitted. This file-type limitation is separate from uploading a CSV to configure site access.
* The CSV upload and public example utility do not configure sensitivity-label exclusions. This article does not document a bulk label-management API.
* A saved policy or successful API response is not a substitute for testing access with the intended account.

## Use the Python administration utility

The full example code and commands are maintained in the OpenAI Cookbook:

* [Administration guide](https://github.com/openai/openai-cookbook/blob/main/examples/chatgpt/sharepoint_site_access/sharepoint_site_access.md).
* [Python administration script](https://github.com/openai/openai-cookbook/blob/main/examples/chatgpt/sharepoint_site_access/sharepoint_site_access_admin.py).
* [Offline test file](https://github.com/openai/openai-cookbook/blob/main/examples/chatgpt/sharepoint_site_access/test_sharepoint_site_access_admin.py).

Use Python 3.10 or later. The utility uses the Python standard library. Read the guide before running it and use dry runs to review changes.

The current utility reads credentials from environment variables; use the guide’s secure input instructions. It requires explicit confirmation for clearing an allowlist. A removal can execute without that confirmation, so review a removal with a dry run first.

For retry behavior and optional idempotency keys, see [Retry a policy update safely](https://github.com/openai/openai-cookbook/blob/main/examples/chatgpt/sharepoint_site_access/sharepoint_site_access.md#retry-a-policy-update-safely). Use idempotency keys only when the workspace supports them, and inspect the current policy after an ambiguous failure.

The utility does not enable workspace features or verify enforcement. Its offline tests use mocked Microsoft Graph and ChatGPT Admin API calls.

Multi-request changes are not atomic. If a multi-collection removal fails partway through, earlier removals may already have succeeded. Read the current policy before retrying.

## FAQ

### Do site controls replace Microsoft permissions?

No. The app still uses each user’s Microsoft permissions. OpenAI applies the configured site filtering before responses are shown to the user and model.

### Does an empty allowlist block all sites?

No. An empty allowlist does not mean “block all.” If a deny list contains entries, those collections remain blocked. When neither list contains entries, users’ Microsoft permissions and other configured controls determine access.

### Are Admin API changes logged?

Admin API policy changes are recorded through workspace audit and compliance logging.

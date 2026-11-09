<!-- source: https://help.openai.com/en/articles/20001610-managing-outlook-email-sensitivity-label-exclusions -->

# Managing Outlook email sensitivity-label exclusions

Exclude Outlook emails with selected Microsoft Purview sensitivity labels from your ChatGPT workspace's Outlook access.

Updated: 19 days ago

Workspace owners and admins can exclude Outlook emails carrying selected Microsoft Purview sensitivity labels from ChatGPT's Outlook access.

Excluded emails are filtered from search and list results and blocked on direct reads and actions targeting those emails. Their attachments are also blocked through the Outlook app.

Each user's existing Microsoft permissions still apply. These controls do not change labels or permissions in Microsoft 365.

## Availability

These controls are available in Enterprise workspaces where enabled. Confirm that you're in the intended ChatGPT workspace, that you're a workspace owner or admin, and that the app is enabled. If **Safety & Security Controls** is still missing, contact your OpenAI account team or [OpenAI Support](https://help.openai.com/articles/6614161). Include your workspace plan, your role, and the control you can't find.

## Before you begin

Obtain the GUID of each sensitivity label you want to exclude from your Microsoft 365 or Purview administrator. Use the label GUID rather than its display name.

Add each label explicitly, including sublabels you want to exclude.

# Configure label exclusions

1. Open Outlook Email in your workspace's app settings.
2. Open **Safety & Security Controls**.
3. Under **Excluded Outlook email sensitivity labels**, enter a label's GUID.
4. Select **Add label**.
5. Repeat for each label you want to exclude.
6. Select **Save**.

An empty list adds no label-based restrictions. Unlabeled emails remain eligible under the user's Microsoft permissions and other configured controls.

# Test your configuration

Use non-sensitive test content. For write tests, use a test item and a harmless change.

1. Confirm that the test account can open the test emails directly in Outlook.
2. Start a new ChatGPT conversation and request an email without an excluded label.
3. Request an email carrying an excluded label. It should be unavailable through the Outlook app.
4. Test an attachment belonging to an excluded email. It should also be unavailable through the Outlook app.
5. If members use actions targeting existing emails, test an approved action against permitted and excluded emails.

Policy changes can take time to propagate. Verify fresh requests after saving.

## If excluded content still appears

Confirm whether the response used a new request through Outlook Email. Information already in a conversation or Memory is not evidence that the app retrieved it again. Don't paste excluded content into the test prompt.

Reopen **Safety & Security Controls** and confirm the saved label GUIDs. Ask your Microsoft administrator to verify the label on the email, including the exact sublabel GUID. A label inside an attached file is not an email-label match.

If a fresh app request still retrieves excluded content, contact your OpenAI account team or [OpenAI Support](https://help.openai.com/articles/6614161). Include the relevant saved restrictions, an identifier or link for the affected email, if available, the connected account and workspace, the test time and time zone, and what happened. Include a request ID if one is shown; otherwise, say it wasn't shown. Don't include the excluded content itself.

# Change the exclusions

Add or remove label GUIDs under **Excluded Outlook email sensitivity labels**, then select **Save**. Reopen the settings and confirm the saved list.

Removing a label from the list allows emails with that label to become eligible again, subject to Microsoft permissions and other configured controls.

# Understand the limitations

* Only explicitly listed label GUIDs are excluded. Listing a parent label does not automatically exclude its sublabels.
* Labels inside attachment files are not checked independently.
* Exclusions do not grant access to emails or attachments the connected Microsoft account cannot access.
* These settings do not alter sensitivity labels or permissions in Microsoft 365.
* Changing these controls does not delete content already retrieved into conversations or remove saved memories. Manage conversations and Memory separately. For removal options, see: [Memory in ChatGPT](https://help.openai.com/articles/8590148) and [Deleting and archiving chats](https://help.openai.com/articles/8809935).

For connecting Outlook Email and reviewing its permissions, see: [Outlook Email and Calendar apps in ChatGPT](https://help.openai.com/articles/12512241).

# FAQ

## Are attachments to an excluded email also blocked?

Yes. Attachments belonging to an excluded email are blocked through the Outlook app.

## Are labels inside attachment files checked separately?

No. These exclusions apply to labels on the email. They do not independently scan sensitivity labels inside attached files.

## What happens when the exclusion list is empty?

The list adds no label-based restrictions. Microsoft permissions and other configured controls still apply.

## Does excluding a parent label also exclude its sublabels?

No. Add each sublabel's GUID separately.

## How do I confirm the active exclusion policy?

Reopen **Safety & Security Controls** and confirm the saved label GUIDs, including any sublabels you intend to exclude. After making changes, select **Save**, then test permitted and excluded emails with fresh requests. Existing conversation content or Memory does not show whether Outlook retrieved an email again.

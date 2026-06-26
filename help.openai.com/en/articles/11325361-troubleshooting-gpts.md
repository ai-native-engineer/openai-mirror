<!-- source: https://help.openai.com/en/articles/11325361-troubleshooting-gpts -->

# Troubleshooting GPTs

Diagnose common GPT issues related to performance, configuration, sharing, and workspace policies.

Updated: 21 days ago

Availability for GPT features varies by plan and workspace permissions. For current availability details, see: [GPTs in ChatGPT](https://help.openai.com/articles/8554407).

# Performance issues

## GPT is not following instructions

Review the GPT’s instructions for conflicting or overly broad guidance.

* Shorten instructions where possible.
* Remove duplicate or conflicting rules.
* Use more explicit structure for multi-step behavior, such as: *When X happens, do Y.*
* Add one or two clear examples if the behavior needs to be more consistent.

If the GPT still behaves inconsistently, test smaller changes in Preview so it is easier to identify what improved or broke the behavior.

## GPT is not using attached knowledge files well

Check whether the answer should actually depend on the uploaded files.

* Use clearer, more text-forward source files when possible.
* Try narrower prompts that refer more directly to the uploaded material.
* Confirm that the needed information is actually present in the files.
* If possible, simplify complex PDFs, slides, or layouts into cleaner text-based formats.
* Avoid relying on images alone. Images included in files may not be reliably interpreted. Ensure you include clear text or annotations describing any important visuals.

Knowledge works best for reference material. Put rules, tone, and workflow behavior in instructions, not in uploaded files.

## Links are not clickable

If the GPT is returning plain text instead of linked text, update the instructions to say how links should be formatted.  
  
For example, you can tell the GPT to format links as Markdown: [text](url).  
  
This is usually a formatting issue in the GPT’s instructions, not a sharing or access problem.

## File downloads fail

If a GPT cannot generate or return downloadable files, first confirm that setting **Code Interpreter & Data Analysis** is enabled for the GPT.  
  
If the issue continues:

* Retry with a smaller output file.
* Check whether the file generation step completed successfully.
* Test the same task again in Preview.

Some download failures are generic file-link errors, so the issue is not always the GPT configuration itself.

# Issues while creating or editing a GPT

## Capabilities are missing

If a capability is not visible, it may not be available for that account or workspace.  
  
Check whether:

* The feature is available for the respective subscription plan.
* The workspace allows that feature.
* The user has the required role permissions in a managed workspace.

For workspace restrictions, see: [Managing GPT access in Enterprise and Edu workspaces](https://help.openai.com/articles/8555535).

## Apps or actions are unavailable

Apps and actions are separate integration paths, and one GPT cannot use both at the same time.  
  
Check whether:

* The workspace has apps disabled.
* The GPT already has actions configured, which prevents apps from being used.
* The GPT uses action domains that are not allowed by workspace policy.

In managed workspaces, admins can disable apps for workspace-created GPTs and can restrict which domains GPT actions can use.

# Issues when sharing

## Sharing options are grayed out

Sharing and publishing options can be limited by plan, workspace policy, or the GPT’s configuration.  
  
Check whether:

* The workspace allows that level of sharing.
* The GPT is eligible for public sharing.

The GPT uses apps, which can block public link sharing and GPT Store publishing.

* The GPT uses public actions without a valid Privacy Policy URL.
* The Builder Profile requirements for public publishing are complete.

For more on sharing and publishing, see: [Sharing and Publishing GPTs.](https://help.openai.com/articles/8798878)

## GPT is inaccessible or not found

In managed workspaces, a GPT may be unavailable because of how it was shared or because of workspace restrictions.  
  
Check whether:

* The GPT was shared at a level the workspace allows.
* The GPT is a third-party GPT blocked by workspace policy.
* Data residency requirements limit access to workspace-created GPTs only.
* The GPT depends on Apps or Actions that are not allowed in that workspace.

If the GPT uses blocked Action domains, the GPT may still be visible, but the Actions themselves may be unavailable or rejected.

## Public publishing is blocked

If public publishing is blocked, review the GPT’s public publishing requirements.  
  
Check whether:

* The **Builder Profile** is complete.
* The GPT has a category if one is required.
* Any public Actions have a valid Privacy Policy URL.
* The GPT was blocked by a moderation or policy review.

If an appeal option is available, you can submit an appeal. While an appeal is pending, you may still be able to use the GPT privately, but you will not be able to edit, update, or share it with others until the appeal is resolved or canceled.

# Report a GPT for content violation

If you believe a GPT violates policy or should be reviewed, use the in-product reporting option when it is available. For detailed instructions, see: [Reporting Content in ChatGPT and OpenAI Platforms](https://help.openai.com/articles/10245791).  
  
When you report an issue, include:

* The GPT name or link.
* What happened?
* Timestamps, if relevant.

# Still not working?

If you are not sure whether the issue is caused by the GPT’s setup, sharing configuration, or workspace policy:

1. Test the GPT in Preview.
2. Confirm which capabilities, Apps, or Actions are enabled.
3. Check how the GPT is shared.
4. In managed workspaces, review workspace settings and role permissions.
5. If the issue involves blocked publishing, missing access, or policy review, check the related sharing or admin article.

## Before escalating

Before escalating the issue, collect:

* The GPT link.
* Whether the issue affects one user or many users.
* Whether it only happens in a specific workspace.
* Whether the GPT uses apps or actions.
* Whether the problem started after a recent edit or policy change.

## Contact OpenAI Support

For instructions on reaching out to OpenAI Support, see: [How can I contact support?](https://help.openai.com/articles/6614161)

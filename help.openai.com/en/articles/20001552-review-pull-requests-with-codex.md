<!-- source: https://help.openai.com/en/articles/20001552-review-pull-requests-with-codex -->

# Review pull requests with Codex

Find pull requests, inspect changes, and work through review feedback with Codex.

Code Review brings pull requests, code changes, review findings, comments, and checks into one place. You can review someone else’s changes, follow feedback on your own pull requests, or ask Codex to explain a change before you respond.

The Code Review plugin supports review on desktop and web. GitLab merge-request review is available as a preview. GitLab cloud code reviews are not available.

# Before you begin

Use a repository account that can access the pull request you want to review. Your repository permissions determine what you can read or change.

In a managed workspace, the Code Review plugin and any required app connection must be available to you. Installing a plugin does not grant access to a repository.

For plugin setup and workspace controls, see [Plugins in ChatGPT and Codex](/en/articles/20001256-plugins-in-chatgpt-and-codex).

# Find a pull request

Open Code Review to find pull requests you’ve authored or been asked to review. Use search and filters to narrow the list, then select a pull request.

Check the repository, title, author, and branch to confirm you’re reviewing the intended change. The description explains the author’s goal; the diff shows the code that changed.

# Review the changes

1. Read the pull request description and summary.
2. Inspect the changed files and relevant lines in the diff.
3. Review findings and existing comments.
4. Check test results, checks, and any unresolved merge conflicts.
5. Ask Codex about anything that needs more investigation.

Review generated findings against the relevant code before relying on them.

# Ask Codex about a pull request

Use the pull request’s conversation to ask questions about the changes or investigate a finding. Include the behavior or review criteria you care about. For example:

* “Explain how this change affects sign-in.”
* “Check whether the new error path releases the database connection.”
* “Show me the code that supports this finding.”
* “Compare this revision with the review feedback and identify anything still unresolved.”

You can also ask Codex to prepare a fix. Describe the change you want and any limits on its scope, then inspect the resulting diff and test results.

For example: “Address the error-handling finding. Keep the change limited to this function and add a test for the failing case.”

Review the result before submitting comments, committing changes, or merging.

# Review GitLab merge requests

The GitLab preview brings merge requests into Code Review. You can inspect changes and use Codex to help understand and work through review feedback.

Use the GitLab connection for the account and projects you intend to review. For connection options and repository permissions, see [Connecting GitLab to ChatGPT and Codex](/en/articles/20001486-connecting-gitlab-to-chatgpt-and-codex).

The in-app preview does not include GitLab cloud code reviews. Connecting GitLab or seeing a merge request in Code Review does not enable automatic cloud review for that repository.

# Frequently asked questions

## Can I review local changes before creating a pull request?

Yes. You can ask Codex to review local changes. See the [Code review guide](https://learn.chatgpt.com/docs/code-review) for local review options.

## Does this move my existing cloud reviews to the new cloud environments?

No. This update does not migrate existing cloud code review to the new cloud environments.

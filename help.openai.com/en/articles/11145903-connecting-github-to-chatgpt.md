<!-- source: https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt -->

# Connecting GitHub to ChatGPT

Access your GitHub repositories directly in ChatGPT to analyze, search, and cite code.

Updated: 9 days ago

# Overview

You can connect your GitHub repositories to ChatGPT apps, as well as ChatGPT agent, to ask questions based on your own code.  
  
When you connect to GitHub, ChatGPT can pull live data from your repositories—code, README files, and other docs—and reason over it in real time, either with an app with sync, an app with file search, or an app with deep research. Just connect, ask a question, and ChatGPT will read, analyze, and cite the relevant snippets straight from your GitHub content.

**Note:** GitHub App availability may vary by ChatGPT plan and experience. For example, ChatGPT Plus users may not see the GitHub App in the standard ChatGPT experience, even if it is available in other experiences such as Deep Research or Agent Mode.

# Connecting GitHub to ChatGPT

You can connect GitHub to ChatGPT by selecting **Settings** → **Apps** and locating **GitHub** in the [ChatGPT app directory](/en/articles/11487775-apps-in-chatgpt).

From there, you’ll be directed to GitHub to install and authorize the ChatGPT app, and then select the repositories ChatGPT can access. After connecting, ChatGPT may ask which repositories you use most so it can sync them for improved speed and quality. This sync selection is separate from GitHub repository access; ChatGPT can still access repositories you allowed in GitHub even if they aren’t selected for sync.

To change which repositories ChatGPT can access, go to **Settings** → **Apps**, open **GitHub**, then select **Choose repositories** (or **Configure Repositories on GitHub**) to open GitHub’s repository access page. To disconnect GitHub from ChatGPT, go to **Settings** → **Apps**, open **GitHub**, then select **Disconnect**.

## Why don’t I see some of my repositories after connecting ChatGPT to GitHub?

Generally there’s a ~5 minute delay before your repositories will display as available in ChatGPT.

Additional reasons why you may not see a repository yet:

* **Private or newly created repositories:** If your repository is private or was created after initially connecting to GitHub, it may not appear immediately in ChatGPT. Please visit [this link](https://github.com/apps/chatgpt-codex-connector/installations/select_target) or tap on the **Gear** icon in the Settings page for Github in ChatGPT to configure access to the desired repositories.

* **Repository requires GitHub admin approval:** Your repository may be blocked by your GitHub admin from being connected to ChatGPT. Please visit [this link](https://github.com/apps/chatgpt-codex-connector/installations/select_target) or tap on the **Gear** icon in the Settings page for Github in ChatGPT. From here, you can “Request” access to repositories that can be approved by your IT administrator.

* **Repositories not indexed by GitHub:** Due to GitHub’s search indexing behavior, the repository may not be in GitHub’s index, and therefore isn’t visible to the ChatGPT app when searching. You can manually trigger indexing by going to GitHub and performing a search for the repository using this format: `repo:{username/repo_name} import` (e.g., repo:openai/codex import). Note that the index may take ~5-10 minutes before it becomes available to the connector.

# Data and Privacy

## How ChatGPT works with Github

ChatGPT forms search queries from your prompts to find relevant information in your connected GitHub repositories and sends these queries to GitHub. For example, if you ask, “Can you show me where I handled file uploads in the backend?” ChatGPT might search your GitHub repositories using a query like “file upload handler backend.” If needed, it may do a few different searches to find the most relevant code or files.

## Will OpenAI use content from GitHub to train its models?

By default, content sent by customers using business offerings—such as ChatGPT Business, Enterprise, Edu, and our API—is not used to improve our models. Please see our [Enterprise Privacy page](https://openai.com/enterprise-privacy/) for information on how we use business data.  
  
When using our services from an individual subscription, we may use your content to train our models if your “Improve the model for everyone” setting is on. You can read more about how your data is stored and used in [this article in our help center](/en/articles/7730893-data-controls-faq).  
  
Data Residency is supported for Github in all available regions. Read more about Data residency.

# FAQ

## How can GitHub admins approve the ChatGPT app?

GitHub admins can follow [these instructions](https://docs.github.com/en/organizations/managing-oauth-access-to-your-organizations-data/approving-oauth-apps-for-your-organization) to approve OAuth apps, such as the ChatGPT app, for their organization.

## How do I search for individual files in a repository?

You can only search for the name of your GitHub repositories. Searching for specific file names is not supported.

## Can I disallow specific repositories from being accessed by the ChatGPT app?

Yes, however this is controlled in GitHub settings. Admins can follow [these instructions](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/reviewing-github-apps-installed-in-your-organization) to forbid access to specific repositories.

## Can I push code, updates, or PRs to GitHub once I connect to ChatGPT?

The GitHub app in ChatGPT only lets you **read** from your repositories to analyze and search your code. If you want to generate, edit, and push code directly to GitHub, that’s available through our [Codex product.](https://developers.openai.com/codex)

## What if I have IP Allow List enabled on GitHub?

If you have IP Allow List enabled on GitHub at either the enterprise or organization-level, you will need to ensure that you add [OpenAI's egress IP blocks](https://developers.openai.com/codex/enterprise/#configure-the-github-connector-ip-allow-list) to the IP Allow List.

## Why can I use GitHub in Deep Research or Agent mode but not in Chat?

GitHub App availability can vary by ChatGPT plan and product experience. Some plans may allow the GitHub App in Deep Research or Agent mode but not in the standard ChatGPT experience. If you do not see GitHub in Chat, check your ChatGPT plan details.  
  
You can learn more in our [Codex Help Center article](/en/articles/11369540-using-codex-with-your-chatgpt-plan).

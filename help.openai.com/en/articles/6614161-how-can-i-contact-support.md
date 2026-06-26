<!-- source: https://help.openai.com/en/articles/6614161-how-can-i-contact-support -->

# How can I contact support?

Need assistance? Here's how to reach us and get the help you need.

Updated: 9 days ago

## Contacting Support

You can contact OpenAI Support by opening the chat bubble icon displayed at the bottom-right of [help.openai.com](https://help.openai.com).  
  
When you start a new chat, you’ll first interact with our virtual assistant. If the bot can’t resolve your issue and a human agent joins, please be prepared to share the details listed in the Best Practices checklist below so we can route and resolve your request as quickly as possible.

## Useful Resources

* For account, login, and billing issues, please refer to our dedicated section: [Account, Login, and Billing](https://help.openai.com/en/collections/3943089-account-login-and-billing)
* To check the current status of our services, visit: [status.openai.com](https://status.openai.com)

## Best Practices for Submitting a Support Request

To help us assist you most efficiently, please include the following information in your support request:

* **Description of the Issue**: Provide a clear and concise explanation of the problem you're experiencing.
* **Account Email Address**: Include the email address you use to sign in so Support can locate the correct account. If you're unsure or contacting from a different email, list any possible email addresses and the sign-in method used (Google/Apple/Microsoft/password). Do not share passwords or one-time codes.
* **Steps to Reproduce**: Outline the steps that led to the issue, if applicable.
* **Timestamps**: Include the date and time when the issue occurred, along with your time zone.
* **Account Email (and Plan)**: Provide the email address you use to sign in (and your subscription tier, if applicable) to help us locate and verify your account. Do not share passwords. If you have a different billing or alternate email, please mention that as well.
* **Request or Completion IDs**: If reporting an issue with the API, share any relevant IDs associated with the issue. See [API documentation](https://platform.openai.com/docs/api-reference/debugging-requests) about debugging requests.
* **Screenshots, Screen Recordings, and Code Snippets**: Attach any visual aids that can help illustrate the problem.
* Please ensure no personal or sensitive data is included.
* **Environment Details**: Include your browser name and version, operating system, device type, and whether you are on a corporate or home network.
* **Workspace or Organization ID**: If you're part of a ChatGPT Team, Business, or Enterprise workspace, provide the unique ID or workspace name.
* **Custom GPT Identifier**: If your issue involves a custom GPT, share the GPT's public link or ID.
* **Safety or Policy Flag Information**: If you received a policy violation or safety flag, include the exact message and any associated request ID.

Providing these details will enable our support team to address your concerns more effectively.

## Recording a HAR file for Troubleshooting UI Issues

In order to help with various issues with Interface of ChatGPT, Platform and other products, ChatGPT Conversations or other non-API-related scenarios, Support team may ask you to record a HAR file in your browser for replicating the issue.  
  
A HAR file, or HTTP Archive file, is **a JSON-formatted archive that logs a web browser's interactions with a website**. It captures details like requests, responses, headers, and timings, making it useful for troubleshooting and performance analysis  
  
  
**Recording a HAR File is easy and does not require technical skills**.  
  
See steps below:

1. Open Developer Tools by right-clicking the webpage and selecting "Inspect", or by pressing Ctrl+Shift+I (Windows/Linux) or Cmd+Opt+I (Mac).
2. Navigate to the "Network" tab.
3. Enable the "Preserve log" checkbox.
4. Click the "crossed circle" button to clear any existing logs from the Network tab.
5. (Important) Reproduce the issue while the network requests are recorded (specifically, perform the actions that lead to an error or other unexpected behavior that you are concerned about).
6. Click the download icon ("Export HAR (sanitized)..." button) to save the file to your computer.

You can use [this video guide](https://www.youtube.com/watch?v=y2yanWTNxGk) (not affiliated with OpenAI) as a reference point.  

<!-- yt-inline:y2yanWTNxGk -->
[![YouTube y2yanWTNxGk](https://img.youtube.com/vi/y2yanWTNxGk/hqdefault.jpg)](https://www.youtube.com/watch?v=y2yanWTNxGk)

<details>
<summary>자막: YouTube y2yanWTNxGk</summary>

_(자막 없음)_

</details>

  
Please be informed that HAR files may include personal or other sensitive data. You can use a tool like [Cloudflare's HAR sanitizer](https://har-sanitizer.pages.dev/) to remove any personal information before sharing. Some browsers, like Google Chrome, automatically sanitize the HAR file when saving.  
  
Note: The ChatGPT desktop app does not currently provide developer tools for HAR capture. If your HAR file exceeds the 25 MB attachment limit, upload it to a secure cloud storage location (e.g., Google Drive or Dropbox) and share a view-only link in your support ticket.

## Troubleshooting Common ChatGPT UI Issues

Try the steps below before escalating to Support:

* File Upload Failures: Ensure the file is under 20 MB, refresh the page, clear browser cache and cookies, disable extensions, or use an incognito/private window. Network filters (VPNs, proxies, firewalls) can also block uploads.
* SSO “No accounts found”: Sign in with the same Microsoft or Google account that owns or is invited to the workspace. Try a private window, sign out and back in, or ask an admin to invite the correct email if your organization recently changed domains.

## Enterprise and Business Admin Portal Guidance

Admins for ChatGPT Team, Business, and Enterprise plans can manage users and settings from the Admin Portal (Settings → Admin Console).

* Invite or remove members and manage seat assignments
* Configure SSO domains and SCIM provisioning
* Review usage and audit logs
* Set data retention, export controls, and policy settings

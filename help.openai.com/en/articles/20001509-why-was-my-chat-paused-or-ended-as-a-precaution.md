<!-- source: https://help.openai.com/en/articles/20001509-why-was-my-chat-paused-or-ended-as-a-precaution -->

# Why was my chat paused or ended as a precaution?

Learn what to review when a conversation is paused or ended as a precaution in ChatGPT, Codex, or the API.

Updated: 16 days ago

![Why was my chat paused or ended as a precaution?](https://images.ctfassets.net/j22is2dtoxu1/6RmCkmtl1jNaZUV6JUNVlk/5f656af2f7541f712df0c39f5624a040/e00a0c1a-d508-41a5-a9bc-a9431061ec0f.png?q=80&fm=webp&w=1065)

When using Astra models, to ensure agents interpret and follow your instructions correctly, we have a system that pauses or stops conversations across ChatGPT, Codex and the API if it detects the agent may not have been interpreting your instructions correctly in cases such as transferring sensitive data, accessing sensitive data, or making destructive changes.

If your conversation was paused or ended, this does not necessarily mean the agent made a mistake, only that it is worth reviewing the agent's actions to ensure it interpreted and followed your instructions correctly.

# What should I do if my chat was paused as a precaution?

* Open **Review findings** (or review the error returned by the API) and read the full explanation.
* Compare the findings with what you intended the agent to do, and the agent’s recent actions. You may want to check the relevant changes, tool calls and outputs.
* If you cannot determine whether continuing is appropriate, leave the task stopped.
* If continuation is available and you believe the actions of the agent were in fact safe and in accordance with your instructions, you can allow the conversation to continue.

If you allow the conversation to continue, the monitoring system remains active. The chat can be paused again if the system identifies another concern about how your instructions are being followed.

# What should I do if my chat was ended as a precaution?

In some cases, such as on mobile, or when your request is using zero data retention (ZDR), we are unable to provide a detailed explanation of what was detected, and the chat is not able to be resumed.

In this case we recommend reviewing the work the agent already performed to ensure it appears safe.

# How does OpenAI safeguard the API from the same issues?

## Which API requests are monitored by this system?

The same system described above asynchronously monitors requests to Astra in the Responses API, when either [persisted reasoning](https://developers.openai.com/api/docs/guides/reasoning?api-mode=responses#preserve-reasoning-across-calls), WebSockets, or OpenAI’s compaction is used. The Chat Completions API is not scanned by this specific monitoring system.

## How to detect that a conversation has been ended in the API by this system?

When the safety system detects that an agent might have interpreted instructions incorrectly in a significant way, the API returns an error with code misalignment\_policy\_violation.

In this case, the given chat is unable to be resumed.

You can learn more about how to detect and handle these errors [in our API documentation](https://developers.openai.com/api/docs/guides/safety-checks/misalignment-monitoring).

## What should my application do if such a case is detected?

You may want to consider setting up some system to enable somebody to review the actions that the agent took in such conversations, for example by providing a UI to the end-user to review.

Once a conversation is stopped for this reason in the API, it is unable to be resumed.

# How to centrally track potential misalignment events as an organization

We provide a webhooks system to enable enterprises to centrally track such events. You can configure webhooks to receive alerts for these events across the API, Codex and ChatGPT.

A webhook sends monitoring alerts to a server you operate. Webhooks are configured **separately** for the API (including Codex usage via the API) and for ChatGPT/Codex workspaces.

Choose the setup that matches how the agent is authenticated:

|  |  |  |
| --- | --- | --- |
| **Agent activity** | **Where to configure** | **Event to subscribe to** |
| API requestsCodex using an API key | API project Settings → Webhooks | safety.alert.created |
| ChatGPT/Codex activity | Admin Console → Credentials → Webhooks | safety.org\_alert.created |

## For API traffic (including Codex using an API key)

For API traffic, webhooks can be configured per project.

* Open the API Platform and select the project whose activity you want to receive alerts for.
* Go to project [**Settings → Webhooks**](https://platform.openai.com/settings/project/webhooks) and select **Create**.
* Enter an endpoint name and the public HTTPS URL of your webhook receiver.
* Subscribe to safety.alert.created and create the endpoint.
* Save the signing secret when it is displayed. Store it securely; it is shown only once.
* Test your receiver and confirm that it verifies signatures, acknowledges delivery, and routes notifications to the right team.

You need permission to manage webhooks in the selected project. If you use several API projects, configure the appropriate endpoint and subscription in each project.

For general setup, testing, and signature-verification examples, see the [API webhook guide](https://developers.openai.com/api/docs/guides/webhooks).

## For supported ChatGPT and Codex workspace activity

* Sign in as an owner of the eligible workspace and open the **Admin Console**.
* Select the workspace, then go to **Credentials → Webhooks**.
* Add your public HTTPS endpoint and subscribe to safety.org\_alert.created.
* Save the signing secret securely and test the receiver.

This configuration is for supported workspace activity, including Codex signed in with ChatGPT. It is separate from an API project’s webhook settings. Workspace ownership is required; an admin or member role alone is not sufficient.

If the setting is unavailable, check that you selected the intended workspace, that you are its owner, and that the feature is available for that workspace. For personal accounts, follow the pause or stop guidance shown in the product; this workspace setup is not a personal webhook setting.

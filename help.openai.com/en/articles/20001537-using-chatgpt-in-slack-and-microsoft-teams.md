<!-- source: https://help.openai.com/en/articles/20001537-using-chatgpt-in-slack-and-microsoft-teams -->

# Using @ChatGPT in Slack and Microsoft Teams

Work with your organization’s @ChatGPT assistant in Slack and Microsoft Teams, and understand its account, connections, and access.

Work with your organization’s @ChatGPT assistant in Slack and Microsoft Teams, and understand its account, connections, and access.

Use your organization’s @ChatGPT assistant in Slack or Microsoft Teams to ask questions, summarize information, or draft work with teammates.

Your administrator configures the assistant’s instructions and connections to company tools. What it can help with depends on that setup and the information available to it. For some requests, @ChatGPT can ask to use apps connected to your own account. Review and approve that access when prompted.

For other ways to use ChatGPT with Slack or Microsoft Teams, see: [ChatGPT with Slack and Microsoft Teams](https://help.openai.com/articles/20001536).

Your organization must install and enable the @ChatGPT assistant before you can use it. Ask your workspace administrator where it is available and which company tools it can use.

For administrator setup instructions, see: [Setting up and managing @ChatGPT in Slack and Microsoft Teams](https://help.openai.com/articles/20001538).

If you previously used ChatGPT from Slack's sidebar, ask your administrator about moving to @ChatGPT. For existing installations and the required Slack permissions upgrade, see: [ChatGPT with Slack and Microsoft Teams](https://help.openai.com/articles/20001536#existing-users-of-the-chatgpt-app-in-slack).

# Start a conversation

Start with a request that includes everything @ChatGPT needs in your message. This helps you try the assistant before asking it to find information in a connected tool.

1. Open a channel where your organization has enabled @ChatGPT.
2. Mention @ChatGPT and describe what you want it to do.
3. Read the response, check the details, and mention @ChatGPT again if you want a change.

For example, you could ask:

@ChatGPT, write a short project update based on our discussion in this thread.

In Slack, @ChatGPT needs to be added to the channel. Your administrator can also configure which channels can start conversations with it. Slack channel restrictions do not restrict direct messages.

Use your organization’s instructions for supported Microsoft Teams conversations.

# Understand accounts, access, and privacy

## Account and setup

@ChatGPT runs through a service account: an account configured for the assistant, rather than your personal ChatGPT account. Your Slack or Teams account identifies you as the person making the request.

In enabled channels, you can make requests without connecting your own ChatGPT account, unless your administrator requires account connection. Requests that use your personal apps require separate connection and authorization.

A direct message to @ChatGPT does not, by itself, switch the assistant to your personal ChatGPT account.

## Data and connections

@ChatGPT uses the conversation context available to it and the tools your organization has configured. It does not automatically inherit your access to files, apps, or private channels.

Your organization can give @ChatGPT access to company tools through workspace connections. For these connections, the connected account’s permissions determine what information the assistant can read and which actions it can take.

For example, if a company information source is connected, you can ask @ChatGPT to use a specific document. Include its name or direct link and explain what you need from it. Your own ability to open the document does not establish that @ChatGPT can open it.

For some requests, @ChatGPT may need apps connected to your own account. Review the requested access when prompted. Your approval does not let other people use your connected apps by asking @ChatGPT.

In Slack, if you see **Allow for a week**, you can select it to remember the requested access level for 7 days. You may still be asked to confirm that a task is for you when several people are participating.

If @ChatGPT says an approval request has expired, mention @ChatGPT again to retry.

## Memory and instructions

Your personal saved memories, custom instructions, skills, and ChatGPT conversation history do not automatically carry over to @ChatGPT. Include the context or preferences it needs in your request.

Your administrator can set instructions for @ChatGPT, such as how it should communicate or use connected tools.

At launch, @ChatGPT does not record or access memory.

## Response visibility

Replies in shared conversations are visible to their participants. Consider that audience before including information in a message or authorizing a request that uses a personal connection.

Generated files can have their own permissions. A teammate may be able to see a file link in the conversation without being able to open the file. Check the file’s location and sharing settings with its owner before distributing it.

# Complete a required account connection

Your administrator may require you to connect your Slack or Microsoft Teams account to ChatGPT before using the assistant. If you receive that request:

1. Open the connection link in the request.
2. Sign in to the intended ChatGPT account if prompted.
3. Complete the Slack or Microsoft Teams connection for the intended organization and account.
4. Return to the original thread and retry your request.

If your organization blocks the connection or you cannot complete it, ask your workspace administrator for help. A request to authorize a personal app or approve Microsoft access for a file is separate; follow the instructions shown for that request.

# Resolve common problems

## Find the assistant

Confirm that you are in the intended Slack workspace or Teams tenant. If @ChatGPT is missing, ask your administrator to check installation, assignment, and where the assistant is enabled.

## Get a response

Mention the correct @ChatGPT assistant in a fresh thread and try a request using information included in your message. If it still does not respond, send your administrator the message link and the approximate time.

## Restore access to company information

Include a direct link to the source and review any personal authorization the assistant requests. If access still fails after you complete authorization, ask the connection owner to check the shared connection and the connected account’s permissions.

Report whether the assistant can open the direct link, find the source by name, or neither. These results help identify the problem.

## Open a generated file

Ask the file owner or your administrator to check the file’s location and permissions. Access to the conversation and access to the file are separate.

When asking for help, include the affected workspace, message link, expected result, actual result, and any error text. Do not include passwords, access tokens, or other credentials.

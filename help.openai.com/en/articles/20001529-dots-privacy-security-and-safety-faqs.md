<!-- source: https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs -->

# Dots privacy, security, and safety FAQs

Learn what your dot can access, how it uses and protects your information, and when it needs your approval.

Updated: yesterday

## Access and permissions

### Can my dot use plugins I’ve already set up in ChatGPT, ChatGPT Work, or Codex?

Yes. Plugin permissions are shared across dots, ChatGPT, ChatGPT Work, and Codex. Your dot can use your existing connections within the permissions you’ve granted.

Your dot comes with strong defaults for which actions need your approval each time, which you can approve in advance, and which it can take without asking. See the [Actions, approvals, and control section](https://help.openai.com/articles/20001529#actions-approvals-and-control) for more details.

### Where do I grant new permissions or manage existing ones?

You can connect new plugins and manage existing ones in ChatGPT’s **Plugins** tab. These connections are shared across dots, ChatGPT, ChatGPT Work, and Codex.

You can also set up a separate Slack account for your dot, giving it its own identity and access in those services. Your dot can still use the plugins you’ve already connected to ChatGPT, even if it has its own email or Slack account.

### How do I control what my dot can read or change through plugins?

You can manage access to different plugins in ChatGPT’s **Plugins** tab. Your dot follows strong defaults about when it needs your approval before taking actions through plugins.

Custom Rules let you set additional boundaries for dots, such as telling your dot never to send emails. These rules cannot override certain built-in guardrails and safety requirements.

Your dot can also look for useful updates before you make a request. This is called proactive research. It can read information from permitted connected sources and save private notes, but its research tools cannot directly:

* Send messages to other people.
* Change content through plugins.
* Control a browser or computer.

Any follow-up action must follow the usual action rules and safety checks. Those same rules apply to tasks you’ve already authorized that continue in the background.

### Can my dot access my camera, microphone, or screen?

Before your dot can access your computer’s camera, microphone, or screen, you must connect your computer to your dot. You must also give the ChatGPT app permission to access your camera, microphone, or screen in your device settings.

### Are dots available to users under 18?

No. Dots are not yet available to users under 18.

## Data use, memory, and privacy

### Does my dot share memory with ChatGPT?

Yes. Your dot can receive memories and recent conversation context from ChatGPT, and conversations with your dot can contribute to memory in ChatGPT. Memory can continue to be shared between ChatGPT and your dot after setup.

Turning off **Memory** in ChatGPT stops that sharing. It does not delete information that your dot has already received.

### What information does my dot retain, and how is it protected?

Your dot can retain context from your conversations and plugins for as long as you keep your dot. Deleting your dot starts deletion of its own context. Any information that your dot has shared with ChatGPT Memory can be separately managed in ChatGPT Memory settings.

Your dot’s context does not retain credentials, images, or screenshots. Files your dot creates or uses in other locations, such as ChatGPT Library, your computer, or a connected storage service, follow that location’s retention policies. Deleting a Library file does not by itself delete a copy already attached to your dot’s conversation.

OpenAI encrypts your content while it is stored and while it travels between you, OpenAI, and our service providers. In an eligible Enterprise workspace configured with Enterprise Key Management (EKM), long-term data in new dots supports customer-managed encryption keys. For EKM setup, see [OpenAI Enterprise Key Management (EKM) Overview](https://help.openai.com/articles/20000943).

### Can I see, correct, or delete what my dot remembers about me?

Deleting your dot starts deletion of its own context. You currently cannot view, delete, or directly modify individual dot memories, including specific details that enter the dot’s context from plugins.

### What happens to my information if I disconnect a service linked through a plugin?

This stops new access through that connection. It does not delete information your dot has already built into its context.

### What happens to my information if I delete my dot?

* **Delete your dot:** This starts deletion of your dot’s own context.
* **Files and conversations:** Files, Codex threads, and ChatGPT conversations your dot created are stored separately. Deleting your dot does not delete them.
* **ChatGPT memories:** Memories from your other ChatGPT conversations remain in place. You can manage them through ChatGPT’s memory controls.

### Does pausing my dot or removing workspace access delete its information?

No. Pausing a dot or removing a member’s permission to use it does not delete the dot’s stored information.

For Enterprise access and pause controls, see [Manage dots in ChatGPT workspaces](https://help.openai.com/articles/20001554). For supported storage and inference regions, see [Data residency and inference residency for ChatGPT](https://help.openai.com/articles/9903489).

### Can I use dots with protected health information?

Dots are HIPAA-eligible when used from an eligible ChatGPT workspace under a BAA and enabled for your role. Other features and third-party services your dot uses retain their own coverage and restrictions. Review [HIPAA eligible products and functionality](https://help.openai.com/articles/20001069) before using protected health information.

### Can people associated with OpenAI review my dot’s activity if I’ve turned off model improvement?

Yes. Human review may occur in limited [circumstances](https://help.openai.com/articles/7039943#authorized-human-access-to-content), including safety-related cases, even when model improvement is turned off.

### Does OpenAI use information from my dot to improve its models? How do I opt out?

For ChatGPT Business, Enterprise, and Edu workspaces, we don’t use your data to train our models by default. For personal ChatGPT plans, your “**Improve the model for everyone**” setting controls whether your dots’ conversations and work may be used to improve our models. This may include actions dots take, work they delegate to other agents, automations you set up, and data from connected apps that is used to inform your conversations. We take steps to remove personal identifiers where possible before using eligible data.

We don’t train directly on proactive background research or its notes. If a dot brings information from that research into an eligible conversation or task, that information may be used for training, depending on your settings.  You can turn off “**Improve the model for everyone**” in ChatGPT settings. You can read more about how your data is used in [Data controls in ChatGPT](https://help.openai.com/articles/7730893).

### How do I request access to, correction of, or deletion of my personal information?

You can submit a request through OpenAI’s [Privacy Portal](https://privacy.openai.com/) or email [dsar@openai.com](mailto:dsar@openai.com), even if you don’t have an OpenAI account.

Depending on where you live, your rights may include accessing, correcting, deleting, or receiving a copy of your personal data. We may ask for information to verify your identity. See our [Privacy Policy](https://openai.com/policies/privacy-policy/) for details.

### How does OpenAI use service providers?

OpenAI uses service providers to help operate its services, including hosting, cloud infrastructure, support, safety, and email delivery. These providers may access, process, or store personal information under OpenAI’s instructions to carry out those services.

See our [Privacy Policy](https://openai.com/policies/privacy-policy/) for more information. For information processed on behalf of business customers, the applicable customer agreement governs how it is handled.

## Actions, approvals, and control

### Which actions require my approval or for me to take over?

If you ask your dot to perform sensitive actions, your dot may confirm your explicit approval (which in some cases can be given in advance) or ask you to take over to finish the action yourself. Your dot has been instructed to follow these policies:

* The most sensitive actions like changing a password or transferring money require you to take over so you can complete them yourself.
* Other actions like permanently deleting data or installing software may require approval each time you ask your dot to perform them.
* In some of these cases such as sending recurring messages, you can give your approval in advance instead of each time.

Your dot uses your instructions to understand when and how it can act on your behalf. You can help make those boundaries clear by being specific about what you’re approving. For a future message, include who it should go to, what it should say, and when or under what conditions it should be sent. Approving one message does not give your dot ongoing permission to contact people on your behalf. Any advance approval remains limited to what you authorized.  Dots can still make mistakes, so always review consequential work.

### What can I allow or block with Custom Rules, and which approval requirements or safety checks can’t be overridden?

Your dot comes loaded with strong defaults on which actions need to be confirmed at action time, pre-approved, or which do not require confirmation.  Custom Rules let you customize these and tell your dot which supported actions it can take independently, which require your approval, and which it should not take. You can view your Custom Rules by accessing your settings.  Custom Rules cannot turn off core safety requirements, such as when your dot asks you to take back over to change a password.  Custom Rules also cannot change the separate safety review system, Auto-review, or the restrictions on proactive research.

### How can I review and guide my dot’s activity?

Activity View in the desktop app shows your dot’s ongoing and delegated tasks. You can see task descriptions and their status to follow its progress. You can also review steps your dot has taken.

You can add context, correct a misunderstanding, change direction, or ask your dot to stop.

### Can I stop my dot, correct its instructions, or reverse an action it has already taken?

As your dot works, you can provide updated guidance, change direction, or ask it to stop.

Whether a completed action can be reversed depends on the action and the app involved. You can ask your dot to help correct a mistake, but some actions cannot be undone.

### What should I do if my dot makes a mistake, shares information unexpectedly, or takes an action I didn’t intend?

Your dot can make mistakes. If you’ve spotted an error, you can ask your dot to fix the problem and it may be able to undo actions. For instance, your dot may be able to reverse unintended edits to a document or recall an email. If you’d like to report a mistake, see [Getting started with your dot](https://help.openai.com/articles/20001530) for more guidance.

## Security and built-in safeguards

### How can I help keep my account secure when using dots?

Multi-factor authentication (MFA) adds an extra verification step when you sign in to your ChatGPT account, offering additional protection against phishing and unauthorized access. You can turn it on in **Settings > Security and login**. [Learn how to set up MFA](https://help.openai.com/articles/7967234).

### What safety checks help prevent my dot from sharing private information or acting outside my permissions?

Your dot uses several layers of protection:

* **Model safeguards:** Dots use models from our GPT-6 frontier model family, including GPT-6 Astra and GPT-6.1 Terra. These models are trained to follow safety rules and refuse harmful requests, including requests involving biological or cybersecurity misuse.
* **Plugin permissions** limit what it can access.
* **Custom Rules** let you set additional boundaries for supported actions.
* **Auto-review** checks certain planned actions against your instructions, Custom Rules, and safety requirements before they run.
* **Safety monitoring** looks for potentially harmful behavior as your dot works.

For example, before your dot sends an email, Auto-review checks the recipient and message to help catch a wrong address or information you did not intend to share.

If it blocks the action, your dot may ask for clarification or approval if that could resolve the block, try a permitted alternative, or stop. Your approval cannot override core safety requirements.

Action rules also apply when your dot delegates work or continues working in the background. Proactive research has additional restrictions: its tools cannot directly send messages to other people, change content through plugins, or control a browser or computer.

Your dot cannot turn off required Auto-review checks or remove those research restrictions. These safeguards help reduce risk, but your dot can still make mistakes.

For information about customizing the Auto-review policy, see [Auto-review configuration](https://learn.chatgpt.com/docs/sandboxing/auto-review#configuration).

### How does my dot protect against prompt injection, phishing, and malicious instructions?

A website, email, or document can contain instructions that try to trick your dot into doing something you did not ask for, such as sharing private information. This is called [prompt injection](https://openai.com/safety/prompt-injections/).

Your dot is designed to distinguish your instructions from content it encounters while working. That content does not grant permission on its own.

Additional protections include restrictions on what tools can do, automatic checks before certain actions, approval requirements, and safety monitoring. We also use human and automated testing to find weaknesses and improve these safeguards.

These protections help reduce the risk of malicious instructions causing an unwanted action, but they do not eliminate it.

## Passwords, authentication, and payments

### How does my dot handle passwords?

For supported sign-ins, your dot pauses while you enter your credentials in a secure login form. The form sends your credentials directly to the browser environment without exposing them to the model. Your dot can then continue using the signed-in session.

These protections apply to supported sign-in flows. They don’t cover passwords you share separately in a chat or document, or through a plugin.

### Can my dot complete sign-in and security checks for me?

You may need to provide an authentication code or take over to complete a security check.

### Purchases with cards saved on merchant websites

Your dot can also make purchases using a card you’ve saved on a merchant’s website. These purchases require your approval, which may be given in advance when it specifically covers the purchase.

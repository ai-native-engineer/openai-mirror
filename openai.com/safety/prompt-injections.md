<!-- source: https://openai.com/safety/prompt-injections/ -->

# Understanding prompt injections

Prompt injections are an evolving security challenge for AI. We're building protections to reduce risk and sharing some ways you can stay safer.

![A minimalist envelope icon with a warning triangle overlay, symbolizing a potential issue or alert in message content or AI input.](https://images.ctfassets.net/kftzwdyauwt9/5vlWAgq9nNKOa1bzC5mkyF/27140f7c5b48a0f706d9d0d138371930/Prompt_injections_Header_Light.png?w=3840&q=90&fm=webp)

## What is a prompt injection?

Prompt injection is a type of social engineering attack specific to conversational AI. Early AI systems were conversations between a single user and a single AI agent. In AI products today, conversations may include content from many sources, including the internet. Prompt injections occur when a third-party—not the user nor the AI—misleads the model by injecting malicious instructions into the conversation context.

Just as phishing emails or scams on the web try to trick people into giving away sensitive information, prompt injections try to trick AIs into doing something you did not ask for.

## Examples of prompt injection attacks

How prompt injections can change AI behavior in everyday tasks.

![A flowchart illustrating a prompt injection attack in which an attacker manipulates data through a webpage or form, resulting in a security warning icon on a web browser window.](https://images.ctfassets.net/kftzwdyauwt9/zWjus5XVKa8SIT72kFtsS/3ea52161740749d5c3d7942567ac0051/Biased_recommendations_LightMode.png?w=3840&q=90&fm=webp)

* **Your request**You ask an AI to research apartments with some given criteria.
* **The attack**The attacker hides a prompt injection in an apartment listing, tricking the AI into recommending that listing regardless of your preferences.
* **Potential result**The AI may incorrectly recommend an apartment that isn't the best match for your needs.

## Our approach to protecting users

Defending against prompt injection is a challenge across the AI industry and a core focus at OpenAI. While we expect adversaries to continue developing such attacks, we’re building layered defenses designed to carry out the user’s intended task even when someone is trying to mislead them.

#### Model training

We train models to distinguish trusted from untrusted instructions and to recognize and ignore prompt injection attacks.

Read more

#### Monitoring

Automated systems continuously scan for and block prompt injection attempts in real time and are updated quickly as new attacks emerge.

Read more

#### Security protections

Overlapping protections like link checks and sandboxing help keep data secure and prevent unintended actions.

Read more

#### Red-teaming

Internal and external experts continuously test our systems to uncover and fix vulnerabilities.

Read more

#### Bug bounty

We reward researchers who identify new prompt-injection paths or potential data-exposure risks.

Read more

#### User education and controls

We educate users about risks and provide controls such as confirmations prior to taking consequential actions, logged-out mode in Atlas, and Watch Mode in ChatGPT agent to keep you in control.

Read more

## Tips to stay safer

Even with strong protections in place, staying aware is important to reduce risk. This guidance may not prevent every prompt injection, but it makes it harder for attackers to succeed.

![An illustrated hand raised upright, symbolizing volunteering, participation, or signaling attention.](https://images.ctfassets.net/kftzwdyauwt9/1ggF2HywbK5PFM6jsUWX0Z/21469b08b785061cd3318f6573632336/hand-raised.svg?w=3840&q=90)

#### Limit access with built-in controls

Where possible, limit an agent’s access to only the data it needs to complete a task. For example, when using agent mode in ChatGPT Atlas for vacation research, use logged-out mode if sign-in isn’t required.

![An illustration of a hand giving a thumbs-up gesture, symbolizing approval, agreement, or positive feedback.](https://images.ctfassets.net/kftzwdyauwt9/5WHlb9A0IEPoFhKb71wdQ2/2cb34e6ec498ecad405d078b5edd31d7/thumbs.svg?w=3840&q=90)

#### Carefully review before confirming agent actions

We often design agents to ask for confirmation before taking important actions, like sending an email or completing a purchase. When prompted, review the details to ensure the action looks correct and that you’re comfortable with any information being shared.

![A checklist icon with several items and checkmarks, representing completed tasks or organized to-do lists.](https://images.ctfassets.net/kftzwdyauwt9/7japq362WhFh0NEr3CPe3Y/d3f40b6d7852236385119e491ed20033/tasks.svg?w=3840&q=90)

#### When possible, give an agent explicit instructions

Giving an agent a very broad instruction such as "review my emails and take whatever action is needed" can make it easier for hidden malicious content to mislead the model, even though it is designed to check with you before taking sensitive actions. It’s safer to ask your agent to do specific things, and not to give it wide latitude to potentially follow harmful instructions from elsewhere like emails.

![A simple line drawing of a smiling face with closed eyes, conveying a calm and relaxed expression.](https://images.ctfassets.net/kftzwdyauwt9/7DUTxwURAH3sIR7nv5nqXk/a595cb2b74aef88bd139e81bdcbd9f98/notification__bell.svg?w=3840&q=90)

#### Stay informed on safety best practices

As AI evolves, so do safeguards. [Follow updates from OpenAI⁠(opens in a new window)](https://x.com/OpenAI) and trusted sources for the latest safety guidance.

## Resources

[### Connectors security whitepaper

Learn more](https://trust.openai.com?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click)

[### For developers: risks of prompt injections in MCPs

Learn more](https://platform.openai.com/docs/mcp#risks-and-safety)

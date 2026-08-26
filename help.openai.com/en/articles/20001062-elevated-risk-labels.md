<!-- source: https://help.openai.com/en/articles/20001062-elevated-risk-labels -->

# Elevated Risk labels

Understand Elevated Risk labels and the additional security considerations for connected apps and web access.

AI products can be more helpful when connected to your apps and the web, and we’ve invested heavily in keeping connected data secure from risks such as [prompt injection attacks](https://openai.com/safety/prompt-injections/). Our products have numerous existing protections across the model, product, and system levels. This includes sandboxing, [protections against URL-based data exfiltration](https://openai.com/index/ai-agent-link-safety/), monitoring and enforcement, and enterprise controls like role-based access and audit logs.

At the same time, some network-related capabilities introduce new risks, especially prompt injections, that aren’t yet fully addressed by the industry’s safety and security mitigations. Some users may be comfortable taking on these risks, and we believe it’s important for users to have the ability to decide whether and how to use them, especially while working with their private data.

To make such risks easier to understand, we aim to communicate this risk using a consistent “Elevated Risk” label, terminology, and icon (the exclamation mark within a shield), in a way that makes sense for each feature and product. This labelling provides additional user visibility and control on top of the existing protections.

Note: Features labeled “Elevated risk” are offered on an optional and early access basis, outside of the standard representations and warranties we make for our generally available services. Users should only turn on these features if they understand and are comfortable with the additional risks.

![Elevated Risk label with orange warning icon](https://images.ctfassets.net/j22is2dtoxu1/DbGGlbaJvQWfJJQFk8VOk/5b58644cc80c9d13739c92c825c3d5ad/Screenshot_2026-02-17_at_11.04.13_AM.png?q=80&fm=webp&w=240)

## What does “Elevated risk” mean?

When a capability is labeled “Elevated risk”, this indicates that usage of the feature introduces some risks that aren’t yet fully addressed by the industry’s safety and security mitigations. Each time you see this label, you will typically find guidance on the risk that usage of the feature introduces and what to be aware of, often via a “Learn more” link.

For example, in Codex, our coding assistant, developers can grant Codex network access so it can take actions on the web like looking up documentation. This capability also carries elevated risk of prompt injection attacks. The relevant settings screen therefore includes the “Elevated Risk” label, along with a clear explanation of what changes, what risks may be introduced, and when that access is appropriate.

The most common elevated risk that such labeled features have is [prompt injection attacks](https://openai.com/safety/prompt-injections/).

As safeguards improve, we may remove the “Elevated risk” label once we determine the risks are reasonably mitigated for users.

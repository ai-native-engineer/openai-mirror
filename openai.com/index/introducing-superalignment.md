<!-- source: https://openai.com/index/introducing-superalignment/ -->

July 5, 2023

# Introducing Superalignment

###### We need scientific and technical breakthroughs to steer and control AI systems much smarter than us. To solve this problem within four years, we’re starting a new team, co-led by Ilya Sutskever and Jan Leike, and dedicating 20% of the compute we’ve secured to date to this effort. We’re looking for excellent ML researchers and engineers to join us.

---

Superintelligence will be the most impactful technology humanity has ever invented, and could help us solve many of the world’s most important problems. But the vast power of superintelligence could also be very dangerous, and could lead to the disempowerment of humanity or even human extinction.

While superintelligence[A](#citation-bottom-A) seems far off now, we believe it could arrive this decade.

Managing these risks will require, among [other things⁠](/index/how-should-ai-systems-behave/), [new institutions for governance⁠](/index/governance-of-superintelligence/) and solving the problem of superintelligence alignment:

*How do we ensure AI systems much smarter than humans follow human intent?*

Currently, we don't have a solution for steering or controlling a potentially superintelligent AI, and preventing it from going rogue. Our current techniques for aligning AI, such as [reinforcement learning from human feedback⁠](/index/instruction-following/), rely on humans’ ability to supervise AI. But humans won’t be able to reliably supervise AI systems much smarter than us,[B](#citation-bottom-B) and so our current alignment techniques will not scale to superintelligence. We need new scientific and technical breakthroughs.

#### Our approach

Our goal is to build a roughly human-level [automated alignment researcher⁠](https://openai.com/blog/our-approach-to-alignment-research). We can then use vast amounts of compute to scale our efforts, and iteratively align superintelligence.To align the first automated alignment researcher, we will need to 1) develop a scalable training method, 2) validate the resulting model, and 3) stress test our entire alignment pipeline:

1. To provide a training signal on tasks that are difficult for humans to evaluate, we can leverage AI systems to [assist evaluation of other AI systems⁠](https://openai.com/research/critiques) (*scalable oversight).* In addition, we want to understand and control how our models generalize our oversight to tasks we can’t supervise (*generalization)*.
2. To validate the alignment of our systems, we [automate search for problematic behavior⁠(opens in a new window)](https://www.deepmind.com/blog/red-teaming-language-models-with-language-models) (*robustness)* and problematic internals ([*automated interpretability*⁠](https://openai.com/research/language-models-can-explain-neurons-in-language-models)).
3. Finally, we can test our entire pipeline by deliberately training misaligned models, and confirming that our techniques detect the worst kinds of misalignments (*adversarial testing*).

We expect our research priorities will evolve substantially as we learn more about the problem and we’ll likely add entirely new research areas. We are planning to share more on our roadmap in the future.

#### The new team

We are assembling a team of top machine learning researchers and engineers to work on this problem. 

We are dedicating 20% of the compute we’ve secured to date over the next four years to solving the problem of superintelligence alignment. Our chief basic research bet is our new Superalignment team, but getting this right is critical to achieve our mission and we expect many teams to contribute, from developing new methods to scaling them up to deployment.

> Our goal is to solve the core technical challenges of superintelligence alignment in four years.

While this is an incredibly ambitious goal and we’re not guaranteed to succeed, we are optimistic that a focused, concerted effort can solve this problem:[C](#citation-bottom-C) There are many ideas that have shown promise in preliminary experiments, we have increasingly useful metrics for progress, and we can use today’s models to study many of these problems empirically. 

Ilya Sutskever (cofounder and Chief Scientist of OpenAI) has made this his core research focus, and will be co-leading the team with Jan Leike (Head of Alignment). Joining the team are researchers and engineers from our previous alignment team, as well as researchers from other teams across the company.

We’re also looking for outstanding new researchers and engineers to join this effort. Superintelligence alignment is fundamentally a machine learning problem, and we think great machine learning experts—even if they’re not already working on alignment—will be critical to solving it.

We plan to share the fruits of this effort broadly and view contributing to alignment and safety of non-OpenAI models as an important part of our work.

This new team’s work is in addition to existing work at OpenAI aimed at improving the [safety of current models⁠](/index/our-approach-to-ai-safety/) like ChatGPT, as well as understanding and mitigating other risks from AI such as misuse, economic disruption, disinformation, bias and discrimination, addiction and overreliance, and others. While this new team will focus on the machine learning challenges of aligning superintelligent AI systems with human intent, there are related sociotechnical problems on which we are [actively engaging with interdisciplinary experts⁠](/index/democratic-inputs-to-ai/) to make sure our technical solutions consider broader human and societal concerns.

#### Join us

Superintelligence alignment is one of the most important unsolved technical problems of our time. We need the world’s best minds to solve this problem.

If you’ve been successful in machine learning, but you haven’t worked on alignment before, this is your time to make the switch! We believe this is a tractable machine learning problem, and you could make enormous contributions.

*If you’re interested, we’d love to hear from you! Please apply for our* [*research engineer*⁠](https://openai.com/careers/search/?c=86a66e6f-8ddc-493d-b71f-2f6f6d2769a6%2C6dd4a467-446d-4093-8d57-d4633a571123%2Cd36236ec-fb74-49bd-bd3f-9d8365e2e2cb%2C18ad45e4-3e90-44b9-abc6-60b2df26b03e%2C0f06f916-a404-414f-813f-6ac7ff781c61%2C3345bedf-45ec-4ae1-ad44-b0affc79bcb5%2C44e5a4a8-f930-456c-8f38-aa63090f9035%2Cc16efb3c-493d-401c-a76f-a493cfccbeb8%2C0c0f1511-91d1-4317-a68a-52ec2f849450%2C224d99ae-26ec-4751-8af3-ed7d104b60a2%2Ca3326dee-4be8-436d-ab8d-bcd611f3bedd%2Cfb2b77c5-5f20-4a93-a1c4-c3d640d88e04) *and* [*research scientist*⁠](https://openai.com/careers/search/?c=86a66e6f-8ddc-493d-b71f-2f6f6d2769a6%2C6dd4a467-446d-4093-8d57-d4633a571123%2Cd36236ec-fb74-49bd-bd3f-9d8365e2e2cb%2C18ad45e4-3e90-44b9-abc6-60b2df26b03e%2C0f06f916-a404-414f-813f-6ac7ff781c61%2C3345bedf-45ec-4ae1-ad44-b0affc79bcb5%2C44e5a4a8-f930-456c-8f38-aa63090f9035%2Cc16efb3c-493d-401c-a76f-a493cfccbeb8%2C0c0f1511-91d1-4317-a68a-52ec2f849450%2C224d99ae-26ec-4751-8af3-ed7d104b60a2%2Ca3326dee-4be8-436d-ab8d-bcd611f3bedd%2Cfb2b77c5-5f20-4a93-a1c4-c3d640d88e04) *positions.*

* [View careers](/careers/search/?c=alignment)

## Footnotes

1. A

   Here we focus on superintelligence rather than AGI to stress a much higher capability level. We have a lot of uncertainty over the speed of development of the technology over the next few years, so we choose to aim for the more difficult target to align a much more capable system.
2. B

   Other assumptions could also break down in the future, like favorable generalization properties during deployment or our models’ inability to successfully detect and undermine supervision during training.
3. C

   Solving the problem includes providing evidence and arguments that convince the machine learning and safety community that it has been solved. If we fail to have a very high level of confidence in our solutions, we hope our findings let us and the community plan appropriately.

## Authors

Jan Leike, Ilya Sutskever

## Contributors

Leopold Aschenbrenner and others from the Superalignment team

## Related research

![Weak To Strong Generalization](https://images.ctfassets.net/kftzwdyauwt9/1tCf4AONiCc3OkX47FmFy0/f95e25993d309257c631c4e64b699685/weak-to-strong-generalization.jpg?w=3840&q=90&fm=webp)

[Weak-to-strong generalization

SafetyDec 14, 2023](/index/weak-to-strong-generalization/)

![Practices For Governing Agentic AI Systems](https://images.ctfassets.net/kftzwdyauwt9/dfdeca52-d054-4ce9-18d684209ff9/f3a2e6e71ebefb70fca386ff7bbb9d92/practices-for-governing-agentic-ai-systems.jpg?w=3840&q=90&fm=webp)

[Practices for Governing Agentic AI Systems

PublicationDec 14, 2023](/index/practices-for-governing-agentic-ai-systems/)

![Blurry abstract shaped objects](https://images.ctfassets.net/kftzwdyauwt9/de9e8dc2-a39b-46c9-9df155f978ee/6832517e10505bd6886279603ad0f6aa/image_11.png?w=3840&q=90&fm=webp)

[DALL·E 3 system card

ReleaseOct 3, 2023](/index/dall-e-3-system-card/)

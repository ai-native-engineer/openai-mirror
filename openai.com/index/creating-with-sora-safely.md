<!-- source: https://openai.com/index/creating-with-sora-safely/ -->

March 23, 2026

[Safety](/news/safety-alignment/)

# Creating with Sora safely

[Read previous version](/index/launching-sora-responsibly/)

*As of April 26, 2026, the Sora product is no longer available.*

---

The Sora 2 model and the Sora app offer state-of-the-art video generation with a new way to create together, and we’ve made sure safety is built in from the very start. Our approach is anchored in concrete protections:

* **Distinguishing AI content**. Every video generated with Sora includes both visible and invisible provenance signals. All Sora videos also embed C2PA metadata—an industry-standard signature—and we maintain internal reverse-image and audio search tools that can trace videos back to Sora with high accuracy, building on successful systems from ChatGPT image generation and Sora 1. Many outputs also carry visible, dynamically moving watermarks which include the name of the creator.
* **Image-to-video with real person likeness**. As we continue to strengthen Sora’s guardrails, we’re enabling more creative expression and connection, including letting people create videos from photos of family and friends. Users can upload images with people to make videos in Sora, after attesting that they have consent from people featured and rights to upload the media. Image-to-video generations with people are subject to particularly strict safety guardrails, even stricter than what’s allowed with Sora Characters (formerly known as the cameo feature). Images including kids and young-looking persons are subject to even stricter moderation and guardrails about what can be created from them. These videos will always have watermarks upon sharing as well.
* **Consent-based likeness using characters**. We created [characters⁠(opens in a new window)](https://help.openai.com/en/articles/12435986-generating-content-with-characters) to give you strong control over your likeness in Sora. Likeness includes your appearance and your voice. We have guardrails intended to ensure that your audio and image likeness captured in characters are used with your consent. Only you decide who can use your characters, and you can revoke access at any time. We also take measures to block depictions of public figures, except those using the characters feature. Videos that include your characters—including drafts created by other users—are always visible to you. This lets you easily review and delete (and, if needed, report) any videos featuring your character. We also apply extra safety guardrails to any video with a character, and you can even turn on an even stricter set of guardrails that restrict types of usage. This includes limiting major changes to your appearance, putting you in embarrassing situations, and keeping your identity broadly consistent.
* **Safeguards for teens**. Sora includes stronger protections for younger users, including limitations on mature output. The feed is designed to be appropriate for all Sora users and content that may be harmful, unsafe, or age-inappropriate is filtered out for teen accounts. Teen profiles are not recommended to adults and adults cannot initiate messages with teens. Parental controls in ChatGPT let parents manage whether teens can send and receive DMs, as well as select a non-personalized feed in the Sora app. And by default, teens also have limits on how much they can continuously scroll in Sora.
* **Filtering harmful content**. Sora uses layered defenses to keep the feed safe while leaving room for creativity. At creation, guardrails seek to block unsafe content before it’s made—including sexual material, terrorist propaganda, and self-harm promotion—by checking both prompts and outputs across multiple video frames and audio transcripts. We’ve red teamed to explore novel risks, and we’ve tightened policies relative to image generation given Sora’s greater realism and the addition of motion and audio. Beyond generation, automated systems scan all feed content against our [Global Usage Policies⁠](/policies/usage-policies/) and filter out unsafe or age-inappropriate material. These systems are continuously updated as we learn about new risks and are complemented by human review focused on the highest-impact harms.
* **Audio safeguards**. Adding audio to Sora raises the bar for safety, and while perfect protections are difficult, we continue to invest seriously in this area. Sora automatically scans transcripts of generated speech for potential policy violations, and also blocks attempts to generate music that imitates living artists or existing works. Our systems are designed to detect and stop such prompts, and we honor takedown requests from creators who believe a Sora output infringes on their work.
* **User control and recourse.** You choose when and how to share your videos, and you can remove your published content at any time. Videos will only be shared to the feed when you choose to do so. Every video, profile, direct message, comment, and character can be reported for abuse, with clear recourse when policies are violated. You can also choose to block accounts at any time, which will prevent others from seeing your profile or posts, using your character, and contacting you via direct message.

* [Sora](/news/?tags=sora)
* [2026](/news/?tags=2026)

## Author

The Sora team

## Keep reading

![oai 1x1](https://images.ctfassets.net/kftzwdyauwt9/7eONRWq61MKUix4tK4t88Y/170085acc9b241a0bdfba429bd217907/oai_1x1.png?w=3840&q=90&fm=webp)

[Advancing youth safety and opportunity through global leadership

Global AffairsJun 2, 2026](/index/advancing-youth-safety-and-opportunity-through-global-leadership/)

![Technical foundations > Art Card](https://images.ctfassets.net/kftzwdyauwt9/6gugGfSiM1oO6UHxxwnqTk/c7173a5a2c096a8f8a24c258ddfa22dd/ArtCard-TechnicalFoundations.png?w=3840&q=90&fm=webp)

[A shared playbook for trustworthy third party evaluations

SafetyMay 29, 2026](/index/trustworthy-third-party-evaluations-foundations/)

![Frontier Governance Framework > card image ](https://images.ctfassets.net/kftzwdyauwt9/2KoiHuErR5YxXGUnhCU8VY/e392c6249ec4644e07e944edea22e837/Frame2.png?w=3840&q=90&fm=webp)

[OpenAI’s Frontier Governance Framework

SafetyMay 28, 2026](/index/openai-frontier-governance-framework/)

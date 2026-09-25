<!-- source: https://openai.com/index/disrupting-malicious-uses-of-ai-romance-scam/ -->

February 1, 2026

[Safety](/news/safety-alignment/)

# Romance scams: AI-enabled romance scam workflows

OpenAI banned accounts using AI to support romance scam workflows, including outreach, translation, victim engagement, and investment-fraud lures.

Loading…

Share

*This case study was originally published in OpenAI’s* [*February 2026*⁠(opens in a new window)](https://cdn.openai.com/pdf/df438d70-e3fe-4a6c-a403-ff632def8f79/disrupting-malicious-uses-of-ai.pdf) *report on disrupting malicious uses of AI.*

Since we began reporting on our disruptions of scam networks that sought to abuse our models [a year ago⁠(opens in a new window)](https://cdn.openai.com/threat-intelligence-reports/disrupting-malicious-uses-of-our-models-february-2025-update.pdf), we’ve taken down many scam operations from different parts of the world. They included “task” scams, which defraud their victims by convincing them to pay money in as a way of accessing non-existent earnings for trivial tasks, and investment scams, which defraud their victims by convincing them to put money into non-existent investment companies.

One common type of scam since long before the days of AI is the romance scam, in which scammers pose as a potential romantic partner and attempt to convince their target that they have met a love match before asking them for ever more money. Our first published scam disruption featured a newly stood up criminal operation in Cambodia that had used ChatGPT to generate messages for a romance scam, some of which were spread on social media. Since then, we’ve disrupted various attempted romance scams. As we wrote in [June⁠(opens in a new window)](https://cdn.openai.com/threat-intelligence-reports/5f73af09-a3a3-4a55-992e-069237681620/disrupting-malicious-uses-of-ai-june-2025.pdf), these and other scams tend to follow a common pattern in their use of AI, which we think of as the ping (cold contact), the zing (generate emotion), and the sting (extract money).

**The ping (cold contact):** the scammer generates content designed to attract the potential target’s attention by appealing to their interests. For example, the “pig butchering” scam we reported last year frequently targeted American men in their 40s in the medical professions by replying to social media posts they made about golf. Other operations used cold-call SMS messages, fake recruitment messages or, in our most recent romance scam case (described below), social media ads. In each case, the threat actors used ChatGPT to generate messages that might be more engaging and less obviously non-native than traditional scams.

![Golf-themed ping from the “pig butchering” network we reported in 2025, replying to a Facebook post by a user not linked to the operation.](https://images.ctfassets.net/kftzwdyauwt9/2qWvqXAU1CkCLxZi5sWP1V/278c2bc64f0d128b33b05ef1784fc3a4/image01.png?w=3840&q=90&fm=webp)

Golf-themed ping from the “pig butchering” network we reported in 2025, replying to a Facebook post by a user not linked to the operation.

**The zing (generate emotion):** the scammer generates content designed to trigger strong emotions in the target, and thus make them easier to manipulate. Romance scams try to make the target attracted to the scammer. Other scams can include trying to make the target excited about a potentially lucrative deal, afraid of missing an opportunity, or alarmed about an alleged legal risk or unpaid bill. Sometimes, the zing can be included in the same message as the ping.

![Cold-call SMS from the scam operation “Wrong Number” that we exposed in June 2025, including details of implausibly high returns for little work, likely designed to create the “zing” effect.](https://images.ctfassets.net/kftzwdyauwt9/3fFvAVCD7UFW2CMc8jBlDy/e9dc99b84d1bd3ac9e123334e8b3202a/image02.png?w=3840&q=90&fm=webp)

Cold-call SMS from the scam operation “Wrong Number” that we exposed in June 2025, including details of implausibly high returns for little work, likely designed to create the “zing” effect.

**The sting (extract money):** the scammer generates content designed to convince the target to hand over money. The reasons given can vary enormously. For example, romance scams may ask the target to invest in the beloved’s business, or hand over money to cover a financial crisis. “Task” scams tell their targets to pay money in so they can access (fictional) money they believe they earned. Investment scams tell the targets to put their money into non-existent investments.

![Cold-call SMS from the scam operation “Wrong Number” that we exposed in June 2025, including details of implausibly high returns for little work, likely designed to create the “zing” effect.](https://images.ctfassets.net/kftzwdyauwt9/3UlUejD6AUmEvDWoLJCqSt/9b4d82cdc09f3000e29aa8ce47a9e459/image03.png?w=3840&q=90&fm=webp)

Cold-call SMS from the scam operation “Wrong Number” that we exposed in June 2025, including details of implausibly high returns for little work, likely designed to create the “zing” effect.

As this flow suggests, an essential component of scams is the distribution network. Different scam operations that we’ve exposed sent their pings via SMS, encrypted messaging apps, social media posts, online ads, or a combination of all of them; scams in the pre-AI era are notorious for having used [emails⁠(opens in a new window)](https://consumer.ftc.gov/consumer-alerts/2021/03/spotting-scammy-emails), [phone calls⁠(opens in a new window)](https://consumer.ftc.gov/articles/phone-scams), or even, in the nineteenth century, [letters⁠(opens in a new window)](https://www.laphamsquarterly.org/swindle-fraud/letter-scam#:~:text=From%20The%20Memoirs%20of%20Vidocq%3A,million%20francs) and [telegrams⁠(opens in a new window)](https://www.aobf.org/wp-content/uploads/2020/06/2.2.Gregory.pdf#:~:text=The%20Journal%20of%20Behavioral%20Finance,University%20of%20New%20England%20Abstract). Many scams take a scattergun approach to distribution, but some appear to attempt precision targeting. For example, the “pig butchering” scam [we reported in February 2025⁠(opens in a new window)](https://cdn.openai.com/threat-intelligence-reports/disrupting-malicious-uses-of-our-models-february-2025-update.pdf) focused on topics such as golf; another romance scam used social media ads to target young men in Indonesia; and [celebrity scams⁠(opens in a new window)](https://consumer.ftc.gov/consumer-alerts/2018/08/scammers-impersonate-celebrities-social-media) typically pose as a famous person and then target that person’s fan groups. While the fragmentary nature of the evidence makes it difficult to reliably compare different scams that we disrupted, we assess that the scam’s chosen distribution method (e.g., scattershot or targeted) plays a significant role in each scam’s ability to successfully reach and exploit its targets, regardless of the degree to which the operation used AI for different functions.

* [Cambodia](/news/?tags=actor-origin-cambodia)
* [United States](/news/?tags=target-geography-united-states)
* [Indonesia](/news/?tags=target-geography-indonesia)
* [Fraud & scams](/news/?tags=activity-type-fraud-scams)

## Author

## Keep reading

[View all](/news/)

![COVERT IO: Operation "Date Bait" card image.](https://images.ctfassets.net/kftzwdyauwt9/dmuaCard7jczv8ZAQpYaSf3MHOW7EM/976564398aff3abcd802a5b9c276311e/1x1___COVERT_IO__Operation__Date_Bait_.png?w=3840&q=90&fm=webp)

[Operation “Date Bait”: AI-enabled scam targeting loveseekers

SafetyFeb 1, 2026](/index/disrupting-malicious-uses-of-ai-date-bait/)

![SCAM: Operation "False Witness" card image.](https://images.ctfassets.net/kftzwdyauwt9/dmuaCard1jpf7tKUjA3UjSbQEgqHMY/47eb11909e5c542f67afa14ef26be41b/1x1___SCAM__Operation__False_Witness_.png?w=3840&q=90&fm=webp)

[Operation “False Witness”: Fake recovery service impersonating authorities

SafetyFeb 1, 2026](/index/disrupting-malicious-uses-of-ai-false-witness/)

![SURVEILLANCE: Operation "Silver Lining Playbook" card image.](https://images.ctfassets.net/kftzwdyauwt9/dmuaCard5EyztnzBrxfmeUwFvj4Yox/60e22473333452d13efae1ff2b22c73c/1x1___SURVEILLANCE__Operation__Silver_Lining_Playbook_.png?w=3840&q=90&fm=webp)

[Silver lining playbook: Likely China-origin activity targeting US persons

SafetyFeb 1, 2026](/index/disrupting-malicious-uses-of-ai-silver-lining-playbook/)

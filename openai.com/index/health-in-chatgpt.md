<!-- source: https://openai.com/index/health-in-chatgpt/ -->

July 23, 2026

[Product](/news/product-releases/)

# Launching Health in ChatGPT

Rolling out to U.S. users, you can securely connect your health information to help you better understand and navigate your health.

Health in ChatGPT is launching to U.S. users. You can choose to securely connect Apple Health and supported medical records so ChatGPT can help you understand your information in context, keep track of what has changed, and have more informed, personalized conversations. The experience builds on feedback from early testers and gives you control over what you connect and when ChatGPT can use it.

Every week, more than 300 million people turn to ChatGPT with health-related questions—from understanding a lab result and preparing for an appointment to making sense of what a doctor said and building a healthier routine. But the context behind those questions is often scattered across patient portals, medical records, apps, and wearables, making it difficult to see and act on the complete picture.

With your permission, ChatGPT can now draw on relevant information you’ve connected in Health to help you compare a new result with prior tests, summarize changes since your last appointment, or explore how sleep, activity, and workouts relate to your routine. This can reduce the need to repeatedly gather, upload, or explain the same details, helping you feel more informed, ask better questions, and take a more active role in your health while supporting, not replacing, the care you receive from medical professionals.

We’re continuing to improve the models behind health conversations so ChatGPT can reason more carefully across complex details, explain health information clearly, ask for missing context, and recognize when professional care may be needed. GPT‑5.5 Instant brought frontier health intelligence to all free users. GPT‑5.6 Sol builds on that progress with even stronger performance on more complex questions.

Health is built with layered privacy and security safeguards. Connected medical records and Apple Health information, and conversations that use it, are not used to train our foundation models or target ads. We’re beginning to roll out Health to logged-in ChatGPT users 18 and older in the U.S. on web and iOS across Free, Go, Plus, and Pro plans today. Open Health from the sidebar in ChatGPT to get started. Health is not yet available in Codex.

## What early users are saying

“The most useful part has been turning scattered medical history into something I can actually understand and explain. I have multiple overlapping issues and ChatGPT helped connect those pieces into a clear timeline, explain the medical terms in plain English, and create summaries I could share with a physical therapist or trainer.

This has helped me feel less lost in my own health history. Instead of just seeing disconnected diagnoses, imaging results, and surgery notes, I could understand the bigger pattern. It made the information more usable and gave me better language to advocate for myself with providers and trainers.”

—Blake, technical program manager

## Health conversations grounded in your information

Earlier this year, we introduced a [dedicated health experience⁠](https://openai.com/index/introducing-chatgpt-health/) to a limited group of users that required visiting a separate space in ChatGPT to get the full benefit. Early testing showed that health questions often arose naturally in the course of conversations. For example, while planning meals or looking for recipes, someone might want ChatGPT to take a food allergy or dietary restriction into account. Among people with access, more than 70% of health-related conversations took place outside the dedicated health experience. Moving to a separate space added an unnecessary step.

Based on that feedback, you can now choose to let ChatGPT draw on relevant information you’ve connected in Health across your conversations, without needing to start within Health. With your permission, ChatGPT can consider relevant information you have connected, such as medications, lab results, recent visits, sleep, and activity, alongside the goals and context you share. This added context can make everyday conversations more useful. For example, ChatGPT can consider a dietary restriction when helping you choose a restaurant, or a recent injury when planning lower-impact weekend activities with your family. You can ask follow-up questions, add context, or correct information that is incomplete or out of date.

Health, in the left sidebar, remains your home base for connecting and managing your information, seeing recent data and trends, exploring suggested prompts, browsing synced records, and returning to past health conversations.

![Mobile phone showing a ChatGPT Health conversation recommending a 25-minute brisk walk after dinner, based on the user’s recent activity and missed workout.](https://images.ctfassets.net/kftzwdyauwt9/401YnvyXTYuaYIEWxnV48W/4113364c476df0fd17cce4d6e299e7d0/Health_Chat_1.png?w=3840&q=90&fm=webp)

## Improving health intelligence with physicians

We use dedicated training to improve the models behind health conversations in ChatGPT. GPT‑5.5 Instant, available to users on the Free plan, has made meaningful gains in recognizing when urgent care may be needed, asking for relevant context, explaining uncertainty, and making complex information easier to understand. On our most challenging health evaluations, it performed at a level comparable to our frontier Thinking models at the time of evaluation. [Learn more about those results and our work with physicians⁠](https://openai.com/index/improving-health-intelligence-in-chatgpt/).

[GPT‑5.6 Sol⁠](https://openai.com/index/gpt-5-6/), available to paid users, is our strongest model yet for health. It builds on our progress with stronger performance on tasks that require reasoning across complex details, clear communication, and careful judgment. It can help explain a visit note in plain language, understand how lab results have changed over time, consider the factors across options a doctor discussed, or prepare questions for a follow-up appointment.

To measure progress, we work with hundreds of physicians around the world to develop realistic health scenarios and detailed rubrics that define what a strong response should do. These evaluations assess qualities including accuracy, safety, communication, context awareness, completeness, and appropriate escalation. Every GPT‑5.6 model outperformed GPT‑5.5 on [HealthBench Professional⁠(opens in a new window)](https://arxiv.org/pdf/2604.27470), an evaluation of AI performance on challenging health tasks.

Finally, physicians extensively tested Health in ChatGPT before release, helping us measure and improve real-world model performance and safety with connected health data. While these results represent meaningful progress and we are continuously improving our models, ChatGPT can still make mistakes and does not replace the care and judgment of qualified medical professionals. We encourage people to verify important information and discuss medical decisions with their healthcare provider.

## Built with privacy, security, and control

Health is built with layered privacy and security safeguards. All ChatGPT conversations are encrypted at rest and in transit, and information connected in Health receives additional encryption protections.

**The information connected in Health is not used to train our foundation models or target ads.** Connected medical records and Apple Health information, and conversations that use it, are not used to train our foundation models or target ads, regardless of the model-training setting you choose for ChatGPT. Conversations that do not use this data follow your standard ChatGPT model-training setting choices, which you can change at any time in Settings > Data Controls.

**You decide when ChatGPT can use the information connected in Health.** By default, ChatGPT asks for permission before using connected medical records and Apple Health information to personalize a response. You can approve each request or choose to always allow access, which turns off these permission prompts. You can change this setting anytime in Settings > Plugins > Health.

**You can disconnect your Health information at any time.** Disconnect accounts at any time in Health > Accounts. When you do, data synced from that source is deleted from OpenAI’s systems within 30 days. Information already included in your ChatGPT conversation history remains until you delete those conversations.

**Memory remains in your control.** To personalize future chats, [memories⁠](https://openai.com/index/chatgpt-memory-dreaming/) can be created from your Health conversations. Memories are not created directly from connected medical records and Apple Health information. If you’d like to have a conversation without creating memories, you can use [Temporary Chat⁠(opens in a new window)](https://help.openai.com/en/articles/8914046-temporary-chat-faq) or turn memory off in Settings > Memory.

**Additional safeguards help protect sensitive sharing.** Before ChatGPT takes an action in another connected plugin that could disclose Health information, like sending your running partner a training plan based on your Apple Health data, additional safeguards help check that the sharing matches your request. For some sensitive actions, ChatGPT may ask you to confirm before proceeding. We continue to test these safeguards through dedicated red-team exercises focused on connected information in Health and use the findings to strengthen our protections.

## How to connect and use your health information

You can ask health questions in ChatGPT without connecting anything. To use Health and get responses grounded in your own information, you can choose to connect Apple Health, supported medical records from U.S. hospital systems, One Medical, or Function Health.

### Connect your health information

Open Health from the sidebar or More menu in ChatGPT and select “Get started.” ChatGPT will guide you through securely connecting your health information.

![Four mobile phone mockups showing the ChatGPT Health setup flow: selecting Health from the sidebar, connecting health data, reviewing privacy information, and enabling Apple Health.](https://images.ctfassets.net/kftzwdyauwt9/4anho9Yqyrb6FiHhg6xwXy/e3283724638c3ef9717f97c64edd641c/Health_1a.png?w=3840&q=90&fm=webp)

Once connected, your information will begin syncing, which may take a few minutes. While it syncs, you can connect additional accounts or return later.

![Two mobile phone mockups showing a list of healthcare accounts available to connect and a confirmation that One Medical data has synced, including medications, conditions, and lab records.](https://images.ctfassets.net/kftzwdyauwt9/1U8u4prkkkkIlsVQz7pbq0/6975a0c7bf69b8792af2ee9c7afba301/Health_1b.png?w=3840&q=90&fm=webp)

### Using a wearable or another health app?

If you use a wearable, fitness, or nutrition app that shares data with Apple Health, make sure sharing is turned on. Once you connect Apple Health to ChatGPT, ChatGPT can use the information that app makes available through Apple Health, when you allow it. Available information varies by app and metric, and some proprietary scores may not transfer.

### Review and update relevant health details

After connecting, you can review conditions and medications, remove anything that is no longer relevant, and add details that may be missing, including family health history. Connected information may not always be complete or current, for example, a medication may remain listed after you stop taking it, so tell ChatGPT when something changes and check important details against the original source.

![Three mobile phone mockups showing setup screens for reviewing medical conditions, reviewing medications, and adding health issues from family history.](https://images.ctfassets.net/kftzwdyauwt9/5ewWarQ5GiUhknkI38zina/e76381a06e47784188f8445965a48fd9/Health_2.png?w=3840&q=90&fm=webp)

### Bring your health context into conversations

Once your information is synced, you can ask questions anywhere in ChatGPT. When relevant, ChatGPT may use Health information based on your permissions. By default, ChatGPT asks before using this information. You can allow access once or choose to always allow it, and can change this setting anytime in Settings > Plugins > Health. You can also add @Health to your message to explicitly ask ChatGPT to include health context.

![Close-up of an mobile phone showing a request about recent lab results and a permission prompt asking whether ChatGPT may use the Health app once or always.](https://images.ctfassets.net/kftzwdyauwt9/3ShXaXhTSCgwtmdcaYaGFC/dce3f2c35670405aa3362c7e79a9ba07/Health_3.png?w=3840&q=90&fm=webp)

### Explore and manage your health information

Return to Health anytime to see recent data and trends, find suggested prompts, browse synced records, revisit past conversations, and manage your connected accounts.

![Four mobile phone mockups showing ChatGPT Health screens for activity and health metrics, health-related chats, lab records, and connected healthcare accounts.](https://images.ctfassets.net/kftzwdyauwt9/1DzdUf7AkgDCrV6IIxhcwj/1e01b27856ad14191ca8b6ede3d346d1/Health_4.png?w=3840&q=90&fm=webp)

* [ChatGPT](/news/?tags=chatgpt)

![OpenAI Presence 1x1](https://images.ctfassets.net/kftzwdyauwt9/5JBDenSGI6wx5CMPPlaM5J/da9d8e27a0bd70d845a816b28ac641a9/OpenAI_Presence_1x1.png?w=3840&q=90&fm=webp)

[Introducing OpenAI Presence

ProductJul 22, 2026](/index/introducing-openai-presence/)

![GPT-5.6 is now the preferred model in Microsoft 365 Copilot > Cover image](https://images.ctfassets.net/kftzwdyauwt9/3MPipvFMxS8m3kTyCtwFgj/015747dcd34cb667a221688cfca64e0f/Frame.png?w=3840&q=90&fm=webp)

[GPT-5.6 is now the preferred model in Microsoft 365 Copilot

ProductJul 9, 2026](/index/gpt-5-6-preferred-model-microsoft-365-copilot/)

[ChatGPT is now a partner for your most ambitious work

ProductJul 9, 2026](/index/chatgpt-for-your-most-ambitious-work/)

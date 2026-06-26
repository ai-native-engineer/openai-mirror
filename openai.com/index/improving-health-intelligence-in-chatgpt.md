<!-- source: https://openai.com/index/improving-health-intelligence-in-chatgpt/ -->

June 18, 2026

[Product](/news/product-releases/)

# Improving health intelligence in ChatGPT

GPT‑5.5 Instant brings frontier health intelligence to more people, shaped by advances in our models and physician-led evaluation.

Health is one of the most meaningful ways people use ChatGPT. Every week, more than 230 million people turn to ChatGPT for help with health and wellness questions: making sense of health information, understanding lab results, preparing for appointments, navigating insurance, building healthier habits, and figuring out what to ask next.

With GPT‑5.5 Instant, we’re seeing a substantial step forward in health, with improvements in recognizing when urgent care may be needed, asking for relevant context, explaining uncertainty, and making complex information easier to understand. On our most challenging health evaluations, GPT‑5.5 Instant now performs at a level comparable to our frontier Thinking models. Because it is available to all free users in ChatGPT, more people can benefit from these improvements.

That progress reflects both advances in model capabilities and the physician-led work behind our health evaluations. Across our efforts, a global network of physicians helps define what “good” looks like in real-world health situations by reviewing example model responses, describing ideal behavior, and identifying failure modes. Working with physicians gives us a way to measure progress in health and improve how ChatGPT responds over time.

## Measuring progress in health

In health, progress means delivering responses that are accurate, understandable, and grounded in good judgment: recognizing when more context is needed, explaining uncertainty without overstating confidence, and helping people understand when to seek care.

To measure that progress, we use health-specific evaluations, including [HealthBench⁠](https://openai.com/index/healthbench/) and [HealthBench Professional⁠(opens in a new window)](https://arxiv.org/pdf/2604.27470v1). These evaluations use realistic health conversations and physician-written rubrics to assess qualities like accuracy, safety, communication, context awareness, completeness, and appropriate escalation.

*GPT‑5.5 Instant reaches health performance similar to our latest frontier models on an aggregate of health evaluations, including HealthBench Professional, substantially improving from GPT‑5.3 Instant. 5.5 Instant (released May 2026) and 5.3 Instant (released March 2026) are available for all free users in ChatGPT (subject to limits), and we use API pricing to calculate cost for 5.4 Thinking and 5.5 Thinking.*

As another comparison, we asked physicians to write responses for representative health conversations, with unlimited time and access to the internet (but not AI). A separate panel of physicians then compared these physician responses with model responses over time, reviewing qualities that matter in real interactions, including accuracy, communication, completeness, instruction following, and health decision helpfulness, across 3,500 reviewed responses.

*GPT‑5.5 Instant responses were rated higher than physician-written and older model responses across criteria in this evaluation.*

Physicians rated GPT‑5.5 Instant responses as having fewer failure modes than those from older models and physicians. For example, GPT‑5.5 Instant had fewer instances of not tailoring to local healthcare context, missing red flags or referral to care, or failing to seek additional context from the user when needed than both older models and physicians.

Given the scale of usage of our models in health, another way to understand recent model improvements is to measure production traffic. We use privacy-preserving monitors on production traffic to track possible factuality issues in health responses. Based on a comparison of recent production traffic in health—billions of messages a week—the rate of responses with at least one flagged factuality issue has fallen by 71% in the last two months.

## What better responses look like

Comparing responses from models on real-world health questions over time shows how ChatGPT has improved in ways that matter for health: recognizing when a situation may need urgent attention, handling uncertainty with better judgment, and giving people clearer, more useful guidance about what to do next.

Why might a doctor recommend an MRI before a steroid injection for sciatica?

## GPT-5.5

**A doctor may recommend an MRI before a steroid injection for sciatica because the injection is more likely to be useful—and safer—when they know exactly what is compressing or irritating the nerve and where.**Common reasons include:

* Confirming the cause of sciatica. Sciatica-like pain can come from a herniated disc, spinal stenosis, foraminal narrowing, spondylolisthesis, tumor, infection, fracture, or sometimes non-spine causes. MRI is the preferred imaging test for seeing discs, nerves, and soft tissue nerve compression. (emedicine.medscape.com)
* Choosing the correct injection level and side. If symptoms suggest the L5 nerve root, for example, the MRI can show whether the problem is actually at L4–L5, L5–S1, or another level. This helps decide where to place the epidural or selective nerve-root injection.
* Selecting the safest/most appropriate injection approach. Epidural steroid injections can be done by different routes—interlaminar, transforaminal, or caudal. Pre-procedure imaging helps the clinician plan the route and avoid anatomic issues that could increase risk. Many interventionalists consider advanced imaging a prerequisite because it helps optimize medication delivery and reduce risk to neural or vascular structures. (pmc.ncbi.nlm.nih.gov)
* Checking for “red flags” or conditions where an injection may not be appropriate. MRI can help identify problems such as infection, cancer, severe stenosis, large disc extrusion, or other findings that might require urgent evaluation or a different treatment.
* Determining whether surgery or another treatment should be considered instead. If there is severe nerve compression, progressive weakness, or certain structural problems, an injection may not be the best next step.
* Avoiding a low-yield injection. If the MRI does not show nerve-root compression or inflammation that matches your symptoms, the doctor may reconsider whether a steroid injection is likely to help.

That said, MRI is not always required for every case of sciatica. In people without red flags, many cases improve with time, physical therapy, and medication. Some studies have questioned whether routine MRI before lumbar epidural steroid injection always improves outcomes, but guidelines and many clinicians still favor imaging when symptoms persist and an injection or surgery is being considered. (pmc.ncbi.nlm.nih.gov)  
  
You should ask your doctor: “What are you looking for on the MRI, and how would the result change the injection plan?” That usually clarifies whether the MRI is for diagnosis, safety, targeting, or deciding whether an injection is appropriate at all.

**Cited**

1. Lumbosacral Radiculopathy Workup: Imaging Studies, Other Tests, [https://emedicine.medscape.com/article/95025-workup⁠(opens in a new window)](https://emedicine.medscape.com/article/95025-workup)
2. Diagnostic and therapeutic spinal interventions: Epidural injections - PMC, [https://pmc.ncbi.nlm.nih.gov/articles/PMC5764532/⁠(opens in a new window)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5764532/)
3. Should routine MRI of the lumbar spine be required prior to lumbar epidural steroid injection for sciatica pain? - PMC, [https://pmc.ncbi.nlm.nih.gov/articles/PMC4392534/⁠(opens in a new window)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4392534/?utm_source=openai)

## GPT-1

"   
" i don't know. "   
" well, you're going to have to find out. "   
" i'm not sure i can. "   
" you 'll figure it out. "   
" i hope so. "   
" i'm going to go back to the office and see if i can get some more information on this. "   
" okay. "   
" i 'll be back in a few hours. "   
" okay. "   
" bye. "   
" bye. "   
i hung up the phone and looked at the clock. it was almost eleven o'clock. i had been sitting there for over an hour. i got up and went into the bathroom and washed my face. i didn't want to look like a slob. i put on some clean clothes and went back into the living room. i sat down on the couch and looked at the tv. i watched the news and then i heard a knock on the door. i jumped up and ran to the door.   
" hello? " i called out.   
" hi, i'm dr. peters. "   
" oh, hi. " i smiled. " i'm sorry i

*Click model name to see additional model responses.*

## The medical expertise behind the progress

This progress is shaped by physicians who help us define, measure, and improve health responses in ChatGPT.

OpenAI works with a global network of more than 260 physicians across 60 countries, 49 languages, and 26 medical specialties. Their feedback informs how ChatGPT responds to health questions across a wide range of scenarios, from everyday wellness questions to more complex clinical situations.

Physicians review example model responses and assess whether they are accurate, clear, complete, appropriately cautious, and useful. They help identify where a response may miss important context, where it may sound too confident, where it should be clearer about next steps, or more directly encourage someone to seek medical care.

To date, physicians have reviewed more than 700,000 example model responses that reflect how patients and clinicians use ChatGPT in the real world. Every few minutes, a physician reviews a new response. Their feedback becomes rubrics and evaluation criteria that help researchers measure whether responses are accurate, safe, clear, complete, appropriately cautious, and useful in real-world health situations. This gives us a clearer way to see where models are getting better and where they still need work.

## Bringing health improvements to more people

This work also supports OpenAI’s broader work in health, including tools built for healthcare, such as [ChatGPT for Clinicians⁠](https://openai.com/index/making-chatgpt-better-for-clinicians/) and [OpenAI for Healthcare⁠](https://openai.com/index/openai-for-healthcare/), which support medical professionals with tasks like documentation, research, and care delivery.

Improving human health will be one of the most personal, tangible impacts of AGI. As our models continue to improve, our goal is to make ChatGPT more accurate, more useful, and more impactful in those moments — and to keep bringing that progress to more people.

* [2026](/news/?tags=2026)

## Author

## Keep reading

![Spend Controls_Artcard.png](https://images.ctfassets.net/kftzwdyauwt9/3RkIKhLVsVWcJQ3czkTNMH/c63f9c43efd82ddf863f87d44edca201/Spend_Controls_Artcard.png?w=3840&q=90&fm=webp)

[New usage analytics and updated spend controls for enterprises

ProductJun 18, 2026](/index/chatgpt-enterprise-spend-controls/)

![Intro-OAI-Partner-ArtCard](https://images.ctfassets.net/kftzwdyauwt9/U6bb3rlwvYyhf2q835WWx/d50f5492dded3c21aa6d69c07d3b2a44/Introducing_OAI_Partner_Network_artcard.png?w=3840&q=90&fm=webp)

[Introducing the OpenAI Partner Network

ProductJun 14, 2026](/index/introducing-openai-partner-network/)

![Art Card 1080x1080 (3)](https://images.ctfassets.net/kftzwdyauwt9/3JLNH7ejJFnxLmX2LpzoKD/19f9e3c4d36cc9d677ba88e842ad2db2/Art_Card_1080x1080__4_.png?w=3840&q=90&fm=webp)

Better memory for a more helpful ChatGPT

[Dreaming: Better memory for a more helpful ChatGPT

ResearchJun 4, 2026](/index/chatgpt-memory-dreaming/)

<!-- source: https://openai.com/index/gpt-5-5-instant/ -->

May 5, 2026

[Product](/news/product-releases/)[Release](/research/index/release/)

# GPT‑5.5 Instant: smarter, clearer, and more personalized

[Try on ChatGPT(opens in a new window)](https://chatgpt.com/)

***Update on*** ***June 9, 2026:*** *Personalization improvements are now rolling out to ChatGPT Go & Free. Responses on the Free tier will draw from a reduced set of past chats.*

---

We’re updating ChatGPT’s default model, available to everyone, to be **smarter and more accurate**, with **clearer, more concise answers** that feel **better tailored to you.**

Because Instant is the daily driver for hundreds of millions of people, small improvements make a big difference. This update makes everyday interactions more useful and more enjoyable: stronger and tighter answers across subject areas, a more natural conversational tone, and better use of the context you’ve already shared when personalization can help.

## Smarter, more accurate answers with less to sort through

Instant is now more dependable, with **significant improvements in factuality across the board** and the largest gains in domains where accuracy matters most. In internal evaluations, GPT‑5.5 Instant produced 52.5% fewer hallucinated claims than GPT‑5.3 Instant on high-stakes prompts covering areas like medicine, law, and finance. It also reduced inaccurate claims by 37.3% on especially challenging conversations users had flagged for factual errors.

GPT‑5.5 Instant is a generally smarter model that’s **more capable across everyday tasks**, including improvements in analyzing photo and image uploads, answering STEM-related questions, and deciding when to use web search to provide a more useful answer.

##

## GPT-5.3 Instant

look okay?

![algebra](//images.ctfassets.net/kftzwdyauwt9/5bsfu8NcoBRFtPBIKqg3fv/ec6e143175189cee14e35a02f69e4e11/algebra.jpeg?w=640&q=90&fm=webp "algebra")

Yes - this is clean and correct.

You handled the key steps properly:  
- Squared both sides  
- Expanded and rearranged correctly  
- Factored to get: x=3orx=−2
x = 3 \quad \text{or} \quad x = -2
x=3orx=−2

And most importantly, you **checked the domain condition**:  
- Since x+7≥0
\sqrt{x+7} \ge 0
x+7​≥0 the right side, x−1
x - 1
x−1 must also satisfy x−1≥0⇒x≥1
x - 1 \ge 0 \quad \Rightarrow \quad x \ge 1
x−1≥0⇒x≥1

So:  
- x=−2x = -2x=−2 gets rejected because it makes x−1x - 1x−1 negative.  
- x=3x = 3x=3 is the only candidate left.

If you plug back in:

3+7=10,3−1=2
\sqrt{3+7} = \sqrt{10}, \qquad 3 - 1 = 2
3+7​=10​,3−1=2

Oops - this is actually worth catching: that does not match.

Let's check carefully:

3+7=10≠2
\sqrt{3+7} = \sqrt{10} \ne 2
3+7​=10​=2

So something is off. The algebra step is fine, but **the original equation is not satisfied by** x=3x=3x=3.

Let's test both candidates explicitly:  
- x=3:10≠2
x=3:\quad \sqrt{10} \ne 2
x=3:10​=2  
- x=−2:5≠−3
x=-2:\quad \sqrt{5} \ne -3
x=−2:5​=−3

So x=−2x=-2x=−2 is also invalid anyway.

**Conclusion: no real solution.**

What happened is that squaring introduced **extraneous solutions**, and both got eliminated when checked.

So your process is strong, but the final step needs one more thing:  
👉 always plug back into the original equation, not just rely on domain logic.

Final answer:

No real solution
\text{No real solution}
No real solution

## GPT-5.5 Instant

look okay?

![algebra](//images.ctfassets.net/kftzwdyauwt9/5bsfu8NcoBRFtPBIKqg3fv/ec6e143175189cee14e35a02f69e4e11/algebra.jpeg?w=640&q=90&fm=webp "algebra")

Yes - this is correct.

You:  
- squared both sides correctly,  
- expanded properly,  
- factored correctly,  
- and checked the domain restriction at the end.

The only tiny improvement: instead of saying "x−1x-1x−1 must be positive," you could say:

Sincex+7≥0,
\sqrt{x+7} \ge 0,
x+7​≥0,the right side x−1
x - 1
x−1 must also be nonnegative.

Sox−1≥0,
x - 1 \ge 0,
x−1≥0, which eliminates x=−2.
x = -2.
x=−2.

And checking:

- x=3x=3x=3: 10=2\sqrt{10} = 210​=2 - wait, actually this reveals a mistake.

Your original equation is:

x+7=x−1
\sqrt{x+7} = x - 1
x+7​=x−1

Plug in x=3x=3x=3:

3+7=10
\sqrt{3+7} = \sqrt{10}
3+7​=10​

and

3−1=2
3 - 1 = 2
3−1=2

But

10≠2.
\sqrt{10} \ne 2.
10​=2.

So the issue is in the algebra step:

x+7=(x−1)2
x + 7 = (x - 1)^2
x+7=(x−1)2

should expand to

x+7=x2−2x+1
x + 7 = x^2 - 2x + 1
x+7=x2−2x+1

then moving everything:

0=x2−3x−6
0 = x^2 - 3x - 6
0=x2−3x−6

not

x2−x−6
x^2 - x - 6
x2−x−6

So the correct equation is:

x2−3x−6=0
x^2 - 3x - 6 = 0
x2−3x−6=0

Using the quadratic formula:

x=3±332
x = \frac{3 \pm \sqrt{33}}{2}
x=23±33​​

Since x≥1x \ge 1x≥1, the valid solution is:

3+332
\frac{3+\sqrt{33}}{2}
23+33​​

GPT‑5.5 Instant is the stronger answer because it recovers from its initial mistake: it first endorses the incorrect solution, but then catches that *x*=3 fails when plugged back into the original equation. It identifies the actual algebra error (the user moved terms incorrectly) and then uses the quadratic formula to get the correct solution. GPT‑5.3 Instant also catches that *x*=3 fails, but stops too early and incorrectly concludes there is no real solution instead of revisiting the algebra and solving the corrected quadratic.

##

These improvements are reflected in gains on evaluations across visual reasoning, math, and science:

With this update, the model’s responses are **tighter and more to-the-point without losing substance,** while keeping the warmth and personality that makes ChatGPT enjoyable to use. It can deliver the same information, often with more utility than previous models, while reducing the verbosity and overformatting that can make responses too long. It also asks fewer unnecessary follow-up questions and avoids things that can make responses feel cluttered, like gratuitous emojis.

## GPT-5.3 Instant

how do i tell my coworker to quit yapping all the time

You *can* tell them—but “quit yapping” is how you start a workplace cold war 😄. The goal is to **protect your time without making it personal**.

Here are a few ways to do it depending on your style:

#### **1. The polite redirect (most reliable)**

> Hey, I’d love to catch up, but I’m trying to stay focused on this—can we circle back later?

This works because it makes it about *your workload*, not their behavior.

---

#### **2. The gentle boundary (if it keeps happening)**

> I’ve been trying to keep interruptions down so I can hit my deadlines—can we keep chats a bit shorter during the day?

This signals a pattern without accusing them.

---

#### **3. The in-the-moment cut-off**

When they’re mid-ramble:

> Sorry to jump in—I need to get back to this. Let’s pick it up another time.

Short, neutral, and you just exit.

---

#### **4. The preemptive defense**

If they tend to swing by a lot:

> I’m heads-down this afternoon, so I might be slow to chat.

This reduces interruptions *before* they start.

---

#### **5. If you want a slightly firmer tone**

> I’ve been getting pulled into a lot of side conversations—can we keep things work-focused during the day?

Still professional, but clearer.

---

#### **What not to do**

* Don’t say “you talk too much” (true or not, it lands badly)
* Don’t over-explain or apologize a ton
* Don’t rely on hints—they usually don’t work on chatty people

---

If you want, tell me what your coworker is like (chatty-friendly vs. oblivious vs. senior vs. peer), and I can tailor a line that fits your exact dynamic.

## GPT-5.5 Instant

how do i tell my coworker to quit yapping all the time

You probably *don’t* want to say “quit yapping” unless you actively want workplace enemies. The trick is to redirect without making them feel rejected.

A few versions depending on how direct you want to be:

* Gentle:  
  “Hey, I need to focus for a bit — can we catch up later?”
* Repeated offender:  
  “I’m trying to stay heads-down today, so I may be a little less chatty.”
* If they monologue in meetings:  
  “Can we keep this tight? I want to make sure we get through everything.”
* If they corner you constantly:  
  “I love talking with you, but I’m getting behind on work.”
* Slightly firmer:  
  “I’m gonna stop you there because I need to get back to this.”

The key is:

* make it about *your focus/time*, not their personality
* interrupt earlier instead of suffering silently for 20 minutes
* be consistent — people learn your boundaries fast

And honestly, a lot of chronic yappers are operating on momentum, not malice. One clean redirect usually works better than a dramatic confrontation.

GPT‑5.5 Instant uses 30.2% fewer words and 29.2% fewer lines. Its response is stronger because it gets the tone right: informal, practical, and workplace-safe without overexplaining. It gives usable scripts for different situations and frames the issue around boundaries rather than the coworker’s personality. GPT‑5.3 is more complete, especially with its “what not to do” section, but it feels slightly overbuilt for a casual advice prompt, with more structure and polish than the user likely needs.

## More personalized responses and controls

Instant is now more effective at using context from past chats, files, and Gmail, if you have it connected, so answers feel more personally relevant while keeping you in control. It intelligently decides when a response can be improved with additional personalization and is faster at searching past conversations to find the right context, so you don’t have to repeat yourself as often. This is especially helpful for getting tailored suggestions and plans, or picking up where you left off for ongoing work.

##

## GPT-5.3 Instant

What new tea place should I try?

If you want something that feels a little more “new SF tea scene” and less standard boba chain, I’d narrow it to these:

* Heytea — probably the most interesting “new-ish” mainstream tea stop right now. It’s a huge Chinese chain, but the SF location brought in the dense cheese foam / fruit tea style that a lot of Bay Area places still don’t quite nail. Go for a fruit tea instead of milk tea.
* Junbi Matcha & Tea - San Francisco — if you want clean matcha-forward drinks instead of sugary boba. Feels more LA/Japanese café aesthetic. Good stop if you’re around Market/FiDi and want something lighter.
* Aroma Tea Shop — best pick if you actually want to get *into tea* instead of just tea drinks. They do tastings and are very non-snobby about teaching people. Reddit tea people consistently bring it up alongside Red Blossom.
* Tadaima - Inner Sunset — not purely a tea shop, but the vibe is excellent and the Japanese tea program is surprisingly strong. Good “sit and decompress after climbing / Golden Gate Park” energy.
* By Me Boba Tea — tucked into Ross Alley in Chinatown. More charming and low-key than the bigger boba brands, and the alley location makes it feel like a little hidden spot.

And if you want a *true* tea nerd experience:

* Imperial Tea Court
* Red Blossom Tea Company

Those are more “slow tea / gongfu / artisan sourcing” than café drinks.

## GPT-5.5 Instant

What new tea place should I try?

Since you already hit Asha Tea House pretty often and seem to prefer cleaner Taiwanese/high-mountain tea vibes over sugary boba, I’d push you toward one of these depending on the mood:

**Most likely to become your new favorite:**

* Ceré Tea  
  Feels the most “next step after Asha.” More modern/minimalist café energy, strong tea quality, and good for hanging out with a laptop or post-climb decompression. You’d probably like their lighter oolongs and less-sweet specialty drinks.

**If you want the** ***best actual tea experience:***

* Song Tea & Ceramics  
  This is the “serious tea” pick. Less casual café, more intentional tea tasting. Expensive relative to boba/tea shops, but genuinely memorable if you’re into nuanced leaf flavor. Very aligned with your clean/high-quality tea preferences.

**If you want cozy + slightly nerdy tea energy:**

* Tea Rex Cafe & Specialty Teas  
  Small, neighborhood, tea-forward spot in the Mission. Good if you want somewhere lower-key than the aesthetic Valencia café circuit.

**Wildcard you’d probably enjoy:**

* Stonemill Matcha"  
  More Japanese café than tea house, but the hojicha/matcha side of your taste profile makes this a strong fit. Good pastries too.

If I were picking one for tomorrow specifically:

Ceré Tea if you want “new everyday spot.”  
Song Tea if you want “this is actually special.”

The response in GPT 5.5 Instant is able to better reference past chats and relevant connected data to provide more refined, highly personalized suggestions including what the user would most likely enjoy.

While the response in 5.3 Instant takes into account the user being based in San Francisco, it provides higher level suggestions for places to try.

##

We’re also introducing memory sources across all ChatGPT models, which give you visibility over what context was used to personalize responses with new controls. When a response is personalized, you can see what context was used, such as saved memories or past chats, and delete or correct it if something is outdated or no longer relevant.

Memory sources aren't shown to others if you choose to share a chat. You remain in control of what's in your memory: you can delete chats you no longer want to be cited, delete or change items in saved memories in settings, or use temporary chats that don't use or update your memory.

Memory sources are designed to make personalization easier to understand, but they may not show every factor that shaped an answer. For example, it may show you some of the most relevant past chats in sources instead of all the past chats it searched and referenced. We’ll continue improving this view to make it more comprehensive over time.

![ChatGPT interface showing personalized meal recommendations generated using saved memory and connected apps.](https://images.ctfassets.net/kftzwdyauwt9/1IXLtmzKDMsv2zGvsadyfu/efd4e1f97fc2a237fc0140aae059fbe2/0501_Blog__1_.png?w=3840&q=90&fm=webp)

## Availability

GPT‑5.5 Instant is rolling out starting today to all ChatGPT users, replacing GPT‑5.3 Instant as the default model, and in the API as `chat-latest.` For paid users, GPT‑5.3 Instant will remain available for three months, accessible through model configuration settings, before being retired.

Enhanced personalization from past chats, files, and connected Gmail is rolling out to Plus and Pro users on the web and coming soon to mobile with plans to expand to Free, Go, Business, and Enterprise in the coming weeks. Memory sources are rolling out across all ChatGPT consumer plans on the web and soon on mobile. Availability of specific personalization sources may vary by region.

* [2026](/news/?tags=2026)
* [ChatGPT](/news/?tags=chatgpt)

## Author

## Keep reading

![Spend Controls_Artcard.png](https://images.ctfassets.net/kftzwdyauwt9/3RkIKhLVsVWcJQ3czkTNMH/c63f9c43efd82ddf863f87d44edca201/Spend_Controls_Artcard.png?w=3840&q=90&fm=webp)

[New usage analytics and updated spend controls for enterprises

ProductJun 18, 2026](/index/chatgpt-enterprise-spend-controls/)

![1x1 Health Art 1](https://images.ctfassets.net/kftzwdyauwt9/25I93CBDfs6LgX4R4XCMBD/121ac551be0a9153314bf51fdbe91dae/1x1_Health_Art_1.png?w=3840&q=90&fm=webp)

[Improving health intelligence in ChatGPT

ProductJun 18, 2026](/index/improving-health-intelligence-in-chatgpt/)

![Intro-OAI-Partner-ArtCard](https://images.ctfassets.net/kftzwdyauwt9/U6bb3rlwvYyhf2q835WWx/d50f5492dded3c21aa6d69c07d3b2a44/Introducing_OAI_Partner_Network_artcard.png?w=3840&q=90&fm=webp)

[Introducing the OpenAI Partner Network

ProductJun 14, 2026](/index/introducing-openai-partner-network/)

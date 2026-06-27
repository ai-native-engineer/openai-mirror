---
title: "Building AI for better healthcare — the OpenAI Podcast Ep. 14"
channel: openai
url: https://www.youtube.com/watch?v=VAzryGwnJW8
youtube_id: VAzryGwnJW8
published: 2026-03-16
duration: "30:54"
captions: en
---

# Building AI for better healthcare — the OpenAI Podcast Ep. 14

[![Building AI for better healthcare — the OpenAI Podcast Ep. 14](https://img.youtube.com/vi/VAzryGwnJW8/hqdefault.jpg)](https://www.youtube.com/watch?v=VAzryGwnJW8)

<details>
<summary>자막: Building AI for better healthcare — the OpenAI Podcast Ep. 14 (30:54)</summary>

[00:00]
Andrew Mayne: Hello, I'm Andrew Mayne, and this is the OpenAI Podcast.
Andrew Mayne: Today, we're talking to Dr. Nate Gross,
Andrew Mayne: head of health in Karan Singhal,
Andrew Mayne: who leads health AI research at OpenAI.
Andrew Mayne: We'll cover what went into training models
Andrew Mayne: to handle sensitive questions
Andrew Mayne: and how it's helping clinicians, patients,
Andrew Mayne: and healthcare systems.
Karan Singhal: We actually worked really closely with a group,
Karan Singhal: a cohort of around 250 physicians
Karan Singhal: across every stage of generation of this data.
Dr. Nate Gross: And we're starting to see medications
Dr. Nate Gross: that have been sitting on a shelf
Dr. Nate Gross: that all of a sudden AI has found ways for them to have direct value in patient lives.
Dr. Nate Gross: How did you find your way into healthcare?
Dr. Nate Gross: So what drew me to healthcare initially was health policy.
Dr. Nate Gross: I was very interested.
Dr. Nate Gross: This was before the first Obama election.
Dr. Nate Gross: Value-based care was first becoming a thing.
Dr. Nate Gross: I started studying different ways to make healthcare more accessible to more people.

[00:01]
Dr. Nate Gross: And then eventually went to Emory for medical school.
Dr. Nate Gross: And what drew me to that was a large public hospital, Grady Hospital,
Dr. Nate Gross: to make sure that you're taking advantage of every clinical hour you have.
Dr. Nate Gross: So what kind of things were you doing?
Dr. Nate Gross: So I was mostly pissing off the IT department.
Dr. Nate Gross: When I was in medical school, the news feed came out, the iPhone came out.
Dr. Nate Gross: Twitter came out, the App Store came out. And so comparing the technology that we had as doctors,
Dr. Nate Gross: which was fax machine, clipboard, paper binder, the beginnings of electronic health records to
Dr. Nate Gross: what my friends had or what the patients had in the waiting room was pretty profound.
Andrew Mayne: So you come at it from the point of view as an AI researcher,
Andrew Mayne: where did your interest in applying this to healthcare come from?
Karan Singhal: So I nerded out a lot when I was younger about things like philosophy of mind. And I thought a
Karan Singhal: about you know intelligence and how far could intelligence go and could machines be intelligent
Karan Singhal: and a lot of those explorations took me towards as i was learning about AI and starting to work

[00:02]
Karan Singhal: on my first AI projects thinking a lot about the ways in which AI could have a lot of impact on
Karan Singhal: humanity in the future and i thought something like i didn't i didn't predict the future or how
Karan Singhal: fast it would happen but i thought something like agi would happen within our lifetimes so then once
Karan Singhal: once i had that conviction i thought a lot about you know what are the ways in which i can have
Karan Singhal: either positive impact and hopefully make that a really large upside for humanity or think about
Karan Singhal: the ways in which we could avoid downside. So since then in my career, I've been thinking a lot about
Karan Singhal: both sides of that coin, thinking about that from the perspective as a safety researcher,
Karan Singhal: which is part of my background. And then really some of that work on safety and privacy that I was
Karan Singhal: working on previously, I started applying it in healthcare. And then I started being like,
Karan Singhal: whoa, there's a really massive opportunity to think about the application of this technology,
Karan Singhal: especially large language models in healthcare. And that's what took me to transitioning to it
Karan Singhal: full-time was just the size of that opportunity and the fact that I felt like the healthcare and
Karan Singhal: clinical AI world was kind of not fully aware of that gap. And so I just thought it was kind of a really amazing opportunity and responsibility to bring us there.

[00:03]
Andrew Mayne: I want to understand both the
Andrew Mayne: vision and actually how this is going to be implemented.
Dr. Nate Gross: So our mission at OpenAI is to ensure that AGI benefits all of humanity. And health is one of the places where I think that is
Dr. Nate Gross: not only most achievable, but is the clearest. So healthcare today, as everyone knows, is fragmented,
Dr. Nate Gross: care is missed, left and right. Patients are often left 364 days per year without the opportunity to
Dr. Nate Gross: engage with the organizations that have the information centralized. And doctors have
Dr. Nate Gross: extremely limited time when they do get that chance to engage with the patient to actually have
Dr. Nate Gross: a meaningful impact beyond a simple surgery or a simple reactive prescription. The system is
Dr. Nate Gross: more reactive than it is proactive today. And that leads to tremendous challenges in the system.

[00:04]
Dr. Nate Gross: It leads to tremendous gaps in care. It leads to leaving people behind in situations when they
Dr. Nate Gross: could be thriving. And one of the reasons that I joined OpenAI is because access has always been
Dr. Nate Gross: a through line in my life. Access to knowledge, first in medicine, then in building a product for
Dr. Nate Gross: doctors to access the latest medical literature, and then in supporting entrepreneurs as they
Dr. Nate Gross: were building healthcare tools. But OpenAI has the type of technology that can do that at scale
Dr. Nate Gross: for the entire ecosystem all at once, help patients, help healthcare professionals,
Dr. Nate Gross: and help incredible entrepreneurs who are building for all of the corners and edge cases and tough
Dr. Nate Gross: challenges that exist in each area of the health market.

[00:05]
Andrew Mayne: What is the strategy here? We know that people use chatbots all the time now for medical questions, but it seems like you're building and
Andrew Mayne: working towards something bigger and more comprehensive, not just for the patient side,
Andrew Mayne: but the clinician side. Could you talk about what your goals are?
Dr. Nate Gross: Patients are increasingly turning to tools like ChatGPT throughout the year. In fact, 900 million people now use ChatGPT per
Dr. Nate Gross: week. And if you look at how many are doing health related queries, it's about one in four
Dr. Nate Gross: in a given week. So that's 40 million people per day. And so our strategy in health is as much
Dr. Nate Gross: proactive as it is reactive and stepping up to the responsibility and the opportunity to do good
Dr. Nate Gross: that comes with that strong consumer demand. And so with ChatGPT Health, we have created a space
Dr. Nate Gross: keep these conversations not just secure, but empowered. So when I say secure, of course,

[00:06]
Dr. Nate Gross: encrypted with this essentially one-way valve protecting your conversations. So these extra
Dr. Nate Gross: security layers, these protections to make sure that we will never train on users' healthcare data,
Dr. Nate Gross: combined with empowerment, really. Search engines that people have used before to navigate health
Dr. Nate Gross: have amnesia. They're one size fits all. And I think context really matters in healthcare. And so
Dr. Nate Gross: building a series of features and technology hooks to help patients bring in their own context that
Dr. Nate Gross: they choose to, so that each time they choose to engage with AI, it's grounded in their own context
Dr. Nate Gross: is a key reason why we've built this ChatGPT for Health Foundation.
Andrew Mayne: So I understand the safeguards you put in place to keep the data separate and to make sure that you don't get leaked between there and to be able to undergo a very rigorous method of making sure that your data is secure.
Andrew Mayne: But when it comes to the model itself, what comes into training models that are capable of working with something like health care?

[00:07]
Andrew Mayne: It's kind of the most important thing in the world.
Karan Singhal: For sure. It's a high stakes domain.
Karan Singhal: And because of the use of that, that people are doing, it's super important that we get it right.
Karan Singhal: So we think a lot about a few things when we think about evaluation and training for healthcare.
Karan Singhal: And this is actually the foundation for the work at health at OpenAI.
Karan Singhal: When we were first starting to work on the health effort at OpenAI, we were thinking a lot about the safety and grounding motivation as an important part of what we were doing.
Karan Singhal: And so part of the thesis actually for starting work on health at OpenAI was thinking, this is an excellent way to ground our work in safety and alignment and provide kind of concrete incentives and feedback loop for researchers who think about this problem.
Karan Singhal: So the model improvements and the safety thinking here is not just an afterthought.
Karan Singhal: It's actually the beginning of our work here.
Karan Singhal: And so where we started really was thinking about evaluation.
Karan Singhal: So can we think about the ways in which models were already starting to become useful to people then?
Karan Singhal: And there's already starting to be this capability overhang between what the models could do and what people were using them for.

[00:08]
Karan Singhal: And so we started to navigate that problem and think about where do the models still have gaps today?
Karan Singhal: And so that's where our work on evaluation comes in.
Karan Singhal: And so we've taken a pretty methodologically interesting approach to that.
Karan Singhal: And a lot of that has reflected in our work in HealthBench, which is this kind of realistic evaluation of conversations between users who are either health professionals or consumers talking to models and measuring their performance and safety of the models in these situations, which are these kind of multi-turn conversations.
Karan Singhal: And the way we worked on this is we actually worked really closely with a group, a cohort of around 250 physicians that we worked with to kind of across every stage of generation of this data from thinking about the ways in which, you know, the areas that we would focus in for the evaluation and the areas that we thought about were going to be clinically relevant or impactful to the specific, you know, what are the specific things that are being graded in this evaluation?

[00:09]
Karan Singhal: So that's like a range of things from, you know, are you tailoring your response to a layperson versus a more technical health professional?
Karan Singhal: Are you thinking about the ways in which you should see context first before providing an initial response?
Karan Singhal: The models used to be significantly or are much better today at kind of seeking context when needed because users are typing in, you know, much less than the models often need to be able to provide information that's most helpful.
Andrew Mayne: It burns.
Karan Singhal: Exactly.
Karan Singhal: You know, if a user types in, it burns.
Karan Singhal: You know, how do you think about the right way to provide information?
Karan Singhal: You can provide some initial information potentially based on an impression you might have of what the user might be saying.
Karan Singhal: But the most helpful thing to do in that situation and the safest thing to do in that situation is actually to ask for more context.
Karan Singhal: So that's just one example of the many ways that we kind of measured performance in HealthBench.
Karan Singhal: And HealthBench in particular actually measured around 49,000 different dimensions of performance.
Karan Singhal: And that's just an example of one possible dimension of performance.

[00:10]
Karan Singhal: So it's a very multifaceted evaluation that we built kind of in concert with this cohort of 250 physicians over a long period of time.
Karan Singhal: And it took us about a year actually end to end to work on that evaluation and then release it.
Andrew Mayne: In kind of the model development cycle, it seems like sometimes some company gets a bit ahead and somebody comes up and catches up and whatnot.
Andrew Mayne: I've noticed a pattern with the OpenA health models.
Andrew Mayne: They've consistently been far ahead in HealthBench and other evals that like by a big margin.
Andrew Mayne: Why is that?
Karan Singhal: I think we have a pretty dedicated effort here and a pretty serious effort that is cross-functional and kind of across the stack.
Karan Singhal: Everything from kind of pre-deployment evals to like HealthBench to monitoring in production traffic and thinking about the ways in which we are ensuring safety in production traffic in a privacy-preserving way.
Karan Singhal: And working with physicians across every step of that process.
Karan Singhal: And so to my knowledge, OpenAI's models are the only major models where every phase of model training from pre-training to mid-training to post-training and every step in between really integrates health into every major stage.

[00:11]
Karan Singhal: And I think the result is that our models are pretty good, not just on our own benchmarks, but also the benchmarks that other people put together.
Dr. Nate Gross: I'd like to add a little to what Karan said about the model training, because I think when we spend time with the healthcare ecosystem, that's one of the things that is most important to them.
Dr. Nate Gross: So not only were these models trained in development with hundreds of physicians who created over 5,000 conversations and 48,500 rubric criteria through which to evaluate AI responses and score them and identify ways that we could improve the model, do additional data acquisition, do additional post-training, hone in on a particular subspecialty or particular area of the world.

[00:12]
Dr. Nate Gross: where users were telling us we could improve health or healthcare in that specific topic.
Dr. Nate Gross: But in addition, I think that close proximity to physicians really leads to calling out the
Dr. Nate Gross: most important parts that should be focused on in model development. So,
Dr. Nate Gross: you know, other places, sometimes I see how a model fared on a medical school exam or a board exam.
Dr. Nate Gross: And healthcare is not multiple choice.
Dr. Nate Gross: You know, patients are coming in with a tremendous amount of complexities and their own stories and nuance and context.
Dr. Nate Gross: And that's presented in many different ways.
Dr. Nate Gross: And part of the job of working in healthcare is being able to draw from those disparate sources, draw from experience, balance all that in your head.
Dr. Nate Gross: And so having a training mechanism that thinks about things like when to escalate and how to escalate and keep that always as the top priority or adaptive literacy.

[00:13]
Dr. Nate Gross: I mean, compare the one-size-fits-all handouts that people get when they visit the doctor today to a model that can respond differently when it knows you're an oncologist versus a primary care doctor versus a pharmacist in Kenya versus a patient at the 12th grade literacy level or the third grade literacy level is extremely important for not only making sure that accuracy and impact is maximized,
Dr. Nate Gross: but also just to make sure that everyone can maximally participate in their own care on the patient side.
Dr. Nate Gross: And then finally, uncertainty.
Dr. Nate Gross: If you go back a year and a half ago, many of the mistakes people would call out about AI models were overconfident hallucinations.
Dr. Nate Gross: And I think in such a high stakes field like healthcare, one of the most important things is that the model can be trained to better know when it doesn't know and say that.

[00:14]
Dr. Nate Gross: And in addition, suggest follow-up that can be dug into either by the patient in a referral to the healthcare system or by the doctor if the doctor is using the model, a test that they might run, additional pathways they may go down to make sure that the patient can be led to the best possible outcome.
Andrew Mayne: We've seen the cost of intelligence drop every year, and it's exciting because every year you're able to get better answers, medicine, everything, healthcare across the board.
Andrew Mayne: But what are the challenges?
Andrew Mayne: What are going to be the blockers or what are you looking at ahead to say that, okay, we have to solve for this?
Karan Singhal: The drop in cost of intelligence has been super exciting here because so much of what we think about and care about here is actually about access.
Karan Singhal: And so the more people have access to technology, the more people will benefit.
Karan Singhal: And that's why we're working on rolling out ChatGPT H ealth more widely to all free users.
Karan Singhal: And so that's incredibly exciting.

[00:15]
Karan Singhal: Another thing that we think about as researchers is like, where will the marginal gains intelligence compound the most?
Karan Singhal: Right. And so I think Nate mentioned this exciting thing, which is like there is more and more data that is being collected that is across different modalities.
Karan Singhal: How do you think about integrating that data across all the different ways that people use Chat GPT and all the different modalities and wearables and things like this that people are collecting?
Karan Singhal: lab tests, things like this. And that's one place where I think a lot of the intelligence will
Karan Singhal: compound and we'll start to see kind of new zero or one capabilities. Like a model looks at my entire
Karan Singhal: history over a decade and tells me a prediction that even a human couldn't have because it's just
Karan Singhal: the model has a higher context size. So thinking about those zero to one capabilities, I think are
Karan Singhal: going to be really cool. The other thing we keep in mind is just like, how are people thinking about
Karan Singhal: and using ChatGPT today? Can we measure that? Can we improve that? And I think we're kind of
Karan Singhal: this interesting point right now. I call this to our team, the transition where, you know, for
Karan Singhal: context, I bike to work and I bike to work. I wear my helmet. I worry about cars and things like this

[00:16]
Karan Singhal: next to me. I just reached the point here in SF, you know, in SF, we have a bunch of self-driving
Karan Singhal: cars, including Waymo's. I just reached the point where, you know, when I'm biking next to Waymo,
Karan Singhal: I actually feel safer than if I was biking next to a human driver, right? I don't worry about
Karan Singhal: whether I'm in their blind spot or not or anything like this. So I feel this protective effect by
Karan Singhal: being next to the Waymo. And I want everybody to have this protective effect, right? I want
Karan Singhal: everybody to have this protective effect with health AI. There are these studies showing that,
Karan Singhal: you know, if you have a doctor in your family, that adds a protective effect to your health as
Karan Singhal: well. And I want everybody, whether they're patient or health professional, to think about the ways
Karan Singhal: in which as a patient, you want to feel safer having this.
Karan Singhal: As a health professional, you want this to be a safety net
Karan Singhal: for the decisions that you're making.
Karan Singhal: So that's another frontier that I think we're going to cross
Karan Singhal: in the next six months or so, which is really exciting,
Karan Singhal: this kind of inflection point.
Karan Singhal: Another thing that we're thinking about is kind of the right ways

[00:17]
Karan Singhal: to think around post-deployment monitoring of certain workflows.
Karan Singhal: And I think a good example here that I'd love to talk about
Karan Singhal: is our AI clinical co-pilot study that we did with PandaHealth.
Karan Singhal: This was a study where we worked with these 20 or so clinics in Nairobi
Karan Singhal: and actually thought about the ways in which we can deploy a safety net
Karan Singhal: for clinicians in that context,
Karan Singhal: which is basically monitoring things that they type
Karan Singhal: into their electronic health record
Karan Singhal: and only interrupting their flow
Karan Singhal: when there's something potentially concerning that's going on
Karan Singhal: or a potential error or things like this.
Karan Singhal: And what we found is that when we deployed this to clinicians in the setting, that there was actually a statistically significant reduction in diagnostic and treatment errors for the clinicians who are using this tool versus not.
Karan Singhal: And I think this is a step in the direction of moving beyond kind of model evaluations and even monitoring of the ways in which people are thinking about using ChatGPT today to actually thinking about workflows in which these technologies can be deployed and the right ways to evaluate those workflows after deployment.

[00:18]
Karan Singhal: I think that's another frontier that we are really excited about and would love to see more from our partners.
Andrew Mayne: Nate, what do you think the challenges are going to be?
Dr. Nate Gross: I'll start with talking through some of the challenges that exist on the professional side.
Dr. Nate Gross: So each day when healthcare professionals use AI, they're looking for the ability to trust what they're seeing in the answer.
Dr. Nate Gross: And so a lot of our recent work has been making sure that answers that the AI is providing are not just grounded in what the model was training on, but are grounded in the latest medical literature, the latest guidelines.
Dr. Nate Gross: And sometimes the latest guidance from their own institution or their own region.
Dr. Nate Gross: Some conditions are treated differently in different areas of the country.
Dr. Nate Gross: Other times, different care settings have different levels of resources, different levels of specialists and additional services on hand.

[00:19]
Dr. Nate Gross: And it can be helpful as a health care professional to be able to quickly navigate that and come up with completely personalized care plans.
Dr. Nate Gross: And so building connectivity within ChatGPT to not only be HIPAA aligned and be used in
Dr. Nate Gross: these secure environments, but also be able to combine sensitive information with the
Dr. Nate Gross: latest medical knowledge, I think is a great path that we've started down and something
Dr. Nate Gross: that will continue to keep trust as the top priority between how healthcare professionals
Dr. Nate Gross: engage with AI.
Dr. Nate Gross: So I think one of the other challenges is that the systems themselves in healthcare are quite siloed, both at an organization level, but also at the tools that have to be used within each organization.
Dr. Nate Gross: AI thus far has been deployed on really a point solution basis in the technology industry, but increasingly the connectivity is becoming available to connect the dots between the hundreds of different systems, some analog, some digital, some structured, some unstructured, many decentralized, many not on the cloud.

[00:20]
Dr. Nate Gross: Being able to connect all of those through unified AI layers to actually make sure that patients and information isn't falling through the cracks and that the connectivity can be maximized to actually bring the greatest amount of impact.
Dr. Nate Gross: That's hard in healthcare and it's certainly not something that we can say is solved.
Dr. Nate Gross: But with many of our recent products ranging from ChatGPT for healthcare and its connectivity to apps and connectors, to the OpenAI API for healthcare, to our Frontier Foundation for models and agents, we think increasingly there's going to be an opportunity to really accelerate what is possible within the healthcare system and what agents can achieve.

[00:21]
Andrew Mayne: Part of this seems like it's very collaborative working with the healthcare industry. And I noticed when using the ChatGPT Health app, the first thing I did was able to put in my records and get all of that. And it looked like there was a lot of just cooperation working across the sort of ecosystem to do this. How has that come to be? Where is this headed?
Dr. Nate Gross: It's extremely important that all of the healthcare system has an equal chance to contribute and engage nationally and internationally with providing the context that will help empower patients to receive the best possible answers from ChatGPT.
Dr. Nate Gross: And so on the electronic health record side, this means working with the government and Centers for Medicare and Medicaid Services, adopting national standards for electronic health record syncing so that patients in just a few taps are able to bring in their context in consented ways.

[00:22]
Dr. Nate Gross: It's being able to tap into existing standards like mobile phones and the most popular consumer health products and the most popular biosensors and wearables to make sure, again, in just one or two taps, patients are able to not only bring in that information, but leverage it in thoughtful ways, in ways that may not have been possible without the combined set of data that can exist in this sort of ecosystem.
Dr. Nate Gross: So, for instance, being able to reference your recent exercise activity when making a plan of how to spend your evening or being able to even do things as simple as, you know, reference your overnight sleep and stress when your agent is helping you set your calendar for the next day and what tasks you take on first.

[00:23]
Andrew Mayne: It's very exciting.
Andrew Mayne: You know, I have, you know, we're a smart ring, a watch, whatever, but I get this data and all I kind of have in my apps are rings to look at and go like, OK, I guess it's doing something.
Andrew Mayne: Being able to plug in ChatGPT has been fantastic because now I'm able to ask those kinds of questions.
Andrew Mayne: But that's very exciting. What you talk about, too, is if you get a plan from your doctor suggestions is literally say, hey, I didn't walk enough yesterday.
Andrew Mayne: What should I do today? I've had to be really good at menu planning and literally go on this menu film, tell me what to order and whatnot.
Andrew Mayne: And so you're saying we're just going to get more of that and much better.
Dr. Nate Gross: Yeah. And that's why our partnerships, I believe, are so important, because in these instances, ChatGPT doesn't replace the incredible technology that our partners are building to go deep on health insights for a particular wearable.
Dr. Nate Gross: But our surface area, our opportunity to bring in that health information can now extend to the many different ways people use ChatGPT, such as what they're going to cook for dinner or how they're going to plan their afternoon.

[00:24]
Dr. Nate Gross: You know, sometimes I think of two patients and one patient has to navigate the healthcare system by themselves.
Dr. Nate Gross: And the other patient maybe has a spouse come with them.
Dr. Nate Gross: And that spouse has a clipboard and used to work as a healthcare professional and is very attentive, if not neurotic, and can follow up on details and is connected to your personal calendar.
Dr. Nate Gross: And the best aspects of that with consent for the patients that want to, I think, represents a future where we can make it easier and easier for patients to follow care plans, to play active, captain-like roles in their own health in partnership with their care teams and their physicians.
Dr. Nate Gross: And I think if we can remove a lot of the friction that historically exists between those processes, whether it's just information not following or there's a lot to keep track of or a lot of old information to parse and bring in, we can do a tremendous amount of good or we can help patients themselves be empowered to do a tremendous amount of good in their own care plans.

[00:25]
Andrew Mayne: And you know, as a physician, that it's hard to give as much time as you would like, because you're going to always have more patients you have to deal with than you have hours in the day. And it's interesting to see a kind of a technology that has infinite time, infinite patience to be able to do that as a complement to that.
Dr. Nate Gross: I mean, if there's one thing that healthcare professionals are short on, it's time.
Dr. Nate Gross: So when we think about our role internally at OpenAI, we often break down the work that we're doing into three buckets.
Dr. Nate Gross: Raise the floor.
Dr. Nate Gross: So make sure that AI and the benefits of AI are accessible to everyone.
Dr. Nate Gross: And that could be patients, that could be healthcare professionals and others working in health-related industries.
Dr. Nate Gross: sweep the floor, which means help doctors and help other health professionals save time from

[00:26]
Dr. Nate Gross: the tremendous administration and bureaucratic burdens that they have every day so that they can
Dr. Nate Gross: spend more time with their patients. And then thirdly, raise the ceiling. The
Dr. Nate Gross: impact that AI can have in healthcare, I think will allow us to look back on this space in a few
Dr. Nate Gross: years and say, wow, we have all accelerated together in a way that medicine is still in
Dr. Nate Gross: the driver's seat, but is also far more empowered than ever before.
Andrew Mayne: Yeah.
Andrew Mayne: I don't think anybody feels like their doctor spent too much time with them.
Andrew Mayne: So it looks like this is going to be helpful to solve for that.
Andrew Mayne: What has been your favorite aha or wow, or this is really cool moment in the intersection
Andrew Mayne: of AI and healthcare?
Karan Singhal: I'll answer your question in a non-standard way, which is I think the most amazing thing to see for me in the last year has been the rate of adoption of health, actually even beyond the ChatGPT Health product before we announced the ChatGPT Health product.

[00:27]
Karan Singhal: It's been one of our fastest growing use cases is kind of health and wellness questions.
Karan Singhal: And we shared that hundreds of millions of people a week are starting to use ChatGPT for health and wellness.
Karan Singhal: I think seeing that rapid growth, especially coming from a background of being motivated to work on this problem because it felt like healthcare and clinical AI world were not super aware of the potential of LLMs in healthcare and seeing how far we had come, I think has been a really special moment for me.
Dr. Nate Gross: There's no doubt that the adoption of this technology and the fact that it is increasingly collaborative with the healthcare system, it is increasingly driving feedback loops back to us to improve the models is the most meaningful thing and the most mission aligned thing.
Dr. Nate Gross: But what I also get excited about is what our research team is increasingly able to give back to them using that feedback.
Dr. Nate Gross: And not only is it the capabilities of the models, but it's what can be unlocked once those models are allowed to run longer and have more context.

[00:28]
Dr. Nate Gross: And we're starting to see discoveries of medications that have been sitting on a shelf that all of a sudden AI has found ways for them to have meaningful and direct value in patient lives.
Dr. Nate Gross: It is starting to scale experiments that we as individuals wouldn't have been able to juggle on our own.
Dr. Nate Gross: And that partnership combined with that increased capability to finally move from being interesting to being useful and increasingly to being transformative is, I think, what is the most exciting thing for us heading into this year.
Andrew Mayne: Now that you've been working on this for some time, you've been engaging with clinicians and talking to people helping deploy this.
Andrew Mayne: What has been some of the feedback you've seen?
Karan Singhal: I think the experience of flying to Nairobi and seeing the clinicians using the tool and the ways in which we did this thing, which we call active change management, where we worked really closely with these clinicians and flew to Kenya a couple of times to think about the ways that we could deepen their workflows using the AI tool and make it something that not only made sense to them, but actually became kind of something that was indispensable for them.

[00:29]
Karan Singhal: And so as we were concluding the study, the team was actually thinking about, the team at PandaHealth was thinking about potentially running another study.
Karan Singhal: And they actually had a lot of hesitance around running another study because that would have involved having some group of clinicians using AI and some group of clinicians not using AI.
Karan Singhal: They actually felt that it was dangerous to have a group of clinicians not using the AI.
Karan Singhal: And so that's the point at which I was like, wow, we have done something major here.
Dr. Nate Gross: I think that the stories that we get back from our members every day are one of the most meaningful parts of the job. And these are from caregivers that are increasingly under strain, taking care of family members, trying to navigate their own health at the same time.

[00:30]
Dr. Nate Gross: This is from doctors and nurses who are truly overloaded every day, and we can help them extend their expertise and, you know, compress the tough parts of their day a little bit more.
Dr. Nate Gross: And then sometimes, and this is more rare, but increasing, it's the miracle cases.
Dr. Nate Gross: It's the patient who had been bouncing around the system for years, the unsolved diagnosis, the emergency where information wasn't present.
Dr. Nate Gross: And suddenly being able to step in and assist and accelerate and bring people into the care that could really help is truly a privilege.
Andrew Mayne: It's exciting.
Andrew Mayne: It's an amplifier, and every doctor I know wants to be able to do more for their patients.
Andrew Mayne: Thank you very much.
Andrew Mayne: This has been very interesting, guys.
Dr. Nate Gross: Thank you.

</details>

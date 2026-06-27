---
title: "Episode 16: Building AI for Life Sciences"
channel: openai
url: https://www.youtube.com/watch?v=UZyH0nx5zgI
youtube_id: UZyH0nx5zgI
published: 2026-04-16
duration: "44:25"
captions: en
---

# Episode 16: Building AI for Life Sciences

[![Episode 16: Building AI for Life Sciences](https://img.youtube.com/vi/UZyH0nx5zgI/hqdefault.jpg)](https://www.youtube.com/watch?v=UZyH0nx5zgI)

<details>
<summary>자막: Episode 16: Building AI for Life Sciences (44:25)</summary>

[00:00]
Andrew Mayne: Hello, I'm Andrew Mayne, and this is the OpenAI Podcast. On today's episode, we're talking with
Andrew Mayne: research lead Joy Jiao and product lead Yunyun Wang about OpenAI for Life Sciences. We'll explore
Andrew Mayne: what new models are making possible in biology and medicine and what it takes to deploy the most advanced capabilities responsibly.
Joy Jiao: This allows it to kind of reach new levels of difficulty and
Joy Jiao: discovery that we didn't think was even possible before.
Yunyun Wang: Putting like really capable expert level knowledge in the hands of a greater amount of people.
Joy Jiao: One of the taglines was to scale test time compute to cure all disease. So that is like our team tagline.
Andrew Mayne: We started off with just a basic API and then we had ChatGPT, which is more conversational,
Andrew Mayne: was really good for text as code became a capability, went through basically code models
Andrew Mayne: and then Codex. Now that you're getting more scientists and the life sciences working on
Andrew Mayne: these systems, does that mean things have to evolve to help with the way researchers might work with these tools?

[00:01]
Yunyun Wang: Yeah, we're really excited to build and deploy the life sciences model series.
Yunyun Wang: So this is a new biochemistry focused model series that's really anchored on these very complex
Yunyun Wang: life science research workflows. And we're focused on adding new like mechanistic understanding,
Yunyun Wang: starting with genomics understanding and protein understanding, and really focused on early
Yunyun Wang: discovery use cases, because we feel like that's one of the core bottlenecks that greater thinking
Yunyun Wang: time, greater compute, and really leveraging more capable AI models can help meaningfully
Yunyun Wang: scale some of these research barriers. And I think there's also a model orchestration piece of
Yunyun Wang: actually how to embed this into workflows. And it's been really great, first off, having all these
Yunyun Wang: different product surfaces to deploy to.
Yunyun Wang: We're seeing a lot of really great literature synthesis
Yunyun Wang: workflows happening on ChatGPT.
Yunyun Wang: And these models really push the frontier of long trajectory

[00:02]
Yunyun Wang: agentic workflows.
Yunyun Wang: And we're really able to empower that on Codex.
Yunyun Wang: And more on the model orchestration piece
Yunyun Wang: is that I think for enterprise use cases,
Yunyun Wang: there's this reproducibility and repeatability element.
Yunyun Wang: And we are trying to overcome this by working on some of the life sciences research plugins
Yunyun Wang: that we're shipping for very specific translational bio users.
Yunyun Wang: So the life sciences research plugin has over 50 skills, which are essentially templatized
Yunyun Wang: repeatable workflows that if you need to, whether do some sort of cross evidence match
Yunyun Wang: and search across various different papers, or do pathway analysis, something that's like
Yunyun Wang: repeatable that you often do, we can have almost like a one-click deploy option by using our
Yunyun Wang: life sciences plugins on top. And that's also how we're seeing the balance between scaling for very specialized purposes.
Yunyun Wang: Something we're hoping to get into is maybe clinical purposes, but also make

[00:03]
Yunyun Wang: it still very general use for all foundational biology.
Joy Jiao: I think the models can get quite far by
Joy Jiao: using tools. So for example, we can use open source protein structure prediction algorithms
Joy Jiao: and start a research stack. And in this case, the model is acting kind of like a regular
Joy Jiao: computational biologist. You will kind of go run these tools on a computer. You will look at the
Joy Jiao: output. You will tweak the input a little bit. So I think that is something our models can already
Joy Jiao: do. I do think what will make the models even more powerful is to start to turn them more into
Joy Jiao: kind of a biochemistry expert. And I think with this kind of intuition and expertise,
Joy Jiao: you can use these tools even more intelligently and get at the right answer more quickly.
Andrew Mayne: How did you get your interest in life sciences?
Joy Jiao: My, I guess, original background was actually in life sciences. So I've always been interested in
Joy Jiao: biology as a kid. I got my PhD in systems biology around like a decade ago from Harvard.

[00:04]
Joy Jiao: I found academia to be very interesting, but the pace was a little bit more slow moving than I would have liked.
Joy Jiao: And I think just the experience of kind of like having to physically be in the lab and kind of like transferring small amounts of liquid from one tool to another.
Joy Jiao: I think I wanted something a little bit faster paced where I felt like I was more in direct control of my own velocity.
Joy Jiao: So I went from that to software and I ended up here at OpenAI.
Joy Jiao: And so this is kind of like a full circle moment for me
Joy Jiao: where I'm starting to look at biology again
Joy Jiao: and looking at how to accelerate my previous self with AI.
Joy Jiao: So yeah, really excited to see what progress AI can make in this space.
Andrew Mayne: So you're like, yeah, this is too slow.
Andrew Mayne: Let me go off an AI and speed it up so I can get back into it.
Joy Jiao: Yeah, except from this end,
Joy Jiao: I don't really ever want to touch a pipette or anything again.
Joy Jiao: So I would prefer for my robots to do it for me.
Yunyun Wang: Yeah, we joke about that a lot.
Yunyun Wang: A lot of our motivation for this is we can automate pipetting
Yunyun Wang: and never have to do that again.

[00:05]
Andrew Mayne: Well, that's what's interesting. I was looking at what you all did with Ginkgo Bioworks and the idea of taking GPT-5 and taking an AI system and then working with a robotic lab and how it was able to speed things up. Could you tell us a little about that?
Joy Jiao: Yeah, the Ginkgo work is interesting because I think when it started, I think it was like July of last year, 2025.
Joy Jiao: And at that point, GPT-5 had just finished training.
Joy Jiao: We were really not sure if the models could do any kind of biology.
Joy Jiao: We didn't really have that much biology in our training data.
Joy Jiao: It was mostly math and computer science, which I think makes sense because these things have verifiable solutions.
Joy Jiao: And this is usually not the case in biology unless you can go and do the experiment in a lab, right?
Joy Jiao: So when we started the collaboration with Ginkgo, it was really, can the model do any biology at all?
Joy Jiao: Can it design experiments that actually make reactants, like make the product that we want?
Joy Jiao: So it was actually quite surprising, I think, when GPT-5 designed the first set of experiments with Ginkgo.

[00:06]
Joy Jiao: And the results came back.
Joy Jiao: Oh, we made a non-zero amount of protein.
Joy Jiao: That was actually quite surprising.
Joy Jiao: And then I think progressing from that point in time, which is just roughly like six months ago to now, where it actually just feels quite obvious that our models can accelerate science is actually just really surprising.
Yunyun Wang: And it really shows the art of the possible, I think.
Yunyun Wang: I think before that experiment led by Joy and the Ginkgo team was conducted, I think we really didn't know for ourselves.
Yunyun Wang: And I always say, like, we kind of learn that for ourselves when we engage in these experiments and we have a few more in the works with others.
Yunyun Wang: And I think that is like the type of acceleration that we're looking for.
Yunyun Wang: Ingesting high throughput experimental data is really difficult.
Yunyun Wang: It's very compute intensive.
Yunyun Wang: And I think for a lot of these scientific workflows, like the true bottleneck for the speed and progress of scientific acceleration is at like almost a human bottlenecks.

[00:07]
Yunyun Wang: And I think the future that me and Joy see is that it's no longer human bottlenecks, but rather maybe compute bottlenecks.
Yunyun Wang: And we're really able to deploy many sub-agents doing parallel orchestration to divide and conquer all these tasks.
Yunyun Wang: And the researcher can now spend their time on really analyzing, interpreting the most meaningful insights coming out of that.
Andrew Mayne: So Yunyun, how did you get into this?
Yunyun Wang: Yeah, I think reflecting back, I've actually been working on like biology research in some shape or form for a majority of my time here at OpenAI.
Yunyun Wang: So I first started on working on biorisk mitigations and a lot of our biodefense initiatives.
Yunyun Wang: And so I feel like coming to now working on the life sciences research side gives me like just appreciation for how difficult this problem is and tackling it from both sides.
Yunyun Wang: And my initial entries point into wet lab research was actually through doing a lot of infectious disease and virology work.
Yunyun Wang: So I think I've always done the interest in biosecurity in that way.

[00:08]
Yunyun Wang: So this just feels like a really great moment right now to work on it, especially when our models are getting more capable with beneficial use and just general life sciences.
Andrew Mayne: How long has OpenAI been focused on life sciences?
Yunyun Wang: Yeah, I would say it was really the way we design our capability evals that show us that this is possible.
Yunyun Wang: So it's been, I think, for at least two years now that we have worked on a lot of our early research experiments.
Yunyun Wang: And now with the Ginkgo autonomous wet lab model in the loop experiments.
Joy Jiao: I think we have a few more research partners in the space that we're really excited about.
Joy Jiao: I think I can't actually name everyone right now, but there's a lot of stuff kind of in the chemical design, protein design, enzyme design space that I think is very AI native and a lot of people are interested in.
Joy Jiao: So understanding how the world works, understanding how chemicals react, understanding how cells interact, how pathways inside cells interact, all the way to can we accelerate drug discovery?

[00:09]
Joy Jiao: So given a disease can a model help scientists understand the mechanism, can we once given a target actually design a drug against that target?
Joy Jiao: Can we even accelerate the FDA approval process?
Joy Jiao: So I think there's a role for AI to play kind of at every step of this pipeline.
Joy Jiao: And yeah, I think there's a lot of AI possible in everything.
Andrew Mayne: I've been to some of those cutting edge labs and on the outside you have this impression of it.
Andrew Mayne: Then you walk in there and you literally see somebody with a row of Petri dishes, a row of samples, and just some grad student going click, click, click.
Andrew Mayne: And I'm like, oh, this is the pace of science.
Andrew Mayne: This is fast.
Andrew Mayne: With me.
Andrew Mayne: Yeah, exactly.
Andrew Mayne: You're like, enough of this.
Andrew Mayne: I got to go speed this up.
Andrew Mayne: But we forget that's often the pace of science is just how fast the human hands can move through that.
Andrew Mayne: And with a tool like that, it's kind of exciting.
Andrew Mayne: When you start using these tools to maybe think about new pathways for treatments or just evaluate, you also introduce the idea that these could be used for things that maybe are less desirable.

[00:10]
Andrew Mayne: Bioweapons are something that comes up a lot.
Andrew Mayne: The fact that if an AI can figure out how to do a code exploit, might be able to figure out how to do a gene exploit.
Andrew Mayne: How are you addressing that?
Yunyun Wang: Yeah, that's a great question.
Yunyun Wang: And I think it is just probably one of the most severe risks that we're currently really tracking for rising AI capabilities.
Yunyun Wang: Our first approach to that was really thinking about how do we assess for information hazards?
Yunyun Wang: At what point does a model now maybe give the final step in a synthesis of a dangerous pathogen?
Yunyun Wang: And what we found is that the precursor steps to that really looks very benign.
Yunyun Wang: And it's really hard to distinguish between.
Yunyun Wang: So another way to put it is like the same steps that a beneficial, like a legitimate actor might take is looks very similar to the ones that a dangerous, harmful actor.
Andrew Mayne: You start with something that's.
Yunyun Wang: Yes, exactly.
Yunyun Wang: So I still think that we we made the right call for really taking a very risk averse approach to that.

[00:11]
Yunyun Wang: But now I'm really excited about like differentiated access and like responsible deployment as really a core pillar of all of our safeguards work and really understanding that there are different user segments.
Yunyun Wang: And I almost feel like the future we're going towards is something like models as a professions, similar to how they models have different personalities.
Yunyun Wang: And sometimes you want to invoke the right one, depending on the type of like workflow you're looking at.
Yunyun Wang: So I think how this translates is similar to how biologists working on like therapeutics and their research, they require access to data sets are often very tightly controlled or they require access to just expert level.
Yunyun Wang: Like they all have PhDs and have like expert level like biology, like knowledge.
Yunyun Wang: How does that compare to how does that translate over to two models?

[00:12]
Yunyun Wang: I think that's why we have to kind of similarly take the same training approach, but also the same security approach and deploying that in like a way where we can have those very heightened enterprise grade controls in place.
Andrew Mayne: So you just mentioned safeguards.
Andrew Mayne: Can you explain how that applies here, where you would need them, why you would need them?
Yunyun Wang: Yeah.
Yunyun Wang: So we very thoughtfully design and design new safeguards for pretty much all of our models across very different risk areas.
Yunyun Wang: But I think when it came to bio, this was like the first dual use risk that is both also a capability risk.
Yunyun Wang: So it very much correlates with how we as capabilities improve, the risk correlates.
Yunyun Wang: And I think that's why our first approach, when we really there was no precedent for a lot of this work,
Yunyun Wang: and we were the first to really activate these high safeguards when we saw that significant reasoning jump in our model capabilities.
Yunyun Wang: We really wanted to make sure that we did it right.
Yunyun Wang: And I think the best way to get it right is to incrementally deploy.

[00:13]
Joy Jiao: Yeah, I think it's really a fine line between having a very capable model that's capable of accelerating benign science and beneficial science versus a model that could be used by a bad actor.
Joy Jiao: And I think the safest model here would be a model just had no capability, right?
Andrew Mayne: It's not very good.
Joy Jiao: Yeah, it's not very good, but it's very safe.
Joy Jiao: And on the other hand, if you had a model that is basically an oracle of the physical world, it basically knows everything about every experiment, that model could fall into the wrong hands and do potentially very bad things because someone can go and say, hey, design a new novel pandemic potential pathogen.
Joy Jiao: And the model can just go and do that autonomously.
Joy Jiao: So I think we need to kind of figure out where we draw the line in between the two and kind of think about who gets access to a potentially very capable model and who doesn't.
Joy Jiao: And what we found in kind of what we call general access traffic is that it's very difficult to figure out what a user's actual intentions are just from kind of reading a prompt.

[00:14]
Joy Jiao: And I think as an example of this, let's say someone says, hey, help me clone a gene.
Joy Jiao: The model might not even be given what the gene is, but it can come up with a protocol for it.
Joy Jiao: And so this gene could just be something like green fluorescent protein or it could be a toxin.
Joy Jiao: And there's basically no way to figure that out from the context of the conversation.
Joy Jiao: And so this becomes a very difficult problem in production.
Joy Jiao: And basically, I think, like you said, we decided to kind of err on the side of safety
Joy Jiao: here and basically say that, OK, if we think that there is a potential for misuse, we either
Joy Jiao: have the model kind of self-refuse the user, in which case it tends to say things like,
Joy Jiao: Sorry, I can't really help you with that, but I can give you a high-level overview of this protocol instead.
Joy Jiao: And this, unfortunately, very much annoys our kind of professional scientists, understandably.
Joy Jiao: And we also kind of have multiple layers of mitigation on top of that.

[00:15]
Joy Jiao: But I think really to unlock the full capabilities of our models, what we need is this differentiated access.
Joy Jiao: And what this means is we know who the user actually is.
Joy Jiao: They are a professional working at a legitimate research institution or a pharma company.
Joy Jiao: And because of the regulations around these institutions, we know that, for example, all
Joy Jiao: the reagents are being tracked.
Joy Jiao: All the cell lines that they're using are being tracked.
Joy Jiao: And so this gives us confidence that this is a legitimate user and not a random person
Joy Jiao: in a basement doing who knows what.
Joy Jiao: And that allows us to give them basically more capabilities than we are able to provide
Joy Jiao: to the general access traffic.
Andrew Mayne: What can you do right now?
Andrew Mayne: If you're working with the models,
Andrew Mayne: you're working it within a laboratory,
Andrew Mayne: what would you say the capability is at this moment?
Joy Jiao: So I think people use the models
Joy Jiao: for very different things.
Joy Jiao: I've talked to people in the Baker Lab recently

[00:16]
Joy Jiao: on kind of how they've been using our models on Codex.
Joy Jiao: And sometimes it's as simple as,
Joy Jiao: hey, can you write a spreadsheet for me?
Joy Jiao: I want to just minimize the number of pipetting steps
Joy Jiao: that I have to make.
Joy Jiao: And this hits me very hard because I had done the same thing by hand in grad school.
Joy Jiao: So that's like a very simple just mathematical software operation.
Joy Jiao: And then there's much harder tasks.
Joy Jiao: Can you design a enzyme for me without these biological design tools?
Joy Jiao: So I think there's a huge range of sophistication.
Joy Jiao: Yeah.
Yunyun Wang: And something I'm very excited about is how we can use our models to be a more powerful
Yunyun Wang: discriminator and like really testing and assessing like new novel ideas. And I think something that
Yunyun Wang: I've been noticing as a trend with a lot of our research partners and also the users of our models
Yunyun Wang: is that models for scientific research and tasks almost require a different like persona or a
Yunyun Wang: different prompting style. So we, I often feel like, you know, like a model that is much more

[00:17]
Yunyun Wang: scrutinizing or a skeptic at good ideas is it's very similar to how human scientists would go
Yunyun Wang: assess originality and feasibility. It's really, I think, helping understand out of all the new
Yunyun Wang: papers and new publications out there that push the frontier of a lot of these hypotheses,
Yunyun Wang: what are the ones that are really feasible and valid for testing that's going to help
Yunyun Wang: lead to new breakthroughs? And then translating this to something like disease target screening,
Yunyun Wang: selection, like the potentials for these drug targets are endless, but it's really like narrowing
Yunyun Wang: down the aperture. And I feel like that's where like the assistance comes. Like this is extremely
Yunyun Wang: difficult work to do at scale and having a model that can like empower and accelerate that process,
Yunyun Wang: I think is kind of like one of the immediate impacts we're hoping to see by responsibly deploying this model to those users.
Andrew Mayne: It seems like it's a very interesting trajectory. You went from
Andrew Mayne: There was, you had GPT-3 on the API and GPT-3.5, then you get ChatGPT, and now we have ChatGPT apps, and now we have Codex.

[00:18]
Andrew Mayne: And it sounds like these things, just the number of things you can do with this continues to grow.
Andrew Mayne: How would you see this building?
Andrew Mayne: You know, do you see this as basically just becoming a complete infrastructure for kind of every kind of inquiry you might want to pursue?
Joy Jiao: Yeah, I think the dream is to have a lot of the basic foundations of scientific workflows happen on Codex.
Joy Jiao: and I think that the goal is to have Codex to pretty much be able to do everything that is
Joy Jiao: possible to do on the computer. Of course, we also want to extend beyond that with kind of
Joy Jiao: hooking it up to robotics and so forth. But I think right now we already do things, for example,
Joy Jiao: if we have a bunch of different dev boxes on our remote, on our laptop, we can actually say,
Joy Jiao: hey, Codex, go and run this code on all of these different dev boxes that are all remote and then
Joy Jiao: Codex can do that. We can say, monitor this for me. And I can kind of like go away and do something
Joy Jiao: else. And the Codex are just like, they're watching all the logs for you. It can build a lot of just

[00:19]
Joy Jiao: kind of fit for purpose software for analyzing specific pieces of data, for visualizing data.
Joy Jiao: So for example, if we have experimental biology data that we're sending each other on the team,
Joy Jiao: what I've noticed recently is instead of sending the raw data, we've started sending HTML files
Joy Jiao: are just these kind of like beautiful UIs that Codex has built with kind of like spinning proteins.
Joy Jiao: And it's actually just really, it kind of changes the way that we share with each other and collaborate.
Yunyun Wang: Yeah, when we first started mapping out how users and organizations might adopt this,
Yunyun Wang: I think we envisioned that each scientist would get their personal assistant or their coworker.
Yunyun Wang: And this is a way that they can scale up their collective output.
Yunyun Wang: And then the next paradigm of that would be scaling up whole research institutions where a whole program team can actually deploy a workforce of various agents and they can all do parallel task delegation, kind of mimicking a lot of these existing patterns.

[00:20]
Yunyun Wang: And we can figure out the pieces of how they can all collectively work together to solve larger tasks.
Andrew Mayne: It's interesting because OpenAI has talked about the need for compute.
Andrew Mayne: And I think that sometimes we just sort of think like, okay, so I can have more conversations and stuff.
Andrew Mayne: But when you're talking about the idea of building these tools to become entire platforms or scientific exploration, it sounds like the compute advantage is really critical.
Joy Jiao: Yeah, I think there's two different axises we can think about how we are scaling compute.
Joy Jiao: The one that I think everyone's familiar with is just getting bigger models.
Joy Jiao: And I think as we went from GPT-2 to 3, there was a huge size increase.
Joy Jiao: And there were just these amazing emergent properties from the model.
Joy Jiao: I mean, thinking about when GPT-2 was released, we were all kind of collectively amazed that
Joy Jiao: it was able to write a coherent article about unicorns.

[00:21]
Joy Jiao: And now we're in a completely different world, right?
Joy Jiao: And a lot of that is driven by model architecture, yes, but also just the number of parameters
Joy Jiao: in the model just allows it to achieve this incredible intelligence that we never thought
Joy Jiao: was possible before. And then on the other axis, we have what we call test time compute scaling.
Joy Jiao: And this is when you are inferencing a model, when it's kind of spitting out tokens.
Joy Jiao: And this is a thing that happened fairly recently when we call these reasoning models,
Joy Jiao: is that it can think for a scalable amount of time. And this is variable depending on how
Joy Jiao: difficult it thinks a problem is. But we can have the model think for days where really there's kind
Joy Jiao: of ways to just kind of have it think forever about a problem. And this allows it to kind of
Joy Jiao: reach new levels of difficulty and discovery that we didn't think was even possible before.
Andrew Mayne: When we think about data centers, we often just sort of think about it as generating cat pictures
Andrew Mayne: or doing text conversations. But I think that's really the helpful framework to look at is that

[00:22]
Andrew Mayne: these are going to be systems for doing extremely long-term, big, complex processes of thinking
Andrew Mayne: about this. And to me, it just makes a lot more sense when projects like Stargate saying,
Andrew Mayne: we're going to be building a lot of compute. It's not just for what we're doing now, but it's going to be for things like that.
Joy Jiao: When we had first announced the Teams formation on Slack,
Joy Jiao: I think one of the taglines was to scale test time compute to cure all disease. So that is
Joy Jiao: It's like our team tagline.
Yunyun Wang: It's our team motto.
Andrew Mayne: That's ambitious.
Joy Jiao: Yeah.
Andrew Mayne: I had a friend whose child was born with one of those orphan diseases, and she would do
Andrew Mayne: fundraisers, do everything she could to try to support.
Andrew Mayne: Some researchers were trying to find a cure for this, but there's just not enough time,
Andrew Mayne: not enough people.
Andrew Mayne: And I'm hopeful that we're kind of in an age now where these kinds of tools are going to
Andrew Mayne: make that maybe a thing of the past.
Joy Jiao: Yeah.
Joy Jiao: I think we're already seeing the model help a lot in these cases.
Joy Jiao: I think from things like drug repurposing.
Joy Jiao: So for example, a drug that's already been cleared by the FDA

[00:23]
Joy Jiao: for use in one different indication,
Joy Jiao: but from mechanistic understandings of how that drug works,
Joy Jiao: the model has suggested in many different cases
Joy Jiao: for maybe you can use this drug to temporarily ameliorate symptoms.
Joy Jiao: We're also seeing a lot of advances in personalized medicine.
Joy Jiao: So for example, the design of ASOs or other RNA-based treatments is very common.
Joy Jiao: And I think, yeah, we are actually very, very close to being able to scale this up in a really vast way with AI.
Joy Jiao: I think just in the next year or two, I think we'll see very big changes here.
Andrew Mayne: Every researcher I know, when you ask them what they could use in their lab, they always say more hands, more people, more people doing this kind of work.
Andrew Mayne: And you hear some people talk about, well, is AI going to displace that?
Andrew Mayne: And I think, no, it sounds like it's just a big accelerator
Andrew Mayne: for all the things that could be done.
Joy Jiao: Yeah, I completely agree.

[00:24]
Joy Jiao: I feel like when you think about lab automation, for example,
Joy Jiao: a lot of the bottleneck comes from actually being able to translate a protocol
Joy Jiao: into something that can be run on the platform.
Joy Jiao: And we've had partners tell us about how Codex has been helping them do this.
Joy Jiao: And this is kind of fundamentally a half coding problem,
Joy Jiao: half understanding how a lab works.
Joy Jiao: And then I think thinking about the data analysis piece, I feel like having our models kind of walk through a user who maybe doesn't have the deepest understanding of statistics.
Joy Jiao: They can still rigorously analyze the data that's coming in.
Joy Jiao: The model can kind of help them probe different hypotheses or it can suggest different statistical tests.
Joy Jiao: It can point out potential issues and biases in the data.
Joy Jiao: I think these are all ways of kind of uplifting individual scientists and helping them do better science.
Joy Jiao: But I don't think we can ever fully replace the scientists in the loop.
Andrew Mayne: So you've been putting it into the lab.
Andrew Mayne: You've figured out how to help with automation.
Andrew Mayne: Where do you think we're going to be six months from now, 12 months from now?

[00:25]
Joy Jiao: Well, I would really love to get to the point where we can say that AI has designed a new drug or cured a disease.
Joy Jiao: I don't know if that can happen in six months, but I will hope in the next few years that's going to happen.
Joy Jiao: I think we're seeing signs of this happening kind of all over different stages of the pipeline.
Joy Jiao: I think obviously earlier in the drug discovery process where you're kind of looking at literature synthesis or the model is kind of discovering new biology.
Joy Jiao: For that to become a new drug on the market is going to be a very long process, possibly like a decade.
Joy Jiao: But I think there's ways that we can really speed up this process by starting at maybe the clinical trial stage.
Joy Jiao: We're starting a little bit before then in the safety reviews or in the drug design phase.
Joy Jiao: So I think, yeah, basically that's what I'm the most excited about coming up in the next few years.
Yunyun Wang: Yeah, for me, I think I'm most excited about all the possibilities
Yunyun Wang: that our users, our scientists can do on our platforms. So for one, I think a huge win would

[00:26]
Yunyun Wang: be if a researcher can patent a new finding or a new discovery on our platform and using our models.
Yunyun Wang: And that's why we really focus on early discovery and starting with building, like teaching the
Yunyun Wang: models, like the mechanistic understanding. So this is, again, like trying to provide the most
Yunyun Wang: powerful tools through our life sciences models to these scientists so they can really accelerate the speed of their research.
Andrew Mayne: Do you think we'll get to a point where the models are going to get
Andrew Mayne: really good at basically predicting the cell or predicting the outcome?
Joy Jiao: I think definitely, yes. I think it depends on the complexity of a system. So for example, one thing our models are already
Joy Jiao: very good at is predicting the outcome of a chemical reaction. And I think as you increase
Joy Jiao: in biochemical and biological complexity, some of the hardest things to predict is given a drug,
Joy Jiao: will this be toxic to a specific person or to a specific system? And I want to slowly work our way

[00:27]
Joy Jiao: up to that, but that is definitely on a roadmap. That's something we want to do eventually.
Andrew Mayne: When we're looking at models that do things like language or math, it's pretty easy to
Andrew Mayne: put together evals for it? Did it get the problem right or get it wrong? What do evals look like for models that are doing biology?
Joy Jiao: Yeah, we have various different ways of evaluating model
Joy Jiao: performance. A really nice way to do this is kind of with experimental data. So someone has already
Joy Jiao: done the experiment and then you ask the model, can it kind of predict the outcome of these
Joy Jiao: experiments? So a lot of the kind of virtual cell work, basically it looks like this, right? So
Joy Jiao: model and then you try to get it to predict a unseen perturbation. We can also do a lot with
Joy Jiao: synthetic data. And this means that maybe you have generated a set of data and you put very specific
Joy Jiao: characteristics in this data that could be kind of like foot guns for the model.
Joy Jiao: And these are things that maybe a typical computational biologist might encounter day to

[00:28]
Joy Jiao: day. So this could be some weird bias in the data. It could be some QC thing that you have to do or
Joy Jiao: statistical correction. And because we generated the data ourselves, then we can actually go and
Joy Jiao: test the model's capability as a computational biologist that doesn't catch all of these
Joy Jiao: different mistakes. So there's a lot of different ways you can be creative with evaluation.
Joy Jiao: But that being said, I think YLAB is still kind of the final real evaluation of the model, right?
Joy Jiao: And as you like to say, nothing in biology is really real until you can prove it in the real
Joy Jiao: world. And so we do have a lot of research collaborations where we try to do just that.
Yunyun Wang: Yeah, evals have really become more complex and sophisticated over time.
Yunyun Wang: And I think that's especially true for designing evals that can really capture both value creation, but solving complex problems for life sciences.
Yunyun Wang: So I think we really try to focus on examples that are not like toy problems, but really capture that.
Yunyun Wang: Like, for example, like the the messiness of like pre-processed site data.
Yunyun Wang: And when we design these new evaluations, a starting point is often just trying to recreate an existing experiment.

[00:29]
Yunyun Wang: So something that has already a baseline. So we already know what the either current state of the art looks like or the current ground truth looks like.
Yunyun Wang: So a evaluation I'm really excited about is looking at if our models can assess like the antibody binding predictions and looking at how that's been done for an existing virus variant.
Yunyun Wang: And then once we have already done that baseline, we can push forward and say, can we do this with something that hasn't been done before?
Yunyun Wang: And I think that is like some of the precursor steps to de novo antibody design, maybe expanding the neutralization for new viral variants.
Yunyun Wang: And that's also on the path to new treatments and potentially developing new vaccines.
Andrew Mayne: What has been the reception in the life sciences, particularly at conferences in the community, people you know?
Andrew Mayne: Have you seen a lot of willingness to embrace this or skepticism or people who just don't think it's helpful?

[00:30]
Joy Jiao: I think it probably depends on what part of the country you're in.
Joy Jiao: I feel like kind of being on the West Coast, everyone is pretty AI-pilled.
Joy Jiao: And so they really embrace this AI scientist, the agentic workflows, and they really kind of see the future for AI.
Joy Jiao: When I'm at a conference on the East Coast, this changes a lot.
Joy Jiao: I think people are generally a bit more skeptical. Maybe there's a little bit more
Joy Jiao: doubt around the AI capabilities. And yeah, I think it's just maybe like a cultural difference.
Joy Jiao: I think most of the big AI labs are here. And so we kind of have a firsthand experience of what the
Joy Jiao: models are capable of. And this kind of changes our perspective a little bit.
Andrew Mayne: How do you bridge that gap? How do you get more scientists to understand? Because it sounds like
Andrew Mayne: the more people contributing, the better, because there are weaknesses or areas need to be improved
Andrew Mayne: upon and the more you get people who are maybe skeptical about this to sort of figure out how to participate?
Joy Jiao: Yeah, I think there's a few different ways. The easiest way is by launching our models

[00:31]
Joy Jiao: through different platforms like Chat or Codex. And I think just by kind of showing individual
Joy Jiao: scientists how useful this could be, maybe just making a serial dilution spreadsheet for someone
Joy Jiao: who's pipetting, but that has real value, right? And I think you can kind of build up from there.
Joy Jiao: I think coming from the other end, we do have these more deep research collaborations with labs
Joy Jiao: for example, like antibody design or enzyme design. And these sort of things are kind of more,
Joy Jiao: you know, they result in publications and then people will read and say, okay, you know,
Joy Jiao: a AI system did a lot of work. It has biological novelty. It's been proven out in the wet lab. And
Joy Jiao: so I think that also lends credibility to the system. Yeah. I think the simple answer is you
Yunyun Wang: show by doing and you show by publishing and engaging with the scientific community.
Yunyun Wang: And I think the skepticism is really healthy and should be welcomed.
Yunyun Wang: I think it's just really great to see people get really excited because and also trying to disprove maybe because the potential for this technology is so great if we get it right and if we can actually really leverage its full capability.

[00:32]
Yunyun Wang: So I feel like the carefulness about how do we actually make this work for real problems is like very much warranted.
Yunyun Wang: But yeah, I think when we publish, and I think that just also shows a need for more rigorous
Yunyun Wang: evaluations that represent these life science workflows and research problems so people can
Yunyun Wang: look at and eval and say, yes, I feel like now I have 100 different ideas for how I can
Yunyun Wang: implement this into my lab and solve some of the current bottlenecks I'm facing.
Joy Jiao: I actually think there's a certain amount of stress I've encountered from people who
Joy Jiao: are worried that, you know, AI is really powerful, but they don't know how to use it the right way.
Joy Jiao: And so there is this general feeling of like, I need more AI in my workflow, in my life, but they
Joy Jiao: don't know where AI should come in. And I think part of the product vision is to just make it so
Joy Jiao: simple that it just works. So you can just go to something like Codex and say, hey, I want to do

[00:33]
Joy Jiao: whatever I'm doing today. And then Codex can figure out all the different pieces,
Joy Jiao: the multi-agent workflows, the tool calling, all of that. And so, yeah, basically you don't have to
Joy Jiao: stress about how to get uplift from AI, and it just happens naturally.
Andrew Mayne: We do see those step changes every time these models become smarter and understand users
Andrew Mayne: better.
Andrew Mayne: You get more utility because some people go, I don't have to spend a lot of time trying
Andrew Mayne: to prompt it or figure out all the tricks to it.
Andrew Mayne: If you were talking to somebody who was considering getting into the life sciences, maybe a high
Andrew Mayne: school student right now, what advice would you give them?
Joy Jiao: I feel like when I was in high school, so I did the USA Biology Olympiad back when I was a high school student.
Joy Jiao: And I think out of all the different Olympias, I think biology was seen as kind of the most like memorization heavy one versus like math, right?
Joy Jiao: Where it's kind of more, I don't know, test time compute scaling, whereas biology is more kind of memory and retrieval.

[00:34]
Joy Jiao: I think my hope is that with AI having kind of like learned all the relationships between all the different research pieces is that it can really uplift human creativity and just make the process less memorization and more kind of helping people connect different fields of research together.
Joy Jiao: And just kind of, I guess, furthering the frontiers of what people are able to explore in biology.
Joy Jiao: So, yeah, I feel like my advice to, I guess, a high school student would be that maybe you don't have to kind of go and memorize all the biology books.
Joy Jiao: You should just do more exploration with AI.
Joy Jiao: I think you can definitely read papers and just ask questions.
Joy Jiao: And I think you can do both deeper dives and broader overviews this way.
Joy Jiao: And I think just the way of learning really changes.
Yunyun Wang: I found that when I was in the lab, there was like a real like solo, like individual aspect of doing biology research compared to like, for example, when I went to my first like CS hackathon, there was some excitement about just like the collaborative nature when we first like built our app together.

[00:35]
Yunyun Wang: So I feel like that's really the future I hope to see for early adopters and students using our models and maybe using it in the Codex runtime because there is a collaborative nature to it, too.
Yunyun Wang: I think, for example, sending your scripts or sending your conversations or maybe one day we all have our own co-scientists or agent and we can deploy our agent to now work with a teammate in that way.
Yunyun Wang: I think there's just like new like interactions and new modalities for us.
Yunyun Wang: So I would just encourage students to adopt early and just to like also pioneer their own path for how they would like to use it.
Yunyun Wang: For me personally, I always actually kind of felt like I got into wet lab a little bit too early.
Yunyun Wang: And like we mentioned earlier, I did not enjoy pipetting.

[00:36]
Andrew Mayne: That's the theme here.
Andrew Mayne: Nobody likes pipetting.
Yunyun Wang: Yeah, there's a lot of like very intense manual tasks involved.
Yunyun Wang: And so I hope that like, you know, when our AI models can connect with physical devices that, yeah, we can just like make a lot of like the learning curve more fun for students so that they can kind of like learn with the models and then kind of like maximize their time with like the really interesting interactions spaces.
Andrew Mayne: So I've been working with a student. I like to help students come with projects. And one of them is we've taken Codex and he's connected to a greenhouse and basically using it to get photos back and to look at it and to evaluate it. And I think it's been fun to see how he's been taking both AI technology and then something traditional like a greenhouse and combining them two and basically building up the skill set of learning how to use the two of them.
Andrew Mayne: When you talk to your peers, you talk to people who are running labs or running experiments, researchers, what advice do you have for them? Because the problem I see is that a lot of them go, that's great. I just don't have the time. But ultimately, what we're trying to do is save them time. So do you have any kind of quick advice that you give them or any ways you try to maybe inspire them?

[00:37]
Joy Jiao: Most people that I know, I think in academia use AI in, I think, two main ways that I've seen.
Joy Jiao: One is to kind of talk to AI about an existing piece of research paper or something and just kind of make sure that you're understanding things the right way or kind of fact checking.
Joy Jiao: And this is personally what I really like to use AI for because you can ask really dumb questions and you don't feel any judgment.
Joy Jiao: actually just really wonderful for learning. And I think people use a lot for analyzing
Joy Jiao: experimental results. And I think this comes back to the statistics piece that I learned,
Joy Jiao: what I mentioned before, where sometimes you don't know what the right way to analyze your data is,

[00:38]
Joy Jiao: or there's just kind of so many different interdisciplinary fields that your data might
Joy Jiao: touch on something in chemistry or something in like a random niche field of like protein biology.
Joy Jiao: And the really nice thing is that a model can kind of like pull those different ways of data analysis in for you and kind of explore all of these different paths.
Joy Jiao: I feel like both of those are pretty low lift ways to try things out.
Joy Jiao: So you could just kind of like throw a PDF file at AI and just be like, hey, help me understand this paper and just have a natural conversation.
Joy Jiao: Or you can boot up Codex and do some data analysis directly on your laptop.
Yunyun Wang: Yeah, I would say that you'd have to start with making sure it doesn't feel like work right away.
Yunyun Wang: So maybe it'll be easier when you're focusing on AI adoption to just like work on like a hobby project or a passion project.
Yunyun Wang: For me, for example, I actually started working on like more like literature synthesis tasks when I was doing creative writing projects,

[00:39]
Yunyun Wang: which are kind of like just something that was not at all related to like our day to day,
Yunyun Wang: even though biology is a very creative space.
Yunyun Wang: I was just exploring that through a different, different medium.
Yunyun Wang: And I think that's actually when I started unlocking like a lot of different ways to either prompt the model or to actually access different data sources.
Yunyun Wang: So I think that just gave me a lot of like pattern matching abilities for when I was trying to apply it,
Yunyun Wang: because we're not going to get it right in the first try.
Yunyun Wang: And it is really hard.
Yunyun Wang: And I feel like the progress and pace of this field moves so fast that every week or month,
Yunyun Wang: there is a new pretty exciting development that might change how we engage with models
Yunyun Wang: or AI systems.
Yunyun Wang: So I think it's just important to get started somewhere.
Yunyun Wang: And I think another theme is the collaboration element.
Yunyun Wang: I feel like it's more powerful when you have a recommendation from either somebody on your
Yunyun Wang: direct team who is doing the same day-to-day tasks as you.
Yunyun Wang: That happens a lot on our team as well, where somebody will say, oh, I got Codex to like now touch these three different like internal like databases that we weren't able to connect before.

[00:40]
Yunyun Wang: And I don't even like the latent space, the latent capabilities are just so vast that there's a lot that we just don't know until again, we can do it.
Yunyun Wang: So I think just having conversations with your friends, your lab mates, your teammates will, I think, spark a lot of those conversations, a lot of those creative juices and then help you help you with your own adoption.
Andrew Mayne: What does science look like 10 years from now?
Yunyun Wang: I think when we started this team, we do have like really just ambitious targets.
Yunyun Wang: And one of those is like, I think we do want to make meaningful strides towards or even
Yunyun Wang: if like assist with like curing a disease.
Yunyun Wang: And I think there's just so many rare like orphan diseases that doesn't really have the
Yunyun Wang: attention and the resources that it warrants because it's just such a difficult field to
Yunyun Wang: actually, for example, clinical research is so difficult to actually bring that to patients

[00:41]
Yunyun Wang: and to market.
Yunyun Wang: So while 10 years, I feel like it's just a really long timeline, I'm really excited about
Yunyun Wang: some of the progress that we can make.
Yunyun Wang: And I think it's good to be carefully optimistic that we're going to see some of those
Yunyun Wang: breakthroughs pretty soon.
Joy Jiao: Yeah, I think maybe this is a bit of a sci-fi vision that I have of the world that I really hope becomes reality, which is that you have these autonomous labs.
Joy Jiao: They are just mostly robots and you have them all hooked up to AI and you just have autonomous research institutes that are constantly running and curing human disease.
Joy Jiao: It's maybe making new materials, making new drugs.
Joy Jiao: It's maybe solving personalized medicine.
Joy Jiao: There's a lot of NF1 or just ultra rare diseases where people without vast monetary and research scientific resources can even begin to think about solving.
Joy Jiao: But we can solve that with AI.
Joy Jiao: And I think we can kind of almost break through the financial and regulatory and monetary constraints with the system.

[00:42]
Joy Jiao: So I think that that's kind of the dream.
Joy Jiao: And I think also even separately thinking kind of more about the biosecurity side of things.
Joy Jiao: these systems can be kind of constantly sampling our environment, right? It can be sampling
Joy Jiao: wastewater. It can be sampling the air and constantly detecting potential threats or even
Joy Jiao: just better predictions for the flu and getting better flu vaccines. But just generally, these
Joy Jiao: different medical countermeasures, I think should be happening autonomously in 10 years. And I think that that's basically something, yeah, I'm really excited about.
Andrew Mayne: The AI lab is exciting because I
Andrew Mayne: think if people really understand what it means is it's not, there aren't scientists, it's there
Andrew Mayne: are more scientists, but they sit at home and they go into Codex and say, can you go run this
Andrew Mayne: experiment for me? And like, you have a data center, you have a science center doing that.
Joy Jiao: Right, exactly. Yeah. And I think I didn't talk about the scientists in the vision I was just
Joy Jiao: describing, but obviously there are people involved in here. And I think it's really kind of

[00:43]
Joy Jiao: high level direction setting from the humans. We're saying, here's a patient with this disease.
Joy Jiao: here are some potential solutions or things that maybe you can look at.
Joy Jiao: And I think that AI can then go off and explore different ideas.
Joy Jiao: It can design experiments and then come back to the humans and say,
Joy Jiao: here's what I found.
Joy Jiao: What do you think we should do next?
Joy Jiao: And this can be kind of an academic discussion.
Joy Jiao: It's a little bit similar to kind of the way that people interact with codex today,
Joy Jiao: where you say, here, go write a function or go write a piece of code.
Joy Jiao: And it writes it and says, here's the code.
Joy Jiao: And then the person tells the next thing to do.
Joy Jiao: So I think it's a little bit similar to that kind of interaction, but on a much grander scale and on a much longer time horizon.
Yunyun Wang: I think it's really like the democratizing science aspect and putting like really capable expert level knowledge in the hands of a greater amount of people.
Yunyun Wang: And I think what that can mean for personalized medicine, for bolstering our societal defenses.

[00:44]
Yunyun Wang: There's just like so many naturally occurring new like variants every year, new like influenza strains.
Yunyun Wang: So I think it's really just like securing defenses and feeling like we actually have more agency to counter all that.
Yunyun Wang: And I think I'm really excited about a lot of like the medical countermeasure acceleration work as well.
Andrew Mayne: Well, it's very exciting. Thank you for sharing this with us.
Yunyun Wang: Thank you for having us.
Joy Jiao: Yeah, thank you so much.

</details>

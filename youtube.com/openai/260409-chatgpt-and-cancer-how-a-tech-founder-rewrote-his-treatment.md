---
title: "ChatGPT and Cancer: How a Tech Founder Rewrote His Treatment Plan"
channel: openai
url: https://www.youtube.com/watch?v=OAlHiQLsYQM
youtube_id: OAlHiQLsYQM
published: 2026-04-09
duration: "48:26"
captions: en-orig
---

# ChatGPT and Cancer: How a Tech Founder Rewrote His Treatment Plan

[![ChatGPT and Cancer: How a Tech Founder Rewrote His Treatment Plan](https://img.youtube.com/vi/OAlHiQLsYQM/hqdefault.jpg)](https://www.youtube.com/watch?v=OAlHiQLsYQM)

<details>
<summary>자막: ChatGPT and Cancer: How a Tech Founder Rewrote His Treatment Plan (48:26)</summary>

[00:00]
Good afternoon everyone and welcome to
the Open AI Forum. I'm Chris Nicholson
and I'm really glad to have all of you
joining us today. Um for those who are
new, the Open AI Forum is a global
community where we bring together people
across industries to share how AI is
being used in the real world, what we're
learning and how we can shape its impact
together. Um today's conversation is a
powerful example of that impact. Uh
we're joined by Sid Sijbrandij,
co-founder and executive chair of
GitLab, and Jacob Stern, a geneticist
working closely with Sid.
Together they're going to share a deeply
personal and deeply technical story
about using AI in the context of a
serious illness.
I've known Sid for more than a decade
now.
Uh and I'm very grateful that all of you
are here today. Uh so with that, I'll

[00:01]
hand it over to Scott McKinney,
researcher at Open AI, to more fully
introduce Sid and Jacob. Thanks, Chris.
I'm Scott McKinney. I'm a researcher at
Open AI and I'm thrilled to have Sid and
Jacob here today.
As Chris mentioned, Sid has been
battling osteosarcoma. It's a rare and
tenacious form of bone cancer. It
affects fewer than a thousand Americans
a year. If it recurs after the first
line of treatment, survival rates are
typically measured in months.
I myself have been fighting the same
fight since 2020 and I've seen firsthand
how sparse, blunt, and frankly gruesome
the treatment options are. And I've seen
how quickly they can be exhausted.
After Sid's cancer came back, faced with
the unfaceable, he and Jacob went into
founder mode, tackling the problem with
intensity and audacity.
When the traditional healthcare system
brought them to the end of the road,
they decided to pave their own.
As you'll hear in their talk, they're
chaining together bleeding-edge tools in
conjunction with AI to push the
boundaries of personalized medicine.
And what I love about this story is that
it's not just about resourcefulness in
response to his own medical crisis, but

[00:02]
rather as entrepreneurs, they're
interested in blazing a trail for others
to follow.
I was first connected to Jacob and Sid
last year in the context of my own
diagnosis and they've been enormously
generous in sharing their playbook and
it's totally changed how I've navigated
the situation. Thank you.
I like to think that their approach
offers a glimpse into the future of
medicine that can one day be accessible
to all. It's given me hope for my own
family and for every family afflicted
with cancer.
I've been inspired to watch Sid leverage
his energy, ambition, and resources to
chase his own cure. In my own small way,
I feel like I get to do that here at
Open AI.
AGI may be the tide that lifts all
boats, but many of us are particularly
excited about how it can transform
medicine. And we're working hard to make
that vision a reality.
The team has created public benchmarks
for evaluating models in the healthcare
domain, deployed clinical co-pilots in
primary care settings, and we're working
to democratize access to medical
expertise in ChatGPT health.
In this regard, I think the future is

[00:03]
very bright.
So with that, I'm honored to give you
Sid and Jacob.
Well, well, thank you so much for that
wonderful introduction, Scott and and
Chris. Uh really excited to be here
today and to walk you through my cancer
journey and emphasize along the way how
AI has helped us work through enormous
amounts of data and navigate new
treatments.
I came to the US more than a decade ago
in 20
uh 15 with a startup called GitLab. Six
years later we took that public.
But the next year after going public, a
lot happened.
You all at Open AI released ChatGPT.
Um there was a
Nobel Prize awarded to a very
interesting technology.
But also on the downside, I got some
weird feeling when I was doing a bench
press. I was doing a bench press and I
felt a pain around my heart area and I
thought, oh, I know this is not going to
be a heart attack because I've had this

[00:04]
before.
But unlike the few other times, it
didn't go away and after 2 weeks I
couldn't sleep in the night. At 4:00
a.m. I went to um uh I went to the the
the hospital, to the emergency room and
they they said, "Well, there's no such
thing as a 2-week heart attack, so so
that's good."
And they took an X-ray and sent me home.
There was nothing going on according to
them.
But um
uh a few hours later I got a phone call
and it was my GP and he said, "Do you
know how to meditate?"
I thought that was a very vague area
question of him and I said, "Yes, I
actually I do know how to meditate."
He's like, "Well, you better start
meditating right now because you have
super high blood pressure and you might
have an aneurysm.
And the pain you're feeling might be
your aorta starting to burst. So, chill
out and also get to the emergency room
right now. I'll call ahead. Um
so I did that and they had good news. My
aorta was fine, but they also had bad

[00:05]
news. There was a 6 cm
what turned out to be a tumor growing
from my vertebrae.
And so I had to
do surgery really, really urgently to
remove that. They put in a frame, uh
they uh did a spine fusion.
We did radiation. We did very extensive
chemo. And as Scott mentioned earlier,
it's kind of medieval how rough that is.
It was hard for me to even get to the
restroom. I needed four blood
transfusions to keep my uh to to even
keep alive.
As I hinted earlier,
2022, something else happened. It there
was a Nobel Prize for click chemistry.
You might not have heard of it, but it's
a way to combine two compounds in a
human without any side effects. It
doesn't do anything else. It always
happens. It's a very specific reaction.
It's genius. That's why it won a Nobel

[00:06]
Prize.
And I was lucky enough during YC to meet
uh someone.
Jose is his name and he was starting a
company around it. He was first in
patients with click chemistry. And over
time, he struggled to fundraise. Now
he's okay, but at that time, before the
Nobel Prize, it wasn't trendy. Biotech
VCs didn't believe in it and over time I
became his biggest investor. It became
my biggest investment. And we ended up
becoming best friends.
And now that I was in trouble, he said,
"You know what? Let's try this treatment
for you."
And that opened up my eyes that it was
possible to get a treatment just for a
single patient. I always thought it had
to be a big trial. But if you're in a
really bad spot, the uh there's a an
option called a single patient IND.
The FDA approves 99.7%.
Uh they even say now that they're
approving 100% and it's a great pathway
if you're uh

[00:07]
with a disease and and there are very
few options.
Despite all of our efforts, 2 years
later, we had a remission. It started
growing again. It had a local
progression. And there were no more
standard of care medicines. My
oncologist couldn't recommend something
that he thought was going to make a
difference. He said, "Hey, go look for
trials." But it's a rare disease. There
were no trials.
So this became
life or death for me and I quit my day
job and started going founder mode on my
cancer.
And I went all out. I did all the
diagnostics I could could my get my
hands on.
Typically people say, "Only do the
diagnostics if you know like what you're
going to do with it." We didn't do that
at all. We did every single technology
we could find and and uh we collected a
lot of data.
We started making treatments. If there's
no treatment left, you need to make
them.
And we started doing as much as possible

[00:08]
in parallel. We were out of time and
most people die because
the disease progresses.
And we're trying to scale it for other
people.
In the maximal diagnostics, we've done
everything under the sun and if you want
to see some of that, there's 25
terabytes of data available on
osteosarc.com.
One of the things we did was single-cell
sequencing. It's a really cool
technology where you individually sample
thousands of cells. It allowed us to
isolate my cancer cells and look at the
properties of the cancer cells. And we
found out they had a lot of FAP. It's
kind of a fibrous tissue.
And that was great because we found in
Germany
a doctor that had an experimental
treatment where you combine FAP
with radioactive substances. So I went
there, did it twice. I was in iso- the
isolation ward afterwards because you
were kind of you had to glow up. Um
and it was really, really successful.

[00:09]
The two treatments led to 60% necrosis
and 20% shrinkage. And the cancer
detached from my dura and we were able
to go in and scoop it out of my body.
And when we looked at the sequencing
we've done along the way, the TCR
sequencing in particular, we saw that
we've been able to all the immuno three
treatments
get a lot of angry T cells in me. So I
did everything under the sun. I did dual
checkpoint inhibitors, NK cells, a super
antagonist, an oncolytic virus. So we
had my immune system riled up. But the
tumor microenvironment was so was
suppressive. It didn't allow the immune
system to go in. And we suspect what
happened is that because we disabled the
FAP cells, they stopped signaling to the
neutrophils and we turned the cold tumor
hot. Suddenly the immune cells were able
to go in. We don't know this for
certain, but that's what we think
happened.
We also looked at MDM2 as a

[00:10]
therapy for me.
I am really, really high on the MDM2
expression. It's just some protein, but
I'm I'm off the scale. I'm the index
tumor over here. So, I'm on the 0.3%
and we started looking like, are there
any drugs? And there were drugs. People
made them. But then they stopped all the
development because drugs only get to
market if it's a blockbuster.
If
the majority of patients are served with
it. That wasn't the case for MDM2.
And so they stopped it and they were
about to turn off the freezers. So,
we're now paying to keep the freezers on
and I'm looking for a pathway to bring
this medicine to market because it might
help other people beside me. Not the
majority of patients, but if there's 10
or 20% that'd be really awesome outcome
as well.
One of the best things that happened
with Maximal Diagnostics is that the
single cell sequencing and got me in
touch with Jacob, who's now running the
enterprise of my care. Jacob. Go.

[00:11]
Thanks, Sid. Um and thanks so much for
having us. Um you know, I'm not a
doctor. Uh I met Sid through Jose, the
mutual friend, who uh was working on the
click chemistry-based drugs.
And at the time I was working at 10x
Genomics, a company that makes the
equipment that enables a single cell
sequencing. I was there for 6 years.
And when I met Sid, I started talking
about what we're doing at my 10x. We do
single cell.
Sid explained how he and his team were
using single cell to actually inform his
care.
And at 10x, the mission statement is to
master biology to advance human health.
And this was the first time I'd actually
met someone in person who was doing
this. He was mastering biology to
advance his own human health.
Uh and I found this to be super
compelling and as we got to know each
other and I got to know the story, uh I
got to understand the extent to which he
was living in the future and how to
envision to do even more.
And so, what you can see here is the
vast array of of technologies we're
using to analyze Sid's cancer. We're
doing stuff that I'm more familiar with

[00:12]
like single cell sequencing uh or some
of the bulk DNA or RNA sequencing, but
we're also stretching way outside of my
comfort zone. We're doing targeted radio
diagnostics, extensive pathology
staining, using organoid models to test
the effect of drugs directly on Sid's
cancer.
And so, for me,
I've become an extensive user of AI to
basically bring myself up to par
and uh enable me to talk with experts
about these different domains and have
intelligent conversations about how we
can drive this forward for Sid and
actually make use of this data. So, I'm
actually going to take you through a
little bit of my historical chat GPT
history so you can see a few examples of
how I actually did this in practice.
Um so, this is a a screen a screenshot
from last summer where we wanted to just
run an experiment. Let's take the output
of one of these bulk RNA sequencing
experiments where we're basically
counting the number of times that each
gene is being is being detected at the
RNA level in the sample from Sid's
tumor. Uh and this is expressed in a CSV

[00:13]
file. All right, it's genes and then
counts.
And we fed this to at this point it was
uh 400 on the pro plan and said, "What
do you think of it?" And I wanted to see
what came out. And frankly, even then it
was remarkable. Uh you'll see here if
you zoom in, uh it it flagged B7H3,
which you'll recognize later in the
presentation. And then it also
recognized some of the immune dynamics
uh that Sid talked about earlier, which
we've studied in much more detail since
uh at the single cell level.
And now what we're doing is much more
advanced. I mean, these models are
progressing at an absolutely insane
rate. Uh and we've built some harnessing
for ourselves where we can ask a we can
ask a question in natural language and
spin up a series of agents that can go
uh do literature search, formulate its
own hypothesis, basically structure uh
structure a bioinformatic analysis and
then execute that and bring back a
summary.
So, what I have here is a recent example
where I'm asking this system that we

[00:14]
built about chip clonal hematopoiesis of
indeterminate potential. This is
something that many people get as they
age. Uh it's basically the blood the
blood cells losing polyclonality as we
age uh and it can, if things go wrong,
lead to leukemia. And as we got sort of
a hint that this might be happening in
Sid from our uh from our team, it
spooked us because this can be a side
effect of the chemotherapy that Sid took
a number of years ago.
And so, one of the first things I did is
I went to the system and just asked. You
can see the the question that I posed
here. It's pretty natural in API costs.
It thought for 30 minutes.
Uh did a series of tool calls. It did
its own literature review, formulated
the set of markers it wanted to look
for. This is hooked up to about 600
600,000 single cells from uh a number of
time points that we've taken from Sid's
blood. So, it can actually run the
analysis directly in Sid's blood and
come back to me with a report of here's
what I think, here's my conclusions,

[00:15]
here's the interactive plots, and then
here's my whole history, here's the code
it wrote in Python, etc.
And I'm not going to trust this out of
the box. Um it can certainly make
mistakes, but what it does give me is
it's a rapid way uh for me to get up to
speed and start to understand
the sort of circumstances around this
disease. Again, I'm not a doctor. I
didn't train in chip. But here, I can
rapidly come up to speed on the disease
more generally and also on Sid's biology
specifically. And it's led us it's led
me be a good counterpart to the
informaticians who have since looked
into this in much more depth and
thankfully we put this risk to bed.
Um
so, on top of doing the maximum
diagnostics, we're also uh making a
number of treatments from scratch
specifically for Sid. And uh you know,
this is even further outside of my
comfort zone than the analysis is and
it's frankly been radicalizing for me to
find that you can just make your own
drug. And so, before Sid goes through
and talks about some specific vignettes
here, I just want to sort of give an

[00:16]
overview of some of the modalities uh
just to just to level set. So, the first
one he'll talk about is the cancer
vaccine. Uh in this case, an mRNA
vaccine specifically.
So, you can think about this similar to
the vaccine that you've taken for COVID
or for the flu, whatever it is, where
the idea here is to educate the immune
system to prepare itself to fight
something that's foreign.
Uh in the case of the COVID vaccine,
you're exposing the body to the spike
protein of of of COVID itself. In this
case, we've encoded a number of
mutations that are present in Sid's
cancer, which basically differentiate
the foreign cancer from Sid's normal
tissue into the vaccine. And when we put
that in, we're priming his immune cells
uh to be ready to patrol and try and
fight the cancer if it sees it.
Uh the next vignette will be around a
TCR T cell therapy. Uh TCR stands for T
cell receptor. And T cells are one of
the business ends of the immune system.
Uh T cells are very killy. They uh they

[00:17]
use a T cell receptor to detect
something very specific and then uh
basically they
shoot out proteins that rip holes in
cells that are close to them.
And so, what we can do here is something
that's a little bit more direct than
what we're doing in vaccines,
where through some of the work we've
done with single cell sequencing and uh
some very capable partners have done
very thorough work, as you'll see, uh
we've identified TCRs T cell receptors
that are likely very specific for Sid's
cancer. And we can engineer those
directly into healthy T cells, grow a
bunch of those up, and then inject them
directly into Sid. Hopefully, we never
have to do that, but we're preparing in
case we need to.
Uh the last one I'll talk about briefly
is the CAR T cell therapy. In this case,
CAR stands for chimeric antigen uh
receptor.
This is an extension of that same
concept of the TCRT,
where we're taking a T cell, the killer
immune cell, as a chassis
and souping it up and then engineering
in the receptor, basically what it's

[00:18]
going to use to recognize. And we picked
a target that through the maximum
diagnostics, we saw as present on, you
know, most if not all of Sid's cancer
cells.
And through this, this is this is the
really killy one, where if we really
needed a nuke to deploy, we're putting
this on the shelf as an insurance
policy, a sort of super killy CAR T
that's specific and very potent.
Yeah, so we did the personalized mRNA
vaccine. It's super exciting. I was the
first patient of an
investigator-initiated trial.
And while doing that, it was awesome to
learn what goes into making it. There's
all these antigens that you you can
encode in it. You have
bits and bytes basically to encode base
pairs to encode in the virus. You have a
limited set. So, what you select
matters. And we used tons of different
ways to determine that. Like, what was
in my tumor samples? What is scoring
high in different models?
And right now, this is more of an art

[00:19]
than a science, but we've already seen
companies that are starting to use AI to
do this automatically. And that is very,
very exciting because that means you can
do it for millions of patients. I can
see a future where
you get a personalized vaccine against
your cancer. And that will have to come
from AI because we don't have enough
doctors to do this. Also, typically
these engineering AI approaches yield
better results in our opinion. So, very,
very exciting what AI can do here.
We were very fortunate that we got this
from project start to injection in only
6 months. And
we see those times coming down even
further in the future.
Jacob mentioned the TCRT.
It's a very interesting
thing to make as It's very complex to
make,
but a lot of decision-making goes into
it. A lot of data goes into it. And what
we've seen is that the diagnostics,

[00:20]
if you have good kind of tumor samples
and you do a lot of sampling, it really
helps inform how you design it. Here
again, there were lots of decision
variables like do we do that? Yes, no,
why? A lot of reasoning, a lot of logic.
And to do this at scale, you'll need AI
as well.
The last example I'll give is, I think,
a really powerful one of how the
diagnostics are influencing the medicine
development.
We selected B7H3
as a target for my CAR-T. The CAR-T,
remember that's that super killing
nuclear bomb that you're going to set
off.
But we wanted to know where is that
present? And you have genetic data about
me, but there's nothing as good as doing
an actual scan. And we were able to
access one. It was in China, in Beijing.
So I traveled there in October. And we
did the scan. And the doctors came back
and he said, "We have really good news

[00:21]
and really bad news."
Well, what's the good news? The good
news is they didn't see any cancer. So
yay, still clean.
The bad news is that my liver was
showing up three and a half times as
much as the 20 Chinese people they
scanned before me.
So now we were very worried. If I ever
were to take this medicine, I might lose
my liver.
So we went back to Cole Robo who's
making it. He said, "Can you do
something about it?" He says, "Well,
actually, I was the first one to invent
a larger gate for CAR-Ts, an end gate.
Two things have to be present." So we
went back and looked at like what's
really not present in the liver. It's
FAP. You know that from the first one,
the radio ligand therapy. That has very
low liver expression.
And by needing those both things to be
present, the B7H3
and the FAP, we're going to make sure

[00:22]
that if I need use the nuclear bomb, it
doesn't go off in my liver.
And it was amazing to see that feedback
loop, how a better scan informed that.
Last anecdote is something we saw. It's
called PENX3.
And it it it it
on the genetic data, it like sprung at
us. It was represented
10 times 10,000 times as much in my
cancer as in my healthy tissue.
That's that's an incredible difference.
And we were eager like, "Okay, let's see
what medicines are available." But when
we scoured the literature, there was
nothing. There there were a few a few
mentions of it. No one's really done the
research. And most protein targets,
people will have published on it. They
they they just go look for what's
expressed on the outside of a cell. So
this was really strange. Why wasn't
there anything?
And we think we figured it out. It's a
hydrophobic thing. So if you do your
tests in water, like most people do,
you're not going to find this thing. The

[00:23]
only reason we found it is because we
went back to the data and did a
painstaking analysis. And this is again
something that AI is incredible for. It
has much more patience than a human. It
will go through all those
terabytes of data and find the proteins
that matter. A human would not have the
patience for this. And we were
lucky that we we were able to find this.
And now we're running a binder campaign
trying to see if we can engineer
something against this.
So that's some of the anecdotes of how
we made the personalized drugs and
diagnostics. Back to you, Jacob. Yeah.
So
uh once again, we'll dive back into my
ChatGPT history. Um
I would say this is an area again where
I'm even more out of my depth than I am
with some of the more adventurous uh
analysis modalities. And so what I'm
doing absolutely would not have been
possible 2 years ago. Because if I were
trying to uh navigate to the expert
who's at some biotech company, you know,

[00:24]
it advancing, you know, some program
that's going to be used for millions of
people, just the knowledge is very
sparse. But what AI has made possible,
particularly I think I'm the super user
of deep research, is the democratization
of that specialized knowledge. And it
doesn't make me a specialist, but it
makes me someone who is competent enough
to talk to specialists and push some of
these programs forward while owning the
objective of let's keep Sid alive.
And so here you can see some of the
stuff we were looking at as we were
thinking about the mRNA vaccine. Uh last
summer as we were considering how are we
going to do this, we were looking at
options ranging from working with one of
these, you know, big professional
contract development manufacturing
operations that makes drugs
professionally, probably makes the COVID
vaccine actually, uh down to could we
actually just have some academic group
make it in their lab as if they were
putting it in a mouse and would we put
that in Sid? And so for that, we
actually thought from first principles

[00:25]
around what are the quality control
metrics we would want to see from
something in order to feel comfortable
that what we're putting in Sid is going
to work, it's going to be what we
expect, it's going to be clean, it's not
going to give him sepsis, etc. And of
course all that work was done with AI.
Um
and that meant that when we were
introduced to the academic team that
ended up making the mRNA vaccine, which
has been an amazing collaboration, uh it
did two things. One, we were prepared to
ask reasonable questions and understand
what they were saying and what they were
planning to do. And perhaps even more
importantly, it made us good partners to
them. Uh because we were sophisticated
enough to understand what they were
doing. And that built a relationship of
trust. And we had to fight through a lot
of things to actually get this done. And
we did that together. And that was built
on sort of this mutual understanding and
mutual ability to talk about the
nitty-gritty details here.
Uh
here this is on PENXIN3. As Sid
explained, this is a really understudied
target. When we're thinking from first
principles about Sid, if you go back to

[00:26]
that plot, uh we don't have to go back
there, but on that plot, the PENXIN3 was
way off the diagonal. It was clearly the
best target for Sid.
Um but it's not the best target for
almost anybody else. And so it's a
target that's understudied. And so as
we're trying to do a binder discovery
campaign against PENXIN3, uh we're sort
of MacGyvering through it. We're
inventing new reagents. We're thinking
through new assays. Uh we're trying to
triage different data sites to see if we
have a good binder or not. Is it a false
positive or a false negative? And as
we're thinking through that, like AI
does feel like an Iron Man suit to allow
us to assess all these different
specialty things and think about think
about these really arcane nuanced uh
points in this like arcane process. And
it makes it accessible to somebody like
me.
If we think about kind of
the treatments in parallel, what where
did that come from?

[00:27]
I think something you have to be aware
of as a patient is that the incentives
for the doctors are very, very different
from the incentives for you as a
patient.
The doctors want to minimize their
liability. And their liability is when
they prescribe a treatment and
there is severe side effects and
including death from those effects.
As a patient, you want to maximize
survivability.
In my case, because it's a nasty cancer
with like medieval medicine, I'd rather
die from a treatment than from the
cancer. Dying from cancer is a really
miserable way to go.
That is not what you will get with
doctors. They have very different
incentives than you.
And most patients, they get too few
medicines and they die because the
medicines that they got didn't work.
They didn't have time to try the other
things. They get metastatic cancer and

[00:28]
they pass away.
AI is amazing at helping you suggest
things to discuss with your oncologist
to combine things.
And the standard, I think, pushback you
get from an oncologist is this has never
been tested in a randomized control
trial.
That is true. But a randomized control
trial is a hundred million dollars. We
can't test every combination of
medicines that way. It also it's not
needed. From first principles, you can
just see do the side effects do the
medicines have the same side effect
profile? Do they add up? You almost
would you kind of need to look at this
organ by organ. If one drug is hitting
your kidneys, you want the other drug to
hit your liver. You don't want to take
two kidney drugs at the same time. So AI
is incredibly useful to help you
through that, to have that dialogue with
your doctor, but to come well informed

[00:29]
and to push them to get closer to
maximum survivability because that will
not be their default mode.
If you want to see what treatments I've
combined, um you can see see so on
osteosarc.com/timeline
where we have all my different
treatments and all the modalities listed
out.
Some of the things I'm doing are
incredibly expensive.
Some of the things I'm doing are not
incredibly expensive. You can get bulk
RNA sequencing these days for 50 bucks.
Whole genome sequencing started $500.
AI is amazing. For $20, you get super
capable tools.
Treatments in parallel will consume more
drugs. but if those drugs are generics,
the the pricing is super affordable.
So, there's there are things that should
be accessible to people if they can
convince their doctor to prescribe them.

[00:30]
And then aside from that, for some of
the more adventurous things that we're
doing,
part of the way we're trying to scale
this for others is we've started a
series of companies to try and put this
on rails. Cuz for Sid and a few other
families who are sort of pursuing this
at the absolute maximum, it's been the
coming up the learning curve and
starting from scratch and developing
relationships and developing
competencies, etc. But what we want to
do is sort of pave the road behind us so
that it's easier for the next person,
the next person, the next person. If Sid
and a few others like him are Roadster
Model 001, how do we do the Roadster
that somebody can buy off the shelf and
work our way from the Model S to the
Model 3? Uh and of course AI is deeply
embedded in all of these things because
it's a deflationary technology. It's how
we get things It's how we bend the cost
curve and how we get things to scale.
And so, I'll give a couple of examples
through the portfolio. Uh one of the
companies is Valis.
Uh they're doing the maximum diagnostics

[00:31]
from a uh gene expression perspective,
running things like single cell
sequencing and running through all the
raw bulk RNA sequencing data to find the
right target for somebody's cancer
regardless of the tissue of origin.
And so, here you can see sort of the
plot looking at a specific patient and
the expression levels, etc. But once the
uh once the target's identified, in this
case DLL3, using AI to pull in all sorts
of context about this target, active
clinical trials, biological data,
pharmaceutical companies to work with,
etc.
And then
for another one, Arden.
Uh Arden is taking a similar approach to
complex unresolved immune disorders by
doing maximum profiling of blood uh to
try and get into a treat, measure,
analyze, repeat cycle with combination
of targeted uh
targeted immunomodulators that are
tailored to whatever the person's blood
is actually saying.
And the the CEO of Arden, when he starts
working with somebody, often what comes

[00:32]
back is a gigantic Google Drive folder
or in one case a 9,000-page document
documenting somebody's medical history.
And so, he's actually used AI to build
an AI tool that helps him parcel this
information and get up to speed with the
patient and help them uh parse the
history to make a better plan going
forward.
So,
I've been very, very lucky that what we
did worked and there's no evidence of
disease since we did the radioactive
treatment and uh surgery. It's not for a
lack of trying.
Uh couple of weeks ago, I did a bunch of
experimental scans. They These scans
combine a protein binder, for example,
for B7H3, but also FAP2, FAP with a
scan. And I'm super excited that there's
more and more of these proteins kind of
becoming available so you can do a scan.
I can see a future where instead of just
trying a drug,
even a generic drug, if there's a
protein it binds to, you want to make

[00:33]
sure that is expressed in your cancer
and you want to be aware where else it's
expressed so you can view for those side
effects. That differs per person. If we
can do the scan first, that's great.
With some of these, you can do the scan
first and then you can do the scan in
the morning and you can do the treatment
in the afternoon where they bind
something radioactive to it. I think
this field is
poised to take off really, really
rapidly.
By searching and scouring the world, my
therapeutic ladder, the options
available to me have gone from zero
treatments to 30 treatments that I don't
want to use, I'd rather not use, but
it's great to have options.
I want to thank you so much for watching
us and we super look forward to your
questions. Thank you.
Hey guys.
That was amazing. Thank you so much.
Yeah. Um
one of my takeaways that that I'm not
you know, people maybe who haven't
suffered cancer or haven't gone through
cancer like you, they may be surprised

[00:34]
is how dynamic and proactive
uh you have been with cancer. You've
you've learned from it so quickly. And
it feels like that the speed of your
learning process is kind of the key to
getting this far. Is that how you feel?
Yeah, and we we learned a lot from other
people, other patients, uh concierge
medicine groups that are super, super
good, but also a lot of AI and a lot of
first principles. I think medicine has
lost its way in a little bit that
the
only work with randomized controlled
trials, but there's some first
principles thinking would would really
help in a lot of lot of cases. Yeah. Um
people people throw around the term a
cure for cancer a lot and lament that AI
has not given us the promised cure for
cancer. But like I I feel like what I'm
learning from you is that
curing cancer may happen one patient at
a time.
Right? So, you're really painting a
future of personalized medicine where

[00:35]
there's not a single cure.
Yeah, it's we're trying to bring that
I think some of the stuff we presented
today is going to be the standard of
care 30 years from now. We're trying to
bring it to the present. Some of these
to the present for older people
and all of this to the present for some
people.
Yeah. I I heard you making some
recommendations. I know there's a lot of
families out there who have had brushes
with cancer or who are going through
cancer now. And what I hear you saying
is there's affordable ways to gather
data and there are affordable tools help
you analyze and understand that data so
that you you may ask for better
treatments and eventually get to better
outcomes. Is that Is that the gist of
your message? Especially if you have a
rare cancer, it's super important to be
a good advocate. And even if you have a
known rare cancer, we've met many
survivors who said that being being
stepping up their advocacy has really
paid off for them. Yeah, amazing. Okay,
I'm going to open this up to um

[00:36]
questions from the community. So, we got
Jason DeLuca who asks, "Did you ever hit
a point where things felt absolutely
hopeless? And what was your breakthrough
moment with the tech?"
I think um
it wasn't a tech thing, but I felt very,
very hopeless for 15 minutes when I
um
I got uh radiology result.
And it was a classic. I was in a
meeting, but all of my reports um it was
um during an offsite and I got a message
from my GP. He says,
"Uh
it's positive, not subtle."
Oh, okay, great, positive. Uh
and then I'm like, "Oh, no, no, wait.
It's the the reverse in medicine. What's
going on?" So, I opened it. My lungs lit
up like a Christmas tree and um
with bone cancer, you're really afraid
of spreading to the lungs.
And it was a single diagnosis from
uh from the

[00:37]
uh from radiology that the cancer has
spread and uh there were so many it was
inoperable.
And so, that was I walked out of the
room uh
uh you process for 10 minutes, you call
your wife, you call your CFO and CLO and
then you go from there. And the next
day, the board came over. That was That
was fun.
Um and you're kind of like, well, this
been a ride. Thanks, everyone. All the
doctors signed off like,
"Oh, so sorry to hear about the news."
And then of the seven doctors we had in
the loop,
one guy, one guy like, "I don't like how
this spread by the lymph nodes. This
This is not how osteosarcoma spreads
through the lymph node."
And he's like, "Yeah, 60% this isn't
cancer."
And it turns out it was the remnants of
COVID.
Uh but that was certainly a low point.
Yeah. But yeah, you also learn 10

[00:38]
minutes plus 5 minutes. Yeah. Uh and
you're you're back and you're you're
going to you're you're you're
you're making the most of of what's
left. Yeah.
Um
that's a wild ride. That was wild. Yeah.
Um okay, I Here's another question. Um
let's see. I want to
And and like for an AI angle, it would
have been nice to have AI look at it
because it might have given a
differential diagnosis. This could be
cancer or this could be COVID. That
would have been super, super helpful in
that situation. Yeah, and a lot of folks
don't have seven doctors with with one
at the end. No, that that sixth opinion.
>> That one doctor that has seen seen
10,000 sarcoma cases, there's probably
only one Sans Chala in the in the world.
Yeah. Um
how
So, it sounds like this journey has been
um personally transformative for you.
So,
>> For sure.
What

[00:39]
what has changed in you and in have your
approach to life? Like how how is this
changed you as a person? Not your body,
but your spirit.
Um
I think it made you makes you realize
that kind of the the things you learn as
kind of I was I was a software
entrepreneur.
I didn't think those I didn't think
those skills would translate to cancer.
And
I thought in the beginning I'm I'm this
delusional tech guy
doing this
um and and no way that without a PhD I
can I can have a positive impact.
But we learned along the way there's
there's lots of ways in which the system
is misguided.
Um if you look on my website, you'll
find
over 10 things, I think, that to change
in the system to be more patient first.
And it's given me the confidence to like
try it on other things outside of
cancer.
Um and yeah, might not always work.

[00:40]
Maybe I I got lucky, but it's worth
trying. And as long as people try and
and and AI has helped us kind of find
the courage to kind of question the
status quo.
I I mean, it sounds to me that
you kind of have a movement in mind
here, you know, that a movement could
come out of this experience
where many people whose lives are at
stake
seek a greater change. So, uh
you know, in addition to reading
your site and I want you to repeat your
site so everybody knows where to go, but
in addition to reading your site, where
do people
what can people do? Not not just for
themselves, but also for for everyone.
I think
take agency.
Ask ask your chatbot.
Don't take it as as as as the truth, but
like help it inform your conversations
with your oncologist.
Uh we've talked to tons of patients.
Scott wasn't the only one. We'll
continue to do so.
Today is today I hired someone full-time
to to help us

[00:41]
to to enable us to help more more
patients.
So, shout out to Punima.
She's going to have a busy busy first
day, I think, because the cancer at site
c.com might get some emails today. Yeah.
We're we're we're looking forward to
that. And there's amazing people in the
industry like Roxandra who's trying to
drive clinical trial abundance. AI is
going to
enable us to dis- to kind of discover
and make so many more medicines, but we
still have to run these trials to prove
that they work and and she's done doing
amazing work to make those trials more
accessible and affordable enabling
enabling many more medicines to come to
market. Because we need both. We need We
need the AI, but we also need clinical
trial abundance. I think, Chris,
something that's pretty striking just in
doing this every day
is people in biotech and medicine almost
uniformly are in it for the right
reasons.
And it's like people want to help
people. For sure. And people under the
hood in the pharmaceutical industry,
they want to make medicines that like

[00:42]
advance human health. Um
same with anybody who's going into
medicine, right? These are hard roads
uh and there's easier ways to make
money, frankly. Um
but as we've gone out to
try to talk to people, to scour the
world for collaborations, whatever it
is, uh and sort of put the energy of
what we're trying to do out there, uh
the response has been really encouraging
because people want to help.
And um
people want to find a better way and
people just want to help patients.
And so, I think
the there is a positive sum energy out
there, at least from what we've uh
encountered.
And so, that gives me a lot of optimism.
Um
it feels I think a lot of folks outside
the business may not be aware how much
of a bottleneck clinical trials are.
The cost, finding candidates to do them.
It sounds
like you two are really thinking about
how to alleviate that bottleneck. What
What
What are some of the problems there?
Please talk to me about how you've

[00:43]
understood clinical trials and how you
think they might be improved. Yeah, for
sure. Uh Roxandra has done an amazing
job publishing on this.
For example, one of the things that it
makes clinical trials expensive
is that you have to get approval from
the
FDA before you can start it. And that
takes time. And time time kills
everything. It it it people run out of
money.
So, in Australia, they've just been
using a notification.
That is so much better.
And you can see in the safety data that
it's just as safe.
So, that's kind of a no-brainer to kind
of copy that from Australia. These these
the cost for these trials are getting
out of hand. It's more than a billion
dollars to successfully get a drug to
market. That is insane. That's limiting
the the drugs that get to market. There
should be 100 times more medicine if we
can get the cost down.
Another thing that we've really
struggled with was the IRBs at
hospitals. These are so-called ethical

[00:44]
review boards.
They are incredibly hard to work with
um because there's no incentive to kind
of
go in the IRB.
Um
and
what would be really great if there's
IRB freedom where you're not forced to
use the IRB of the hospital, but you can
go to independent parties as well who
are proven more affordable, more
efficient, and just as safe.
Now, how does how does it currently
work? You've got an IRB in a hospital,
and if you want patients associated with
that hospital to participate in a
clinical trial, you have to work through
the IRB? You have to use a hospital IRB.
And what happens is as a patient, this
ethical review board
I get wheeled in to pre-op at 7:00 a.m.
And they're discussing kind of
commas and and formulations that
are
really don't materially matter
until the point where I get rolled into

[00:45]
the operating theater at 3:00 p.m.
without an IRB sign-off still.
It's insane.
That's protecting me. Like waiting the
entire day to to to do some
dots and commas on a file that no one's
ever going to look at again, and it's
not material to any of it. It is it is
it's absolutely bonkers.
And the best way to solve it is to give
researchers freedom to to to pick. And
and it sounds like you're saying
sometimes the delay in care actually has
much graver consequences for patients.
>> If you
me, with all my resources and all my
agency, if I'm running into that, think
about how many people never get treated
at all. It's it's and how much
energy and and enthusiasm gets sucked
out of the investigators running these
trials.
And how about the matching problem? Like
how are people developing
uh potential treatments supposed to find
the folks that whose whose electronic
health
records qualify them for the trial? It

[00:46]
seems like uh an unsolved problem.
Yeah, for sure. So, like navigating
clinical trials, there there's there's
good websites, but AI could really help.
Especially if
if you have more diagnostic data and
using that to find a trial that really
fits you.
Yeah. Um
This has been deeply inspiring. Um let's
see, we've got Okay, I think we're we're
at the end of these questions. Um
so, we're we're going to move we're
going to move to to wrap this up. Um
I want to say before we wrap it up, uh
I learned a lot. I think our community
has learned a lot. We're going to keep
learning
you guys after this talk is over. So,
thank you for coming in and being
partners with us. Yeah, thanks for
having us. Yeah. Um
so,
I think this this gave us all a better
understanding of what's possible with AI
and and
um and that's one of the purposes of
this series is to inspire people
by highlighting what

[00:47]
innovators like you are doing so that
other people might find their own path
forward. Um and and hopefully AI can
also lower the frictions for them in
their search for their own um
uh way of navigating this complexity. Um
and as you said, Jacob,
a lot of people want this to work
better, and what we're fighting often is
not each other, but the complexity of a
system, a legacy of previous For sure.
uh previous years and decisions. Um so,
thank you everybody who joined us today.
Um the forum is shaped by you and your
questions and your curiosity. We're
grateful for you
uh here in the conversations um that we
get to have with you. Um as a look
ahead, we have some more forum events
coming up. Uh that includes
conversations um like reimagining
cultural heritage with OpenAI. That's
going to happen with the Sanskriti
uh Foundation uh and Asmona next
Tuesday, March 24th at 8:00 a.m. Pacific
time. Um that session's a replay of a
recorded event uh OpenAI forum event

[00:48]
that was originally held in India um
brought together uh by OpenAI, Asmona,
the Sanskriti Foundation, uh which is
one of India's leading cultural
institutions. So, we'll be sharing more
details soon. Uh stay tuned. Keep an eye
on your inbox and the forum platform, uh
and thank you for being here. And we'll
see you at the next event.

</details>

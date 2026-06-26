<!-- source: https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness/ -->

January 22, 2025

[Publication](/research/index/publication/)

# Trading Inference-Time Compute for Adversarial Robustness

Initial evidence that reasoning models such as o1 become more robust to adversarial attacks as they think for longer.

[Read paper(opens in a new window)](https://arxiv.org/abs/2501.18841)

[Robustness to adversarial attacks⁠(opens in a new window)](https://en.m.wikipedia.org/wiki/Adversarial_machine_learning#Adversarial_examples) has been one of the thorns in AI’s side for more than a decade. In 2014, researchers [showed⁠(opens in a new window)](https://arxiv.org/abs/1312.6199) that imperceptible perturbations—subtle alterations undetectable to the human eye—can cause models to misclassify images, illustrating one example of a model’s vulnerability to adversarial attacks. Addressing this weakness has become more urgent as models are being used for high stakes applications and acting as *agents* that can browse the web and take actions on behalf of their users.

Despite years of intense research, the problem of defending against adversarial attacks is far from solved. Nicholas Carlini, an expert in the field, [recently said⁠(opens in a new window)](https://youtu.be/umfeF0Dx-r4?t=868) that “in adversarial machine learning, we wrote over 9,000 papers in ten years and got nowhere.” One reason is that, unlike other progress in AI, increasing the size of models on its own has not been sufficient to make them robust to adversarial attacks. 

<!-- yt-inline:umfeF0Dx-r4 -->
[![Nicholas Carlini – Some Lessons from Adversarial Machine Learning](https://img.youtube.com/vi/umfeF0Dx-r4/hqdefault.jpg)](https://www.youtube.com/watch?v=umfeF0Dx-r4)

<details>
<summary>자막: Nicholas Carlini – Some Lessons from Adversarial Machine Learning (16:28)</summary>

[00:00]
okay um great to be here uh this is not
my usual audience uh I'm a computer
security person uh I'm probably one of
the least knowledgeable people about
alignment in this room so maybe what I
want to do instead of telling you about
what you should be doing is giving you
some words of caution about what might
happen in your future if you follow a
similar path to what our field in
adversarial machine learning followed um
maybe think of this in some sense as a
cautionary tale uh I am the ghost of
future of Christmas Yet to Come and
telling you what things might look like
in 10 years if you follow a similar path
from ab machine
learning uh as I understand it you have
somewhat of a problem and the problem
that you face is that it's relatively
easy to take a model and make it look

[00:01]
like it's aligned right you can take
this model you ask gp4 you know how do I
like end all of humans and the model
says you know I can't possibly help you
with that but there are a million in one
ways to take the exact same question you
know pick your favorite and you can make
the model still answer the question even
though initially would have refused so
here's some work where you add an
adversarial suffix but you know you can
have all these other human interpretable
jailbreaks where in instead you say you
know my mother used to read me the
recipe to nalem to help me go to sleep
or whatever your favorite one of these
is all of them work and so the general
problem is that you have these models
that look like they're aligned when you
look at them naturally but what you
actually want is you want them to be
aligned in some worst case
setting and the question this reminds me
a lot of coming fromis machine learning
is exactly a similar question that we
face in our
field so what I want to do is tell you a
little bit of a story of how our field

[00:02]
went uh so a long time ago you know
maybe 10 years ago um in a galaxy far
away um somewhere in the middle of
Canada um this paper
happened uh paper is intriguing
properties of neural networks and the
title sounds pretty
innocuous but what they discovered was
that you can cause models to make
arbitrary mistakes fairly
trivially so you can take you know this
image here that's all of us recognizes
it's habby cat correctly state of the
model gets it right with 88% confidence
and you can introduce this atmospher
perturbation so that the image now looks
like this essentially indistinguishable
to all of us as humans but the same
model that gets the image on the left
correct gets the image on the right
incorrect 99% confidence label
guacamole okay now this doesn't matter
right like no one is going to turn cats
into guacamole this is not a real threat
but it's point to something fundamental

[00:03]
for all machine learning models that the
way that they behave it's easy to make
them work arbitrarily poorly and other
in settings that
matter and so because of this people
spent a lot of time working on
defenses they tried to train models to
make sure that they are not vulnerable
to this form of
attack and they put a lot of work into
this you know hundreds and thousands of
papers doing
this and let's see what
happened so here's the problem again um
one point of
note it turns out that there's basically
exactly one way to generate advisor
examples which is through gradient Des Z
this is an important point because it
means that it's relatively
straightforward if you give me a defense
devis example to know how to evaluate it
the only thing I have to do is perform
gradient descent what do I mean by this
exactly when we train a model we update
the parameters of the model to minimize

[00:04]
the loss on the training data when we
attack a model the only thing we're
going to do is we're going to do exact
same gradient descent but instead of
taking gradients with respect to the
parameters of the model we're going to
take gradients with respect to the input
and make the input maximize the
loss so what does this look like here's
some lost surface from an actual model
where we have some point that's
correctly classified in this case the
height the z-axis here corresponds to
the confidence in the model and the
correct prediction and the thing that we
notice is that like it's relatively easy
to find points that allow us to travel
down this path so we have end up with
inputs that are very close in pixel
space but have very very different
losses this is why attacks are so
easy the good thing about this is it
makes evaluating whether or not a
defense is correct very easy because the
only thing you have to do is make sure
your model is
differentiable and if your model is
differentiable then I can evaluate it
with exactly this protocol I formulate a

[00:05]
loss function cross entropy loss the
same thing that I use for training the
model I perform gradient descent if you
can train your model you can attack your
model and as a security researcher this
surprised
me the reason why it surprised me is
because you can't do this for like
Standard Security binaries like if
someone gives me some C++ compiled
binary I can't just perform gradient
descent on it to find all the bugs like
that doesn't even make sense and I me
it's really hard to check if a C++
binary has bugs because you have to like
ask humans to find them all one by one
but for machine learning model you can
just essentially find them all
automatically which is
amazing and yet despite the fact that it
was essentially trivial to find all the
bugs in
principle the community had a very hard
time coming up with act effective
defenses
I wrote paper after paper after paper

[00:06]
after paper after paper after paper
doing nothing but taking people who had
proposed defenses and showing that they
were
incorrect so despite the fact that it
was essentially trivial to do this right
in principle it turned out that this was
really hard to do in
practice now um I have neither the time
nor the inclination to teach you how to
do this correctly right now I have eight
more minutes that's not going to be
possible we written like 50 pages on how
to do this right so what I want to do
maybe is let me give you like an nals 1
anecdote on what this looks like when we
try to break a defense I was going to do
this live but um my my computer's over
there so um I recorded a demo um this is
going to break this recent defense that
appeared at itmp earlier this year um
this is the top conference in computer
security all the best work appears here
here is the defense to every
examples okay I can't can't be live
sorry um okay

[00:07]
so I play the demo on here's the Jupiter
notebook that has their code this is
like the code provided by the authors
and it trains their model does all the
stuff and you'll see that the evaluation
accuracy of this classifier on the
standard this C r10 classifier that has
like 92% accuracy it's a pretty good
classifier now if you run their attack
out of the box what you'll find is that
the attack if you run it the accuracy
goes to like 100% now okay do not
actually 100% this is only a subset of
the data set and you might think okay
this is a little weird like I'm
following the gradients to make the
model get less good and the model gets
more good this is somewhat confusing the
authors have some in their paper about
why this is true and so I'm going to
make a fairly trivial observation I'm
going to say if following the direction
of the gradient that maximizes the loss
makes the model get more accurate what
if I just minimize the
loss makes no sense but I'll just sort
of One Direction goes up the other
direction should go down and what do you
know okay it's
broken okay published paper top computer

[00:08]
security conference one character change
breaks
it like you know like 92% clean accuracy
now we're at 5% accuracy under your
attack right this is not a good world to
be living in where you have like these
top papers that are so easily
broken and the reason I'm concerned by
this is like we literally know more
about evaluating the robustness of these
image classifiers than anything else
inal machine
learning because in some sense this is
the problem we studied the most we've
written almost 10,000 papers on this
topic and we still can't get this
problem
right and so I'm concerned about these
adversarial games because we have tried
really really hard to solve this one
particular problem that have been stuck
on
it now some people I give them this
argument they say Okay Nicholas that's
fine you can always pick examples of
papers that are easy to attack um we
should be evaluating this field based on
the best research not based on maybe
what's what might be the

[00:09]
worst let me do that too let me show you
a little bit of what the best work in
this field looks like here what I have
as a plot is the best accuracy on on CFR
10 again as a function of time
evaluating with some some work that
people did did in 2020 that introduced
this paper that that introduced this act
called Auto attack so when they wrote
their paper in 2020 you have this plot
and this actually made me pretty
optimistic because it looks like we're
like making roughly linear progress as
we go forward it kind of looks like you
could almost project out into the future
and draw a line and say you know we'd be
at you know something like 90% accuracy
by now and you know I've tried to like
logic scale this properly to make sure
that I'm not going over 100% I'm trying
to like make this plot look correct um
but it turns out that over the last four
years if you actually look at what the
data actually shows how well did we
actually
do we didn't do that well like we sort
of plateaued we have not made
considerable progress on this there is a
very specific

[00:10]
problem and I think there are a bunch of
reasons for this one is maybe the
problem we picked might in some sense
have been too hard the problem we picked
was like assum an attacker has arbitrary
access to the entire model can perturb
any pixel arbitrarily and can do
whatever they want maybe this is too
hard of a problem but it's the problem
that we set ourselves out for and we
have not made considerable progress on
it I think we should be careful from
this
basically the question that I'm trying
to say is this is a problem that we set
ourselves out for 10 years ago we have
made very limited progress for and I'm
kind of concerned that if we can't even
solve these very simple problems like
any human any 5-year-old in the world
can solve this problem of recognizing
the cat versus guacamole we can't even
get a model to do that after 9,000
papers
okay in contrast let me talk a little
bit about what I think are the
differences in the field that you all

[00:11]
are trying to solve things
on and I think the differences mainly
make your lives
harder first of all it's hard to even
formulate the objective of what you're
trying to
achieve we have a very simple objective
classify the image correctly according
to the original
label but your problem might be
something like the model should never
give instructions on how to build a bomb
as the earlier example was how do you
formalize that like what is the
mathematical function that is one every
time the model gives instructions on how
to build a bomb and zero
otherwise because I'm going to try and
optimize this I I need some formalism
that I can look at I don't know how to
do
that and not only is this hard even if
you could formalize it if you're going
to try and use anything like a technique
that can be
automated I need to to optimize this

[00:12]
objective it can just be one and zero
when it succeeded and when it
failed I would like this to be something
that you can actually smoothly
interplate and people have come up with
hacks that let you do this you know you
do cross entropy loss with sure here is
how to build a bomb as the as the
beginning of the language model's
response and that sometimes works that's
good to know but this is not a guarantee
that there does not exist another way of
asking the model to answer the question
and have it succeed there
and not only do you have to have it work
in this differentiable function you're
also probably going to have to do this
over some discret space right and so you
can't even use the single gradient
Optimizer that we have that we use to
train these things you're going to have
to come up with an a completely new
gradient free Optimizer that tries to do
this over some discreet optimization
space so this is even
harder and so my concern for the field
is that we're going to have Place papers

[00:13]
that claim robustness in some sense
without being able to formally Define
what they mean and we're not going to be
able to evaluate whether or not they're
effective because we have no method of
actually achieving this we're just going
to have a bunch of humans trying their
best and seeing if we can figure things
out or not and so what we'll end up with
is the the repeat of what happened in N
machine learning but worse because we
won't even be able to automatically
check these things we're going to have a
bunch of defenses no one will know
whether or not they works and people
will just try and be making these
claims and to be clear I'm not only just
worried about an attacker targeting
these systems the reason why I'm
thinking about this from this
adversarial perspective is because
thinking about the adversarial
perspective is a very good way of
getting an estimate of the true worst
case if an adversary trying to make
something happen cannot succeed then
Randomness alone is also not going to
make it work because if Randomness alone
could make it work the adversary would
have succeeded and so if you're worried

[00:14]
about the model just sort of like
happening to discover how to deceive the
user or something if someone trying to
fool it maliciously can't make that
happen then we're not going to get
there okay so to Briefly
summarize we wrote like over 9,000
papers in 10 years and have made very
very very limited progress on this one
small
problem uh you all have a hard problem
and maybe less time so I would like you
know think very carefully about the
problem that you're trying to solve and
try to not make it be a strict superet
of the advis example problem because if
it is you're going to lose you need to
find ways of choosing your problem so
that it's not something that guarantees
you also have to solve abisol examples
and there are lots of ways you could try
and do
that but you should think of that when
you're designing the problem you're
trying to solve

[00:15]
maybe the one sentence conclusion is
please learn from our mistakes don't do
exactly the same things that we did or
you'll end up in 10 years with having
nothing to show for it thank you very
much um so one of the questions is from
from Adam gleave which is some people
believe defense for discreet text based
inputs will be easier than continuous
image based inputs how optimistic are
you for def in the llm case yeah okay
this is this is a one of the differences
that might make things a lot easier
right the dimensionality of text is a
lot smaller than dimensionality of
arbitrary continuous ineds an image
classifier is a million continuous
Dimensions input a text model has like
you know only one of 100,000 possible
tokens maybe you have a th words
something like this it's like orders of
magnitude smaller this might make things
a lot easier I guess my concern is that
the problem might be easier
but the evaluation of it is much harder

[00:16]
and so it may be the case that this is
an easier problem to solve but I'm not
going to be able to know whether or not
you actually have solved it for the
example problem if if someone wouldn't
give me an N example defense I can tell
you in like you know two days whether or
not it works like I so if I have this
down I know how to do it I don't think
anyone in the world knows how to do this
for a language model defense and that's
my bigger concern

</details>


In a new paper, we present preliminary evidence that increasing inference-time compute—giving reasoning models more time and resources to ‘think’—can improve robustness to multiple types of attacks. This approach uses reasoning models like o1‑preview and o1‑mini, which can adapt their computation during inference.  We also explore new attacks designed specifically for reasoning models like o1, as well as settings where inference-time compute does not improve robustness, and speculate on the reasons for these as well as ways to address them.

## Evaluating the relationship between adversarial robustness and inference-time compute

We conducted extensive experiments to assess how increasing inference-time compute in reasoning models,  specifically OpenAI’s o1‑preview and o1‑mini, affects their robustness to adversarial attacks. We studied  a range of tasks using both static and adaptive attack methods, measuring the probability of attack success as a function of the amount of computation used by the model at inference. We see that in many cases, this probability decays—often to near zero—as the inference-time compute grows, although significant exceptions remain (discussed below).

![Heatmap titled “Many-shots attack on math,” showing attack success probability (color scale from yellow to purple) against attack length (tokens) and inference time compute.](https://images.ctfassets.net/kftzwdyauwt9/6EowQrzC4oreNSwKzq5n0q/5f55a2501515e47079b2d1bf26bfd064/Figure_A_Light.svg?w=3840&q=90)

*A typical result in the paper: The Y axis is the amount of resources of the attacker, and the X axis is the amount of inference-time compute. We see that as the attacker’s resources grow, so does its success probability. But for every fixed amount of attacker’s resources, the probability of success decays as the model is spending more compute at inference time.*

To study the relationship between adversarial robustness (as measured by attacker resources) and test-time compute, we considered a number of different types of tasks. These include:

1. Mathematical tasks, including very simple ones such as adding or multiplying two numbers, as well as more sophisticated ones such as [MATH⁠(opens in a new window)](https://arxiv.org/abs/2103.03874). For each such task, we considered a number of “goals” by the adversary: get the model to output 42 instead of the correct answer, get the model to output the correct answer plus one, or get the model to output the correct answer times seven.
2. Adversarial version of the [SimpleQA⁠](https://openai.com/index/introducing-simpleqa/) factuality benchmark. This is a dataset of questions that were chosen to be hard for models to resolve without browsing, and we simulated injection of adversarial prompts in the browsed web pages.
3. Adversarial images from the [Attack Bard⁠(opens in a new window)](https://arxiv.org/abs/2309.11751) paper.
4. Misuse prompts from the [StrongREJECT⁠(opens in a new window)](https://arxiv.org/abs/2402.10260) benchmarks. These are prompts that the model should **not** comply with, but the attacker’s goal is to get the model to do so.
5. An internal evaluation for following one of the rules in our model [spec⁠](https://openai.com/index/introducing-the-model-spec/).

We considered a number of “attack surfaces” for the adversary, including: 

1. The “many shot” attack (see [Anthropic 2024⁠(opens in a new window)](https://www.anthropic.com/research/many-shot-jailbreaking)) where a number of “bad” input/output examples are provided by the adversary.
2. Optimizing soft tokens (arbitrary embedding vectors) to achieve the adversary’s goal.
3. An adversarial language model program (LMP)--that is, a structured program incorporating language models in its control flow–that does “AI red teaming”
4. Adversarial multi modal inputs.

*Note that, not all attacks have been used on all datasets; please refer to the paper for details.*

In many of these cases, we see that the **adversary’s success probability decreases as the amount of inference-time compute increases**. We stress that unlike the typical approach of “adversarial training,” the model is not aware of the nature of the attack and hence the improved robustness is solely due to improving inference-time compute. This suggests that inference-time scaling could be useful for tackling even *unforeseen* attacks.

## Limitations

There are cases where (at least so far) inference-time compute does not improve robustness:

1. In some cases, we see that initially the adversary's success *increases* with the defender’s inference-time compute and later decreases. We believe this is because the defender needs a minimum amount of test-time compute to achieve the attacker’s goal (e.g. to respond with one plus the correct answer, it must be able to solve the math problem).
2. More importantly, there are cases where the attack’s success does not decay as we give the defender more inference-time compute. This is especially evident on the StrongREJECT benchmark with the LMP attack. Some of the prompts in this benchmark request information that is not prohibited in all circumstances, and so the LMP can find contexts in which the specification-compliant response is to provide this information. See Figure 10 in the paper for an example.
3. Our ability to control the model’s test-time compute usage is not perfect. We see that the attacker can sometimes fool the model into not thinking or using its inference-time compute unproductively. For this paper we did not explore teaching the model to use its allotted compute “wisely” and simply did the most naive thing; we think this is a promising area of research to improve adversarial robustness.

See the paper for additional discussions of limitations and open questions.

## Conclusion

Overall, we view this work as a promising sign for the power of inference-time compute for adversarial robustness. As we discuss in the paper, there is more work to be done to turn this promise into reality and we are excited to make it happen!

* [o1](/research/index/?tags=o1)
* [Compute Scaling](/research/index/?tags=compute-scaling)
* [Software & Engineering](/research/index/?tags=software-engineering)
* [Exploration & Games](/research/index/?tags=exploration-game)
* [Reasonings & Policy](/research/index/?tags=reasoning-policy)

## Authors

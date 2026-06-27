---
title: "Reinforcement Fine-Tuning—12 Days of OpenAI: Day 2"
channel: openai
url: https://www.youtube.com/watch?v=yCIYS9fx56U
youtube_id: yCIYS9fx56U
published: 2024-12-06
duration: "20:35"
captions: en-orig
---

# Reinforcement Fine-Tuning—12 Days of OpenAI: Day 2

[![Reinforcement Fine-Tuning—12 Days of OpenAI: Day 2](https://img.youtube.com/vi/yCIYS9fx56U/hqdefault.jpg)](https://www.youtube.com/watch?v=yCIYS9fx56U)

<details>
<summary>자막: Reinforcement Fine-Tuning—12 Days of OpenAI: Day 2 (20:35)</summary>

[00:00]
hi everyone my name is Mark and I lead
research at openai yesterday we took 01
out of preview and we launched it in
chbt we're soon going to launch it in
the API if you haven't been following o1
it's our latest series of model
improvements that allow the models to
think for a while before they come back
with a response today we're really
excited to preview our latest
advancement in our model customization
program it'll let users find to 01 on
their own data sets and again this isn't
standard fine tuning this is
reinforcement fine tuning which really
leverages the reinforcement learning
algorithms that took us from Advanced
High School level to expert PhD level
for your own use cases I want to stress
again that this is a preview of
something that we're going to launch
publicly next year but if you are a
university or you're a researcher or
you're an Enterprise we'll give you some
information on how you can access our

[00:01]
output program later so why would you
want this thing well it allows you to
take your golden data sets and turn them
into unique
offerings that will give you the same
magic that we have for your own users
and your own customers so I'll let John
Julie and Justin say a little bit more
yeah hello everyone yeah my name is John
Allard and I'm an engineer here at openi
hi everyone I'm Julie W I'm a researcher
here at open AI I'm Justin ree I'm a
computational biologist at Berkeley lb
today today we're so excited to be
introducing this new way of model
customization for our 01 series of
models uh reinforcement fine tuning or
rft for short for the first time
developers researchers and machine
learning Engineers will be able to use
reinforcement learning to create expert
models capable of excelling at their
specific tasks within their domain we
believe that any field which requires
deep expertise in their AI models stands
the benefit so if you work in say legal
Finance engineering Insurance uh this

[00:02]
one's for you for example we recently
partnered with Thompson Reuters to to
use reinforcement fine-tuning to
fine-tune 01 mini to be a legal
assistant in their co-counsel AI um this
this tool assist their legal
Professionals in accomplishing some of
their most analytical
workflows yeah so some of you will be
familiar with the supervised fine tuning
API that we launched um early last year
and supervised fine tuning is really
powerful what you're trying to do is get
the model to replicate features that it
finds in uh input text or images and
this is great if you want to change the
tone or the style or the response format
of the model now with reinforcement
fine-tuning or reindeer enforcement fine
tuning I should
say the with reinforcement fine tuning
um it's actually it's different so
you're not just teaching the model to
mimic its um its inputs what you're
teaching it to do is to learn to reason
in entirely new ways over custom domains
and the way this works is that we when
the model sees a problem we give it

[00:03]
space to Think Through the problem and
then we grade the final answer from the
model and then using the power of
reinforcement learning we reinforce
lines of thinking that led to correct
answers and we disincentivize lines of
thinking that led to incorrect answers
um and what you'll see is that you know
with as little as a few dozen examples
the model will learn to reason in new
and effective ways over custom domains
that's crazy that you can do that with
just 12 examples that's not something
you can do with regular uh fine tuning
yeah exactly yeah in the in the space of
large language models and large machine
learning a few dozen examples is is
basically nothing yeah so for the first
time our model customization platform
will support reinforcement learning and
and notably this is the same technique
that we use internally at open AI to
train our Frontier models like gp40 and
the o1 series one area with many
exciting applications is scientific
research but don't just take our word
for it that's why we're joined today by
Justin ree uh Justin is a researcher at
Berkeley lab and one of his areas of
study is using computational methods to

[00:04]
understand the Gen the genetic causes
underlying rare diseases Justin thank
you so much for being here do you mind
telling us a little bit more about your
research and how reinforcement fine
tuning might help sure thanks it's great
to be here so one of the areas of my
research is rare genetic disease so
contrary to the name rare rare genetic
disease is actually not rare So any one
rare disease is rare but if you put them
all together um they're actually quite
common and so we're talking about 300
million people globally who who suffer
from a rare disease and what's more
these people often have a long
diagnostic Odyssey of months to years
before they find out about their
condition W it's like uh the whole
population of the US yes it's not a
small number of people and so what we're
working on is better uh computational
tools and methods to to Really research
what's important uh and and to help us
understand and treat these diseases so
we we do our work in kind of an academic
setting and learning more about the rare
disease and their causes and the the
hope is we'll be able to advance the
healthcare for these folks uh going down
the line and now assessing rare disease

[00:05]
is kind of hard because you kind of have
to have two things you have to have sort
of expert domain knowledge about the the
medical side of things and you also have
to have uh sort of systematic reasoning
over the biomedical data and this is an
area where we think that o the oan model
can really help us out with its
reasoning capabilities that makes a lot
of sense you know our large language
models have domain knowledge and our o1
models are really systemic reasoners so
it seems like now there's a pretty good
computational method for addressing some
of these that's right can you tell us a
little a little bit more about the data
sets that you're using sure so this was
sort of a collaborative effort between
uh our our group and charot Hospital in
Germany and Peter Robinson's lab and the
Monarch initiative um and what we did
really was was to extract disease
information from hundreds of scientific
Publications that were case reports
about rare disease and so uh we sort of
curated the information uh and that's
lists of signs and symptoms that were
present in in the patient and that were
excluded in the patient and then of
course the the disease that they had and
importantly for the conversation the

[00:06]
causative Gene that was mutated that was
causing the problems in these fols I see
so you and maybe some doctors are trying
to figure out given a patient symptoms
uh What gene might have mutated to cause
those symptoms yeah that's right and and
so something we've been working on
together with the open AI team is is uh
training the old one the old one models
to reason more effectively about the
causes of disease incredible thank you
Justin uh we're now going to give you a
preview of reinforcement fine-tuning at
work and not to steal any Thunder but
we're going to take 01 mini and make it
exceed the performance of 01 on this
task uh that's the 01 that we just
launched yesterday and this matters so
much because o1 mini is a smaller faster
and cheaper model than 01 yeah so using
Justin's data set we're going to show
you can just drastically improve the
performance of ow and mini um on this
task where given a list of symptoms
you're trying to predict which Gene
might be responsible for the genetic
disease and so to give an overview of
this process we're going to start by

[00:07]
looking at uh data sets that are used to
train the model and graders that are
used to evaluate the model and then
we're going to um launch a training job
on open AI training infrastructure and
finally we'll evaluate the resulting
fine-tune model so we can see how it's
improved over the base model that we
started with so to start us off we're
going to jump over to the open AI
development platform and we're going to
go ahead and we're going to create a new
model so um you know we've had
supervised fine tuning for a bit over a
year now what we're going to do is we're
going to select reinforcement fine
tuning now we're going to be training o1
so we'll select that as the base model
and now we need to upload a training
data set and now training data sets
they're just Json L files which is just
a file where each line in the file is an
example that you want the model to be
trained on for this um case Justin and
his colleagues assembled a data set of
about 1100 examples um and so I'll go
ahead and upload that one and just so
that we get a really good feel for um
how this data set works and what this
task is we'll zoom in on an individual
data point really quickly and so this is

[00:08]
what an individual data point looks like
and there's really three important
things here so the first is the case
report and this is a description of the
patient and the patient symptoms so we
see that the patient was a 51-year-old
woman the disease onset was not
specified we have a list of symptoms
like hyperism um hyperthyroidism and
others um as Justin said earlier we have
the absent symptoms um these are the
symptoms that are not present and this
is important because it helps the model
to rule out genes that it might think
would otherwise be responsible um for
the symptoms that are present next we
have the instructions and I'm sure if
you're watching this live stream you're
familiar with prompting and so all we're
doing here is just prompting the model
for um what we wanted to do for this
task and so what we're saying is you
know given the list of symptoms and the
case report can you list all the genes
that you think might be responsible for
the um for the genetic disease that that
you think is present and then we also
asked it to provide an explanation for
why it thinks those genes might be
responsible um finally we also have the
correct answer and so this is the gene

[00:09]
that we happen to know is responsible
but importantly we're not showing this
to the model during the training process
that would be cheating but we're using
it internally during the training
process to grade the model's outputs or
to check if the model is correct this is
a pretty hard task uh I definitely have
no hope of answering this question yeah
I mean you can tell that we're we've
come up far away from just trying to
count the number of RS in the word
strawberry yeah so
um so um now when we give the model this
prompt this case report and these
instructions the model is going to
output something like this which is a
list of genes that it thinks might be
responsible and importantly the genes
are in sorted order where the first Gene
in the list is the one that it thinks is
most likely to be responsible the second
one in the list is the one that it
thinks is second most likely and so on
and so forth cool so um we'll hop back
over and so um next we need to upload
some validation data and validation data
um it's going to be in the exact same
format as the training data but
importantly there's no no overlap in the

[00:10]
correct genes between the validation
data set and the training data set and
what that means is that the model can't
cheat it has to um or it can't learn to
just memorize a list of symptoms and
Associate those with the gene it has to
actually generalize from the training
data set to the validation data set
gotcha so I mean where's the
reinforcement part come in you know we
talked about grading uh is that part of
the process here yeah that's a really
good question so grading is done by this
concept of graders that we're we're
introducing here and so um graders are
are really simple what a greater does is
it takes the output from the model and
it takes the correct answer and it
Compares them and it returns a score
between zero and one and so zero means
that the model did not get the answer
correct at all and one means the model
got the answer correct and you can also
give partial credit so it can be
anywhere in that range so for this
specific task we have a grader that
looks like this so it takes the correct
answer um that we happen to know and it
takes the output from the model which is
the list of genes and it produces a
score so in this case you know foxy3 is
the correct answer it was second in the

[00:11]
list of genes and so it gets a score of
like 7 I see so if it had instead said
foxy 3 was first in the list I would
have gotten a grade of one yeah exactly
and then as it gets further and further
along the list the score kind of
gradually decays to zero ah nice makes
sense um but what if I have a task that
isn't you know grading A ranked list do
we have other graders that are more
General yeah yeah so we're supplying
kind of a collection of graders that we
think pretty effectively cover the space
of possible intents that you might have
um you for while doing enforcement fine
tuning and we're always adding more yeah
and eventually we're going to hopefully
let you define your own graders yeah
yeah maybe like upload a python file or
something and do some custom grading
yeah cool so um we've defined our
training data set we've defined our
validation data set let me go ahead and
copy in the grader really quick
um and now openi allows you to set um
you know we allow you to customize these
fine tuning runs by setting hyper
parameters but we set some pretty good
default so I'm just going to go ahead
and click create
here now what this is doing is is um you

[00:12]
know we we've just kicked off a training
job um and so the really cool thing is
that um you bring the data set and you
bring the greater and these are the
places where you really have domain
expertise and where you can really
contribute to this problem and then you
get to leverage the full power of open
AI reinforcement learning algorithms and
our full distributed model training
stack to customize a Frontier Model for
your use case so as a user as a user I
just like to bring my data set and
grader and open takes care of everything
else yeah exactly yeah um so you know
reinforcement F tuning jobs can take
anywhere from a few hours to a few days
to run so we're going to jump over to a
job that I ran earlier this week on the
same data set um just so we can kind of
see the
results so I'll jump over
here um so I have this job that I ran
earlier this week um it completed
successfully It produced a fine two
model for us and there's one thing that
I want to um look at which is um the
validation reward score and so what this
is is the it's the average score from
the greater on the validation data set
and how it changed over the course of

[00:13]
the fine-tuning run and so what we can
see is that the score is going up and as
we said earlier since there's no overlap
in genes between the training data set
and the validation data set it means
that the model really learned to
generalize on our task um it wasn't
simply memorizing a list of symptoms and
mapping those to genes so you know while
this is cool you know the chart goes up
and to the right which is what we like
to see um it'd be nice if we could get a
better feel for how the model has
actually changed during the fine-tuning
process and so you know we'll we'll take
a closer look at that now
all right so we're going to pop over to
the evaluations dashboard which is a
product in our developer platform that
we launched earlier this year um there's
a lot of numbers but don't worry we're
going to go through all of them so I've
set up three different runs here the
first one was uh a run against our 01
model which we released yesterday the
second was against 01 mini which was the
starting point of our fine-tuning job
and then finally uh the reinforcement
fine tuned 01 mini now we looked at the
reward going up and to the right but

[00:14]
what does that actually mean for this
task I've set up three different
evaluations to sort of assess that the
first one is top at one which is how
often is the correct answer the very
first item in the list top at five which
is how often is the correct answer in
the top five elements of the list and
finally top at Max did we at all put the
right answer in our list um and so
looking at top at one we can see that
our starting point ow and mini got 177%
on our data set of about 200
01 got 25% so it's doing better uh but
then our fine-tuned 01 mini got
31% awesome uh I took a screenshot of
this and I put it into chat GPT and
asked it to make me a plot a Christmas
them plot and uh here's a nice
visualization of those nine numbers that
we saw earlier so you can see uh our
starting point 01 mini uh across top at
one top at 5 and top at Max our 01 model
and then finally our best performing
model which is this 01 mini fine tune

[00:15]
here in um dotted red line so looking at
these results what do you think Justin
well I I think this is pretty impressive
performance and and especially the
increase in the in the validation uh
data because that implies that the model
is learning something generally about
how to reason over these kind of data
which is pretty exciting um and and so
an obvious question you might ask is how
is this doing comparing compared to
existing bioinformatics tools and I
don't really have an Apples to Apples
comparison but um because typically in
this kind of experiment you would
provide uh genomic sequencing data and
we haven't included that here um but the
sort of open-ended quering of models
here over incomplete symptom list is is
new and exciting I think great uh so
these are aggregate statistics but let's
look at the actual model responses so
I'm going to pop on over to this data
tab let's filter by the passes uh and so
here is the input that we're giving to
the model so the problem as John
described earlier is to identify genes
that may be responsible for a set of

[00:16]
observed symptoms uh we asked the model
to Output a dictionary containing both a
string that explains you know why did I
pick these genes and of course the genes
themselves in ranked order and then
finally we have the symptom list as well
so this um patient presented with sub
endal nodules
seizure uh yeah and a couple other
things uh we then run our models so this
was our 01 model this this one our
fine-tuned o1 Mini model um we gave it
that input and now the output is uh this
dictionary that we described earlier so
reasoning the combination of sub endal
nodules uh seizure cortical tubulars are
indicative of this complex which is
commonly caused by mutations in these
genes um it lists a couple other
potential ones and then it says
tsc2 is the most likely um candidate and
if we scroll back on over to our answer
we'll see that tsc2 is in fact the

[00:17]
correct answer so that allowed us to get
a pass on top at one top at five and top
at Max so looking at this output um
Justin like is this a useful output for
the model to be giving back yeah
absolutely so it's particularly useful
to see the model's reasoning and that's
a big contribution here and also the r
obviously the rank list of answers so
even if the the the correct answer is
not first you know you can you can look
at all the possibilities um and
it's it's also great to see the
fine-tuning improves the performance of
in the rank list of possible answers so
that that right answer is getting closer
to one so that's gratifying Justin kind
of zooming out a little bit like how
does reinforcement learning shape your
field um can you talk about some Trends
in viy sure so I I think there's a lot
of interest in the research community
and Import in using these models for
these for these kind of tasks and so the
feeling for this particular use case is
that the best solution in in the near
term is probably a hybrid solution

[00:18]
between existing bioinformatic tools and
these uh models like 01 uh and so this
is I think is excellent progressing sort
of characterizing the strengths of these
models and and and also how we can use
uh tools like fine-tuning to improve
performance um and so like I said
there's not really a comparable
Benchmark to compare the two but um it
it's it's definitely progress and and
how we can use these models to kind of
understand disease and then you know in
a larger sense to sort of how we can
incorporate these models into a workflow
that will eventually improve healthcare
for these folks right amazing thank you
Justin so while we've just shown you an
exciting application of reinforcement
fine-tuning in scientific research this
is a general purpose technique we've
seen promising results in data sets from
biocham from AI safety from legal um and
from Health Care as well we can think of
hundreds of more examples or tasks that
we can use this model on but we know
that you can probably think of many more
uh so that's why we're so excited to be
expanding uh our Alpha program today to

[00:19]
enable more people to push the
boundaries of the capabilities of our 01
models on the tasks that matter the most
to them yeah so you know we've been
working with a small group of trusted
Partners to really test out
reinforcement fine tuning and today
we're expanding Alpha access via what
we're calling the reinforcement
fine-tuning research program so um you
know this program is ideal for
organizations who are currently working
on very complex tasks with teams of
experts and who think that they might
benefit from AI assistant on these tasks
so you know if you're interested in
applying for one of these limited spots
you can find a link to the application
in the description of this live stream
and as Mark said ear um earlier you know
we plan on launching this product
reinforcement fine tuning publicly early
next year yeah we're all really truly
excited to see what you do with
reinforcement fine tuning and really
speaking as a researcher there's nothing
that makes us happier than seeing our
models being adapted and used to advance
you know science knowledge in the real
world do you have a joke for us today
well as so happens I do uh as it's

[00:20]
become a tradition I have a Christmas
theme joke so you know we live in San
Francisco self-driving vehicles are all
the rage and actually Santa's been
trying to get in on this too um he's
trying to make a self-driving sleigh but
he for some reason his models just keep
not identifying trees and the Slate is
hitting trees left and right uh do you
guys have any guesses
why
no he didn't he didn't Pine tun his
oh jeez okay all right um please join us
next week we'll have a lot more to share
thank you

</details>

---
title: "Words to Bytes: Exploring Language Tokenizations | Sam Gbafa | OpenAI Scholars Demo Day 2021"
channel: openai
url: https://www.youtube.com/watch?v=TsFLqbiim4M
youtube_id: TsFLqbiim4M
published: 2021-05-10
duration: "15:17"
captions: en-orig
---

# Words to Bytes: Exploring Language Tokenizations | Sam Gbafa | OpenAI Scholars Demo Day 2021

[![Words to Bytes: Exploring Language Tokenizations | Sam Gbafa | OpenAI Scholars Demo Day 2021](https://img.youtube.com/vi/TsFLqbiim4M/hqdefault.jpg)](https://www.youtube.com/watch?v=TsFLqbiim4M)

<details>
<summary>자막: Words to Bytes: Exploring Language Tokenizations | Sam Gbafa | OpenAI Scholars Demo Day 2021 (15:17)</summary>

[00:00]
all right um hey everyone my name is sam
and i'm excited to talk to you guys
about the project i've been working on
for the last six months
um word to bites exploring language
situations
um so i'm going to talk a bit about my
background uh then
dive into project context uh then dive
into the project
and then talk about what i've learned
just during my time at open ai
all right um so um i've worked at
software engineering for last couple
years and i was working on my startup
level
which is a platform for choice-based
stories where people could create their
own 3d adventure stories
and other people could play them during
this time i encountered gt2 and i
thought it'd be really cool to enable
writers to create
kind of ai generated stories um gpc2
didn't have the greatest completions
but it did get me really interested in
language models um
in other generative models um so i was
interested in
multimodal uh explorations and maybe
videos that could
uh models that could um
maybe generate future videos from

[00:01]
current video or future audio from
current audio but i quickly realized
that that'd be pretty challenging um
so um well uh so while in scholars
program i explored
lots of different things um explore
sequence models like lstms and
transformers
i learned the basics the basic problems
and solutions that occur in deep
learning
in deep networks like vanishing
exploiting gradients learn about meta
evolution
resonance a bit about reinforcement
learning um and throughout this time i
was always interested in
being able to apply some of these
techniques to learning multiple
modalities
particularly because it's how we learn
as humans um we don't just read text we
have visual and auditory experiences
that help us create
our own internal models and i was
interested in how machines can do that
um so because uh our audience is really
general i wanted to give some context
to my project um so first i wanna talk
about sequence modeling
uh sequence models are used to explore
data where your input or output data
has a particular sequence that encodes

[00:02]
information
um so common example is something like
siri where you're like hey siri turn on
the lights
um or you can have an example um like
deepmind is doing where you're taking
going from a dna sequence
to a folded protein um
another thing i want to uh kind of
introduce is the idea of unsupervised
learning particularly with particularly
with other aggressive models
um so auto aggressive sequence model uh
predicts current or future values uh
based on past values
so um uh gt3
is open ai's one of their
popular language models um and
my the model i train is really similar
so you have a training corpus
um right now i can consider all of
wikipedia as an example
as a particular article about the
titanic um you could break
you break up your corpus by taking maybe
the first 64 words in next 64 words
and come up with training examples um so
with each example
um you're basically giving it to your
model and having your model predict each

[00:03]
word
um and basically you're giving your
model these examples over and over and
over again
and ideally as it's going through these
training examples it's learning the
relationships there
um so if you were to perform inference
and give your model
uh an example and say that satanic was
uh your model might complete it and say
it was the largest ship
or was a british passenger liner
um so diving into my project
so my project basically looked at
sequence models
and particularly tokenizations on those
sequence models
um i looked at some previous works on
other language models
and there are some interesting findings
that led me to focus on tokenization
uh the first was that fine grain finer
grain tokenizations outperformed larger
levels of organizations
so um if you have uh sub words in your
vocabulary
more sub words then those models
outperformed
models with just really big words in the
vocabulary um and additionally learning
the segmentations
could lead to better generalizations and

[00:04]
i'll talk a bit about what i mean by
that
so for my project i took a look at
different tokenizations on the same
dataset
the data i used included articles from
wall street journal and articles
wikipedia
i looked at tokenizations i looked at
words sub words and character
tokenizations
uh and each tokenizer was pre-trained on
the training data
um so i want to give some examples of
what i mean by tokenization
um so i have an example sentence we want
swimming to mitigate the effects
of the blistering sun um so let's look
at words organization of this
um so here we went swimming to mitigate
the effects of blistering sun
um each space um so the tokens are
separated by white space
uh each space is represented by this
underscore um
and so yeah it's pretty pretty
straightforward uh a subword
tokenization
a bricks your uh it breaks your work
your sequence up into sub words
uh so here you can see went is split

[00:05]
into two sub words and likewise swimming
uh the ing is separated from
uh swim uh and also at the end
blistering you can see it's broken up
into three subwords
uh so this allows your model to learn
the relationships
between parts of words uh
most english speakers know that ing
kind of means that you're doing a
particular verb
um so allows your model to also build uh
understanding of that kind of
relationship as well
so what happens if you tokenize like
even smaller segments
uh so you can look at character
technicians um so here
each character is broken up or the
sequence is broken up by each character
um multilingual models are really
uh can have improved performance by uh
tokenizing on
characters um due to the nature of how
different languages are broken up
um maybe if you have uh
like a pictographic language like
chinese uh versus english you maybe
don't want to break it up into
into words um and then

[00:06]
i also took a look at uh bytes
optimizations um
so this is the same sequence in
represented as bytes uh it's
functionally the same as a character
tokenization when you look at english
and this is because unicode uh encodes
characters
as one to four bytes and english
characters are usually encoded as one
byte
so for example we have hui is meeting um
hue is one character
but translates to three characters um so
if we had a
uh multilingual corpus then by
tokenization would be totally worth
looking at
uh but i decided not to so um
for my project i use a 12-layer decoder
only transformer
uh it's about 80 million parameters um i
looked at pantry bank data
on word subword with 40 000 uh
vocabulary and character segmentations
uh the amount of compute was all
constant
and it was the same model and context
length and uh
so we'll talk about some of those
results here we're looking at the
training perplexity
so perplexity is a measure of how well

[00:07]
your model um the degeneration of your
model like how good they are
um so high perplexity uh your model
might generate something like
i fell off the boat and into a porcupine
um versus i fell off the boat and into
the water
um so the first statement is really
hyperplexity
second statement makes more sense lower
complexity um it's really hard to see
what's going on here um so let's like
take a look um at some of these training
steps
so um like zoomed in so here you can see
um your word perplexity is generally
lower um at your lowest and it's
increasing or decreasing
um the fastest uh with training time
um your you would ex so i would expect
um
when performing this uh this experiment
i expected subworks to outperform
characters
um but i here they don't and
uh it's partially because our training
corpus is relatively small
so using a tender tree bank data set you
have
about 10 000 vocabulary words um so

[00:08]
having a 40 000
vocabulary sub word um is a bit
it's a bit high and so it's your your
character
models perform actually better than your
subwoofer models um and so i'll talk
about ways that
uh we could prevent that additionally
um there was our validation for
flexibility is really high um
so this was a one run among many
several runs uh showed this relationship
between words upwards and characters
um however it's just to show that um
our model initially overfit but in
regularizing uh it wasn't regularized
we weren't generalizing well in
this particular run so
some of our findings were that smaller
segmentations can have more nuanced
representation
but you need a larger model to capture
these relationships well
it's partially because these transformer
buildups builds up
its representation in the earlier layers
um

[00:09]
so with characters if you have uh
you you have to maybe build a
representation of a word
before you are able to predict the next
word
um another thing worth considering
um in the project is to vary the context
length so if you have
um in our example from earlier um
it was 11 words but it was 59 characters
so in order to represent the same amount
of data uh your context length
the same amount of uh yeah i guess the
same amount of data your context length
needs to be
uh longer for these smaller
segmentations
um this number of subwords is a really
important hyperparameter uh when doing
these comparisons so it's worth
including multiple subword tokenizers
as you do a sweep
and then also uh larger and more diverse
data sets should be explored
particularly if you're going to explore
a byte level tokenizations um
and so i want to talk a bit about just

[00:10]
what i learned throughout the entire
scholars program um
so uh i come from engineering background
and not really research and so it was
really great for me to
learn how to identify and get the most
out of uh just reading papers
um that was like probably uh one of the
biggest takeaways for me is just
being able to take in a paper and uh i
didn't
identify what's useful there um i
learned just about building various
models and understanding what different
architectures are doing
um i'm i've always been interested in
just like software architecture
and architecture of models is a really
interesting place to explore
um so just learn all yeah just learned a
lot there
um i learned about getting your data
right and just how small issues and your
in your data can really blow up in a
deep network and you could kind of spend
some time trying to figure out what's
going wrong and it could just
be in your data um i was in a place
where my model was terrible and i
couldn't learn
um so i learned all about overfitting
and hyper parameter optimization
um there are a lot of little subtle
details and it's a really iterative

[00:11]
process where
maybe you're cheating a running race
scheduler you're
continuing your optimizers um just
really tweaking a lot of stuff
but when you really get it right you see
these exponential improvements and it's
really awesome
um i also learned about regularization
where your model is really
learning the training data but trying to
get your model to generalize
and learn something real um is like it's
huge
it's its own uh particular challenge and
um the last thing i want to talk about
was that i
just learned and thought a lot about the
implications of these generative models
um before i like joined i was really
excited about these generative models
and like just
super cool didn't really think about
like the implications of
releasing them um but just being open ai
and um
talking to people and just reading a lot
about this it kind of gave me this
perspective of really thinking about
what the
what are the implications of the models
we create and their impact on
like society and democracy um so that
was really great
um yeah that was um yeah

[00:12]
that was a lot um but i want to thank uh
i want to thank you guys for listening
i want to thank my mentor arvind um just
he was super helpful
for all this i was very patient and gave
such great insights
um and i want to thank my fellow
scholars for just being here with me
um so with that uh let's dive into
q a
um
okay um those size vocabulary for the
different organization schemes
um so
um for the
um for the word uh so the tokenizers
were pre-trained um
and they learned the vocabulary uh
as they went through uh the pre-training
so for the word tokenization um pinch

[00:13]
rebank had about ten thousand
vocabulary words uh the sub-word
tokenization
had 40 000 vocabulary words and the
uh character tokenization actually had a
much smaller vocabulary
um because it was they only learned the
unique characters
um so the character vocabulary uh
was i think about i think it was over
50 characters i don't know the exact
number
um uh how does
exploring tokenizations relate to
multimodal models
um well
um i guess to share that um
sorry um so uh
i wanted to um i guess i set out to do a
scaling law suite
and to look at uh these different
tokenizations and how they scale
um and this was so that i could then
maybe learn the segmentations
um and then see how learning and
segmentation improve

[00:14]
the model um
so by learning the segmentations
um in in text i thought there may be
some insights
in learning the segmentations and um
in other modalities um there's previous
research that suggests
uh if you learn the segmentations you
can really improve your performance
um so like multi multilingual
translations um seem to be improved by
uh learning and segmentation so going
from english or spanish to japanese
outperform english to japanese or
spanish to japanese if you learn the
segmentation
um so i was really interested in
learning segmentation but i first wanted
to kind of get a baseline
of what the current tokenizations did so
that's kind of the
projecting my project
see think i'm at time

[00:15]
um but
yeah um if anyone wants to reach out to
me um uh feel free
to reach out to me over email um and
yeah with that
i would like to introduce showa and

</details>

<!-- source: https://developers.openai.com/cookbook/examples/vector_databases/pinecone/gen_qa/ -->

## Search the cookbook

Feb 7, 2023

# Retrieval augmented generative question answering with Pinecone

This recipe is archived and may reference outdated models or APIs.

[JA](https://github.com/jamescalam)

[jamescalam](https://github.com/jamescalam)

[View on GitHub](https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/pinecone/Gen_QA.ipynb) [Download raw](https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/vector_databases/pinecone/Gen_QA.ipynb)

#### Fixing LLMs that Hallucinate

In this notebook we will learn how to query relevant contexts to our queries from Pinecone, and pass these to a generative OpenAI model to generate an answer backed by real data sources.

A common problem with using GPT-3 to factually answer questions is that GPT-3 can sometimes make things up. The GPT models have a broad range of general knowledge, but this does not necessarily apply to more specific information. For that we use the Pinecone vector database as our *“external knowledge base”* — like *long-term memory* for GPT-3.

Required installs for this notebook are:

!pip install -qU openai pinecone-client datasets

[?25l     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/55.3 KB[0m [31m?[0m eta [36m-:--:--[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m55.3/55.3 KB[0m [31m1.7 MB/s[0m eta [36m0:00:00[0m
[?25h  Installing build dependencies ... [?25l[?25hdone
  Getting requirements to build wheel ... [?25l[?25hdone
  Preparing metadata (pyproject.toml) ... [?25l[?25hdone
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m170.6/170.6 KB[0m [31m13.7 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m452.9/452.9 KB[0m [31m30.4 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m58.3/58.3 KB[0m [31m6.8 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m213.0/213.0 KB[0m [31m17.3 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m132.0/132.0 KB[0m [31m13.7 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m182.4/182.4 KB[0m [31m18.6 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m140.6/140.6 KB[0m [31m6.7 MB/s[0m eta [36m0:00:00[0m
[?25h  Building wheel for openai (pyproject.toml) ... [?25l[?25hdone

import openai

# get API key from top-right dropdown on OpenAI website
openai.api_key = "OPENAI_API_KEY"

For many questions *state-of-the-art (SOTA)* LLMs are more than capable of answering correctly.

query = "who was the 12th person on the moon and when did they land?"

# now query `gpt-3.5-turbo-instruct` WITHOUT context
res = openai.Completion.create(
    engine='gpt-3.5-turbo-instruct',
    prompt=query,
    temperature=0,
    max_tokens=400,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None

res['choices'][0]['text'].strip()

'The 12th person on the moon was Harrison Schmitt, and he landed on December 11, 1972.'

However, that isn’t always the case. First let’s first rewrite the above into a simple function so we’re not rewriting this every time.

def complete(prompt):
    res = openai.Completion.create(
        engine='gpt-3.5-turbo-instruct',
        prompt=prompt,
        temperature=0,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    return res['choices'][0]['text'].strip()

Now let’s ask a more specific question about training a type of transformer model called a *sentence transformer*. The ideal answer we’d be looking for is *“Multiple Negatives Ranking (MNR) loss”*.

Don’t worry if this is a new term to you, it isn’t required to understand what we’re doing or demoing here.

query = (
    "Which training method should I use for sentence transformers when " +
    "I only have pairs of related sentences?"

complete(query)

'If you only have pairs of related sentences, then the best training method to use for sentence transformers is the supervised learning approach. This approach involves providing the model with labeled data, such as pairs of related sentences, and then training the model to learn the relationships between the sentences. This approach is often used for tasks such as natural language inference, semantic similarity, and paraphrase identification.'

One of the common answers we get to this is:

The best training method to use for fine-tuning a pre-trained model with sentence transformers is the Masked Language Model (MLM) training. MLM training involves randomly masking some of the words in a sentence and then training the model to predict the masked words. This helps the model to learn the context of the sentence and better understand the relationships between words.

This answer seems pretty convincing right? Yet, it’s wrong. MLM is typically used in the pretraining step of a transformer model but *“cannot”* be used to fine-tune a sentence-transformer, and has nothing to do with having *“pairs of related sentences”*.

An alternative answer we receive (and the one we returned above) is about `supervised learning approach` being the most suitable. This is completely true, but it’s not specific and doesn’t answer the question.

We have two options for enabling our LLM in understanding and correctly answering this question:

1. We fine-tune the LLM on text data covering the topic mentioned, likely on articles and papers talking about sentence transformers, semantic search training methods, etc.
2. We use **R**etrieval **A**ugmented **G**eneration (RAG), a technique that implements an information retrieval component to the generation process. Allowing us to retrieve relevant information and feed this information into the generation model as a *secondary* source of information.

We will demonstrate option **2**.

---

## Building a Knowledge Base

With option **2** the retrieval of relevant information requires an external *“Knowledge Base”*, a place where we can store and use to efficiently retrieve information. We can think of this as the external *long-term memory* of our LLM.

We will need to retrieve information that is semantically related to our queries, to do this we need to use *“dense vector embeddings”*. These can be thought of as numerical representations of the *meaning* behind our sentences.

To create these dense vectors we use the `text-embedding-3-small` model.

We have already authenticated our OpenAI connection, to create an embedding we just do:

embed_model = "text-embedding-ada-002"

res = openai.Embedding.create(
    input=[
        "Sample document text goes here",
        "there will be several phrases in each batch"
    ], engine=embed_model

In the response `res` we will find a JSON-like object containing our new embeddings within the `'data'` field.

res.keys()

dict_keys(['object', 'data', 'model', 'usage'])

Inside `'data'` we will find two records, one for each of the two sentences we just embedded. Each vector embedding contains `1536` dimensions (the output dimensionality of the `text-embedding-3-small` model.

len(res['data'])

len(res['data'][0]['embedding']), len(res['data'][1]['embedding'])

(1536, 1536)

We will apply this same embedding logic to a dataset containing information relevant to our query (and many other queries on the topics of ML and AI).

### Data Preparation

The dataset we will be using is the `jamescalam/youtube-transcriptions` from Hugging Face *Datasets*. It contains transcribed audio from several ML and tech YouTube channels. We download it with:

from datasets import load_dataset

data = load_dataset('jamescalam/youtube-transcriptions', split='train')
data

Using custom data configuration jamescalam--youtube-transcriptions-6a482f3df0aedcdb
Reusing dataset json (/Users/jamesbriggs/.cache/huggingface/datasets/jamescalam___json/jamescalam--youtube-transcriptions-6a482f3df0aedcdb/0.0.0/ac0ca5f5289a6cf108e706efcf040422dbbfa8e658dee6a819f20d76bb84d26b)

Dataset({
    features: ['title', 'published', 'url', 'video_id', 'channel_id', 'id', 'text', 'start', 'end'],
    num_rows: 208619
})

data[0]

{'title': 'Training and Testing an Italian BERT - Transformers From Scratch #4',
 'published': '2021-07-06 13:00:03 UTC',
 'url': 'https://youtu.be/35Pdoyi6ZoQ',

<!-- yt-inline:35Pdoyi6ZoQ -->
[![Training and Testing an Italian BERT - Transformers From Scratch #4](https://img.youtube.com/vi/35Pdoyi6ZoQ/hqdefault.jpg)](https://www.youtube.com/watch?v=35Pdoyi6ZoQ)

<details>
<summary>자막: Training and Testing an Italian BERT - Transformers From Scratch #4 (30:38)</summary>

[00:00]
hi welcome to the video so
this is the fourth video
in a transformers from scratch mini
series
so if you haven't been following along
we've essentially covered what you can
see on the screen so
we got some data we built a tokenizer
with it
and then we've set up our input pipeline
ready to begin
actually training our model which is
what we're going to cover in this
video so let's move
over to the code and we see here that
we have essentially everything we've
done so far so
we've built our
input data our input pipeline and we're
now at a point where we
have a data loader pi torch data loader
ready
and we can begin training a model with
it so there are
a few things to be aware of so

[00:01]
i mean first let's just have a quick
look at the structure
of our data so when we're training
a model for mass language modeling
we need a few a few tensors we need we
need three
tensors and this is for training roberta
by the way as well
same thing with as well we have our
empire ids attention mask and our labels
our input ids have roughly 15
of their values mass so we can see that
here we have these two tensors
these are the labels and we have the
real tokens in here
the token ids and then in our input ids
tensor we have these have been replaced
with
master tokens number fours so
that's the structure of our input data
we've
created a torch data set from it
and use that to create a torch data

[00:02]
loader
and with that we can we can actually
begin
setting up our model for training so
there are a few a few things uh to that
we can't just begin training
straight away so the first thing that we
need to do is
create a roberta config object
and this is the config object is
something that we use when we're
initializing a
transformer from scratch in order to
initialize it with a
certain set of parameters so
we'll do that first so we want from
transformers
import roberta config
okay and to create that config
object we do this so
we do revert to config and then
in here we need to specify
different parameters now the
one of the main ones is the vocab size

[00:03]
now
this needs to match to whichever vocab
size
we have already created
in our tokenizer when correct building
our tokenizers so
i mean for me if i go all the way up
here
[Music]
to to here this is where i created the
tokenizer
i can see okay it's this number here so
522 so i'm going to
set that but if we
if you don't have that you can just
write tokenizer
vocab size so here
and that will return your your focus so
i mean let's let's replace that
we'll do this now
as well as that we want to also set this
so
max position embedding
and this needs to be set to your

[00:04]
max length plus two in this case so
uh max length is is set up here
so where where is it match left here 512
plus two because we have these added
special tokens
if we don't do that we'll end up with a
index error because we're going beyond
the embedding limits
then we want our hidden size so this is
the size of the vectors that
our embedding layers within roberto will
create so
each token so we have 514 or 12 tokens
and each one of those will be assigned a
vector of size
768 this is the typical number so
that's the originally came from the bert
based model
then we set up the the architecture of
the the internals of the model so we

[00:05]
want the
number of attention heads which i'm
going to set to 12
and also the number of
hidden layers which i
so the default for this is for roberta
12 but i'm going to go with six
for the sake of keeping training times a
little shorter
and then we also need to add type vocab
size which is just one
so that's the the different token types
that we have
we just have one don't need to don't
need to worry about that
okay so that's our configuration object
ready and we can import and initialize a
roberta model with that so we want
from transformers this is kind of
similar to what we
usually do import roberta
and we're doing this for mass lm so mlm

[00:06]
right so we're training using mlm
so we want robotic for mass lm and we
initialize our model
using that roberto for mass lm object
and we just pass in our config and
this will that's right there is
initialize our
roberto model so that's a plain roberta
model
randomly initialize weights and and so
on and
now we can move on to setting up
everything for for training so we have
our model now we need to
prepare a few things before we train it
first thing is we need to
decide which device we're going to be
training on so whether that's
cpu or a cuda enabled gpu and to
figure out if we have that we write well
we
can write torch cuda is available
so we write this and for me it is so

[00:07]
the typical way that you would you would
decide whether you're using
uh cuda or cpu or the typical line of
code that will
decide it for you is the right device
and you do torch dot cuda
or device sorry
and then your iq inside here if
it's available otherwise we are going to
use
torch device cpu
now cpu
takes yeah it's just it takes a really
long time so
if you are using cpu um
now you have to leave it overnight for
sure
maybe even longer even if it's just like
a little bit of data
it takes so long um so
but hopefully hopefully you have a gpu
if not just
you're gonna have to be patient that's
all
or if you could maybe try and use google

[00:08]
colab
but you have to use the premium version
because otherwise it's just going to
shut off after like an hour or two i
don't know i don't really use it so i
don't know how long it will it would
train for before just
deciding it's uh it's done and the gpu
is also not that
good anyway so yeah
however however you can however you can
do it
and then after that we want to move our
model to
our device so
whether it's gpu or cpu we move over
there we're going to get
a really big output now so some model
so this is like the the structure of our
model so we can see a few interesting
things
we got uh roberta for mlm we have
the roberto model and then inside that
we have our embeddings
and then we have our 12 did i say 12
i think it was six six encoders
should be yeah so it goes up it goes

[00:09]
from zero to five star six
and then we have the the outputs here
and then our
final bit which is the language modeling
head the mlm head
so that's cool now we need our
optimizer so from transformers
import and w which is adam with
weight decay and
and what we're going to do is i'm just
going to activate the training mode of
our model it's going to give us loads of
output again
so just yeah you know maybe i can just
let's just remove that there we go
easier
and then our optimizer is going to be
adam w
we need to pass in our model parameters
and we need a learning rate so
from i mean i don't usually use roberta
but
looking online this looks like a
reasonable

[00:10]
learning rate i think you can go from
sort of here to
i think from what i remember down to
like here
that's the sort of typical range but
obviously it's going to depend on how
much data you have and
don't do that how much data you have and
loads of different
things right so
that's what i'm going to go with and
that should be pretty much it
so that's our sale now we're just going
to create our
training loop now for the training loop
we want to import tqdm so we can
see how far through we are
we're going to train for two epochs and
we're going to initialize our loop
object using tqdm
so dqdm
we have our data loader what is the name
of that data loader i'm not sure

[00:11]
let's data loader
cool data loader
and we set leave equals true
but i need that sorry i need that in the
same cell so four
batch in loop
and then here we you know run through
each of the steps that we're going to
perform for every single
training glute so the first thing we do
is initialize the gradient in our
optimizer so
zero grab so reason we do this is
after the first loop our optimizer is
going to be
assigned a set of gradients which you're
going to use to
optimize our model and on the next loop
we don't want
those residual gradients to still be
there in our optimizer we want to

[00:12]
essentially reset it for the next loop
so that's that's what we're doing here
then we want our our tensors so we have
input ids
and that is going to be batch input
ids and we also want to move that over
to our
our gpu or cpu if you're on if you're on
that
and this is pretty much the same for
how three so
mass labels
and this is just a tension mask okay so
we've extracted our tensors and we just
need to feed them into our model now
so we're going to get our outputs from
the model
which is model input ids
attention mask which is going to be
equal to mask
and our labels

[00:13]
equal to labels
so everything has been fed into our
model
we have our outputs now we need to
extract a few things
from the output so we well we need the
loss
so we write loss equals outputs dot loss
and from that we want to calculate
all of the different parameters in our
model we need to calculate the loss for
each one of those parameters so we do
this loss dot backwards to
back propagate through all of those
different values and get that loss
after we've done that we use our
optimizer
take a set and optimize all those
parameters based on
that that loss then that's everything we
need to train the model
and then just a few things so for the
progress bar i just want
a little bit of information there just
so i know what's going on
and that's right loop set description

[00:14]
and that's what i just want to print out
the epoch
so write that
and then i want to set the post fixed as
well so loop
dot set post fix
and here i just want to see lost so
we'll just do lost loss
item like that so
that should be everything yeah let's
let's run that see see what happens
hopefully it should work nope
didn't work okay
let's see
oh no it's a cuda error
so probably just need to refresh
everything i hate cuda errors one moment
okay so finally figure out took so long

[00:15]
so
if so a few tips anyway when you do get
a cuda error
switch your device to cpu and
then rerun everything and you should get
a more understandable error so if we
come down here i've changed its cpu
we see that we get an index error scroll
down
index out of range itself so the reason
for this
is so you you get this error
if you don't have the extra two tokens
onto the end of here but
you know we added them so i was pretty
confused about that
and then it took me a really long time
to realize that this argument is wrong
and there should be an s on the end so
that would seem that was the
error so yeah super
super cool that that that was literally
it it took
me so long to to figure that out
but now we have it that's good we need
to run

[00:16]
everything again so i'm just going to
run through everything remove
the remove this this cell here where i
change it to
cpu because i don't need it now
and just re-execute that
okay so we're back and we've finished
training our model now
now it has taken a long time this is a
is a few days later
um and i made a few changes during
training as well so
this definitely wasn't the cleanest
training process because i was kind of
updating parameters as it was going
along
so initially well first
we've trained for like three and a bit
epochs and i've trained on the full data
set as well
so
if i come up here i think do i print out
how much data it was
um

[00:17]
maybe in another file
so if we come down here so yeah there's
a lot more data here so
we have 200 no
20 let me think 2 million
okay so 2 million samples in that final
run
and initially when we when we started
training we started with
a learning rate of one e to the minus
five
now i looked into this a little bit and
it just was not
really moving and i'll show you in a
minute so i for the second epoch
i moved it down to one e to the minus
four
or moved it up sorry to one e to the
minus four
and that you know that mood started
moving things a lot quicker so that that
was good and then
in total like i said it was three and a
bit epochs
other than that i didn't really change
anything the only thing i did was i
trained like one epoch at a time because
i wanted to
see how you know how the results were

[00:18]
looking after each epoch
and that was quite interesting so let me
let me show you that
okay so this is after the first epoch so
okay we so here what i'm doing is i've
got this fill which is a pipeline
fill object and i'm entering ciao and
then putting in now mass
and then and i'm i'm i wanted to say
ciao come over right
in the middle i want that to predict
comey now
this is the after the first epoch and we
can see it's not
yeah it's it's just it's putting like
random
[Music]
random characters so question mark here
three dots here uh chao and chao again
here
kind of weird so yeah not
not the best right then we move on to
the
second epoch and it's getting it's just
well it's so rubbish
at least it's got words right so like
here we have a word
uh ciao kiva or chiva

[00:19]
okay ciao kiva
i don't know if that's the way i always
the c h in italian i always get messed
up
if there's any italians watching them
i'm sorry
um ciao
you know at least we're getting words
but none of these so it doesn't make any
sense
okay so no i'm still not good
now if we come across again so this is
this one yeah this one now we get it so
the
first the the rest of these are kind of
the rest of them are nonsense
okay so the the four here
ignore them however at the top we get
this
score of zero point three three and we
get ciao kamivas so that's what we
wanted so that's good
means it's working this was this was
after the third in a bit epoch
let me show you loss function as well
so this i know this is really messy

[00:20]
um so here we have our i don't know why
this one's so short actually
why is that one so short
hmm strange but maybe i didn't
yeah if the last one doesn't look like i
finished training for the full epoch so
i thought i did uh maybe something
happened i'm not sure
but fine uh that's is what it is that's
fine
so the first set of training i did was
it was here
and you see in the middle my my computer
went to sleep for a bit overnight
because it was just
so loud so i turned it off for a bit um
and then continue going down now this
first epoch is when we're at
one point or one e to the minus five and
then
here i was testing the one e to the
minus four and you can see straight away
it goes down
way quicker so it's like okay we're
gonna go with that
it's clearly a lot better and then

[00:21]
continued over here
next epoch and then find the final one
here which it didn't seem to change much
anyway but
um there was there was so pretty clear
difference
so that's the the loss over time
and yeah i mean we've seen the results
from that so
now we have that let's move on to
actually
uh testing the model so i'm going to
bring larry and i'm going to
just open the the file
okay so this is the the testing we're
going to do so we're using the
the file mask we've got this pipeline um
sorry film us i've got this pipeline
and we're just what i'm going to do is
just get lara to come in
and some italian sentences and just add
this random mass token in and
see if the results are bearable or not
so
let's see um so i will see you in a
minute
this is lara she can speak italian so
she's going to
go through this and test it a few times

[00:22]
and
hopefully say it's good let's see
hopefully
ciao okay so all you need to do
is we have like a sentence here
and you just write some italian and then
for one of the words in there
we want to replace it with this text
here and then that's going to like
mask that word and then the model is
going to try and predict what is there
and hopefully we'll predict let's uh
let's see so just write some italian
phrases not
not too difficult yet and see
so i i don't have to write all bar
no no no no you right just write a
sentence and okay
maybe a few words there i'll just okay
can i put comma
or yeah

[00:23]
okay and then so which word should we
cover cornmeal
okay and then
okay so just cover it with the
mask and see what it says so not this
i seem to rerun these as well
okay let's give it a moment
yeah but the second one coming back it's
almost there does
kiva mean anything like who
yeah it's like like is there someone
but we like i understand because i'm
italian but i don't think that
um we don't usually say that
i don't think i'm gonna say that it's
fine i'm gonna say that as it's good

[00:24]
so let's do it again maybe yeah try
another one
oh wait actually what about these ones
no no no definitely not right no
[Music]
no no okay but it just like be after
bungiorno
i i wouldn't expect uh cuba
cuba it's okay
okay so you can just put another one
like where we put phil again
right in the sentence so we're here
yeah so we can ride
yeah um yeah and then what do you want
to replace
maybe as well okay
yeah so which one you decide it's fine

[00:25]
i think it's interesting okay let's try
it
yeah that's good
[Music]
yeah that's that's quite good yeah
that's cool okay
should we try with dober like using the
same phrase but
okay pink control z right
okay let's run it
in the second one

[00:26]
let's try another one yeah
um
[Music]
okay let's remove prepare
[Music]

[00:27]
grammatically difficult
when it's like that you know i don't i
don't know like
doesn't
that's very good no but it's good
because obvious cimo it's for
uh third person plural it's like we
had obviously is third person singular
so
if he had or she had yeah choosing

[00:28]
something
what does this actually mean so what
would have happened
if we had chosen another day
so the first one say
ave will be the third person
you will be the first person so if i had
chosen another day
say it's a second person plural
so it will be if they had choosing
another day
uh say they should th this one now
see how the dishes yeah this is good
seven is a shield as well
no maybe no no but the first three are
very good yeah
i have an idea so now if we change
to say so if we put
se loro so if we specify the person
maybe
we'll take the correct one so if we put

[00:29]
say loro and then we expect it to say
so let's run it
that's cool that's very good and then
the other ones
is right i mean the the
i'm saying well the the verb it's uh
incorrect but
yes and it's in the wrong place but it's
saying the right uh
like the meaning is correct yeah but the
grammar
it's not correct okay all right okay
yeah
oh it's cool you want something it
actually worked
because i wasn't sure if i could just um
wait worked a child coming back but that
was all i tested it with
so i was a little bit worried though it
might not
do anything else but thank you you're
welcome
thanks bye
okay so i think that's a
pretty good result so i mean

[00:30]
that's pretty much everything we we
needed for for building our
model our transform model although i do
want to so we're going to do one more
video after this
where we're going to upload
our model to the hooking face model hub
and then what we'll be able to do is
actually download it directly from
hogging face which i think will be
will be super cool to to do that and
figure out how we
actually put all that together so yeah i
think
good result pretty happy with that and
thank you for watching and i will see
you again in the next one

</details>

 'video_id': '35Pdoyi6ZoQ',
 'channel_id': 'UCv83tO5cePwHMt1952IVVHw',
 'id': '35Pdoyi6ZoQ-t0.0',
 'text': 'Hi, welcome to the video.',
 'start': 0.0,
 'end': 9.36}

The dataset contains many small snippets of text data. We will need to merge many snippets from each video to create more substantial chunks of text that contain more information.

from tqdm.auto import tqdm

new_data = []

window = 20  # number of sentences to combine
stride = 4  # number of sentences to 'stride' over, used to create overlap

for i in tqdm(range(0, len(data), stride)):
    i_end = min(len(data)-1, i+window)
    if data[i]['title'] != data[i_end]['title']:
        # in this case we skip this entry as we have start/end of two videos
        continue
    text = ' '.join(data[i:i_end]['text'])
    # create the new merged dataset
    new_data.append({
        'start': data[i]['start'],
        'end': data[i_end]['end'],
        'title': data[i]['title'],
        'text': text,
        'id': data[i]['id'],
        'url': data[i]['url'],
        'published': data[i]['published'],
        'channel_id': data[i]['channel_id']
    })

  0%|          | 0/52155 [00:00<?, ?it/s]

new_data[0]

{'start': 0.0,
 'end': 74.12,
 'title': 'Training and Testing an Italian BERT - Transformers From Scratch #4',
 'text': "Hi, welcome to the video. So this is the fourth video in a Transformers from Scratch mini series. So if you haven't been following along, we've essentially covered what you can see on the screen. So we got some data. We built a tokenizer with it. And then we've set up our input pipeline ready to begin actually training our model, which is what we're going to cover in this video. So let's move over to the code. And we see here that we have essentially everything we've done so far. So we've built our input data, our input pipeline. And we're now at a point where we have a data loader, PyTorch data loader, ready. And we can begin training a model with it. So there are a few things to be aware of. So I mean, first, let's just have a quick look at the structure of our data.",
 'id': '35Pdoyi6ZoQ-t0.0',
 'url': 'https://youtu.be/35Pdoyi6ZoQ',
 'published': '2021-07-06 13:00:03 UTC',
 'channel_id': 'UCv83tO5cePwHMt1952IVVHw'}

Now we need a place to store these embeddings and enable a efficient *vector search* through them all. To do that we use **`Pinecone`**, we can get a [free API key](https://app.pinecone.io) and enter it below where we will initialize our connection to `Pinecone` and create a new index.

import pinecone

index_name = 'openai-youtube-transcriptions'

# initialize connection to pinecone (get API key at app.pinecone.io)
pinecone.init(
    api_key="PINECONE_API_KEY",
    environment="us-east1-gcp"  # may be different, check at app.pinecone.io

# check if index already exists (it shouldn't if this is first time)
if index_name not in pinecone.list_indexes():
    # if does not exist, create index
    pinecone.create_index(
        index_name,
        dimension=len(res['data'][0]['embedding']),
        metric='cosine',
        metadata_config={'indexed': ['channel_id', 'published']}
# connect to index
index = pinecone.Index(index_name)
# view index stats
index.describe_index_stats()

{'dimension': 1536,
 'index_fullness': 0.0,
 'namespaces': {},
 'total_vector_count': 0}

We can see the index is currently empty with a `total_vector_count` of `0`. We can begin populating it with OpenAI `text-embedding-3-small` built embeddings like so:

from tqdm.auto import tqdm
from time import sleep

batch_size = 100  # how many embeddings we create and insert at once

for i in tqdm(range(0, len(new_data), batch_size)):
    # find end of batch
    i_end = min(len(new_data), i+batch_size)
    meta_batch = new_data[i:i_end]
    # get ids
    ids_batch = [x['id'] for x in meta_batch]
    # get texts to encode
    texts = [x['text'] for x in meta_batch]
    # create embeddings (try-except added to avoid RateLimitError)
    done = False
    while not done:
        try:
            res = openai.Embedding.create(input=texts, engine=embed_model)
            done = True
        except:
            sleep(5)
    embeds = [record['embedding'] for record in res['data']]
    # cleanup metadata
    meta_batch = [{
        'start': x['start'],
        'end': x['end'],
        'title': x['title'],
        'text': x['text'],
        'url': x['url'],
        'published': x['published'],
        'channel_id': x['channel_id']
    } for x in meta_batch]
    to_upsert = list(zip(ids_batch, embeds, meta_batch))
    # upsert to Pinecone
    index.upsert(vectors=to_upsert)

  0%|          | 0/487 [00:00<?, ?it/s]

Now we search, for this we need to create a *query vector* `xq`:

res = openai.Embedding.create(
    input=[query],
    engine=embed_model

# retrieve from Pinecone
xq = res['data'][0]['embedding']

# get relevant contexts (including the questions)
res = index.query(xq, top_k=2, include_metadata=True)

res

{'matches': [{'id': 'pNvujJ1XyeQ-t418.88',
              'metadata': {'channel_id': 'UCv83tO5cePwHMt1952IVVHw',
                           'end': 568.4,
                           'published': datetime.date(2021, 11, 24),
                           'start': 418.88,
                           'text': 'pairs of related sentences you can go '
                                   'ahead and actually try training or '
                                   'fine-tuning using NLI with multiple '
                                   "negative ranking loss. If you don't have "
                                   'that fine. Another option is that you have '
                                   'a semantic textual similarity data set or '
                                   'STS and what this is is you have so you '
                                   'have sentence A here, sentence B here and '
                                   'then you have a score from from 0 to 1 '
                                   'that tells you the similarity between '
                                   'those two scores and you would train this '
                                   'using something like cosine similarity '
                                   "loss. Now if that's not an option and your "
                                   'focus or use case is on building a '
                                   'sentence transformer for another language '
                                   'where there is no current sentence '
                                   'transformer you can use multilingual '
                                   'parallel data. So what I mean by that is '
                                   'so parallel data just means translation '
                                   'pairs so if you have for example a English '
                                   'sentence and then you have another '
                                   'language here so it can it can be anything '
                                   "I'm just going to put XX and that XX is "
                                   'your target language you can fine-tune a '
                                   'model using something called multilingual '
                                   'knowledge distillation and what that does '
                                   'is takes a monolingual model for example '
                                   'in English and using those translation '
                                   'pairs it distills the knowledge the '
                                   'semantic similarity knowledge from that '
                                   'monolingual English model into a '
                                   'multilingual model which can handle both '
                                   'English and your target language. So '
                                   "they're three options quite popular very "
                                   'common that you can go for and as a '
                                   'supervised methods the chances are that '
                                   'probably going to outperform anything you '
                                   'do with unsupervised training at least for '
                                   'now. So if none of those sound like '
                                   'something',
                           'title': 'Today Unsupervised Sentence Transformers, '
                                    'Tomorrow Skynet (how TSDAE works)',
                           'url': 'https://youtu.be/pNvujJ1XyeQ'},

<!-- yt-inline:pNvujJ1XyeQ -->
[![Today Unsupervised Sentence Transformers, Tomorrow Skynet (how TSDAE works)](https://img.youtube.com/vi/pNvujJ1XyeQ/hqdefault.jpg)](https://www.youtube.com/watch?v=pNvujJ1XyeQ)

<details>
<summary>자막: Today Unsupervised Sentence Transformers, Tomorrow Skynet (how TSDAE works) (44:21)</summary>

[00:00]
in this video we're going to have a look
at how we can train sentence
transformers
without needing any labeled data so if
you're new to
sentence transformers sentence
embeddings or vectors
a sentence vector as we'll call it is
simply a numerical representation
of a sentence or paragraph if you think
about language it's
a very human centric concept it's not
built for computers so computers really
struggle
to get the meaning
or concepts that we
as humans find very easy to communicate
using language
now the modernist computers appeared
during and around world war ii
the first application of nlp came soon
after in 1954 with the georgetown
machine translation experiment
in that first decade of research

[00:01]
those involved were pretty optimistic
that they were going to solve the
problem with machine translation in just
a few short years obviously they were a
little bit optimistic and
[Music]
that's still a problem that's still not
solved we still haven't solved machine
translation and the same goes for
anything in nlp but
in the past
decade especially
there have been
a lot of breakthroughs the the field of
nlp has progressed at an incredible rate
in
just the past decade
and we now have
an
incredible ecosystem of language models
and techniques that we can use for a lot
of different use cases now
a lot of this recent success is in part
thanks to the dense vector
representations
of
language so those are

[00:02]
vectors so numerical vectors that a
machine can understand
but are built in such a way that they
actually provide a numerical
representation
of the semantic sort of meaning behind
whatever is those vectors represent
whether that be tokens words or
sentences paragraphs and so on so and
with those dense vectors we
now have
a way for computers to comprehend and
understand
to an extent
the semantic meaning behind language
to build those
you know given a lot of data and a lot
of compute
we
tend to use transform models in nlp
transformers are the de facto standard
and for building representations of
sentences or paragraphs
there is a
subcategory of transformers called
sentence transformers now the training

[00:03]
process to
build a transformer
begins
with something called pre-training
that produces a generic transform model
and then we
fine-tune that so we train that further
using
special methods to build
sentence transformers that can produce
these very
information rich and accurate
sentence vectors
now
where is pre-training
tends to use unsupervised training
methods
fine-tuning
tends to be
more along the lines of supervised
training
and what that means is that we need a
lot of labeled data and for some domains
and languages
there simply
is not enough labeled data out there to
actually build
a sentence transformer
for those specific domains or languages

[00:04]
so that means that
you can always spend a long time
gathering data and labeling all the data
to get tens of thousands of
labeled samples or you can go ahead and
try fine-tuning model using unsupervised
training now unsupervised training i
will tell you straight away it's not
going to get you the performance that
you would get from a supervised training
approach however if you do not have the
label data to train
using a supervised approach one
supervisor training is your best bet and
it still works pretty well
so in this video
that's what we're going to cover we're
going to cover how we can train a
sentence transform or fine-tune sentence
transformer
using a unsupervised
training method called transformer base
sequential denoising auto encoder so

[00:05]
what we'll do is is jump straight into
it
and take a look at
where we might want to use this training
approach and and how we can actually
implement it
so the first question we need to ask is
do we really need to
resort to unsupervised training
now
what we're going to do here is just have
a look at the a few the most popular
training approaches and what sort of
data we need for that so the first one
we're looking at here
is natural language inference
or nli
and nli requires that we have
pairs of sentences
that are labeled as either
contradictory
neutral which means they're
not necessarily related
or
as entailing or
as inferring each other so you have
you have pairs

[00:06]
that entail each other
so they are both very similar
pairs that are neutral
and also pairs
that are contradictory
and this is the traditional nli data now
using a another version of
fine tuning with with nli
called
a multiple
negatives ranking loss
uh you can get by with
only entailment pairs so pairs that are
related to each other
or positive pairs
and
it can also use contradictory pairs to
improve the performance of training as
well
but you don't need it so if you have
positive pairs of

[00:07]
related sentences
you can go ahead and actually try
training or fine-tuning using an ally
with with multiple native ranking loss
if you don't have that
fine
another option is that you have a
semantic textual similarity okay cell
sts
and what this is is you have so you have
sentence a here
sentence b here
and then you have a score from from zero
to one
that tells you the similarity between
those two scores
and you would train this using something
like
cosine similarity loss
now if that's not an option
and your your focus or use case is on
building a
sentence transformer for another
language where there is no current
sentence transformer
you can use multilingual parallel data

[00:08]
so what i mean by that is so parallel
data just means translation pairs so if
you have for example a english sentence
and then you have
another language here so it can it can
be anything i'm just going to put xx
and that xx is your target language you
can fine-tune a model using something
called
multilingual
knowledge
and distillation
and what that does it takes a
monolingual model for example in english
and using those translation pairs it
distills the knowledge the
semantic similarity knowledge from that
monolingual english model
into a multilingual model
which can handle both english and your
your target language so
there are
three options
uh that are quite popular very common

[00:09]
that you can go for
and as a supervised methods the chances
are they're probably going to
outperform anything you do with
unsupervised training at least for now
so
if none of those sound like something
you can do the data sets or
if
it sounds like you probably can't get
data that seems like that and it doesn't
match your use case
then we would have to move on to
unsupervised training
so
like like i've written here you want to
go for unsupervised if you have little
to no data
in your unique domain or your low
resource language and
with low resource language you also have
no translation data so from a
from a source language like english
or you can use other languages as well
just as long as there's a monolingual
model in that source language to your
target language

[00:10]
so if you if we can't do that we move on
to unsupervised
learning and one of the the best
approaches at the moment is this
transformer based and sequential
denoising auto encoder now there are
other approaches as well but we're not
going to cover those and i think for now
this is probably your best bet although
there is
other methods being researched that do
look quite promising as well
so
the way that the tsje works is
if you have let's say you have a
sentence here
what you do is you take your sentence
and
you corrupt that data so
so we have this
and what we're going to do is just kind
of remove parts of that or we'll modify
it in a different way and and
do some other things to it so it's
slightly different
but not too different that it should not
be similar

[00:11]
and we take both of these so we take the
modified input
and we feed it into
our encoder model so our transformer
our transformer outputs a set of tokens
and we use some sort of pooling method
to convert those
into a single sentence vector
so
with that sentence vector we process
that through another model here which is
a decoder model
so it goes into decoder model and what
that decoder model must do
is actually optimize
to produce a
sentence here to produce the same text
so it has to
try and predict
this original sentence
and these weights
in the decoder and encoder are

[00:12]
optimized
in order for the decoder to be able to
actually do that
and that is the that is tsdae it's not
particularly
complex when you sort of look at a very
high level
and it's certainly a very intelligent
way of
building a sentence transformer without
any label data
now let's have a look a little
graphic here to compare
ts dei to
mlm now
mlm is mass language modeling and that
is a pre-training approach that a few of
you will probably be familiar with and
that's why i wanted to include this
comparison in here
so
with mlm which is the
bottom down here
we
take some input text and we mask one of
the tokens in in that text

[00:13]
we pass it through an encoder which
outputs all these token vectors and and
basically these token vectors for every
every word almost every word or subword
here
will be represented by one of these
token vectors or token embeddings all
those are passed into the decoder and
the decoder attempts to
predict
which word
or token
is behind that must token here
so it's trying to optimize for that mass
to become elephant
and and that's how you pre-train a
transformer or one of the ways that you
can pre-train the transformer
ts dae is is different
for quite a few reasons but the i think
the main
reasons you
you can think of
is
one we are not necessarily masking the
input
and it was found that the the best way

[00:14]
or the best approach is to actually
delete
the the token so you see here we we
should have that mask here but it's not
there anymore we just removed it
so one re delete rather than mask
although in the
in the tse dae paper they did test both
we have an encoder as before
but that is followed by this pooling
step and
this pooling step takes the token
vectors that we we see down here
and it converts them into a single
sentence vector
so
that sentence effect is passed on to the
decoder so if you compare both of these
steps here
these two
the decoder in mass language modeling is
getting a lot more information it's
getting token level
information whereas the decoder in
dealing with a lot less data and it's
dealing with sentence level information

[00:15]
rather than token level information
and it is then optimizing for the same
thing to try and predict
that
we should have this text here with
elephant rather than the missing
or corrupted text that was input into
the encoder initially
so that's the main difference between
both of those
now
in the
in the ts
d a paper
uh from wang reimers and grovitch
they tested
different approaches to to
fine-tuning
so the first of those is
the noise types so
when we take that original text and we
corrupt it
what is the best approach in you know
how do we how do we corrupt it and they
found that deleting tokens so
this box here

[00:16]
produces the best results
other options you could you can swap
tokens
so sort one word for another you can
mask as we saw with mass language
modeling can replace those tokens you
can add new tokens
you do different things right
but the
by far the best
here
was to just delete the token
now there's also you know how many
tokens do you delete so going through
each token you assign a probability of
that token being deleted and that's what
we see here this noise ratio
so again best best approach there is 0.6
okay so
we're going through each
token and assigning probability of 60
that that token will be deleted
so you are removing quite a lot of data
and then we have the the pooling method
so the the little circle after the
after the encoder
and
the best or the highest performing

[00:17]
approach here was
was using mean pooling
okay
but to mean pool you have another step
of actually taking average across all
those word vectors or token vectors
whereas with
pooling you don't do that you just take
the cls token which is
a
it's a classified token
from from bert so
if you've seen it before it looks like
this
okay and then you have your other tokens
following it
so that
is the approach that they they stuck
with they they went and used deletion
only in in corrupting that data
ratio 6.0.6
with a probability of 60
and at the end they use cls pooling
you can use mean pooling as well or even
max it's up to you but
we later on we're going to stick with

[00:18]
with cls to follow along with the with
the paper
it's just a actually quick
explanation of cls and meme pooling if
you if it's new to you um so
we have our encoder we output loads of
token token vectors
see less pooling we just take that that
single
single vector and that creates that is
our sentence vector so we're not really
doing anything there we're just kind of
extracting that vector
whereas with mean balling we're taking
an average
over all of the output token vectors
to create our sentence vector
so i mean that's it for the
visual
explanation
so let's jump into
how actually build or fine tune
a model
using this approach
okay so
we have
here i'm just loading a data set so
we're using using cookie and face data
sets here if you if you haven't used it

[00:19]
before you you would want to pick
install
data sets
and
what we're doing is getting the oscat
data set oscar corpus which is basically
a massive multilingual corpus it has a
lot of different languages in there i
i'm sure not every single language but
if you can think of a language it's
probably in there
and
we're taking the english portion of that
just
so i can
actually read and understand things
and
we're taking the training data
okay and this is important so
the oscar data set or at least for
english
the size of that
is quite massive it's 1.8 terabytes of
data
if you don't include this streaming true
all that's going to download to your
computer and i assume you probably a lot
of us probably don't even have that much

[00:20]
memory available on our machines anyway
so it won't work
so you need to add streaming equals true
because what that will do is as we
request a sample from the data set it
will download it and pull it through for
us one at a time not full thing
so it's obviously a lot more efficient
it's not going to break our computer or
anything
now
because we're streaming it we have to
kind of iterate through it so if i want
to show you
part of that so i'm going to go for row
in oscar
print that row and just break
okay so we're just going to print the
first first
item there so we have these two
features id which is just an index id
value and we also have text
now in here we you can see quite a lot
so there's this text and it's
it's pretty long so there's there's
multiple paragraphs in there multiple
sentences

[00:21]
and
when we're training with tsd
we only want smallish sentences we just
want one sentence for each sample
so
we we need to split that we need to
split that up into
just sentences
so
to do that i'm going to import re
because i want to split
for
just
periods here full stops periods
and i also want to to split on new line
characters
and i want to remove spaces at the same
time so i just want to remove anything
that indicates that this is a new
sentence or paragraph and split based on
on that
character so i'm going to create
a regex re.compile
and
that is going to be any full stop
followed
by
a space
that's an optional thing so it doesn't
have to be space

[00:22]
and also
optionally followed by a new line
character okay so this is just going to
match any full stop
for sure and it will also allow for that
to be a space included in that and there
will allow that for that to include a
new line character as well
so that's gonna catch everything for us
and let's see
what that looks like so we
write splitter
dot split
and we'll go row so the row that will
just pull through
text
and
yeah
okay so now we see that we have all
these nice sentences rather than
just one massive
paragraph you see some here
are not very long and what we'll do is
we'll remove them later on
because they're not ready sentences
so
let's do that

[00:23]
i'm gonna
create a
a number here which is going to count a
number of sentences we
manage to
capture
so
in reality or at least in the
tsdae paper
they found that 10k is pretty much all
you need
and
you can sort of go up to 100k as well if
you want
so
we're going to we're going to go up to
100k we probably don't necessarily need
to probably say 10k maybe even lowest
and english is a probably a reasonably
easy one for this to to figure out so
you could possibly go even lower and
still get decent results
so that's that's one thing about ts dae
is that you need very little data which
is pretty cool especially when it's not
labeled so we have
sentences i'm going to create a list
and we're going to just iterate through
so for row
in oscar

[00:24]
we need to create our new sentences so
new sentences equals splitter.split
and that will be row
tapes like we did before
and we also want to say
we want to remove
a sentence so
say line
for
line
and sentence
if
sorry in new sentences
new sentences
if that line or the length of that line
is
less
than
no greater than
10.
okay so we're saying
we only want
to include strings that have a character
length of greater than 10 and we can
maybe
even increase that because if we look at
this
this is definitely more than 10 so
let's just go with 20 for now and and

[00:25]
see how that goes
now
there are new sentences from a single
sample and we want to extend our
sentences list
with those new sentences
so we just write send
new sentences
okay
and
like i said oscar is a massive data set
if we if we run through this
for the whole data set we're going to
end up with
a lot of sentences and we don't need
that many we're only 10 to 100 000
sentences so what i'm going to say is
number of sentences
is going to
be equal to
the length of new sentences
so the number of new sentences that
we've just added
we're going to add that onto new
uh num
number of sentences so
once that
exceeds

[00:26]
100k
then we want to break so we're going to
stop
uh it's numb sentence
okay
and with that we we should be able to
run that it should be quite quick
okay
pretty pretty nice and easy there
and the next step as we usually would
with
pie torch is
we want to put this data
into a dataset object and then we want
to load that dataset object into a data
loader
now
because we're doing this thing where we
corrupt our data by adding noise to it
we
either need to do that manually when
we're building our data set objects
or
what we can do is just use the sentence
transformers
denoising autoencoder dataset object

[00:27]
so to use that we just write from
sentence transformers
dot data sets
import
denoising
auto encoder data set
and we're also going to to create the
data loader now as well so as we usually
would in pytorch we'll just import that
as well so it's from
torch dot
data or utils
dot data
import
data loader
and we want to create our data set so
data set is equal
to denoising auto encoder data set and
we just pass our data into that
so
sentences
and
that is all we need for our data set so
from there we can create our our data

[00:28]
loader
so it's
loader equals
sorry data loader
and we pass in our data set and we also
want to say okay what are the batch set
what is the batch size and do we want to
shuffle the data
so for the batch size
we're going to put eight
we don't shuffle the data
shuffle is true and we also want to drop
the last patch because this will it
would not be the same
same batch size as the
rest of our batches or most likely will
not be
so we just drop it it's easier so we run
that so we now have that's how
data is prepared for
fine tuning
and we now need to move on to
the
final
preparation before we actually fine-tune
the model which is setting up the loss

[00:29]
function and the actual
training function itself
so
before we actually even do the loss
function we need to define the model
that we're going to be training so
we're going to be using
based on case from the hook and face
transformers library
and to initialize that or we will
initialize that through sensor
transformers so from sentence
transformers
import
from sentence transformer
and we also
also want
models
now the
dirt model is going to be
models.transformer
and then in here we just pass the name
based on case so this will
just download models directly from home
face
models repository as as we would with
the transformers library
so we want to write bert base

[00:30]
in case
and then we also need a
pooling layer so
right pooling
equals models dot
pooling
and
as we saw before when we were working
for everything we want to use
pooling using the cls or classifier
token
so
to do that
we will need to pass cls
in there but before we do that we also
actually need to
tell the pooling
layer
what number or what dimensionality
to expect from that vector
and to get that
i'll show you
we can just write bert equals get word
embedding dimension and we'll see seven
six eight but we will uh once it's
actually defined so let me put that in
there
so i'll add that in there
okay

[00:31]
run this you'll see in a sec
okay that's just initializing everything
and we have that 768
now what we have here are two separate
layers and we need to combine them very
full merging both into a single
sentence transform model so to do that
we want to write model equals this is
where sentence transformer part comes in
we have modules and that will be bet
followed by the pooling
layer
and then we can also print out the sort
of description
of that model as well
so we see we have transformer using the
model
and
we also see the pooling
we have the word embedded dimension and
we also have the pooling mode
cls token is true whereas the rest of
them before it's because we're not using
those pooling methods
now with the model defined we can
we can find our loss function so we
write from sentence transformers dot

[00:32]
losses
and we're going to import the denoising
auto and code loss
and we'll use that to define our loss
function so we just write denoising
autoencoder loss
and we pass in our model
so
it knows what to
what to actually optimize
and
we also need to
make sure that we tie the the encoder
and decoder
weight so we
add true in there
okay because we have that encode decode
and we're tying those weights together
because the performance is better we can
also set faults
but the performance will not be as it's
good
so
that is
everything we we can go ahead and
actually move on to this training
function so model.fit
so

[00:33]
what we're going to be doing here
is we write model.fit
and
if i just add a few points here so we're
going to be using adam optimizer
we are going to be using a learning rate
so lr
of
3e to -5
and
that learning rate is constant so
we're going to be using a
constant learning rate
so if you've watched through the last
videos we tend we have tended to use a
warm-up
before we actually move on to that
learning rate so we we warm up to our
learning rate
with this we're just going to constant
learning rate all the way through and
there's no also no
weight decay in there
so
model that fit we need to say
what are what are
our training objectives
so we we just write train
objectives

[00:34]
and then in there we pass a list and in
here we need pairs of
data loaders and the loss functions
we're going to use to optimize with that
data in our case we just have one of
these so it's just loader
the data and also loss
we're going to train for one epoch
that's the epoch sequence one we are
going to be using
the adam optimizer the default optimizer
here is a adam w or adam weight decay
optimizer
from the
transformers library
so if we want to use adam we just set
the weighted k to zero so we write
weight decay
equals zero
we also need to set a scheduler
so this is why
i mentioned before so scheduler
equals
constant
learning rate okay so we're not doing
any any warm-up we're just going with

[00:35]
the constant learning rate all the way
through and then we want to pass our
optimizer
parameters
so here we're just passing the learning
rate
nothing more so that is
three
three e to the minus five
and while training we're probably going
to want to see the
progress bar
so i'm going to set that equal to true
as well
now
after that
after we finish training you're probably
going to want to save the model
so
you can you can save that as
wherever you would like
so i'm going to write tsdae
but i'm going to
start running that and now i'm going to
stop it and i'm going because it takes a
it doesn't take long to be fair
with 100 000 samples this took 20
minutes
on a reasonably good
gpu so that's a rtx 3090 so it's

[00:36]
obviously a decent gpu but it's nothing
like it's like tesla or anything like
that
so
it is this is really quick
i was pretty impressed okay you can so
you can see that this is training so i'm
gonna do is pause that or stop that and
i'm gonna switch over to the other
notebook where i have that training
and the evaluation that i performed
afterwards we'll just run through really
quickly
okay so
we're here now
uh yep you can see everything is
the same as before
model save i'll say there and
oh there was one thing i i
did want to mention so if you do get an
error with an ltk
you just need to do this you just need
to
either pip install nltk if you haven't
already go installed and then you just
run this input and ltk
and that's going to download this punk
tokenizer which is used
in the
in the denoising

[00:37]
process so that when we're adding noise
and then and denoising and whatever else
it uses that tokenizer so that's why we
why we need that in there
so if you do
get that here
you just run that
so
after that we so we train the model and
we want to evaluate the performance of
the model because we want to see that
has actually worked
so
one benchmark that you probably see me
use a few times already
is the semantic textual similarity
benchmark or stsb
which again we use we can use home based
data sets to call that
so it's from the glue data set it's the
stsb part of that and we're going to
take the
validation split so we're not taking the
training data although we can if we want
because we haven't trained on that
just in case
and that contains one sentence two
sentence and a label
this label is a score so if you remember

[00:38]
earlier we were talking about scs
data that we can train using cosine
similarity loss
that this is the data that we would use
so we have that label score and in this
data set it ranges from zero to five we
want to normalize that from zero to one
so
that's what i'm doing here i'm using the
data sets map function and then a
lambda in here and we're just dividing
all those by
five mapping them all
from zero to one
then
we are reformatting that that benchmark
date stsb data
using the sentence transformers input
example class so we need this
because we're using the evaluators
from the section transformers library
later
so all we do there is we loop through
create a list
and we append input example
objects that contain

[00:39]
the the two sentences and the label so
the score
and then we initialize a similarity
evaluator
so we can see this is called
embedding similarity evaluator so that's
for this type of data
the scs data
and we're just passing all the samples
we have there and you can write csv if
you want but i'm not doing that because
i just want to see
the the score in here i don't really
need i don't want to see on the detail
as i just want to
to have a look at the overall score and
then we just evaluate the model so you
just pass the model to your evaluator
and
using the model that we we train with ts
dae
we get 0.75
which is the
speedman's coefficient so
basically saying how
where our model is scoring high
does that correlate to where the true
scores are high or the true labels are

[00:40]
high
and
0.75 means yes there is correlation
there's it's
reason it's pretty strong right it's
it's not the strongest we'll see in a
minute but it's it's pretty strong
so that's
a good score
and
we can see that it is working now if we
compare that to an untrained model so
what we had before before we actually
fine-tuned it with
ts die
so we scroll down
i've just reinitialized something here
the same model as before
and evaluated it scroll down a little
bit to find a score
and you see we get this like
0.32 which is obviously way lower and
yeah there's some correlation there but
it's not
not not great
so
die is
giving us pretty
good results i think like it is really
not bad
now

[00:41]
something we mentioned earlier is
yes tsdae works it's an unsupervised
method but the unsupervised method
is
or cannot really be compared to
supervised methods in terms of the the
performance that you you'll get from
your sensory transformer
and so i wanted to show you that here
so
first thing i've done it is taking the
original expert so the first
one
and
[Music]
okay we get 0.8 or 0.81 if you want to
round up
so
it's
about seven percent better than
than the other than the the
unsupervised method which
is a fair bit but it's it's not massive
so at least our one supervisor's model
is up there
in like a good area of performance it's
not best
but it does work
and as well in the paper they did

[00:42]
do better than this i think they got to
i think 78 maybe
so they they also did better than
what i got here anyway so you can
probably do better
and then i wanted to look at a more
advanced model one of the more recent
models at least uh like mpnet
so
the mp net model scored
pretty much 89 or 0.89
so we get okay result i would apprec i i
think pretty good result tsa
but obviously you can't compare it to
those unsupervised
models
now that's it for this video
i
think at least for me
this unsupervised approach to training
is
actually one of the coolest things
or at least one of the coolest
approaches to to training and building
models that i've seen in sentence
transformers
possibly only really paralleled

[00:43]
with
multi-lingual knowledge distillation for
training multilingual models
both of these together
for me i think are really incredible i
know this isn't like the the best
performance when you think about all of
the
low resource languages out there that
don't really have that much data they
just have one structured text dates like
this or the all the domains
very specific domains
where they just have loads of text data
but they don't have label data and they
can't afford to pay someone to go and
create all that data or don't have the
time to even
i think
this
is
a really cool method to actually be able
to
to use i mean you you don't really need
anything
so
for that reason i think this is really
cool and is definitely
one of
the
most interesting ways of training

[00:44]
in my opinion
just
training something without labeled data
that actually works pretty well
so yeah that's it for this video i i
hope it's been useful
and
thank you very much for watching and
i'll see you in the next one

</details>

              'score': 0.865277052,
              'sparseValues': {},
              'values': []},
             {'id': 'WS1uVMGhlWQ-t737.28',
              'metadata': {'channel_id': 'UCv83tO5cePwHMt1952IVVHw',
                           'end': 900.72,
                           'published': datetime.date(2021, 10, 20),
                           'start': 737.28,
                           'text': "were actually more accurate. So we can't "
                                   "really do that. We can't use this what is "
                                   'called a mean pooling approach. Or we '
                                   "can't use it in its current form. Now the "
                                   'solution to this problem was introduced by '
                                   'two people in 2019 Nils Reimers and Irenia '
                                   'Gurevich. They introduced what is the '
                                   'first sentence transformer or sentence '
                                   'BERT. And it was found that sentence BERT '
                                   'or S BERT outformed all of the previous '
                                   'Save the Art models on pretty much all '
                                   'benchmarks. Not all of them but most of '
                                   'them. And it did it in a very quick time. '
                                   'So if we compare it to BERT, if we wanted '
                                   'to find the most similar sentence pair '
                                   'from 10,000 sentences in that 2019 paper '
                                   'they found that with BERT that took 65 '
                                   'hours. With S BERT embeddings they could '
                                   'create all the embeddings in just around '
                                   'five seconds. And then they could compare '
                                   'all those with cosine similarity in 0.01 '
                                   "seconds. So it's a lot faster. We go from "
                                   '65 hours to just over five seconds which '
                                   'is I think pretty incredible. Now I think '
                                   "that's pretty much all the context we need "
                                   'behind sentence transformers. And what we '
                                   'do now is dive into a little bit of how '
                                   'they actually work. Now we said before we '
                                   'have the core transform models and what S '
                                   'BERT does is fine tunes on sentence pairs '
                                   'using what is called a Siamese '
                                   'architecture or Siamese network. What we '
                                   'mean by a Siamese network is that we have '
                                   'what we can see, what can view as two BERT '
                                   'models that are identical and the weights '
                                   'between those two models are tied. Now in '
                                   'reality when implementing this we just use '
                                   'a single BERT model. And what we do is we '
                                   'process one sentence, a sentence A through '
                                   'the model and then we process another '
                                   'sentence, sentence B through the model. '
                                   "And that's the sentence pair. So with our "
                                   'cross-linked we were processing the '
                                   'sentence pair together. We were putting '
                                   'them both together, processing them all at '
                                   'once. This time we process them '
                                   'separately. And during training what '
                                   'happens is the weights',
                           'title': 'Intro to Sentence Embeddings with '
                                    'Transformers',
                           'url': 'https://youtu.be/WS1uVMGhlWQ'},

<!-- yt-inline:WS1uVMGhlWQ -->
[![Intro to Sentence Embeddings with Transformers](https://img.youtube.com/vi/WS1uVMGhlWQ/hqdefault.jpg)](https://www.youtube.com/watch?v=WS1uVMGhlWQ)

<details>
<summary>자막: Intro to Sentence Embeddings with Transformers (31:05)</summary>

[00:00]
hi welcome to the video we're going to
explore
how we can use sentence transformers and
sentence embeddings
in nlp for
semantic similarity applications
now in in the video we're
going to have a quick recap on
transformers and where they came from so
we're going to have a quick look at
recurring neural networks and the
attention mechanism
and then we're going to move on to
trying to define you know what is the
difference between a transformer and a
sentence transformer and also
understanding okay why
are these embeddings that are produced
by transformers or sentence transformers
specifically so good
and at the end we're also going to go
through how we can implement our own
sentence transformers in python as well
so
i think
we should just jump straight into it
[Applause]
before we dive into sentence

[00:01]
transformers i think
it would make a lot of sense if we piece
together where transformers come from
with the intention of
trying to understand why we use
transformers now rather than some other
architecture and i think it's also very
important if we try and figure out the
difference between a transformer and a
sentence transformer as well so we're
going to start with recurrent neural
networks and more specifically i want to
have a look at machine translation so
machine translation use something called
a encode decoder network where you would
have a encoder which is a set of
well recurrent units usually something
like lstms or gurus
and
information
or that encoder would would encode some
sort of input text so in
let's say english it would encode that
english text into something called a
context vector and then this context
vector would be passed along to a

[00:02]
decoder network which again is just
another set
of lstm or grid units
and it would decode those into our
target language say like french or in
this case actually italian
that is how machine translation works
back with recurring neural networks
the only issue is that we're trying to
pass a lot of information through that
single point between the encoder and the
decoder
now
that creates what is called the
information bottleneck there's too much
information trying to be crammed through
that single one point
so
what they came up with is something
called the attention mechanism what the
attention mechanism does is for every
step or every uh token that is decoded
by our decoder that token is
sent to the attention mechanism and the
alignment between the decoder at that
time step is compared to

[00:03]
all of the encoder units or on all of
the encoder hidden states
and what that does is essentially builds
this type of attention so it tells the
decoder which tokens from the encoder to
focus on so it's literally saying you
know where do i need to pay attention to
whatever my current unit is and this
attention mechanism why produce it is
something
like this so this is from a another very
well known
paper in 2015 and what you can see is a
matrix of the we have the french
words or the french translation on the
on the left on the y axis and then on
the top we have the english translation
and
all of these boxes you see
are the activations of the attention
mechanism so we can see essentially
which words are the most aligned and

[00:04]
that is essentially what the attention
mechanism did it allowed the decoder to
focus on the most relevant words in the
decode in the encoder part of the
network now moving on in 2017 there was
a another paper called attention is all
you need and
this really marked i think
what is the turning point in nlp
what was found in this paper is that
they could remove the recurrent parts of
the encoder decoder network and maintain
just the attention mechanism and
what they produced with a few
modifications to the attention was a
high performing model than any of the
recurrent neural networks with attention
or without attention that came before it
and
what they named this new this new model
was a transformer
so
this is this 2017 paper attention is all
you need is where transformers came from

[00:05]
and
they actually came from a mechanism that
was aimed to help improve recurrent
neural networks
now of course like i said the attention
mechanism was not just a plain same
plain attention mechanism that was used
before
in recurrent neural networks it had been
modified a little bit as well and those
modifications really came down to
three key changes
and
those were positional encoding which
replaced the key advantage of recording
networks in nlp which was the ability to
consider the order of a sequence because
they were recurring your networks they
considered one word or one time set
after the other so there's a there is a
sense of order to those models that does
not appear in for example convolutional
neural networks and this positional
encoding worked by adding a set of
varying sine wave activations to each

[00:06]
input embedding and
these activations varied based on the
position of the word or token so
what you have there is a way for the
network to identify the order of the
tokens or the token activations or
embeddings that are being processed the
next change was self-attention
now self-attention is where the
attention mechanism is applied between a
word
and all of the other words in its own
context
so the sentence or the paragraph that it
belongs in now we saw with the encoder
decoder that attention was being applied
between the decoder and the encoder this
is like applying attention to the
encoder and the encoder again and what
this did is rather than just embedding
the meaning of a word it also embeds the
context of a word into its vector or
word representations

[00:07]
which obviously greatly enriched the
amount of information that you have
within that embedding
and then the the third and final change
that they made was the addition of
multi-head attention
and
we can see multi-header tension as
several parallel attention mechanisms
working together
and using these multiple attention heads
allowed the representation of several
sets of relationships rather than just a
single set now these new transform
models also had the benefit of
generalizing very well so what we found
with transformer models and of course
you could do this to an extent with your
current neural networks as well
but it was
far less effective
so with transformed models we take the
core of the model which is being trained
using a significant amount of time and
computing power by the likes of google

[00:08]
and openai
we we just take that core model add a
few layers onto the end of it that are
designed in a way for our specific use
case
and
train it a little bit more so we
fine-tune it
and
i think one of the most widely known of
these or very the most popular of these
models is probably bert and of course
there are other models as well later in
this video we're going to have a look at
one called the mp-net model
but there is is certainly one of the i
think most popular of those
now so far we've sort of explained that
transformers have a much richer
embeddings uh or word or token
embeddings than anything that came
before
and that's good but we're we're
interested in not word or token level
embeddings but sentence embeddings
because we
want to do a semantic similarity between

[00:09]
sentences or paragraphs
and
of course transformers they work the
inside of the transformer works based on
word level or token level embeddings so
that doesn't really help us that much
so what would happen before sentence
transformers were introduced is we would
use something called a cross encoder so
we would have a bert cross encoder model
and like i said before we have the
corbett model and then we just add a
couple of layers onto the end of it and
fine-tune it for our specific use case
and that's what cross-encoder is it's
the core
bert model
as you can see on the screen right now
it's a core birth model followed by a
feed forward neural network we pass two
sentences into the bert model at once
the birth model
embeds them with very rich
word and token level embeddings the
feedforward network takes those and

[00:10]
decides how similar those two sentences
are
now this is fine and it's actually
accurate it works well
but it's not really scalable because
essentially every time you want to
compare a pair of sentences you
have to run a full inference computation
on birds so let's say we wanted to
perform a semantic similarity search
across just 100 000 sentences which is
is a reasonably small data set we would
have to run
the
bert inference computation
100 000 times
to actually go through
and identify the similarity between all
of those sentences and that's going to
take a lot of time
and it gets worse as well i mean if you
consider clustering all of those 100
000 sentences
we would end up with just under 500
million comparisons there

[00:11]
so
running a full bert
inference prediction 500 million times
just to cluster 100 000 sentences
obviously that's not scalable that will
take a very very long time so ideally
what we need is something like word or
token embeddings but for sentences
now
with the original bert we we could
actually produce these they just were
not very good so what we could do is
take the
mean value
across all of our word embeddings that
typically burdens 512 those being output
by the model we take the average across
all of those and take that average as
what we call sentence embedding now
there were other methods of doing this
as well
that was probably the most popular and
effective one
and we could say that sentence embedding
saw it somewhere and then we could just
compare it to other sentence embeddings
using something that's a bit simpler
than a full bert um computation like

[00:12]
cosine similarity and
that is much faster that that's fast
enough uh for us but it's just not that
accurate and it was actually found that
comparing average average glove
embeddings which were produced in in
were
actually more accurate
so
we can't really do that we we can't use
this
what is called a mean pooling approach
or we can't use it in its current form
now the solution to this problem was
introduced by two people in in 2019
and nils reimers and irinha garewicz
they introduce what is the first
sentence transformer or sentence bert
and it's found a sentence bear or expert
outperformed all of the
previous save the art models
on pretty much all benchmarks not all of

[00:13]
them but but most of them
and it did it in a very
quick time
so if we compare it to bert
if we wanted to find the most similar
sentence pair from 10 000 sentences in
that 2019 paper they found that
with that took 65 hours
with esper embeddings they could create
all the embeddings in just around five
seconds
and then they could compare all those
with cosine similarity in 0.01 seconds
so
it's a lot faster we go from 65 hours to
just over five seconds which is
i think pretty incredible
now i think that's pretty much all the
context we need behind sentence
transformers and
what we'll do now is dive into a little
bit of how they actually work
now
we said before we have the core
transform models and what expert does is
fine tunes on sentence pairs using what

[00:14]
is called a siamese architecture or
siamese network
what we mean by a side news network
is that we have what we can see what can
view as
two bird models that are identical and
the weight between those two models are
tied now
in reality when we're implementing this
we just use a single bert model and what
we do is we
process one sentence a sentence a
through the model and then we process
another sentence sentence b through the
model and that's the sentence pair so
with our cross encoder we were
processing the sentence pair together we
were putting them both together pressing
them all at once this time we process
them separately and
during training what happens is the
weights with invert
are optimized to
reduce the difference between two vector
embeddings or two sentence embeddings
that are produced for sentence a and
sentence b

[00:15]
and those those sentence embeddings are
called u and v now to actually create
those sentences and buildings we do what
we did before with bert where we do the
mean pooling operation now the reason
that this works better is because we're
fine tuning it so with bear we didn't
fine tune it this time we are fine
tuning it now there are several
different ways of training experts but
the one that was covered most
prominently in the original paper is
called the softmax loss approach
and that's what we are going to be
describing here now for the softmax
loss approach
we can train on natural language
inference data sets
now the 2019 paper used two of those the
sanford natural language inference
corpus and the multi-genre natural
language inference corpus
now
both of these were merged together and
what we have inside there

[00:16]
are sentence pairs one is
a premise which suggests a certain
hypothesis so those two sentence pairs
are in some cases related
and we can tell whether they're related
or not using the label feature
now the label feature contains three
different classes we have zero which
is called entailment and
what this is is it indicates that the
premise
sentence suggests the hypothesis
sentence
then we have class one or label one that
means the two sentences are neutral so
they could both be true but they are not
necessarily related
and then we have number two which is
contradiction which means the premise
and hypothesis sentences contradict each
other
now given this data we we feed sentence
a into
bert first for our fine tuning

[00:17]
and then we feed sentence b into
bert so that's our premise and
hypothesis
the siamese bert or orbert
um outputs
two sentences are bendings u and v
from this process and what we do is
concatenate those two sentence
embeddings now the the paper explained a
few different ways of doing that but the
most effective
was take u and v and what we do is we
take the absolute value
of u
minus v which is an element-wise
operation so basically finding the
difference between u and v and that
produces this other vector which is the
bar u minus v bar
and then we concatenate all of those
together
so they all get concatenated together
and then they are passed
into a feed-forward neural network now

[00:18]
this feed forward neural network
takes the concatenated and vector length
or sentence embedding length as its
input
and outputs just three
activations now there's three
activations align with our three labels
so what we do from from there we have
those three activations we then need to
calculate the softmax loss between those
predicted labels and the true labels
now softmax loss is nothing more
than a cross-entropy loss function
and that's really all it is all there is
to to training one of these models now
we are going to cover all of this
uh in full we're gonna go through the
code and everything and train our own a
sentence better model
but for now we're just describing the
process and we'll cover that in another
well probably the next video and article
now
that's really i think everything
we need to know for now on on how they

[00:19]
work and where they are where sentence
transforms and transformers come from so
let's
jump into python and what we'll do is
actually implement some of these models
using the sentence transformers library
which which was built by the same people
who who
designed
the first sentence transformer experts
so let's go ahead and do that now
so the first thing that you will need to
do if you
do not already have sentence
transformers installed
is
just pip install sentence transformers
like so i already have it installed so
i'm not going to to go ahead and run
that
so all i'm going to do now is from
sentence transformers
i'm going to
import to the sentence transformer
class
object
and then from there we can initialize a
sentence transform it's super easy so
all we need to write is model

[00:20]
equals sentence transformer
and then in here we just need to
write our model name now
if you go to
this website
expert.net
you will find a load of different models
now the one that we will be using is
this so this is the original svet model
and if we just come down here and print
out what that will return to us
we will see a few different components
so you can see that we have well we have
two components we have the transform
model and we have the pooling
layer which is the mean pooling that i
mentioned before
now the transformer we see that the max
sequence amounts to the maximum number
of tokens that we can input there's 128
and you see that we're using
the base model is a bert model from the
hooking first hooking face library

[00:21]
then in
pooling we can see the output dimension
of our sentence vector which is
768 and we can also see the way that the
tokens have been pulled to create the
sentence and betting which is just the
amine pooling approach
now
given
these sentences here
i'm gonna run that
all we need to do to actually encode
those
is we write model.encode
and then we just press sentences
and they that will create our embeddings
so i'm just gonna call this embeddings
and let's see what they look like so
embedding this again
and we see that we have these which are
our embedding so each one of these
is for a single sentence so up here we
have the first sentence here
and
these are each of dimensionality 768.

[00:22]
so we can we can check the shape of that
if we want as well just to confirm that
that is true so you see that we have
five embeddings five sentences
each one 768 dimensions and now now that
we have our sentence embeddings
we can use these to quickly compare
sentence similarity for
quite a few different use cases
the most popular are somatic textual
similarity which is a comparison of
sentence pads which is what we are going
to do here
and
generally this is is probably most often
used for for benchmarking these kinds of
models
then we have semantic search now we've
covered semantic search a lot already
in in other articles and videos
and this is information retrieval using
semantic meaning
so given a set of sentences we can
search using a query sentence

[00:23]
and identify the most similar records so
this enables us to search
based on concepts rather than specific
words
which is is pretty cool and we also have
clustering so we can cluster our
sentences which is obviously useful for
things like topic modeling
now we can put together a very fast sts
and so the
semantic textual similarity example
using nothing more than a cosine
similarity function and numpy so we just
want to import numpy as np and we also
i'm going to use
the sentence transformers
cosine similarity function so write
cosine
so write sentence transformers util
import cosine
okay so from there what i'm going to do
is i'm going to initialize a empty array
of zeros
and i want that to be length first

[00:24]
sentences so i want it to be a five
by five array
and what we're going to do is is loop
through all of these sentence and
bearings that we produce from experts
and compare those with the cosine
similarity
so we just want to write for i in
range i'm going to let the sentences
and we just want to say
similarity function or similarity array
from
high
to the end
on this specific column
is going to equal to
cosine sim
and then here we want to put our
embeddings we just want the
the current position followed by
the other other embeddings
okay and that will populate our our
similarity array
so we can we print that out and we'll
see okay so down the middle here so i

[00:25]
i've not
populated these because
these um
well we've already got those pairs on on
this side of the
array you'll see we're going to
visualize it so you that'll probably
make more sense but let's do that now so
we're going to import
map plot lib not pie plot
that's plt and i'm also going to import
seaborn just makes it a little bit
easier and nicer as well and i'm just
going to write sns dot heat map
in here sim
and
we want annotations set to true
okay so this is just a visual that array
that we produced just now
and we can see here so we have the
sentence
um
values or sentence positions so sentence
zero if we go here actually let me print
them out here said that makes more sense

[00:26]
so if i print sentences
maybe it's very fine
so i'll put them like this yeah
so we have uh number zero is obviously
this first sentence
and then we have number one two three
and four
and that correlates to uh zero to four
and zero to four uh here on the other
two axes so if we want to look at the
most
uh similar pair according to our expert
model is this four and three which gets
a cosine similarity of 0.64
and if we have a look
three and four are these two so these
two are the only ones that kind of mean
the same thing and i've written
these
so that they
are basically they basically carry
or they share none of the same
descriptive words so for dentists we
have dental specialists

[00:27]
chewing bricks
i put flossing so not even the same
thing
and construction materials as well it's
not even the same thing there
but very similar uh sort of concepts
that we're talking about there so you
can see that it's identifying those two
as the most similar concept which is
pretty cool and then we get some other
uh similarity scores which are kind of
high here and they're not really related
so we have three and zero
let's talk about eggplants and mannequin
heads so it's pretty different i suppose
in reality someone being an eggplant and
this sort of thing is
both kind of like weird strange things
to happen so maybe that's why it's
capturing similarity there but
it's not obviously similar um
so generally i think it's good that it
identifies this as being the most
similar
but it could be better and
we do find that with the more recent
models it is in fact better
so what we can do is i'm going to get

[00:28]
this other model
and we just call it model
and we're going to do sentence
transformer again and this time we are
using the mpnet base model
now this is uh
basically the the highest performing
model
at the moment although i i was
uh told
on
on on the channel's discord by ashraq
that there is actually when they were
training this mp net model
they also trained a roberta model
and
if you although the robota model is not
shown on the sentence transformers home
page
you can see in the competition where
they train both these models that they
did also train that model
and it does have a slightly higher
performance as well it might be slower
i'm not sure probably because it's
roberta but the performance of that is
actually is actually higher than

[00:29]
the mp net version of that model which
is pretty cool
now
here we can see something or a few
things that's slightly different for
the match sequence length is three times
as long as it was with the bird model
using mp net base model
and we also have this additional
normalization function
now let's just take what we we wrote up
here so i'm just going to take this
bring it down here
and let's just use the heat map straight
away so sms heat
maps sim and
anat equals true
and we'll see something slightly
different or we should do um this isn't
so i haven't processed the similarity
yet
all the embeddings so it's right
embeddings equals
model dot encode sentences

[00:30]
now if we run it
we'll see that
the
similarity of these ones of these other
um sentence pairs is now a lot lower but
it's still identifying four and three is
pretty similar
so we can see straight away there's a
decent performance increase from from
this mp net model which is like their
most recent model
and the original esper model here
so i think that's pretty cool to see it
as well
now that's it for this model uh
introducing sentence embeddings and the
sentence transformers
library and models
now
going forwards obviously this is a
series of videos so we're going to be
covering a lot more than just sentence
transformers but
next we are actually going to cover how
we can train a
sentence bert model an esper model which
i think will be will be pretty cool
so
until then that that's it for now so

[00:31]
thank you very much for watching and i
will see you in the next one bye

</details>

              'score': 0.85855335,
              'sparseValues': {},
              'values': []}],
 'namespace': ''}

limit = 3750

def retrieve(query):
    res = openai.Embedding.create(
        input=[query],
        engine=embed_model

    # retrieve from Pinecone
    xq = res['data'][0]['embedding']

    # get relevant contexts
    res = index.query(xq, top_k=3, include_metadata=True)
    contexts = [
        x['metadata']['text'] for x in res['matches']
    ]

    # build our prompt with the retrieved contexts included
    prompt_start = (
        "Answer the question based on the context below.\n\n"+
        "Context:\n"
    prompt_end = (
        f"\n\nQuestion: {query}\nAnswer:"
    # append contexts until hitting limit
    for i in range(1, len(contexts)):
        if len("\n\n---\n\n".join(contexts[:i])) >= limit:
            prompt = (
                prompt_start +
                "\n\n---\n\n".join(contexts[:i-1]) +
                prompt_end
            break
        elif i == len(contexts)-1:
            prompt = (
                prompt_start +
                "\n\n---\n\n".join(contexts) +
                prompt_end
    return prompt

# first we retrieve relevant items from Pinecone
query_with_contexts = retrieve(query)
query_with_contexts

"Answer the question based on the context below.\n\nContext:\npairs of related sentences you can go ahead and actually try training or fine-tuning using NLI with multiple negative ranking loss. If you don't have that fine. Another option is that you have a semantic textual similarity data set or STS and what this is is you have so you have sentence A here, sentence B here and then you have a score from from 0 to 1 that tells you the similarity between those two scores and you would train this using something like cosine similarity loss. Now if that's not an option and your focus or use case is on building a sentence transformer for another language where there is no current sentence transformer you can use multilingual parallel data. So what I mean by that is so parallel data just means translation pairs so if you have for example a English sentence and then you have another language here so it can it can be anything I'm just going to put XX and that XX is your target language you can fine-tune a model using something called multilingual knowledge distillation and what that does is takes a monolingual model for example in English and using those translation pairs it distills the knowledge the semantic similarity knowledge from that monolingual English model into a multilingual model which can handle both English and your target language. So they're three options quite popular very common that you can go for and as a supervised methods the chances are that probably going to outperform anything you do with unsupervised training at least for now. So if none of those sound like something\n\n---\n\nwere actually more accurate. So we can't really do that. We can't use this what is called a mean pooling approach. Or we can't use it in its current form. Now the solution to this problem was introduced by two people in 2019 Nils Reimers and Irenia Gurevich. They introduced what is the first sentence transformer or sentence BERT. And it was found that sentence BERT or S BERT outformed all of the previous Save the Art models on pretty much all benchmarks. Not all of them but most of them. And it did it in a very quick time. So if we compare it to BERT, if we wanted to find the most similar sentence pair from 10,000 sentences in that 2019 paper they found that with BERT that took 65 hours. With S BERT embeddings they could create all the embeddings in just around five seconds. And then they could compare all those with cosine similarity in 0.01 seconds. So it's a lot faster. We go from 65 hours to just over five seconds which is I think pretty incredible. Now I think that's pretty much all the context we need behind sentence transformers. And what we do now is dive into a little bit of how they actually work. Now we said before we have the core transform models and what S BERT does is fine tunes on sentence pairs using what is called a Siamese architecture or Siamese network. What we mean by a Siamese network is that we have what we can see, what can view as two BERT models that are identical and the weights between those two models are tied. Now in reality when implementing this we just use a single BERT model. And what we do is we process one sentence, a sentence A through the model and then we process another sentence, sentence B through the model. And that's the sentence pair. So with our cross-linked we were processing the sentence pair together. We were putting them both together, processing them all at once. This time we process them separately. And during training what happens is the weights\n\n---\n\nTransformer-based Sequential Denoising Autoencoder. So what we'll do is jump straight into it and take a look at where we might want to use this training approach and and how we can actually implement it. So the first question we need to ask is do we really need to resort to unsupervised training? Now what we're going to do here is just have a look at a few of the most popular training approaches and what sort of data we need for that. So the first one we're looking at here is Natural Language Inference or NLI and NLI requires that we have pairs of sentences that are labeled as either contradictory, neutral which means they're not necessarily related or as entailing or as inferring each other. So you have pairs that entail each other so they are both very similar pairs that are neutral and also pairs that are contradictory. And this is the traditional NLI data. Now using another version of fine-tuning with NLI called a multiple negatives ranking loss you can get by with only entailment pairs so pairs that are related to each other or positive pairs and it can also use contradictory pairs to improve the performance of training as well but you don't need it. So if you have positive pairs of related sentences you can go ahead and actually try training or fine-tuning using NLI with multiple negative ranking loss. If you don't have that fine. Another option is that you have a semantic textual similarity data set or STS and what this is is you have so you have sentence A here, sentence B\n\nQuestion: Which training method should I use for sentence transformers when I only have pairs of related sentences?\nAnswer:"

# then we complete the context-infused query
complete(query_with_contexts)

'You should use Natural Language Inference (NLI) with multiple negative ranking loss.'

And we get a pretty great answer straight away, specifying to use *multiple-rankings loss* (also called *multiple negatives ranking loss*).

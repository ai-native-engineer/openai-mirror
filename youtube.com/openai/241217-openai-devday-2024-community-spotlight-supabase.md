---
title: "OpenAI DevDay 2024 | Community Spotlight | Supabase"
channel: openai
url: https://www.youtube.com/watch?v=0_sHinA0RV0
youtube_id: 0_sHinA0RV0
published: 2024-12-17
duration: "9:36"
captions: en-orig
---

# OpenAI DevDay 2024 | Community Spotlight | Supabase

[![OpenAI DevDay 2024 | Community Spotlight | Supabase](https://img.youtube.com/vi/0_sHinA0RV0/hqdefault.jpg)](https://www.youtube.com/watch?v=0_sHinA0RV0)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | Supabase (9:36)</summary>

[00:00]
thank you hi I'm Thor I work on
developer experience at superbase now
before we jump in can I get a quick show
of fans uh who your create software for
a
living okay a bunch of folks and uh keep
your hand up if you really enjoy writing
database
migrations yeah I thought so um and
that's exactly why we've created
database. built the AI powered postgress
playground in the
browser now you can think of it like jet
gpt's code interpreter but for postgress
giving an AI model full autonomy over
the database means that it can run
multiple operations backto back without
delay it makes AI feel even more
humanlike and
useful this novel experience is only
part possible thanks to gp4 O's

[00:01]
incredible understanding of postgress
and SQL paired with a disposable in
browser database so we don't have to
worry about data loss and we can just
let the model run wild so if you want to
play along you can just go to database.
build and um let's do some life demo
here uh I did some offerings to the demo
Gods earlier so let's track some movies
so we can just fire that off and we can
see now we're going to GPT 40 uh we're
getting some SQL we're running that SQL
and the SQL that we're getting back from
the model we're running it directly on
the database that is running in the
browser so this is using PG light um
which is running postgress in the
browser through WM uh and then we can
see here okay the movies table has been
created fantastic so that's it we got
our first migration uh in the

[00:02]
box now how are we able to give the
model so much autonomy and really the
secret Sauer is tool calling so we use
tool calls not only to execute SQL in PG
light but also to perform other actions
that you would normally only find kind
of in the graphical user interface okay
let's dive a bit deeper under the hood
to see kind of what's
Happening uh we're using the versel AI
SDK here here and it's been a great open
source tool to iterate quickly uh and
actually this is the new uh r.o open AI
theme uh I think it was released
yesterday so uh big shout out to Edwin
and the the ray team for making that uh
open so you can get some really nice
code screenshots
there and of course like the rest of
super Bays this is open source as well
so you can jump in and have a look uh
later
yourself but so this is where the magic

[00:03]
happens so on tool call provides the
client side tools that the model can
automatically invoke and Max steps
defines a limit in case we get kind of
stuck in an infinite
Loop so let's take the example of the
execute SQL tool call here um we set up
our tool call schema kind of using sort
uh in
typescript and then we have a use on
tool called hook which implements the
tool functionality so we sanitize the
response a bit and then return the query
results uh and the updated schema here
so let's step through our demo earlier
where we kind of said we want to track
some movies so initially we make an
artificial tool call uh to get the
database schema and share that as
context with um the model together with
kind of the users's message here uh
which just says track some movies

[00:04]
um and so in the response we get the
execute SQL tool call uh together with
our create table SQL which we then um
immediately kind of run on the database
so we're running that query client site
in the in browser database and then we
feed the query results and the updated
schema back to the model to generate
kind of the streaming response that we
saw here where it says the movies table
has been created and we render that to
the I and lastly um in a final step we
asked the model to rename the
conversation and with that our database
uh and so we see here the conversation
was renamed to movie tracking database
and that's our final tool call here and
these are just happening back to back
with kind of any user interaction so so
as you can see with kind of all the
functionality being tool calls that
means the model has a lot of autonomy to
chain various tools

[00:05]
together uh and this also enables the
application to self-heal uh for example
any SQL errors from postest are fed back
to the language model so that it can try
a few more attempts at kind of solving
um the
issue another really cool feature uh
here is the inbuilt um in uh the
built-in Vector embedding support using
PG vector and Transformers Js so let's
go back to our demo and actually say add
five
movies um and embeddings on their
titles and so ah I probably should be
typing add five movie
examples and
embeddings on their
titles so we're going to fire this off
and we're going to run again kind of our
multi-step um

[00:06]
models here hopefully come on no okay I
think we we might have ran into an issue
here so so what it should do is let me
quickly reload that if we can
recover okay I get
my demo got offerings weren't accepted
let's try it again see okay we're
working on
it and so now you can see we're first um
executing our SQL to kind of seed some
sample data in our database and then in
the next step we're generating the
embeddings for all the titles and we're
storing them in a separate database
because if you worked with Vector
embeddings before even with small models
and you know smaller Dimensions these
are pretty large so we kind of want to
keep them outside and you can see okay
we got kind of five movies in Here and
Now what we can do is by having the
embeddings um in the database as well we
can do semantic search right so we can

[00:07]
say use semantic search to find a
movie about
Batman okay and so now we're going to go
off again we're running a couple steps
back to back uh so we're going to
generate embeddings you know for Batman
and then what we're doing here is so
we're using PG Vector um to perform
cosine distance to find kind of all the
movies that are related to Batman and
then we get back okay the dark KN
fantastic so we have um you know
semantic search built into this tool a
really really neat really neat feature
here
now just like copy and te make for great
drink so does mixing a traditional
graphical user interface with a large
language model so all of the actions in
the UI are implemented as tool calls and
when an action is clicked in the user

[00:08]
interface we simply fire off a message
in the chat and let the model handle the
rest now a little warning while this is
great for your user experience and
iterating quickly it's not so great for
your wallet so do watch out for that
another great feature here charts so
we're using chartjs here uh one of the
more mature charting libraries available
in JavaScript and the reason we chose it
is because GPT 40 has a really good
understanding ing of the syntax and
configuration so by simply chatting to
the model you can fully customize kind
of anything that you can do with chartjs
you can change um the chart type the AES
the colors uh so as long as chartjs
supports it uh GPD 40 can make it
happen lastly quick look at impact and
next steps here so we were able to sign
up more than 60,000 users in 3 months so
I think there's definitely something
here um we've also just launched live

[00:09]
share which allows you to connect to
your in browser database from any
postgress client um we just published a
blog post about this the tech um is
really really fantastic so do check that
out um a bunch more interesting stuff
happening but that's pretty much all I
have time for so if you have any
questions just find me later but the
chist I want you to take away is that
tool calls plus full database access
make for a pretty powerful postest
sandbox thank you

</details>

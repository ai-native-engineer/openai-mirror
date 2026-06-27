---
title: "OpenAI DevDay 2024 | Community Spotlight | Dust"
channel: openai
url: https://www.youtube.com/watch?v=RNcXWPCaLqg
youtube_id: RNcXWPCaLqg
published: 2024-12-17
duration: "12:05"
captions: en-orig
---

# OpenAI DevDay 2024 | Community Spotlight | Dust

[![OpenAI DevDay 2024 | Community Spotlight | Dust](https://img.youtube.com/vi/RNcXWPCaLqg/hqdefault.jpg)](https://www.youtube.com/watch?v=RNcXWPCaLqg)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | Dust (12:05)</summary>

[00:00]
all right welcome to this talk about
unified text to SQL for data warehouses
spreadsheets and csvs that's a pretty
long and rough title but we'll try to do
something a little bit more
comprehensible out of this talk um I'm
Alden I'm a Solutions engineer at dust
and dust is a company that's basically
an AI operating system so we help you
build assistance uh that are specialized
with your company's knowledge attached
um that's that could be a lot of
different things we've got a lot of
bricks that you can attach I'll talk to
about that right after and the good
thing is that your assistants are
embeddable everywhere because you we
have a pretty strong API and a Dev
platform and so you can just embid like
for example here uh this is zendesk and
you've got a dust assistant on the side
so your agents can talk to your company
data and even to other zenes tickets
directly from zendesk um what bricks
were was like talking about basically

[00:01]
you can add internal knowledge we can
add uh semantic search code
interpretation web search transcription
etc etc but the one we're going to be
talking about today is table queries
basically we want to be able to query
tables out of just regular good old text
let's start with a small
demo this is using an assistant that I
built uh that's plugged to our snowlake
warehouse and I'm asking it to visualize
the average number of messages sent on
the dust platform per day uh per week
actually and differentiate the top 10
workspaces with a different colors and
the rest with another color what's
happening there is that you can see that
it's querying tables it's telling us
what it's doing um then it's receiving
the data from Snowflake and it's
building a react component and then the
react component is going to be
interpreted by the the code interpreter
to build a pretty nice graph cool thing
is that you see we have some exponential
curve going on uh so that's a good sign

[00:02]
for us if we open the tools that were
used by this assistant we have some
chain of thoughts happening so it's
telling us why it was doing this and
then we've got the SQL query that was
used you can see that the SQL was
actually pretty long and if you needed
somebody to actually make it uh that
would take a while or a lot of SQL
knowledge let's keep going in the
conversation ask the same for active
users because we had the number of
messages now we want the number of
active users and at the same time we're
going to ask the same for the most used
assistants it's moving but that's the
second thing I asked in the same
conversation so here we're going to have
three different graphs one conversation
a lot of data points and the cool thing
is that the data points are not showing
up directly in the prompt because that
would take way too much time to generate
the components uh we'll see how they how
they show up right
after what I really want to do here with
the three graphs is to make one combined
graph with well one combined react
component with um actual buttons that

[00:03]
are going to let me switch between all
these components all these graphs so I'm
asking that right now it's going to
build the components and the cool thing
is that it's going to reuse the data
because we uploaded that as CSV files
directly available to the to the model
so here it should zoom in on the files
yeah there we go we've got the three
files here message users and agents um
and the react component is just creating
the graph using the files with the data
in it and boom we've got three graphs
nice buttons and we can
switch no need to know anything about
SQL no need to know anything about
coding so that was a warehouse that was
snowflake we asked one database for data
what if we want to use different sources
from different places let's say I have a
file with um on the Google Drive my HR
team has a file with the employees and
their roles and on a CSV I've got the

[00:04]
workspace usage of my users and I want
to know the roles that use dust the most
that's a pretty good thing to know
because we want to know which teams are
using it which use cases they have Etc
so it's pretty cool to know from
different places um how to merge the
data so I'm building an assistant
basically an assistant is a set of
instruction with tools attached so here
my tool is query tables and there's a
little description of the tool that I
built which is info about users activity
and roles we'll see that right after the
pretty important part here is database
that I ticked if I want to uh enable web
search for example for that assistant I
just take the web search box and I would
be able to ask you know um how many
metals each country won during the Paris
24 uh 2024 Olympics and that would graph
it but now I just want to use my own
data so my query table tool was built
like that so I've got my employees role
spreadsheet which is a Google sheet and

[00:05]
I've got my CSV of usage which is
something I downloaded directly on dust
from the dust
API I'm going to ask this assistant what
are the roles of our top five users
because that's exactly what I want to
see well I could say top 20 top 100
whatever um but the important part here
is the SQL query that's showing up here
so it's basically just doing a regular
gold old SQL query on two tables and the
two tables are the two files they are
coming from different storages different
world they shouldn't be able to talk at
the same place um but here we just have
a left join on the two files on the
employees email and the result is that
we've got the name the user number of
messages and roll so we've been able to
merge two different files going from two
different places just by asking okay so
how does this work uh to know how it
works I need to talk a little bit about
the desk architecture first we've got a
few components the first one is called

[00:06]
front this is basically where the
customers show up API web UI Etc um
that's connected to something called
connectors so whenever someone plugs
data to dust uh if you decide to plug
your Google Drive your notion your slack
Etc your GitHub or whatever uh it's
synced through a connector all that is
sync to a posr database and stores
stores stores the data and then it talks
to something called core which is a rust
application that talks directly to the
llms and talks to the quadrant database
which is a vector search database that's
how we do our
rag okay so what happens when I upload a
file on Dust so I can upload it from
Front I'm just dump a CSV in the UI for
example or I I can upload it from a
connector let's say I connected Google
Drive a new a new spreadsheet shows up
and then I'm syncing everything what
we're doing is that we're unifying those
files as a CSV so whatever the the
original file input is it could be a

[00:07]
spreadsheet a database a Google sheet it
becomes a CSV and then we parse it and
we try to find the column types um from
that we try to find the actual column
names that would be the easiest to use
for the llm so we're starring it with
different names than the actual file
just to make it more like easier to use
for the llm we store all that in our PG
database and we call that augmented
schema once the the user actually asks
the question we send both of that to the
llm we decide to send the augmented
schema the the actual query we send that
as a language called dbml um and we're
going to send that to any model that can
has that can use function calls so we're
model agnostic but for that particular
tool um we need function calls and our
function call is going to give us two
different results so structured outputs
basically uh a chain of thoughts and the

[00:08]
query let's deep dive a little bit into
that so basically what we're sending to
the LM is the full conversation history
that's what we saw I just said okay do
the same for users do the same for
messages um then we see the augmented
schema which is the the documented
columns that I just talked about and if
we find specific values uh if we find
enms in the columns we will send the
specific values that are possible for
column as well to make the job easier
again and then we'll we will send some
examples so we take all the table heads
so all the files basically and we send
the first 16 rows to the LM just to make
sure it's aware of the data structure
and then we do a structured output call
that's actually not true on our side
because we built that before the
structured outputs were available so
we're doing a function call but now we
could switch it to a structured output
call um and it's giving us three things
Chain of Thought which is the little
purple squares that I was showing you
when I opened the tool and the and the
SQL file

[00:09]
um the results of the the the title of
the file that you would download if
there's a file because sometimes the
user just ask a question a question and
the there's nothing to query like the it
just ask something else than than
anything that's in a database and the
SQL query again or not if we decide not
to run a SQL query we're not going to
run
anything once we have the SQL query
we've got two different paths um if it's
a warehouse so right now we only have
snowflake but we'll get to Red shift and
bit query uh we just execute the query
in the warehouse get the result back if
it's a file then it gets a little
trickier um we actually spin up
adjusting time in memory database so
it's a SQL light database that we spin
up in Rust so it's super fast so the
latency from the llm is big enough so
that we have time to spin up an a
database and feed it and so we feed all
the files in a database while the the LM
is thinking and then Boom the database

[00:10]
is ready um with all the files as a
table and then you can just do a left
join uh on any of the tables um okay now
we executed our query what's the rest
it's fairly easy we just store the query
um result as a CSV we're going to upload
it to S3 or GCS um and basically that's
what I showed after after that if I want
to build a component on top of it the
component can can just use the file
without having to spin up like spit a
lot of to of tokens because we started
building that um by just inputting all
the all the data points directly in the
llm that was super expensive uh and it
was super slow because the the the llm
was building the entire component
spinning all the data points uh using
files is a lot
easier so just to make sure uh the LM
understands the data structure of the
result we're going to show a few lines
to the llm as well um then the LM is

[00:11]
going to be able to generate a pretty
nice charting code we use recharts and
we're implementing D3 GS as well um this
component downloads all the files the
csvs and there we go we've got our
graph so
basically the goal of everybody in this
place is to reach AGI right we're we're
we're going to try to to rush to that uh
but I think we reach
natural language bi on our side so this
is used by a lot of non-technical teams
to be able to do bi that they were not
able to do before um they could they
could likely do that with dashboards and
stuff like that but the time spent to
build a dashboard compared to the time
spent just asking a question to your to
your Warehouse uh or to like completely
out this um out of range uh files is is
really really big
that's pretty much it thank you very

[00:12]
much um all there

</details>

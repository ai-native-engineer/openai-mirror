---
title: "OpenAI DevDay 2024 | Community Spotlight | Sana AI"
channel: openai
url: https://www.youtube.com/watch?v=RndBNbHuV4s
youtube_id: RndBNbHuV4s
published: 2024-12-17
duration: "14:19"
captions: en-orig
---

# OpenAI DevDay 2024 | Community Spotlight | Sana AI

[![OpenAI DevDay 2024 | Community Spotlight | Sana AI](https://img.youtube.com/vi/RndBNbHuV4s/hqdefault.jpg)](https://www.youtube.com/watch?v=RndBNbHuV4s)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | Sana AI (14:19)</summary>

[00:00]
good afternoon everyone I'm Jerry I'm an
AI product lead here at SAA and today
I'm joined by my colleague Daniel um who
is one of our AI lead Engineers on
Oni um over the last year we've been
building a lot in agents and agentic
workflows for Enterprises and today we'd
love to share a few of our findings in
the space um with uh with
you but first you might ask how did we
get started on this mission in the first
place why why are we doing this and our
mission at SAA is to to solve access to
knowledge and we see access to knowledge
and solving access to knowledge as
solving a meta problem once this is
solved we believe that a lot more people
can fulfill their missions much quicker
and to this extent actually ear today

[00:01]
we've announced another $55 million uh
Venture round um so we're very very
happy to to share that as well here
today now what do we do at saana so at
its core saana is an AI assistant
platform we bring together unstructured
data so you can think about data from
meeting notes or you can think about
data from one of the 100 plus
Integrations that we have live in the
platform as well as structured data so
this can come from any of your databases
or any of your systems of record and
then all this data is actually available
in the sa user interface via Enterprise
search via natural uh language chat and
then via sheets which is something we
just launched earlier today which allows
you to do a lot more complex workflows
and and data
extraction however for the rest of the
presentation today and our findings will
focus on on the chat with the structured
data part of uh

[00:02]
SII and when it comes to our agent
dealing with structured data flows um
our agent can handle two different types
of of workflows we have data analysis
and then we also have transactional
workflows which are which are more more
complex and this is important because
these type of workflows allow users to
interact with data from multiple sources
directly in SAA without uh ever having
to leave the the Unified
um user platform and with that I will
now um Go and show you a live demo of
what we've built so
far so this is our this is our platform
and here I can use the chat and I have a
prompt that I want to ask SI to help me
with and here I'm asking it to do the
following task I'm asking it to list
opportunities owned by a specific user
in a specific stage

[00:03]
in my CRM account and sa actually has to
do a couple of things here in the
background um that are not so it's not
just uh just one thing it first has to
get the description complete a search
and then um and then put all of that
into into a query uh query
sequence I can go ahead and I can ask
son to do something else um as well I
could say add to a Google doc for
instance and I can actually show you
exactly um what what saana has done here
in the background so in the first
step we have to look at the schema that
we have in Salesforce so what does it
mean opportunity and how does this tie
to everything else we have in Salesforce
how does this tie to the accounts we
have in Salesforce or the people we have
in Salesforce Etc then the second step
is to understand what we mean by Freda
so we're looking for a specific user and
we need to tie to understand her user
right to be able to tie it to the

[00:04]
opportunity and then finally in the
Google query in the final query we are
actually uh compiling everything
together and that's how we got to to uh
to the result and then um here I asked
it to push this to a Google Document for
instance I can make any changes I want
so let's say I have a demo up here uh
maybe this one will change the
amount and then I can easily create a
document directly in Sun
once this is done I can actually click
viewing Google Docs and this is opened
in a in a new sheet for
me so that's one way in which you can
interact with structured data in SAA
another way you can interact with with
um with this type of data is through
what we have here in tasks which are
pre-created um user prompts or you can
think about it as templates as well here
what I'm doing is I'm selecting a
meeting that a colleague of mine had so
this is an actual um uh meeting that

[00:05]
took over uh zoom and then I'm asking
SAA to pick out specific things like was
the budget discussed in the meeting
where specific competitors discussed in
the meeting um what's the need that was
mentioned in the meeting and then I want
those things to be sent to the relevant
fields in in my Salesforce account so
Sana actually does a couple of things
here first it matches the opportunity
name from the meeting with the uh
relevant Salesforce account and then
allows me to review the rest of the
actions here so let's say if I want to
make some changes maybe the timeline is
actually October 30th I can make that
and then I just click update opportunity
and then this is automatically synced in
Salesforce so if I come to Salesforce
and I I go down to my actual bnct Fields
I can see that this has actually been
mirrored here as
well so now that I've showed you a
little bit of uh what's possible to to

[00:06]
build in SAA I'm going to pass it over
to my colleague Daniel who's going to
explain how we've actually been able to
build all
this thank you so much Jerry so before I
dive into the architecture I wanted to
talk about one particular problem that
we've seen and provide some analysis so
agents can sometimes fail to sequence
complex tool calling flows so for
example in the Salesforce analysis that
we saw recently that required these
three particular tools so the first one
was getting the schema and let's say the
agent tried to go just straight to the
SQL query it might not actually know
what our Salesforce instance looks like
it might output some incorrect SQL um
maybe you can recover from that but this
is not great for a user in a real-time
interaction so I wanted to do some
analysis and figure out exactly what
kinds of agent configurations are going
to be more or less successful for this
problem the first thing I looked at was
different strategies for providing
instructions so a lot of you are

[00:07]
probably familiar with the kinds of chat
apis for a model like GPD 40 but just to
kind of refresh if we're thinking about
where we might want to give instructions
to an agent or an assistant that could
be in the system message so ours is
something like urana AI we give it some
personality guard rails that could also
be in the in the user messages and then
it could also be in the toolss so each
request is going to have the tools
attached and the tools are both the
schema that it might call call but also
they have a description um so I'm
looking at where do we want to put these
instructions for these
sequences one strategy could be to
provide a how to guide in a user message
so for example if using tools please use
tool a then tool B then tool C gets the
point
across strategy number two would be a
list dependencies in tool descriptions
so we could say tool C depends on tool B
and Tool B depends on tool a and so you

[00:08]
can infer from that that you need to do
tool a then B then C so just a different
way of getting the same instructions
across and so we created this grid of
different agent configurations to figure
out which of these strategies will be
more successful across the top you can
see the two different instruction
strategies and down the side we can see
different numbers of tools that we gave
to the agent and so what we found is
that providing this how-to guide
instruction in a user message was super
important um even with 15 tools the
agent was able to pick out the right
ones and complete our workflow
successfully and just to clarify this is
for one of these three-step
workflows
um this strategy works well in system
messages as well especially if you have
a simple agent that has one purpose I
think that's a great solution for us we
like to use user messages because that
allows us to put these instructions at
different points in the con conversation
history and then on the right side the
tool description approach did not work
very well

[00:09]
um and interestingly this is not a
phrasing issue if we copy and paste the
exact same prompt from our user message
into a tool description it'll still fail
to sequence these complex workflows so
even though it's being turned into the
same tokens a little bit different
application there and I think this is
really consistent with the view people
have that an llm might be really good at
picking out a needle and a Hy stack so
15 tools not a problem but for these
reasoning or sequencing tasks it can use
a bit more instructions and so that
how-to guide approach is a great way to
do that for simpler workflows we ran the
same analysis and found that it was
successful across the board so that's
great if your agent only needs to use
one tool at a time two tools you
probably don't have to think too hard
about instructions and you can probably
fit a lot of tools into the same
agent so now having done that analysis
getting back to our solution at sauna of
course we want to handle both the
complex and the simple workflows so
we've created this internal interface
that we call a tool set a tool set is

[00:10]
going to have a name you're looking at
right here the tool set for the uh
workflow that we were just demoing for
the Salesforce agent that queries the
data so the name is explore Salesforce
records of course we have the three
tools that are required as part of this
tool set and then we also have our cross
tool usage instructions so copying this
verbatim from the code base when using
SQL and that's salesforce's version of
SQL always refer to the describe API to
understand the scheme you're quiring and
then use the find record ID tool to find
the ID for Relevant foreign relations
and so on so we're kind of getting the
sequencing instructions across and
overall this tool set is a package
that's going to allow our agent to
execute some specific workflow in some
context but of course going back to the
title of this talk we're talking about
multi-talented agents and how do we
solve this problem of doing all these
workflows you know creating Google Docs
querying snowflake Salesforce Etc all
from the same user interface and so for

[00:11]
that we're going to need some routing so
we have a router llm that's going to
pick out tool sets and for that reason
each tool set also has special selection
criteria so also copying verbatim from
the codebase this tool set allows the
assistant to find Or List Salesforce
records of any type using SQL queries
does not handle right operations only
select if one of the following is true
so you can see how we can kind of carve
out the very specific conditions in
which the users's message
should be handled by this particular set
of tools and in this way we make sure
that the user not accidentally getting a
bunch of tools thrown in their face but
also that if they want this agenting
workflow to happen they're going to end
up with the best set of tools to
complete
it so now tying that all together when
our backend receives a new message from
the user we kick off in parallel that
tool set router I just discussed as well
as our primary query planner and search
engine so we have
have the search engine is kind of like a

[00:12]
default tool set that's really the bread
and butter of Sonet
AI it has Vector search web search and
Knowledge Graph Search and so altogether
this is pulling unstructured and
structured data from all across
company's
knowledge and assuming that we select a
tool set that is going to go to our
recursive agent along with those search
results so this part is really important
this is how we can do these requests
like for example when we were analyzing
a meeting and then taking that
unstructured data putting it into
Salesforce that's how we're able to pull
search results and then put it into a
structured Place using tool
sets one last thing I want to talk about
is high integrity tool responses this is
another thing that we take very
seriously so you could think of an agent
as interacting directly with an API
however in a system like sauna that's
not really the case the agent is
interacting with validators at first
it's interacting with a user perhaps
right we saw Jerry was able to make

[00:13]
modifications to the request before
submitting it the user could cancel it
um so there's all these different system
interactions that we think it's really
nice to be able to display to the agent
so that the agent can make Intelligent
Decisions going forward so an example
tool response that we might send back to
the agent is one tool use past scheme of
validation two the user modified the
name field three the User submitted at
2:41 p.m. and finally the API responded
with success and so on and so in this
way our agent always knows exactly
what's going on with the user and
enables these really high collaboration
workflows so the two big actionable
takeaways from this presentation first
of all add tool sequencing instructions
via a user or system message this will
enable these more complex workflows and
two provide comprehensive system and
user feedback and Tool responses to make
sure that the agent understands what's
going on and can collaborate really

[00:14]
well so these are just a few of our
learnings from our research here at
sauna we're super excited to continue
building General agents and we think
that by combining that with all of your
company's knowledge we'll be able to
unlock huge amounts of productivity and
help people solve bigger problems so
thank you

</details>

<!-- source: https://academy.openai.com/public/clubs/champions-ecqup/videos/make-work-flow-proactively-monitor-accounts-with-codex-2026-06-12 -->

[Champions](/en/public/clubs/champions-ecqup/overview)

[navigation.content](/en/public/clubs/champions-ecqup/content)

Sign in or Join the community to continue

Get Started

# Make Work Flow: Proactively monitor accounts with Codex

Posted Jun 12, 2026 | Views 79

# Codex for Work

# Activators

# Use Cases

Share

## SUMMARY

Make Work Flow is our series showcasing how Activators\* build AI-powered workflows that help their teams get real work done. In this session, Yash Pahade (AI Success Engineer, OpenAI) will share how he uses Codex to monitor important account information proactively, rather than relying on manual checks and scattered updates. He will walk through how he uses Coded for gathering relevant signals, surfacing what needs attention, monitoring key metrics, and making it easier to stay ahead of changes. Attendees will walk away with an example to adapt and use to track updates, spot issues earlier, and prepare for timely follow-up.

+ Read More

## TRANSCRIPT

[00:08:27] Kenna Valdez:

Hi, everyone. Thank you so much for joining us today. We're really excited to kick off this session. I'm going to give everyone one minute before we really get started.

While we're waiting, please feel free to share where you're joining us from in the chat: city, country, state of mind—whatever you're most comfortable with. We will kick things off in just a minute.

Again, thank you all for joining us today. I just want to make sure folks have time to trickle in and get connected before we begin.

All right, thank you so much. I see we're all over the place—that's amazing. Boston, California, Japan, Mexico. Thank you all for taking the time.

Okay, I am going to go ahead and kick things off. Hello, my name is Kenna. Welcome to Make Work Flow. This is an OpenAI series showcasing how real AI Activators—the people designing, building, and scaling AI workflows for their teams—do just that.

We'll share how members of many different kinds of teams at OpenAI have built workflows to help with the real work their teams already do. Whether or not you call yourself or think of yourself as an AI Champion yet, this series is meant to give you real examples of useful workflows and use cases that you can take back and adapt to your team, along with tips to design, build, and scale those workflows safely and effectively.

A couple of housekeeping items: this session is being recorded. The recording, presentation, and follow-up resources will be shared in the Champion Community on OpenAI Academy, where you signed up to attend this event.

I'll be in the chat, along with Christina, throughout the session, so please feel free to raise your questions. We'll address as many as we can before the end of the live session today.

In this particular session, Yash, a member of our AI Success Engineering team here at OpenAI, is going to share how he uses Codex to proactively keep up with important context about his accounts.

With that, I'm going to hand it over to you to introduce yourself and your workflow.

[00:12:01] Yash Pahade:

Awesome. Thank you, everyone. Like Kenna mentioned, my name is Yash. I currently work as an AI Success Engineer here at OpenAI.

A lot of my job is supporting our customers, making sure they're getting the most out of our products, and ensuring that I have full context on what they're doing almost at all times.

As somebody who recently joined OpenAI, there is a lot of context that I need to ingest in order to understand what our customers are up to. A lot of that information lives in different places. We use many different tools, some similar to what you might use at your own organizations, such as Slack, Google Drive, meeting recorders, and so on.

There's a lot of information and context that I need to pull together. As an AI Success Engineer, I wanted a way to scan all of that information, stay up to date, and make sure the other members of my team who also support these accounts are up to date as well.

That's what I'm going to show you today. Kenna, is it okay for me to share my screen?

[00:13:12] Kenna Valdez:

We should be good, yes.

[00:13:14] Yash Pahade:

Awesome. There we go. Just confirming: can we see my screen?

[00:13:32] Kenna Valdez:

Yep, you're good to go.

[00:13:33] Yash Pahade:

Great. Like I mentioned, there are a lot of different sources of information, and I want to stay up to date. I wanted a way to scan what is going on every day.

I was able to use some of our AI tools, like Codex, to build something really simple but also somewhat sophisticated that keeps me up to date almost all the time.

What you're looking at is a demo version of the pages I use for my customers. I call it a command center. Let's call the customer Acme for today.

I usually start by trying to understand what has changed since I last refreshed the page: the state of the account, whether there are any support items, whether customers have shared feedback in any of our channels or submitted tickets, anything related to scheduling, upcoming meetings, recent meetings, and usage metrics for our AI tools, such as ChatGPT. I can see how many weekly active users they have and what has changed.

You can see that I'm building up a lot of this context on a Notion page. I have sections like recent activity that go deeper into the higher-level information.

[00:14:56] Kenna Valdez:

One moment, Yash, before you dive in. Is it possible to make your screen share a little bigger so folks can see it more clearly?

[00:15:03] Yash Pahade:

Of course. Sorry about that. Is this clearer?

[00:15:06] Kenna Valdez:

Thank you. Let us know in the chat with a thumbs-up.

[00:15:13] Yash Pahade:

Okay, great.

You can see that I'm keeping track of recent activity with the customer, including the latest touchpoints. All of this is generated with Codex.

I'm also looking at next touchpoints. Based on recent meetings and conversations, what are the next things I need to do?

I'm keeping track of meetings as well—what is coming up this week and what has already happened. For example, for a meeting earlier this week, I have information about whether it was internal or external, the meeting title, and notes from the session. All of this is populated with Codex.

The metrics are interesting too. I'm keeping track of things like total ARR, API usage trends, weekly active users, seats filled, and so on.

One thing I wanted to point out is that when you're using tools like Codex, there are limitations based on what the tool you're interacting with makes available. For example, Notion does not really give Codex access to its native charting capability through the API. Codex recognized that and built some very basic charting using ASCII.

You can see that it's a simple visualization. It's nothing too elaborate, but it gives me a good idea of the trend.

Codex can pick up on many of these things intuitively, with some prompting from me as well. I got a lot of this working in the first iteration of the command center.

As we scroll down, there are more metrics. It also shares some of the data it uses to put this together, which I have linked. It looks like the link is not present in this specific demo, but you can still see the weekly snapshot views and how the metrics are visualized over time.

A lot of this information is pulled from our internal data sources. As an AI Success Engineer, I do not have to spend a lot of time writing complex SQL queries, running them every day, and maintaining the reporting. This happens automatically.

Another useful section is recent cases. Codex can pull ongoing support cases or tickets into the dashboard once the relevant source is connected. That makes it easy to keep track of which tickets are in progress, what blockers exist, and what has closed recently. It helps me avoid constantly switching between tools.

Even something as simple as a to-do list can be updated automatically based on Slack activity, emails, documentation, call transcripts, and so on. I can also change it manually. For example, I can have it remove certain to-do items when I change their status from in progress to done.

Another thing I find helpful is news related to my accounts. Especially when you work with companies that are more public-facing or consumer-facing, there is a lot of useful information I would want to know. Otherwise, I might need to check sources like CNBC, Reddit, and other news sites manually.

Codex searches the web and pulls information it thinks is relevant. If there is a new initiative, I can talk to my customers about it, understand how they are thinking about new products they have discussed publicly, and consider how I can support them.

Finally, I have the different data sources aggregated in one place: documents, Gong calls, use cases they are building toward, stakeholders on our side and their side, operating sources, and account-specific data.

This gives me a simple snapshot that I can scan every day to understand where things stand. It updates automatically each day.

I can switch gears now and show you how we're doing that. Before I do, did we want to stop for questions?

[00:20:07] Kenna Valdez:

I think we do have one question. I know this was something Codex initiated a little unexpectedly during your first run-through.

[00:20:09] Yash Pahade:

Sure.

[00:20:15] Kenna Valdez:

The question is about the visuals. Do you have any tips for guiding the formatting or the desired end state of the visuals Codex creates?

[00:20:30] Yash Pahade:

Sure. I'm assuming that by visuals, you mean some of the metrics here.

Generally, when you're prompting Codex, there is some feedback and back-and-forth involved. Sometimes it happens on the first try. Otherwise, I give it examples of what I want the output to look like.

For charting, I might say that I prefer bar charts, horizontal charts, or pie charts. It also depends on the tool. With Notion, Codex does not have access to the native charting capability because, I believe, it is gated behind an API endpoint. Depending on the tool, you may be able to get more granular in how you describe the output.

For the overall structure, it really comes down to prompting and having a back-and-forth conversation with Codex. It is an iterative process.

Once something is output to Notion, I can go back and say, "These are the sections I want. These are the sections I do not want. I would prefer this to be a table rather than bullet points." I can also specify that I want a line graph or a horizontal bar chart, as Ed mentioned earlier.

[00:21:48] Kenna Valdez:

Completely agree. I think you hit two important points that match my experience as well.

First, iteration is okay. If you need to take additional steps to describe your preferences, it is okay to have that back-and-forth with Codex to get where you want to go.

Second, sharing examples can help. Sometimes I will take a screenshot of another dashboard or a format I want to follow. Codex can be very good at using the visual examples you give it to create something more aligned with what you want.

I know iteration has been a big part of building this automation for you, so I want to let you move on to the build.

[00:22:31] Yash Pahade:

Definitely. That is a good segue into the build itself.

There are different ways to build automations with Codex. The easiest and most effective way I have found is to open a chat with Codex and describe the automation I want.

I start with a very simple prompt, such as: "Here are all the different data sources I have, and I would like a command center view or a daily pulse showing what is happening with these accounts."

As you go back and forth with it, Codex iterates and builds on top of the automation.

You can see the Automations tab here. This is the actual automation, and Codex has started populating the instructions. I did not write all of these instructions myself. Codex generated them based on the back-and-forth conversation in the chat window.

It understands that it should update the Notion command center, which is linked to the Notion page that was created. It also defines the sections and structure of the page, such as the daily pulse, recent activity, calendar, and so on. It goes deeper into what each section should include and what the daily workflow should do.

It takes the points and instructions I have given it, such as checking my Google Drive and the relevant Slack channels. To reduce hallucinations and add guardrails, I can tell it to check specific Slack DMs as well. Sometimes conversations happen in groups with me, another team member, or a customer, and it can read the context from those conversations.

It formulates the structure and workflow based on that information.

If I see it making mistakes, I can ask questions like, "Where are you getting this information from?" I can also read through the instructions myself to understand exactly what Codex has been told to do and what adjustments I need to make.

You can see all of the steps the daily workflow takes to build the page. There are a lot of instructions because I have had a lot of back-and-forth with it. For the most part, it does a good job of rereading the document, making adjustments based on feedback, and continuing to evolve.

It is an iterative process, and there is still room for improvement. I also get feedback from the other members of my team about what they would like to see because this is a source of truth for the entire team supporting the account.

[00:25:42] Kenna Valdez:

That's a great point.

[00:25:42] Yash Pahade:

Awesome.

[00:25:43] Kenna Valdez:

Before we move to another great question from the chat, I want to ask what you think the next evolution or iteration of this automation is.

You mentioned that the team uses this as a source of truth. Can you give us a sense of the impact—what things looked like before you built it versus after—and how you are thinking about making it more useful next?

[00:26:18] Yash Pahade:

Definitely. In terms of impact, this saves a lot of cycles that would otherwise be spent asking questions about the status of an account.

Instead of having to share information explicitly over Slack or in one-on-one conversations, I can point people to this source of truth.

It also helps me catch changes early, such as an increase or decrease in usage, so I can make the right decision.

[00:26:44] Kenna Valdez:

Right.

[00:26:45] Yash Pahade:

Before this, I had to spend a lot of time querying different tools to pull the data, maintaining those queries, running them every day, and generating reporting. Now I do not really have to do any of that, so it has changed my workflow significantly.

It also makes me think about how I can improve it further. There is still a level of sophistication I would like to add. That is not necessarily because of Codex. It is partly about putting more time into organizing my to-do list and the underlying information.

There are things the automation might miss, or times when it might hallucinate. Improving that is a process of adding better guardrails and organizing the information more effectively.

Since I started using this, I have also become much better at building supporting automations. For example, meeting notes that come in after a meeting are automatically organized in my Google Drive by another automation, which makes it easier for this one to pick them up.

Those are the kinds of smaller improvements I am continuing to make so this becomes an even better source of truth.

[00:28:10] Kenna Valdez:

Thanks, Yash. We have a couple of additional great questions. Please continue to share your questions in the chat.

As you can see, we want to show you the workflow, but we also reserve plenty of time for questions because we want you to leave these sessions feeling able to reuse and adapt these workflows for your own teams and workspaces.

Angelique is trying to understand the architecture behind how the information is collected and used by Codex.

When you talk about the news section of your command center, Codex is pulling information from external sources like news sites. When Codex retrieves that information, is it storing it locally and keeping it, or how is it using that context?

[00:29:00] Yash Pahade:

That's a good question.

For news sources or other text-based information, the information that is selected lives in the Notion document itself. Codex reads that and then looks for updates.

I explicitly instruct it to run a web search for anything relevant. If nothing relevant appears, it does not change the existing data in the command center. It just marks when that source was last updated, so I have a better idea of how fresh the information is.

[00:29:38] Kenna Valdez:

Got it. So it saves the sources you want it to use when it searches, and the information it takes from those sources is saved in the command center. But it is not necessarily saving the full website or article content locally.

[00:29:57] Yash Pahade:

Exactly.

More broadly, I do have data stored for much of this workflow, which goes back to the importance of organizing the data.

I am not relying on Codex to create and store all of the underlying data itself. The data comes from other tools. Meeting notes may be captured by a transcriber. Information that customers share with me, such as documentation, is stored as well.

That information can live locally for Codex to read, or it can live in a system like Google Drive.

[00:30:39] Kenna Valdez:

That makes sense. The core point is that you can instruct Codex to work one way or the other.

My follow-up is about access, permissions, and token usage. When you built this, you were relatively new—at least to the go-to-market organization at OpenAI. How did you think through those considerations so you could use this thoughtfully and responsibly with the team?

[00:31:12] Yash Pahade:

That's a good question. I'll start with token usage.

In the automation, you can specify how often it runs. If I need something to check for a new Slack message or email every 30 minutes, that will consume more tokens, even though the underlying sources may not have changed.

This command center does not need to update every hour. Updating it once every morning works well, so I configured the schedule that way to be mindful of token usage.

The model and reasoning level are also important. I use GPT-5.5 with a high reasoning level because this is a more complex task with a lot of information to process.

For a simpler task, such as organizing data sources, I might use GPT-5.4 with a lower reasoning level.

You also asked about access. You can connect applications through ChatGPT and, in turn, Codex. That is how access is gated.

There is an MCP connection between Codex and tools such as Slack. There are permissioning considerations to be aware of, but that is generally how Codex communicates with those tools.

As a new employee, I went through the normal process of getting access to the tools I needed and then connecting those approved tools to ChatGPT and Codex.

[00:33:19] Kenna Valdez:

That's a great point. Celeste asked whether you have had success getting Codex to log into other systems using your credentials.

Could you explain what happens once you have access to an app such as Google Drive and want to add that connection to ChatGPT and Codex?

[00:33:42] Yash Pahade:

It is pretty simple. You go into ChatGPT, find the Apps section, connect the app, and authenticate with your credentials. Codex should then have access through that connection.

Something to be aware of is that you may occasionally need to reauthenticate if a connection breaks, but for the most part the tools have been stable.

I also believe this workflow is going to become simpler soon, so you may see the connection process improve. Even now, though, it is fairly straightforward: connect the app in ChatGPT and then give Codex access through that connection.

[00:34:26] Kenna Valdez:

Thanks so much, Yash.

We have covered some of how you approached the build, and we have a few more questions coming in. Please continue to share them in the chat.

One question is whether performance may change depending on the language of the content. Have you asked this automation, or another automation you built, to analyze sources in multiple languages? If so, did that affect the output?

[00:35:04] Yash Pahade:

For the most part, I have used English and asked it to analyze English text.

I know it can read other languages. Depending on the model and reasoning level, results may vary, but from what I have heard internally and what I have seen using the tool, it seems to understand multiple languages reasonably well.

I have not used multiple languages for this particular use case, especially with the Notion component, so I cannot speak to it directly.

[00:35:49] Kenna Valdez:

One other question is about connecting accounts specifically.

Can you connect multiple Gmail accounts to a single instance, or is it a one-to-one connection between your Drive or workspace and your ChatGPT and Codex account?

[00:36:14] Yash Pahade:

To be completely candid, I'm not 100% sure.

My understanding is that you authenticate one account per ChatGPT account. You can be part of different organizations within your account, but I believe each connected account would be associated with a different ChatGPT and Codex account.

So I do not believe you can connect multiple Gmail accounts in that way, but I am not 100% sure.

[00:36:41] Kenna Valdez:

Just to add context, some of this depends on how your organization has configured its workspace, the permissions it allows you to grant to apps, and which apps you are allowed to connect.

You can check the Help Center to understand what is technically possible, but you should also confirm your own organization's policies and settings.

For security and information handling, I would especially encourage people in regulated industries or lines of business to review the documentation and check with their account team.

Different organizations and lines of business may have different settings designed to ensure that information is not saved locally when it should not be, or that certain sources and outputs are not included in a team-wide command center like this one.

It will depend on your organization and its settings.

We have about a minute left, and I want to make sure we close on time. Yash, if you'll let me share my screen one more time.

[00:38:28] Yash Pahade:

There you go.

[00:38:29] Kenna Valdez:

Thank you.

As a reminder, you joined today's session through the OpenAI Champion Community. The Champion Community on OpenAI Academy is your space to find more AI adoption insights, real examples, and resources to help you design useful workflows that are responsibly integrated into your systems so you can scale them safely to your team.

Please sign up for more Make Work Flow sessions. We have more sessions coming up where we will share additional examples from real work.

You can also sign up for the Insights from the OpenAI Champion Network webinar next week, where we will share the adoption trends we are observing and what you should do about them as an AI Champion.

As you build new ways of working for your teams, please come back to the community and share what you can in the Use Cases forum. You should always follow your company's security and privacy policies, but we would love to see what you have built.

The workflow Yash shared today was one of his first Codex use cases as a member of the go-to-market team at OpenAI. This month's theme is sharing your first Codex use cases and what surprised you or did not work as expected.

Please check out the Use Cases forum in the community. You will find more examples from others, and you will have a chance to win swag if you share.

Finally, for those of you who do not know, the Enterprise Champion Network is open to AI leaders across organizations on the OpenAI Enterprise plan. It offers deeper engagement with other AI Champions and OpenAI.

Whether you are an executive sponsor, an organization-wide coordinator, or a functional or departmental lead, you will find opportunities to participate in deeper engagement, provide feedback, and help shape the future of OpenAI.

You can learn more at champions.openai.com.

Thank you, everyone, for staying with us for a couple of extra minutes. We really appreciate you joining us, and we hope you found today's session useful.

Look out for additional assets in the Champion Community to help you adapt the workflow Yash shared today for your own teams.

Thank you so much, Yash, for sharing what you built with us.

[00:40:51] Yash Pahade:

Thanks for having me.

[00:40:53] Kenna Valdez:

All right, everyone. Thank you. Have a great rest of your day and the rest of your week. We'll see you soon.

[00:40:57] Christina Meng:

Thank you.

[00:40:59] Yash Pahade:

Thanks.

+ Read More

Sign in or Join the community

![OpenAI Academy](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-black-monoblossom-743de6c6-b680-4334-8cd5-fee30f7a2202-1739890376705.png?fit=scale-down&width=100)

Create an account

## Watch More

[11:00](/en/public/videos/workflow-clip-proactively-monitor-accounts-with-codex-2026-06-12)

[Workflow clip: Proactively monitor accounts with Codex](/en/public/videos/workflow-clip-proactively-monitor-accounts-with-codex-2026-06-12)

Posted Jun 12, 2026 | Views 79

# Codex for Work

# Activators

# Use Cases

[31:00](/en/public/videos/recording-make-work-flow-automate-crm-updates-with-codex-2026-06-18)

[Recording: Make Work Flow: Automate CRM Updates with Codex](/en/public/videos/recording-make-work-flow-automate-crm-updates-with-codex-2026-06-18)

Posted Jun 18, 2026 | Views 79

# Codex for Work

# Use Cases

# Activators

[3:00](/en/public/videos/confidence-scoring-and-skill-hardening-with-codex-2026-06-18)

[Confidence scoring and skill hardening with Codex](/en/public/videos/confidence-scoring-and-skill-hardening-with-codex-2026-06-18)

Posted Jun 18, 2026 | Views 89

# Codex

# champions

# AI Techniques

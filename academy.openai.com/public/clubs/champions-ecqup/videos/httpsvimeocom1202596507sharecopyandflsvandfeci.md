<!-- source: https://academy.openai.com/public/clubs/champions-ecqup/videos/httpsvimeocom1202596507sharecopyandflsvandfeci -->

[Champions](/en/public/clubs/champions-ecqup/overview)

[navigation.content](/en/public/clubs/champions-ecqup/content)

Sign in or Join the community to continue

Get Started

# Workflow clip: Automate CRM updates with Codex

Posted Jun 18, 2026 | Views 56

# Codex for Work

# Use Cases

# Activators

Share

## SUMMARY

If customer notes, emails, call transcripts, and account context often stay outside the CRM, this video shows how Codex can help structure reviewed update proposals, add field-level guardrails, and support desktop or mobile updates.

+ Read More

## TRANSCRIPT

1
00:00:00.000 --> 00:00:04.927
Bryant McCombs: All right, so just, really quickly. Just wanted to show you. Let's

2
00:00:04.927 --> 00:00:09.855
light over here. First a skill that I created so. The first thing that you're likely

3
00:00:09.855 --> 00:00:14.782
going to going to want to do is build something that's repeatable. So for those

4
00:00:14.782 --> 00:00:19.709
of you who are unfamiliar with the idea of a skill, it's essentially just kind

5
00:00:19.709 --> 00:00:24.636
of reusable instructions that you could use for templization, or some level of

6
00:00:24.636 --> 00:00:29.564
determination or determinism around. Rather so, say, for example, if you had a

7
00:00:29.564 --> 00:00:34.491
specific template or a specific field, that you always wanted to update in the

8
00:00:34.491 --> 00:00:39.418
same way. Skills are a great use case for something like that. So the first thing

9
00:00:39.418 --> 00:00:44.345
that I did for this particular skill was again I wanted to. One be very explicit

10
00:00:44.345 --> 00:00:49.273
around like you know what it's supposed to be doing right. So in this case, I told

11
00:00:49.273 --> 00:00:54.200
it that it's a an enterprise account director. With a responsibility to update

12
00:00:54.200 --> 00:00:59.127
Salesforce. And that its role was to translate those approved customer and internal

13
00:00:59.127 --> 00:01:04.055
account context into accurate and concise Salesforce updates. And then the next

14
00:01:04.055 --> 00:01:08.982
really important thing that I wanted to do was give it a sense of what its guardrail

15
00:01:08.982 --> 00:01:13.909
should be right. So whenever you're building out a skill, especially if it's something

16
00:01:13.909 --> 00:01:18.836
that has write permissions in this case. So for those of you who are unfamiliar,

17
00:01:18.836 --> 00:01:23.764
write permissions. It's basically just the ability to change information within

18
00:01:23.764 --> 00:01:28.691
whatever application that you're using. But if you're using something, or if you're

19
00:01:28.691 --> 00:01:33.618
building something that has write permissions, you want to make sure that you're

20
00:01:33.618 --> 00:01:38.545
still the write permissions. In the right guardrails into that particular use case,

21
00:01:38.545 --> 00:01:43.473
right so. And this could, in this case. I said that the workflow should not modify

22
00:01:43.473 --> 00:01:48.400
the opportunity. Amount should not modify the stage, should not modify the close

23
00:01:48.400 --> 00:01:53.327
date, forecast category. Without my explicit approval, right? So whenever you're

24
00:01:53.327 --> 00:01:58.255
building something where you know you're not sure what level of trust you have.

25
00:01:58.255 --> 00:02:03.182
In the workflow, quite yet. Or if there are things that just have kind of higher

26
00:02:03.182 --> 00:02:08.109
table stakes in terms of you know. The changes that you're making to them. If those

27
00:02:08.109 --> 00:02:13.036
are kind of like mission, critical fields that you're changing, you'll want to

28
00:02:13.036 --> 00:02:17.964
make sure that you're implementing some level of guardrails right? So, so that

29
00:02:17.964 --> 00:02:22.891
that was the next piece that I wanted to address. And then what I wanted to do

30
00:02:22.891 --> 00:02:27.818
is just kind of define what that output structure should look like. So. Obviously,

31
00:02:27.818 --> 00:02:32.745
within every organization there are certain norms, certain philosophies in terms

32
00:02:32.745 --> 00:02:37.673
of how certain either presentations or docs or sheets should actually look so.

33
00:02:37.673 --> 00:02:42.600
I want to tell also. Make sure that I explicitly call that out. In the output here

34
00:02:42.600 --> 00:02:47.527
as well. And so, for the output, I just talked about how yeah for account summary

35
00:02:47.527 --> 00:02:52.455
changes for opportunity changes. They should all look specific way. And so you

36
00:02:52.455 --> 00:02:57.382
could see. We then created this skill here, which is our Salesforce account. Update

37
00:02:57.382 --> 00:03:02.309
skill. And then what I'll typically do after I build, a skill is, I'll say okay.

38
00:03:02.309 --> 00:03:07.236
Given my role, what are some of the different use cases that I could potentially

39
00:03:07.236 --> 00:03:12.164
leverage? This skill for and then how can I use this to optimize my existing? Workflows.

40
00:03:12.164 --> 00:03:17.091
And so you never want to just use a skill just for one thing, right? So. There's

41
00:03:17.091 --> 00:03:22.018
a little bit of like duality here, right where? The narrower the skill is, the

42
00:03:22.018 --> 00:03:26.945
more performant. It's going to be right. So I would never recommend building a

43
00:03:26.945 --> 00:03:31.873
skill that just has like this. Really broad applicability, right? But then you

44
00:03:31.873 --> 00:03:36.800
also want to figure out okay? Once I've built this skill, that is like pretty narrowly

45
00:03:36.800 --> 00:03:41.727
focused like what else can I actually do with it? Right so what else could it potentially

46
00:03:41.727 --> 00:03:46.655
be helpful for so. In this case it's also calling out that for this narrowly built

47
00:03:46.655 --> 00:03:51.582
skill it could also be really helpful for post meeting Salesforce cleanup. It could

48
00:03:51.582 --> 00:03:56.509
be helpful for pre forecast account. Hygiene for customer threads here I'm translation,

49
00:03:56.509 --> 00:04:01.436
MEDDIC refreshes task creation et cetera. So again, it's not like a one size fits

50
00:04:01.436 --> 00:04:06.364
all skill. But it can also be incredibly valuable across a number of other use

51
00:04:06.364 --> 00:04:11.291
cases as well. And then the last thing I want to call out was that whenever you've

52
00:04:11.291 --> 00:04:16.218
built a skill, you could also strengthen that skill by having it also. Either call

53
00:04:16.218 --> 00:04:21.145
other skills, or call other plugins or MCPs. That could also make that skill more

54
00:04:21.145 --> 00:04:26.073
valuable. So in this case I also wanted to ask it. Okay, what are some of the additional

55
00:04:26.073 --> 00:04:31.000
skills or plugins or MCPs? That I could also incorporate with a skill to make this

56
00:04:31.000 --> 00:04:35.927
workflow even stronger. And so, in this case it came back and said. Actually yeah,

57
00:04:35.927 --> 00:04:40.855
you could probably use a Salesforce plugin that would make this skill stronger,

58
00:04:40.855 --> 00:04:45.782
or you could use a gmail or outlook skill that could make this stronger or a slacker

59
00:04:45.782 --> 00:04:50.709
teams basically. It's looking across all of the different contexts that's available

60
00:04:50.709 --> 00:04:55.636
to it. And saying okay, if you connected all of these other data sources, you could

61
00:04:55.636 --> 00:05:00.564
make the skill even more valuable or more impactful. And then the last, last thing

62
00:05:00.564 --> 00:05:05.491
that I want to show you is that you could also automate these skills as well, or

63
00:05:05.491 --> 00:05:10.418
automate these workflows as well. So in this case I wanted to say okay great. I

64
00:05:10.418 --> 00:05:15.345
would love to automate this. So let's plan to run this every friday. At four pm.

65
00:05:15.345 --> 00:05:20.273
And then, if it's missing any context, just let me know. And I will provide that

66
00:05:20.273 --> 00:05:25.200
context that way. You can make sure that you're able to update anything else within

67
00:05:25.200 --> 00:05:30.127
Salesforce. All right, so let's move on to the demo. Just so you can kind of see

68
00:05:30.127 --> 00:05:35.055
what this looks like. Live. All right great so. What we're going to look at is

69
00:05:35.055 --> 00:05:39.982
just the ability for Codex to help. An account team update a Salesforce opportunity.

70
00:05:39.982 --> 00:05:44.909
So I'm just going to pop back over here, and you can see. In this case, we have

71
00:05:44.909 --> 00:05:49.836
this kind of makeshift Salesforce, or demo Salesforce Salesforce account called

72
00:05:49.836 --> 00:05:54.764
macomb's consulting. And then we have our demo opportunity. We have the ability

73
00:05:54.764 --> 00:05:59.691
to change a number of different fields here, so we could change the stage. We could

74
00:05:59.691 --> 00:06:04.618
change the forecast category, we could change the dollar amount. The close date.

75
00:06:04.618 --> 00:06:09.545
When does the contract start? When does the contract end next steps? Et cetera

76
00:06:09.545 --> 00:06:14.473
right? So let's pop back over to Salesforce, and you can see right now. We have

77
00:06:14.473 --> 00:06:19.400
it in the evaluation stage. We have a dollar amo unt of about two hundred and forty

78
00:06:19.400 --> 00:06:24.327
k. We have a closed date of september thirtieth. Of september. We have no contract.

79
00:06:24.327 --> 00:06:29.255
Start date and we have no contract end. Date. And then we have no next steps, which

80
00:06:29.255 --> 00:06:34.182
is a big no, no. Here, at OpenAI. So we're going to make sure we get those things

81
00:06:34.182 --> 00:06:39.109
updated so that our internal stakeholders have a better sense of what's happening

82
00:06:39.109 --> 00:06:44.036
across this opportunity. So let's go ahead and pop back over to Codex. And I'm

83
00:06:44.036 --> 00:06:48.964
going to say please update the contract, start date to december, twenty fifth of

84
00:06:48.964 --> 00:06:53.891
december, twenty, twenty six. That's easy enough date to remember. And then for

85
00:06:53.891 --> 00:06:58.818
the next steps let's say that we're going to have a conversation with the chief

86
00:06:58.818 --> 00:07:03.745
innovation officer at macomb's consulting on. June twenty ninth of june. And then

87
00:07:03.745 --> 00:07:08.673
let's go ahead and let that cook. In this case I'm going to use medium reasoning.

88
00:07:08.673 --> 00:07:13.600
And then I'm going to just do this on fast. Just to call out, really quickly. Depending

89
00:07:13.600 --> 00:07:18.527
on the level of complexity of the use case. You're going to want to make sure that

90
00:07:18.527 --> 00:07:23.455
you're kind of adjusting what models you're using. The kind of analogy that I'll

91
00:07:23.455 --> 00:07:28.382
always use is that you never want to use a sledgehammer for a nail. Right so there's

92
00:07:28.382 --> 00:07:33.309
some instances where low effort and medium effort make a lot of sense. And then

93
00:07:33.309 --> 00:07:38.236
they're going to be other instances where high effort or yeah extra high effort

94
00:07:38.236 --> 00:07:43.164
might make more sense. I typically will use high effort and extra high for planning.

95
00:07:43.164 --> 00:07:48.091
So just to show you really quickly. You also have the ability to use this planning

96
00:07:48.091 --> 00:07:53.018
function which just do backslash. Oops, that's a high spell plan. So you also have

97
00:07:53.018 --> 00:07:57.945
the ability to use this planning function called plan mode where it'll also Codex

98
00:07:57.945 --> 00:08:02.873
will also just kind of figure out. Okay, what are the you know? Ten to fifteen

99
00:08:02.873 --> 00:08:07.800
to twenty steps. That we should complete to execute this particular task. But again,

100
00:08:07.800 --> 00:08:12.727
I'll typically use extra high or high with planning just to figure out. What should

101
00:08:12.727 --> 00:08:17.655
the overall plan be? And then I'll come back and use medium or low effort to actually

102
00:08:17.655 --> 00:08:22.582
execute on that plan. That way, it's a lot more efficient. Because again, you don't

103
00:08:22.582 --> 00:08:27.509
necessarily need, you know, high or extra high to actually do that. Execution once

104
00:08:27.509 --> 00:08:32.436
you've already built out a well executable plan. All right, so let's go ahead and

105
00:08:32.436 --> 00:08:37.364
run. This one. So again I'm saying please update the contract start date to december

106
00:08:37.364 --> 00:08:42.291
twenty fifth. And then we're going to have a conversation with the chief innovation

107
00:08:42.291 --> 00:08:47.218
officer, and becomes consulting. On june twenty ninth of june. But we have one

108
00:08:47.218 --> 00:08:52.145
last thing that I'll call out. Is that you'll notice that I used the dictation

109
00:08:52.145 --> 00:08:57.073
function for this as well, so I'm typically almost never typing in Codex anymore,

110
00:08:57.073 --> 00:09:02.000
I'm typically just using our dictation function. And as a result my ability to

111
00:09:02.000 --> 00:09:06.927
type quickly has. Significantly degraded all right so let's go ahead and see what

112
00:09:06.927 --> 00:09:11.855
this looks like. All right, so this will probably take about twenty, thirty seconds

113
00:09:11.855 --> 00:09:16.782
or so. But let's pop back over, and you can see again. We were saying, we want

114
00:09:16.782 --> 00:09:21.709
to move this to december twenty fifth. And then we also want to update the next

115
00:09:21.709 --> 00:09:26.636
steps. Great, so you can see that it's using our Salesforce account updates workflow.

116
00:09:26.636 --> 00:09:31.564
So one thing I wanted to call out is that I did not explicitly ask it. To use that

117
00:09:31.564 --> 00:09:36.491
skill, one thing Codex is excellent at is what we call disambiguation. So it's

118
00:09:36.491 --> 00:09:41.418
great at figuring out okay what? Tools, or what skills could I use? That will help

119
00:09:41.418 --> 00:09:46.345
me resolve this particular workflow resolve. This particular challenge, so yeah,

120
00:09:46.345 --> 00:09:51.273
if your task is ambiguous, it'll just kind of solve for that. With its own reasoning.

121
00:09:51.273 --> 00:09:56.200
Great, all right, so it's gone ahead and said. It updated and verified that macomb's

122
00:09:56.200 --> 00:10:01.127
consulting demo update. It changed the contract. Start date to december, twenty

123
00:10:01.127 --> 00:10:06.055
fifth. And updated the next steps. So let's go back and see whether it did that

124
00:10:06.055 --> 00:10:10.982
we'll go ahead and refresh our opportunity here. And voila, we could see that it's

125
00:10:10.982 --> 00:10:15.909
updated, updated. The contract start date due december twenty. Fifth. And it's

126
00:10:15.909 --> 00:10:20.836
updated our next steps to we are going to have a conversation with the chief innovation

127
00:10:20.836 --> 00:10:25.764
officer comes consulting. On june twenty ninth. So again super powerful like I

128
00:10:25.764 --> 00:10:30.691
mentioned it's really helpful right to be able to. Do this just with one account.

129
00:10:30.691 --> 00:10:35.618
But the power really shows up when you're able to do this. Across twenty five or

130
00:10:35.618 --> 00:10:40.545
forty accounts at the same time, right? But then, one other really powerful thing

131
00:10:40.545 --> 00:10:45.473
that I wanted to show you is the ability to use this via Codex mobile. So I'm just

132
00:10:45.473 --> 00:10:50.400
going to pull out my phone here really quickly. As you can see, and again, like

133
00:10:50.400 --> 00:10:55.327
I said, I hardly do much typing these days, I'm mostly just using voice or using

134
00:10:55.327 --> 00:11:00.255
dictation to make a lot of these updates these days. So, but not only that, but

135
00:11:00.255 --> 00:11:05.182
I'm doing like a lot of this. On the go these days. So a lot of these updates are

136
00:11:05.182 --> 00:11:10.109
being made from my bed or via park bench or a treadmill, so I just want to show

137
00:11:10.109 --> 00:11:15.036
you again how how powerful a Codex mobile has gotten. So I'm going to go ahead

138
00:11:15.036 --> 00:11:19.964
and say. Please update the close date to december twenty fifth. As well, and then

139
00:11:19.964 --> 00:11:24.891
let's make the contract start date. Or sorry let's keep the contract start date.

140
00:11:24.891 --> 00:11:29.818
As is, and make the contract end. Date. January. First of january. Twenty twenty

141
00:11:29.818 --> 00:11:34.745
seven. And then let's also remove those next steps. That we made previously. And

142
00:11:34.745 --> 00:11:39.673
change it to the chief ai officer, and let's have that conversation. With the chief

143
00:11:39.673 --> 00:11:44.600
ai officer on july second. Cool, so we're going to go ahead and send that. I know

144
00:11:44.600 --> 00:11:49.527
you can't see my screen but it's. Doing everything that you would imagine it would

145
00:11:49.527 --> 00:11:54.455
do. Within Codex it's talking to Salesforce. It's thinking through the different

146
00:11:54.455 --> 00:11:59.382
next steps, that I provided it right now. It's doing a lot of this manually right.

147
00:11:59.382 --> 00:12:04.309
But I could also, just as easily point out a slack channel pointing out a email

148
00:12:04.309 --> 00:12:09.236
thread pointed at gong. Drop in a transcript from a previous call, and it'll make

149
00:12:09.236 --> 00:12:14.164
all of these updates automatically without me having to again speaking to my phone.

150
00:12:14.164 --> 00:12:19.091
Or use the dictate function. Ah via. Via Codex desktop app. All right, so it's

151
00:12:19.091 --> 00:12:24.018
told me that it's gone ahead. And made those updates on my phone so I'm just going

152
00:12:24.018 --> 00:12:28.945
to go ahead and refresh. One more time just so you can see how powerful Codex mobile

153
00:12:28.945 --> 00:12:33.873
is. And voila, it's made all of those updates. So I could have been anywhere. I

154
00:12:33.873 --> 00:12:38.800
just happen to be in front of my computer this time. But you saw my hands I wasn't

155
00:12:38.800 --> 00:12:43.727
touching my computer. I could have been walking around the office. I could have

156
00:12:43.727 --> 00:12:48.655
been at my home, I could have been on the train if I had wi-fi, and I was above

157
00:12:48.655 --> 00:12:53.582
ground. But yeah you can be anywhere with Codex mobile now. And make incredibly

158
00:12:53.582 --> 00:12:58.509
powerful changes across a number of different applications. So just wanted to show

159
00:12:58.509 --> 00:13:03.436
that as well. But that's the end of my demo, I hope. This was helpful, I hope you

160
00:13:03.436 --> 00:13:08.364
could find number of different use cases. The last thing I'll say here is that.

161
00:13:08.364 --> 00:13:13.291
Obviously this demos was specific to Salesforce. But you could do this with virtually

162
00:13:13.291 --> 00:13:18.218
any application that could be connected to Codex. That has write permissions right?

163
00:13:18.218 --> 00:13:23.145
So the possibilities become a little bit endless in terms of what you could actually

164
00:13:23.145 --> 00:13:28.073
do. If this technology, so I hope this was helpful. And I hope you start to find

165
00:13:28.073 --> 00:13:33.000
your own use cases.

+ Read More

Sign in or Join the community

![OpenAI Academy](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-black-monoblossom-743de6c6-b680-4334-8cd5-fee30f7a2202-1739890376705.png?fit=scale-down&width=100)

Create an account

Like

## Watch More

[31:00](/en/public/videos/recording-make-work-flow-automate-crm-updates-with-codex-2026-06-18)

[Recording: Make Work Flow: Automate CRM Updates with Codex](/en/public/videos/recording-make-work-flow-automate-crm-updates-with-codex-2026-06-18)

Posted Jun 18, 2026 | Views 79

# Codex for Work

# Use Cases

# Activators

[11:00](/en/public/videos/workflow-clip-proactively-monitor-accounts-with-codex-2026-06-12)

[Workflow clip: Proactively monitor accounts with Codex](/en/public/videos/workflow-clip-proactively-monitor-accounts-with-codex-2026-06-12)

Posted Jun 12, 2026 | Views 79

# Codex for Work

# Activators

# Use Cases

[3:00](/en/public/videos/confidence-scoring-and-skill-hardening-with-codex-2026-06-18)

[Confidence scoring and skill hardening with Codex](/en/public/videos/confidence-scoring-and-skill-hardening-with-codex-2026-06-18)

Posted Jun 18, 2026 | Views 89

# Codex

# champions

# AI Techniques

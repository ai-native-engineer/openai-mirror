<!-- source: https://academy.openai.com/public/clubs/champions-ecqup/videos/recording-make-work-flow-automate-crm-updates-with-codex-2026-06-18 -->

[Champions](/en/public/clubs/champions-ecqup/overview)

[navigation.content](/en/public/clubs/champions-ecqup/content)

Sign in or Join the community to continue

Get Started

# Recording: Make Work Flow: Automate CRM Updates with Codex

Posted Jun 18, 2026 | Views 79

# Codex for Work

# Use Cases

# Activators

Share

## SUMMARY

Make Work Flow is our series showcasing how Activators build AI-powered workflows that help their teams get real work done. In this session, Bryant Mccombs (Account Director, OpenAI) shares how he uses Codex to reduce the manual effort involved in keeping CRM records up to date. He will walk through a workflow for turning information from everyday work into cleaner, more consistent system updates. Attendees will learn how similar approaches can help reduce repetitive data entry, improve record quality, and create more time for higher-value work.

+ Read More

## TRANSCRIPT

1
00:00:00.000 --> 00:00:05.552
Kenna Valdez: Hello everyone, good morning, good afternoon, good evening. Whatever

2
00:00:05.552 --> 00:00:11.103
it may be for you, thank you for hopping on and joining us today. I'm going to

3
00:00:11.103 --> 00:00:16.655
pause for just one minute before we get started to give you all a chance to to

4
00:00:16.655 --> 00:00:22.207
get connected. To the call I still see folks trickling in while we're waiting.

5
00:00:22.207 --> 00:00:27.759
Please feel free to share what you had or are going to have. Depending on what

6
00:00:27.759 --> 00:00:33.310
time it is for you. For breakfast this morning, even if it's just coffee. Let me

7
00:00:33.310 --> 00:00:38.862
know how you take your coffee. And we can talk about why breakfast is important.

8
00:00:38.862 --> 00:00:44.414
In the community after the call today. All right. I see a little bit of a pause,

9
00:00:44.414 --> 00:00:49.966
so I'm going to go ahead and kick things off. Because I think folks have had a

10
00:00:49.966 --> 00:00:55.517
chance to get connected. Welcome to make work flow. This is our series focused

11
00:00:55.517 --> 00:01:01.069
on showcasing how real ai activators. The people who are designing, integrating,

12
00:01:01.069 --> 00:01:06.621
and scaling ai workflows for their teams do just that. So we'll share how members

13
00:01:06.621 --> 00:01:12.172
of all kinds of different teams at open ai across functions built real work flows

14
00:01:12.172 --> 00:01:17.724
to help with the work. That their teams actually do. So, whether or not you call

15
00:01:17.724 --> 00:01:23.276
yourself, or think of yourself as an ai champion. Yet the series is meant to give

16
00:01:23.276 --> 00:01:28.828
you real examples of useful workflows that you can take back and adapt to your

17
00:01:28.828 --> 00:01:34.379
team. And the tips to help you design, build and introduce those workflows safely

18
00:01:34.379 --> 00:01:39.931
and effectively. There's a couple housekeeping items this session is being recorded.

19
00:01:39.931 --> 00:01:45.483
And the presentation will be shared in the champion community. On open ai academy,

20
00:01:45.483 --> 00:01:51.034
where you most likely signed up to attend this event. So you've already are probably

21
00:01:51.034 --> 00:01:56.586
familiar. I will be in chat. Throughout the session my name is kenna christine,

22
00:01:56.586 --> 00:02:02.138
and I are part of the champion programs. Team over here at open ai. So please raise

23
00:02:02.138 --> 00:02:07.690
your questions to us. There, in chat, and we'll use the second half of the session

24
00:02:07.690 --> 00:02:13.241
today. To answer, as many of your questions as we can. But now I want to go ahead

25
00:02:13.241 --> 00:02:18.793
and introduce bryant. Because in this session bryant's going to share us with us.

26
00:02:18.793 --> 00:02:24.345
How he uses Codex to keep up with the important context around his accounts more

27
00:02:24.345 --> 00:02:29.897
proactively and build and update CRM to do so. So I'll go ahead and stop my share.

28
00:02:29.897 --> 00:02:35.448
Bryant, and give you a moment to introduce yourself a little better to the group.

29
00:02:35.448 --> 00:02:41.000
And then we'll dive into the workflow you built.

30
00:02:41.000 --> 00:02:45.300
Bryant McCombs: Sounds like plan. How's it going everyone? My name is Bryant McCombs.

31
00:02:45.300 --> 00:02:49.600
I'm an account director here. At OpenAI I've been with OpenAI for about two years,

32
00:02:49.600 --> 00:02:53.900
primarily working with our large enterprise customers, helping them build out their

33
00:02:53.900 --> 00:02:58.200
ai strategies with our technology. And then in my spare time of. There is so much

34
00:02:58.200 --> 00:03:02.500
of um. I will typically work with our internal teams to figure out how we could

35
00:03:02.500 --> 00:03:06.800
use OpenAI technology to make our sales team more innovative as well. So really

36
00:03:06.800 --> 00:03:11.100
excited, just kind of walk through some of the workflows that I found to be incredibly

37
00:03:11.100 --> 00:03:15.400
valuable. And just kind of talk through how we've built them. And then demo them

38
00:03:15.400 --> 00:03:19.700
and hopefully you walk away with something that you could also implement within

39
00:03:19.700 --> 00:03:24.000
your own organization. So let me go ahead and share my screen.

40
00:03:24.000 --> 00:03:30.000
Kenna Valdez: People are already excited pray. We're getting lots of applause.

41
00:03:30.000 --> 00:03:34.500
Bryant McCombs: All right. Can everyone see my screen. Because everyone looking

42
00:03:34.500 --> 00:03:39.000
into a white void currently.

43
00:03:39.000 --> 00:03:44.333
Kenna Valdez: We're getting a little lag, but that's normal. So make sure we've

44
00:03:44.333 --> 00:03:49.667
got this feature online before I. Like to take things and run. Or not seeing your

45
00:03:49.667 --> 00:03:55.000
screen just yet.

46
00:03:55.000 --> 00:03:58.000
Bryant McCombs: It, said, servoir. So let's just try that one more time.

47
00:03:58.000 --> 00:04:05.000
Kenna Valdez: Okay.

48
00:04:05.000 --> 00:04:06.000
Bryant McCombs: How about now?

49
00:04:06.000 --> 00:04:08.000
Kenna Valdez: There we go.

50
00:04:08.000 --> 00:04:12.567
Bryant McCombs: Perfect. All right, so really just want to kind of dig into kind

51
00:04:12.567 --> 00:04:17.134
of like the before. And after, before I jump into the build. So as you can see

52
00:04:17.134 --> 00:04:21.701
before I was very sad. Codex was not really involved in the process. As you can

53
00:04:21.701 --> 00:04:26.269
see right, so every customer interaction, every node, every email. It was all being

54
00:04:26.269 --> 00:04:30.836
done manually on my own. So first, I would have this customer interaction, which

55
00:04:30.836 --> 00:04:35.403
again could be a live customer. Call it could be an email thread. It could be some

56
00:04:35.403 --> 00:04:39.970
sort of slack exchange, or maybe just a quick internal conversation. And then I

57
00:04:39.970 --> 00:04:44.537
had to capture the notes from that interaction, so I would have to take those raw

58
00:04:44.537 --> 00:04:49.104
notes. And then turn those into something useful. So I would have to understand

59
00:04:49.104 --> 00:04:53.672
what changed maybe. Across the account I'd have to understand who said what? What

60
00:04:53.672 --> 00:04:58.239
was confirmed in a conversation, what was just kind of like my own internal interpretation

61
00:04:58.239 --> 00:05:02.806
versus what was just. Something that may have hap pened on the call. And then I

62
00:05:02.806 --> 00:05:07.373
had to turn those notes into some sort of follow up communication. So again that

63
00:05:07.373 --> 00:05:11.940
maybe that was email, maybe that was slack, but it had to be turned into something

64
00:05:11.940 --> 00:05:16.507
actionable that could be shared with some sort of internal or external stakeholder.

65
00:05:16.507 --> 00:05:21.075
And then I would have to dig through Salesforce to kind of figure out. Okay, what

66
00:05:21.075 --> 00:05:25.642
are the fields, what are the objects that need to be updated for? Again, my internal

67
00:05:25.642 --> 00:05:30.209
stakeholders to have a sense of what's actually happening across these accounts.

68
00:05:30.209 --> 00:05:34.776
So I know some of this. Probably sounds a little bit simple for folks right? But

69
00:05:34.776 --> 00:05:39.343
this is where a lot of kind of CRM hygiene tends to break down. It's where you

70
00:05:39.343 --> 00:05:43.910
kind of hear that classic. Oh, I'll update it in Salesforce later. Right and so

71
00:05:43.910 --> 00:05:48.478
what Codex is allowed for me to do is be much more consistent. But then, also,

72
00:05:48.478 --> 00:05:53.045
just save me a ton of time, so I'm finding that it's typically saving me. Somewhere

73
00:05:53.045 --> 00:05:57.612
on average of like three to four hours per week. Again, as I'm updating a lot of

74
00:05:57.612 --> 00:06:02.179
these different accounts, there are some account directors at. Some have, you know,

75
00:06:02.179 --> 00:06:06.746
upwards of seventy accounts. There's been times in my career at open ai, where

76
00:06:06.746 --> 00:06:11.313
I've managed somewhere between twenty five and forty accounts. Right so, when you're

77
00:06:11.313 --> 00:06:15.881
updating these object? These objects, these fields, these notes across that many

78
00:06:15.881 --> 00:06:20.448
accounts. A lot of the context kind of gets lost and it's really difficult to rein

79
00:06:20.448 --> 00:06:25.015
consistent and updating all these different things. So that's where I found the

80
00:06:25.015 --> 00:06:29.582
majority of the value in the workflow that we're getting ready to walk through.

81
00:06:29.582 --> 00:06:34.149
And so, as you can see now, I'm very happy. Because Codex is resolving. I'd say

82
00:06:34.149 --> 00:06:38.716
the vast majority of this workflow today right? So, instead of me doing all these

83
00:06:38.716 --> 00:06:43.284
manual notes, these emails, these slacks digging through all of these disparate

84
00:06:43.284 --> 00:06:47.851
data sources for context. That I would then update within Salesforce again. Codex

85
00:06:47.851 --> 00:06:52.418
is looking across all of these disparate data sources, so maybe it's looking at

86
00:06:52.418 --> 00:06:56.985
a call recording or maybe it's looking at an email thread or maybe it's looking

87
00:06:56.985 --> 00:07:01.552
at a slack conversation between myself. And either an internal or external contact.

88
00:07:01.552 --> 00:07:06.119
And then it's aggregating all that information. And then, figuring out where in

89
00:07:06.119 --> 00:07:10.687
Salesforce it actually needs to update these specific fields. So, for example,

90
00:07:10.687 --> 00:07:15.254
I can get off of a customer call. And they could say something like yeah, we're

91
00:07:15.254 --> 00:07:19.821
ready to move forward with this contract. And I could just update or upload that

92
00:07:19.821 --> 00:07:24.388
transcript into Codex and Codex will parse through that transcript and it'll say

93
00:07:24.388 --> 00:07:28.955
oh, it sounds like that customer is ready to move forward, so I'm moving the opportunity

94
00:07:28.955 --> 00:07:33.522
stage for this particular opportunity. From from evaluation to contract and negotiation.

95
00:07:33.522 --> 00:07:38.090
And again, before, that was something that I would have to do. Manually dig through

96
00:07:38.090 --> 00:07:42.657
Salesforce, figure out how to update the field. Et cetera. And now I could do that.

97
00:07:42.657 --> 00:07:47.224
All in one fell swoop, the other thing that I want to call out is that on one account,

98
00:07:47.224 --> 00:07:51.791
this, or one on one opportunity, this can seem like it's not saving you. A ton

99
00:07:51.791 --> 00:07:56.358
of time. But imagine the ability to do this across forty accounts. All at the same

100
00:07:56.358 --> 00:08:00.925
time, right? So you could also do batch updates, which is where I think the value

101
00:08:00.925 --> 00:08:05.493
really starts to compound. So if you're just doing this for one account, yeah sure

102
00:08:05.493 --> 00:08:10.060
like I can go into a one account and say yeah update. These three or four fields,

103
00:08:10.060 --> 00:08:14.627
and I could do that in Salesforce, probably nearly as fast as I can do it. In Codex,

104
00:08:14.627 --> 00:08:19.194
right, it's Codex is probably going to take twenty thirty seconds to do that right?

105
00:08:19.194 --> 00:08:23.761
But then if I'm doing that across twenty five or forty accounts at the same time.

106
00:08:23.761 --> 00:08:28.328
Codex is going to be significantly faster than I would be able to. Kind of dig

107
00:08:28.328 --> 00:08:32.896
through Salesforce and update all those different fields and all those different

108
00:08:32.896 --> 00:08:37.463
objects. So again, that's why we're seeing a ton of value across the board. In

109
00:08:37.463 --> 00:08:42.030
account directors who've started to leverage this approach, and I'd say the biggest

110
00:08:42.030 --> 00:08:46.597
change that we're seeing is that again. Every I'd say pretty much. Every account

111
00:08:46.597 --> 00:08:51.164
director within open ai now is using some form of this particular use case. I'd

112
00:08:51.164 --> 00:08:55.731
say it's probably the most popular use case. Across our go-to-market team today

113
00:08:55.731 --> 00:09:00.299
and again it's completely changing the way that people work and making a significantly

114
00:09:00.299 --> 00:09:04.866
more efficient than we used to be. When it comes to all things Salesforce so. So

115
00:09:04.866 --> 00:09:09.433
I'll jump into the actual demo. But before I do anything that you want to jump

116
00:09:09.433 --> 00:09:14.000
in with kind of christine. All right great.

117
00:09:14.000 --> 00:09:16.000
Kenna Valdez: Good let's dive in.

118
00:09:16.000 --> 00:09:20.927
Bryant McCombs: All right, so just, really quickly. Just wanted to show you. Let's

119
00:09:20.927 --> 00:09:25.855
light over here. First a skill that I created so. The first thing that you're likely

120
00:09:25.855 --> 00:09:30.782
going to going to want to do is build something that's repeatable. So for those

121
00:09:30.782 --> 00:09:35.709
of you who are unfamiliar with the idea of a skill, it's essentially just kind

122
00:09:35.709 --> 00:09:40.636
of reusable instructions that you could use for templization, or some level of

123
00:09:40.636 --> 00:09:45.564
determination or determinism around. Rather so, say, for example, if you had a

124
00:09:45.564 --> 00:09:50.491
specific template or a specific field, that you always wanted to update in the

125
00:09:50.491 --> 00:09:55.418
same way. Skills are a great use case for something like that. So the first thing

126
00:09:55.418 --> 00:10:00.345
that I did for this particular skill was again I wanted to. One be very explicit

127
00:10:00.345 --> 00:10:05.273
around like you know what it's supposed to be doing right. So in this case, I told

128
00:10:05.273 --> 00:10:10.200
it that it's a an enterprise account director. With a responsibility to update

129
00:10:10.200 --> 00:10:15.127
Salesforce. And that its role was to translate those approved customer and internal

130
00:10:15.127 --> 00:10:20.055
account context into accurate and concise Salesforce updates. And then the next

131
00:10:20.055 --> 00:10:24.982
really important thing that I wanted to do was give it a sense of what its guardrail

132
00:10:24.982 --> 00:10:29.909
should be right. So whenever you're building out a skill, especially if it's something

133
00:10:29.909 --> 00:10:34.836
that has write permissions in this case. So for those of you who are unfamiliar,

134
00:10:34.836 --> 00:10:39.764
write permissions. It's basically just the ability to change information within

135
00:10:39.764 --> 00:10:44.691
whatever application that you're using. But if you're using something, or if you're

136
00:10:44.691 --> 00:10:49.618
building something that has write permissions, you want to make sure that you're

137
00:10:49.618 --> 00:10:54.545
still the write permissions. In the right guardrails into that particular use case,

138
00:10:54.545 --> 00:10:59.473
right so. And this could, in this case. I said that the workflow should not modify

139
00:10:59.473 --> 00:11:04.400
the opportunity. Amount should not modify the stage, should not modify the close

140
00:11:04.400 --> 00:11:09.327
date, forecast category. Without my explicit approval, right? So whenever you're

141
00:11:09.327 --> 00:11:14.255
building something where you know you're not sure what level of trust you have.

142
00:11:14.255 --> 00:11:19.182
In the workflow, quite yet. Or if there are things that just have kind of higher

143
00:11:19.182 --> 00:11:24.109
table stakes in terms of you know. The changes that you're making to them. If those

144
00:11:24.109 --> 00:11:29.036
are kind of like mission, critical fields that you're changing, you'll want to

145
00:11:29.036 --> 00:11:33.964
make sure that you're implementing some level of guardrails right? So, so that

146
00:11:33.964 --> 00:11:38.891
that was the next piece that I wanted to address. And then what I wanted to do

147
00:11:38.891 --> 00:11:43.818
is just kind of define what that output structure should look like. So. Obviously,

148
00:11:43.818 --> 00:11:48.745
within every organization there are certain norms, certain philosophies in terms

149
00:11:48.745 --> 00:11:53.673
of how certain either presentations or docs or sheets should actually look so.

150
00:11:53.673 --> 00:11:58.600
I want to tell also. Make sure that I explicitly call that out. In the output here

151
00:11:58.600 --> 00:12:03.527
as well. And so, for the output, I just talked about how yeah for account summary

152
00:12:03.527 --> 00:12:08.455
changes for opportunity changes. They should all look specific way. And so you

153
00:12:08.455 --> 00:12:13.382
could see. We then created this skill here, which is our Salesforce account. Update

154
00:12:13.382 --> 00:12:18.309
skill. And then what I'll typically do after I build, a skill is, I'll say okay.

155
00:12:18.309 --> 00:12:23.236
Given my role, what are some of the different use cases that I could potentially

156
00:12:23.236 --> 00:12:28.164
leverage? This skill for and then how can I use this to optimize my existing? Workflows.

157
00:12:28.164 --> 00:12:33.091
And so you never want to just use a skill just for one thing, right? So. There's

158
00:12:33.091 --> 00:12:38.018
a little bit of like duality here, right where? The narrower the skill is, the

159
00:12:38.018 --> 00:12:42.945
more performant. It's going to be right. So I would never recommend building a

160
00:12:42.945 --> 00:12:47.873
skill that just has like this. Really broad applicability, right? But then you

161
00:12:47.873 --> 00:12:52.800
also want to figure out okay? Once I've built this skill, that is like pretty narrowly

162
00:12:52.800 --> 00:12:57.727
focused like what else can I actually do with it? Right so what else could it potentially

163
00:12:57.727 --> 00:13:02.655
be helpful for so. In this case it's also calling out that for this narrowly built

164
00:13:02.655 --> 00:13:07.582
skill it could also be really helpful for post meeting Salesforce cleanup. It could

165
00:13:07.582 --> 00:13:12.509
be helpful for pre forecast account. Hygiene for customer threads here I'm translation,

166
00:13:12.509 --> 00:13:17.436
MEDDIC refreshes task creation et cetera. So again, it's not like a one size fits

167
00:13:17.436 --> 00:13:22.364
all skill. But it can also be incredibly valuable across a number of other use

168
00:13:22.364 --> 00:13:27.291
cases as well. And then the last thing I want to call out was that whenever you've

169
00:13:27.291 --> 00:13:32.218
built a skill, you could also strengthen that skill by having it also. Either call

170
00:13:32.218 --> 00:13:37.145
other skills, or call other plugins or MCPs. That could also make that skill more

171
00:13:37.145 --> 00:13:42.073
valuable. So in this case I also wanted to ask it. Okay, what are some of the additional

172
00:13:42.073 --> 00:13:47.000
skills or plugins or MCPs? That I could also incorporate with a skill to make this

173
00:13:47.000 --> 00:13:51.927
workflow even stronger. And so, in this case it came back and said. Actually yeah,

174
00:13:51.927 --> 00:13:56.855
you could probably use a Salesforce plugin that would make this skill stronger,

175
00:13:56.855 --> 00:14:01.782
or you could use a gmail or outlook skill that could make this stronger or a slacker

176
00:14:01.782 --> 00:14:06.709
teams basically. It's looking across all of the different contexts that's available

177
00:14:06.709 --> 00:14:11.636
to it. And saying okay, if you connected all of these other data sources, you could

178
00:14:11.636 --> 00:14:16.564
make the skill even more valuable or more impactful. And then the last, last thing

179
00:14:16.564 --> 00:14:21.491
that I want to show you is that you could also automate these skills as well, or

180
00:14:21.491 --> 00:14:26.418
automate these workflows as well. So in this case I wanted to say okay great. I

181
00:14:26.418 --> 00:14:31.345
would love to automate this. So let's plan to run this every friday. At four pm.

182
00:14:31.345 --> 00:14:36.273
And then, if it's missing any context, just let me know. And I will provide that

183
00:14:36.273 --> 00:14:41.200
context that way. You can make sure that you're able to update anything else within

184
00:14:41.200 --> 00:14:46.127
Salesforce. All right, so let's move on to the demo. Just so you can kind of see

185
00:14:46.127 --> 00:14:51.055
what this looks like. Live. All right great so. What we're going to look at is

186
00:14:51.055 --> 00:14:55.982
just the ability for Codex to help. An account team update a Salesforce opportunity.

187
00:14:55.982 --> 00:15:00.909
So I'm just going to pop back over here, and you can see. In this case, we have

188
00:15:00.909 --> 00:15:05.836
this kind of makeshift Salesforce, or demo Salesforce Salesforce account called

189
00:15:05.836 --> 00:15:10.764
macomb's consulting. And then we have our demo opportunity. We have the ability

190
00:15:10.764 --> 00:15:15.691
to change a number of different fields here, so we could change the stage. We could

191
00:15:15.691 --> 00:15:20.618
change the forecast category, we could change the dollar amount. The close date.

192
00:15:20.618 --> 00:15:25.545
When does the contract start? When does the contract end next steps? Et cetera

193
00:15:25.545 --> 00:15:30.473
right? So let's pop back over to Salesforce, and you can see right now. We have

194
00:15:30.473 --> 00:15:35.400
it in the evaluation stage. We have a dollar amo unt of about two hundred and forty

195
00:15:35.400 --> 00:15:40.327
k. We have a closed date of september thirtieth. Of september. We have no contract.

196
00:15:40.327 --> 00:15:45.255
Start date and we have no contract end. Date. And then we have no next steps, which

197
00:15:45.255 --> 00:15:50.182
is a big no, no. Here, at OpenAI. So we're going to make sure we get those things

198
00:15:50.182 --> 00:15:55.109
updated so that our internal stakeholders have a better sense of what's happening

199
00:15:55.109 --> 00:16:00.036
across this opportunity. So let's go ahead and pop back over to Codex. And I'm

200
00:16:00.036 --> 00:16:04.964
going to say please update the contract, start date to december, twenty fifth of

201
00:16:04.964 --> 00:16:09.891
december, twenty, twenty six. That's easy enough date to remember. And then for

202
00:16:09.891 --> 00:16:14.818
the next steps let's say that we're going to have a conversation with the chief

203
00:16:14.818 --> 00:16:19.745
innovation officer at macomb's consulting on. June twenty ninth of june. And then

204
00:16:19.745 --> 00:16:24.673
let's go ahead and let that cook. In this case I'm going to use medium reasoning.

205
00:16:24.673 --> 00:16:29.600
And then I'm going to just do this on fast. Just to call out, really quickly. Depending

206
00:16:29.600 --> 00:16:34.527
on the level of complexity of the use case. You're going to want to make sure that

207
00:16:34.527 --> 00:16:39.455
you're kind of adjusting what models you're using. The kind of analogy that I'll

208
00:16:39.455 --> 00:16:44.382
always use is that you never want to use a sledgehammer for a nail. Right so there's

209
00:16:44.382 --> 00:16:49.309
some instances where low effort and medium effort make a lot of sense. And then

210
00:16:49.309 --> 00:16:54.236
they're going to be other instances where high effort or yeah extra high effort

211
00:16:54.236 --> 00:16:59.164
might make more sense. I typically will use high effort and extra high for planning.

212
00:16:59.164 --> 00:17:04.091
So just to show you really quickly. You also have the ability to use this planning

213
00:17:04.091 --> 00:17:09.018
function which just do backslash. Oops, that's a high spell plan. So you also have

214
00:17:09.018 --> 00:17:13.945
the ability to use this planning function called plan mode where it'll also Codex

215
00:17:13.945 --> 00:17:18.873
will also just kind of figure out. Okay, what are the you know? Ten to fifteen

216
00:17:18.873 --> 00:17:23.800
to twenty steps. That we should complete to execute this particular task. But again,

217
00:17:23.800 --> 00:17:28.727
I'll typically use extra high or high with planning just to figure out. What should

218
00:17:28.727 --> 00:17:33.655
the overall plan be? And then I'll come back and use medium or low effort to actually

219
00:17:33.655 --> 00:17:38.582
execute on that plan. That way, it's a lot more efficient. Because again, you don't

220
00:17:38.582 --> 00:17:43.509
necessarily need, you know, high or extra high to actually do that. Execution once

221
00:17:43.509 --> 00:17:48.436
you've already built out a well executable plan. All right, so let's go ahead and

222
00:17:48.436 --> 00:17:53.364
run. This one. So again I'm saying please update the contract start date to december

223
00:17:53.364 --> 00:17:58.291
twenty fifth. And then we're going to have a conversation with the chief innovation

224
00:17:58.291 --> 00:18:03.218
officer, and becomes consulting. On june twenty ninth of june. But we have one

225
00:18:03.218 --> 00:18:08.145
last thing that I'll call out. Is that you'll notice that I used the dictation

226
00:18:08.145 --> 00:18:13.073
function for this as well, so I'm typically almost never typing in Codex anymore,

227
00:18:13.073 --> 00:18:18.000
I'm typically just using our dictation function. And as a result my ability to

228
00:18:18.000 --> 00:18:22.927
type quickly has. Significantly degraded all right so let's go ahead and see what

229
00:18:22.927 --> 00:18:27.855
this looks like. All right, so this will probably take about twenty, thirty seconds

230
00:18:27.855 --> 00:18:32.782
or so. But let's pop back over, and you can see again. We were saying, we want

231
00:18:32.782 --> 00:18:37.709
to move this to december twenty fifth. And then we also want to update the next

232
00:18:37.709 --> 00:18:42.636
steps. Great, so you can see that it's using our Salesforce account updates workflow.

233
00:18:42.636 --> 00:18:47.564
So one thing I wanted to call out is that I did not explicitly ask it. To use that

234
00:18:47.564 --> 00:18:52.491
skill, one thing Codex is excellent at is what we call disambiguation. So it's

235
00:18:52.491 --> 00:18:57.418
great at figuring out okay what? Tools, or what skills could I use? That will help

236
00:18:57.418 --> 00:19:02.345
me resolve this particular workflow resolve. This particular challenge, so yeah,

237
00:19:02.345 --> 00:19:07.273
if your task is ambiguous, it'll just kind of solve for that. With its own reasoning.

238
00:19:07.273 --> 00:19:12.200
Great, all right, so it's gone ahead and said. It updated and verified that macomb's

239
00:19:12.200 --> 00:19:17.127
consulting demo update. It changed the contract. Start date to december, twenty

240
00:19:17.127 --> 00:19:22.055
fifth. And updated the next steps. So let's go back and see whether it did that

241
00:19:22.055 --> 00:19:26.982
we'll go ahead and refresh our opportunity here. And voila, we could see that it's

242
00:19:26.982 --> 00:19:31.909
updated, updated. The contract start date due december twenty. Fifth. And it's

243
00:19:31.909 --> 00:19:36.836
updated our next steps to we are going to have a conversation with the chief innovation

244
00:19:36.836 --> 00:19:41.764
officer comes consulting. On june twenty ninth. So again super powerful like I

245
00:19:41.764 --> 00:19:46.691
mentioned it's really helpful right to be able to. Do this just with one account.

246
00:19:46.691 --> 00:19:51.618
But the power really shows up when you're able to do this. Across twenty five or

247
00:19:51.618 --> 00:19:56.545
forty accounts at the same time, right? But then, one other really powerful thing

248
00:19:56.545 --> 00:20:01.473
that I wanted to show you is the ability to use this via Codex mobile. So I'm just

249
00:20:01.473 --> 00:20:06.400
going to pull out my phone here really quickly. As you can see, and again, like

250
00:20:06.400 --> 00:20:11.327
I said, I hardly do much typing these days, I'm mostly just using voice or using

251
00:20:11.327 --> 00:20:16.255
dictation to make a lot of these updates these days. So, but not only that, but

252
00:20:16.255 --> 00:20:21.182
I'm doing like a lot of this. On the go these days. So a lot of these updates are

253
00:20:21.182 --> 00:20:26.109
being made from my bed or via park bench or a treadmill, so I just want to show

254
00:20:26.109 --> 00:20:31.036
you again how how powerful a Codex mobile has gotten. So I'm going to go ahead

255
00:20:31.036 --> 00:20:35.964
and say. Please update the close date to december twenty fifth. As well, and then

256
00:20:35.964 --> 00:20:40.891
let's make the contract start date. Or sorry let's keep the contract start date.

257
00:20:40.891 --> 00:20:45.818
As is, and make the contract end. Date. January. First of january. Twenty twenty

258
00:20:45.818 --> 00:20:50.745
seven. And then let's also remove those next steps. That we made previously. And

259
00:20:50.745 --> 00:20:55.673
change it to the chief ai officer, and let's have that conversation. With the chief

260
00:20:55.673 --> 00:21:00.600
ai officer on july second. Cool, so we're going to go ahead and send that. I know

261
00:21:00.600 --> 00:21:05.527
you can't see my screen but it's. Doing everything that you would imagine it would

262
00:21:05.527 --> 00:21:10.455
do. Within Codex it's talking to Salesforce. It's thinking through the different

263
00:21:10.455 --> 00:21:15.382
next steps, that I provided it right now. It's doing a lot of this manually right.

264
00:21:15.382 --> 00:21:20.309
But I could also, just as easily point out a slack channel pointing out a email

265
00:21:20.309 --> 00:21:25.236
thread pointed at gong. Drop in a transcript from a previous call, and it'll make

266
00:21:25.236 --> 00:21:30.164
all of these updates automatically without me having to again speaking to my phone.

267
00:21:30.164 --> 00:21:35.091
Or use the dictate function. Ah via. Via Codex desktop app. All right, so it's

268
00:21:35.091 --> 00:21:40.018
told me that it's gone ahead. And made those updates on my phone so I'm just going

269
00:21:40.018 --> 00:21:44.945
to go ahead and refresh. One more time just so you can see how powerful Codex mobile

270
00:21:44.945 --> 00:21:49.873
is. And voila, it's made all of those updates. So I could have been anywhere. I

271
00:21:49.873 --> 00:21:54.800
just happen to be in front of my computer this time. But you saw my hands I wasn't

272
00:21:54.800 --> 00:21:59.727
touching my computer. I could have been walking around the office. I could have

273
00:21:59.727 --> 00:22:04.655
been at my home, I could have been on the train if I had wi-fi, and I was above

274
00:22:04.655 --> 00:22:09.582
ground. But yeah you can be anywhere with Codex mobile now. And make incredibly

275
00:22:09.582 --> 00:22:14.509
powerful changes across a number of different applications. So just wanted to show

276
00:22:14.509 --> 00:22:19.436
that as well. But that's the end of my demo, I hope. This was helpful, I hope you

277
00:22:19.436 --> 00:22:24.364
could find number of different use cases. The last thing I'll say here is that.

278
00:22:24.364 --> 00:22:29.291
Obviously this demos was specific to Salesforce. But you could do this with virtually

279
00:22:29.291 --> 00:22:34.218
any application that could be connected to Codex. That has write permissions right?

280
00:22:34.218 --> 00:22:39.145
So the possibilities become a little bit endless in terms of what you could actually

281
00:22:39.145 --> 00:22:44.073
do. If this technology, so I hope this was helpful. And I hope you start to find

282
00:22:44.073 --> 00:22:49.000
your own use cases.

283
00:22:49.000 --> 00:22:53.286
Kenna Valdez: Thank you so much, Bryant. We have a number of excellent questions,

284
00:22:53.286 --> 00:22:57.571
I think. One of which I'll start with, because it's related to the connection to

285
00:22:57.571 --> 00:23:01.857
Salesforce or whatever serum you're using. How did you think about defining the

286
00:23:01.857 --> 00:23:06.143
level of access? The skill has to salesforces. Is it just tied to your user access?

287
00:23:06.143 --> 00:23:10.429
I know you went over a couple of. Restrictions that you put around the updates

288
00:23:10.429 --> 00:23:14.714
that it makes. How did you kind of like think through that process and implement

289
00:23:14.714 --> 00:23:19.000
that.

290
00:23:19.000 --> 00:23:23.067
Bryant McCombs: Yeah, so it's a lot of it is kind of. At the abin level, right?

291
00:23:23.067 --> 00:23:27.133
So a lot of the decisions that are made around what I've actually what I actually

292
00:23:27.133 --> 00:23:31.200
have access to or made it. The abn level, but generally speaking, what we're finding

293
00:23:31.200 --> 00:23:35.267
most organizations are doing is that whatever a user currently has access to in

294
00:23:35.267 --> 00:23:39.333
terms of write permissions. And read permissions. They should likely have access

295
00:23:39.333 --> 00:23:43.400
to within Codex as well. Right, there's not necessarily a huge discernible difference

296
00:23:43.400 --> 00:23:47.467
between giving someone access manually to these fields. Versus giving access to

297
00:23:47.467 --> 00:23:51.533
these fields via Codex. So that's typically what we're seeing in some organizations

298
00:23:51.533 --> 00:23:55.600
obviously. There are going to be some nuances there where you know there are fields

299
00:23:55.600 --> 00:23:59.667
that people may not even realize. They have access to right. So making sure that

300
00:23:59.667 --> 00:24:03.733
you're doing an audit upfront as an admin and making sure that these folks aren't

301
00:24:03.733 --> 00:24:07.800
editing things that could have a critical impact. On the business obviously is

302
00:24:07.800 --> 00:24:11.867
really important. Due diligence to do upfront, but, generally speaking, whatever

303
00:24:11.867 --> 00:24:15.933
someone has access to currently is likely. Something that you should be comfortable

304
00:24:15.933 --> 00:24:20.000
giving them access to via Codex as well.

305
00:24:20.000 --> 00:24:24.778
Kenna Valdez: Yeah yeah definitely that's definitely a huge part of the. The workflow

306
00:24:24.778 --> 00:24:29.556
build portion of being an activator is partnering with your workspace, admin or

307
00:24:29.556 --> 00:24:34.333
any sort of stakeholders who are going to help make those governance decisions.

308
00:24:34.333 --> 00:24:39.111
So, just as a reminder, you're always building for your team. But within the system

309
00:24:39.111 --> 00:24:43.889
of your larger organization and and the the settings and configuration sort of

310
00:24:43.889 --> 00:24:48.667
permissions that you've been given to to all the different tools and and business

311
00:24:48.667 --> 00:24:53.444
processes that you have access to, related to that as well. We had some questions

312
00:24:53.444 --> 00:24:58.222
come in around traceability, so how do you track what? Changes were made by the

313
00:24:58.222 --> 00:25:03.000
skill and sales force.

314
00:25:03.000 --> 00:25:07.333
Bryant McCombs: Yeah, so we have opportunities, change fields generally. So, for

315
00:25:07.333 --> 00:25:11.667
the most part, for a count directors, we're mainly looking at the opportunity.

316
00:25:11.667 --> 00:25:16.000
Fields and account fields. But yeah, we have both a top opportunity. Field. Change

317
00:25:16.000 --> 00:25:20.333
fields or columns, and then also account field change columns as well. So I could

318
00:25:20.333 --> 00:25:24.667
also just build a report that can show everything. That Bryant McCombs has changed

319
00:25:24.667 --> 00:25:29.000
over the course of a month, either on the account level or the opportunity level.

320
00:25:29.000 --> 00:25:33.333
So yeah I'd say that's the best way to kind of trace it but yeah again that's typically

321
00:25:33.333 --> 00:25:37.667
happening with our sales ops or revenue operations teams to just make sure that

322
00:25:37.667 --> 00:25:42.000
we're being compliant.

323
00:25:42.000 --> 00:25:47.000
Kenna Valdez: Great, and what was that confidence? Score?

324
00:25:47.000 --> 00:25:51.286
Bryant McCombs: That's something that I've just kind of built out on my own. So

325
00:25:51.286 --> 00:25:55.571
over time I've kind of developed my own. Just like confidence. Score for any output

326
00:25:55.571 --> 00:25:59.857
from either ChatGPT or Codex. But it's basically if you. As, like you as encodex,

327
00:25:59.857 --> 00:26:04.143
or you, as in ChatGPT, are not one hundred percent. Confident in the answer, just

328
00:26:04.143 --> 00:26:08.429
tell me why. So give me like a better sense of okay. These are the things that

329
00:26:08.429 --> 00:26:12.714
would give me one hundred percent confidence in. If it can just go, look at those

330
00:26:12.714 --> 00:26:17.000
things up. I'll have, like a follow-up prompt that says okay, great look. Those

331
00:26:17.000 --> 00:26:21.286
things up to make yourself one hundred percent confident. Or if it's external,

332
00:26:21.286 --> 00:26:25.571
facing communication or internal facing communication that I need to be. One hundred

333
00:26:25.571 --> 00:26:29.857
percent accurate. I'll say, just remove anything where you don't have. One hundred

334
00:26:29.857 --> 00:26:34.143
percent confidence until you get to one hundred percent confidence, but yeah it's

335
00:26:34.143 --> 00:26:38.429
basically it's not like a super like quantitative metric necessarily. It's more

336
00:26:38.429 --> 00:26:42.714
so okay like did you pull? In? Every necessary resource, and then, if not, like

337
00:26:42.714 --> 00:26:47.000
what assumptions are you making? Say that I could remove those assumptions.

338
00:26:47.000 --> 00:26:51.429
Kenna Valdez: Yeah, and that actually ties into the last question that I have.

339
00:26:51.429 --> 00:26:55.857
In the chat, and then we'll we'll wrap things up in terms of what exactly you review

340
00:26:55.857 --> 00:27:00.286
and approve. Have you ever thought about? And this sounds like part in part. The

341
00:27:00.286 --> 00:27:04.714
confidence score describing what steps you take to come to a judgment. And then,

342
00:27:04.714 --> 00:27:09.143
briefing Codex on that like exactly exact approach. So where do you kind of draw

343
00:27:09.143 --> 00:27:13.571
that line between? What the confidence score can tell you where you want to stop?

344
00:27:13.571 --> 00:27:18.000
And really have that that human review point.

345
00:27:18.000 --> 00:27:22.308
Bryant McCombs: No I love that so. We internally a lot of folks will call this

346
00:27:22.308 --> 00:27:26.615
skill hardening. So if you have a skill and it's working well like eighty five

347
00:27:26.615 --> 00:27:30.923
percent of the time, right? I think. What a lot of folks would expect is that you

348
00:27:30.923 --> 00:27:35.231
know just kind of leave. It, as is, and you get comfortable with that. Eighty five

349
00:27:35.231 --> 00:27:39.538
percent right. But I think what's. As we all kind of become builders, like as knowledge

350
00:27:39.538 --> 00:27:43.846
workers start to become builders. It's going to become incumbent upon us to have

351
00:27:43.846 --> 00:27:48.154
more of kind of like a iterative mindset when it comes to how we build these things

352
00:27:48.154 --> 00:27:52.462
right. So what I'll typically do is I'll just say okay great. This is a great output

353
00:27:52.462 --> 00:27:56.769
in the future. Here are three or four things that I would like you to kind of.

354
00:27:56.769 --> 00:28:01.077
Consider, as a part of this skill going forward. And I'm just doing that over and

355
00:28:01.077 --> 00:28:05.385
over again. And then I found that the fidelity of these use cases, or of these

356
00:28:05.385 --> 00:28:09.692
skills over time, is just significantly increased. So if you're willing to just

357
00:28:09.692 --> 00:28:14.000
kind of like put in the work with some of these skills and say, I'll give an example.

358
00:28:14.000 --> 00:28:18.308
I have, like a email triage skill, right that responds to all of my emails. Every

359
00:28:18.308 --> 00:28:22.615
morning, or at least creates drafts for all of my emails every morning. And I'd

360
00:28:22.615 --> 00:28:26.923
say, in the beginning I was editing a lot of these drafts right like I was like

361
00:28:26.923 --> 00:28:31.231
that's not how I sound or like, that's not how I'd respond to this particular situation.

362
00:28:31.231 --> 00:28:35.538
Et cetera, or it was being like overly formal. If it were like, you know someone

363
00:28:35.538 --> 00:28:39.846
internal, obviously slack. And then, maybe, like too informal with with an external

364
00:28:39.846 --> 00:28:44.154
stakeholder. So over time I've had to harden that skill, like I have like a. This

365
00:28:44.154 --> 00:28:48.462
is how bryant talk, skill, and I've had to harden that over time, and it's gotten

366
00:28:48.462 --> 00:28:52.769
significantly better to the point where I'd say like I've gone from editing. You

367
00:28:52.769 --> 00:28:57.077
know fifty percent of the drafts to now probably editing editing like you know

368
00:28:57.077 --> 00:29:01.385
twenty percent. Or, like fifteen percent of the draft. So again it's definitely

369
00:29:01.385 --> 00:29:05.692
going to become more incumbent upon us as builders. To continue to iterate on the

370
00:29:05.692 --> 00:29:10.000
things that we're building.

371
00:29:10.000 --> 00:29:14.200
Kenna Valdez: Yeah, completely agree. I think iteration is a normal part of the

372
00:29:14.200 --> 00:29:18.400
process, and we almost need to normalize it internally for ourselves. Have definitely

373
00:29:18.400 --> 00:29:22.600
gone through the same experience with both personal and and team prompts that I've

374
00:29:22.600 --> 00:29:26.800
built. It's not a prompt and done, it's definitely like you. Continue to provide

375
00:29:26.800 --> 00:29:31.000
feedback over time I.

376
00:29:31.000 --> 00:29:32.000
Bryant McCombs: Exactly.

377
00:29:32.000 --> 00:29:37.167
Kenna Valdez: Am going to go ahead and close this out with a few reminders today.

378
00:29:37.167 --> 00:29:42.333
Thank you all for joining us, we hope to you found today's session helpful, thank

379
00:29:42.333 --> 00:29:47.500
you, bryant, for sharing the build. How you think about skills? This was super

380
00:29:47.500 --> 00:29:52.667
super helpful to me, so hopefully. It was helpful to all of you. But, as a reminder,

381
00:29:52.667 --> 00:29:57.833
the champion community on open ai academy is your space to find more ai adoption

382
00:29:57.833 --> 00:30:03.000
insights, real examples like this one and resources to help you design them for

383
00:30:03.000 --> 00:30:08.167
your teams. And responsibly integrate them into your systems. So sign up for more.

384
00:30:08.167 --> 00:30:13.333
Make workflow sessions for more examples from real work. And our upcoming sessions

385
00:30:13.333 --> 00:30:18.500
we'll continue to share what adoption trends were observing, and what you can do

386
00:30:18.500 --> 00:30:23.667
about them. As an ai champion and finally as you build new ways of working for

387
00:30:23.667 --> 00:30:28.833
your team as you take this workflow and go and adapt it, please come back to the

388
00:30:28.833 --> 00:30:34.000
community and share what you can. In our use cases for them. I should always follow

389
00:30:34.000 --> 00:30:39.167
your company's security and privacy policies. But we would love to see what you

390
00:30:39.167 --> 00:30:44.333
build, and there's a chance to earn some swag in it for you. In our monthly activation

391
00:30:44.333 --> 00:30:49.500
challenge, so we'd love to learn more about your first Codex. Use cases. All right,

392
00:30:49.500 --> 00:30:54.667
everyone, thank you so much for joining us today. For make workflow, thank you,

393
00:30:54.667 --> 00:30:59.833
Bryant, for sharing and thank you for joining us again. And we hope to see you

394
00:30:59.833 --> 00:31:05.000
in the community.

+ Read More

Sign in or Join the community

![OpenAI Academy](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-black-monoblossom-743de6c6-b680-4334-8cd5-fee30f7a2202-1739890376705.png?fit=scale-down&width=100)

Create an account

## Watch More

[30:00](/en/public/videos/make-work-flow-proactively-monitor-accounts-with-codex-2026-06-12)

[Make Work Flow: Proactively monitor accounts with Codex](/en/public/videos/make-work-flow-proactively-monitor-accounts-with-codex-2026-06-12)

Posted Jun 12, 2026 | Views 79

# Codex for Work

# Activators

# Use Cases

[13:00](/en/public/videos/httpsvimeocom1202596507sharecopyandflsvandfeci)

[Workflow clip: Automate CRM updates with Codex](/en/public/videos/httpsvimeocom1202596507sharecopyandflsvandfeci)

Posted Jun 18, 2026 | Views 56

# Codex for Work

# Use Cases

# Activators

[3:00](/en/public/videos/confidence-scoring-and-skill-hardening-with-codex-2026-06-18)

[Confidence scoring and skill hardening with Codex](/en/public/videos/confidence-scoring-and-skill-hardening-with-codex-2026-06-18)

Posted Jun 18, 2026 | Views 89

# Codex

# champions

# AI Techniques

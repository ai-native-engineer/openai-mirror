<!-- source: https://openai.com/index/more-on-dota-2/ -->

August 16, 2017

[Milestone](/research/index/milestone/)

# More on Dota 2

![Person with headphones on, focused on playing Dota on a screen in front of them](https://images.ctfassets.net/kftzwdyauwt9/ba4575a3-7d89-40f5-8fea18a441d7/b86f86f6733d1b69561a8323fb382076/more-on-dota-2.jpg?w=3840&q=90&fm=webp)

Our Dota 2 result shows that self-play can catapult the performance of machine learning systems from far below human level to superhuman, given sufficient compute. In the span of a month, our system went from barely matching a high-ranked player to beating the top pros and has continued to improve since then. Supervised deep learning systems can only be as good as their training datasets, but in self-play systems, the available data improves automatically as the agent gets better.

![Chart 1](https://images.ctfassets.net/kftzwdyauwt9/f5a3cc18-6716-4c68-6e6f6a219382/9fb1e9e47b5349b2428c2addb1cb7c21/chart-1.png?w=3840&q=90&fm=webp)

[TrueSkill⁠(opens in a new window)](https://en.wikipedia.org/wiki/TrueSkill) rating (similar to the ELO rating in chess) of our best bot over time, computed by simulating games between the bots and observing the win ratios. Improvements came from every part of the system, from adding new features to algorithmic improvements to scaling things up. The graph is surprisingly linear, meaning the team improved the bot exponentially over time.

The project’s timeline is the following. For some perspective, 15% of players are below 1.5k [MMR⁠(opens in a new window)](https://dota.rgp.io/mmr/); 58% of players are below 3k; 99.99% are below 7.5k.

* **March 1st**: had our first classical reinforcement learning [results⁠(opens in a new window)](https://www.youtube.com/watch?v=5Fv2c4aNS2w&feature=youtu.be) in a simple Dota environment, where a Drow Ranger learns to kite a hardcoded Earthshaker.
* **May 8th**: 1.5k MMR tester says he’s been getting better faster than the bot.
* **Early June**: beat 1.5k MMR tester
* **June 30th**: winning most games against 3k MMR tester
* **July 8th**: barely get first [win⁠(opens in a new window)](https://www.youtube.com/watch?v=FBoUHay7XBI&feature=youtu.be&t=345) against 7.5k MMR semi-pro tester.
* **August 7th**: beat [Blitz⁠(opens in a new window)](http://wiki.teamliquid.net/dota2/Blitz) (6.2k former pro) 3–0, [Pajkatt⁠(opens in a new window)](http://wiki.teamliquid.net/dota2/Pajkatt) (8.5k pro) 2–1, and [CC&C⁠(opens in a new window)](http://wiki.teamliquid.net/dota2/CC%26C) (8.9k pro) 3–0. All agreed that Sumail would figure out how to beat it.
* **August 9th**: beat Arteezy (10k pro, top player) 10–0. He says Sumail could figure out this bot.
* **August 10th**: beat Sumail (8.3k pro, top 1v1 player) 6–0, who says it’s unbeatable. Plays the Aug 9th bot, where he goes 2–1.
* **August 11th**: beat Dendi (7.3k pro, former world champion, old-school crowd favorite) 2–0. Bot has 60% win rate versus August 10th bot.

## The task

The full game is 5v5, but 1v1 also [appears⁠(opens in a new window)](https://www.youtube.com/watch?v=KOlw9SYjr4c) in some [tournaments⁠(opens in a new window)](http://wiki.teamliquid.net/dota2/Dota_2_Asia_Championships/2017/Solo_Tournament#Rules). Our bot played under standard tournament rules—we did not add AI-specific simplifications to 1v1.

<!-- yt-inline:KOlw9SYjr4c -->
[![Miracle- vs Paparazzi - Finals Solo 1v1 Game 1 Shadow Fiend - DAC 2017](https://img.youtube.com/vi/KOlw9SYjr4c/hqdefault.jpg)](https://www.youtube.com/watch?v=KOlw9SYjr4c)

<details>
<summary>자막: Miracle- vs Paparazzi - Finals Solo 1v1 Game 1 Shadow Fiend - DAC 2017 (12:37)</summary>

[00:00]
was smoking when he was a TI, but I'm
fairly certain the 1v1 tournament a
denial does not actually count as a
kill.
And it's first to two kills, not first
to two deaths.
Oh, the courier.
Paparazzi with the leak going with the
two branches once again for one less
damage, but one more agility, one more
intel. And how massive is that?
Oh, what happened to his taunt?
Yeah, show me that taunt. There we go.
Miracle dish swag.
He's he's he's got the swagger. I hope
it automatically does it in the 1v1
after the kill. Cuz it's kind of like
it's a it's a team wipe. It's true
true true. The taunt does get triggered.
So, it's not always the players who
actually do it. It is an in-game
mechanic that can just automatically
trigger the taunt.
All right, let's see if Paparazzi
actually gets the block as well. It's
another thing which you kind of miss
about the Warcraft 3 version. It
actually spawned the creep wave after 30
seconds. So, you didn't have to wait the
entire time out like we are doing right

[00:01]
now. It was actually a hell of a lot
quicker.
Small things. It's the It's the little
things. Trying to think if there's
anything other than
anything else that's cool that you can
do in the match. I don't think we've
seen anything else.
Anyways, back to the radiant block. You
can't really manipulate anything cuz
you're not allowed to use You're not
allowed to use the jungle camps or any
creeps from inside the jungle. Um
Nope. I I always wanted like if someone
would be able to like like afford into
the later game like a shadow amulet and
then set a trap in the middle.
Yeah, right. It's uh it's expensive. Oh,
okay, Miracle. He lost the range creep.
That's good. No, we had that debate last
time. We had that debate during the
quarterfinals. It's good if you can get
the deny off. Yeah, but if you can't,
then the creep wave for Paparazzi is now
going to be held at the perfect
position. So, Miracle needs to get the
deny to make it work and he doesn't.
Creep goes to uh to Paparazzi. And now
Miracle's in a bit of a rough position
where he's going to struggle to get
control of the wave back again. Yeah,
Paparazzi has pulled the melee creeps to
the uphill. Even if Miracle times the
last hit right, he might not be able to

[00:02]
get the last hit, but Then again,
Paparazzi missed both of them. Oh, he's
taking so much damage. Oh my god, he is
not healthy on HP. And now he has to
fight into See, this is what happens
when you block. Yeah. And he's got the
race keeping in front. Now you got the
double wave coming the way of Miracle.
He doesn't have the race to fight with,
but Paparazzi's taking still a hell of a
lot of damage at this early point of the
game. Whoa. Okay.
So many creeps and he's not level two
yet, so he can't do anything about it.
Push the tower. Two tower damage. That's
what this comes down to or fight Miracle
underneath his own T1 tower. Not the
greatest in the world. Miracle does have
the extra armor when he's got this. And
Paparazzi can be careful not to take
damage from the tower. He's running out
of creeps. That's worth though. He got
the range creep deny. But now Miracle is
still farming underneath his own tower.
It's not easy to last hit as an SF with
four souls under your own tower though.
I think overall this is a pretty big win
for Paparazzi.
I think he got one range creep deny
versus the zero of Miracle. So, I would
value like range creep

[00:03]
two maybe as opposed to regular one.
Okay. So, he's at like four and three
versus five and one.
I guess it doesn't give you an extra
soul though. Yeah, we just keep rubber
banding the waves back and forward. This
one's going to sit a little bit cleaner
as Miracle okay. Oh, Miracle.
He lined them up beautifully. He was
ready for that. Please, he sells a tango
immediately after. And now he's going to
lose like four souls because of this. Oh
my god.
He actually is able to deny up to almost
the entire wave as well. He took three
out of those four in the creep wave and
three denies.
Paparazzi
Yeah, he he was definitely ready. I like
how he has tangos too. I haven't seen
too many other players go with tangos.
They just wants to go with salves.
They've always been doing the salves.
There's not going to be no consistent
regeneration. And now okay, quickly
Wraith is just establishes who's boss.
Well, you know Miracle's mana is at 48
versus Paparazzi who can triple Wraith.
Hello.
Ooh. And Miracle back to the safety of
the T1 tower.
And
At least he knows this is a best of
three. So, if Even if this SF match up

[00:04]
goes a little bit haywire, there's still
a second chance.
How was the
XP looking? Level four versus level
three and a half, I believe. Uh just shy
of the four of Paparazzi. But Miracle's
at least got a better position now with
the creep wave. No, he doesn't.
have his regeneration, however, which is
the bigger problem. He doesn't have mana
to uh prevent Paparazzi from going up
Oh, that was a whiff. Yeah, it was
attempted attempted cancel.
Miracle just moves back underneath the
tower. He's still getting the the denies
underneath the tower.
And Miracle needs a break here.
He has it. He has He has clarity.
Just Just don't lose it. Wraith Wraith
is on the way back into the soul world.
1v1s are stressful. Oh, another missed
Wraith. And that almost works for
Miracle because now he's able to deny up
that range creep in relative safety.
Turns for his own Wraith Wraith doesn't
actually hit most of the radiant creep
wave, so he doesn't lose that momentum
either. No sticks yet for either side.
Paparazzi going for the clarity Miracle.
Looks like you got one on Miracle.

[00:05]
Are they going to both chicken out and
just not try and hit the long range
Wraith or are they both going to try and
man up?
The only chicken out is Paparazzi. Oh,
no. Yeah.
He's got the These are donkeys.
Oh, nice dodge.
Bait it.
See, why don't actually come in closer?
Like Miracle still needs to just let the
con
Let the salve burn off.
Radiant vision is OP with the observer
ward strength. You really want to have
ward by night time by the way. This is
actually quite important.
Something Miracle might uh
Well, he's actually got salves like in
He's got two salves in his stash. He
could afford the observer ward if he
wanted. The courier just came back and
uh
Paparazzi is trashing Miracle in denies.
10 to three.
That's disgusting.
Hey, there's always Wraith to come back,
right?
Not if you have no mana.
Yeah, that is a problem. And you can't
use runes. You can't use bottle. This is
where the big level difference comes
into play. Level five versus level four

[00:06]
and a half. That's not even close in
level. Miracle again having to cop the
Wraith and the and a physical attack. I
mean he has a proper stick already. No
surprise factor there.
Yeah, and the full magic wand the on
Paparazzi.
clarity?
Yeah, he should be able to. Uh it's
night time, dude. And the observer
ward's on his hill. I don't actually
know if he sees it.
Now he does.
Just out of vision. He He could see him
turning like he does see him to try and
do the Wraith. Dude, Paparazzi has had
to play so many 1v1s to play like this.
It's It's
ridiculous how good he is
in this 1v1.
Miracle just has to hug the safety that
is his T1 tower. Build up his souls. Put
Paparazzi into a bad position and don't
let that clarity stop.
Okay, now now we're back to parity with
level five versus level five.
Oh, the Wraith is from Miracle.
Another range creep deny though. This
really start to add up. Level six versus
level five. Not that big of a deal
unless you skill Requiem at six, which
we haven't really seen too much cuz they
I believe expect this to go a little bit
longer. Yeah, it looks like it's going

[00:07]
to.
Still decent amount on the line. You
want to take a trophy home from this.
So, even if both these teams are unable
to claim victory of the entire on on the
entire of DAC,
they can still take home a trophy.
Obviously, Liquid are incapable of doing
that now.
IGV still in the running.
All right. Courier still in the run
again. Miracle is in desperate need of
of consumables.
No boots either. Both of them committed
heavily to regen. All right. So, they're
they're both basically finish up their
magic wands now. Dude, he is getting
trashed in denies. It was 10 to three.
That was 19 to three. Hey, it just takes
a good couple of Wraiths and you get
back into this. Obviously, Miracle needs
mana. If you were on Miracle's side, you
would see see the truth, Toby.
I probably would, but we'll live in
denial for now.
Just like Miracle.
He doesn't have any denies, man. That's
all Paparazzi's. 20 20 denies to three
denies. It's
Yeah.

[00:08]
Miracle does not earn this mid lane at
all. I think he probably Yeah, now he
definitely sees the clarity. Well,
Wraith number one. That's all he's got,
but Paparazzi still has five wand
charges, three tango charges, as well as
the salve. That's a lot to go for.
[Laughter]
Wonderful way to fill in the details of
Carle.
Glad that I'm even laughing at that. I
was like
I actually looked over to Miracle's face
when he wrote it. And he is totally
serious when he when he wrote that. Like
there wasn't even a smirk coming up on
his face when he did it.
They're in the zone.
Do you get in the zone when you play
Dota, Toby? Uh yeah, but my zone is one
of failure.
That's why I get into the zone of
commentary.
And when you do that, I won't notice
anything.
Like I actually gave myself burn
blisters on my feet
uh during the middle of a cast. I
actually burned my foot on the carpet

[00:09]
cuz I was just like
doing that little nervous thing when you
sit still
and managed to actually like burn a hole
in the bottom of my foot during the
middle of a cast. Didn't even notice.
Miracle trouble? It seems that if we go
on a side story, Miracle like somebody
gets in a lot of trouble.
This This time it's Miracle.
Need some boots, sir.
He does.
Cannot afford it.
Cuz now the deny count is 25
to three.
And Paparazzi has this in the bag as
long as he doesn't screw it up. That's
That's all he needs to do. And Miracle
okay.
He might need to refresh that observer
ward actually kind of soon. It's about
to expire.
Well, he should have the money for it.
See that net worth difference? It's
almost a thousand net worth difference
between the two.
And Paparazzi knows it.
I've heard some uh
different philosophies on like the boots
choice for Shadow Fiend. There's a lot
of different options you can go with at
this point. You can go Aquila to push a
tower. You can go casual buckler is mega

[00:10]
value because you're right-clicking a
lot. You can also go for
treads or phase. Phase pretty good at
chasing people down. Treads just
straight better on one-on-one man
fighting, depending on what you think's
going to happen. So, this is where it
gets maybe a little bit unorthodox.
Blade Mail owns in 1v1, too. Oh my god,
it is so good. Affording that is going
to be rather difficult, however. Like
the chain mail little the gun, like at
least that part can be bought. Like uh
Like that that'll help you in the in the
physical battle.
But when you've got half of the CS,
in fact, all the CS which is currently
missing from Miracle, if you took the
denies of Paparazzi, he's got 80 in
total. 81 in total against the 30
of Miracle, if you start counting up the
denies and and last hits. I need boots.
He needs something. But like right now
it's it's poverty versus riches. Yeah.
He sounds like that CM that got trashed
like 15 minutes in. I still don't have
my boots, guys. I died eight times. I
died eight times. I don't know what I'm
meant to do. Frostbite creep in the

[00:11]
jungle. Can you please buy the wards,
Dazzle? I need my boots.
I will purchase boots of speed.
Oh, man. This is getting uglier and
uglier. Yeah, like you wonder when's the
point where you say, "You know what? I
actually just have to TP back."
Uh I have to go back and just and TP TP
out. Like that's it.
You can double raise the next wave. Can
do it. Actually, I don't think he has
enough mana to do so. It looks like he
doesn't really want to miss that much.
He's got a clock coming in for
Paparazzi. So, he's going for the
resistance. So, Miracle's way back into
this is going to be through like that
quick bursting of razes if he can do it.
But he's building up uh stick charges.
11 of five. 11 is almost enough to
tickle a raze.
Yeah. 12 Oh, casual clock. Oh, wow.
That is actually pretty cool. He's not
going to be taking that much that many
right clicks. He's just going to go
straight for the max razes. It's that

[00:12]
man It's the only way Miracle can get
back into this. He's He's got to
actually trigger multiple razes and
Paparazzi is not going to let the damage
fly his way. Maybe this is where you
commit to like a blight stone though by
Miracle and just go for the straight
one-on-one. Okay, Miracle comes in
really really close. He's still only got
one one one shot up his sleeve and
Paparazzi will take it. The raze behind
the tower. Miracle knew it was falling
apart for him. That was
So, game one Game one is done. Miracle
actually like pushed his chair back at
the end of that. He's like, "Oh,
Okay, what do I do now?" You didn't
mention Maybe he thought the whole thing
was over. That one raze creep It didn't
serve him that well.

</details>


The bot operated off the following interfaces:

* **Observations:** Bot API features, which are designed to be the same set of features that humans can see, related to heroes, creeps, courier, and the terrain near the hero. The game is partially observable.
* **Actions:** Actions accessible by the bot API, chosen at a frequency comparable to humans, including moving to a location, attacking a unit, or using an item.
* **Feedback:** The bot received incentives for winning and basic metrics like health and [last hits⁠(opens in a new window)](https://dota2.gamepedia.com/Creep_control_techniques#Last-hitting).

We whitelisted a few dozen item builds that bots could use, and picked one for evaluation. We also separately trained the initial creep block using traditional RL techniques, as it happens before the opponent appears.

## The International

Our approach, combining small amounts of “coaching” with self-play, allowed us to massively improve our agent between the Monday and Thursday of The International. On Monday evening, Pajkatt won using an unusual item build (buying an early magic wand). We added this item build to the training whitelist.

Around 1pm on Wednesday, we tested the latest bot. The bot would lose a bunch of health in the first wave. We thought perhaps we needed to roll back, but noticed further gameplay was amazing, and the first wave behavior was baiting the other bots to be aggressive towards it. Further self-play fixed the issue, as the bot learned to counter the baiting strategy. In the meanwhile, we stitched it together with Monday’s bot for the first wave only, and completed the process twenty minutes before Arteezy showed up at 4pm.

After the Arteezy matches, we updated the creep block model, which increased TrueSkill by one point. Further training before Sumail’s match on Thursday increased TrueSkill by two points. Sumail pointed out that the bot had learned to cast razes out of the enemy’s vision. This was due to a mechanic we hadn’t known about: abilities cast outside of the enemy’s vision prevent the enemy from gaining a wand charge.

Arteezy also played a match against our 7.5k semi-pro tester. Arteezy was winning the whole game, but our tester still managed to surprise him with a strategy he’d learned from the bot. Arteezy remarked afterwards that this was a strategy that Paparazi had used against him once and was not commonly practiced.

Pajkatt beating Monday’s bot. Note he baits the bot into engaging, and uses regeneration (faerie fires and a magic wand) to heal up. The bot is generally very good at deciding who will win a fight, but it’s never played against someone with early wand before.

## Bot exploits

Though Sumail called the bot “unbeatable”, it can still be confused in situations very different from what it’s seen. We set up the bot at a LAN event at The International, where players played over 1,000 games to beat the bot by any means possible.

The successful exploits fell into three archetypes:

* **Creep pulling**: it’s possible to repeatedly attract the lane creeps into chasing you right when they spawn (between the bot’s tier 2 and tier 3 towers). You end up with dozens of creeps chasing you around the map, and eventually the bot’s tower dies via attrition.
* **Orb of venom + wind lace**: this gives you a big movement speed advantage over the bot at level 1 and allows for a quick first blood. You need to exploit this head start to kill the bot one more time.
* **Level 1 raze**: this requires a lot of skill, but several 6–7k MMR players were able to kill the bot at level 1 by successfully hitting 3–5 razes in a short span of time.

Fixing these issues for 1v1 would be similar to fixing the Pajkatt bug. But for 5v5, such issues aren’t exploits at all, and we’ll need a system which can handle totally weird and wacky situations it’s never seen.

## Infrastructure

We’re not ready to talk about agent internals—the team is focused on solving 5v5 first.

The first step in the project was figuring out how to run Dota 2 in the cloud on a physical GPU. The game gave an obscure error message on GPU cloud instances. But when starting it on Greg’s personal GPU desktop (which is the desktop brought onstage during the show), we noticed that Dota booted when the monitor was plugged in, but gave the same error message when unplugged. So we configured our cloud GPU instances to pretend there was a physical monitor attached.

Dota didn’t support custom dedicated servers at the time, meaning that running scalably and without a GPU was possible only with very slow software rendering. We then created a shim to stub out most OpenGL calls, except the ones needed to boot.

At the same time, we wrote a scripted bot—we needed a baseline for comparison (especially because the builtin bots don’t work well on 1v1) and to understand all the semantics of the [bot API⁠(opens in a new window)](https://developer.valvesoftware.com/wiki/Dota_Bot_Scripting). The scripted bot reaches 70 last hits in ten minutes on an empty lane, but still loses to reasonable humans. Our current best 1v1 bot reaches more like 97 (it destroys the tower before then, so we can only extrapolate), and the theoretical maximum is 101.

Bot playing versus [SirActionSlacks⁠(opens in a new window)](http://wiki.teamliquid.net/dota2/SirActionSlacks). The strategy of distracting the bot with a courier rush did not work.

## 5v5

1v1 is complicated, but 5v5 is an ocean of complexity. We know we’ll need to further push the limits of AI in order to solve it.

One well-established place to start is with behavioral cloning. Dota has about a million public matches a day. The replays for these matches are stored on Valve’s servers for two weeks. We’ve been downloading every expert-level replay since last November, and have amassed a dataset of 5.8M games (each game is about 45 minutes with 10 humans). We use [OpenDota⁠(opens in a new window)](https://www.opendota.com/) to discover these replays, and are donating $12k (10 years of their fundraising goal) to support the project.

We have many more ideas, and are [hiring⁠](/careers/) engineers (must be intrigued by machine learning, but need not be an expert) and researchers to help us make this happen. We thank Microsoft Azure and Valve for their support in this endeavor.

* [OpenAI Five](/research/index/?tags=openai-five)
* [Exploration & Games](/research/index/?tags=exploration-game)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)
* [Software & Engineering](/research/index/?tags=software-engineering)

## Author

## Related articles

![Scaling Laws For Reward Model Overoptimization](https://images.ctfassets.net/kftzwdyauwt9/a8801fe6-8892-472b-f746d1d9fb2d/547c46ed9a8a71e89efbb7a7963a8932/image-6.webp?w=3840&q=90&fm=webp)

[Scaling laws for reward model overoptimization

PublicationOct 19, 2022](/index/scaling-laws-for-reward-model-overoptimization/)

![Screenshot of a scene from Minecraft](https://images.ctfassets.net/kftzwdyauwt9/ef9fc360-1a5a-4ca3-5c25b83b3564/50c07940455cc86ef84d91526d9cf3e0/vpt.jpg?w=3840&q=90&fm=webp)

[Learning to play Minecraft with Video PreTraining

ConclusionJun 23, 2022](/index/vpt/)

![Techniques For Training Large Neural Networks](https://images.ctfassets.net/kftzwdyauwt9/62793de4-0f01-42fc-539325d9af36/bc1ac82499fc1dc43f59accdd31d0195/image-9.webp?w=3840&q=90&fm=webp)

[Techniques for training large neural networks

PublicationJun 9, 2022](/index/techniques-for-training-large-neural-networks/)

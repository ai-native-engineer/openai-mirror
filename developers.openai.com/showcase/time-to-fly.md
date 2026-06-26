<!-- source: https://developers.openai.com/showcase/time-to-fly/ -->

## Search developer resources

[← All projects](/showcase) 

![Time to Fly app screenshot](/showcase/time-to-fly.webp)

Description

Time to Fly is a cosmic logic puzzle built in Codex with GPT-5.5 and GPT Image 2. Players position planets along fixed orbits and set a rocket's launch angle, then use every planet's gravity to bend the rocket toward a distant galaxy across five increasingly difficult levels.

## Build notes

### Initial prompt

Copy prompt
 

Use @game-studio to build a game called "Time to Fly." [Optional: Use the provided reference images as inspiration for its visual direction.]

Create a polished cosmic logic puzzle where players guide a rocket into a distant galaxy by positioning planets and using their gravitational pull.

Each level presents a miniature solar system. Before launching, the player adjusts the rocket's launch angle and drags planets around their fixed circular orbits. Once launched, the rocket flies freely and its trajectory is altered by the gravitational field of each planet it encounters.

## Core Mechanics

- The game has five levels.
- Level N contains N planets, progressing from one planet in Level 1 to five planets in Level 5.
- Planets remain stationary after being positioned and do not move automatically.
- Players can drag each planet around its fixed orbit before launching.
- Players launch the rocket using a button or the spacebar.
- Do not show a trajectory preview.
- Every planet must be used to successfully complete its level.
- If the rocket misses the galaxy, it flies into space and the player can immediately retry.
- There are no lives or retry limits.

Each planet should have a consistent size, appearance, and gravitational strength throughout the game. Larger planets should exert a stronger pull across a larger area. The rocket's direction should change naturally based on its entry angle, distance from the planet, and the planet's gravitational strength.

Clearly visualize gravitational fields using refined glowing or pulsing effects, but keep the interface uncluttered and easy to understand.

## Level Design

Each level should have only a small number of valid solutions:

- Level 1: An approachable introduction using one planet.
- Level 2: Accessible, but requires deliberate positioning.
- Level 3: Introduces meaningful multi-planet planning.
- Level 4: A challenging orbital puzzle requiring careful sequencing.
- Level 5: A difficult final puzzle requiring precise use of all five planets.

Planets should begin at randomized positions when starting a new game. Their positions must remain unchanged when retrying the same level.

## Visual Direction

The game should feel like an elegant, luminous constellation puzzle set inside a miniature solar system. Use glowing planets, atmospheric gravitational fields, rich cosmic backgrounds, and a distant galaxy that feels like a rewarding destination.

Keep the composition cinematic but readable, with planets arranged like a constellation rather than in a simple line. The interface should be minimal so nothing obstructs the playfield.

Polish the rocket launch, gravitational interactions, failure state, and galaxy arrival animation. The final experience should be visually striking, instantly understandable, satisfying to experiment with, and increasingly challenging across its five levels.

[Try in Codex](codex://threads/new?prompt=Use+%40game-studio+to+build+a+game+called+%22Time+to+Fly.%22+%5BOptional%3A+Use+the+provided+reference+images+as+inspiration+for+its+visual+direction.%5D%0A%0ACreate+a+polished+cosmic+logic+puzzle+where+players+guide+a+rocket+into+a+distant+galaxy+by+positioning+planets+and+using+their+gravitational+pull.%0A%0AEach+level+presents+a+miniature+solar+system.+Before+launching%2C+the+player+adjusts+the+rocket%27s+launch+angle+and+drags+planets+around+their+fixed+circular+orbits.+Once+launched%2C+the+rocket+flies+freely+and+its+trajectory+is+altered+by+the+gravitational+field+of+each+planet+it+encounters.%0A%0A%23%23+Core+Mechanics%0A%0A-+The+game+has+five+levels.%0A-+Level+N+contains+N+planets%2C+progressing+from+one+planet+in+Level+1+to+five+planets+in+Level+5.%0A-+Planets+remain+stationary+after+being+positioned+and+do+not+move+automatically.%0A-+Players+can+drag+each+planet+around+its+fixed+orbit+before+launching.%0A-+Players+launch+the+rocket+using+a+button+or+the+spacebar.%0A-+Do+not+show+a+trajectory+preview.%0A-+Every+planet+must+be+used+to+successfully+complete+its+level.%0A-+If+the+rocket+misses+the+galaxy%2C+it+flies+into+space+and+the+player+can+immediately+retry.%0A-+There+are+no+lives+or+retry+limits.%0A%0AEach+planet+should+have+a+consistent+size%2C+appearance%2C+and+gravitational+strength+throughout+the+game.+Larger+planets+should+exert+a+stronger+pull+across+a+larger+area.+The+rocket%27s+direction+should+change+naturally+based+on+its+entry+angle%2C+distance+from+the+planet%2C+and+the+planet%27s+gravitational+strength.%0A%0AClearly+visualize+gravitational+fields+using+refined+glowing+or+pulsing+effects%2C+but+keep+the+interface+uncluttered+and+easy+to+understand.%0A%0A%23%23+Level+Design%0A%0AEach+level+should+have+only+a+small+number+of+valid+solutions%3A%0A%0A-+Level+1%3A+An+approachable+introduction+using+one+planet.%0A-+Level+2%3A+Accessible%2C+but+requires+deliberate+positioning.%0A-+Level+3%3A+Introduces+meaningful+multi-planet+planning.%0A-+Level+4%3A+A+challenging+orbital+puzzle+requiring+careful+sequencing.%0A-+Level+5%3A+A+difficult+final+puzzle+requiring+precise+use+of+all+five+planets.%0A%0APlanets+should+begin+at+randomized+positions+when+starting+a+new+game.+Their+positions+must+remain+unchanged+when+retrying+the+same+level.%0A%0A%23%23+Visual+Direction%0A%0AThe+game+should+feel+like+an+elegant%2C+luminous+constellation+puzzle+set+inside+a+miniature+solar+system.+Use+glowing+planets%2C+atmospheric+gravitational+fields%2C+rich+cosmic+backgrounds%2C+and+a+distant+galaxy+that+feels+like+a+rewarding+destination.%0A%0AKeep+the+composition+cinematic+but+readable%2C+with+planets+arranged+like+a+constellation+rather+than+in+a+simple+line.+The+interface+should+be+minimal+so+nothing+obstructs+the+playfield.%0A%0APolish+the+rocket+launch%2C+gravitational+interactions%2C+failure+state%2C+and+galaxy+arrival+animation.+The+final+experience+should+be+visually+striking%2C+instantly+understandable%2C+satisfying+to+experiment+with%2C+and+increasingly+challenging+across+its+five+levels.)

### Iterations

1. Refined the core gravity gameplay by adding orbital rotation, improving launch aiming and gravity interactions, simplifying visual guidance, and making retries preserve the player's setup.
2. Used Goal Mode to redesign and validate the five-level difficulty curve, introduce hazards with moons, improve gravity behavior, and confirm each level had playable solutions.
3. Tuned level layouts and rules so later puzzles required deliberate positioning, careful sequencing, and meaningful use of every planet.
4. Polished the game feel and presentation with generated rocket artwork, improved controls and responsive layouts, refined flight motion, and cinematic galaxy-arrival transitions.
5. Added scoring, pilot identities, high-score behavior, a leaderboard, and a final victory experience.
6. Optimized rendering and assets, reducing the game assets from roughly 33 MB to 2.8 MB while improving loading and runtime performance.
7. Final step

   Added automated gameplay and leaderboard regression coverage, then hardened the scoring system with server-verified runs and anti-cheat protections.

Built with

Codex + GPT-5.5 + GPT Image 2

Models

GPT-5.5GPT Image 2

APIs / Products

Codex

Use case

[Games](/showcase?use_case=games)

Harness

Codex

Type

[Game](/showcase?app_type=game)

## Related projects

[![Swifty Dungeon](/showcase/swifty-dungeon.png)

### Swifty Dungeon

Swifty Dungeon is a playable native macOS dungeon crawler created...

GPT-5.5  Codex  Swift](/showcase/swifty-dungeon)[![Swifty Roguelike](/showcase/swifty-roguelike.png)

### Swifty Roguelike

Swifty Roguelike is a playable native macOS prototype created with Codex...

GPT-5.5  Codex  Swift](/showcase/swifty-roguelike)[![Brick Platformer](/showcase/brick-platformer.webp)

### Brick Platformer

This platformer game was generated with Codex + GPT-5

GPT-5.5  Codex  React](/showcase/brick-platformer)

<!-- source: https://developers.openai.com/showcase/swifty-dungeon/ -->

## Search developer resources

[← All projects](/showcase) 

![Swifty Dungeon app screenshot](/showcase/swifty-dungeon.png)

Description

Swifty Dungeon is a playable native macOS dungeon crawler created end-to-end in Codex with GPT-5.5. It combines a raycast-style first-person viewport, procedural labyrinth floors, turn-based movement and combat, equipment, inventory, item pickups, potions, leveling, animated enemy sprites, sidebars, minimap, HUD controls, and unified logging telemetry.

## Build notes

### Initial prompt

Copy prompt
 

Use $imagegen and @Build macOS apps to build a native macOS first-person dungeon crawler.

First, use $imagegen to generate a screenshot/interface of the ideal app: a native SwiftUI Liquid Glass app with the playable dungeon view in the center, the character and on-screen arrow keys in the bottom area, and player status plus inventory in the right sidebar.

The game should be a turn-by-turn dungeon crawler where you navigate randomly generated labyrinths, fight monsters, level up, and reach the next floor. Use $imagegen again to generate dungeon tilesets, wall textures, and floor themes. Build the app with enough telemetry to debug it, and make the deliverable playable end to end.

[Try in Codex](codex://threads/new?prompt=Use+%24imagegen+and+%40Build+macOS+apps+to+build+a+native+macOS+first-person+dungeon+crawler.%0A%0AFirst%2C+use+%24imagegen+to+generate+a+screenshot%2Finterface+of+the+ideal+app%3A+a+native+SwiftUI+Liquid+Glass+app+with+the+playable+dungeon+view+in+the+center%2C+the+character+and+on-screen+arrow+keys+in+the+bottom+area%2C+and+player+status+plus+inventory+in+the+right+sidebar.%0A%0AThe+game+should+be+a+turn-by-turn+dungeon+crawler+where+you+navigate+randomly+generated+labyrinths%2C+fight+monsters%2C+level+up%2C+and+reach+the+next+floor.+Use+%24imagegen+again+to+generate+dungeon+tilesets%2C+wall+textures%2C+and+floor+themes.+Build+the+app+with+enough+telemetry+to+debug+it%2C+and+make+the+deliverable+playable+end+to+end.)

### Iterations

1. Use $imagegen to generate the ideal app screenshot/interface: native SwiftUI Liquid Glass, center dungeon view, bottom movement controls, and right status/inventory sidebar.
2. Use the generated image as direction for a first playable version, then use $imagegen to create dungeon sprites and wall textures.
3. Use $imagegen to generate a monster sprite sheet with animation frames, then bring those animations into the game engine.
4. Use $imagegen again to generate dungeon tilesets, wall textures, and floor themes.
5. Polish the native macOS interface and tidy the code.
6. Make the deliverable playable end to end.
7. Final step

   An open-sourced Swifty Dungeon prototype with generated visual direction, a playable end-to-end game loop, telemetry, screenshot, README, and build scripts.

Built with

Codex + GPT-5.5 + ImageGen

Models

GPT-5.5GPT Image 2

APIs / Products

Codex

Tech stack

Swift [SwiftUI](/showcase?tech_stack=SwiftUI) SwiftPMmacOS

Use case

[Games](/showcase?use_case=games)  [Visual experience](/showcase?use_case=visual-experience)

Harness

Codex

Type

[Game](/showcase?app_type=game)

## Related projects

[![Swifty Roguelike](/showcase/swifty-roguelike.png)

### Swifty Roguelike

Swifty Roguelike is a playable native macOS prototype created with Codex...

GPT-5.5  Codex  Swift](/showcase/swifty-roguelike)[![Time to Fly](/showcase/time-to-fly.webp)

### Time to Fly

Time to Fly is a cosmic logic puzzle built in Codex with GPT-5

GPT-5.5  Codex](/showcase/time-to-fly)[![Brick Platformer](/showcase/brick-platformer.webp)

### Brick Platformer

This platformer game was generated with Codex + GPT-5

GPT-5.5  Codex  React](/showcase/brick-platformer)

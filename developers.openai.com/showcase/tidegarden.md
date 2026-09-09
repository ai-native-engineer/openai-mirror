<!-- source: https://developers.openai.com/showcase/tidegarden/ -->

For the complete documentation index, see [llms.txt](/llms.txt). Markdown versions of documentation pages are available by appending
`.md` to the page URL.

## Showcase projects

[![Velocity Loop](/showcase/velocity-loop/cover-generated-sep4.webp)

### Velocity Loop

A 3D toy-car time-trial game set in miniature workshops.](/showcase/velocity-loop)[![Abyssal](/showcase/abyssal-bioluminescent-ecosystem/cover-generated-sep4.webp)

### Abyssal

A procedural underwater scene with bioluminescent marine life.](/showcase/abyssal-bioluminescent-ecosystem)[![Clockwork Observatory](/showcase/impossible-kinetic-architecture/cover-generated-sep4.webp)

### Clockwork Observatory

An interactive 3D scene of a transforming mechanical observatory.](/showcase/impossible-kinetic-architecture)[![Living Cell](/showcase/living-cell-cross-section/cover-generated-sep4.webp)

### Living Cell

An interactive 3D cell cross-section with inspectable structures.](/showcase/living-cell-cross-section)[![Hollowflux](/showcase/hollowflux/final.webp)

### Hollowflux

A procedural dungeon crawler with combat shaped by reactive water.](/showcase/hollowflux)[![Little Ritual](/showcase/little-ritual/cover-generated-sep4.webp)

### Little Ritual

A 3D coffee-delivery game on a small spherical world.](/showcase/little-ritual)[![Physics museum](/showcase/physics-museum/cover-generated-sep4.webp)

### Physics museum

A 3D science museum with five interactive exhibits.](/showcase/physics-museum)[![Sunwake](/showcase/sunwake/gameplay-sailing.webp)

### Sunwake

A sailing game about crossing wild seas and reaching lighthouses.](/showcase/sunwake)[![Void Explorer](/showcase/void-explorer/launch-cover-four-wing.webp)

### Void Explorer

A procedural space exploration game with planets to land on.](/showcase/void-explorer)[![Tidegarden](/showcase/tidegarden/cover-generated.webp)

### Tidegarden

A 3D tropical island with a living reef and rolling waves.](/showcase/tidegarden)[![Asterism](/showcase/gpt-5-6-asterism.webp)

### Asterism

Build constellations from a finite deck of named stars and illuminate the...](/showcase/asterism)[![Codex Pet Arena](/showcase/codex-pet-arena.webp)

### Codex Pet Arena

A fast, colorful platform arena where animated pets collect tokens, grow...](/showcase/codex-pet-arena)[![MiniTown](/showcase/gpt-5-6-minitown.webp)

### MiniTown

A tiny living town where zones grow, residents commute, and warm lights...](/showcase/minitown)[![Backroom Center: Corrupted](/showcase/gpt-5-6-backroom-center-corrupted.webp)

### Backroom Center: Corrupted

An infinite data-center labyrinth seen through a deteriorating VHS camcorder.](/showcase/backroom-center-corrupted)[![Phantasy Codex Adventure](/showcase/gpt-5-6-phantasy-codex-adventure.webp)

### Phantasy Codex Adventure

A persistent retro action RPG with procedural worlds, classes, bosses, and...](/showcase/phantasy-codex-adventure)[![Tiny Rails Rollercoaster](/showcase/tiny-rails-rollercoaster/cover-generated-sep4.webp)

### Tiny Rails Rollercoaster

A nostalgic miniature coaster with eight routes and hands-on driving modes.](/showcase/tiny-rails-rollercoaster)[![Glass Towers](/showcase/gpt-5-6-glass-towers.webp)

### Glass Towers

A minimalist 3D balancing game built from translucent forms.](/showcase/glass-towers)[![Paper Glider](/showcase/gpt-5-6-paper-glider.webp)

### Paper Glider

An arcade glider through sunlit, procedurally generated rooms.](/showcase/paper-glider)[![Time to Fly](/showcase/time-to-fly.webp)

### Time to Fly

Cosmic logic puzzle game about orbital rotation.](/showcase/time-to-fly)[![Swifty Roguelike](/showcase/swifty-roguelike.png)

### Swifty Roguelike

A native macOS ASCII roguelike built with SwiftUI Canvas and a modern...](/showcase/swifty-roguelike)[![Swifty Dungeon](/showcase/swifty-dungeon.png)

### Swifty Dungeon

A native SwiftUI first-person dungeon crawler with generated textures...](/showcase/swifty-dungeon)[![Brick Platformer](/showcase/brick-platformer.webp)

### Brick Platformer

Browser platformer game with brick rooftops and side-scrolling action.](/showcase/brick-platformer)[![Turn-based RPG](/showcase/trpg.webp)

### Turn-based RPG

A browser demo that turns GPT-5.4 into a turn-based role-playing game with...](/showcase/turn-based-rpg)[![Neon FPS](/showcase/neon-fps.webp)

### Neon FPS

Neon first-person shooter game with arcade-style combat.](/showcase/rift-vox)[![Theme Park Builder](/showcase/theme-park.webp)

### Theme Park Builder

Mini-game where you can build your own theme park.](/showcase/theme-park-builder)

[Try it live](https://tidegarden.openai.chatgpt.site/)

## Build process

tidegarden

![Early island prototype with a spiky palm, sparse foliage, and flat turquoise water.](https://cdn.openai.com/devhub/showcase/tidegarden/early-prototype-700d523f2181.webp)Early island prototype with sparse foliage and flat turquoise water.

### Build process

1. **Build the first island**

   The first island had a spiky palm and flat water. A generated reference set the direction for the foliage, turquoise shallows, and warm afternoon light.

   Reference images

   ![Generated visual reference of a leaning palm on a sunlit island with clear turquoise shallows and a detailed reef.](https://cdn.openai.com/devhub/showcase/tidegarden/north-star-e3c3261dcae0.webp)

   Create a tiny tropical island in Oriel with a beach, grass, one palm, open ocean, and clouds. Generate a believable realtime 3D reference with a leaning palm, turquoise shallows, and warm afternoon light, then use it as the visual north star. Inspect the rendered scene as you improve it.
2. **Give the palm and grass life**

   Reworked a spiky palm and sparse grass through better geometry, GPU foliage, wind, shading, and softer ground transitions.
3. **Assemble an editable reef in Blender**

   Built and arranged reef banks from reusable colony forms, keeping the Blender sources editable and preserving their materials in the scene.
4. **Give the water depth and light**

   Progressed from flat, depthless water through early reef experiments to refraction and moving underwater light.
5. **Build tools to see the problems**

   Added high-contrast surface captures, motion inspection, and shader and overdraw diagnostics to guide the rendering work.
6. **Simplify the shoreline foam**

   Overcomplicated foam gave way to a texture-driven shoreline: thinner white wash, lighting, fine bubbles, and room to recede.
7. **Make the wave cause the wash**

   Rejected loops and straight stripes, then connected irregular crests, shoreline wash, and retreat to the same traveling wave.
8. **Lower the cost and ship**

   Compressed and cached assets, simplified shading, capped rendering at 1080p, and used FXAA with 37% fewer water triangles.

## Related projects

[![Hollowflux](/showcase/hollowflux/final.webp)

### Hollowflux

A procedural dungeon crawler built with Codex

GPT-6 Astra  Codex  TypeScript](/showcase/hollowflux)[![Little Ritual](/showcase/little-ritual/cover-generated-sep4.webp)

### Little Ritual

A single-player 3D browser game about delivering coffee and exploring a...

GPT-6 Astra  Codex  TypeScript](/showcase/little-ritual)[![Sunwake](/showcase/sunwake/gameplay-sailing.webp)

### Sunwake

A sailing game built with Codex. Follow the visual references through...

GPT-6 Astra  Codex  TypeScript](/showcase/sunwake)

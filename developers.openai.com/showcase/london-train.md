<!-- source: https://developers.openai.com/showcase/london-train/ -->

## Search developer resources

[← All projects](/showcase) 

![London Dream Railway app screenshot](/showcase/london-train.webp)

Description

London Dream Railway is an interactive 3D scene with miniature trains, recognizable London landmarks, moving boats, seasonal modes, an auto tour, train follow mode, and an interactive driver cab. Peter started with an initial Codex generation without skills, then used Computer Use repeatedly to walk through the app, test each area, identify issues, and guide further improvements.

## Build notes

### Initial prompt

Copy prompt
 

Create a dream toy-railway version of London in Three.js: a bright voxel train-table world where little red trains and Tube-like carriages weave through the capital's most famous landmarks. It should feel like the ultimate playroom train set, but with excellent London recognizability.

If you use Three.js, add an import map (before the module script) mapping "three" and "three/addons/" to the same pinned version, and import only via those names. Never reuse identifiers in the same scope - use descriptive variable names.

#### TABLE SETUP

- Let the city sit on a visible playtable or wooden base so the toy-train format is obvious.
- Use elevated tracks, short viaducts, tidy tunnels, and small station platforms.
- The overall layout should be readable from a slightly top-down three-quarter camera.

#### LANDMARKS

- Include Elizabeth Tower / Westminster, Tower Bridge, the London Eye, St Paul's, The Shard, and Battersea.
- Landmarks should be tightly packed around the tracks so trains constantly pass recognizable icons.
- Add small parks and river sections to stop the table feeling too crowded.

#### TRAINS + TRACKS

- Run multiple train loops at once: classic bright-red toy trains, Tube-inspired trains, and maybe a tiny DLR-style shuttle.
- Use branching points or track switches that visibly reroute trains.
- Add a few cutaway tunnel sections so the train movement is easy to follow.

#### STYLE

- Keep everything crisp, bright, and toy-clean.
- Red, blue, yellow, and fresh green should dominate rather than grey realism.
- No dark station lighting, no smoky atmosphere, and no heavy grime.

#### CONTROLS

- Track-switch toggles.
- Train count / speed slider.
- Tunnel cutaway toggle.
- Follow-train camera plus a reset overview.
- Camera presets: full table, bridge crossing, station close-up, tunnel slice.

#### TECHNICAL

- Instanced sleepers, rails, trees, windows, and repeat props.
- Keep train motion smooth and predictable.
- Target >=55 FPS and clamp devicePixelRatio <= 2.

[Try in Codex](codex://threads/new?prompt=Create+a+dream+toy-railway+version+of+London+in+Three.js%3A+a+bright+voxel+train-table+world+where+little+red+trains+and+Tube-like+carriages+weave+through+the+capital%27s+most+famous+landmarks.+It+should+feel+like+the+ultimate+playroom+train+set%2C+but+with+excellent+London+recognizability.%0A%0AIf+you+use+Three.js%2C+add+an+import+map+%28before+the+module+script%29+mapping+%22three%22+and+%22three%2Faddons%2F%22+to+the+same+pinned+version%2C+and+import+only+via+those+names.+Never+reuse+identifiers+in+the+same+scope+-+use+descriptive+variable+names.%0A%0A%23%23%23%23+TABLE+SETUP%0A%0A-+Let+the+city+sit+on+a+visible+playtable+or+wooden+base+so+the+toy-train+format+is+obvious.%0A-+Use+elevated+tracks%2C+short+viaducts%2C+tidy+tunnels%2C+and+small+station+platforms.%0A-+The+overall+layout+should+be+readable+from+a+slightly+top-down+three-quarter+camera.%0A%0A%23%23%23%23+LANDMARKS%0A%0A-+Include+Elizabeth+Tower+%2F+Westminster%2C+Tower+Bridge%2C+the+London+Eye%2C+St+Paul%27s%2C+The+Shard%2C+and+Battersea.%0A-+Landmarks+should+be+tightly+packed+around+the+tracks+so+trains+constantly+pass+recognizable+icons.%0A-+Add+small+parks+and+river+sections+to+stop+the+table+feeling+too+crowded.%0A%0A%23%23%23%23+TRAINS+%2B+TRACKS%0A%0A-+Run+multiple+train+loops+at+once%3A+classic+bright-red+toy+trains%2C+Tube-inspired+trains%2C+and+maybe+a+tiny+DLR-style+shuttle.%0A-+Use+branching+points+or+track+switches+that+visibly+reroute+trains.%0A-+Add+a+few+cutaway+tunnel+sections+so+the+train+movement+is+easy+to+follow.%0A%0A%23%23%23%23+STYLE%0A%0A-+Keep+everything+crisp%2C+bright%2C+and+toy-clean.%0A-+Red%2C+blue%2C+yellow%2C+and+fresh+green+should+dominate+rather+than+grey+realism.%0A-+No+dark+station+lighting%2C+no+smoky+atmosphere%2C+and+no+heavy+grime.%0A%0A%23%23%23%23+CONTROLS%0A%0A-+Track-switch+toggles.%0A-+Train+count+%2F+speed+slider.%0A-+Tunnel+cutaway+toggle.%0A-+Follow-train+camera+plus+a+reset+overview.%0A-+Camera+presets%3A+full+table%2C+bridge+crossing%2C+station+close-up%2C+tunnel+slice.%0A%0A%23%23%23%23+TECHNICAL%0A%0A-+Instanced+sleepers%2C+rails%2C+trees%2C+windows%2C+and+repeat+props.%0A-+Keep+train+motion+smooth+and+predictable.%0A-+Target+%3E%3D55+FPS+and+clamp+devicePixelRatio+%3C%3D+2.)

### Iterations

1. Generated the first Three.js toy-railway version of London from the initial prompt without using skills.
2. Used Computer Use to walk through the app, test the experience end to end, and identify issues in the scene and controls.
3. Fixed issues found during validation and improved the clarity of the landmarks, trains, controls, and camera behavior.
4. Added new interaction ideas, including the train POV view and seasonal modes.
5. Repeated the Codex and Computer Use loop several times, testing each part of the app after each improvement.
6. Final step

   Validated the full interactive experience with Computer Use, including the train POV view, seasonal modes, landmarks, trains, controls, and camera behavior.

Built with

Codex + GPT-5.4 + Computer Use validation

Model

GPT-5.4

APIs / Products

CodexComputer Use

Tech stack

[Three.js](/showcase?tech_stack=Three.js) HTMLCSSJavaScript

Use case

[Visual experience](/showcase?use_case=visual-experience)

Harness

Codex

Type

[App](/showcase?app_type=app)

## Related projects

[![Golden Gate Experience](/showcase/golden-gate.webp)

### Golden Gate Experience

This experience was generated with Codex + GPT-5

GPT-5.5  Codex  React](/showcase/golden-gate-flight-experience)[![Procedural City Generator](/showcase/city-generator.webp)

### Procedural City Generator

This 3D procedural city generator was generated with Codex + GPT-5

GPT-5.5  Codex  React](/showcase/procedural-city-generator)[![Real estate data viz](/showcase/real-estate-data.webp)

### Real estate data viz

This app was generated with Codex + GPT-5

GPT-5.4  Codex  Next.js](/showcase/real-estate-data-viz)

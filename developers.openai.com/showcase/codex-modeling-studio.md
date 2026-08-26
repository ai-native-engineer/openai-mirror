<!-- source: https://developers.openai.com/showcase/codex-modeling-studio/ -->

![Codex Modeling Studio app screenshot](/showcase/codex-modeling-studio.webp)

Build and refine 3D scenes alongside Codex. Watch changes as they happen, steer the work, and inspect the scene independently.

Codex can inspect a scene, change its geometry, and refine textures through WebMCP. You can watch each edit in the 3D viewport and steer the next change while working on the same scene.

Tool capabilities (3)

Plan and implement a browser-based 3D modeling studio that Codex can operate through WebMCP. Give it tools for creating and editing models, composing basic scenes, applying materials, and rendering polished individual assets.
The studio should run in the browser without a built-in application server. Design it primarily for Codex to create, inspect, and refine models through tools, with a clean interface that lets the user follow along.
Prioritize the model viewport over a dense manual-editing dashboard. Deploy it as a hosted website.

[Try in Codex](codex://threads/new?prompt=Plan+and+implement+a+browser-based+3D+modeling+studio+that+Codex+can+operate+through+WebMCP.+Give+it+tools+for+creating+and+editing+models%2C+composing+basic+scenes%2C+applying+materials%2C+and+rendering+polished+individual+assets.%0AThe+studio+should+run+in+the+browser+without+a+built-in+application+server.+Design+it+primarily+for+Codex+to+create%2C+inspect%2C+and+refine+models+through+tools%2C+with+a+clean+interface+that+lets+the+user+follow+along.%0APrioritize+the+model+viewport+over+a+dense+manual-editing+dashboard.+Deploy+it+as+a+hosted+website.)

1. Started with a WebAssembly and WebGPU client.
2. Added tools, then had Codex use them to find limitations.
3. Repeated that loop to improve the tools' expressiveness and latency.
4. Final step

   Added a feedback tool backed by the Sites database.

Tech stack

WebAssemblyWebGPU

[![Crossword Desk](/showcase/crossword-desk.webp)

Codex](/showcase/ko-field-beat-machine)[![Margin Editor](/showcase/margin-editor.webp)

### Margin Editor

Create notes and discuss changes with Codex in the same document

Codex](/showcase/margin-editor)

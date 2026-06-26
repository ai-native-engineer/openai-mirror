<!-- source: https://developers.openai.com/showcase/forged-in-silence/ -->

## Search developer resources

[← All projects](/showcase) 

![Forged in Silence app screenshot](/showcase/forged-in-silence.webp)

Description

Forged in Silence is a premium ecommerce storefront built with Codex from a researched Vite, React, and React Three Fiber plan. The home page is a scroll-driven 3D experience where a procedurally generated katana, built without Blender or an external 3D model, animates through cinematic sections before continuing into product pages, cart behavior, checkout, custom commission requests, and contact flows.

## Build notes

### Initial prompt

Copy prompt
 

Create a new Vite + React project with the following setup:

1. Initialize a Vite project with React template in the root directory.
2. Install these exact dependencies:
- three
- @react-three/fiber
- @react-three/drei
- gsap
- @gsap/react
- lenis

3. Create this exact folder structure:

src/
components/
Scene.jsx
Katana.jsx
sections/
HeroDrop.jsx
BladeSection.jsx
EdgeSection.jsx
RotationSection.jsx
DrawSection.jsx
EndCard.jsx
hooks/
useScrollAnimation.js
styles/
global.css
App.jsx
main.jsx

4. In index.html, add this inside <head>:

<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@300;400;700&family=Bebas+Neue&display=swap" rel="stylesheet">

5. In src/styles/global.css write the base reset, black/white/steel/gold/accent variables, fixed full-viewport canvas styling, and scroll-container/section layout for a 100vh cinematic scroll experience.

6. In src/main.jsx render App with React.StrictMode and import global.css.

7. In src/App.jsx create a placeholder with <Scene /> and six 100vh scroll sections inside .scroll-container.

8. In src/components/Scene.jsx create a React Three Fiber Canvas with camera position [0, 0, 5], ambient and directional lighting, and a simple metallic blade placeholder mesh.

Make sure vite.config.js is standard React config. Run npm install. Do not run the dev server. Run "npm run build" and fix any errors that appear. Do not change any visual or logic code — only fix build errors.

[Try in Codex](codex://threads/new?prompt=Create+a+new+Vite+%2B+React+project+with+the+following+setup%3A%0A%0A1.+Initialize+a+Vite+project+with+React+template+in+the+root+directory.%0A2.+Install+these+exact+dependencies%3A%0A-+three%0A-+%40react-three%2Ffiber%0A-+%40react-three%2Fdrei%0A-+gsap%0A-+%40gsap%2Freact%0A-+lenis%0A%0A3.+Create+this+exact+folder+structure%3A%0A%0Asrc%2F%0Acomponents%2F%0AScene.jsx%0AKatana.jsx%0Asections%2F%0AHeroDrop.jsx%0ABladeSection.jsx%0AEdgeSection.jsx%0ARotationSection.jsx%0ADrawSection.jsx%0AEndCard.jsx%0Ahooks%2F%0AuseScrollAnimation.js%0Astyles%2F%0Aglobal.css%0AApp.jsx%0Amain.jsx%0A%0A4.+In+index.html%2C+add+this+inside+%3Chead%3E%3A%0A%0A%3Clink+rel%3D%22preconnect%22+href%3D%22https%3A%2F%2Ffonts.googleapis.com%22%3E%0A%3Clink+href%3D%22https%3A%2F%2Ffonts.googleapis.com%2Fcss2%3Ffamily%3DNoto%2BSerif%2BJP%3Awght%40300%3B400%3B700%26family%3DBebas%2BNeue%26display%3Dswap%22+rel%3D%22stylesheet%22%3E%0A%0A5.+In+src%2Fstyles%2Fglobal.css+write+the+base+reset%2C+black%2Fwhite%2Fsteel%2Fgold%2Faccent+variables%2C+fixed+full-viewport+canvas+styling%2C+and+scroll-container%2Fsection+layout+for+a+100vh+cinematic+scroll+experience.%0A%0A6.+In+src%2Fmain.jsx+render+App+with+React.StrictMode+and+import+global.css.%0A%0A7.+In+src%2FApp.jsx+create+a+placeholder+with+%3CScene+%2F%3E+and+six+100vh+scroll+sections+inside+.scroll-container.%0A%0A8.+In+src%2Fcomponents%2FScene.jsx+create+a+React+Three+Fiber+Canvas+with+camera+position+%5B0%2C+0%2C+5%5D%2C+ambient+and+directional+lighting%2C+and+a+simple+metallic+blade+placeholder+mesh.%0A%0AMake+sure+vite.config.js+is+standard+React+config.+Run+npm+install.+Do+not+run+the+dev+server.+Run+%22npm+run+build%22+and+fix+any+errors+that+appear.+Do+not+change+any+visual+or+logic+code+%E2%80%94+only+fix+build+errors.)

### Iterations

1. Researched the Vite, React, and React Three Fiber architecture, then gave Codex a detailed scaffold spec.
2. Set up the Vite app with React, Three.js, React Three Fiber, GSAP, Lenis, and a section-based component structure.
3. Built the katana procedurally in Three.js BufferGeometry without relying on Blender or an external model.
4. Tuned cinematic lighting and materials across several Codex passes, including metalness, roughness, key light, fill light, gold highlights, RectAreaLight, SpotLight, and environment reflections.
5. Connected Lenis smooth scrolling to a GSAP ScrollTrigger timeline across six cinematic sections.
6. Added mixed Japanese and English typography, scroll-triggered text reveals, dust particles, vignette, CRT scanlines, a gold progress indicator, DPR capping, and responsive camera behavior.
7. Final step

   Expanded the cinematic 3D scene into a complete storefront with product pages, cart behavior, checkout, custom commission requests, and contact flows.

Built with

Codex + GPT-5.4

Model

GPT-5.4

APIs / Products

Codex

Tech stack

[React](/showcase?tech_stack=React)  [Three.js](/showcase?tech_stack=Three.js) ViteGSAPLenis

Use case

[Ecommerce](/showcase?use_case=ecommerce)  [Visual experience](/showcase?use_case=visual-experience)

Harness

Codex

Type

[Storefront](/showcase?app_type=storefront)

## Related projects

[![E-commerce website](/showcase/ecommerce.webp)

### E-commerce website

This storefront was generated with Codex, using `gpt-image-1

GPT-5.4  Codex  Next.js](/showcase/e-commerce-website)[![Watchmaker Landing Page](/showcase/watchmaker-landing-page.webp)

### Watchmaker Landing Page

This landing page was generated with Codex + GPT-5

GPT-5.5  Codex](/showcase/watchmaker-landing-page)[![London Dream Railway](/showcase/london-train.webp)

### London Dream Railway

London Dream Railway is an interactive 3D scene with miniature trains...

GPT-5.4  Codex  Three.js](/showcase/london-train)

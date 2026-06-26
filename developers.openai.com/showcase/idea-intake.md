<!-- source: https://developers.openai.com/showcase/idea-intake/ -->

## Search developer resources

[← All sites](/showcase/sites) 

![Sparkboard app screenshot](/showcase/sites-idea-intake.jpg)

Description

A collaborative idea intake dashboard with a trending feature, board-status navigation, search and filters, upvote-driven idea cards, and top contributor rankings.

## Prompt

Copy prompt
 

@sites

Build an internal employee Idea Intake app called "[APP NAME]", similar to a modern idea box. Use the company’s authenticated workspace identity and deploy the finished app for everyone in the workspace.

## Product Requirements

Employees should be able to:
- Submit ideas through a polished modal form.
- Upvote ideas once per authenticated user.
- Open an idea detail panel and add comments.
- View their own submissions in a "My Ideas" view.
- Search, filter, and sort ideas.
- Browse ideas by workflow status.
- View a contributor leaderboard based on votes received by their submitted ideas.

Each idea must include:
- Title
- Problem to solve
- Intended audience
- Expected impact
- Effort estimate: low, medium, or high
- Category
- Supporting links
- Status
- Score
- Author
- Created and updated timestamps

Include board views for:
- New
- Trending
- Under review
- Accepted
- Shipped
- Archived

## Persistence And Authentication

Use Cloudflare D1 with a logical `DB` binding.

Create D1 tables for:
- `ideas`
- `votes`
- `comments`
- `status_history`
- `leaderboard_snapshots`

Use the forwarded `oai-authenticated-user-email` request header for identity-aware behavior.

Enforce duplicate vote prevention server-side with a unique D1 index on `(idea_id, user_email)`. Do not rely only on client-side state.

Store status changes in `status_history`. Refresh a daily leaderboard snapshot when an idea is submitted or upvoted.

Include realistic seeded example ideas so the initial experience feels complete and can be visually reviewed immediately.

## Interface

Build the usable product interface directly. Do not create a marketing landing page.

Use a lively, colorful, modern-but-fun design:
- Warm off-white background
- Deep ink typography
- Saturated coral, cobalt blue, violet, amber, and mint accents
- Rounded but restrained components
- Crisp code-native SVG icons
- Playful editorial SaaS feel
- Accessible contrast
- No gradients, stock imagery, mascots, or excessive card nesting

Desktop layout:
- Compact left sidebar with the app name
- Primary navigation: Discover, My Ideas, Leaderboard
- Status navigation with item counts
- Main header: "Ideas worth building"
- Prominent "Share an idea" button
- Coral featured trending-idea band
- Search, category, status, and sort controls
- Two-column score-sorted idea feed
- Right rail with top contributors, category key, and a small encouragement panel

Each idea card should show:
- Prominent upvote control and score
- Title
- Concise problem statement
- Category
- Effort estimate
- Status
- Author
- Comment count

Mobile layout:
- Keep the navigation readable without horizontal overflow
- Collapse the right rail
- Preserve the submission CTA, featured idea, filters, and score-sorted feed

## Technical Requirements

Use the Sites vinext starter and produce a Cloudflare Worker-compatible ESM build.

Store hosting configuration in `.openai/hosting.json`:
- D1 binding: `DB`
- R2 binding: `null`

Keep the Drizzle schema in `db/schema.ts`.
Generate and include the Drizzle migration.
Keep D1 access behind a small helper rather than reading runtime bindings throughout route handlers.

## Verification

Before deployment:
- Run lint
- Run strict TypeScript checking
- Generate and inspect the D1 migration
- Run the production build
- Verify the desktop UI in the in-app browser
- Verify a mobile viewport around `390x844`
- Capture `public/screenshot.jpeg` directly at `1200x630`
- Confirm the deployment artifact includes the Worker entry point, hosting metadata, D1 migration, and screenshot

Test these workflows against local D1:
- Submit an idea
- Confirm it appears in My Ideas
- Upvote an idea
- Confirm a duplicate vote is rejected
- Add a comment
- Filter to an individual status board
- Open the leaderboard

## Deployment

After validation, save and deploy the site through Sites hosting.

Set access mode to `workspace_all` so every active workspace member can use it.

If deployment is blocked by environment or tenant policy, report the exact blocked step and leave the verified artifact ready for publishing from an approved environment.

[Try in Codex](codex://threads/new?prompt=%40sites%0A%0ABuild+an+internal+employee+Idea+Intake+app+called+%22%5BAPP+NAME%5D%22%2C+similar+to+a+modern+idea+box.+Use+the+company%E2%80%99s+authenticated+workspace+identity+and+deploy+the+finished+app+for+everyone+in+the+workspace.%0A%0A%23%23+Product+Requirements%0A%0AEmployees+should+be+able+to%3A%0A-+Submit+ideas+through+a+polished+modal+form.%0A-+Upvote+ideas+once+per+authenticated+user.%0A-+Open+an+idea+detail+panel+and+add+comments.%0A-+View+their+own+submissions+in+a+%22My+Ideas%22+view.%0A-+Search%2C+filter%2C+and+sort+ideas.%0A-+Browse+ideas+by+workflow+status.%0A-+View+a+contributor+leaderboard+based+on+votes+received+by+their+submitted+ideas.%0A%0AEach+idea+must+include%3A%0A-+Title%0A-+Problem+to+solve%0A-+Intended+audience%0A-+Expected+impact%0A-+Effort+estimate%3A+low%2C+medium%2C+or+high%0A-+Category%0A-+Supporting+links%0A-+Status%0A-+Score%0A-+Author%0A-+Created+and+updated+timestamps%0A%0AInclude+board+views+for%3A%0A-+New%0A-+Trending%0A-+Under+review%0A-+Accepted%0A-+Shipped%0A-+Archived%0A%0A%23%23+Persistence+And+Authentication%0A%0AUse+Cloudflare+D1+with+a+logical+%60DB%60+binding.%0A%0ACreate+D1+tables+for%3A%0A-+%60ideas%60%0A-+%60votes%60%0A-+%60comments%60%0A-+%60status_history%60%0A-+%60leaderboard_snapshots%60%0A%0AUse+the+forwarded+%60oai-authenticated-user-email%60+request+header+for+identity-aware+behavior.%0A%0AEnforce+duplicate+vote+prevention+server-side+with+a+unique+D1+index+on+%60%28idea_id%2C+user_email%29%60.+Do+not+rely+only+on+client-side+state.%0A%0AStore+status+changes+in+%60status_history%60.+Refresh+a+daily+leaderboard+snapshot+when+an+idea+is+submitted+or+upvoted.%0A%0AInclude+realistic+seeded+example+ideas+so+the+initial+experience+feels+complete+and+can+be+visually+reviewed+immediately.%0A%0A%23%23+Interface%0A%0ABuild+the+usable+product+interface+directly.+Do+not+create+a+marketing+landing+page.%0A%0AUse+a+lively%2C+colorful%2C+modern-but-fun+design%3A%0A-+Warm+off-white+background%0A-+Deep+ink+typography%0A-+Saturated+coral%2C+cobalt+blue%2C+violet%2C+amber%2C+and+mint+accents%0A-+Rounded+but+restrained+components%0A-+Crisp+code-native+SVG+icons%0A-+Playful+editorial+SaaS+feel%0A-+Accessible+contrast%0A-+No+gradients%2C+stock+imagery%2C+mascots%2C+or+excessive+card+nesting%0A%0ADesktop+layout%3A%0A-+Compact+left+sidebar+with+the+app+name%0A-+Primary+navigation%3A+Discover%2C+My+Ideas%2C+Leaderboard%0A-+Status+navigation+with+item+counts%0A-+Main+header%3A+%22Ideas+worth+building%22%0A-+Prominent+%22Share+an+idea%22+button%0A-+Coral+featured+trending-idea+band%0A-+Search%2C+category%2C+status%2C+and+sort+controls%0A-+Two-column+score-sorted+idea+feed%0A-+Right+rail+with+top+contributors%2C+category+key%2C+and+a+small+encouragement+panel%0A%0AEach+idea+card+should+show%3A%0A-+Prominent+upvote+control+and+score%0A-+Title%0A-+Concise+problem+statement%0A-+Category%0A-+Effort+estimate%0A-+Status%0A-+Author%0A-+Comment+count%0A%0AMobile+layout%3A%0A-+Keep+the+navigation+readable+without+horizontal+overflow%0A-+Collapse+the+right+rail%0A-+Preserve+the+submission+CTA%2C+featured+idea%2C+filters%2C+and+score-sorted+feed%0A%0A%23%23+Technical+Requirements%0A%0AUse+the+Sites+vinext+starter+and+produce+a+Cloudflare+Worker-compatible+ESM+build.%0A%0AStore+hosting+configuration+in+%60.openai%2Fhosting.json%60%3A%0A-+D1+binding%3A+%60DB%60%0A-+R2+binding%3A+%60null%60%0A%0AKeep+the+Drizzle+schema+in+%60db%2Fschema.ts%60.%0AGenerate+and+include+the+Drizzle+migration.%0AKeep+D1+access+behind+a+small+helper+rather+than+reading+runtime+bindings+throughout+route+handlers.%0A%0A%23%23+Verification%0A%0ABefore+deployment%3A%0A-+Run+lint%0A-+Run+strict+TypeScript+checking%0A-+Generate+and+inspect+the+D1+migration%0A-+Run+the+production+build%0A-+Verify+the+desktop+UI+in+the+in-app+browser%0A-+Verify+a+mobile+viewport+around+%60390x844%60%0A-+Capture+%60public%2Fscreenshot.jpeg%60+directly+at+%601200x630%60%0A-+Confirm+the+deployment+artifact+includes+the+Worker+entry+point%2C+hosting+metadata%2C+D1+migration%2C+and+screenshot%0A%0ATest+these+workflows+against+local+D1%3A%0A-+Submit+an+idea%0A-+Confirm+it+appears+in+My+Ideas%0A-+Upvote+an+idea%0A-+Confirm+a+duplicate+vote+is+rejected%0A-+Add+a+comment%0A-+Filter+to+an+individual+status+board%0A-+Open+the+leaderboard%0A%0A%23%23+Deployment%0A%0AAfter+validation%2C+save+and+deploy+the+site+through+Sites+hosting.%0A%0ASet+access+mode+to+%60workspace_all%60+so+every+active+workspace+member+can+use+it.%0A%0AIf+deployment+is+blocked+by+environment+or+tenant+policy%2C+report+the+exact+blocked+step+and+leave+the+verified+artifact+ready+for+publishing+from+an+approved+environment.)

Built with

Sites in Codex

Model

GPT-5.5

Tech stack

Vinext

Use case

[Internal Tools](/showcase?use_case=internal-tools)

Type

[App](/showcase?app_type=app)

## Related projects

[![Enablement Hub](/showcase/sites-enablement-hub.png)

### Enablement Hub

An internal learning hub with featured training, announcements, and a...

GPT-5.5  Vinext](/showcase/enablement-hub)[![Event Planning Hub](/showcase/sites-event-planning-hub.jpg)

### Event Planning Hub

An event planning dashboard with active request triage, event templates...

GPT-5.5  Vinext](/showcase/event-planning-hub)[![Launch Cal](/showcase/sites-launch-cal.jpg)

### Launch Cal

A monthly product and feature calendar with team, status, surface, risk...

GPT-5.5  Vinext](/showcase/launch-cal)

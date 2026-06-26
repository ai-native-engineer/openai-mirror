<!-- source: https://developers.openai.com/showcase/launch-cal/ -->

## Search developer resources

[← All sites](/showcase/sites) 

![Launch Cal app screenshot](/showcase/sites-launch-cal.jpg)

Description

A monthly product and feature calendar with team, status, surface, risk, and freshness filters plus launch details for checklists, source links, dependencies, go-to-market notes, and blockers.

## Prompt

Copy prompt
 

@sites Build and deploy an internal workspace app called Launch Cal.

Use the company’s connected Slack, Google Drive, Notion, and Google Calendar context to organize upcoming product and feature launches. Use D1 for cached launch records and normalized source references. If live source ingestion is not available during the initial build, create realistic representative launch records that demonstrate the intended workflow.

The primary experience should be a polished monthly calendar view, not a generic dashboard. Group launch items by target date and show each item as a compact colored block. Use distinct accent colors for each product area. Each calendar block should surface the launch type, title, owner initials, status, and dependency-risk indicator.

Add:
- A top navigation bar with the Launch Cal brand, a global search field, and the current user avatar.
- Month navigation with previous, next, and Today controls.
- A filter toolbar for team, status, surface, dependency risk, and source freshness.
- A launch count and a dependency-risk legend.
- A footer noting that records refresh from Slack, Drive, Notion, and Google Calendar.

Keep the page header intentionally minimal:
- Show only the title “Upcoming launches.”
- Do not add an eyebrow label above the title.
- Do not add a subtitle below the title.
- Do not show a “D1 cache live” badge, sync timestamp, or overflow dot menu in the top navigation.

Each launch calendar item must open a detailed side-panel modal with:
- Status and dependency-risk badges
- Launch title and summary
- Owner, launch date, and launch type
- Interactive launch checklist with completion progress
- Normalized source links back to Slack, Drive, Notion, and Google Calendar
- Relevant docs
- Dependencies
- Go-to-market notes
- Blockers
- Last updated time
- Connected-source count

Design direction:
- Modern internal product-tool aesthetic
- Warm off-white background with subtle borders and restrained shadows
- Functional, information-dense calendar layout
- Colored UI blocks for launch items
- Clean typography and compact spacing
- Avoid unnecessary dashboard cards or decorative chrome
- Make the first viewport feel immediately useful and visually polished

Persist checklist updates in D1. Keep the normalized source-reference model suitable for future refresh jobs.

Build, validate, and deploy the finished app. Make it accessible to all active users in the workspace.

[Try in Codex](codex://threads/new?prompt=%40sites+Build+and+deploy+an+internal+workspace+app+called+Launch+Cal.%0A%0AUse+the+company%E2%80%99s+connected+Slack%2C+Google+Drive%2C+Notion%2C+and+Google+Calendar+context+to+organize+upcoming+product+and+feature+launches.+Use+D1+for+cached+launch+records+and+normalized+source+references.+If+live+source+ingestion+is+not+available+during+the+initial+build%2C+create+realistic+representative+launch+records+that+demonstrate+the+intended+workflow.%0A%0AThe+primary+experience+should+be+a+polished+monthly+calendar+view%2C+not+a+generic+dashboard.+Group+launch+items+by+target+date+and+show+each+item+as+a+compact+colored+block.+Use+distinct+accent+colors+for+each+product+area.+Each+calendar+block+should+surface+the+launch+type%2C+title%2C+owner+initials%2C+status%2C+and+dependency-risk+indicator.%0A%0AAdd%3A%0A-+A+top+navigation+bar+with+the+Launch+Cal+brand%2C+a+global+search+field%2C+and+the+current+user+avatar.%0A-+Month+navigation+with+previous%2C+next%2C+and+Today+controls.%0A-+A+filter+toolbar+for+team%2C+status%2C+surface%2C+dependency+risk%2C+and+source+freshness.%0A-+A+launch+count+and+a+dependency-risk+legend.%0A-+A+footer+noting+that+records+refresh+from+Slack%2C+Drive%2C+Notion%2C+and+Google+Calendar.%0A%0AKeep+the+page+header+intentionally+minimal%3A%0A-+Show+only+the+title+%E2%80%9CUpcoming+launches.%E2%80%9D%0A-+Do+not+add+an+eyebrow+label+above+the+title.%0A-+Do+not+add+a+subtitle+below+the+title.%0A-+Do+not+show+a+%E2%80%9CD1+cache+live%E2%80%9D+badge%2C+sync+timestamp%2C+or+overflow+dot+menu+in+the+top+navigation.%0A%0AEach+launch+calendar+item+must+open+a+detailed+side-panel+modal+with%3A%0A-+Status+and+dependency-risk+badges%0A-+Launch+title+and+summary%0A-+Owner%2C+launch+date%2C+and+launch+type%0A-+Interactive+launch+checklist+with+completion+progress%0A-+Normalized+source+links+back+to+Slack%2C+Drive%2C+Notion%2C+and+Google+Calendar%0A-+Relevant+docs%0A-+Dependencies%0A-+Go-to-market+notes%0A-+Blockers%0A-+Last+updated+time%0A-+Connected-source+count%0A%0ADesign+direction%3A%0A-+Modern+internal+product-tool+aesthetic%0A-+Warm+off-white+background+with+subtle+borders+and+restrained+shadows%0A-+Functional%2C+information-dense+calendar+layout%0A-+Colored+UI+blocks+for+launch+items%0A-+Clean+typography+and+compact+spacing%0A-+Avoid+unnecessary+dashboard+cards+or+decorative+chrome%0A-+Make+the+first+viewport+feel+immediately+useful+and+visually+polished%0A%0APersist+checklist+updates+in+D1.+Keep+the+normalized+source-reference+model+suitable+for+future+refresh+jobs.%0A%0ABuild%2C+validate%2C+and+deploy+the+finished+app.+Make+it+accessible+to+all+active+users+in+the+workspace.)

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

GPT-5.5  Vinext](/showcase/event-planning-hub)[![Onboarding Hub](/showcase/sites-onboarding-hub.png)

### Onboarding Hub

A personalized new-hire dashboard with current progress, suggested...

GPT-5.5  Vinext](/showcase/onboarding-hub)

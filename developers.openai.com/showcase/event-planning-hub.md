<!-- source: https://developers.openai.com/showcase/event-planning-hub/ -->

## Search developer resources

[← All sites](/showcase/sites) 

![Event Planning Hub app screenshot](/showcase/sites-event-planning-hub.jpg)

Description

An event planning dashboard with active request triage, event templates, recent playbacks, an upcoming calendar, event health metrics, and policy readiness.

## Prompt

Copy prompt
 

@sites Build and deploy an internal, workspace-authenticated Event Planning Hub for our company. Make it available to everyone in the workspace.

Use connected company sources to make the app feel grounded in the organization:
- Google Calendar: identify relevant planned event dates and avoid scheduling conflicts.
- Slack: find event-planning channels and recent planning updates.
- Google Drive: link briefs, budgets, run-of-show documents, and event assets.
- Notion: surface event policies, approval guidance, and reusable playbooks.
- If a connected source does not contain useful results, use realistic seeded examples and keep the source references configurable. Do not expose unrelated or sensitive workspace content.

Build an event intake workflow available to all workspace users. The intake form should include:
- Event title
- Event type
- Audience
- Assigned owner
- Objective
- Date range
- Location or virtual format
- Budget
- Expected headcount
- Vendors
- Policy needs
- Notes and relevant resource links

Permissions:
- Any workspace user can submit an intake request.
- Only the assigned event owner can accept or reject the request.
- Enforce owner-only acceptance server-side, not only in the interface.

Create separate views for:
- Overview dashboard
- Active intake requests
- Upcoming events
- Past events
- Templates
- Policies and playbooks

Allow users to duplicate a past event or start from templates such as:
- Meetup
- Customer dinner
- Webinar
- Recruiting event
- Team offsite

Each event detail page should include:
- Event health summary with clear status signals
- Timeline and milestones
- Tasks and owners
- Resource links from Drive, Slack, Notion, and Calendar
- Approval status
- Owner comments
- Policy checklist
- Activity updates

Include policy checklist items for:
- General approvals
- Accessibility
- Swag
- Vendor review
- Privacy
- Communications

Use D1 as the authoritative data store for:
- Event records
- Intake status
- Approvals
- Template metadata
- Tasks and task status
- Policy checklist progress
- Resource links
- Comments

Use R2 only if real file uploads are implemented. Otherwise, store Google Drive references rather than duplicating files.

Design direction:
- Make the interface feel like an operations command center for event owners.
- Use a modern, elevated dashboard style with a dark navigation sidebar, a light content canvas, polished cards, strong information hierarchy, and joyful accent colors.
- Prioritize quick scanning: show pending approvals, policy readiness, upcoming milestones, scheduling conflicts, event health, and recent planning activity prominently.
- Use realistic company-specific examples derived from the connected sources when appropriate.

Before deployment:
- Verify that the production build succeeds.
- Perform a visual review of the dashboard, intake flow, event detail view, and responsive layout.
- Deploy with workspace-wide access.

[Try in Codex](codex://threads/new?prompt=%40sites+Build+and+deploy+an+internal%2C+workspace-authenticated+Event+Planning+Hub+for+our+company.+Make+it+available+to+everyone+in+the+workspace.%0A%0AUse+connected+company+sources+to+make+the+app+feel+grounded+in+the+organization%3A%0A-+Google+Calendar%3A+identify+relevant+planned+event+dates+and+avoid+scheduling+conflicts.%0A-+Slack%3A+find+event-planning+channels+and+recent+planning+updates.%0A-+Google+Drive%3A+link+briefs%2C+budgets%2C+run-of-show+documents%2C+and+event+assets.%0A-+Notion%3A+surface+event+policies%2C+approval+guidance%2C+and+reusable+playbooks.%0A-+If+a+connected+source+does+not+contain+useful+results%2C+use+realistic+seeded+examples+and+keep+the+source+references+configurable.+Do+not+expose+unrelated+or+sensitive+workspace+content.%0A%0ABuild+an+event+intake+workflow+available+to+all+workspace+users.+The+intake+form+should+include%3A%0A-+Event+title%0A-+Event+type%0A-+Audience%0A-+Assigned+owner%0A-+Objective%0A-+Date+range%0A-+Location+or+virtual+format%0A-+Budget%0A-+Expected+headcount%0A-+Vendors%0A-+Policy+needs%0A-+Notes+and+relevant+resource+links%0A%0APermissions%3A%0A-+Any+workspace+user+can+submit+an+intake+request.%0A-+Only+the+assigned+event+owner+can+accept+or+reject+the+request.%0A-+Enforce+owner-only+acceptance+server-side%2C+not+only+in+the+interface.%0A%0ACreate+separate+views+for%3A%0A-+Overview+dashboard%0A-+Active+intake+requests%0A-+Upcoming+events%0A-+Past+events%0A-+Templates%0A-+Policies+and+playbooks%0A%0AAllow+users+to+duplicate+a+past+event+or+start+from+templates+such+as%3A%0A-+Meetup%0A-+Customer+dinner%0A-+Webinar%0A-+Recruiting+event%0A-+Team+offsite%0A%0AEach+event+detail+page+should+include%3A%0A-+Event+health+summary+with+clear+status+signals%0A-+Timeline+and+milestones%0A-+Tasks+and+owners%0A-+Resource+links+from+Drive%2C+Slack%2C+Notion%2C+and+Calendar%0A-+Approval+status%0A-+Owner+comments%0A-+Policy+checklist%0A-+Activity+updates%0A%0AInclude+policy+checklist+items+for%3A%0A-+General+approvals%0A-+Accessibility%0A-+Swag%0A-+Vendor+review%0A-+Privacy%0A-+Communications%0A%0AUse+D1+as+the+authoritative+data+store+for%3A%0A-+Event+records%0A-+Intake+status%0A-+Approvals%0A-+Template+metadata%0A-+Tasks+and+task+status%0A-+Policy+checklist+progress%0A-+Resource+links%0A-+Comments%0A%0AUse+R2+only+if+real+file+uploads+are+implemented.+Otherwise%2C+store+Google+Drive+references+rather+than+duplicating+files.%0A%0ADesign+direction%3A%0A-+Make+the+interface+feel+like+an+operations+command+center+for+event+owners.%0A-+Use+a+modern%2C+elevated+dashboard+style+with+a+dark+navigation+sidebar%2C+a+light+content+canvas%2C+polished+cards%2C+strong+information+hierarchy%2C+and+joyful+accent+colors.%0A-+Prioritize+quick+scanning%3A+show+pending+approvals%2C+policy+readiness%2C+upcoming+milestones%2C+scheduling+conflicts%2C+event+health%2C+and+recent+planning+activity+prominently.%0A-+Use+realistic+company-specific+examples+derived+from+the+connected+sources+when+appropriate.%0A%0ABefore+deployment%3A%0A-+Verify+that+the+production+build+succeeds.%0A-+Perform+a+visual+review+of+the+dashboard%2C+intake+flow%2C+event+detail+view%2C+and+responsive+layout.%0A-+Deploy+with+workspace-wide+access.)

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

GPT-5.5  Vinext](/showcase/enablement-hub)[![Launch Cal](/showcase/sites-launch-cal.jpg)

### Launch Cal

A monthly product and feature calendar with team, status, surface, risk...

GPT-5.5  Vinext](/showcase/launch-cal)[![Onboarding Hub](/showcase/sites-onboarding-hub.png)

### Onboarding Hub

A personalized new-hire dashboard with current progress, suggested...

GPT-5.5  Vinext](/showcase/onboarding-hub)

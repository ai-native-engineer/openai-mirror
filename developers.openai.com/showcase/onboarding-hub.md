<!-- source: https://developers.openai.com/showcase/onboarding-hub/ -->

## Search developer resources

[← All sites](/showcase/sites) 

![Onboarding Hub app screenshot](/showcase/sites-onboarding-hub.png)

Description

A personalized new-hire dashboard with current progress, suggested meetings, a first-week checklist, and a browsable resource library.

## Prompt

Copy prompt
 

@site-creator Build a new-hire-facing internal site called **Onboarding Hub**.

Use @notion to find the company’s onboarding plans, @google-drive to find relevant docs and slide decks, and @slack to find broadly useful onboarding channels, support channels, announcement channels, cohort channels, and welcome threads.

Base the dashboard content on the company’s real resources. Do not hardcode checklist items, meetings, channels, or resource links. Prefer company-wide guidance over team-specific material unless a source explicitly indicates that it applies to the authenticated user’s team or role.

Use the authenticated-user email header to personalize the greeting:
`Welcome, <first name>`

Create one unified **first-week checklist** derived from the discovered onboarding materials. Include required setup tasks in the same checklist rather than a separate card. Every checkbox must contribute to one current-progress total.

Each checklist item should show:
- Completion state
- Due date
- Link to its source document, slide deck, internal page, or Slack thread

Do not show owners or DRIs in the checklist. Save checkbox changes to D1 immediately and restore them after reload.

Create a **Suggested meetings** card based on the onboarding plan and welcome materials. Include relevant first-week sessions, introductions, manager meetings, buddy meetings, or new-joiner sessions when supported by the sources. Do not show individual `+` buttons beside meetings. Include one `Plan my first week` action pinned to the bottom of the card.

Create a full-width **Resource library** below the progress, meetings, and checklist cards. Group discovered resources into the most appropriate categories, using these as a starting point when relevant:
- Company basics
- Benefits
- Security
- Team rituals
- Product knowledge
- Engineering setup

Each resource should link to its real source and support D1-backed bookmarks. Omit empty categories and add better company-specific categories when the source materials call for them.

Include a lower row with:
- **Your documents**
- **Notes for your manager**
- **Helpful Slack channels**

Populate Helpful Slack channels from the company’s real workspace. Prefer generally useful onboarding, announcement, support, employee-question, and culture channels. Include role-specific channels only when clearly appropriate for the user.

The notes card should stretch to the full height of the row and include a tall textarea.

Users should be able to upload:
- Profile picture: PNG or JPG, up to 5 MB
- Signed employee handbook: PDF, up to 10 MB

Store uploaded file bytes in R2 and file metadata in D1. Restore uploaded document states after reload. Allow users to replace or remove uploaded files. Replacing or clearing a file must remove the previous R2 object and its D1 metadata.

Use D1 for:
- Checklist completion
- Bookmarks
- Notes
- Manager overrides
- Uploaded-document metadata

Use R2 for:
- User-uploaded document bytes

Design the site as a calm employee-facing dashboard with clear next steps and low cognitive load. Use a bento-box layout:
- Current progress in the upper-left card
- Unified first-week checklist on the right
- Suggested meetings beneath progress, stretched so its bottom aligns with the checklist
- Full-width resource library below those cards
- Documents, notes, and helpful Slack channels in the lower row

Use the product name **Onboarding Hub** in the header. Do not show a week/date chip. Avoid role-specific badges and personalization labels. Only the **Current progress** card should have an eyebrow label.

[Try in Codex](codex://threads/new?prompt=%40site-creator+Build+a+new-hire-facing+internal+site+called+**Onboarding+Hub**.%0A%0AUse+%40notion+to+find+the+company%E2%80%99s+onboarding+plans%2C+%40google-drive+to+find+relevant+docs+and+slide+decks%2C+and+%40slack+to+find+broadly+useful+onboarding+channels%2C+support+channels%2C+announcement+channels%2C+cohort+channels%2C+and+welcome+threads.%0A%0ABase+the+dashboard+content+on+the+company%E2%80%99s+real+resources.+Do+not+hardcode+checklist+items%2C+meetings%2C+channels%2C+or+resource+links.+Prefer+company-wide+guidance+over+team-specific+material+unless+a+source+explicitly+indicates+that+it+applies+to+the+authenticated+user%E2%80%99s+team+or+role.%0A%0AUse+the+authenticated-user+email+header+to+personalize+the+greeting%3A%0A%60Welcome%2C+%3Cfirst+name%3E%60%0A%0ACreate+one+unified+**first-week+checklist**+derived+from+the+discovered+onboarding+materials.+Include+required+setup+tasks+in+the+same+checklist+rather+than+a+separate+card.+Every+checkbox+must+contribute+to+one+current-progress+total.%0A%0AEach+checklist+item+should+show%3A%0A-+Completion+state%0A-+Due+date%0A-+Link+to+its+source+document%2C+slide+deck%2C+internal+page%2C+or+Slack+thread%0A%0ADo+not+show+owners+or+DRIs+in+the+checklist.+Save+checkbox+changes+to+D1+immediately+and+restore+them+after+reload.%0A%0ACreate+a+**Suggested+meetings**+card+based+on+the+onboarding+plan+and+welcome+materials.+Include+relevant+first-week+sessions%2C+introductions%2C+manager+meetings%2C+buddy+meetings%2C+or+new-joiner+sessions+when+supported+by+the+sources.+Do+not+show+individual+%60%2B%60+buttons+beside+meetings.+Include+one+%60Plan+my+first+week%60+action+pinned+to+the+bottom+of+the+card.%0A%0ACreate+a+full-width+**Resource+library**+below+the+progress%2C+meetings%2C+and+checklist+cards.+Group+discovered+resources+into+the+most+appropriate+categories%2C+using+these+as+a+starting+point+when+relevant%3A%0A-+Company+basics%0A-+Benefits%0A-+Security%0A-+Team+rituals%0A-+Product+knowledge%0A-+Engineering+setup%0A%0AEach+resource+should+link+to+its+real+source+and+support+D1-backed+bookmarks.+Omit+empty+categories+and+add+better+company-specific+categories+when+the+source+materials+call+for+them.%0A%0AInclude+a+lower+row+with%3A%0A-+**Your+documents**%0A-+**Notes+for+your+manager**%0A-+**Helpful+Slack+channels**%0A%0APopulate+Helpful+Slack+channels+from+the+company%E2%80%99s+real+workspace.+Prefer+generally+useful+onboarding%2C+announcement%2C+support%2C+employee-question%2C+and+culture+channels.+Include+role-specific+channels+only+when+clearly+appropriate+for+the+user.%0A%0AThe+notes+card+should+stretch+to+the+full+height+of+the+row+and+include+a+tall+textarea.%0A%0AUsers+should+be+able+to+upload%3A%0A-+Profile+picture%3A+PNG+or+JPG%2C+up+to+5+MB%0A-+Signed+employee+handbook%3A+PDF%2C+up+to+10+MB%0A%0AStore+uploaded+file+bytes+in+R2+and+file+metadata+in+D1.+Restore+uploaded+document+states+after+reload.+Allow+users+to+replace+or+remove+uploaded+files.+Replacing+or+clearing+a+file+must+remove+the+previous+R2+object+and+its+D1+metadata.%0A%0AUse+D1+for%3A%0A-+Checklist+completion%0A-+Bookmarks%0A-+Notes%0A-+Manager+overrides%0A-+Uploaded-document+metadata%0A%0AUse+R2+for%3A%0A-+User-uploaded+document+bytes%0A%0ADesign+the+site+as+a+calm+employee-facing+dashboard+with+clear+next+steps+and+low+cognitive+load.+Use+a+bento-box+layout%3A%0A-+Current+progress+in+the+upper-left+card%0A-+Unified+first-week+checklist+on+the+right%0A-+Suggested+meetings+beneath+progress%2C+stretched+so+its+bottom+aligns+with+the+checklist%0A-+Full-width+resource+library+below+those+cards%0A-+Documents%2C+notes%2C+and+helpful+Slack+channels+in+the+lower+row%0A%0AUse+the+product+name+**Onboarding+Hub**+in+the+header.+Do+not+show+a+week%2Fdate+chip.+Avoid+role-specific+badges+and+personalization+labels.+Only+the+**Current+progress**+card+should+have+an+eyebrow+label.)

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

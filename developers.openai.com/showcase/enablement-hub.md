<!-- source: https://developers.openai.com/showcase/enablement-hub/ -->

## Search developer resources

[← All sites](/showcase/sites) 

![Enablement Hub app screenshot](/showcase/sites-enablement-hub.png)

Description

An internal learning hub with featured training, announcements, and a resource grid filtered by role, team, product area, level, format, and freshness.

## Prompt

Copy prompt
 

@site-creator Build and deploy an internal Enablement Hub for our company.

Use @google-drive to find relevant training decks, documents, and recordings, @notion for resource pages and playbooks, and @slack for announcements and recommended learning links. Also include useful external training resources from our company’s official academy, documentation, and developer sites when available.

The app should list training resources, demos, playbooks, important links, recordings, and relevant Slack announcements. Store the catalog in D1.

Organize resources by:
- Role
- Team
- Product area
- Difficulty
- Format
- Freshness

Build a dynamic resources grid that updates immediately when users search or change filters. On desktop, place the search field and all filters on the same row. Allow controls to wrap cleanly on smaller screens.

Add bookmarks:
- Each resource card should have a selectable bookmark control.
- Save bookmarks per authenticated employee in D1.
- Add a “My learning” tab in the top navigation.
- Populate “My learning” with the employee’s bookmarked resources.
- Bookmarks must persist after reloads and across sessions.
- Show a helpful empty state when no resources have been saved.

Use the workspace-authenticated employee identity. In the top navigation, show a compact circular avatar containing only the uppercase first letter of the employee’s email alias. For example, `jamie.smith@company.com` should display `J`.

Design the app as a modern, airy internal hub with:
- A clean top navigation with “Discover” and “My learning”
- A bento-box Overview section without an “Overview” title
- Bento cards for a featured learning path, an important announcement, a key update, and newly added resources
- A Resources section below with the search and filter bar, resource count, and responsive content grid
- Clear visual source indicators for Drive, Notion, Slack, official academy content, and developer documentation

Use realistic content discovered from the connected company sources rather than placeholder text. Keep the design polished and responsive. Validate the D1 migrations, bookmark persistence, authenticated avatar letter, search behavior, filters, and mobile layout before deploying.

[Try in Codex](codex://threads/new?prompt=%40site-creator+Build+and+deploy+an+internal+Enablement+Hub+for+our+company.%0A%0AUse+%40google-drive+to+find+relevant+training+decks%2C+documents%2C+and+recordings%2C+%40notion+for+resource+pages+and+playbooks%2C+and+%40slack+for+announcements+and+recommended+learning+links.+Also+include+useful+external+training+resources+from+our+company%E2%80%99s+official+academy%2C+documentation%2C+and+developer+sites+when+available.%0A%0AThe+app+should+list+training+resources%2C+demos%2C+playbooks%2C+important+links%2C+recordings%2C+and+relevant+Slack+announcements.+Store+the+catalog+in+D1.%0A%0AOrganize+resources+by%3A%0A-+Role%0A-+Team%0A-+Product+area%0A-+Difficulty%0A-+Format%0A-+Freshness%0A%0ABuild+a+dynamic+resources+grid+that+updates+immediately+when+users+search+or+change+filters.+On+desktop%2C+place+the+search+field+and+all+filters+on+the+same+row.+Allow+controls+to+wrap+cleanly+on+smaller+screens.%0A%0AAdd+bookmarks%3A%0A-+Each+resource+card+should+have+a+selectable+bookmark+control.%0A-+Save+bookmarks+per+authenticated+employee+in+D1.%0A-+Add+a+%E2%80%9CMy+learning%E2%80%9D+tab+in+the+top+navigation.%0A-+Populate+%E2%80%9CMy+learning%E2%80%9D+with+the+employee%E2%80%99s+bookmarked+resources.%0A-+Bookmarks+must+persist+after+reloads+and+across+sessions.%0A-+Show+a+helpful+empty+state+when+no+resources+have+been+saved.%0A%0AUse+the+workspace-authenticated+employee+identity.+In+the+top+navigation%2C+show+a+compact+circular+avatar+containing+only+the+uppercase+first+letter+of+the+employee%E2%80%99s+email+alias.+For+example%2C+%60jamie.smith%40company.com%60+should+display+%60J%60.%0A%0ADesign+the+app+as+a+modern%2C+airy+internal+hub+with%3A%0A-+A+clean+top+navigation+with+%E2%80%9CDiscover%E2%80%9D+and+%E2%80%9CMy+learning%E2%80%9D%0A-+A+bento-box+Overview+section+without+an+%E2%80%9COverview%E2%80%9D+title%0A-+Bento+cards+for+a+featured+learning+path%2C+an+important+announcement%2C+a+key+update%2C+and+newly+added+resources%0A-+A+Resources+section+below+with+the+search+and+filter+bar%2C+resource+count%2C+and+responsive+content+grid%0A-+Clear+visual+source+indicators+for+Drive%2C+Notion%2C+Slack%2C+official+academy+content%2C+and+developer+documentation%0A%0AUse+realistic+content+discovered+from+the+connected+company+sources+rather+than+placeholder+text.+Keep+the+design+polished+and+responsive.+Validate+the+D1+migrations%2C+bookmark+persistence%2C+authenticated+avatar+letter%2C+search+behavior%2C+filters%2C+and+mobile+layout+before+deploying.)

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

[![Event Planning Hub](/showcase/sites-event-planning-hub.jpg)

### Event Planning Hub

An event planning dashboard with active request triage, event templates...

GPT-5.5  Vinext](/showcase/event-planning-hub)[![Launch Cal](/showcase/sites-launch-cal.jpg)

### Launch Cal

A monthly product and feature calendar with team, status, surface, risk...

GPT-5.5  Vinext](/showcase/launch-cal)[![Onboarding Hub](/showcase/sites-onboarding-hub.png)

### Onboarding Hub

A personalized new-hire dashboard with current progress, suggested...

GPT-5.5  Vinext](/showcase/onboarding-hub)

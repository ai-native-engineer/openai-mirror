<!-- source: https://developers.openai.com/showcase/pulse-dashboard/ -->

## Search developer resources

[← All sites](/showcase/sites) 

![Pulse Dashboard app screenshot](/showcase/sites-pulse-dashboard.png)

Description

An executive dashboard with KPI cards, momentum trends, revenue targets, a metric health table, and an operator-ready lineage drawer.

## Prompt

Copy prompt
 

@site-creator Build an internal company Pulse Dashboard.

Use @kepler as the primary metrics and warehouse query tool, @slack for metric discussions, and @spreadsheets for manually maintained targets.

Create a clean, executive-readable KPI dashboard using metrics relevant to the company and informed by active Slack discussions. Keep the interface modern, airy, and restrained, with subtle accent colors.

## Main Layout

Do not add a top navigation bar. Start directly with the dashboard title and a short descriptive subtitle.

Place a compact Filters control and a functional timing-window dropdown near the title. Support rolling 4-week, 12-week, 26-week, and 52-week views. Changing the timing window must update KPI values, deltas, charts, targets, and table labels.

Do not add a fake refresh button, dead links, warning banners, Data operations cards, or Recent annotations cards.

## KPI Cards

Show the main KPIs in a prominent card grid. Each KPI card must display:

- Current value
- Delta for the selected timing window
- Freshness
- Compact trend visualization
- Status such as fresh, partial, stale, or permission denied

Make every dashboard card clickable, not only the top KPI cards. Clicking a card should open the most relevant metric lineage detail.

Use a subtle neutral badge for cached-preview or partial-source states. Avoid prominent yellow warning treatments.

## Charts And Targets

Include:

- A product or business momentum chart that updates with the selected timing window
- A target-attainment card sourced from the maintained spreadsheet
- A full-width Metric health table

The Metric health table should show:

- Metric
- Status
- Coverage
- Selected-window change
- Trend

## Metric Lineage Drawer

Add a metric lineage drawer for operator debugging. It should show:

- Selected metric name and description
- Status, coverage, and freshness
- Source tables, fields, and saved queries from Kepler
- A link to the underlying saved query
- A Discussion or support section with a relevant Slack channel

Use real Slack channels when available. Otherwise, hide this section.

Do not include a generic Query states legend in the drawer.

## Data And Caching

Use D1 to persist:

- Dashboard configurations
- Saved filters
- Metric annotations for future operator workflows
- A separate cached metric snapshot for each supported timing window

Seed only missing timing-window caches. Do not overwrite a previously refreshed cached snapshot when the dashboard loads.

Show loading, stale, partial-data, and permission-denied states contextually on metrics and inside the lineage drawer, without adding a large warning banner.

## Quality Bar

Keep the primary view calm and executive-focused. Operator detail should be available through clickable cards and the lineage drawer instead of cluttering the main dashboard.

[Try in Codex](codex://threads/new?prompt=%40site-creator+Build+an+internal+company+Pulse+Dashboard.%0A%0AUse+%40kepler+as+the+primary+metrics+and+warehouse+query+tool%2C+%40slack+for+metric+discussions%2C+and+%40spreadsheets+for+manually+maintained+targets.%0A%0ACreate+a+clean%2C+executive-readable+KPI+dashboard+using+metrics+relevant+to+the+company+and+informed+by+active+Slack+discussions.+Keep+the+interface+modern%2C+airy%2C+and+restrained%2C+with+subtle+accent+colors.%0A%0A%23%23+Main+Layout%0A%0ADo+not+add+a+top+navigation+bar.+Start+directly+with+the+dashboard+title+and+a+short+descriptive+subtitle.%0A%0APlace+a+compact+Filters+control+and+a+functional+timing-window+dropdown+near+the+title.+Support+rolling+4-week%2C+12-week%2C+26-week%2C+and+52-week+views.+Changing+the+timing+window+must+update+KPI+values%2C+deltas%2C+charts%2C+targets%2C+and+table+labels.%0A%0ADo+not+add+a+fake+refresh+button%2C+dead+links%2C+warning+banners%2C+Data+operations+cards%2C+or+Recent+annotations+cards.%0A%0A%23%23+KPI+Cards%0A%0AShow+the+main+KPIs+in+a+prominent+card+grid.+Each+KPI+card+must+display%3A%0A%0A-+Current+value%0A-+Delta+for+the+selected+timing+window%0A-+Freshness%0A-+Compact+trend+visualization%0A-+Status+such+as+fresh%2C+partial%2C+stale%2C+or+permission+denied%0A%0AMake+every+dashboard+card+clickable%2C+not+only+the+top+KPI+cards.+Clicking+a+card+should+open+the+most+relevant+metric+lineage+detail.%0A%0AUse+a+subtle+neutral+badge+for+cached-preview+or+partial-source+states.+Avoid+prominent+yellow+warning+treatments.%0A%0A%23%23+Charts+And+Targets%0A%0AInclude%3A%0A%0A-+A+product+or+business+momentum+chart+that+updates+with+the+selected+timing+window%0A-+A+target-attainment+card+sourced+from+the+maintained+spreadsheet%0A-+A+full-width+Metric+health+table%0A%0AThe+Metric+health+table+should+show%3A%0A%0A-+Metric%0A-+Status%0A-+Coverage%0A-+Selected-window+change%0A-+Trend%0A%0A%23%23+Metric+Lineage+Drawer%0A%0AAdd+a+metric+lineage+drawer+for+operator+debugging.+It+should+show%3A%0A%0A-+Selected+metric+name+and+description%0A-+Status%2C+coverage%2C+and+freshness%0A-+Source+tables%2C+fields%2C+and+saved+queries+from+Kepler%0A-+A+link+to+the+underlying+saved+query%0A-+A+Discussion+or+support+section+with+a+relevant+Slack+channel%0A%0AUse+real+Slack+channels+when+available.+Otherwise%2C+hide+this+section.%0A%0ADo+not+include+a+generic+Query+states+legend+in+the+drawer.%0A%0A%23%23+Data+And+Caching%0A%0AUse+D1+to+persist%3A%0A%0A-+Dashboard+configurations%0A-+Saved+filters%0A-+Metric+annotations+for+future+operator+workflows%0A-+A+separate+cached+metric+snapshot+for+each+supported+timing+window%0A%0ASeed+only+missing+timing-window+caches.+Do+not+overwrite+a+previously+refreshed+cached+snapshot+when+the+dashboard+loads.%0A%0AShow+loading%2C+stale%2C+partial-data%2C+and+permission-denied+states+contextually+on+metrics+and+inside+the+lineage+drawer%2C+without+adding+a+large+warning+banner.%0A%0A%23%23+Quality+Bar%0A%0AKeep+the+primary+view+calm+and+executive-focused.+Operator+detail+should+be+available+through+clickable+cards+and+the+lineage+drawer+instead+of+cluttering+the+main+dashboard.)

Built with

Sites in Codex

Model

GPT-5.5

Tech stack

Vinext

Use case

[Data visualization](/showcase?use_case=data-visualization)

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

<!-- source: https://developers.openai.com/learn/developers-codex-plugin/ -->

## Search developer resources

The OpenAI Developers plugin helps you build AI applications and agents in
Codex with OpenAI Platform access and OpenAI API setup guidance. Adaptations
for Claude Code and Cursor bundle the portable developer skills and public
OpenAI Docs MCP server without the Codex-specific Platform connector. The Codex
plugin works together with the
[OpenAI Docs Skill](https://github.com/openai/skills/tree/main/skills/.curated/openai-docs)
that comes bundled with your Codex install.

It includes:

* **OpenAI API Platform:** connect Codex to the
  [OpenAI API Platform](https://platform.openai.com/).
* **OpenAI Docs MCP:** use current OpenAI documentation from Claude Code or
  Cursor.
* **API key setup:** create, save, and connect a project API key from Codex, or
  get guided local `OPENAI_API_KEY` setup in Claude Code and Cursor.
* **Agents SDK:** build and deploy OpenAI Agents SDK apps from an idea, a repo,
  or a prior Codex thread.
* **Troubleshooting:** identify common OpenAI API failures and route
  you to the right next step.

## Get started with Codex

If you are new to Codex, start here before installing the plugin:

1. [Download the Codex app](/codex/app#getting-started) for macOS or Windows.
2. Follow the [Codex quickstart](/codex/quickstart) to sign in, choose a
   project, and send your first message.

## Install the plugin

Choose an option 

Codex appCodex CLIClaude appClaude Code CLICursor

[Install the OpenAI Developers plugin](codex://plugins/install/openai-developers?marketplace=openai-curated)

1. Open Codex

   Start Codex from your terminal:

   codex
2. Open the plugin browser

   Run:

   /plugins
3. Install the plugin

   Search for **OpenAI Developers**, open it, and select `Install plugin`.
4. Complete any setup prompts

   If Codex asks you to connect the bundled OpenAI Platform app, complete
   that setup so the plugin can create project API keys when needed.
5. Start a new thread

   Open a new thread before using the plugin for the first time.

1. Open the plugin settings

   In the Claude app, open **Settings**, then select **Plugins**.
2. Add the marketplace

   Select **Add** in the top-right corner, then choose **Add Marketplace**.
   In the modal, select **Add from a repository**.
3. Add the repository

   Enter `https://github.com/openai/openai-developers-for-claude` and select
   **Sync**. Do not append a `.git` suffix.
4. Install the plugin

   When **OpenAI Developers** appears, open it and select **Install**.

1. Add the plugin marketplace

   In Claude Code, run:

   /plugin marketplace add openai/openai-developers-for-claude
2. Install the plugin

   Run:

   /plugin install openai-developers@openai-developers
3. Start a new session

   Start a new Claude Code session before using the plugin for the first
   time.

1. Open the plugin settings

   In Cursor, open **Settings**, then select **Plugins**.
2. Add the repository

   Paste `https://github.com/openai/openai-developers-for-cursor` into the
   plugin search box.
3. Install the plugin

   When **OpenAI Developers** appears, open it and select **Install**.

## Use the plugin

After installation, start building with your coding agent. Codex can use the
plugin automatically when the task calls for OpenAI Platform interactions, such
as creating API keys or troubleshooting API issues. Claude Code and Cursor can
use the plugin’s skills and bundled Docs MCP server for OpenAI API, model,
Agents SDK, and ChatGPT Apps guidance.

The plugin is useful when you want your coding agent to:

* build an app or agent that uses the OpenAI API
* set up OpenAI API access for the app you are building
* diagnose common OpenAI API errors and explain the next step.

## Sample prompts

### Build a new app

### Build an app with the Responses API

Create a campaign studio that turns a brief into polished copy and generated visual directions.

Copy
 [Open in Codex](codex://new?prompt=Build+a+full-stack+campaign+concept+studio+for+marketing+teams+using+the+current+OpenAI+Responses+API.%0A%0AThe+app+should+let+a+user+enter+a+short+campaign+brief%2C+target+audience%2C+product+details%2C+tone%2C+and+desired+channels.+It+should+generate%3A%0A%0A-+a+concise+campaign+concept%0A-+3+headline%2Fbody+copy+variants%0A-+a+launch+checklist%0A-+image+prompts+and+generated+images+for+the+campaign+direction%0A%0ARequirements%3A%0A%0A-+Use+the+current+OpenAI+API+patterns+for+the+Responses+API%2C+not+legacy+Completions+or+Chat+Completions+code.%0A-+Use+text+generation+and+image+generation+in+the+flow.%0A-+Create+a+clean%2C+production-quality+UI+with+loading%2C+error%2C+and+empty+states.%0A-+Keep+server-side+OpenAI+calls+off+the+client+and+document+the+client%2Fserver+boundary.%0A-+Include+OPENAI_API_KEY+environment+variable+setup.%0A-+Add+a+README+with+install%2C+run%2C+and+deployment+notes.%0A-+Add+a+small+validation+plan+and+explain+where+to+adjust+the+model%2C+prompt%2C+and+image+settings+later.%0A%0ADocumentation%3A%0A%0A-+If+the+OpenAI+Docs+skill+is+available%2C+use+it+to+verify+the+latest+OpenAI+API+guidance+before+implementing.%0A-+If+the+OpenAI+Docs+skill+is+not+available%2C+install+the+OpenAI+Docs+skill+and+use+it.%0A-+If+the+OpenAI+Docs+skill+cannot+be+installed+or+used%2C+use+web+search+to+search+the+latest+OpenAI+developer+documentation+on+developers.openai.com%2Fapi.%0A-+Reference+https%3A%2F%2Fdevelopers.openai.com%2Fapi%2Fdocs%2Fmodels+for+guidance+on+the+latest+models+to+use.%0A%0AFrontend%3A%0A%0A-+If+the+Frontend+skill+is+installed%2C+use+it+for+frontend+implementation+and+polish.%0A-+If+the+Frontend+skill+is+not+installed%2C+install+the+Frontend+skill+and+use+it.+%5B%40OpenAI+Developers%5D%28plugin%3A%2F%2Fopenai-developers%40openai-curated%29)

### Build an agent with the Agents SDK

Create a launch-planning agent with a frontend, useful tools, and observability hooks.

Copy
 [Open in Codex](codex://new?prompt=Build+a+working+launch-planning+agent+app+called+%22Launch+Desk%22+using+the+current+OpenAI+Agents+SDK.%0A%0AThe+app+should+help+an+engineering+team+turn+a+rough+launch+idea+into+an+actionable+release+plan.+Users+should+enter+a+product+brief%2C+audience%2C+launch+date%2C+constraints%2C+and+available+assets+in+a+frontend+UI.+The+agent+should+respond+with+a+prioritized+plan%2C+risk+register%2C+owner+checklist%2C+launch+copy+suggestions%2C+and+follow-up+questions+when+key+details+are+missing.%0A%0ARequirements%3A%0A%0A-+Build+a+polished+frontend+for+interacting+with+the+agent.+Do+not+make+this+a+CLI-only+tool.%0A-+Build+the+agent+with+clear+instructions+and+a+project+structure+that+separates+frontend+UI%2C+server%2FAPI+routes%2C+agent+setup%2C+tools%2C+and+tests.%0A-+Include+useful+tool+patterns%2C+such+as+extracting+tasks+from+the+brief%2C+checking+launch+readiness+against+a+rubric%2C+generating+owner+checklists%2C+and+drafting+channel-specific+launch+copy.%0A-+Include+streaming+or+progressive+response+updates%2C+and+verify+them+end-to-end+by+posting+to+the+local+API+route+and+reading+the+stream+until+at+least+one+tool+progress+event+and+one+model+text+delta+are+received.%0A-+Include+tracing+or+observability+hooks+if+idiomatic.%0A-+Include+OPENAI_API_KEY+environment+variable+setup+and+local+setup+instructions.%0A-+Make+it+easy+for+a+developer+to+understand%2C+run%2C+test%2C+and+extend+with+new+tools+or+handoffs.%0A-+Add+a+README+and+a+validation+checklist+for+the+agent+behavior%2C+frontend+flow%2C+and+tool+outputs.%0A-+Use+current+OpenAI+API+and+Agents+SDK+patterns.+Do+not+use+deprecated+Assistants+API+or+legacy+Chat+Completions+scaffolding+unless+you+explicitly+explain+why+a+compatibility+shim+is+needed.%0A%0ALocal+run+and+verification+requirement%3A%0AAfter+implementing%2C+start+the+frontend+and+backend+dev+servers+in+a+way+that+can+actually+reach+the+OpenAI+API+from+the+server+process.+If+the+environment+uses+sandboxed+command+execution%2C+do+not+assume+localhost+success+means+OpenAI+API+access+works.+Verify+the+agent+endpoint+with+a+real+streamed+POST+request+to+the+local+API+and+confirm+that+it+emits+at+least+one+tool+event+and+one+model+text+delta.+If+the+server+cannot+reach+the+OpenAI+API%2C+diagnose+and+fix+the+server+run+mode+or+clearly+report+the+exact+blocker.%0A%0ADo+not+finish+after+only+checking+%2Fapi%2Fhealth%2C+Vite+startup%2C+TypeScript%2C+or+unit+tests.+The+final+verification+must+include+an+end-to-end+agent+call+through+the+frontend%2FAPI+route+using+the+configured+OPENAI_API_KEY.%0A%0ADocumentation%3A%0A%0A-+If+the+OpenAI+Docs+skill+is+available%2C+use+it+to+verify+the+latest+OpenAI+API+guidance+before+implementing.%0A-+If+the+OpenAI+Docs+skill+is+not+available%2C+install+the+OpenAI+Docs+skill+and+use+it.%0A-+If+the+OpenAI+Docs+skill+cannot+be+installed+or+used%2C+use+web+search+to+search+the+latest+OpenAI+developer+documentation+on+developers.openai.com%2Fapi.%0A-+Reference+https%3A%2F%2Fdevelopers.openai.com%2Fapi%2Fdocs%2Fmodels+for+guidance+on+the+latest+models+to+use.%0A%0AFrontend%3A%0A%0A-+If+the+Frontend+skill+is+installed%2C+use+it+for+frontend+implementation+and+polish.%0A-+If+the+Frontend+skill+is+not+installed%2C+install+the+Frontend+skill+and+use+it.+%5B%40OpenAI+Developers%5D%28plugin%3A%2F%2Fopenai-developers%40openai-curated%29)

### Build a realtime audio app

Make a voice-first worldbuilding companion with low-latency audio interactions.

Copy
 [Open in Codex](codex://new?prompt=Build+a+creative+realtime+audio+app+called+%22World+Room%22+using+the+current+OpenAI+Realtime+API.%0A%0AThe+experience+should+let+a+user+speak+with+a+live+worldbuilding+companion+that+helps+invent+settings%2C+characters%2C+conflicts%2C+and+scene+hooks.+Audio+should+be+central+to+the+experience%2C+with+low-latency+turn-taking+and+a+playful+voice+interaction+model.%0A%0ARequirements%3A%0A%0A-+Use+the+current+Realtime+API+patterns+for+low-latency+audio%2C+not+a+request%2Fresponse+text-only+loop.%0A-+Support+audio+input+and+output%2C+and+include+text+transcript+display+if+practical.%0A-+Clearly+separate+browser%2Fclient+responsibilities+from+server%2Fsession-token+responsibilities.%0A-+Include+setup+steps+for+OPENAI_API_KEY+and+local+development.%0A-+Add+developer+notes+for+latency%2C+session+lifecycle%2C+permissions%2C+and+error+recovery.%0A-+Keep+the+UI+focused+and+polished+with+obvious+microphone%2Fsession+states.%0A-+Include+a+validation+checklist+for+testing+audio+permissions%2C+connection+recovery%2C+and+basic+conversation+quality.%0A%0ADocumentation%3A%0A%0A-+If+the+OpenAI+Docs+skill+is+available%2C+use+it+to+verify+the+latest+OpenAI+API+guidance+before+implementing.%0A-+If+the+OpenAI+Docs+skill+is+not+available%2C+install+the+OpenAI+Docs+skill+and+use+it.%0A-+If+the+OpenAI+Docs+skill+cannot+be+installed+or+used%2C+use+web+search+to+search+the+latest+OpenAI+developer+documentation+on+developers.openai.com%2Fapi.%0A-+Reference+https%3A%2F%2Fdevelopers.openai.com%2Fapi%2Fdocs%2Fmodels+for+guidance+on+the+latest+models+to+use.%0A%0AFrontend%3A%0A%0A-+If+the+Frontend+skill+is+installed%2C+use+it+for+frontend+implementation+and+polish.%0A-+If+the+Frontend+skill+is+not+installed%2C+install+the+Frontend+skill+and+use+it.+%5B%40OpenAI+Developers%5D%28plugin%3A%2F%2Fopenai-developers%40openai-curated%29)

### Improve an existing app

### Upgrade to the latest model

Create a no-code-change plan to modernize model/API usage while preserving behavior.

Copy
 [Open in Codex](codex://new?prompt=Inspect+this+repository%27s+OpenAI+integration+and+create+a+plan+to+upgrade+to+the+latest+recommended+model+and+API+patterns+for+this+app.+Do+not+change+code.%0A%0APlease%3A%0A%0A-+Find+all+OpenAI+SDK+calls%2C+model+names%2C+prompt+construction%2C+streaming+paths%2C+structured+outputs%2C+tool+usage%2C+and+tests.%0A-+Identify+outdated+model+usage+or+legacy+API+patterns.%0A-+Recommend+the+safest+current+API+path+for+this+app%2C+such+as+Responses+API+for+general+multimodal%2Ftool-using+workflows%2C+Agents+SDK+for+agentic+orchestration%2C+or+Realtime+API+for+low-latency+voice+experiences.%0A-+Produce+a+step-by-step+implementation+plan+that+preserves+behavior+and+public+interfaces+where+possible.%0A-+Flag+risky+changes%2C+compatibility+concerns%2C+and+areas+that+need+manual+review.%0A-+Recommend+the+tests%2C+fixtures%2C+and+docs+that+should+be+added+or+updated.%0A-+Finish+with+a+concise+migration+plan%2C+risk+notes%2C+and+a+validation+plan+I+can+run+locally.%0A%0ADocumentation%3A%0A%0A-+If+the+OpenAI+Docs+skill+is+available%2C+use+it+to+verify+the+latest+OpenAI+API+guidance+before+implementing.%0A-+If+the+OpenAI+Docs+skill+is+not+available%2C+install+the+OpenAI+Docs+skill+and+use+it.%0A-+If+the+OpenAI+Docs+skill+cannot+be+installed+or+used%2C+use+web+search+to+search+the+latest+OpenAI+developer+documentation+on+developers.openai.com%2Fapi.%0A-+Reference+https%3A%2F%2Fdevelopers.openai.com%2Fapi%2Fdocs%2Fmodels+for+guidance+on+the+latest+models+to+use.%0A%0AFrontend%3A%0A%0A-+If+the+Frontend+skill+is+installed%2C+use+it+for+frontend+implementation+and+polish.%0A-+If+the+Frontend+skill+is+not+installed%2C+install+the+Frontend+skill+and+use+it.+%5B%40OpenAI+Developers%5D%28plugin%3A%2F%2Fopenai-developers%40openai-curated%29)

### Optimize my API implementation

Create a no-code-change optimization plan for quality, latency, reliability, and cost.

Copy
 [Open in Codex](codex://new?prompt=Review+this+app%27s+OpenAI+API+implementation+and+create+a+plan+to+improve+quality%2C+latency%2C+reliability%2C+and+cost.+Do+not+change+code.%0A%0APlease%3A%0A%0A-+Trace+the+current+request+flow+from+UI%2FAPI+handlers+through+OpenAI+SDK+calls.%0A-+Look+for+opportunities+to+improve+model+choice%2C+prompting%2C+structured+outputs%2C+built-in+tools%2C+streaming%2C+retries%2C+timeouts%2C+caching%2C+multimodal+handling%2C+and+error+messages.%0A-+Propose+concrete+implementation+steps%2C+file+areas+to+touch%2C+and+sequencing.%0A-+Keep+the+plan+behavior-compatible+unless+there+is+a+strong+reason+to+change+behavior.%0A-+Recommend+tests+or+lightweight+validation+scripts+for+the+affected+paths.%0A-+Summarize+each+proposed+change+with+the+expected+benefit+and+tradeoff.%0A-+Call+out+follow-up+opportunities+that+need+product+or+infra+decisions+before+implementation.%0A%0ADocumentation%3A%0A%0A-+If+the+OpenAI+Docs+skill+is+available%2C+use+it+to+verify+the+latest+OpenAI+API+guidance+before+implementing.%0A-+If+the+OpenAI+Docs+skill+is+not+available%2C+install+the+OpenAI+Docs+skill+and+use+it.%0A-+If+the+OpenAI+Docs+skill+cannot+be+installed+or+used%2C+use+web+search+to+search+the+latest+OpenAI+developer+documentation+on+developers.openai.com%2Fapi.%0A-+Reference+https%3A%2F%2Fdevelopers.openai.com%2Fapi%2Fdocs%2Fmodels+for+guidance+on+the+latest+models+to+use.%0A%0AFrontend%3A%0A%0A-+If+the+Frontend+skill+is+installed%2C+use+it+for+frontend+implementation+and+polish.%0A-+If+the+Frontend+skill+is+not+installed%2C+install+the+Frontend+skill+and+use+it.+%5B%40OpenAI+Developers%5D%28plugin%3A%2F%2Fopenai-developers%40openai-curated%29)

### Migrate from Responses API to Agents SDK

Create a no-code-change migration plan for whether and how to move to the Agents SDK.

Copy
 [Open in Codex](codex://new?prompt=Inspect+this+existing+app+built+with+the+Responses+API+and+create+a+migration+plan+for+whether+it+should+move+to+the+OpenAI+Agents+SDK.+Do+not+change+code.%0A%0APlease%3A%0A%0A-+Map+the+current+Responses+API+workflows%2C+prompts%2C+tools%2C+streaming+behavior%2C+and+state+management.%0A-+Decide+whether+the+app+benefits+from+a+more+agentic+architecture+with+tools%2C+handoffs%2C+tracing%2C+or+streaming+orchestration.%0A-+If+the+migration+is+justified%2C+produce+a+scoped+migration+plan+toward+the+Agents+SDK+while+preserving+key+behavior+and+user+experience.%0A-+If+only+part+of+the+app+should+migrate%2C+define+the+boundary+and+explain+what+should+remain+on+the+Responses+API.%0A-+Recommend+tests+and+setup+docs+to+add+or+update.%0A-+Explain+the+proposed+architecture+changes%2C+especially+where+tools%2C+handoffs%2C+tracing%2C+or+streaming+add+value.%0A-+Finish+with+a+migration+plan%2C+rollback+notes%2C+and+a+validation+checklist.%0A%0ADocumentation%3A%0A%0A-+If+the+OpenAI+Docs+skill+is+available%2C+use+it+to+verify+the+latest+OpenAI+API+guidance+before+implementing.%0A-+If+the+OpenAI+Docs+skill+is+not+available%2C+install+the+OpenAI+Docs+skill+and+use+it.%0A-+If+the+OpenAI+Docs+skill+cannot+be+installed+or+used%2C+use+web+search+to+search+the+latest+OpenAI+developer+documentation+on+developers.openai.com%2Fapi.%0A-+Reference+https%3A%2F%2Fdevelopers.openai.com%2Fapi%2Fdocs%2Fmodels+for+guidance+on+the+latest+models+to+use.%0A%0AFrontend%3A%0A%0A-+If+the+Frontend+skill+is+installed%2C+use+it+for+frontend+implementation+and+polish.%0A-+If+the+Frontend+skill+is+not+installed%2C+install+the+Frontend+skill+and+use+it.+%5B%40OpenAI+Developers%5D%28plugin%3A%2F%2Fopenai-developers%40openai-curated%29)

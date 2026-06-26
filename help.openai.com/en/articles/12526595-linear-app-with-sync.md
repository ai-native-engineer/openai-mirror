<!-- source: https://help.openai.com/en/articles/12526595-linear-app-with-sync -->

# Linear - app with sync

Updated: 10 days ago

**Overview**  
  
The Linear app with sync lets ChatGPT securely access your team’s Linear issues and discussions to answer questions. You can connect, disconnect, or update the connection at any time. Once enabled, ChatGPT will automatically reference content in Linear when relevant.  
  
  
**Type**: app with sync  
  
  
**Where you can use it**: Chat  
  
  
[Learn more about connecting a new app](/en/articles/11487775-connectors-in-chatgpt#h_615184a466).

## Example prompts

* “Find Linear tickets related to ‘customer feedback’ and highlight common themes.”
* “Find all unresolved bugs related to authentication and check progress”

[Learn more about app use cases and prompts.](/en/articles/12084614-connector-use-cases-and-prompts)

# Capabilities and Permissions

#### What it can access

* **Supported:** Issues, tickets and comments
* **Not Indexed**: Attachments, or linked external integrations

#### What it can do

* Read access to issues and comments via the Linear API
* Supports both synced indexing and on-demand fetching of current ticket data
* Supports write actions where available, including creating Linear tickets

**Permissions requested (scopes):**

* `read`
* `write`

#### Known Limitations

* Attachments, images, or linked assets are not synced or searchable.
* Sync time varies depending on workspace size.
* A newly connected Linear account might take several hours or longer to sync, depending on ticket volume.
* Newly created issues may take a few hours to appear.
* Requires a Linear workspace with API access enabled; only tickets visible to the connected user are included.

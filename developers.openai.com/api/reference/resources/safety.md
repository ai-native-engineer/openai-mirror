<!-- source: https://developers.openai.com/api/reference/resources/safety/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Safety

#### SafetyAlerts

##### [Retrieve a safety alert](/api/reference/resources/safety/subresources/alerts/methods/retrieve)

GET/safety/alerts/{id}

##### ModelsExpand Collapse

SafetyAlert object { id, created\_at, error\_type, 6 more }

id: string

created\_at: number

formatunixtime

error\_type: "potentially\_unintended\_data\_transfer" or "potentially\_unintended\_data\_access" or "potentially\_unintended\_destructive\_activity" or "other"

One of the following:

"potentially\_unintended\_data\_transfer"

"potentially\_unintended\_data\_access"

"potentially\_unintended\_destructive\_activity"

"other"

model: string

object: "safety.alert"

reason: string or null

A customer-safe description derived from error\_type, or null for zero data retention requests.

request\_id: string

request\_paused: boolean

Whether block registration succeeded for this request. This does not confirm that response execution stopped.

response\_id: string

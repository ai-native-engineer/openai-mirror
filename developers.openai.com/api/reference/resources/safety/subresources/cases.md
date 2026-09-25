<!-- source: https://developers.openai.com/api/reference/resources/safety/subresources/cases/ -->

[Safety](/api/reference/resources/safety)

# Cases

##### [Get safety case](/api/reference/resources/safety/subresources/cases/methods/retrieve)

GET/safety/cases/{id}

##### ModelsExpand Collapse

SafetyCase object { id, created\_at, entity\_identifier, 3 more }

entity\_identifier: string

notice: object { type }

type: "warning" or "deactivation"

"warning"

"deactivation"

object: "safety.case"

reason: string or null

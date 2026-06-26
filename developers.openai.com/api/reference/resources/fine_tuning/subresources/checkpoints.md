<!-- source: https://developers.openai.com/api/reference/resources/fine_tuning/subresources/checkpoints/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Fine Tuning](/api/reference/resources/fine_tuning)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Checkpoints

#### CheckpointsPermissions

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [List checkpoint permissions](/api/reference/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/retrieve)

Deprecated

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [List checkpoint permissions](/api/reference/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/list)

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [Create checkpoint permissions](/api/reference/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/create)

POST/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [Delete checkpoint permission](/api/reference/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/delete)

DELETE/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions/{permission\_id}

##### ModelsExpand Collapse

PermissionRetrieveResponse object { data, has\_more, object, 2 more }

data: array of object { id, created\_at, object, project\_id }

id: string

The permission identifier, which can be referenced in the API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

object: "checkpoint.permission"

The object type, which is always “checkpoint.permission”.

project\_id: string

The project identifier that the permission is for.

has\_more: boolean

object: "list"

first\_id: optional string

last\_id: optional string

PermissionListResponse object { id, created\_at, object, project\_id }

The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

id: string

The permission identifier, which can be referenced in the API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

object: "checkpoint.permission"

The object type, which is always “checkpoint.permission”.

project\_id: string

The project identifier that the permission is for.

PermissionCreateResponse object { id, created\_at, object, project\_id }

The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

id: string

The permission identifier, which can be referenced in the API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

object: "checkpoint.permission"

The object type, which is always “checkpoint.permission”.

project\_id: string

The project identifier that the permission is for.

PermissionDeleteResponse object { id, deleted, object }

id: string

The ID of the fine-tuned model checkpoint permission that was deleted.

deleted: boolean

Whether the fine-tuned model checkpoint permission was successfully deleted.

object: "checkpoint.permission"

The object type, which is always “checkpoint.permission”.

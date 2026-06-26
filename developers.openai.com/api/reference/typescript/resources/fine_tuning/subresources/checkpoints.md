<!-- source: https://developers.openai.com/api/reference/typescript/resources/fine_tuning/subresources/checkpoints/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Fine Tuning](/api/reference/typescript/resources/fine_tuning)

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

##### [List checkpoint permissions](/api/reference/typescript/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/retrieve)

Deprecated

client.fineTuning.checkpoints.permissions.retrieve(stringfineTunedModelCheckpoint, PermissionRetrieveParams { after, limit, order, project\_id } query?, RequestOptionsoptions?): [PermissionRetrieveResponse](/api/reference/typescript/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_retrieve_response%20%3E%20(schema)) { data, has\_more, object, 2 more }

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [List checkpoint permissions](/api/reference/typescript/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/list)

client.fineTuning.checkpoints.permissions.list(stringfineTunedModelCheckpoint, PermissionListParams { after, limit, order, project\_id } query?, RequestOptionsoptions?): ConversationCursorPage<[PermissionListResponse](/api/reference/typescript/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_list_response%20%3E%20(schema)) { id, created\_at, object, project\_id } >

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [Create checkpoint permissions](/api/reference/typescript/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/create)

client.fineTuning.checkpoints.permissions.create(stringfineTunedModelCheckpoint, PermissionCreateParams { project\_ids } body, RequestOptionsoptions?): Page<[PermissionCreateResponse](/api/reference/typescript/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_create_response%20%3E%20(schema)) { id, created\_at, object, project\_id } >

POST/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [Delete checkpoint permission](/api/reference/typescript/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/delete)

client.fineTuning.checkpoints.permissions.delete(stringpermissionID, PermissionDeleteParams { fine\_tuned\_model\_checkpoint } params, RequestOptionsoptions?): [PermissionDeleteResponse](/api/reference/typescript/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions/{permission\_id}

##### ModelsExpand Collapse

PermissionRetrieveResponse { data, has\_more, object, 2 more }

data: Array<Data>

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

first\_id?: string | null

last\_id?: string | null

PermissionListResponse { id, created\_at, object, project\_id }

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

PermissionCreateResponse { id, created\_at, object, project\_id }

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

PermissionDeleteResponse { id, deleted, object }

id: string

The ID of the fine-tuned model checkpoint permission that was deleted.

deleted: boolean

Whether the fine-tuned model checkpoint permission was successfully deleted.

object: "checkpoint.permission"

The object type, which is always “checkpoint.permission”.

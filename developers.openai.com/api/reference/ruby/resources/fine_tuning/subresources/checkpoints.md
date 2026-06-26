<!-- source: https://developers.openai.com/api/reference/ruby/resources/fine_tuning/subresources/checkpoints/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Fine Tuning](/api/reference/ruby/resources/fine_tuning)

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

##### [List checkpoint permissions](/api/reference/ruby/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/retrieve)

Deprecated

fine\_tuning.checkpoints.permissions.retrieve(fine\_tuned\_model\_checkpoint, \*\*kwargs) -> [PermissionRetrieveResponse](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_retrieve_response%20%3E%20(schema)) { data, has\_more, object, 2 more }

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [List checkpoint permissions](/api/reference/ruby/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/list)

fine\_tuning.checkpoints.permissions.list(fine\_tuned\_model\_checkpoint, \*\*kwargs) -> ConversationCursorPage<[PermissionListResponse](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_list_response%20%3E%20(schema)) { id, created\_at, object, project\_id } >

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [Create checkpoint permissions](/api/reference/ruby/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/create)

fine\_tuning.checkpoints.permissions.create(fine\_tuned\_model\_checkpoint, \*\*kwargs) -> Page<[PermissionCreateResponse](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_create_response%20%3E%20(schema)) { id, created\_at, object, project\_id } >

POST/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [Delete checkpoint permission](/api/reference/ruby/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/delete)

fine\_tuning.checkpoints.permissions.delete(permission\_id, \*\*kwargs) -> [PermissionDeleteResponse](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions/{permission\_id}

##### ModelsExpand Collapse

class PermissionRetrieveResponse { data, has\_more, object, 2 more }

data: Array[Data{ id, created\_at, object, project\_id}]

id: String

The permission identifier, which can be referenced in the API endpoints.

created\_at: Integer

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

object: :"checkpoint.permission"

The object type, which is always “checkpoint.permission”.

project\_id: String

The project identifier that the permission is for.

has\_more: bool

object: :list

first\_id: String

last\_id: String

class PermissionListResponse { id, created\_at, object, project\_id }

The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

id: String

The permission identifier, which can be referenced in the API endpoints.

created\_at: Integer

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

object: :"checkpoint.permission"

The object type, which is always “checkpoint.permission”.

project\_id: String

The project identifier that the permission is for.

class PermissionCreateResponse { id, created\_at, object, project\_id }

The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

id: String

The permission identifier, which can be referenced in the API endpoints.

created\_at: Integer

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

object: :"checkpoint.permission"

The object type, which is always “checkpoint.permission”.

project\_id: String

The project identifier that the permission is for.

class PermissionDeleteResponse { id, deleted, object }

id: String

The ID of the fine-tuned model checkpoint permission that was deleted.

deleted: bool

Whether the fine-tuned model checkpoint permission was successfully deleted.

object: :"checkpoint.permission"

The object type, which is always “checkpoint.permission”.

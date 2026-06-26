<!-- source: https://developers.openai.com/api/reference/python/resources/fine_tuning/subresources/checkpoints/subresources/permissions/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Fine Tuning](/api/reference/python/resources/fine_tuning)

[Checkpoints](/api/reference/python/resources/fine_tuning/subresources/checkpoints)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Permissions

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [List checkpoint permissions](/api/reference/python/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/retrieve)

Deprecated

fine\_tuning.checkpoints.permissions.retrieve(strfine\_tuned\_model\_checkpoint, PermissionRetrieveParams\*\*kwargs)  -> [PermissionRetrieveResponse](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_retrieve_response%20%3E%20(schema))

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [List checkpoint permissions](/api/reference/python/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/list)

fine\_tuning.checkpoints.permissions.list(strfine\_tuned\_model\_checkpoint, PermissionListParams\*\*kwargs)  -> SyncConversationCursorPage[[PermissionListResponse](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_list_response%20%3E%20(schema))]

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [Create checkpoint permissions](/api/reference/python/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/create)

fine\_tuning.checkpoints.permissions.create(strfine\_tuned\_model\_checkpoint, PermissionCreateParams\*\*kwargs)  -> SyncPage[[PermissionCreateResponse](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_create_response%20%3E%20(schema))]

POST/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [Delete checkpoint permission](/api/reference/python/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/delete)

fine\_tuning.checkpoints.permissions.delete(strpermission\_id, PermissionDeleteParams\*\*kwargs)  -> [PermissionDeleteResponse](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_delete_response%20%3E%20(schema))

DELETE/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions/{permission\_id}

##### ModelsExpand Collapse

class PermissionRetrieveResponse: …

data: List[Data]

id: str

The permission identifier, which can be referenced in the API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

object: Literal["checkpoint.permission"]

The object type, which is always “checkpoint.permission”.

project\_id: str

The project identifier that the permission is for.

has\_more: bool

object: Literal["list"]

first\_id: Optional[str]

last\_id: Optional[str]

class PermissionListResponse: …

The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

id: str

The permission identifier, which can be referenced in the API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

object: Literal["checkpoint.permission"]

The object type, which is always “checkpoint.permission”.

project\_id: str

The project identifier that the permission is for.

class PermissionCreateResponse: …

The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

id: str

The permission identifier, which can be referenced in the API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

object: Literal["checkpoint.permission"]

The object type, which is always “checkpoint.permission”.

project\_id: str

The project identifier that the permission is for.

class PermissionDeleteResponse: …

id: str

The ID of the fine-tuned model checkpoint permission that was deleted.

deleted: bool

Whether the fine-tuned model checkpoint permission was successfully deleted.

object: Literal["checkpoint.permission"]

The object type, which is always “checkpoint.permission”.

<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/external_storage/ -->

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

# External Storage

##### [Create an external storage configuration](/api/reference/resources/admin/subresources/organization/subresources/external_storage/methods/create)

POST/organization/external\_storage

##### [Delete an external storage configuration](/api/reference/resources/admin/subresources/organization/subresources/external_storage/methods/delete)

DELETE/organization/external\_storage/{external\_storage\_id}

##### [List external storage configurations](/api/reference/resources/admin/subresources/organization/subresources/external_storage/methods/list)

GET/organization/external\_storage

##### [Get an external storage configuration](/api/reference/resources/admin/subresources/organization/subresources/external_storage/methods/retrieve)

GET/organization/external\_storage/{external\_storage\_id}

##### [Validate an external storage configuration](/api/reference/resources/admin/subresources/organization/subresources/external_storage/methods/validate)

POST/organization/external\_storage/{external\_storage\_id}/validate

##### ModelsExpand Collapse

AwsExternalStorageProvider object { account\_id, bucket, external\_id, 3 more }

account\_id: string

bucket: string

external\_id: string

region: string

role\_arn: string

type: "aws"

AzureExternalStorageProvider object { account\_name, container, region, 4 more }

account\_name: string

container: string

region: string

resource\_group: string

subscription\_id: string

tenant\_id: string

type: "azure"

ExternalStorageConfiguration object { id, created\_at, geography, 4 more }

geography: string

object: "organization.external\_storage"

project\_id: string

provider: [AwsExternalStorageProvider](/api/reference/resources/admin#(resource)%20admin.organization.external_storage%20%3E%20(model)%20aws_external_storage_provider%20%3E%20(schema)) { account\_id, bucket, external\_id, 3 more }  or [AzureExternalStorageProvider](/api/reference/resources/admin#(resource)%20admin.organization.external_storage%20%3E%20(model)%20azure_external_storage_provider%20%3E%20(schema)) { account\_name, container, region, 4 more }  or [GcpExternalStorageProvider](/api/reference/resources/admin#(resource)%20admin.organization.external_storage%20%3E%20(model)%20gcp_external_storage_provider%20%3E%20(schema)) { audience, bucket, region, 4 more }

AwsExternalStorageProvider object { account\_id, bucket, external\_id, 3 more }

account\_id: string

bucket: string

external\_id: string

region: string

role\_arn: string

type: "aws"

AzureExternalStorageProvider object { account\_name, container, region, 4 more }

account\_name: string

container: string

region: string

resource\_group: string

subscription\_id: string

tenant\_id: string

type: "azure"

GcpExternalStorageProvider object { audience, bucket, region, 4 more }

audience: string

bucket: string

region: string

type: "gcp"

workload\_identity\_pool\_id: string

workload\_identity\_project\_number: string

workload\_identity\_provider\_id: string

status: "pending" or "validated" or "unhealthy"

"pending"

"validated"

"unhealthy"

ExternalStorageDeleted object { id, deleted, object }

deleted: boolean

object: "organization.external\_storage.deleted"

GcpExternalStorageProvider object { audience, bucket, region, 4 more }

audience: string

bucket: string

region: string

type: "gcp"

workload\_identity\_pool\_id: string

workload\_identity\_project\_number: string

workload\_identity\_provider\_id: string

<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/external_storage/methods/create/ -->

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[External Storage](/api/reference/resources/admin/subresources/organization/subresources/external_storage)

# Create an external storage configuration

POST/organization/external\_storage

Register one customer-managed external storage configuration.

##### Body ParametersJSONExpand Collapse

project\_id: string

provider: object { bucket, role\_arn, type }  or object { account\_name, container, resource\_group, 3 more }  or object { bucket, type, workload\_identity\_pool\_id, 2 more }

Aws object { bucket, role\_arn, type }

bucket: string

role\_arn: string

type: "aws"

Azure object { account\_name, container, resource\_group, 3 more }

account\_name: string

container: string

resource\_group: string

subscription\_id: string

tenant\_id: string

type: "azure"

Gcp object { bucket, type, workload\_identity\_pool\_id, 2 more }

bucket: string

type: "gcp"

workload\_identity\_pool\_id: string

workload\_identity\_project\_number: string

workload\_identity\_provider\_id: string

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

AWS S3Azure Blob Storage

### Create an external storage configuration

curl -X POST https://api.openai.com/v1/organization/external_storage \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "project_id": "proj_abc123",
    "provider": {
      "type": "aws",
      "bucket": "customer-logs",
      "role_arn": "arn:aws:iam::123456789012:role/OpenAIExternalStorageRole"
  }'

  "object": "organization.external_storage",
  "id": "extstorage_abc123",
  "project_id": "proj_abc123",
  "provider": {
    "type": "aws",
    "account_id": "123456789012",
    "region": "us-east-1",
    "bucket": "customer-logs",
    "role_arn": "arn:aws:iam::123456789012:role/OpenAIExternalStorageRole",
    "external_id": "proj_abc123"
  },
  "geography": "US",
  "status": "pending",
  "created_at": 1711471533

### Create an external storage configuration

curl -X POST https://api.openai.com/v1/organization/external_storage \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "project_id": "proj_azure123",
    "provider": {
      "type": "azure",
      "tenant_id": "11111111-1111-1111-1111-111111111111",
      "subscription_id": "22222222-2222-2222-2222-222222222222",
      "resource_group": "customer-rg",
      "account_name": "customerstorage",
      "container": "openai-data"
  }'

  "object": "organization.external_storage",
  "id": "extstorage_azure123",
  "project_id": "proj_azure123",
  "provider": {
    "type": "azure",
    "tenant_id": "11111111-1111-1111-1111-111111111111",
    "subscription_id": "22222222-2222-2222-2222-222222222222",
    "resource_group": "customer-rg",
    "account_name": "customerstorage",
    "container": "openai-data",
    "region": "eastus"
  },
  "geography": "US",
  "status": "pending",
  "created_at": 1711471533

  "created_at": 0,
  "geography": "geography",
  "object": "organization.external_storage",
  "project_id": "project_id",
  "provider": {
    "account_id": "account_id",
    "bucket": "bucket",
    "external_id": "external_id",
    "region": "region",
    "role_arn": "role_arn",
    "type": "aws"
  },
  "status": "pending"

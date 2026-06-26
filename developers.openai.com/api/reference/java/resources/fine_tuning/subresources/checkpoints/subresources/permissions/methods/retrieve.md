<!-- source: https://developers.openai.com/api/reference/java/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Fine Tuning](/api/reference/java/resources/fine_tuning)

[Checkpoints](/api/reference/java/resources/fine_tuning/subresources/checkpoints)

[Permissions](/api/reference/java/resources/fine_tuning/subresources/checkpoints/subresources/permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List checkpoint permissions

Deprecated: Retrieve is deprecated. Please swap to the paginated list method instead.

[PermissionRetrieveResponse](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20PermissionRetrieveResponse%20%3E%20(schema)) fineTuning().checkpoints().permissions().retrieve(PermissionRetrieveParamsparams = PermissionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to view all permissions for a fine-tuned model checkpoint.

##### ParametersExpand Collapse

PermissionRetrieveParams params

Optional<String> fineTunedModelCheckpoint

Optional<String> after

Identifier for the last permission ID from the previous pagination request.

Optional<Long> limit

Number of permissions to retrieve.

Optional<[Order](/api/reference/java/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/retrieve#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

The order in which to retrieve permissions.

ASCENDING("ascending")

DESCENDING("descending")

Optional<String> projectId

The ID of the project to get permissions for.

##### ReturnsExpand Collapse

class PermissionRetrieveResponse:

List<Data> data

String id

The permission identifier, which can be referenced in the API endpoints.

long createdAt

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

JsonValue; object\_ "checkpoint.permission"constant"checkpoint.permission"constant

The object type, which is always “checkpoint.permission”.

String projectId

The project identifier that the permission is for.

boolean hasMore

JsonValue; object\_ "list"constant"list"constant

Optional<String> firstId

Optional<String> lastId

### List checkpoint permissions

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.finetuning.checkpoints.permissions.PermissionRetrieveParams;
import com.openai.models.finetuning.checkpoints.permissions.PermissionRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        PermissionRetrieveResponse permission = client.fineTuning().checkpoints().permissions().retrieve("ft-AF1WoRqd3aJAHsqc9NY7iL8F");

  "object": "list",
  "data": [
      "object": "checkpoint.permission",
      "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
      "created_at": 1721764867,
      "project_id": "proj_abGMw1llN8IrBb6SvvY5A1iH"
      "object": "checkpoint.permission",
      "id": "cp_enQCFmOTGj3syEpYVhBRLTSy",
      "created_at": 1721764800,
      "project_id": "proj_iqGMw1llN8IrBb6SvvY5A1oF"
  ],
  "first_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "last_id": "cp_enQCFmOTGj3syEpYVhBRLTSy",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "object": "checkpoint.permission",
      "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
      "created_at": 1721764867,
      "project_id": "proj_abGMw1llN8IrBb6SvvY5A1iH"
      "object": "checkpoint.permission",
      "id": "cp_enQCFmOTGj3syEpYVhBRLTSy",
      "created_at": 1721764800,
      "project_id": "proj_iqGMw1llN8IrBb6SvvY5A1oF"
  ],
  "first_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "last_id": "cp_enQCFmOTGj3syEpYVhBRLTSy",
  "has_more": false

<!-- source: https://developers.openai.com/api/reference/java/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/create/ -->

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

# Create checkpoint permissions

PermissionCreatePage fineTuning().checkpoints().permissions().create(PermissionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

**NOTE:** Calling this endpoint requires an [admin API key](../admin-api-keys).

This enables organization owners to share fine-tuned models with other projects in their organization.

##### ParametersExpand Collapse

PermissionCreateParams params

Optional<String> fineTunedModelCheckpoint

List<String> projectIds

The project identifiers to grant access to.

##### ReturnsExpand Collapse

class PermissionCreateResponse:

The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

String id

The permission identifier, which can be referenced in the API endpoints.

long createdAt

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

JsonValue; object\_ "checkpoint.permission"constant"checkpoint.permission"constant

The object type, which is always “checkpoint.permission”.

String projectId

The project identifier that the permission is for.

### Create checkpoint permissions

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
import com.openai.models.finetuning.checkpoints.permissions.PermissionCreatePage;
import com.openai.models.finetuning.checkpoints.permissions.PermissionCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        PermissionCreateParams params = PermissionCreateParams.builder()
            .fineTunedModelCheckpoint("ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd")
            .addProjectId("string")
            .build();
        PermissionCreatePage page = client.fineTuning().checkpoints().permissions().create(params);

  "object": "list",
  "data": [
      "object": "checkpoint.permission",
      "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
      "created_at": 1721764867,
      "project_id": "proj_abGMw1llN8IrBb6SvvY5A1iH"
  ],
  "first_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "last_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "object": "checkpoint.permission",
      "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
      "created_at": 1721764867,
      "project_id": "proj_abGMw1llN8IrBb6SvvY5A1iH"
  ],
  "first_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "last_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "has_more": false

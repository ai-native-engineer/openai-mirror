<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/workload_identity_providers/ -->

# Workload Identity Providers

## Create Platform workload identity provider

`WorkloadIdentityProvider admin().organization().workloadIdentityProviders().create(WorkloadIdentityProviderCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/organization/workload_identity_providers`

Register an OIDC provider for keyless project service-account authentication.

### Parameters

- `WorkloadIdentityProviderCreateParams params`

  - `String audience`

    `minLength: 1`

  - `String issuer`

    `minLength: 1`

  - `String name`

    `minLength: 1`

  - `JsonValue; type "oidc"constant`

    - `OIDC("oidc")`

  - `Optional<List<AttributeTransformation>> attributeTransformations`

    `maxItems: 20`

    - `String attribute`

      `minLength: 1`, `maxLength: 256`

    - `String expression`

      `minLength: 1`, `maxLength: 4096`

  - `Optional<String> description`

  - `Optional<Boolean> enabled`

  - `Optional<Verification> verification`

    - `class Discovery:`

      - `Optional<String> discoveryUrl`

      - `JsonValue; type "discovery"constant`

        - `DISCOVERY("discovery")`

    - `class UploadedJwks:`

      - `Jwks jwks`

      - `JsonValue; type "uploaded_jwks"constant`

        - `UPLOADED_JWKS("uploaded_jwks")`

### Returns

- `class WorkloadIdentityProvider:`

  - `String id`

  - `List<AttributeTransformation> attributeTransformations`

    - `String attribute`

    - `String expression`

  - `String audience`

  - `long createdAt`

  - `Optional<String> description`

  - `boolean enabled`

  - `String issuer`

  - `String name`

  - `JsonValue; object_ "organization.workload_identity_provider"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_PROVIDER("organization.workload_identity_provider")`

  - `JsonValue; type "oidc"constant`

    - `OIDC("oidc")`

  - `long updatedAt`

  - `Verification verification`

    - `class Discovery:`

      - `Optional<String> discoveryUrl`

      - `JsonValue; type "discovery"constant`

        - `DISCOVERY("discovery")`

    - `class UploadedJwks:`

      - `Jwks jwks`

      - `JsonValue; type "uploaded_jwks"constant`

        - `UPLOADED_JWKS("uploaded_jwks")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.workloadidentityproviders.WorkloadIdentityProvider;
import com.openai.models.admin.organization.workloadidentityproviders.WorkloadIdentityProviderCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        WorkloadIdentityProviderCreateParams params = WorkloadIdentityProviderCreateParams.builder()
            .audience("x")
            .issuer("x")
            .name("x")
            .build();
        WorkloadIdentityProvider workloadIdentityProvider = client.admin().organization().workloadIdentityProviders().create(params);
    }
}
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_transformations": [
    {
      "attribute": "attribute",
      "expression": "expression"
    }
  ],
  "audience": "audience",
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "issuer": "issuer",
  "name": "name",
  "object": "organization.workload_identity_provider",
  "type": "oidc",
  "updated_at": 0,
  "verification": {
    "discovery_url": "discovery_url",
    "type": "discovery"
  }
}
```

## Delete Platform workload identity provider

`WorkloadIdentityProviderDeleted admin().organization().workloadIdentityProviders().delete(WorkloadIdentityProviderDeleteParamsparams = WorkloadIdentityProviderDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Delete a provider after deleting all its federation rules.

### Parameters

- `WorkloadIdentityProviderDeleteParams params`

  - `Optional<String> workloadIdentityProviderId`

    `minLength: 1`

### Returns

- `class WorkloadIdentityProviderDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "organization.workload_identity_provider.deleted"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_PROVIDER_DELETED("organization.workload_identity_provider.deleted")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.workloadidentityproviders.WorkloadIdentityProviderDeleteParams;
import com.openai.models.admin.organization.workloadidentityproviders.WorkloadIdentityProviderDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        WorkloadIdentityProviderDeleted workloadIdentityProviderDeleted = client.admin().organization().workloadIdentityProviders().delete("x");
    }
}
```

#### 200 — Example

```json
{
  "id": "id",
  "deleted": true,
  "object": "organization.workload_identity_provider.deleted"
}
```

## List Platform workload identity providers

`WorkloadIdentityProviderListPage admin().organization().workloadIdentityProviders().list(WorkloadIdentityProviderListParamsparams = WorkloadIdentityProviderListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/organization/workload_identity_providers`

List OIDC providers in the authenticated Admin API key's organization.

### Parameters

- `WorkloadIdentityProviderListParams params`

  - `Optional<String> after`

    `minLength: 1`

  - `Optional<Long> limit`

    `minimum: 1`, `maximum: 100`

  - `Optional<Order> order`

    - `ASC("asc")`

    - `DESC("desc")`

### Returns

- `class WorkloadIdentityProvider:`

  - `String id`

  - `List<AttributeTransformation> attributeTransformations`

    - `String attribute`

    - `String expression`

  - `String audience`

  - `long createdAt`

  - `Optional<String> description`

  - `boolean enabled`

  - `String issuer`

  - `String name`

  - `JsonValue; object_ "organization.workload_identity_provider"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_PROVIDER("organization.workload_identity_provider")`

  - `JsonValue; type "oidc"constant`

    - `OIDC("oidc")`

  - `long updatedAt`

  - `Verification verification`

    - `class Discovery:`

      - `Optional<String> discoveryUrl`

      - `JsonValue; type "discovery"constant`

        - `DISCOVERY("discovery")`

    - `class UploadedJwks:`

      - `Jwks jwks`

      - `JsonValue; type "uploaded_jwks"constant`

        - `UPLOADED_JWKS("uploaded_jwks")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.workloadidentityproviders.WorkloadIdentityProviderListPage;
import com.openai.models.admin.organization.workloadidentityproviders.WorkloadIdentityProviderListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        WorkloadIdentityProviderListPage page = client.admin().organization().workloadIdentityProviders().list();
    }
}
```

#### 200 — Example

```json
{
  "data": [
    {
      "id": "id",
      "attribute_transformations": [
        {
          "attribute": "attribute",
          "expression": "expression"
        }
      ],
      "audience": "audience",
      "created_at": 0,
      "description": "description",
      "enabled": true,
      "issuer": "issuer",
      "name": "name",
      "object": "organization.workload_identity_provider",
      "type": "oidc",
      "updated_at": 0,
      "verification": {
        "discovery_url": "discovery_url",
        "type": "discovery"
      }
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve Platform workload identity provider

`WorkloadIdentityProvider admin().organization().workloadIdentityProviders().retrieve(WorkloadIdentityProviderRetrieveParamsparams = WorkloadIdentityProviderRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Retrieve an OIDC provider in the authenticated organization.

### Parameters

- `WorkloadIdentityProviderRetrieveParams params`

  - `Optional<String> workloadIdentityProviderId`

    `minLength: 1`

### Returns

- `class WorkloadIdentityProvider:`

  - `String id`

  - `List<AttributeTransformation> attributeTransformations`

    - `String attribute`

    - `String expression`

  - `String audience`

  - `long createdAt`

  - `Optional<String> description`

  - `boolean enabled`

  - `String issuer`

  - `String name`

  - `JsonValue; object_ "organization.workload_identity_provider"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_PROVIDER("organization.workload_identity_provider")`

  - `JsonValue; type "oidc"constant`

    - `OIDC("oidc")`

  - `long updatedAt`

  - `Verification verification`

    - `class Discovery:`

      - `Optional<String> discoveryUrl`

      - `JsonValue; type "discovery"constant`

        - `DISCOVERY("discovery")`

    - `class UploadedJwks:`

      - `Jwks jwks`

      - `JsonValue; type "uploaded_jwks"constant`

        - `UPLOADED_JWKS("uploaded_jwks")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.workloadidentityproviders.WorkloadIdentityProvider;
import com.openai.models.admin.organization.workloadidentityproviders.WorkloadIdentityProviderRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        WorkloadIdentityProvider workloadIdentityProvider = client.admin().organization().workloadIdentityProviders().retrieve("x");
    }
}
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_transformations": [
    {
      "attribute": "attribute",
      "expression": "expression"
    }
  ],
  "audience": "audience",
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "issuer": "issuer",
  "name": "name",
  "object": "organization.workload_identity_provider",
  "type": "oidc",
  "updated_at": 0,
  "verification": {
    "discovery_url": "discovery_url",
    "type": "discovery"
  }
}
```

## Update Platform workload identity provider

`WorkloadIdentityProvider admin().organization().workloadIdentityProviders().update(WorkloadIdentityProviderUpdateParamsparams = WorkloadIdentityProviderUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Update supplied provider fields, preserving omitted fields.

### Parameters

- `WorkloadIdentityProviderUpdateParams params`

  - `Optional<String> workloadIdentityProviderId`

    `minLength: 1`

  - `Optional<List<AttributeTransformation>> attributeTransformations`

    `maxItems: 20`

    - `String attribute`

      `minLength: 1`, `maxLength: 256`

    - `String expression`

      `minLength: 1`, `maxLength: 4096`

  - `Optional<String> audience`

    `minLength: 1`

  - `Optional<String> description`

  - `Optional<Boolean> enabled`

  - `Optional<String> issuer`

    `minLength: 1`

  - `Optional<String> name`

    `minLength: 1`

  - `Optional<Verification> verification`

    - `class DiscoveryVerificationParam:`

      - `Optional<String> discoveryUrl`

      - `JsonValue; type "discovery"constant`

        - `DISCOVERY("discovery")`

    - `class UploadedJwksVerificationParam:`

      - `Jwks jwks`

      - `JsonValue; type "uploaded_jwks"constant`

        - `UPLOADED_JWKS("uploaded_jwks")`

### Returns

- `class WorkloadIdentityProvider:`

  - `String id`

  - `List<AttributeTransformation> attributeTransformations`

    - `String attribute`

    - `String expression`

  - `String audience`

  - `long createdAt`

  - `Optional<String> description`

  - `boolean enabled`

  - `String issuer`

  - `String name`

  - `JsonValue; object_ "organization.workload_identity_provider"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_PROVIDER("organization.workload_identity_provider")`

  - `JsonValue; type "oidc"constant`

    - `OIDC("oidc")`

  - `long updatedAt`

  - `Verification verification`

    - `class Discovery:`

      - `Optional<String> discoveryUrl`

      - `JsonValue; type "discovery"constant`

        - `DISCOVERY("discovery")`

    - `class UploadedJwks:`

      - `Jwks jwks`

      - `JsonValue; type "uploaded_jwks"constant`

        - `UPLOADED_JWKS("uploaded_jwks")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.workloadidentityproviders.WorkloadIdentityProvider;
import com.openai.models.admin.organization.workloadidentityproviders.WorkloadIdentityProviderUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        WorkloadIdentityProvider workloadIdentityProvider = client.admin().organization().workloadIdentityProviders().update("x");
    }
}
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_transformations": [
    {
      "attribute": "attribute",
      "expression": "expression"
    }
  ],
  "audience": "audience",
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "issuer": "issuer",
  "name": "name",
  "object": "organization.workload_identity_provider",
  "type": "oidc",
  "updated_at": 0,
  "verification": {
    "discovery_url": "discovery_url",
    "type": "discovery"
  }
}
```

## Domain Types

### Workload Identity Provider

- `class WorkloadIdentityProvider:`

  - `String id`

  - `List<AttributeTransformation> attributeTransformations`

    - `String attribute`

    - `String expression`

  - `String audience`

  - `long createdAt`

  - `Optional<String> description`

  - `boolean enabled`

  - `String issuer`

  - `String name`

  - `JsonValue; object_ "organization.workload_identity_provider"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_PROVIDER("organization.workload_identity_provider")`

  - `JsonValue; type "oidc"constant`

    - `OIDC("oidc")`

  - `long updatedAt`

  - `Verification verification`

    - `class Discovery:`

      - `Optional<String> discoveryUrl`

      - `JsonValue; type "discovery"constant`

        - `DISCOVERY("discovery")`

    - `class UploadedJwks:`

      - `Jwks jwks`

      - `JsonValue; type "uploaded_jwks"constant`

        - `UPLOADED_JWKS("uploaded_jwks")`

### Workload Identity Provider Deleted

- `class WorkloadIdentityProviderDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "organization.workload_identity_provider.deleted"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_PROVIDER_DELETED("organization.workload_identity_provider.deleted")`

# Federation Rules

## Create Platform workload identity federation rule

`FederationRule admin().organization().workloadIdentityProviders().federationRules().create(FederationRuleCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

Bind verified token attributes to an existing project service account.

### Parameters

- `FederationRuleCreateParams params`

  - `Optional<String> workloadIdentityProviderId`

    `minLength: 1`

  - `AttributeMatchers attributeMatchers`

    - `String`

    - `boolean`

    - `class UnionMember2: A class that can be one of several variants.union`

      - `long`

      - `double`

  - `String projectId`

    `minLength: 1`

  - `String serviceAccountId`

    `minLength: 1`

  - `Optional<String> description`

  - `Optional<Boolean> enabled`

  - `Optional<String> name`

  - `Optional<Permissions> permissions`

    - `JsonValue;`

      - `JsonValue; type "service_account_default"constant`

        - `SERVICE_ACCOUNT_DEFAULT("service_account_default")`

    - `class Restricted:`

      - `List<String> scopes`

        `minItems: 1`

      - `JsonValue; type "restricted"constant`

        - `RESTRICTED("restricted")`

### Returns

- `class FederationRule:`

  - `String id`

  - `AttributeMatchers attributeMatchers`

    - `String`

    - `boolean`

    - `class UnionMember2: A class that can be one of several variants.union`

      - `long`

      - `double`

  - `long createdAt`

  - `Optional<String> description`

  - `boolean enabled`

  - `Optional<String> name`

  - `JsonValue; object_ "organization.workload_identity_federation_rule"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_FEDERATION_RULE("organization.workload_identity_federation_rule")`

  - `Permissions permissions`

    - `JsonValue;`

      - `JsonValue; type "service_account_default"constant`

        - `SERVICE_ACCOUNT_DEFAULT("service_account_default")`

    - `class Restricted:`

      - `List<String> scopes`

      - `JsonValue; type "restricted"constant`

        - `RESTRICTED("restricted")`

  - `String projectId`

  - `String serviceAccountId`

  - `long updatedAt`

  - `String workloadIdentityProviderId`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.JsonValue;
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRule;
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRuleCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FederationRuleCreateParams params = FederationRuleCreateParams.builder()
            .workloadIdentityProviderId("x")
            .attributeMatchers(FederationRuleCreateParams.AttributeMatchers.builder()
                .putAdditionalProperty("foo", JsonValue.from("string"))
                .build())
            .projectId("x")
            .serviceAccountId("x")
            .build();
        FederationRule federationRule = client.admin().organization().workloadIdentityProviders().federationRules().create(params);
    }
}
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_matchers": {
    "foo": "string"
  },
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "name": "name",
  "object": "organization.workload_identity_federation_rule",
  "permissions": {
    "type": "service_account_default"
  },
  "project_id": "project_id",
  "service_account_id": "service_account_id",
  "updated_at": 0,
  "workload_identity_provider_id": "workload_identity_provider_id"
}
```

## Delete Platform workload identity federation rule

`FederationRuleDeleted admin().organization().workloadIdentityProviders().federationRules().delete(FederationRuleDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Delete a federation rule to a project service account.

### Parameters

- `FederationRuleDeleteParams params`

  - `String workloadIdentityProviderId`

    `minLength: 1`

  - `Optional<String> workloadIdentityFederationRuleId`

    `minLength: 1`

### Returns

- `class FederationRuleDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "organization.workload_identity_federation_rule.deleted"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_FEDERATION_RULE_DELETED("organization.workload_identity_federation_rule.deleted")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRuleDeleteParams;
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRuleDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FederationRuleDeleteParams params = FederationRuleDeleteParams.builder()
            .workloadIdentityProviderId("x")
            .workloadIdentityFederationRuleId("x")
            .build();
        FederationRuleDeleted federationRuleDeleted = client.admin().organization().workloadIdentityProviders().federationRules().delete(params);
    }
}
```

#### 200 — Example

```json
{
  "id": "id",
  "deleted": true,
  "object": "organization.workload_identity_federation_rule.deleted"
}
```

## List Platform workload identity federation rules

`FederationRuleListPage admin().organization().workloadIdentityProviders().federationRules().list(FederationRuleListParamsparams = FederationRuleListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

List the provider's federation rules to project service accounts.

### Parameters

- `FederationRuleListParams params`

  - `Optional<String> workloadIdentityProviderId`

    `minLength: 1`

  - `Optional<String> after`

    `minLength: 1`

  - `Optional<Long> limit`

    `minimum: 1`, `maximum: 100`

  - `Optional<Order> order`

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<String> serviceAccountId`

    `minLength: 1`

### Returns

- `class FederationRule:`

  - `String id`

  - `AttributeMatchers attributeMatchers`

    - `String`

    - `boolean`

    - `class UnionMember2: A class that can be one of several variants.union`

      - `long`

      - `double`

  - `long createdAt`

  - `Optional<String> description`

  - `boolean enabled`

  - `Optional<String> name`

  - `JsonValue; object_ "organization.workload_identity_federation_rule"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_FEDERATION_RULE("organization.workload_identity_federation_rule")`

  - `Permissions permissions`

    - `JsonValue;`

      - `JsonValue; type "service_account_default"constant`

        - `SERVICE_ACCOUNT_DEFAULT("service_account_default")`

    - `class Restricted:`

      - `List<String> scopes`

      - `JsonValue; type "restricted"constant`

        - `RESTRICTED("restricted")`

  - `String projectId`

  - `String serviceAccountId`

  - `long updatedAt`

  - `String workloadIdentityProviderId`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRuleListPage;
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRuleListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FederationRuleListPage page = client.admin().organization().workloadIdentityProviders().federationRules().list("x");
    }
}
```

#### 200 — Example

```json
{
  "data": [
    {
      "id": "id",
      "attribute_matchers": {
        "foo": "string"
      },
      "created_at": 0,
      "description": "description",
      "enabled": true,
      "name": "name",
      "object": "organization.workload_identity_federation_rule",
      "permissions": {
        "type": "service_account_default"
      },
      "project_id": "project_id",
      "service_account_id": "service_account_id",
      "updated_at": 0,
      "workload_identity_provider_id": "workload_identity_provider_id"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve Platform workload identity federation rule

`FederationRule admin().organization().workloadIdentityProviders().federationRules().retrieve(FederationRuleRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Retrieve a federation rule owned by the authenticated organization and provider.

### Parameters

- `FederationRuleRetrieveParams params`

  - `String workloadIdentityProviderId`

    `minLength: 1`

  - `Optional<String> workloadIdentityFederationRuleId`

    `minLength: 1`

### Returns

- `class FederationRule:`

  - `String id`

  - `AttributeMatchers attributeMatchers`

    - `String`

    - `boolean`

    - `class UnionMember2: A class that can be one of several variants.union`

      - `long`

      - `double`

  - `long createdAt`

  - `Optional<String> description`

  - `boolean enabled`

  - `Optional<String> name`

  - `JsonValue; object_ "organization.workload_identity_federation_rule"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_FEDERATION_RULE("organization.workload_identity_federation_rule")`

  - `Permissions permissions`

    - `JsonValue;`

      - `JsonValue; type "service_account_default"constant`

        - `SERVICE_ACCOUNT_DEFAULT("service_account_default")`

    - `class Restricted:`

      - `List<String> scopes`

      - `JsonValue; type "restricted"constant`

        - `RESTRICTED("restricted")`

  - `String projectId`

  - `String serviceAccountId`

  - `long updatedAt`

  - `String workloadIdentityProviderId`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRule;
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRuleRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FederationRuleRetrieveParams params = FederationRuleRetrieveParams.builder()
            .workloadIdentityProviderId("x")
            .workloadIdentityFederationRuleId("x")
            .build();
        FederationRule federationRule = client.admin().organization().workloadIdentityProviders().federationRules().retrieve(params);
    }
}
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_matchers": {
    "foo": "string"
  },
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "name": "name",
  "object": "organization.workload_identity_federation_rule",
  "permissions": {
    "type": "service_account_default"
  },
  "project_id": "project_id",
  "service_account_id": "service_account_id",
  "updated_at": 0,
  "workload_identity_provider_id": "workload_identity_provider_id"
}
```

## Update Platform workload identity federation rule

`FederationRule admin().organization().workloadIdentityProviders().federationRules().update(FederationRuleUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Update supplied matcher, permission, metadata, or enabled fields.

### Parameters

- `FederationRuleUpdateParams params`

  - `String workloadIdentityProviderId`

    `minLength: 1`

  - `Optional<String> workloadIdentityFederationRuleId`

    `minLength: 1`

  - `Optional<AttributeMatchers> attributeMatchers`

    - `String`

    - `boolean`

    - `class UnionMember2: A class that can be one of several variants.union`

      - `long`

      - `double`

  - `Optional<String> description`

  - `Optional<Boolean> enabled`

  - `Optional<String> name`

  - `Optional<Permissions> permissions`

    - `JsonValue;`

      - `JsonValue; type "service_account_default"constant`

        - `SERVICE_ACCOUNT_DEFAULT("service_account_default")`

    - `class RestrictedPermissionsParam:`

      - `List<String> scopes`

        `minItems: 1`

      - `JsonValue; type "restricted"constant`

        - `RESTRICTED("restricted")`

### Returns

- `class FederationRule:`

  - `String id`

  - `AttributeMatchers attributeMatchers`

    - `String`

    - `boolean`

    - `class UnionMember2: A class that can be one of several variants.union`

      - `long`

      - `double`

  - `long createdAt`

  - `Optional<String> description`

  - `boolean enabled`

  - `Optional<String> name`

  - `JsonValue; object_ "organization.workload_identity_federation_rule"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_FEDERATION_RULE("organization.workload_identity_federation_rule")`

  - `Permissions permissions`

    - `JsonValue;`

      - `JsonValue; type "service_account_default"constant`

        - `SERVICE_ACCOUNT_DEFAULT("service_account_default")`

    - `class Restricted:`

      - `List<String> scopes`

      - `JsonValue; type "restricted"constant`

        - `RESTRICTED("restricted")`

  - `String projectId`

  - `String serviceAccountId`

  - `long updatedAt`

  - `String workloadIdentityProviderId`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRule;
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRuleUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FederationRuleUpdateParams params = FederationRuleUpdateParams.builder()
            .workloadIdentityProviderId("x")
            .workloadIdentityFederationRuleId("x")
            .build();
        FederationRule federationRule = client.admin().organization().workloadIdentityProviders().federationRules().update(params);
    }
}
```

#### 200 — Example

```json
{
  "id": "id",
  "attribute_matchers": {
    "foo": "string"
  },
  "created_at": 0,
  "description": "description",
  "enabled": true,
  "name": "name",
  "object": "organization.workload_identity_federation_rule",
  "permissions": {
    "type": "service_account_default"
  },
  "project_id": "project_id",
  "service_account_id": "service_account_id",
  "updated_at": 0,
  "workload_identity_provider_id": "workload_identity_provider_id"
}
```

## Domain Types

### Federation Rule

- `class FederationRule:`

  - `String id`

  - `AttributeMatchers attributeMatchers`

    - `String`

    - `boolean`

    - `class UnionMember2: A class that can be one of several variants.union`

      - `long`

      - `double`

  - `long createdAt`

  - `Optional<String> description`

  - `boolean enabled`

  - `Optional<String> name`

  - `JsonValue; object_ "organization.workload_identity_federation_rule"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_FEDERATION_RULE("organization.workload_identity_federation_rule")`

  - `Permissions permissions`

    - `JsonValue;`

      - `JsonValue; type "service_account_default"constant`

        - `SERVICE_ACCOUNT_DEFAULT("service_account_default")`

    - `class Restricted:`

      - `List<String> scopes`

      - `JsonValue; type "restricted"constant`

        - `RESTRICTED("restricted")`

  - `String projectId`

  - `String serviceAccountId`

  - `long updatedAt`

  - `String workloadIdentityProviderId`

### Federation Rule Deleted

- `class FederationRuleDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "organization.workload_identity_federation_rule.deleted"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_FEDERATION_RULE_DELETED("organization.workload_identity_federation_rule.deleted")`

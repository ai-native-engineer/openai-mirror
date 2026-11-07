<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/create/ -->

## Create Platform workload identity federation rule

`client.Admin.Organization.WorkloadIdentityProviders.FederationRules.New(ctx, workloadIdentityProviderID, body) (*FederationRule, error)`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

Bind verified token attributes to an existing project service account.

- `workloadIdentityProviderID string`

  `minLength: 1`

- `body AdminOrganizationWorkloadIdentityProviderFederationRuleNewParams`

  - `AttributeMatchers param.Field[map[string, AdminOrganizationWorkloadIdentityProviderFederationRuleNewParamsAttributeMatcherUnion]]`

    - `string`

    - `bool`

    - `type UnionMember2 interface{…}`

      - `int64`

      - `float64`

  - `ProjectID param.Field[string]`

    `minLength: 1`

  - `ServiceAccountID param.Field[string]`

    `minLength: 1`

  - `Description param.Field[string]`

  - `Enabled param.Field[bool]`

  - `Name param.Field[string]`

  - `Permissions param.Field[AdminOrganizationWorkloadIdentityProviderFederationRuleNewParamsPermissionsUnion]`

    - `type AdminOrganizationWorkloadIdentityProviderFederationRuleNewParamsPermissionsServiceAccountDefault struct{…}`

      - `Type ServiceAccountDefault`

        - `const ServiceAccountDefaultServiceAccountDefault ServiceAccountDefault = "service_account_default"`

    - `type AdminOrganizationWorkloadIdentityProviderFederationRuleNewParamsPermissionsRestricted struct{…}`

      - `Scopes []string`

        `minItems: 1`

      - `Type Restricted`

        - `const RestrictedRestricted Restricted = "restricted"`

- `type FederationRule struct{…}`

  - `ID string`

  - `AttributeMatchers map[string, FederationRuleAttributeMatcherUnion]`

    - `string`

    - `bool`

    - `type UnionMember2 interface{…}`

      - `int64`

      - `float64`

  - `CreatedAt int64`

  - `Description string`

  - `Enabled bool`

  - `Name string`

  - `Object OrganizationWorkloadIdentityFederationRule`

    - `const OrganizationWorkloadIdentityFederationRuleOrganizationWorkloadIdentityFederationRule OrganizationWorkloadIdentityFederationRule = "organization.workload_identity_federation_rule"`

  - `Permissions FederationRulePermissionsUnion`

    - `type FederationRulePermissionsServiceAccountDefault struct{…}`

      - `Type ServiceAccountDefault`

        - `const ServiceAccountDefaultServiceAccountDefault ServiceAccountDefault = "service_account_default"`

    - `type FederationRulePermissionsRestricted struct{…}`

      - `Scopes []string`

      - `Type Restricted`

        - `const RestrictedRestricted Restricted = "restricted"`

  - `ProjectID string`

  - `ServiceAccountID string`

  - `UpdatedAt int64`

  - `WorkloadIdentityProviderID string`

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  federationRule, err := client.Admin.Organization.WorkloadIdentityProviders.FederationRules.New(
    context.TODO(),
    "x",
    openai.AdminOrganizationWorkloadIdentityProviderFederationRuleNewParams{
      AttributeMatchers: map[string]openai.AdminOrganizationWorkloadIdentityProviderFederationRuleNewParamsAttributeMatcherUnion{
      "foo": {
        OfString: openai.String("string"),
      ProjectID: "x",
      ServiceAccountID: "x",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", federationRule.ID)

  "attribute_matchers": {
    "foo": "string"
  "enabled": true,
  "object": "organization.workload_identity_federation_rule",
  "permissions": {
    "type": "service_account_default"
  "project_id": "project_id",
  "service_account_id": "service_account_id",
  "updated_at": 0,
  "workload_identity_provider_id": "workload_identity_provider_id"

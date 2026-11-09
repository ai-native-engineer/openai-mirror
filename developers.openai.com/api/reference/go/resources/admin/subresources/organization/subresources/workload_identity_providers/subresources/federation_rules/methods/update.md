<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/update/ -->

## Update Platform workload identity federation rule

`client.Admin.Organization.WorkloadIdentityProviders.FederationRules.Update(ctx, workloadIdentityProviderID, workloadIdentityFederationRuleID, body) (*FederationRule, error)`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Update supplied matcher, permission, metadata, or enabled fields.

- `workloadIdentityProviderID string`

  `minLength: 1`

- `workloadIdentityFederationRuleID string`

  `minLength: 1`

- `body AdminOrganizationWorkloadIdentityProviderFederationRuleUpdateParams`

  - `AttributeMatchers param.Field[map[string, AdminOrganizationWorkloadIdentityProviderFederationRuleUpdateParamsAttributeMatcherUnion]]`

    - `string`

    - `bool`

    - `type UnionMember2 interface{…}`

      - `int64`

      - `float64`

  - `Description param.Field[string]`

  - `Enabled param.Field[bool]`

  - `Name param.Field[string]`

  - `Permissions param.Field[AdminOrganizationWorkloadIdentityProviderFederationRuleUpdateParamsPermissionsUnion]`

    - `type AdminOrganizationWorkloadIdentityProviderFederationRuleUpdateParamsPermissionsDefaultPermissionsParam struct{…}`

      - `Type ServiceAccountDefault`

        - `const ServiceAccountDefaultServiceAccountDefault ServiceAccountDefault = "service_account_default"`

    - `type AdminOrganizationWorkloadIdentityProviderFederationRuleUpdateParamsPermissionsRestrictedPermissionsParam struct{…}`

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
  federationRule, err := client.Admin.Organization.WorkloadIdentityProviders.FederationRules.Update(
    context.TODO(),
    "x",
    "x",
    openai.AdminOrganizationWorkloadIdentityProviderFederationRuleUpdateParams{

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

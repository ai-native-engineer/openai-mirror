<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/list/ -->

## List Platform workload identity federation rules

`client.Admin.Organization.WorkloadIdentityProviders.FederationRules.List(ctx, workloadIdentityProviderID, query) (*CursorPage[FederationRule], error)`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

List the provider's federation rules to project service accounts.

- `workloadIdentityProviderID string`

  `minLength: 1`

- `query AdminOrganizationWorkloadIdentityProviderFederationRuleListParams`

  - `After param.Field[string]`

    `minLength: 1`

  - `Limit param.Field[int64]`

    `minimum: 1`, `maximum: 100`

  - `Order param.Field[AdminOrganizationWorkloadIdentityProviderFederationRuleListParamsOrderString]`

    - `type AdminOrganizationWorkloadIdentityProviderFederationRuleListParamsOrderString string`

      - `const AdminOrganizationWorkloadIdentityProviderFederationRuleListParamsOrderStringAsc AdminOrganizationWorkloadIdentityProviderFederationRuleListParamsOrderString = "asc"`

      - `const AdminOrganizationWorkloadIdentityProviderFederationRuleListParamsOrderStringDesc AdminOrganizationWorkloadIdentityProviderFederationRuleListParamsOrderString = "desc"`

  - `ServiceAccountID param.Field[string]`

    `minLength: 1`

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
  page, err := client.Admin.Organization.WorkloadIdentityProviders.FederationRules.List(
    context.TODO(),
    "x",
    openai.AdminOrganizationWorkloadIdentityProviderFederationRuleListParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "data": [
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
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

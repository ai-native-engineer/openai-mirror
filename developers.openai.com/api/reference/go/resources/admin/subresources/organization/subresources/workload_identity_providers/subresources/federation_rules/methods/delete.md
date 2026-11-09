<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/delete/ -->

## Delete Platform workload identity federation rule

`client.Admin.Organization.WorkloadIdentityProviders.FederationRules.Delete(ctx, workloadIdentityProviderID, workloadIdentityFederationRuleID) (*FederationRuleDeleted, error)`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Delete a federation rule to a project service account.

- `workloadIdentityProviderID string`

  `minLength: 1`

- `workloadIdentityFederationRuleID string`

  `minLength: 1`

- `type FederationRuleDeleted struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object OrganizationWorkloadIdentityFederationRuleDeleted`

    - `const OrganizationWorkloadIdentityFederationRuleDeletedOrganizationWorkloadIdentityFederationRuleDeleted OrganizationWorkloadIdentityFederationRuleDeleted = "organization.workload_identity_federation_rule.deleted"`

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
  federationRuleDeleted, err := client.Admin.Organization.WorkloadIdentityProviders.FederationRules.Delete(
    context.TODO(),
    "x",
    "x",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", federationRuleDeleted.ID)

  "deleted": true,
  "object": "organization.workload_identity_federation_rule.deleted"

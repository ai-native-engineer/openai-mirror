<!-- source: https://help.openai.com/en/articles/20001193-gpt-rosalind-for-life-sciences-research -->

# GPT-Rosalind for life sciences research

Learn about GPT-Rosalind, request access for your organization or academic lab, and get help with setup.

Updated: 5 days ago

GPT-Rosalind is a family of models for life sciences research. These models help research teams synthesize evidence, reason across biological data, and coordinate workflows across scientific tools, literature, databases, internal systems, and specialist models.

GPT-Rosalind combines specialized biological reasoning with scientific tool use to support target research, genomics and sequencing analysis, protein and sequence analysis, medicinal chemistry, literature synthesis, wet-lab troubleshooting, and experiment planning. In Codex, the Life Sciences Research plugin connects these workflows to scientific tools, databases, and data sources.

To request access, use the route for your organization or lab below. Buying a subscription or joining a workspace does not automatically give you GPT-Rosalind access.

## Availability

Eligible organizations with Enterprise or Business agreements can request GPT-Rosalind through OpenAI's trusted-access program. Access is limited to approved users and is subject to applicable safety and compliance requirements. Your organization's approval determines which workspaces and products you can use.

Academic labs at U.S. universities can apply through the Rosalind Academic Plan. This Business-based offer has its own eligibility and verification requirements. It is separate from the ChatGPT Edu subscription and the ChatGPT for Academic Researchers program. For eligibility, the offer, and application instructions, see: [Rosalind Academic Plan](https://help.openai.com/articles/20001602).

Approved institutional customers can use GPT-Rosalind in ChatGPT and Codex, and through the OpenAI API where separately approved. The Rosalind Academic Plan does not include API access or API credits. GPT-Rosalind is not currently available through Amazon Bedrock (AWS).

## Rosalind Research and Rosalind Discovery

Research and Discovery are two access tiers for GPT-Rosalind. Each tier has its own model access and biological safeguards. OpenAI reviews your organization's application to determine the access it qualifies for. Discovery approval does not grant Research access; moving to Research requires additional review and approval.

### Rosalind Research

Research supports frontier biological work. The Research tier includes GPT-6 Rosalind Research and GPT-5.5 Rosalind Research.

### Rosalind Discovery

Discovery supports everyday scientific work, including reviewing literature, analyzing biological data, writing scientific code, interpreting protocols, and planning experiments. It uses the existing Rosalind 5.5 model with Discovery-specific safeguards and stricter monitoring than Research. Discovery approval does not include GPT-5.5 Rosalind Research or GPT-6 Rosalind Research.

### GPT-6 Rosalind Research

GPT-6 Rosalind Research is available to a limited set of approved Research organizations in Work and Codex, and through the API where separately approved. It is not available in the Chat tab. Access requires the appropriate Research approval for your organization and user; approval for GPT-Rosalind Discovery does not grant Research access.

Customers can continue to select GPT-5.5 Rosalind Research for existing workflows. Your approval and activation instructions determine which models and products you can use.

In Enterprise workspaces, GPT-6 Rosalind Research starts in a two-week Admin Preview and is off by default during that period. Admins can enable it for approved Research users and configure access for after the preview. Existing Research approval does not bypass Admin Preview.

# Request and track access

## Choose the application route

* For an organization applying under an Enterprise or Business agreement, open the [GPT-Rosalind access request](https://openai.com/form/life-sciences-access). You can also [contact sales](https://openai.com/solutions/industries/life-sciences/) for information about institutional access.
* For a lab at a U.S. university without an OpenAI Enterprise agreement, ask your principal investigator (PI) or designated lab lead to follow the [Rosalind Academic Plan application instructions](https://help.openai.com/articles/20001602).
* If your university has an OpenAI Enterprise agreement, contact your university administrator or OpenAI account team to request access through that agreement. If you're unsure which agreement or workspace applies, check with them before submitting an application.

Check whether your organization or lab already has an application in progress. A university email address does not extend an approval to every department, lab, or workspace.

## Complete an institutional application

An authorized, verified organization member can apply. The applicant does not need to be a workspace owner or admin, but must have authority to represent the organization. A verified owner or admin completes the separate final approval.

1. Sign in with the account associated with your organization and open the access request.
2. Select the organization and complete the required organizational verification.
3. Provide the requested research and intended-use information, and review the available data-handling options and submission statements.
4. Submit the application and follow the next action shown.

For an institutional request, open [Track your application](https://chatgpt.com/r/b749fb02595e04c3007a54375f3f4374/status) with the account associated with the request. If you're applying through the Academic Plan, use the status instructions in your academic application.

After the required reviews, a verified organization owner or admin must accept the applicable terms, acknowledge pricing, and authorize activation for the correct organization. Follow the approval instructions and confirm that activation is complete before asking users to start. Passing verification or accepting terms does not, by itself, mean the model is ready to use.

# Set up access in ChatGPT

## Add users to the ChatGPT workspace

Before enabling GPT-Rosalind, confirm that access activation is complete and that you are using the approved workspace. The following invitation and custom-role instructions apply to institutional workspaces with those controls. For Academic Plan membership and PI permissions, follow the [lab access instructions](https://help.openai.com/articles/20001602).

1. Switch to the GPT-Rosalind-enabled workspace and open **Workspace settings**.
2. Select **Members**.
3. Select **Invite member**.
4. Enter the approved users' email addresses or upload a CSV.
5. Choose the appropriate role and seat type, then send the invitations.

After users join, a workspace owner must check their model permissions. Workspace membership alone does not grant GPT-Rosalind access.

## Enable GPT-Rosalind in ChatGPT

For eligible Enterprise and Edu workspaces that use custom roles, a workspace Owner can create and assign a role for approved users. Workspace Admins can update existing roles where supported; they cannot create or assign custom roles.

1. Switch to the approved workspace and open **Workspace** **settings**.
2. Select **Groups** and create or select a group for GPT-Rosalind access.
3. Add the approved users to the group.
4. Open **Permissions & roles**, then **Custom** **roles**.
5. Create a custom role and assign it to the group.
6. Turn on **Life Sciences** and the required **Skills** and **Codex** permissions for the approved setup. In Enterprise workspaces, keep the Rosalind model control Off for the default member role and turn it On for the custom role assigned to approved users. Users without another role granting access inherit the Off default.

Review all direct and group role assignments. A permission set to **Off** in one role can still be granted by another role. Plan and seat eligibility also apply. Allow up to 5 minutes for role changes to take effect, then ask an approved user to check access.

For the full role-management procedure, see: [Managing feature access with role-based access control in ChatGPT](https://help.openai.com/articles/11750701).

For a Business workspace, follow the access-management instructions supplied with your approval. Academic Plan workspaces use the PI or lab lead's access controls; do not use the Enterprise and Edu custom-role procedure above. If the expected controls are missing, contact OpenAI Support.

## Use GPT-Rosalind in ChatGPT

After access is enabled, make sure you are working in the GPT-Rosalind-enabled workspace.

GPT-6 Rosalind Research is not available in the Chat tab. If you have the required Research access, use Work or Codex.

1. Open the workspace switcher and select the approved workspace.
2. Open **Skills** and confirm that the provisioned skills are available.
3. Turn on the skills you plan to use.
4. Start a new chat.
5. Open the model picker and select **GPT-Rosalind**.

Select GPT-Rosalind when starting the work you want to use it for. If it isn't listed, follow the access checks in the FAQ below.

# Use GPT-Rosalind in Codex

1. Sign in to Codex with the approved workspace.
2. Open **Plugins**.
3. Install the **Life Sciences Research** **Plugin**.
4. Start a new thread.
5. Open the model picker and select **GPT-6 Rosalind Research**, or the GPT-Rosalind model included in your existing approval.

Installing the plugin does not grant model access. Your account also needs GPT-Rosalind access and the required Codex and plugin permissions.

# Use GPT-6 Rosalind Research in Work

Open Work in your approved workspace and select **GPT-6 Rosalind Research** in the model picker. Your organization and user must have the required Research access.

If the model is missing, ask your workspace owner or administrator to confirm your Research approval, activation, and model permissions. Follow the access checks in the FAQ below if you still need help.

# Add users for API access

These instructions apply only to organizations separately approved for GPT-Rosalind API access. The Academic Plan does not include API access or API credits, and approval for a ChatGPT workspace does not approve a different API organization.

Eligible organizations can use GPT-Rosalind through the OpenAI API for approved internal research tools, workflows, and applications. API access is not available for customer-facing products or external commercial applications at this time.

For GPT-6 Rosalind Research API access, use the model identifier gpt-6-rosalind in your approved API organization. Approval for a different GPT-Rosalind model does not, by itself, grant access to this model.

For manually managed API memberships, ask someone with permission to manage members to:

1. Go to [API](https://platform.openai.com) [Platform](https://platform.openai.com).
2. Open **Settings**.
3. Select **People**.
4. Add the approved member and check their project access.

If your organization manages membership through synchronized groups, follow its Admin console process instead. For more information about API organization setup, see: [Setting up your organization](https://developers.openai.com/api/docs/guides/production-best-practices#setting-up-your-organization).

# Work with large research datasets in Codex

GPT-Rosalind does not need raw, large-scale datasets added directly into context to support in-depth analysis.

For omics data or other large datasets, point GPT-Rosalind to the files in a local directory, database, or approved storage system. You can then ask a specific research question, and GPT-Rosalind can help choose the right analysis, run targeted steps over the data, interpret the outputs, and turn useful workflows into repeatable skills.

This approach keeps raw files in storage and lets GPT-Rosalind perform focused, tool-driven analysis at query time. It is usually faster and more effective than trying to process the full dataset directly in context.

# Data and security

Your approved product, agreement, and active workspace configuration determine the data protections that apply. Confirm your institution's requirements with your administrator or OpenAI account team before adding research data.

Research and Discovery approvals cover internal work by authorized personnel. Do not share credentials or make approved model access available to outside users through a customer-facing product, API, agent, or service.

For institutional deployments, GPT-Rosalind is delivered through ChatGPT Enterprise, Codex, and the API with enterprise security and governance controls. The platform supports enterprise deployments with Regulated Workspaces and BAAs, along with SOC 2 Type 2 and HIPAA-aligned standards. OpenAI does not train on enterprise customer data by default.

Those enterprise arrangements do not automatically apply to the Business-based Academic Plan. GPT-Rosalind approval does not, by itself, activate Enhanced Privacy or Zero Data Retention. For the academic offer's data-handling information, see: [Rosalind Academic Plan](https://help.openai.com/articles/20001602).

Eligible Enterprise and Edu workspaces use role-based access controls to manage feature access. For details, see: [Managing feature access with role-based access control in ChatGPT](https://help.openai.com/articles/11750701).

# FAQ

## What is GPT-Rosalind?

GPT-Rosalind is a family of models built for life sciences research. GPT-Rosalind models are designed for deep scientific reasoning, stronger tool and database use, and safe access to multi-step workflows across areas such as protein understanding, genomics analysis, and biochemistry reasoning.

## What is Rosalind Workbench?

Rosalind Workbench is a dedicated scientific research workspace available in Codex and ChatGPT. It brings together specialized tools, data viewers, and guided workflows for working with biological structures, sequences, genomics, and other research data.

At launch, Rosalind Workbench includes customizable workflows for next-generation sequencing, including FASTQ quality control, bulk RNA sequencing, and single-cell RNA sequencing.

You do not need access to the GPT-Rosalind model to use Rosalind Workbench. Workbench availability does not confirm that your account has GPT-Rosalind model access.

## Who is GPT-Rosalind best for?

The model is best suited for bioinformaticians, computational biologists, and early discovery biologists.

## What can GPT-Rosalind do?

GPT-Rosalind can help scientists reason across biological data, use tools and synthesize evidence from multiple sources, generate and refine hypotheses, and support multi-step workflows such as target discovery, target validation, and experiment planning.

## What stage of research is it best for?

The model is currently most valuable for early discovery and hypothesis generation, especially for target biology, mechanism understanding, literature synthesis, and omics interpretation.

## How is GPT-Rosalind different from general-purpose models in ChatGPT and Codex?

GPT-Rosalind is built for scientific research workflows rather than general productivity use cases. It offers deeper biological reasoning, literature synthesis workflows, longer reasoning for complex tasks, and access to scientific tools and databases for research tasks.

## Can customers use their own internal knowledge and data?

Some workflows can use internal knowledge and data through Codex and custom workflows, but this is not fully available out of the box. What is possible depends on how the data is structured and may require custom setup, skills, or automation. Check your organization's data-handling requirements before connecting a source or adding data.

## How can organizations get access to GPT-Rosalind?

Use the application route described in Request and track access above. For institutional applications, a verified owner or admin must complete final acceptance before activation. For academic labs, the PI or designated lab lead follows the Academic Plan process. Check an existing application before submitting another request.

## Can eligible customers access GPT-Rosalind in the API?

Yes, if their organization is separately approved for GPT-Rosalind API access for internal research tools, workflows, and applications. Customer-facing products and external commercial applications are outside that access scope. The Rosalind Academic Plan does not include API access or API credits.

## How much does GPT-Rosalind cost?

For institutional pricing, review the [API pricing page](https://developers.openai.com/api/docs/pricing), the [credit-based](https://help.openai.com/articles/11481834) [ChatGPT Rate Card](https://help.openai.com/articles/11481834), the [Enterprise token-based ChatGPT Rate Card](https://help.openai.com/articles/20001415), and your organization's agreement. Check the rate for the model you select: GPT-6 Rosalind Research has different Standard rates from the existing Rosalind 5.5 models. GPT-Rosalind Discovery uses the existing Rosalind 5.5 rates.

For complimentary seats, eligibility, and offer terms for academic labs, see: [Rosalind Academic Plan](https://help.openai.com/articles/20001602). Purchasing a regular Business subscription does not enroll your lab in that offer or grant GPT-Rosalind access.

## What data protections are in place?

Use the data protections in your approved product and agreement. Enterprise security and privacy arrangements are not automatically included in the Academic Plan. Review Data and security above and confirm any specific retention or regulated-data requirements with your administrator or OpenAI account team before using the model with that data.

## How can I get help with setup or access?

For workspace setup, model access, billing, or technical issues, [contact OpenAI Support](https://help.openai.com/articles/6614161). Include the affected product, application status, workspace or organization ID, exact error, approximate time and time zone, and checks you have already tried. For an API issue, include the request ID if available.

Do not send passwords, API keys, one-time codes, identity documents, or sensitive research data in an ordinary support message. Submit identity documents only through the designated verification process.

## I was approved or added, but I still cannot see GPT-Rosalind. What should I check?

1. Sign in with the account associated with your application and switch to the approved workspace or API organization.
2. Check the application instructions for any outstanding acceptance or setup step. Approval and completed activation are separate.
3. Ask the workspace owner to check your membership, seat eligibility, and model permissions. In an Academic Plan workspace, ask your PI or lab lead.
4. In an Enterprise or Edu workspace that uses custom roles, review all direct and group assignments. One role can still grant access even when another is set to **Off**.
5. Confirm approval for the product and model you are using. Codex permissions and plugin installation are separate from model access; API access requires an approved API organization. GPT-6 Rosalind Research requires Research approval and is available in Work, Codex, and the API where approved, not in the Chat tab.

For an institutional request, check [Track your application](https://chatgpt.com/r/b749fb02595e04c3007a54375f3f4374/status). For an Academic Plan request, follow your academic application status instructions. If you still cannot use the model, contact OpenAI Support with the details listed above.

## What should I do if verification is incomplete or shows an error?

Follow the instructions in the verification flow associated with your application. If a link has expired, the flow repeats, or completed verification has not advanced the application, contact OpenAI Support with the exact message and approximate time of the attempt. Check the existing application before submitting another one. Completing verification is one part of review and does not confirm model activation.

## How do I ask about an application decision?

Follow the instructions in your decision notice. If the next step is unclear, contact OpenAI Support with your application email, institution or organization, and current status. A new submission does not guarantee approval.

<!-- source: https://help.openai.com/en/articles/20001338-managing-chatgpt-sites-for-your-workspace -->

# Managing ChatGPT Sites for your workspace

Manage Site access, publishing, and workspace controls for ChatGPT Sites.

# Overview

ChatGPT Sites lets workspace members create and share hosted Sites from ChatGPT. Workspace owners and admins can help determine who can create Sites, who can publish them, how Sites are shared, and how Sites should be reviewed or removed when needed.  
  
This article is for ChatGPT Business, Enterprise, and Edu owners and admins. Available controls depend on your plan and workspace configuration.

# Owner / admin responsibilities

Before enabling Sites broadly, decide who should be able to create Sites, whether public publishing should be allowed, what content can be published, and how your organization will handle support, review, takedown, and compliance questions.

Sites is currently in beta, and is not eligible for data or inference residency.

# Enable or limit Sites

Business workspaces have Sites enabled by default. Enterprise owners and admins can use role-based access controls (RBAC) to decide who can create Sites and who can publish them.  
  
In Enterprise workspaces, public publishing is off by default. To enable it, turn on public publishing in Workspace settings, then grant the appropriate users or groups permission to create and publish Sites through RBAC.  
  
If a workspace member cannot use Sites, check whether Sites is enabled for the workspace, whether the member is in an eligible role or group, and whether the member is signed in to the correct workspace.

# Manage publishing and access

A Site can be limited to its owner and workspace admins, shared with active members of the workspace, or shared with selected active users or groups where supported. Public access is available only when public publishing is enabled and the member has permission to publish.  
  
Public sharing makes a Site available outside the workspace according to the audience selected in the publishing flow.  
  
Available controls vary by plan and workspace configuration. Custom domains are not available in Enterprise workspaces at launch. If you cannot find or use a control, contact OpenAI Support.

# Data, compliance, and residency considerations

Sites can involve prompts, instructions, files, site code, generated artifacts, hosted URLs, storage, and logs needed to operate and secure the Site.  
  
ChatGPT Sites does not support data residency or inference residency at launch. This includes deployed Sites, Site code, D1/R2 data and file storage, artifacts, and logs. Learn more in [Data residency and inference residency](/en/articles/9903489-data-residency-and-inference-residency).

## Recommended workspace policy

* Give members clear guidelines for creating Sites that comply with your organization’s security, confidentiality, privacy, and other requirements.

* Define a policy for when public publishing is allowed.

* Require review before publishing sites that include confidential, sensitive, or third-party content.

* Decide who can approve public Sites and who can remove them.

* Document where members should report suspicious, malicious, infringing, or unsafe Sites.

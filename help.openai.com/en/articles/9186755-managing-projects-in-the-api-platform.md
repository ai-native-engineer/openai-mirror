<!-- source: https://help.openai.com/en/articles/9186755-managing-projects-in-the-api-platform -->

# Managing projects in the API platform

Updated: 9 days ago

Projects aim to provide customers the ability to organize their work. Organizations can manage access and limits, provision service accounts (through the UI), and track usage against a constrained scope within a project (e.g. models, capabilities, threads, assistants, fine tuning, storage, etc.). Usage activity can be broken down by project, and users can view billing and set budgets per project.  
  
Organization owners can view all of their Active and Archived projects in the [Projects page](https://platform.openai.com/projects). Learn more about [user roles and permissions in the API Platform](#h_962ddad85d).

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-931ba19021ce580a223efcf8/786d3e9841c598b878729a109f99d87b/Frame_1.png)

## **Who can create a project?**

Only organization owners can create a project. Please refer to [**roles and permissions**](#h_962ddad85d) for more information.  
  
To switch between organizations, hover over your organization’s name on the top-left of the page and select the organization from the list:

![Projects page with the organization switcher open, listing Personal and Staging organizations](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-73974019ae2533300003ca90/462e4846200393d8596da4cf21e99ea0/Frame_2.png)

For those organizations that are on a consolidated billing plan, sub-orgs are identified separately. Projects cannot be created within sub-orgs.

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-f2d68d0fb6fa3adaa8c275e8/ebca66c5f44ae9a94195cea0bc82d05c/Frame_3.png)

## **How do projects work?**

Every organization includes a “Default project” that **cannot be deleted**. You can configure the rate limits, virtual model permissions, and spend budgets (as of November 2024). It inherits the full configuration of the organization, so you cannot directly add members or service accounts to it.

## **How do I create a project?**

First, hover on the project name on the left-corner of the page and select **Create project**.

![API platform project menu with Create project highlighted under Default project](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-d00ecfd0034110429a88f7e2/f6b334d3996f5cedba03b41bda11983c/Frame_4.png)

Provide a name, description, and website for your project and then select `Create`.

![Create a new project dialog in the API platform with fields for project name, use case, and business website](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-bc08f5cedb92f5eb54a6c877/0b2fcc854bdae87e8a2a2711051a85b4/Frame_5.png)

## **How do I add users to a project?**

Newly added organization members are not automatically added to the “Default project”. New members can be invited to the project either when they are invited to the organization (by enabling the "Invite to default project" checkbox) or after the member has accepted the organization invitation.   
  
Users invited via the Admin API follow the rules outlined by [the `/organization/invites` endpoint](https://platform.openai.com/docs/api-reference/invite/create).  
  
If you encounter an error when inviting users to a project through the UI or the Admin API, first confirm that the target project exists and is not archived before resending the invitation.  
  
Organization owners are automatically added as owners to new projects created within an organization.

## **What are the different user roles within organizations and projects, and what permissions do they entail?**

Whereas [Organizations have ‘owner’ and ‘reader’ roles](/en/articles/4936812-how-do-i-add-change-or-remove-members-on-my-openai-api-account), projects have ‘owner’ and ‘member’ roles. Project members are analogous to organization readers. Please refer to the table below for a more detailed description of what permissions accompany each user role.

| **Role** | **Scope** | **Description** |
| --- | --- | --- |
| Owner | Organization | Can create/view all projects, all users, all API keys. Has the ability to monitor across all projects within the organization with the  [Projects page](https://platform.openai.com/projects) . Able to set organization budgets and project budgets. Can grant permissions to view usage information for others in the org. Can archive projects. |
| Reader | Organization | Can perform inference, use resources, and create keys in their projects. Can be added to projects. Cannot create projects and manage users. |
| Owner | Project | Can add other users to the project and rename the project, as well as all the abilities of a Member. Able to set project budgets. Can archive the project. |
| Member | Project | Can perform inference, use resources, and create keys at the project level. |

## **If I’m not an Owner in the organization, what do I have access to?**

Users that are not Owners in the organization can only see projects that they are members of. Only the organization owner can see all projects, members, and API keys at the project level, and have access to the [Projects page](https://platform.openai.com/projects).

* Only the members of a project (and organization owners) can see the fine tuned models that have been created within that project, the threads from any Assistants created, or any files that have been added.
* Members of a project can see who all the other members of that project are and their roles (i.e. Owner or Member).

## **How do I update a user’s project role or remove a user from a project?**

Only the Owner of a project can update a user’s project role or remove a user from a project. Please refer to [**roles and permissions**](#h_962ddad85d) for more information.  
  
To update a user in a project, go to your [organization settings](https://platform.openai.com/settings/organization), select the project, and click on **Members**. You have the option to set each member’s role as a **Member** or **Owner.** You can also select **Remove** to remove the user from the project.

## **What is a service account, and how does it differ from a regular user account?**

A service account acts as a pseudo-user designed for system access, distinct from individual user accounts. Only organization and project owners can create service accounts.

Service accounts are only scoped to projects.

## **Add a member to a project**

If you click the `+ Add member` button you will see a list of users in your organization with the role `Reader`. If you want to add the user who is not currently within your organization, you'd need to add them to the organization first (you can keep the 'Add to Default Project" checkbox unchecked if you don't want to give these users wider access). This list will not include service accounts. During this step you can choose if their role is either `Owner` or `Member`:

![Project members with Add team members dialog assigning a user the Member role](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-8273831400e2cf19628038e5/2f6ff84088b9c3461b1ede34e529c306/Frame_2B10.png)

When you add a team member, you must assign them either the **Member**or **Owner** role. Project members can make API requests that read or modify data, whereas project owners can also modify project settings and project budgets and manage project members. Please refer to [**roles and permissions**](#h_962ddad85d) for more information.

## **How to create a service account for a project**

First navigate to the project you want to create a service account for by choosing from the dropdown found in the navigation bar:

![API platform project switcher open with options to create a project or manage projects](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-4be33755a1d118b8f967cf68/e8fd1ddd4d6e876c701f4aa1948eadf7/Frame_8.png)

Then, go to your [organization settings](https://platform.openai.com/settings/organization) -> Project -> Members -> click on `+ Service account`:

Service accounts created at the project level are unique to the project and cannot be used outside of the project they are created in.

![Project Members page with Create a service account dialog after selecting the Service account option](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-55141d2d732828e5f41ea23d/31605b67bd1d4d7e7e8de125e88863a0/Frame_9.png)

### **Naming the service account**

Regardless of whether you create the service account at the organization level or create one unique to a project, when you create a service account you can create a unique service account ID consisting of letters, numbers, and hyphens to easily identify the service account.

### **Save the service account API key**

After selecting the **Create** button, an API key is immediately created for the service account and the secret key will be displayed. Save this secret key somewhere safe and secure. For security reasons, you won't be able to view it again through your OpenAI account. If you lose this secret key, then you will need to generate a new one.

![Members page with Save your key modal after creating a service account](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-b1281352b3d8ce8e18be65a4/8f9b44dfe45aebf2e0e2b08993818017/Frame_15.png)

The service account API key permissions are defaulted to read and write all of the project’s API resources. These permissions can be updated in your project’s API Keys settings.  
  
Service accounts are listed alongside project members in your project’s member settings page. Please refer [**here**](#h_9363816891) to learn more about updating or removing a service account’s access in your project’s member settings page.

All service accounts across both projects and organizations will be displayed alongside your human users in the [organization level members page](https://platform.openai.com/settings/organization/members).

Service accounts are managed like regular accounts. From the Organization -> [Members menu](https://platform.openai.com/settings/organization/team) you can **Remove** a service account or update the role:

![OpenAI API Members settings with a service account role menu open for Reader or Owner](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-4aa0d12197e22b7289ea3b22/d2a77a02f7648634a700295b3589e6c7/Frame_11.png)

## **How do I manage API keys within my organization's projects?**

You can create and manage API keys for each project on that project’s settings page. In your [organization settings](https://platform.openai.com/settings/organization), select the project, and click on **API Keys**.   
  
To create a new secret key, select `+ Create new secret key`. You can also select the Edit icon next to a secret key to edit its permissions.

![API keys page for a project with the Create new secret key button highlighted](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-e0b10057112edb4f7ffd81c0/3b9fb08bcc636eaefee1a7f6c5391ea2/Frame_12.png)

You can set permissions for each of your API keys when you create a new secret key or by editing an existing key.  
  
Three levels of permissions are available: All, Restricted, and Read Only.

* **All** — Full permissions are set for the secret key. This is the default setting.
* **Restricted** — Enables the user to set None, Read, and Write permissions for each endpoint.

  + For example, you create an API key that specifically does not have permission to Read or Write to the /v1/assistants endpoint:

    ![Create new secret key dialog in the API platform with Restricted permissions selected](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-31e55bc83cf1bbb71a5c8c5e/03b55611063f104024f3d50a6a875625/Frame_13.png)

* **Read Only** — Read permissions are set for all endpoints.

## **How is access managed for users belonging to multiple projects or organizations?**

Users can be members of as many projects as are needed. Within a project, users can generate a personal API key that is scoped and limited to accessing that project and its resources.

## **How do I set and manage rate limits for my organization's projects?**

Only the Owner of an organization can set and manage project level rate limits. Please refer to [**roles and permissions**](#h_962ddad85d) for more information.  
  
In your [organization settings](https://platform.openai.com/settings/organization), click on the project you want to update and select **Limits** in the Project section of the navigation list**.** You can update your **Model Usage** on this page.  
  
Model usageallows you to configure which models can be used by the project, and **rate limits** can be set for each model as needed.

## **How do I set and manage budgets for my organization's projects?**

Only the Owners of an organization and Owners of a project can set and manage project budgets. Please refer to [**roles and permissions**](#h_962ddad85d) for more information. To change the limits at the organization level, in your [organization settings](https://platform.openai.com/settings/organization), click on **Limits,** and scroll down to **Usage limits.**

![Project Limits page with organization budget controls, usage alerts, and model rate limits table](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-4b099160e0811a08b5e56234/a45511110021b333af9dca7bd8b4ce00/image.png)

To set your project limits, in your [organization settings](https://platform.openai.com/settings/organization), click on the project you want to update and select **Limits.** You can update your **Monthly budget**, **Notification threshold**, and **Model Usage**.  
  
Setting a **monthly budget** allows you to establish soft spending thresholds for your project. When usage exceeds this limit within a given calendar month (UTC), API requests will continue to be processed without interruption. This feature is designed to help you monitor usage through budget alerts, but it does not enforce a hard cap on spending. When a project budget is created, by default, an alert will be created at the 100% threshold. Additional budgets at different thresholds can be set by clicking **Add Alert**.  
  
Please note that the organization owner(s) and project owner(s) will always receive these messages and this cannot be customized.

![Project Limits page with Add budget alert dialog set to notify at 90% budget usage](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-57ecf2bca8bc57a984598001/d97a7a9ecc9506730d2012656503cf25/image.png)

## **How do I delete or archive a project?**

Projects can be archived through either the new [project listing](https://platform.openai.com/projects) page or on the settings of an individual project. **Once a project is archived it cannot be restored**. When proceeding with an archive, you will be prompted to enter the project’s name to proceed forward.  
  
You can view a list of all archived projects through the “Archived” tab on the same [project listing](https://platform.openai.com/projects) page.

![API platform Projects page with the Archived tab selected to view archived projects](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-e01f6014e215dc2e2eadbfd6/c4526e43c31e2dcefe43957d893b3237/Frame_14.png)

Deleting projects is not possible, we maintain a history of all projects to ensure continuity with usage and billing tracking.

## **Is there a limit to the number of projects I can have in my organization?**

Organizations can create up to 2,000 projects by default.

## **Can resources be shared across projects?**

Project resources (such as files, assistants, storage, or threads) are scoped to the project and cannot be accessed from non-admin members outside of the project. Furthermore, resources cannot be moved between projects.

The one exception is that fine tunes in the "Default project" can be accessed from other projects.

## **What is the file storage quota per project?**

OpenAI currently support a file storage quota of 100 GB of files per project.   
  
If this quota is breached, you will see the following error:

```
You have exceeded your file storage quota. Organizations are limited to 100 GB of files. Please reduce the file size or contact support.
```

We recommend you delete unused files stored on your account. For reference, you can [view and list files with](https://platform.openai.com/docs/api-reference/files/list) the API.

## **I'm a project owner, why can't I see the Usage Dashboard for my project?**

A projects Usage Dashboard visibility is not related to the role of a user within a project. Instead, it is determined by your role within the organization *and* the settings at <https://platform.openai.com/settings/organization/data-controls/visibility>

![Project setting for Usage dashboard visibility with Visible to organization owners selected](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-aac96d5b58be10172f8f0ff1/2b10e349c6bc2cc36af223b0da3e9c34/Screenshot_2025-02-12_at_1_53_22_E2_80_AFPM.png)

If you're unable to see a Usage Dashboard, this setting is likely set to "Visible to organization owners".

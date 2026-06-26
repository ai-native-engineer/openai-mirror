<!-- source: https://help.openai.com/en/articles/9083985-groups-in-chatgpt-enterprise-and-edu -->

# Groups in ChatGPT Enterprise and Edu

Manage access and permissions in your ChatGPT Enterprise workspace with groups

Updated: 10 days ago

# Overview

Groups let you control access and permissions with more granularity inside a ChatGPT Enterprise workspace. Groups allow the usage of [RBAC](/en/articles/11750701-rbac), and allow for easy configuration of access to other settings!  
  
Note that only workspace **owners** and **admins** can modify group settings or add members to groups.  
  
---

# Create or manage a group

1. In ChatGPT, go to **Manage workspace**.
2. Select **groups** in the left sidebar.
3. Choose **Create group**.
4. Enter a **name** and optional **description**.
5. **Add members** to add members individually or in bulk.

To update an existing group, open it from the list and select **Manage** to edit the group settings, or delete the group.  
  
For information on managing groups using SCIM, please refer to our article: [OpenAI ChatGPT SCIM Integration FAQ](/en/articles/9627404-openai-chatgpt-scim-integration-faq)  
  
---

# Limits and availability

* **Maximum number of groups per workspace**: 10,000
* **Maximum number of users per group:** No limit

---

# FAQ

## Who can create and manage groups?

Only workspace owners and admins.

## Can regular users see groups?

Yes, they can see groups when they share a GPT, but they cannot create or edit groups.

## Can users request to join a group?

No. Users must be invited by an owner or admin.

## What can I control with groups today?

Groups are required if using [RBAC](/en/articles/11750701-rbac), and are also used to easily allow access to GPTs, projects, apps, and more.

## Can users be members of more than one group?

Yes, users can be members of multiple groups.

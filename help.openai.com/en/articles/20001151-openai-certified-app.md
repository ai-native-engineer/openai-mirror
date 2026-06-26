<!-- source: https://help.openai.com/en/articles/20001151-openai-certified-app -->

# OpenAI Certified app

Learn about the OpenAI Certified app, including setup instructions, access requirements, and troubleshooting guidance.

Updated: 10 days ago

# Overview

OpenAI Certified is a Coursera-powered learning experience in ChatGPT that allows eligible learners to access supported OpenAI learning content, complete assessments, and earn credentials where available.  
  
Users will need a Coursera account to use the app. If you’re already signed in to Coursera, ChatGPT can take you directly to the course experience. If not, you’ll be redirected to Coursera to sign in or create an account.  
  
Upon completion of eligible courses or assessments, learners may receive an OpenAI-issued credential through Coursera and distributed via Credly, a third-party credentialing platform.

## Availability

At this time, the OpenAI Certified app is available only for ChatGPT Enterprise and Edu workspaces on an invite-only basis.  
  
If you’re interested in enrolling, contact your OpenAI account representative.

# Getting started

To use OpenAI Certified, an admin must first enable it for the workspace. After that, each user must connect the app individually before using it.

## For admins: enable the app for your workspace

To make OpenAI Certified available to users in your workspace:

1. Go to **Admin settings** in ChatGPT.
2. Select **Permissions & roles**.
3. In **Workspace**, confirm that **Connected data** > **Allow members to use apps** is turned on.
4. Select **Apps**.
5. Select the **Directory** tab.
6. Find **OpenAI Certified**.
7. Select **Enable**.

After you select **Enable**, review the enable flow and complete setup for your workspace.

### Configure access for custom roles (RBAC)

If your workspace uses custom roles:

1. During setup, select **Configure access**.
2. Limit the app to the appropriate roles for your workspace.

After the app is enabled, eligible members in the workspace can connect and use it.

## For users: connect OpenAI Certified

After your workspace admin enables OpenAI Certified and your role has access, you must connect the app before using it.

1. Open **Settings** in ChatGPT.
2. Select **Apps**.
3. Select **Add more**.
4. Find **OpenAI Certified**.
5. Select **Connect**.
6. Review the consent screen and continue to Coursera.
7. Sign in to Coursera or create a Coursera account if needed.
8. Allow access and return to ChatGPT.

After you connect the app, you can open OpenAI Certified in ChatGPT and begin using the learning experience.

# Using the app

After you connect OpenAI Certified, you can enroll in eligible courses, complete assessments, and track your progress in the learning experience.  
  
To start:

1. Open a new or existing chat in ChatGPT.
2. Select the **+ (tools menu)** in the message composer.
3. Select the **more options menu (•••)**.
4. Select **OpenAI Certified**.
5. Send a message, such as “Show my courses”.

Alternatively, enter **@OpenAI Certified** in the message composer.

# Data, privacy, and compliance

### Containment of Memory and Chat History

OpenAI Certified does not provide Coursera access to ChatGPT chat history or the user’s saved memory store. Coursera only receives the specific, minimal data exchanged through the OpenAI Certified app for a given interaction. These data flows are limited to course state, progress, and assessment-related inputs/outputs required to operate the learning experience.  
  
If Memory or related personalization features are enabled in ChatGPT settings, ChatGPT may use saved memories and prior conversation context to personalize responses within ChatGPT. This personalization occurs entirely within ChatGPT and is not shared as a separate memory- or chat-history feed to Coursera. Coursera continues to only receive the limited course-state and assessment-related data necessary for course delivery.  
  
OpenAI does not access or use customer content or memories from customer tenants for analytics, program evaluation, or product improvement for the Certification Program.  
  
Separately, inputs explicitly submitted within the certification experience (e.g., assessment responses or in-product surveys) may be used to support program delivery and evaluation.

### Usage Data Access

OpenAI may process limited service usage data (e.g., telemetry, system performance metrics, abuse monitoring signals, and reliability diagnostics) for the purpose of operating and maintaining the ChatGPT service. This data does not include customer content or memory data and is not used to train generalized or commercial models without explicit customer consent.

### Data flow between Coursera and OpenAI

Within the OpenAI Certified app, ChatGPT may retrieve course content from Coursera and send back only the minimal course-state data required to operate the experience, such as:

* Progress and completion status
* Assessment results
* Limited structured feedback from assessment interactions

For certain assessment types (e.g., roleplay-based evaluations), the response payload may include a score and a high-level AI-generated feedback summary. This output is a sanitized evaluation artifact and does not include raw chat transcripts, memory data, or conversation history.

## Compliance Platform

Conversation data may still appear in standard conversation exports in the OpenAI Compliance Platform, but it is not identified as OpenAI Certified app usage specifically.  
  
For more information, see: [OpenAI Compliance Platform for Enterprise Customers](/en/articles/9261474-openai-compliance-platform-for-enterprise-customers).

# FAQ

## Why can’t I see the OpenAI Certified app in ChatGPT?

Access is limited to eligible Enterprise and Edu workspaces on an invite-only basis. If the app does not appear, your workspace may not be included in the rollout or your admin may not have enabled it.  
  
If you believe you should have access, contact your workspace admin to confirm that the app has been enabled for your account.

## Do I need a Coursera account and a Credly account to use the app?

Yes. A Coursera account is required to access courses through the app. You will sign in or create an account during setup.  
  
A Credly account is required to receive and view completion credentials. If you do not already have a Credly account, you will be prompted to create a new account upon receiving your Credly credential via email.

## Will I receive a certificate or badge after completing a course?

Yes. Eligible learners may receive an OpenAI-issued credential through Coursera and distributed via Credly, a third-party credentialing platform.

## Why didn’t I receive my badge after finishing a course?

This can occur if course requirements are incomplete or if there is a mismatch between the email used for Coursera and Credly.  
  
Verify that all course requirements are completed, including the pre- and post-course surveys and final assessment, and check the Credly account associated with your Coursera email or the alternate email used for Credly.

## Why am I seeing errors when using the app?

This typically indicates an issue with session loading, permissions, or app connectivity. Start a new ChatGPT conversation and try again. If the issue persists, contact OpenAI Support.

## Does Coursera or Credly get access to my ChatGPT conversations?

No. Chat history is not shared during account linking or when using the app.

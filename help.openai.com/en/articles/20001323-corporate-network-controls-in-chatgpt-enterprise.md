<!-- source: https://help.openai.com/en/articles/20001323-corporate-network-controls-in-chatgpt-enterprise -->

# Corporate Network Controls in ChatGPT Enterprise

Workspace Blocking is a feature that allows ChatGPT Enterprise customers to restrict access to specific ChatGPT workspaces, ensuring that users can log in and interact within the allowed workspaces.

Updated: 2 days ago

# Overview

Workspace Blocking is a feature that allows ChatGPT Enterprise customers to restrict access to specific ChatGPT workspaces, ensuring that users can log in and interact within the allowed workspaces. This feature ensures that users within your organization are limited to accessing specific, approved workspaces.

# How it works

* **Custom header setup:** You configure which workspaces are allowed by adding a custom HTTP header, `ChatGPT-Allowed-Workspace-Id`, to your network configuration. This header contains one or more workspace IDs (UUIDs) that specify which workspaces users can access.
* **ChatGPT filters access:**

  + When a user logs into ChatGPT Enterprise, the system checks if the workspace they are trying to access matches any of the workspace UUIDs listed in the `ChatGPT-Allowed-Workspace-Id` header.
  + If the user tries to access a workspace not listed in the header, ChatGPT automatically filters this request, blocking access to that workspace. As long as a user has access to at least one workspace, the filtering happens silently. In cases where the user ends up with access to no workspaces after filtering, the user will receive a `403 Forbidden` error.
  + Only the workspaces listed in the header will be accessible, and any other workspaces (including personal workspaces) are filtered out by the system.
* **Supporting multiple workspaces:** If your organization needs to allow access to more than one workspace, you can include multiple workspace UUIDs in the header, separated by commas with no space in between.

# Setup

## Step 1: Get the Workspace ID

To allow access to specific workspaces, you will need to find the Workspace UUID for each allowed workspace. This UUID can be found in the ChatGPT admin settings:

* Log in to your ChatGPT Enterprise admin account.
* Navigate to the Admin Settings page.
* Find the Workspace ID (UUID) that corresponds to each workspace you want to allow.

Example Workspace UUID: `437adf77-4085-4b22-b7b1-de7b6f5ec6c0`

## Step 2: SASE vendors

For enterprise-wide implementations, organizations can work with their Secure Access Service Edge (SASE) partners. These partners can enforce the Workspace Blocking feature at the network level.

## Step 3: Configuration

* **Allow multiple workspaces (if needed):**To allow access to multiple workspaces, input the Workspace UUIDs separated by commas.
* **Specify URL Targeting:**

  + Ensure that the header is applied to the ChatGPT URL. Set the URL filter to apply only to requests made to `https://chatgpt.com/*`

## Step 4: Error Handling

* **403 Forbidden Error:** If a user attempts to access a workspace and there are no available workspaces after filtering, they will see a `403 Forbidden` error, and a message will indicate they are not authorized to access the workspace.
* **400 Bad Request Error:** If the header value is malformed (e.g., the workspace UUID is incorrect), all requests with that header will fail with a `400 Bad Request` error.

## Step 5: Block anonymous (logged out) ChatGPT usage

ChatGPT can also be used without an account or workspace at all, we call this our anonymous or logged-out product. To effectively block this type of usage work with your SASE vendor to block access to URLs that start with `https://chatgpt.com/backend-anon/` or use the same browser configuration you used to insert headers to also block URLs with that prefix.

## Step 6: Consider ChatGPT desktop and mobile application compatibility

ChatGPT desktop and mobile apps implement certificate pinning. This restricts the set of server certificates a client will accept, adding an extra safeguard against advanced interception (MiTM) attacks where a valid certificate has been compromised. The pinning check happens after the server certificate has already been validated against trusted root certificates.  
  
In order for ChatGPT desktop and mobile applications to work properly when SSL inspection is enabled (required to implement the above network controls), you will need to add your own certificates to the pin list, and distribute them to clients via MDM. See here for detailed instructions: <https://docsend.com/view/rrk4mx9aashcekp7>

# FAQ

## Will workspace blocking work on iOS mobile devices, macOS and Android applications?

Workspace Blocking via network header injection can be enforced on ChatGPT applications on managed devices where certificate pinning exceptions have been deployed via MDM as described above.  
  
If an organization wants to prevent users from accessing ChatGPT (including personal accounts) through the iOS, macOS, and Android apps, they can configure their network firewall, proxy, or SASE service to block access to the following domains:

* **Android app:** `android.chat.openai.com`
* **Desktop web app:** `desktop.chatgpt.com`
* **iOS app:** `ios.chat.openai.com`

Please note that blocking access to the above domains blocks *all* traffic to the applications, meaning no one will be able to access ChatGPT via these platforms, regardless of whether they are using a personal or an Enterprise account.

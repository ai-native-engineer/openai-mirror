<!-- source: https://help.openai.com/en/articles/8867743-assign-api-key-permissions -->

# Assign API Key Permissions

Updated: 10 days ago

You can set permissions for user-owned API keys when you create a new secret key or by editing an existing key. Users with service-account management permissions, typically organization or project owners, can create service account keys. If you do not see this option, ask an owner to create the service account key. The key-creation dialog does not show these permission controls for service account keys.

* **All** — Full permissions are set for the secret key. This is the default setting.
* **Restricted** — Lets users choose specific API-key scopes for resources/endpoints. Available choices vary by resource and can include None, Read, Write, or request-specific permissions.
* For example, you create an API key that specifically does not have permission to Read or Write to the /v1/assistants endpoint:

* **Read Only** ― Read permissions are set for all endpoints.

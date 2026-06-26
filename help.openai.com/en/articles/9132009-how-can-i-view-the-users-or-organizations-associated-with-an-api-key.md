<!-- source: https://help.openai.com/en/articles/9132009-how-can-i-view-the-users-or-organizations-associated-with-an-api-key -->

# How can I view the users or organizations associated with an API key?

Updated: 14 days ago

If you need to find the user and organizations associated with an API key, you can do so by calling the https://api.openai.com/v1/me endpoint, using the API key as the Bearer token.  
  
Here's an example of what this would look like as a cURL call:

```
curl https://api.openai.com/v1/me \  
-H "Authorization: Bearer $OPENAI_API_KEY"
```

This will return an object with the following structure (non-critical elements removed for convenience):

```
{  
  "object": "user",  
  "id": "user-1234",  
  "email": "user@yourcompany.com",  
  "name": "Users Name",  
  ...  
  "orgs": {  
    "object": "list",  
    "data": [  
      {  
        "object": "organization",  
        "id": "org-abcd",  
        "title": "Org 1 Name",  
         ...  
      },  
      {  
        "object": "organization",  
        "id": "org-1234",  
        "title": "Org 2 Name",  
         ...  
      }  
    ]
```

You can use this information to perform any needed follow-up actions (for example: if an API key is leaked, revoke it from the API keys settings page for its scope - Organization API keys at https://platform.openai.com/settings/organization/api-keys, or the relevant Project API keys page. If you do not have access, ask an organization or project owner to revoke it).

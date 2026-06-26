<!-- source: https://help.openai.com/en/articles/9242831-how-does-the-launch-of-assistants-api-v2-affect-my-assistants-launched-with-api-v1 -->

# How does the launch of Assistants API v2 affect my Assistants launched with API v1?

Implications on Playground, cost, and migration

Updated: 14 days ago

As of March 11, 2025, we’ve released the building blocks of our new Agents platform. For details, see our API docs for our [Responses API](https://platform.openai.com/docs/quickstart?api-mode=responses), Tools including [Web Search](https://platform.openai.com/docs/guides/tools-web-search), [File Search](https://platform.openai.com/docs/guides/tools-file-search), and [Computer Use](https://platform.openai.com/docs/guides/tools-computer-use), and our [Agents SDK](https://platform.openai.com/docs/guides/agents-sdk#page-top) with [Tracing](https://platform.openai.com/docs/guides/agents-sdk#tracing).

* **No Automatic Upgrade**: Your current Assistants, Threads, and Runs are not automatically migrated to v2. They remain accessible and operational under the v1 API unless you choose to migrate them manually.
* **Access to Both Versions**: Both v1 and v2 API versions are fully accessible to you. This means you can continue using v1 for your existing assistants or explore the new features and improvements offered by v2.
* **Token Usage Differences**: There may be variations in token usage between v1 and v2, particularly tools like file\_search and retrieval. While the file\_search tool in v2 typically consumes fewer tokens on average compared to the retrieval tool in v1, you can still use the older retrieval tool with the v1 version header if you'd like.
* **Migration Options**: While the Playground UI and updated SDK versions migrated to use the v2 version of the API, your Assistants are not automatically upgraded. You have the flexibility to choose which API version to use for your integration. Remember, there’s no default API version for Assistant objects, so you can continue using the older version until the end of 2024 if preferred. For more information regarding migration from Assistants v1 to v2, please check out this [migration guide](https://platform.openai.com/docs/assistants/migration).

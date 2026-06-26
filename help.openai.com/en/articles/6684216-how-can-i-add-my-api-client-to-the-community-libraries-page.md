<!-- source: https://help.openai.com/en/articles/6684216-how-can-i-add-my-api-client-to-the-community-libraries-page -->

# How can I add my API client to the Community Libraries page?

Criteria and steps to ensure your library is ready to be added to our Community Libraries page

Updated: 10 days ago

OpenAI maintains a [Community Libraries](https://beta.openai.com/docs/libraries/community-libraries) page where we list API clients that developers can use to access the OpenAI API.  
  
If you've built an open source library that you'd like added to this page – thank you! We love to see developers build additional API tooling for other developers. We also want to make sure we are steering developers to good solutions that will make them successful long term, so we have a few criteria that we require before listing libraries on our website.  
  
Please make sure you meet the criteria listed below, and then fill our our [Community Libraries request form](https://share.hsforms.com/1y0Ixew-rQOOZisFfnhszVA4sk30).

1. **Standard open source license**

To be listed, we require that community libraries use a [permissive open-source license](https://choosealicense.com/) such as MIT. This allows our customers to more easily fork libraries if necessary in the event that the owners stop maintaining it or adding features.

1. **Load API keys through environment variables**

Code samples in the README must encourage the use of environment variables to load the OpenAI API key, instead of hardcoding it in the source code.

1. **Correct, high quality code that accurately reflects the API**

Code should be easy to read/follow, and should generally adhere to our [OpenAPI spec](https://github.com/openai/openai-openapi/blob/master/openapi.yaml) – new libraries should **not** include endpoints marked as `deprecated: true` in this spec.

1. **State that it’s an unofficial library**

Please state somewhere near the top of your README that it’s an “unofficial" or "community-maintained” library.

1. **Commit to maintaining the library**

This primarily means addressing issues and reviewing+merging pull requests. It can also be a good idea to set up Github Issue & PR templates like we have in our [official node library](https://github.com/openai/openai-node/tree/master/.github/ISSUE_TEMPLATE).

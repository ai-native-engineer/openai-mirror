<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/responses/methods/connect/ -->

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

[Responses](/api/reference/python/resources/beta/subresources/responses)

# Connect

beta.responses.connect()

Function

Connect to a persistent Responses API WebSocket. Send `response.create` events and receive response stream events over the socket.

### Connect

Python

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
client.beta.responses.connect()

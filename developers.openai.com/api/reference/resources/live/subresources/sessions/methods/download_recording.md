<!-- source: https://developers.openai.com/api/reference/resources/live/subresources/sessions/methods/download_recording/ -->

[Live](/api/reference/resources/live)

[Sessions](/api/reference/resources/live/subresources/sessions)

# Download recording

GET/live/sessions/{session\_id}/content

Get Live session content

session\_id: string

The ID of the stored Live session to download. Use the session ID returned when the session started with storage enabled.

### Download recording

curl https://api.openai.com/v1/live/sessions/$SESSION_ID/content \

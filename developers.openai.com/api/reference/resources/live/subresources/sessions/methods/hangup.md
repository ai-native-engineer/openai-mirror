<!-- source: https://developers.openai.com/api/reference/resources/live/subresources/sessions/methods/hangup/ -->

[Live](/api/reference/resources/live)

[Sessions](/api/reference/resources/live/subresources/sessions)

# Hang up session

POST/live/sessions/{session\_id}/hangup

End a SIP call identified by session\_id.

session\_id: string

### Hang up session

curl https://api.openai.com/v1/live/sessions/$SESSION_ID/hangup \
    -X POST \

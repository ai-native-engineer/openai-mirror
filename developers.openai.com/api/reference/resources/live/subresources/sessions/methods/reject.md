<!-- source: https://developers.openai.com/api/reference/resources/live/subresources/sessions/methods/reject/ -->

[Live](/api/reference/resources/live)

[Sessions](/api/reference/resources/live/subresources/sessions)

# Reject call

POST/live/sessions/{session\_id}/reject

Reject an incoming SIP call. Send a required SIP rejection status\_code between 300 and 699.

session\_id: string

##### Body ParametersJSONExpand Collapse

status\_code: number

SIP rejection status sent to the caller. This field is required.

minimum300

maximum699

### Reject call

curl https://api.openai.com/v1/live/sessions/$SESSION_ID/reject \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
          "status_code": 486
        }'

<!-- source: https://developers.openai.com/api/reference/resources/live/subresources/sessions/methods/refer/ -->

[Live](/api/reference/resources/live)

[Sessions](/api/reference/resources/live/subresources/sessions)

# Transfer call

POST/live/sessions/{session\_id}/refer

Transfer a SIP call to another destination. Supply a nonblank target\_uri for the SIP Refer-To header.

session\_id: string

##### Body ParametersJSONExpand Collapse

target\_uri: string

Nonblank URI for the SIP Refer-To header, such as tel:+14155550123 or sip:[agent@example.com](mailto:agent@example.com).

minLength1

### Transfer call

curl https://api.openai.com/v1/live/sessions/$SESSION_ID/refer \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
          "target_uri": "tel:+14155550123"
        }'

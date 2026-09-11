<!-- source: https://developers.openai.com/api/reference/resources/live/subresources/sessions/ -->

[Live](/api/reference/resources/live)

# Sessions

##### [Accept call](/api/reference/resources/live/subresources/sessions/methods/accept)

POST/live/sessions/{session\_id}/accept

##### [Download recording](/api/reference/resources/live/subresources/sessions/methods/download_recording)

GET/live/sessions/{session\_id}/content

##### [Fork session](/api/reference/resources/live/subresources/sessions/methods/fork)

POST/live/sessions/{session\_id}/fork

##### [Hang up session](/api/reference/resources/live/subresources/sessions/methods/hangup)

POST/live/sessions/{session\_id}/hangup

##### [Transfer call](/api/reference/resources/live/subresources/sessions/methods/refer)

POST/live/sessions/{session\_id}/refer

##### [Reject call](/api/reference/resources/live/subresources/sessions/methods/reject)

POST/live/sessions/{session\_id}/reject

##### ModelsExpand Collapse

SessionForkResponse object { session, transport }

The created Live session identifier and WebRTC answer. Apply transport.sdp as the peer’s remote answer and wait for session.started on the data channel before sending commands.

session: object { id }

The newly created Live session. Use its ID for session controls and sideband connections.

Opaque session identifier. Preserve the returned value unchanged, including its prefix.

transport: object { sdp, type }

WebRTC transport with the SDP answer.

sdp: string

Session Description Protocol message for the WebRTC connection.

minLength1

type: "webrtc"

The transport used for the Live session. Always `webrtc`.

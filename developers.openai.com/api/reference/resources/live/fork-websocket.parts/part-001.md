<!-- source: https://developers.openai.com/api/reference/resources/live/fork-websocket/ -->
<!-- part of: https://developers.openai.com/api/reference/resources/live/fork-websocket/ -->

<!-- chunk-start -->

# Fork WebSocket

> For the complete documentation index, see [llms.txt](/llms.txt). Markdown versions of documentation pages are available by appending `.md` to the page URL.

Start a new Live session from stored conversation state. Send and receive audio and control events on the new WebSocket connection.

WS `/v1/live/sessions/{session_id}/fork`

## Connection

`wss://api.openai.com/v1/live/sessions/{session_id}/fork`

Authenticate from your backend with your OpenAI API key in the `Authorization: Bearer $OPENAI_API_KEY` header. Keep the key on your server.

`session_id` (required path parameter): The ID of the stored source session to fork. The fork receives a new session ID.

No query parameters. After connecting, send session.start with a session overrides object. An empty object inherits the stored configuration. Do not supply a new model. Wait for session.started before sending audio or other commands.

## Inputs

Required once after connecting. Omitted settings are inherited, including store. You may override Responses delegation settings, storage, and the new WebSocket audio format. Frontend client permissions apply only to WebRTC forks.

### First message: session.start

```json
{
  "type": "session.start",
  "session": {}
}
```

[All client events](#client-events)

## Outputs

The server confirms the new session is ready. Use its new ID for subsequent sideband connections and session controls.

### Fork ready · excerpt: session.started

```json
{
  "type": "session.started",
  "event_id": "event_started_1",
  "session": {
    "id": "live_fork_123",
    "expires_at": 1788307200,
    "status": "active",
    "model": "gpt-live-1"
  }
}
```

[All server events](#server-events)

[Learn how to store a session and fork its conversation.](https://developers.openai.com/api/docs/guides/live-conversations#store-and-fork-a-session)

## Client events

### session.start

Start a Live session after connecting to a stored session’s fork WebSocket. Send an empty `session` object to use the stored configuration.

#### Schema

Schema name: `LiveForkSessionStartEvent`

```json
{
  "(resource) live > (model) fork_session_start_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveForkSessionStartEvent",
    "docstring": "Start a Live session after connecting to a stored session’s fork WebSocket. Send an empty `session` object to use the stored configuration.",
    "ident": "ForkSessionStartEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "session"
        },
        {
          "ident": "type"
        },
        {
          "ident": "event_id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) fork_session_start_event > (schema) > (property) session",
      "(resource) live > (model) fork_session_start_event > (schema) > (property) type",
      "(resource) live > (model) fork_session_start_event > (schema) > (property) event_id"
    ]
  },
  "(resource) live > (model) fork_session_start_event > (schema) > (property) session": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveForkSessionStartEvent/properties/session",
    "deprecated": false,
    "key": "session",
    "docstring": "Overrides for a stored session after connecting to the fork WebSocket. An empty object inherits the stored configuration; do not supply a new model. audio.format applies only to the new WebSocket connection. client overrides are only supported for WebRTC forks.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ForkSessionConfig",
      "$ref": "(resource) live > (model) fork_session_config > (schema)"
    },
    "optional": false,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "object",
    "modelPath": "(resource) live > (model) fork_session_config",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) fork_session_config > (schema) > (property) audio",
      "(resource) live > (model) fork_session_config > (schema) > (property) client",
      "(resource) live > (model) fork_session_config > (schema) > (property) delegation",
      "(resource) live > (model) fork_session_config > (schema) > (property) store"
    ]
  },
  "(resource) live > (model) fork_session_start_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveForkSessionStartEvent/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The Live client event type. Always `session.start`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveForkSessionStartEvent/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.start"
        }
      ]
    },
    "default": "session.start",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) fork_session_start_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) fork_session_start_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveForkSessionStartEvent/properties/event_id",
    "deprecated": false,
    "key": "event_id",
    "docstring": "Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 512
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) fork_session_config > (schema) > (property) audio": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveForkSessionConfigParam/properties/audio",
    "deprecated": false,
    "key": "audio",
    "docstring": "Audio format for a WebSocket fork. WebRTC forks negotiate their audio format and must omit this field.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "format"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) fork_session_config > (schema) > (property) audio > (property) format"
    ]
  },
  "(resource) live > (model) fork_session_config > (schema) > (property) client": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveForkSessionConfigParam/properties/client",
    "deprecated": false,
    "key": "client",
    "docstring": "Frontend data-channel permissions for a WebRTC fork. Omitted permissions inherit the stored values. Not supported for WebSocket forks.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ClientConfig",
      "$ref": "(resource) live > (model) client_config > (schema)"
    },
    "optional": true,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "object",
    "modelPath": "(resource) live > (model) client_config",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) client_config > (schema) > (property) data_channel"
    ]
  },
  "(resource) live > (model) fork_session_config > (schema) > (property) delegation": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveForkSessionConfigParam/properties/delegation",
    "deprecated": false,
    "key": "delegation",
    "docstring": "Overrides for the stored session’s Responses backend. Only supported when the stored session already uses Responses delegation; the delegation type cannot change.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "responses"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) fork_session_config > (schema) > (property) delegation > (property) type",
      "(resource) live > (model) fork_session_config > (schema) > (property) delegation > (property) responses"
    ]
  },
  "(resource) live > (model) fork_session_config > (schema) > (property) store": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveForkSessionConfigParam/properties/store",
    "deprecated": false,
    "key": "store",
    "docstring": "Whether to store the forked session. Omission inherits the stored session's setting.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) fork_session_config > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveForkSessionConfigParam",
    "docstring": "Overrides for a stored session after connecting to the fork WebSocket. An empty object inherits the stored configuration; do not supply a new model. audio.format applies only to the new WebSocket connection. client overrides are only supported for WebRTC forks.",
    "ident": "ForkSessionConfig",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "audio"
        },
        {
          "ident": "client"
        },
        {
          "ident": "delegation"
        },
        {
          "ident": "store"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) fork_session_config > (schema) > (property) audio",
      "(resource) live > (model) fork_session_config > (schema) > (property) client",
      "(resource) live > (model) fork_session_config > (schema) > (property) delegation",
      "(resource) live > (model) fork_session_config > (schema) > (property) store"
    ]
  },
  "(resource) live > (model) fork_session_start_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.start"
    }
  },
  "(resource) live > (model) fork_session_config > (schema) > (property) audio > (property) format": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveForkAudioParam/properties/format",
    "deprecated": false,
    "key": "format",
    "docstring": "Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "AudioFormat",
      "$ref": "(resource) live > (model) audio_format > (schema)"
    },
    "optional": true,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "union",
    "modelPath": "(resource) live > (model) audio_format",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) audio_format > (schema) > (variant) 0",
      "(resource) live > (model) audio_format > (schema) > (variant) 1",
      "(resource) live > (model) audio_format > (schema) > (variant) 2"
    ]
  },
  "(resource) live > (model) client_config > (schema) > (property) data_channel": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveClientConfigParam/properties/data_channel",
    "deprecated": false,
    "key": "data_channel",
    "docstring": "Client and server event permissions for the WebRTC frontend data channel.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "DataChannelConfig",
      "$ref": "(resource) live > (model) data_channel_config > (schema)"
    },
    "optional": false,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "object",
    "modelPath": "(resource) live > (model) data_channel_config",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) data_channel_config > (schema) > (property) allowed_client_events",
      "(resource) live > (model) data_channel_config > (schema) > (property) allowed_server_events"
    ]
  },
  "(resource) live > (model) client_config > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveClientConfigParam",
    "docstring": "Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.",
    "ident": "ClientConfig",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "data_channel"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) client_config > (schema) > (property) data_channel"
    ]
  },
  "(resource) live > (model) fork_session_config > (schema) > (property) delegation > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationUpdateParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The delegation owner. Always `responses` for tasks handled by the Responses API.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveResponsesDelegationUpdateParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "responses"
        }
      ]
    },
    "default": "responses",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) fork_session_config > (schema) > (property) delegation > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) fork_session_config > (schema) > (property) delegation > (property) responses": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationUpdateParam/properties/responses",
    "deprecated": false,
    "key": "responses",
    "docstring": "Responses backend settings to update. Omitted settings keep their existing values.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponsesDelegationUpdateConfig",
      "$ref": "(resource) live > (model) responses_delegation_update_config > (schema)"
    },
    "optional": true,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "object",
    "modelPath": "(resource) live > (model) responses_delegation_update_config",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) instructions",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) max_output_tokens",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) model",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) parallel_tool_calls",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools"
    ]
  },
  "(resource) live > (model) audio_format > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveAudioFormat/oneOf/0",
    "docstring": "Raw, mono 16-bit little-endian PCM audio for a Live WebSocket connection.",
    "ident": "AudioPCM",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "rate"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) audio_format > (schema) > (variant) 0 > (property) rate",
      "(resource) live > (model) audio_format > (schema) > (variant) 0 > (property) type"
    ]
  },
  "(resource) live > (model) audio_format > (schema) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveAudioFormat/oneOf/1",
    "docstring": "Raw, mono G.711 μ-law audio for a Live WebSocket connection.",
    "ident": "AudioPCMU",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "rate"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) audio_format > (schema) > (variant) 1 > (property) rate",
      "(resource) live > (model) audio_format > (schema) > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) audio_format > (schema) > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveAudioFormat/oneOf/2",
    "docstring": "Raw, mono G.711 A-law audio for a Live WebSocket connection.",
    "ident": "AudioPCMA",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "rate"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) audio_format > (schema) > (variant) 2 > (property) rate",
      "(resource) live > (model) audio_format > (schema) > (variant) 2 > (property) type"
    ]
  },
  "(resource) live > (model) audio_format > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveAudioFormat",
    "docstring": "Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.",
    "ident": "AudioFormat",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveAudioFormat",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "rate"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "rate"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "rate"
            },
            {
              "ident": "type"
            }
          ]
        }
      ]
    },
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) audio_format > (schema) > (variant) 0",
      "(resource) live > (model) audio_format > (schema) > (variant) 1",
      "(resource) live > (model) audio_format > (schema) > (variant) 2"
    ]
  },
  "(resource) live > (model) data_channel_config > (schema) > (property) allowed_client_events": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveDataChannelConfigParam/properties/allowed_client_events",
    "deprecated": false,
    "key": "allowed_client_events",
    "docstring": "Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveDataChannelConfigParam/properties/allowed_client_events",
      "types": [
        {
          "kind": "HttpTypeUnion",
          "oasRef": "#/components/schemas/LiveDataChannelConfigParam/properties/allowed_client_events/oneOf/0",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "all"
            }
          ]
        },
        {
          "kind": "HttpTypeArray",
          "oasRef": "#/components/schemas/LiveDataChannelConfigParam/properties/allowed_client_events/oneOf/1",
          "elementType": {
            "kind": "HttpTypeString"
          }
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) data_channel_config > (schema) > (property) allowed_client_events > (variant) 0",
      "(resource) live > (model) data_channel_config > (schema) > (property) allowed_client_events > (variant) 1"
    ]
  },
  "(resource) live > (model) data_channel_config > (schema) > (property) allowed_server_events": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveDataChannelConfigParam/properties/allowed_server_events",
    "deprecated": false,
    "key": "allowed_server_events",
    "docstring": "Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveDataChannelConfigParam/properties/allowed_server_events",
      "types": [
        {
          "kind": "HttpTypeUnion",
          "oasRef": "#/components/schemas/LiveDataChannelConfigParam/properties/allowed_server_events/oneOf/0",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "all"
            }
          ]
        },
        {
          "kind": "HttpTypeArray",
          "oasRef": "#/components/schemas/LiveDataChannelConfigParam/properties/allowed_server_events/oneOf/1",
          "elementType": {
            "kind": "HttpTypeReference",
            "ident": "ServerEventSelector",
            "$ref": "(resource) live > (model) server_event_selector > (schema)"
          }
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) data_channel_config > (schema) > (property) allowed_server_events > (variant) 0",
      "(resource) live > (model) data_channel_config > (schema) > (property) allowed_server_events > (variant) 1"
    ]
  },
  "(resource) live > (model) data_channel_config > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveDataChannelConfigParam",
    "docstring": "Control which Live events an untrusted WebRTC frontend can send and receive over its data channel. These restrictions do not apply to trusted sideband connections.",
    "ident": "DataChannelConfig",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "allowed_client_events"
        },
        {
          "ident": "allowed_server_events"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) data_channel_config > (schema) > (property) allowed_client_events",
      "(resource) live > (model) data_channel_config > (schema) > (property) allowed_server_events"
    ]
  },
  "(resource) live > (model) fork_session_config > (schema) > (property) delegation > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "responses"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) instructions": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/instructions",
    "deprecated": false,
    "key": "instructions",
    "docstring": "Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) max_output_tokens": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/max_output_tokens",
    "deprecated": false,
    "key": "max_output_tokens",
    "docstring": "Maximum number of output tokens for each delegated response.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 16
    },
    "optional": true,
    "nullable": true,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) model": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/model",
    "deprecated": false,
    "key": "model",
    "docstring": "The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) parallel_tool_calls": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/parallel_tool_calls",
    "deprecated": false,
    "key": "parallel_tool_calls",
    "docstring": "Whether the delegated Responses model may request multiple tool calls in a single response.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/reasoning",
    "deprecated": false,
    "key": "reasoning",
    "docstring": "Reasoning settings passed to each delegated Responses request.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "effort"
        },
        {
          "ident": "summary"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) summary"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/service_tier",
    "deprecated": false,
    "key": "service_tier",
    "docstring": "Service tier for delegated Responses requests.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/service_tier",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "default"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "fast_tier_temp_pilot"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "flex"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "priority"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "ultrafast"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 0",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 1",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 2",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 3",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 4",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 5"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/text",
    "deprecated": false,
    "key": "text",
    "docstring": "Text generation settings passed to each delegated Responses request.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "verbosity"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text > (property) verbosity"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tool_choice",
    "deprecated": false,
    "key": "tool_choice",
    "docstring": "Controls which tool the Responses backend uses when handling a task delegated by the Live model.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tool_choice",
      "types": [
        {
          "kind": "HttpTypeUnion",
          "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tool_choice/oneOf/0",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "auto"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "none"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "required"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "name"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "name"
            },
            {
              "ident": "server_label"
            },
            {
              "ident": "type"
            }
          ]
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 0",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 1",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tools",
    "deprecated": false,
    "key": "tools",
    "docstring": "Tools available to the Responses backend while it handles tasks delegated by the Live model.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tools",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tools/items",
        "types": [
          {
            "kind": "HttpTypeReference",
            "ident": "FunctionTool",
            "$ref": "(resource) live > (model) function_tool > (schema)"
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              }
            ]
          }
        ]
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools > (items) > (variant) 0",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools > (items) > (variant) 1"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam",
    "docstring": "Updates to the Responses backend of an existing Live session. Omitted settings retain their current values.",
    "ident": "ResponsesDelegationUpdateConfig",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "instructions"
        },
        {
          "ident": "max_output_tokens"
        },
        {
          "ident": "model"
        },
        {
          "ident": "parallel_tool_calls"
        },
        {
          "ident": "reasoning"
        },
        {
          "ident": "service_tier"
        },
        {
          "ident": "text"
        },
        {
          "ident": "tool_choice"
        },
        {
          "ident": "tools"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) instructions",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) max_output_tokens",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) model",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) parallel_tool_calls",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools"
    ]
  },
  "(resource) live > (model) audio_format > (schema) > (variant) 0 > (property) rate": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionAudioFormatPCMParam/properties/rate",
    "deprecated": false,
    "key": "rate",
    "docstring": "Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionAudioFormatPCMParam/properties/rate",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": 16000
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": 24000
        }
      ]
    },
    "constraints": {
      "minimum": 16000,
      "maximum": 24000
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) audio_format > (schema) > (variant) 0 > (property) rate > (member) 0",
      "(resource) live > (model) audio_format > (schema) > (variant) 0 > (property) rate > (member) 1"
    ]
  },
  "(resource) live > (model) audio_format > (schema) > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionAudioFormatPCMParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The audio encoding. Always `audio/pcm`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionAudioFormatPCMParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "audio/pcm"
        }
      ]
    },
    "default": "audio/pcm",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) audio_format > (schema) > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) audio_format > (schema) > (variant) 1 > (property) rate": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionAudioFormatPCMUParam/properties/rate",
    "deprecated": false,
    "key": "rate",
    "docstring": "Audio sample rate in hertz. G.711 audio uses 8000 Hz.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 8000,
      "maximum": 8000
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) audio_format > (schema) > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionAudioFormatPCMUParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The audio encoding. Always `audio/pcmu`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionAudioFormatPCMUParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "audio/pcmu"
        }
      ]
    },
    "default": "audio/pcmu",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) audio_format > (schema) > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) audio_format > (schema) > (variant) 2 > (property) rate": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionAudioFormatPCMAParam/properties/rate",
    "deprecated": false,
    "key": "rate",
    "docstring": "Audio sample rate in hertz. G.711 audio uses 8000 Hz.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 8000,
      "maximum": 8000
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) audio_format > (schema) > (variant) 2 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionAudioFormatPCMAParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The audio encoding. Always `audio/pcma`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionAudioFormatPCMAParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "audio/pcma"
        }
      ]
    },
    "default": "audio/pcma",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) audio_format > (schema) > (variant) 2 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) data_channel_config > (schema) > (property) allowed_client_events > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveDataChannelConfigParam/properties/allowed_client_events/oneOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveDataChannelConfigParam/properties/allowed_client_events/oneOf/0",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "all"
        }
      ]
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) data_channel_config > (schema) > (property) allowed_client_events > (variant) 0 > (member) 0"
    ]
  },
  "(resource) live > (model) data_channel_config > (schema) > (property) allowed_client_events > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveDataChannelConfigParam/properties/allowed_client_events/oneOf/1",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/LiveDataChannelConfigParam/properties/allowed_client_events/oneOf/1",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "children": []
  },
  "(resource) live > (model) data_channel_config > (schema) > (property) allowed_server_events > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveDataChannelConfigParam/properties/allowed_server_events/oneOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveDataChannelConfigParam/properties/allowed_server_events/oneOf/0",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "all"
        }
      ]
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) data_channel_config > (schema) > (property) allowed_server_events > (variant) 0 > (member) 0"
    ]
  },
  "(resource) live > (model) data_channel_config > (schema) > (property) allowed_server_events > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveDataChannelConfigParam/properties/allowed_server_events/oneOf/1",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/LiveDataChannelConfigParam/properties/allowed_server_events/oneOf/1",
      "elementType": {
        "kind": "HttpTypeReference",
        "ident": "ServerEventSelector",
        "$ref": "(resource) live > (model) server_event_selector > (schema)"
      }
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) server_event_selector > (schema) > (property) type",
      "(resource) live > (model) server_event_selector > (schema) > (property) response_event"
    ]
  },
  "(resource) live > (model) server_event_selector > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveAllowedServerEventParam",
    "docstring": "A Live server event selector for the WebRTC frontend data channel.",
    "ident": "ServerEventSelector",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "response_event"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) server_event_selector > (schema) > (property) type",
      "(resource) live > (model) server_event_selector > (schema) > (property) response_event"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveDelegationReasoningInputParam/properties/effort",
    "deprecated": false,
    "key": "effort",
    "docstring": "How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveDelegationReasoningInputParam/properties/effort",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "none"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "minimal"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "medium"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "xhigh"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 0",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 1",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 2",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 3",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 4",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 5"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) summary": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveDelegationReasoningInputParam/properties/summary",
    "deprecated": false,
    "key": "summary",
    "docstring": "The reasoning summary to request from the delegated Responses model, when supported.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveDelegationReasoningInputParam/properties/summary",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "concise"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "detailed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) summary > (member) 0",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) summary > (member) 1",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) summary > (member) 2"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "default"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "fast_tier_temp_pilot"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "flex"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "priority"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "ultrafast"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text > (property) verbosity": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveDelegationTextInputParam/properties/verbosity",
    "deprecated": false,
    "key": "verbosity",
    "docstring": "The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveDelegationTextInputParam/properties/verbosity",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "medium"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text > (property) verbosity > (member) 0",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text > (property) verbosity > (member) 1",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text > (property) verbosity > (member) 2"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tool_choice/oneOf/0",
    "ident": "LiveToolChoiceEnum",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tool_choice/oneOf/0",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "none"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "required"
        }
      ]
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 0 > (member) 0",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 0 > (member) 1",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 0 > (member) 2"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tool_choice/oneOf/1",
    "ident": "LiveFunctionToolChoiceParam",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 1 > (property) name",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tool_choice/oneOf/2",
    "ident": "LiveMCPToolChoiceParam",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        },
        {
          "ident": "server_label"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2 > (property) name",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2 > (property) server_label",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2 > (property) type"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools > (items) > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "FunctionTool",
      "$ref": "(resource) live > (model) function_tool > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) function_tool > (schema) > (property) name",
      "(resource) live > (model) function_tool > (schema) > (property) type",
      "(resource) live > (model) function_tool > (schema) > (property) description",
      "(resource) live > (model) function_tool > (schema) > (property) parameters",
      "(resource) live > (model) function_tool > (schema) > (property) strict"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools > (items) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tools/items/oneOf/1",
    "docstring": "A web search tool available to the Live session’s Responses backend.",
    "ident": "WebSearch",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools > (items) > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) function_tool > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveFunctionToolInputParam",
    "docstring": "A function tool available to the Responses backend when the Live model delegates a task.",
    "ident": "FunctionTool",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        },
        {
          "ident": "type"
        },
        {
          "ident": "description"
        },
        {
          "ident": "parameters"
        },
        {
          "ident": "strict"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) function_tool > (schema) > (property) name",
      "(resource) live > (model) function_tool > (schema) > (property) type",
      "(resource) live > (model) function_tool > (schema) > (property) description",
      "(resource) live > (model) function_tool > (schema) > (property) parameters",
      "(resource) live > (model) function_tool > (schema) > (property) strict"
    ]
  },
  "(resource) live > (model) audio_format > (schema) > (variant) 0 > (property) rate > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": 16000
    }
  },
  "(resource) live > (model) audio_format > (schema) > (variant) 0 > (property) rate > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": 24000
    }
  },
  "(resource) live > (model) audio_format > (schema) > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "audio/pcm"
    }
  },
  "(resource) live > (model) audio_format > (schema) > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "audio/pcmu"
    }
  },
  "(resource) live > (model) audio_format > (schema) > (variant) 2 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "audio/pcma"
    }
  },
  "(resource) live > (model) data_channel_config > (schema) > (property) allowed_client_events > (variant) 0 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "all"
    }
  },
  "(resource) live > (model) data_channel_config > (schema) > (property) allowed_server_events > (variant) 0 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "all"
    }
  },
  "(resource) live > (model) server_event_selector > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveAllowedServerEventParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The outer Live server event type. Use 'response.event' for Responses events.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 256
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) server_event_selector > (schema) > (property) response_event": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveAllowedServerEventParam/properties/response_event",
    "deprecated": false,
    "key": "response_event",
    "docstring": "The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 256
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "none"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "minimal"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "medium"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "xhigh"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) summary > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "concise"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) summary > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "detailed"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) summary > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text > (property) verbosity > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text > (property) verbosity > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "medium"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text > (property) verbosity > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 0 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 0 > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "none"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 0 > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "required"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 1 > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveFunctionToolChoiceParam/properties/name",
    "deprecated": false,
    "key": "name",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveFunctionToolChoiceParam/properties/type",
    "deprecated": false,
    "key": "type",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveFunctionToolChoiceParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function"
        }
      ]
    },
    "default": "function",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2 > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveMCPToolChoiceParam/properties/name",
    "deprecated": false,
    "key": "name",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2 > (property) server_label": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveMCPToolChoiceParam/properties/server_label",
    "deprecated": false,
    "key": "server_label",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveMCPToolChoiceParam/properties/type",
    "deprecated": false,
    "key": "type",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveMCPToolChoiceParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "mcp"
        }
      ]
    },
    "default": "mcp",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) function_tool > (schema) > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveFunctionToolInputParam/properties/name",
    "deprecated": false,
    "key": "name",
    "docstring": "The name the delegated Responses model uses when calling this function.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) function_tool > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveFunctionToolInputParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The tool type. Always `function`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveFunctionToolInputParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function"
        }
      ]
    },
    "default": "function",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) function_tool > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) function_tool > (schema) > (property) description": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveFunctionToolInputParam/properties/description",
    "deprecated": false,
    "key": "description",
    "docstring": "What the function does and when the delegated Responses model should call it.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) function_tool > (schema) > (property) parameters": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveFunctionToolInputParam/properties/parameters",
    "deprecated": false,
    "key": "parameters",
    "docstring": "A JSON Schema object describing the arguments accepted by the function.",
    "type": {
      "kind": "HttpTypeReference",
      "oasRef": "#/components/schemas/LiveFunctionToolInputParam/properties/parameters",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnknown"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "map",
    "children": []
  },
  "(resource) live > (model) function_tool > (schema) > (property) strict": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveFunctionToolInputParam/properties/strict",
    "deprecated": false,
    "key": "strict",
    "docstring": "Whether the delegated Responses model must follow the function’s parameter schema exactly.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools > (items) > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveWebSearchToolInputParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The tool type. Always `web_search`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveWebSearchToolInputParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "web_search"
        }
      ]
    },
    "default": "web_search",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools > (items) > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mcp"
    }
  },
  "(resource) live > (model) function_tool > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools > (items) > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "web_search"
    }
  }
}
```

#### Example

```json
{
  "type": "session.start",
  "session": {}
}
```

### session.update

Update the delegation settings of an active Live session. The server acknowledges accepted changes with `session.updated`.

#### Schema

Schema name: `LiveSessionUpdateParam`

```json
{
  "(resource) live > (model) session_update_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveSessionUpdateParam",
    "docstring": "Update the delegation settings of an active Live session. The server acknowledges accepted changes with `session.updated`.",
    "ident": "SessionUpdateEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "session"
        },
        {
          "ident": "type"
        },
        {
          "ident": "event_id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_update_event > (schema) > (property) session",
      "(resource) live > (model) session_update_event > (schema) > (property) type",
      "(resource) live > (model) session_update_event > (schema) > (property) event_id"
    ]
  },
  "(resource) live > (model) session_update_event > (schema) > (property) session": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionUpdateParam/properties/session",
    "deprecated": false,
    "key": "session",
    "docstring": "Sparse delegation updates. Omitted settings retain their values. The delegation type cannot change, including resetting Responses delegation to null or client. Model, frontend instructions, audio, and startup input are immutable.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "SessionUpdateConfig",
      "$ref": "(resource) live > (model) session_update_config > (schema)"
    },
    "optional": false,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "object",
    "modelPath": "(resource) live > (model) session_update_config",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_update_config > (schema) > (property) delegation"
    ]
  },
  "(resource) live > (model) session_update_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionUpdateParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The Live client event type. Always `session.update`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionUpdateParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.update"
        }
      ]
    },
    "default": "session.update",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) session_update_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) session_update_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionUpdateParam/properties/event_id",
    "deprecated": false,
    "key": "event_id",
    "docstring": "Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 512
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) session_update_config > (schema) > (property) delegation": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionUpdateParams/properties/delegation",
    "deprecated": false,
    "key": "delegation",
    "docstring": "Delegation settings to update. The delegation type must match the current session; omitted settings retain their values.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionUpdateParams/properties/delegation",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "ClientDelegation",
          "$ref": "(resource) live > (model) client_delegation > (schema)"
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            },
            {
              "ident": "responses"
            }
          ]
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) session_update_config > (schema) > (property) delegation > (variant) 0",
      "(resource) live > (model) session_update_config > (schema) > (property) delegation > (variant) 1"
    ]
  },
  "(resource) live > (model) session_update_config > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveSessionUpdateParams",
    "docstring": "Changes to an active Live session. Only delegation backend settings can be updated after startup.",
    "ident": "SessionUpdateConfig",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "delegation"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_update_config > (schema) > (property) delegation"
    ]
  },
  "(resource) live > (model) session_update_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.update"
    }
  },
  "(resource) live > (model) session_update_config > (schema) > (property) delegation > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ClientDelegation",
      "$ref": "(resource) live > (model) client_delegation > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) client_delegation > (schema) > (property) type"
    ]
  },
  "(resource) live > (model) session_update_config > (schema) > (property) delegation > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveSessionUpdateParams/properties/delegation/anyOf/0/oneOf/1",
    "docstring": "Update the Responses backend for an existing Live session without changing delegation ownership.",
    "ident": "Responses",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "responses"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_update_config > (schema) > (property) delegation > (variant) 1 > (property) type",
      "(resource) live > (model) session_update_config > (schema) > (property) delegation > (variant) 1 > (property) responses"
    ]
  },
  "(resource) live > (model) client_delegation > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveClientDelegationParam",
    "docstring": "Delegate tasks to your application. The Live session emits delegation events that your backend handles.",
    "ident": "ClientDelegation",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) client_delegation > (schema) > (property) type"
    ]
  },
  "(resource) live > (model) client_delegation > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveClientDelegationParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The delegation owner. Always `client` for tasks handled by your application.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveClientDelegationParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "client"
        }
      ]
    },
    "default": "client",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) client_delegation > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) session_update_config > (schema) > (property) delegation > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationUpdateParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The delegation owner. Always `responses` for tasks handled by the Responses API.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveResponsesDelegationUpdateParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "responses"
        }
      ]
    },
    "default": "responses",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) session_update_config > (schema) > (property) delegation > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) session_update_config > (schema) > (property) delegation > (variant) 1 > (property) responses": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationUpdateParam/properties/responses",
    "deprecated": false,
    "key": "responses",
    "docstring": "Responses backend settings to update. Omitted settings keep their existing values.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponsesDelegationUpdateConfig",
      "$ref": "(resource) live > (model) responses_delegation_update_config > (schema)"
    },
    "optional": true,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "object",
    "modelPath": "(resource) live > (model) responses_delegation_update_config",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) instructions",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) max_output_tokens",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) model",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) parallel_tool_calls",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools"
    ]
  },
  "(resource) live > (model) client_delegation > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "client"
    }
  },
  "(resource) live > (model) session_update_config > (schema) > (property) delegation > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "responses"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) instructions": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/instructions",
    "deprecated": false,
    "key": "instructions",
    "docstring": "Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) max_output_tokens": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/max_output_tokens",
    "deprecated": false,
    "key": "max_output_tokens",
    "docstring": "Maximum number of output tokens for each delegated response.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 16
    },
    "optional": true,
    "nullable": true,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) model": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/model",
    "deprecated": false,
    "key": "model",
    "docstring": "The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) parallel_tool_calls": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/parallel_tool_calls",
    "deprecated": false,
    "key": "parallel_tool_calls",
    "docstring": "Whether the delegated Responses model may request multiple tool calls in a single response.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/reasoning",
    "deprecated": false,
    "key": "reasoning",
    "docstring": "Reasoning settings passed to each delegated Responses request.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "effort"
        },
        {
          "ident": "summary"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) summary"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/service_tier",
    "deprecated": false,
    "key": "service_tier",
    "docstring": "Service tier for delegated Responses requests.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/service_tier",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "default"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "fast_tier_temp_pilot"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "flex"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "priority"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "ultrafast"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 0",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 1",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 2",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 3",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 4",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 5"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/text",
    "deprecated": false,
    "key": "text",
    "docstring": "Text generation settings passed to each delegated Responses request.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "verbosity"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text > (property) verbosity"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tool_choice",
    "deprecated": false,
    "key": "tool_choice",
    "docstring": "Controls which tool the Responses backend uses when handling a task delegated by the Live model.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tool_choice",
      "types": [
        {
          "kind": "HttpTypeUnion",
          "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tool_choice/oneOf/0",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "auto"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "none"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "required"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "name"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "name"
            },
            {
              "ident": "server_label"
            },
            {
              "ident": "type"
            }
          ]
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 0",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 1",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tools",
    "deprecated": false,
    "key": "tools",
    "docstring": "Tools available to the Responses backend while it handles tasks delegated by the Live model.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tools",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tools/items",
        "types": [
          {
            "kind": "HttpTypeReference",
            "ident": "FunctionTool",
            "$ref": "(resource) live > (model) function_tool > (schema)"
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              }
            ]
          }
        ]
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools > (items) > (variant) 0",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools > (items) > (variant) 1"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam",
    "docstring": "Updates to the Responses backend of an existing Live session. Omitted settings retain their current values.",
    "ident": "ResponsesDelegationUpdateConfig",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "instructions"
        },
        {
          "ident": "max_output_tokens"
        },
        {
          "ident": "model"
        },
        {
          "ident": "parallel_tool_calls"
        },
        {
          "ident": "reasoning"
        },
        {
          "ident": "service_tier"
        },
        {
          "ident": "text"
        },
        {
          "ident": "tool_choice"
        },
        {
          "ident": "tools"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) instructions",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) max_output_tokens",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) model",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) parallel_tool_calls",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveDelegationReasoningInputParam/properties/effort",
    "deprecated": false,
    "key": "effort",
    "docstring": "How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveDelegationReasoningInputParam/properties/effort",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "none"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "minimal"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "medium"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "xhigh"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 0",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 1",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 2",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 3",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 4",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 5"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) summary": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveDelegationReasoningInputParam/properties/summary",
    "deprecated": false,
    "key": "summary",
    "docstring": "The reasoning summary to request from the delegated Responses model, when supported.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveDelegationReasoningInputParam/properties/summary",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "concise"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "detailed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) summary > (member) 0",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) summary > (member) 1",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) summary > (member) 2"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "default"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "fast_tier_temp_pilot"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "flex"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "priority"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) service_tier > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "ultrafast"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text > (property) verbosity": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveDelegationTextInputParam/properties/verbosity",
    "deprecated": false,
    "key": "verbosity",
    "docstring": "The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveDelegationTextInputParam/properties/verbosity",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "medium"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text > (property) verbosity > (member) 0",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text > (property) verbosity > (member) 1",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text > (property) verbosity > (member) 2"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tool_choice/oneOf/0",
    "ident": "LiveToolChoiceEnum",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tool_choice/oneOf/0",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "none"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "required"
        }
      ]
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 0 > (member) 0",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 0 > (member) 1",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 0 > (member) 2"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tool_choice/oneOf/1",
    "ident": "LiveFunctionToolChoiceParam",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 1 > (property) name",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tool_choice/oneOf/2",
    "ident": "LiveMCPToolChoiceParam",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        },
        {
          "ident": "server_label"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2 > (property) name",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2 > (property) server_label",
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2 > (property) type"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools > (items) > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "FunctionTool",
      "$ref": "(resource) live > (model) function_tool > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) function_tool > (schema) > (property) name",
      "(resource) live > (model) function_tool > (schema) > (property) type",
      "(resource) live > (model) function_tool > (schema) > (property) description",
      "(resource) live > (model) function_tool > (schema) > (property) parameters",
      "(resource) live > (model) function_tool > (schema) > (property) strict"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools > (items) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsUpdateInputParam/properties/tools/items/oneOf/1",
    "docstring": "A web search tool available to the Live session’s Responses backend.",
    "ident": "WebSearch",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools > (items) > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) function_tool > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveFunctionToolInputParam",
    "docstring": "A function tool available to the Responses backend when the Live model delegates a task.",
    "ident": "FunctionTool",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        },
        {
          "ident": "type"
        },
        {
          "ident": "description"
        },
        {
          "ident": "parameters"
        },
        {
          "ident": "strict"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) function_tool > (schema) > (property) name",
      "(resource) live > (model) function_tool > (schema) > (property) type",
      "(resource) live > (model) function_tool > (schema) > (property) description",
      "(resource) live > (model) function_tool > (schema) > (property) parameters",
      "(resource) live > (model) function_tool > (schema) > (property) strict"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "none"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "minimal"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "medium"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) effort > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "xhigh"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) summary > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "concise"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) summary > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "detailed"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) reasoning > (property) summary > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text > (property) verbosity > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text > (property) verbosity > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "medium"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) text > (property) verbosity > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 0 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 0 > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "none"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 0 > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "required"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 1 > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveFunctionToolChoiceParam/properties/name",
    "deprecated": false,
    "key": "name",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveFunctionToolChoiceParam/properties/type",
    "deprecated": false,
    "key": "type",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveFunctionToolChoiceParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function"
        }
      ]
    },
    "default": "function",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2 > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveMCPToolChoiceParam/properties/name",
    "deprecated": false,
    "key": "name",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2 > (property) server_label": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveMCPToolChoiceParam/properties/server_label",
    "deprecated": false,
    "key": "server_label",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveMCPToolChoiceParam/properties/type",
    "deprecated": false,
    "key": "type",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveMCPToolChoiceParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "mcp"
        }
      ]
    },
    "default": "mcp",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) function_tool > (schema) > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveFunctionToolInputParam/properties/name",
    "deprecated": false,
    "key": "name",
    "docstring": "The name the delegated Responses model uses when calling this function.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) function_tool > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveFunctionToolInputParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The tool type. Always `function`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveFunctionToolInputParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function"
        }
      ]
    },
    "default": "function",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) function_tool > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) function_tool > (schema) > (property) description": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveFunctionToolInputParam/properties/description",
    "deprecated": false,
    "key": "description",
    "docstring": "What the function does and when the delegated Responses model should call it.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) function_tool > (schema) > (property) parameters": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveFunctionToolInputParam/properties/parameters",
    "deprecated": false,
    "key": "parameters",
    "docstring": "A JSON Schema object describing the arguments accepted by the function.",
    "type": {
      "kind": "HttpTypeReference",
      "oasRef": "#/components/schemas/LiveFunctionToolInputParam/properties/parameters",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnknown"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "map",
    "children": []
  },
  "(resource) live > (model) function_tool > (schema) > (property) strict": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveFunctionToolInputParam/properties/strict",
    "deprecated": false,
    "key": "strict",
    "docstring": "Whether the delegated Responses model must follow the function’s parameter schema exactly.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools > (items) > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveWebSearchToolInputParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The tool type. Always `web_search`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveWebSearchToolInputParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "web_search"
        }
      ]
    },
    "default": "web_search",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools > (items) > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tool_choice > (variant) 2 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mcp"
    }
  },
  "(resource) live > (model) function_tool > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function"
    }
  },
  "(resource) live > (model) responses_delegation_update_config > (schema) > (property) tools > (items) > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "web_search"
    }
  }
}
```

#### Example

```json
{
  "type": "session.update",
  "event_id": "evt_update_001",
  "session": {
    "delegation": {
      "type": "responses",
      "responses": {
        "instructions": "Check restaurant availability. Ask before confirming a booking.",
        "max_output_tokens": 1024
      }
    }
  }
}
```

### session.input_audio.append

Send audio to a Live session over its primary WebSocket. WebRTC and SIP sessions send audio over their media transport.

#### Schema

Schema name: `LiveInputAudioAppendEvent`

```json
{
  "(resource) live > (model) input_audio_append_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInputAudioAppendEvent",
    "docstring": "Send audio to a Live session over its primary WebSocket. WebRTC and SIP sessions send audio over their media transport.",
    "ident": "InputAudioAppendEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "audio"
        },
        {
          "ident": "type"
        },
        {
          "ident": "event_id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) input_audio_append_event > (schema) > (property) audio",
      "(resource) live > (model) input_audio_append_event > (schema) > (property) type",
      "(resource) live > (model) input_audio_append_event > (schema) > (property) event_id"
    ]
  },
  "(resource) live > (model) input_audio_append_event > (schema) > (property) audio": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputAudioAppendEvent/properties/audio",
    "deprecated": false,
    "key": "audio",
    "docstring": "Base64-encoded raw audio in the startup-selected format, without a WAV or other container header. Primary WebSocket only; media transports use their audio track. Audio appends have no acknowledgment. Reflected sideband server events reuse this event type and audio key, with no timestamps or event_id; their audio is always mono PCM16LE at 24 kHz.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) input_audio_append_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputAudioAppendEvent/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The Live client event type. Always `session.input_audio.append`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInputAudioAppendEvent/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.input_audio.append"
        }
      ]
    },
    "default": "session.input_audio.append",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) input_audio_append_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) input_audio_append_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputAudioAppendEvent/properties/event_id",
    "deprecated": false,
    "key": "event_id",
    "docstring": "Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 512
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) input_audio_append_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.input_audio.append"
    }
  }
}
```

#### Example

```json
{
  "type": "session.input_audio.append",
  "audio": "AACAAIAAAIAAAP9/AIAAgA=="
}
```

### session.input_audio.mute

Mute audio input to the Live model without closing the session. The server acknowledges with `session.input_audio.muted`.

#### Schema

Schema name: `LiveInputAudioMuteParam`

```json
{
  "(resource) live > (model) input_audio_mute_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInputAudioMuteParam",
    "docstring": "Mute audio input to the Live model without closing the session. The server acknowledges with `session.input_audio.muted`.",
    "ident": "InputAudioMuteEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "event_id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) input_audio_mute_event > (schema) > (property) type",
      "(resource) live > (model) input_audio_mute_event > (schema) > (property) event_id"
    ]
  },
  "(resource) live > (model) input_audio_mute_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputAudioMuteParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The Live client event type. Always `session.input_audio.mute`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInputAudioMuteParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.input_audio.mute"
        }
      ]
    },
    "default": "session.input_audio.mute",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) input_audio_mute_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) input_audio_mute_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputAudioMuteParam/properties/event_id",
    "deprecated": false,
    "key": "event_id",
    "docstring": "Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 512
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) input_audio_mute_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.input_audio.mute"
    }
  }
}
```

#### Example

```json
{
  "type": "session.input_audio.mute",
  "event_id": "evt_mute_001"
}
```

### session.input_audio.unmute

Resume audio input to a Live model after muting it. The server acknowledges with `session.input_audio.unmuted`.

#### Schema

Schema name: `LiveInputAudioUnmuteParam`

```json
{
  "(resource) live > (model) input_audio_unmute_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInputAudioUnmuteParam",
    "docstring": "Resume audio input to a Live model after muting it. The server acknowledges with `session.input_audio.unmuted`.",
    "ident": "InputAudioUnmuteEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "event_id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) input_audio_unmute_event > (schema) > (property) type",
      "(resource) live > (model) input_audio_unmute_event > (schema) > (property) event_id"
    ]
  },
  "(resource) live > (model) input_audio_unmute_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputAudioUnmuteParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The Live client event type. Always `session.input_audio.unmute`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInputAudioUnmuteParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.input_audio.unmute"
        }
      ]
    },
    "default": "session.input_audio.unmute",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) input_audio_unmute_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) input_audio_unmute_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputAudioUnmuteParam/properties/event_id",
    "deprecated": false,
    "key": "event_id",
    "docstring": "Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 512
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) input_audio_unmute_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.input_audio.unmute"
    }
  }
}
```

#### Example

```json
{
  "type": "session.input_audio.unmute",
  "event_id": "evt_unmute_001"
}
```

### session.instructions.append

Append instructions to the Live conversation while it is running, optionally associating them with an existing client delegation.

#### Schema

Schema name: `LiveInstructionsAppendParam`

```json
{
  "(resource) live > (model) instructions_append_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInstructionsAppendParam",
    "docstring": "Append instructions to the Live conversation while it is running, optionally associating them with an existing client delegation.",
    "ident": "InstructionsAppendEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "content"
        },
        {
          "ident": "delegation_id"
        },
        {
          "ident": "type"
        },
        {
          "ident": "event_id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) instructions_append_event > (schema) > (property) content",
      "(resource) live > (model) instructions_append_event > (schema) > (property) delegation_id",
      "(resource) live > (model) instructions_append_event > (schema) > (property) type",
      "(resource) live > (model) instructions_append_event > (schema) > (property) event_id"
    ]
  },
  "(resource) live > (model) instructions_append_event > (schema) > (property) content": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInstructionsAppendParam/properties/content",
    "deprecated": false,
    "key": "content",
    "docstring": "Instruction text to append, limited to 500 tokens. This is a plain string, not an array of content parts.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) instructions_append_event > (schema) > (property) delegation_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInstructionsAppendParam/properties/delegation_id",
    "deprecated": false,
    "key": "delegation_id",
    "docstring": "Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1
    },
    "optional": false,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) instructions_append_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInstructionsAppendParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The Live client event type. Always `session.instructions.append`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInstructionsAppendParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.instructions.append"
        }
      ]
    },
    "default": "session.instructions.append",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) instructions_append_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) instructions_append_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInstructionsAppendParam/properties/event_id",
    "deprecated": false,
    "key": "event_id",
    "docstring": "Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 512
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) instructions_append_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.instructions.append"
    }
  }
}
```

#### Example

```json
{
  "type": "session.instructions.append",
  "event_id": "evt_instructions_001",
  "delegation_id": null,
  "content": "The caller prefers outdoor seating."
}
```

### session.thinking.append

Provide silent reasoning or progress context to the Live model, optionally for an existing client delegation.

#### Schema

Schema name: `LiveThinkingAppendParam`

```json
{
  "(resource) live > (model) thinking_append_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveThinkingAppendParam",
    "docstring": "Provide silent reasoning or progress context to the Live model, optionally for an existing client delegation.",
    "ident": "ThinkingAppendEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "content"
        },
        {
          "ident": "delegation_id"
        },
        {
          "ident": "type"
        },
        {
          "ident": "event_id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) thinking_append_event > (schema) > (property) content",
      "(resource) live > (model) thinking_append_event > (schema) > (property) delegation_id",
      "(resource) live > (model) thinking_append_event > (schema) > (property) type",
      "(resource) live > (model) thinking_append_event > (schema) > (property) event_id"
    ]
  },
  "(resource) live > (model) thinking_append_event > (schema) > (property) content": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveThinkingAppendParam/properties/content",
    "deprecated": false,
    "key": "content",
    "docstring": "Silent reasoning or progress context, limited to 500 tokens. It does not directly request speech, but can influence later speech and is not a secrecy boundary.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) thinking_append_event > (schema) > (property) delegation_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveThinkingAppendParam/properties/delegation_id",
    "deprecated": false,
    "key": "delegation_id",
    "docstring": "Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1
    },
    "optional": false,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) thinking_append_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveThinkingAppendParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The Live client event type. Always `session.thinking.append`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveThinkingAppendParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.thinking.append"
        }
      ]
    },
    "default": "session.thinking.append",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) thinking_append_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) thinking_append_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveThinkingAppendParam/properties/event_id",
    "deprecated": false,
    "key": "event_id",
    "docstring": "Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 512
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) thinking_append_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.thinking.append"
    }
  }
}
```

#### Example

```json
{
  "type": "session.thinking.append",
  "event_id": "evt_thinking_001",
  "delegation_id": "del_abc123",
  "content": "Checking availability for two guests at 7 PM."
}
```

### session.commentary.append

Provide context the Live model can communicate to the user, optionally for an existing client delegation.

#### Schema

Schema name: `LiveCommentaryAppendParam`

```json
{
  "(resource) live > (model) commentary_append_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveCommentaryAppendParam",
    "docstring": "Provide context the Live model can communicate to the user, optionally for an existing client delegation.",
    "ident": "CommentaryAppendEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "content"
        },
        {
          "ident": "delegation_id"
        },
        {
          "ident": "type"
        },
        {
          "ident": "event_id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) commentary_append_event > (schema) > (property) content",
      "(resource) live > (model) commentary_append_event > (schema) > (property) delegation_id",
      "(resource) live > (model) commentary_append_event > (schema) > (property) type",
      "(resource) live > (model) commentary_append_event > (schema) > (property) event_id"
    ]
  },
  "(resource) live > (model) commentary_append_event > (schema) > (property) content": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveCommentaryAppendParam/properties/content",
    "deprecated": false,
    "key": "content",
    "docstring": "Speakable context for the Live model, limited to 500 tokens. Use this for a result the model should communicate; use session.thinking.append for silent context.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) commentary_append_event > (schema) > (property) delegation_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveCommentaryAppendParam/properties/delegation_id",
    "deprecated": false,
    "key": "delegation_id",
    "docstring": "Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1
    },
    "optional": false,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) commentary_append_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveCommentaryAppendParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The Live client event type. Always `session.commentary.append`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveCommentaryAppendParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.commentary.append"
        }
      ]
    },
    "default": "session.commentary.append",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) commentary_append_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) commentary_append_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveCommentaryAppendParam/properties/event_id",
    "deprecated": false,
    "key": "event_id",
    "docstring": "Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 512
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) commentary_append_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.commentary.append"
    }
  }
}
```

#### Example

```json
{
  "type": "session.commentary.append",
  "event_id": "evt_commentary_001",
  "delegation_id": "del_abc123",
  "content": "There is an outdoor table for two at 7 PM. Ask whether to reserve it."
}
```

### response.item.create

Add an input item to the Live session’s Responses backend. Requires Responses delegation; use `response.create` to request a response.

#### Schema

Schema name: `LiveResponseItemCreateParam`

```json
{
  "(resource) live > (model) response_item_create_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponseItemCreateParam",
    "docstring": "Add an input item to the Live session’s Responses backend. Requires Responses delegation; use `response.create` to request a response.",
    "ident": "ResponseItemCreateEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "item"
        },
        {
          "ident": "type"
        },
        {
          "ident": "event_id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item",
      "(resource) live > (model) response_item_create_event > (schema) > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) event_id"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponseItemCreateParam/properties/item",
    "deprecated": false,
    "key": "item",
    "docstring": "An input item to append to the Responses backend conversation, such as a user message or a function tool result.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveResponseItemCreateParam/properties/item",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "EasyInputMessage",
          "$ref": "(resource) responses > (model) easy_input_message > (schema)"
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "content"
            },
            {
              "ident": "role"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ResponseOutputMessage",
          "$ref": "(resource) responses > (model) response_output_message > (schema)"
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "queries"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            },
            {
              "ident": "results"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "pending_safety_checks"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            },
            {
              "ident": "action"
            },
            {
              "ident": "actions"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "call_id"
            },
            {
              "ident": "output"
            },
            {
              "ident": "type"
            },
            {
              "ident": "id"
            },
            {
              "ident": "acknowledged_safety_checks"
            },
            {
              "ident": "status"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "action"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "arguments"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "name"
            },
            {
              "ident": "type"
            },
            {
              "ident": "id"
            },
            {
              "ident": "async"
            },
            {
              "ident": "caller"
            },
            {
              "ident": "namespace"
            },
            {
              "ident": "status"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "output"
            },
            {
              "ident": "type"
            },
            {
              "ident": "id"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "caller"
            },
            {
              "ident": "name"
            },
            {
              "ident": "namespace"
            },
            {
              "ident": "status"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "arguments"
            },
            {
              "ident": "type"
            },
            {
              "ident": "id"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "execution"
            },
            {
              "ident": "status"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "tools"
            },
            {
              "ident": "type"
            },
            {
              "ident": "id"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "execution"
            },
            {
              "ident": "status"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "role"
            },
            {
              "ident": "tools"
            },
            {
              "ident": "type"
            },
            {
              "ident": "id"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            },
            {
              "ident": "id"
            },
            {
              "ident": "reasoning"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "summary"
            },
            {
              "ident": "type"
            },
            {
              "ident": "content"
            },
            {
              "ident": "encrypted_content"
            },
            {
              "ident": "status"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "encrypted_content"
            },
            {
              "ident": "type"
            },
            {
              "ident": "id"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "result"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            },
            {
              "ident": "action"
            },
            {
              "ident": "background"
            },
            {
              "ident": "output_format"
            },
            {
              "ident": "quality"
            },
            {
              "ident": "revised_prompt"
            },
            {
              "ident": "size"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "code"
            },
            {
              "ident": "container_id"
            },
            {
              "ident": "outputs"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "action"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "output"
            },
            {
              "ident": "type"
            },
            {
              "ident": "status"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "action"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "type"
            },
            {
              "ident": "id"
            },
            {
              "ident": "caller"
            },
            {
              "ident": "environment"
            },
            {
              "ident": "status"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "call_id"
            },
            {
              "ident": "output"
            },
            {
              "ident": "type"
            },
            {
              "ident": "id"
            },
            {
              "ident": "caller"
            },
            {
              "ident": "max_output_length"
            },
            {
              "ident": "status"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "call_id"
            },
            {
              "ident": "operation"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            },
            {
              "ident": "id"
            },
            {
              "ident": "caller"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "call_id"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            },
            {
              "ident": "id"
            },
            {
              "ident": "caller"
            },
            {
              "ident": "output"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "server_label"
            },
            {
              "ident": "tools"
            },
            {
              "ident": "type"
            },
            {
              "ident": "error"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "arguments"
            },
            {
              "ident": "name"
            },
            {
              "ident": "server_label"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "approval_request_id"
            },
            {
              "ident": "approve"
            },
            {
              "ident": "type"
            },
            {
              "ident": "id"
            },
            {
              "ident": "reason"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "arguments"
            },
            {
              "ident": "name"
            },
            {
              "ident": "server_label"
            },
            {
              "ident": "type"
            },
            {
              "ident": "approval_request_id"
            },
            {
              "ident": "error"
            },
            {
              "ident": "output"
            },
            {
              "ident": "status"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "call_id"
            },
            {
              "ident": "output"
            },
            {
              "ident": "type"
            },
            {
              "ident": "id"
            },
            {
              "ident": "caller"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "call_id"
            },
            {
              "ident": "input"
            },
            {
              "ident": "name"
            },
            {
              "ident": "type"
            },
            {
              "ident": "id"
            },
            {
              "ident": "async"
            },
            {
              "ident": "caller"
            },
            {
              "ident": "namespace"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            },
            {
              "ident": "id"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "code"
            },
            {
              "ident": "fingerprint"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "id"
            },
            {
              "ident": "call_id"
            },
            {
              "ident": "result"
            },
            {
              "ident": "status"
            },
            {
              "ident": "type"
            }
          ]
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 12",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 14",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 24",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 25",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 29",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 30",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 31",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponseItemCreateParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The Live client event type. Always `response.item.create`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveResponseItemCreateParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "response.item.create"
        }
      ]
    },
    "default": "response.item.create",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponseItemCreateParam/properties/event_id",
    "deprecated": false,
    "key": "event_id",
    "docstring": "Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 512
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "EasyInputMessage",
      "$ref": "(resource) responses > (model) easy_input_message > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) easy_input_message > (schema) > (property) content",
      "(resource) responses > (model) easy_input_message > (schema) > (property) role",
      "(resource) responses > (model) easy_input_message > (schema) > (property) phase",
      "(resource) responses > (model) easy_input_message > (schema) > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/0",
    "docstring": "A message input to the model with a role indicating instruction following\nhierarchy. Instructions given with the `developer` or `system` role take\nprecedence over instructions given with the `user` role.\n",
    "ident": "Message",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "content"
        },
        {
          "ident": "role"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) content",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) role",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) status",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseOutputMessage",
      "$ref": "(resource) responses > (model) response_output_message > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_message > (schema) > (property) id",
      "(resource) responses > (model) response_output_message > (schema) > (property) content",
      "(resource) responses > (model) response_output_message > (schema) > (property) role",
      "(resource) responses > (model) response_output_message > (schema) > (property) status",
      "(resource) responses > (model) response_output_message > (schema) > (property) type",
      "(resource) responses > (model) response_output_message > (schema) > (property) phase"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/2",
    "docstring": "The results of a file search tool call. See the\n[file search guide](/api/docs/guides/tools-file-search) for more information.\n",
    "ident": "FileSearchCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "queries"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        },
        {
          "ident": "results"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) queries",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) status",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/3",
    "docstring": "A tool call to a computer use tool. See the\n[computer use guide](/api/docs/guides/tools-computer-use) for more information.\n",
    "ident": "ComputerCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "pending_safety_checks"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        },
        {
          "ident": "action"
        },
        {
          "ident": "actions"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) call_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) pending_safety_checks",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) status",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) action",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) actions"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/4",
    "docstring": "The output of a computer tool call.",
    "ident": "ComputerCallOutput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "call_id"
        },
        {
          "ident": "output"
        },
        {
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "acknowledged_safety_checks"
        },
        {
          "ident": "status"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) call_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) output",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) acknowledged_safety_checks",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) status"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/5",
    "docstring": "The results of a web search tool call. See the\n[web search guide](/api/docs/guides/tools-web-search) for more information.\n",
    "ident": "WebSearchCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "action"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) status",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/6",
    "docstring": "A tool call to run a function. See the\n[function calling guide](/api/docs/guides/function-calling) for more information.\n",
    "ident": "FunctionCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "arguments"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "name"
        },
        {
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "async"
        },
        {
          "ident": "caller"
        },
        {
          "ident": "namespace"
        },
        {
          "ident": "status"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) arguments",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) call_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) name",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) async",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) caller",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) namespace",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) status"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/7",
    "docstring": "The output of a function tool call.",
    "ident": "FunctionCallOutput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "output"
        },
        {
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "caller"
        },
        {
          "ident": "name"
        },
        {
          "ident": "namespace"
        },
        {
          "ident": "status"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) output",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) call_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) caller",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) name",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) namespace",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) status"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/8",
    "ident": "ToolSearchCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "arguments"
        },
        {
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "execution"
        },
        {
          "ident": "status"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) arguments",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) call_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) execution",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) status"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/9",
    "ident": "ToolSearchOutput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "tools"
        },
        {
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "execution"
        },
        {
          "ident": "status"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) call_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) execution",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) status"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/10",
    "ident": "AdditionalTools",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "role"
        },
        {
          "ident": "tools"
        },
        {
          "ident": "type"
        },
        {
          "ident": "id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) role",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) id"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 12": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/11",
    "docstring": "An update to the conversation's response configuration. The configuration\nremains in effect for subsequent responses until it is replaced by another\nconfiguration update.\n",
    "ident": "ConfigurationUpdate",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "reasoning"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 12 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 12 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 12 > (property) reasoning"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/12",
    "docstring": "A description of the chain of thought used by a reasoning model while generating\na response. Be sure to include these items in your `input` to the Responses API\nfor subsequent turns of a conversation if you are manually\n[managing context](/api/docs/guides/conversation-state).\n",
    "ident": "Reasoning",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "summary"
        },
        {
          "ident": "type"
        },
        {
          "ident": "content"
        },
        {
          "ident": "encrypted_content"
        },
        {
          "ident": "status"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) summary",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) content",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) encrypted_content",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) status"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 14": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/13",
    "docstring": "A compaction item generated by the [`v1/responses/compact` API](/api/reference/resources/responses/methods/compact).",
    "ident": "Compaction",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "encrypted_content"
        },
        {
          "ident": "type"
        },
        {
          "ident": "id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 14 > (property) encrypted_content",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 14 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 14 > (property) id"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/14",
    "docstring": "An image generation request made by the model.",
    "ident": "ImageGenerationCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "result"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        },
        {
          "ident": "action"
        },
        {
          "ident": "background"
        },
        {
          "ident": "output_format"
        },
        {
          "ident": "quality"
        },
        {
          "ident": "revised_prompt"
        },
        {
          "ident": "size"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) result",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) status",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) action",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) background",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) output_format",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) quality",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) revised_prompt",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) size"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/15",
    "docstring": "A tool call to run code.\n",
    "ident": "CodeInterpreterCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "code"
        },
        {
          "ident": "container_id"
        },
        {
          "ident": "outputs"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) code",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) container_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) outputs",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) status",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/16",
    "docstring": "A tool call to run a command on the local shell.\n",
    "ident": "LocalShellCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "action"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) action",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) call_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) status",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/17",
    "docstring": "The output of a local shell tool call.\n",
    "ident": "LocalShellCallOutput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "output"
        },
        {
          "ident": "type"
        },
        {
          "ident": "status"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18 > (property) output",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18 > (property) status"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/18",
    "docstring": "A tool representing a request to execute one or more shell commands.",
    "ident": "ShellCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "action"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "caller"
        },
        {
          "ident": "environment"
        },
        {
          "ident": "status"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) action",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) call_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) caller",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) environment",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) status"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/19",
    "docstring": "The streamed output items emitted by a shell tool call.",
    "ident": "ShellCallOutput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "call_id"
        },
        {
          "ident": "output"
        },
        {
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "caller"
        },
        {
          "ident": "max_output_length"
        },
        {
          "ident": "status"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) call_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) output",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) caller",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) max_output_length",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) status"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/20",
    "docstring": "A tool call representing a request to create, delete, or update files using diff patches.",
    "ident": "ApplyPatchCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "call_id"
        },
        {
          "ident": "operation"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "caller"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) call_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) status",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) caller"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/21",
    "docstring": "The streamed output emitted by an apply patch tool call.",
    "ident": "ApplyPatchCallOutput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "call_id"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "caller"
        },
        {
          "ident": "output"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) call_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) status",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) caller",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) output"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/22",
    "docstring": "A list of tools available on an MCP server.\n",
    "ident": "McpListTools",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "server_label"
        },
        {
          "ident": "tools"
        },
        {
          "ident": "type"
        },
        {
          "ident": "error"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) server_label",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) tools",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) error"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 24": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/23",
    "docstring": "A request for human approval of a tool invocation.\n",
    "ident": "McpApprovalRequest",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "arguments"
        },
        {
          "ident": "name"
        },
        {
          "ident": "server_label"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 24 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 24 > (property) arguments",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 24 > (property) name",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 24 > (property) server_label",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 24 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 25": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/24",
    "docstring": "A response to an MCP approval request.\n",
    "ident": "McpApprovalResponse",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "approval_request_id"
        },
        {
          "ident": "approve"
        },
        {
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "reason"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 25 > (property) approval_request_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 25 > (property) approve",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 25 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 25 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 25 > (property) reason"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/25",
    "docstring": "An invocation of a tool on an MCP server.\n",
    "ident": "McpCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "arguments"
        },
        {
          "ident": "name"
        },
        {
          "ident": "server_label"
        },
        {
          "ident": "type"
        },
        {
          "ident": "approval_request_id"
        },
        {
          "ident": "error"
        },
        {
          "ident": "output"
        },
        {
          "ident": "status"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) arguments",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) name",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) server_label",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) approval_request_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) error",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) output",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) status"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/26",
    "docstring": "The output of a custom tool call from your code, being sent back to the model.\n",
    "ident": "CustomToolCallOutput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "call_id"
        },
        {
          "ident": "output"
        },
        {
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "caller"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) call_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) output",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) caller"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Item/oneOf/27",
    "docstring": "A call to a custom tool created by the model.\n",
    "ident": "CustomToolCall",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "call_id"
        },
        {
          "ident": "input"
        },
        {
          "ident": "name"
        },
        {
          "ident": "type"
        },
        {
          "ident": "id"
        },
        {
          "ident": "async"
        },
        {
          "ident": "caller"
        },
        {
          "ident": "namespace"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) call_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) input",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) name",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) async",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) caller",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) namespace"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 29": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/InputItem/oneOf/2",
    "docstring": "Compacts the current context. Must be the final input item.",
    "ident": "CompactionTrigger",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 29 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 29 > (property) id"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 30": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/InputItem/oneOf/3",
    "docstring": "An internal identifier for an item to reference.",
    "ident": "ItemReference",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 30 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 30 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 31": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/InputItem/oneOf/4",
    "ident": "Program",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "code"
        },
        {
          "ident": "fingerprint"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 31 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 31 > (property) call_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 31 > (property) code",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 31 > (property) fingerprint",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 31 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/InputItem/oneOf/5",
    "ident": "ProgramOutput",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "call_id"
        },
        {
          "ident": "result"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32 > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32 > (property) call_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32 > (property) result",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32 > (property) status",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32 > (property) type"
    ]
  },
  "(resource) responses > (model) easy_input_message > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/EasyInputMessage",
    "docstring": "A message input to the model with a role indicating instruction following\nhierarchy. Instructions given with the `developer` or `system` role take\nprecedence over instructions given with the `user` role. Messages with the\n`assistant` role are presumed to have been generated by the model in previous\ninteractions.\n",
    "ident": "EasyInputMessage",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "content"
        },
        {
          "ident": "role"
        },
        {
          "ident": "phase"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) easy_input_message > (schema) > (property) content",
      "(resource) responses > (model) easy_input_message > (schema) > (property) role",
      "(resource) responses > (model) easy_input_message > (schema) > (property) phase",
      "(resource) responses > (model) easy_input_message > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) response_output_message > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputMessage",
    "docstring": "An output message from the model.\n",
    "ident": "ResponseOutputMessage",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "content"
        },
        {
          "ident": "role"
        },
        {
          "ident": "status"
        },
        {
          "ident": "type"
        },
        {
          "ident": "phase"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_message > (schema) > (property) id",
      "(resource) responses > (model) response_output_message > (schema) > (property) content",
      "(resource) responses > (model) response_output_message > (schema) > (property) role",
      "(resource) responses > (model) response_output_message > (schema) > (property) status",
      "(resource) responses > (model) response_output_message > (schema) > (property) type",
      "(resource) responses > (model) response_output_message > (schema) > (property) phase"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "response.item.create"
    }
  },
  "(resource) responses > (model) easy_input_message > (schema) > (property) content": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/EasyInputMessage/properties/content",
    "deprecated": false,
    "key": "content",
    "docstring": "Text, image, or audio input to the model, used to generate a response.\nCan also contain previous assistant responses.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/EasyInputMessage/properties/content",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ResponseInputMessageContentList",
          "$ref": "(resource) responses > (model) response_input_message_content_list > (schema)"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) easy_input_message > (schema) > (property) content > (variant) 0",
      "(resource) responses > (model) easy_input_message > (schema) > (property) content > (variant) 1"
    ]
  },
  "(resource) responses > (model) easy_input_message > (schema) > (property) role": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/EasyInputMessage/properties/role",
    "deprecated": false,
    "key": "role",
    "docstring": "The role of the message input. One of `user`, `assistant`, `system`, or\n`developer`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/EasyInputMessage/properties/role",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "user"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "assistant"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "system"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "developer"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) easy_input_message > (schema) > (property) role > (member) 0",
      "(resource) responses > (model) easy_input_message > (schema) > (property) role > (member) 1",
      "(resource) responses > (model) easy_input_message > (schema) > (property) role > (member) 2",
      "(resource) responses > (model) easy_input_message > (schema) > (property) role > (member) 3"
    ]
  },
  "(resource) responses > (model) easy_input_message > (schema) > (property) phase": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/EasyInputMessage/properties/phase",
    "deprecated": false,
    "key": "phase",
    "docstring": "Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).\nFor models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend\nphase on all assistant messages — dropping it can degrade performance. Not used for user messages.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/EasyInputMessage/properties/phase",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "commentary"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "final_answer"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) easy_input_message > (schema) > (property) phase > (member) 0",
      "(resource) responses > (model) easy_input_message > (schema) > (property) phase > (member) 1"
    ]
  },
  "(resource) responses > (model) easy_input_message > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/EasyInputMessage/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the message input. Always `message`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/EasyInputMessage/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "message"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) easy_input_message > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) content": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputMessage/properties/content",
    "deprecated": false,
    "key": "content",
    "docstring": "A list of one or many input items to the model, containing different content \ntypes.\n",
    "title": "Input item content list",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseInputMessageContentList",
      "$ref": "(resource) responses > (model) response_input_message_content_list > (schema)"
    },
    "optional": false,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "array",
    "modelPath": "(resource) responses > (model) response_input_message_content_list",
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) response_input_content > (schema) > (variant) 0",
      "(resource) responses > (model) response_input_content > (schema) > (variant) 1",
      "(resource) responses > (model) response_input_content > (schema) > (variant) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) role": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputMessage/properties/role",
    "deprecated": false,
    "key": "role",
    "docstring": "The role of the message input. One of `user`, `system`, or `developer`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/InputMessage/properties/role",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "user"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "system"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "developer"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) role > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) role > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) role > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputMessage/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of item. One of `in_progress`, `completed`, or\n`incomplete`. Populated when items are returned via API.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/InputMessage/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) status > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) status > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputMessage/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the message input. Always set to `message`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/InputMessage/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "message"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_output_message > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/OutputMessage/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the output message.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_output_message > (schema) > (property) content": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/OutputMessage/properties/content",
    "deprecated": false,
    "key": "content",
    "docstring": "The content of the output message.\n",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/OutputMessage/properties/content",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/OutputMessage/properties/content/items",
        "types": [
          {
            "kind": "HttpTypeReference",
            "ident": "ResponseOutputText",
            "$ref": "(resource) responses > (model) response_output_text > (schema)"
          },
          {
            "kind": "HttpTypeReference",
            "ident": "ResponseOutputRefusal",
            "$ref": "(resource) responses > (model) response_output_refusal > (schema)"
          }
        ]
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) response_output_message > (schema) > (property) content > (items) > (variant) 0",
      "(resource) responses > (model) response_output_message > (schema) > (property) content > (items) > (variant) 1"
    ]
  },
  "(resource) responses > (model) response_output_message > (schema) > (property) role": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/OutputMessage/properties/role",
    "deprecated": false,
    "key": "role",
    "docstring": "The role of the output message. Always `assistant`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/OutputMessage/properties/role",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "assistant"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_output_message > (schema) > (property) role > (member) 0"
    ]
  },
  "(resource) responses > (model) response_output_message > (schema) > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/OutputMessage/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the message input. One of `in_progress`, `completed`, or\n`incomplete`. Populated when input items are returned via API.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/OutputMessage/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_output_message > (schema) > (property) status > (member) 0",
      "(resource) responses > (model) response_output_message > (schema) > (property) status > (member) 1",
      "(resource) responses > (model) response_output_message > (schema) > (property) status > (member) 2"
    ]
  },
  "(resource) responses > (model) response_output_message > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/OutputMessage/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the output message. Always `message`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/OutputMessage/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "message"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_output_message > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_output_message > (schema) > (property) phase": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/OutputMessage/properties/phase",
    "deprecated": false,
    "key": "phase",
    "docstring": "Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).\nFor models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend\nphase on all assistant messages — dropping it can degrade performance. Not used for user messages.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/OutputMessage/properties/phase",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "commentary"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "final_answer"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_output_message > (schema) > (property) phase > (member) 0",
      "(resource) responses > (model) response_output_message > (schema) > (property) phase > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchToolCall/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the file search tool call.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) queries": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchToolCall/properties/queries",
    "deprecated": false,
    "key": "queries",
    "docstring": "The queries used to search for files.\n",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/FileSearchToolCall/properties/queries",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchToolCall/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the file search tool call. One of `in_progress`,\n`searching`, `incomplete` or `failed`,\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FileSearchToolCall/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "searching"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "failed"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) status > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) status > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) status > (member) 3",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) status > (member) 4"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchToolCall/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the file search tool call. Always `file_search_call`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FileSearchToolCall/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "file_search_call"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchToolCall/properties/results",
    "deprecated": false,
    "key": "results",
    "docstring": "The results of the file search tool call.\n",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/FileSearchToolCall/properties/results",
      "elementType": {
        "kind": "HttpTypeObject",
        "members": [
          {
            "ident": "attributes"
          },
          {
            "ident": "file_id"
          },
          {
            "ident": "filename"
          },
          {
            "ident": "score"
          },
          {
            "ident": "text"
          }
        ]
      }
    },
    "optional": true,
    "nullable": true,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results > (items) > (property) attributes",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results > (items) > (property) file_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results > (items) > (property) filename",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results > (items) > (property) score",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results > (items) > (property) text"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerToolCall/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the computer call.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) call_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerToolCall/properties/call_id",
    "deprecated": false,
    "key": "call_id",
    "docstring": "An identifier used when responding to the tool call with output.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) pending_safety_checks": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerToolCall/properties/pending_safety_checks",
    "deprecated": false,
    "key": "pending_safety_checks",
    "docstring": "The pending safety checks for the computer call.\n",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/ComputerToolCall/properties/pending_safety_checks",
      "elementType": {
        "kind": "HttpTypeObject",
        "members": [
          {
            "ident": "id"
          },
          {
            "ident": "code"
          },
          {
            "ident": "message"
          }
        ]
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) pending_safety_checks > (items) > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) pending_safety_checks > (items) > (property) code",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) pending_safety_checks > (items) > (property) message"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerToolCall/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the item. One of `in_progress`, `completed`, or\n`incomplete`. Populated when items are returned via API.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ComputerToolCall/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) status > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) status > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerToolCall/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the computer call. Always `computer_call`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ComputerToolCall/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "computer_call"
        }
      ]
    },
    "default": "computer_call",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) action": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerToolCall/properties/action",
    "deprecated": false,
    "key": "action",
    "docstring": "A click action.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ComputerAction",
      "$ref": "(resource) responses > (model) computer_action > (schema)"
    },
    "optional": true,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "union",
    "modelPath": "(resource) responses > (model) computer_action",
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 0",
      "(resource) responses > (model) computer_action > (schema) > (variant) 1",
      "(resource) responses > (model) computer_action > (schema) > (variant) 2",
      "(resource) responses > (model) computer_action > (schema) > (variant) 3",
      "(resource) responses > (model) computer_action > (schema) > (variant) 4",
      "(resource) responses > (model) computer_action > (schema) > (variant) 5",
      "(resource) responses > (model) computer_action > (schema) > (variant) 6",
      "(resource) responses > (model) computer_action > (schema) > (variant) 7",
      "(resource) responses > (model) computer_action > (schema) > (variant) 8"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) actions": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerToolCall/properties/actions",
    "deprecated": false,
    "key": "actions",
    "docstring": "Flattened batched actions for `computer_use`. Each action includes an\n`type` discriminator and action-specific fields.\n",
    "title": "Computer Action List",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ComputerActionList",
      "$ref": "(resource) responses > (model) computer_action_list > (schema)"
    },
    "optional": true,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "array",
    "modelPath": "(resource) responses > (model) computer_action_list",
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 0",
      "(resource) responses > (model) computer_action > (schema) > (variant) 1",
      "(resource) responses > (model) computer_action > (schema) > (variant) 2",
      "(resource) responses > (model) computer_action > (schema) > (variant) 3",
      "(resource) responses > (model) computer_action > (schema) > (variant) 4",
      "(resource) responses > (model) computer_action > (schema) > (variant) 5",
      "(resource) responses > (model) computer_action > (schema) > (variant) 6",
      "(resource) responses > (model) computer_action > (schema) > (variant) 7",
      "(resource) responses > (model) computer_action > (schema) > (variant) 8"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) call_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerCallOutputItemParam/properties/call_id",
    "deprecated": false,
    "key": "call_id",
    "docstring": "The ID of the computer tool call that produced the output.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) output": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerCallOutputItemParam/properties/output",
    "deprecated": false,
    "key": "output",
    "docstring": "A computer screenshot image used with the computer use tool.\n",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseComputerToolCallOutputScreenshot",
      "$ref": "(resource) responses > (model) response_computer_tool_call_output_screenshot > (schema)"
    },
    "optional": false,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "object",
    "modelPath": "(resource) responses > (model) response_computer_tool_call_output_screenshot",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_computer_tool_call_output_screenshot > (schema) > (property) type",
      "(resource) responses > (model) response_computer_tool_call_output_screenshot > (schema) > (property) file_id",
      "(resource) responses > (model) response_computer_tool_call_output_screenshot > (schema) > (property) image_url"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerCallOutputItemParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the computer tool call output. Always `computer_call_output`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ComputerCallOutputItemParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "computer_call_output"
        }
      ]
    },
    "default": "computer_call_output",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerCallOutputItemParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The ID of the computer tool call output.",
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "cuo_123"
    ],
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) acknowledged_safety_checks": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerCallOutputItemParam/properties/acknowledged_safety_checks",
    "deprecated": false,
    "key": "acknowledged_safety_checks",
    "docstring": "The safety checks reported by the API that have been acknowledged by the developer.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/ComputerCallOutputItemParam/properties/acknowledged_safety_checks",
      "elementType": {
        "kind": "HttpTypeObject",
        "members": [
          {
            "ident": "id"
          },
          {
            "ident": "code"
          },
          {
            "ident": "message"
          }
        ]
      }
    },
    "optional": true,
    "nullable": true,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) acknowledged_safety_checks > (items) > (property) id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) acknowledged_safety_checks > (items) > (property) code",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) acknowledged_safety_checks > (items) > (property) message"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerCallOutputItemParam/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ComputerCallOutputItemParam/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) status > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) status > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchToolCall/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the web search tool call.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchToolCall/properties/action",
    "deprecated": false,
    "key": "action",
    "docstring": "An object describing the specific action taken in this web search call.\nIncludes details on how the model used the web (search, open_page, find_in_page).\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/WebSearchToolCall/properties/action",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            },
            {
              "ident": "queries"
            },
            {
              "ident": "query"
            },
            {
              "ident": "sources"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            },
            {
              "ident": "url"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "pattern"
            },
            {
              "ident": "type"
            },
            {
              "ident": "url"
            }
          ]
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchToolCall/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the web search tool call.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/WebSearchToolCall/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "searching"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "failed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) status > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) status > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) status > (member) 3",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) status > (member) 4"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchToolCall/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the web search tool call. Always `web_search_call`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/WebSearchToolCall/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "web_search_call"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) arguments": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolCall/properties/arguments",
    "deprecated": false,
    "key": "arguments",
    "docstring": "A JSON string of the arguments to pass to the function.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) call_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolCall/properties/call_id",
    "deprecated": false,
    "key": "call_id",
    "docstring": "The unique ID of the function tool call generated by the model.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolCall/properties/name",
    "deprecated": false,
    "key": "name",
    "docstring": "The name of the function to run.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolCall/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the function tool call. Always `function_call`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionToolCall/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function_call"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolCall/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the function tool call.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) async": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolCall/properties/async",
    "deprecated": false,
    "key": "async",
    "docstring": "Whether the function tool call runs asynchronously.\n",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) caller": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolCall/properties/caller",
    "deprecated": false,
    "key": "caller",
    "docstring": "The execution context that produced this tool call.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionToolCall/properties/caller",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "caller_id"
            },
            {
              "ident": "type"
            }
          ]
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) caller > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) caller > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) namespace": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolCall/properties/namespace",
    "deprecated": false,
    "key": "namespace",
    "docstring": "The namespace of the function to run.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolCall/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the item. One of `in_progress`, `completed`, or\n`incomplete`. Populated when items are returned via API.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionToolCall/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) status > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) status > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) output": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/output",
    "deprecated": false,
    "key": "output",
    "docstring": "Text, image, or file output of the function tool call.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/output",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeArray",
          "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/output/oneOf/1",
          "elementType": {
            "kind": "HttpTypeUnion",
            "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/output/oneOf/1/items",
            "types": [
              {
                "kind": "HttpTypeReference",
                "ident": "ResponseInputTextContent",
                "$ref": "(resource) responses > (model) response_input_text_content > (schema)"
              },
              {
                "kind": "HttpTypeReference",
                "ident": "ResponseInputImageContent",
                "$ref": "(resource) responses > (model) response_input_image_content > (schema)"
              },
              {
                "kind": "HttpTypeReference",
                "ident": "ResponseInputFileContent",
                "$ref": "(resource) responses > (model) response_input_file_content > (schema)"
              }
            ]
          }
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) output > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) output > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the function tool call output. Always `function_call_output`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function_call_output"
        }
      ]
    },
    "default": "function_call_output",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the function tool call output. Populated when this item is returned via API.",
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "fc_123"
    ],
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) call_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/call_id",
    "deprecated": false,
    "key": "call_id",
    "docstring": "The unique ID of the function tool call generated by the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) caller": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/caller",
    "deprecated": false,
    "key": "caller",
    "docstring": "The execution context that produced this tool call.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/caller",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "caller_id"
            },
            {
              "ident": "type"
            }
          ]
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) caller > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) caller > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/name",
    "deprecated": false,
    "key": "name",
    "docstring": "The name of the tool that produced the output.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 128
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) namespace": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/namespace",
    "deprecated": false,
    "key": "namespace",
    "docstring": "The namespace of the tool that produced the output.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) status > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) status > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) arguments": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ToolSearchCallItemParam/properties/arguments",
    "deprecated": false,
    "key": "arguments",
    "docstring": "The arguments supplied to the tool search call.",
    "type": {
      "kind": "HttpTypeUnknown"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "unknown",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ToolSearchCallItemParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The item type. Always `tool_search_call`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ToolSearchCallItemParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "tool_search_call"
        }
      ]
    },
    "default": "tool_search_call",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ToolSearchCallItemParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of this tool search call.",
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "tsc_123"
    ],
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) call_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ToolSearchCallItemParam/properties/call_id",
    "deprecated": false,
    "key": "call_id",
    "docstring": "The unique ID of the tool search call generated by the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) execution": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ToolSearchCallItemParam/properties/execution",
    "deprecated": false,
    "key": "execution",
    "docstring": "Whether tool search was executed by the server or by the client.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ToolSearchCallItemParam/properties/execution",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "server"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "client"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) execution > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) execution > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ToolSearchCallItemParam/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the tool search call.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ToolSearchCallItemParam/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) status > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) status > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ToolSearchOutputItemParam/properties/tools",
    "deprecated": false,
    "key": "tools",
    "docstring": "The loaded tool definitions returned by the tool search output.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/ToolSearchOutputItemParam/properties/tools",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/ToolSearchOutputItemParam/properties/tools/items",
        "types": [
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "name"
              },
              {
                "ident": "parameters"
              },
              {
                "ident": "strict"
              },
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              },
              {
                "ident": "async"
              },
              {
                "ident": "defer_loading"
              },
              {
                "ident": "description"
              },
              {
                "ident": "output_schema"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "vector_store_ids"
              },
              {
                "ident": "filters"
              },
              {
                "ident": "max_num_results"
              },
              {
                "ident": "ranking_options"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "display_height"
              },
              {
                "ident": "display_width"
              },
              {
                "ident": "environment"
              },
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "external_web_access"
              },
              {
                "ident": "filters"
              },
              {
                "ident": "search_context_size"
              },
              {
                "ident": "user_location"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "server_label"
              },
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              },
              {
                "ident": "allowed_tools"
              },
              {
                "ident": "authorization"
              },
              {
                "ident": "connector_id"
              },
              {
                "ident": "defer_loading"
              },
              {
                "ident": "headers"
              },
              {
                "ident": "require_approval"
              },
              {
                "ident": "server_description"
              },
              {
                "ident": "server_url"
              },
              {
                "ident": "tunnel_id"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "container"
              },
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "action"
              },
              {
                "ident": "background"
              },
              {
                "ident": "input_fidelity"
              },
              {
                "ident": "input_image_mask"
              },
              {
                "ident": "model"
              },
              {
                "ident": "moderation"
              },
              {
                "ident": "output_compression"
              },
              {
                "ident": "output_format"
              },
              {
                "ident": "partial_images"
              },
              {
                "ident": "quality"
              },
              {
                "ident": "size"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              },
              {
                "ident": "environment"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "name"
              },
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              },
              {
                "ident": "async"
              },
              {
                "ident": "defer_loading"
              },
              {
                "ident": "description"
              },
              {
                "ident": "format"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "description"
              },
              {
                "ident": "name"
              },
              {
                "ident": "tools"
              },
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "description"
              },
              {
                "ident": "execution"
              },
              {
                "ident": "parameters"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "search_content_types"
              },
              {
                "ident": "search_context_size"
              },
              {
                "ident": "user_location"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              }
            ]
          }
        ]
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 7",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 9",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 13",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 15"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ToolSearchOutputItemParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The item type. Always `tool_search_output`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ToolSearchOutputItemParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "tool_search_output"
        }
      ]
    },
    "default": "tool_search_output",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ToolSearchOutputItemParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of this tool search output.",
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "tso_123"
    ],
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) call_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ToolSearchOutputItemParam/properties/call_id",
    "deprecated": false,
    "key": "call_id",
    "docstring": "The unique ID of the tool search call generated by the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) execution": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ToolSearchOutputItemParam/properties/execution",
    "deprecated": false,
    "key": "execution",
    "docstring": "Whether tool search was executed by the server or by the client.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ToolSearchOutputItemParam/properties/execution",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "server"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "client"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) execution > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) execution > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ToolSearchOutputItemParam/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the tool search output.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ToolSearchOutputItemParam/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) status > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) status > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) role": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/AdditionalToolsItemParam/properties/role",
    "deprecated": false,
    "key": "role",
    "docstring": "The role that provided the additional tools. Only `developer` is supported.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/AdditionalToolsItemParam/properties/role",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "developer"
        }
      ]
    },
    "default": "developer",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) role > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/AdditionalToolsItemParam/properties/tools",
    "deprecated": false,
    "key": "tools",
    "docstring": "A list of additional tools made available at this item.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/AdditionalToolsItemParam/properties/tools",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/AdditionalToolsItemParam/properties/tools/items",
        "types": [
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "name"
              },
              {
                "ident": "parameters"
              },
              {
                "ident": "strict"
              },
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              },
              {
                "ident": "async"
              },
              {
                "ident": "defer_loading"
              },
              {
                "ident": "description"
              },
              {
                "ident": "output_schema"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "vector_store_ids"
              },
              {
                "ident": "filters"
              },
              {
                "ident": "max_num_results"
              },
              {
                "ident": "ranking_options"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "display_height"
              },
              {
                "ident": "display_width"
              },
              {
                "ident": "environment"
              },
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "external_web_access"
              },
              {
                "ident": "filters"
              },
              {
                "ident": "search_context_size"
              },
              {
                "ident": "user_location"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "server_label"
              },
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              },
              {
                "ident": "allowed_tools"
              },
              {
                "ident": "authorization"
              },
              {
                "ident": "connector_id"
              },
              {
                "ident": "defer_loading"
              },
              {
                "ident": "headers"
              },
              {
                "ident": "require_approval"
              },
              {
                "ident": "server_description"
              },
              {
                "ident": "server_url"
              },
              {
                "ident": "tunnel_id"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "container"
              },
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "action"
              },
              {
                "ident": "background"
              },
              {
                "ident": "input_fidelity"
              },
              {
                "ident": "input_image_mask"
              },
              {
                "ident": "model"
              },
              {
                "ident": "moderation"
              },
              {
                "ident": "output_compression"
              },
              {
                "ident": "output_format"
              },
              {
                "ident": "partial_images"
              },
              {
                "ident": "quality"
              },
              {
                "ident": "size"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              },
              {
                "ident": "environment"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "name"
              },
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              },
              {
                "ident": "async"
              },
              {
                "ident": "defer_loading"
              },
              {
                "ident": "description"
              },
              {
                "ident": "format"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "description"
              },
              {
                "ident": "name"
              },
              {
                "ident": "tools"
              },
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "description"
              },
              {
                "ident": "execution"
              },
              {
                "ident": "parameters"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "search_content_types"
              },
              {
                "ident": "search_context_size"
              },
              {
                "ident": "user_location"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              }
            ]
          }
        ]
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 7",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 9",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 10",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 11",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 13",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 15"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/AdditionalToolsItemParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The item type. Always `additional_tools`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/AdditionalToolsItemParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "additional_tools"
        }
      ]
    },
    "default": "additional_tools",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/AdditionalToolsItemParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of this additional tools item.",
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "at_123"
    ],
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 12 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ResponseConfigurationUpdateItemParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The item type. Always `configuration_update`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ResponseConfigurationUpdateItemParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "configuration_update"
        }
      ]
    },
    "default": "configuration_update",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 12 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 12 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ResponseConfigurationUpdateItemParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the configuration update item.",
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "cnfu_123"
    ],
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 12 > (property) reasoning": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ResponseConfigurationUpdateItemParam/properties/reasoning",
    "deprecated": false,
    "key": "reasoning",
    "docstring": "Updates to reasoning configuration. Only effort is supported.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "effort"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 12 > (property) reasoning > (property) effort"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ReasoningItem/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique identifier of the reasoning content.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) summary": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ReasoningItem/properties/summary",
    "deprecated": false,
    "key": "summary",
    "docstring": "Reasoning summary content.\n",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/ReasoningItem/properties/summary",
      "elementType": {
        "kind": "HttpTypeReference",
        "ident": "SummaryTextContent",
        "$ref": "(resource) conversations > (model) summary_text_content > (schema)"
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) conversations > (model) summary_text_content > (schema) > (property) text",
      "(resource) conversations > (model) summary_text_content > (schema) > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ReasoningItem/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the object. Always `reasoning`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ReasoningItem/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "reasoning"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) content": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ReasoningItem/properties/content",
    "deprecated": false,
    "key": "content",
    "docstring": "Reasoning text content.\n",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/ReasoningItem/properties/content",
      "elementType": {
        "kind": "HttpTypeObject",
        "members": [
          {
            "ident": "text"
          },
          {
            "ident": "type"
          }
        ]
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) content > (items) > (property) text",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) content > (items) > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) encrypted_content": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ReasoningItem/properties/encrypted_content",
    "deprecated": false,
    "key": "encrypted_content",
    "docstring": "The encrypted content of the reasoning item. This is populated by default\nfor reasoning items returned by `POST /v1/responses` and WebSocket\n`response.create` requests.\n\nWhen streaming, use the completed reasoning item and its\n`encrypted_content` from the `response.output_item.done` event in\nsubsequent requests. The `encrypted_content` in\n`response.output_item.added` may be incomplete. This is especially\nimportant when `store` is `false` or when using Zero Data Retention.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ReasoningItem/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the item. One of `in_progress`, `completed`, or\n`incomplete`. Populated when items are returned via API.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ReasoningItem/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) status > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) status > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 14 > (property) encrypted_content": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CompactionSummaryItemParam/properties/encrypted_content",
    "deprecated": false,
    "key": "encrypted_content",
    "docstring": "The encrypted content of the compaction summary.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 20971520
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 14 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CompactionSummaryItemParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the item. Always `compaction`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CompactionSummaryItemParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "compaction"
        }
      ]
    },
    "default": "compaction",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 14 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 14 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CompactionSummaryItemParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The ID of the compaction item.",
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "cmp_123"
    ],
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenToolCall/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the image generation call.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) result": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenToolCall/properties/result",
    "deprecated": false,
    "key": "result",
    "docstring": "The generated image encoded in base64.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenToolCall/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the image generation call.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenToolCall/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "generating"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "failed"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) status > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) status > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) status > (member) 3"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenToolCall/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the image generation call. Always `image_generation_call`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenToolCall/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "image_generation_call"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) action": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenToolCall/properties/action",
    "deprecated": false,
    "key": "action",
    "docstring": "The action used for image generation.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenToolCall/properties/action",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "generate"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "edit"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) action > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) action > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) action > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) background": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenToolCall/properties/background",
    "deprecated": false,
    "key": "background",
    "docstring": "The background setting used for generation.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenToolCall/properties/background",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "transparent"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "opaque"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) background > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) background > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) background > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) output_format": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenToolCall/properties/output_format",
    "deprecated": false,
    "key": "output_format",
    "docstring": "The output format used for generation.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenToolCall/properties/output_format",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "png"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "webp"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "jpeg"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) output_format > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) output_format > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) output_format > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) quality": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenToolCall/properties/quality",
    "deprecated": false,
    "key": "quality",
    "docstring": "The quality of the image generated by the image generation tool call. One of `low`, `medium`, `high`, `xhigh`, `max`, or `auto`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenToolCall/properties/quality",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "medium"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "xhigh"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "max"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) quality > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) quality > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) quality > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) quality > (member) 3",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) quality > (member) 4",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) quality > (member) 5"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) revised_prompt": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenToolCall/properties/revised_prompt",
    "deprecated": false,
    "key": "revised_prompt",
    "docstring": "The prompt that was used after any model prompt rewriting.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) size": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenToolCall/properties/size",
    "deprecated": false,
    "key": "size",
    "docstring": "The image dimensions as a `WIDTHxHEIGHT` string, for example `1536x864`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenToolCall/properties/size",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnion",
          "oasRef": "#/components/schemas/ImageGenToolCall/properties/size/anyOf/0/anyOf/1",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "1024x1024"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "1024x1536"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "1536x1024"
            }
          ]
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) size > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) size > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CodeInterpreterToolCall/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the code interpreter tool call.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) code": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CodeInterpreterToolCall/properties/code",
    "deprecated": false,
    "key": "code",
    "docstring": "The code to run, or null if not available.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) container_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CodeInterpreterToolCall/properties/container_id",
    "deprecated": false,
    "key": "container_id",
    "docstring": "The ID of the container used to run the code.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) outputs": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CodeInterpreterToolCall/properties/outputs",
    "deprecated": false,
    "key": "outputs",
    "docstring": "The outputs generated by the code interpreter, such as logs or images.\nCan be null if no outputs are available.\n",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/CodeInterpreterToolCall/properties/outputs",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/CodeInterpreterToolCall/properties/outputs/anyOf/0/items",
        "types": [
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "logs"
              },
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "type"
              },
              {
                "ident": "url"
              }
            ]
          }
        ]
      }
    },
    "optional": false,
    "nullable": true,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) outputs > (items) > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) outputs > (items) > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CodeInterpreterToolCall/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CodeInterpreterToolCall/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "interpreting"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "failed"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) status > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) status > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) status > (member) 3",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) status > (member) 4"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CodeInterpreterToolCall/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the code interpreter tool call. Always `code_interpreter_call`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CodeInterpreterToolCall/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "code_interpreter_call"
        }
      ]
    },
    "default": "code_interpreter_call",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalShellToolCall/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the local shell call.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) action": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalShellToolCall/properties/action",
    "deprecated": false,
    "key": "action",
    "docstring": "Execute a shell command on the server.",
    "title": "Local shell exec action",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "command"
        },
        {
          "ident": "env"
        },
        {
          "ident": "type"
        },
        {
          "ident": "timeout_ms"
        },
        {
          "ident": "user"
        },
        {
          "ident": "working_directory"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) action > (property) command",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) action > (property) env",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) action > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) action > (property) timeout_ms",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) action > (property) user",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) action > (property) working_directory"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) call_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalShellToolCall/properties/call_id",
    "deprecated": false,
    "key": "call_id",
    "docstring": "The unique ID of the local shell tool call generated by the model.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalShellToolCall/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the local shell call.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LocalShellToolCall/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) status > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) status > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalShellToolCall/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the local shell call. Always `local_shell_call`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LocalShellToolCall/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "local_shell_call"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalShellToolCallOutput/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the local shell tool call generated by the model.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18 > (property) output": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalShellToolCallOutput/properties/output",
    "deprecated": false,
    "key": "output",
    "docstring": "A JSON string of the output of the local shell tool call.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalShellToolCallOutput/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the local shell tool call output. Always `local_shell_call_output`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LocalShellToolCallOutput/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "local_shell_call_output"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalShellToolCallOutput/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the item. One of `in_progress`, `completed`, or `incomplete`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LocalShellToolCallOutput/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18 > (property) status > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18 > (property) status > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) action": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallItemParam/properties/action",
    "deprecated": false,
    "key": "action",
    "docstring": "The shell commands and limits that describe how to run the tool call.",
    "title": "Shell action",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "commands"
        },
        {
          "ident": "max_output_length"
        },
        {
          "ident": "timeout_ms"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) action > (property) commands",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) action > (property) max_output_length",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) action > (property) timeout_ms"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) call_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallItemParam/properties/call_id",
    "deprecated": false,
    "key": "call_id",
    "docstring": "The unique ID of the shell tool call generated by the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallItemParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the item. Always `shell_call`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionShellCallItemParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "shell_call"
        }
      ]
    },
    "default": "shell_call",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallItemParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the shell tool call. Populated when this item is returned via API.",
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "sh_123"
    ],
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) caller": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallItemParam/properties/caller",
    "deprecated": false,
    "key": "caller",
    "docstring": "The execution context that produced this tool call.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionShellCallItemParam/properties/caller",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "caller_id"
            },
            {
              "ident": "type"
            }
          ]
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) caller > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) caller > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) environment": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallItemParam/properties/environment",
    "deprecated": false,
    "key": "environment",
    "docstring": "The environment to execute the shell commands in.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionShellCallItemParam/properties/environment",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "LocalEnvironment",
          "$ref": "(resource) responses > (model) local_environment > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ContainerReference",
          "$ref": "(resource) responses > (model) container_reference > (schema)"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) environment > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) environment > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallItemParam/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.",
    "title": "Shell call status",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionShellCallItemParam/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) status > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) status > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) call_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallOutputItemParam/properties/call_id",
    "deprecated": false,
    "key": "call_id",
    "docstring": "The unique ID of the shell tool call generated by the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) output": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallOutputItemParam/properties/output",
    "deprecated": false,
    "key": "output",
    "docstring": "Captured chunks of stdout and stderr output, along with their associated outcomes.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/FunctionShellCallOutputItemParam/properties/output",
      "elementType": {
        "kind": "HttpTypeReference",
        "ident": "ResponseFunctionShellCallOutputContent",
        "$ref": "(resource) responses > (model) response_function_shell_call_output_content > (schema)"
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) outcome",
      "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) stderr",
      "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) stdout"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallOutputItemParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the item. Always `shell_call_output`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionShellCallOutputItemParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "shell_call_output"
        }
      ]
    },
    "default": "shell_call_output",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallOutputItemParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the shell tool call output. Populated when this item is returned via API.",
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "sho_123"
    ],
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) caller": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallOutputItemParam/properties/caller",
    "deprecated": false,
    "key": "caller",
    "docstring": "The execution context that produced this tool call.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionShellCallOutputItemParam/properties/caller",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "caller_id"
            },
            {
              "ident": "type"
            }
          ]
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) caller > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) caller > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) max_output_length": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallOutputItemParam/properties/max_output_length",
    "deprecated": false,
    "key": "max_output_length",
    "docstring": "The maximum number of UTF-8 characters captured for this shell call's combined output.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallOutputItemParam/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the shell call output.",
    "title": "Shell call status",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionShellCallOutputItemParam/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) status > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) status > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) call_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApplyPatchToolCallItemParam/properties/call_id",
    "deprecated": false,
    "key": "call_id",
    "docstring": "The unique ID of the apply patch tool call generated by the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApplyPatchToolCallItemParam/properties/operation",
    "deprecated": false,
    "key": "operation",
    "docstring": "The specific create, delete, or update instruction for the apply_patch tool call.",
    "title": "Apply patch operation",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ApplyPatchToolCallItemParam/properties/operation",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "diff"
            },
            {
              "ident": "path"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "path"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "diff"
            },
            {
              "ident": "path"
            },
            {
              "ident": "type"
            }
          ]
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation > (variant) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation > (variant) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApplyPatchToolCallItemParam/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the apply patch tool call. One of `in_progress` or `completed`.",
    "title": "Apply patch call status",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ApplyPatchToolCallItemParam/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) status > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApplyPatchToolCallItemParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the item. Always `apply_patch_call`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ApplyPatchToolCallItemParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "apply_patch_call"
        }
      ]
    },
    "default": "apply_patch_call",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApplyPatchToolCallItemParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the apply patch tool call. Populated when this item is returned via API.",
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "apc_123"
    ],
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) caller": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApplyPatchToolCallItemParam/properties/caller",
    "deprecated": false,
    "key": "caller",
    "docstring": "The execution context that produced this tool call.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ApplyPatchToolCallItemParam/properties/caller",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "caller_id"
            },
            {
              "ident": "type"
            }
          ]
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) caller > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) caller > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) call_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApplyPatchToolCallOutputItemParam/properties/call_id",
    "deprecated": false,
    "key": "call_id",
    "docstring": "The unique ID of the apply patch tool call generated by the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApplyPatchToolCallOutputItemParam/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the apply patch tool call output. One of `completed` or `failed`.",
    "title": "Apply patch call output status",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ApplyPatchToolCallOutputItemParam/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "failed"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) status > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApplyPatchToolCallOutputItemParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the item. Always `apply_patch_call_output`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ApplyPatchToolCallOutputItemParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "apply_patch_call_output"
        }
      ]
    },
    "default": "apply_patch_call_output",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApplyPatchToolCallOutputItemParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the apply patch tool call output. Populated when this item is returned via API.",
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "apco_123"
    ],
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) caller": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApplyPatchToolCallOutputItemParam/properties/caller",
    "deprecated": false,
    "key": "caller",
    "docstring": "The execution context that produced this tool call.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ApplyPatchToolCallOutputItemParam/properties/caller",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "caller_id"
            },
            {
              "ident": "type"
            }
          ]
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) caller > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) caller > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) output": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApplyPatchToolCallOutputItemParam/properties/output",
    "deprecated": false,
    "key": "output",
    "docstring": "Optional human-readable log text from the apply patch tool (e.g., patch results or errors).",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 10485760
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPListTools/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the list.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) server_label": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPListTools/properties/server_label",
    "deprecated": false,
    "key": "server_label",
    "docstring": "The label of the MCP server.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) tools": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPListTools/properties/tools",
    "deprecated": false,
    "key": "tools",
    "docstring": "The tools available on the server.\n",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/MCPListTools/properties/tools",
      "elementType": {
        "kind": "HttpTypeObject",
        "members": [
          {
            "ident": "input_schema"
          },
          {
            "ident": "name"
          },
          {
            "ident": "annotations"
          },
          {
            "ident": "description"
          }
        ]
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) tools > (items) > (property) input_schema",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) tools > (items) > (property) name",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) tools > (items) > (property) annotations",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) tools > (items) > (property) description"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPListTools/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the item. Always `mcp_list_tools`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/MCPListTools/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "mcp_list_tools"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) error": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPListTools/properties/error",
    "deprecated": false,
    "key": "error",
    "docstring": "Error message if the server could not list tools.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 24 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPApprovalRequest/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the approval request.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 24 > (property) arguments": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPApprovalRequest/properties/arguments",
    "deprecated": false,
    "key": "arguments",
    "docstring": "A JSON string of arguments for the tool.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 24 > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPApprovalRequest/properties/name",
    "deprecated": false,
    "key": "name",
    "docstring": "The name of the tool to run.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 24 > (property) server_label": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPApprovalRequest/properties/server_label",
    "deprecated": false,
    "key": "server_label",
    "docstring": "The label of the MCP server making the request.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 24 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPApprovalRequest/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the item. Always `mcp_approval_request`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/MCPApprovalRequest/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "mcp_approval_request"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 24 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 25 > (property) approval_request_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPApprovalResponse/properties/approval_request_id",
    "deprecated": false,
    "key": "approval_request_id",
    "docstring": "The ID of the approval request being answered.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 25 > (property) approve": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPApprovalResponse/properties/approve",
    "deprecated": false,
    "key": "approve",
    "docstring": "Whether the request was approved.\n",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 25 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPApprovalResponse/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the item. Always `mcp_approval_response`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/MCPApprovalResponse/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "mcp_approval_response"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 25 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 25 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPApprovalResponse/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the approval response\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 25 > (property) reason": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPApprovalResponse/properties/reason",
    "deprecated": false,
    "key": "reason",
    "docstring": "Optional reason for the decision.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolCall/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the tool call.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) arguments": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolCall/properties/arguments",
    "deprecated": false,
    "key": "arguments",
    "docstring": "A JSON string of the arguments passed to the tool.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolCall/properties/name",
    "deprecated": false,
    "key": "name",
    "docstring": "The name of the tool that was run.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) server_label": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolCall/properties/server_label",
    "deprecated": false,
    "key": "server_label",
    "docstring": "The label of the MCP server running the tool.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolCall/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the item. Always `mcp_call`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/MCPToolCall/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "mcp_call"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) approval_request_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolCall/properties/approval_request_id",
    "deprecated": false,
    "key": "approval_request_id",
    "docstring": "Unique identifier for the MCP tool call approval request.\nInclude this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) error": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolCall/properties/error",
    "deprecated": false,
    "key": "error",
    "docstring": "The error from the tool call, if any.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "McpToolCallError",
      "$ref": "(resource) responses > (model) mcp_tool_call_error > (schema)"
    },
    "optional": true,
    "nullable": true,
    "modelImplicit": false,
    "schemaType": "union",
    "modelPath": "(resource) responses > (model) mcp_tool_call_error",
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 0",
      "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 1",
      "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) output": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolCall/properties/output",
    "deprecated": false,
    "key": "output",
    "docstring": "The output from the tool call.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolCall/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/MCPToolCall/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "in_progress"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "calling"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "failed"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) status > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) status > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) status > (member) 3",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) status > (member) 4"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) call_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolCallOutput/properties/call_id",
    "deprecated": false,
    "key": "call_id",
    "docstring": "The call ID, used to map this custom tool call output to a custom tool call.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) output": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolCallOutput/properties/output",
    "deprecated": false,
    "key": "output",
    "docstring": "The output from the custom tool call generated by your code.\nCan be a string or an list of output content.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CustomToolCallOutput/properties/output",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeArray",
          "oasRef": "#/components/schemas/CustomToolCallOutput/properties/output/oneOf/1",
          "elementType": {
            "kind": "HttpTypeUnion",
            "oasRef": "#/components/schemas/CustomToolCallOutput/properties/output/oneOf/1/items",
            "types": [
              {
                "kind": "HttpTypeReference",
                "ident": "ResponseInputText",
                "$ref": "(resource) responses > (model) response_input_text > (schema)"
              },
              {
                "kind": "HttpTypeReference",
                "ident": "ResponseInputImage",
                "$ref": "(resource) responses > (model) response_input_image > (schema)"
              },
              {
                "kind": "HttpTypeReference",
                "ident": "ResponseInputFile",
                "$ref": "(resource) responses > (model) response_input_file > (schema)"
              }
            ]
          }
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) output > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) output > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolCallOutput/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the custom tool call output. Always `custom_tool_call_output`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CustomToolCallOutput/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "custom_tool_call_output"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolCallOutput/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the custom tool call output in the OpenAI platform.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) caller": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolCallOutput/properties/caller",
    "deprecated": false,
    "key": "caller",
    "docstring": "The execution context that produced this tool call.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CustomToolCallOutput/properties/caller",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "caller_id"
            },
            {
              "ident": "type"
            }
          ]
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) caller > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) caller > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) call_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolCall/properties/call_id",
    "deprecated": false,
    "key": "call_id",
    "docstring": "An identifier used to map this custom tool call to a tool call output.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) input": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolCall/properties/input",
    "deprecated": false,
    "key": "input",
    "docstring": "The input for the custom tool call generated by the model.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolCall/properties/name",
    "deprecated": false,
    "key": "name",
    "docstring": "The name of the custom tool being called.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolCall/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the custom tool call. Always `custom_tool_call`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CustomToolCall/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "custom_tool_call"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolCall/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the custom tool call in the OpenAI platform.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) async": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolCall/properties/async",
    "deprecated": false,
    "key": "async",
    "docstring": "Whether the custom tool call runs asynchronously.\n",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) caller": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolCall/properties/caller",
    "deprecated": false,
    "key": "caller",
    "docstring": "The execution context that produced this tool call.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CustomToolCall/properties/caller",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "caller_id"
            },
            {
              "ident": "type"
            }
          ]
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) caller > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) caller > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) namespace": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolCall/properties/namespace",
    "deprecated": false,
    "key": "namespace",
    "docstring": "The namespace of the custom tool being called.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 29 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CompactionTriggerItemParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the item. Always `compaction_trigger`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CompactionTriggerItemParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "compaction_trigger"
        }
      ]
    },
    "default": "compaction_trigger",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 29 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 29 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CompactionTriggerItemParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of this compaction trigger.",
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "msg_123"
    ],
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 30 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ItemReferenceParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The ID of the item to reference.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 30 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ItemReferenceParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of item to reference. Always `item_reference`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ItemReferenceParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "item_reference"
        }
      ]
    },
    "default": "item_reference",
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 30 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 31 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ProgramItemParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of this program item.",
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "cm_123"
    ],
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 31 > (property) call_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ProgramItemParam/properties/call_id",
    "deprecated": false,
    "key": "call_id",
    "docstring": "The stable call ID of the program item.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 31 > (property) code": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ProgramItemParam/properties/code",
    "deprecated": false,
    "key": "code",
    "docstring": "The JavaScript source executed by programmatic tool calling.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 10485760
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 31 > (property) fingerprint": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ProgramItemParam/properties/fingerprint",
    "deprecated": false,
    "key": "fingerprint",
    "docstring": "Opaque program replay fingerprint that must be round-tripped.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 10485760
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 31 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ProgramItemParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The item type. Always `program`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ProgramItemParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "program"
        }
      ]
    },
    "default": "program",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 31 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ProgramOutputItemParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of this program output item.",
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "cmo_123"
    ],
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32 > (property) call_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ProgramOutputItemParam/properties/call_id",
    "deprecated": false,
    "key": "call_id",
    "docstring": "The call ID of the program item.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32 > (property) result": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ProgramOutputItemParam/properties/result",
    "deprecated": false,
    "key": "result",
    "docstring": "The result produced by the program item.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 10485760
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ProgramOutputItemParam/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The terminal status of the program output.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ProgramOutputItemParam/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32 > (property) status > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32 > (property) status > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ProgramOutputItemParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The item type. Always `program_output`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ProgramOutputItemParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "program_output"
        }
      ]
    },
    "default": "program_output",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32 > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) easy_input_message > (schema) > (property) content > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/EasyInputMessage/properties/content/oneOf/0",
    "docstring": "A text input to the model.\n",
    "ident": "TextInput",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) responses > (model) easy_input_message > (schema) > (property) content > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseInputMessageContentList",
      "$ref": "(resource) responses > (model) response_input_message_content_list > (schema)"
    },
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) response_input_content > (schema) > (variant) 0",
      "(resource) responses > (model) response_input_content > (schema) > (variant) 1",
      "(resource) responses > (model) response_input_content > (schema) > (variant) 2"
    ]
  },
  "(resource) responses > (model) response_input_message_content_list > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/InputMessageContentList",
    "docstring": "A list of one or many input items to the model, containing different content \ntypes.\n",
    "ident": "ResponseInputMessageContentList",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/InputMessageContentList",
      "elementType": {
        "kind": "HttpTypeReference",
        "ident": "ResponseInputContent",
        "$ref": "(resource) responses > (model) response_input_content > (schema)"
      }
    },
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) response_input_content > (schema) > (variant) 0",
      "(resource) responses > (model) response_input_content > (schema) > (variant) 1",
      "(resource) responses > (model) response_input_content > (schema) > (variant) 2"
    ]
  },
  "(resource) responses > (model) easy_input_message > (schema) > (property) role > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "user"
    }
  },
  "(resource) responses > (model) easy_input_message > (schema) > (property) role > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "assistant"
    }
  },
  "(resource) responses > (model) easy_input_message > (schema) > (property) role > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "system"
    }
  },
  "(resource) responses > (model) easy_input_message > (schema) > (property) role > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "developer"
    }
  },
  "(resource) responses > (model) easy_input_message > (schema) > (property) phase > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "commentary"
    }
  },
  "(resource) responses > (model) easy_input_message > (schema) > (property) phase > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "final_answer"
    }
  },
  "(resource) responses > (model) easy_input_message > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "message"
    }
  },
  "(resource) responses > (model) response_input_content > (schema) > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseInputText",
      "$ref": "(resource) responses > (model) response_input_text > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_text > (schema) > (property) text",
      "(resource) responses > (model) response_input_text > (schema) > (property) type",
      "(resource) responses > (model) response_input_text > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) responses > (model) response_input_content > (schema) > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseInputImage",
      "$ref": "(resource) responses > (model) response_input_image > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_image > (schema) > (property) detail",
      "(resource) responses > (model) response_input_image > (schema) > (property) type",
      "(resource) responses > (model) response_input_image > (schema) > (property) file_id",
      "(resource) responses > (model) response_input_image > (schema) > (property) image_url",
      "(resource) responses > (model) response_input_image > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) responses > (model) response_input_content > (schema) > (variant) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseInputFile",
      "$ref": "(resource) responses > (model) response_input_file > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_file > (schema) > (property) type",
      "(resource) responses > (model) response_input_file > (schema) > (property) detail",
      "(resource) responses > (model) response_input_file > (schema) > (property) file_data",
      "(resource) responses > (model) response_input_file > (schema) > (property) file_id",
      "(resource) responses > (model) response_input_file > (schema) > (property) file_url",
      "(resource) responses > (model) response_input_file > (schema) > (property) filename",
      "(resource) responses > (model) response_input_file > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) role > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "user"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) role > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "system"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) role > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "developer"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "message"
    }
  },
  "(resource) responses > (model) response_output_message > (schema) > (property) content > (items) > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseOutputText",
      "$ref": "(resource) responses > (model) response_output_text > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations",
      "(resource) responses > (model) response_output_text > (schema) > (property) logprobs",
      "(resource) responses > (model) response_output_text > (schema) > (property) text",
      "(resource) responses > (model) response_output_text > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) response_output_message > (schema) > (property) content > (items) > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseOutputRefusal",
      "$ref": "(resource) responses > (model) response_output_refusal > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_refusal > (schema) > (property) refusal",
      "(resource) responses > (model) response_output_refusal > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) response_output_text > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/OutputTextContent",
    "docstring": "A text output from the model.",
    "ident": "ResponseOutputText",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "annotations"
        },
        {
          "ident": "logprobs"
        },
        {
          "ident": "text"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations",
      "(resource) responses > (model) response_output_text > (schema) > (property) logprobs",
      "(resource) responses > (model) response_output_text > (schema) > (property) text",
      "(resource) responses > (model) response_output_text > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) response_output_refusal > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/RefusalContent",
    "docstring": "A refusal from the model.",
    "ident": "ResponseOutputRefusal",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "refusal"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_refusal > (schema) > (property) refusal",
      "(resource) responses > (model) response_output_refusal > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) response_output_message > (schema) > (property) role > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "assistant"
    }
  },
  "(resource) responses > (model) response_output_message > (schema) > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) responses > (model) response_output_message > (schema) > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) responses > (model) response_output_message > (schema) > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) responses > (model) response_output_message > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "message"
    }
  },
  "(resource) responses > (model) response_output_message > (schema) > (property) phase > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "commentary"
    }
  },
  "(resource) responses > (model) response_output_message > (schema) > (property) phase > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "final_answer"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "searching"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) status > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) status > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "failed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "file_search_call"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results > (items) > (property) attributes": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchToolCall/properties/results/anyOf/0/items/properties/attributes",
    "deprecated": false,
    "key": "attributes",
    "docstring": "Set of 16 key-value pairs that can be attached to an object. This can be\nuseful for storing additional information about the object in a structured\nformat, and querying for objects via API or the dashboard. Keys are strings\nwith a maximum length of 64 characters. Values are strings with a maximum\nlength of 512 characters, booleans, or numbers.\n",
    "type": {
      "kind": "HttpTypeReference",
      "oasRef": "#/components/schemas/FileSearchToolCall/properties/results/anyOf/0/items/properties/attributes",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnion",
          "oasRef": "#/components/schemas/VectorStoreFileAttributes/anyOf/0/additionalProperties",
          "types": [
            {
              "kind": "HttpTypeString"
            },
            {
              "kind": "HttpTypeNumber"
            },
            {
              "kind": "HttpTypeBoolean"
            }
          ]
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "map",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results > (items) > (property) attributes > (items) > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results > (items) > (property) attributes > (items) > (variant) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results > (items) > (property) attributes > (items) > (variant) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results > (items) > (property) file_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchToolCall/properties/results/anyOf/0/items/properties/file_id",
    "deprecated": false,
    "key": "file_id",
    "docstring": "The unique ID of the file.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results > (items) > (property) filename": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchToolCall/properties/results/anyOf/0/items/properties/filename",
    "deprecated": false,
    "key": "filename",
    "docstring": "The name of the file.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results > (items) > (property) score": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchToolCall/properties/results/anyOf/0/items/properties/score",
    "deprecated": false,
    "key": "score",
    "docstring": "The relevance score of the file - a value between 0 and 1.\n",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "format": "float"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results > (items) > (property) text": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchToolCall/properties/results/anyOf/0/items/properties/text",
    "deprecated": false,
    "key": "text",
    "docstring": "The text that was retrieved from the file.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) pending_safety_checks > (items) > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerCallSafetyCheckParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The ID of the pending safety check.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) pending_safety_checks > (items) > (property) code": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerCallSafetyCheckParam/properties/code",
    "deprecated": false,
    "key": "code",
    "docstring": "The type of the pending safety check.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) pending_safety_checks > (items) > (property) message": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerCallSafetyCheckParam/properties/message",
    "deprecated": false,
    "key": "message",
    "docstring": "Details about the pending safety check.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 4 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "computer_call"
    }
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComputerAction/oneOf/0",
    "docstring": "A click action.",
    "ident": "Click",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "button"
        },
        {
          "ident": "type"
        },
        {
          "ident": "x"
        },
        {
          "ident": "y"
        },
        {
          "ident": "keys"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) button",
      "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) type",
      "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) x",
      "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) y",
      "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) keys"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComputerAction/oneOf/1",
    "docstring": "A double click action.",
    "ident": "DoubleClick",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "keys"
        },
        {
          "ident": "type"
        },
        {
          "ident": "x"
        },
        {
          "ident": "y"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 1 > (property) keys",
      "(resource) responses > (model) computer_action > (schema) > (variant) 1 > (property) type",
      "(resource) responses > (model) computer_action > (schema) > (variant) 1 > (property) x",
      "(resource) responses > (model) computer_action > (schema) > (variant) 1 > (property) y"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComputerAction/oneOf/2",
    "docstring": "A drag action.",
    "ident": "Drag",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "path"
        },
        {
          "ident": "type"
        },
        {
          "ident": "keys"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 2 > (property) path",
      "(resource) responses > (model) computer_action > (schema) > (variant) 2 > (property) type",
      "(resource) responses > (model) computer_action > (schema) > (variant) 2 > (property) keys"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 3": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComputerAction/oneOf/3",
    "docstring": "A collection of keypresses the model would like to perform.",
    "ident": "Keypress",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "keys"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 3 > (property) keys",
      "(resource) responses > (model) computer_action > (schema) > (variant) 3 > (property) type"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 4": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComputerAction/oneOf/4",
    "docstring": "A mouse move action.",
    "ident": "Move",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "x"
        },
        {
          "ident": "y"
        },
        {
          "ident": "keys"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 4 > (property) type",
      "(resource) responses > (model) computer_action > (schema) > (variant) 4 > (property) x",
      "(resource) responses > (model) computer_action > (schema) > (variant) 4 > (property) y",
      "(resource) responses > (model) computer_action > (schema) > (variant) 4 > (property) keys"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 5": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComputerAction/oneOf/5",
    "docstring": "A screenshot action.",
    "ident": "Screenshot",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 5 > (property) type"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 6": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComputerAction/oneOf/6",
    "docstring": "A scroll action.",
    "ident": "Scroll",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "scroll_x"
        },
        {
          "ident": "scroll_y"
        },
        {
          "ident": "type"
        },
        {
          "ident": "x"
        },
        {
          "ident": "y"
        },
        {
          "ident": "keys"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 6 > (property) scroll_x",
      "(resource) responses > (model) computer_action > (schema) > (variant) 6 > (property) scroll_y",
      "(resource) responses > (model) computer_action > (schema) > (variant) 6 > (property) type",
      "(resource) responses > (model) computer_action > (schema) > (variant) 6 > (property) x",
      "(resource) responses > (model) computer_action > (schema) > (variant) 6 > (property) y",
      "(resource) responses > (model) computer_action > (schema) > (variant) 6 > (property) keys"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 7": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComputerAction/oneOf/7",
    "docstring": "An action to type in text.",
    "ident": "Type",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "text"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 7 > (property) text",
      "(resource) responses > (model) computer_action > (schema) > (variant) 7 > (property) type"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 8": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComputerAction/oneOf/8",
    "docstring": "A wait action.",
    "ident": "Wait",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 8 > (property) type"
    ]
  },
  "(resource) responses > (model) computer_action > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComputerAction",
    "docstring": "A click action.",
    "ident": "ComputerAction",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ComputerAction",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "button"
            },
            {
              "ident": "type"
            },
            {
              "ident": "x"
            },
            {
              "ident": "y"
            },
            {
              "ident": "keys"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "keys"
            },
            {
              "ident": "type"
            },
            {
              "ident": "x"
            },
            {
              "ident": "y"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "path"
            },
            {
              "ident": "type"
            },
            {
              "ident": "keys"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "keys"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            },
            {
              "ident": "x"
            },
            {
              "ident": "y"
            },
            {
              "ident": "keys"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "scroll_x"
            },
            {
              "ident": "scroll_y"
            },
            {
              "ident": "type"
            },
            {
              "ident": "x"
            },
            {
              "ident": "y"
            },
            {
              "ident": "keys"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "text"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            }
          ]
        }
      ]
    },
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 0",
      "(resource) responses > (model) computer_action > (schema) > (variant) 1",
      "(resource) responses > (model) computer_action > (schema) > (variant) 2",
      "(resource) responses > (model) computer_action > (schema) > (variant) 3",
      "(resource) responses > (model) computer_action > (schema) > (variant) 4",
      "(resource) responses > (model) computer_action > (schema) > (variant) 5",
      "(resource) responses > (model) computer_action > (schema) > (variant) 6",
      "(resource) responses > (model) computer_action > (schema) > (variant) 7",
      "(resource) responses > (model) computer_action > (schema) > (variant) 8"
    ]
  },
  "(resource) responses > (model) computer_action_list > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComputerActionList",
    "docstring": "Flattened batched actions for `computer_use`. Each action includes an\n`type` discriminator and action-specific fields.\n",
    "ident": "ComputerActionList",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/ComputerActionList",
      "elementType": {
        "kind": "HttpTypeReference",
        "ident": "ComputerAction",
        "$ref": "(resource) responses > (model) computer_action > (schema)"
      }
    },
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 0",
      "(resource) responses > (model) computer_action > (schema) > (variant) 1",
      "(resource) responses > (model) computer_action > (schema) > (variant) 2",
      "(resource) responses > (model) computer_action > (schema) > (variant) 3",
      "(resource) responses > (model) computer_action > (schema) > (variant) 4",
      "(resource) responses > (model) computer_action > (schema) > (variant) 5",
      "(resource) responses > (model) computer_action > (schema) > (variant) 6",
      "(resource) responses > (model) computer_action > (schema) > (variant) 7",
      "(resource) responses > (model) computer_action > (schema) > (variant) 8"
    ]
  },
  "(resource) responses > (model) response_computer_tool_call_output_screenshot > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerScreenshotImage/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Specifies the event type. For a computer screenshot, this property is \nalways set to `computer_screenshot`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ComputerScreenshotImage/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "computer_screenshot"
        }
      ]
    },
    "default": "computer_screenshot",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_computer_tool_call_output_screenshot > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_computer_tool_call_output_screenshot > (schema) > (property) file_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerScreenshotImage/properties/file_id",
    "deprecated": false,
    "key": "file_id",
    "docstring": "The identifier of an uploaded file that contains the screenshot.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_computer_tool_call_output_screenshot > (schema) > (property) image_url": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerScreenshotImage/properties/image_url",
    "deprecated": false,
    "key": "image_url",
    "docstring": "The URL of the screenshot image.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "format": "uri"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_computer_tool_call_output_screenshot > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComputerScreenshotImage",
    "docstring": "A computer screenshot image used with the computer use tool.\n",
    "ident": "ResponseComputerToolCallOutputScreenshot",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "file_id"
        },
        {
          "ident": "image_url"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_computer_tool_call_output_screenshot > (schema) > (property) type",
      "(resource) responses > (model) response_computer_tool_call_output_screenshot > (schema) > (property) file_id",
      "(resource) responses > (model) response_computer_tool_call_output_screenshot > (schema) > (property) image_url"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "computer_call_output"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) acknowledged_safety_checks > (items) > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerCallSafetyCheckParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The ID of the pending safety check.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) acknowledged_safety_checks > (items) > (property) code": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerCallSafetyCheckParam/properties/code",
    "deprecated": false,
    "key": "code",
    "docstring": "The type of the pending safety check.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) acknowledged_safety_checks > (items) > (property) message": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerCallSafetyCheckParam/properties/message",
    "deprecated": false,
    "key": "message",
    "docstring": "Details about the pending safety check.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 5 > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/WebSearchToolCall/properties/action/oneOf/0",
    "docstring": "Action type \"search\" - Performs a web search query.\n",
    "ident": "Search",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "queries"
        },
        {
          "ident": "query"
        },
        {
          "ident": "sources"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0 > (property) queries",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0 > (property) query",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0 > (property) sources"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/WebSearchToolCall/properties/action/oneOf/1",
    "docstring": "Action type \"open_page\" - Opens a specific URL from search results.\n",
    "ident": "OpenPage",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "url"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 1 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 1 > (property) url"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/WebSearchToolCall/properties/action/oneOf/2",
    "docstring": "Action type \"find_in_page\": Searches for a pattern within a loaded page.\n",
    "ident": "FindInPage",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "pattern"
        },
        {
          "ident": "type"
        },
        {
          "ident": "url"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 2 > (property) pattern",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 2 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 2 > (property) url"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "searching"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) status > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "failed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) status > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "web_search_call"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function_call"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) caller > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolCallCaller/oneOf/0",
    "ident": "Direct",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) caller > (variant) 0 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) caller > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolCallCaller/oneOf/1",
    "ident": "Program",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "caller_id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) caller > (variant) 1 > (property) caller_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) caller > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) output > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/output/oneOf/0",
    "docstring": "A JSON string of the output of the function tool call.",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) output > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/output/oneOf/1",
    "docstring": "An array of content outputs (text, image, file) for the function tool call.",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/output/oneOf/1",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/FunctionCallOutputItemParam/properties/output/oneOf/1/items",
        "types": [
          {
            "kind": "HttpTypeReference",
            "ident": "ResponseInputTextContent",
            "$ref": "(resource) responses > (model) response_input_text_content > (schema)"
          },
          {
            "kind": "HttpTypeReference",
            "ident": "ResponseInputImageContent",
            "$ref": "(resource) responses > (model) response_input_image_content > (schema)"
          },
          {
            "kind": "HttpTypeReference",
            "ident": "ResponseInputFileContent",
            "$ref": "(resource) responses > (model) response_input_file_content > (schema)"
          }
        ]
      }
    },
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) output > (variant) 1 > (items) > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) output > (variant) 1 > (items) > (variant) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) output > (variant) 1 > (items) > (variant) 2"
    ]
  },
  "(resource) responses > (model) response_input_text_content > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/InputTextContentParam",
    "docstring": "A text input to the model.",
    "ident": "ResponseInputTextContent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "text"
        },
        {
          "ident": "type"
        },
        {
          "ident": "prompt_cache_breakpoint"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_text_content > (schema) > (property) text",
      "(resource) responses > (model) response_input_text_content > (schema) > (property) type",
      "(resource) responses > (model) response_input_text_content > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) responses > (model) response_input_image_content > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/InputImageContentParamAutoParam",
    "docstring": "An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision)",
    "ident": "ResponseInputImageContent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "detail"
        },
        {
          "ident": "file_id"
        },
        {
          "ident": "image_url"
        },
        {
          "ident": "prompt_cache_breakpoint"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_image_content > (schema) > (property) type",
      "(resource) responses > (model) response_input_image_content > (schema) > (property) detail",
      "(resource) responses > (model) response_input_image_content > (schema) > (property) file_id",
      "(resource) responses > (model) response_input_image_content > (schema) > (property) image_url",
      "(resource) responses > (model) response_input_image_content > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) responses > (model) response_input_file_content > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/InputFileContentParam",
    "docstring": "A file input to the model.",
    "ident": "ResponseInputFileContent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "detail"
        },
        {
          "ident": "file_data"
        },
        {
          "ident": "file_id"
        },
        {
          "ident": "file_url"
        },
        {
          "ident": "filename"
        },
        {
          "ident": "prompt_cache_breakpoint"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_file_content > (schema) > (property) type",
      "(resource) responses > (model) response_input_file_content > (schema) > (property) detail",
      "(resource) responses > (model) response_input_file_content > (schema) > (property) file_data",
      "(resource) responses > (model) response_input_file_content > (schema) > (property) file_id",
      "(resource) responses > (model) response_input_file_content > (schema) > (property) file_url",
      "(resource) responses > (model) response_input_file_content > (schema) > (property) filename",
      "(resource) responses > (model) response_input_file_content > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function_call_output"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) caller > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolCallCallerParam/oneOf/0",
    "ident": "Direct",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) caller > (variant) 0 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) caller > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolCallCallerParam/oneOf/1",
    "ident": "Program",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "caller_id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) caller > (variant) 1 > (property) caller_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) caller > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "tool_search_call"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) execution > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "server"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) execution > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "client"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 9 > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/0",
    "docstring": "Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).",
    "ident": "Function",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        },
        {
          "ident": "parameters"
        },
        {
          "ident": "strict"
        },
        {
          "ident": "type"
        },
        {
          "ident": "allowed_callers"
        },
        {
          "ident": "async"
        },
        {
          "ident": "defer_loading"
        },
        {
          "ident": "description"
        },
        {
          "ident": "output_schema"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) name",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) parameters",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) strict",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) allowed_callers",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) async",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) defer_loading",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) description",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) output_schema"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/1",
    "docstring": "A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).",
    "ident": "FileSearch",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "vector_store_ids"
        },
        {
          "ident": "filters"
        },
        {
          "ident": "max_num_results"
        },
        {
          "ident": "ranking_options"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) vector_store_ids",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) filters",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) max_num_results",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) ranking_options"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/2",
    "docstring": "A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).",
    "ident": "Computer",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 2 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/3",
    "docstring": "A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).",
    "ident": "ComputerUsePreview",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "display_height"
        },
        {
          "ident": "display_width"
        },
        {
          "ident": "environment"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) display_height",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) display_width",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) environment",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/4",
    "docstring": "Search the Internet for sources related to the prompt. Learn more about the\n[web search tool](/api/docs/guides/tools-web-search).\n",
    "ident": "WebSearch",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "external_web_access"
        },
        {
          "ident": "filters"
        },
        {
          "ident": "search_context_size"
        },
        {
          "ident": "user_location"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) external_web_access",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) filters",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) search_context_size",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) user_location"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/5",
    "docstring": "Give the model access to additional tools via remote Model Context Protocol\n(MCP) servers. [Learn more about MCP](/api/docs/guides/tools-connectors-mcp).\n",
    "ident": "Mcp",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "server_label"
        },
        {
          "ident": "type"
        },
        {
          "ident": "allowed_callers"
        },
        {
          "ident": "allowed_tools"
        },
        {
          "ident": "authorization"
        },
        {
          "ident": "connector_id"
        },
        {
          "ident": "defer_loading"
        },
        {
          "ident": "headers"
        },
        {
          "ident": "require_approval"
        },
        {
          "ident": "server_description"
        },
        {
          "ident": "server_url"
        },
        {
          "ident": "tunnel_id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) server_label",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) allowed_callers",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) allowed_tools",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) authorization",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) defer_loading",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) headers",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) server_description",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) server_url",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) tunnel_id"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/6",
    "docstring": "A tool that runs Python code to help generate a response to a prompt.\n",
    "ident": "CodeInterpreter",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "container"
        },
        {
          "ident": "type"
        },
        {
          "ident": "allowed_callers"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) allowed_callers"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 7": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/7",
    "ident": "ProgrammaticToolCalling",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 7 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/8",
    "docstring": "A tool that generates images using the GPT image models.\n",
    "ident": "ImageGeneration",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "action"
        },
        {
          "ident": "background"
        },
        {
          "ident": "input_fidelity"
        },
        {
          "ident": "input_image_mask"
        },
        {
          "ident": "model"
        },
        {
          "ident": "moderation"
        },
        {
          "ident": "output_compression"
        },
        {
          "ident": "output_format"
        },
        {
          "ident": "partial_images"
        },
        {
          "ident": "quality"
        },
        {
          "ident": "size"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) action",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) background",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) input_fidelity",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) input_image_mask",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) moderation",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) output_compression",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) output_format",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) partial_images",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) quality",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) size"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 9": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/9",
    "docstring": "A tool that allows the model to execute shell commands in a local environment.",
    "ident": "LocalShell",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 9 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/10",
    "docstring": "A tool that allows the model to execute shell commands.",
    "ident": "Shell",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "allowed_callers"
        },
        {
          "ident": "environment"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) allowed_callers",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) environment"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/11",
    "docstring": "A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)",
    "ident": "Custom",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        },
        {
          "ident": "type"
        },
        {
          "ident": "allowed_callers"
        },
        {
          "ident": "async"
        },
        {
          "ident": "defer_loading"
        },
        {
          "ident": "description"
        },
        {
          "ident": "format"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) name",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) allowed_callers",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) async",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) defer_loading",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) description",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) format"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/12",
    "docstring": "Groups function/custom tools under a shared namespace.",
    "ident": "Namespace",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "description"
        },
        {
          "ident": "name"
        },
        {
          "ident": "tools"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) description",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) name",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 13": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/13",
    "docstring": "Hosted or BYOT tool search configuration for deferred tools.",
    "ident": "ToolSearch",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "description"
        },
        {
          "ident": "execution"
        },
        {
          "ident": "parameters"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 13 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 13 > (property) description",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 13 > (property) execution",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 13 > (property) parameters"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/14",
    "docstring": "This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).",
    "ident": "WebSearchPreview",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "search_content_types"
        },
        {
          "ident": "search_context_size"
        },
        {
          "ident": "user_location"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) search_content_types",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) search_context_size",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) user_location"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 15": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/15",
    "docstring": "Allows the assistant to create, delete, or update files using unified diffs.",
    "ident": "ApplyPatch",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "allowed_callers"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 15 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 15 > (property) allowed_callers"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "tool_search_output"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) execution > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "server"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) execution > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "client"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) role > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "developer"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/0",
    "docstring": "Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).",
    "ident": "Function",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        },
        {
          "ident": "parameters"
        },
        {
          "ident": "strict"
        },
        {
          "ident": "type"
        },
        {
          "ident": "allowed_callers"
        },
        {
          "ident": "async"
        },
        {
          "ident": "defer_loading"
        },
        {
          "ident": "description"
        },
        {
          "ident": "output_schema"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) name",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) parameters",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) strict",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) allowed_callers",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) async",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) defer_loading",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) description",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) output_schema"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/1",
    "docstring": "A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).",
    "ident": "FileSearch",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "vector_store_ids"
        },
        {
          "ident": "filters"
        },
        {
          "ident": "max_num_results"
        },
        {
          "ident": "ranking_options"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) vector_store_ids",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) filters",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) max_num_results",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) ranking_options"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/2",
    "docstring": "A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).",
    "ident": "Computer",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 2 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/3",
    "docstring": "A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).",
    "ident": "ComputerUsePreview",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "display_height"
        },
        {
          "ident": "display_width"
        },
        {
          "ident": "environment"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) display_height",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) display_width",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) environment",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/4",
    "docstring": "Search the Internet for sources related to the prompt. Learn more about the\n[web search tool](/api/docs/guides/tools-web-search).\n",
    "ident": "WebSearch",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "external_web_access"
        },
        {
          "ident": "filters"
        },
        {
          "ident": "search_context_size"
        },
        {
          "ident": "user_location"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) external_web_access",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) filters",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) search_context_size",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) user_location"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/5",
    "docstring": "Give the model access to additional tools via remote Model Context Protocol\n(MCP) servers. [Learn more about MCP](/api/docs/guides/tools-connectors-mcp).\n",
    "ident": "Mcp",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "server_label"
        },
        {
          "ident": "type"
        },
        {
          "ident": "allowed_callers"
        },
        {
          "ident": "allowed_tools"
        },
        {
          "ident": "authorization"
        },
        {
          "ident": "connector_id"
        },
        {
          "ident": "defer_loading"
        },
        {
          "ident": "headers"
        },
        {
          "ident": "require_approval"
        },
        {
          "ident": "server_description"
        },
        {
          "ident": "server_url"
        },
        {
          "ident": "tunnel_id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) server_label",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) allowed_callers",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) allowed_tools",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) authorization",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) defer_loading",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) headers",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) server_description",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) server_url",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) tunnel_id"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/6",
    "docstring": "A tool that runs Python code to help generate a response to a prompt.\n",
    "ident": "CodeInterpreter",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "container"
        },
        {
          "ident": "type"
        },
        {
          "ident": "allowed_callers"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) allowed_callers"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 7": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/7",
    "ident": "ProgrammaticToolCalling",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 7 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/8",
    "docstring": "A tool that generates images using the GPT image models.\n",
    "ident": "ImageGeneration",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "action"
        },
        {
          "ident": "background"
        },
        {
          "ident": "input_fidelity"
        },
        {
          "ident": "input_image_mask"
        },
        {
          "ident": "model"
        },
        {
          "ident": "moderation"
        },
        {
          "ident": "output_compression"
        },
        {
          "ident": "output_format"
        },
        {
          "ident": "partial_images"
        },
        {
          "ident": "quality"
        },
        {
          "ident": "size"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) action",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) background",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) input_fidelity",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) input_image_mask",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) moderation",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) output_compression",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) output_format",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) partial_images",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) quality",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) size"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 9": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/9",
    "docstring": "A tool that allows the model to execute shell commands in a local environment.",
    "ident": "LocalShell",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 9 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 10": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/10",
    "docstring": "A tool that allows the model to execute shell commands.",
    "ident": "Shell",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "allowed_callers"
        },
        {
          "ident": "environment"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 10 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 10 > (property) allowed_callers",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 10 > (property) environment"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 11": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/11",
    "docstring": "A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)",
    "ident": "Custom",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "name"
        },
        {
          "ident": "type"
        },
        {
          "ident": "allowed_callers"
        },
        {
          "ident": "async"
        },
        {
          "ident": "defer_loading"
        },
        {
          "ident": "description"
        },
        {
          "ident": "format"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 11 > (property) name",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 11 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 11 > (property) allowed_callers",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 11 > (property) async",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 11 > (property) defer_loading",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 11 > (property) description",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 11 > (property) format"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/12",
    "docstring": "Groups function/custom tools under a shared namespace.",
    "ident": "Namespace",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "description"
        },
        {
          "ident": "name"
        },
        {
          "ident": "tools"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) description",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) name",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 13": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/13",
    "docstring": "Hosted or BYOT tool search configuration for deferred tools.",
    "ident": "ToolSearch",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "description"
        },
        {
          "ident": "execution"
        },
        {
          "ident": "parameters"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 13 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 13 > (property) description",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 13 > (property) execution",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 13 > (property) parameters"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/14",
    "docstring": "This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).",
    "ident": "WebSearchPreview",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "search_content_types"
        },
        {
          "ident": "search_context_size"
        },
        {
          "ident": "user_location"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) search_content_types",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) search_context_size",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) user_location"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 15": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Tool/oneOf/15",
    "docstring": "Allows the assistant to create, delete, or update files using unified diffs.",
    "ident": "ApplyPatch",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "allowed_callers"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 15 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 15 > (property) allowed_callers"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "additional_tools"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 12 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "configuration_update"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 12 > (property) reasoning > (property) effort": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ResponseConfigurationUpdateItemParam/properties/reasoning/properties/effort",
    "deprecated": false,
    "key": "effort",
    "docstring": "The reasoning effort to use for subsequent responses until another\nconfiguration update replaces it.\n",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ReasoningEffort",
      "$ref": "(resource) $shared > (model) reasoning_effort > (schema)"
    },
    "default": "medium",
    "optional": true,
    "nullable": true,
    "modelImplicit": false,
    "schemaType": "enum",
    "modelPath": "(resource) $shared > (model) reasoning_effort",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) $shared > (model) reasoning_effort > (schema) > (member) 0",
      "(resource) $shared > (model) reasoning_effort > (schema) > (member) 1",
      "(resource) $shared > (model) reasoning_effort > (schema) > (member) 2",
      "(resource) $shared > (model) reasoning_effort > (schema) > (member) 3",
      "(resource) $shared > (model) reasoning_effort > (schema) > (member) 4",
      "(resource) $shared > (model) reasoning_effort > (schema) > (member) 5",
      "(resource) $shared > (model) reasoning_effort > (schema) > (member) 6"
    ]
  },
  "(resource) conversations > (model) summary_text_content > (schema) > (property) text": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/SummaryTextContent/properties/text",
    "deprecated": false,
    "key": "text",
    "docstring": "A summary of the reasoning output from the model so far.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) conversations > (model) summary_text_content > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/SummaryTextContent/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the object. Always `summary_text`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/SummaryTextContent/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "summary_text"
        }
      ]
    },
    "default": "summary_text",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) conversations > (model) summary_text_content > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) conversations > (model) summary_text_content > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/SummaryTextContent",
    "docstring": "A summary text from the model.",
    "ident": "SummaryTextContent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "text"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) conversations > (model) summary_text_content > (schema) > (property) text",
      "(resource) conversations > (model) summary_text_content > (schema) > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "reasoning"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) content > (items) > (property) text": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ReasoningTextContent/properties/text",
    "deprecated": false,
    "key": "text",
    "docstring": "The reasoning text from the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) content > (items) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ReasoningTextContent/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the reasoning text. Always `reasoning_text`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ReasoningTextContent/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "reasoning_text"
        }
      ]
    },
    "default": "reasoning_text",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) content > (items) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 13 > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 14 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "compaction"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "generating"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) status > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "failed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "image_generation_call"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) action > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "generate"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) action > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "edit"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) action > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) background > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "transparent"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) background > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "opaque"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) background > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) output_format > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "png"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) output_format > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "webp"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) output_format > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "jpeg"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) quality > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) quality > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "medium"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) quality > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) quality > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "xhigh"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) quality > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "max"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) quality > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) size > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ImageGenToolCall/properties/size/anyOf/0/anyOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) size > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ImageGenToolCall/properties/size/anyOf/0/anyOf/1",
    "docstring": "The image dimensions as a `WIDTHxHEIGHT` string, for example `1536x864`.",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenToolCall/properties/size/anyOf/0/anyOf/1",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "1024x1024"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "1024x1536"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "1536x1024"
        }
      ]
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) size > (variant) 1 > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) size > (variant) 1 > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 15 > (property) size > (variant) 1 > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) outputs > (items) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/CodeInterpreterToolCall/properties/outputs/anyOf/0/items/oneOf/0",
    "docstring": "The logs output from the code interpreter.",
    "ident": "Logs",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "logs"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) outputs > (items) > (variant) 0 > (property) logs",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) outputs > (items) > (variant) 0 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) outputs > (items) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/CodeInterpreterToolCall/properties/outputs/anyOf/0/items/oneOf/1",
    "docstring": "The image output from the code interpreter.",
    "ident": "Image",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "url"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) outputs > (items) > (variant) 1 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) outputs > (items) > (variant) 1 > (property) url"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) status > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "interpreting"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) status > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "failed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "code_interpreter_call"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) action > (property) command": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalShellExecAction/properties/command",
    "deprecated": false,
    "key": "command",
    "docstring": "The command to run.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/LocalShellExecAction/properties/command",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) action > (property) env": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalShellExecAction/properties/env",
    "deprecated": false,
    "key": "env",
    "docstring": "Environment variables to set for the command.",
    "type": {
      "kind": "HttpTypeReference",
      "oasRef": "#/components/schemas/LocalShellExecAction/properties/env",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeString"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "map",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) action > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalShellExecAction/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the local shell action. Always `exec`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LocalShellExecAction/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "exec"
        }
      ]
    },
    "default": "exec",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) action > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) action > (property) timeout_ms": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalShellExecAction/properties/timeout_ms",
    "deprecated": false,
    "key": "timeout_ms",
    "docstring": "Optional timeout in milliseconds for the command.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) action > (property) user": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalShellExecAction/properties/user",
    "deprecated": false,
    "key": "user",
    "docstring": "Optional user to run the command as.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) action > (property) working_directory": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalShellExecAction/properties/working_directory",
    "deprecated": false,
    "key": "working_directory",
    "docstring": "Optional working directory to run the command in.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 17 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "local_shell_call"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "local_shell_call_output"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 18 > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) action > (property) commands": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellActionParam/properties/commands",
    "deprecated": false,
    "key": "commands",
    "docstring": "Ordered shell commands for the execution environment to run.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/FunctionShellActionParam/properties/commands",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) action > (property) max_output_length": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellActionParam/properties/max_output_length",
    "deprecated": false,
    "key": "max_output_length",
    "docstring": "Maximum number of UTF-8 characters to capture from combined stdout and stderr output.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) action > (property) timeout_ms": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellActionParam/properties/timeout_ms",
    "deprecated": false,
    "key": "timeout_ms",
    "docstring": "Maximum wall-clock time in milliseconds to allow the shell commands to run.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "shell_call"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) caller > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolCallCallerParam/oneOf/0",
    "ident": "Direct",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) caller > (variant) 0 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) caller > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolCallCallerParam/oneOf/1",
    "ident": "Program",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "caller_id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) caller > (variant) 1 > (property) caller_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) caller > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) environment > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "LocalEnvironment",
      "$ref": "(resource) responses > (model) local_environment > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) local_environment > (schema) > (property) type",
      "(resource) responses > (model) local_environment > (schema) > (property) skills"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) environment > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ContainerReference",
      "$ref": "(resource) responses > (model) container_reference > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) container_reference > (schema) > (property) container_id",
      "(resource) responses > (model) container_reference > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) local_environment > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LocalEnvironmentParam",
    "ident": "LocalEnvironment",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "skills"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) local_environment > (schema) > (property) type",
      "(resource) responses > (model) local_environment > (schema) > (property) skills"
    ]
  },
  "(resource) responses > (model) container_reference > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ContainerReferenceParam",
    "ident": "ContainerReference",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "container_id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) container_reference > (schema) > (property) container_id",
      "(resource) responses > (model) container_reference > (schema) > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) outcome": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallOutputContentParam/properties/outcome",
    "deprecated": false,
    "key": "outcome",
    "docstring": "The exit or timeout outcome associated with this shell call.",
    "title": "Shell call outcome",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionShellCallOutputContentParam/properties/outcome",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "exit_code"
            },
            {
              "ident": "type"
            }
          ]
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) outcome > (variant) 0",
      "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) outcome > (variant) 1"
    ]
  },
  "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) stderr": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallOutputContentParam/properties/stderr",
    "deprecated": false,
    "key": "stderr",
    "docstring": "Captured stderr output for the shell call.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 10485760
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) stdout": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallOutputContentParam/properties/stdout",
    "deprecated": false,
    "key": "stdout",
    "docstring": "Captured stdout output for the shell call.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 10485760
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_function_shell_call_output_content > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/FunctionShellCallOutputContentParam",
    "docstring": "Captured stdout and stderr for a portion of a shell tool call output.",
    "ident": "ResponseFunctionShellCallOutputContent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "outcome"
        },
        {
          "ident": "stderr"
        },
        {
          "ident": "stdout"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) outcome",
      "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) stderr",
      "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) stdout"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "shell_call_output"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) caller > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolCallCallerParam/oneOf/0",
    "ident": "Direct",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) caller > (variant) 0 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) caller > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolCallCallerParam/oneOf/1",
    "ident": "Program",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "caller_id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) caller > (variant) 1 > (property) caller_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) caller > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ApplyPatchOperationParam/oneOf/0",
    "docstring": "Instruction for creating a new file via the apply_patch tool.",
    "ident": "CreateFile",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "diff"
        },
        {
          "ident": "path"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation > (variant) 0 > (property) diff",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation > (variant) 0 > (property) path",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation > (variant) 0 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ApplyPatchOperationParam/oneOf/1",
    "docstring": "Instruction for deleting an existing file via the apply_patch tool.",
    "ident": "DeleteFile",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "path"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation > (variant) 1 > (property) path",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ApplyPatchOperationParam/oneOf/2",
    "docstring": "Instruction for updating an existing file via the apply_patch tool.",
    "ident": "UpdateFile",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "diff"
        },
        {
          "ident": "path"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation > (variant) 2 > (property) diff",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation > (variant) 2 > (property) path",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation > (variant) 2 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "apply_patch_call"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) caller > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolCallCallerParam/oneOf/0",
    "ident": "Direct",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) caller > (variant) 0 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) caller > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolCallCallerParam/oneOf/1",
    "ident": "Program",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "caller_id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) caller > (variant) 1 > (property) caller_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) caller > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "failed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "apply_patch_call_output"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) caller > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolCallCallerParam/oneOf/0",
    "ident": "Direct",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) caller > (variant) 0 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) caller > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolCallCallerParam/oneOf/1",
    "ident": "Program",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "caller_id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) caller > (variant) 1 > (property) caller_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) caller > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) tools > (items) > (property) input_schema": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPListToolsTool/properties/input_schema",
    "deprecated": false,
    "key": "input_schema",
    "docstring": "The JSON schema describing the tool's input.\n",
    "type": {
      "kind": "HttpTypeUnknown"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "unknown",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) tools > (items) > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPListToolsTool/properties/name",
    "deprecated": false,
    "key": "name",
    "docstring": "The name of the tool.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) tools > (items) > (property) annotations": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPListToolsTool/properties/annotations",
    "deprecated": false,
    "key": "annotations",
    "docstring": "Additional annotations about the tool.\n",
    "type": {
      "kind": "HttpTypeUnknown"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "unknown",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) tools > (items) > (property) description": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPListToolsTool/properties/description",
    "deprecated": false,
    "key": "description",
    "docstring": "The description of the tool.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 23 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mcp_list_tools"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 24 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mcp_approval_request"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 25 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mcp_approval_response"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mcp_call"
    }
  },
  "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/MCPToolCallError/oneOf/0",
    "ident": "McpProtocolError",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "code"
        },
        {
          "ident": "message"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 0 > (property) code",
      "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 0 > (property) message",
      "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 0 > (property) type"
    ]
  },
  "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/MCPToolCallError/oneOf/1",
    "ident": "McpToolExecutionError",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "content"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 1 > (property) content",
      "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 1 > (property) type"
    ]
  },
  "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/MCPToolCallError/oneOf/2",
    "ident": "HTTPError",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "code"
        },
        {
          "ident": "message"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 2 > (property) code",
      "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 2 > (property) message",
      "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 2 > (property) type"
    ]
  },
  "(resource) responses > (model) mcp_tool_call_error > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/MCPToolCallError",
    "ident": "McpToolCallError",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/MCPToolCallError",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "code"
            },
            {
              "ident": "message"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "content"
            },
            {
              "ident": "type"
            }
          ]
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "code"
            },
            {
              "ident": "message"
            },
            {
              "ident": "type"
            }
          ]
        }
      ]
    },
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 0",
      "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 1",
      "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in_progress"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) status > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) status > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "calling"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 26 > (property) status > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "failed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) output > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/CustomToolCallOutput/properties/output/oneOf/0",
    "docstring": "A string of the output of the custom tool call.\n",
    "ident": "StringOutput",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) output > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/CustomToolCallOutput/properties/output/oneOf/1",
    "docstring": "Text, image, or file output of the custom tool call.\n",
    "ident": "OutputContentList",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/CustomToolCallOutput/properties/output/oneOf/1",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/CustomToolCallOutput/properties/output/oneOf/1/items",
        "types": [
          {
            "kind": "HttpTypeReference",
            "ident": "ResponseInputText",
            "$ref": "(resource) responses > (model) response_input_text > (schema)"
          },
          {
            "kind": "HttpTypeReference",
            "ident": "ResponseInputImage",
            "$ref": "(resource) responses > (model) response_input_image > (schema)"
          },
          {
            "kind": "HttpTypeReference",
            "ident": "ResponseInputFile",
            "$ref": "(resource) responses > (model) response_input_file > (schema)"
          }
        ]
      }
    },
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) output > (variant) 1 > (items) > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) output > (variant) 1 > (items) > (variant) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) output > (variant) 1 > (items) > (variant) 2"
    ]
  },
  "(resource) responses > (model) response_input_text > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/InputTextContent",
    "docstring": "A text input to the model.",
    "ident": "ResponseInputText",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "text"
        },
        {
          "ident": "type"
        },
        {
          "ident": "prompt_cache_breakpoint"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_text > (schema) > (property) text",
      "(resource) responses > (model) response_input_text > (schema) > (property) type",
      "(resource) responses > (model) response_input_text > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) responses > (model) response_input_image > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/InputImageContent",
    "docstring": "An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).",
    "ident": "ResponseInputImage",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "detail"
        },
        {
          "ident": "type"
        },
        {
          "ident": "file_id"
        },
        {
          "ident": "image_url"
        },
        {
          "ident": "prompt_cache_breakpoint"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_image > (schema) > (property) detail",
      "(resource) responses > (model) response_input_image > (schema) > (property) type",
      "(resource) responses > (model) response_input_image > (schema) > (property) file_id",
      "(resource) responses > (model) response_input_image > (schema) > (property) image_url",
      "(resource) responses > (model) response_input_image > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) responses > (model) response_input_file > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/InputFileContent",
    "docstring": "A file input to the model.",
    "ident": "ResponseInputFile",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "detail"
        },
        {
          "ident": "file_data"
        },
        {
          "ident": "file_id"
        },
        {
          "ident": "file_url"
        },
        {
          "ident": "filename"
        },
        {
          "ident": "prompt_cache_breakpoint"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_file > (schema) > (property) type",
      "(resource) responses > (model) response_input_file > (schema) > (property) detail",
      "(resource) responses > (model) response_input_file > (schema) > (property) file_data",
      "(resource) responses > (model) response_input_file > (schema) > (property) file_id",
      "(resource) responses > (model) response_input_file > (schema) > (property) file_url",
      "(resource) responses > (model) response_input_file > (schema) > (property) filename",
      "(resource) responses > (model) response_input_file > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "custom_tool_call_output"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) caller > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolCallCallerParam/oneOf/0",
    "ident": "Direct",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) caller > (variant) 0 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) caller > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolCallCallerParam/oneOf/1",
    "ident": "Program",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "caller_id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) caller > (variant) 1 > (property) caller_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) caller > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "custom_tool_call"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) caller > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolCallCaller/oneOf/0",
    "ident": "Direct",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) caller > (variant) 0 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) caller > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ToolCallCaller/oneOf/1",
    "ident": "Program",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "caller_id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) caller > (variant) 1 > (property) caller_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) caller > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 29 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "compaction_trigger"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 30 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "item_reference"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 31 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "program"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 32 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "program_output"
    }
  },
  "(resource) responses > (model) response_input_content > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/InputContent",
    "docstring": "A text input to the model.",
    "ident": "ResponseInputContent",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/InputContent",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "ResponseInputText",
          "$ref": "(resource) responses > (model) response_input_text > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ResponseInputImage",
          "$ref": "(resource) responses > (model) response_input_image > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ResponseInputFile",
          "$ref": "(resource) responses > (model) response_input_file > (schema)"
        }
      ]
    },
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) response_input_content > (schema) > (variant) 0",
      "(resource) responses > (model) response_input_content > (schema) > (variant) 1",
      "(resource) responses > (model) response_input_content > (schema) > (variant) 2"
    ]
  },
  "(resource) responses > (model) response_input_text > (schema) > (property) text": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputTextContent/properties/text",
    "deprecated": false,
    "key": "text",
    "docstring": "The text input to the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_text > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputTextContent/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the input item. Always `input_text`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/InputTextContent/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "input_text"
        }
      ]
    },
    "default": "input_text",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_text > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_input_text > (schema) > (property) prompt_cache_breakpoint": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputTextContent/properties/prompt_cache_breakpoint",
    "deprecated": false,
    "key": "prompt_cache_breakpoint",
    "docstring": "Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.",
    "title": "Prompt cache breakpoint",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "mode"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_text > (schema) > (property) prompt_cache_breakpoint > (property) mode"
    ]
  },
  "(resource) responses > (model) response_input_image > (schema) > (property) detail": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputImageContent/properties/detail",
    "deprecated": false,
    "key": "detail",
    "docstring": "The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ImageDetail",
      "$ref": "(resource) responses > (model) image_detail > (schema)"
    },
    "optional": false,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "enum",
    "modelPath": "(resource) responses > (model) image_detail",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) image_detail > (schema) > (member) 0",
      "(resource) responses > (model) image_detail > (schema) > (member) 1",
      "(resource) responses > (model) image_detail > (schema) > (member) 2",
      "(resource) responses > (model) image_detail > (schema) > (member) 3"
    ]
  },
  "(resource) responses > (model) response_input_image > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputImageContent/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the input item. Always `input_image`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/InputImageContent/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "input_image"
        }
      ]
    },
    "default": "input_image",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_image > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_input_image > (schema) > (property) file_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputImageContent/properties/file_id",
    "deprecated": false,
    "key": "file_id",
    "docstring": "The ID of the file to be sent to the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_image > (schema) > (property) image_url": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputImageContent/properties/image_url",
    "deprecated": false,
    "key": "image_url",
    "docstring": "The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "format": "uri"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_image > (schema) > (property) prompt_cache_breakpoint": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputImageContent/properties/prompt_cache_breakpoint",
    "deprecated": false,
    "key": "prompt_cache_breakpoint",
    "docstring": "Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.",
    "title": "Prompt cache breakpoint",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "mode"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_image > (schema) > (property) prompt_cache_breakpoint > (property) mode"
    ]
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputFileContent/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the input item. Always `input_file`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/InputFileContent/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "input_file"
        }
      ]
    },
    "default": "input_file",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_file > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) detail": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputFileContent/properties/detail",
    "deprecated": false,
    "key": "detail",
    "docstring": "The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/InputFileContent/properties/detail",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_file > (schema) > (property) detail > (member) 0",
      "(resource) responses > (model) response_input_file > (schema) > (property) detail > (member) 1",
      "(resource) responses > (model) response_input_file > (schema) > (property) detail > (member) 2"
    ]
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) file_data": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputFileContent/properties/file_data",
    "deprecated": false,
    "key": "file_data",
    "docstring": "The content of the file to be sent to the model.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) file_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputFileContent/properties/file_id",
    "deprecated": false,
    "key": "file_id",
    "docstring": "The ID of the file to be sent to the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) file_url": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputFileContent/properties/file_url",
    "deprecated": false,
    "key": "file_url",
    "docstring": "The URL of the file to be sent to the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "format": "uri"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) filename": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputFileContent/properties/filename",
    "deprecated": false,
    "key": "filename",
    "docstring": "The name of the file to be sent to the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) prompt_cache_breakpoint": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputFileContent/properties/prompt_cache_breakpoint",
    "deprecated": false,
    "key": "prompt_cache_breakpoint",
    "docstring": "Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.",
    "title": "Prompt cache breakpoint",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "mode"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_file > (schema) > (property) prompt_cache_breakpoint > (property) mode"
    ]
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/OutputTextContent/properties/annotations",
    "deprecated": false,
    "key": "annotations",
    "docstring": "The annotations of the text output.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/OutputTextContent/properties/annotations",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/OutputTextContent/properties/annotations/items",
        "types": [
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "file_id"
              },
              {
                "ident": "filename"
              },
              {
                "ident": "index"
              },
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "end_index"
              },
              {
                "ident": "start_index"
              },
              {
                "ident": "title"
              },
              {
                "ident": "type"
              },
              {
                "ident": "url"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "container_id"
              },
              {
                "ident": "end_index"
              },
              {
                "ident": "file_id"
              },
              {
                "ident": "filename"
              },
              {
                "ident": "start_index"
              },
              {
                "ident": "type"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "file_id"
              },
              {
                "ident": "index"
              },
              {
                "ident": "type"
              }
            ]
          }
        ]
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 0",
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 1",
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 2",
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 3"
    ]
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) logprobs": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/OutputTextContent/properties/logprobs",
    "deprecated": false,
    "key": "logprobs",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/OutputTextContent/properties/logprobs",
      "elementType": {
        "kind": "HttpTypeObject",
        "members": [
          {
            "ident": "token"
          },
          {
            "ident": "bytes"
          },
          {
            "ident": "logprob"
          },
          {
            "ident": "top_logprobs"
          }
        ]
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_text > (schema) > (property) logprobs > (items) > (property) token",
      "(resource) responses > (model) response_output_text > (schema) > (property) logprobs > (items) > (property) bytes",
      "(resource) responses > (model) response_output_text > (schema) > (property) logprobs > (items) > (property) logprob",
      "(resource) responses > (model) response_output_text > (schema) > (property) logprobs > (items) > (property) top_logprobs"
    ]
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) text": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/OutputTextContent/properties/text",
    "deprecated": false,
    "key": "text",
    "docstring": "The text output from the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/OutputTextContent/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the output text. Always `output_text`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/OutputTextContent/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "output_text"
        }
      ]
    },
    "default": "output_text",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_output_text > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_output_refusal > (schema) > (property) refusal": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/RefusalContent/properties/refusal",
    "deprecated": false,
    "key": "refusal",
    "docstring": "The refusal explanation from the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_output_refusal > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/RefusalContent/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the refusal. Always `refusal`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/RefusalContent/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "refusal"
        }
      ]
    },
    "default": "refusal",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_output_refusal > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results > (items) > (property) attributes > (items) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/VectorStoreFileAttributes/anyOf/0/additionalProperties/oneOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results > (items) > (property) attributes > (items) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/VectorStoreFileAttributes/anyOf/0/additionalProperties/oneOf/1",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 3 > (property) results > (items) > (property) attributes > (items) > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/VectorStoreFileAttributes/anyOf/0/additionalProperties/oneOf/2",
    "ident": "UnionMember2",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) button": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ClickParam/properties/button",
    "deprecated": false,
    "key": "button",
    "docstring": "Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ClickParam/properties/button",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "left"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "right"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "wheel"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "back"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "forward"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) button > (member) 0",
      "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) button > (member) 1",
      "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) button > (member) 2",
      "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) button > (member) 3",
      "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) button > (member) 4"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ClickParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Specifies the event type. For a click action, this property is always `click`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ClickParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "click"
        }
      ]
    },
    "default": "click",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) x": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ClickParam/properties/x",
    "deprecated": false,
    "key": "x",
    "docstring": "The x-coordinate where the click occurred.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) y": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ClickParam/properties/y",
    "deprecated": false,
    "key": "y",
    "docstring": "The y-coordinate where the click occurred.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) keys": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ClickParam/properties/keys",
    "deprecated": false,
    "key": "keys",
    "docstring": "The keys being held while clicking.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/ClickParam/properties/keys",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": true,
    "nullable": true,
    "schemaType": "array",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 1 > (property) keys": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/DoubleClickAction/properties/keys",
    "deprecated": false,
    "key": "keys",
    "docstring": "The keys being held while double-clicking.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/DoubleClickAction/properties/keys",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": false,
    "nullable": true,
    "schemaType": "array",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/DoubleClickAction/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Specifies the event type. For a double click action, this property is always set to `double_click`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/DoubleClickAction/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "double_click"
        }
      ]
    },
    "default": "double_click",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 1 > (property) x": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/DoubleClickAction/properties/x",
    "deprecated": false,
    "key": "x",
    "docstring": "The x-coordinate where the double click occurred.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 1 > (property) y": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/DoubleClickAction/properties/y",
    "deprecated": false,
    "key": "y",
    "docstring": "The y-coordinate where the double click occurred.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 2 > (property) path": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/DragParam/properties/path",
    "deprecated": false,
    "key": "path",
    "docstring": "An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg\n```\n[\n  { x: 100, y: 200 },\n  { x: 200, y: 300 }\n]\n```",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/DragParam/properties/path",
      "elementType": {
        "kind": "HttpTypeObject",
        "members": [
          {
            "ident": "x"
          },
          {
            "ident": "y"
          }
        ]
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 2 > (property) path > (items) > (property) x",
      "(resource) responses > (model) computer_action > (schema) > (variant) 2 > (property) path > (items) > (property) y"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 2 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/DragParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Specifies the event type. For a drag action, this property is always set to `drag`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/DragParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "drag"
        }
      ]
    },
    "default": "drag",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 2 > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 2 > (property) keys": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/DragParam/properties/keys",
    "deprecated": false,
    "key": "keys",
    "docstring": "The keys being held while dragging the mouse.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/DragParam/properties/keys",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": true,
    "nullable": true,
    "schemaType": "array",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 3 > (property) keys": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/KeyPressAction/properties/keys",
    "deprecated": false,
    "key": "keys",
    "docstring": "The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/KeyPressAction/properties/keys",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 3 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/KeyPressAction/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Specifies the event type. For a keypress action, this property is always set to `keypress`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/KeyPressAction/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "keypress"
        }
      ]
    },
    "default": "keypress",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 3 > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 4 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MoveParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Specifies the event type. For a move action, this property is always set to `move`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/MoveParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "move"
        }
      ]
    },
    "default": "move",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 4 > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 4 > (property) x": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MoveParam/properties/x",
    "deprecated": false,
    "key": "x",
    "docstring": "The x-coordinate to move to.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 4 > (property) y": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MoveParam/properties/y",
    "deprecated": false,
    "key": "y",
    "docstring": "The y-coordinate to move to.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 4 > (property) keys": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MoveParam/properties/keys",
    "deprecated": false,
    "key": "keys",
    "docstring": "The keys being held while moving the mouse.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/MoveParam/properties/keys",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": true,
    "nullable": true,
    "schemaType": "array",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 5 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ScreenshotParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Specifies the event type. For a screenshot action, this property is always set to `screenshot`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ScreenshotParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "screenshot"
        }
      ]
    },
    "default": "screenshot",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 5 > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 6 > (property) scroll_x": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ScrollParam/properties/scroll_x",
    "deprecated": false,
    "key": "scroll_x",
    "docstring": "The horizontal scroll distance.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 6 > (property) scroll_y": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ScrollParam/properties/scroll_y",
    "deprecated": false,
    "key": "scroll_y",
    "docstring": "The vertical scroll distance.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 6 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ScrollParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Specifies the event type. For a scroll action, this property is always set to `scroll`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ScrollParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "scroll"
        }
      ]
    },
    "default": "scroll",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 6 > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 6 > (property) x": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ScrollParam/properties/x",
    "deprecated": false,
    "key": "x",
    "docstring": "The x-coordinate where the scroll occurred.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 6 > (property) y": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ScrollParam/properties/y",
    "deprecated": false,
    "key": "y",
    "docstring": "The y-coordinate where the scroll occurred.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 6 > (property) keys": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ScrollParam/properties/keys",
    "deprecated": false,
    "key": "keys",
    "docstring": "The keys being held while scrolling.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/ScrollParam/properties/keys",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": true,
    "nullable": true,
    "schemaType": "array",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 7 > (property) text": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/TypeParam/properties/text",
    "deprecated": false,
    "key": "text",
    "docstring": "The text to type.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 7 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/TypeParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Specifies the event type. For a type action, this property is always set to `type`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/TypeParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "type"
        }
      ]
    },
    "default": "type",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 7 > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 8 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WaitParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Specifies the event type. For a wait action, this property is always set to `wait`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/WaitParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "wait"
        }
      ]
    },
    "default": "wait",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) computer_action > (schema) > (variant) 8 > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_computer_tool_call_output_screenshot > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "computer_screenshot"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchActionSearch/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The action type.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/WebSearchActionSearch/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "search"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0 > (property) queries": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchActionSearch/properties/queries",
    "deprecated": false,
    "key": "queries",
    "docstring": "The search queries.\n",
    "title": "Search queries",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/WebSearchActionSearch/properties/queries",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0 > (property) query": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchActionSearch/properties/query",
    "deprecated": true,
    "key": "query",
    "docstring": "The search query.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0 > (property) sources": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchActionSearch/properties/sources",
    "deprecated": false,
    "key": "sources",
    "docstring": "The sources used in the search.\n",
    "title": "Web search sources",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/WebSearchActionSearch/properties/sources",
      "elementType": {
        "kind": "HttpTypeObject",
        "members": [
          {
            "ident": "type"
          },
          {
            "ident": "url"
          }
        ]
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0 > (property) sources > (items) > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0 > (property) sources > (items) > (property) url"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchActionOpenPage/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The action type.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/WebSearchActionOpenPage/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "open_page"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 1 > (property) url": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchActionOpenPage/properties/url",
    "deprecated": false,
    "key": "url",
    "docstring": "The URL opened by the model.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "format": "uri"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 2 > (property) pattern": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchActionFind/properties/pattern",
    "deprecated": false,
    "key": "pattern",
    "docstring": "The pattern or text to search for within the page.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 2 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchActionFind/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The action type.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/WebSearchActionFind/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "find_in_page"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 2 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 2 > (property) url": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchActionFind/properties/url",
    "deprecated": false,
    "key": "url",
    "docstring": "The URL of the page searched for the pattern.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "format": "uri"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) caller > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/DirectToolCallCaller/properties/type",
    "deprecated": false,
    "key": "type",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/DirectToolCallCaller/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "direct"
        }
      ]
    },
    "default": "direct",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) caller > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) caller > (variant) 1 > (property) caller_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ProgramToolCallCaller/properties/caller_id",
    "deprecated": false,
    "key": "caller_id",
    "docstring": "The call ID of the program item that produced this tool call.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) caller > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ProgramToolCallCaller/properties/type",
    "deprecated": false,
    "key": "type",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ProgramToolCallCaller/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "program"
        }
      ]
    },
    "default": "program",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) caller > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) output > (variant) 1 > (items) > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseInputTextContent",
      "$ref": "(resource) responses > (model) response_input_text_content > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_text_content > (schema) > (property) text",
      "(resource) responses > (model) response_input_text_content > (schema) > (property) type",
      "(resource) responses > (model) response_input_text_content > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) output > (variant) 1 > (items) > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseInputImageContent",
      "$ref": "(resource) responses > (model) response_input_image_content > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_image_content > (schema) > (property) type",
      "(resource) responses > (model) response_input_image_content > (schema) > (property) detail",
      "(resource) responses > (model) response_input_image_content > (schema) > (property) file_id",
      "(resource) responses > (model) response_input_image_content > (schema) > (property) image_url",
      "(resource) responses > (model) response_input_image_content > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) output > (variant) 1 > (items) > (variant) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponseInputFileContent",
      "$ref": "(resource) responses > (model) response_input_file_content > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_file_content > (schema) > (property) type",
      "(resource) responses > (model) response_input_file_content > (schema) > (property) detail",
      "(resource) responses > (model) response_input_file_content > (schema) > (property) file_data",
      "(resource) responses > (model) response_input_file_content > (schema) > (property) file_id",
      "(resource) responses > (model) response_input_file_content > (schema) > (property) file_url",
      "(resource) responses > (model) response_input_file_content > (schema) > (property) filename",
      "(resource) responses > (model) response_input_file_content > (schema) > (property) prompt_cache_breakpoint"
    ]
  },
  "(resource) responses > (model) response_input_text_content > (schema) > (property) text": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputTextContentParam/properties/text",
    "deprecated": false,
    "key": "text",
    "docstring": "The text input to the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 10485760
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_text_content > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputTextContentParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the input item. Always `input_text`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/InputTextContentParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "input_text"
        }
      ]
    },
    "default": "input_text",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_text_content > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_input_text_content > (schema) > (property) prompt_cache_breakpoint": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputTextContentParam/properties/prompt_cache_breakpoint",
    "deprecated": false,
    "key": "prompt_cache_breakpoint",
    "docstring": "Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.",
    "title": "Prompt cache breakpoint",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "mode"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_text_content > (schema) > (property) prompt_cache_breakpoint > (property) mode"
    ]
  },
  "(resource) responses > (model) response_input_image_content > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputImageContentParamAutoParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the input item. Always `input_image`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/InputImageContentParamAutoParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "input_image"
        }
      ]
    },
    "default": "input_image",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_image_content > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_input_image_content > (schema) > (property) detail": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputImageContentParamAutoParam/properties/detail",
    "deprecated": false,
    "key": "detail",
    "docstring": "The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ImageDetail",
      "$ref": "(resource) responses > (model) image_detail > (schema)"
    },
    "optional": true,
    "nullable": true,
    "modelImplicit": false,
    "schemaType": "enum",
    "modelPath": "(resource) responses > (model) image_detail",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) image_detail > (schema) > (member) 0",
      "(resource) responses > (model) image_detail > (schema) > (member) 1",
      "(resource) responses > (model) image_detail > (schema) > (member) 2",
      "(resource) responses > (model) image_detail > (schema) > (member) 3"
    ]
  },
  "(resource) responses > (model) response_input_image_content > (schema) > (property) file_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputImageContentParamAutoParam/properties/file_id",
    "deprecated": false,
    "key": "file_id",
    "docstring": "The ID of the file to be sent to the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "file-123"
    ],
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_image_content > (schema) > (property) image_url": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputImageContentParamAutoParam/properties/image_url",
    "deprecated": false,
    "key": "image_url",
    "docstring": "The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 20971520,
      "format": "uri"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_image_content > (schema) > (property) prompt_cache_breakpoint": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputImageContentParamAutoParam/properties/prompt_cache_breakpoint",
    "deprecated": false,
    "key": "prompt_cache_breakpoint",
    "docstring": "Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.",
    "title": "Prompt cache breakpoint",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "mode"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_image_content > (schema) > (property) prompt_cache_breakpoint > (property) mode"
    ]
  },
  "(resource) responses > (model) response_input_file_content > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputFileContentParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the input item. Always `input_file`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/InputFileContentParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "input_file"
        }
      ]
    },
    "default": "input_file",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_file_content > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_input_file_content > (schema) > (property) detail": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputFileContentParam/properties/detail",
    "deprecated": false,
    "key": "detail",
    "docstring": "The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/InputFileContentParam/properties/detail",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_file_content > (schema) > (property) detail > (member) 0",
      "(resource) responses > (model) response_input_file_content > (schema) > (property) detail > (member) 1",
      "(resource) responses > (model) response_input_file_content > (schema) > (property) detail > (member) 2"
    ]
  },
  "(resource) responses > (model) response_input_file_content > (schema) > (property) file_data": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputFileContentParam/properties/file_data",
    "deprecated": false,
    "key": "file_data",
    "docstring": "The base64-encoded data of the file to be sent to the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "maxLength": 73400320
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_file_content > (schema) > (property) file_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputFileContentParam/properties/file_id",
    "deprecated": false,
    "key": "file_id",
    "docstring": "The ID of the file to be sent to the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "examples": [
      "file-123"
    ],
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_file_content > (schema) > (property) file_url": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputFileContentParam/properties/file_url",
    "deprecated": false,
    "key": "file_url",
    "docstring": "The URL of the file to be sent to the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "format": "uri"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_file_content > (schema) > (property) filename": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputFileContentParam/properties/filename",
    "deprecated": false,
    "key": "filename",
    "docstring": "The name of the file to be sent to the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_input_file_content > (schema) > (property) prompt_cache_breakpoint": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InputFileContentParam/properties/prompt_cache_breakpoint",
    "deprecated": false,
    "key": "prompt_cache_breakpoint",
    "docstring": "Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.",
    "title": "Prompt cache breakpoint",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "mode"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_input_file_content > (schema) > (property) prompt_cache_breakpoint > (property) mode"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) caller > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/DirectToolCallCallerParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The caller type. Always `direct`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/DirectToolCallCallerParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "direct"
        }
      ]
    },
    "default": "direct",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) caller > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) caller > (variant) 1 > (property) caller_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ProgramToolCallCallerParam/properties/caller_id",
    "deprecated": false,
    "key": "caller_id",
    "docstring": "The call ID of the program item that produced this tool call.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 64
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) caller > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ProgramToolCallCallerParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The caller type. Always `program`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ProgramToolCallCallerParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "program"
        }
      ]
    },
    "default": "program",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) caller > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/name",
    "deprecated": false,
    "key": "name",
    "docstring": "The name of the function to call.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) parameters": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/parameters",
    "deprecated": false,
    "key": "parameters",
    "docstring": "A JSON schema object describing the parameters of the function.",
    "type": {
      "kind": "HttpTypeReference",
      "oasRef": "#/components/schemas/FunctionTool/properties/parameters",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnknown"
        }
      ]
    },
    "optional": false,
    "nullable": true,
    "schemaType": "map",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) strict": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/strict",
    "deprecated": false,
    "key": "strict",
    "docstring": "Whether strict parameter validation is enforced for this function tool.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": false,
    "nullable": true,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the function tool. Always `function`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionTool/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function"
        }
      ]
    },
    "default": "function",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) allowed_callers": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/allowed_callers",
    "deprecated": false,
    "key": "allowed_callers",
    "docstring": "The tool invocation context(s).",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/FunctionTool/properties/allowed_callers",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/FunctionTool/properties/allowed_callers/anyOf/0/items",
        "types": [
          {
            "kind": "HttpTypeLiteral",
            "literal": "direct"
          },
          {
            "kind": "HttpTypeLiteral",
            "literal": "programmatic"
          }
        ]
      }
    },
    "optional": true,
    "nullable": true,
    "schemaType": "array",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) allowed_callers > (items) > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) allowed_callers > (items) > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) async": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/async",
    "deprecated": false,
    "key": "async",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) defer_loading": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/defer_loading",
    "deprecated": false,
    "key": "defer_loading",
    "docstring": "Whether this function is deferred and loaded via tool search.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) description": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/description",
    "deprecated": false,
    "key": "description",
    "docstring": "A description of the function. Used by the model to determine whether or not to call the function.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) output_schema": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/output_schema",
    "deprecated": false,
    "key": "output_schema",
    "docstring": "A JSON schema object describing the JSON value encoded in string outputs for this function.",
    "type": {
      "kind": "HttpTypeReference",
      "oasRef": "#/components/schemas/FunctionTool/properties/output_schema",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnknown"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "map",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchTool/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the file search tool. Always `file_search`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FileSearchTool/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "file_search"
        }
      ]
    },
    "default": "file_search",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) vector_store_ids": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchTool/properties/vector_store_ids",
    "deprecated": false,
    "key": "vector_store_ids",
    "docstring": "The IDs of the vector stores to search.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/FileSearchTool/properties/vector_store_ids",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) filters": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchTool/properties/filters",
    "deprecated": false,
    "key": "filters",
    "docstring": "A filter to apply.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FileSearchTool/properties/filters",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "ComparisonFilter",
          "$ref": "(resource) $shared > (model) comparison_filter > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "CompoundFilter",
          "$ref": "(resource) $shared > (model) compound_filter > (schema)"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) filters > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) filters > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) max_num_results": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchTool/properties/max_num_results",
    "deprecated": false,
    "key": "max_num_results",
    "docstring": "The maximum number of results to return. This number should be between 1 and 50 inclusive.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) ranking_options": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchTool/properties/ranking_options",
    "deprecated": false,
    "key": "ranking_options",
    "docstring": "Ranking options for search.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "hybrid_search"
        },
        {
          "ident": "ranker"
        },
        {
          "ident": "score_threshold"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) hybrid_search",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) ranker",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) score_threshold"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 2 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerTool/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the computer tool. Always `computer`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ComputerTool/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "computer"
        }
      ]
    },
    "default": "computer",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 2 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) display_height": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerUsePreviewTool/properties/display_height",
    "deprecated": false,
    "key": "display_height",
    "docstring": "The height of the computer display.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) display_width": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerUsePreviewTool/properties/display_width",
    "deprecated": false,
    "key": "display_width",
    "docstring": "The width of the computer display.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) environment": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerUsePreviewTool/properties/environment",
    "deprecated": false,
    "key": "environment",
    "docstring": "The type of computer environment to control.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ComputerUsePreviewTool/properties/environment",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "windows"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "mac"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "linux"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "ubuntu"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "browser"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 3",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 4"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerUsePreviewTool/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the computer use tool. Always `computer_use_preview`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ComputerUsePreviewTool/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "computer_use_preview"
        }
      ]
    },
    "default": "computer_use_preview",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchTool/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/WebSearchTool/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "web_search"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "web_search_2025_08_26"
        }
      ]
    },
    "default": "web_search",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) type > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) type > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) external_web_access": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchTool/properties/external_web_access",
    "deprecated": false,
    "key": "external_web_access",
    "docstring": "Allow live internet access for web search. Defaults to true when omitted. When false, the web search tool runs in offline/cache-only mode and will not fetch new external content.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "default": true,
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) filters": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchTool/properties/filters",
    "deprecated": false,
    "key": "filters",
    "docstring": "Filters for the search.\n",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "allowed_domains"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) filters > (property) allowed_domains"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) search_context_size": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchTool/properties/search_context_size",
    "deprecated": false,
    "key": "search_context_size",
    "docstring": "High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/WebSearchTool/properties/search_context_size",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "medium"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        }
      ]
    },
    "default": "medium",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) search_context_size > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) search_context_size > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) search_context_size > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) user_location": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchTool/properties/user_location",
    "deprecated": false,
    "key": "user_location",
    "docstring": "The approximate location of the user.\n",
    "title": "Web search approximate location",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "city"
        },
        {
          "ident": "country"
        },
        {
          "ident": "region"
        },
        {
          "ident": "timezone"
        },
        {
          "ident": "type"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) city",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) country",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) region",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) timezone",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) server_label": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/server_label",
    "deprecated": false,
    "key": "server_label",
    "docstring": "A label for this MCP server, used to identify it in tool calls.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the MCP tool. Always `mcp`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/MCPTool/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "mcp"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) allowed_callers": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/allowed_callers",
    "deprecated": false,
    "key": "allowed_callers",
    "docstring": "The tool invocation context(s).",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/MCPTool/properties/allowed_callers",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/MCPTool/properties/allowed_callers/anyOf/0/items",
        "types": [
          {
            "kind": "HttpTypeLiteral",
            "literal": "direct"
          },
          {
            "kind": "HttpTypeLiteral",
            "literal": "programmatic"
          }
        ]
      }
    },
    "optional": true,
    "nullable": true,
    "schemaType": "array",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) allowed_callers > (items) > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) allowed_callers > (items) > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) allowed_tools": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools",
    "deprecated": false,
    "key": "allowed_tools",
    "docstring": "List of allowed tool names or a filter object.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools",
      "types": [
        {
          "kind": "HttpTypeArray",
          "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools/anyOf/0/oneOf/0",
          "elementType": {
            "kind": "HttpTypeString"
          }
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "read_only"
            },
            {
              "ident": "tool_names"
            }
          ]
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) allowed_tools > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) allowed_tools > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) authorization": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/authorization",
    "deprecated": false,
    "key": "authorization",
    "docstring": "An OAuth access token that can be used with a remote MCP server, either\nwith a custom MCP server URL or a service connector. Your application\nmust handle the OAuth authorization flow and provide the token here.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/connector_id",
    "deprecated": false,
    "key": "connector_id",
    "docstring": "Identifier for service connectors, like those available in ChatGPT. One of\n`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more\nabout service connectors [here](/api/docs/guides/tools-connectors-mcp#connectors).\n\nCurrently supported `connector_id` values are:\n\n- Dropbox: `connector_dropbox`\n- Gmail: `connector_gmail`\n- Google Calendar: `connector_googlecalendar`\n- Google Drive: `connector_googledrive`\n- Microsoft Teams: `connector_microsoftteams`\n- Outlook Calendar: `connector_outlookcalendar`\n- Outlook Email: `connector_outlookemail`\n- SharePoint: `connector_sharepoint`\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/MCPTool/properties/connector_id",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_dropbox"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_gmail"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_googlecalendar"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_googledrive"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_microsoftteams"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_outlookcalendar"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_outlookemail"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_sharepoint"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 3",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 4",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 5",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 6",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 7"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) defer_loading": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/defer_loading",
    "deprecated": false,
    "key": "defer_loading",
    "docstring": "Whether this MCP tool is deferred and discovered via tool search.\n",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) headers": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/headers",
    "deprecated": false,
    "key": "headers",
    "docstring": "Optional HTTP headers to send to the MCP server. Use for authentication\nor other purposes.\n",
    "type": {
      "kind": "HttpTypeReference",
      "oasRef": "#/components/schemas/MCPTool/properties/headers",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeString"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "map",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/require_approval",
    "deprecated": false,
    "key": "require_approval",
    "docstring": "Specify which of the MCP server's tools require approval.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/MCPTool/properties/require_approval",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "always"
            },
            {
              "ident": "never"
            }
          ]
        },
        {
          "kind": "HttpTypeUnion",
          "oasRef": "#/components/schemas/MCPTool/properties/require_approval/anyOf/0/oneOf/1",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "always"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "never"
            }
          ]
        }
      ]
    },
    "default": "always",
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) server_description": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/server_description",
    "deprecated": false,
    "key": "server_description",
    "docstring": "Optional description of the MCP server, used to provide more context.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) server_url": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/server_url",
    "deprecated": false,
    "key": "server_url",
    "docstring": "The URL for the MCP server. One of `server_url`, `connector_id`, or\n`tunnel_id` must be provided.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "format": "uri"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) tunnel_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/tunnel_id",
    "deprecated": false,
    "key": "tunnel_id",
    "docstring": "The Secure MCP Tunnel ID to use instead of a direct server URL. One of\n`server_url`, `connector_id`, or `tunnel_id` must be provided.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CodeInterpreterTool/properties/container",
    "deprecated": false,
    "key": "container",
    "docstring": "The code interpreter container. Can be a container ID or an object that\nspecifies uploaded file IDs to make available to your code, along with an\noptional `memory_limit` setting.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CodeInterpreterTool/properties/container",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            },
            {
              "ident": "file_ids"
            },
            {
              "ident": "memory_limit"
            },
            {
              "ident": "network_policy"
            }
          ]
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CodeInterpreterTool/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the code interpreter tool. Always `code_interpreter`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CodeInterpreterTool/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "code_interpreter"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) allowed_callers": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CodeInterpreterTool/properties/allowed_callers",
    "deprecated": false,
    "key": "allowed_callers",
    "docstring": "The tool invocation context(s).",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/CodeInterpreterTool/properties/allowed_callers",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/CodeInterpreterTool/properties/allowed_callers/anyOf/0/items",
        "types": [
          {
            "kind": "HttpTypeLiteral",
            "literal": "direct"
          },
          {
            "kind": "HttpTypeLiteral",
            "literal": "programmatic"
          }
        ]
      }
    },
    "optional": true,
    "nullable": true,
    "schemaType": "array",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) allowed_callers > (items) > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) allowed_callers > (items) > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 7 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ProgrammaticToolCallingParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the tool. Always `programmatic_tool_calling`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ProgrammaticToolCallingParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "programmatic_tool_calling"
        }
      ]
    },
    "default": "programmatic_tool_calling",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 7 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the image generation tool. Always `image_generation`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "image_generation"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) action": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/action",
    "deprecated": false,
    "key": "action",
    "docstring": "Whether to generate a new image or edit an existing image. Default: `auto`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/action",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "generate"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "edit"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) action > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) action > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) action > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) background": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/background",
    "deprecated": false,
    "key": "background",
    "docstring": "Set the background of the generated image. One of `transparent`, `opaque`,\nor `auto`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`, including\ntheir `2026-09-08` snapshots, support `opaque` and `transparent`\nbackgrounds. Transparent backgrounds are available for supported GPT Image\nmodels. For `gpt-image-2` and `gpt-image-2-2026-04-21`, this support is in\npreview. When using `transparent`, set the output format to `png` or `webp`.\nDefault: `auto`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/background",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "transparent"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "opaque"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        }
      ]
    },
    "default": "auto",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) background > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) background > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) background > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) input_fidelity": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/input_fidelity",
    "deprecated": false,
    "key": "input_fidelity",
    "docstring": "Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/input_fidelity",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) input_fidelity > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) input_fidelity > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) input_image_mask": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/input_image_mask",
    "deprecated": false,
    "key": "input_image_mask",
    "docstring": "Optional mask for inpainting. Contains `image_url`\n(string, optional) and `file_id` (string, optional).\n",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "file_id"
        },
        {
          "ident": "image_url"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) input_image_mask > (property) file_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) input_image_mask > (property) image_url"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/model",
    "deprecated": false,
    "key": "model",
    "docstring": "The image generation model to use. One of `gpt-image-1`,\n`gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,\n`gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,\n`gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,\n`gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:\n`gpt-image-1`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/model",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnion",
          "oasRef": "#/components/schemas/ImageGenTool/properties/model/anyOf/1",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-1"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-1-mini"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-1.5"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-2"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-2-2026-04-21"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-2.5-sunburst"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-2.5-sunburst-2026-09-08"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-2.5-flare"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-2.5-flare-2026-09-08"
            }
          ]
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) moderation": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/moderation",
    "deprecated": false,
    "key": "moderation",
    "docstring": "Moderation level for the generated image. Default: `auto`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/moderation",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        }
      ]
    },
    "default": "auto",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) moderation > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) moderation > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) output_compression": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/output_compression",
    "deprecated": false,
    "key": "output_compression",
    "docstring": "Compression level for the output image. Default: 100.\n",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 0,
      "maximum": 100
    },
    "default": 100,
    "optional": true,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) output_format": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/output_format",
    "deprecated": false,
    "key": "output_format",
    "docstring": "The output format of the generated image. One of `png`, `webp`, or\n`jpeg`. Default: `png`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/output_format",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "png"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "webp"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "jpeg"
        }
      ]
    },
    "default": "png",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) output_format > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) output_format > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) output_format > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) partial_images": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/partial_images",
    "deprecated": false,
    "key": "partial_images",
    "docstring": "Number of partial images to generate in streaming mode, from 0 (default value) to 3.\n",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 0,
      "maximum": 3
    },
    "default": 0,
    "optional": true,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) quality": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/quality",
    "deprecated": false,
    "key": "quality",
    "docstring": "The quality of the generated image. The GPT image models support `low`,\n`medium`, and `high`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`,\nincluding their `2026-09-08` snapshots, also support `xhigh` and `max`.\nDefault: `auto`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/quality",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "medium"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "xhigh"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "max"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        }
      ]
    },
    "default": "auto",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 3",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 4",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 5"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) size": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/size",
    "deprecated": false,
    "key": "size",
    "docstring": "The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model's current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/size",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnion",
          "oasRef": "#/components/schemas/ImageGenTool/properties/size/anyOf/1",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "1024x1024"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "1024x1536"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "1536x1024"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "auto"
            }
          ]
        }
      ]
    },
    "default": "auto",
    "optional": true,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 9 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalShellToolParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the local shell tool. Always `local_shell`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LocalShellToolParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "local_shell"
        }
      ]
    },
    "default": "local_shell",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 9 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellToolParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the shell tool. Always `shell`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionShellToolParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "shell"
        }
      ]
    },
    "default": "shell",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) allowed_callers": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellToolParam/properties/allowed_callers",
    "deprecated": false,
    "key": "allowed_callers",
    "docstring": "The tool invocation context(s).",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/FunctionShellToolParam/properties/allowed_callers",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/FunctionShellToolParam/properties/allowed_callers/anyOf/0/items",
        "types": [
          {
            "kind": "HttpTypeLiteral",
            "literal": "direct"
          },
          {
            "kind": "HttpTypeLiteral",
            "literal": "programmatic"
          }
        ]
      }
    },
    "optional": true,
    "nullable": true,
    "schemaType": "array",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) allowed_callers > (items) > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) allowed_callers > (items) > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) environment": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellToolParam/properties/environment",
    "deprecated": false,
    "key": "environment",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionShellToolParam/properties/environment",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "ContainerAuto",
          "$ref": "(resource) responses > (model) container_auto > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "LocalEnvironment",
          "$ref": "(resource) responses > (model) local_environment > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ContainerReference",
          "$ref": "(resource) responses > (model) container_reference > (schema)"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) environment > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) environment > (variant) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) environment > (variant) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolParam/properties/name",
    "deprecated": false,
    "key": "name",
    "docstring": "The name of the custom tool, used to identify it in tool calls.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the custom tool. Always `custom`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CustomToolParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "custom"
        }
      ]
    },
    "default": "custom",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) allowed_callers": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolParam/properties/allowed_callers",
    "deprecated": false,
    "key": "allowed_callers",
    "docstring": "The tool invocation context(s).",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/CustomToolParam/properties/allowed_callers",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/CustomToolParam/properties/allowed_callers/anyOf/0/items",
        "types": [
          {
            "kind": "HttpTypeLiteral",
            "literal": "direct"
          },
          {
            "kind": "HttpTypeLiteral",
            "literal": "programmatic"
          }
        ]
      }
    },
    "optional": true,
    "nullable": true,
    "schemaType": "array",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) allowed_callers > (items) > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) allowed_callers > (items) > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) async": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolParam/properties/async",
    "deprecated": false,
    "key": "async",
    "docstring": "Whether the tool response can be returned asynchronously versus immediately returned on next response creation.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) defer_loading": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolParam/properties/defer_loading",
    "deprecated": false,
    "key": "defer_loading",
    "docstring": "Whether this tool should be deferred and discovered via tool search.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) description": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolParam/properties/description",
    "deprecated": false,
    "key": "description",
    "docstring": "Optional description of the custom tool, used to provide more context.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) format": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomToolParam/properties/format",
    "deprecated": false,
    "key": "format",
    "docstring": "The input format for the custom tool. Default is unconstrained text.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "CustomToolInputFormat",
      "$ref": "(resource) $shared > (model) custom_tool_input_format > (schema)"
    },
    "optional": true,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "union",
    "modelPath": "(resource) $shared > (model) custom_tool_input_format",
    "childrenParentSchema": "union",
    "children": [
      "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 0",
      "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) description": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/NamespaceToolParam/properties/description",
    "deprecated": false,
    "key": "description",
    "docstring": "A description of the namespace shown to the model.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/NamespaceToolParam/properties/name",
    "deprecated": false,
    "key": "name",
    "docstring": "The namespace name used in tool calls (for example, `crm`).",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/NamespaceToolParam/properties/tools",
    "deprecated": false,
    "key": "tools",
    "docstring": "The function/custom tools available inside this namespace.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/NamespaceToolParam/properties/tools",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/NamespaceToolParam/properties/tools/items",
        "types": [
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "name"
              },
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              },
              {
                "ident": "async"
              },
              {
                "ident": "defer_loading"
              },
              {
                "ident": "description"
              },
              {
                "ident": "output_schema"
              },
              {
                "ident": "parameters"
              },
              {
                "ident": "strict"
              }
            ]
          },
          {
            "kind": "HttpTypeObject",
            "members": [
              {
                "ident": "name"
              },
              {
                "ident": "type"
              },
              {
                "ident": "allowed_callers"
              },
              {
                "ident": "async"
              },
              {
                "ident": "defer_loading"
              },
              {
                "ident": "description"
              },
              {
                "ident": "format"
              }
            ]
          }
        ]
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/NamespaceToolParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the tool. Always `namespace`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/NamespaceToolParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "namespace"
        }
      ]
    },
    "default": "namespace",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 13 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ToolSearchToolParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the tool. Always `tool_search`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ToolSearchToolParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "tool_search"
        }
      ]
    },
    "default": "tool_search",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 13 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 13 > (property) description": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ToolSearchToolParam/properties/description",
    "deprecated": false,
    "key": "description",
    "docstring": "Description shown to the model for a client-executed tool search tool.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 13 > (property) execution": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ToolSearchToolParam/properties/execution",
    "deprecated": false,
    "key": "execution",
    "docstring": "Whether tool search is executed by the server or by the client.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ToolSearchToolParam/properties/execution",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "server"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "client"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 13 > (property) execution > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 13 > (property) execution > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 13 > (property) parameters": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ToolSearchToolParam/properties/parameters",
    "deprecated": false,
    "key": "parameters",
    "docstring": "Parameter schema for a client-executed tool search tool.",
    "type": {
      "kind": "HttpTypeUnknown"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "unknown",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchPreviewTool/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/WebSearchPreviewTool/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "web_search_preview"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "web_search_preview_2025_03_11"
        }
      ]
    },
    "default": "web_search_preview",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) type > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) type > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) search_content_types": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchPreviewTool/properties/search_content_types",
    "deprecated": false,
    "key": "search_content_types",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/WebSearchPreviewTool/properties/search_content_types",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/WebSearchPreviewTool/properties/search_content_types/items",
        "types": [
          {
            "kind": "HttpTypeLiteral",
            "literal": "text"
          },
          {
            "kind": "HttpTypeLiteral",
            "literal": "image"
          }
        ]
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) search_content_types > (items) > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) search_content_types > (items) > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) search_context_size": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchPreviewTool/properties/search_context_size",
    "deprecated": false,
    "key": "search_context_size",
    "docstring": "High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/WebSearchPreviewTool/properties/search_context_size",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "medium"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) search_context_size > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) search_context_size > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) search_context_size > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) user_location": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchPreviewTool/properties/user_location",
    "deprecated": false,
    "key": "user_location",
    "docstring": "The user's location.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "type"
        },
        {
          "ident": "city"
        },
        {
          "ident": "country"
        },
        {
          "ident": "region"
        },
        {
          "ident": "timezone"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) city",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) country",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) region",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) timezone"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 15 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApplyPatchToolParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the tool. Always `apply_patch`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ApplyPatchToolParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "apply_patch"
        }
      ]
    },
    "default": "apply_patch",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 15 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 15 > (property) allowed_callers": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApplyPatchToolParam/properties/allowed_callers",
    "deprecated": false,
    "key": "allowed_callers",
    "docstring": "The tool invocation context(s).",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/ApplyPatchToolParam/properties/allowed_callers",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/ApplyPatchToolParam/properties/allowed_callers/anyOf/0/items",
        "types": [
          {
            "kind": "HttpTypeLiteral",
            "literal": "direct"
          },
          {
            "kind": "HttpTypeLiteral",
            "literal": "programmatic"
          }
        ]
      }
    },
    "optional": true,
    "nullable": true,
    "schemaType": "array",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 15 > (property) allowed_callers > (items) > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 15 > (property) allowed_callers > (items) > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/name",
    "deprecated": false,
    "key": "name",
    "docstring": "The name of the function to call.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) parameters": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/parameters",
    "deprecated": false,
    "key": "parameters",
    "docstring": "A JSON schema object describing the parameters of the function.",
    "type": {
      "kind": "HttpTypeReference",
      "oasRef": "#/components/schemas/FunctionTool/properties/parameters",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnknown"
        }
      ]
    },
    "optional": false,
    "nullable": true,
    "schemaType": "map",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) strict": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/strict",
    "deprecated": false,
    "key": "strict",
    "docstring": "Whether strict parameter validation is enforced for this function tool.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": false,
    "nullable": true,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the function tool. Always `function`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionTool/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "function"
        }
      ]
    },
    "default": "function",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) allowed_callers": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/allowed_callers",
    "deprecated": false,
    "key": "allowed_callers",
    "docstring": "The tool invocation context(s).",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/FunctionTool/properties/allowed_callers",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/FunctionTool/properties/allowed_callers/anyOf/0/items",
        "types": [
          {
            "kind": "HttpTypeLiteral",
            "literal": "direct"
          },
          {
            "kind": "HttpTypeLiteral",
            "literal": "programmatic"
          }
        ]
      }
    },
    "optional": true,
    "nullable": true,
    "schemaType": "array",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) allowed_callers > (items) > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) allowed_callers > (items) > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) async": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/async",
    "deprecated": false,
    "key": "async",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) defer_loading": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/defer_loading",
    "deprecated": false,
    "key": "defer_loading",
    "docstring": "Whether this function is deferred and loaded via tool search.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) description": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/description",
    "deprecated": false,
    "key": "description",
    "docstring": "A description of the function. Used by the model to determine whether or not to call the function.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) output_schema": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionTool/properties/output_schema",
    "deprecated": false,
    "key": "output_schema",
    "docstring": "A JSON schema object describing the JSON value encoded in string outputs for this function.",
    "type": {
      "kind": "HttpTypeReference",
      "oasRef": "#/components/schemas/FunctionTool/properties/output_schema",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnknown"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "map",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchTool/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the file search tool. Always `file_search`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FileSearchTool/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "file_search"
        }
      ]
    },
    "default": "file_search",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) vector_store_ids": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchTool/properties/vector_store_ids",
    "deprecated": false,
    "key": "vector_store_ids",
    "docstring": "The IDs of the vector stores to search.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/FileSearchTool/properties/vector_store_ids",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) filters": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchTool/properties/filters",
    "deprecated": false,
    "key": "filters",
    "docstring": "A filter to apply.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FileSearchTool/properties/filters",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "ComparisonFilter",
          "$ref": "(resource) $shared > (model) comparison_filter > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "CompoundFilter",
          "$ref": "(resource) $shared > (model) compound_filter > (schema)"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) filters > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) filters > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) max_num_results": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchTool/properties/max_num_results",
    "deprecated": false,
    "key": "max_num_results",
    "docstring": "The maximum number of results to return. This number should be between 1 and 50 inclusive.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) ranking_options": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileSearchTool/properties/ranking_options",
    "deprecated": false,
    "key": "ranking_options",
    "docstring": "Ranking options for search.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "hybrid_search"
        },
        {
          "ident": "ranker"
        },
        {
          "ident": "score_threshold"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) hybrid_search",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) ranker",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) score_threshold"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 2 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerTool/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the computer tool. Always `computer`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ComputerTool/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "computer"
        }
      ]
    },
    "default": "computer",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 2 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) display_height": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerUsePreviewTool/properties/display_height",
    "deprecated": false,
    "key": "display_height",
    "docstring": "The height of the computer display.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) display_width": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerUsePreviewTool/properties/display_width",
    "deprecated": false,
    "key": "display_width",
    "docstring": "The width of the computer display.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) environment": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerUsePreviewTool/properties/environment",
    "deprecated": false,
    "key": "environment",
    "docstring": "The type of computer environment to control.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ComputerUsePreviewTool/properties/environment",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "windows"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "mac"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "linux"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "ubuntu"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "browser"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 3",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 4"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComputerUsePreviewTool/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the computer use tool. Always `computer_use_preview`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ComputerUsePreviewTool/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "computer_use_preview"
        }
      ]
    },
    "default": "computer_use_preview",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchTool/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/WebSearchTool/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "web_search"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "web_search_2025_08_26"
        }
      ]
    },
    "default": "web_search",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) type > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) type > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) external_web_access": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchTool/properties/external_web_access",
    "deprecated": false,
    "key": "external_web_access",
    "docstring": "Allow live internet access for web search. Defaults to true when omitted. When false, the web search tool runs in offline/cache-only mode and will not fetch new external content.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "default": true,
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) filters": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchTool/properties/filters",
    "deprecated": false,
    "key": "filters",
    "docstring": "Filters for the search.\n",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "allowed_domains"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) filters > (property) allowed_domains"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) search_context_size": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchTool/properties/search_context_size",
    "deprecated": false,
    "key": "search_context_size",
    "docstring": "High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/WebSearchTool/properties/search_context_size",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "medium"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        }
      ]
    },
    "default": "medium",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) search_context_size > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) search_context_size > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) search_context_size > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) user_location": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchTool/properties/user_location",
    "deprecated": false,
    "key": "user_location",
    "docstring": "The approximate location of the user.\n",
    "title": "Web search approximate location",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "city"
        },
        {
          "ident": "country"
        },
        {
          "ident": "region"
        },
        {
          "ident": "timezone"
        },
        {
          "ident": "type"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) city",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) country",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) region",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) timezone",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) server_label": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/server_label",
    "deprecated": false,
    "key": "server_label",
    "docstring": "A label for this MCP server, used to identify it in tool calls.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the MCP tool. Always `mcp`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/MCPTool/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "mcp"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) allowed_callers": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/allowed_callers",
    "deprecated": false,
    "key": "allowed_callers",
    "docstring": "The tool invocation context(s).",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/MCPTool/properties/allowed_callers",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/MCPTool/properties/allowed_callers/anyOf/0/items",
        "types": [
          {
            "kind": "HttpTypeLiteral",
            "literal": "direct"
          },
          {
            "kind": "HttpTypeLiteral",
            "literal": "programmatic"
          }
        ]
      }
    },
    "optional": true,
    "nullable": true,
    "schemaType": "array",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) allowed_callers > (items) > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) allowed_callers > (items) > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) allowed_tools": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools",
    "deprecated": false,
    "key": "allowed_tools",
    "docstring": "List of allowed tool names or a filter object.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools",
      "types": [
        {
          "kind": "HttpTypeArray",
          "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools/anyOf/0/oneOf/0",
          "elementType": {
            "kind": "HttpTypeString"
          }
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "read_only"
            },
            {
              "ident": "tool_names"
            }
          ]
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) allowed_tools > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) allowed_tools > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) authorization": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/authorization",
    "deprecated": false,
    "key": "authorization",
    "docstring": "An OAuth access token that can be used with a remote MCP server, either\nwith a custom MCP server URL or a service connector. Your application\nmust handle the OAuth authorization flow and provide the token here.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/connector_id",
    "deprecated": false,
    "key": "connector_id",
    "docstring": "Identifier for service connectors, like those available in ChatGPT. One of\n`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more\nabout service connectors [here](/api/docs/guides/tools-connectors-mcp#connectors).\n\nCurrently supported `connector_id` values are:\n\n- Dropbox: `connector_dropbox`\n- Gmail: `connector_gmail`\n- Google Calendar: `connector_googlecalendar`\n- Google Drive: `connector_googledrive`\n- Microsoft Teams: `connector_microsoftteams`\n- Outlook Calendar: `connector_outlookcalendar`\n- Outlook Email: `connector_outlookemail`\n- SharePoint: `connector_sharepoint`\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/MCPTool/properties/connector_id",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_dropbox"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_gmail"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_googlecalendar"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_googledrive"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_microsoftteams"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_outlookcalendar"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_outlookemail"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connector_sharepoint"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 3",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 4",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 5",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 6",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 7"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) defer_loading": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/defer_loading",
    "deprecated": false,
    "key": "defer_loading",
    "docstring": "Whether this MCP tool is deferred and discovered via tool search.\n",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) headers": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/headers",
    "deprecated": false,
    "key": "headers",
    "docstring": "Optional HTTP headers to send to the MCP server. Use for authentication\nor other purposes.\n",
    "type": {
      "kind": "HttpTypeReference",
      "oasRef": "#/components/schemas/MCPTool/properties/headers",
      "ident": "Record",
      "typeParameters": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeString"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "map",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/require_approval",
    "deprecated": false,
    "key": "require_approval",
    "docstring": "Specify which of the MCP server's tools require approval.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/MCPTool/properties/require_approval",
      "types": [
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "always"
            },
            {
              "ident": "never"
            }
          ]
        },
        {
          "kind": "HttpTypeUnion",
          "oasRef": "#/components/schemas/MCPTool/properties/require_approval/anyOf/0/oneOf/1",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "always"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "never"
            }
          ]
        }
      ]
    },
    "default": "always",
    "optional": true,
    "nullable": true,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) server_description": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/server_description",
    "deprecated": false,
    "key": "server_description",
    "docstring": "Optional description of the MCP server, used to provide more context.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) server_url": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/server_url",
    "deprecated": false,
    "key": "server_url",
    "docstring": "The URL for the MCP server. One of `server_url`, `connector_id`, or\n`tunnel_id` must be provided.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "format": "uri"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) tunnel_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/tunnel_id",
    "deprecated": false,
    "key": "tunnel_id",
    "docstring": "The Secure MCP Tunnel ID to use instead of a direct server URL. One of\n`server_url`, `connector_id`, or `tunnel_id` must be provided.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CodeInterpreterTool/properties/container",
    "deprecated": false,
    "key": "container",
    "docstring": "The code interpreter container. Can be a container ID or an object that\nspecifies uploaded file IDs to make available to your code, along with an\noptional `memory_limit` setting.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CodeInterpreterTool/properties/container",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeObject",
          "members": [
            {
              "ident": "type"
            },
            {
              "ident": "file_ids"
            },
            {
              "ident": "memory_limit"
            },
            {
              "ident": "network_policy"
            }
          ]
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CodeInterpreterTool/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the code interpreter tool. Always `code_interpreter`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CodeInterpreterTool/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "code_interpreter"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) allowed_callers": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CodeInterpreterTool/properties/allowed_callers",
    "deprecated": false,
    "key": "allowed_callers",
    "docstring": "The tool invocation context(s).",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/CodeInterpreterTool/properties/allowed_callers",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/CodeInterpreterTool/properties/allowed_callers/anyOf/0/items",
        "types": [
          {
            "kind": "HttpTypeLiteral",
            "literal": "direct"
          },
          {
            "kind": "HttpTypeLiteral",
            "literal": "programmatic"
          }
        ]
      }
    },
    "optional": true,
    "nullable": true,
    "schemaType": "array",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) allowed_callers > (items) > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) allowed_callers > (items) > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 7 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ProgrammaticToolCallingParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the tool. Always `programmatic_tool_calling`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ProgrammaticToolCallingParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "programmatic_tool_calling"
        }
      ]
    },
    "default": "programmatic_tool_calling",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 7 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the image generation tool. Always `image_generation`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "image_generation"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) action": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/action",
    "deprecated": false,
    "key": "action",
    "docstring": "Whether to generate a new image or edit an existing image. Default: `auto`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/action",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "generate"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "edit"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) action > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) action > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) action > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) background": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/background",
    "deprecated": false,
    "key": "background",
    "docstring": "Set the background of the generated image. One of `transparent`, `opaque`,\nor `auto`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`, including\ntheir `2026-09-08` snapshots, support `opaque` and `transparent`\nbackgrounds. Transparent backgrounds are available for supported GPT Image\nmodels. For `gpt-image-2` and `gpt-image-2-2026-04-21`, this support is in\npreview. When using `transparent`, set the output format to `png` or `webp`.\nDefault: `auto`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/background",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "transparent"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "opaque"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        }
      ]
    },
    "default": "auto",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) background > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) background > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) background > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) input_fidelity": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/input_fidelity",
    "deprecated": false,
    "key": "input_fidelity",
    "docstring": "Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/input_fidelity",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) input_fidelity > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) input_fidelity > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) input_image_mask": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/input_image_mask",
    "deprecated": false,
    "key": "input_image_mask",
    "docstring": "Optional mask for inpainting. Contains `image_url`\n(string, optional) and `file_id` (string, optional).\n",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "file_id"
        },
        {
          "ident": "image_url"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) input_image_mask > (property) file_id",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) input_image_mask > (property) image_url"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/model",
    "deprecated": false,
    "key": "model",
    "docstring": "The image generation model to use. One of `gpt-image-1`,\n`gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,\n`gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,\n`gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,\n`gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:\n`gpt-image-1`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/model",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnion",
          "oasRef": "#/components/schemas/ImageGenTool/properties/model/anyOf/1",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-1"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-1-mini"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-1.5"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-2"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-2-2026-04-21"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-2.5-sunburst"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-2.5-sunburst-2026-09-08"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-2.5-flare"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-image-2.5-flare-2026-09-08"
            }
          ]
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) moderation": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/moderation",
    "deprecated": false,
    "key": "moderation",
    "docstring": "Moderation level for the generated image. Default: `auto`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/moderation",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        }
      ]
    },
    "default": "auto",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) moderation > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) moderation > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) output_compression": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/output_compression",
    "deprecated": false,
    "key": "output_compression",
    "docstring": "Compression level for the output image. Default: 100.\n",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 0,
      "maximum": 100
    },
    "default": 100,
    "optional": true,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) output_format": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/output_format",
    "deprecated": false,
    "key": "output_format",
    "docstring": "The output format of the generated image. One of `png`, `webp`, or\n`jpeg`. Default: `png`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/output_format",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "png"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "webp"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "jpeg"
        }
      ]
    },
    "default": "png",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) output_format > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) output_format > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) output_format > (member) 2"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) partial_images": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/partial_images",
    "deprecated": false,
    "key": "partial_images",
    "docstring": "Number of partial images to generate in streaming mode, from 0 (default value) to 3.\n",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "constraints": {
      "minimum": 0,
      "maximum": 3
    },
    "default": 0,
    "optional": true,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) quality": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/quality",
    "deprecated": false,
    "key": "quality",
    "docstring": "The quality of the generated image. The GPT image models support `low`,\n`medium`, and `high`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`,\nincluding their `2026-09-08` snapshots, also support `xhigh` and `max`.\nDefault: `auto`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/quality",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "low"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "medium"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "high"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "xhigh"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "max"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        }
      ]
    },
    "default": "auto",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 3",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 4",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 5"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) size": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/size",
    "deprecated": false,
    "key": "size",
    "docstring": "The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model's current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ImageGenTool/properties/size",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnion",
          "oasRef": "#/components/schemas/ImageGenTool/properties/size/anyOf/1",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "1024x1024"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "1024x1536"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "1536x1024"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "auto"
            }
          ]
        }
      ]
    },
    "default": "auto",
    "optional": true,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 9 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalShellToolParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the local shell tool. Always `local_shell`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LocalShellToolParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "local_shell"
        }
      ]
    },
    "default": "local_shell",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 9 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 10 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellToolParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the shell tool. Always `shell`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionShellToolParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "shell"
        }
      ]
    },
    "default": "shell",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 10 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 10 > (property) allowed_callers": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellToolParam/properties/allowed_callers",
    "deprecated": false,
    "key": "allowed_callers",
    "docstring": "The tool invocation context(s).",
    "type": {

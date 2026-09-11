<!-- source: https://developers.openai.com/api/reference/resources/live/primary-websocket/ -->
<!-- part of: https://developers.openai.com/api/reference/resources/live/primary-websocket/ -->

<!-- chunk-start -->
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tools"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The delegation owner. Always `responses` for tasks handled by the Responses API.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveResponsesDelegationParam/properties/type",
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
      "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) content": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialDeveloperMessageItemParam/properties/content",
    "deprecated": false,
    "key": "content",
    "docstring": "The message content. Supply exactly one text part for the initial Live conversation history.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/LiveInitialDeveloperMessageItemParam/properties/content",
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
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) content > (items) > (property) text",
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) content > (items) > (property) type"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) role": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialDeveloperMessageItemParam/properties/role",
    "deprecated": false,
    "key": "role",
    "docstring": "The author of this history message. Always `developer`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialDeveloperMessageItemParam/properties/role",
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
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) role > (member) 0"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialDeveloperMessageItemParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialDeveloperMessageItemParam/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The supplied message’s status. Live uses its text as history and does not resume an incomplete message.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialDeveloperMessageItemParam/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) status > (member) 0",
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) status > (member) 1"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialDeveloperMessageItemParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The history item type. Always `message`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialDeveloperMessageItemParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "message"
        }
      ]
    },
    "default": "message",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) content": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialUserMessageItemParam/properties/content",
    "deprecated": false,
    "key": "content",
    "docstring": "The message content. Supply exactly one text part for the initial Live conversation history.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/LiveInitialUserMessageItemParam/properties/content",
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
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) content > (items) > (property) text",
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) content > (items) > (property) type"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) role": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialUserMessageItemParam/properties/role",
    "deprecated": false,
    "key": "role",
    "docstring": "The author of this history message. Always `user`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialUserMessageItemParam/properties/role",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "user"
        }
      ]
    },
    "default": "user",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) role > (member) 0"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialUserMessageItemParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialUserMessageItemParam/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The supplied message’s status. Live uses its text as history and does not resume an incomplete message.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialUserMessageItemParam/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) status > (member) 0",
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) status > (member) 1"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialUserMessageItemParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The history item type. Always `message`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialUserMessageItemParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "message"
        }
      ]
    },
    "default": "message",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialAssistantMessageItemParam/properties/content",
    "deprecated": false,
    "key": "content",
    "docstring": "The message content. Supply exactly one text part for the initial Live conversation history.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/LiveInitialAssistantMessageItemParam/properties/content",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/LiveInitialAssistantMessageItemParam/properties/content/items",
        "types": [
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
                "ident": "text"
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
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content > (items) > (variant) 0",
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content > (items) > (variant) 1"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) role": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialAssistantMessageItemParam/properties/role",
    "deprecated": false,
    "key": "role",
    "docstring": "The author of this history message. Always `assistant`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialAssistantMessageItemParam/properties/role",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "assistant"
        }
      ]
    },
    "default": "assistant",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) role > (member) 0"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialAssistantMessageItemParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialAssistantMessageItemParam/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The supplied message’s status. Live uses its text as history and does not resume an incomplete message.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialAssistantMessageItemParam/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "incomplete"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "completed"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) status > (member) 0",
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) status > (member) 1"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialAssistantMessageItemParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The history item type. Always `message`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialAssistantMessageItemParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "message"
        }
      ]
    },
    "default": "message",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) type > (member) 0"
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
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInitialSessionAudioOutputParam/properties/voice/oneOf/0/anyOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInitialSessionAudioOutputParam/properties/voice/oneOf/0/anyOf/1",
    "docstring": "The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialSessionAudioOutputParam/properties/voice/oneOf/0/anyOf/1",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "alloy"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "ash"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "ballad"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "beacon"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "bossa"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "cedar"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "cinder"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "coral"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "delta"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "echo"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gleam"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "marin"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "meridian"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "quartz"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "ripple"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "sage"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "shimmer"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "stone"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "tempo"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "verse"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "vesper"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "willow"
        }
      ]
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 0",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 1",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 2",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 3",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 4",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 5",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 6",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 7",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 8",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 9",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 10",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 11",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 12",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 13",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 14",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 15",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 16",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 17",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 18",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 19",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 20",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 21"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "CustomVoice",
      "$ref": "(resource) live > (model) custom_voice > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) custom_voice > (schema) > (property) id"
    ]
  },
  "(resource) live > (model) custom_voice > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveCustomVoiceParam",
    "ident": "CustomVoice",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) custom_voice > (schema) > (property) id"
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
  "(resource) live > (model) client_delegation > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "client"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) model": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/model",
    "deprecated": false,
    "key": "model",
    "docstring": "The model used for server-owned Responses delegations.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) instructions": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/instructions",
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
  "(resource) live > (model) responses_delegation_config > (schema) > (property) max_output_tokens": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/max_output_tokens",
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
  "(resource) live > (model) responses_delegation_config > (schema) > (property) parallel_tool_calls": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/parallel_tool_calls",
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
  "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/reasoning",
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
      "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) effort",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) summary"
    ]
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) service_tier": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/service_tier",
    "deprecated": false,
    "key": "service_tier",
    "docstring": "Service tier for delegated Responses requests.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/service_tier",
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
      "(resource) live > (model) responses_delegation_config > (schema) > (property) service_tier > (member) 0",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) service_tier > (member) 1",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) service_tier > (member) 2",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) service_tier > (member) 3",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) service_tier > (member) 4",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) service_tier > (member) 5"
    ]
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) text": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/text",
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
      "(resource) live > (model) responses_delegation_config > (schema) > (property) text > (property) verbosity"
    ]
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/tool_choice",
    "deprecated": false,
    "key": "tool_choice",
    "docstring": "Controls which tool the Responses backend uses when handling a task delegated by the Live model.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/tool_choice",
      "types": [
        {
          "kind": "HttpTypeUnion",
          "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/tool_choice/oneOf/0",
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
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 0",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 1",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 2"
    ]
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tools": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/tools",
    "deprecated": false,
    "key": "tools",
    "docstring": "Tools available to the Responses backend while it handles tasks delegated by the Live model.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/tools",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/tools/items",
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
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tools > (items) > (variant) 0",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tools > (items) > (variant) 1"
    ]
  },
  "(resource) live > (model) responses_delegation_config > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam",
    "docstring": "Model, prompt, and tool settings for tasks delegated by the Live session to a Responses backend.",
    "ident": "ResponsesDelegationConfig",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "model"
        },
        {
          "ident": "instructions"
        },
        {
          "ident": "max_output_tokens"
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
      "(resource) live > (model) responses_delegation_config > (schema) > (property) model",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) instructions",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) max_output_tokens",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) parallel_tool_calls",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) service_tier",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) text",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tools"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "responses"
    }
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) content > (items) > (property) text": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialInputTextContentPartParam/properties/text",
    "deprecated": false,
    "key": "text",
    "docstring": "The message text to include in the Live session’s initial conversation history.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) content > (items) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialInputTextContentPartParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The text content type. Always `input_text`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialInputTextContentPartParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "input_text"
        }
      ]
    },
    "default": "input_text",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) content > (items) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) role > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "developer"
    }
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "message"
    }
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) content > (items) > (property) text": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialInputTextContentPartParam/properties/text",
    "deprecated": false,
    "key": "text",
    "docstring": "The message text to include in the Live session’s initial conversation history.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) content > (items) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialInputTextContentPartParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The text content type. Always `input_text`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialInputTextContentPartParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "input_text"
        }
      ]
    },
    "default": "input_text",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) content > (items) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) role > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "user"
    }
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "message"
    }
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content > (items) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInitialAssistantMessageItemParam/properties/content/items/oneOf/0",
    "docstring": "Assistant text supplied as conversation history when starting a Live session.",
    "ident": "Text",
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
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content > (items) > (variant) 0 > (property) text",
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content > (items) > (variant) 0 > (property) type"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content > (items) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInitialAssistantMessageItemParam/properties/content/items/oneOf/1",
    "docstring": "Assistant output text supplied as conversation history when starting a Live session.",
    "ident": "OutputText",
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
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content > (items) > (variant) 1 > (property) text",
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content > (items) > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) role > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "assistant"
    }
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "incomplete"
    }
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) status > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "completed"
    }
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "message"
    }
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
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "alloy"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "ash"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "ballad"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "beacon"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "bossa"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "cedar"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 6": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "cinder"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 7": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "coral"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 8": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "delta"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 9": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "echo"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 10": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gleam"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 11": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "marin"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 12": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "meridian"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 13": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "quartz"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 14": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "ripple"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 15": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "sage"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 16": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "shimmer"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 17": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "stone"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 18": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "tempo"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 19": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "verse"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 20": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "vesper"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1 > (member) 21": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "willow"
    }
  },
  "(resource) live > (model) custom_voice > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveCustomVoiceParam/properties/id",
    "deprecated": false,
    "key": "id",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 128
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
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
  "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) effort": {
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
      "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) effort > (member) 0",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) effort > (member) 1",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) effort > (member) 2",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) effort > (member) 3",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) effort > (member) 4",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) effort > (member) 5"
    ]
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) summary": {
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
      "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) summary > (member) 0",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) summary > (member) 1",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) summary > (member) 2"
    ]
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) service_tier > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) service_tier > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "default"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) service_tier > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "fast_tier_temp_pilot"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) service_tier > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "flex"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) service_tier > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "priority"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) service_tier > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "ultrafast"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) text > (property) verbosity": {
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
      "(resource) live > (model) responses_delegation_config > (schema) > (property) text > (property) verbosity > (member) 0",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) text > (property) verbosity > (member) 1",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) text > (property) verbosity > (member) 2"
    ]
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/tool_choice/oneOf/0",
    "ident": "LiveToolChoiceEnum",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/tool_choice/oneOf/0",
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
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 0 > (member) 0",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 0 > (member) 1",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 0 > (member) 2"
    ]
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/tool_choice/oneOf/1",
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
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 1 > (property) name",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/tool_choice/oneOf/2",
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
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 2 > (property) name",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 2 > (property) server_label",
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 2 > (property) type"
    ]
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tools > (items) > (variant) 0": {
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
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tools > (items) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponsesDelegationSettingsInputParam/properties/tools/items/oneOf/1",
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
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tools > (items) > (variant) 1 > (property) type"
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
  "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) content > (items) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "input_text"
    }
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) content > (items) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "input_text"
    }
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content > (items) > (variant) 0 > (property) text": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialTextContentPartParam/properties/text",
    "deprecated": false,
    "key": "text",
    "docstring": "The message text to include in the Live session’s initial conversation history.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content > (items) > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialTextContentPartParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The text content type. Always `text`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialTextContentPartParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "text"
        }
      ]
    },
    "default": "text",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content > (items) > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content > (items) > (variant) 1 > (property) text": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialOutputTextContentPartParam/properties/text",
    "deprecated": false,
    "key": "text",
    "docstring": "The message text to include in the Live session’s initial conversation history.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content > (items) > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialOutputTextContentPartParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The text content type. Always `output_text`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialOutputTextContentPartParam/properties/type",
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
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content > (items) > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) effort > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "none"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) effort > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "minimal"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) effort > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) effort > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "medium"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) effort > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) effort > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "xhigh"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) summary > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "concise"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) summary > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "detailed"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) reasoning > (property) summary > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) text > (property) verbosity > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) text > (property) verbosity > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "medium"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) text > (property) verbosity > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 0 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 0 > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "none"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 0 > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "required"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 1 > (property) name": {
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
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 1 > (property) type": {
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
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 2 > (property) name": {
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
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 2 > (property) server_label": {
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
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 2 > (property) type": {
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
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 2 > (property) type > (member) 0"
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
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tools > (items) > (variant) 1 > (property) type": {
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
      "(resource) live > (model) responses_delegation_config > (schema) > (property) tools > (items) > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content > (items) > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "text"
    }
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content > (items) > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "output_text"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function"
    }
  },
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tool_choice > (variant) 2 > (property) type > (member) 0": {
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
  "(resource) live > (model) responses_delegation_config > (schema) > (property) tools > (items) > (variant) 1 > (property) type > (member) 0": {
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
  "type": "session.closed",
  "event_id": "evt_closed_001",
  "client_event_id": "evt_close_001",
  "reason": "close_requested",
  "session": {
    "id": "live_abc123",
    "model": "gpt-live-1",
    "status": "active",
    "expires_at": 1788555600,
    "instructions": "Help the caller plan a restaurant reservation. Confirm details before booking.",
    "input": [],
    "audio": {
      "format": {
        "type": "audio/pcm",
        "rate": 24000
      },
      "output": {
        "voice": "marin"
      }
    },
    "delegation": {
      "type": "client"
    }
  },
  "usage": {
    "seconds": 45.8
  }
}
```

### error

Reports an error in the Live session, such as an invalid client command. Use error.client_event_id, when present, to identify the command that caused the error.

#### Schema

Schema name: `LiveErrorEvent`

```json
{
  "(resource) live > (model) error_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveErrorEvent",
    "docstring": "Reports an error in the Live session, such as an invalid client command. Use error.client_event_id, when present, to identify the command that caused the error.",
    "ident": "ErrorEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "error"
        },
        {
          "ident": "event_id"
        },
        {
          "ident": "type"
        },
        {
          "ident": "client_event_id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) error_event > (schema) > (property) error",
      "(resource) live > (model) error_event > (schema) > (property) event_id",
      "(resource) live > (model) error_event > (schema) > (property) type",
      "(resource) live > (model) error_event > (schema) > (property) client_event_id"
    ]
  },
  "(resource) live > (model) error_event > (schema) > (property) error": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveErrorEvent/properties/error",
    "deprecated": false,
    "key": "error",
    "docstring": "Details of the Live error and the client command that caused it, when known.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "Error",
      "$ref": "(resource) live > (model) error > (schema)"
    },
    "optional": false,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "object",
    "modelPath": "(resource) live > (model) error",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) error > (schema) > (property) code",
      "(resource) live > (model) error > (schema) > (property) message",
      "(resource) live > (model) error > (schema) > (property) type",
      "(resource) live > (model) error > (schema) > (property) client_event_id",
      "(resource) live > (model) error > (schema) > (property) param"
    ]
  },
  "(resource) live > (model) error_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveErrorEvent/properties/event_id",
    "deprecated": false,
    "key": "event_id",
    "docstring": "The unique ID of the Live server event.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) error_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveErrorEvent/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The event type, always `error`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveErrorEvent/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "error"
        }
      ]
    },
    "default": "error",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) error_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) error_event > (schema) > (property) client_event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveErrorEvent/properties/client_event_id",
    "deprecated": false,
    "key": "client_event_id",
    "docstring": "The event_id of the client command associated with this server event, when supplied.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) error > (schema) > (property) code": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveLiveError/properties/code",
    "deprecated": false,
    "key": "code",
    "docstring": "A machine-readable code identifying the Live error, such as `unknown_parameter`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) error > (schema) > (property) message": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveLiveError/properties/message",
    "deprecated": false,
    "key": "message",
    "docstring": "A human-readable explanation of the Live error.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) error > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveLiveError/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The category of error, such as `invalid_request_error` for an invalid Live client command.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) error > (schema) > (property) client_event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveLiveError/properties/client_event_id",
    "deprecated": false,
    "key": "client_event_id",
    "docstring": "The event_id of the client command that caused the error, when supplied.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) error > (schema) > (property) param": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveLiveError/properties/param",
    "deprecated": false,
    "key": "param",
    "docstring": "The parameter that caused the error, when applicable, such as `session.voice`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) error > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveLiveError",
    "docstring": "Details of an error encountered by the Live session, including the affected parameter or client command when available.",
    "ident": "Error",
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
        },
        {
          "ident": "client_event_id"
        },
        {
          "ident": "param"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) error > (schema) > (property) code",
      "(resource) live > (model) error > (schema) > (property) message",
      "(resource) live > (model) error > (schema) > (property) type",
      "(resource) live > (model) error > (schema) > (property) client_event_id",
      "(resource) live > (model) error > (schema) > (property) param"
    ]
  },
  "(resource) live > (model) error_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "error"
    }
  }
}
```

#### Example

```json
{
  "type": "error",
  "event_id": "evt_error_001",
  "error": {
    "type": "invalid_request_error",
    "code": "unknown_parameter",
    "message": "Unknown parameter: 'session.voice'.",
    "param": "session.voice",
    "client_event_id": "evt_invalid_001"
  }
}
```

### info

An informational notice about the Live session, such as the event permissions applied to a frontend data channel.

#### Schema

Schema name: `LiveInfoEvent`

```json
{
  "(resource) live > (model) info_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInfoEvent",
    "docstring": "An informational notice about the Live session, such as the event permissions applied to a frontend data channel.",
    "ident": "InfoEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "code"
        },
        {
          "ident": "event_id"
        },
        {
          "ident": "message"
        },
        {
          "ident": "type"
        },
        {
          "ident": "client_event_id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) info_event > (schema) > (property) code",
      "(resource) live > (model) info_event > (schema) > (property) event_id",
      "(resource) live > (model) info_event > (schema) > (property) message",
      "(resource) live > (model) info_event > (schema) > (property) type",
      "(resource) live > (model) info_event > (schema) > (property) client_event_id"
    ]
  },
  "(resource) live > (model) info_event > (schema) > (property) code": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInfoEvent/properties/code",
    "deprecated": false,
    "key": "code",
    "docstring": "A machine-readable code for the notice, such as `data_channel_permissions`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) info_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInfoEvent/properties/event_id",
    "deprecated": false,
    "key": "event_id",
    "docstring": "The unique ID of the Live server event.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) info_event > (schema) > (property) message": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInfoEvent/properties/message",
    "deprecated": false,
    "key": "message",
    "docstring": "A human-readable explanation of the Live session notice.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) info_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInfoEvent/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The event type, always `info`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInfoEvent/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "info"
        }
      ]
    },
    "default": "info",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) info_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) info_event > (schema) > (property) client_event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInfoEvent/properties/client_event_id",
    "deprecated": false,
    "key": "client_event_id",
    "docstring": "The event_id of the client command associated with this server event, when supplied.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) info_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "info"
    }
  }
}
```

#### Example

```json
{
  "type": "info",
  "event_id": "evt_info_001",
  "code": "data_channel_permissions",
  "message": "The frontend data channel is configured with restricted event permissions."
}
```

### session.input_audio.append

Input audio received from the primary transport and reflected to a Live sideband connection before model-input muting.

#### Schema

Schema name: `LiveInputAudioAppend`

```json
{
  "(resource) live > (model) server_event > (schema) > (variant) 7": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveServerEvent-2/oneOf/7",
    "docstring": "Input audio received from the primary transport and reflected to a Live sideband connection before model-input muting.",
    "ident": "SessionInputAudioAppend",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "audio"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) server_event > (schema) > (variant) 7 > (property) audio",
      "(resource) live > (model) server_event > (schema) > (variant) 7 > (property) type"
    ]
  },
  "(resource) live > (model) server_event > (schema) > (variant) 7 > (property) audio": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputAudioAppend/properties/audio",
    "deprecated": false,
    "key": "audio",
    "docstring": "Base64-encoded raw mono PCM16LE at 24 kHz received from the primary transport, reflected to the sideband before model-input muting. This server event uses the same audio key as the client command, but is not an acknowledgment of it.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) server_event > (schema) > (variant) 7 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputAudioAppend/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The event type, always `session.input_audio.append`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInputAudioAppend/properties/type",
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
      "(resource) live > (model) server_event > (schema) > (variant) 7 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) server_event > (schema) > (variant) 7 > (property) type > (member) 0": {
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

### transport.dtmf.received

A SIP DTMF keypress received from the caller. Delivered only to sideband observers.

#### Schema

Schema name: `LiveTransportDTMFReceived`

```json
{
  "(resource) live > (model) server_event > (schema) > (variant) 17": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveServerEvent-2/oneOf/17",
    "docstring": "A SIP DTMF keypress received from the caller. Delivered only to sideband observers.",
    "ident": "TransportDtmfReceived",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "event"
        },
        {
          "ident": "event_id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) server_event > (schema) > (variant) 17 > (property) event",
      "(resource) live > (model) server_event > (schema) > (variant) 17 > (property) event_id",
      "(resource) live > (model) server_event > (schema) > (variant) 17 > (property) type"
    ]
  },
  "(resource) live > (model) server_event > (schema) > (variant) 17 > (property) event": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportDTMFReceived/properties/event",
    "deprecated": false,
    "key": "event",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 1
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) server_event > (schema) > (variant) 17 > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportDTMFReceived/properties/event_id",
    "deprecated": false,
    "key": "event_id",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) server_event > (schema) > (variant) 17 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportDTMFReceived/properties/type",
    "deprecated": false,
    "key": "type",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveTransportDTMFReceived/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "transport.dtmf.received"
        }
      ]
    },
    "default": "transport.dtmf.received",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) server_event > (schema) > (variant) 17 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) server_event > (schema) > (variant) 17 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "transport.dtmf.received"
    }
  }
}
```

#### Example

```json
{
  "type": "transport.dtmf.received",
  "event_id": "event_dtmf_1",
  "event": "5"
}
```

### transport.dtmf.send

A SIP DTMF keypress successfully sent by the hosted tool. Delivered only to sideband observers; this is not a client command.

#### Schema

Schema name: `LiveTransportDTMFSend`

```json
{
  "(resource) live > (model) server_event > (schema) > (variant) 18": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveServerEvent-2/oneOf/18",
    "docstring": "A SIP DTMF keypress successfully sent by the hosted tool. Delivered only to sideband observers; this is not a client command.",
    "ident": "TransportDtmfSend",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "event"
        },
        {
          "ident": "event_id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) server_event > (schema) > (variant) 18 > (property) event",
      "(resource) live > (model) server_event > (schema) > (variant) 18 > (property) event_id",
      "(resource) live > (model) server_event > (schema) > (variant) 18 > (property) type"
    ]
  },
  "(resource) live > (model) server_event > (schema) > (variant) 18 > (property) event": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportDTMFSend/properties/event",
    "deprecated": false,
    "key": "event",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 1
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) server_event > (schema) > (variant) 18 > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportDTMFSend/properties/event_id",
    "deprecated": false,
    "key": "event_id",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) server_event > (schema) > (variant) 18 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportDTMFSend/properties/type",
    "deprecated": false,
    "key": "type",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveTransportDTMFSend/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "transport.dtmf.send"
        }
      ]
    },
    "default": "transport.dtmf.send",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) server_event > (schema) > (variant) 18 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) server_event > (schema) > (variant) 18 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "transport.dtmf.send"
    }
  }
}
```

#### Example

```json
{
  "type": "transport.dtmf.send",
  "event_id": "event_dtmf_2",
  "event": "#"
}
```

### transport.ringing

The outbound SIP provider leg is ringing or providing early media. Delivered only to sideband observers.

#### Schema

Schema name: `LiveTransportRinging`

```json
{
  "(resource) live > (model) server_event > (schema) > (variant) 19": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveServerEvent-2/oneOf/19",
    "docstring": "The outbound SIP provider leg is ringing or providing early media. Delivered only to sideband observers.",
    "ident": "TransportRinging",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "event_id"
        },
        {
          "ident": "session_id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) server_event > (schema) > (variant) 19 > (property) event_id",
      "(resource) live > (model) server_event > (schema) > (variant) 19 > (property) session_id",
      "(resource) live > (model) server_event > (schema) > (variant) 19 > (property) type"
    ]
  },
  "(resource) live > (model) server_event > (schema) > (variant) 19 > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportRinging/properties/event_id",
    "deprecated": false,
    "key": "event_id",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) server_event > (schema) > (variant) 19 > (property) session_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportRinging/properties/session_id",
    "deprecated": false,
    "key": "session_id",
    "docstring": "The canonical Live session ID.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) server_event > (schema) > (variant) 19 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportRinging/properties/type",
    "deprecated": false,
    "key": "type",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveTransportRinging/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "transport.ringing"
        }
      ]
    },
    "default": "transport.ringing",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) server_event > (schema) > (variant) 19 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) server_event > (schema) > (variant) 19 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "transport.ringing"
    }
  }
}
```

#### Example

```json
{
  "type": "transport.ringing",
  "event_id": "event_call_1",
  "session_id": "live_u0_123"
}
```

### transport.answered

The outbound SIP provider leg answered and media is established. Delivered only to sideband observers.

#### Schema

Schema name: `LiveTransportAnswered`

```json
{
  "(resource) live > (model) server_event > (schema) > (variant) 20": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveServerEvent-2/oneOf/20",
    "docstring": "The outbound SIP provider leg answered and media is established. Delivered only to sideband observers.",
    "ident": "TransportAnswered",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "event_id"
        },
        {
          "ident": "session_id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) server_event > (schema) > (variant) 20 > (property) event_id",
      "(resource) live > (model) server_event > (schema) > (variant) 20 > (property) session_id",
      "(resource) live > (model) server_event > (schema) > (variant) 20 > (property) type"
    ]
  },
  "(resource) live > (model) server_event > (schema) > (variant) 20 > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportAnswered/properties/event_id",
    "deprecated": false,
    "key": "event_id",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) server_event > (schema) > (variant) 20 > (property) session_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportAnswered/properties/session_id",
    "deprecated": false,
    "key": "session_id",
    "docstring": "The canonical Live session ID.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) server_event > (schema) > (variant) 20 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportAnswered/properties/type",
    "deprecated": false,
    "key": "type",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveTransportAnswered/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "transport.answered"
        }
      ]
    },
    "default": "transport.answered",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) server_event > (schema) > (variant) 20 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) server_event > (schema) > (variant) 20 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "transport.answered"
    }
  }
}
```

#### Example

```json
{
  "type": "transport.answered",
  "event_id": "event_call_2",
  "session_id": "live_u0_123"
}
```

### transport.failed

An asynchronous outbound SIP setup failure. Delivered only to sideband observers.

#### Schema

Schema name: `LiveTransportFailed`

```json
{
  "(resource) live > (model) server_event > (schema) > (variant) 21": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveServerEvent-2/oneOf/21",
    "docstring": "An asynchronous outbound SIP setup failure. Delivered only to sideband observers.",
    "ident": "TransportFailed",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "error"
        },
        {
          "ident": "event_id"
        },
        {
          "ident": "session_id"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) error",
      "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) event_id",
      "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) session_id",
      "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) type"
    ]
  },
  "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) error": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportFailed/properties/error",
    "deprecated": false,
    "key": "error",
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
        },
        {
          "ident": "param"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) error > (property) code",
      "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) error > (property) message",
      "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) error > (property) type",
      "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) error > (property) param"
    ]
  },
  "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportFailed/properties/event_id",
    "deprecated": false,
    "key": "event_id",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) session_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportFailed/properties/session_id",
    "deprecated": false,
    "key": "session_id",
    "docstring": "The canonical Live session ID.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportFailed/properties/type",
    "deprecated": false,
    "key": "type",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveTransportFailed/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "transport.failed"
        }
      ]
    },
    "default": "transport.failed",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) error > (property) code": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportCallError/properties/code",
    "deprecated": false,
    "key": "code",
    "docstring": "The call setup failure code.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) error > (property) message": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportCallError/properties/message",
    "deprecated": false,
    "key": "message",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) error > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportCallError/properties/type",
    "deprecated": false,
    "key": "type",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveTransportCallError/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "call_error"
        }
      ]
    },
    "default": "call_error",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) error > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) error > (property) param": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveTransportCallError/properties/param",
    "deprecated": false,
    "key": "param",
    "docstring": "The parameter related to the error, if any. Empty when no parameter applies.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "transport.failed"
    }
  },
  "(resource) live > (model) server_event > (schema) > (variant) 21 > (property) error > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "call_error"
    }
  }
}
```

#### Example

```json
{
  "type": "transport.failed",
  "event_id": "event_call_4",
  "session_id": "live_u0_123",
  "error": {
    "type": "call_error",
    "code": "provider_invite_failed",
    "message": "provider rejected the call",
    "param": ""
  }
}
```

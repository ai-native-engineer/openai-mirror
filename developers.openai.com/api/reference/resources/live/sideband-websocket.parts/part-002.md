<!-- source: https://developers.openai.com/api/reference/resources/live/sideband-websocket/ -->
<!-- part of: https://developers.openai.com/api/reference/resources/live/sideband-websocket/ -->

<!-- chunk-start -->
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Annotation/oneOf/0",
    "docstring": "A citation to a file.",
    "ident": "FileCitation",
    "type": {
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
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 0 > (property) file_id",
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 0 > (property) filename",
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 0 > (property) index",
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 0 > (property) type"
    ]
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Annotation/oneOf/1",
    "docstring": "A citation for a web resource used to generate a model response.",
    "ident": "URLCitation",
    "type": {
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
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 1 > (property) end_index",
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 1 > (property) start_index",
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 1 > (property) title",
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 1 > (property) type",
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 1 > (property) url"
    ]
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Annotation/oneOf/2",
    "docstring": "A citation for a container file used to generate a model response.",
    "ident": "ContainerFileCitation",
    "type": {
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
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 2 > (property) container_id",
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 2 > (property) end_index",
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 2 > (property) file_id",
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 2 > (property) filename",
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 2 > (property) start_index",
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 2 > (property) type"
    ]
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 3": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/Annotation/oneOf/3",
    "docstring": "A path to a file.\n",
    "ident": "FilePath",
    "type": {
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
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 3 > (property) file_id",
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 3 > (property) index",
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 3 > (property) type"
    ]
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) logprobs > (items) > (property) token": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LogProb/properties/token",
    "deprecated": false,
    "key": "token",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) logprobs > (items) > (property) bytes": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LogProb/properties/bytes",
    "deprecated": false,
    "key": "bytes",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/LogProb/properties/bytes",
      "elementType": {
        "kind": "HttpTypeNumber"
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) logprobs > (items) > (property) logprob": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LogProb/properties/logprob",
    "deprecated": false,
    "key": "logprob",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) logprobs > (items) > (property) top_logprobs": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LogProb/properties/top_logprobs",
    "deprecated": false,
    "key": "top_logprobs",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/LogProb/properties/top_logprobs",
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
          }
        ]
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) response_output_text > (schema) > (property) logprobs > (items) > (property) top_logprobs > (items) > (property) token",
      "(resource) responses > (model) response_output_text > (schema) > (property) logprobs > (items) > (property) top_logprobs > (items) > (property) bytes",
      "(resource) responses > (model) response_output_text > (schema) > (property) logprobs > (items) > (property) top_logprobs > (items) > (property) logprob"
    ]
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "output_text"
    }
  },
  "(resource) responses > (model) response_output_refusal > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "refusal"
    }
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) button > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "left"
    }
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) button > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "right"
    }
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) button > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "wheel"
    }
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) button > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "back"
    }
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) button > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "forward"
    }
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "click"
    }
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "double_click"
    }
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 2 > (property) path > (items) > (property) x": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CoordParam/properties/x",
    "deprecated": false,
    "key": "x",
    "docstring": "The x-coordinate.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 2 > (property) path > (items) > (property) y": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CoordParam/properties/y",
    "deprecated": false,
    "key": "y",
    "docstring": "The y-coordinate.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 2 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "drag"
    }
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 3 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "keypress"
    }
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 4 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "move"
    }
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 5 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "screenshot"
    }
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 6 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "scroll"
    }
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 7 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "type"
    }
  },
  "(resource) responses > (model) computer_action > (schema) > (variant) 8 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "wait"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "search"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0 > (property) sources > (items) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchActionSearch/properties/sources/items/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of source. Always `url`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/WebSearchActionSearch/properties/sources/items/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "url"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0 > (property) sources > (items) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0 > (property) sources > (items) > (property) url": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchActionSearch/properties/sources/items/properties/url",
    "deprecated": false,
    "key": "url",
    "docstring": "The URL of the source.\n",
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "open_page"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 2 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "find_in_page"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) caller > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 7 > (property) caller > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "program"
    }
  },
  "(resource) responses > (model) response_input_text_content > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "input_text"
    }
  },
  "(resource) responses > (model) response_input_text_content > (schema) > (property) prompt_cache_breakpoint > (property) mode": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/PromptCacheBreakpointParam/properties/mode",
    "deprecated": false,
    "key": "mode",
    "docstring": "The breakpoint mode. Always `explicit`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/PromptCacheBreakpointParam/properties/mode",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "explicit"
        }
      ]
    },
    "default": "explicit",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_text_content > (schema) > (property) prompt_cache_breakpoint > (property) mode > (member) 0"
    ]
  },
  "(resource) responses > (model) response_input_image_content > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "input_image"
    }
  },
  "(resource) responses > (model) response_input_image_content > (schema) > (property) prompt_cache_breakpoint > (property) mode": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/PromptCacheBreakpointParam/properties/mode",
    "deprecated": false,
    "key": "mode",
    "docstring": "The breakpoint mode. Always `explicit`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/PromptCacheBreakpointParam/properties/mode",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "explicit"
        }
      ]
    },
    "default": "explicit",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_image_content > (schema) > (property) prompt_cache_breakpoint > (property) mode > (member) 0"
    ]
  },
  "(resource) responses > (model) response_input_file_content > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "input_file"
    }
  },
  "(resource) responses > (model) response_input_file_content > (schema) > (property) detail > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) responses > (model) response_input_file_content > (schema) > (property) detail > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) responses > (model) response_input_file_content > (schema) > (property) detail > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) responses > (model) response_input_file_content > (schema) > (property) prompt_cache_breakpoint > (property) mode": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/PromptCacheBreakpointParam/properties/mode",
    "deprecated": false,
    "key": "mode",
    "docstring": "The breakpoint mode. Always `explicit`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/PromptCacheBreakpointParam/properties/mode",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "explicit"
        }
      ]
    },
    "default": "explicit",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_input_file_content > (schema) > (property) prompt_cache_breakpoint > (property) mode > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) caller > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 8 > (property) caller > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "program"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) allowed_callers > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 0 > (property) allowed_callers > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "file_search"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) filters > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ComparisonFilter",
      "$ref": "(resource) $shared > (model) comparison_filter > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) comparison_filter > (schema) > (property) key",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) type",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) value"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) filters > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "CompoundFilter",
      "$ref": "(resource) $shared > (model) compound_filter > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) compound_filter > (schema) > (property) filters",
      "(resource) $shared > (model) compound_filter > (schema) > (property) type"
    ]
  },
  "(resource) $shared > (model) comparison_filter > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComparisonFilter",
    "docstring": "A filter used to compare a specified attribute key to a given value using a defined comparison operation.\n",
    "ident": "ComparisonFilter",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "key"
        },
        {
          "ident": "type"
        },
        {
          "ident": "value"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) comparison_filter > (schema) > (property) key",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) type",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) value"
    ]
  },
  "(resource) $shared > (model) compound_filter > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/CompoundFilter",
    "docstring": "Combine multiple filters using `and` or `or`.",
    "ident": "CompoundFilter",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "filters"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) compound_filter > (schema) > (property) filters",
      "(resource) $shared > (model) compound_filter > (schema) > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) hybrid_search": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/RankingOptions/properties/hybrid_search",
    "deprecated": false,
    "key": "hybrid_search",
    "docstring": "Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "embedding_weight"
        },
        {
          "ident": "text_weight"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) hybrid_search > (property) embedding_weight",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) hybrid_search > (property) text_weight"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) ranker": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/RankingOptions/properties/ranker",
    "deprecated": false,
    "key": "ranker",
    "docstring": "The ranker to use for the file search.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/RankingOptions/properties/ranker",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "default-2024-11-15"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) ranker > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) ranker > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) score_threshold": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/RankingOptions/properties/score_threshold",
    "deprecated": false,
    "key": "score_threshold",
    "docstring": "The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 2 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "computer"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "windows"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mac"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "linux"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "ubuntu"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "browser"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 3 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "computer_use_preview"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "web_search"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) type > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "web_search_2025_08_26"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) filters > (property) allowed_domains": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchTool/properties/filters/anyOf/0/properties/allowed_domains",
    "deprecated": false,
    "key": "allowed_domains",
    "docstring": "Allowed domains for the search. If not provided, all domains are allowed.\nSubdomains of the provided domains are allowed as well.\n\nExample: `[\"pubmed.ncbi.nlm.nih.gov\"]`\n",
    "title": "Allowed domains for the search.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/WebSearchTool/properties/filters/anyOf/0/properties/allowed_domains",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "default": [],
    "optional": true,
    "nullable": true,
    "schemaType": "array",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) search_context_size > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) search_context_size > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "medium"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) search_context_size > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) city": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchApproximateLocation/anyOf/0/properties/city",
    "deprecated": false,
    "key": "city",
    "docstring": "Free text input for the city of the user, e.g. `San Francisco`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) country": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchApproximateLocation/anyOf/0/properties/country",
    "deprecated": false,
    "key": "country",
    "docstring": "The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) region": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchApproximateLocation/anyOf/0/properties/region",
    "deprecated": false,
    "key": "region",
    "docstring": "Free text input for the region of the user, e.g. `California`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) timezone": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchApproximateLocation/anyOf/0/properties/timezone",
    "deprecated": false,
    "key": "timezone",
    "docstring": "The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchApproximateLocation/anyOf/0/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of location approximation. Always `approximate`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/WebSearchApproximateLocation/anyOf/0/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "approximate"
        }
      ]
    },
    "default": "approximate",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mcp"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) allowed_callers > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) allowed_callers > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) allowed_tools > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools/anyOf/0/oneOf/0",
    "docstring": "A string array of allowed tool names",
    "ident": "McpAllowedTools",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools/anyOf/0/oneOf/0",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) allowed_tools > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools/anyOf/0/oneOf/1",
    "docstring": "A filter object to specify which tools are allowed.\n",
    "ident": "McpToolFilter",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "read_only"
        },
        {
          "ident": "tool_names"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) allowed_tools > (variant) 1 > (property) read_only",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) allowed_tools > (variant) 1 > (property) tool_names"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_dropbox"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_gmail"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_googlecalendar"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_googledrive"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_microsoftteams"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_outlookcalendar"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 6": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_outlookemail"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 7": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_sharepoint"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/MCPTool/properties/require_approval/anyOf/0/oneOf/0",
    "docstring": "Specify which of the MCP server's tools require approval. Can be\n`always`, `never`, or a filter object associated with tools\nthat require approval.\n",
    "ident": "McpToolApprovalFilter",
    "type": {
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
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) always",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) never"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/MCPTool/properties/require_approval/anyOf/0/oneOf/1",
    "docstring": "Specify a single approval policy for all tools. One of `always` or\n`never`. When set to `always`, all tools will require approval. When\nset to `never`, all tools will not require approval.\n",
    "ident": "McpToolApprovalSetting",
    "type": {
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
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 1 > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 1 > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/CodeInterpreterTool/properties/container/oneOf/0",
    "docstring": "The container ID.",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/CodeInterpreterTool/properties/container/oneOf/1",
    "docstring": "Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.",
    "ident": "CodeInterpreterToolAuto",
    "type": {
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
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) file_ids",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) network_policy"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "code_interpreter"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) allowed_callers > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) allowed_callers > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 7 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic_tool_calling"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "image_generation"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) action > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "generate"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) action > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "edit"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) action > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) background > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "transparent"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) background > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "opaque"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) background > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) input_fidelity > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) input_fidelity > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) input_image_mask > (property) file_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/input_image_mask/properties/file_id",
    "deprecated": false,
    "key": "file_id",
    "docstring": "File ID for the mask image.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) input_image_mask > (property) image_url": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/input_image_mask/properties/image_url",
    "deprecated": false,
    "key": "image_url",
    "docstring": "Base64-encoded mask image.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ImageGenTool/properties/model/anyOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ImageGenTool/properties/model/anyOf/1",
    "docstring": "The image generation model to use. One of `gpt-image-1`,\n`gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,\n`gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,\n`gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,\n`gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:\n`gpt-image-1`.\n",
    "ident": "UnionMember1",
    "type": {
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
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 3",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 4",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 5",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 6",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 7",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 8"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) moderation > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) moderation > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) output_format > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "png"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) output_format > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "webp"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) output_format > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "jpeg"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "medium"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "xhigh"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "max"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ImageGenTool/properties/size/anyOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ImageGenTool/properties/size/anyOf/1",
    "docstring": "The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model's current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.",
    "ident": "UnionMember1",
    "type": {
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
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1 > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1 > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1 > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1 > (member) 3"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 9 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "local_shell"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "shell"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) allowed_callers > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) allowed_callers > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) environment > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ContainerAuto",
      "$ref": "(resource) responses > (model) container_auto > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) container_auto > (schema) > (property) type",
      "(resource) responses > (model) container_auto > (schema) > (property) file_ids",
      "(resource) responses > (model) container_auto > (schema) > (property) memory_limit",
      "(resource) responses > (model) container_auto > (schema) > (property) network_policy",
      "(resource) responses > (model) container_auto > (schema) > (property) skills"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) environment > (variant) 1": {
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 10 > (property) environment > (variant) 2": {
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
  "(resource) responses > (model) container_auto > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ContainerAutoParam",
    "ident": "ContainerAuto",
    "type": {
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
        },
        {
          "ident": "skills"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) container_auto > (schema) > (property) type",
      "(resource) responses > (model) container_auto > (schema) > (property) file_ids",
      "(resource) responses > (model) container_auto > (schema) > (property) memory_limit",
      "(resource) responses > (model) container_auto > (schema) > (property) network_policy",
      "(resource) responses > (model) container_auto > (schema) > (property) skills"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "custom"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) allowed_callers > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 11 > (property) allowed_callers > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic"
    }
  },
  "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/CustomToolParam/properties/format/oneOf/0",
    "docstring": "Unconstrained free-form text.",
    "ident": "Text",
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
      "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 0 > (property) type"
    ]
  },
  "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/CustomToolParam/properties/format/oneOf/1",
    "docstring": "A grammar defined by the user.",
    "ident": "Grammar",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "definition"
        },
        {
          "ident": "syntax"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 1 > (property) definition",
      "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 1 > (property) syntax",
      "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 1 > (property) type"
    ]
  },
  "(resource) $shared > (model) custom_tool_input_format > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/CustomToolParam/properties/format",
    "docstring": "The input format for the custom tool. Default is unconstrained text.",
    "ident": "CustomToolInputFormat",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CustomToolParam/properties/format",
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
              "ident": "definition"
            },
            {
              "ident": "syntax"
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
      "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 0",
      "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/NamespaceToolParam/properties/tools/items/oneOf/0",
    "ident": "Function",
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
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) name",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) allowed_callers",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) async",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) defer_loading",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) description",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) output_schema",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) parameters",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) strict"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/NamespaceToolParam/properties/tools/items/oneOf/1",
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
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) name",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) allowed_callers",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) async",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) defer_loading",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) description",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) format"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "namespace"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 13 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "tool_search"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 13 > (property) execution > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "server"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 13 > (property) execution > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "client"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "web_search_preview"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) type > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "web_search_preview_2025_03_11"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) search_content_types > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "text"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) search_content_types > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "image"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) search_context_size > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) search_context_size > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "medium"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) search_context_size > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApproximateLocation/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of location approximation. Always `approximate`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ApproximateLocation/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "approximate"
        }
      ]
    },
    "default": "approximate",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) city": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApproximateLocation/properties/city",
    "deprecated": false,
    "key": "city",
    "docstring": "Free text input for the city of the user, e.g. `San Francisco`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) country": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApproximateLocation/properties/country",
    "deprecated": false,
    "key": "country",
    "docstring": "The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) region": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApproximateLocation/properties/region",
    "deprecated": false,
    "key": "region",
    "docstring": "Free text input for the region of the user, e.g. `California`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) timezone": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApproximateLocation/properties/timezone",
    "deprecated": false,
    "key": "timezone",
    "docstring": "The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 15 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "apply_patch"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 15 > (property) allowed_callers > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 15 > (property) allowed_callers > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) allowed_callers > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 0 > (property) allowed_callers > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "file_search"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) filters > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ComparisonFilter",
      "$ref": "(resource) $shared > (model) comparison_filter > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) comparison_filter > (schema) > (property) key",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) type",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) value"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) filters > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "CompoundFilter",
      "$ref": "(resource) $shared > (model) compound_filter > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) compound_filter > (schema) > (property) filters",
      "(resource) $shared > (model) compound_filter > (schema) > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) hybrid_search": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/RankingOptions/properties/hybrid_search",
    "deprecated": false,
    "key": "hybrid_search",
    "docstring": "Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "embedding_weight"
        },
        {
          "ident": "text_weight"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) hybrid_search > (property) embedding_weight",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) hybrid_search > (property) text_weight"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) ranker": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/RankingOptions/properties/ranker",
    "deprecated": false,
    "key": "ranker",
    "docstring": "The ranker to use for the file search.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/RankingOptions/properties/ranker",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "default-2024-11-15"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) ranker > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) ranker > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) score_threshold": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/RankingOptions/properties/score_threshold",
    "deprecated": false,
    "key": "score_threshold",
    "docstring": "The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 2 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "computer"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "windows"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mac"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "linux"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "ubuntu"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) environment > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "browser"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 3 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "computer_use_preview"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "web_search"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) type > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "web_search_2025_08_26"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) filters > (property) allowed_domains": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchTool/properties/filters/anyOf/0/properties/allowed_domains",
    "deprecated": false,
    "key": "allowed_domains",
    "docstring": "Allowed domains for the search. If not provided, all domains are allowed.\nSubdomains of the provided domains are allowed as well.\n\nExample: `[\"pubmed.ncbi.nlm.nih.gov\"]`\n",
    "title": "Allowed domains for the search.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/WebSearchTool/properties/filters/anyOf/0/properties/allowed_domains",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "default": [],
    "optional": true,
    "nullable": true,
    "schemaType": "array",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) search_context_size > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) search_context_size > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "medium"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) search_context_size > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) city": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchApproximateLocation/anyOf/0/properties/city",
    "deprecated": false,
    "key": "city",
    "docstring": "Free text input for the city of the user, e.g. `San Francisco`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) country": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchApproximateLocation/anyOf/0/properties/country",
    "deprecated": false,
    "key": "country",
    "docstring": "The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) region": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchApproximateLocation/anyOf/0/properties/region",
    "deprecated": false,
    "key": "region",
    "docstring": "Free text input for the region of the user, e.g. `California`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) timezone": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchApproximateLocation/anyOf/0/properties/timezone",
    "deprecated": false,
    "key": "timezone",
    "docstring": "The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/WebSearchApproximateLocation/anyOf/0/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of location approximation. Always `approximate`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/WebSearchApproximateLocation/anyOf/0/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "approximate"
        }
      ]
    },
    "default": "approximate",
    "optional": true,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mcp"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) allowed_callers > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) allowed_callers > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) allowed_tools > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools/anyOf/0/oneOf/0",
    "docstring": "A string array of allowed tool names",
    "ident": "McpAllowedTools",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools/anyOf/0/oneOf/0",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) allowed_tools > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/MCPTool/properties/allowed_tools/anyOf/0/oneOf/1",
    "docstring": "A filter object to specify which tools are allowed.\n",
    "ident": "McpToolFilter",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "read_only"
        },
        {
          "ident": "tool_names"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) allowed_tools > (variant) 1 > (property) read_only",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) allowed_tools > (variant) 1 > (property) tool_names"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_dropbox"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_gmail"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_googlecalendar"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_googledrive"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_microsoftteams"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_outlookcalendar"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 6": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_outlookemail"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) connector_id > (member) 7": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connector_sharepoint"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/MCPTool/properties/require_approval/anyOf/0/oneOf/0",
    "docstring": "Specify which of the MCP server's tools require approval. Can be\n`always`, `never`, or a filter object associated with tools\nthat require approval.\n",
    "ident": "McpToolApprovalFilter",
    "type": {
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
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) always",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) never"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/MCPTool/properties/require_approval/anyOf/0/oneOf/1",
    "docstring": "Specify a single approval policy for all tools. One of `always` or\n`never`. When set to `always`, all tools will require approval. When\nset to `never`, all tools will not require approval.\n",
    "ident": "McpToolApprovalSetting",
    "type": {
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
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 1 > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 1 > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/CodeInterpreterTool/properties/container/oneOf/0",
    "docstring": "The container ID.",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/CodeInterpreterTool/properties/container/oneOf/1",
    "docstring": "Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.",
    "ident": "CodeInterpreterToolAuto",
    "type": {
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
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) file_ids",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) network_policy"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "code_interpreter"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) allowed_callers > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) allowed_callers > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 7 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic_tool_calling"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "image_generation"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) action > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "generate"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) action > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "edit"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) action > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) background > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "transparent"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) background > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "opaque"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) background > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) input_fidelity > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) input_fidelity > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) input_image_mask > (property) file_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/input_image_mask/properties/file_id",
    "deprecated": false,
    "key": "file_id",
    "docstring": "File ID for the mask image.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) input_image_mask > (property) image_url": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ImageGenTool/properties/input_image_mask/properties/image_url",
    "deprecated": false,
    "key": "image_url",
    "docstring": "Base64-encoded mask image.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ImageGenTool/properties/model/anyOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ImageGenTool/properties/model/anyOf/1",
    "docstring": "The image generation model to use. One of `gpt-image-1`,\n`gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,\n`gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,\n`gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,\n`gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:\n`gpt-image-1`.\n",
    "ident": "UnionMember1",
    "type": {
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
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 3",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 4",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 5",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 6",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 7",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 8"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) moderation > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) moderation > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) output_format > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "png"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) output_format > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "webp"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) output_format > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "jpeg"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "medium"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "xhigh"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "max"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) quality > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ImageGenTool/properties/size/anyOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ImageGenTool/properties/size/anyOf/1",
    "docstring": "The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model's current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.",
    "ident": "UnionMember1",
    "type": {
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
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1 > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1 > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1 > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1 > (member) 3"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 9 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "local_shell"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 10 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "shell"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 10 > (property) allowed_callers > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 10 > (property) allowed_callers > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 10 > (property) environment > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ContainerAuto",
      "$ref": "(resource) responses > (model) container_auto > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) container_auto > (schema) > (property) type",
      "(resource) responses > (model) container_auto > (schema) > (property) file_ids",
      "(resource) responses > (model) container_auto > (schema) > (property) memory_limit",
      "(resource) responses > (model) container_auto > (schema) > (property) network_policy",
      "(resource) responses > (model) container_auto > (schema) > (property) skills"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 10 > (property) environment > (variant) 1": {
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 10 > (property) environment > (variant) 2": {
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 11 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "custom"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 11 > (property) allowed_callers > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 11 > (property) allowed_callers > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/NamespaceToolParam/properties/tools/items/oneOf/0",
    "ident": "Function",
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
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) name",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) allowed_callers",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) async",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) defer_loading",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) description",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) output_schema",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) parameters",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) strict"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/NamespaceToolParam/properties/tools/items/oneOf/1",
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
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) name",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) type",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) allowed_callers",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) async",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) defer_loading",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) description",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) format"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "namespace"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 13 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "tool_search"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 13 > (property) execution > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "server"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 13 > (property) execution > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "client"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "web_search_preview"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) type > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "web_search_preview_2025_03_11"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) search_content_types > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "text"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) search_content_types > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "image"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) search_context_size > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "low"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) search_context_size > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "medium"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) search_context_size > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "high"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApproximateLocation/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of location approximation. Always `approximate`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ApproximateLocation/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "approximate"
        }
      ]
    },
    "default": "approximate",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) city": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApproximateLocation/properties/city",
    "deprecated": false,
    "key": "city",
    "docstring": "Free text input for the city of the user, e.g. `San Francisco`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) country": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApproximateLocation/properties/country",
    "deprecated": false,
    "key": "country",
    "docstring": "The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) region": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApproximateLocation/properties/region",
    "deprecated": false,
    "key": "region",
    "docstring": "Free text input for the region of the user, e.g. `California`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) timezone": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ApproximateLocation/properties/timezone",
    "deprecated": false,
    "key": "timezone",
    "docstring": "The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 15 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "apply_patch"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 15 > (property) allowed_callers > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 15 > (property) allowed_callers > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) outputs > (items) > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "logs"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 16 > (property) outputs > (items) > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "image"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) caller > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 19 > (property) caller > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "program"
    }
  },
  "(resource) responses > (model) local_environment > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "local"
    }
  },
  "(resource) responses > (model) local_skill > (schema) > (property) description": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalSkillParam/properties/description",
    "deprecated": false,
    "key": "description",
    "docstring": "The description of the skill.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) local_skill > (schema) > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalSkillParam/properties/name",
    "deprecated": false,
    "key": "name",
    "docstring": "The name of the skill.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) local_skill > (schema) > (property) path": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LocalSkillParam/properties/path",
    "deprecated": false,
    "key": "path",
    "docstring": "The path to the directory containing the skill.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) local_skill > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LocalSkillParam",
    "ident": "LocalSkill",
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
          "ident": "path"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) local_skill > (schema) > (property) description",
      "(resource) responses > (model) local_skill > (schema) > (property) name",
      "(resource) responses > (model) local_skill > (schema) > (property) path"
    ]
  },
  "(resource) responses > (model) container_reference > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "container_reference"
    }
  },
  "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) outcome > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallOutputTimeoutOutcomeParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The outcome type. Always `timeout`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionShellCallOutputTimeoutOutcomeParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "timeout"
        }
      ]
    },
    "default": "timeout",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) outcome > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) outcome > (variant) 1 > (property) exit_code": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallOutputExitOutcomeParam/properties/exit_code",
    "deprecated": false,
    "key": "exit_code",
    "docstring": "The exit code returned by the shell process.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) outcome > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionShellCallOutputExitOutcomeParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The outcome type. Always `exit`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionShellCallOutputExitOutcomeParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "exit"
        }
      ]
    },
    "default": "exit",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) outcome > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) caller > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 20 > (property) caller > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "program"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "create_file"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "delete_file"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) operation > (variant) 2 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "update_file"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) caller > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 21 > (property) caller > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "program"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) caller > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 22 > (property) caller > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "program"
    }
  },
  "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mcp_protocol_error"
    }
  },
  "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "mcp_tool_execution_error"
    }
  },
  "(resource) responses > (model) mcp_tool_call_error > (schema) > (variant) 2 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "http_error"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) caller > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 27 > (property) caller > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "program"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) caller > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 28 > (property) caller > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "program"
    }
  },
  "(resource) responses > (model) response_input_text > (schema) > (property) prompt_cache_breakpoint > (property) mode > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "explicit"
    }
  },
  "(resource) responses > (model) response_input_image > (schema) > (property) prompt_cache_breakpoint > (property) mode > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "explicit"
    }
  },
  "(resource) responses > (model) response_input_file > (schema) > (property) prompt_cache_breakpoint > (property) mode > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "explicit"
    }
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 0 > (property) file_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileCitationBody/properties/file_id",
    "deprecated": false,
    "key": "file_id",
    "docstring": "The ID of the file.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 0 > (property) filename": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileCitationBody/properties/filename",
    "deprecated": false,
    "key": "filename",
    "docstring": "The filename of the file cited.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 0 > (property) index": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileCitationBody/properties/index",
    "deprecated": false,
    "key": "index",
    "docstring": "The index of the file in the list of files.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FileCitationBody/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the file citation. Always `file_citation`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FileCitationBody/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "file_citation"
        }
      ]
    },
    "default": "file_citation",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 1 > (property) end_index": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/UrlCitationBody/properties/end_index",
    "deprecated": false,
    "key": "end_index",
    "docstring": "The index of the last character of the URL citation in the message.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 1 > (property) start_index": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/UrlCitationBody/properties/start_index",
    "deprecated": false,
    "key": "start_index",
    "docstring": "The index of the first character of the URL citation in the message.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 1 > (property) title": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/UrlCitationBody/properties/title",
    "deprecated": false,
    "key": "title",
    "docstring": "The title of the web resource.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/UrlCitationBody/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the URL citation. Always `url_citation`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/UrlCitationBody/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "url_citation"
        }
      ]
    },
    "default": "url_citation",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 1 > (property) url": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/UrlCitationBody/properties/url",
    "deprecated": false,
    "key": "url",
    "docstring": "The URL of the web resource.",
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
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 2 > (property) container_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerFileCitationBody/properties/container_id",
    "deprecated": false,
    "key": "container_id",
    "docstring": "The ID of the container file.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 2 > (property) end_index": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerFileCitationBody/properties/end_index",
    "deprecated": false,
    "key": "end_index",
    "docstring": "The index of the last character of the container file citation in the message.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 2 > (property) file_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerFileCitationBody/properties/file_id",
    "deprecated": false,
    "key": "file_id",
    "docstring": "The ID of the file.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 2 > (property) filename": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerFileCitationBody/properties/filename",
    "deprecated": false,
    "key": "filename",
    "docstring": "The filename of the container file cited.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 2 > (property) start_index": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerFileCitationBody/properties/start_index",
    "deprecated": false,
    "key": "start_index",
    "docstring": "The index of the first character of the container file citation in the message.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 2 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerFileCitationBody/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the container file citation. Always `container_file_citation`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ContainerFileCitationBody/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "container_file_citation"
        }
      ]
    },
    "default": "container_file_citation",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 2 > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 3 > (property) file_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FilePath/properties/file_id",
    "deprecated": false,
    "key": "file_id",
    "docstring": "The ID of the file.\n",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 3 > (property) index": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FilePath/properties/index",
    "deprecated": false,
    "key": "index",
    "docstring": "The index of the file in the list of files.\n",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 3 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FilePath/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the file path. Always `file_path`.\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FilePath/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "file_path"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 3 > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) logprobs > (items) > (property) top_logprobs > (items) > (property) token": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/TopLogProb/properties/token",
    "deprecated": false,
    "key": "token",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) logprobs > (items) > (property) top_logprobs > (items) > (property) bytes": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/TopLogProb/properties/bytes",
    "deprecated": false,
    "key": "bytes",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/TopLogProb/properties/bytes",
      "elementType": {
        "kind": "HttpTypeNumber"
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) logprobs > (items) > (property) top_logprobs > (items) > (property) logprob": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/TopLogProb/properties/logprob",
    "deprecated": false,
    "key": "logprob",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 6 > (property) action > (variant) 0 > (property) sources > (items) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "url"
    }
  },
  "(resource) responses > (model) response_input_text_content > (schema) > (property) prompt_cache_breakpoint > (property) mode > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "explicit"
    }
  },
  "(resource) responses > (model) response_input_image_content > (schema) > (property) prompt_cache_breakpoint > (property) mode > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "explicit"
    }
  },
  "(resource) responses > (model) response_input_file_content > (schema) > (property) prompt_cache_breakpoint > (property) mode > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "explicit"
    }
  },
  "(resource) $shared > (model) comparison_filter > (schema) > (property) key": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComparisonFilter/properties/key",
    "deprecated": false,
    "key": "key",
    "docstring": "The key to compare against the value.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) $shared > (model) comparison_filter > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComparisonFilter/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.\n- `eq`: equals\n- `ne`: not equal\n- `gt`: greater than\n- `gte`: greater than or equal\n- `lt`: less than\n- `lte`: less than or equal\n- `in`: in\n- `nin`: not in\n",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ComparisonFilter/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "eq"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "ne"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gt"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "gte"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "lt"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "lte"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "in"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "nin"
        }
      ]
    },
    "default": "eq",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) $shared > (model) comparison_filter > (schema) > (property) type > (member) 0",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) type > (member) 1",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) type > (member) 2",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) type > (member) 3",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) type > (member) 4",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) type > (member) 5",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) type > (member) 6",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) type > (member) 7"
    ]
  },
  "(resource) $shared > (model) comparison_filter > (schema) > (property) value": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ComparisonFilter/properties/value",
    "deprecated": false,
    "key": "value",
    "docstring": "The value to compare against the attribute key; supports string, number, or boolean types.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ComparisonFilter/properties/value",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeNumber"
        },
        {
          "kind": "HttpTypeBoolean"
        },
        {
          "kind": "HttpTypeArray",
          "oasRef": "#/components/schemas/ComparisonFilter/properties/value/oneOf/3",
          "elementType": {
            "kind": "HttpTypeUnion",
            "oasRef": "#/components/schemas/ComparisonFilter/properties/value/oneOf/3/items",
            "types": [
              {
                "kind": "HttpTypeString"
              },
              {
                "kind": "HttpTypeNumber"
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
      "(resource) $shared > (model) comparison_filter > (schema) > (property) value > (variant) 0",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) value > (variant) 1",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) value > (variant) 2",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) value > (variant) 3"
    ]
  },
  "(resource) $shared > (model) compound_filter > (schema) > (property) filters": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CompoundFilter/properties/filters",
    "deprecated": false,
    "key": "filters",
    "docstring": "Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/CompoundFilter/properties/filters",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/CompoundFilter/properties/filters/items",
        "types": [
          {
            "kind": "HttpTypeReference",
            "ident": "ComparisonFilter",
            "$ref": "(resource) $shared > (model) comparison_filter > (schema)"
          },
          {
            "kind": "HttpTypeUnknown"
          }
        ]
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) $shared > (model) compound_filter > (schema) > (property) filters > (items) > (variant) 0",
      "(resource) $shared > (model) compound_filter > (schema) > (property) filters > (items) > (variant) 1"
    ]
  },
  "(resource) $shared > (model) compound_filter > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CompoundFilter/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Type of operation: `and` or `or`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CompoundFilter/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "and"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "or"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) $shared > (model) compound_filter > (schema) > (property) type > (member) 0",
      "(resource) $shared > (model) compound_filter > (schema) > (property) type > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) hybrid_search > (property) embedding_weight": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/HybridSearchOptions/properties/embedding_weight",
    "deprecated": false,
    "key": "embedding_weight",
    "docstring": "The weight of the embedding in the reciprocal ranking fusion.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) hybrid_search > (property) text_weight": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/HybridSearchOptions/properties/text_weight",
    "deprecated": false,
    "key": "text_weight",
    "docstring": "The weight of the text in the reciprocal ranking fusion.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) ranker > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) ranker > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "default-2024-11-15"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "approximate"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) allowed_tools > (variant) 1 > (property) read_only": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolFilter/properties/read_only",
    "deprecated": false,
    "key": "read_only",
    "docstring": "Indicates whether or not a tool modifies data or is read-only. If an\nMCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),\nit will match this filter.\n",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) allowed_tools > (variant) 1 > (property) tool_names": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolFilter/properties/tool_names",
    "deprecated": false,
    "key": "tool_names",
    "docstring": "List of allowed tool names.",
    "title": "MCP allowed tools",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/MCPToolFilter/properties/tool_names",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) always": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/require_approval/anyOf/0/oneOf/0/properties/always",
    "deprecated": false,
    "key": "always",
    "docstring": "A filter object to specify which tools are allowed.\n",
    "title": "MCP tool filter",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "read_only"
        },
        {
          "ident": "tool_names"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) always > (property) read_only",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) always > (property) tool_names"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) never": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/require_approval/anyOf/0/oneOf/0/properties/never",
    "deprecated": false,
    "key": "never",
    "docstring": "A filter object to specify which tools are allowed.\n",
    "title": "MCP tool filter",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "read_only"
        },
        {
          "ident": "tool_names"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) never > (property) read_only",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) never > (property) tool_names"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 1 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "always"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 1 > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "never"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/AutoCodeInterpreterToolParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Always `auto`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/AutoCodeInterpreterToolParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        }
      ]
    },
    "default": "auto",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) file_ids": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/AutoCodeInterpreterToolParam/properties/file_ids",
    "deprecated": false,
    "key": "file_ids",
    "docstring": "An optional list of uploaded files to make available to your code.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/AutoCodeInterpreterToolParam/properties/file_ids",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/AutoCodeInterpreterToolParam/properties/memory_limit",
    "deprecated": false,
    "key": "memory_limit",
    "docstring": "The memory limit for the code interpreter container.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/AutoCodeInterpreterToolParam/properties/memory_limit",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "1g"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "4g"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "16g"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "64g"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit > (member) 3"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) network_policy": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/AutoCodeInterpreterToolParam/properties/network_policy",
    "deprecated": false,
    "key": "network_policy",
    "docstring": "Network access policy for the container.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/AutoCodeInterpreterToolParam/properties/network_policy",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "ContainerNetworkPolicyDisabled",
          "$ref": "(resource) responses > (model) container_network_policy_disabled > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ContainerNetworkPolicyAllowlist",
          "$ref": "(resource) responses > (model) container_network_policy_allowlist > (schema)"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) network_policy > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) network_policy > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-1"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-1-mini"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-1.5"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-2"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-2-2026-04-21"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-2.5-sunburst"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 6": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-2.5-sunburst-2026-09-08"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 7": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-2.5-flare"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 8": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-2.5-flare-2026-09-08"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "1024x1024"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1 > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "1024x1536"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1 > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "1536x1024"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1 > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) responses > (model) container_auto > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerAutoParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Automatically creates a container for this request",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ContainerAutoParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "container_auto"
        }
      ]
    },
    "default": "container_auto",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) container_auto > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) container_auto > (schema) > (property) file_ids": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerAutoParam/properties/file_ids",
    "deprecated": false,
    "key": "file_ids",
    "docstring": "An optional list of uploaded files to make available to your code.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/ContainerAutoParam/properties/file_ids",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) responses > (model) container_auto > (schema) > (property) memory_limit": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerAutoParam/properties/memory_limit",
    "deprecated": false,
    "key": "memory_limit",
    "docstring": "The memory limit for the container.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ContainerAutoParam/properties/memory_limit",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "1g"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "4g"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "16g"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "64g"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) container_auto > (schema) > (property) memory_limit > (member) 0",
      "(resource) responses > (model) container_auto > (schema) > (property) memory_limit > (member) 1",
      "(resource) responses > (model) container_auto > (schema) > (property) memory_limit > (member) 2",
      "(resource) responses > (model) container_auto > (schema) > (property) memory_limit > (member) 3"
    ]
  },
  "(resource) responses > (model) container_auto > (schema) > (property) network_policy": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerAutoParam/properties/network_policy",
    "deprecated": false,
    "key": "network_policy",
    "docstring": "Network access policy for the container.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ContainerAutoParam/properties/network_policy",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "ContainerNetworkPolicyDisabled",
          "$ref": "(resource) responses > (model) container_network_policy_disabled > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ContainerNetworkPolicyAllowlist",
          "$ref": "(resource) responses > (model) container_network_policy_allowlist > (schema)"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) container_auto > (schema) > (property) network_policy > (variant) 0",
      "(resource) responses > (model) container_auto > (schema) > (property) network_policy > (variant) 1"
    ]
  },
  "(resource) responses > (model) container_auto > (schema) > (property) skills": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerAutoParam/properties/skills",
    "deprecated": false,
    "key": "skills",
    "docstring": "An optional list of skills referenced by id or inline data.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/ContainerAutoParam/properties/skills",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/ContainerAutoParam/properties/skills/items",
        "types": [
          {
            "kind": "HttpTypeReference",
            "ident": "SkillReference",
            "$ref": "(resource) responses > (model) skill_reference > (schema)"
          },
          {
            "kind": "HttpTypeReference",
            "ident": "InlineSkill",
            "$ref": "(resource) responses > (model) inline_skill > (schema)"
          }
        ]
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) responses > (model) container_auto > (schema) > (property) skills > (items) > (variant) 0",
      "(resource) responses > (model) container_auto > (schema) > (property) skills > (items) > (variant) 1"
    ]
  },
  "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomTextFormatParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Unconstrained text format. Always `text`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CustomTextFormatParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "text"
        }
      ]
    },
    "default": "text",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 1 > (property) definition": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomGrammarFormatParam/properties/definition",
    "deprecated": false,
    "key": "definition",
    "docstring": "The grammar definition.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 1 > (property) syntax": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomGrammarFormatParam/properties/syntax",
    "deprecated": false,
    "key": "syntax",
    "docstring": "The syntax of the grammar definition. One of `lark` or `regex`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CustomGrammarFormatParam/properties/syntax",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "lark"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "regex"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 1 > (property) syntax > (member) 0",
      "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 1 > (property) syntax > (member) 1"
    ]
  },
  "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/CustomGrammarFormatParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Grammar format. Always `grammar`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/CustomGrammarFormatParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "grammar"
        }
      ]
    },
    "default": "grammar",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/name",
    "deprecated": false,
    "key": "name",
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/type",
    "deprecated": false,
    "key": "type",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionToolParam/properties/type",
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
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) allowed_callers": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/allowed_callers",
    "deprecated": false,
    "key": "allowed_callers",
    "docstring": "The tool invocation context(s).",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/FunctionToolParam/properties/allowed_callers",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/FunctionToolParam/properties/allowed_callers/anyOf/0/items",
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
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) allowed_callers > (items) > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) allowed_callers > (items) > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) async": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/async",
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) defer_loading": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/defer_loading",
    "deprecated": false,
    "key": "defer_loading",
    "docstring": "Whether this function should be deferred and discovered via tool search.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) description": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/description",
    "deprecated": false,
    "key": "description",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) output_schema": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/output_schema",
    "deprecated": false,
    "key": "output_schema",
    "docstring": "A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.",
    "type": {
      "kind": "HttpTypeReference",
      "oasRef": "#/components/schemas/FunctionToolParam/properties/output_schema",
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) parameters": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/parameters",
    "deprecated": false,
    "key": "parameters",
    "type": {
      "kind": "HttpTypeUnknown"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "unknown",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) strict": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/strict",
    "deprecated": false,
    "key": "strict",
    "docstring": "Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) name": {
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) type": {
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
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) allowed_callers": {
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
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) allowed_callers > (items) > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) allowed_callers > (items) > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) async": {
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) defer_loading": {
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) description": {
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) format": {
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "approximate"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) hybrid_search > (property) embedding_weight": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/HybridSearchOptions/properties/embedding_weight",
    "deprecated": false,
    "key": "embedding_weight",
    "docstring": "The weight of the embedding in the reciprocal ranking fusion.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) hybrid_search > (property) text_weight": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/HybridSearchOptions/properties/text_weight",
    "deprecated": false,
    "key": "text_weight",
    "docstring": "The weight of the text in the reciprocal ranking fusion.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) ranker > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 1 > (property) ranking_options > (property) ranker > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "default-2024-11-15"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 4 > (property) user_location > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "approximate"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) allowed_tools > (variant) 1 > (property) read_only": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolFilter/properties/read_only",
    "deprecated": false,
    "key": "read_only",
    "docstring": "Indicates whether or not a tool modifies data or is read-only. If an\nMCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),\nit will match this filter.\n",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) allowed_tools > (variant) 1 > (property) tool_names": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolFilter/properties/tool_names",
    "deprecated": false,
    "key": "tool_names",
    "docstring": "List of allowed tool names.",
    "title": "MCP allowed tools",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/MCPToolFilter/properties/tool_names",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) always": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/require_approval/anyOf/0/oneOf/0/properties/always",
    "deprecated": false,
    "key": "always",
    "docstring": "A filter object to specify which tools are allowed.\n",
    "title": "MCP tool filter",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "read_only"
        },
        {
          "ident": "tool_names"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) always > (property) read_only",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) always > (property) tool_names"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) never": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPTool/properties/require_approval/anyOf/0/oneOf/0/properties/never",
    "deprecated": false,
    "key": "never",
    "docstring": "A filter object to specify which tools are allowed.\n",
    "title": "MCP tool filter",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "read_only"
        },
        {
          "ident": "tool_names"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) never > (property) read_only",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) never > (property) tool_names"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 1 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "always"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 1 > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "never"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/AutoCodeInterpreterToolParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Always `auto`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/AutoCodeInterpreterToolParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "auto"
        }
      ]
    },
    "default": "auto",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) file_ids": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/AutoCodeInterpreterToolParam/properties/file_ids",
    "deprecated": false,
    "key": "file_ids",
    "docstring": "An optional list of uploaded files to make available to your code.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/AutoCodeInterpreterToolParam/properties/file_ids",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/AutoCodeInterpreterToolParam/properties/memory_limit",
    "deprecated": false,
    "key": "memory_limit",
    "docstring": "The memory limit for the code interpreter container.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/AutoCodeInterpreterToolParam/properties/memory_limit",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "1g"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "4g"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "16g"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "64g"
        }
      ]
    },
    "optional": true,
    "nullable": true,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit > (member) 1",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit > (member) 2",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit > (member) 3"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) network_policy": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/AutoCodeInterpreterToolParam/properties/network_policy",
    "deprecated": false,
    "key": "network_policy",
    "docstring": "Network access policy for the container.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/AutoCodeInterpreterToolParam/properties/network_policy",
      "types": [
        {
          "kind": "HttpTypeReference",
          "ident": "ContainerNetworkPolicyDisabled",
          "$ref": "(resource) responses > (model) container_network_policy_disabled > (schema)"
        },
        {
          "kind": "HttpTypeReference",
          "ident": "ContainerNetworkPolicyAllowlist",
          "$ref": "(resource) responses > (model) container_network_policy_allowlist > (schema)"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) network_policy > (variant) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) network_policy > (variant) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-1"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-1-mini"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-1.5"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-2"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-2-2026-04-21"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-2.5-sunburst"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 6": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-2.5-sunburst-2026-09-08"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 7": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-2.5-flare"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) model > (variant) 1 > (member) 8": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-image-2.5-flare-2026-09-08"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "1024x1024"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1 > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "1024x1536"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1 > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "1536x1024"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 8 > (property) size > (variant) 1 > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/name",
    "deprecated": false,
    "key": "name",
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/type",
    "deprecated": false,
    "key": "type",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/FunctionToolParam/properties/type",
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
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) allowed_callers": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/allowed_callers",
    "deprecated": false,
    "key": "allowed_callers",
    "docstring": "The tool invocation context(s).",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/FunctionToolParam/properties/allowed_callers",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/FunctionToolParam/properties/allowed_callers/anyOf/0/items",
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
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) allowed_callers > (items) > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) allowed_callers > (items) > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) async": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/async",
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) defer_loading": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/defer_loading",
    "deprecated": false,
    "key": "defer_loading",
    "docstring": "Whether this function should be deferred and discovered via tool search.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) description": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/description",
    "deprecated": false,
    "key": "description",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) output_schema": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/output_schema",
    "deprecated": false,
    "key": "output_schema",
    "docstring": "A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.",
    "type": {
      "kind": "HttpTypeReference",
      "oasRef": "#/components/schemas/FunctionToolParam/properties/output_schema",
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) parameters": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/parameters",
    "deprecated": false,
    "key": "parameters",
    "type": {
      "kind": "HttpTypeUnknown"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "unknown",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) strict": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/FunctionToolParam/properties/strict",
    "deprecated": false,
    "key": "strict",
    "docstring": "Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) name": {
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) type": {
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
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) allowed_callers": {
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
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) allowed_callers > (items) > (member) 0",
      "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) allowed_callers > (items) > (member) 1"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) async": {
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) defer_loading": {
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) description": {
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) format": {
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
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 14 > (property) user_location > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "approximate"
    }
  },
  "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) outcome > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "timeout"
    }
  },
  "(resource) responses > (model) response_function_shell_call_output_content > (schema) > (property) outcome > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "exit"
    }
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "file_citation"
    }
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "url_citation"
    }
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 2 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "container_file_citation"
    }
  },
  "(resource) responses > (model) response_output_text > (schema) > (property) annotations > (items) > (variant) 3 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "file_path"
    }
  },
  "(resource) $shared > (model) comparison_filter > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "eq"
    }
  },
  "(resource) $shared > (model) comparison_filter > (schema) > (property) type > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "ne"
    }
  },
  "(resource) $shared > (model) comparison_filter > (schema) > (property) type > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gt"
    }
  },
  "(resource) $shared > (model) comparison_filter > (schema) > (property) type > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gte"
    }
  },
  "(resource) $shared > (model) comparison_filter > (schema) > (property) type > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "lt"
    }
  },
  "(resource) $shared > (model) comparison_filter > (schema) > (property) type > (member) 5": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "lte"
    }
  },
  "(resource) $shared > (model) comparison_filter > (schema) > (property) type > (member) 6": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "in"
    }
  },
  "(resource) $shared > (model) comparison_filter > (schema) > (property) type > (member) 7": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "nin"
    }
  },
  "(resource) $shared > (model) comparison_filter > (schema) > (property) value > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComparisonFilter/properties/value/oneOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) $shared > (model) comparison_filter > (schema) > (property) value > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComparisonFilter/properties/value/oneOf/1",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "children": []
  },
  "(resource) $shared > (model) comparison_filter > (schema) > (property) value > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComparisonFilter/properties/value/oneOf/2",
    "ident": "UnionMember2",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "children": []
  },
  "(resource) $shared > (model) comparison_filter > (schema) > (property) value > (variant) 3": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComparisonFilter/properties/value/oneOf/3",
    "ident": "UnionMember3",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/ComparisonFilter/properties/value/oneOf/3",
      "elementType": {
        "kind": "HttpTypeUnion",
        "oasRef": "#/components/schemas/ComparisonFilter/properties/value/oneOf/3/items",
        "types": [
          {
            "kind": "HttpTypeString"
          },
          {
            "kind": "HttpTypeNumber"
          }
        ]
      }
    },
    "childrenParentSchema": "union",
    "children": [
      "(resource) $shared > (model) comparison_filter > (schema) > (property) value > (variant) 3 > (items) > (variant) 0",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) value > (variant) 3 > (items) > (variant) 1"
    ]
  },
  "(resource) $shared > (model) compound_filter > (schema) > (property) filters > (items) > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ComparisonFilter",
      "$ref": "(resource) $shared > (model) comparison_filter > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) $shared > (model) comparison_filter > (schema) > (property) key",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) type",
      "(resource) $shared > (model) comparison_filter > (schema) > (property) value"
    ]
  },
  "(resource) $shared > (model) compound_filter > (schema) > (property) filters > (items) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/CompoundFilter/properties/filters/items/oneOf/1",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeUnknown"
    },
    "children": []
  },
  "(resource) $shared > (model) compound_filter > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "and"
    }
  },
  "(resource) $shared > (model) compound_filter > (schema) > (property) type > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "or"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) always > (property) read_only": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolFilter/properties/read_only",
    "deprecated": false,
    "key": "read_only",
    "docstring": "Indicates whether or not a tool modifies data or is read-only. If an\nMCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),\nit will match this filter.\n",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) always > (property) tool_names": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolFilter/properties/tool_names",
    "deprecated": false,
    "key": "tool_names",
    "docstring": "List of allowed tool names.",
    "title": "MCP allowed tools",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/MCPToolFilter/properties/tool_names",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) never > (property) read_only": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolFilter/properties/read_only",
    "deprecated": false,
    "key": "read_only",
    "docstring": "Indicates whether or not a tool modifies data or is read-only. If an\nMCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),\nit will match this filter.\n",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) never > (property) tool_names": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolFilter/properties/tool_names",
    "deprecated": false,
    "key": "tool_names",
    "docstring": "List of allowed tool names.",
    "title": "MCP allowed tools",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/MCPToolFilter/properties/tool_names",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "1g"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "4g"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "16g"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "64g"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) network_policy > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ContainerNetworkPolicyDisabled",
      "$ref": "(resource) responses > (model) container_network_policy_disabled > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) container_network_policy_disabled > (schema) > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) network_policy > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ContainerNetworkPolicyAllowlist",
      "$ref": "(resource) responses > (model) container_network_policy_allowlist > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) container_network_policy_allowlist > (schema) > (property) allowed_domains",
      "(resource) responses > (model) container_network_policy_allowlist > (schema) > (property) type",
      "(resource) responses > (model) container_network_policy_allowlist > (schema) > (property) domain_secrets"
    ]
  },
  "(resource) responses > (model) container_network_policy_disabled > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ContainerNetworkPolicyDisabledParam",
    "ident": "ContainerNetworkPolicyDisabled",
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
      "(resource) responses > (model) container_network_policy_disabled > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) container_network_policy_allowlist > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ContainerNetworkPolicyAllowlistParam",
    "ident": "ContainerNetworkPolicyAllowlist",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "allowed_domains"
        },
        {
          "ident": "type"
        },
        {
          "ident": "domain_secrets"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) container_network_policy_allowlist > (schema) > (property) allowed_domains",
      "(resource) responses > (model) container_network_policy_allowlist > (schema) > (property) type",
      "(resource) responses > (model) container_network_policy_allowlist > (schema) > (property) domain_secrets"
    ]
  },
  "(resource) responses > (model) container_auto > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "container_auto"
    }
  },
  "(resource) responses > (model) container_auto > (schema) > (property) memory_limit > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "1g"
    }
  },
  "(resource) responses > (model) container_auto > (schema) > (property) memory_limit > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "4g"
    }
  },
  "(resource) responses > (model) container_auto > (schema) > (property) memory_limit > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "16g"
    }
  },
  "(resource) responses > (model) container_auto > (schema) > (property) memory_limit > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "64g"
    }
  },
  "(resource) responses > (model) container_auto > (schema) > (property) network_policy > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ContainerNetworkPolicyDisabled",
      "$ref": "(resource) responses > (model) container_network_policy_disabled > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) container_network_policy_disabled > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) container_auto > (schema) > (property) network_policy > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ContainerNetworkPolicyAllowlist",
      "$ref": "(resource) responses > (model) container_network_policy_allowlist > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) container_network_policy_allowlist > (schema) > (property) allowed_domains",
      "(resource) responses > (model) container_network_policy_allowlist > (schema) > (property) type",
      "(resource) responses > (model) container_network_policy_allowlist > (schema) > (property) domain_secrets"
    ]
  },
  "(resource) responses > (model) container_auto > (schema) > (property) skills > (items) > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "SkillReference",
      "$ref": "(resource) responses > (model) skill_reference > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) skill_reference > (schema) > (property) skill_id",
      "(resource) responses > (model) skill_reference > (schema) > (property) type",
      "(resource) responses > (model) skill_reference > (schema) > (property) version"
    ]
  },
  "(resource) responses > (model) container_auto > (schema) > (property) skills > (items) > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "InlineSkill",
      "$ref": "(resource) responses > (model) inline_skill > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) inline_skill > (schema) > (property) description",
      "(resource) responses > (model) inline_skill > (schema) > (property) name",
      "(resource) responses > (model) inline_skill > (schema) > (property) source",
      "(resource) responses > (model) inline_skill > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) skill_reference > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/SkillReferenceParam",
    "ident": "SkillReference",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "skill_id"
        },
        {
          "ident": "type"
        },
        {
          "ident": "version"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) skill_reference > (schema) > (property) skill_id",
      "(resource) responses > (model) skill_reference > (schema) > (property) type",
      "(resource) responses > (model) skill_reference > (schema) > (property) version"
    ]
  },
  "(resource) responses > (model) inline_skill > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/InlineSkillParam",
    "ident": "InlineSkill",
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
          "ident": "source"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) inline_skill > (schema) > (property) description",
      "(resource) responses > (model) inline_skill > (schema) > (property) name",
      "(resource) responses > (model) inline_skill > (schema) > (property) source",
      "(resource) responses > (model) inline_skill > (schema) > (property) type"
    ]
  },
  "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "text"
    }
  },
  "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 1 > (property) syntax > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "lark"
    }
  },
  "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 1 > (property) syntax > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "regex"
    }
  },
  "(resource) $shared > (model) custom_tool_input_format > (schema) > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "grammar"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) allowed_callers > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) allowed_callers > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "custom"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) allowed_callers > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 10 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) allowed_callers > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) always > (property) read_only": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolFilter/properties/read_only",
    "deprecated": false,
    "key": "read_only",
    "docstring": "Indicates whether or not a tool modifies data or is read-only. If an\nMCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),\nit will match this filter.\n",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) always > (property) tool_names": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolFilter/properties/tool_names",
    "deprecated": false,
    "key": "tool_names",
    "docstring": "List of allowed tool names.",
    "title": "MCP allowed tools",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/MCPToolFilter/properties/tool_names",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) never > (property) read_only": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolFilter/properties/read_only",
    "deprecated": false,
    "key": "read_only",
    "docstring": "Indicates whether or not a tool modifies data or is read-only. If an\nMCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),\nit will match this filter.\n",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 5 > (property) require_approval > (variant) 0 > (property) never > (property) tool_names": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/MCPToolFilter/properties/tool_names",
    "deprecated": false,
    "key": "tool_names",
    "docstring": "List of allowed tool names.",
    "title": "MCP allowed tools",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/MCPToolFilter/properties/tool_names",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "auto"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "1g"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "4g"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "16g"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) memory_limit > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "64g"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) network_policy > (variant) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ContainerNetworkPolicyDisabled",
      "$ref": "(resource) responses > (model) container_network_policy_disabled > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) container_network_policy_disabled > (schema) > (property) type"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 6 > (property) container > (variant) 1 > (property) network_policy > (variant) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ContainerNetworkPolicyAllowlist",
      "$ref": "(resource) responses > (model) container_network_policy_allowlist > (schema)"
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) container_network_policy_allowlist > (schema) > (property) allowed_domains",
      "(resource) responses > (model) container_network_policy_allowlist > (schema) > (property) type",
      "(resource) responses > (model) container_network_policy_allowlist > (schema) > (property) domain_secrets"
    ]
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "function"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) allowed_callers > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 0 > (property) allowed_callers > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "custom"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) allowed_callers > (items) > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "direct"
    }
  },
  "(resource) live > (model) response_item_create_event > (schema) > (property) item > (variant) 11 > (property) tools > (items) > (variant) 12 > (property) tools > (items) > (variant) 1 > (property) allowed_callers > (items) > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "programmatic"
    }
  },
  "(resource) $shared > (model) comparison_filter > (schema) > (property) value > (variant) 3 > (items) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComparisonFilter/properties/value/oneOf/3/items/oneOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) $shared > (model) comparison_filter > (schema) > (property) value > (variant) 3 > (items) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ComparisonFilter/properties/value/oneOf/3/items/oneOf/1",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "children": []
  },
  "(resource) responses > (model) container_network_policy_disabled > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerNetworkPolicyDisabledParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Disable outbound network access. Always `disabled`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ContainerNetworkPolicyDisabledParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "disabled"
        }
      ]
    },
    "default": "disabled",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) container_network_policy_disabled > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) container_network_policy_allowlist > (schema) > (property) allowed_domains": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerNetworkPolicyAllowlistParam/properties/allowed_domains",
    "deprecated": false,
    "key": "allowed_domains",
    "docstring": "A list of allowed domains when type is `allowlist`.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/ContainerNetworkPolicyAllowlistParam/properties/allowed_domains",
      "elementType": {
        "kind": "HttpTypeString"
      }
    },
    "optional": false,
    "nullable": false,
    "schemaType": "array",
    "children": []
  },
  "(resource) responses > (model) container_network_policy_allowlist > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerNetworkPolicyAllowlistParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Allow outbound network access only to specified domains. Always `allowlist`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ContainerNetworkPolicyAllowlistParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "allowlist"
        }
      ]
    },
    "default": "allowlist",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) container_network_policy_allowlist > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) container_network_policy_allowlist > (schema) > (property) domain_secrets": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerNetworkPolicyAllowlistParam/properties/domain_secrets",
    "deprecated": false,
    "key": "domain_secrets",
    "docstring": "Optional domain-scoped secrets for allowlisted domains.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/ContainerNetworkPolicyAllowlistParam/properties/domain_secrets",
      "elementType": {
        "kind": "HttpTypeReference",
        "ident": "ContainerNetworkPolicyDomainSecret",
        "$ref": "(resource) responses > (model) container_network_policy_domain_secret > (schema)"
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) container_network_policy_domain_secret > (schema) > (property) domain",
      "(resource) responses > (model) container_network_policy_domain_secret > (schema) > (property) name",
      "(resource) responses > (model) container_network_policy_domain_secret > (schema) > (property) value"
    ]
  },
  "(resource) responses > (model) skill_reference > (schema) > (property) skill_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/SkillReferenceParam/properties/skill_id",
    "deprecated": false,
    "key": "skill_id",
    "docstring": "The ID of the referenced skill.",
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
  "(resource) responses > (model) skill_reference > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/SkillReferenceParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "References a skill created with the /v1/skills endpoint.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/SkillReferenceParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "skill_reference"
        }
      ]
    },
    "default": "skill_reference",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) skill_reference > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) skill_reference > (schema) > (property) version": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/SkillReferenceParam/properties/version",
    "deprecated": false,
    "key": "version",
    "docstring": "Optional skill version. Use a positive integer or 'latest'. Omit for default.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) inline_skill > (schema) > (property) description": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InlineSkillParam/properties/description",
    "deprecated": false,
    "key": "description",
    "docstring": "The description of the skill.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) inline_skill > (schema) > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InlineSkillParam/properties/name",
    "deprecated": false,
    "key": "name",
    "docstring": "The name of the skill.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) inline_skill > (schema) > (property) source": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InlineSkillParam/properties/source",
    "deprecated": false,
    "key": "source",
    "docstring": "Inline skill payload",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "InlineSkillSource",
      "$ref": "(resource) responses > (model) inline_skill_source > (schema)"
    },
    "optional": false,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "object",
    "modelPath": "(resource) responses > (model) inline_skill_source",
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) inline_skill_source > (schema) > (property) data",
      "(resource) responses > (model) inline_skill_source > (schema) > (property) media_type",
      "(resource) responses > (model) inline_skill_source > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) inline_skill > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InlineSkillParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "Defines an inline skill for this request.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/InlineSkillParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "inline"
        }
      ]
    },
    "default": "inline",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) inline_skill > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) container_network_policy_disabled > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "disabled"
    }
  },
  "(resource) responses > (model) container_network_policy_allowlist > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "allowlist"
    }
  },
  "(resource) responses > (model) container_network_policy_domain_secret > (schema) > (property) domain": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerNetworkPolicyDomainSecretParam/properties/domain",
    "deprecated": false,
    "key": "domain",
    "docstring": "The domain associated with the secret.",
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
  "(resource) responses > (model) container_network_policy_domain_secret > (schema) > (property) name": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerNetworkPolicyDomainSecretParam/properties/name",
    "deprecated": false,
    "key": "name",
    "docstring": "The name of the secret to inject for the domain.",
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
  "(resource) responses > (model) container_network_policy_domain_secret > (schema) > (property) value": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/ContainerNetworkPolicyDomainSecretParam/properties/value",
    "deprecated": false,
    "key": "value",
    "docstring": "The secret value to inject for the domain.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 10485760
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) container_network_policy_domain_secret > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ContainerNetworkPolicyDomainSecretParam",
    "ident": "ContainerNetworkPolicyDomainSecret",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "domain"
        },
        {
          "ident": "name"
        },
        {
          "ident": "value"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) container_network_policy_domain_secret > (schema) > (property) domain",
      "(resource) responses > (model) container_network_policy_domain_secret > (schema) > (property) name",
      "(resource) responses > (model) container_network_policy_domain_secret > (schema) > (property) value"
    ]
  },
  "(resource) responses > (model) skill_reference > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "skill_reference"
    }
  },
  "(resource) responses > (model) inline_skill_source > (schema) > (property) data": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InlineSkillSourceParam/properties/data",
    "deprecated": false,
    "key": "data",
    "docstring": "Base64-encoded skill zip bundle.",
    "type": {
      "kind": "HttpTypeString"
    },
    "constraints": {
      "minLength": 1,
      "maxLength": 70254592
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) responses > (model) inline_skill_source > (schema) > (property) media_type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InlineSkillSourceParam/properties/media_type",
    "deprecated": false,
    "key": "media_type",
    "docstring": "The media type of the inline skill payload. Must be `application/zip`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/InlineSkillSourceParam/properties/media_type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "application/zip"
        }
      ]
    },
    "default": "application/zip",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) inline_skill_source > (schema) > (property) media_type > (member) 0"
    ]
  },
  "(resource) responses > (model) inline_skill_source > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/InlineSkillSourceParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The type of the inline skill source. Must be `base64`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/InlineSkillSourceParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "base64"
        }
      ]
    },
    "default": "base64",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) responses > (model) inline_skill_source > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) responses > (model) inline_skill_source > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/InlineSkillSourceParam",
    "docstring": "Inline skill payload",
    "ident": "InlineSkillSource",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "data"
        },
        {
          "ident": "media_type"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) responses > (model) inline_skill_source > (schema) > (property) data",
      "(resource) responses > (model) inline_skill_source > (schema) > (property) media_type",
      "(resource) responses > (model) inline_skill_source > (schema) > (property) type"
    ]
  },
  "(resource) responses > (model) inline_skill > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "inline"
    }
  },
  "(resource) responses > (model) inline_skill_source > (schema) > (property) media_type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "application/zip"
    }
  },
  "(resource) responses > (model) inline_skill_source > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "base64"
    }
  }
}
```

#### Example

```json
{
  "type": "response.item.create",
  "event_id": "evt_item_001",
  "item": {
    "type": "message",
    "role": "user",
    "content": [
      {
        "type": "input_text",
        "text": "Please check for a table for two at 7 PM."
      }
    ]
  }
}
```

### response.create

Request a response from the Live session’s Responses backend, or continue a delegated response waiting for tool results. Requires Responses delegation.

#### Schema

Schema name: `LiveResponseCreateParam`

```json
{
  "(resource) live > (model) response_create_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponseCreateParam",
    "docstring": "Request a response from the Live session’s Responses backend, or continue a delegated response waiting for tool results. Requires Responses delegation.",
    "ident": "ResponseCreateEvent",
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
      "(resource) live > (model) response_create_event > (schema) > (property) type",
      "(resource) live > (model) response_create_event > (schema) > (property) event_id"
    ]
  },
  "(resource) live > (model) response_create_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponseCreateParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The Live client event type. Always `response.create`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveResponseCreateParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "response.create"
        }
      ]
    },
    "default": "response.create",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_create_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_create_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponseCreateParam/properties/event_id",
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
  "(resource) live > (model) response_create_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "response.create"
    }
  }
}
```

#### Example

```json
{
  "type": "response.create",
  "event_id": "evt_response_001"
}
```

### session.close

Request that the Live session close. The terminal `session.closed` event contains the close reason and final usage.

#### Schema

Schema name: `LiveSessionCloseParam`

```json
{
  "(resource) live > (model) session_close_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveSessionCloseParam",
    "docstring": "Request that the Live session close. The terminal `session.closed` event contains the close reason and final usage.",
    "ident": "SessionCloseEvent",
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
      "(resource) live > (model) session_close_event > (schema) > (property) type",
      "(resource) live > (model) session_close_event > (schema) > (property) event_id"
    ]
  },
  "(resource) live > (model) session_close_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionCloseParam/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The Live client event type. Always `session.close`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionCloseParam/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.close"
        }
      ]
    },
    "default": "session.close",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) session_close_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) session_close_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionCloseParam/properties/event_id",
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
  "(resource) live > (model) session_close_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.close"
    }
  }
}
```

#### Example

```json
{
  "type": "session.close",
  "event_id": "evt_close_001"
}
```

## Server events

### session.started

Returned when a Live session has started. Contains the resolved session configuration, including server defaults.

#### Schema

Schema name: `LiveSessionStarted`

```json
{
  "(resource) live > (model) session_started_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveSessionStarted",
    "docstring": "Returned when a Live session has started. Contains the resolved session configuration, including server defaults.",
    "ident": "SessionStartedEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "event_id"
        },
        {
          "ident": "session"
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
      "(resource) live > (model) session_started_event > (schema) > (property) event_id",
      "(resource) live > (model) session_started_event > (schema) > (property) session",
      "(resource) live > (model) session_started_event > (schema) > (property) type",
      "(resource) live > (model) session_started_event > (schema) > (property) client_event_id"
    ]
  },
  "(resource) live > (model) session_started_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionStarted/properties/event_id",
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
  "(resource) live > (model) session_started_event > (schema) > (property) session": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionStarted/properties/session",
    "deprecated": false,
    "key": "session",
    "docstring": "The resolved Live session configuration and server-assigned session metadata.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "SessionResource",
      "$ref": "(resource) live > (model) session_resource > (schema)"
    },
    "optional": false,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "object",
    "modelPath": "(resource) live > (model) session_resource",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) id",
      "(resource) live > (model) session_resource > (schema) > (property) expires_at",
      "(resource) live > (model) session_resource > (schema) > (property) model",
      "(resource) live > (model) session_resource > (schema) > (property) status",
      "(resource) live > (model) session_resource > (schema) > (property) audio",
      "(resource) live > (model) session_resource > (schema) > (property) client",
      "(resource) live > (model) session_resource > (schema) > (property) delegation",
      "(resource) live > (model) session_resource > (schema) > (property) input",
      "(resource) live > (model) session_resource > (schema) > (property) instructions",
      "(resource) live > (model) session_resource > (schema) > (property) store"
    ]
  },
  "(resource) live > (model) session_started_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionStarted/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The event type, always `session.started`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionStarted/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.started"
        }
      ]
    },
    "default": "session.started",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) session_started_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) session_started_event > (schema) > (property) client_event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionStarted/properties/client_event_id",
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
  "(resource) live > (model) session_resource > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the Live session. Use this ID for sideband connections, forking, and recording download.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) session_resource > (schema) > (property) expires_at": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/expires_at",
    "deprecated": false,
    "key": "expires_at",
    "docstring": "The Unix timestamp, in seconds, at which the Live session expires.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) session_resource > (schema) > (property) model": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/model",
    "deprecated": false,
    "key": "model",
    "docstring": "The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/model",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnion",
          "oasRef": "#/components/schemas/ModelIdsLive/anyOf/1",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-live-1"
            }
          ]
        }
      ]
    },
    "examples": [
      "gpt-live-1"
    ],
    "optional": false,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 0",
      "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 1"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the session snapshot. Always `active`, including the final snapshot in session.closed; use the event type to determine that the session has closed.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "active"
        }
      ]
    },
    "default": "active",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) status > (member) 0"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/audio",
    "deprecated": false,
    "key": "audio",
    "docstring": "Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "format"
        },
        {
          "ident": "output"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) format",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) client": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/client",
    "deprecated": false,
    "key": "client",
    "docstring": "Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.",
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
  "(resource) live > (model) session_resource > (schema) > (property) delegation": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/delegation",
    "deprecated": false,
    "key": "delegation",
    "docstring": "Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/delegation",
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
              "ident": "responses"
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
      "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 0",
      "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) input": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/input",
    "deprecated": false,
    "key": "input",
    "docstring": "Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/input",
      "elementType": {
        "kind": "HttpTypeReference",
        "ident": "InitialItem",
        "$ref": "(resource) live > (model) initial_item > (schema)"
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 0",
      "(resource) live > (model) initial_item > (schema) > (variant) 1",
      "(resource) live > (model) initial_item > (schema) > (variant) 2"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) instructions": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/instructions",
    "deprecated": false,
    "key": "instructions",
    "docstring": "Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) session_resource > (schema) > (property) store": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/store",
    "deprecated": false,
    "key": "store",
    "docstring": "Whether to store the session for later forking and recording download. Defaults to false for new sessions.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) session_resource > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveSessionResourceParam",
    "docstring": "The resolved Live session configuration and server-assigned session metadata.",
    "ident": "SessionResource",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "expires_at"
        },
        {
          "ident": "model"
        },
        {
          "ident": "status"
        },
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
          "ident": "input"
        },
        {
          "ident": "instructions"
        },
        {
          "ident": "store"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) id",
      "(resource) live > (model) session_resource > (schema) > (property) expires_at",
      "(resource) live > (model) session_resource > (schema) > (property) model",
      "(resource) live > (model) session_resource > (schema) > (property) status",
      "(resource) live > (model) session_resource > (schema) > (property) audio",
      "(resource) live > (model) session_resource > (schema) > (property) client",
      "(resource) live > (model) session_resource > (schema) > (property) delegation",
      "(resource) live > (model) session_resource > (schema) > (property) input",
      "(resource) live > (model) session_resource > (schema) > (property) instructions",
      "(resource) live > (model) session_resource > (schema) > (property) store"
    ]
  },
  "(resource) live > (model) session_started_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.started"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ModelIdsLive/anyOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ModelIdsLive/anyOf/1",
    "docstring": "The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ModelIdsLive/anyOf/1",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-live-1"
        }
      ]
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 1 > (member) 0"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "active"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) format": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialSessionAudioParam/properties/format",
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
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialSessionAudioParam/properties/output",
    "deprecated": false,
    "key": "output",
    "docstring": "The voice used for speech generated by the Live model.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "voice"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice"
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
  "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 0": {
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
  "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/delegation/anyOf/0/oneOf/1",
    "docstring": "Delegate tasks to a Responses model managed by the Live session.",
    "ident": "Responses",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "responses"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1 > (property) responses",
      "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1 > (property) type"
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
  "(resource) live > (model) initial_item > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInitialItem/oneOf/0",
    "docstring": "A developer message included in the initial text history of a Live session.",
    "ident": "Developer",
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
          "ident": "id"
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
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) content",
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) role",
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) id",
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) status",
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) type"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInitialItem/oneOf/1",
    "docstring": "A user message included in the initial text history of a Live session.",
    "ident": "User",
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
          "ident": "id"
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
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) content",
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) role",
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) id",
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) status",
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInitialItem/oneOf/2",
    "docstring": "An assistant message included in the initial text history of a Live session.",
    "ident": "Assistant",
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
          "ident": "id"
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
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content",
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) role",
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) id",
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) status",
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) type"
    ]
  },
  "(resource) live > (model) initial_item > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInitialItem",
    "docstring": "A developer, user, or assistant message supplied as text history before the Live session starts.",
    "ident": "InitialItem",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialItem",
      "types": [
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
              "ident": "id"
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
              "ident": "content"
            },
            {
              "ident": "role"
            },
            {
              "ident": "id"
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
              "ident": "content"
            },
            {
              "ident": "role"
            },
            {
              "ident": "id"
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
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 0",
      "(resource) live > (model) initial_item > (schema) > (variant) 1",
      "(resource) live > (model) initial_item > (schema) > (variant) 2"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 1 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-live-1"
    }
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
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialSessionAudioOutputParam/properties/voice",
    "deprecated": false,
    "key": "voice",
    "docstring": "The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialSessionAudioOutputParam/properties/voice",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
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
        {
          "kind": "HttpTypeReference",
          "ident": "CustomVoice",
          "$ref": "(resource) live > (model) custom_voice > (schema)"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 0",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 2"
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
  "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1 > (property) responses": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationParam/properties/responses",
    "deprecated": false,
    "key": "responses",
    "docstring": "Backend model, prompt, and tools used when the Live session delegates a task to Responses.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponsesDelegationConfig",
      "$ref": "(resource) live > (model) responses_delegation_config > (schema)"
    },
    "optional": false,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "object",
    "modelPath": "(resource) live > (model) responses_delegation_config",
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
  "type": "session.started",
  "event_id": "evt_started_001",
  "client_event_id": "evt_start_001",
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
  }
}
```

### session.updated

Returned when a Live session update is accepted. Contains the resolved session configuration after the update.

#### Schema

Schema name: `LiveSessionUpdated`

```json
{
  "(resource) live > (model) session_updated_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveSessionUpdated",
    "docstring": "Returned when a Live session update is accepted. Contains the resolved session configuration after the update.",
    "ident": "SessionUpdatedEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "event_id"
        },
        {
          "ident": "session"
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
      "(resource) live > (model) session_updated_event > (schema) > (property) event_id",
      "(resource) live > (model) session_updated_event > (schema) > (property) session",
      "(resource) live > (model) session_updated_event > (schema) > (property) type",
      "(resource) live > (model) session_updated_event > (schema) > (property) client_event_id"
    ]
  },
  "(resource) live > (model) session_updated_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionUpdated/properties/event_id",
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
  "(resource) live > (model) session_updated_event > (schema) > (property) session": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionUpdated/properties/session",
    "deprecated": false,
    "key": "session",
    "docstring": "The resolved Live session configuration and server-assigned session metadata.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "SessionResource",
      "$ref": "(resource) live > (model) session_resource > (schema)"
    },
    "optional": false,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "object",
    "modelPath": "(resource) live > (model) session_resource",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) id",
      "(resource) live > (model) session_resource > (schema) > (property) expires_at",
      "(resource) live > (model) session_resource > (schema) > (property) model",
      "(resource) live > (model) session_resource > (schema) > (property) status",
      "(resource) live > (model) session_resource > (schema) > (property) audio",
      "(resource) live > (model) session_resource > (schema) > (property) client",
      "(resource) live > (model) session_resource > (schema) > (property) delegation",
      "(resource) live > (model) session_resource > (schema) > (property) input",
      "(resource) live > (model) session_resource > (schema) > (property) instructions",
      "(resource) live > (model) session_resource > (schema) > (property) store"
    ]
  },
  "(resource) live > (model) session_updated_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionUpdated/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The event type, always `session.updated`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionUpdated/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.updated"
        }
      ]
    },
    "default": "session.updated",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) session_updated_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) session_updated_event > (schema) > (property) client_event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionUpdated/properties/client_event_id",
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
  "(resource) live > (model) session_resource > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the Live session. Use this ID for sideband connections, forking, and recording download.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) session_resource > (schema) > (property) expires_at": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/expires_at",
    "deprecated": false,
    "key": "expires_at",
    "docstring": "The Unix timestamp, in seconds, at which the Live session expires.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) session_resource > (schema) > (property) model": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/model",
    "deprecated": false,
    "key": "model",
    "docstring": "The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/model",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnion",
          "oasRef": "#/components/schemas/ModelIdsLive/anyOf/1",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-live-1"
            }
          ]
        }
      ]
    },
    "examples": [
      "gpt-live-1"
    ],
    "optional": false,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 0",
      "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 1"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the session snapshot. Always `active`, including the final snapshot in session.closed; use the event type to determine that the session has closed.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "active"
        }
      ]
    },
    "default": "active",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) status > (member) 0"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/audio",
    "deprecated": false,
    "key": "audio",
    "docstring": "Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "format"
        },
        {
          "ident": "output"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) format",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) client": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/client",
    "deprecated": false,
    "key": "client",
    "docstring": "Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.",
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
  "(resource) live > (model) session_resource > (schema) > (property) delegation": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/delegation",
    "deprecated": false,
    "key": "delegation",
    "docstring": "Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/delegation",
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
              "ident": "responses"
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
      "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 0",
      "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) input": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/input",
    "deprecated": false,
    "key": "input",
    "docstring": "Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/input",
      "elementType": {
        "kind": "HttpTypeReference",
        "ident": "InitialItem",
        "$ref": "(resource) live > (model) initial_item > (schema)"
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 0",
      "(resource) live > (model) initial_item > (schema) > (variant) 1",
      "(resource) live > (model) initial_item > (schema) > (variant) 2"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) instructions": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/instructions",
    "deprecated": false,
    "key": "instructions",
    "docstring": "Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) session_resource > (schema) > (property) store": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/store",
    "deprecated": false,
    "key": "store",
    "docstring": "Whether to store the session for later forking and recording download. Defaults to false for new sessions.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) session_resource > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveSessionResourceParam",
    "docstring": "The resolved Live session configuration and server-assigned session metadata.",
    "ident": "SessionResource",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "expires_at"
        },
        {
          "ident": "model"
        },
        {
          "ident": "status"
        },
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
          "ident": "input"
        },
        {
          "ident": "instructions"
        },
        {
          "ident": "store"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) id",
      "(resource) live > (model) session_resource > (schema) > (property) expires_at",
      "(resource) live > (model) session_resource > (schema) > (property) model",
      "(resource) live > (model) session_resource > (schema) > (property) status",
      "(resource) live > (model) session_resource > (schema) > (property) audio",
      "(resource) live > (model) session_resource > (schema) > (property) client",
      "(resource) live > (model) session_resource > (schema) > (property) delegation",
      "(resource) live > (model) session_resource > (schema) > (property) input",
      "(resource) live > (model) session_resource > (schema) > (property) instructions",
      "(resource) live > (model) session_resource > (schema) > (property) store"
    ]
  },
  "(resource) live > (model) session_updated_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.updated"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ModelIdsLive/anyOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ModelIdsLive/anyOf/1",
    "docstring": "The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ModelIdsLive/anyOf/1",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-live-1"
        }
      ]
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 1 > (member) 0"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "active"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) format": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialSessionAudioParam/properties/format",
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
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialSessionAudioParam/properties/output",
    "deprecated": false,
    "key": "output",
    "docstring": "The voice used for speech generated by the Live model.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "voice"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice"
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
  "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 0": {
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
  "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/delegation/anyOf/0/oneOf/1",
    "docstring": "Delegate tasks to a Responses model managed by the Live session.",
    "ident": "Responses",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "responses"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1 > (property) responses",
      "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1 > (property) type"
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
  "(resource) live > (model) initial_item > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInitialItem/oneOf/0",
    "docstring": "A developer message included in the initial text history of a Live session.",
    "ident": "Developer",
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
          "ident": "id"
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
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) content",
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) role",
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) id",
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) status",
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) type"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInitialItem/oneOf/1",
    "docstring": "A user message included in the initial text history of a Live session.",
    "ident": "User",
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
          "ident": "id"
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
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) content",
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) role",
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) id",
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) status",
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInitialItem/oneOf/2",
    "docstring": "An assistant message included in the initial text history of a Live session.",
    "ident": "Assistant",
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
          "ident": "id"
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
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content",
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) role",
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) id",
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) status",
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) type"
    ]
  },
  "(resource) live > (model) initial_item > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInitialItem",
    "docstring": "A developer, user, or assistant message supplied as text history before the Live session starts.",
    "ident": "InitialItem",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialItem",
      "types": [
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
              "ident": "id"
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
              "ident": "content"
            },
            {
              "ident": "role"
            },
            {
              "ident": "id"
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
              "ident": "content"
            },
            {
              "ident": "role"
            },
            {
              "ident": "id"
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
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 0",
      "(resource) live > (model) initial_item > (schema) > (variant) 1",
      "(resource) live > (model) initial_item > (schema) > (variant) 2"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 1 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-live-1"
    }
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
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialSessionAudioOutputParam/properties/voice",
    "deprecated": false,
    "key": "voice",
    "docstring": "The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialSessionAudioOutputParam/properties/voice",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
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
        {
          "kind": "HttpTypeReference",
          "ident": "CustomVoice",
          "$ref": "(resource) live > (model) custom_voice > (schema)"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 0",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 2"
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
  "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1 > (property) responses": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationParam/properties/responses",
    "deprecated": false,
    "key": "responses",
    "docstring": "Backend model, prompt, and tools used when the Live session delegates a task to Responses.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponsesDelegationConfig",
      "$ref": "(resource) live > (model) responses_delegation_config > (schema)"
    },
    "optional": false,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "object",
    "modelPath": "(resource) live > (model) responses_delegation_config",
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
  "type": "session.updated",
  "event_id": "evt_updated_001",
  "client_event_id": "evt_update_001",
  "session": {
    "id": "live_def456",
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
      "type": "responses",
      "responses": {
        "model": "gpt-6-astra",
        "instructions": "Check restaurant availability. Ask before confirming a booking.",
        "max_output_tokens": 1024,
        "tools": []
      }
    }
  }
}
```

### session.input_audio.muted

Returned when a session.input_audio.mute command is accepted. Input audio is no longer sent to the model; sideband audio reflection continues.

#### Schema

Schema name: `LiveInputAudioMuted`

```json
{
  "(resource) live > (model) input_audio_muted_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInputAudioMuted",
    "docstring": "Returned when a session.input_audio.mute command is accepted. Input audio is no longer sent to the model; sideband audio reflection continues.",
    "ident": "InputAudioMutedEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
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
      "(resource) live > (model) input_audio_muted_event > (schema) > (property) event_id",
      "(resource) live > (model) input_audio_muted_event > (schema) > (property) type",
      "(resource) live > (model) input_audio_muted_event > (schema) > (property) client_event_id"
    ]
  },
  "(resource) live > (model) input_audio_muted_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputAudioMuted/properties/event_id",
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
  "(resource) live > (model) input_audio_muted_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputAudioMuted/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The event type, always `session.input_audio.muted`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInputAudioMuted/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.input_audio.muted"
        }
      ]
    },
    "default": "session.input_audio.muted",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) input_audio_muted_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) input_audio_muted_event > (schema) > (property) client_event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputAudioMuted/properties/client_event_id",
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
  "(resource) live > (model) input_audio_muted_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.input_audio.muted"
    }
  }
}
```

#### Example

```json
{
  "type": "session.input_audio.muted",
  "event_id": "evt_muted_001",
  "client_event_id": "evt_mute_001"
}
```

### session.input_audio.unmuted

Returned when a session.input_audio.unmute command is accepted. Input audio is sent to the model again.

#### Schema

Schema name: `LiveInputAudioUnmuted`

```json
{
  "(resource) live > (model) input_audio_unmuted_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInputAudioUnmuted",
    "docstring": "Returned when a session.input_audio.unmute command is accepted. Input audio is sent to the model again.",
    "ident": "InputAudioUnmutedEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
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
      "(resource) live > (model) input_audio_unmuted_event > (schema) > (property) event_id",
      "(resource) live > (model) input_audio_unmuted_event > (schema) > (property) type",
      "(resource) live > (model) input_audio_unmuted_event > (schema) > (property) client_event_id"
    ]
  },
  "(resource) live > (model) input_audio_unmuted_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputAudioUnmuted/properties/event_id",
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
  "(resource) live > (model) input_audio_unmuted_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputAudioUnmuted/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The event type, always `session.input_audio.unmuted`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInputAudioUnmuted/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.input_audio.unmuted"
        }
      ]
    },
    "default": "session.input_audio.unmuted",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) input_audio_unmuted_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) input_audio_unmuted_event > (schema) > (property) client_event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputAudioUnmuted/properties/client_event_id",
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
  "(resource) live > (model) input_audio_unmuted_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.input_audio.unmuted"
    }
  }
}
```

#### Example

```json
{
  "type": "session.input_audio.unmuted",
  "event_id": "evt_unmuted_001",
  "client_event_id": "evt_unmute_001"
}
```

### session.instructions.appended

Returned when a session.instructions.append command is accepted into the Live session timeline. Acknowledges the appended instructions without guaranteeing that the model has acted on them.

#### Schema

Schema name: `LiveInstructionsAppended`

```json
{
  "(resource) live > (model) instructions_appended_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInstructionsAppended",
    "docstring": "Returned when a session.instructions.append command is accepted into the Live session timeline. Acknowledges the appended instructions without guaranteeing that the model has acted on them.",
    "ident": "InstructionsAppendedEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "end_ms"
        },
        {
          "ident": "event_id"
        },
        {
          "ident": "start_ms"
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
      "(resource) live > (model) instructions_appended_event > (schema) > (property) end_ms",
      "(resource) live > (model) instructions_appended_event > (schema) > (property) event_id",
      "(resource) live > (model) instructions_appended_event > (schema) > (property) start_ms",
      "(resource) live > (model) instructions_appended_event > (schema) > (property) type",
      "(resource) live > (model) instructions_appended_event > (schema) > (property) client_event_id"
    ]
  },
  "(resource) live > (model) instructions_appended_event > (schema) > (property) end_ms": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInstructionsAppended/properties/end_ms",
    "deprecated": false,
    "key": "end_ms",
    "docstring": "The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) instructions_appended_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInstructionsAppended/properties/event_id",
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
  "(resource) live > (model) instructions_appended_event > (schema) > (property) start_ms": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInstructionsAppended/properties/start_ms",
    "deprecated": false,
    "key": "start_ms",
    "docstring": "The start of this event on the Live session timeline, in milliseconds from the beginning of the session.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) instructions_appended_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInstructionsAppended/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The event type, always `session.instructions.appended`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInstructionsAppended/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.instructions.appended"
        }
      ]
    },
    "default": "session.instructions.appended",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) instructions_appended_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) instructions_appended_event > (schema) > (property) client_event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInstructionsAppended/properties/client_event_id",
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
  "(resource) live > (model) instructions_appended_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.instructions.appended"
    }
  }
}
```

#### Example

```json
{
  "type": "session.instructions.appended",
  "event_id": "evt_instructions_002",
  "client_event_id": "evt_instructions_001",
  "start_ms": 1200,
  "end_ms": 1400
}
```

### session.thinking.appended

Returned when a session.thinking.append command is accepted into the Live session timeline. Acknowledges the added reasoning context without guaranteeing any spoken output.

#### Schema

Schema name: `LiveThinkingAppended`

```json
{
  "(resource) live > (model) thinking_appended_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveThinkingAppended",
    "docstring": "Returned when a session.thinking.append command is accepted into the Live session timeline. Acknowledges the added reasoning context without guaranteeing any spoken output.",
    "ident": "ThinkingAppendedEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "end_ms"
        },
        {
          "ident": "event_id"
        },
        {
          "ident": "start_ms"
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
      "(resource) live > (model) thinking_appended_event > (schema) > (property) end_ms",
      "(resource) live > (model) thinking_appended_event > (schema) > (property) event_id",
      "(resource) live > (model) thinking_appended_event > (schema) > (property) start_ms",
      "(resource) live > (model) thinking_appended_event > (schema) > (property) type",
      "(resource) live > (model) thinking_appended_event > (schema) > (property) client_event_id"
    ]
  },
  "(resource) live > (model) thinking_appended_event > (schema) > (property) end_ms": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveThinkingAppended/properties/end_ms",
    "deprecated": false,
    "key": "end_ms",
    "docstring": "The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) thinking_appended_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveThinkingAppended/properties/event_id",
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
  "(resource) live > (model) thinking_appended_event > (schema) > (property) start_ms": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveThinkingAppended/properties/start_ms",
    "deprecated": false,
    "key": "start_ms",
    "docstring": "The start of this event on the Live session timeline, in milliseconds from the beginning of the session.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) thinking_appended_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveThinkingAppended/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The event type, always `session.thinking.appended`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveThinkingAppended/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.thinking.appended"
        }
      ]
    },
    "default": "session.thinking.appended",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) thinking_appended_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) thinking_appended_event > (schema) > (property) client_event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveThinkingAppended/properties/client_event_id",
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
  "(resource) live > (model) thinking_appended_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.thinking.appended"
    }
  }
}
```

#### Example

```json
{
  "type": "session.thinking.appended",
  "event_id": "evt_thinking_002",
  "client_event_id": "evt_thinking_001",
  "start_ms": 4600,
  "end_ms": 4800
}
```

### session.commentary.appended

Returned when a session.commentary.append command is accepted into the Live session timeline. Acknowledges the added commentary without guaranteeing exact wording or completed audio playback.

#### Schema

Schema name: `LiveCommentaryAppended`

```json
{
  "(resource) live > (model) commentary_appended_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveCommentaryAppended",
    "docstring": "Returned when a session.commentary.append command is accepted into the Live session timeline. Acknowledges the added commentary without guaranteeing exact wording or completed audio playback.",
    "ident": "CommentaryAppendedEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "end_ms"
        },
        {
          "ident": "event_id"
        },
        {
          "ident": "start_ms"
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
      "(resource) live > (model) commentary_appended_event > (schema) > (property) end_ms",
      "(resource) live > (model) commentary_appended_event > (schema) > (property) event_id",
      "(resource) live > (model) commentary_appended_event > (schema) > (property) start_ms",
      "(resource) live > (model) commentary_appended_event > (schema) > (property) type",
      "(resource) live > (model) commentary_appended_event > (schema) > (property) client_event_id"
    ]
  },
  "(resource) live > (model) commentary_appended_event > (schema) > (property) end_ms": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveCommentaryAppended/properties/end_ms",
    "deprecated": false,
    "key": "end_ms",
    "docstring": "The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) commentary_appended_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveCommentaryAppended/properties/event_id",
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
  "(resource) live > (model) commentary_appended_event > (schema) > (property) start_ms": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveCommentaryAppended/properties/start_ms",
    "deprecated": false,
    "key": "start_ms",
    "docstring": "The start of this event on the Live session timeline, in milliseconds from the beginning of the session.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) commentary_appended_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveCommentaryAppended/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The event type, always `session.commentary.appended`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveCommentaryAppended/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.commentary.appended"
        }
      ]
    },
    "default": "session.commentary.appended",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) commentary_appended_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) commentary_appended_event > (schema) > (property) client_event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveCommentaryAppended/properties/client_event_id",
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
  "(resource) live > (model) commentary_appended_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.commentary.appended"
    }
  }
}
```

#### Example

```json
{
  "type": "session.commentary.appended",
  "event_id": "evt_commentary_002",
  "client_event_id": "evt_commentary_001",
  "start_ms": 5200,
  "end_ms": 5400
}
```

### session.input_transcript.delta

A transcript fragment for user input audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

#### Schema

Schema name: `LiveInputTranscriptDelta`

```json
{
  "(resource) live > (model) input_transcript_delta_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInputTranscriptDelta",
    "docstring": "A transcript fragment for user input audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.",
    "ident": "InputTranscriptDeltaEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "delta"
        },
        {
          "ident": "end_ms"
        },
        {
          "ident": "event_id"
        },
        {
          "ident": "start_ms"
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
      "(resource) live > (model) input_transcript_delta_event > (schema) > (property) delta",
      "(resource) live > (model) input_transcript_delta_event > (schema) > (property) end_ms",
      "(resource) live > (model) input_transcript_delta_event > (schema) > (property) event_id",
      "(resource) live > (model) input_transcript_delta_event > (schema) > (property) start_ms",
      "(resource) live > (model) input_transcript_delta_event > (schema) > (property) type",
      "(resource) live > (model) input_transcript_delta_event > (schema) > (property) client_event_id"
    ]
  },
  "(resource) live > (model) input_transcript_delta_event > (schema) > (property) delta": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputTranscriptDelta/properties/delta",
    "deprecated": false,
    "key": "delta",
    "docstring": "The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) input_transcript_delta_event > (schema) > (property) end_ms": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputTranscriptDelta/properties/end_ms",
    "deprecated": false,
    "key": "end_ms",
    "docstring": "The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) input_transcript_delta_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputTranscriptDelta/properties/event_id",
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
  "(resource) live > (model) input_transcript_delta_event > (schema) > (property) start_ms": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputTranscriptDelta/properties/start_ms",
    "deprecated": false,
    "key": "start_ms",
    "docstring": "The start of this event on the Live session timeline, in milliseconds from the beginning of the session.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) input_transcript_delta_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputTranscriptDelta/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The event type, always `session.input_transcript.delta`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInputTranscriptDelta/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.input_transcript.delta"
        }
      ]
    },
    "default": "session.input_transcript.delta",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) input_transcript_delta_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) input_transcript_delta_event > (schema) > (property) client_event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInputTranscriptDelta/properties/client_event_id",
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
  "(resource) live > (model) input_transcript_delta_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.input_transcript.delta"
    }
  }
}
```

#### Example

```json
{
  "type": "session.input_transcript.delta",
  "event_id": "evt_input_transcript_001",
  "delta": "A table for two at seven, please.",
  "start_ms": 1600,
  "end_ms": 3400
}
```

### session.output_transcript.delta

A transcript fragment for assistant output audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

#### Schema

Schema name: `LiveOutputTranscriptDelta`

```json
{
  "(resource) live > (model) output_transcript_delta_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveOutputTranscriptDelta",
    "docstring": "A transcript fragment for assistant output audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.",
    "ident": "OutputTranscriptDeltaEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "delta"
        },
        {
          "ident": "end_ms"
        },
        {
          "ident": "event_id"
        },
        {
          "ident": "start_ms"
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
      "(resource) live > (model) output_transcript_delta_event > (schema) > (property) delta",
      "(resource) live > (model) output_transcript_delta_event > (schema) > (property) end_ms",
      "(resource) live > (model) output_transcript_delta_event > (schema) > (property) event_id",
      "(resource) live > (model) output_transcript_delta_event > (schema) > (property) start_ms",
      "(resource) live > (model) output_transcript_delta_event > (schema) > (property) type",
      "(resource) live > (model) output_transcript_delta_event > (schema) > (property) client_event_id"
    ]
  },
  "(resource) live > (model) output_transcript_delta_event > (schema) > (property) delta": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveOutputTranscriptDelta/properties/delta",
    "deprecated": false,
    "key": "delta",
    "docstring": "The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) output_transcript_delta_event > (schema) > (property) end_ms": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveOutputTranscriptDelta/properties/end_ms",
    "deprecated": false,
    "key": "end_ms",
    "docstring": "The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) output_transcript_delta_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveOutputTranscriptDelta/properties/event_id",
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
  "(resource) live > (model) output_transcript_delta_event > (schema) > (property) start_ms": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveOutputTranscriptDelta/properties/start_ms",
    "deprecated": false,
    "key": "start_ms",
    "docstring": "The start of this event on the Live session timeline, in milliseconds from the beginning of the session.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) output_transcript_delta_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveOutputTranscriptDelta/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The event type, always `session.output_transcript.delta`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveOutputTranscriptDelta/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.output_transcript.delta"
        }
      ]
    },
    "default": "session.output_transcript.delta",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) output_transcript_delta_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) output_transcript_delta_event > (schema) > (property) client_event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveOutputTranscriptDelta/properties/client_event_id",
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
  "(resource) live > (model) output_transcript_delta_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.output_transcript.delta"
    }
  }
}
```

#### Example

```json
{
  "type": "session.output_transcript.delta",
  "event_id": "evt_output_transcript_001",
  "delta": "Would you like me to reserve that table?",
  "start_ms": 5400,
  "end_ms": 7200
}
```

### session.delegation.created

Returned when the Live model delegates work to your application or a Responses backend. Contains delegation metadata and the position on the session timeline where the work was delegated.

#### Schema

Schema name: `LiveDelegationCreated`

```json
{
  "(resource) live > (model) delegation_created_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveDelegationCreated",
    "docstring": "Returned when the Live model delegates work to your application or a Responses backend. Contains delegation metadata and the position on the session timeline where the work was delegated.",
    "ident": "DelegationCreatedEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "delegation"
        },
        {
          "ident": "event_id"
        },
        {
          "ident": "offset_ms"
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
      "(resource) live > (model) delegation_created_event > (schema) > (property) delegation",
      "(resource) live > (model) delegation_created_event > (schema) > (property) event_id",
      "(resource) live > (model) delegation_created_event > (schema) > (property) offset_ms",
      "(resource) live > (model) delegation_created_event > (schema) > (property) type",
      "(resource) live > (model) delegation_created_event > (schema) > (property) client_event_id"
    ]
  },
  "(resource) live > (model) delegation_created_event > (schema) > (property) delegation": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveDelegationCreated/properties/delegation",
    "deprecated": false,
    "key": "delegation",
    "docstring": "The delegated work identifier and destination. This object contains metadata, not the task text.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "target"
        },
        {
          "ident": "type"
        },
        {
          "ident": "response_id"
        }
      ]
    },
    "optional": false,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) delegation_created_event > (schema) > (property) delegation > (property) id",
      "(resource) live > (model) delegation_created_event > (schema) > (property) delegation > (property) target",
      "(resource) live > (model) delegation_created_event > (schema) > (property) delegation > (property) type",
      "(resource) live > (model) delegation_created_event > (schema) > (property) delegation > (property) response_id"
    ]
  },
  "(resource) live > (model) delegation_created_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveDelegationCreated/properties/event_id",
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
  "(resource) live > (model) delegation_created_event > (schema) > (property) offset_ms": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveDelegationCreated/properties/offset_ms",
    "deprecated": false,
    "key": "offset_ms",
    "docstring": "The position on the Live session timeline where the delegation was created, in milliseconds from the beginning of the session.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) delegation_created_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveDelegationCreated/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The event type, always `session.delegation.created`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveDelegationCreated/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.delegation.created"
        }
      ]
    },
    "default": "session.delegation.created",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) delegation_created_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) delegation_created_event > (schema) > (property) client_event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveDelegationCreated/properties/client_event_id",
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
  "(resource) live > (model) delegation_created_event > (schema) > (property) delegation > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveDelegationItem/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the delegation. Use this as delegation_id when replying to client-owned work or correlating Responses events.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) delegation_created_event > (schema) > (property) delegation > (property) target": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveDelegationItem/properties/target",
    "deprecated": false,
    "key": "target",
    "docstring": "Where the Live model delegated the work: `client` for your application, or `responses` for the configured Responses backend.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveDelegationItem/properties/target",
      "types": [
        {
          "kind": "HttpTypeUnion",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "client"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "responses"
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
      "(resource) live > (model) delegation_created_event > (schema) > (property) delegation > (property) target > (variant) 0"
    ]
  },
  "(resource) live > (model) delegation_created_event > (schema) > (property) delegation > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveDelegationItem/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The object type, always `delegation`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveDelegationItem/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "delegation"
        }
      ]
    },
    "default": "delegation",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) delegation_created_event > (schema) > (property) delegation > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) delegation_created_event > (schema) > (property) delegation > (property) response_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveDelegationItem/properties/response_id",
    "deprecated": false,
    "key": "response_id",
    "docstring": "The ID of the Responses API response associated with a Responses delegation. Omitted for client delegations.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) delegation_created_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.delegation.created"
    }
  },
  "(resource) live > (model) delegation_created_event > (schema) > (property) delegation > (property) target > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "docstring": "Where the Live model delegated the work: `client` for your application, or `responses` for the configured Responses backend.",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "client"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "responses"
        }
      ]
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) delegation_created_event > (schema) > (property) delegation > (property) target > (variant) 0 > (member) 0",
      "(resource) live > (model) delegation_created_event > (schema) > (property) delegation > (property) target > (variant) 0 > (member) 1"
    ]
  },
  "(resource) live > (model) delegation_created_event > (schema) > (property) delegation > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "delegation"
    }
  },
  "(resource) live > (model) delegation_created_event > (schema) > (property) delegation > (property) target > (variant) 0 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "client"
    }
  },
  "(resource) live > (model) delegation_created_event > (schema) > (property) delegation > (property) target > (variant) 0 > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "responses"
    }
  }
}
```

#### Example

```json
{
  "type": "session.delegation.created",
  "event_id": "evt_delegation_001",
  "offset_ms": 3600,
  "delegation": {
    "id": "del_abc123",
    "type": "delegation",
    "target": "client"
  }
}
```

### response.event

A streaming Responses API event from a backend delegated to by the Live session. Use the outer delegation_id to associate the nested stream with its Live delegation.

#### Schema

Schema name: `LiveResponseEvent`

```json
{
  "(resource) live > (model) response_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveResponseEvent",
    "docstring": "A streaming Responses API event from a backend delegated to by the Live session. Use the outer delegation_id to associate the nested stream with its Live delegation.",
    "ident": "ResponseEvent",
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
        },
        {
          "ident": "client_event_id"
        },
        {
          "ident": "delegation_id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) response_event > (schema) > (property) event",
      "(resource) live > (model) response_event > (schema) > (property) event_id",
      "(resource) live > (model) response_event > (schema) > (property) type",
      "(resource) live > (model) response_event > (schema) > (property) client_event_id",
      "(resource) live > (model) response_event > (schema) > (property) delegation_id"
    ]
  },
  "(resource) live > (model) response_event > (schema) > (property) event": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponseEvent/properties/event",
    "deprecated": false,
    "key": "event",
    "docstring": "The nested Responses streaming event. Dispatch on its type field. Response lifecycle snapshots omit input and clear instructions, tools, and output to keep messages small; consume granular output events for the generated content.",
    "type": {
      "kind": "HttpTypeReference",
      "oasRef": "#/components/schemas/LiveResponseEvent/properties/event",
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
    "nullable": false,
    "schemaType": "map",
    "children": []
  },
  "(resource) live > (model) response_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponseEvent/properties/event_id",
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
  "(resource) live > (model) response_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponseEvent/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The event type, always `response.event`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveResponseEvent/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "response.event"
        }
      ]
    },
    "default": "response.event",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) response_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) response_event > (schema) > (property) client_event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponseEvent/properties/client_event_id",
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
  "(resource) live > (model) response_event > (schema) > (property) delegation_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponseEvent/properties/delegation_id",
    "deprecated": false,
    "key": "delegation_id",
    "docstring": "The Live delegation associated with the nested Responses event. May be null or omitted when the event cannot be correlated with a delegation.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) response_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "response.event"
    }
  }
}
```

#### Example

```json
{
  "type": "response.event",
  "event_id": "evt_response_002",
  "delegation_id": "del_responses123",
  "event": {
    "type": "response.output_text.delta",
    "item_id": "msg_abc123",
    "output_index": 0,
    "content_index": 0,
    "delta": "An outdoor table is available at 7 PM.",
    "sequence_number": 3,
    "logprobs": []
  }
}
```

### session.usage.updated

Reports cumulative Live audio usage and, when available, the most recent context-window usage. Delegated Responses token usage is reported separately in response.event events.

#### Schema

Schema name: `LiveSessionUsageUpdated`

```json
{
  "(resource) live > (model) session_usage_updated_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveSessionUsageUpdated",
    "docstring": "Reports cumulative Live audio usage and, when available, the most recent context-window usage. Delegated Responses token usage is reported separately in response.event events.",
    "ident": "SessionUsageUpdatedEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "event_id"
        },
        {
          "ident": "type"
        },
        {
          "ident": "usage"
        },
        {
          "ident": "client_event_id"
        },
        {
          "ident": "context_window"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_usage_updated_event > (schema) > (property) event_id",
      "(resource) live > (model) session_usage_updated_event > (schema) > (property) type",
      "(resource) live > (model) session_usage_updated_event > (schema) > (property) usage",
      "(resource) live > (model) session_usage_updated_event > (schema) > (property) client_event_id",
      "(resource) live > (model) session_usage_updated_event > (schema) > (property) context_window"
    ]
  },
  "(resource) live > (model) session_usage_updated_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionUsageUpdated/properties/event_id",
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
  "(resource) live > (model) session_usage_updated_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionUsageUpdated/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The event type, always `session.usage.updated`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionUsageUpdated/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.usage.updated"
        }
      ]
    },
    "default": "session.usage.updated",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) session_usage_updated_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) session_usage_updated_event > (schema) > (property) usage": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionUsageUpdated/properties/usage",
    "deprecated": false,
    "key": "usage",
    "docstring": "The cumulative Live audio usage so far.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "SessionUsage",
      "$ref": "(resource) live > (model) session_usage > (schema)"
    },
    "optional": false,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "object",
    "modelPath": "(resource) live > (model) session_usage",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_usage > (schema) > (property) seconds"
    ]
  },
  "(resource) live > (model) session_usage_updated_event > (schema) > (property) client_event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionUsageUpdated/properties/client_event_id",
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
  "(resource) live > (model) session_usage_updated_event > (schema) > (property) context_window": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionUsageUpdated/properties/context_window",
    "deprecated": false,
    "key": "context_window",
    "docstring": "The latest measured Live context-window usage. Omitted when the context limit is unknown.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "usage_ratio"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_usage_updated_event > (schema) > (property) context_window > (property) usage_ratio"
    ]
  },
  "(resource) live > (model) session_usage_updated_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.usage.updated"
    }
  },
  "(resource) live > (model) session_usage > (schema) > (property) seconds": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionUsage/properties/seconds",
    "deprecated": false,
    "key": "seconds",
    "docstring": "The cumulative Live audio duration in seconds. Do not sum this value across usage events.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) live > (model) session_usage > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveSessionUsage",
    "docstring": "Cumulative audio duration for a Live session. Values are totals for the session, not increments to sum across usage events.",
    "ident": "SessionUsage",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "seconds"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_usage > (schema) > (property) seconds"
    ]
  },
  "(resource) live > (model) session_usage_updated_event > (schema) > (property) context_window > (property) usage_ratio": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveContextWindowUsage/properties/usage_ratio",
    "deprecated": false,
    "key": "usage_ratio",
    "docstring": "The latest active context token count divided by the Live model context limit. Can decrease after compaction and may lag between measured audio frames.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "number",
    "children": []
  }
}
```

#### Example

```json
{
  "type": "session.usage.updated",
  "event_id": "evt_usage_001",
  "usage": {
    "seconds": 32.5
  },
  "context_window": {
    "usage_ratio": 0.12
  }
}
```

### session.closed

Returned after the Live session finishes finalizing, with the close reason, final session snapshot, and cumulative audio usage. A connection closing without this event does not confirm successful finalization.

#### Schema

Schema name: `LiveSessionClosed`

```json
{
  "(resource) live > (model) session_closed_event > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveSessionClosed",
    "docstring": "Returned after the Live session finishes finalizing, with the close reason, final session snapshot, and cumulative audio usage. A connection closing without this event does not confirm successful finalization.",
    "ident": "SessionClosedEvent",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "event_id"
        },
        {
          "ident": "reason"
        },
        {
          "ident": "session"
        },
        {
          "ident": "type"
        },
        {
          "ident": "usage"
        },
        {
          "ident": "client_event_id"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_closed_event > (schema) > (property) event_id",
      "(resource) live > (model) session_closed_event > (schema) > (property) reason",
      "(resource) live > (model) session_closed_event > (schema) > (property) session",
      "(resource) live > (model) session_closed_event > (schema) > (property) type",
      "(resource) live > (model) session_closed_event > (schema) > (property) usage",
      "(resource) live > (model) session_closed_event > (schema) > (property) client_event_id"
    ]
  },
  "(resource) live > (model) session_closed_event > (schema) > (property) event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionClosed/properties/event_id",
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
  "(resource) live > (model) session_closed_event > (schema) > (property) reason": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionClosed/properties/reason",
    "deprecated": false,
    "key": "reason",
    "docstring": "Why the Live session ended: `close_requested` for an application close or hangup request, `expired` for the session duration limit, `content` for a safety filter, `remote_hangup` for a graceful remote disconnect, or `connection_lost` for an unexpected primary or upstream disconnection.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionClosed/properties/reason",
      "types": [
        {
          "kind": "HttpTypeUnion",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "close_requested"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "expired"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "content"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "remote_hangup"
            },
            {
              "kind": "HttpTypeLiteral",
              "literal": "connection_lost"
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
      "(resource) live > (model) session_closed_event > (schema) > (property) reason > (variant) 0"
    ]
  },
  "(resource) live > (model) session_closed_event > (schema) > (property) session": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionClosed/properties/session",
    "deprecated": false,
    "key": "session",
    "docstring": "The resolved Live session configuration and server-assigned session metadata.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "SessionResource",
      "$ref": "(resource) live > (model) session_resource > (schema)"
    },
    "optional": false,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "object",
    "modelPath": "(resource) live > (model) session_resource",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) id",
      "(resource) live > (model) session_resource > (schema) > (property) expires_at",
      "(resource) live > (model) session_resource > (schema) > (property) model",
      "(resource) live > (model) session_resource > (schema) > (property) status",
      "(resource) live > (model) session_resource > (schema) > (property) audio",
      "(resource) live > (model) session_resource > (schema) > (property) client",
      "(resource) live > (model) session_resource > (schema) > (property) delegation",
      "(resource) live > (model) session_resource > (schema) > (property) input",
      "(resource) live > (model) session_resource > (schema) > (property) instructions",
      "(resource) live > (model) session_resource > (schema) > (property) store"
    ]
  },
  "(resource) live > (model) session_closed_event > (schema) > (property) type": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionClosed/properties/type",
    "deprecated": false,
    "key": "type",
    "docstring": "The event type, always `session.closed`.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionClosed/properties/type",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "session.closed"
        }
      ]
    },
    "default": "session.closed",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) session_closed_event > (schema) > (property) type > (member) 0"
    ]
  },
  "(resource) live > (model) session_closed_event > (schema) > (property) usage": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionClosed/properties/usage",
    "deprecated": false,
    "key": "usage",
    "docstring": "The final cumulative Live audio usage after session finalization.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "SessionUsage",
      "$ref": "(resource) live > (model) session_usage > (schema)"
    },
    "optional": false,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "object",
    "modelPath": "(resource) live > (model) session_usage",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_usage > (schema) > (property) seconds"
    ]
  },
  "(resource) live > (model) session_closed_event > (schema) > (property) client_event_id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionClosed/properties/client_event_id",
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
  "(resource) live > (model) session_closed_event > (schema) > (property) reason > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "docstring": "Why the Live session ended: `close_requested` for an application close or hangup request, `expired` for the session duration limit, `content` for a safety filter, `remote_hangup` for a graceful remote disconnect, or `connection_lost` for an unexpected primary or upstream disconnection.",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeUnion",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "close_requested"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "expired"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "content"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "remote_hangup"
        },
        {
          "kind": "HttpTypeLiteral",
          "literal": "connection_lost"
        }
      ]
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) session_closed_event > (schema) > (property) reason > (variant) 0 > (member) 0",
      "(resource) live > (model) session_closed_event > (schema) > (property) reason > (variant) 0 > (member) 1",
      "(resource) live > (model) session_closed_event > (schema) > (property) reason > (variant) 0 > (member) 2",
      "(resource) live > (model) session_closed_event > (schema) > (property) reason > (variant) 0 > (member) 3",
      "(resource) live > (model) session_closed_event > (schema) > (property) reason > (variant) 0 > (member) 4"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) id": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/id",
    "deprecated": false,
    "key": "id",
    "docstring": "The unique ID of the Live session. Use this ID for sideband connections, forking, and recording download.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) session_resource > (schema) > (property) expires_at": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/expires_at",
    "deprecated": false,
    "key": "expires_at",
    "docstring": "The Unix timestamp, in seconds, at which the Live session expires.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "integer",
    "children": []
  },
  "(resource) live > (model) session_resource > (schema) > (property) model": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/model",
    "deprecated": false,
    "key": "model",
    "docstring": "The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/model",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
          "kind": "HttpTypeUnion",
          "oasRef": "#/components/schemas/ModelIdsLive/anyOf/1",
          "types": [
            {
              "kind": "HttpTypeLiteral",
              "literal": "gpt-live-1"
            }
          ]
        }
      ]
    },
    "examples": [
      "gpt-live-1"
    ],
    "optional": false,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 0",
      "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 1"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) status": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/status",
    "deprecated": false,
    "key": "status",
    "docstring": "The status of the session snapshot. Always `active`, including the final snapshot in session.closed; use the event type to determine that the session has closed.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/status",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "active"
        }
      ]
    },
    "default": "active",
    "optional": false,
    "nullable": false,
    "schemaType": "enum",
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) status > (member) 0"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/audio",
    "deprecated": false,
    "key": "audio",
    "docstring": "Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "format"
        },
        {
          "ident": "output"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) format",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) client": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/client",
    "deprecated": false,
    "key": "client",
    "docstring": "Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.",
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
  "(resource) live > (model) session_resource > (schema) > (property) delegation": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/delegation",
    "deprecated": false,
    "key": "delegation",
    "docstring": "Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/delegation",
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
              "ident": "responses"
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
      "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 0",
      "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) input": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/input",
    "deprecated": false,
    "key": "input",
    "docstring": "Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.",
    "type": {
      "kind": "HttpTypeArray",
      "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/input",
      "elementType": {
        "kind": "HttpTypeReference",
        "ident": "InitialItem",
        "$ref": "(resource) live > (model) initial_item > (schema)"
      }
    },
    "optional": true,
    "nullable": false,
    "schemaType": "array",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 0",
      "(resource) live > (model) initial_item > (schema) > (variant) 1",
      "(resource) live > (model) initial_item > (schema) > (variant) 2"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) instructions": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/instructions",
    "deprecated": false,
    "key": "instructions",
    "docstring": "Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.",
    "type": {
      "kind": "HttpTypeString"
    },
    "optional": true,
    "nullable": true,
    "schemaType": "string",
    "children": []
  },
  "(resource) live > (model) session_resource > (schema) > (property) store": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/store",
    "deprecated": false,
    "key": "store",
    "docstring": "Whether to store the session for later forking and recording download. Defaults to false for new sessions.",
    "type": {
      "kind": "HttpTypeBoolean"
    },
    "optional": true,
    "nullable": false,
    "schemaType": "boolean",
    "children": []
  },
  "(resource) live > (model) session_resource > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveSessionResourceParam",
    "docstring": "The resolved Live session configuration and server-assigned session metadata.",
    "ident": "SessionResource",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "id"
        },
        {
          "ident": "expires_at"
        },
        {
          "ident": "model"
        },
        {
          "ident": "status"
        },
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
          "ident": "input"
        },
        {
          "ident": "instructions"
        },
        {
          "ident": "store"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) id",
      "(resource) live > (model) session_resource > (schema) > (property) expires_at",
      "(resource) live > (model) session_resource > (schema) > (property) model",
      "(resource) live > (model) session_resource > (schema) > (property) status",
      "(resource) live > (model) session_resource > (schema) > (property) audio",
      "(resource) live > (model) session_resource > (schema) > (property) client",
      "(resource) live > (model) session_resource > (schema) > (property) delegation",
      "(resource) live > (model) session_resource > (schema) > (property) input",
      "(resource) live > (model) session_resource > (schema) > (property) instructions",
      "(resource) live > (model) session_resource > (schema) > (property) store"
    ]
  },
  "(resource) live > (model) session_closed_event > (schema) > (property) type > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "session.closed"
    }
  },
  "(resource) live > (model) session_usage > (schema) > (property) seconds": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveSessionUsage/properties/seconds",
    "deprecated": false,
    "key": "seconds",
    "docstring": "The cumulative Live audio duration in seconds. Do not sum this value across usage events.",
    "type": {
      "kind": "HttpTypeNumber"
    },
    "optional": false,
    "nullable": false,
    "schemaType": "number",
    "children": []
  },
  "(resource) live > (model) session_usage > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveSessionUsage",
    "docstring": "Cumulative audio duration for a Live session. Values are totals for the session, not increments to sum across usage events.",
    "ident": "SessionUsage",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "seconds"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_usage > (schema) > (property) seconds"
    ]
  },
  "(resource) live > (model) session_closed_event > (schema) > (property) reason > (variant) 0 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "close_requested"
    }
  },
  "(resource) live > (model) session_closed_event > (schema) > (property) reason > (variant) 0 > (member) 1": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "expired"
    }
  },
  "(resource) live > (model) session_closed_event > (schema) > (property) reason > (variant) 0 > (member) 2": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "content"
    }
  },
  "(resource) live > (model) session_closed_event > (schema) > (property) reason > (variant) 0 > (member) 3": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "remote_hangup"
    }
  },
  "(resource) live > (model) session_closed_event > (schema) > (property) reason > (variant) 0 > (member) 4": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "connection_lost"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ModelIdsLive/anyOf/0",
    "ident": "UnionMember0",
    "type": {
      "kind": "HttpTypeString"
    },
    "children": []
  },
  "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/ModelIdsLive/anyOf/1",
    "docstring": "The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.",
    "ident": "UnionMember1",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/ModelIdsLive/anyOf/1",
      "types": [
        {
          "kind": "HttpTypeLiteral",
          "literal": "gpt-live-1"
        }
      ]
    },
    "childrenParentSchema": "enum",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 1 > (member) 0"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) status > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "active"
    }
  },
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) format": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialSessionAudioParam/properties/format",
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
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialSessionAudioParam/properties/output",
    "deprecated": false,
    "key": "output",
    "docstring": "The voice used for speech generated by the Live model.",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "voice"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "object",
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice"
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
  "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 0": {
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
  "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveSessionResourceParam/properties/delegation/anyOf/0/oneOf/1",
    "docstring": "Delegate tasks to a Responses model managed by the Live session.",
    "ident": "Responses",
    "type": {
      "kind": "HttpTypeObject",
      "members": [
        {
          "ident": "responses"
        },
        {
          "ident": "type"
        }
      ]
    },
    "childrenParentSchema": "object",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1 > (property) responses",
      "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1 > (property) type"
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
  "(resource) live > (model) initial_item > (schema) > (variant) 0": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInitialItem/oneOf/0",
    "docstring": "A developer message included in the initial text history of a Live session.",
    "ident": "Developer",
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
          "ident": "id"
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
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) content",
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) role",
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) id",
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) status",
      "(resource) live > (model) initial_item > (schema) > (variant) 0 > (property) type"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 1": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInitialItem/oneOf/1",
    "docstring": "A user message included in the initial text history of a Live session.",
    "ident": "User",
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
          "ident": "id"
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
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) content",
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) role",
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) id",
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) status",
      "(resource) live > (model) initial_item > (schema) > (variant) 1 > (property) type"
    ]
  },
  "(resource) live > (model) initial_item > (schema) > (variant) 2": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInitialItem/oneOf/2",
    "docstring": "An assistant message included in the initial text history of a Live session.",
    "ident": "Assistant",
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
          "ident": "id"
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
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) content",
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) role",
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) id",
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) status",
      "(resource) live > (model) initial_item > (schema) > (variant) 2 > (property) type"
    ]
  },
  "(resource) live > (model) initial_item > (schema)": {
    "kind": "HttpDeclTypeAlias",
    "oasRef": "#/components/schemas/LiveInitialItem",
    "docstring": "A developer, user, or assistant message supplied as text history before the Live session starts.",
    "ident": "InitialItem",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialItem",
      "types": [
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
              "ident": "id"
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
              "ident": "content"
            },
            {
              "ident": "role"
            },
            {
              "ident": "id"
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
              "ident": "content"
            },
            {
              "ident": "role"
            },
            {
              "ident": "id"
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
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) initial_item > (schema) > (variant) 0",
      "(resource) live > (model) initial_item > (schema) > (variant) 1",
      "(resource) live > (model) initial_item > (schema) > (variant) 2"
    ]
  },
  "(resource) live > (model) session_resource > (schema) > (property) model > (variant) 1 > (member) 0": {
    "kind": "HttpDeclReference",
    "type": {
      "kind": "HttpTypeLiteral",
      "literal": "gpt-live-1"
    }
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
  "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveInitialSessionAudioOutputParam/properties/voice",
    "deprecated": false,
    "key": "voice",
    "docstring": "The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.",
    "type": {
      "kind": "HttpTypeUnion",
      "oasRef": "#/components/schemas/LiveInitialSessionAudioOutputParam/properties/voice",
      "types": [
        {
          "kind": "HttpTypeString"
        },
        {
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
        {
          "kind": "HttpTypeReference",
          "ident": "CustomVoice",
          "$ref": "(resource) live > (model) custom_voice > (schema)"
        }
      ]
    },
    "optional": true,
    "nullable": false,
    "schemaType": "union",
    "childrenParentSchema": "union",
    "children": [
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 0",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 1",
      "(resource) live > (model) session_resource > (schema) > (property) audio > (property) output > (property) voice > (variant) 2"
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
  "(resource) live > (model) session_resource > (schema) > (property) delegation > (variant) 1 > (property) responses": {
    "kind": "HttpDeclProperty",
    "oasRef": "#/components/schemas/LiveResponsesDelegationParam/properties/responses",
    "deprecated": false,
    "key": "responses",
    "docstring": "Backend model, prompt, and tools used when the Live session delegates a task to Responses.",
    "type": {
      "kind": "HttpTypeReference",
      "ident": "ResponsesDelegationConfig",
      "$ref": "(resource) live > (model) responses_delegation_config > (schema)"
    },
    "optional": false,
    "nullable": false,
    "modelImplicit": false,
    "schemaType": "object",
    "modelPath": "(resource) live > (model) responses_delegation_config",
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

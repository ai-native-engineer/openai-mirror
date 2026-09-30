<!-- source: https://developers.openai.com/api/reference/go/resources/live/ -->

# Live

## Create session

`client.Live.New(ctx, body) (*LiveNewResponse, error)`

**post** `/live/sessions`

Create a Live WebRTC session. Start with the [Live prompting guide](/api/docs/guides/live-prompting).

### Parameters

- `body LiveNewParams`

  - `Session param.Field[MediaSessionConfig]`

    Startup configuration for the Live session.

  - `Transport param.Field[LiveNewParamsTransport]`

    WebRTC transport with the browser's SDP offer.

    - `Sdp string`

      Session Description Protocol message for the WebRTC connection.

    - `Type Webrtc`

      The transport used for the Live session. Always `webrtc`.

      - `const WebrtcWebrtc Webrtc = "webrtc"`

### Returns

- `type LiveNewResponse struct{…}`

  The created Live session identifier and WebRTC answer. Apply transport.sdp as the peer's remote answer and wait for session.started on the data channel before sending commands.

  - `Session LiveNewResponseSession`

    The newly created Live session. Use its ID for session controls and sideband connections.

    - `ID string`

      Opaque session identifier. Preserve the returned value unchanged, including its prefix.

  - `Transport LiveNewResponseTransport`

    WebRTC transport with the SDP answer.

    - `Sdp string`

      Session Description Protocol message for the WebRTC connection.

    - `Type Webrtc`

      The transport used for the Live session. Always `webrtc`.

      - `const WebrtcWebrtc Webrtc = "webrtc"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/live"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  live, err := client.Live.New(context.TODO(), live.LiveNewParams{
    Session: live.MediaSessionConfigParam{
      Model: live.MediaSessionConfigModelGPTLive1,
    },
    Transport: live.LiveNewParamsTransport{
      Sdp: "x",
    },
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", live.Session)
}
```

#### Response

```json
{
  "session": {
    "id": "live_123"
  },
  "transport": {
    "type": "webrtc",
    "sdp": "<SDP answer>"
  }
}
```

## Domain Types

### Audio Format

- `type AudioFormatUnion interface{…}`

  Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

  - `AudioFormatAudioPCM`

    - `Rate int64`

      Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

      - `const AudioFormatAudioPCMRate16000 AudioFormatAudioPCMRate = 16000`

      - `const AudioFormatAudioPCMRate24000 AudioFormatAudioPCMRate = 24000`

    - `Type AudioPCM`

      The audio encoding. Always `audio/pcm`.

      - `const AudioPCMAudioPCM AudioPCM = "audio/pcm"`

  - `AudioFormatAudioPCMU`

    - `Rate int64`

      Audio sample rate in hertz. G.711 audio uses 8000 Hz.

    - `Type AudioPCMU`

      The audio encoding. Always `audio/pcmu`.

      - `const AudioPCMUAudioPCMU AudioPCMU = "audio/pcmu"`

  - `AudioFormatAudioPCMA`

    - `Rate int64`

      Audio sample rate in hertz. G.711 audio uses 8000 Hz.

    - `Type AudioPCMA`

      The audio encoding. Always `audio/pcma`.

      - `const AudioPCMAAudioPCMA AudioPCMA = "audio/pcma"`

### Built In Voice

- `type BuiltInVoice string`

  A built-in voice available for Live speech.

  - `const BuiltInVoiceAlloy BuiltInVoice = "alloy"`

  - `const BuiltInVoiceAsh BuiltInVoice = "ash"`

  - `const BuiltInVoiceBallad BuiltInVoice = "ballad"`

  - `const BuiltInVoiceBeacon BuiltInVoice = "beacon"`

  - `const BuiltInVoiceBossa BuiltInVoice = "bossa"`

  - `const BuiltInVoiceCedar BuiltInVoice = "cedar"`

  - `const BuiltInVoiceCinder BuiltInVoice = "cinder"`

  - `const BuiltInVoiceCoral BuiltInVoice = "coral"`

  - `const BuiltInVoiceDelta BuiltInVoice = "delta"`

  - `const BuiltInVoiceEcho BuiltInVoice = "echo"`

  - `const BuiltInVoiceGleam BuiltInVoice = "gleam"`

  - `const BuiltInVoiceMarin BuiltInVoice = "marin"`

  - `const BuiltInVoiceMeridian BuiltInVoice = "meridian"`

  - `const BuiltInVoiceQuartz BuiltInVoice = "quartz"`

  - `const BuiltInVoiceRipple BuiltInVoice = "ripple"`

  - `const BuiltInVoiceSage BuiltInVoice = "sage"`

  - `const BuiltInVoiceShimmer BuiltInVoice = "shimmer"`

  - `const BuiltInVoiceStone BuiltInVoice = "stone"`

  - `const BuiltInVoiceTempo BuiltInVoice = "tempo"`

  - `const BuiltInVoiceVerse BuiltInVoice = "verse"`

  - `const BuiltInVoiceVesper BuiltInVoice = "vesper"`

  - `const BuiltInVoiceWillow BuiltInVoice = "willow"`

### Client Config

- `type ClientConfig struct{…}`

  Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

  - `DataChannel DataChannelConfig`

    Client and server event permissions for the WebRTC frontend data channel.

    - `AllowedClientEvents DataChannelConfigAllowedClientEventsUnion`

      Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

      - `All`

        - `const AllAll All = "all"`

      - `[]string`

    - `AllowedServerEvents DataChannelConfigAllowedServerEventsUnion`

      Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

      - `All`

        - `const AllAll All = "all"`

      - `[]ServerEventSelector`

        - `Type string`

          The outer Live server event type. Use 'response.event' for Responses events.

        - `ResponseEvent string`

          The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

### Client Delegation

- `type ClientDelegation struct{…}`

  Delegate tasks to your application. The Live session emits delegation events that your backend handles.

  - `Type Client`

    The delegation owner. Always `client` for tasks handled by your application.

    - `const ClientClient Client = "client"`

### Client Event

- `type ClientEventUnion interface{…}`

  Client events for Live. Initialize a primary WebSocket with session.start and wait for session.started. WebRTC creation already starts the session. Audio append is primary WebSocket-only. See the [Live prompting guide](https://developers.openai.com/api/docs/guides/live-prompting) before writing frontend instructions and delegation policies.

  - `type SessionStartEvent struct{…}`

    Start a Live session on a primary WebSocket. Send this event before other commands and wait for `session.started`.

    - `Session SessionConfig`

      Initial configuration for a primary WebSocket. Send session.start first and wait for session.started before application commands. WebRTC creation already starts the session; do not send this event again on its data channel.

      - `Model SessionConfigModel`

        The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

        - `string`

        - `SessionConfigModel`

          - `const SessionConfigModelGPTLive1 SessionConfigModel = "gpt-live-1"`

      - `Audio SessionConfigAudio`

        Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

        - `Format AudioFormatUnion`

          Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

          - `AudioFormatAudioPCM`

            - `Rate int64`

              Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

              - `const AudioFormatAudioPCMRate16000 AudioFormatAudioPCMRate = 16000`

              - `const AudioFormatAudioPCMRate24000 AudioFormatAudioPCMRate = 24000`

            - `Type AudioPCM`

              The audio encoding. Always `audio/pcm`.

              - `const AudioPCMAudioPCM AudioPCM = "audio/pcm"`

          - `AudioFormatAudioPCMU`

            - `Rate int64`

              Audio sample rate in hertz. G.711 audio uses 8000 Hz.

            - `Type AudioPCMU`

              The audio encoding. Always `audio/pcmu`.

              - `const AudioPCMUAudioPCMU AudioPCMU = "audio/pcmu"`

          - `AudioFormatAudioPCMA`

            - `Rate int64`

              Audio sample rate in hertz. G.711 audio uses 8000 Hz.

            - `Type AudioPCMA`

              The audio encoding. Always `audio/pcma`.

              - `const AudioPCMAAudioPCMA AudioPCMA = "audio/pcma"`

        - `Output SessionConfigAudioOutput`

          The voice used for speech generated by the Live model.

          - `Voice SessionConfigAudioOutputVoiceUnion`

            The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

            - `string`

            - `type BuiltInVoice string`

              A built-in voice available for Live speech.

              - `const BuiltInVoiceAlloy BuiltInVoice = "alloy"`

              - `const BuiltInVoiceAsh BuiltInVoice = "ash"`

              - `const BuiltInVoiceBallad BuiltInVoice = "ballad"`

              - `const BuiltInVoiceBeacon BuiltInVoice = "beacon"`

              - `const BuiltInVoiceBossa BuiltInVoice = "bossa"`

              - `const BuiltInVoiceCedar BuiltInVoice = "cedar"`

              - `const BuiltInVoiceCinder BuiltInVoice = "cinder"`

              - `const BuiltInVoiceCoral BuiltInVoice = "coral"`

              - `const BuiltInVoiceDelta BuiltInVoice = "delta"`

              - `const BuiltInVoiceEcho BuiltInVoice = "echo"`

              - `const BuiltInVoiceGleam BuiltInVoice = "gleam"`

              - `const BuiltInVoiceMarin BuiltInVoice = "marin"`

              - `const BuiltInVoiceMeridian BuiltInVoice = "meridian"`

              - `const BuiltInVoiceQuartz BuiltInVoice = "quartz"`

              - `const BuiltInVoiceRipple BuiltInVoice = "ripple"`

              - `const BuiltInVoiceSage BuiltInVoice = "sage"`

              - `const BuiltInVoiceShimmer BuiltInVoice = "shimmer"`

              - `const BuiltInVoiceStone BuiltInVoice = "stone"`

              - `const BuiltInVoiceTempo BuiltInVoice = "tempo"`

              - `const BuiltInVoiceVerse BuiltInVoice = "verse"`

              - `const BuiltInVoiceVesper BuiltInVoice = "vesper"`

              - `const BuiltInVoiceWillow BuiltInVoice = "willow"`

            - `type CustomVoice struct{…}`

              - `ID string`

      - `Client ClientConfig`

        Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

        - `DataChannel DataChannelConfig`

          Client and server event permissions for the WebRTC frontend data channel.

          - `AllowedClientEvents DataChannelConfigAllowedClientEventsUnion`

            Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

            - `All`

              - `const AllAll All = "all"`

            - `[]string`

          - `AllowedServerEvents DataChannelConfigAllowedServerEventsUnion`

            Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

            - `All`

              - `const AllAll All = "all"`

            - `[]ServerEventSelector`

              - `Type string`

                The outer Live server event type. Use 'response.event' for Responses events.

              - `ResponseEvent string`

                The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

      - `Delegation SessionConfigDelegationUnion`

        Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

        - `type ClientDelegation struct{…}`

          Delegate tasks to your application. The Live session emits delegation events that your backend handles.

          - `Type Client`

            The delegation owner. Always `client` for tasks handled by your application.

            - `const ClientClient Client = "client"`

        - `SessionConfigDelegationResponses`

          - `Responses ResponsesDelegationConfig`

            Backend model, prompt, and tools used when the Live session delegates a task to Responses.

            - `Model string`

              The model used for server-owned Responses delegations.

            - `Instructions string`

              Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

            - `MaxOutputTokens int64`

              Maximum number of output tokens for each delegated response.

            - `ParallelToolCalls bool`

              Whether the delegated Responses model may request multiple tool calls in a single response.

            - `Reasoning ResponsesDelegationConfigReasoning`

              Reasoning settings passed to each delegated Responses request.

              - `Effort string`

                How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

                - `const ResponsesDelegationConfigReasoningEffortNone ResponsesDelegationConfigReasoningEffort = "none"`

                - `const ResponsesDelegationConfigReasoningEffortMinimal ResponsesDelegationConfigReasoningEffort = "minimal"`

                - `const ResponsesDelegationConfigReasoningEffortLow ResponsesDelegationConfigReasoningEffort = "low"`

                - `const ResponsesDelegationConfigReasoningEffortMedium ResponsesDelegationConfigReasoningEffort = "medium"`

                - `const ResponsesDelegationConfigReasoningEffortHigh ResponsesDelegationConfigReasoningEffort = "high"`

                - `const ResponsesDelegationConfigReasoningEffortXhigh ResponsesDelegationConfigReasoningEffort = "xhigh"`

              - `Summary string`

                The reasoning summary to request from the delegated Responses model, when supported.

                - `const ResponsesDelegationConfigReasoningSummaryConcise ResponsesDelegationConfigReasoningSummary = "concise"`

                - `const ResponsesDelegationConfigReasoningSummaryDetailed ResponsesDelegationConfigReasoningSummary = "detailed"`

                - `const ResponsesDelegationConfigReasoningSummaryAuto ResponsesDelegationConfigReasoningSummary = "auto"`

            - `ServiceTier ResponsesDelegationConfigServiceTier`

              Service tier for delegated Responses requests.

              - `const ResponsesDelegationConfigServiceTierAuto ResponsesDelegationConfigServiceTier = "auto"`

              - `const ResponsesDelegationConfigServiceTierDefault ResponsesDelegationConfigServiceTier = "default"`

              - `const ResponsesDelegationConfigServiceTierFastTierTempPilot ResponsesDelegationConfigServiceTier = "fast_tier_temp_pilot"`

              - `const ResponsesDelegationConfigServiceTierFlex ResponsesDelegationConfigServiceTier = "flex"`

              - `const ResponsesDelegationConfigServiceTierPriority ResponsesDelegationConfigServiceTier = "priority"`

              - `const ResponsesDelegationConfigServiceTierUltrafast ResponsesDelegationConfigServiceTier = "ultrafast"`

            - `Text ResponsesDelegationConfigText`

              Text generation settings passed to each delegated Responses request.

              - `Verbosity string`

                The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

                - `const ResponsesDelegationConfigTextVerbosityLow ResponsesDelegationConfigTextVerbosity = "low"`

                - `const ResponsesDelegationConfigTextVerbosityMedium ResponsesDelegationConfigTextVerbosity = "medium"`

                - `const ResponsesDelegationConfigTextVerbosityHigh ResponsesDelegationConfigTextVerbosity = "high"`

            - `ToolChoice ResponsesDelegationConfigToolChoiceUnion`

              Controls which tool the Responses backend uses when handling a task delegated by the Live model.

              - `string`

                - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "auto"`

                - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "none"`

                - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "required"`

              - `ResponsesDelegationConfigToolChoiceLiveFunctionToolChoiceParam`

                - `Name string`

                - `Type Function`

                  - `const FunctionFunction Function = "function"`

              - `ResponsesDelegationConfigToolChoiceLiveMcpToolChoiceParam`

                - `Name string`

                - `ServerLabel string`

                - `Type Mcp`

                  - `const McpMcp Mcp = "mcp"`

            - `Tools []ResponsesDelegationConfigToolUnion`

              Tools available to the Responses backend while it handles tasks delegated by the Live model.

              - `type FunctionTool struct{…}`

                A function tool available to the Responses backend when the Live model delegates a task.

                - `Name string`

                  The name the delegated Responses model uses when calling this function.

                - `Type Function`

                  The tool type. Always `function`.

                  - `const FunctionFunction Function = "function"`

                - `Description string`

                  What the function does and when the delegated Responses model should call it.

                - `Parameters map[string, any]`

                  A JSON Schema object describing the arguments accepted by the function.

                - `Strict bool`

                  Whether the delegated Responses model must follow the function’s parameter schema exactly.

              - `ResponsesDelegationConfigToolWebSearch`

                - `Type WebSearch`

                  The tool type. Always `web_search`.

                  - `const WebSearchWebSearch WebSearch = "web_search"`

          - `Type Responses`

            The delegation owner. Always `responses` for tasks handled by the Responses API.

            - `const ResponsesResponses Responses = "responses"`

      - `Input []InitialItemUnion`

        Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

        - `InitialItemDeveloper`

          - `Content []InitialItemDeveloperContent`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `Text string`

              The message text to include in the Live session’s initial conversation history.

            - `Type string`

              The text content type. Always `input_text`.

              - `const InitialItemDeveloperContentTypeInputText InitialItemDeveloperContentType = "input_text"`

          - `Role Developer`

            The author of this history message. Always `developer`.

            - `const DeveloperDeveloper Developer = "developer"`

          - `ID string`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Status string`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `const InitialItemDeveloperStatusIncomplete InitialItemDeveloperStatus = "incomplete"`

            - `const InitialItemDeveloperStatusCompleted InitialItemDeveloperStatus = "completed"`

          - `Type string`

            The history item type. Always `message`.

            - `const InitialItemDeveloperTypeMessage InitialItemDeveloperType = "message"`

        - `InitialItemUser`

          - `Content []InitialItemUserContent`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `Text string`

              The message text to include in the Live session’s initial conversation history.

            - `Type string`

              The text content type. Always `input_text`.

              - `const InitialItemUserContentTypeInputText InitialItemUserContentType = "input_text"`

          - `Role User`

            The author of this history message. Always `user`.

            - `const UserUser User = "user"`

          - `ID string`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Status string`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `const InitialItemUserStatusIncomplete InitialItemUserStatus = "incomplete"`

            - `const InitialItemUserStatusCompleted InitialItemUserStatus = "completed"`

          - `Type string`

            The history item type. Always `message`.

            - `const InitialItemUserTypeMessage InitialItemUserType = "message"`

        - `InitialItemAssistant`

          - `Content []InitialItemAssistantContentUnion`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `InitialItemAssistantContentText`

              - `Text string`

                The message text to include in the Live session’s initial conversation history.

              - `Type string`

                The text content type. Always `text`.

                - `const InitialItemAssistantContentTextTypeText InitialItemAssistantContentTextType = "text"`

            - `InitialItemAssistantContentOutputText`

              - `Text string`

                The message text to include in the Live session’s initial conversation history.

              - `Type OutputText`

                The text content type. Always `output_text`.

                - `const OutputTextOutputText OutputText = "output_text"`

          - `Role Assistant`

            The author of this history message. Always `assistant`.

            - `const AssistantAssistant Assistant = "assistant"`

          - `ID string`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Status string`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `const InitialItemAssistantStatusIncomplete InitialItemAssistantStatus = "incomplete"`

            - `const InitialItemAssistantStatusCompleted InitialItemAssistantStatus = "completed"`

          - `Type string`

            The history item type. Always `message`.

            - `const InitialItemAssistantTypeMessage InitialItemAssistantType = "message"`

      - `Instructions string`

        Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

      - `Store bool`

        Whether to store the session for later forking and recording download. Defaults to false for new sessions.

    - `Type SessionStart`

      The Live client event type. Always `session.start`.

      - `const SessionStartSessionStart SessionStart = "session.start"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type SessionUpdateEvent struct{…}`

    Update the delegation settings of an active Live session. The server acknowledges accepted changes with `session.updated`.

    - `Session SessionUpdateConfig`

      Sparse delegation updates. Omitted settings retain their values. The delegation type cannot change, including resetting Responses delegation to null or client. Model, frontend instructions, audio, and startup input are immutable.

      - `Delegation SessionUpdateConfigDelegationUnion`

        Delegation settings to update. The delegation type must match the current session; omitted settings retain their values.

        - `type ClientDelegation struct{…}`

          Delegate tasks to your application. The Live session emits delegation events that your backend handles.

        - `SessionUpdateConfigDelegationResponses`

          - `Type Responses`

            The delegation owner. Always `responses` for tasks handled by the Responses API.

            - `const ResponsesResponses Responses = "responses"`

          - `Responses ResponsesDelegationUpdateConfig`

            Responses backend settings to update. Omitted settings keep their existing values.

            - `Instructions string`

              Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

            - `MaxOutputTokens int64`

              Maximum number of output tokens for each delegated response.

            - `Model string`

              The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.

            - `ParallelToolCalls bool`

              Whether the delegated Responses model may request multiple tool calls in a single response.

            - `Reasoning ResponsesDelegationUpdateConfigReasoning`

              Reasoning settings passed to each delegated Responses request.

              - `Effort string`

                How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

                - `const ResponsesDelegationUpdateConfigReasoningEffortNone ResponsesDelegationUpdateConfigReasoningEffort = "none"`

                - `const ResponsesDelegationUpdateConfigReasoningEffortMinimal ResponsesDelegationUpdateConfigReasoningEffort = "minimal"`

                - `const ResponsesDelegationUpdateConfigReasoningEffortLow ResponsesDelegationUpdateConfigReasoningEffort = "low"`

                - `const ResponsesDelegationUpdateConfigReasoningEffortMedium ResponsesDelegationUpdateConfigReasoningEffort = "medium"`

                - `const ResponsesDelegationUpdateConfigReasoningEffortHigh ResponsesDelegationUpdateConfigReasoningEffort = "high"`

                - `const ResponsesDelegationUpdateConfigReasoningEffortXhigh ResponsesDelegationUpdateConfigReasoningEffort = "xhigh"`

              - `Summary string`

                The reasoning summary to request from the delegated Responses model, when supported.

                - `const ResponsesDelegationUpdateConfigReasoningSummaryConcise ResponsesDelegationUpdateConfigReasoningSummary = "concise"`

                - `const ResponsesDelegationUpdateConfigReasoningSummaryDetailed ResponsesDelegationUpdateConfigReasoningSummary = "detailed"`

                - `const ResponsesDelegationUpdateConfigReasoningSummaryAuto ResponsesDelegationUpdateConfigReasoningSummary = "auto"`

            - `ServiceTier ResponsesDelegationUpdateConfigServiceTier`

              Service tier for delegated Responses requests.

              - `const ResponsesDelegationUpdateConfigServiceTierAuto ResponsesDelegationUpdateConfigServiceTier = "auto"`

              - `const ResponsesDelegationUpdateConfigServiceTierDefault ResponsesDelegationUpdateConfigServiceTier = "default"`

              - `const ResponsesDelegationUpdateConfigServiceTierFastTierTempPilot ResponsesDelegationUpdateConfigServiceTier = "fast_tier_temp_pilot"`

              - `const ResponsesDelegationUpdateConfigServiceTierFlex ResponsesDelegationUpdateConfigServiceTier = "flex"`

              - `const ResponsesDelegationUpdateConfigServiceTierPriority ResponsesDelegationUpdateConfigServiceTier = "priority"`

              - `const ResponsesDelegationUpdateConfigServiceTierUltrafast ResponsesDelegationUpdateConfigServiceTier = "ultrafast"`

            - `Text ResponsesDelegationUpdateConfigText`

              Text generation settings passed to each delegated Responses request.

              - `Verbosity string`

                The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

                - `const ResponsesDelegationUpdateConfigTextVerbosityLow ResponsesDelegationUpdateConfigTextVerbosity = "low"`

                - `const ResponsesDelegationUpdateConfigTextVerbosityMedium ResponsesDelegationUpdateConfigTextVerbosity = "medium"`

                - `const ResponsesDelegationUpdateConfigTextVerbosityHigh ResponsesDelegationUpdateConfigTextVerbosity = "high"`

            - `ToolChoice ResponsesDelegationUpdateConfigToolChoiceUnion`

              Controls which tool the Responses backend uses when handling a task delegated by the Live model.

              - `string`

                - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "auto"`

                - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "none"`

                - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "required"`

              - `ResponsesDelegationUpdateConfigToolChoiceLiveFunctionToolChoiceParam`

                - `Name string`

                - `Type Function`

                  - `const FunctionFunction Function = "function"`

              - `ResponsesDelegationUpdateConfigToolChoiceLiveMcpToolChoiceParam`

                - `Name string`

                - `ServerLabel string`

                - `Type Mcp`

                  - `const McpMcp Mcp = "mcp"`

            - `Tools []ResponsesDelegationUpdateConfigToolUnion`

              Tools available to the Responses backend while it handles tasks delegated by the Live model.

              - `type FunctionTool struct{…}`

                A function tool available to the Responses backend when the Live model delegates a task.

              - `ResponsesDelegationUpdateConfigToolWebSearch`

                - `Type WebSearch`

                  The tool type. Always `web_search`.

                  - `const WebSearchWebSearch WebSearch = "web_search"`

    - `Type SessionUpdate`

      The Live client event type. Always `session.update`.

      - `const SessionUpdateSessionUpdate SessionUpdate = "session.update"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type InputAudioAppendEvent struct{…}`

    Send audio to a Live session over its primary WebSocket. WebRTC and SIP sessions send audio over their media transport.

    - `Audio string`

      Base64-encoded raw audio in the startup-selected format, without a WAV or other container header. Primary WebSocket only; media transports use their audio track. Audio appends have no acknowledgment. Reflected sideband server events reuse this event type and audio key, with no timestamps or event_id; their audio is always mono PCM16LE at 24 kHz.

    - `Type SessionInputAudioAppend`

      The Live client event type. Always `session.input_audio.append`.

      - `const SessionInputAudioAppendSessionInputAudioAppend SessionInputAudioAppend = "session.input_audio.append"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type InputAudioMuteEvent struct{…}`

    Mute audio input to the Live model without closing the session. The server acknowledges with `session.input_audio.muted`.

    - `Type SessionInputAudioMute`

      The Live client event type. Always `session.input_audio.mute`.

      - `const SessionInputAudioMuteSessionInputAudioMute SessionInputAudioMute = "session.input_audio.mute"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type InputAudioUnmuteEvent struct{…}`

    Resume audio input to a Live model after muting it. The server acknowledges with `session.input_audio.unmuted`.

    - `Type SessionInputAudioUnmute`

      The Live client event type. Always `session.input_audio.unmute`.

      - `const SessionInputAudioUnmuteSessionInputAudioUnmute SessionInputAudioUnmute = "session.input_audio.unmute"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type InstructionsAppendEvent struct{…}`

    Append instructions to the Live conversation while it is running, optionally associating them with an existing client delegation.

    - `Content string`

      Instruction text to append, limited to 500 tokens. This is a plain string, not an array of content parts.

    - `DelegationID string`

      Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

    - `Type SessionInstructionsAppend`

      The Live client event type. Always `session.instructions.append`.

      - `const SessionInstructionsAppendSessionInstructionsAppend SessionInstructionsAppend = "session.instructions.append"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type ThinkingAppendEvent struct{…}`

    Provide silent reasoning or progress context to the Live model, optionally for an existing client delegation.

    - `Content string`

      Silent reasoning or progress context, limited to 500 tokens. It does not directly request speech, but can influence later speech and is not a secrecy boundary.

    - `DelegationID string`

      Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

    - `Type SessionThinkingAppend`

      The Live client event type. Always `session.thinking.append`.

      - `const SessionThinkingAppendSessionThinkingAppend SessionThinkingAppend = "session.thinking.append"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type CommentaryAppendEvent struct{…}`

    Provide context the Live model can communicate to the user, optionally for an existing client delegation.

    - `Content string`

      Speakable context for the Live model, limited to 500 tokens. Use this for a result the model should communicate; use session.thinking.append for silent context.

    - `DelegationID string`

      Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

    - `Type SessionCommentaryAppend`

      The Live client event type. Always `session.commentary.append`.

      - `const SessionCommentaryAppendSessionCommentaryAppend SessionCommentaryAppend = "session.commentary.append"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type ResponseItemCreateEvent struct{…}`

    Add an input item to the Live session’s Responses backend. Requires Responses delegation; use `response.create` to request a response.

    - `Item ResponseInputItemUnion`

      An input item to append to the Responses backend conversation, such as a user message or a function tool result.

      - `type EasyInputMessage struct{…}`

        A message input to the model with a role indicating instruction following
        hierarchy. Instructions given with the `developer` or `system` role take
        precedence over instructions given with the `user` role. Messages with the
        `assistant` role are presumed to have been generated by the model in previous
        interactions.

        - `Content EasyInputMessageContentUnion`

          Text, image, or audio input to the model, used to generate a response.
          Can also contain previous assistant responses.

          - `string`

          - `type ResponseInputMessageContentList []ResponseInputContentUnion`

            A list of one or many input items to the model, containing different content
            types.

            - `type ResponseInputText struct{…}`

              A text input to the model.

              - `Text string`

                The text input to the model.

              - `Type InputText`

                The type of the input item. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

              - `PromptCacheBreakpoint ResponseInputTextPromptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `Mode Explicit`

                  The breakpoint mode. Always `explicit`.

                  - `const ExplicitExplicit Explicit = "explicit"`

            - `type ResponseInputImage struct{…}`

              An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

              - `Detail ResponseInputImageDetail`

                The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                - `const ResponseInputImageDetailLow ResponseInputImageDetail = "low"`

                - `const ResponseInputImageDetailHigh ResponseInputImageDetail = "high"`

                - `const ResponseInputImageDetailAuto ResponseInputImageDetail = "auto"`

                - `const ResponseInputImageDetailOriginal ResponseInputImageDetail = "original"`

              - `Type InputImage`

                The type of the input item. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

              - `FileID string`

                The ID of the file to be sent to the model.

              - `ImageURL string`

                The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

              - `PromptCacheBreakpoint ResponseInputImagePromptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `Mode Explicit`

                  The breakpoint mode. Always `explicit`.

                  - `const ExplicitExplicit Explicit = "explicit"`

            - `type ResponseInputFile struct{…}`

              A file input to the model.

              - `Type InputFile`

                The type of the input item. Always `input_file`.

                - `const InputFileInputFile InputFile = "input_file"`

              - `Detail ResponseInputFileDetail`

                The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

                - `const ResponseInputFileDetailAuto ResponseInputFileDetail = "auto"`

                - `const ResponseInputFileDetailLow ResponseInputFileDetail = "low"`

                - `const ResponseInputFileDetailHigh ResponseInputFileDetail = "high"`

              - `FileData string`

                The content of the file to be sent to the model.

              - `FileID string`

                The ID of the file to be sent to the model.

              - `FileURL string`

                The URL of the file to be sent to the model.

              - `Filename string`

                The name of the file to be sent to the model.

              - `PromptCacheBreakpoint ResponseInputFilePromptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `Mode Explicit`

                  The breakpoint mode. Always `explicit`.

                  - `const ExplicitExplicit Explicit = "explicit"`

        - `Role EasyInputMessageRole`

          The role of the message input. One of `user`, `assistant`, `system`, or
          `developer`.

          - `const EasyInputMessageRoleUser EasyInputMessageRole = "user"`

          - `const EasyInputMessageRoleAssistant EasyInputMessageRole = "assistant"`

          - `const EasyInputMessageRoleSystem EasyInputMessageRole = "system"`

          - `const EasyInputMessageRoleDeveloper EasyInputMessageRole = "developer"`

        - `Phase EasyInputMessagePhase`

          Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
          For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
          phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

          - `const EasyInputMessagePhaseCommentary EasyInputMessagePhase = "commentary"`

          - `const EasyInputMessagePhaseFinalAnswer EasyInputMessagePhase = "final_answer"`

        - `Type EasyInputMessageType`

          The type of the message input. Always `message`.

          - `const EasyInputMessageTypeMessage EasyInputMessageType = "message"`

      - `type ResponseInputItemMessage struct{…}`

        A message input to the model with a role indicating instruction following
        hierarchy. Instructions given with the `developer` or `system` role take
        precedence over instructions given with the `user` role.

        - `Content ResponseInputMessageContentList`

          A list of one or many input items to the model, containing different content
          types.

        - `Role string`

          The role of the message input. One of `user`, `system`, or `developer`.

          - `const ResponseInputItemMessageRoleUser ResponseInputItemMessageRole = "user"`

          - `const ResponseInputItemMessageRoleSystem ResponseInputItemMessageRole = "system"`

          - `const ResponseInputItemMessageRoleDeveloper ResponseInputItemMessageRole = "developer"`

        - `Status string`

          The status of item. One of `in_progress`, `completed`, or
          `incomplete`. Populated when items are returned via API.

          - `const ResponseInputItemMessageStatusInProgress ResponseInputItemMessageStatus = "in_progress"`

          - `const ResponseInputItemMessageStatusCompleted ResponseInputItemMessageStatus = "completed"`

          - `const ResponseInputItemMessageStatusIncomplete ResponseInputItemMessageStatus = "incomplete"`

        - `Type string`

          The type of the message input. Always set to `message`.

          - `const ResponseInputItemMessageTypeMessage ResponseInputItemMessageType = "message"`

      - `type ResponseOutputMessage struct{…}`

        An output message from the model.

        - `ID string`

          The unique ID of the output message.

        - `Content []ResponseOutputMessageContentUnion`

          The content of the output message.

          - `type ResponseOutputText struct{…}`

            A text output from the model.

            - `Annotations []ResponseOutputTextAnnotationUnion`

              The annotations of the text output.

              - `type ResponseOutputTextAnnotationFileCitation struct{…}`

                A citation to a file.

                - `FileID string`

                  The ID of the file.

                - `Filename string`

                  The filename of the file cited.

                - `Index int64`

                  The index in the output text at which to insert the file citation.

                - `Type FileCitation`

                  The type of the file citation. Always `file_citation`.

                  - `const FileCitationFileCitation FileCitation = "file_citation"`

              - `type ResponseOutputTextAnnotationURLCitation struct{…}`

                A citation for a web resource used to generate a model response.

                - `EndIndex int64`

                  The index of the last character of the URL citation in the message.

                - `StartIndex int64`

                  The index of the first character of the URL citation in the message.

                - `Title string`

                  The title of the web resource.

                - `Type URLCitation`

                  The type of the URL citation. Always `url_citation`.

                  - `const URLCitationURLCitation URLCitation = "url_citation"`

                - `URL string`

                  The URL of the web resource.

              - `type ResponseOutputTextAnnotationContainerFileCitation struct{…}`

                A citation for a container file used to generate a model response.

                - `ContainerID string`

                  The ID of the container file.

                - `EndIndex int64`

                  The index of the last character of the container file citation in the message.

                - `FileID string`

                  The ID of the file.

                - `Filename string`

                  The filename of the container file cited.

                - `StartIndex int64`

                  The index of the first character of the container file citation in the message.

                - `Type ContainerFileCitation`

                  The type of the container file citation. Always `container_file_citation`.

                  - `const ContainerFileCitationContainerFileCitation ContainerFileCitation = "container_file_citation"`

              - `type ResponseOutputTextAnnotationFilePath struct{…}`

                A path to a file.

                - `FileID string`

                  The ID of the file.

                - `Index int64`

                  The index of the file in the list of files.

                - `Type FilePath`

                  The type of the file path. Always `file_path`.

                  - `const FilePathFilePath FilePath = "file_path"`

            - `Text string`

              The text output from the model.

            - `Type OutputText`

              The type of the output text. Always `output_text`.

              - `const OutputTextOutputText OutputText = "output_text"`

            - `Logprobs []ResponseOutputTextLogprob`

              - `Token string`

              - `Bytes []int64`

              - `Logprob float64`

              - `TopLogprobs []ResponseOutputTextLogprobTopLogprob`

                - `Token string`

                - `Bytes []int64`

                - `Logprob float64`

          - `type ResponseOutputRefusal struct{…}`

            A refusal from the model.

            - `Refusal string`

              The refusal explanation from the model.

            - `Type Refusal`

              The type of the refusal. Always `refusal`.

              - `const RefusalRefusal Refusal = "refusal"`

        - `Role Assistant`

          The role of the output message. Always `assistant`.

          - `const AssistantAssistant Assistant = "assistant"`

        - `Status ResponseOutputMessageStatus`

          The status of the message input. One of `in_progress`, `completed`, or
          `incomplete`. Populated when input items are returned via API.

          - `const ResponseOutputMessageStatusInProgress ResponseOutputMessageStatus = "in_progress"`

          - `const ResponseOutputMessageStatusCompleted ResponseOutputMessageStatus = "completed"`

          - `const ResponseOutputMessageStatusIncomplete ResponseOutputMessageStatus = "incomplete"`

        - `Type Message`

          The type of the output message. Always `message`.

          - `const MessageMessage Message = "message"`

        - `Phase ResponseOutputMessagePhase`

          Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
          For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
          phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

          - `const ResponseOutputMessagePhaseCommentary ResponseOutputMessagePhase = "commentary"`

          - `const ResponseOutputMessagePhaseFinalAnswer ResponseOutputMessagePhase = "final_answer"`

      - `type ResponseFileSearchToolCall struct{…}`

        The results of a file search tool call. See the
        [file search guide](/api/docs/guides/tools-file-search) for more information.

        - `ID string`

          The unique ID of the file search tool call.

        - `Queries []string`

          The queries used to search for files.

        - `Status ResponseFileSearchToolCallStatus`

          The status of the file search tool call. One of `in_progress`,
          `searching`, `incomplete` or `failed`,

          - `const ResponseFileSearchToolCallStatusInProgress ResponseFileSearchToolCallStatus = "in_progress"`

          - `const ResponseFileSearchToolCallStatusSearching ResponseFileSearchToolCallStatus = "searching"`

          - `const ResponseFileSearchToolCallStatusCompleted ResponseFileSearchToolCallStatus = "completed"`

          - `const ResponseFileSearchToolCallStatusIncomplete ResponseFileSearchToolCallStatus = "incomplete"`

          - `const ResponseFileSearchToolCallStatusFailed ResponseFileSearchToolCallStatus = "failed"`

        - `Type FileSearchCall`

          The type of the file search tool call. Always `file_search_call`.

          - `const FileSearchCallFileSearchCall FileSearchCall = "file_search_call"`

        - `Results []ResponseFileSearchToolCallResult`

          The results of the file search tool call.

          - `Attributes map[string, ResponseFileSearchToolCallResultAttributeUnion]`

            Set of 16 key-value pairs that can be attached to an object. This can be
            useful for storing additional information about the object in a structured
            format, and querying for objects via API or the dashboard. Keys are strings
            with a maximum length of 64 characters. Values are strings with a maximum
            length of 512 characters, booleans, or numbers.

            - `string`

            - `float64`

            - `bool`

          - `FileID string`

            The unique ID of the file.

          - `Filename string`

            The name of the file.

          - `Score float64`

            The relevance score of the file - a value between 0 and 1.

          - `Text string`

            The text that was retrieved from the file.

      - `type ResponseComputerToolCall struct{…}`

        A tool call to a computer use tool. See the
        [computer use guide](/api/docs/guides/tools-computer-use) for more information.

        - `ID string`

          The unique ID of the computer call.

        - `CallID string`

          An identifier used when responding to the tool call with output.

        - `PendingSafetyChecks []ResponseComputerToolCallPendingSafetyCheck`

          The pending safety checks for the computer call.

          - `ID string`

            The ID of the pending safety check.

          - `Code string`

            The type of the pending safety check.

          - `Message string`

            Details about the pending safety check.

        - `Status ResponseComputerToolCallStatus`

          The status of the item. One of `in_progress`, `completed`, or
          `incomplete`. Populated when items are returned via API.

          - `const ResponseComputerToolCallStatusInProgress ResponseComputerToolCallStatus = "in_progress"`

          - `const ResponseComputerToolCallStatusCompleted ResponseComputerToolCallStatus = "completed"`

          - `const ResponseComputerToolCallStatusIncomplete ResponseComputerToolCallStatus = "incomplete"`

        - `Type ResponseComputerToolCallType`

          The type of the computer call. Always `computer_call`.

          - `const ResponseComputerToolCallTypeComputerCall ResponseComputerToolCallType = "computer_call"`

        - `Action ResponseComputerToolCallActionUnion`

          A click action.

          - `type ResponseComputerToolCallActionClick struct{…}`

            A click action.

            - `Button string`

              Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

              - `const ResponseComputerToolCallActionClickButtonLeft ResponseComputerToolCallActionClickButton = "left"`

              - `const ResponseComputerToolCallActionClickButtonRight ResponseComputerToolCallActionClickButton = "right"`

              - `const ResponseComputerToolCallActionClickButtonWheel ResponseComputerToolCallActionClickButton = "wheel"`

              - `const ResponseComputerToolCallActionClickButtonBack ResponseComputerToolCallActionClickButton = "back"`

              - `const ResponseComputerToolCallActionClickButtonForward ResponseComputerToolCallActionClickButton = "forward"`

            - `Type Click`

              Specifies the event type. For a click action, this property is always `click`.

              - `const ClickClick Click = "click"`

            - `X int64`

              The x-coordinate where the click occurred.

            - `Y int64`

              The y-coordinate where the click occurred.

            - `Keys []string`

              The keys being held while clicking.

          - `type ResponseComputerToolCallActionDoubleClick struct{…}`

            A double click action.

            - `Keys []string`

              The keys being held while double-clicking.

            - `Type DoubleClick`

              Specifies the event type. For a double click action, this property is always set to `double_click`.

              - `const DoubleClickDoubleClick DoubleClick = "double_click"`

            - `X int64`

              The x-coordinate where the double click occurred.

            - `Y int64`

              The y-coordinate where the double click occurred.

          - `type ResponseComputerToolCallActionDrag struct{…}`

            A drag action.

            - `Path []ResponseComputerToolCallActionDragPath`

              An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

              ```
              [
                { x: 100, y: 200 },
                { x: 200, y: 300 }
              ]
              ```

              - `X int64`

                The x-coordinate.

              - `Y int64`

                The y-coordinate.

            - `Type Drag`

              Specifies the event type. For a drag action, this property is always set to `drag`.

              - `const DragDrag Drag = "drag"`

            - `Keys []string`

              The keys being held while dragging the mouse.

          - `type ResponseComputerToolCallActionKeypress struct{…}`

            A collection of keypresses the model would like to perform.

            - `Keys []string`

              The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

            - `Type Keypress`

              Specifies the event type. For a keypress action, this property is always set to `keypress`.

              - `const KeypressKeypress Keypress = "keypress"`

          - `type ResponseComputerToolCallActionMove struct{…}`

            A mouse move action.

            - `Type Move`

              Specifies the event type. For a move action, this property is always set to `move`.

              - `const MoveMove Move = "move"`

            - `X int64`

              The x-coordinate to move to.

            - `Y int64`

              The y-coordinate to move to.

            - `Keys []string`

              The keys being held while moving the mouse.

          - `type ResponseComputerToolCallActionScreenshot struct{…}`

            A screenshot action.

            - `Type Screenshot`

              Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

              - `const ScreenshotScreenshot Screenshot = "screenshot"`

          - `type ResponseComputerToolCallActionScroll struct{…}`

            A scroll action.

            - `ScrollX int64`

              The horizontal scroll distance.

            - `ScrollY int64`

              The vertical scroll distance.

            - `Type Scroll`

              Specifies the event type. For a scroll action, this property is always set to `scroll`.

              - `const ScrollScroll Scroll = "scroll"`

            - `X int64`

              The x-coordinate where the scroll occurred.

            - `Y int64`

              The y-coordinate where the scroll occurred.

            - `Keys []string`

              The keys being held while scrolling.

          - `type ResponseComputerToolCallActionType struct{…}`

            An action to type in text.

            - `Text string`

              The text to type.

            - `Type Type`

              Specifies the event type. For a type action, this property is always set to `type`.

              - `const TypeType Type = "type"`

          - `type ResponseComputerToolCallActionWait struct{…}`

            A wait action.

            - `Type Wait`

              Specifies the event type. For a wait action, this property is always set to `wait`.

              - `const WaitWait Wait = "wait"`

        - `Actions ComputerActionList`

          Flattened batched actions for `computer_use`. Each action includes an
          `type` discriminator and action-specific fields.

          - `type ComputerActionClick struct{…}`

            A click action.

            - `Button string`

              Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

              - `const ComputerActionClickButtonLeft ComputerActionClickButton = "left"`

              - `const ComputerActionClickButtonRight ComputerActionClickButton = "right"`

              - `const ComputerActionClickButtonWheel ComputerActionClickButton = "wheel"`

              - `const ComputerActionClickButtonBack ComputerActionClickButton = "back"`

              - `const ComputerActionClickButtonForward ComputerActionClickButton = "forward"`

            - `Type Click`

              Specifies the event type. For a click action, this property is always `click`.

              - `const ClickClick Click = "click"`

            - `X int64`

              The x-coordinate where the click occurred.

            - `Y int64`

              The y-coordinate where the click occurred.

            - `Keys []string`

              The keys being held while clicking.

          - `type ComputerActionDoubleClick struct{…}`

            A double click action.

            - `Keys []string`

              The keys being held while double-clicking.

            - `Type DoubleClick`

              Specifies the event type. For a double click action, this property is always set to `double_click`.

              - `const DoubleClickDoubleClick DoubleClick = "double_click"`

            - `X int64`

              The x-coordinate where the double click occurred.

            - `Y int64`

              The y-coordinate where the double click occurred.

          - `type ComputerActionDrag struct{…}`

            A drag action.

            - `Path []ComputerActionDragPath`

              An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

              ```
              [
                { x: 100, y: 200 },
                { x: 200, y: 300 }
              ]
              ```

              - `X int64`

                The x-coordinate.

              - `Y int64`

                The y-coordinate.

            - `Type Drag`

              Specifies the event type. For a drag action, this property is always set to `drag`.

              - `const DragDrag Drag = "drag"`

            - `Keys []string`

              The keys being held while dragging the mouse.

          - `type ComputerActionKeypress struct{…}`

            A collection of keypresses the model would like to perform.

            - `Keys []string`

              The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

            - `Type Keypress`

              Specifies the event type. For a keypress action, this property is always set to `keypress`.

              - `const KeypressKeypress Keypress = "keypress"`

          - `type ComputerActionMove struct{…}`

            A mouse move action.

            - `Type Move`

              Specifies the event type. For a move action, this property is always set to `move`.

              - `const MoveMove Move = "move"`

            - `X int64`

              The x-coordinate to move to.

            - `Y int64`

              The y-coordinate to move to.

            - `Keys []string`

              The keys being held while moving the mouse.

          - `type ComputerActionScreenshot struct{…}`

            A screenshot action.

            - `Type Screenshot`

              Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

              - `const ScreenshotScreenshot Screenshot = "screenshot"`

          - `type ComputerActionScroll struct{…}`

            A scroll action.

            - `ScrollX int64`

              The horizontal scroll distance.

            - `ScrollY int64`

              The vertical scroll distance.

            - `Type Scroll`

              Specifies the event type. For a scroll action, this property is always set to `scroll`.

              - `const ScrollScroll Scroll = "scroll"`

            - `X int64`

              The x-coordinate where the scroll occurred.

            - `Y int64`

              The y-coordinate where the scroll occurred.

            - `Keys []string`

              The keys being held while scrolling.

          - `type ComputerActionType struct{…}`

            An action to type in text.

            - `Text string`

              The text to type.

            - `Type Type`

              Specifies the event type. For a type action, this property is always set to `type`.

              - `const TypeType Type = "type"`

          - `type ComputerActionWait struct{…}`

            A wait action.

            - `Type Wait`

              Specifies the event type. For a wait action, this property is always set to `wait`.

              - `const WaitWait Wait = "wait"`

      - `type ResponseInputItemComputerCallOutput struct{…}`

        The output of a computer tool call.

        - `CallID string`

          The ID of the computer tool call that produced the output.

        - `Output ResponseComputerToolCallOutputScreenshot`

          A computer screenshot image used with the computer use tool.

          - `Type ComputerScreenshot`

            Specifies the event type. For a computer screenshot, this property is
            always set to `computer_screenshot`.

            - `const ComputerScreenshotComputerScreenshot ComputerScreenshot = "computer_screenshot"`

          - `FileID string`

            The identifier of an uploaded file that contains the screenshot.

          - `ImageURL string`

            The URL of the screenshot image.

        - `Type ComputerCallOutput`

          The type of the computer tool call output. Always `computer_call_output`.

          - `const ComputerCallOutputComputerCallOutput ComputerCallOutput = "computer_call_output"`

        - `ID string`

          The ID of the computer tool call output.

        - `AcknowledgedSafetyChecks []ResponseInputItemComputerCallOutputAcknowledgedSafetyCheck`

          The safety checks reported by the API that have been acknowledged by the developer.

          - `ID string`

            The ID of the pending safety check.

          - `Code string`

            The type of the pending safety check.

          - `Message string`

            Details about the pending safety check.

        - `Status string`

          The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

          - `const ResponseInputItemComputerCallOutputStatusInProgress ResponseInputItemComputerCallOutputStatus = "in_progress"`

          - `const ResponseInputItemComputerCallOutputStatusCompleted ResponseInputItemComputerCallOutputStatus = "completed"`

          - `const ResponseInputItemComputerCallOutputStatusIncomplete ResponseInputItemComputerCallOutputStatus = "incomplete"`

      - `type ResponseFunctionWebSearch struct{…}`

        The results of a web search tool call. See the
        [web search guide](/api/docs/guides/tools-web-search) for more information.

        - `ID string`

          The unique ID of the web search tool call.

        - `Action ResponseFunctionWebSearchActionUnion`

          An object describing the specific action taken in this web search call.
          Includes details on how the model used the web (search, open_page, find_in_page).

          - `type ResponseFunctionWebSearchActionSearch struct{…}`

            Action type "search" - Performs a web search query.

            - `Type Search`

              The action type.

              - `const SearchSearch Search = "search"`

            - `Queries []string`

              The search queries.

            - `Query string`

              The search query.

            - `Sources []ResponseFunctionWebSearchActionSearchSource`

              The sources used in the search.

              - `Type URL`

                The type of source. Always `url`.

                - `const URLURL URL = "url"`

              - `URL string`

                The URL of the source.

          - `type ResponseFunctionWebSearchActionOpenPage struct{…}`

            Action type "open_page" - Opens a specific URL from search results.

            - `Type OpenPage`

              The action type.

              - `const OpenPageOpenPage OpenPage = "open_page"`

            - `URL string`

              The URL opened by the model.

          - `type ResponseFunctionWebSearchActionFindInPage struct{…}`

            Action type "find_in_page": Searches for a pattern within a loaded page.

            - `Pattern string`

              The pattern or text to search for within the page.

            - `Type FindInPage`

              The action type.

              - `const FindInPageFindInPage FindInPage = "find_in_page"`

            - `URL string`

              The URL of the page searched for the pattern.

        - `Status ResponseFunctionWebSearchStatus`

          The status of the web search tool call.

          - `const ResponseFunctionWebSearchStatusInProgress ResponseFunctionWebSearchStatus = "in_progress"`

          - `const ResponseFunctionWebSearchStatusSearching ResponseFunctionWebSearchStatus = "searching"`

          - `const ResponseFunctionWebSearchStatusCompleted ResponseFunctionWebSearchStatus = "completed"`

          - `const ResponseFunctionWebSearchStatusFailed ResponseFunctionWebSearchStatus = "failed"`

          - `const ResponseFunctionWebSearchStatusIncomplete ResponseFunctionWebSearchStatus = "incomplete"`

        - `Type WebSearchCall`

          The type of the web search tool call. Always `web_search_call`.

          - `const WebSearchCallWebSearchCall WebSearchCall = "web_search_call"`

      - `type ResponseFunctionToolCall struct{…}`

        A tool call to run a function. See the
        [function calling guide](/api/docs/guides/function-calling) for more information.

        - `Arguments string`

          A JSON string of the arguments to pass to the function.

        - `CallID string`

          The unique ID of the function tool call generated by the model.

        - `Name string`

          The name of the function to run.

        - `Type FunctionCall`

          The type of the function tool call. Always `function_call`.

          - `const FunctionCallFunctionCall FunctionCall = "function_call"`

        - `ID string`

          The unique ID of the function tool call.

        - `Async bool`

          Whether the function tool call runs asynchronously.

        - `Caller ResponseFunctionToolCallCallerUnion`

          The execution context that produced this tool call.

          - `type ResponseFunctionToolCallCallerDirect struct{…}`

            - `Type Direct`

              - `const DirectDirect Direct = "direct"`

          - `type ResponseFunctionToolCallCallerProgram struct{…}`

            - `CallerID string`

              The call ID of the program item that produced this tool call.

            - `Type Program`

              - `const ProgramProgram Program = "program"`

        - `Namespace string`

          The namespace of the function to run.

        - `Status ResponseFunctionToolCallStatus`

          The status of the item. One of `in_progress`, `completed`, or
          `incomplete`. Populated when items are returned via API.

          - `const ResponseFunctionToolCallStatusInProgress ResponseFunctionToolCallStatus = "in_progress"`

          - `const ResponseFunctionToolCallStatusCompleted ResponseFunctionToolCallStatus = "completed"`

          - `const ResponseFunctionToolCallStatusIncomplete ResponseFunctionToolCallStatus = "incomplete"`

      - `type ResponseInputItemFunctionCallOutput struct{…}`

        The output of a function tool call.

        - `Output ResponseInputItemFunctionCallOutputOutputUnion`

          Text, image, or file output of the function tool call.

          - `string`

          - `type ResponseFunctionCallOutputItemList []ResponseFunctionCallOutputItemUnion`

            An array of content outputs (text, image, file) for the function tool call.

            - `type ResponseInputTextContent struct{…}`

              A text input to the model.

              - `Text string`

                The text input to the model.

              - `Type InputText`

                The type of the input item. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

              - `PromptCacheBreakpoint ResponseInputTextContentPromptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `Mode Explicit`

                  The breakpoint mode. Always `explicit`.

                  - `const ExplicitExplicit Explicit = "explicit"`

            - `type ResponseInputImageContent struct{…}`

              An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision)

              - `Type InputImage`

                The type of the input item. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

              - `Detail ResponseInputImageContentDetail`

                The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                - `const ResponseInputImageContentDetailLow ResponseInputImageContentDetail = "low"`

                - `const ResponseInputImageContentDetailHigh ResponseInputImageContentDetail = "high"`

                - `const ResponseInputImageContentDetailAuto ResponseInputImageContentDetail = "auto"`

                - `const ResponseInputImageContentDetailOriginal ResponseInputImageContentDetail = "original"`

              - `FileID string`

                The ID of the file to be sent to the model.

              - `ImageURL string`

                The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

              - `PromptCacheBreakpoint ResponseInputImageContentPromptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `Mode Explicit`

                  The breakpoint mode. Always `explicit`.

                  - `const ExplicitExplicit Explicit = "explicit"`

            - `type ResponseInputFileContent struct{…}`

              A file input to the model.

              - `Type InputFile`

                The type of the input item. Always `input_file`.

                - `const InputFileInputFile InputFile = "input_file"`

              - `Detail ResponseInputFileContentDetail`

                The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

                - `const ResponseInputFileContentDetailAuto ResponseInputFileContentDetail = "auto"`

                - `const ResponseInputFileContentDetailLow ResponseInputFileContentDetail = "low"`

                - `const ResponseInputFileContentDetailHigh ResponseInputFileContentDetail = "high"`

              - `FileData string`

                The base64-encoded data of the file to be sent to the model.

              - `FileID string`

                The ID of the file to be sent to the model.

              - `FileURL string`

                The URL of the file to be sent to the model.

              - `Filename string`

                The name of the file to be sent to the model.

              - `PromptCacheBreakpoint ResponseInputFileContentPromptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `Mode Explicit`

                  The breakpoint mode. Always `explicit`.

                  - `const ExplicitExplicit Explicit = "explicit"`

        - `Type FunctionCallOutput`

          The type of the function tool call output. Always `function_call_output`.

          - `const FunctionCallOutputFunctionCallOutput FunctionCallOutput = "function_call_output"`

        - `ID string`

          The unique ID of the function tool call output. Populated when this item is returned via API.

        - `CallID string`

          The unique ID of the function tool call generated by the model.

        - `Caller ResponseInputItemFunctionCallOutputCallerUnion`

          The execution context that produced this tool call.

          - `type ResponseInputItemFunctionCallOutputCallerDirect struct{…}`

            - `Type Direct`

              The caller type. Always `direct`.

              - `const DirectDirect Direct = "direct"`

          - `type ResponseInputItemFunctionCallOutputCallerProgram struct{…}`

            - `CallerID string`

              The call ID of the program item that produced this tool call.

            - `Type Program`

              The caller type. Always `program`.

              - `const ProgramProgram Program = "program"`

        - `Name string`

          The name of the tool that produced the output.

        - `Namespace string`

          The namespace of the tool that produced the output.

        - `Status string`

          The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

          - `const ResponseInputItemFunctionCallOutputStatusInProgress ResponseInputItemFunctionCallOutputStatus = "in_progress"`

          - `const ResponseInputItemFunctionCallOutputStatusCompleted ResponseInputItemFunctionCallOutputStatus = "completed"`

          - `const ResponseInputItemFunctionCallOutputStatusIncomplete ResponseInputItemFunctionCallOutputStatus = "incomplete"`

      - `type ResponseInputItemToolSearchCall struct{…}`

        - `Arguments any`

          The arguments supplied to the tool search call.

        - `Type ToolSearchCall`

          The item type. Always `tool_search_call`.

          - `const ToolSearchCallToolSearchCall ToolSearchCall = "tool_search_call"`

        - `ID string`

          The unique ID of this tool search call.

        - `CallID string`

          The unique ID of the tool search call generated by the model.

        - `Execution string`

          Whether tool search was executed by the server or by the client.

          - `const ResponseInputItemToolSearchCallExecutionServer ResponseInputItemToolSearchCallExecution = "server"`

          - `const ResponseInputItemToolSearchCallExecutionClient ResponseInputItemToolSearchCallExecution = "client"`

        - `Status string`

          The status of the tool search call.

          - `const ResponseInputItemToolSearchCallStatusInProgress ResponseInputItemToolSearchCallStatus = "in_progress"`

          - `const ResponseInputItemToolSearchCallStatusCompleted ResponseInputItemToolSearchCallStatus = "completed"`

          - `const ResponseInputItemToolSearchCallStatusIncomplete ResponseInputItemToolSearchCallStatus = "incomplete"`

      - `type ResponseToolSearchOutputItemParamResp struct{…}`

        - `Tools []ToolUnion`

          The loaded tool definitions returned by the tool search output.

          - `type FunctionTool struct{…}`

            Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

            - `Name string`

              The name of the function to call.

            - `Parameters map[string, any]`

              A JSON schema object describing the parameters of the function.

            - `Strict bool`

              Whether strict parameter validation is enforced for this function tool.

            - `Type Function`

              The type of the function tool. Always `function`.

              - `const FunctionFunction Function = "function"`

            - `AllowedCallers []string`

              The tool invocation context(s).

              - `const FunctionToolAllowedCallerDirect FunctionToolAllowedCaller = "direct"`

              - `const FunctionToolAllowedCallerProgrammatic FunctionToolAllowedCaller = "programmatic"`

            - `Async bool`

            - `DeferLoading bool`

              Whether this function is deferred and loaded via tool search.

            - `Description string`

              A description of the function. Used by the model to determine whether or not to call the function.

            - `OutputSchema map[string, any]`

              A JSON schema object describing the JSON value encoded in string outputs for this function.

          - `type FileSearchTool struct{…}`

            A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

            - `Type FileSearch`

              The type of the file search tool. Always `file_search`.

              - `const FileSearchFileSearch FileSearch = "file_search"`

            - `VectorStoreIDs []string`

              The IDs of the vector stores to search.

            - `Filters FileSearchToolFiltersUnion`

              A filter to apply.

              - `type ComparisonFilter struct{…}`

                A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                - `Key string`

                  The key to compare against the value.

                - `Type ComparisonFilterType`

                  Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                  - `eq`: equals
                  - `ne`: not equal
                  - `gt`: greater than
                  - `gte`: greater than or equal
                  - `lt`: less than
                  - `lte`: less than or equal
                  - `in`: in
                  - `nin`: not in

                  - `const ComparisonFilterTypeEq ComparisonFilterType = "eq"`

                  - `const ComparisonFilterTypeNe ComparisonFilterType = "ne"`

                  - `const ComparisonFilterTypeGt ComparisonFilterType = "gt"`

                  - `const ComparisonFilterTypeGte ComparisonFilterType = "gte"`

                  - `const ComparisonFilterTypeLt ComparisonFilterType = "lt"`

                  - `const ComparisonFilterTypeLte ComparisonFilterType = "lte"`

                  - `const ComparisonFilterTypeIn ComparisonFilterType = "in"`

                  - `const ComparisonFilterTypeNin ComparisonFilterType = "nin"`

                - `Value ComparisonFilterValueUnion`

                  The value to compare against the attribute key; supports string, number, or boolean types.

                  - `string`

                  - `float64`

                  - `bool`

                  - `type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion`

                    - `string`

                    - `float64`

              - `type CompoundFilter struct{…}`

                Combine multiple filters using `and` or `or`.

                - `Filters []CompoundFilterFilterUnion`

                  Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

                  - `type ComparisonFilter struct{…}`

                    A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                  - `type CompoundFilter struct{…}`

                    Combine multiple filters using `and` or `or`.

                - `Type CompoundFilterType`

                  Type of operation: `and` or `or`.

                  - `const CompoundFilterTypeAnd CompoundFilterType = "and"`

                  - `const CompoundFilterTypeOr CompoundFilterType = "or"`

            - `MaxNumResults int64`

              The maximum number of results to return. This number should be between 1 and 50 inclusive.

            - `RankingOptions FileSearchToolRankingOptions`

              Ranking options for search.

              - `HybridSearch FileSearchToolRankingOptionsHybridSearch`

                Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

                - `EmbeddingWeight float64`

                  The weight of the embedding in the reciprocal ranking fusion.

                - `TextWeight float64`

                  The weight of the text in the reciprocal ranking fusion.

              - `Ranker string`

                The ranker to use for the file search.

                - `const FileSearchToolRankingOptionsRankerAuto FileSearchToolRankingOptionsRanker = "auto"`

                - `const FileSearchToolRankingOptionsRankerDefault2024_11_15 FileSearchToolRankingOptionsRanker = "default-2024-11-15"`

              - `ScoreThreshold float64`

                The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

          - `type ComputerTool struct{…}`

            A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

            - `Type Computer`

              The type of the computer tool. Always `computer`.

              - `const ComputerComputer Computer = "computer"`

          - `type ComputerUsePreviewTool struct{…}`

            A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

            - `DisplayHeight int64`

              The height of the computer display.

            - `DisplayWidth int64`

              The width of the computer display.

            - `Environment ComputerUsePreviewToolEnvironment`

              The type of computer environment to control.

              - `const ComputerUsePreviewToolEnvironmentWindows ComputerUsePreviewToolEnvironment = "windows"`

              - `const ComputerUsePreviewToolEnvironmentMac ComputerUsePreviewToolEnvironment = "mac"`

              - `const ComputerUsePreviewToolEnvironmentLinux ComputerUsePreviewToolEnvironment = "linux"`

              - `const ComputerUsePreviewToolEnvironmentUbuntu ComputerUsePreviewToolEnvironment = "ubuntu"`

              - `const ComputerUsePreviewToolEnvironmentBrowser ComputerUsePreviewToolEnvironment = "browser"`

            - `Type ComputerUsePreview`

              The type of the computer use tool. Always `computer_use_preview`.

              - `const ComputerUsePreviewComputerUsePreview ComputerUsePreview = "computer_use_preview"`

          - `type WebSearchTool struct{…}`

            Search the Internet for sources related to the prompt. Learn more about the
            [web search tool](/api/docs/guides/tools-web-search).

            - `Type WebSearchToolType`

              The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

              - `const WebSearchToolTypeWebSearch WebSearchToolType = "web_search"`

              - `const WebSearchToolTypeWebSearch2025_08_26 WebSearchToolType = "web_search_2025_08_26"`

            - `ExternalWebAccess bool`

              Allow live internet access for web search. Defaults to true when omitted. When false, the web search tool runs in offline/cache-only mode and will not fetch new external content.

            - `Filters WebSearchToolFilters`

              Filters for the search.

              - `AllowedDomains []string`

                Allowed domains for the search. If not provided, all domains are allowed.
                Subdomains of the provided domains are allowed as well.

                Example: `["pubmed.ncbi.nlm.nih.gov"]`

            - `SearchContextSize WebSearchToolSearchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `const WebSearchToolSearchContextSizeLow WebSearchToolSearchContextSize = "low"`

              - `const WebSearchToolSearchContextSizeMedium WebSearchToolSearchContextSize = "medium"`

              - `const WebSearchToolSearchContextSizeHigh WebSearchToolSearchContextSize = "high"`

            - `UserLocation WebSearchToolUserLocation`

              The approximate location of the user. If omitted or null, defaults to the
              United States. To avoid this fallback, pass `{"type": "approximate"}` without
              location fields. To localize results, provide the relevant location fields.

              - `City string`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Country string`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Region string`

                Free text input for the region of the user, e.g. `California`.

              - `Timezone string`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

              - `Type string`

                The type of location approximation. Always `approximate`.

                - `const WebSearchToolUserLocationTypeApproximate WebSearchToolUserLocationType = "approximate"`

          - `type ToolMcp struct{…}`

            Give the model access to additional tools via remote Model Context Protocol
            (MCP) servers. [Learn more about MCP](/api/docs/guides/tools-connectors-mcp).

            - `ServerLabel string`

              A label for this MCP server, used to identify it in tool calls.

            - `Type Mcp`

              The type of the MCP tool. Always `mcp`.

              - `const McpMcp Mcp = "mcp"`

            - `AllowedCallers []string`

              The tool invocation context(s).

              - `const ToolMcpAllowedCallerDirect ToolMcpAllowedCaller = "direct"`

              - `const ToolMcpAllowedCallerProgrammatic ToolMcpAllowedCaller = "programmatic"`

            - `AllowedTools ToolMcpAllowedToolsUnion`

              List of allowed tool names or a filter object.

              - `type ToolMcpAllowedToolsMcpAllowedTools []string`

                A string array of allowed tool names

              - `type ToolMcpAllowedToolsMcpToolFilter struct{…}`

                A filter object to specify which tools are allowed.

                - `ReadOnly bool`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `ToolNames []string`

                  List of allowed tool names.

            - `Authorization string`

              An OAuth access token that can be used with a remote MCP server, either
              with a custom MCP server URL or a service connector. Your application
              must handle the OAuth authorization flow and provide the token here.

            - `ConnectorID string`

              Identifier for service connectors, like those available in ChatGPT. One of
              `server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
              about service connectors [here](/api/docs/guides/tools-connectors-mcp#connectors).

              This field is deprecated for models released after September 1, 2026.
              Use `server_url` to connect to a remote MCP server, or `tunnel_id` to
              connect through a Secure MCP Tunnel.

              Currently supported `connector_id` values are:

              - Dropbox: `connector_dropbox`
              - Gmail: `connector_gmail`
              - Google Calendar: `connector_googlecalendar`
              - Google Drive: `connector_googledrive`
              - Microsoft Teams: `connector_microsoftteams`
              - Outlook Calendar: `connector_outlookcalendar`
              - Outlook Email: `connector_outlookemail`
              - SharePoint: `connector_sharepoint`

              - `const ToolMcpConnectorIDConnectorDropbox ToolMcpConnectorID = "connector_dropbox"`

              - `const ToolMcpConnectorIDConnectorGmail ToolMcpConnectorID = "connector_gmail"`

              - `const ToolMcpConnectorIDConnectorGooglecalendar ToolMcpConnectorID = "connector_googlecalendar"`

              - `const ToolMcpConnectorIDConnectorGoogledrive ToolMcpConnectorID = "connector_googledrive"`

              - `const ToolMcpConnectorIDConnectorMicrosoftteams ToolMcpConnectorID = "connector_microsoftteams"`

              - `const ToolMcpConnectorIDConnectorOutlookcalendar ToolMcpConnectorID = "connector_outlookcalendar"`

              - `const ToolMcpConnectorIDConnectorOutlookemail ToolMcpConnectorID = "connector_outlookemail"`

              - `const ToolMcpConnectorIDConnectorSharepoint ToolMcpConnectorID = "connector_sharepoint"`

            - `DeferLoading bool`

              Whether this MCP tool is deferred and discovered via tool search.

            - `Headers map[string, string]`

              Optional HTTP headers to send to the MCP server. Use for authentication
              or other purposes.

            - `RequireApproval ToolMcpRequireApprovalUnion`

              Specify which of the MCP server's tools require approval.

              - `type ToolMcpRequireApprovalMcpToolApprovalFilter struct{…}`

                Specify which of the MCP server's tools require approval. Can be
                `always`, `never`, or a filter object associated with tools
                that require approval.

                - `Always ToolMcpRequireApprovalMcpToolApprovalFilterAlways`

                  A filter object to specify which tools are allowed.

                  - `ReadOnly bool`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `ToolNames []string`

                    List of allowed tool names.

                - `Never ToolMcpRequireApprovalMcpToolApprovalFilterNever`

                  A filter object to specify which tools are allowed.

                  - `ReadOnly bool`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `ToolNames []string`

                    List of allowed tool names.

              - `type ToolMcpRequireApprovalMcpToolApprovalSetting string`

                Specify a single approval policy for all tools. One of `always` or
                `never`. When set to `always`, all tools will require approval. When
                set to `never`, all tools will not require approval.

                - `const ToolMcpRequireApprovalMcpToolApprovalSettingAlways ToolMcpRequireApprovalMcpToolApprovalSetting = "always"`

                - `const ToolMcpRequireApprovalMcpToolApprovalSettingNever ToolMcpRequireApprovalMcpToolApprovalSetting = "never"`

            - `ServerDescription string`

              Optional description of the MCP server, used to provide more context.

            - `ServerURL string`

              The URL for the MCP server. One of `server_url`, `connector_id`, or
              `tunnel_id` must be provided.

            - `TunnelID string`

              The Secure MCP Tunnel ID to use instead of a direct server URL. One of
              `server_url`, `connector_id`, or `tunnel_id` must be provided.

          - `type ToolCodeInterpreter struct{…}`

            A tool that runs Python code to help generate a response to a prompt.

            - `Container ToolCodeInterpreterContainerUnion`

              The code interpreter container. Can be a container ID or an object that
              specifies uploaded file IDs to make available to your code, along with an
              optional `memory_limit` setting.

              - `string`

              - `type ToolCodeInterpreterContainerCodeInterpreterContainerAuto struct{…}`

                Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

                - `Type Auto`

                  Always `auto`.

                  - `const AutoAuto Auto = "auto"`

                - `FileIDs []string`

                  An optional list of uploaded files to make available to your code.

                - `MemoryLimit string`

                  The memory limit for the code interpreter container.

                  - `const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit1g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "1g"`

                  - `const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit4g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "4g"`

                  - `const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit16g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "16g"`

                  - `const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit64g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "64g"`

                - `NetworkPolicy ToolCodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicyUnion`

                  Network access policy for the container.

                  - `type ContainerNetworkPolicyDisabled struct{…}`

                    - `Type Disabled`

                      Disable outbound network access. Always `disabled`.

                      - `const DisabledDisabled Disabled = "disabled"`

                  - `type ContainerNetworkPolicyAllowlist struct{…}`

                    - `AllowedDomains []string`

                      A list of allowed domains when type is `allowlist`.

                    - `Type Allowlist`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `const AllowlistAllowlist Allowlist = "allowlist"`

                    - `DomainSecrets []ContainerNetworkPolicyDomainSecret`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `Domain string`

                        The domain associated with the secret.

                      - `Name string`

                        The name of the secret to inject for the domain.

                      - `Value string`

                        The secret value to inject for the domain.

            - `Type CodeInterpreter`

              The type of the code interpreter tool. Always `code_interpreter`.

              - `const CodeInterpreterCodeInterpreter CodeInterpreter = "code_interpreter"`

            - `AllowedCallers []string`

              The tool invocation context(s).

              - `const ToolCodeInterpreterAllowedCallerDirect ToolCodeInterpreterAllowedCaller = "direct"`

              - `const ToolCodeInterpreterAllowedCallerProgrammatic ToolCodeInterpreterAllowedCaller = "programmatic"`

          - `type ToolProgrammaticToolCalling struct{…}`

            - `Type ProgrammaticToolCalling`

              The type of the tool. Always `programmatic_tool_calling`.

              - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

          - `type ToolImageGeneration struct{…}`

            A tool that generates images using the GPT image models.

            - `Type ImageGeneration`

              The type of the image generation tool. Always `image_generation`.

              - `const ImageGenerationImageGeneration ImageGeneration = "image_generation"`

            - `Action string`

              Whether to generate a new image or edit an existing image. Default: `auto`.

              - `const ToolImageGenerationActionGenerate ToolImageGenerationAction = "generate"`

              - `const ToolImageGenerationActionEdit ToolImageGenerationAction = "edit"`

              - `const ToolImageGenerationActionAuto ToolImageGenerationAction = "auto"`

            - `Background string`

              Allows to set transparency for the background of the generated image(s). Must
              be one of `transparent`, `opaque`, or `auto` (default value). When `auto` is
              used, the model will automatically determine the best background for the
              image.

              `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`, including their
              `2026-09-08` snapshots, support `opaque` and `transparent` backgrounds.
              Transparent backgrounds are available for supported GPT Image models. For
              `gpt-image-2` and `gpt-image-2-2026-04-21`, this support is in preview. When
              using `transparent`, set the output format to `png` or `webp`.

              - `const ToolImageGenerationBackgroundTransparent ToolImageGenerationBackground = "transparent"`

              - `const ToolImageGenerationBackgroundOpaque ToolImageGenerationBackground = "opaque"`

              - `const ToolImageGenerationBackgroundAuto ToolImageGenerationBackground = "auto"`

            - `InputFidelity string`

              Controls fidelity to the original input image(s). This parameter is supported for GPT image models that support input fidelity. `gpt-image-2` and `gpt-image-2-2026-04-21` ignore this parameter.

              - `const ToolImageGenerationInputFidelityHigh ToolImageGenerationInputFidelity = "high"`

              - `const ToolImageGenerationInputFidelityLow ToolImageGenerationInputFidelity = "low"`

            - `InputImageMask ToolImageGenerationInputImageMask`

              Optional mask for inpainting. Contains `image_url`
              (string, optional) and `file_id` (string, optional).

              - `FileID string`

                File ID for the mask image.

              - `ImageURL string`

                Base64-encoded mask image.

            - `Model string`

              The image generation model to use. One of `gpt-image-1`,
              `gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
              `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
              `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
              `gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
              `gpt-image-1`.

              - `string`

              - `string`

                - `const ToolImageGenerationModelGPTImage1 ToolImageGenerationModel = "gpt-image-1"`

                - `const ToolImageGenerationModelGPTImage1Mini ToolImageGenerationModel = "gpt-image-1-mini"`

                - `const ToolImageGenerationModelGPTImage2 ToolImageGenerationModel = "gpt-image-2"`

                - `const ToolImageGenerationModelGPTImage2_2026_04_21 ToolImageGenerationModel = "gpt-image-2-2026-04-21"`

                - `const ToolImageGenerationModelGPTImage2_5Sunburst ToolImageGenerationModel = "gpt-image-2.5-sunburst"`

                - `const ToolImageGenerationModelGPTImage2_5Sunburst2026_09_08 ToolImageGenerationModel = "gpt-image-2.5-sunburst-2026-09-08"`

                - `const ToolImageGenerationModelGPTImage2_5Flare ToolImageGenerationModel = "gpt-image-2.5-flare"`

                - `const ToolImageGenerationModelGPTImage2_5Flare2026_09_08 ToolImageGenerationModel = "gpt-image-2.5-flare-2026-09-08"`

                - `const ToolImageGenerationModelGPTImage1_5 ToolImageGenerationModel = "gpt-image-1.5"`

                - `const ToolImageGenerationModelChatgptImageLatest ToolImageGenerationModel = "chatgpt-image-latest"`

            - `Moderation string`

              Moderation level for the generated image. Default: `auto`.

              - `const ToolImageGenerationModerationAuto ToolImageGenerationModeration = "auto"`

              - `const ToolImageGenerationModerationLow ToolImageGenerationModeration = "low"`

            - `OutputCompression int64`

              Compression level for the output image. Default: 100.

            - `OutputFormat string`

              The output format of the generated image. One of `png`, `webp`, or
              `jpeg`. Default: `png`.

              - `const ToolImageGenerationOutputFormatPNG ToolImageGenerationOutputFormat = "png"`

              - `const ToolImageGenerationOutputFormatWebP ToolImageGenerationOutputFormat = "webp"`

              - `const ToolImageGenerationOutputFormatJPEG ToolImageGenerationOutputFormat = "jpeg"`

            - `PartialImages int64`

              Number of partial images to generate in streaming mode, from 0 (default value) to 3.

            - `Quality string`

              The quality of the generated image. The GPT image models support `low`,
              `medium`, and `high`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`,
              including their `2026-09-08` snapshots, also support `xhigh` and `max`.
              Default: `auto`.

              - `const ToolImageGenerationQualityLow ToolImageGenerationQuality = "low"`

              - `const ToolImageGenerationQualityMedium ToolImageGenerationQuality = "medium"`

              - `const ToolImageGenerationQualityHigh ToolImageGenerationQuality = "high"`

              - `const ToolImageGenerationQualityXhigh ToolImageGenerationQuality = "xhigh"`

              - `const ToolImageGenerationQualityMax ToolImageGenerationQuality = "max"`

              - `const ToolImageGenerationQualityAuto ToolImageGenerationQuality = "auto"`

            - `Size string`

              The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model's current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

              - `string`

              - `string`

                - `const ToolImageGenerationSize1024x1024 ToolImageGenerationSize = "1024x1024"`

                - `const ToolImageGenerationSize1024x1536 ToolImageGenerationSize = "1024x1536"`

                - `const ToolImageGenerationSize1536x1024 ToolImageGenerationSize = "1536x1024"`

                - `const ToolImageGenerationSizeAuto ToolImageGenerationSize = "auto"`

          - `type ToolLocalShell struct{…}`

            A tool that allows the model to execute shell commands in a local environment.

            - `Type LocalShell`

              The type of the local shell tool. Always `local_shell`.

              - `const LocalShellLocalShell LocalShell = "local_shell"`

          - `type FunctionShellTool struct{…}`

            A tool that allows the model to execute shell commands.

            - `Type Shell`

              The type of the shell tool. Always `shell`.

              - `const ShellShell Shell = "shell"`

            - `AllowedCallers []string`

              The tool invocation context(s).

              - `const FunctionShellToolAllowedCallerDirect FunctionShellToolAllowedCaller = "direct"`

              - `const FunctionShellToolAllowedCallerProgrammatic FunctionShellToolAllowedCaller = "programmatic"`

            - `Environment FunctionShellToolEnvironmentUnion`

              - `type ContainerAuto struct{…}`

                - `Type ContainerAuto`

                  Automatically creates a container for this request

                  - `const ContainerAutoContainerAuto ContainerAuto = "container_auto"`

                - `FileIDs []string`

                  An optional list of uploaded files to make available to your code.

                - `MemoryLimit ContainerAutoMemoryLimit`

                  The memory limit for the container.

                  - `const ContainerAutoMemoryLimit1g ContainerAutoMemoryLimit = "1g"`

                  - `const ContainerAutoMemoryLimit4g ContainerAutoMemoryLimit = "4g"`

                  - `const ContainerAutoMemoryLimit16g ContainerAutoMemoryLimit = "16g"`

                  - `const ContainerAutoMemoryLimit64g ContainerAutoMemoryLimit = "64g"`

                - `NetworkPolicy ContainerAutoNetworkPolicyUnion`

                  Network access policy for the container.

                  - `type ContainerNetworkPolicyDisabled struct{…}`

                  - `type ContainerNetworkPolicyAllowlist struct{…}`

                - `Skills []ContainerAutoSkillUnion`

                  An optional list of skills referenced by id or inline data.

                  - `type SkillReference struct{…}`

                    - `SkillID string`

                      The ID of the referenced skill.

                    - `Type SkillReference`

                      References a skill created with the /v1/skills endpoint.

                      - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

                    - `Version string`

                      Optional skill version. Use a positive integer or 'latest'. Omit for default.

                  - `type InlineSkill struct{…}`

                    - `Description string`

                      The description of the skill.

                    - `Name string`

                      The name of the skill.

                    - `Source InlineSkillSource`

                      Inline skill payload

                      - `Data string`

                        Base64-encoded skill zip bundle.

                      - `MediaType ApplicationZip`

                        The media type of the inline skill payload. Must be `application/zip`.

                        - `const ApplicationZipApplicationZip ApplicationZip = "application/zip"`

                      - `Type Base64`

                        The type of the inline skill source. Must be `base64`.

                        - `const Base64Base64 Base64 = "base64"`

                    - `Type Inline`

                      Defines an inline skill for this request.

                      - `const InlineInline Inline = "inline"`

              - `type LocalEnvironment struct{…}`

                - `Type Local`

                  Use a local computer environment.

                  - `const LocalLocal Local = "local"`

                - `Skills []LocalSkill`

                  An optional list of skills.

                  - `Description string`

                    The description of the skill.

                  - `Name string`

                    The name of the skill.

                  - `Path string`

                    The path to the directory containing the skill.

              - `type ContainerReference struct{…}`

                - `ContainerID string`

                  The ID of the referenced container.

                - `Type ContainerReference`

                  References a container created with the /v1/containers endpoint

                  - `const ContainerReferenceContainerReference ContainerReference = "container_reference"`

          - `type CustomTool struct{…}`

            A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

            - `Name string`

              The name of the custom tool, used to identify it in tool calls.

            - `Type Custom`

              The type of the custom tool. Always `custom`.

              - `const CustomCustom Custom = "custom"`

            - `AllowedCallers []string`

              The tool invocation context(s).

              - `const CustomToolAllowedCallerDirect CustomToolAllowedCaller = "direct"`

              - `const CustomToolAllowedCallerProgrammatic CustomToolAllowedCaller = "programmatic"`

            - `Async bool`

              Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

            - `DeferLoading bool`

              Whether this tool should be deferred and discovered via tool search.

            - `Description string`

              Optional description of the custom tool, used to provide more context.

            - `Format CustomToolInputFormatUnion`

              The input format for the custom tool. Default is unconstrained text.

              - `type CustomToolInputFormatText struct{…}`

                Unconstrained free-form text.

                - `Type Text`

                  Unconstrained text format. Always `text`.

                  - `const TextText Text = "text"`

              - `type CustomToolInputFormatGrammar struct{…}`

                A grammar defined by the user.

                - `Definition string`

                  The grammar definition.

                - `Syntax string`

                  The syntax of the grammar definition. One of `lark` or `regex`.

                  - `const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"`

                  - `const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"`

                - `Type Grammar`

                  Grammar format. Always `grammar`.

                  - `const GrammarGrammar Grammar = "grammar"`

          - `type NamespaceTool struct{…}`

            Groups function/custom tools under a shared namespace.

            - `Description string`

              A description of the namespace shown to the model.

            - `Name string`

              The namespace name used in tool calls (for example, `crm`).

            - `Tools []NamespaceToolToolUnion`

              The function/custom tools available inside this namespace.

              - `type NamespaceToolToolFunction struct{…}`

                - `Name string`

                - `Type Function`

                  - `const FunctionFunction Function = "function"`

                - `AllowedCallers []string`

                  The tool invocation context(s).

                  - `const NamespaceToolToolFunctionAllowedCallerDirect NamespaceToolToolFunctionAllowedCaller = "direct"`

                  - `const NamespaceToolToolFunctionAllowedCallerProgrammatic NamespaceToolToolFunctionAllowedCaller = "programmatic"`

                - `Async bool`

                  Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

                - `DeferLoading bool`

                  Whether this function should be deferred and discovered via tool search.

                - `Description string`

                - `OutputSchema map[string, any]`

                  A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

                - `Parameters any`

                - `Strict bool`

                  Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

              - `type CustomTool struct{…}`

                A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

            - `Type Namespace`

              The type of the tool. Always `namespace`.

              - `const NamespaceNamespace Namespace = "namespace"`

          - `type ToolSearchTool struct{…}`

            Hosted or BYOT tool search configuration for deferred tools.

            - `Type ToolSearch`

              The type of the tool. Always `tool_search`.

              - `const ToolSearchToolSearch ToolSearch = "tool_search"`

            - `Description string`

              Description shown to the model for a client-executed tool search tool.

            - `Execution ToolSearchToolExecution`

              Whether tool search is executed by the server or by the client.

              - `const ToolSearchToolExecutionServer ToolSearchToolExecution = "server"`

              - `const ToolSearchToolExecutionClient ToolSearchToolExecution = "client"`

            - `Parameters any`

              Parameter schema for a client-executed tool search tool.

          - `type WebSearchPreviewTool struct{…}`

            This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

            - `Type WebSearchPreviewToolType`

              The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

              - `const WebSearchPreviewToolTypeWebSearchPreview WebSearchPreviewToolType = "web_search_preview"`

              - `const WebSearchPreviewToolTypeWebSearchPreview2025_03_11 WebSearchPreviewToolType = "web_search_preview_2025_03_11"`

            - `SearchContentTypes []string`

              - `const WebSearchPreviewToolSearchContentTypeText WebSearchPreviewToolSearchContentType = "text"`

              - `const WebSearchPreviewToolSearchContentTypeImage WebSearchPreviewToolSearchContentType = "image"`

            - `SearchContextSize WebSearchPreviewToolSearchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `const WebSearchPreviewToolSearchContextSizeLow WebSearchPreviewToolSearchContextSize = "low"`

              - `const WebSearchPreviewToolSearchContextSizeMedium WebSearchPreviewToolSearchContextSize = "medium"`

              - `const WebSearchPreviewToolSearchContextSizeHigh WebSearchPreviewToolSearchContextSize = "high"`

            - `UserLocation WebSearchPreviewToolUserLocation`

              The approximate location of the user. If omitted or null, defaults to the United States. To avoid this fallback, pass `{"type": "approximate"}` without location fields. To localize results, provide the relevant location fields.

              - `Type Approximate`

                The type of location approximation. Always `approximate`.

                - `const ApproximateApproximate Approximate = "approximate"`

              - `City string`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Country string`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Region string`

                Free text input for the region of the user, e.g. `California`.

              - `Timezone string`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

          - `type ApplyPatchTool struct{…}`

            Allows the assistant to create, delete, or update files using unified diffs.

            - `Type ApplyPatch`

              The type of the tool. Always `apply_patch`.

              - `const ApplyPatchApplyPatch ApplyPatch = "apply_patch"`

            - `AllowedCallers []string`

              The tool invocation context(s).

              - `const ApplyPatchToolAllowedCallerDirect ApplyPatchToolAllowedCaller = "direct"`

              - `const ApplyPatchToolAllowedCallerProgrammatic ApplyPatchToolAllowedCaller = "programmatic"`

        - `Type ToolSearchOutput`

          The item type. Always `tool_search_output`.

          - `const ToolSearchOutputToolSearchOutput ToolSearchOutput = "tool_search_output"`

        - `ID string`

          The unique ID of this tool search output.

        - `CallID string`

          The unique ID of the tool search call generated by the model.

        - `Execution ResponseToolSearchOutputItemParamExecution`

          Whether tool search was executed by the server or by the client.

          - `const ResponseToolSearchOutputItemParamExecutionServer ResponseToolSearchOutputItemParamExecution = "server"`

          - `const ResponseToolSearchOutputItemParamExecutionClient ResponseToolSearchOutputItemParamExecution = "client"`

        - `Status ResponseToolSearchOutputItemParamStatus`

          The status of the tool search output.

          - `const ResponseToolSearchOutputItemParamStatusInProgress ResponseToolSearchOutputItemParamStatus = "in_progress"`

          - `const ResponseToolSearchOutputItemParamStatusCompleted ResponseToolSearchOutputItemParamStatus = "completed"`

          - `const ResponseToolSearchOutputItemParamStatusIncomplete ResponseToolSearchOutputItemParamStatus = "incomplete"`

      - `type ResponseInputItemAdditionalTools struct{…}`

        - `Role Developer`

          The role that provided the additional tools. Only `developer` is supported.

          - `const DeveloperDeveloper Developer = "developer"`

        - `Tools []ToolUnion`

          A list of additional tools made available at this item.

          - `type FunctionTool struct{…}`

            Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

          - `type FileSearchTool struct{…}`

            A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

          - `type ComputerTool struct{…}`

            A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

          - `type ComputerUsePreviewTool struct{…}`

            A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

          - `type WebSearchTool struct{…}`

            Search the Internet for sources related to the prompt. Learn more about the
            [web search tool](/api/docs/guides/tools-web-search).

          - `type ToolMcp struct{…}`

            Give the model access to additional tools via remote Model Context Protocol
            (MCP) servers. [Learn more about MCP](/api/docs/guides/tools-connectors-mcp).

          - `type ToolCodeInterpreter struct{…}`

            A tool that runs Python code to help generate a response to a prompt.

          - `type ToolProgrammaticToolCalling struct{…}`

          - `type ToolImageGeneration struct{…}`

            A tool that generates images using the GPT image models.

          - `type ToolLocalShell struct{…}`

            A tool that allows the model to execute shell commands in a local environment.

          - `type FunctionShellTool struct{…}`

            A tool that allows the model to execute shell commands.

          - `type CustomTool struct{…}`

            A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

          - `type NamespaceTool struct{…}`

            Groups function/custom tools under a shared namespace.

          - `type ToolSearchTool struct{…}`

            Hosted or BYOT tool search configuration for deferred tools.

          - `type WebSearchPreviewTool struct{…}`

            This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

          - `type ApplyPatchTool struct{…}`

            Allows the assistant to create, delete, or update files using unified diffs.

        - `Type AdditionalTools`

          The item type. Always `additional_tools`.

          - `const AdditionalToolsAdditionalTools AdditionalTools = "additional_tools"`

        - `ID string`

          The unique ID of this additional tools item.

      - `type ResponseConfigurationUpdateItemParamResp struct{…}`

        An update to the conversation's response configuration. The configuration
        remains in effect for subsequent responses until it is replaced by another
        configuration update.

        - `Type ConfigurationUpdate`

          The item type. Always `configuration_update`.

          - `const ConfigurationUpdateConfigurationUpdate ConfigurationUpdate = "configuration_update"`

        - `ID string`

          The unique ID of the configuration update item.

        - `Reasoning ResponseConfigurationUpdateItemParamReasoningResp`

          Updates to reasoning configuration. Only effort is supported.

          - `Effort ReasoningEffort`

            The reasoning effort to use for subsequent responses until another
            configuration update replaces it.

            - `const ReasoningEffortNone ReasoningEffort = "none"`

            - `const ReasoningEffortMinimal ReasoningEffort = "minimal"`

            - `const ReasoningEffortLow ReasoningEffort = "low"`

            - `const ReasoningEffortMedium ReasoningEffort = "medium"`

            - `const ReasoningEffortHigh ReasoningEffort = "high"`

            - `const ReasoningEffortXhigh ReasoningEffort = "xhigh"`

            - `const ReasoningEffortMax ReasoningEffort = "max"`

      - `type ResponseReasoningItem struct{…}`

        A description of the chain of thought used by a reasoning model while generating
        a response. Be sure to include these items in your `input` to the Responses API
        for subsequent turns of a conversation if you are manually
        [managing context](/api/docs/guides/conversation-state).

        - `ID string`

          The unique identifier of the reasoning content.

        - `Summary []ResponseReasoningItemSummary`

          Reasoning summary content.

          - `Text string`

            A summary of the reasoning output from the model so far.

          - `Type SummaryText`

            The type of the object. Always `summary_text`.

            - `const SummaryTextSummaryText SummaryText = "summary_text"`

        - `Type Reasoning`

          The type of the object. Always `reasoning`.

          - `const ReasoningReasoning Reasoning = "reasoning"`

        - `Content []ResponseReasoningItemContent`

          Reasoning text content.

          - `Text string`

            The reasoning text from the model.

          - `Type ReasoningText`

            The type of the reasoning text. Always `reasoning_text`.

            - `const ReasoningTextReasoningText ReasoningText = "reasoning_text"`

        - `EncryptedContent string`

          The encrypted content of the reasoning item. This is populated by default
          for reasoning items returned by `POST /v1/responses` and WebSocket
          `response.create` requests.

          When streaming, use the completed reasoning item and its
          `encrypted_content` from the `response.output_item.done` event in
          subsequent requests. The `encrypted_content` in
          `response.output_item.added` may be incomplete. This is especially
          important when `store` is `false` or when using Zero Data Retention.

        - `Status ResponseReasoningItemStatus`

          The status of the item. One of `in_progress`, `completed`, or
          `incomplete`. Populated when items are returned via API.

          - `const ResponseReasoningItemStatusInProgress ResponseReasoningItemStatus = "in_progress"`

          - `const ResponseReasoningItemStatusCompleted ResponseReasoningItemStatus = "completed"`

          - `const ResponseReasoningItemStatusIncomplete ResponseReasoningItemStatus = "incomplete"`

      - `type ResponseCompactionItemParamResp struct{…}`

        A compaction item generated by the [`v1/responses/compact` API](/api/reference/resources/responses/methods/compact).

        - `EncryptedContent string`

          The encrypted content of the compaction summary.

        - `Type Compaction`

          The type of the item. Always `compaction`.

          - `const CompactionCompaction Compaction = "compaction"`

        - `ID string`

          The ID of the compaction item.

      - `type ResponseInputItemImageGenerationCall struct{…}`

        An image generation request made by the model.

        - `ID string`

          The unique ID of the image generation call.

        - `Result string`

          The generated image encoded in base64.

        - `Status string`

          The status of the image generation call.

          - `const ResponseInputItemImageGenerationCallStatusInProgress ResponseInputItemImageGenerationCallStatus = "in_progress"`

          - `const ResponseInputItemImageGenerationCallStatusCompleted ResponseInputItemImageGenerationCallStatus = "completed"`

          - `const ResponseInputItemImageGenerationCallStatusGenerating ResponseInputItemImageGenerationCallStatus = "generating"`

          - `const ResponseInputItemImageGenerationCallStatusFailed ResponseInputItemImageGenerationCallStatus = "failed"`

        - `Type ImageGenerationCall`

          The type of the image generation call. Always `image_generation_call`.

          - `const ImageGenerationCallImageGenerationCall ImageGenerationCall = "image_generation_call"`

        - `Action string`

          The action used for image generation.

          - `const ResponseInputItemImageGenerationCallActionGenerate ResponseInputItemImageGenerationCallAction = "generate"`

          - `const ResponseInputItemImageGenerationCallActionEdit ResponseInputItemImageGenerationCallAction = "edit"`

          - `const ResponseInputItemImageGenerationCallActionAuto ResponseInputItemImageGenerationCallAction = "auto"`

        - `Background string`

          The background setting used for generation.

          - `const ResponseInputItemImageGenerationCallBackgroundTransparent ResponseInputItemImageGenerationCallBackground = "transparent"`

          - `const ResponseInputItemImageGenerationCallBackgroundOpaque ResponseInputItemImageGenerationCallBackground = "opaque"`

          - `const ResponseInputItemImageGenerationCallBackgroundAuto ResponseInputItemImageGenerationCallBackground = "auto"`

        - `OutputFormat string`

          The output format used for generation.

          - `const ResponseInputItemImageGenerationCallOutputFormatPNG ResponseInputItemImageGenerationCallOutputFormat = "png"`

          - `const ResponseInputItemImageGenerationCallOutputFormatWebP ResponseInputItemImageGenerationCallOutputFormat = "webp"`

          - `const ResponseInputItemImageGenerationCallOutputFormatJPEG ResponseInputItemImageGenerationCallOutputFormat = "jpeg"`

        - `Quality string`

          The quality of the image generated by the image generation tool call. One of `low`, `medium`, `high`, `xhigh`, `max`, or `auto`.

          - `const ResponseInputItemImageGenerationCallQualityLow ResponseInputItemImageGenerationCallQuality = "low"`

          - `const ResponseInputItemImageGenerationCallQualityMedium ResponseInputItemImageGenerationCallQuality = "medium"`

          - `const ResponseInputItemImageGenerationCallQualityHigh ResponseInputItemImageGenerationCallQuality = "high"`

          - `const ResponseInputItemImageGenerationCallQualityXhigh ResponseInputItemImageGenerationCallQuality = "xhigh"`

          - `const ResponseInputItemImageGenerationCallQualityMax ResponseInputItemImageGenerationCallQuality = "max"`

          - `const ResponseInputItemImageGenerationCallQualityAuto ResponseInputItemImageGenerationCallQuality = "auto"`

        - `RevisedPrompt string`

          The prompt that was used after any model prompt rewriting.

        - `Size string`

          The image dimensions as a `WIDTHxHEIGHT` string, for example `1536x864`.

          - `string`

          - `string`

            - `const ResponseInputItemImageGenerationCallSize1024x1024 ResponseInputItemImageGenerationCallSize = "1024x1024"`

            - `const ResponseInputItemImageGenerationCallSize1024x1536 ResponseInputItemImageGenerationCallSize = "1024x1536"`

            - `const ResponseInputItemImageGenerationCallSize1536x1024 ResponseInputItemImageGenerationCallSize = "1536x1024"`

      - `type ResponseCodeInterpreterToolCall struct{…}`

        A tool call to run code.

        - `ID string`

          The unique ID of the code interpreter tool call.

        - `Code string`

          The code to run, or null if not available.

        - `ContainerID string`

          The ID of the container used to run the code.

        - `Outputs []ResponseCodeInterpreterToolCallOutputUnion`

          The outputs generated by the code interpreter, such as logs or images.
          Can be null if no outputs are available.

          - `type ResponseCodeInterpreterToolCallOutputLogs struct{…}`

            The logs output from the code interpreter.

            - `Logs string`

              The logs output from the code interpreter.

            - `Type Logs`

              The type of the output. Always `logs`.

              - `const LogsLogs Logs = "logs"`

          - `type ResponseCodeInterpreterToolCallOutputImage struct{…}`

            The image output from the code interpreter.

            - `Type Image`

              The type of the output. Always `image`.

              - `const ImageImage Image = "image"`

            - `URL string`

              The URL of the image output from the code interpreter.

        - `Status ResponseCodeInterpreterToolCallStatus`

          The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

          - `const ResponseCodeInterpreterToolCallStatusInProgress ResponseCodeInterpreterToolCallStatus = "in_progress"`

          - `const ResponseCodeInterpreterToolCallStatusCompleted ResponseCodeInterpreterToolCallStatus = "completed"`

          - `const ResponseCodeInterpreterToolCallStatusIncomplete ResponseCodeInterpreterToolCallStatus = "incomplete"`

          - `const ResponseCodeInterpreterToolCallStatusInterpreting ResponseCodeInterpreterToolCallStatus = "interpreting"`

          - `const ResponseCodeInterpreterToolCallStatusFailed ResponseCodeInterpreterToolCallStatus = "failed"`

        - `Type CodeInterpreterCall`

          The type of the code interpreter tool call. Always `code_interpreter_call`.

          - `const CodeInterpreterCallCodeInterpreterCall CodeInterpreterCall = "code_interpreter_call"`

      - `type ResponseInputItemLocalShellCall struct{…}`

        A tool call to run a command on the local shell.

        - `ID string`

          The unique ID of the local shell call.

        - `Action ResponseInputItemLocalShellCallAction`

          Execute a shell command on the server.

          - `Command []string`

            The command to run.

          - `Env map[string, string]`

            Environment variables to set for the command.

          - `Type Exec`

            The type of the local shell action. Always `exec`.

            - `const ExecExec Exec = "exec"`

          - `TimeoutMs int64`

            Optional timeout in milliseconds for the command.

          - `User string`

            Optional user to run the command as.

          - `WorkingDirectory string`

            Optional working directory to run the command in.

        - `CallID string`

          The unique ID of the local shell tool call generated by the model.

        - `Status string`

          The status of the local shell call.

          - `const ResponseInputItemLocalShellCallStatusInProgress ResponseInputItemLocalShellCallStatus = "in_progress"`

          - `const ResponseInputItemLocalShellCallStatusCompleted ResponseInputItemLocalShellCallStatus = "completed"`

          - `const ResponseInputItemLocalShellCallStatusIncomplete ResponseInputItemLocalShellCallStatus = "incomplete"`

        - `Type LocalShellCall`

          The type of the local shell call. Always `local_shell_call`.

          - `const LocalShellCallLocalShellCall LocalShellCall = "local_shell_call"`

      - `type ResponseInputItemLocalShellCallOutput struct{…}`

        The output of a local shell tool call.

        - `ID string`

          The unique ID of the local shell tool call generated by the model.

        - `Output string`

          A JSON string of the output of the local shell tool call.

        - `Type LocalShellCallOutput`

          The type of the local shell tool call output. Always `local_shell_call_output`.

          - `const LocalShellCallOutputLocalShellCallOutput LocalShellCallOutput = "local_shell_call_output"`

        - `Status string`

          The status of the item. One of `in_progress`, `completed`, or `incomplete`.

          - `const ResponseInputItemLocalShellCallOutputStatusInProgress ResponseInputItemLocalShellCallOutputStatus = "in_progress"`

          - `const ResponseInputItemLocalShellCallOutputStatusCompleted ResponseInputItemLocalShellCallOutputStatus = "completed"`

          - `const ResponseInputItemLocalShellCallOutputStatusIncomplete ResponseInputItemLocalShellCallOutputStatus = "incomplete"`

      - `type ResponseInputItemShellCall struct{…}`

        A tool representing a request to execute one or more shell commands.

        - `Action ResponseInputItemShellCallAction`

          The shell commands and limits that describe how to run the tool call.

          - `Commands []string`

            Ordered shell commands for the execution environment to run.

          - `MaxOutputLength int64`

            Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

          - `TimeoutMs int64`

            Maximum wall-clock time in milliseconds to allow the shell commands to run.

        - `CallID string`

          The unique ID of the shell tool call generated by the model.

        - `Type ShellCall`

          The type of the item. Always `shell_call`.

          - `const ShellCallShellCall ShellCall = "shell_call"`

        - `ID string`

          The unique ID of the shell tool call. Populated when this item is returned via API.

        - `Caller ResponseInputItemShellCallCallerUnion`

          The execution context that produced this tool call.

          - `type ResponseInputItemShellCallCallerDirect struct{…}`

            - `Type Direct`

              The caller type. Always `direct`.

              - `const DirectDirect Direct = "direct"`

          - `type ResponseInputItemShellCallCallerProgram struct{…}`

            - `CallerID string`

              The call ID of the program item that produced this tool call.

            - `Type Program`

              The caller type. Always `program`.

              - `const ProgramProgram Program = "program"`

        - `Environment ResponseInputItemShellCallEnvironmentUnion`

          The environment to execute the shell commands in.

          - `type LocalEnvironment struct{…}`

          - `type ContainerReference struct{…}`

        - `Status string`

          The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

          - `const ResponseInputItemShellCallStatusInProgress ResponseInputItemShellCallStatus = "in_progress"`

          - `const ResponseInputItemShellCallStatusCompleted ResponseInputItemShellCallStatus = "completed"`

          - `const ResponseInputItemShellCallStatusIncomplete ResponseInputItemShellCallStatus = "incomplete"`

      - `type ResponseInputItemShellCallOutput struct{…}`

        The streamed output items emitted by a shell tool call.

        - `CallID string`

          The unique ID of the shell tool call generated by the model.

        - `Output []ResponseFunctionShellCallOutputContent`

          Captured chunks of stdout and stderr output, along with their associated outcomes.

          - `Outcome ResponseFunctionShellCallOutputContentOutcomeUnion`

            The exit or timeout outcome associated with this shell call.

            - `type ResponseFunctionShellCallOutputContentOutcomeTimeout struct{…}`

              Indicates that the shell call exceeded its configured time limit.

              - `Type Timeout`

                The outcome type. Always `timeout`.

                - `const TimeoutTimeout Timeout = "timeout"`

            - `type ResponseFunctionShellCallOutputContentOutcomeExit struct{…}`

              Indicates that the shell commands finished and returned an exit code.

              - `ExitCode int64`

                The exit code returned by the shell process.

              - `Type Exit`

                The outcome type. Always `exit`.

                - `const ExitExit Exit = "exit"`

          - `Stderr string`

            Captured stderr output for the shell call.

          - `Stdout string`

            Captured stdout output for the shell call.

        - `Type ShellCallOutput`

          The type of the item. Always `shell_call_output`.

          - `const ShellCallOutputShellCallOutput ShellCallOutput = "shell_call_output"`

        - `ID string`

          The unique ID of the shell tool call output. Populated when this item is returned via API.

        - `Caller ResponseInputItemShellCallOutputCallerUnion`

          The execution context that produced this tool call.

          - `type ResponseInputItemShellCallOutputCallerDirect struct{…}`

            - `Type Direct`

              The caller type. Always `direct`.

              - `const DirectDirect Direct = "direct"`

          - `type ResponseInputItemShellCallOutputCallerProgram struct{…}`

            - `CallerID string`

              The call ID of the program item that produced this tool call.

            - `Type Program`

              The caller type. Always `program`.

              - `const ProgramProgram Program = "program"`

        - `MaxOutputLength int64`

          The maximum number of UTF-8 characters captured for this shell call's combined output.

        - `Status string`

          The status of the shell call output.

          - `const ResponseInputItemShellCallOutputStatusInProgress ResponseInputItemShellCallOutputStatus = "in_progress"`

          - `const ResponseInputItemShellCallOutputStatusCompleted ResponseInputItemShellCallOutputStatus = "completed"`

          - `const ResponseInputItemShellCallOutputStatusIncomplete ResponseInputItemShellCallOutputStatus = "incomplete"`

      - `type ResponseInputItemApplyPatchCall struct{…}`

        A tool call representing a request to create, delete, or update files using diff patches.

        - `CallID string`

          The unique ID of the apply patch tool call generated by the model.

        - `Operation ResponseInputItemApplyPatchCallOperationUnion`

          The specific create, delete, or update instruction for the apply_patch tool call.

          - `type ResponseInputItemApplyPatchCallOperationCreateFile struct{…}`

            Instruction for creating a new file via the apply_patch tool.

            - `Diff string`

              Unified diff content to apply when creating the file.

            - `Path string`

              Path of the file to create relative to the workspace root.

            - `Type CreateFile`

              The operation type. Always `create_file`.

              - `const CreateFileCreateFile CreateFile = "create_file"`

          - `type ResponseInputItemApplyPatchCallOperationDeleteFile struct{…}`

            Instruction for deleting an existing file via the apply_patch tool.

            - `Path string`

              Path of the file to delete relative to the workspace root.

            - `Type DeleteFile`

              The operation type. Always `delete_file`.

              - `const DeleteFileDeleteFile DeleteFile = "delete_file"`

          - `type ResponseInputItemApplyPatchCallOperationUpdateFile struct{…}`

            Instruction for updating an existing file via the apply_patch tool.

            - `Diff string`

              Unified diff content to apply to the existing file.

            - `Path string`

              Path of the file to update relative to the workspace root.

            - `Type UpdateFile`

              The operation type. Always `update_file`.

              - `const UpdateFileUpdateFile UpdateFile = "update_file"`

        - `Status string`

          The status of the apply patch tool call. One of `in_progress` or `completed`.

          - `const ResponseInputItemApplyPatchCallStatusInProgress ResponseInputItemApplyPatchCallStatus = "in_progress"`

          - `const ResponseInputItemApplyPatchCallStatusCompleted ResponseInputItemApplyPatchCallStatus = "completed"`

        - `Type ApplyPatchCall`

          The type of the item. Always `apply_patch_call`.

          - `const ApplyPatchCallApplyPatchCall ApplyPatchCall = "apply_patch_call"`

        - `ID string`

          The unique ID of the apply patch tool call. Populated when this item is returned via API.

        - `Caller ResponseInputItemApplyPatchCallCallerUnion`

          The execution context that produced this tool call.

          - `type ResponseInputItemApplyPatchCallCallerDirect struct{…}`

            - `Type Direct`

              The caller type. Always `direct`.

              - `const DirectDirect Direct = "direct"`

          - `type ResponseInputItemApplyPatchCallCallerProgram struct{…}`

            - `CallerID string`

              The call ID of the program item that produced this tool call.

            - `Type Program`

              The caller type. Always `program`.

              - `const ProgramProgram Program = "program"`

      - `type ResponseInputItemApplyPatchCallOutput struct{…}`

        The streamed output emitted by an apply patch tool call.

        - `CallID string`

          The unique ID of the apply patch tool call generated by the model.

        - `Status string`

          The status of the apply patch tool call output. One of `completed` or `failed`.

          - `const ResponseInputItemApplyPatchCallOutputStatusCompleted ResponseInputItemApplyPatchCallOutputStatus = "completed"`

          - `const ResponseInputItemApplyPatchCallOutputStatusFailed ResponseInputItemApplyPatchCallOutputStatus = "failed"`

        - `Type ApplyPatchCallOutput`

          The type of the item. Always `apply_patch_call_output`.

          - `const ApplyPatchCallOutputApplyPatchCallOutput ApplyPatchCallOutput = "apply_patch_call_output"`

        - `ID string`

          The unique ID of the apply patch tool call output. Populated when this item is returned via API.

        - `Caller ResponseInputItemApplyPatchCallOutputCallerUnion`

          The execution context that produced this tool call.

          - `type ResponseInputItemApplyPatchCallOutputCallerDirect struct{…}`

            - `Type Direct`

              The caller type. Always `direct`.

              - `const DirectDirect Direct = "direct"`

          - `type ResponseInputItemApplyPatchCallOutputCallerProgram struct{…}`

            - `CallerID string`

              The call ID of the program item that produced this tool call.

            - `Type Program`

              The caller type. Always `program`.

              - `const ProgramProgram Program = "program"`

        - `Output string`

          Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

      - `type ResponseInputItemMcpListTools struct{…}`

        A list of tools available on an MCP server.

        - `ID string`

          The unique ID of the list.

        - `ServerLabel string`

          The label of the MCP server.

        - `Tools []ResponseInputItemMcpListToolsTool`

          The tools available on the server.

          - `InputSchema any`

            The JSON schema describing the tool's input.

          - `Name string`

            The name of the tool.

          - `Annotations any`

            Additional annotations about the tool.

          - `Description string`

            The description of the tool.

        - `Type McpListTools`

          The type of the item. Always `mcp_list_tools`.

          - `const McpListToolsMcpListTools McpListTools = "mcp_list_tools"`

        - `Error string`

          Error message if the server could not list tools.

      - `type ResponseInputItemMcpApprovalRequest struct{…}`

        A request for human approval of a tool invocation.

        - `ID string`

          The unique ID of the approval request.

        - `Arguments string`

          A JSON string of arguments for the tool.

        - `Name string`

          The name of the tool to run.

        - `ServerLabel string`

          The label of the MCP server making the request.

        - `Type McpApprovalRequest`

          The type of the item. Always `mcp_approval_request`.

          - `const McpApprovalRequestMcpApprovalRequest McpApprovalRequest = "mcp_approval_request"`

      - `type ResponseInputItemMcpApprovalResponse struct{…}`

        A response to an MCP approval request.

        - `ApprovalRequestID string`

          The ID of the approval request being answered.

        - `Approve bool`

          Whether the request was approved.

        - `Type McpApprovalResponse`

          The type of the item. Always `mcp_approval_response`.

          - `const McpApprovalResponseMcpApprovalResponse McpApprovalResponse = "mcp_approval_response"`

        - `ID string`

          The unique ID of the approval response

        - `Reason string`

          Optional reason for the decision.

      - `type ResponseInputItemMcpCall struct{…}`

        An invocation of a tool on an MCP server.

        - `ID string`

          The unique ID of the tool call.

        - `Arguments string`

          A JSON string of the arguments passed to the tool.

        - `Name string`

          The name of the tool that was run.

        - `ServerLabel string`

          The label of the MCP server running the tool.

        - `Type McpCall`

          The type of the item. Always `mcp_call`.

          - `const McpCallMcpCall McpCall = "mcp_call"`

        - `ApprovalRequestID string`

          Unique identifier for the MCP tool call approval request.
          Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

        - `Error McpToolCallErrorUnion`

          The error from the tool call, if any.

          - `type McpToolCallErrorMcpProtocolError struct{…}`

            - `Code int64`

            - `Message string`

            - `Type McpProtocolError`

              - `const McpProtocolErrorMcpProtocolError McpProtocolError = "mcp_protocol_error"`

          - `type McpToolCallErrorMcpToolExecutionError struct{…}`

            - `Content any`

            - `Type McpToolExecutionError`

              - `const McpToolExecutionErrorMcpToolExecutionError McpToolExecutionError = "mcp_tool_execution_error"`

          - `type McpToolCallErrorHTTPError struct{…}`

            - `Code int64`

            - `Message string`

            - `Type HTTPError`

              - `const HTTPErrorHTTPError HTTPError = "http_error"`

        - `Output string`

          The output from the tool call.

        - `Status string`

          The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

          - `const ResponseInputItemMcpCallStatusInProgress ResponseInputItemMcpCallStatus = "in_progress"`

          - `const ResponseInputItemMcpCallStatusCompleted ResponseInputItemMcpCallStatus = "completed"`

          - `const ResponseInputItemMcpCallStatusIncomplete ResponseInputItemMcpCallStatus = "incomplete"`

          - `const ResponseInputItemMcpCallStatusCalling ResponseInputItemMcpCallStatus = "calling"`

          - `const ResponseInputItemMcpCallStatusFailed ResponseInputItemMcpCallStatus = "failed"`

      - `type ResponseCustomToolCallOutput struct{…}`

        The output of a custom tool call from your code, being sent back to the model.

        - `CallID string`

          The call ID, used to map this custom tool call output to a custom tool call.

        - `Output ResponseCustomToolCallOutputOutputUnion`

          The output from the custom tool call generated by your code.
          Can be a string or an list of output content.

          - `string`

          - `type ResponseCustomToolCallOutputOutputOutputContentList []ResponseCustomToolCallOutputOutputOutputContentListItemUnion`

            Text, image, or file output of the custom tool call.

            - `type ResponseInputText struct{…}`

              A text input to the model.

            - `type ResponseInputImage struct{…}`

              An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

            - `type ResponseInputFile struct{…}`

              A file input to the model.

        - `Type CustomToolCallOutput`

          The type of the custom tool call output. Always `custom_tool_call_output`.

          - `const CustomToolCallOutputCustomToolCallOutput CustomToolCallOutput = "custom_tool_call_output"`

        - `ID string`

          The unique ID of the custom tool call output in the OpenAI platform.

        - `Caller ResponseCustomToolCallOutputCallerUnion`

          The execution context that produced this tool call.

          - `type ResponseCustomToolCallOutputCallerDirect struct{…}`

            - `Type Direct`

              The caller type. Always `direct`.

              - `const DirectDirect Direct = "direct"`

          - `type ResponseCustomToolCallOutputCallerProgram struct{…}`

            - `CallerID string`

              The call ID of the program item that produced this tool call.

            - `Type Program`

              The caller type. Always `program`.

              - `const ProgramProgram Program = "program"`

      - `type ResponseCustomToolCall struct{…}`

        A call to a custom tool created by the model.

        - `CallID string`

          An identifier used to map this custom tool call to a tool call output.

        - `Input string`

          The input for the custom tool call generated by the model.

        - `Name string`

          The name of the custom tool being called.

        - `Type CustomToolCall`

          The type of the custom tool call. Always `custom_tool_call`.

          - `const CustomToolCallCustomToolCall CustomToolCall = "custom_tool_call"`

        - `ID string`

          The unique ID of the custom tool call in the OpenAI platform.

        - `Async bool`

          Whether the custom tool call runs asynchronously.

        - `Caller ResponseCustomToolCallCallerUnion`

          The execution context that produced this tool call.

          - `type ResponseCustomToolCallCallerDirect struct{…}`

            - `Type Direct`

              - `const DirectDirect Direct = "direct"`

          - `type ResponseCustomToolCallCallerProgram struct{…}`

            - `CallerID string`

              The call ID of the program item that produced this tool call.

            - `Type Program`

              - `const ProgramProgram Program = "program"`

        - `Namespace string`

          The namespace of the custom tool being called.

      - `type ResponseInputItemCompactionTrigger struct{…}`

        Compacts the current context. Must be the final input item.

        - `Type CompactionTrigger`

          The type of the item. Always `compaction_trigger`.

          - `const CompactionTriggerCompactionTrigger CompactionTrigger = "compaction_trigger"`

      - `type ResponseInputItemItemReference struct{…}`

        An internal identifier for an item to reference.

        - `ID string`

          The ID of the item to reference.

        - `Type string`

          The type of item to reference. Always `item_reference`.

          - `const ResponseInputItemItemReferenceTypeItemReference ResponseInputItemItemReferenceType = "item_reference"`

      - `type ResponseInputItemProgram struct{…}`

        - `ID string`

          The unique ID of this program item.

        - `CallID string`

          The stable call ID of the program item.

        - `Code string`

          The JavaScript source executed by programmatic tool calling.

        - `Fingerprint string`

          Opaque program replay fingerprint that must be round-tripped.

        - `Type Program`

          The item type. Always `program`.

          - `const ProgramProgram Program = "program"`

      - `type ResponseInputItemProgramOutput struct{…}`

        - `ID string`

          The unique ID of this program output item.

        - `CallID string`

          The call ID of the program item.

        - `Result string`

          The result produced by the program item.

        - `Status string`

          The terminal status of the program output.

          - `const ResponseInputItemProgramOutputStatusCompleted ResponseInputItemProgramOutputStatus = "completed"`

          - `const ResponseInputItemProgramOutputStatusIncomplete ResponseInputItemProgramOutputStatus = "incomplete"`

        - `Type ProgramOutput`

          The item type. Always `program_output`.

          - `const ProgramOutputProgramOutput ProgramOutput = "program_output"`

    - `Type ResponseItemCreate`

      The Live client event type. Always `response.item.create`.

      - `const ResponseItemCreateResponseItemCreate ResponseItemCreate = "response.item.create"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type ResponseCreateEvent struct{…}`

    Request a response from the Live session’s Responses backend, or continue a delegated response waiting for tool results. Requires Responses delegation.

    - `Type ResponseCreate`

      The Live client event type. Always `response.create`.

      - `const ResponseCreateResponseCreate ResponseCreate = "response.create"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type SessionCloseEvent struct{…}`

    Request that the Live session close. The terminal `session.closed` event contains the close reason and final usage.

    - `Type SessionClose`

      The Live client event type. Always `session.close`.

      - `const SessionCloseSessionClose SessionClose = "session.close"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Commentary Append Event

- `type CommentaryAppendEvent struct{…}`

  Provide context the Live model can communicate to the user, optionally for an existing client delegation.

  - `Content string`

    Speakable context for the Live model, limited to 500 tokens. Use this for a result the model should communicate; use session.thinking.append for silent context.

  - `DelegationID string`

    Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

  - `Type SessionCommentaryAppend`

    The Live client event type. Always `session.commentary.append`.

    - `const SessionCommentaryAppendSessionCommentaryAppend SessionCommentaryAppend = "session.commentary.append"`

  - `EventID string`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Commentary Appended Event

- `type CommentaryAppendedEvent struct{…}`

  Returned when a session.commentary.append command is accepted into the Live session timeline. Acknowledges the added commentary without guaranteeing exact wording or completed audio playback.

  - `EndMs int64`

    The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

  - `EventID string`

    The unique ID of the Live server event.

  - `StartMs int64`

    The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

  - `Type SessionCommentaryAppended`

    The event type, always `session.commentary.appended`.

    - `const SessionCommentaryAppendedSessionCommentaryAppended SessionCommentaryAppended = "session.commentary.appended"`

  - `ClientEventID string`

    The event_id of the client command associated with this server event, when supplied.

### Custom Voice

- `type CustomVoice struct{…}`

  - `ID string`

### Data Channel Config

- `type DataChannelConfig struct{…}`

  Control which Live events an untrusted WebRTC frontend can send and receive over its data channel. These restrictions do not apply to trusted sideband connections.

  - `AllowedClientEvents DataChannelConfigAllowedClientEventsUnion`

    Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

    - `All`

      - `const AllAll All = "all"`

    - `[]string`

  - `AllowedServerEvents DataChannelConfigAllowedServerEventsUnion`

    Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

    - `All`

      - `const AllAll All = "all"`

    - `[]ServerEventSelector`

      - `Type string`

        The outer Live server event type. Use 'response.event' for Responses events.

      - `ResponseEvent string`

        The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

### Delegation Created Event

- `type DelegationCreatedEvent struct{…}`

  Returned when the Live model delegates work to your application or a Responses backend. Contains delegation metadata and the position on the session timeline where the work was delegated.

  - `Delegation DelegationCreatedEventDelegation`

    The delegated work identifier and destination. This object contains metadata, not the task text.

    - `ID string`

      The unique ID of the delegation. Use this as delegation_id when replying to client-owned work or correlating Responses events.

    - `Target string`

      Where the Live model delegated the work: `client` for your application, or `responses` for the configured Responses backend.

      - `string`

        - `const DelegationCreatedEventDelegationTargetStringClient DelegationCreatedEventDelegationTargetString = "client"`

        - `const DelegationCreatedEventDelegationTargetStringResponses DelegationCreatedEventDelegationTargetString = "responses"`

    - `Type Delegation`

      The object type, always `delegation`.

      - `const DelegationDelegation Delegation = "delegation"`

    - `ResponseID string`

      The ID of the Responses API response associated with a Responses delegation. Omitted for client delegations.

  - `EventID string`

    The unique ID of the Live server event.

  - `OffsetMs int64`

    The position on the Live session timeline where the delegation was created, in milliseconds from the beginning of the session.

  - `Type SessionDelegationCreated`

    The event type, always `session.delegation.created`.

    - `const SessionDelegationCreatedSessionDelegationCreated SessionDelegationCreated = "session.delegation.created"`

  - `ClientEventID string`

    The event_id of the client command associated with this server event, when supplied.

### Error

- `type Error struct{…}`

  Details of an error encountered by the Live session, including the affected parameter or client command when available.

  - `Code string`

    A machine-readable code identifying the Live error, such as `unknown_parameter`.

  - `Message string`

    A human-readable explanation of the Live error.

  - `Type string`

    The category of error, such as `invalid_request_error` for an invalid Live client command.

  - `ClientEventID string`

    The event_id of the client command that caused the error, when supplied.

  - `Param string`

    The parameter that caused the error, when applicable, such as `session.voice`.

### Error Event

- `type ErrorEvent struct{…}`

  Reports an error in the Live session, such as an invalid client command. Use error.client_event_id, when present, to identify the command that caused the error.

  - `Error Error`

    Details of the Live error and the client command that caused it, when known.

    - `Code string`

      A machine-readable code identifying the Live error, such as `unknown_parameter`.

    - `Message string`

      A human-readable explanation of the Live error.

    - `Type string`

      The category of error, such as `invalid_request_error` for an invalid Live client command.

    - `ClientEventID string`

      The event_id of the client command that caused the error, when supplied.

    - `Param string`

      The parameter that caused the error, when applicable, such as `session.voice`.

  - `EventID string`

    The unique ID of the Live server event.

  - `Type Error`

    The event type, always `error`.

    - `const ErrorError Error = "error"`

  - `ClientEventID string`

    The event_id of the client command associated with this server event, when supplied.

### Fork Session Config

- `type ForkSessionConfig struct{…}`

  Overrides for a stored session after connecting to the fork WebSocket. An empty object inherits the stored configuration; do not supply a new model. audio.format applies only to the new WebSocket connection. client overrides are only supported for WebRTC forks.

  - `Audio ForkSessionConfigAudio`

    Audio format for a WebSocket fork. WebRTC forks negotiate their audio format and must omit this field.

    - `Format AudioFormatUnion`

      Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

      - `AudioFormatAudioPCM`

        - `Rate int64`

          Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

          - `const AudioFormatAudioPCMRate16000 AudioFormatAudioPCMRate = 16000`

          - `const AudioFormatAudioPCMRate24000 AudioFormatAudioPCMRate = 24000`

        - `Type AudioPCM`

          The audio encoding. Always `audio/pcm`.

          - `const AudioPCMAudioPCM AudioPCM = "audio/pcm"`

      - `AudioFormatAudioPCMU`

        - `Rate int64`

          Audio sample rate in hertz. G.711 audio uses 8000 Hz.

        - `Type AudioPCMU`

          The audio encoding. Always `audio/pcmu`.

          - `const AudioPCMUAudioPCMU AudioPCMU = "audio/pcmu"`

      - `AudioFormatAudioPCMA`

        - `Rate int64`

          Audio sample rate in hertz. G.711 audio uses 8000 Hz.

        - `Type AudioPCMA`

          The audio encoding. Always `audio/pcma`.

          - `const AudioPCMAAudioPCMA AudioPCMA = "audio/pcma"`

  - `Client ClientConfig`

    Frontend data-channel permissions for a WebRTC fork. Omitted permissions inherit the stored values. Not supported for WebSocket forks.

    - `DataChannel DataChannelConfig`

      Client and server event permissions for the WebRTC frontend data channel.

      - `AllowedClientEvents DataChannelConfigAllowedClientEventsUnion`

        Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

        - `All`

          - `const AllAll All = "all"`

        - `[]string`

      - `AllowedServerEvents DataChannelConfigAllowedServerEventsUnion`

        Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

        - `All`

          - `const AllAll All = "all"`

        - `[]ServerEventSelector`

          - `Type string`

            The outer Live server event type. Use 'response.event' for Responses events.

          - `ResponseEvent string`

            The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

  - `Delegation ForkSessionConfigDelegation`

    Overrides for the stored session’s Responses backend. Only supported when the stored session already uses Responses delegation; the delegation type cannot change.

    - `Type Responses`

      The delegation owner. Always `responses` for tasks handled by the Responses API.

      - `const ResponsesResponses Responses = "responses"`

    - `Responses ResponsesDelegationUpdateConfig`

      Responses backend settings to update. Omitted settings keep their existing values.

      - `Instructions string`

        Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

      - `MaxOutputTokens int64`

        Maximum number of output tokens for each delegated response.

      - `Model string`

        The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.

      - `ParallelToolCalls bool`

        Whether the delegated Responses model may request multiple tool calls in a single response.

      - `Reasoning ResponsesDelegationUpdateConfigReasoning`

        Reasoning settings passed to each delegated Responses request.

        - `Effort string`

          How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

          - `const ResponsesDelegationUpdateConfigReasoningEffortNone ResponsesDelegationUpdateConfigReasoningEffort = "none"`

          - `const ResponsesDelegationUpdateConfigReasoningEffortMinimal ResponsesDelegationUpdateConfigReasoningEffort = "minimal"`

          - `const ResponsesDelegationUpdateConfigReasoningEffortLow ResponsesDelegationUpdateConfigReasoningEffort = "low"`

          - `const ResponsesDelegationUpdateConfigReasoningEffortMedium ResponsesDelegationUpdateConfigReasoningEffort = "medium"`

          - `const ResponsesDelegationUpdateConfigReasoningEffortHigh ResponsesDelegationUpdateConfigReasoningEffort = "high"`

          - `const ResponsesDelegationUpdateConfigReasoningEffortXhigh ResponsesDelegationUpdateConfigReasoningEffort = "xhigh"`

        - `Summary string`

          The reasoning summary to request from the delegated Responses model, when supported.

          - `const ResponsesDelegationUpdateConfigReasoningSummaryConcise ResponsesDelegationUpdateConfigReasoningSummary = "concise"`

          - `const ResponsesDelegationUpdateConfigReasoningSummaryDetailed ResponsesDelegationUpdateConfigReasoningSummary = "detailed"`

          - `const ResponsesDelegationUpdateConfigReasoningSummaryAuto ResponsesDelegationUpdateConfigReasoningSummary = "auto"`

      - `ServiceTier ResponsesDelegationUpdateConfigServiceTier`

        Service tier for delegated Responses requests.

        - `const ResponsesDelegationUpdateConfigServiceTierAuto ResponsesDelegationUpdateConfigServiceTier = "auto"`

        - `const ResponsesDelegationUpdateConfigServiceTierDefault ResponsesDelegationUpdateConfigServiceTier = "default"`

        - `const ResponsesDelegationUpdateConfigServiceTierFastTierTempPilot ResponsesDelegationUpdateConfigServiceTier = "fast_tier_temp_pilot"`

        - `const ResponsesDelegationUpdateConfigServiceTierFlex ResponsesDelegationUpdateConfigServiceTier = "flex"`

        - `const ResponsesDelegationUpdateConfigServiceTierPriority ResponsesDelegationUpdateConfigServiceTier = "priority"`

        - `const ResponsesDelegationUpdateConfigServiceTierUltrafast ResponsesDelegationUpdateConfigServiceTier = "ultrafast"`

      - `Text ResponsesDelegationUpdateConfigText`

        Text generation settings passed to each delegated Responses request.

        - `Verbosity string`

          The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

          - `const ResponsesDelegationUpdateConfigTextVerbosityLow ResponsesDelegationUpdateConfigTextVerbosity = "low"`

          - `const ResponsesDelegationUpdateConfigTextVerbosityMedium ResponsesDelegationUpdateConfigTextVerbosity = "medium"`

          - `const ResponsesDelegationUpdateConfigTextVerbosityHigh ResponsesDelegationUpdateConfigTextVerbosity = "high"`

      - `ToolChoice ResponsesDelegationUpdateConfigToolChoiceUnion`

        Controls which tool the Responses backend uses when handling a task delegated by the Live model.

        - `string`

          - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "auto"`

          - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "none"`

          - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "required"`

        - `ResponsesDelegationUpdateConfigToolChoiceLiveFunctionToolChoiceParam`

          - `Name string`

          - `Type Function`

            - `const FunctionFunction Function = "function"`

        - `ResponsesDelegationUpdateConfigToolChoiceLiveMcpToolChoiceParam`

          - `Name string`

          - `ServerLabel string`

          - `Type Mcp`

            - `const McpMcp Mcp = "mcp"`

      - `Tools []ResponsesDelegationUpdateConfigToolUnion`

        Tools available to the Responses backend while it handles tasks delegated by the Live model.

        - `type FunctionTool struct{…}`

          A function tool available to the Responses backend when the Live model delegates a task.

          - `Name string`

            The name the delegated Responses model uses when calling this function.

          - `Type Function`

            The tool type. Always `function`.

            - `const FunctionFunction Function = "function"`

          - `Description string`

            What the function does and when the delegated Responses model should call it.

          - `Parameters map[string, any]`

            A JSON Schema object describing the arguments accepted by the function.

          - `Strict bool`

            Whether the delegated Responses model must follow the function’s parameter schema exactly.

        - `ResponsesDelegationUpdateConfigToolWebSearch`

          - `Type WebSearch`

            The tool type. Always `web_search`.

            - `const WebSearchWebSearch WebSearch = "web_search"`

  - `Store bool`

    Whether to store the forked session. Omission inherits the stored session's setting.

### Fork Session Start Event

- `type ForkSessionStartEvent struct{…}`

  Start a Live session after connecting to a stored session’s fork WebSocket. Send an empty `session` object to use the stored configuration.

  - `Session ForkSessionConfig`

    Overrides for a stored session after connecting to the fork WebSocket. An empty object inherits the stored configuration; do not supply a new model. audio.format applies only to the new WebSocket connection. client overrides are only supported for WebRTC forks.

    - `Audio ForkSessionConfigAudio`

      Audio format for a WebSocket fork. WebRTC forks negotiate their audio format and must omit this field.

      - `Format AudioFormatUnion`

        Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

        - `AudioFormatAudioPCM`

          - `Rate int64`

            Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

            - `const AudioFormatAudioPCMRate16000 AudioFormatAudioPCMRate = 16000`

            - `const AudioFormatAudioPCMRate24000 AudioFormatAudioPCMRate = 24000`

          - `Type AudioPCM`

            The audio encoding. Always `audio/pcm`.

            - `const AudioPCMAudioPCM AudioPCM = "audio/pcm"`

        - `AudioFormatAudioPCMU`

          - `Rate int64`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `Type AudioPCMU`

            The audio encoding. Always `audio/pcmu`.

            - `const AudioPCMUAudioPCMU AudioPCMU = "audio/pcmu"`

        - `AudioFormatAudioPCMA`

          - `Rate int64`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `Type AudioPCMA`

            The audio encoding. Always `audio/pcma`.

            - `const AudioPCMAAudioPCMA AudioPCMA = "audio/pcma"`

    - `Client ClientConfig`

      Frontend data-channel permissions for a WebRTC fork. Omitted permissions inherit the stored values. Not supported for WebSocket forks.

      - `DataChannel DataChannelConfig`

        Client and server event permissions for the WebRTC frontend data channel.

        - `AllowedClientEvents DataChannelConfigAllowedClientEventsUnion`

          Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

          - `All`

            - `const AllAll All = "all"`

          - `[]string`

        - `AllowedServerEvents DataChannelConfigAllowedServerEventsUnion`

          Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

          - `All`

            - `const AllAll All = "all"`

          - `[]ServerEventSelector`

            - `Type string`

              The outer Live server event type. Use 'response.event' for Responses events.

            - `ResponseEvent string`

              The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

    - `Delegation ForkSessionConfigDelegation`

      Overrides for the stored session’s Responses backend. Only supported when the stored session already uses Responses delegation; the delegation type cannot change.

      - `Type Responses`

        The delegation owner. Always `responses` for tasks handled by the Responses API.

        - `const ResponsesResponses Responses = "responses"`

      - `Responses ResponsesDelegationUpdateConfig`

        Responses backend settings to update. Omitted settings keep their existing values.

        - `Instructions string`

          Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

        - `MaxOutputTokens int64`

          Maximum number of output tokens for each delegated response.

        - `Model string`

          The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.

        - `ParallelToolCalls bool`

          Whether the delegated Responses model may request multiple tool calls in a single response.

        - `Reasoning ResponsesDelegationUpdateConfigReasoning`

          Reasoning settings passed to each delegated Responses request.

          - `Effort string`

            How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

            - `const ResponsesDelegationUpdateConfigReasoningEffortNone ResponsesDelegationUpdateConfigReasoningEffort = "none"`

            - `const ResponsesDelegationUpdateConfigReasoningEffortMinimal ResponsesDelegationUpdateConfigReasoningEffort = "minimal"`

            - `const ResponsesDelegationUpdateConfigReasoningEffortLow ResponsesDelegationUpdateConfigReasoningEffort = "low"`

            - `const ResponsesDelegationUpdateConfigReasoningEffortMedium ResponsesDelegationUpdateConfigReasoningEffort = "medium"`

            - `const ResponsesDelegationUpdateConfigReasoningEffortHigh ResponsesDelegationUpdateConfigReasoningEffort = "high"`

            - `const ResponsesDelegationUpdateConfigReasoningEffortXhigh ResponsesDelegationUpdateConfigReasoningEffort = "xhigh"`

          - `Summary string`

            The reasoning summary to request from the delegated Responses model, when supported.

            - `const ResponsesDelegationUpdateConfigReasoningSummaryConcise ResponsesDelegationUpdateConfigReasoningSummary = "concise"`

            - `const ResponsesDelegationUpdateConfigReasoningSummaryDetailed ResponsesDelegationUpdateConfigReasoningSummary = "detailed"`

            - `const ResponsesDelegationUpdateConfigReasoningSummaryAuto ResponsesDelegationUpdateConfigReasoningSummary = "auto"`

        - `ServiceTier ResponsesDelegationUpdateConfigServiceTier`

          Service tier for delegated Responses requests.

          - `const ResponsesDelegationUpdateConfigServiceTierAuto ResponsesDelegationUpdateConfigServiceTier = "auto"`

          - `const ResponsesDelegationUpdateConfigServiceTierDefault ResponsesDelegationUpdateConfigServiceTier = "default"`

          - `const ResponsesDelegationUpdateConfigServiceTierFastTierTempPilot ResponsesDelegationUpdateConfigServiceTier = "fast_tier_temp_pilot"`

          - `const ResponsesDelegationUpdateConfigServiceTierFlex ResponsesDelegationUpdateConfigServiceTier = "flex"`

          - `const ResponsesDelegationUpdateConfigServiceTierPriority ResponsesDelegationUpdateConfigServiceTier = "priority"`

          - `const ResponsesDelegationUpdateConfigServiceTierUltrafast ResponsesDelegationUpdateConfigServiceTier = "ultrafast"`

        - `Text ResponsesDelegationUpdateConfigText`

          Text generation settings passed to each delegated Responses request.

          - `Verbosity string`

            The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

            - `const ResponsesDelegationUpdateConfigTextVerbosityLow ResponsesDelegationUpdateConfigTextVerbosity = "low"`

            - `const ResponsesDelegationUpdateConfigTextVerbosityMedium ResponsesDelegationUpdateConfigTextVerbosity = "medium"`

            - `const ResponsesDelegationUpdateConfigTextVerbosityHigh ResponsesDelegationUpdateConfigTextVerbosity = "high"`

        - `ToolChoice ResponsesDelegationUpdateConfigToolChoiceUnion`

          Controls which tool the Responses backend uses when handling a task delegated by the Live model.

          - `string`

            - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "auto"`

            - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "none"`

            - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "required"`

          - `ResponsesDelegationUpdateConfigToolChoiceLiveFunctionToolChoiceParam`

            - `Name string`

            - `Type Function`

              - `const FunctionFunction Function = "function"`

          - `ResponsesDelegationUpdateConfigToolChoiceLiveMcpToolChoiceParam`

            - `Name string`

            - `ServerLabel string`

            - `Type Mcp`

              - `const McpMcp Mcp = "mcp"`

        - `Tools []ResponsesDelegationUpdateConfigToolUnion`

          Tools available to the Responses backend while it handles tasks delegated by the Live model.

          - `type FunctionTool struct{…}`

            A function tool available to the Responses backend when the Live model delegates a task.

            - `Name string`

              The name the delegated Responses model uses when calling this function.

            - `Type Function`

              The tool type. Always `function`.

              - `const FunctionFunction Function = "function"`

            - `Description string`

              What the function does and when the delegated Responses model should call it.

            - `Parameters map[string, any]`

              A JSON Schema object describing the arguments accepted by the function.

            - `Strict bool`

              Whether the delegated Responses model must follow the function’s parameter schema exactly.

          - `ResponsesDelegationUpdateConfigToolWebSearch`

            - `Type WebSearch`

              The tool type. Always `web_search`.

              - `const WebSearchWebSearch WebSearch = "web_search"`

    - `Store bool`

      Whether to store the forked session. Omission inherits the stored session's setting.

  - `Type SessionStart`

    The Live client event type. Always `session.start`.

    - `const SessionStartSessionStart SessionStart = "session.start"`

  - `EventID string`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Function Tool

- `type FunctionTool struct{…}`

  A function tool available to the Responses backend when the Live model delegates a task.

  - `Name string`

    The name the delegated Responses model uses when calling this function.

  - `Type Function`

    The tool type. Always `function`.

    - `const FunctionFunction Function = "function"`

  - `Description string`

    What the function does and when the delegated Responses model should call it.

  - `Parameters map[string, any]`

    A JSON Schema object describing the arguments accepted by the function.

  - `Strict bool`

    Whether the delegated Responses model must follow the function’s parameter schema exactly.

### Info Event

- `type InfoEvent struct{…}`

  An informational notice about the Live session, such as the event permissions applied to a frontend data channel.

  - `Code string`

    A machine-readable code for the notice, such as `data_channel_permissions`.

  - `EventID string`

    The unique ID of the Live server event.

  - `Message string`

    A human-readable explanation of the Live session notice.

  - `Type Info`

    The event type, always `info`.

    - `const InfoInfo Info = "info"`

  - `ClientEventID string`

    The event_id of the client command associated with this server event, when supplied.

### Initial Item

- `type InitialItemUnion interface{…}`

  A developer, user, or assistant message supplied as text history before the Live session starts.

  - `InitialItemDeveloper`

    - `Content []InitialItemDeveloperContent`

      The message content. Supply exactly one text part for the initial Live conversation history.

      - `Text string`

        The message text to include in the Live session’s initial conversation history.

      - `Type string`

        The text content type. Always `input_text`.

        - `const InitialItemDeveloperContentTypeInputText InitialItemDeveloperContentType = "input_text"`

    - `Role Developer`

      The author of this history message. Always `developer`.

      - `const DeveloperDeveloper Developer = "developer"`

    - `ID string`

      An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

    - `Status string`

      The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

      - `const InitialItemDeveloperStatusIncomplete InitialItemDeveloperStatus = "incomplete"`

      - `const InitialItemDeveloperStatusCompleted InitialItemDeveloperStatus = "completed"`

    - `Type string`

      The history item type. Always `message`.

      - `const InitialItemDeveloperTypeMessage InitialItemDeveloperType = "message"`

  - `InitialItemUser`

    - `Content []InitialItemUserContent`

      The message content. Supply exactly one text part for the initial Live conversation history.

      - `Text string`

        The message text to include in the Live session’s initial conversation history.

      - `Type string`

        The text content type. Always `input_text`.

        - `const InitialItemUserContentTypeInputText InitialItemUserContentType = "input_text"`

    - `Role User`

      The author of this history message. Always `user`.

      - `const UserUser User = "user"`

    - `ID string`

      An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

    - `Status string`

      The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

      - `const InitialItemUserStatusIncomplete InitialItemUserStatus = "incomplete"`

      - `const InitialItemUserStatusCompleted InitialItemUserStatus = "completed"`

    - `Type string`

      The history item type. Always `message`.

      - `const InitialItemUserTypeMessage InitialItemUserType = "message"`

  - `InitialItemAssistant`

    - `Content []InitialItemAssistantContentUnion`

      The message content. Supply exactly one text part for the initial Live conversation history.

      - `InitialItemAssistantContentText`

        - `Text string`

          The message text to include in the Live session’s initial conversation history.

        - `Type string`

          The text content type. Always `text`.

          - `const InitialItemAssistantContentTextTypeText InitialItemAssistantContentTextType = "text"`

      - `InitialItemAssistantContentOutputText`

        - `Text string`

          The message text to include in the Live session’s initial conversation history.

        - `Type OutputText`

          The text content type. Always `output_text`.

          - `const OutputTextOutputText OutputText = "output_text"`

    - `Role Assistant`

      The author of this history message. Always `assistant`.

      - `const AssistantAssistant Assistant = "assistant"`

    - `ID string`

      An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

    - `Status string`

      The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

      - `const InitialItemAssistantStatusIncomplete InitialItemAssistantStatus = "incomplete"`

      - `const InitialItemAssistantStatusCompleted InitialItemAssistantStatus = "completed"`

    - `Type string`

      The history item type. Always `message`.

      - `const InitialItemAssistantTypeMessage InitialItemAssistantType = "message"`

### Input Audio Append Event

- `type InputAudioAppendEvent struct{…}`

  Send audio to a Live session over its primary WebSocket. WebRTC and SIP sessions send audio over their media transport.

  - `Audio string`

    Base64-encoded raw audio in the startup-selected format, without a WAV or other container header. Primary WebSocket only; media transports use their audio track. Audio appends have no acknowledgment. Reflected sideband server events reuse this event type and audio key, with no timestamps or event_id; their audio is always mono PCM16LE at 24 kHz.

  - `Type SessionInputAudioAppend`

    The Live client event type. Always `session.input_audio.append`.

    - `const SessionInputAudioAppendSessionInputAudioAppend SessionInputAudioAppend = "session.input_audio.append"`

  - `EventID string`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Input Audio Mute Event

- `type InputAudioMuteEvent struct{…}`

  Mute audio input to the Live model without closing the session. The server acknowledges with `session.input_audio.muted`.

  - `Type SessionInputAudioMute`

    The Live client event type. Always `session.input_audio.mute`.

    - `const SessionInputAudioMuteSessionInputAudioMute SessionInputAudioMute = "session.input_audio.mute"`

  - `EventID string`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Input Audio Muted Event

- `type InputAudioMutedEvent struct{…}`

  Returned when a session.input_audio.mute command is accepted. Input audio is no longer sent to the model; sideband audio reflection continues.

  - `EventID string`

    The unique ID of the Live server event.

  - `Type SessionInputAudioMuted`

    The event type, always `session.input_audio.muted`.

    - `const SessionInputAudioMutedSessionInputAudioMuted SessionInputAudioMuted = "session.input_audio.muted"`

  - `ClientEventID string`

    The event_id of the client command associated with this server event, when supplied.

### Input Audio Unmute Event

- `type InputAudioUnmuteEvent struct{…}`

  Resume audio input to a Live model after muting it. The server acknowledges with `session.input_audio.unmuted`.

  - `Type SessionInputAudioUnmute`

    The Live client event type. Always `session.input_audio.unmute`.

    - `const SessionInputAudioUnmuteSessionInputAudioUnmute SessionInputAudioUnmute = "session.input_audio.unmute"`

  - `EventID string`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Input Audio Unmuted Event

- `type InputAudioUnmutedEvent struct{…}`

  Returned when a session.input_audio.unmute command is accepted. Input audio is sent to the model again.

  - `EventID string`

    The unique ID of the Live server event.

  - `Type SessionInputAudioUnmuted`

    The event type, always `session.input_audio.unmuted`.

    - `const SessionInputAudioUnmutedSessionInputAudioUnmuted SessionInputAudioUnmuted = "session.input_audio.unmuted"`

  - `ClientEventID string`

    The event_id of the client command associated with this server event, when supplied.

### Input Transcript Delta Event

- `type InputTranscriptDeltaEvent struct{…}`

  A transcript fragment for user input audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

  - `Delta string`

    The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

  - `EndMs int64`

    The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

  - `EventID string`

    The unique ID of the Live server event.

  - `StartMs int64`

    The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

  - `Type SessionInputTranscriptDelta`

    The event type, always `session.input_transcript.delta`.

    - `const SessionInputTranscriptDeltaSessionInputTranscriptDelta SessionInputTranscriptDelta = "session.input_transcript.delta"`

  - `ClientEventID string`

    The event_id of the client command associated with this server event, when supplied.

### Instructions Append Event

- `type InstructionsAppendEvent struct{…}`

  Append instructions to the Live conversation while it is running, optionally associating them with an existing client delegation.

  - `Content string`

    Instruction text to append, limited to 500 tokens. This is a plain string, not an array of content parts.

  - `DelegationID string`

    Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

  - `Type SessionInstructionsAppend`

    The Live client event type. Always `session.instructions.append`.

    - `const SessionInstructionsAppendSessionInstructionsAppend SessionInstructionsAppend = "session.instructions.append"`

  - `EventID string`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Instructions Appended Event

- `type InstructionsAppendedEvent struct{…}`

  Returned when a session.instructions.append command is accepted into the Live session timeline. Acknowledges the appended instructions without guaranteeing that the model has acted on them.

  - `EndMs int64`

    The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

  - `EventID string`

    The unique ID of the Live server event.

  - `StartMs int64`

    The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

  - `Type SessionInstructionsAppended`

    The event type, always `session.instructions.appended`.

    - `const SessionInstructionsAppendedSessionInstructionsAppended SessionInstructionsAppended = "session.instructions.appended"`

  - `ClientEventID string`

    The event_id of the client command associated with this server event, when supplied.

### Media Session Config

- `type MediaSessionConfig struct{…}`

  Startup configuration for a Live media session. Follow the [Live prompting guide](https://developers.openai.com/api/docs/guides/live-prompting) when writing frontend instructions and the backend prompt under delegation.responses.instructions.

  - `Model MediaSessionConfigModel`

    The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

    - `string`

    - `MediaSessionConfigModel`

      - `const MediaSessionConfigModelGPTLive1 MediaSessionConfigModel = "gpt-live-1"`

  - `Audio MediaSessionConfigAudio`

    Startup audio configuration. WebRTC and SIP negotiate their audio format on the media transport.

    - `Output MediaSessionConfigAudioOutput`

      Settings for speech generated by the Live model. Choose the voice before starting the session.

      - `Voice MediaSessionConfigAudioOutputVoiceUnion`

        The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

        - `string`

        - `type BuiltInVoice string`

          A built-in voice available for Live speech.

          - `const BuiltInVoiceAlloy BuiltInVoice = "alloy"`

          - `const BuiltInVoiceAsh BuiltInVoice = "ash"`

          - `const BuiltInVoiceBallad BuiltInVoice = "ballad"`

          - `const BuiltInVoiceBeacon BuiltInVoice = "beacon"`

          - `const BuiltInVoiceBossa BuiltInVoice = "bossa"`

          - `const BuiltInVoiceCedar BuiltInVoice = "cedar"`

          - `const BuiltInVoiceCinder BuiltInVoice = "cinder"`

          - `const BuiltInVoiceCoral BuiltInVoice = "coral"`

          - `const BuiltInVoiceDelta BuiltInVoice = "delta"`

          - `const BuiltInVoiceEcho BuiltInVoice = "echo"`

          - `const BuiltInVoiceGleam BuiltInVoice = "gleam"`

          - `const BuiltInVoiceMarin BuiltInVoice = "marin"`

          - `const BuiltInVoiceMeridian BuiltInVoice = "meridian"`

          - `const BuiltInVoiceQuartz BuiltInVoice = "quartz"`

          - `const BuiltInVoiceRipple BuiltInVoice = "ripple"`

          - `const BuiltInVoiceSage BuiltInVoice = "sage"`

          - `const BuiltInVoiceShimmer BuiltInVoice = "shimmer"`

          - `const BuiltInVoiceStone BuiltInVoice = "stone"`

          - `const BuiltInVoiceTempo BuiltInVoice = "tempo"`

          - `const BuiltInVoiceVerse BuiltInVoice = "verse"`

          - `const BuiltInVoiceVesper BuiltInVoice = "vesper"`

          - `const BuiltInVoiceWillow BuiltInVoice = "willow"`

        - `type CustomVoice struct{…}`

          - `ID string`

  - `Client ClientConfig`

    Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

    - `DataChannel DataChannelConfig`

      Client and server event permissions for the WebRTC frontend data channel.

      - `AllowedClientEvents DataChannelConfigAllowedClientEventsUnion`

        Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

        - `All`

          - `const AllAll All = "all"`

        - `[]string`

      - `AllowedServerEvents DataChannelConfigAllowedServerEventsUnion`

        Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

        - `All`

          - `const AllAll All = "all"`

        - `[]ServerEventSelector`

          - `Type string`

            The outer Live server event type. Use 'response.event' for Responses events.

          - `ResponseEvent string`

            The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

  - `Delegation MediaSessionConfigDelegationUnion`

    Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

    - `type ClientDelegation struct{…}`

      Delegate tasks to your application. The Live session emits delegation events that your backend handles.

      - `Type Client`

        The delegation owner. Always `client` for tasks handled by your application.

        - `const ClientClient Client = "client"`

    - `MediaSessionConfigDelegationResponses`

      - `Responses ResponsesDelegationConfig`

        Backend model, prompt, and tools used when the Live session delegates a task to Responses.

        - `Model string`

          The model used for server-owned Responses delegations.

        - `Instructions string`

          Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

        - `MaxOutputTokens int64`

          Maximum number of output tokens for each delegated response.

        - `ParallelToolCalls bool`

          Whether the delegated Responses model may request multiple tool calls in a single response.

        - `Reasoning ResponsesDelegationConfigReasoning`

          Reasoning settings passed to each delegated Responses request.

          - `Effort string`

            How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

            - `const ResponsesDelegationConfigReasoningEffortNone ResponsesDelegationConfigReasoningEffort = "none"`

            - `const ResponsesDelegationConfigReasoningEffortMinimal ResponsesDelegationConfigReasoningEffort = "minimal"`

            - `const ResponsesDelegationConfigReasoningEffortLow ResponsesDelegationConfigReasoningEffort = "low"`

            - `const ResponsesDelegationConfigReasoningEffortMedium ResponsesDelegationConfigReasoningEffort = "medium"`

            - `const ResponsesDelegationConfigReasoningEffortHigh ResponsesDelegationConfigReasoningEffort = "high"`

            - `const ResponsesDelegationConfigReasoningEffortXhigh ResponsesDelegationConfigReasoningEffort = "xhigh"`

          - `Summary string`

            The reasoning summary to request from the delegated Responses model, when supported.

            - `const ResponsesDelegationConfigReasoningSummaryConcise ResponsesDelegationConfigReasoningSummary = "concise"`

            - `const ResponsesDelegationConfigReasoningSummaryDetailed ResponsesDelegationConfigReasoningSummary = "detailed"`

            - `const ResponsesDelegationConfigReasoningSummaryAuto ResponsesDelegationConfigReasoningSummary = "auto"`

        - `ServiceTier ResponsesDelegationConfigServiceTier`

          Service tier for delegated Responses requests.

          - `const ResponsesDelegationConfigServiceTierAuto ResponsesDelegationConfigServiceTier = "auto"`

          - `const ResponsesDelegationConfigServiceTierDefault ResponsesDelegationConfigServiceTier = "default"`

          - `const ResponsesDelegationConfigServiceTierFastTierTempPilot ResponsesDelegationConfigServiceTier = "fast_tier_temp_pilot"`

          - `const ResponsesDelegationConfigServiceTierFlex ResponsesDelegationConfigServiceTier = "flex"`

          - `const ResponsesDelegationConfigServiceTierPriority ResponsesDelegationConfigServiceTier = "priority"`

          - `const ResponsesDelegationConfigServiceTierUltrafast ResponsesDelegationConfigServiceTier = "ultrafast"`

        - `Text ResponsesDelegationConfigText`

          Text generation settings passed to each delegated Responses request.

          - `Verbosity string`

            The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

            - `const ResponsesDelegationConfigTextVerbosityLow ResponsesDelegationConfigTextVerbosity = "low"`

            - `const ResponsesDelegationConfigTextVerbosityMedium ResponsesDelegationConfigTextVerbosity = "medium"`

            - `const ResponsesDelegationConfigTextVerbosityHigh ResponsesDelegationConfigTextVerbosity = "high"`

        - `ToolChoice ResponsesDelegationConfigToolChoiceUnion`

          Controls which tool the Responses backend uses when handling a task delegated by the Live model.

          - `string`

            - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "auto"`

            - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "none"`

            - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "required"`

          - `ResponsesDelegationConfigToolChoiceLiveFunctionToolChoiceParam`

            - `Name string`

            - `Type Function`

              - `const FunctionFunction Function = "function"`

          - `ResponsesDelegationConfigToolChoiceLiveMcpToolChoiceParam`

            - `Name string`

            - `ServerLabel string`

            - `Type Mcp`

              - `const McpMcp Mcp = "mcp"`

        - `Tools []ResponsesDelegationConfigToolUnion`

          Tools available to the Responses backend while it handles tasks delegated by the Live model.

          - `type FunctionTool struct{…}`

            A function tool available to the Responses backend when the Live model delegates a task.

            - `Name string`

              The name the delegated Responses model uses when calling this function.

            - `Type Function`

              The tool type. Always `function`.

              - `const FunctionFunction Function = "function"`

            - `Description string`

              What the function does and when the delegated Responses model should call it.

            - `Parameters map[string, any]`

              A JSON Schema object describing the arguments accepted by the function.

            - `Strict bool`

              Whether the delegated Responses model must follow the function’s parameter schema exactly.

          - `ResponsesDelegationConfigToolWebSearch`

            - `Type WebSearch`

              The tool type. Always `web_search`.

              - `const WebSearchWebSearch WebSearch = "web_search"`

      - `Type Responses`

        The delegation owner. Always `responses` for tasks handled by the Responses API.

        - `const ResponsesResponses Responses = "responses"`

  - `Input []InitialItemUnion`

    Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

    - `InitialItemDeveloper`

      - `Content []InitialItemDeveloperContent`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `Text string`

          The message text to include in the Live session’s initial conversation history.

        - `Type string`

          The text content type. Always `input_text`.

          - `const InitialItemDeveloperContentTypeInputText InitialItemDeveloperContentType = "input_text"`

      - `Role Developer`

        The author of this history message. Always `developer`.

        - `const DeveloperDeveloper Developer = "developer"`

      - `ID string`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Status string`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `const InitialItemDeveloperStatusIncomplete InitialItemDeveloperStatus = "incomplete"`

        - `const InitialItemDeveloperStatusCompleted InitialItemDeveloperStatus = "completed"`

      - `Type string`

        The history item type. Always `message`.

        - `const InitialItemDeveloperTypeMessage InitialItemDeveloperType = "message"`

    - `InitialItemUser`

      - `Content []InitialItemUserContent`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `Text string`

          The message text to include in the Live session’s initial conversation history.

        - `Type string`

          The text content type. Always `input_text`.

          - `const InitialItemUserContentTypeInputText InitialItemUserContentType = "input_text"`

      - `Role User`

        The author of this history message. Always `user`.

        - `const UserUser User = "user"`

      - `ID string`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Status string`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `const InitialItemUserStatusIncomplete InitialItemUserStatus = "incomplete"`

        - `const InitialItemUserStatusCompleted InitialItemUserStatus = "completed"`

      - `Type string`

        The history item type. Always `message`.

        - `const InitialItemUserTypeMessage InitialItemUserType = "message"`

    - `InitialItemAssistant`

      - `Content []InitialItemAssistantContentUnion`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `InitialItemAssistantContentText`

          - `Text string`

            The message text to include in the Live session’s initial conversation history.

          - `Type string`

            The text content type. Always `text`.

            - `const InitialItemAssistantContentTextTypeText InitialItemAssistantContentTextType = "text"`

        - `InitialItemAssistantContentOutputText`

          - `Text string`

            The message text to include in the Live session’s initial conversation history.

          - `Type OutputText`

            The text content type. Always `output_text`.

            - `const OutputTextOutputText OutputText = "output_text"`

      - `Role Assistant`

        The author of this history message. Always `assistant`.

        - `const AssistantAssistant Assistant = "assistant"`

      - `ID string`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Status string`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `const InitialItemAssistantStatusIncomplete InitialItemAssistantStatus = "incomplete"`

        - `const InitialItemAssistantStatusCompleted InitialItemAssistantStatus = "completed"`

      - `Type string`

        The history item type. Always `message`.

        - `const InitialItemAssistantTypeMessage InitialItemAssistantType = "message"`

  - `Instructions string`

    Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

  - `Store bool`

    Whether to store the session for later forking and recording download. Defaults to false for new sessions.

### Media Session Fork Config

- `type MediaSessionForkConfig struct{…}`

  Optional overrides for a stored Live session. Omitted settings are inherited. The model, voice, frontend instructions, and prior conversation come from the stored session. WebRTC negotiates its audio format; audio.format is only supported on WebSocket forks.

  - `Client ClientConfig`

    Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

    - `DataChannel DataChannelConfig`

      Client and server event permissions for the WebRTC frontend data channel.

      - `AllowedClientEvents DataChannelConfigAllowedClientEventsUnion`

        Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

        - `All`

          - `const AllAll All = "all"`

        - `[]string`

      - `AllowedServerEvents DataChannelConfigAllowedServerEventsUnion`

        Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

        - `All`

          - `const AllAll All = "all"`

        - `[]ServerEventSelector`

          - `Type string`

            The outer Live server event type. Use 'response.event' for Responses events.

          - `ResponseEvent string`

            The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

  - `Delegation MediaSessionForkConfigDelegation`

    Update the Responses backend for an existing Live session without changing delegation ownership.

    - `Type Responses`

      The delegation owner. Always `responses` for tasks handled by the Responses API.

      - `const ResponsesResponses Responses = "responses"`

    - `Responses ResponsesDelegationUpdateConfig`

      Responses backend settings to update. Omitted settings keep their existing values.

      - `Instructions string`

        Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

      - `MaxOutputTokens int64`

        Maximum number of output tokens for each delegated response.

      - `Model string`

        The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.

      - `ParallelToolCalls bool`

        Whether the delegated Responses model may request multiple tool calls in a single response.

      - `Reasoning ResponsesDelegationUpdateConfigReasoning`

        Reasoning settings passed to each delegated Responses request.

        - `Effort string`

          How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

          - `const ResponsesDelegationUpdateConfigReasoningEffortNone ResponsesDelegationUpdateConfigReasoningEffort = "none"`

          - `const ResponsesDelegationUpdateConfigReasoningEffortMinimal ResponsesDelegationUpdateConfigReasoningEffort = "minimal"`

          - `const ResponsesDelegationUpdateConfigReasoningEffortLow ResponsesDelegationUpdateConfigReasoningEffort = "low"`

          - `const ResponsesDelegationUpdateConfigReasoningEffortMedium ResponsesDelegationUpdateConfigReasoningEffort = "medium"`

          - `const ResponsesDelegationUpdateConfigReasoningEffortHigh ResponsesDelegationUpdateConfigReasoningEffort = "high"`

          - `const ResponsesDelegationUpdateConfigReasoningEffortXhigh ResponsesDelegationUpdateConfigReasoningEffort = "xhigh"`

        - `Summary string`

          The reasoning summary to request from the delegated Responses model, when supported.

          - `const ResponsesDelegationUpdateConfigReasoningSummaryConcise ResponsesDelegationUpdateConfigReasoningSummary = "concise"`

          - `const ResponsesDelegationUpdateConfigReasoningSummaryDetailed ResponsesDelegationUpdateConfigReasoningSummary = "detailed"`

          - `const ResponsesDelegationUpdateConfigReasoningSummaryAuto ResponsesDelegationUpdateConfigReasoningSummary = "auto"`

      - `ServiceTier ResponsesDelegationUpdateConfigServiceTier`

        Service tier for delegated Responses requests.

        - `const ResponsesDelegationUpdateConfigServiceTierAuto ResponsesDelegationUpdateConfigServiceTier = "auto"`

        - `const ResponsesDelegationUpdateConfigServiceTierDefault ResponsesDelegationUpdateConfigServiceTier = "default"`

        - `const ResponsesDelegationUpdateConfigServiceTierFastTierTempPilot ResponsesDelegationUpdateConfigServiceTier = "fast_tier_temp_pilot"`

        - `const ResponsesDelegationUpdateConfigServiceTierFlex ResponsesDelegationUpdateConfigServiceTier = "flex"`

        - `const ResponsesDelegationUpdateConfigServiceTierPriority ResponsesDelegationUpdateConfigServiceTier = "priority"`

        - `const ResponsesDelegationUpdateConfigServiceTierUltrafast ResponsesDelegationUpdateConfigServiceTier = "ultrafast"`

      - `Text ResponsesDelegationUpdateConfigText`

        Text generation settings passed to each delegated Responses request.

        - `Verbosity string`

          The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

          - `const ResponsesDelegationUpdateConfigTextVerbosityLow ResponsesDelegationUpdateConfigTextVerbosity = "low"`

          - `const ResponsesDelegationUpdateConfigTextVerbosityMedium ResponsesDelegationUpdateConfigTextVerbosity = "medium"`

          - `const ResponsesDelegationUpdateConfigTextVerbosityHigh ResponsesDelegationUpdateConfigTextVerbosity = "high"`

      - `ToolChoice ResponsesDelegationUpdateConfigToolChoiceUnion`

        Controls which tool the Responses backend uses when handling a task delegated by the Live model.

        - `string`

          - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "auto"`

          - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "none"`

          - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "required"`

        - `ResponsesDelegationUpdateConfigToolChoiceLiveFunctionToolChoiceParam`

          - `Name string`

          - `Type Function`

            - `const FunctionFunction Function = "function"`

        - `ResponsesDelegationUpdateConfigToolChoiceLiveMcpToolChoiceParam`

          - `Name string`

          - `ServerLabel string`

          - `Type Mcp`

            - `const McpMcp Mcp = "mcp"`

      - `Tools []ResponsesDelegationUpdateConfigToolUnion`

        Tools available to the Responses backend while it handles tasks delegated by the Live model.

        - `type FunctionTool struct{…}`

          A function tool available to the Responses backend when the Live model delegates a task.

          - `Name string`

            The name the delegated Responses model uses when calling this function.

          - `Type Function`

            The tool type. Always `function`.

            - `const FunctionFunction Function = "function"`

          - `Description string`

            What the function does and when the delegated Responses model should call it.

          - `Parameters map[string, any]`

            A JSON Schema object describing the arguments accepted by the function.

          - `Strict bool`

            Whether the delegated Responses model must follow the function’s parameter schema exactly.

        - `ResponsesDelegationUpdateConfigToolWebSearch`

          - `Type WebSearch`

            The tool type. Always `web_search`.

            - `const WebSearchWebSearch WebSearch = "web_search"`

  - `Store bool`

    Whether to store the forked session. Omission inherits the stored session's setting.

### Output Audio Delta Event

- `type OutputAudioDeltaEvent struct{…}`

  An audio chunk generated by the Live model. Decode and play primary WebSocket chunks in delivery order using the configured session audio format. Sideband connections receive reflected output audio with timestamps.

  - `Delta string`

    Base64-encoded raw audio. Primary WebSocket events use the session's configured format; reflected sideband events use mono PCM16LE at 24 kHz.

  - `Type SessionOutputAudioDelta`

    The event type, always `session.output_audio.delta`.

    - `const SessionOutputAudioDeltaSessionOutputAudioDelta SessionOutputAudioDelta = "session.output_audio.delta"`

  - `EndMs int64`

    Exclusive session-relative end in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket. Dropped output frames leave gaps between reflected ranges.

  - `StartMs int64`

    Inclusive session-relative start in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket.

### Output Transcript Delta Event

- `type OutputTranscriptDeltaEvent struct{…}`

  A transcript fragment for assistant output audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

  - `Delta string`

    The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

  - `EndMs int64`

    The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

  - `EventID string`

    The unique ID of the Live server event.

  - `StartMs int64`

    The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

  - `Type SessionOutputTranscriptDelta`

    The event type, always `session.output_transcript.delta`.

    - `const SessionOutputTranscriptDeltaSessionOutputTranscriptDelta SessionOutputTranscriptDelta = "session.output_transcript.delta"`

  - `ClientEventID string`

    The event_id of the client command associated with this server event, when supplied.

### Response Create Event

- `type ResponseCreateEvent struct{…}`

  Request a response from the Live session’s Responses backend, or continue a delegated response waiting for tool results. Requires Responses delegation.

  - `Type ResponseCreate`

    The Live client event type. Always `response.create`.

    - `const ResponseCreateResponseCreate ResponseCreate = "response.create"`

  - `EventID string`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Response Event

- `type ResponseEvent struct{…}`

  A streaming Responses API event from a backend delegated to by the Live session. Use the outer delegation_id to associate the nested stream with its Live delegation.

  - `Event map[string, any]`

    The nested Responses streaming event. Dispatch on its type field. Response lifecycle snapshots omit input and clear instructions, tools, and output to keep messages small; consume granular output events for the generated content.

  - `EventID string`

    The unique ID of the Live server event.

  - `Type ResponseEvent`

    The event type, always `response.event`.

    - `const ResponseEventResponseEvent ResponseEvent = "response.event"`

  - `ClientEventID string`

    The event_id of the client command associated with this server event, when supplied.

  - `DelegationID string`

    The Live delegation associated with the nested Responses event. May be null or omitted when the event cannot be correlated with a delegation.

### Response Item Create Event

- `type ResponseItemCreateEvent struct{…}`

  Add an input item to the Live session’s Responses backend. Requires Responses delegation; use `response.create` to request a response.

  - `Item ResponseInputItemUnion`

    An input item to append to the Responses backend conversation, such as a user message or a function tool result.

    - `type EasyInputMessage struct{…}`

      A message input to the model with a role indicating instruction following
      hierarchy. Instructions given with the `developer` or `system` role take
      precedence over instructions given with the `user` role. Messages with the
      `assistant` role are presumed to have been generated by the model in previous
      interactions.

      - `Content EasyInputMessageContentUnion`

        Text, image, or audio input to the model, used to generate a response.
        Can also contain previous assistant responses.

        - `string`

        - `type ResponseInputMessageContentList []ResponseInputContentUnion`

          A list of one or many input items to the model, containing different content
          types.

          - `type ResponseInputText struct{…}`

            A text input to the model.

            - `Text string`

              The text input to the model.

            - `Type InputText`

              The type of the input item. Always `input_text`.

              - `const InputTextInputText InputText = "input_text"`

            - `PromptCacheBreakpoint ResponseInputTextPromptCacheBreakpoint`

              Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

              - `Mode Explicit`

                The breakpoint mode. Always `explicit`.

                - `const ExplicitExplicit Explicit = "explicit"`

          - `type ResponseInputImage struct{…}`

            An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

            - `Detail ResponseInputImageDetail`

              The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

              - `const ResponseInputImageDetailLow ResponseInputImageDetail = "low"`

              - `const ResponseInputImageDetailHigh ResponseInputImageDetail = "high"`

              - `const ResponseInputImageDetailAuto ResponseInputImageDetail = "auto"`

              - `const ResponseInputImageDetailOriginal ResponseInputImageDetail = "original"`

            - `Type InputImage`

              The type of the input item. Always `input_image`.

              - `const InputImageInputImage InputImage = "input_image"`

            - `FileID string`

              The ID of the file to be sent to the model.

            - `ImageURL string`

              The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

            - `PromptCacheBreakpoint ResponseInputImagePromptCacheBreakpoint`

              Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

              - `Mode Explicit`

                The breakpoint mode. Always `explicit`.

                - `const ExplicitExplicit Explicit = "explicit"`

          - `type ResponseInputFile struct{…}`

            A file input to the model.

            - `Type InputFile`

              The type of the input item. Always `input_file`.

              - `const InputFileInputFile InputFile = "input_file"`

            - `Detail ResponseInputFileDetail`

              The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

              - `const ResponseInputFileDetailAuto ResponseInputFileDetail = "auto"`

              - `const ResponseInputFileDetailLow ResponseInputFileDetail = "low"`

              - `const ResponseInputFileDetailHigh ResponseInputFileDetail = "high"`

            - `FileData string`

              The content of the file to be sent to the model.

            - `FileID string`

              The ID of the file to be sent to the model.

            - `FileURL string`

              The URL of the file to be sent to the model.

            - `Filename string`

              The name of the file to be sent to the model.

            - `PromptCacheBreakpoint ResponseInputFilePromptCacheBreakpoint`

              Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

              - `Mode Explicit`

                The breakpoint mode. Always `explicit`.

                - `const ExplicitExplicit Explicit = "explicit"`

      - `Role EasyInputMessageRole`

        The role of the message input. One of `user`, `assistant`, `system`, or
        `developer`.

        - `const EasyInputMessageRoleUser EasyInputMessageRole = "user"`

        - `const EasyInputMessageRoleAssistant EasyInputMessageRole = "assistant"`

        - `const EasyInputMessageRoleSystem EasyInputMessageRole = "system"`

        - `const EasyInputMessageRoleDeveloper EasyInputMessageRole = "developer"`

      - `Phase EasyInputMessagePhase`

        Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
        For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
        phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

        - `const EasyInputMessagePhaseCommentary EasyInputMessagePhase = "commentary"`

        - `const EasyInputMessagePhaseFinalAnswer EasyInputMessagePhase = "final_answer"`

      - `Type EasyInputMessageType`

        The type of the message input. Always `message`.

        - `const EasyInputMessageTypeMessage EasyInputMessageType = "message"`

    - `type ResponseInputItemMessage struct{…}`

      A message input to the model with a role indicating instruction following
      hierarchy. Instructions given with the `developer` or `system` role take
      precedence over instructions given with the `user` role.

      - `Content ResponseInputMessageContentList`

        A list of one or many input items to the model, containing different content
        types.

      - `Role string`

        The role of the message input. One of `user`, `system`, or `developer`.

        - `const ResponseInputItemMessageRoleUser ResponseInputItemMessageRole = "user"`

        - `const ResponseInputItemMessageRoleSystem ResponseInputItemMessageRole = "system"`

        - `const ResponseInputItemMessageRoleDeveloper ResponseInputItemMessageRole = "developer"`

      - `Status string`

        The status of item. One of `in_progress`, `completed`, or
        `incomplete`. Populated when items are returned via API.

        - `const ResponseInputItemMessageStatusInProgress ResponseInputItemMessageStatus = "in_progress"`

        - `const ResponseInputItemMessageStatusCompleted ResponseInputItemMessageStatus = "completed"`

        - `const ResponseInputItemMessageStatusIncomplete ResponseInputItemMessageStatus = "incomplete"`

      - `Type string`

        The type of the message input. Always set to `message`.

        - `const ResponseInputItemMessageTypeMessage ResponseInputItemMessageType = "message"`

    - `type ResponseOutputMessage struct{…}`

      An output message from the model.

      - `ID string`

        The unique ID of the output message.

      - `Content []ResponseOutputMessageContentUnion`

        The content of the output message.

        - `type ResponseOutputText struct{…}`

          A text output from the model.

          - `Annotations []ResponseOutputTextAnnotationUnion`

            The annotations of the text output.

            - `type ResponseOutputTextAnnotationFileCitation struct{…}`

              A citation to a file.

              - `FileID string`

                The ID of the file.

              - `Filename string`

                The filename of the file cited.

              - `Index int64`

                The index in the output text at which to insert the file citation.

              - `Type FileCitation`

                The type of the file citation. Always `file_citation`.

                - `const FileCitationFileCitation FileCitation = "file_citation"`

            - `type ResponseOutputTextAnnotationURLCitation struct{…}`

              A citation for a web resource used to generate a model response.

              - `EndIndex int64`

                The index of the last character of the URL citation in the message.

              - `StartIndex int64`

                The index of the first character of the URL citation in the message.

              - `Title string`

                The title of the web resource.

              - `Type URLCitation`

                The type of the URL citation. Always `url_citation`.

                - `const URLCitationURLCitation URLCitation = "url_citation"`

              - `URL string`

                The URL of the web resource.

            - `type ResponseOutputTextAnnotationContainerFileCitation struct{…}`

              A citation for a container file used to generate a model response.

              - `ContainerID string`

                The ID of the container file.

              - `EndIndex int64`

                The index of the last character of the container file citation in the message.

              - `FileID string`

                The ID of the file.

              - `Filename string`

                The filename of the container file cited.

              - `StartIndex int64`

                The index of the first character of the container file citation in the message.

              - `Type ContainerFileCitation`

                The type of the container file citation. Always `container_file_citation`.

                - `const ContainerFileCitationContainerFileCitation ContainerFileCitation = "container_file_citation"`

            - `type ResponseOutputTextAnnotationFilePath struct{…}`

              A path to a file.

              - `FileID string`

                The ID of the file.

              - `Index int64`

                The index of the file in the list of files.

              - `Type FilePath`

                The type of the file path. Always `file_path`.

                - `const FilePathFilePath FilePath = "file_path"`

          - `Text string`

            The text output from the model.

          - `Type OutputText`

            The type of the output text. Always `output_text`.

            - `const OutputTextOutputText OutputText = "output_text"`

          - `Logprobs []ResponseOutputTextLogprob`

            - `Token string`

            - `Bytes []int64`

            - `Logprob float64`

            - `TopLogprobs []ResponseOutputTextLogprobTopLogprob`

              - `Token string`

              - `Bytes []int64`

              - `Logprob float64`

        - `type ResponseOutputRefusal struct{…}`

          A refusal from the model.

          - `Refusal string`

            The refusal explanation from the model.

          - `Type Refusal`

            The type of the refusal. Always `refusal`.

            - `const RefusalRefusal Refusal = "refusal"`

      - `Role Assistant`

        The role of the output message. Always `assistant`.

        - `const AssistantAssistant Assistant = "assistant"`

      - `Status ResponseOutputMessageStatus`

        The status of the message input. One of `in_progress`, `completed`, or
        `incomplete`. Populated when input items are returned via API.

        - `const ResponseOutputMessageStatusInProgress ResponseOutputMessageStatus = "in_progress"`

        - `const ResponseOutputMessageStatusCompleted ResponseOutputMessageStatus = "completed"`

        - `const ResponseOutputMessageStatusIncomplete ResponseOutputMessageStatus = "incomplete"`

      - `Type Message`

        The type of the output message. Always `message`.

        - `const MessageMessage Message = "message"`

      - `Phase ResponseOutputMessagePhase`

        Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
        For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
        phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

        - `const ResponseOutputMessagePhaseCommentary ResponseOutputMessagePhase = "commentary"`

        - `const ResponseOutputMessagePhaseFinalAnswer ResponseOutputMessagePhase = "final_answer"`

    - `type ResponseFileSearchToolCall struct{…}`

      The results of a file search tool call. See the
      [file search guide](/api/docs/guides/tools-file-search) for more information.

      - `ID string`

        The unique ID of the file search tool call.

      - `Queries []string`

        The queries used to search for files.

      - `Status ResponseFileSearchToolCallStatus`

        The status of the file search tool call. One of `in_progress`,
        `searching`, `incomplete` or `failed`,

        - `const ResponseFileSearchToolCallStatusInProgress ResponseFileSearchToolCallStatus = "in_progress"`

        - `const ResponseFileSearchToolCallStatusSearching ResponseFileSearchToolCallStatus = "searching"`

        - `const ResponseFileSearchToolCallStatusCompleted ResponseFileSearchToolCallStatus = "completed"`

        - `const ResponseFileSearchToolCallStatusIncomplete ResponseFileSearchToolCallStatus = "incomplete"`

        - `const ResponseFileSearchToolCallStatusFailed ResponseFileSearchToolCallStatus = "failed"`

      - `Type FileSearchCall`

        The type of the file search tool call. Always `file_search_call`.

        - `const FileSearchCallFileSearchCall FileSearchCall = "file_search_call"`

      - `Results []ResponseFileSearchToolCallResult`

        The results of the file search tool call.

        - `Attributes map[string, ResponseFileSearchToolCallResultAttributeUnion]`

          Set of 16 key-value pairs that can be attached to an object. This can be
          useful for storing additional information about the object in a structured
          format, and querying for objects via API or the dashboard. Keys are strings
          with a maximum length of 64 characters. Values are strings with a maximum
          length of 512 characters, booleans, or numbers.

          - `string`

          - `float64`

          - `bool`

        - `FileID string`

          The unique ID of the file.

        - `Filename string`

          The name of the file.

        - `Score float64`

          The relevance score of the file - a value between 0 and 1.

        - `Text string`

          The text that was retrieved from the file.

    - `type ResponseComputerToolCall struct{…}`

      A tool call to a computer use tool. See the
      [computer use guide](/api/docs/guides/tools-computer-use) for more information.

      - `ID string`

        The unique ID of the computer call.

      - `CallID string`

        An identifier used when responding to the tool call with output.

      - `PendingSafetyChecks []ResponseComputerToolCallPendingSafetyCheck`

        The pending safety checks for the computer call.

        - `ID string`

          The ID of the pending safety check.

        - `Code string`

          The type of the pending safety check.

        - `Message string`

          Details about the pending safety check.

      - `Status ResponseComputerToolCallStatus`

        The status of the item. One of `in_progress`, `completed`, or
        `incomplete`. Populated when items are returned via API.

        - `const ResponseComputerToolCallStatusInProgress ResponseComputerToolCallStatus = "in_progress"`

        - `const ResponseComputerToolCallStatusCompleted ResponseComputerToolCallStatus = "completed"`

        - `const ResponseComputerToolCallStatusIncomplete ResponseComputerToolCallStatus = "incomplete"`

      - `Type ResponseComputerToolCallType`

        The type of the computer call. Always `computer_call`.

        - `const ResponseComputerToolCallTypeComputerCall ResponseComputerToolCallType = "computer_call"`

      - `Action ResponseComputerToolCallActionUnion`

        A click action.

        - `type ResponseComputerToolCallActionClick struct{…}`

          A click action.

          - `Button string`

            Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

            - `const ResponseComputerToolCallActionClickButtonLeft ResponseComputerToolCallActionClickButton = "left"`

            - `const ResponseComputerToolCallActionClickButtonRight ResponseComputerToolCallActionClickButton = "right"`

            - `const ResponseComputerToolCallActionClickButtonWheel ResponseComputerToolCallActionClickButton = "wheel"`

            - `const ResponseComputerToolCallActionClickButtonBack ResponseComputerToolCallActionClickButton = "back"`

            - `const ResponseComputerToolCallActionClickButtonForward ResponseComputerToolCallActionClickButton = "forward"`

          - `Type Click`

            Specifies the event type. For a click action, this property is always `click`.

            - `const ClickClick Click = "click"`

          - `X int64`

            The x-coordinate where the click occurred.

          - `Y int64`

            The y-coordinate where the click occurred.

          - `Keys []string`

            The keys being held while clicking.

        - `type ResponseComputerToolCallActionDoubleClick struct{…}`

          A double click action.

          - `Keys []string`

            The keys being held while double-clicking.

          - `Type DoubleClick`

            Specifies the event type. For a double click action, this property is always set to `double_click`.

            - `const DoubleClickDoubleClick DoubleClick = "double_click"`

          - `X int64`

            The x-coordinate where the double click occurred.

          - `Y int64`

            The y-coordinate where the double click occurred.

        - `type ResponseComputerToolCallActionDrag struct{…}`

          A drag action.

          - `Path []ResponseComputerToolCallActionDragPath`

            An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

            ```
            [
              { x: 100, y: 200 },
              { x: 200, y: 300 }
            ]
            ```

            - `X int64`

              The x-coordinate.

            - `Y int64`

              The y-coordinate.

          - `Type Drag`

            Specifies the event type. For a drag action, this property is always set to `drag`.

            - `const DragDrag Drag = "drag"`

          - `Keys []string`

            The keys being held while dragging the mouse.

        - `type ResponseComputerToolCallActionKeypress struct{…}`

          A collection of keypresses the model would like to perform.

          - `Keys []string`

            The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

          - `Type Keypress`

            Specifies the event type. For a keypress action, this property is always set to `keypress`.

            - `const KeypressKeypress Keypress = "keypress"`

        - `type ResponseComputerToolCallActionMove struct{…}`

          A mouse move action.

          - `Type Move`

            Specifies the event type. For a move action, this property is always set to `move`.

            - `const MoveMove Move = "move"`

          - `X int64`

            The x-coordinate to move to.

          - `Y int64`

            The y-coordinate to move to.

          - `Keys []string`

            The keys being held while moving the mouse.

        - `type ResponseComputerToolCallActionScreenshot struct{…}`

          A screenshot action.

          - `Type Screenshot`

            Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

            - `const ScreenshotScreenshot Screenshot = "screenshot"`

        - `type ResponseComputerToolCallActionScroll struct{…}`

          A scroll action.

          - `ScrollX int64`

            The horizontal scroll distance.

          - `ScrollY int64`

            The vertical scroll distance.

          - `Type Scroll`

            Specifies the event type. For a scroll action, this property is always set to `scroll`.

            - `const ScrollScroll Scroll = "scroll"`

          - `X int64`

            The x-coordinate where the scroll occurred.

          - `Y int64`

            The y-coordinate where the scroll occurred.

          - `Keys []string`

            The keys being held while scrolling.

        - `type ResponseComputerToolCallActionType struct{…}`

          An action to type in text.

          - `Text string`

            The text to type.

          - `Type Type`

            Specifies the event type. For a type action, this property is always set to `type`.

            - `const TypeType Type = "type"`

        - `type ResponseComputerToolCallActionWait struct{…}`

          A wait action.

          - `Type Wait`

            Specifies the event type. For a wait action, this property is always set to `wait`.

            - `const WaitWait Wait = "wait"`

      - `Actions ComputerActionList`

        Flattened batched actions for `computer_use`. Each action includes an
        `type` discriminator and action-specific fields.

        - `type ComputerActionClick struct{…}`

          A click action.

          - `Button string`

            Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

            - `const ComputerActionClickButtonLeft ComputerActionClickButton = "left"`

            - `const ComputerActionClickButtonRight ComputerActionClickButton = "right"`

            - `const ComputerActionClickButtonWheel ComputerActionClickButton = "wheel"`

            - `const ComputerActionClickButtonBack ComputerActionClickButton = "back"`

            - `const ComputerActionClickButtonForward ComputerActionClickButton = "forward"`

          - `Type Click`

            Specifies the event type. For a click action, this property is always `click`.

            - `const ClickClick Click = "click"`

          - `X int64`

            The x-coordinate where the click occurred.

          - `Y int64`

            The y-coordinate where the click occurred.

          - `Keys []string`

            The keys being held while clicking.

        - `type ComputerActionDoubleClick struct{…}`

          A double click action.

          - `Keys []string`

            The keys being held while double-clicking.

          - `Type DoubleClick`

            Specifies the event type. For a double click action, this property is always set to `double_click`.

            - `const DoubleClickDoubleClick DoubleClick = "double_click"`

          - `X int64`

            The x-coordinate where the double click occurred.

          - `Y int64`

            The y-coordinate where the double click occurred.

        - `type ComputerActionDrag struct{…}`

          A drag action.

          - `Path []ComputerActionDragPath`

            An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

            ```
            [
              { x: 100, y: 200 },
              { x: 200, y: 300 }
            ]
            ```

            - `X int64`

              The x-coordinate.

            - `Y int64`

              The y-coordinate.

          - `Type Drag`

            Specifies the event type. For a drag action, this property is always set to `drag`.

            - `const DragDrag Drag = "drag"`

          - `Keys []string`

            The keys being held while dragging the mouse.

        - `type ComputerActionKeypress struct{…}`

          A collection of keypresses the model would like to perform.

          - `Keys []string`

            The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

          - `Type Keypress`

            Specifies the event type. For a keypress action, this property is always set to `keypress`.

            - `const KeypressKeypress Keypress = "keypress"`

        - `type ComputerActionMove struct{…}`

          A mouse move action.

          - `Type Move`

            Specifies the event type. For a move action, this property is always set to `move`.

            - `const MoveMove Move = "move"`

          - `X int64`

            The x-coordinate to move to.

          - `Y int64`

            The y-coordinate to move to.

          - `Keys []string`

            The keys being held while moving the mouse.

        - `type ComputerActionScreenshot struct{…}`

          A screenshot action.

          - `Type Screenshot`

            Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

            - `const ScreenshotScreenshot Screenshot = "screenshot"`

        - `type ComputerActionScroll struct{…}`

          A scroll action.

          - `ScrollX int64`

            The horizontal scroll distance.

          - `ScrollY int64`

            The vertical scroll distance.

          - `Type Scroll`

            Specifies the event type. For a scroll action, this property is always set to `scroll`.

            - `const ScrollScroll Scroll = "scroll"`

          - `X int64`

            The x-coordinate where the scroll occurred.

          - `Y int64`

            The y-coordinate where the scroll occurred.

          - `Keys []string`

            The keys being held while scrolling.

        - `type ComputerActionType struct{…}`

          An action to type in text.

          - `Text string`

            The text to type.

          - `Type Type`

            Specifies the event type. For a type action, this property is always set to `type`.

            - `const TypeType Type = "type"`

        - `type ComputerActionWait struct{…}`

          A wait action.

          - `Type Wait`

            Specifies the event type. For a wait action, this property is always set to `wait`.

            - `const WaitWait Wait = "wait"`

    - `type ResponseInputItemComputerCallOutput struct{…}`

      The output of a computer tool call.

      - `CallID string`

        The ID of the computer tool call that produced the output.

      - `Output ResponseComputerToolCallOutputScreenshot`

        A computer screenshot image used with the computer use tool.

        - `Type ComputerScreenshot`

          Specifies the event type. For a computer screenshot, this property is
          always set to `computer_screenshot`.

          - `const ComputerScreenshotComputerScreenshot ComputerScreenshot = "computer_screenshot"`

        - `FileID string`

          The identifier of an uploaded file that contains the screenshot.

        - `ImageURL string`

          The URL of the screenshot image.

      - `Type ComputerCallOutput`

        The type of the computer tool call output. Always `computer_call_output`.

        - `const ComputerCallOutputComputerCallOutput ComputerCallOutput = "computer_call_output"`

      - `ID string`

        The ID of the computer tool call output.

      - `AcknowledgedSafetyChecks []ResponseInputItemComputerCallOutputAcknowledgedSafetyCheck`

        The safety checks reported by the API that have been acknowledged by the developer.

        - `ID string`

          The ID of the pending safety check.

        - `Code string`

          The type of the pending safety check.

        - `Message string`

          Details about the pending safety check.

      - `Status string`

        The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

        - `const ResponseInputItemComputerCallOutputStatusInProgress ResponseInputItemComputerCallOutputStatus = "in_progress"`

        - `const ResponseInputItemComputerCallOutputStatusCompleted ResponseInputItemComputerCallOutputStatus = "completed"`

        - `const ResponseInputItemComputerCallOutputStatusIncomplete ResponseInputItemComputerCallOutputStatus = "incomplete"`

    - `type ResponseFunctionWebSearch struct{…}`

      The results of a web search tool call. See the
      [web search guide](/api/docs/guides/tools-web-search) for more information.

      - `ID string`

        The unique ID of the web search tool call.

      - `Action ResponseFunctionWebSearchActionUnion`

        An object describing the specific action taken in this web search call.
        Includes details on how the model used the web (search, open_page, find_in_page).

        - `type ResponseFunctionWebSearchActionSearch struct{…}`

          Action type "search" - Performs a web search query.

          - `Type Search`

            The action type.

            - `const SearchSearch Search = "search"`

          - `Queries []string`

            The search queries.

          - `Query string`

            The search query.

          - `Sources []ResponseFunctionWebSearchActionSearchSource`

            The sources used in the search.

            - `Type URL`

              The type of source. Always `url`.

              - `const URLURL URL = "url"`

            - `URL string`

              The URL of the source.

        - `type ResponseFunctionWebSearchActionOpenPage struct{…}`

          Action type "open_page" - Opens a specific URL from search results.

          - `Type OpenPage`

            The action type.

            - `const OpenPageOpenPage OpenPage = "open_page"`

          - `URL string`

            The URL opened by the model.

        - `type ResponseFunctionWebSearchActionFindInPage struct{…}`

          Action type "find_in_page": Searches for a pattern within a loaded page.

          - `Pattern string`

            The pattern or text to search for within the page.

          - `Type FindInPage`

            The action type.

            - `const FindInPageFindInPage FindInPage = "find_in_page"`

          - `URL string`

            The URL of the page searched for the pattern.

      - `Status ResponseFunctionWebSearchStatus`

        The status of the web search tool call.

        - `const ResponseFunctionWebSearchStatusInProgress ResponseFunctionWebSearchStatus = "in_progress"`

        - `const ResponseFunctionWebSearchStatusSearching ResponseFunctionWebSearchStatus = "searching"`

        - `const ResponseFunctionWebSearchStatusCompleted ResponseFunctionWebSearchStatus = "completed"`

        - `const ResponseFunctionWebSearchStatusFailed ResponseFunctionWebSearchStatus = "failed"`

        - `const ResponseFunctionWebSearchStatusIncomplete ResponseFunctionWebSearchStatus = "incomplete"`

      - `Type WebSearchCall`

        The type of the web search tool call. Always `web_search_call`.

        - `const WebSearchCallWebSearchCall WebSearchCall = "web_search_call"`

    - `type ResponseFunctionToolCall struct{…}`

      A tool call to run a function. See the
      [function calling guide](/api/docs/guides/function-calling) for more information.

      - `Arguments string`

        A JSON string of the arguments to pass to the function.

      - `CallID string`

        The unique ID of the function tool call generated by the model.

      - `Name string`

        The name of the function to run.

      - `Type FunctionCall`

        The type of the function tool call. Always `function_call`.

        - `const FunctionCallFunctionCall FunctionCall = "function_call"`

      - `ID string`

        The unique ID of the function tool call.

      - `Async bool`

        Whether the function tool call runs asynchronously.

      - `Caller ResponseFunctionToolCallCallerUnion`

        The execution context that produced this tool call.

        - `type ResponseFunctionToolCallCallerDirect struct{…}`

          - `Type Direct`

            - `const DirectDirect Direct = "direct"`

        - `type ResponseFunctionToolCallCallerProgram struct{…}`

          - `CallerID string`

            The call ID of the program item that produced this tool call.

          - `Type Program`

            - `const ProgramProgram Program = "program"`

      - `Namespace string`

        The namespace of the function to run.

      - `Status ResponseFunctionToolCallStatus`

        The status of the item. One of `in_progress`, `completed`, or
        `incomplete`. Populated when items are returned via API.

        - `const ResponseFunctionToolCallStatusInProgress ResponseFunctionToolCallStatus = "in_progress"`

        - `const ResponseFunctionToolCallStatusCompleted ResponseFunctionToolCallStatus = "completed"`

        - `const ResponseFunctionToolCallStatusIncomplete ResponseFunctionToolCallStatus = "incomplete"`

    - `type ResponseInputItemFunctionCallOutput struct{…}`

      The output of a function tool call.

      - `Output ResponseInputItemFunctionCallOutputOutputUnion`

        Text, image, or file output of the function tool call.

        - `string`

        - `type ResponseFunctionCallOutputItemList []ResponseFunctionCallOutputItemUnion`

          An array of content outputs (text, image, file) for the function tool call.

          - `type ResponseInputTextContent struct{…}`

            A text input to the model.

            - `Text string`

              The text input to the model.

            - `Type InputText`

              The type of the input item. Always `input_text`.

              - `const InputTextInputText InputText = "input_text"`

            - `PromptCacheBreakpoint ResponseInputTextContentPromptCacheBreakpoint`

              Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

              - `Mode Explicit`

                The breakpoint mode. Always `explicit`.

                - `const ExplicitExplicit Explicit = "explicit"`

          - `type ResponseInputImageContent struct{…}`

            An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision)

            - `Type InputImage`

              The type of the input item. Always `input_image`.

              - `const InputImageInputImage InputImage = "input_image"`

            - `Detail ResponseInputImageContentDetail`

              The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

              - `const ResponseInputImageContentDetailLow ResponseInputImageContentDetail = "low"`

              - `const ResponseInputImageContentDetailHigh ResponseInputImageContentDetail = "high"`

              - `const ResponseInputImageContentDetailAuto ResponseInputImageContentDetail = "auto"`

              - `const ResponseInputImageContentDetailOriginal ResponseInputImageContentDetail = "original"`

            - `FileID string`

              The ID of the file to be sent to the model.

            - `ImageURL string`

              The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

            - `PromptCacheBreakpoint ResponseInputImageContentPromptCacheBreakpoint`

              Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

              - `Mode Explicit`

                The breakpoint mode. Always `explicit`.

                - `const ExplicitExplicit Explicit = "explicit"`

          - `type ResponseInputFileContent struct{…}`

            A file input to the model.

            - `Type InputFile`

              The type of the input item. Always `input_file`.

              - `const InputFileInputFile InputFile = "input_file"`

            - `Detail ResponseInputFileContentDetail`

              The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

              - `const ResponseInputFileContentDetailAuto ResponseInputFileContentDetail = "auto"`

              - `const ResponseInputFileContentDetailLow ResponseInputFileContentDetail = "low"`

              - `const ResponseInputFileContentDetailHigh ResponseInputFileContentDetail = "high"`

            - `FileData string`

              The base64-encoded data of the file to be sent to the model.

            - `FileID string`

              The ID of the file to be sent to the model.

            - `FileURL string`

              The URL of the file to be sent to the model.

            - `Filename string`

              The name of the file to be sent to the model.

            - `PromptCacheBreakpoint ResponseInputFileContentPromptCacheBreakpoint`

              Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

              - `Mode Explicit`

                The breakpoint mode. Always `explicit`.

                - `const ExplicitExplicit Explicit = "explicit"`

      - `Type FunctionCallOutput`

        The type of the function tool call output. Always `function_call_output`.

        - `const FunctionCallOutputFunctionCallOutput FunctionCallOutput = "function_call_output"`

      - `ID string`

        The unique ID of the function tool call output. Populated when this item is returned via API.

      - `CallID string`

        The unique ID of the function tool call generated by the model.

      - `Caller ResponseInputItemFunctionCallOutputCallerUnion`

        The execution context that produced this tool call.

        - `type ResponseInputItemFunctionCallOutputCallerDirect struct{…}`

          - `Type Direct`

            The caller type. Always `direct`.

            - `const DirectDirect Direct = "direct"`

        - `type ResponseInputItemFunctionCallOutputCallerProgram struct{…}`

          - `CallerID string`

            The call ID of the program item that produced this tool call.

          - `Type Program`

            The caller type. Always `program`.

            - `const ProgramProgram Program = "program"`

      - `Name string`

        The name of the tool that produced the output.

      - `Namespace string`

        The namespace of the tool that produced the output.

      - `Status string`

        The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

        - `const ResponseInputItemFunctionCallOutputStatusInProgress ResponseInputItemFunctionCallOutputStatus = "in_progress"`

        - `const ResponseInputItemFunctionCallOutputStatusCompleted ResponseInputItemFunctionCallOutputStatus = "completed"`

        - `const ResponseInputItemFunctionCallOutputStatusIncomplete ResponseInputItemFunctionCallOutputStatus = "incomplete"`

    - `type ResponseInputItemToolSearchCall struct{…}`

      - `Arguments any`

        The arguments supplied to the tool search call.

      - `Type ToolSearchCall`

        The item type. Always `tool_search_call`.

        - `const ToolSearchCallToolSearchCall ToolSearchCall = "tool_search_call"`

      - `ID string`

        The unique ID of this tool search call.

      - `CallID string`

        The unique ID of the tool search call generated by the model.

      - `Execution string`

        Whether tool search was executed by the server or by the client.

        - `const ResponseInputItemToolSearchCallExecutionServer ResponseInputItemToolSearchCallExecution = "server"`

        - `const ResponseInputItemToolSearchCallExecutionClient ResponseInputItemToolSearchCallExecution = "client"`

      - `Status string`

        The status of the tool search call.

        - `const ResponseInputItemToolSearchCallStatusInProgress ResponseInputItemToolSearchCallStatus = "in_progress"`

        - `const ResponseInputItemToolSearchCallStatusCompleted ResponseInputItemToolSearchCallStatus = "completed"`

        - `const ResponseInputItemToolSearchCallStatusIncomplete ResponseInputItemToolSearchCallStatus = "incomplete"`

    - `type ResponseToolSearchOutputItemParamResp struct{…}`

      - `Tools []ToolUnion`

        The loaded tool definitions returned by the tool search output.

        - `type FunctionTool struct{…}`

          Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

          - `Name string`

            The name of the function to call.

          - `Parameters map[string, any]`

            A JSON schema object describing the parameters of the function.

          - `Strict bool`

            Whether strict parameter validation is enforced for this function tool.

          - `Type Function`

            The type of the function tool. Always `function`.

            - `const FunctionFunction Function = "function"`

          - `AllowedCallers []string`

            The tool invocation context(s).

            - `const FunctionToolAllowedCallerDirect FunctionToolAllowedCaller = "direct"`

            - `const FunctionToolAllowedCallerProgrammatic FunctionToolAllowedCaller = "programmatic"`

          - `Async bool`

          - `DeferLoading bool`

            Whether this function is deferred and loaded via tool search.

          - `Description string`

            A description of the function. Used by the model to determine whether or not to call the function.

          - `OutputSchema map[string, any]`

            A JSON schema object describing the JSON value encoded in string outputs for this function.

        - `type FileSearchTool struct{…}`

          A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

          - `Type FileSearch`

            The type of the file search tool. Always `file_search`.

            - `const FileSearchFileSearch FileSearch = "file_search"`

          - `VectorStoreIDs []string`

            The IDs of the vector stores to search.

          - `Filters FileSearchToolFiltersUnion`

            A filter to apply.

            - `type ComparisonFilter struct{…}`

              A filter used to compare a specified attribute key to a given value using a defined comparison operation.

              - `Key string`

                The key to compare against the value.

              - `Type ComparisonFilterType`

                Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                - `eq`: equals
                - `ne`: not equal
                - `gt`: greater than
                - `gte`: greater than or equal
                - `lt`: less than
                - `lte`: less than or equal
                - `in`: in
                - `nin`: not in

                - `const ComparisonFilterTypeEq ComparisonFilterType = "eq"`

                - `const ComparisonFilterTypeNe ComparisonFilterType = "ne"`

                - `const ComparisonFilterTypeGt ComparisonFilterType = "gt"`

                - `const ComparisonFilterTypeGte ComparisonFilterType = "gte"`

                - `const ComparisonFilterTypeLt ComparisonFilterType = "lt"`

                - `const ComparisonFilterTypeLte ComparisonFilterType = "lte"`

                - `const ComparisonFilterTypeIn ComparisonFilterType = "in"`

                - `const ComparisonFilterTypeNin ComparisonFilterType = "nin"`

              - `Value ComparisonFilterValueUnion`

                The value to compare against the attribute key; supports string, number, or boolean types.

                - `string`

                - `float64`

                - `bool`

                - `type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion`

                  - `string`

                  - `float64`

            - `type CompoundFilter struct{…}`

              Combine multiple filters using `and` or `or`.

              - `Filters []CompoundFilterFilterUnion`

                Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

                - `type ComparisonFilter struct{…}`

                  A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                - `type CompoundFilter struct{…}`

                  Combine multiple filters using `and` or `or`.

              - `Type CompoundFilterType`

                Type of operation: `and` or `or`.

                - `const CompoundFilterTypeAnd CompoundFilterType = "and"`

                - `const CompoundFilterTypeOr CompoundFilterType = "or"`

          - `MaxNumResults int64`

            The maximum number of results to return. This number should be between 1 and 50 inclusive.

          - `RankingOptions FileSearchToolRankingOptions`

            Ranking options for search.

            - `HybridSearch FileSearchToolRankingOptionsHybridSearch`

              Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

              - `EmbeddingWeight float64`

                The weight of the embedding in the reciprocal ranking fusion.

              - `TextWeight float64`

                The weight of the text in the reciprocal ranking fusion.

            - `Ranker string`

              The ranker to use for the file search.

              - `const FileSearchToolRankingOptionsRankerAuto FileSearchToolRankingOptionsRanker = "auto"`

              - `const FileSearchToolRankingOptionsRankerDefault2024_11_15 FileSearchToolRankingOptionsRanker = "default-2024-11-15"`

            - `ScoreThreshold float64`

              The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

        - `type ComputerTool struct{…}`

          A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

          - `Type Computer`

            The type of the computer tool. Always `computer`.

            - `const ComputerComputer Computer = "computer"`

        - `type ComputerUsePreviewTool struct{…}`

          A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

          - `DisplayHeight int64`

            The height of the computer display.

          - `DisplayWidth int64`

            The width of the computer display.

          - `Environment ComputerUsePreviewToolEnvironment`

            The type of computer environment to control.

            - `const ComputerUsePreviewToolEnvironmentWindows ComputerUsePreviewToolEnvironment = "windows"`

            - `const ComputerUsePreviewToolEnvironmentMac ComputerUsePreviewToolEnvironment = "mac"`

            - `const ComputerUsePreviewToolEnvironmentLinux ComputerUsePreviewToolEnvironment = "linux"`

            - `const ComputerUsePreviewToolEnvironmentUbuntu ComputerUsePreviewToolEnvironment = "ubuntu"`

            - `const ComputerUsePreviewToolEnvironmentBrowser ComputerUsePreviewToolEnvironment = "browser"`

          - `Type ComputerUsePreview`

            The type of the computer use tool. Always `computer_use_preview`.

            - `const ComputerUsePreviewComputerUsePreview ComputerUsePreview = "computer_use_preview"`

        - `type WebSearchTool struct{…}`

          Search the Internet for sources related to the prompt. Learn more about the
          [web search tool](/api/docs/guides/tools-web-search).

          - `Type WebSearchToolType`

            The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

            - `const WebSearchToolTypeWebSearch WebSearchToolType = "web_search"`

            - `const WebSearchToolTypeWebSearch2025_08_26 WebSearchToolType = "web_search_2025_08_26"`

          - `ExternalWebAccess bool`

            Allow live internet access for web search. Defaults to true when omitted. When false, the web search tool runs in offline/cache-only mode and will not fetch new external content.

          - `Filters WebSearchToolFilters`

            Filters for the search.

            - `AllowedDomains []string`

              Allowed domains for the search. If not provided, all domains are allowed.
              Subdomains of the provided domains are allowed as well.

              Example: `["pubmed.ncbi.nlm.nih.gov"]`

          - `SearchContextSize WebSearchToolSearchContextSize`

            High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

            - `const WebSearchToolSearchContextSizeLow WebSearchToolSearchContextSize = "low"`

            - `const WebSearchToolSearchContextSizeMedium WebSearchToolSearchContextSize = "medium"`

            - `const WebSearchToolSearchContextSizeHigh WebSearchToolSearchContextSize = "high"`

          - `UserLocation WebSearchToolUserLocation`

            The approximate location of the user. If omitted or null, defaults to the
            United States. To avoid this fallback, pass `{"type": "approximate"}` without
            location fields. To localize results, provide the relevant location fields.

            - `City string`

              Free text input for the city of the user, e.g. `San Francisco`.

            - `Country string`

              The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

            - `Region string`

              Free text input for the region of the user, e.g. `California`.

            - `Timezone string`

              The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

            - `Type string`

              The type of location approximation. Always `approximate`.

              - `const WebSearchToolUserLocationTypeApproximate WebSearchToolUserLocationType = "approximate"`

        - `type ToolMcp struct{…}`

          Give the model access to additional tools via remote Model Context Protocol
          (MCP) servers. [Learn more about MCP](/api/docs/guides/tools-connectors-mcp).

          - `ServerLabel string`

            A label for this MCP server, used to identify it in tool calls.

          - `Type Mcp`

            The type of the MCP tool. Always `mcp`.

            - `const McpMcp Mcp = "mcp"`

          - `AllowedCallers []string`

            The tool invocation context(s).

            - `const ToolMcpAllowedCallerDirect ToolMcpAllowedCaller = "direct"`

            - `const ToolMcpAllowedCallerProgrammatic ToolMcpAllowedCaller = "programmatic"`

          - `AllowedTools ToolMcpAllowedToolsUnion`

            List of allowed tool names or a filter object.

            - `type ToolMcpAllowedToolsMcpAllowedTools []string`

              A string array of allowed tool names

            - `type ToolMcpAllowedToolsMcpToolFilter struct{…}`

              A filter object to specify which tools are allowed.

              - `ReadOnly bool`

                Indicates whether or not a tool modifies data or is read-only. If an
                MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                it will match this filter.

              - `ToolNames []string`

                List of allowed tool names.

          - `Authorization string`

            An OAuth access token that can be used with a remote MCP server, either
            with a custom MCP server URL or a service connector. Your application
            must handle the OAuth authorization flow and provide the token here.

          - `ConnectorID string`

            Identifier for service connectors, like those available in ChatGPT. One of
            `server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
            about service connectors [here](/api/docs/guides/tools-connectors-mcp#connectors).

            This field is deprecated for models released after September 1, 2026.
            Use `server_url` to connect to a remote MCP server, or `tunnel_id` to
            connect through a Secure MCP Tunnel.

            Currently supported `connector_id` values are:

            - Dropbox: `connector_dropbox`
            - Gmail: `connector_gmail`
            - Google Calendar: `connector_googlecalendar`
            - Google Drive: `connector_googledrive`
            - Microsoft Teams: `connector_microsoftteams`
            - Outlook Calendar: `connector_outlookcalendar`
            - Outlook Email: `connector_outlookemail`
            - SharePoint: `connector_sharepoint`

            - `const ToolMcpConnectorIDConnectorDropbox ToolMcpConnectorID = "connector_dropbox"`

            - `const ToolMcpConnectorIDConnectorGmail ToolMcpConnectorID = "connector_gmail"`

            - `const ToolMcpConnectorIDConnectorGooglecalendar ToolMcpConnectorID = "connector_googlecalendar"`

            - `const ToolMcpConnectorIDConnectorGoogledrive ToolMcpConnectorID = "connector_googledrive"`

            - `const ToolMcpConnectorIDConnectorMicrosoftteams ToolMcpConnectorID = "connector_microsoftteams"`

            - `const ToolMcpConnectorIDConnectorOutlookcalendar ToolMcpConnectorID = "connector_outlookcalendar"`

            - `const ToolMcpConnectorIDConnectorOutlookemail ToolMcpConnectorID = "connector_outlookemail"`

            - `const ToolMcpConnectorIDConnectorSharepoint ToolMcpConnectorID = "connector_sharepoint"`

          - `DeferLoading bool`

            Whether this MCP tool is deferred and discovered via tool search.

          - `Headers map[string, string]`

            Optional HTTP headers to send to the MCP server. Use for authentication
            or other purposes.

          - `RequireApproval ToolMcpRequireApprovalUnion`

            Specify which of the MCP server's tools require approval.

            - `type ToolMcpRequireApprovalMcpToolApprovalFilter struct{…}`

              Specify which of the MCP server's tools require approval. Can be
              `always`, `never`, or a filter object associated with tools
              that require approval.

              - `Always ToolMcpRequireApprovalMcpToolApprovalFilterAlways`

                A filter object to specify which tools are allowed.

                - `ReadOnly bool`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `ToolNames []string`

                  List of allowed tool names.

              - `Never ToolMcpRequireApprovalMcpToolApprovalFilterNever`

                A filter object to specify which tools are allowed.

                - `ReadOnly bool`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `ToolNames []string`

                  List of allowed tool names.

            - `type ToolMcpRequireApprovalMcpToolApprovalSetting string`

              Specify a single approval policy for all tools. One of `always` or
              `never`. When set to `always`, all tools will require approval. When
              set to `never`, all tools will not require approval.

              - `const ToolMcpRequireApprovalMcpToolApprovalSettingAlways ToolMcpRequireApprovalMcpToolApprovalSetting = "always"`

              - `const ToolMcpRequireApprovalMcpToolApprovalSettingNever ToolMcpRequireApprovalMcpToolApprovalSetting = "never"`

          - `ServerDescription string`

            Optional description of the MCP server, used to provide more context.

          - `ServerURL string`

            The URL for the MCP server. One of `server_url`, `connector_id`, or
            `tunnel_id` must be provided.

          - `TunnelID string`

            The Secure MCP Tunnel ID to use instead of a direct server URL. One of
            `server_url`, `connector_id`, or `tunnel_id` must be provided.

        - `type ToolCodeInterpreter struct{…}`

          A tool that runs Python code to help generate a response to a prompt.

          - `Container ToolCodeInterpreterContainerUnion`

            The code interpreter container. Can be a container ID or an object that
            specifies uploaded file IDs to make available to your code, along with an
            optional `memory_limit` setting.

            - `string`

            - `type ToolCodeInterpreterContainerCodeInterpreterContainerAuto struct{…}`

              Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

              - `Type Auto`

                Always `auto`.

                - `const AutoAuto Auto = "auto"`

              - `FileIDs []string`

                An optional list of uploaded files to make available to your code.

              - `MemoryLimit string`

                The memory limit for the code interpreter container.

                - `const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit1g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "1g"`

                - `const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit4g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "4g"`

                - `const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit16g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "16g"`

                - `const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit64g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "64g"`

              - `NetworkPolicy ToolCodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicyUnion`

                Network access policy for the container.

                - `type ContainerNetworkPolicyDisabled struct{…}`

                  - `Type Disabled`

                    Disable outbound network access. Always `disabled`.

                    - `const DisabledDisabled Disabled = "disabled"`

                - `type ContainerNetworkPolicyAllowlist struct{…}`

                  - `AllowedDomains []string`

                    A list of allowed domains when type is `allowlist`.

                  - `Type Allowlist`

                    Allow outbound network access only to specified domains. Always `allowlist`.

                    - `const AllowlistAllowlist Allowlist = "allowlist"`

                  - `DomainSecrets []ContainerNetworkPolicyDomainSecret`

                    Optional domain-scoped secrets for allowlisted domains.

                    - `Domain string`

                      The domain associated with the secret.

                    - `Name string`

                      The name of the secret to inject for the domain.

                    - `Value string`

                      The secret value to inject for the domain.

          - `Type CodeInterpreter`

            The type of the code interpreter tool. Always `code_interpreter`.

            - `const CodeInterpreterCodeInterpreter CodeInterpreter = "code_interpreter"`

          - `AllowedCallers []string`

            The tool invocation context(s).

            - `const ToolCodeInterpreterAllowedCallerDirect ToolCodeInterpreterAllowedCaller = "direct"`

            - `const ToolCodeInterpreterAllowedCallerProgrammatic ToolCodeInterpreterAllowedCaller = "programmatic"`

        - `type ToolProgrammaticToolCalling struct{…}`

          - `Type ProgrammaticToolCalling`

            The type of the tool. Always `programmatic_tool_calling`.

            - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

        - `type ToolImageGeneration struct{…}`

          A tool that generates images using the GPT image models.

          - `Type ImageGeneration`

            The type of the image generation tool. Always `image_generation`.

            - `const ImageGenerationImageGeneration ImageGeneration = "image_generation"`

          - `Action string`

            Whether to generate a new image or edit an existing image. Default: `auto`.

            - `const ToolImageGenerationActionGenerate ToolImageGenerationAction = "generate"`

            - `const ToolImageGenerationActionEdit ToolImageGenerationAction = "edit"`

            - `const ToolImageGenerationActionAuto ToolImageGenerationAction = "auto"`

          - `Background string`

            Allows to set transparency for the background of the generated image(s). Must
            be one of `transparent`, `opaque`, or `auto` (default value). When `auto` is
            used, the model will automatically determine the best background for the
            image.

            `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`, including their
            `2026-09-08` snapshots, support `opaque` and `transparent` backgrounds.
            Transparent backgrounds are available for supported GPT Image models. For
            `gpt-image-2` and `gpt-image-2-2026-04-21`, this support is in preview. When
            using `transparent`, set the output format to `png` or `webp`.

            - `const ToolImageGenerationBackgroundTransparent ToolImageGenerationBackground = "transparent"`

            - `const ToolImageGenerationBackgroundOpaque ToolImageGenerationBackground = "opaque"`

            - `const ToolImageGenerationBackgroundAuto ToolImageGenerationBackground = "auto"`

          - `InputFidelity string`

            Controls fidelity to the original input image(s). This parameter is supported for GPT image models that support input fidelity. `gpt-image-2` and `gpt-image-2-2026-04-21` ignore this parameter.

            - `const ToolImageGenerationInputFidelityHigh ToolImageGenerationInputFidelity = "high"`

            - `const ToolImageGenerationInputFidelityLow ToolImageGenerationInputFidelity = "low"`

          - `InputImageMask ToolImageGenerationInputImageMask`

            Optional mask for inpainting. Contains `image_url`
            (string, optional) and `file_id` (string, optional).

            - `FileID string`

              File ID for the mask image.

            - `ImageURL string`

              Base64-encoded mask image.

          - `Model string`

            The image generation model to use. One of `gpt-image-1`,
            `gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
            `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
            `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
            `gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
            `gpt-image-1`.

            - `string`

            - `string`

              - `const ToolImageGenerationModelGPTImage1 ToolImageGenerationModel = "gpt-image-1"`

              - `const ToolImageGenerationModelGPTImage1Mini ToolImageGenerationModel = "gpt-image-1-mini"`

              - `const ToolImageGenerationModelGPTImage2 ToolImageGenerationModel = "gpt-image-2"`

              - `const ToolImageGenerationModelGPTImage2_2026_04_21 ToolImageGenerationModel = "gpt-image-2-2026-04-21"`

              - `const ToolImageGenerationModelGPTImage2_5Sunburst ToolImageGenerationModel = "gpt-image-2.5-sunburst"`

              - `const ToolImageGenerationModelGPTImage2_5Sunburst2026_09_08 ToolImageGenerationModel = "gpt-image-2.5-sunburst-2026-09-08"`

              - `const ToolImageGenerationModelGPTImage2_5Flare ToolImageGenerationModel = "gpt-image-2.5-flare"`

              - `const ToolImageGenerationModelGPTImage2_5Flare2026_09_08 ToolImageGenerationModel = "gpt-image-2.5-flare-2026-09-08"`

              - `const ToolImageGenerationModelGPTImage1_5 ToolImageGenerationModel = "gpt-image-1.5"`

              - `const ToolImageGenerationModelChatgptImageLatest ToolImageGenerationModel = "chatgpt-image-latest"`

          - `Moderation string`

            Moderation level for the generated image. Default: `auto`.

            - `const ToolImageGenerationModerationAuto ToolImageGenerationModeration = "auto"`

            - `const ToolImageGenerationModerationLow ToolImageGenerationModeration = "low"`

          - `OutputCompression int64`

            Compression level for the output image. Default: 100.

          - `OutputFormat string`

            The output format of the generated image. One of `png`, `webp`, or
            `jpeg`. Default: `png`.

            - `const ToolImageGenerationOutputFormatPNG ToolImageGenerationOutputFormat = "png"`

            - `const ToolImageGenerationOutputFormatWebP ToolImageGenerationOutputFormat = "webp"`

            - `const ToolImageGenerationOutputFormatJPEG ToolImageGenerationOutputFormat = "jpeg"`

          - `PartialImages int64`

            Number of partial images to generate in streaming mode, from 0 (default value) to 3.

          - `Quality string`

            The quality of the generated image. The GPT image models support `low`,
            `medium`, and `high`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`,
            including their `2026-09-08` snapshots, also support `xhigh` and `max`.
            Default: `auto`.

            - `const ToolImageGenerationQualityLow ToolImageGenerationQuality = "low"`

            - `const ToolImageGenerationQualityMedium ToolImageGenerationQuality = "medium"`

            - `const ToolImageGenerationQualityHigh ToolImageGenerationQuality = "high"`

            - `const ToolImageGenerationQualityXhigh ToolImageGenerationQuality = "xhigh"`

            - `const ToolImageGenerationQualityMax ToolImageGenerationQuality = "max"`

            - `const ToolImageGenerationQualityAuto ToolImageGenerationQuality = "auto"`

          - `Size string`

            The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model's current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

            - `string`

            - `string`

              - `const ToolImageGenerationSize1024x1024 ToolImageGenerationSize = "1024x1024"`

              - `const ToolImageGenerationSize1024x1536 ToolImageGenerationSize = "1024x1536"`

              - `const ToolImageGenerationSize1536x1024 ToolImageGenerationSize = "1536x1024"`

              - `const ToolImageGenerationSizeAuto ToolImageGenerationSize = "auto"`

        - `type ToolLocalShell struct{…}`

          A tool that allows the model to execute shell commands in a local environment.

          - `Type LocalShell`

            The type of the local shell tool. Always `local_shell`.

            - `const LocalShellLocalShell LocalShell = "local_shell"`

        - `type FunctionShellTool struct{…}`

          A tool that allows the model to execute shell commands.

          - `Type Shell`

            The type of the shell tool. Always `shell`.

            - `const ShellShell Shell = "shell"`

          - `AllowedCallers []string`

            The tool invocation context(s).

            - `const FunctionShellToolAllowedCallerDirect FunctionShellToolAllowedCaller = "direct"`

            - `const FunctionShellToolAllowedCallerProgrammatic FunctionShellToolAllowedCaller = "programmatic"`

          - `Environment FunctionShellToolEnvironmentUnion`

            - `type ContainerAuto struct{…}`

              - `Type ContainerAuto`

                Automatically creates a container for this request

                - `const ContainerAutoContainerAuto ContainerAuto = "container_auto"`

              - `FileIDs []string`

                An optional list of uploaded files to make available to your code.

              - `MemoryLimit ContainerAutoMemoryLimit`

                The memory limit for the container.

                - `const ContainerAutoMemoryLimit1g ContainerAutoMemoryLimit = "1g"`

                - `const ContainerAutoMemoryLimit4g ContainerAutoMemoryLimit = "4g"`

                - `const ContainerAutoMemoryLimit16g ContainerAutoMemoryLimit = "16g"`

                - `const ContainerAutoMemoryLimit64g ContainerAutoMemoryLimit = "64g"`

              - `NetworkPolicy ContainerAutoNetworkPolicyUnion`

                Network access policy for the container.

                - `type ContainerNetworkPolicyDisabled struct{…}`

                - `type ContainerNetworkPolicyAllowlist struct{…}`

              - `Skills []ContainerAutoSkillUnion`

                An optional list of skills referenced by id or inline data.

                - `type SkillReference struct{…}`

                  - `SkillID string`

                    The ID of the referenced skill.

                  - `Type SkillReference`

                    References a skill created with the /v1/skills endpoint.

                    - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

                  - `Version string`

                    Optional skill version. Use a positive integer or 'latest'. Omit for default.

                - `type InlineSkill struct{…}`

                  - `Description string`

                    The description of the skill.

                  - `Name string`

                    The name of the skill.

                  - `Source InlineSkillSource`

                    Inline skill payload

                    - `Data string`

                      Base64-encoded skill zip bundle.

                    - `MediaType ApplicationZip`

                      The media type of the inline skill payload. Must be `application/zip`.

                      - `const ApplicationZipApplicationZip ApplicationZip = "application/zip"`

                    - `Type Base64`

                      The type of the inline skill source. Must be `base64`.

                      - `const Base64Base64 Base64 = "base64"`

                  - `Type Inline`

                    Defines an inline skill for this request.

                    - `const InlineInline Inline = "inline"`

            - `type LocalEnvironment struct{…}`

              - `Type Local`

                Use a local computer environment.

                - `const LocalLocal Local = "local"`

              - `Skills []LocalSkill`

                An optional list of skills.

                - `Description string`

                  The description of the skill.

                - `Name string`

                  The name of the skill.

                - `Path string`

                  The path to the directory containing the skill.

            - `type ContainerReference struct{…}`

              - `ContainerID string`

                The ID of the referenced container.

              - `Type ContainerReference`

                References a container created with the /v1/containers endpoint

                - `const ContainerReferenceContainerReference ContainerReference = "container_reference"`

        - `type CustomTool struct{…}`

          A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

          - `Name string`

            The name of the custom tool, used to identify it in tool calls.

          - `Type Custom`

            The type of the custom tool. Always `custom`.

            - `const CustomCustom Custom = "custom"`

          - `AllowedCallers []string`

            The tool invocation context(s).

            - `const CustomToolAllowedCallerDirect CustomToolAllowedCaller = "direct"`

            - `const CustomToolAllowedCallerProgrammatic CustomToolAllowedCaller = "programmatic"`

          - `Async bool`

            Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

          - `DeferLoading bool`

            Whether this tool should be deferred and discovered via tool search.

          - `Description string`

            Optional description of the custom tool, used to provide more context.

          - `Format CustomToolInputFormatUnion`

            The input format for the custom tool. Default is unconstrained text.

            - `type CustomToolInputFormatText struct{…}`

              Unconstrained free-form text.

              - `Type Text`

                Unconstrained text format. Always `text`.

                - `const TextText Text = "text"`

            - `type CustomToolInputFormatGrammar struct{…}`

              A grammar defined by the user.

              - `Definition string`

                The grammar definition.

              - `Syntax string`

                The syntax of the grammar definition. One of `lark` or `regex`.

                - `const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"`

                - `const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"`

              - `Type Grammar`

                Grammar format. Always `grammar`.

                - `const GrammarGrammar Grammar = "grammar"`

        - `type NamespaceTool struct{…}`

          Groups function/custom tools under a shared namespace.

          - `Description string`

            A description of the namespace shown to the model.

          - `Name string`

            The namespace name used in tool calls (for example, `crm`).

          - `Tools []NamespaceToolToolUnion`

            The function/custom tools available inside this namespace.

            - `type NamespaceToolToolFunction struct{…}`

              - `Name string`

              - `Type Function`

                - `const FunctionFunction Function = "function"`

              - `AllowedCallers []string`

                The tool invocation context(s).

                - `const NamespaceToolToolFunctionAllowedCallerDirect NamespaceToolToolFunctionAllowedCaller = "direct"`

                - `const NamespaceToolToolFunctionAllowedCallerProgrammatic NamespaceToolToolFunctionAllowedCaller = "programmatic"`

              - `Async bool`

                Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

              - `DeferLoading bool`

                Whether this function should be deferred and discovered via tool search.

              - `Description string`

              - `OutputSchema map[string, any]`

                A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

              - `Parameters any`

              - `Strict bool`

                Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

            - `type CustomTool struct{…}`

              A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

          - `Type Namespace`

            The type of the tool. Always `namespace`.

            - `const NamespaceNamespace Namespace = "namespace"`

        - `type ToolSearchTool struct{…}`

          Hosted or BYOT tool search configuration for deferred tools.

          - `Type ToolSearch`

            The type of the tool. Always `tool_search`.

            - `const ToolSearchToolSearch ToolSearch = "tool_search"`

          - `Description string`

            Description shown to the model for a client-executed tool search tool.

          - `Execution ToolSearchToolExecution`

            Whether tool search is executed by the server or by the client.

            - `const ToolSearchToolExecutionServer ToolSearchToolExecution = "server"`

            - `const ToolSearchToolExecutionClient ToolSearchToolExecution = "client"`

          - `Parameters any`

            Parameter schema for a client-executed tool search tool.

        - `type WebSearchPreviewTool struct{…}`

          This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

          - `Type WebSearchPreviewToolType`

            The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

            - `const WebSearchPreviewToolTypeWebSearchPreview WebSearchPreviewToolType = "web_search_preview"`

            - `const WebSearchPreviewToolTypeWebSearchPreview2025_03_11 WebSearchPreviewToolType = "web_search_preview_2025_03_11"`

          - `SearchContentTypes []string`

            - `const WebSearchPreviewToolSearchContentTypeText WebSearchPreviewToolSearchContentType = "text"`

            - `const WebSearchPreviewToolSearchContentTypeImage WebSearchPreviewToolSearchContentType = "image"`

          - `SearchContextSize WebSearchPreviewToolSearchContextSize`

            High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

            - `const WebSearchPreviewToolSearchContextSizeLow WebSearchPreviewToolSearchContextSize = "low"`

            - `const WebSearchPreviewToolSearchContextSizeMedium WebSearchPreviewToolSearchContextSize = "medium"`

            - `const WebSearchPreviewToolSearchContextSizeHigh WebSearchPreviewToolSearchContextSize = "high"`

          - `UserLocation WebSearchPreviewToolUserLocation`

            The approximate location of the user. If omitted or null, defaults to the United States. To avoid this fallback, pass `{"type": "approximate"}` without location fields. To localize results, provide the relevant location fields.

            - `Type Approximate`

              The type of location approximation. Always `approximate`.

              - `const ApproximateApproximate Approximate = "approximate"`

            - `City string`

              Free text input for the city of the user, e.g. `San Francisco`.

            - `Country string`

              The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

            - `Region string`

              Free text input for the region of the user, e.g. `California`.

            - `Timezone string`

              The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

        - `type ApplyPatchTool struct{…}`

          Allows the assistant to create, delete, or update files using unified diffs.

          - `Type ApplyPatch`

            The type of the tool. Always `apply_patch`.

            - `const ApplyPatchApplyPatch ApplyPatch = "apply_patch"`

          - `AllowedCallers []string`

            The tool invocation context(s).

            - `const ApplyPatchToolAllowedCallerDirect ApplyPatchToolAllowedCaller = "direct"`

            - `const ApplyPatchToolAllowedCallerProgrammatic ApplyPatchToolAllowedCaller = "programmatic"`

      - `Type ToolSearchOutput`

        The item type. Always `tool_search_output`.

        - `const ToolSearchOutputToolSearchOutput ToolSearchOutput = "tool_search_output"`

      - `ID string`

        The unique ID of this tool search output.

      - `CallID string`

        The unique ID of the tool search call generated by the model.

      - `Execution ResponseToolSearchOutputItemParamExecution`

        Whether tool search was executed by the server or by the client.

        - `const ResponseToolSearchOutputItemParamExecutionServer ResponseToolSearchOutputItemParamExecution = "server"`

        - `const ResponseToolSearchOutputItemParamExecutionClient ResponseToolSearchOutputItemParamExecution = "client"`

      - `Status ResponseToolSearchOutputItemParamStatus`

        The status of the tool search output.

        - `const ResponseToolSearchOutputItemParamStatusInProgress ResponseToolSearchOutputItemParamStatus = "in_progress"`

        - `const ResponseToolSearchOutputItemParamStatusCompleted ResponseToolSearchOutputItemParamStatus = "completed"`

        - `const ResponseToolSearchOutputItemParamStatusIncomplete ResponseToolSearchOutputItemParamStatus = "incomplete"`

    - `type ResponseInputItemAdditionalTools struct{…}`

      - `Role Developer`

        The role that provided the additional tools. Only `developer` is supported.

        - `const DeveloperDeveloper Developer = "developer"`

      - `Tools []ToolUnion`

        A list of additional tools made available at this item.

        - `type FunctionTool struct{…}`

          Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

        - `type FileSearchTool struct{…}`

          A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

        - `type ComputerTool struct{…}`

          A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

        - `type ComputerUsePreviewTool struct{…}`

          A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

        - `type WebSearchTool struct{…}`

          Search the Internet for sources related to the prompt. Learn more about the
          [web search tool](/api/docs/guides/tools-web-search).

        - `type ToolMcp struct{…}`

          Give the model access to additional tools via remote Model Context Protocol
          (MCP) servers. [Learn more about MCP](/api/docs/guides/tools-connectors-mcp).

        - `type ToolCodeInterpreter struct{…}`

          A tool that runs Python code to help generate a response to a prompt.

        - `type ToolProgrammaticToolCalling struct{…}`

        - `type ToolImageGeneration struct{…}`

          A tool that generates images using the GPT image models.

        - `type ToolLocalShell struct{…}`

          A tool that allows the model to execute shell commands in a local environment.

        - `type FunctionShellTool struct{…}`

          A tool that allows the model to execute shell commands.

        - `type CustomTool struct{…}`

          A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

        - `type NamespaceTool struct{…}`

          Groups function/custom tools under a shared namespace.

        - `type ToolSearchTool struct{…}`

          Hosted or BYOT tool search configuration for deferred tools.

        - `type WebSearchPreviewTool struct{…}`

          This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

        - `type ApplyPatchTool struct{…}`

          Allows the assistant to create, delete, or update files using unified diffs.

      - `Type AdditionalTools`

        The item type. Always `additional_tools`.

        - `const AdditionalToolsAdditionalTools AdditionalTools = "additional_tools"`

      - `ID string`

        The unique ID of this additional tools item.

    - `type ResponseConfigurationUpdateItemParamResp struct{…}`

      An update to the conversation's response configuration. The configuration
      remains in effect for subsequent responses until it is replaced by another
      configuration update.

      - `Type ConfigurationUpdate`

        The item type. Always `configuration_update`.

        - `const ConfigurationUpdateConfigurationUpdate ConfigurationUpdate = "configuration_update"`

      - `ID string`

        The unique ID of the configuration update item.

      - `Reasoning ResponseConfigurationUpdateItemParamReasoningResp`

        Updates to reasoning configuration. Only effort is supported.

        - `Effort ReasoningEffort`

          The reasoning effort to use for subsequent responses until another
          configuration update replaces it.

          - `const ReasoningEffortNone ReasoningEffort = "none"`

          - `const ReasoningEffortMinimal ReasoningEffort = "minimal"`

          - `const ReasoningEffortLow ReasoningEffort = "low"`

          - `const ReasoningEffortMedium ReasoningEffort = "medium"`

          - `const ReasoningEffortHigh ReasoningEffort = "high"`

          - `const ReasoningEffortXhigh ReasoningEffort = "xhigh"`

          - `const ReasoningEffortMax ReasoningEffort = "max"`

    - `type ResponseReasoningItem struct{…}`

      A description of the chain of thought used by a reasoning model while generating
      a response. Be sure to include these items in your `input` to the Responses API
      for subsequent turns of a conversation if you are manually
      [managing context](/api/docs/guides/conversation-state).

      - `ID string`

        The unique identifier of the reasoning content.

      - `Summary []ResponseReasoningItemSummary`

        Reasoning summary content.

        - `Text string`

          A summary of the reasoning output from the model so far.

        - `Type SummaryText`

          The type of the object. Always `summary_text`.

          - `const SummaryTextSummaryText SummaryText = "summary_text"`

      - `Type Reasoning`

        The type of the object. Always `reasoning`.

        - `const ReasoningReasoning Reasoning = "reasoning"`

      - `Content []ResponseReasoningItemContent`

        Reasoning text content.

        - `Text string`

          The reasoning text from the model.

        - `Type ReasoningText`

          The type of the reasoning text. Always `reasoning_text`.

          - `const ReasoningTextReasoningText ReasoningText = "reasoning_text"`

      - `EncryptedContent string`

        The encrypted content of the reasoning item. This is populated by default
        for reasoning items returned by `POST /v1/responses` and WebSocket
        `response.create` requests.

        When streaming, use the completed reasoning item and its
        `encrypted_content` from the `response.output_item.done` event in
        subsequent requests. The `encrypted_content` in
        `response.output_item.added` may be incomplete. This is especially
        important when `store` is `false` or when using Zero Data Retention.

      - `Status ResponseReasoningItemStatus`

        The status of the item. One of `in_progress`, `completed`, or
        `incomplete`. Populated when items are returned via API.

        - `const ResponseReasoningItemStatusInProgress ResponseReasoningItemStatus = "in_progress"`

        - `const ResponseReasoningItemStatusCompleted ResponseReasoningItemStatus = "completed"`

        - `const ResponseReasoningItemStatusIncomplete ResponseReasoningItemStatus = "incomplete"`

    - `type ResponseCompactionItemParamResp struct{…}`

      A compaction item generated by the [`v1/responses/compact` API](/api/reference/resources/responses/methods/compact).

      - `EncryptedContent string`

        The encrypted content of the compaction summary.

      - `Type Compaction`

        The type of the item. Always `compaction`.

        - `const CompactionCompaction Compaction = "compaction"`

      - `ID string`

        The ID of the compaction item.

    - `type ResponseInputItemImageGenerationCall struct{…}`

      An image generation request made by the model.

      - `ID string`

        The unique ID of the image generation call.

      - `Result string`

        The generated image encoded in base64.

      - `Status string`

        The status of the image generation call.

        - `const ResponseInputItemImageGenerationCallStatusInProgress ResponseInputItemImageGenerationCallStatus = "in_progress"`

        - `const ResponseInputItemImageGenerationCallStatusCompleted ResponseInputItemImageGenerationCallStatus = "completed"`

        - `const ResponseInputItemImageGenerationCallStatusGenerating ResponseInputItemImageGenerationCallStatus = "generating"`

        - `const ResponseInputItemImageGenerationCallStatusFailed ResponseInputItemImageGenerationCallStatus = "failed"`

      - `Type ImageGenerationCall`

        The type of the image generation call. Always `image_generation_call`.

        - `const ImageGenerationCallImageGenerationCall ImageGenerationCall = "image_generation_call"`

      - `Action string`

        The action used for image generation.

        - `const ResponseInputItemImageGenerationCallActionGenerate ResponseInputItemImageGenerationCallAction = "generate"`

        - `const ResponseInputItemImageGenerationCallActionEdit ResponseInputItemImageGenerationCallAction = "edit"`

        - `const ResponseInputItemImageGenerationCallActionAuto ResponseInputItemImageGenerationCallAction = "auto"`

      - `Background string`

        The background setting used for generation.

        - `const ResponseInputItemImageGenerationCallBackgroundTransparent ResponseInputItemImageGenerationCallBackground = "transparent"`

        - `const ResponseInputItemImageGenerationCallBackgroundOpaque ResponseInputItemImageGenerationCallBackground = "opaque"`

        - `const ResponseInputItemImageGenerationCallBackgroundAuto ResponseInputItemImageGenerationCallBackground = "auto"`

      - `OutputFormat string`

        The output format used for generation.

        - `const ResponseInputItemImageGenerationCallOutputFormatPNG ResponseInputItemImageGenerationCallOutputFormat = "png"`

        - `const ResponseInputItemImageGenerationCallOutputFormatWebP ResponseInputItemImageGenerationCallOutputFormat = "webp"`

        - `const ResponseInputItemImageGenerationCallOutputFormatJPEG ResponseInputItemImageGenerationCallOutputFormat = "jpeg"`

      - `Quality string`

        The quality of the image generated by the image generation tool call. One of `low`, `medium`, `high`, `xhigh`, `max`, or `auto`.

        - `const ResponseInputItemImageGenerationCallQualityLow ResponseInputItemImageGenerationCallQuality = "low"`

        - `const ResponseInputItemImageGenerationCallQualityMedium ResponseInputItemImageGenerationCallQuality = "medium"`

        - `const ResponseInputItemImageGenerationCallQualityHigh ResponseInputItemImageGenerationCallQuality = "high"`

        - `const ResponseInputItemImageGenerationCallQualityXhigh ResponseInputItemImageGenerationCallQuality = "xhigh"`

        - `const ResponseInputItemImageGenerationCallQualityMax ResponseInputItemImageGenerationCallQuality = "max"`

        - `const ResponseInputItemImageGenerationCallQualityAuto ResponseInputItemImageGenerationCallQuality = "auto"`

      - `RevisedPrompt string`

        The prompt that was used after any model prompt rewriting.

      - `Size string`

        The image dimensions as a `WIDTHxHEIGHT` string, for example `1536x864`.

        - `string`

        - `string`

          - `const ResponseInputItemImageGenerationCallSize1024x1024 ResponseInputItemImageGenerationCallSize = "1024x1024"`

          - `const ResponseInputItemImageGenerationCallSize1024x1536 ResponseInputItemImageGenerationCallSize = "1024x1536"`

          - `const ResponseInputItemImageGenerationCallSize1536x1024 ResponseInputItemImageGenerationCallSize = "1536x1024"`

    - `type ResponseCodeInterpreterToolCall struct{…}`

      A tool call to run code.

      - `ID string`

        The unique ID of the code interpreter tool call.

      - `Code string`

        The code to run, or null if not available.

      - `ContainerID string`

        The ID of the container used to run the code.

      - `Outputs []ResponseCodeInterpreterToolCallOutputUnion`

        The outputs generated by the code interpreter, such as logs or images.
        Can be null if no outputs are available.

        - `type ResponseCodeInterpreterToolCallOutputLogs struct{…}`

          The logs output from the code interpreter.

          - `Logs string`

            The logs output from the code interpreter.

          - `Type Logs`

            The type of the output. Always `logs`.

            - `const LogsLogs Logs = "logs"`

        - `type ResponseCodeInterpreterToolCallOutputImage struct{…}`

          The image output from the code interpreter.

          - `Type Image`

            The type of the output. Always `image`.

            - `const ImageImage Image = "image"`

          - `URL string`

            The URL of the image output from the code interpreter.

      - `Status ResponseCodeInterpreterToolCallStatus`

        The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

        - `const ResponseCodeInterpreterToolCallStatusInProgress ResponseCodeInterpreterToolCallStatus = "in_progress"`

        - `const ResponseCodeInterpreterToolCallStatusCompleted ResponseCodeInterpreterToolCallStatus = "completed"`

        - `const ResponseCodeInterpreterToolCallStatusIncomplete ResponseCodeInterpreterToolCallStatus = "incomplete"`

        - `const ResponseCodeInterpreterToolCallStatusInterpreting ResponseCodeInterpreterToolCallStatus = "interpreting"`

        - `const ResponseCodeInterpreterToolCallStatusFailed ResponseCodeInterpreterToolCallStatus = "failed"`

      - `Type CodeInterpreterCall`

        The type of the code interpreter tool call. Always `code_interpreter_call`.

        - `const CodeInterpreterCallCodeInterpreterCall CodeInterpreterCall = "code_interpreter_call"`

    - `type ResponseInputItemLocalShellCall struct{…}`

      A tool call to run a command on the local shell.

      - `ID string`

        The unique ID of the local shell call.

      - `Action ResponseInputItemLocalShellCallAction`

        Execute a shell command on the server.

        - `Command []string`

          The command to run.

        - `Env map[string, string]`

          Environment variables to set for the command.

        - `Type Exec`

          The type of the local shell action. Always `exec`.

          - `const ExecExec Exec = "exec"`

        - `TimeoutMs int64`

          Optional timeout in milliseconds for the command.

        - `User string`

          Optional user to run the command as.

        - `WorkingDirectory string`

          Optional working directory to run the command in.

      - `CallID string`

        The unique ID of the local shell tool call generated by the model.

      - `Status string`

        The status of the local shell call.

        - `const ResponseInputItemLocalShellCallStatusInProgress ResponseInputItemLocalShellCallStatus = "in_progress"`

        - `const ResponseInputItemLocalShellCallStatusCompleted ResponseInputItemLocalShellCallStatus = "completed"`

        - `const ResponseInputItemLocalShellCallStatusIncomplete ResponseInputItemLocalShellCallStatus = "incomplete"`

      - `Type LocalShellCall`

        The type of the local shell call. Always `local_shell_call`.

        - `const LocalShellCallLocalShellCall LocalShellCall = "local_shell_call"`

    - `type ResponseInputItemLocalShellCallOutput struct{…}`

      The output of a local shell tool call.

      - `ID string`

        The unique ID of the local shell tool call generated by the model.

      - `Output string`

        A JSON string of the output of the local shell tool call.

      - `Type LocalShellCallOutput`

        The type of the local shell tool call output. Always `local_shell_call_output`.

        - `const LocalShellCallOutputLocalShellCallOutput LocalShellCallOutput = "local_shell_call_output"`

      - `Status string`

        The status of the item. One of `in_progress`, `completed`, or `incomplete`.

        - `const ResponseInputItemLocalShellCallOutputStatusInProgress ResponseInputItemLocalShellCallOutputStatus = "in_progress"`

        - `const ResponseInputItemLocalShellCallOutputStatusCompleted ResponseInputItemLocalShellCallOutputStatus = "completed"`

        - `const ResponseInputItemLocalShellCallOutputStatusIncomplete ResponseInputItemLocalShellCallOutputStatus = "incomplete"`

    - `type ResponseInputItemShellCall struct{…}`

      A tool representing a request to execute one or more shell commands.

      - `Action ResponseInputItemShellCallAction`

        The shell commands and limits that describe how to run the tool call.

        - `Commands []string`

          Ordered shell commands for the execution environment to run.

        - `MaxOutputLength int64`

          Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

        - `TimeoutMs int64`

          Maximum wall-clock time in milliseconds to allow the shell commands to run.

      - `CallID string`

        The unique ID of the shell tool call generated by the model.

      - `Type ShellCall`

        The type of the item. Always `shell_call`.

        - `const ShellCallShellCall ShellCall = "shell_call"`

      - `ID string`

        The unique ID of the shell tool call. Populated when this item is returned via API.

      - `Caller ResponseInputItemShellCallCallerUnion`

        The execution context that produced this tool call.

        - `type ResponseInputItemShellCallCallerDirect struct{…}`

          - `Type Direct`

            The caller type. Always `direct`.

            - `const DirectDirect Direct = "direct"`

        - `type ResponseInputItemShellCallCallerProgram struct{…}`

          - `CallerID string`

            The call ID of the program item that produced this tool call.

          - `Type Program`

            The caller type. Always `program`.

            - `const ProgramProgram Program = "program"`

      - `Environment ResponseInputItemShellCallEnvironmentUnion`

        The environment to execute the shell commands in.

        - `type LocalEnvironment struct{…}`

        - `type ContainerReference struct{…}`

      - `Status string`

        The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

        - `const ResponseInputItemShellCallStatusInProgress ResponseInputItemShellCallStatus = "in_progress"`

        - `const ResponseInputItemShellCallStatusCompleted ResponseInputItemShellCallStatus = "completed"`

        - `const ResponseInputItemShellCallStatusIncomplete ResponseInputItemShellCallStatus = "incomplete"`

    - `type ResponseInputItemShellCallOutput struct{…}`

      The streamed output items emitted by a shell tool call.

      - `CallID string`

        The unique ID of the shell tool call generated by the model.

      - `Output []ResponseFunctionShellCallOutputContent`

        Captured chunks of stdout and stderr output, along with their associated outcomes.

        - `Outcome ResponseFunctionShellCallOutputContentOutcomeUnion`

          The exit or timeout outcome associated with this shell call.

          - `type ResponseFunctionShellCallOutputContentOutcomeTimeout struct{…}`

            Indicates that the shell call exceeded its configured time limit.

            - `Type Timeout`

              The outcome type. Always `timeout`.

              - `const TimeoutTimeout Timeout = "timeout"`

          - `type ResponseFunctionShellCallOutputContentOutcomeExit struct{…}`

            Indicates that the shell commands finished and returned an exit code.

            - `ExitCode int64`

              The exit code returned by the shell process.

            - `Type Exit`

              The outcome type. Always `exit`.

              - `const ExitExit Exit = "exit"`

        - `Stderr string`

          Captured stderr output for the shell call.

        - `Stdout string`

          Captured stdout output for the shell call.

      - `Type ShellCallOutput`

        The type of the item. Always `shell_call_output`.

        - `const ShellCallOutputShellCallOutput ShellCallOutput = "shell_call_output"`

      - `ID string`

        The unique ID of the shell tool call output. Populated when this item is returned via API.

      - `Caller ResponseInputItemShellCallOutputCallerUnion`

        The execution context that produced this tool call.

        - `type ResponseInputItemShellCallOutputCallerDirect struct{…}`

          - `Type Direct`

            The caller type. Always `direct`.

            - `const DirectDirect Direct = "direct"`

        - `type ResponseInputItemShellCallOutputCallerProgram struct{…}`

          - `CallerID string`

            The call ID of the program item that produced this tool call.

          - `Type Program`

            The caller type. Always `program`.

            - `const ProgramProgram Program = "program"`

      - `MaxOutputLength int64`

        The maximum number of UTF-8 characters captured for this shell call's combined output.

      - `Status string`

        The status of the shell call output.

        - `const ResponseInputItemShellCallOutputStatusInProgress ResponseInputItemShellCallOutputStatus = "in_progress"`

        - `const ResponseInputItemShellCallOutputStatusCompleted ResponseInputItemShellCallOutputStatus = "completed"`

        - `const ResponseInputItemShellCallOutputStatusIncomplete ResponseInputItemShellCallOutputStatus = "incomplete"`

    - `type ResponseInputItemApplyPatchCall struct{…}`

      A tool call representing a request to create, delete, or update files using diff patches.

      - `CallID string`

        The unique ID of the apply patch tool call generated by the model.

      - `Operation ResponseInputItemApplyPatchCallOperationUnion`

        The specific create, delete, or update instruction for the apply_patch tool call.

        - `type ResponseInputItemApplyPatchCallOperationCreateFile struct{…}`

          Instruction for creating a new file via the apply_patch tool.

          - `Diff string`

            Unified diff content to apply when creating the file.

          - `Path string`

            Path of the file to create relative to the workspace root.

          - `Type CreateFile`

            The operation type. Always `create_file`.

            - `const CreateFileCreateFile CreateFile = "create_file"`

        - `type ResponseInputItemApplyPatchCallOperationDeleteFile struct{…}`

          Instruction for deleting an existing file via the apply_patch tool.

          - `Path string`

            Path of the file to delete relative to the workspace root.

          - `Type DeleteFile`

            The operation type. Always `delete_file`.

            - `const DeleteFileDeleteFile DeleteFile = "delete_file"`

        - `type ResponseInputItemApplyPatchCallOperationUpdateFile struct{…}`

          Instruction for updating an existing file via the apply_patch tool.

          - `Diff string`

            Unified diff content to apply to the existing file.

          - `Path string`

            Path of the file to update relative to the workspace root.

          - `Type UpdateFile`

            The operation type. Always `update_file`.

            - `const UpdateFileUpdateFile UpdateFile = "update_file"`

      - `Status string`

        The status of the apply patch tool call. One of `in_progress` or `completed`.

        - `const ResponseInputItemApplyPatchCallStatusInProgress ResponseInputItemApplyPatchCallStatus = "in_progress"`

        - `const ResponseInputItemApplyPatchCallStatusCompleted ResponseInputItemApplyPatchCallStatus = "completed"`

      - `Type ApplyPatchCall`

        The type of the item. Always `apply_patch_call`.

        - `const ApplyPatchCallApplyPatchCall ApplyPatchCall = "apply_patch_call"`

      - `ID string`

        The unique ID of the apply patch tool call. Populated when this item is returned via API.

      - `Caller ResponseInputItemApplyPatchCallCallerUnion`

        The execution context that produced this tool call.

        - `type ResponseInputItemApplyPatchCallCallerDirect struct{…}`

          - `Type Direct`

            The caller type. Always `direct`.

            - `const DirectDirect Direct = "direct"`

        - `type ResponseInputItemApplyPatchCallCallerProgram struct{…}`

          - `CallerID string`

            The call ID of the program item that produced this tool call.

          - `Type Program`

            The caller type. Always `program`.

            - `const ProgramProgram Program = "program"`

    - `type ResponseInputItemApplyPatchCallOutput struct{…}`

      The streamed output emitted by an apply patch tool call.

      - `CallID string`

        The unique ID of the apply patch tool call generated by the model.

      - `Status string`

        The status of the apply patch tool call output. One of `completed` or `failed`.

        - `const ResponseInputItemApplyPatchCallOutputStatusCompleted ResponseInputItemApplyPatchCallOutputStatus = "completed"`

        - `const ResponseInputItemApplyPatchCallOutputStatusFailed ResponseInputItemApplyPatchCallOutputStatus = "failed"`

      - `Type ApplyPatchCallOutput`

        The type of the item. Always `apply_patch_call_output`.

        - `const ApplyPatchCallOutputApplyPatchCallOutput ApplyPatchCallOutput = "apply_patch_call_output"`

      - `ID string`

        The unique ID of the apply patch tool call output. Populated when this item is returned via API.

      - `Caller ResponseInputItemApplyPatchCallOutputCallerUnion`

        The execution context that produced this tool call.

        - `type ResponseInputItemApplyPatchCallOutputCallerDirect struct{…}`

          - `Type Direct`

            The caller type. Always `direct`.

            - `const DirectDirect Direct = "direct"`

        - `type ResponseInputItemApplyPatchCallOutputCallerProgram struct{…}`

          - `CallerID string`

            The call ID of the program item that produced this tool call.

          - `Type Program`

            The caller type. Always `program`.

            - `const ProgramProgram Program = "program"`

      - `Output string`

        Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

    - `type ResponseInputItemMcpListTools struct{…}`

      A list of tools available on an MCP server.

      - `ID string`

        The unique ID of the list.

      - `ServerLabel string`

        The label of the MCP server.

      - `Tools []ResponseInputItemMcpListToolsTool`

        The tools available on the server.

        - `InputSchema any`

          The JSON schema describing the tool's input.

        - `Name string`

          The name of the tool.

        - `Annotations any`

          Additional annotations about the tool.

        - `Description string`

          The description of the tool.

      - `Type McpListTools`

        The type of the item. Always `mcp_list_tools`.

        - `const McpListToolsMcpListTools McpListTools = "mcp_list_tools"`

      - `Error string`

        Error message if the server could not list tools.

    - `type ResponseInputItemMcpApprovalRequest struct{…}`

      A request for human approval of a tool invocation.

      - `ID string`

        The unique ID of the approval request.

      - `Arguments string`

        A JSON string of arguments for the tool.

      - `Name string`

        The name of the tool to run.

      - `ServerLabel string`

        The label of the MCP server making the request.

      - `Type McpApprovalRequest`

        The type of the item. Always `mcp_approval_request`.

        - `const McpApprovalRequestMcpApprovalRequest McpApprovalRequest = "mcp_approval_request"`

    - `type ResponseInputItemMcpApprovalResponse struct{…}`

      A response to an MCP approval request.

      - `ApprovalRequestID string`

        The ID of the approval request being answered.

      - `Approve bool`

        Whether the request was approved.

      - `Type McpApprovalResponse`

        The type of the item. Always `mcp_approval_response`.

        - `const McpApprovalResponseMcpApprovalResponse McpApprovalResponse = "mcp_approval_response"`

      - `ID string`

        The unique ID of the approval response

      - `Reason string`

        Optional reason for the decision.

    - `type ResponseInputItemMcpCall struct{…}`

      An invocation of a tool on an MCP server.

      - `ID string`

        The unique ID of the tool call.

      - `Arguments string`

        A JSON string of the arguments passed to the tool.

      - `Name string`

        The name of the tool that was run.

      - `ServerLabel string`

        The label of the MCP server running the tool.

      - `Type McpCall`

        The type of the item. Always `mcp_call`.

        - `const McpCallMcpCall McpCall = "mcp_call"`

      - `ApprovalRequestID string`

        Unique identifier for the MCP tool call approval request.
        Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

      - `Error McpToolCallErrorUnion`

        The error from the tool call, if any.

        - `type McpToolCallErrorMcpProtocolError struct{…}`

          - `Code int64`

          - `Message string`

          - `Type McpProtocolError`

            - `const McpProtocolErrorMcpProtocolError McpProtocolError = "mcp_protocol_error"`

        - `type McpToolCallErrorMcpToolExecutionError struct{…}`

          - `Content any`

          - `Type McpToolExecutionError`

            - `const McpToolExecutionErrorMcpToolExecutionError McpToolExecutionError = "mcp_tool_execution_error"`

        - `type McpToolCallErrorHTTPError struct{…}`

          - `Code int64`

          - `Message string`

          - `Type HTTPError`

            - `const HTTPErrorHTTPError HTTPError = "http_error"`

      - `Output string`

        The output from the tool call.

      - `Status string`

        The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

        - `const ResponseInputItemMcpCallStatusInProgress ResponseInputItemMcpCallStatus = "in_progress"`

        - `const ResponseInputItemMcpCallStatusCompleted ResponseInputItemMcpCallStatus = "completed"`

        - `const ResponseInputItemMcpCallStatusIncomplete ResponseInputItemMcpCallStatus = "incomplete"`

        - `const ResponseInputItemMcpCallStatusCalling ResponseInputItemMcpCallStatus = "calling"`

        - `const ResponseInputItemMcpCallStatusFailed ResponseInputItemMcpCallStatus = "failed"`

    - `type ResponseCustomToolCallOutput struct{…}`

      The output of a custom tool call from your code, being sent back to the model.

      - `CallID string`

        The call ID, used to map this custom tool call output to a custom tool call.

      - `Output ResponseCustomToolCallOutputOutputUnion`

        The output from the custom tool call generated by your code.
        Can be a string or an list of output content.

        - `string`

        - `type ResponseCustomToolCallOutputOutputOutputContentList []ResponseCustomToolCallOutputOutputOutputContentListItemUnion`

          Text, image, or file output of the custom tool call.

          - `type ResponseInputText struct{…}`

            A text input to the model.

          - `type ResponseInputImage struct{…}`

            An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

          - `type ResponseInputFile struct{…}`

            A file input to the model.

      - `Type CustomToolCallOutput`

        The type of the custom tool call output. Always `custom_tool_call_output`.

        - `const CustomToolCallOutputCustomToolCallOutput CustomToolCallOutput = "custom_tool_call_output"`

      - `ID string`

        The unique ID of the custom tool call output in the OpenAI platform.

      - `Caller ResponseCustomToolCallOutputCallerUnion`

        The execution context that produced this tool call.

        - `type ResponseCustomToolCallOutputCallerDirect struct{…}`

          - `Type Direct`

            The caller type. Always `direct`.

            - `const DirectDirect Direct = "direct"`

        - `type ResponseCustomToolCallOutputCallerProgram struct{…}`

          - `CallerID string`

            The call ID of the program item that produced this tool call.

          - `Type Program`

            The caller type. Always `program`.

            - `const ProgramProgram Program = "program"`

    - `type ResponseCustomToolCall struct{…}`

      A call to a custom tool created by the model.

      - `CallID string`

        An identifier used to map this custom tool call to a tool call output.

      - `Input string`

        The input for the custom tool call generated by the model.

      - `Name string`

        The name of the custom tool being called.

      - `Type CustomToolCall`

        The type of the custom tool call. Always `custom_tool_call`.

        - `const CustomToolCallCustomToolCall CustomToolCall = "custom_tool_call"`

      - `ID string`

        The unique ID of the custom tool call in the OpenAI platform.

      - `Async bool`

        Whether the custom tool call runs asynchronously.

      - `Caller ResponseCustomToolCallCallerUnion`

        The execution context that produced this tool call.

        - `type ResponseCustomToolCallCallerDirect struct{…}`

          - `Type Direct`

            - `const DirectDirect Direct = "direct"`

        - `type ResponseCustomToolCallCallerProgram struct{…}`

          - `CallerID string`

            The call ID of the program item that produced this tool call.

          - `Type Program`

            - `const ProgramProgram Program = "program"`

      - `Namespace string`

        The namespace of the custom tool being called.

    - `type ResponseInputItemCompactionTrigger struct{…}`

      Compacts the current context. Must be the final input item.

      - `Type CompactionTrigger`

        The type of the item. Always `compaction_trigger`.

        - `const CompactionTriggerCompactionTrigger CompactionTrigger = "compaction_trigger"`

    - `type ResponseInputItemItemReference struct{…}`

      An internal identifier for an item to reference.

      - `ID string`

        The ID of the item to reference.

      - `Type string`

        The type of item to reference. Always `item_reference`.

        - `const ResponseInputItemItemReferenceTypeItemReference ResponseInputItemItemReferenceType = "item_reference"`

    - `type ResponseInputItemProgram struct{…}`

      - `ID string`

        The unique ID of this program item.

      - `CallID string`

        The stable call ID of the program item.

      - `Code string`

        The JavaScript source executed by programmatic tool calling.

      - `Fingerprint string`

        Opaque program replay fingerprint that must be round-tripped.

      - `Type Program`

        The item type. Always `program`.

        - `const ProgramProgram Program = "program"`

    - `type ResponseInputItemProgramOutput struct{…}`

      - `ID string`

        The unique ID of this program output item.

      - `CallID string`

        The call ID of the program item.

      - `Result string`

        The result produced by the program item.

      - `Status string`

        The terminal status of the program output.

        - `const ResponseInputItemProgramOutputStatusCompleted ResponseInputItemProgramOutputStatus = "completed"`

        - `const ResponseInputItemProgramOutputStatusIncomplete ResponseInputItemProgramOutputStatus = "incomplete"`

      - `Type ProgramOutput`

        The item type. Always `program_output`.

        - `const ProgramOutputProgramOutput ProgramOutput = "program_output"`

  - `Type ResponseItemCreate`

    The Live client event type. Always `response.item.create`.

    - `const ResponseItemCreateResponseItemCreate ResponseItemCreate = "response.item.create"`

  - `EventID string`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Responses Delegation Config

- `type ResponsesDelegationConfig struct{…}`

  Model, prompt, and tool settings for tasks delegated by the Live session to a Responses backend.

  - `Model string`

    The model used for server-owned Responses delegations.

  - `Instructions string`

    Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

  - `MaxOutputTokens int64`

    Maximum number of output tokens for each delegated response.

  - `ParallelToolCalls bool`

    Whether the delegated Responses model may request multiple tool calls in a single response.

  - `Reasoning ResponsesDelegationConfigReasoning`

    Reasoning settings passed to each delegated Responses request.

    - `Effort string`

      How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

      - `const ResponsesDelegationConfigReasoningEffortNone ResponsesDelegationConfigReasoningEffort = "none"`

      - `const ResponsesDelegationConfigReasoningEffortMinimal ResponsesDelegationConfigReasoningEffort = "minimal"`

      - `const ResponsesDelegationConfigReasoningEffortLow ResponsesDelegationConfigReasoningEffort = "low"`

      - `const ResponsesDelegationConfigReasoningEffortMedium ResponsesDelegationConfigReasoningEffort = "medium"`

      - `const ResponsesDelegationConfigReasoningEffortHigh ResponsesDelegationConfigReasoningEffort = "high"`

      - `const ResponsesDelegationConfigReasoningEffortXhigh ResponsesDelegationConfigReasoningEffort = "xhigh"`

    - `Summary string`

      The reasoning summary to request from the delegated Responses model, when supported.

      - `const ResponsesDelegationConfigReasoningSummaryConcise ResponsesDelegationConfigReasoningSummary = "concise"`

      - `const ResponsesDelegationConfigReasoningSummaryDetailed ResponsesDelegationConfigReasoningSummary = "detailed"`

      - `const ResponsesDelegationConfigReasoningSummaryAuto ResponsesDelegationConfigReasoningSummary = "auto"`

  - `ServiceTier ResponsesDelegationConfigServiceTier`

    Service tier for delegated Responses requests.

    - `const ResponsesDelegationConfigServiceTierAuto ResponsesDelegationConfigServiceTier = "auto"`

    - `const ResponsesDelegationConfigServiceTierDefault ResponsesDelegationConfigServiceTier = "default"`

    - `const ResponsesDelegationConfigServiceTierFastTierTempPilot ResponsesDelegationConfigServiceTier = "fast_tier_temp_pilot"`

    - `const ResponsesDelegationConfigServiceTierFlex ResponsesDelegationConfigServiceTier = "flex"`

    - `const ResponsesDelegationConfigServiceTierPriority ResponsesDelegationConfigServiceTier = "priority"`

    - `const ResponsesDelegationConfigServiceTierUltrafast ResponsesDelegationConfigServiceTier = "ultrafast"`

  - `Text ResponsesDelegationConfigText`

    Text generation settings passed to each delegated Responses request.

    - `Verbosity string`

      The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

      - `const ResponsesDelegationConfigTextVerbosityLow ResponsesDelegationConfigTextVerbosity = "low"`

      - `const ResponsesDelegationConfigTextVerbosityMedium ResponsesDelegationConfigTextVerbosity = "medium"`

      - `const ResponsesDelegationConfigTextVerbosityHigh ResponsesDelegationConfigTextVerbosity = "high"`

  - `ToolChoice ResponsesDelegationConfigToolChoiceUnion`

    Controls which tool the Responses backend uses when handling a task delegated by the Live model.

    - `string`

      - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "auto"`

      - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "none"`

      - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "required"`

    - `ResponsesDelegationConfigToolChoiceLiveFunctionToolChoiceParam`

      - `Name string`

      - `Type Function`

        - `const FunctionFunction Function = "function"`

    - `ResponsesDelegationConfigToolChoiceLiveMcpToolChoiceParam`

      - `Name string`

      - `ServerLabel string`

      - `Type Mcp`

        - `const McpMcp Mcp = "mcp"`

  - `Tools []ResponsesDelegationConfigToolUnion`

    Tools available to the Responses backend while it handles tasks delegated by the Live model.

    - `type FunctionTool struct{…}`

      A function tool available to the Responses backend when the Live model delegates a task.

      - `Name string`

        The name the delegated Responses model uses when calling this function.

      - `Type Function`

        The tool type. Always `function`.

        - `const FunctionFunction Function = "function"`

      - `Description string`

        What the function does and when the delegated Responses model should call it.

      - `Parameters map[string, any]`

        A JSON Schema object describing the arguments accepted by the function.

      - `Strict bool`

        Whether the delegated Responses model must follow the function’s parameter schema exactly.

    - `ResponsesDelegationConfigToolWebSearch`

      - `Type WebSearch`

        The tool type. Always `web_search`.

        - `const WebSearchWebSearch WebSearch = "web_search"`

### Responses Delegation Update Config

- `type ResponsesDelegationUpdateConfig struct{…}`

  Updates to the Responses backend of an existing Live session. Omitted settings retain their current values.

  - `Instructions string`

    Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

  - `MaxOutputTokens int64`

    Maximum number of output tokens for each delegated response.

  - `Model string`

    The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.

  - `ParallelToolCalls bool`

    Whether the delegated Responses model may request multiple tool calls in a single response.

  - `Reasoning ResponsesDelegationUpdateConfigReasoning`

    Reasoning settings passed to each delegated Responses request.

    - `Effort string`

      How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

      - `const ResponsesDelegationUpdateConfigReasoningEffortNone ResponsesDelegationUpdateConfigReasoningEffort = "none"`

      - `const ResponsesDelegationUpdateConfigReasoningEffortMinimal ResponsesDelegationUpdateConfigReasoningEffort = "minimal"`

      - `const ResponsesDelegationUpdateConfigReasoningEffortLow ResponsesDelegationUpdateConfigReasoningEffort = "low"`

      - `const ResponsesDelegationUpdateConfigReasoningEffortMedium ResponsesDelegationUpdateConfigReasoningEffort = "medium"`

      - `const ResponsesDelegationUpdateConfigReasoningEffortHigh ResponsesDelegationUpdateConfigReasoningEffort = "high"`

      - `const ResponsesDelegationUpdateConfigReasoningEffortXhigh ResponsesDelegationUpdateConfigReasoningEffort = "xhigh"`

    - `Summary string`

      The reasoning summary to request from the delegated Responses model, when supported.

      - `const ResponsesDelegationUpdateConfigReasoningSummaryConcise ResponsesDelegationUpdateConfigReasoningSummary = "concise"`

      - `const ResponsesDelegationUpdateConfigReasoningSummaryDetailed ResponsesDelegationUpdateConfigReasoningSummary = "detailed"`

      - `const ResponsesDelegationUpdateConfigReasoningSummaryAuto ResponsesDelegationUpdateConfigReasoningSummary = "auto"`

  - `ServiceTier ResponsesDelegationUpdateConfigServiceTier`

    Service tier for delegated Responses requests.

    - `const ResponsesDelegationUpdateConfigServiceTierAuto ResponsesDelegationUpdateConfigServiceTier = "auto"`

    - `const ResponsesDelegationUpdateConfigServiceTierDefault ResponsesDelegationUpdateConfigServiceTier = "default"`

    - `const ResponsesDelegationUpdateConfigServiceTierFastTierTempPilot ResponsesDelegationUpdateConfigServiceTier = "fast_tier_temp_pilot"`

    - `const ResponsesDelegationUpdateConfigServiceTierFlex ResponsesDelegationUpdateConfigServiceTier = "flex"`

    - `const ResponsesDelegationUpdateConfigServiceTierPriority ResponsesDelegationUpdateConfigServiceTier = "priority"`

    - `const ResponsesDelegationUpdateConfigServiceTierUltrafast ResponsesDelegationUpdateConfigServiceTier = "ultrafast"`

  - `Text ResponsesDelegationUpdateConfigText`

    Text generation settings passed to each delegated Responses request.

    - `Verbosity string`

      The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

      - `const ResponsesDelegationUpdateConfigTextVerbosityLow ResponsesDelegationUpdateConfigTextVerbosity = "low"`

      - `const ResponsesDelegationUpdateConfigTextVerbosityMedium ResponsesDelegationUpdateConfigTextVerbosity = "medium"`

      - `const ResponsesDelegationUpdateConfigTextVerbosityHigh ResponsesDelegationUpdateConfigTextVerbosity = "high"`

  - `ToolChoice ResponsesDelegationUpdateConfigToolChoiceUnion`

    Controls which tool the Responses backend uses when handling a task delegated by the Live model.

    - `string`

      - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "auto"`

      - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "none"`

      - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "required"`

    - `ResponsesDelegationUpdateConfigToolChoiceLiveFunctionToolChoiceParam`

      - `Name string`

      - `Type Function`

        - `const FunctionFunction Function = "function"`

    - `ResponsesDelegationUpdateConfigToolChoiceLiveMcpToolChoiceParam`

      - `Name string`

      - `ServerLabel string`

      - `Type Mcp`

        - `const McpMcp Mcp = "mcp"`

  - `Tools []ResponsesDelegationUpdateConfigToolUnion`

    Tools available to the Responses backend while it handles tasks delegated by the Live model.

    - `type FunctionTool struct{…}`

      A function tool available to the Responses backend when the Live model delegates a task.

      - `Name string`

        The name the delegated Responses model uses when calling this function.

      - `Type Function`

        The tool type. Always `function`.

        - `const FunctionFunction Function = "function"`

      - `Description string`

        What the function does and when the delegated Responses model should call it.

      - `Parameters map[string, any]`

        A JSON Schema object describing the arguments accepted by the function.

      - `Strict bool`

        Whether the delegated Responses model must follow the function’s parameter schema exactly.

    - `ResponsesDelegationUpdateConfigToolWebSearch`

      - `Type WebSearch`

        The tool type. Always `web_search`.

        - `const WebSearchWebSearch WebSearch = "web_search"`

### Server Event

- `type ServerEventUnion interface{…}`

  Server events for Live. Response lifecycle events are wrapped inside response.event; dispatch the nested event by its full type and tolerate new response event types. Follow the [Live prompting guide](https://developers.openai.com/api/docs/guides/live-prompting) when designing the conversation and delegation policy.

  - `type SessionStartedEvent struct{…}`

    Returned when a Live session has started. Contains the resolved session configuration, including server defaults.

    - `EventID string`

      The unique ID of the Live server event.

    - `Session SessionResource`

      The resolved Live session configuration and server-assigned session metadata.

      - `ID string`

        The unique ID of the Live session. Use this ID for sideband connections, forking, and recording download.

      - `ExpiresAt int64`

        The Unix timestamp, in seconds, at which the Live session expires.

      - `Model SessionResourceModel`

        The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

        - `string`

        - `SessionResourceModel`

          - `const SessionResourceModelGPTLive1 SessionResourceModel = "gpt-live-1"`

      - `Status Active`

        The status of the session snapshot. Always `active`, including the final snapshot in session.closed; use the event type to determine that the session has closed.

        - `const ActiveActive Active = "active"`

      - `Audio SessionResourceAudio`

        Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

        - `Format AudioFormatUnion`

          Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

          - `AudioFormatAudioPCM`

            - `Rate int64`

              Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

              - `const AudioFormatAudioPCMRate16000 AudioFormatAudioPCMRate = 16000`

              - `const AudioFormatAudioPCMRate24000 AudioFormatAudioPCMRate = 24000`

            - `Type AudioPCM`

              The audio encoding. Always `audio/pcm`.

              - `const AudioPCMAudioPCM AudioPCM = "audio/pcm"`

          - `AudioFormatAudioPCMU`

            - `Rate int64`

              Audio sample rate in hertz. G.711 audio uses 8000 Hz.

            - `Type AudioPCMU`

              The audio encoding. Always `audio/pcmu`.

              - `const AudioPCMUAudioPCMU AudioPCMU = "audio/pcmu"`

          - `AudioFormatAudioPCMA`

            - `Rate int64`

              Audio sample rate in hertz. G.711 audio uses 8000 Hz.

            - `Type AudioPCMA`

              The audio encoding. Always `audio/pcma`.

              - `const AudioPCMAAudioPCMA AudioPCMA = "audio/pcma"`

        - `Output SessionResourceAudioOutput`

          The voice used for speech generated by the Live model.

          - `Voice SessionResourceAudioOutputVoiceUnion`

            The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

            - `string`

            - `type BuiltInVoice string`

              A built-in voice available for Live speech.

              - `const BuiltInVoiceAlloy BuiltInVoice = "alloy"`

              - `const BuiltInVoiceAsh BuiltInVoice = "ash"`

              - `const BuiltInVoiceBallad BuiltInVoice = "ballad"`

              - `const BuiltInVoiceBeacon BuiltInVoice = "beacon"`

              - `const BuiltInVoiceBossa BuiltInVoice = "bossa"`

              - `const BuiltInVoiceCedar BuiltInVoice = "cedar"`

              - `const BuiltInVoiceCinder BuiltInVoice = "cinder"`

              - `const BuiltInVoiceCoral BuiltInVoice = "coral"`

              - `const BuiltInVoiceDelta BuiltInVoice = "delta"`

              - `const BuiltInVoiceEcho BuiltInVoice = "echo"`

              - `const BuiltInVoiceGleam BuiltInVoice = "gleam"`

              - `const BuiltInVoiceMarin BuiltInVoice = "marin"`

              - `const BuiltInVoiceMeridian BuiltInVoice = "meridian"`

              - `const BuiltInVoiceQuartz BuiltInVoice = "quartz"`

              - `const BuiltInVoiceRipple BuiltInVoice = "ripple"`

              - `const BuiltInVoiceSage BuiltInVoice = "sage"`

              - `const BuiltInVoiceShimmer BuiltInVoice = "shimmer"`

              - `const BuiltInVoiceStone BuiltInVoice = "stone"`

              - `const BuiltInVoiceTempo BuiltInVoice = "tempo"`

              - `const BuiltInVoiceVerse BuiltInVoice = "verse"`

              - `const BuiltInVoiceVesper BuiltInVoice = "vesper"`

              - `const BuiltInVoiceWillow BuiltInVoice = "willow"`

            - `type CustomVoice struct{…}`

              - `ID string`

      - `Client ClientConfig`

        Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

        - `DataChannel DataChannelConfig`

          Client and server event permissions for the WebRTC frontend data channel.

          - `AllowedClientEvents DataChannelConfigAllowedClientEventsUnion`

            Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

            - `All`

              - `const AllAll All = "all"`

            - `[]string`

          - `AllowedServerEvents DataChannelConfigAllowedServerEventsUnion`

            Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

            - `All`

              - `const AllAll All = "all"`

            - `[]ServerEventSelector`

              - `Type string`

                The outer Live server event type. Use 'response.event' for Responses events.

              - `ResponseEvent string`

                The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

      - `Delegation SessionResourceDelegationUnion`

        Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

        - `type ClientDelegation struct{…}`

          Delegate tasks to your application. The Live session emits delegation events that your backend handles.

          - `Type Client`

            The delegation owner. Always `client` for tasks handled by your application.

            - `const ClientClient Client = "client"`

        - `SessionResourceDelegationResponses`

          - `Responses ResponsesDelegationConfig`

            Backend model, prompt, and tools used when the Live session delegates a task to Responses.

            - `Model string`

              The model used for server-owned Responses delegations.

            - `Instructions string`

              Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

            - `MaxOutputTokens int64`

              Maximum number of output tokens for each delegated response.

            - `ParallelToolCalls bool`

              Whether the delegated Responses model may request multiple tool calls in a single response.

            - `Reasoning ResponsesDelegationConfigReasoning`

              Reasoning settings passed to each delegated Responses request.

              - `Effort string`

                How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

                - `const ResponsesDelegationConfigReasoningEffortNone ResponsesDelegationConfigReasoningEffort = "none"`

                - `const ResponsesDelegationConfigReasoningEffortMinimal ResponsesDelegationConfigReasoningEffort = "minimal"`

                - `const ResponsesDelegationConfigReasoningEffortLow ResponsesDelegationConfigReasoningEffort = "low"`

                - `const ResponsesDelegationConfigReasoningEffortMedium ResponsesDelegationConfigReasoningEffort = "medium"`

                - `const ResponsesDelegationConfigReasoningEffortHigh ResponsesDelegationConfigReasoningEffort = "high"`

                - `const ResponsesDelegationConfigReasoningEffortXhigh ResponsesDelegationConfigReasoningEffort = "xhigh"`

              - `Summary string`

                The reasoning summary to request from the delegated Responses model, when supported.

                - `const ResponsesDelegationConfigReasoningSummaryConcise ResponsesDelegationConfigReasoningSummary = "concise"`

                - `const ResponsesDelegationConfigReasoningSummaryDetailed ResponsesDelegationConfigReasoningSummary = "detailed"`

                - `const ResponsesDelegationConfigReasoningSummaryAuto ResponsesDelegationConfigReasoningSummary = "auto"`

            - `ServiceTier ResponsesDelegationConfigServiceTier`

              Service tier for delegated Responses requests.

              - `const ResponsesDelegationConfigServiceTierAuto ResponsesDelegationConfigServiceTier = "auto"`

              - `const ResponsesDelegationConfigServiceTierDefault ResponsesDelegationConfigServiceTier = "default"`

              - `const ResponsesDelegationConfigServiceTierFastTierTempPilot ResponsesDelegationConfigServiceTier = "fast_tier_temp_pilot"`

              - `const ResponsesDelegationConfigServiceTierFlex ResponsesDelegationConfigServiceTier = "flex"`

              - `const ResponsesDelegationConfigServiceTierPriority ResponsesDelegationConfigServiceTier = "priority"`

              - `const ResponsesDelegationConfigServiceTierUltrafast ResponsesDelegationConfigServiceTier = "ultrafast"`

            - `Text ResponsesDelegationConfigText`

              Text generation settings passed to each delegated Responses request.

              - `Verbosity string`

                The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

                - `const ResponsesDelegationConfigTextVerbosityLow ResponsesDelegationConfigTextVerbosity = "low"`

                - `const ResponsesDelegationConfigTextVerbosityMedium ResponsesDelegationConfigTextVerbosity = "medium"`

                - `const ResponsesDelegationConfigTextVerbosityHigh ResponsesDelegationConfigTextVerbosity = "high"`

            - `ToolChoice ResponsesDelegationConfigToolChoiceUnion`

              Controls which tool the Responses backend uses when handling a task delegated by the Live model.

              - `string`

                - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "auto"`

                - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "none"`

                - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "required"`

              - `ResponsesDelegationConfigToolChoiceLiveFunctionToolChoiceParam`

                - `Name string`

                - `Type Function`

                  - `const FunctionFunction Function = "function"`

              - `ResponsesDelegationConfigToolChoiceLiveMcpToolChoiceParam`

                - `Name string`

                - `ServerLabel string`

                - `Type Mcp`

                  - `const McpMcp Mcp = "mcp"`

            - `Tools []ResponsesDelegationConfigToolUnion`

              Tools available to the Responses backend while it handles tasks delegated by the Live model.

              - `type FunctionTool struct{…}`

                A function tool available to the Responses backend when the Live model delegates a task.

                - `Name string`

                  The name the delegated Responses model uses when calling this function.

                - `Type Function`

                  The tool type. Always `function`.

                  - `const FunctionFunction Function = "function"`

                - `Description string`

                  What the function does and when the delegated Responses model should call it.

                - `Parameters map[string, any]`

                  A JSON Schema object describing the arguments accepted by the function.

                - `Strict bool`

                  Whether the delegated Responses model must follow the function’s parameter schema exactly.

              - `ResponsesDelegationConfigToolWebSearch`

                - `Type WebSearch`

                  The tool type. Always `web_search`.

                  - `const WebSearchWebSearch WebSearch = "web_search"`

          - `Type Responses`

            The delegation owner. Always `responses` for tasks handled by the Responses API.

            - `const ResponsesResponses Responses = "responses"`

      - `Input []InitialItemUnion`

        Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

        - `InitialItemDeveloper`

          - `Content []InitialItemDeveloperContent`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `Text string`

              The message text to include in the Live session’s initial conversation history.

            - `Type string`

              The text content type. Always `input_text`.

              - `const InitialItemDeveloperContentTypeInputText InitialItemDeveloperContentType = "input_text"`

          - `Role Developer`

            The author of this history message. Always `developer`.

            - `const DeveloperDeveloper Developer = "developer"`

          - `ID string`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Status string`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `const InitialItemDeveloperStatusIncomplete InitialItemDeveloperStatus = "incomplete"`

            - `const InitialItemDeveloperStatusCompleted InitialItemDeveloperStatus = "completed"`

          - `Type string`

            The history item type. Always `message`.

            - `const InitialItemDeveloperTypeMessage InitialItemDeveloperType = "message"`

        - `InitialItemUser`

          - `Content []InitialItemUserContent`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `Text string`

              The message text to include in the Live session’s initial conversation history.

            - `Type string`

              The text content type. Always `input_text`.

              - `const InitialItemUserContentTypeInputText InitialItemUserContentType = "input_text"`

          - `Role User`

            The author of this history message. Always `user`.

            - `const UserUser User = "user"`

          - `ID string`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Status string`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `const InitialItemUserStatusIncomplete InitialItemUserStatus = "incomplete"`

            - `const InitialItemUserStatusCompleted InitialItemUserStatus = "completed"`

          - `Type string`

            The history item type. Always `message`.

            - `const InitialItemUserTypeMessage InitialItemUserType = "message"`

        - `InitialItemAssistant`

          - `Content []InitialItemAssistantContentUnion`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `InitialItemAssistantContentText`

              - `Text string`

                The message text to include in the Live session’s initial conversation history.

              - `Type string`

                The text content type. Always `text`.

                - `const InitialItemAssistantContentTextTypeText InitialItemAssistantContentTextType = "text"`

            - `InitialItemAssistantContentOutputText`

              - `Text string`

                The message text to include in the Live session’s initial conversation history.

              - `Type OutputText`

                The text content type. Always `output_text`.

                - `const OutputTextOutputText OutputText = "output_text"`

          - `Role Assistant`

            The author of this history message. Always `assistant`.

            - `const AssistantAssistant Assistant = "assistant"`

          - `ID string`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Status string`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `const InitialItemAssistantStatusIncomplete InitialItemAssistantStatus = "incomplete"`

            - `const InitialItemAssistantStatusCompleted InitialItemAssistantStatus = "completed"`

          - `Type string`

            The history item type. Always `message`.

            - `const InitialItemAssistantTypeMessage InitialItemAssistantType = "message"`

      - `Instructions string`

        Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

      - `Store bool`

        Whether to store the session for later forking and recording download. Defaults to false for new sessions.

    - `Type SessionStarted`

      The event type, always `session.started`.

      - `const SessionStartedSessionStarted SessionStarted = "session.started"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type SessionUpdatedEvent struct{…}`

    Returned when a Live session update is accepted. Contains the resolved session configuration after the update.

    - `EventID string`

      The unique ID of the Live server event.

    - `Session SessionResource`

      The resolved Live session configuration and server-assigned session metadata.

    - `Type SessionUpdated`

      The event type, always `session.updated`.

      - `const SessionUpdatedSessionUpdated SessionUpdated = "session.updated"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type InputAudioMutedEvent struct{…}`

    Returned when a session.input_audio.mute command is accepted. Input audio is no longer sent to the model; sideband audio reflection continues.

    - `EventID string`

      The unique ID of the Live server event.

    - `Type SessionInputAudioMuted`

      The event type, always `session.input_audio.muted`.

      - `const SessionInputAudioMutedSessionInputAudioMuted SessionInputAudioMuted = "session.input_audio.muted"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type InputAudioUnmutedEvent struct{…}`

    Returned when a session.input_audio.unmute command is accepted. Input audio is sent to the model again.

    - `EventID string`

      The unique ID of the Live server event.

    - `Type SessionInputAudioUnmuted`

      The event type, always `session.input_audio.unmuted`.

      - `const SessionInputAudioUnmutedSessionInputAudioUnmuted SessionInputAudioUnmuted = "session.input_audio.unmuted"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type InstructionsAppendedEvent struct{…}`

    Returned when a session.instructions.append command is accepted into the Live session timeline. Acknowledges the appended instructions without guaranteeing that the model has acted on them.

    - `EndMs int64`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `EventID string`

      The unique ID of the Live server event.

    - `StartMs int64`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `Type SessionInstructionsAppended`

      The event type, always `session.instructions.appended`.

      - `const SessionInstructionsAppendedSessionInstructionsAppended SessionInstructionsAppended = "session.instructions.appended"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type ThinkingAppendedEvent struct{…}`

    Returned when a session.thinking.append command is accepted into the Live session timeline. Acknowledges the added reasoning context without guaranteeing any spoken output.

    - `EndMs int64`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `EventID string`

      The unique ID of the Live server event.

    - `StartMs int64`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `Type SessionThinkingAppended`

      The event type, always `session.thinking.appended`.

      - `const SessionThinkingAppendedSessionThinkingAppended SessionThinkingAppended = "session.thinking.appended"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type CommentaryAppendedEvent struct{…}`

    Returned when a session.commentary.append command is accepted into the Live session timeline. Acknowledges the added commentary without guaranteeing exact wording or completed audio playback.

    - `EndMs int64`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `EventID string`

      The unique ID of the Live server event.

    - `StartMs int64`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `Type SessionCommentaryAppended`

      The event type, always `session.commentary.appended`.

      - `const SessionCommentaryAppendedSessionCommentaryAppended SessionCommentaryAppended = "session.commentary.appended"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `ServerEventSessionInputAudioAppend`

    - `Audio string`

      Base64-encoded raw mono PCM16LE at 24 kHz received from the primary transport, reflected to the sideband before model-input muting. This server event uses the same audio key as the client command, but is not an acknowledgment of it.

    - `Type SessionInputAudioAppend`

      The event type, always `session.input_audio.append`.

      - `const SessionInputAudioAppendSessionInputAudioAppend SessionInputAudioAppend = "session.input_audio.append"`

  - `type OutputAudioDeltaEvent struct{…}`

    An audio chunk generated by the Live model. Decode and play primary WebSocket chunks in delivery order using the configured session audio format. Sideband connections receive reflected output audio with timestamps.

    - `Delta string`

      Base64-encoded raw audio. Primary WebSocket events use the session's configured format; reflected sideband events use mono PCM16LE at 24 kHz.

    - `Type SessionOutputAudioDelta`

      The event type, always `session.output_audio.delta`.

      - `const SessionOutputAudioDeltaSessionOutputAudioDelta SessionOutputAudioDelta = "session.output_audio.delta"`

    - `EndMs int64`

      Exclusive session-relative end in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket. Dropped output frames leave gaps between reflected ranges.

    - `StartMs int64`

      Inclusive session-relative start in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket.

  - `type InputTranscriptDeltaEvent struct{…}`

    A transcript fragment for user input audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

    - `Delta string`

      The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

    - `EndMs int64`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `EventID string`

      The unique ID of the Live server event.

    - `StartMs int64`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `Type SessionInputTranscriptDelta`

      The event type, always `session.input_transcript.delta`.

      - `const SessionInputTranscriptDeltaSessionInputTranscriptDelta SessionInputTranscriptDelta = "session.input_transcript.delta"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type OutputTranscriptDeltaEvent struct{…}`

    A transcript fragment for assistant output audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

    - `Delta string`

      The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

    - `EndMs int64`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `EventID string`

      The unique ID of the Live server event.

    - `StartMs int64`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `Type SessionOutputTranscriptDelta`

      The event type, always `session.output_transcript.delta`.

      - `const SessionOutputTranscriptDeltaSessionOutputTranscriptDelta SessionOutputTranscriptDelta = "session.output_transcript.delta"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type DelegationCreatedEvent struct{…}`

    Returned when the Live model delegates work to your application or a Responses backend. Contains delegation metadata and the position on the session timeline where the work was delegated.

    - `Delegation DelegationCreatedEventDelegation`

      The delegated work identifier and destination. This object contains metadata, not the task text.

      - `ID string`

        The unique ID of the delegation. Use this as delegation_id when replying to client-owned work or correlating Responses events.

      - `Target string`

        Where the Live model delegated the work: `client` for your application, or `responses` for the configured Responses backend.

        - `string`

          - `const DelegationCreatedEventDelegationTargetStringClient DelegationCreatedEventDelegationTargetString = "client"`

          - `const DelegationCreatedEventDelegationTargetStringResponses DelegationCreatedEventDelegationTargetString = "responses"`

      - `Type Delegation`

        The object type, always `delegation`.

        - `const DelegationDelegation Delegation = "delegation"`

      - `ResponseID string`

        The ID of the Responses API response associated with a Responses delegation. Omitted for client delegations.

    - `EventID string`

      The unique ID of the Live server event.

    - `OffsetMs int64`

      The position on the Live session timeline where the delegation was created, in milliseconds from the beginning of the session.

    - `Type SessionDelegationCreated`

      The event type, always `session.delegation.created`.

      - `const SessionDelegationCreatedSessionDelegationCreated SessionDelegationCreated = "session.delegation.created"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type ResponseEvent struct{…}`

    A streaming Responses API event from a backend delegated to by the Live session. Use the outer delegation_id to associate the nested stream with its Live delegation.

    - `Event map[string, any]`

      The nested Responses streaming event. Dispatch on its type field. Response lifecycle snapshots omit input and clear instructions, tools, and output to keep messages small; consume granular output events for the generated content.

    - `EventID string`

      The unique ID of the Live server event.

    - `Type ResponseEvent`

      The event type, always `response.event`.

      - `const ResponseEventResponseEvent ResponseEvent = "response.event"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

    - `DelegationID string`

      The Live delegation associated with the nested Responses event. May be null or omitted when the event cannot be correlated with a delegation.

  - `type SessionUsageUpdatedEvent struct{…}`

    Reports cumulative Live audio usage and, when available, the most recent context-window usage. Delegated Responses token usage is reported separately in response.event events.

    - `EventID string`

      The unique ID of the Live server event.

    - `Type SessionUsageUpdated`

      The event type, always `session.usage.updated`.

      - `const SessionUsageUpdatedSessionUsageUpdated SessionUsageUpdated = "session.usage.updated"`

    - `Usage SessionUsage`

      The cumulative Live audio usage so far.

      - `Seconds float64`

        The cumulative Live audio duration in seconds. Do not sum this value across usage events.

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

    - `ContextWindow SessionUsageUpdatedEventContextWindow`

      The latest measured Live context-window usage. Omitted when the context limit is unknown.

      - `UsageRatio float64`

        The latest active context token count divided by the Live model context limit. Can decrease after compaction and may lag between measured audio frames.

  - `type SessionClosedEvent struct{…}`

    Returned after the Live session finishes finalizing, with the close reason, final session snapshot, and cumulative audio usage. A connection closing without this event does not confirm successful finalization.

    - `EventID string`

      The unique ID of the Live server event.

    - `Reason SessionClosedEventReasonString`

      Why the Live session ended: `close_requested` for an application close or hangup request, `expired` for the session duration limit, `content` for a safety filter, `remote_hangup` for a graceful remote disconnect, or `connection_lost` for an unexpected primary or upstream disconnection.

      - `string`

        - `const SessionClosedEventReasonStringCloseRequested SessionClosedEventReasonString = "close_requested"`

        - `const SessionClosedEventReasonStringExpired SessionClosedEventReasonString = "expired"`

        - `const SessionClosedEventReasonStringContent SessionClosedEventReasonString = "content"`

        - `const SessionClosedEventReasonStringRemoteHangup SessionClosedEventReasonString = "remote_hangup"`

        - `const SessionClosedEventReasonStringConnectionLost SessionClosedEventReasonString = "connection_lost"`

    - `Session SessionResource`

      The resolved Live session configuration and server-assigned session metadata.

    - `Type SessionClosed`

      The event type, always `session.closed`.

      - `const SessionClosedSessionClosed SessionClosed = "session.closed"`

    - `Usage SessionUsage`

      The final cumulative Live audio usage after session finalization.

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type ErrorEvent struct{…}`

    Reports an error in the Live session, such as an invalid client command. Use error.client_event_id, when present, to identify the command that caused the error.

    - `Error Error`

      Details of the Live error and the client command that caused it, when known.

      - `Code string`

        A machine-readable code identifying the Live error, such as `unknown_parameter`.

      - `Message string`

        A human-readable explanation of the Live error.

      - `Type string`

        The category of error, such as `invalid_request_error` for an invalid Live client command.

      - `ClientEventID string`

        The event_id of the client command that caused the error, when supplied.

      - `Param string`

        The parameter that caused the error, when applicable, such as `session.voice`.

    - `EventID string`

      The unique ID of the Live server event.

    - `Type Error`

      The event type, always `error`.

      - `const ErrorError Error = "error"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type InfoEvent struct{…}`

    An informational notice about the Live session, such as the event permissions applied to a frontend data channel.

    - `Code string`

      A machine-readable code for the notice, such as `data_channel_permissions`.

    - `EventID string`

      The unique ID of the Live server event.

    - `Message string`

      A human-readable explanation of the Live session notice.

    - `Type Info`

      The event type, always `info`.

      - `const InfoInfo Info = "info"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `ServerEventTransportDtmfReceived`

    - `Event string`

    - `EventID string`

    - `Type TransportDtmfReceived`

      - `const TransportDtmfReceivedTransportDtmfReceived TransportDtmfReceived = "transport.dtmf.received"`

  - `ServerEventTransportDtmfSend`

    - `Event string`

    - `EventID string`

    - `Type TransportDtmfSend`

      - `const TransportDtmfSendTransportDtmfSend TransportDtmfSend = "transport.dtmf.send"`

    - `ClientEventID string`

      The event_id of the client command, when supplied.

  - `ServerEventTransportRinging`

    - `EventID string`

    - `SessionID string`

      The canonical Live session ID.

    - `Type TransportRinging`

      - `const TransportRingingTransportRinging TransportRinging = "transport.ringing"`

  - `ServerEventTransportAnswered`

    - `EventID string`

    - `SessionID string`

      The canonical Live session ID.

    - `Type TransportAnswered`

      - `const TransportAnsweredTransportAnswered TransportAnswered = "transport.answered"`

  - `ServerEventTransportFailed`

    - `Error ServerEventTransportFailedError`

      - `Code string`

        The call setup failure code.

      - `Message string`

      - `Type CallError`

        - `const CallErrorCallError CallError = "call_error"`

      - `Param string`

        The parameter related to the error, if any. Empty when no parameter applies.

    - `EventID string`

    - `SessionID string`

      The canonical Live session ID.

    - `Type TransportFailed`

      - `const TransportFailedTransportFailed TransportFailed = "transport.failed"`

### Server Event Selector

- `type ServerEventSelector struct{…}`

  A Live server event selector for the WebRTC frontend data channel.

  - `Type string`

    The outer Live server event type. Use 'response.event' for Responses events.

  - `ResponseEvent string`

    The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

### Session Close Event

- `type SessionCloseEvent struct{…}`

  Request that the Live session close. The terminal `session.closed` event contains the close reason and final usage.

  - `Type SessionClose`

    The Live client event type. Always `session.close`.

    - `const SessionCloseSessionClose SessionClose = "session.close"`

  - `EventID string`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Session Closed Event

- `type SessionClosedEvent struct{…}`

  Returned after the Live session finishes finalizing, with the close reason, final session snapshot, and cumulative audio usage. A connection closing without this event does not confirm successful finalization.

  - `EventID string`

    The unique ID of the Live server event.

  - `Reason SessionClosedEventReasonString`

    Why the Live session ended: `close_requested` for an application close or hangup request, `expired` for the session duration limit, `content` for a safety filter, `remote_hangup` for a graceful remote disconnect, or `connection_lost` for an unexpected primary or upstream disconnection.

    - `string`

      - `const SessionClosedEventReasonStringCloseRequested SessionClosedEventReasonString = "close_requested"`

      - `const SessionClosedEventReasonStringExpired SessionClosedEventReasonString = "expired"`

      - `const SessionClosedEventReasonStringContent SessionClosedEventReasonString = "content"`

      - `const SessionClosedEventReasonStringRemoteHangup SessionClosedEventReasonString = "remote_hangup"`

      - `const SessionClosedEventReasonStringConnectionLost SessionClosedEventReasonString = "connection_lost"`

  - `Session SessionResource`

    The resolved Live session configuration and server-assigned session metadata.

    - `ID string`

      The unique ID of the Live session. Use this ID for sideband connections, forking, and recording download.

    - `ExpiresAt int64`

      The Unix timestamp, in seconds, at which the Live session expires.

    - `Model SessionResourceModel`

      The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

      - `string`

      - `SessionResourceModel`

        - `const SessionResourceModelGPTLive1 SessionResourceModel = "gpt-live-1"`

    - `Status Active`

      The status of the session snapshot. Always `active`, including the final snapshot in session.closed; use the event type to determine that the session has closed.

      - `const ActiveActive Active = "active"`

    - `Audio SessionResourceAudio`

      Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

      - `Format AudioFormatUnion`

        Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

        - `AudioFormatAudioPCM`

          - `Rate int64`

            Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

            - `const AudioFormatAudioPCMRate16000 AudioFormatAudioPCMRate = 16000`

            - `const AudioFormatAudioPCMRate24000 AudioFormatAudioPCMRate = 24000`

          - `Type AudioPCM`

            The audio encoding. Always `audio/pcm`.

            - `const AudioPCMAudioPCM AudioPCM = "audio/pcm"`

        - `AudioFormatAudioPCMU`

          - `Rate int64`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `Type AudioPCMU`

            The audio encoding. Always `audio/pcmu`.

            - `const AudioPCMUAudioPCMU AudioPCMU = "audio/pcmu"`

        - `AudioFormatAudioPCMA`

          - `Rate int64`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `Type AudioPCMA`

            The audio encoding. Always `audio/pcma`.

            - `const AudioPCMAAudioPCMA AudioPCMA = "audio/pcma"`

      - `Output SessionResourceAudioOutput`

        The voice used for speech generated by the Live model.

        - `Voice SessionResourceAudioOutputVoiceUnion`

          The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

          - `string`

          - `type BuiltInVoice string`

            A built-in voice available for Live speech.

            - `const BuiltInVoiceAlloy BuiltInVoice = "alloy"`

            - `const BuiltInVoiceAsh BuiltInVoice = "ash"`

            - `const BuiltInVoiceBallad BuiltInVoice = "ballad"`

            - `const BuiltInVoiceBeacon BuiltInVoice = "beacon"`

            - `const BuiltInVoiceBossa BuiltInVoice = "bossa"`

            - `const BuiltInVoiceCedar BuiltInVoice = "cedar"`

            - `const BuiltInVoiceCinder BuiltInVoice = "cinder"`

            - `const BuiltInVoiceCoral BuiltInVoice = "coral"`

            - `const BuiltInVoiceDelta BuiltInVoice = "delta"`

            - `const BuiltInVoiceEcho BuiltInVoice = "echo"`

            - `const BuiltInVoiceGleam BuiltInVoice = "gleam"`

            - `const BuiltInVoiceMarin BuiltInVoice = "marin"`

            - `const BuiltInVoiceMeridian BuiltInVoice = "meridian"`

            - `const BuiltInVoiceQuartz BuiltInVoice = "quartz"`

            - `const BuiltInVoiceRipple BuiltInVoice = "ripple"`

            - `const BuiltInVoiceSage BuiltInVoice = "sage"`

            - `const BuiltInVoiceShimmer BuiltInVoice = "shimmer"`

            - `const BuiltInVoiceStone BuiltInVoice = "stone"`

            - `const BuiltInVoiceTempo BuiltInVoice = "tempo"`

            - `const BuiltInVoiceVerse BuiltInVoice = "verse"`

            - `const BuiltInVoiceVesper BuiltInVoice = "vesper"`

            - `const BuiltInVoiceWillow BuiltInVoice = "willow"`

          - `type CustomVoice struct{…}`

            - `ID string`

    - `Client ClientConfig`

      Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

      - `DataChannel DataChannelConfig`

        Client and server event permissions for the WebRTC frontend data channel.

        - `AllowedClientEvents DataChannelConfigAllowedClientEventsUnion`

          Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

          - `All`

            - `const AllAll All = "all"`

          - `[]string`

        - `AllowedServerEvents DataChannelConfigAllowedServerEventsUnion`

          Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

          - `All`

            - `const AllAll All = "all"`

          - `[]ServerEventSelector`

            - `Type string`

              The outer Live server event type. Use 'response.event' for Responses events.

            - `ResponseEvent string`

              The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

    - `Delegation SessionResourceDelegationUnion`

      Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

      - `type ClientDelegation struct{…}`

        Delegate tasks to your application. The Live session emits delegation events that your backend handles.

        - `Type Client`

          The delegation owner. Always `client` for tasks handled by your application.

          - `const ClientClient Client = "client"`

      - `SessionResourceDelegationResponses`

        - `Responses ResponsesDelegationConfig`

          Backend model, prompt, and tools used when the Live session delegates a task to Responses.

          - `Model string`

            The model used for server-owned Responses delegations.

          - `Instructions string`

            Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

          - `MaxOutputTokens int64`

            Maximum number of output tokens for each delegated response.

          - `ParallelToolCalls bool`

            Whether the delegated Responses model may request multiple tool calls in a single response.

          - `Reasoning ResponsesDelegationConfigReasoning`

            Reasoning settings passed to each delegated Responses request.

            - `Effort string`

              How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

              - `const ResponsesDelegationConfigReasoningEffortNone ResponsesDelegationConfigReasoningEffort = "none"`

              - `const ResponsesDelegationConfigReasoningEffortMinimal ResponsesDelegationConfigReasoningEffort = "minimal"`

              - `const ResponsesDelegationConfigReasoningEffortLow ResponsesDelegationConfigReasoningEffort = "low"`

              - `const ResponsesDelegationConfigReasoningEffortMedium ResponsesDelegationConfigReasoningEffort = "medium"`

              - `const ResponsesDelegationConfigReasoningEffortHigh ResponsesDelegationConfigReasoningEffort = "high"`

              - `const ResponsesDelegationConfigReasoningEffortXhigh ResponsesDelegationConfigReasoningEffort = "xhigh"`

            - `Summary string`

              The reasoning summary to request from the delegated Responses model, when supported.

              - `const ResponsesDelegationConfigReasoningSummaryConcise ResponsesDelegationConfigReasoningSummary = "concise"`

              - `const ResponsesDelegationConfigReasoningSummaryDetailed ResponsesDelegationConfigReasoningSummary = "detailed"`

              - `const ResponsesDelegationConfigReasoningSummaryAuto ResponsesDelegationConfigReasoningSummary = "auto"`

          - `ServiceTier ResponsesDelegationConfigServiceTier`

            Service tier for delegated Responses requests.

            - `const ResponsesDelegationConfigServiceTierAuto ResponsesDelegationConfigServiceTier = "auto"`

            - `const ResponsesDelegationConfigServiceTierDefault ResponsesDelegationConfigServiceTier = "default"`

            - `const ResponsesDelegationConfigServiceTierFastTierTempPilot ResponsesDelegationConfigServiceTier = "fast_tier_temp_pilot"`

            - `const ResponsesDelegationConfigServiceTierFlex ResponsesDelegationConfigServiceTier = "flex"`

            - `const ResponsesDelegationConfigServiceTierPriority ResponsesDelegationConfigServiceTier = "priority"`

            - `const ResponsesDelegationConfigServiceTierUltrafast ResponsesDelegationConfigServiceTier = "ultrafast"`

          - `Text ResponsesDelegationConfigText`

            Text generation settings passed to each delegated Responses request.

            - `Verbosity string`

              The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

              - `const ResponsesDelegationConfigTextVerbosityLow ResponsesDelegationConfigTextVerbosity = "low"`

              - `const ResponsesDelegationConfigTextVerbosityMedium ResponsesDelegationConfigTextVerbosity = "medium"`

              - `const ResponsesDelegationConfigTextVerbosityHigh ResponsesDelegationConfigTextVerbosity = "high"`

          - `ToolChoice ResponsesDelegationConfigToolChoiceUnion`

            Controls which tool the Responses backend uses when handling a task delegated by the Live model.

            - `string`

              - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "auto"`

              - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "none"`

              - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "required"`

            - `ResponsesDelegationConfigToolChoiceLiveFunctionToolChoiceParam`

              - `Name string`

              - `Type Function`

                - `const FunctionFunction Function = "function"`

            - `ResponsesDelegationConfigToolChoiceLiveMcpToolChoiceParam`

              - `Name string`

              - `ServerLabel string`

              - `Type Mcp`

                - `const McpMcp Mcp = "mcp"`

          - `Tools []ResponsesDelegationConfigToolUnion`

            Tools available to the Responses backend while it handles tasks delegated by the Live model.

            - `type FunctionTool struct{…}`

              A function tool available to the Responses backend when the Live model delegates a task.

              - `Name string`

                The name the delegated Responses model uses when calling this function.

              - `Type Function`

                The tool type. Always `function`.

                - `const FunctionFunction Function = "function"`

              - `Description string`

                What the function does and when the delegated Responses model should call it.

              - `Parameters map[string, any]`

                A JSON Schema object describing the arguments accepted by the function.

              - `Strict bool`

                Whether the delegated Responses model must follow the function’s parameter schema exactly.

            - `ResponsesDelegationConfigToolWebSearch`

              - `Type WebSearch`

                The tool type. Always `web_search`.

                - `const WebSearchWebSearch WebSearch = "web_search"`

        - `Type Responses`

          The delegation owner. Always `responses` for tasks handled by the Responses API.

          - `const ResponsesResponses Responses = "responses"`

    - `Input []InitialItemUnion`

      Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

      - `InitialItemDeveloper`

        - `Content []InitialItemDeveloperContent`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `Text string`

            The message text to include in the Live session’s initial conversation history.

          - `Type string`

            The text content type. Always `input_text`.

            - `const InitialItemDeveloperContentTypeInputText InitialItemDeveloperContentType = "input_text"`

        - `Role Developer`

          The author of this history message. Always `developer`.

          - `const DeveloperDeveloper Developer = "developer"`

        - `ID string`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Status string`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `const InitialItemDeveloperStatusIncomplete InitialItemDeveloperStatus = "incomplete"`

          - `const InitialItemDeveloperStatusCompleted InitialItemDeveloperStatus = "completed"`

        - `Type string`

          The history item type. Always `message`.

          - `const InitialItemDeveloperTypeMessage InitialItemDeveloperType = "message"`

      - `InitialItemUser`

        - `Content []InitialItemUserContent`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `Text string`

            The message text to include in the Live session’s initial conversation history.

          - `Type string`

            The text content type. Always `input_text`.

            - `const InitialItemUserContentTypeInputText InitialItemUserContentType = "input_text"`

        - `Role User`

          The author of this history message. Always `user`.

          - `const UserUser User = "user"`

        - `ID string`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Status string`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `const InitialItemUserStatusIncomplete InitialItemUserStatus = "incomplete"`

          - `const InitialItemUserStatusCompleted InitialItemUserStatus = "completed"`

        - `Type string`

          The history item type. Always `message`.

          - `const InitialItemUserTypeMessage InitialItemUserType = "message"`

      - `InitialItemAssistant`

        - `Content []InitialItemAssistantContentUnion`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `InitialItemAssistantContentText`

            - `Text string`

              The message text to include in the Live session’s initial conversation history.

            - `Type string`

              The text content type. Always `text`.

              - `const InitialItemAssistantContentTextTypeText InitialItemAssistantContentTextType = "text"`

          - `InitialItemAssistantContentOutputText`

            - `Text string`

              The message text to include in the Live session’s initial conversation history.

            - `Type OutputText`

              The text content type. Always `output_text`.

              - `const OutputTextOutputText OutputText = "output_text"`

        - `Role Assistant`

          The author of this history message. Always `assistant`.

          - `const AssistantAssistant Assistant = "assistant"`

        - `ID string`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Status string`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `const InitialItemAssistantStatusIncomplete InitialItemAssistantStatus = "incomplete"`

          - `const InitialItemAssistantStatusCompleted InitialItemAssistantStatus = "completed"`

        - `Type string`

          The history item type. Always `message`.

          - `const InitialItemAssistantTypeMessage InitialItemAssistantType = "message"`

    - `Instructions string`

      Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

    - `Store bool`

      Whether to store the session for later forking and recording download. Defaults to false for new sessions.

  - `Type SessionClosed`

    The event type, always `session.closed`.

    - `const SessionClosedSessionClosed SessionClosed = "session.closed"`

  - `Usage SessionUsage`

    The final cumulative Live audio usage after session finalization.

    - `Seconds float64`

      The cumulative Live audio duration in seconds. Do not sum this value across usage events.

  - `ClientEventID string`

    The event_id of the client command associated with this server event, when supplied.

### Session Config

- `type SessionConfig struct{…}`

  Initial configuration for a Live session, including its model, conversation instructions, audio, and delegated task handling.

  - `Model SessionConfigModel`

    The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

    - `string`

    - `SessionConfigModel`

      - `const SessionConfigModelGPTLive1 SessionConfigModel = "gpt-live-1"`

  - `Audio SessionConfigAudio`

    Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

    - `Format AudioFormatUnion`

      Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

      - `AudioFormatAudioPCM`

        - `Rate int64`

          Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

          - `const AudioFormatAudioPCMRate16000 AudioFormatAudioPCMRate = 16000`

          - `const AudioFormatAudioPCMRate24000 AudioFormatAudioPCMRate = 24000`

        - `Type AudioPCM`

          The audio encoding. Always `audio/pcm`.

          - `const AudioPCMAudioPCM AudioPCM = "audio/pcm"`

      - `AudioFormatAudioPCMU`

        - `Rate int64`

          Audio sample rate in hertz. G.711 audio uses 8000 Hz.

        - `Type AudioPCMU`

          The audio encoding. Always `audio/pcmu`.

          - `const AudioPCMUAudioPCMU AudioPCMU = "audio/pcmu"`

      - `AudioFormatAudioPCMA`

        - `Rate int64`

          Audio sample rate in hertz. G.711 audio uses 8000 Hz.

        - `Type AudioPCMA`

          The audio encoding. Always `audio/pcma`.

          - `const AudioPCMAAudioPCMA AudioPCMA = "audio/pcma"`

    - `Output SessionConfigAudioOutput`

      The voice used for speech generated by the Live model.

      - `Voice SessionConfigAudioOutputVoiceUnion`

        The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

        - `string`

        - `type BuiltInVoice string`

          A built-in voice available for Live speech.

          - `const BuiltInVoiceAlloy BuiltInVoice = "alloy"`

          - `const BuiltInVoiceAsh BuiltInVoice = "ash"`

          - `const BuiltInVoiceBallad BuiltInVoice = "ballad"`

          - `const BuiltInVoiceBeacon BuiltInVoice = "beacon"`

          - `const BuiltInVoiceBossa BuiltInVoice = "bossa"`

          - `const BuiltInVoiceCedar BuiltInVoice = "cedar"`

          - `const BuiltInVoiceCinder BuiltInVoice = "cinder"`

          - `const BuiltInVoiceCoral BuiltInVoice = "coral"`

          - `const BuiltInVoiceDelta BuiltInVoice = "delta"`

          - `const BuiltInVoiceEcho BuiltInVoice = "echo"`

          - `const BuiltInVoiceGleam BuiltInVoice = "gleam"`

          - `const BuiltInVoiceMarin BuiltInVoice = "marin"`

          - `const BuiltInVoiceMeridian BuiltInVoice = "meridian"`

          - `const BuiltInVoiceQuartz BuiltInVoice = "quartz"`

          - `const BuiltInVoiceRipple BuiltInVoice = "ripple"`

          - `const BuiltInVoiceSage BuiltInVoice = "sage"`

          - `const BuiltInVoiceShimmer BuiltInVoice = "shimmer"`

          - `const BuiltInVoiceStone BuiltInVoice = "stone"`

          - `const BuiltInVoiceTempo BuiltInVoice = "tempo"`

          - `const BuiltInVoiceVerse BuiltInVoice = "verse"`

          - `const BuiltInVoiceVesper BuiltInVoice = "vesper"`

          - `const BuiltInVoiceWillow BuiltInVoice = "willow"`

        - `type CustomVoice struct{…}`

          - `ID string`

  - `Client ClientConfig`

    Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

    - `DataChannel DataChannelConfig`

      Client and server event permissions for the WebRTC frontend data channel.

      - `AllowedClientEvents DataChannelConfigAllowedClientEventsUnion`

        Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

        - `All`

          - `const AllAll All = "all"`

        - `[]string`

      - `AllowedServerEvents DataChannelConfigAllowedServerEventsUnion`

        Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

        - `All`

          - `const AllAll All = "all"`

        - `[]ServerEventSelector`

          - `Type string`

            The outer Live server event type. Use 'response.event' for Responses events.

          - `ResponseEvent string`

            The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

  - `Delegation SessionConfigDelegationUnion`

    Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

    - `type ClientDelegation struct{…}`

      Delegate tasks to your application. The Live session emits delegation events that your backend handles.

      - `Type Client`

        The delegation owner. Always `client` for tasks handled by your application.

        - `const ClientClient Client = "client"`

    - `SessionConfigDelegationResponses`

      - `Responses ResponsesDelegationConfig`

        Backend model, prompt, and tools used when the Live session delegates a task to Responses.

        - `Model string`

          The model used for server-owned Responses delegations.

        - `Instructions string`

          Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

        - `MaxOutputTokens int64`

          Maximum number of output tokens for each delegated response.

        - `ParallelToolCalls bool`

          Whether the delegated Responses model may request multiple tool calls in a single response.

        - `Reasoning ResponsesDelegationConfigReasoning`

          Reasoning settings passed to each delegated Responses request.

          - `Effort string`

            How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

            - `const ResponsesDelegationConfigReasoningEffortNone ResponsesDelegationConfigReasoningEffort = "none"`

            - `const ResponsesDelegationConfigReasoningEffortMinimal ResponsesDelegationConfigReasoningEffort = "minimal"`

            - `const ResponsesDelegationConfigReasoningEffortLow ResponsesDelegationConfigReasoningEffort = "low"`

            - `const ResponsesDelegationConfigReasoningEffortMedium ResponsesDelegationConfigReasoningEffort = "medium"`

            - `const ResponsesDelegationConfigReasoningEffortHigh ResponsesDelegationConfigReasoningEffort = "high"`

            - `const ResponsesDelegationConfigReasoningEffortXhigh ResponsesDelegationConfigReasoningEffort = "xhigh"`

          - `Summary string`

            The reasoning summary to request from the delegated Responses model, when supported.

            - `const ResponsesDelegationConfigReasoningSummaryConcise ResponsesDelegationConfigReasoningSummary = "concise"`

            - `const ResponsesDelegationConfigReasoningSummaryDetailed ResponsesDelegationConfigReasoningSummary = "detailed"`

            - `const ResponsesDelegationConfigReasoningSummaryAuto ResponsesDelegationConfigReasoningSummary = "auto"`

        - `ServiceTier ResponsesDelegationConfigServiceTier`

          Service tier for delegated Responses requests.

          - `const ResponsesDelegationConfigServiceTierAuto ResponsesDelegationConfigServiceTier = "auto"`

          - `const ResponsesDelegationConfigServiceTierDefault ResponsesDelegationConfigServiceTier = "default"`

          - `const ResponsesDelegationConfigServiceTierFastTierTempPilot ResponsesDelegationConfigServiceTier = "fast_tier_temp_pilot"`

          - `const ResponsesDelegationConfigServiceTierFlex ResponsesDelegationConfigServiceTier = "flex"`

          - `const ResponsesDelegationConfigServiceTierPriority ResponsesDelegationConfigServiceTier = "priority"`

          - `const ResponsesDelegationConfigServiceTierUltrafast ResponsesDelegationConfigServiceTier = "ultrafast"`

        - `Text ResponsesDelegationConfigText`

          Text generation settings passed to each delegated Responses request.

          - `Verbosity string`

            The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

            - `const ResponsesDelegationConfigTextVerbosityLow ResponsesDelegationConfigTextVerbosity = "low"`

            - `const ResponsesDelegationConfigTextVerbosityMedium ResponsesDelegationConfigTextVerbosity = "medium"`

            - `const ResponsesDelegationConfigTextVerbosityHigh ResponsesDelegationConfigTextVerbosity = "high"`

        - `ToolChoice ResponsesDelegationConfigToolChoiceUnion`

          Controls which tool the Responses backend uses when handling a task delegated by the Live model.

          - `string`

            - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "auto"`

            - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "none"`

            - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "required"`

          - `ResponsesDelegationConfigToolChoiceLiveFunctionToolChoiceParam`

            - `Name string`

            - `Type Function`

              - `const FunctionFunction Function = "function"`

          - `ResponsesDelegationConfigToolChoiceLiveMcpToolChoiceParam`

            - `Name string`

            - `ServerLabel string`

            - `Type Mcp`

              - `const McpMcp Mcp = "mcp"`

        - `Tools []ResponsesDelegationConfigToolUnion`

          Tools available to the Responses backend while it handles tasks delegated by the Live model.

          - `type FunctionTool struct{…}`

            A function tool available to the Responses backend when the Live model delegates a task.

            - `Name string`

              The name the delegated Responses model uses when calling this function.

            - `Type Function`

              The tool type. Always `function`.

              - `const FunctionFunction Function = "function"`

            - `Description string`

              What the function does and when the delegated Responses model should call it.

            - `Parameters map[string, any]`

              A JSON Schema object describing the arguments accepted by the function.

            - `Strict bool`

              Whether the delegated Responses model must follow the function’s parameter schema exactly.

          - `ResponsesDelegationConfigToolWebSearch`

            - `Type WebSearch`

              The tool type. Always `web_search`.

              - `const WebSearchWebSearch WebSearch = "web_search"`

      - `Type Responses`

        The delegation owner. Always `responses` for tasks handled by the Responses API.

        - `const ResponsesResponses Responses = "responses"`

  - `Input []InitialItemUnion`

    Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

    - `InitialItemDeveloper`

      - `Content []InitialItemDeveloperContent`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `Text string`

          The message text to include in the Live session’s initial conversation history.

        - `Type string`

          The text content type. Always `input_text`.

          - `const InitialItemDeveloperContentTypeInputText InitialItemDeveloperContentType = "input_text"`

      - `Role Developer`

        The author of this history message. Always `developer`.

        - `const DeveloperDeveloper Developer = "developer"`

      - `ID string`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Status string`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `const InitialItemDeveloperStatusIncomplete InitialItemDeveloperStatus = "incomplete"`

        - `const InitialItemDeveloperStatusCompleted InitialItemDeveloperStatus = "completed"`

      - `Type string`

        The history item type. Always `message`.

        - `const InitialItemDeveloperTypeMessage InitialItemDeveloperType = "message"`

    - `InitialItemUser`

      - `Content []InitialItemUserContent`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `Text string`

          The message text to include in the Live session’s initial conversation history.

        - `Type string`

          The text content type. Always `input_text`.

          - `const InitialItemUserContentTypeInputText InitialItemUserContentType = "input_text"`

      - `Role User`

        The author of this history message. Always `user`.

        - `const UserUser User = "user"`

      - `ID string`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Status string`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `const InitialItemUserStatusIncomplete InitialItemUserStatus = "incomplete"`

        - `const InitialItemUserStatusCompleted InitialItemUserStatus = "completed"`

      - `Type string`

        The history item type. Always `message`.

        - `const InitialItemUserTypeMessage InitialItemUserType = "message"`

    - `InitialItemAssistant`

      - `Content []InitialItemAssistantContentUnion`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `InitialItemAssistantContentText`

          - `Text string`

            The message text to include in the Live session’s initial conversation history.

          - `Type string`

            The text content type. Always `text`.

            - `const InitialItemAssistantContentTextTypeText InitialItemAssistantContentTextType = "text"`

        - `InitialItemAssistantContentOutputText`

          - `Text string`

            The message text to include in the Live session’s initial conversation history.

          - `Type OutputText`

            The text content type. Always `output_text`.

            - `const OutputTextOutputText OutputText = "output_text"`

      - `Role Assistant`

        The author of this history message. Always `assistant`.

        - `const AssistantAssistant Assistant = "assistant"`

      - `ID string`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Status string`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `const InitialItemAssistantStatusIncomplete InitialItemAssistantStatus = "incomplete"`

        - `const InitialItemAssistantStatusCompleted InitialItemAssistantStatus = "completed"`

      - `Type string`

        The history item type. Always `message`.

        - `const InitialItemAssistantTypeMessage InitialItemAssistantType = "message"`

  - `Instructions string`

    Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

  - `Store bool`

    Whether to store the session for later forking and recording download. Defaults to false for new sessions.

### Session Resource

- `type SessionResource struct{…}`

  The resolved Live session configuration and server-assigned session metadata.

  - `ID string`

    The unique ID of the Live session. Use this ID for sideband connections, forking, and recording download.

  - `ExpiresAt int64`

    The Unix timestamp, in seconds, at which the Live session expires.

  - `Model SessionResourceModel`

    The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

    - `string`

    - `SessionResourceModel`

      - `const SessionResourceModelGPTLive1 SessionResourceModel = "gpt-live-1"`

  - `Status Active`

    The status of the session snapshot. Always `active`, including the final snapshot in session.closed; use the event type to determine that the session has closed.

    - `const ActiveActive Active = "active"`

  - `Audio SessionResourceAudio`

    Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

    - `Format AudioFormatUnion`

      Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

      - `AudioFormatAudioPCM`

        - `Rate int64`

          Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

          - `const AudioFormatAudioPCMRate16000 AudioFormatAudioPCMRate = 16000`

          - `const AudioFormatAudioPCMRate24000 AudioFormatAudioPCMRate = 24000`

        - `Type AudioPCM`

          The audio encoding. Always `audio/pcm`.

          - `const AudioPCMAudioPCM AudioPCM = "audio/pcm"`

      - `AudioFormatAudioPCMU`

        - `Rate int64`

          Audio sample rate in hertz. G.711 audio uses 8000 Hz.

        - `Type AudioPCMU`

          The audio encoding. Always `audio/pcmu`.

          - `const AudioPCMUAudioPCMU AudioPCMU = "audio/pcmu"`

      - `AudioFormatAudioPCMA`

        - `Rate int64`

          Audio sample rate in hertz. G.711 audio uses 8000 Hz.

        - `Type AudioPCMA`

          The audio encoding. Always `audio/pcma`.

          - `const AudioPCMAAudioPCMA AudioPCMA = "audio/pcma"`

    - `Output SessionResourceAudioOutput`

      The voice used for speech generated by the Live model.

      - `Voice SessionResourceAudioOutputVoiceUnion`

        The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

        - `string`

        - `type BuiltInVoice string`

          A built-in voice available for Live speech.

          - `const BuiltInVoiceAlloy BuiltInVoice = "alloy"`

          - `const BuiltInVoiceAsh BuiltInVoice = "ash"`

          - `const BuiltInVoiceBallad BuiltInVoice = "ballad"`

          - `const BuiltInVoiceBeacon BuiltInVoice = "beacon"`

          - `const BuiltInVoiceBossa BuiltInVoice = "bossa"`

          - `const BuiltInVoiceCedar BuiltInVoice = "cedar"`

          - `const BuiltInVoiceCinder BuiltInVoice = "cinder"`

          - `const BuiltInVoiceCoral BuiltInVoice = "coral"`

          - `const BuiltInVoiceDelta BuiltInVoice = "delta"`

          - `const BuiltInVoiceEcho BuiltInVoice = "echo"`

          - `const BuiltInVoiceGleam BuiltInVoice = "gleam"`

          - `const BuiltInVoiceMarin BuiltInVoice = "marin"`

          - `const BuiltInVoiceMeridian BuiltInVoice = "meridian"`

          - `const BuiltInVoiceQuartz BuiltInVoice = "quartz"`

          - `const BuiltInVoiceRipple BuiltInVoice = "ripple"`

          - `const BuiltInVoiceSage BuiltInVoice = "sage"`

          - `const BuiltInVoiceShimmer BuiltInVoice = "shimmer"`

          - `const BuiltInVoiceStone BuiltInVoice = "stone"`

          - `const BuiltInVoiceTempo BuiltInVoice = "tempo"`

          - `const BuiltInVoiceVerse BuiltInVoice = "verse"`

          - `const BuiltInVoiceVesper BuiltInVoice = "vesper"`

          - `const BuiltInVoiceWillow BuiltInVoice = "willow"`

        - `type CustomVoice struct{…}`

          - `ID string`

  - `Client ClientConfig`

    Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

    - `DataChannel DataChannelConfig`

      Client and server event permissions for the WebRTC frontend data channel.

      - `AllowedClientEvents DataChannelConfigAllowedClientEventsUnion`

        Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

        - `All`

          - `const AllAll All = "all"`

        - `[]string`

      - `AllowedServerEvents DataChannelConfigAllowedServerEventsUnion`

        Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

        - `All`

          - `const AllAll All = "all"`

        - `[]ServerEventSelector`

          - `Type string`

            The outer Live server event type. Use 'response.event' for Responses events.

          - `ResponseEvent string`

            The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

  - `Delegation SessionResourceDelegationUnion`

    Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

    - `type ClientDelegation struct{…}`

      Delegate tasks to your application. The Live session emits delegation events that your backend handles.

      - `Type Client`

        The delegation owner. Always `client` for tasks handled by your application.

        - `const ClientClient Client = "client"`

    - `SessionResourceDelegationResponses`

      - `Responses ResponsesDelegationConfig`

        Backend model, prompt, and tools used when the Live session delegates a task to Responses.

        - `Model string`

          The model used for server-owned Responses delegations.

        - `Instructions string`

          Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

        - `MaxOutputTokens int64`

          Maximum number of output tokens for each delegated response.

        - `ParallelToolCalls bool`

          Whether the delegated Responses model may request multiple tool calls in a single response.

        - `Reasoning ResponsesDelegationConfigReasoning`

          Reasoning settings passed to each delegated Responses request.

          - `Effort string`

            How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

            - `const ResponsesDelegationConfigReasoningEffortNone ResponsesDelegationConfigReasoningEffort = "none"`

            - `const ResponsesDelegationConfigReasoningEffortMinimal ResponsesDelegationConfigReasoningEffort = "minimal"`

            - `const ResponsesDelegationConfigReasoningEffortLow ResponsesDelegationConfigReasoningEffort = "low"`

            - `const ResponsesDelegationConfigReasoningEffortMedium ResponsesDelegationConfigReasoningEffort = "medium"`

            - `const ResponsesDelegationConfigReasoningEffortHigh ResponsesDelegationConfigReasoningEffort = "high"`

            - `const ResponsesDelegationConfigReasoningEffortXhigh ResponsesDelegationConfigReasoningEffort = "xhigh"`

          - `Summary string`

            The reasoning summary to request from the delegated Responses model, when supported.

            - `const ResponsesDelegationConfigReasoningSummaryConcise ResponsesDelegationConfigReasoningSummary = "concise"`

            - `const ResponsesDelegationConfigReasoningSummaryDetailed ResponsesDelegationConfigReasoningSummary = "detailed"`

            - `const ResponsesDelegationConfigReasoningSummaryAuto ResponsesDelegationConfigReasoningSummary = "auto"`

        - `ServiceTier ResponsesDelegationConfigServiceTier`

          Service tier for delegated Responses requests.

          - `const ResponsesDelegationConfigServiceTierAuto ResponsesDelegationConfigServiceTier = "auto"`

          - `const ResponsesDelegationConfigServiceTierDefault ResponsesDelegationConfigServiceTier = "default"`

          - `const ResponsesDelegationConfigServiceTierFastTierTempPilot ResponsesDelegationConfigServiceTier = "fast_tier_temp_pilot"`

          - `const ResponsesDelegationConfigServiceTierFlex ResponsesDelegationConfigServiceTier = "flex"`

          - `const ResponsesDelegationConfigServiceTierPriority ResponsesDelegationConfigServiceTier = "priority"`

          - `const ResponsesDelegationConfigServiceTierUltrafast ResponsesDelegationConfigServiceTier = "ultrafast"`

        - `Text ResponsesDelegationConfigText`

          Text generation settings passed to each delegated Responses request.

          - `Verbosity string`

            The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

            - `const ResponsesDelegationConfigTextVerbosityLow ResponsesDelegationConfigTextVerbosity = "low"`

            - `const ResponsesDelegationConfigTextVerbosityMedium ResponsesDelegationConfigTextVerbosity = "medium"`

            - `const ResponsesDelegationConfigTextVerbosityHigh ResponsesDelegationConfigTextVerbosity = "high"`

        - `ToolChoice ResponsesDelegationConfigToolChoiceUnion`

          Controls which tool the Responses backend uses when handling a task delegated by the Live model.

          - `string`

            - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "auto"`

            - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "none"`

            - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "required"`

          - `ResponsesDelegationConfigToolChoiceLiveFunctionToolChoiceParam`

            - `Name string`

            - `Type Function`

              - `const FunctionFunction Function = "function"`

          - `ResponsesDelegationConfigToolChoiceLiveMcpToolChoiceParam`

            - `Name string`

            - `ServerLabel string`

            - `Type Mcp`

              - `const McpMcp Mcp = "mcp"`

        - `Tools []ResponsesDelegationConfigToolUnion`

          Tools available to the Responses backend while it handles tasks delegated by the Live model.

          - `type FunctionTool struct{…}`

            A function tool available to the Responses backend when the Live model delegates a task.

            - `Name string`

              The name the delegated Responses model uses when calling this function.

            - `Type Function`

              The tool type. Always `function`.

              - `const FunctionFunction Function = "function"`

            - `Description string`

              What the function does and when the delegated Responses model should call it.

            - `Parameters map[string, any]`

              A JSON Schema object describing the arguments accepted by the function.

            - `Strict bool`

              Whether the delegated Responses model must follow the function’s parameter schema exactly.

          - `ResponsesDelegationConfigToolWebSearch`

            - `Type WebSearch`

              The tool type. Always `web_search`.

              - `const WebSearchWebSearch WebSearch = "web_search"`

      - `Type Responses`

        The delegation owner. Always `responses` for tasks handled by the Responses API.

        - `const ResponsesResponses Responses = "responses"`

  - `Input []InitialItemUnion`

    Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

    - `InitialItemDeveloper`

      - `Content []InitialItemDeveloperContent`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `Text string`

          The message text to include in the Live session’s initial conversation history.

        - `Type string`

          The text content type. Always `input_text`.

          - `const InitialItemDeveloperContentTypeInputText InitialItemDeveloperContentType = "input_text"`

      - `Role Developer`

        The author of this history message. Always `developer`.

        - `const DeveloperDeveloper Developer = "developer"`

      - `ID string`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Status string`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `const InitialItemDeveloperStatusIncomplete InitialItemDeveloperStatus = "incomplete"`

        - `const InitialItemDeveloperStatusCompleted InitialItemDeveloperStatus = "completed"`

      - `Type string`

        The history item type. Always `message`.

        - `const InitialItemDeveloperTypeMessage InitialItemDeveloperType = "message"`

    - `InitialItemUser`

      - `Content []InitialItemUserContent`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `Text string`

          The message text to include in the Live session’s initial conversation history.

        - `Type string`

          The text content type. Always `input_text`.

          - `const InitialItemUserContentTypeInputText InitialItemUserContentType = "input_text"`

      - `Role User`

        The author of this history message. Always `user`.

        - `const UserUser User = "user"`

      - `ID string`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Status string`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `const InitialItemUserStatusIncomplete InitialItemUserStatus = "incomplete"`

        - `const InitialItemUserStatusCompleted InitialItemUserStatus = "completed"`

      - `Type string`

        The history item type. Always `message`.

        - `const InitialItemUserTypeMessage InitialItemUserType = "message"`

    - `InitialItemAssistant`

      - `Content []InitialItemAssistantContentUnion`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `InitialItemAssistantContentText`

          - `Text string`

            The message text to include in the Live session’s initial conversation history.

          - `Type string`

            The text content type. Always `text`.

            - `const InitialItemAssistantContentTextTypeText InitialItemAssistantContentTextType = "text"`

        - `InitialItemAssistantContentOutputText`

          - `Text string`

            The message text to include in the Live session’s initial conversation history.

          - `Type OutputText`

            The text content type. Always `output_text`.

            - `const OutputTextOutputText OutputText = "output_text"`

      - `Role Assistant`

        The author of this history message. Always `assistant`.

        - `const AssistantAssistant Assistant = "assistant"`

      - `ID string`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Status string`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `const InitialItemAssistantStatusIncomplete InitialItemAssistantStatus = "incomplete"`

        - `const InitialItemAssistantStatusCompleted InitialItemAssistantStatus = "completed"`

      - `Type string`

        The history item type. Always `message`.

        - `const InitialItemAssistantTypeMessage InitialItemAssistantType = "message"`

  - `Instructions string`

    Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

  - `Store bool`

    Whether to store the session for later forking and recording download. Defaults to false for new sessions.

### Session Start Event

- `type SessionStartEvent struct{…}`

  Start a Live session on a primary WebSocket. Send this event before other commands and wait for `session.started`.

  - `Session SessionConfig`

    Initial configuration for a primary WebSocket. Send session.start first and wait for session.started before application commands. WebRTC creation already starts the session; do not send this event again on its data channel.

    - `Model SessionConfigModel`

      The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

      - `string`

      - `SessionConfigModel`

        - `const SessionConfigModelGPTLive1 SessionConfigModel = "gpt-live-1"`

    - `Audio SessionConfigAudio`

      Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

      - `Format AudioFormatUnion`

        Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

        - `AudioFormatAudioPCM`

          - `Rate int64`

            Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

            - `const AudioFormatAudioPCMRate16000 AudioFormatAudioPCMRate = 16000`

            - `const AudioFormatAudioPCMRate24000 AudioFormatAudioPCMRate = 24000`

          - `Type AudioPCM`

            The audio encoding. Always `audio/pcm`.

            - `const AudioPCMAudioPCM AudioPCM = "audio/pcm"`

        - `AudioFormatAudioPCMU`

          - `Rate int64`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `Type AudioPCMU`

            The audio encoding. Always `audio/pcmu`.

            - `const AudioPCMUAudioPCMU AudioPCMU = "audio/pcmu"`

        - `AudioFormatAudioPCMA`

          - `Rate int64`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `Type AudioPCMA`

            The audio encoding. Always `audio/pcma`.

            - `const AudioPCMAAudioPCMA AudioPCMA = "audio/pcma"`

      - `Output SessionConfigAudioOutput`

        The voice used for speech generated by the Live model.

        - `Voice SessionConfigAudioOutputVoiceUnion`

          The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

          - `string`

          - `type BuiltInVoice string`

            A built-in voice available for Live speech.

            - `const BuiltInVoiceAlloy BuiltInVoice = "alloy"`

            - `const BuiltInVoiceAsh BuiltInVoice = "ash"`

            - `const BuiltInVoiceBallad BuiltInVoice = "ballad"`

            - `const BuiltInVoiceBeacon BuiltInVoice = "beacon"`

            - `const BuiltInVoiceBossa BuiltInVoice = "bossa"`

            - `const BuiltInVoiceCedar BuiltInVoice = "cedar"`

            - `const BuiltInVoiceCinder BuiltInVoice = "cinder"`

            - `const BuiltInVoiceCoral BuiltInVoice = "coral"`

            - `const BuiltInVoiceDelta BuiltInVoice = "delta"`

            - `const BuiltInVoiceEcho BuiltInVoice = "echo"`

            - `const BuiltInVoiceGleam BuiltInVoice = "gleam"`

            - `const BuiltInVoiceMarin BuiltInVoice = "marin"`

            - `const BuiltInVoiceMeridian BuiltInVoice = "meridian"`

            - `const BuiltInVoiceQuartz BuiltInVoice = "quartz"`

            - `const BuiltInVoiceRipple BuiltInVoice = "ripple"`

            - `const BuiltInVoiceSage BuiltInVoice = "sage"`

            - `const BuiltInVoiceShimmer BuiltInVoice = "shimmer"`

            - `const BuiltInVoiceStone BuiltInVoice = "stone"`

            - `const BuiltInVoiceTempo BuiltInVoice = "tempo"`

            - `const BuiltInVoiceVerse BuiltInVoice = "verse"`

            - `const BuiltInVoiceVesper BuiltInVoice = "vesper"`

            - `const BuiltInVoiceWillow BuiltInVoice = "willow"`

          - `type CustomVoice struct{…}`

            - `ID string`

    - `Client ClientConfig`

      Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

      - `DataChannel DataChannelConfig`

        Client and server event permissions for the WebRTC frontend data channel.

        - `AllowedClientEvents DataChannelConfigAllowedClientEventsUnion`

          Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

          - `All`

            - `const AllAll All = "all"`

          - `[]string`

        - `AllowedServerEvents DataChannelConfigAllowedServerEventsUnion`

          Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

          - `All`

            - `const AllAll All = "all"`

          - `[]ServerEventSelector`

            - `Type string`

              The outer Live server event type. Use 'response.event' for Responses events.

            - `ResponseEvent string`

              The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

    - `Delegation SessionConfigDelegationUnion`

      Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

      - `type ClientDelegation struct{…}`

        Delegate tasks to your application. The Live session emits delegation events that your backend handles.

        - `Type Client`

          The delegation owner. Always `client` for tasks handled by your application.

          - `const ClientClient Client = "client"`

      - `SessionConfigDelegationResponses`

        - `Responses ResponsesDelegationConfig`

          Backend model, prompt, and tools used when the Live session delegates a task to Responses.

          - `Model string`

            The model used for server-owned Responses delegations.

          - `Instructions string`

            Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

          - `MaxOutputTokens int64`

            Maximum number of output tokens for each delegated response.

          - `ParallelToolCalls bool`

            Whether the delegated Responses model may request multiple tool calls in a single response.

          - `Reasoning ResponsesDelegationConfigReasoning`

            Reasoning settings passed to each delegated Responses request.

            - `Effort string`

              How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

              - `const ResponsesDelegationConfigReasoningEffortNone ResponsesDelegationConfigReasoningEffort = "none"`

              - `const ResponsesDelegationConfigReasoningEffortMinimal ResponsesDelegationConfigReasoningEffort = "minimal"`

              - `const ResponsesDelegationConfigReasoningEffortLow ResponsesDelegationConfigReasoningEffort = "low"`

              - `const ResponsesDelegationConfigReasoningEffortMedium ResponsesDelegationConfigReasoningEffort = "medium"`

              - `const ResponsesDelegationConfigReasoningEffortHigh ResponsesDelegationConfigReasoningEffort = "high"`

              - `const ResponsesDelegationConfigReasoningEffortXhigh ResponsesDelegationConfigReasoningEffort = "xhigh"`

            - `Summary string`

              The reasoning summary to request from the delegated Responses model, when supported.

              - `const ResponsesDelegationConfigReasoningSummaryConcise ResponsesDelegationConfigReasoningSummary = "concise"`

              - `const ResponsesDelegationConfigReasoningSummaryDetailed ResponsesDelegationConfigReasoningSummary = "detailed"`

              - `const ResponsesDelegationConfigReasoningSummaryAuto ResponsesDelegationConfigReasoningSummary = "auto"`

          - `ServiceTier ResponsesDelegationConfigServiceTier`

            Service tier for delegated Responses requests.

            - `const ResponsesDelegationConfigServiceTierAuto ResponsesDelegationConfigServiceTier = "auto"`

            - `const ResponsesDelegationConfigServiceTierDefault ResponsesDelegationConfigServiceTier = "default"`

            - `const ResponsesDelegationConfigServiceTierFastTierTempPilot ResponsesDelegationConfigServiceTier = "fast_tier_temp_pilot"`

            - `const ResponsesDelegationConfigServiceTierFlex ResponsesDelegationConfigServiceTier = "flex"`

            - `const ResponsesDelegationConfigServiceTierPriority ResponsesDelegationConfigServiceTier = "priority"`

            - `const ResponsesDelegationConfigServiceTierUltrafast ResponsesDelegationConfigServiceTier = "ultrafast"`

          - `Text ResponsesDelegationConfigText`

            Text generation settings passed to each delegated Responses request.

            - `Verbosity string`

              The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

              - `const ResponsesDelegationConfigTextVerbosityLow ResponsesDelegationConfigTextVerbosity = "low"`

              - `const ResponsesDelegationConfigTextVerbosityMedium ResponsesDelegationConfigTextVerbosity = "medium"`

              - `const ResponsesDelegationConfigTextVerbosityHigh ResponsesDelegationConfigTextVerbosity = "high"`

          - `ToolChoice ResponsesDelegationConfigToolChoiceUnion`

            Controls which tool the Responses backend uses when handling a task delegated by the Live model.

            - `string`

              - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "auto"`

              - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "none"`

              - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "required"`

            - `ResponsesDelegationConfigToolChoiceLiveFunctionToolChoiceParam`

              - `Name string`

              - `Type Function`

                - `const FunctionFunction Function = "function"`

            - `ResponsesDelegationConfigToolChoiceLiveMcpToolChoiceParam`

              - `Name string`

              - `ServerLabel string`

              - `Type Mcp`

                - `const McpMcp Mcp = "mcp"`

          - `Tools []ResponsesDelegationConfigToolUnion`

            Tools available to the Responses backend while it handles tasks delegated by the Live model.

            - `type FunctionTool struct{…}`

              A function tool available to the Responses backend when the Live model delegates a task.

              - `Name string`

                The name the delegated Responses model uses when calling this function.

              - `Type Function`

                The tool type. Always `function`.

                - `const FunctionFunction Function = "function"`

              - `Description string`

                What the function does and when the delegated Responses model should call it.

              - `Parameters map[string, any]`

                A JSON Schema object describing the arguments accepted by the function.

              - `Strict bool`

                Whether the delegated Responses model must follow the function’s parameter schema exactly.

            - `ResponsesDelegationConfigToolWebSearch`

              - `Type WebSearch`

                The tool type. Always `web_search`.

                - `const WebSearchWebSearch WebSearch = "web_search"`

        - `Type Responses`

          The delegation owner. Always `responses` for tasks handled by the Responses API.

          - `const ResponsesResponses Responses = "responses"`

    - `Input []InitialItemUnion`

      Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

      - `InitialItemDeveloper`

        - `Content []InitialItemDeveloperContent`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `Text string`

            The message text to include in the Live session’s initial conversation history.

          - `Type string`

            The text content type. Always `input_text`.

            - `const InitialItemDeveloperContentTypeInputText InitialItemDeveloperContentType = "input_text"`

        - `Role Developer`

          The author of this history message. Always `developer`.

          - `const DeveloperDeveloper Developer = "developer"`

        - `ID string`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Status string`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `const InitialItemDeveloperStatusIncomplete InitialItemDeveloperStatus = "incomplete"`

          - `const InitialItemDeveloperStatusCompleted InitialItemDeveloperStatus = "completed"`

        - `Type string`

          The history item type. Always `message`.

          - `const InitialItemDeveloperTypeMessage InitialItemDeveloperType = "message"`

      - `InitialItemUser`

        - `Content []InitialItemUserContent`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `Text string`

            The message text to include in the Live session’s initial conversation history.

          - `Type string`

            The text content type. Always `input_text`.

            - `const InitialItemUserContentTypeInputText InitialItemUserContentType = "input_text"`

        - `Role User`

          The author of this history message. Always `user`.

          - `const UserUser User = "user"`

        - `ID string`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Status string`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `const InitialItemUserStatusIncomplete InitialItemUserStatus = "incomplete"`

          - `const InitialItemUserStatusCompleted InitialItemUserStatus = "completed"`

        - `Type string`

          The history item type. Always `message`.

          - `const InitialItemUserTypeMessage InitialItemUserType = "message"`

      - `InitialItemAssistant`

        - `Content []InitialItemAssistantContentUnion`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `InitialItemAssistantContentText`

            - `Text string`

              The message text to include in the Live session’s initial conversation history.

            - `Type string`

              The text content type. Always `text`.

              - `const InitialItemAssistantContentTextTypeText InitialItemAssistantContentTextType = "text"`

          - `InitialItemAssistantContentOutputText`

            - `Text string`

              The message text to include in the Live session’s initial conversation history.

            - `Type OutputText`

              The text content type. Always `output_text`.

              - `const OutputTextOutputText OutputText = "output_text"`

        - `Role Assistant`

          The author of this history message. Always `assistant`.

          - `const AssistantAssistant Assistant = "assistant"`

        - `ID string`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Status string`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `const InitialItemAssistantStatusIncomplete InitialItemAssistantStatus = "incomplete"`

          - `const InitialItemAssistantStatusCompleted InitialItemAssistantStatus = "completed"`

        - `Type string`

          The history item type. Always `message`.

          - `const InitialItemAssistantTypeMessage InitialItemAssistantType = "message"`

    - `Instructions string`

      Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

    - `Store bool`

      Whether to store the session for later forking and recording download. Defaults to false for new sessions.

  - `Type SessionStart`

    The Live client event type. Always `session.start`.

    - `const SessionStartSessionStart SessionStart = "session.start"`

  - `EventID string`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Session Started Event

- `type SessionStartedEvent struct{…}`

  Returned when a Live session has started. Contains the resolved session configuration, including server defaults.

  - `EventID string`

    The unique ID of the Live server event.

  - `Session SessionResource`

    The resolved Live session configuration and server-assigned session metadata.

    - `ID string`

      The unique ID of the Live session. Use this ID for sideband connections, forking, and recording download.

    - `ExpiresAt int64`

      The Unix timestamp, in seconds, at which the Live session expires.

    - `Model SessionResourceModel`

      The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

      - `string`

      - `SessionResourceModel`

        - `const SessionResourceModelGPTLive1 SessionResourceModel = "gpt-live-1"`

    - `Status Active`

      The status of the session snapshot. Always `active`, including the final snapshot in session.closed; use the event type to determine that the session has closed.

      - `const ActiveActive Active = "active"`

    - `Audio SessionResourceAudio`

      Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

      - `Format AudioFormatUnion`

        Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

        - `AudioFormatAudioPCM`

          - `Rate int64`

            Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

            - `const AudioFormatAudioPCMRate16000 AudioFormatAudioPCMRate = 16000`

            - `const AudioFormatAudioPCMRate24000 AudioFormatAudioPCMRate = 24000`

          - `Type AudioPCM`

            The audio encoding. Always `audio/pcm`.

            - `const AudioPCMAudioPCM AudioPCM = "audio/pcm"`

        - `AudioFormatAudioPCMU`

          - `Rate int64`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `Type AudioPCMU`

            The audio encoding. Always `audio/pcmu`.

            - `const AudioPCMUAudioPCMU AudioPCMU = "audio/pcmu"`

        - `AudioFormatAudioPCMA`

          - `Rate int64`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `Type AudioPCMA`

            The audio encoding. Always `audio/pcma`.

            - `const AudioPCMAAudioPCMA AudioPCMA = "audio/pcma"`

      - `Output SessionResourceAudioOutput`

        The voice used for speech generated by the Live model.

        - `Voice SessionResourceAudioOutputVoiceUnion`

          The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

          - `string`

          - `type BuiltInVoice string`

            A built-in voice available for Live speech.

            - `const BuiltInVoiceAlloy BuiltInVoice = "alloy"`

            - `const BuiltInVoiceAsh BuiltInVoice = "ash"`

            - `const BuiltInVoiceBallad BuiltInVoice = "ballad"`

            - `const BuiltInVoiceBeacon BuiltInVoice = "beacon"`

            - `const BuiltInVoiceBossa BuiltInVoice = "bossa"`

            - `const BuiltInVoiceCedar BuiltInVoice = "cedar"`

            - `const BuiltInVoiceCinder BuiltInVoice = "cinder"`

            - `const BuiltInVoiceCoral BuiltInVoice = "coral"`

            - `const BuiltInVoiceDelta BuiltInVoice = "delta"`

            - `const BuiltInVoiceEcho BuiltInVoice = "echo"`

            - `const BuiltInVoiceGleam BuiltInVoice = "gleam"`

            - `const BuiltInVoiceMarin BuiltInVoice = "marin"`

            - `const BuiltInVoiceMeridian BuiltInVoice = "meridian"`

            - `const BuiltInVoiceQuartz BuiltInVoice = "quartz"`

            - `const BuiltInVoiceRipple BuiltInVoice = "ripple"`

            - `const BuiltInVoiceSage BuiltInVoice = "sage"`

            - `const BuiltInVoiceShimmer BuiltInVoice = "shimmer"`

            - `const BuiltInVoiceStone BuiltInVoice = "stone"`

            - `const BuiltInVoiceTempo BuiltInVoice = "tempo"`

            - `const BuiltInVoiceVerse BuiltInVoice = "verse"`

            - `const BuiltInVoiceVesper BuiltInVoice = "vesper"`

            - `const BuiltInVoiceWillow BuiltInVoice = "willow"`

          - `type CustomVoice struct{…}`

            - `ID string`

    - `Client ClientConfig`

      Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

      - `DataChannel DataChannelConfig`

        Client and server event permissions for the WebRTC frontend data channel.

        - `AllowedClientEvents DataChannelConfigAllowedClientEventsUnion`

          Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

          - `All`

            - `const AllAll All = "all"`

          - `[]string`

        - `AllowedServerEvents DataChannelConfigAllowedServerEventsUnion`

          Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

          - `All`

            - `const AllAll All = "all"`

          - `[]ServerEventSelector`

            - `Type string`

              The outer Live server event type. Use 'response.event' for Responses events.

            - `ResponseEvent string`

              The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

    - `Delegation SessionResourceDelegationUnion`

      Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

      - `type ClientDelegation struct{…}`

        Delegate tasks to your application. The Live session emits delegation events that your backend handles.

        - `Type Client`

          The delegation owner. Always `client` for tasks handled by your application.

          - `const ClientClient Client = "client"`

      - `SessionResourceDelegationResponses`

        - `Responses ResponsesDelegationConfig`

          Backend model, prompt, and tools used when the Live session delegates a task to Responses.

          - `Model string`

            The model used for server-owned Responses delegations.

          - `Instructions string`

            Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

          - `MaxOutputTokens int64`

            Maximum number of output tokens for each delegated response.

          - `ParallelToolCalls bool`

            Whether the delegated Responses model may request multiple tool calls in a single response.

          - `Reasoning ResponsesDelegationConfigReasoning`

            Reasoning settings passed to each delegated Responses request.

            - `Effort string`

              How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

              - `const ResponsesDelegationConfigReasoningEffortNone ResponsesDelegationConfigReasoningEffort = "none"`

              - `const ResponsesDelegationConfigReasoningEffortMinimal ResponsesDelegationConfigReasoningEffort = "minimal"`

              - `const ResponsesDelegationConfigReasoningEffortLow ResponsesDelegationConfigReasoningEffort = "low"`

              - `const ResponsesDelegationConfigReasoningEffortMedium ResponsesDelegationConfigReasoningEffort = "medium"`

              - `const ResponsesDelegationConfigReasoningEffortHigh ResponsesDelegationConfigReasoningEffort = "high"`

              - `const ResponsesDelegationConfigReasoningEffortXhigh ResponsesDelegationConfigReasoningEffort = "xhigh"`

            - `Summary string`

              The reasoning summary to request from the delegated Responses model, when supported.

              - `const ResponsesDelegationConfigReasoningSummaryConcise ResponsesDelegationConfigReasoningSummary = "concise"`

              - `const ResponsesDelegationConfigReasoningSummaryDetailed ResponsesDelegationConfigReasoningSummary = "detailed"`

              - `const ResponsesDelegationConfigReasoningSummaryAuto ResponsesDelegationConfigReasoningSummary = "auto"`

          - `ServiceTier ResponsesDelegationConfigServiceTier`

            Service tier for delegated Responses requests.

            - `const ResponsesDelegationConfigServiceTierAuto ResponsesDelegationConfigServiceTier = "auto"`

            - `const ResponsesDelegationConfigServiceTierDefault ResponsesDelegationConfigServiceTier = "default"`

            - `const ResponsesDelegationConfigServiceTierFastTierTempPilot ResponsesDelegationConfigServiceTier = "fast_tier_temp_pilot"`

            - `const ResponsesDelegationConfigServiceTierFlex ResponsesDelegationConfigServiceTier = "flex"`

            - `const ResponsesDelegationConfigServiceTierPriority ResponsesDelegationConfigServiceTier = "priority"`

            - `const ResponsesDelegationConfigServiceTierUltrafast ResponsesDelegationConfigServiceTier = "ultrafast"`

          - `Text ResponsesDelegationConfigText`

            Text generation settings passed to each delegated Responses request.

            - `Verbosity string`

              The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

              - `const ResponsesDelegationConfigTextVerbosityLow ResponsesDelegationConfigTextVerbosity = "low"`

              - `const ResponsesDelegationConfigTextVerbosityMedium ResponsesDelegationConfigTextVerbosity = "medium"`

              - `const ResponsesDelegationConfigTextVerbosityHigh ResponsesDelegationConfigTextVerbosity = "high"`

          - `ToolChoice ResponsesDelegationConfigToolChoiceUnion`

            Controls which tool the Responses backend uses when handling a task delegated by the Live model.

            - `string`

              - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "auto"`

              - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "none"`

              - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "required"`

            - `ResponsesDelegationConfigToolChoiceLiveFunctionToolChoiceParam`

              - `Name string`

              - `Type Function`

                - `const FunctionFunction Function = "function"`

            - `ResponsesDelegationConfigToolChoiceLiveMcpToolChoiceParam`

              - `Name string`

              - `ServerLabel string`

              - `Type Mcp`

                - `const McpMcp Mcp = "mcp"`

          - `Tools []ResponsesDelegationConfigToolUnion`

            Tools available to the Responses backend while it handles tasks delegated by the Live model.

            - `type FunctionTool struct{…}`

              A function tool available to the Responses backend when the Live model delegates a task.

              - `Name string`

                The name the delegated Responses model uses when calling this function.

              - `Type Function`

                The tool type. Always `function`.

                - `const FunctionFunction Function = "function"`

              - `Description string`

                What the function does and when the delegated Responses model should call it.

              - `Parameters map[string, any]`

                A JSON Schema object describing the arguments accepted by the function.

              - `Strict bool`

                Whether the delegated Responses model must follow the function’s parameter schema exactly.

            - `ResponsesDelegationConfigToolWebSearch`

              - `Type WebSearch`

                The tool type. Always `web_search`.

                - `const WebSearchWebSearch WebSearch = "web_search"`

        - `Type Responses`

          The delegation owner. Always `responses` for tasks handled by the Responses API.

          - `const ResponsesResponses Responses = "responses"`

    - `Input []InitialItemUnion`

      Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

      - `InitialItemDeveloper`

        - `Content []InitialItemDeveloperContent`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `Text string`

            The message text to include in the Live session’s initial conversation history.

          - `Type string`

            The text content type. Always `input_text`.

            - `const InitialItemDeveloperContentTypeInputText InitialItemDeveloperContentType = "input_text"`

        - `Role Developer`

          The author of this history message. Always `developer`.

          - `const DeveloperDeveloper Developer = "developer"`

        - `ID string`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Status string`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `const InitialItemDeveloperStatusIncomplete InitialItemDeveloperStatus = "incomplete"`

          - `const InitialItemDeveloperStatusCompleted InitialItemDeveloperStatus = "completed"`

        - `Type string`

          The history item type. Always `message`.

          - `const InitialItemDeveloperTypeMessage InitialItemDeveloperType = "message"`

      - `InitialItemUser`

        - `Content []InitialItemUserContent`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `Text string`

            The message text to include in the Live session’s initial conversation history.

          - `Type string`

            The text content type. Always `input_text`.

            - `const InitialItemUserContentTypeInputText InitialItemUserContentType = "input_text"`

        - `Role User`

          The author of this history message. Always `user`.

          - `const UserUser User = "user"`

        - `ID string`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Status string`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `const InitialItemUserStatusIncomplete InitialItemUserStatus = "incomplete"`

          - `const InitialItemUserStatusCompleted InitialItemUserStatus = "completed"`

        - `Type string`

          The history item type. Always `message`.

          - `const InitialItemUserTypeMessage InitialItemUserType = "message"`

      - `InitialItemAssistant`

        - `Content []InitialItemAssistantContentUnion`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `InitialItemAssistantContentText`

            - `Text string`

              The message text to include in the Live session’s initial conversation history.

            - `Type string`

              The text content type. Always `text`.

              - `const InitialItemAssistantContentTextTypeText InitialItemAssistantContentTextType = "text"`

          - `InitialItemAssistantContentOutputText`

            - `Text string`

              The message text to include in the Live session’s initial conversation history.

            - `Type OutputText`

              The text content type. Always `output_text`.

              - `const OutputTextOutputText OutputText = "output_text"`

        - `Role Assistant`

          The author of this history message. Always `assistant`.

          - `const AssistantAssistant Assistant = "assistant"`

        - `ID string`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Status string`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `const InitialItemAssistantStatusIncomplete InitialItemAssistantStatus = "incomplete"`

          - `const InitialItemAssistantStatusCompleted InitialItemAssistantStatus = "completed"`

        - `Type string`

          The history item type. Always `message`.

          - `const InitialItemAssistantTypeMessage InitialItemAssistantType = "message"`

    - `Instructions string`

      Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

    - `Store bool`

      Whether to store the session for later forking and recording download. Defaults to false for new sessions.

  - `Type SessionStarted`

    The event type, always `session.started`.

    - `const SessionStartedSessionStarted SessionStarted = "session.started"`

  - `ClientEventID string`

    The event_id of the client command associated with this server event, when supplied.

### Session Update Config

- `type SessionUpdateConfig struct{…}`

  Changes to an active Live session. Only delegation backend settings can be updated after startup.

  - `Delegation SessionUpdateConfigDelegationUnion`

    Delegation settings to update. The delegation type must match the current session; omitted settings retain their values.

    - `type ClientDelegation struct{…}`

      Delegate tasks to your application. The Live session emits delegation events that your backend handles.

      - `Type Client`

        The delegation owner. Always `client` for tasks handled by your application.

        - `const ClientClient Client = "client"`

    - `SessionUpdateConfigDelegationResponses`

      - `Type Responses`

        The delegation owner. Always `responses` for tasks handled by the Responses API.

        - `const ResponsesResponses Responses = "responses"`

      - `Responses ResponsesDelegationUpdateConfig`

        Responses backend settings to update. Omitted settings keep their existing values.

        - `Instructions string`

          Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

        - `MaxOutputTokens int64`

          Maximum number of output tokens for each delegated response.

        - `Model string`

          The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.

        - `ParallelToolCalls bool`

          Whether the delegated Responses model may request multiple tool calls in a single response.

        - `Reasoning ResponsesDelegationUpdateConfigReasoning`

          Reasoning settings passed to each delegated Responses request.

          - `Effort string`

            How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

            - `const ResponsesDelegationUpdateConfigReasoningEffortNone ResponsesDelegationUpdateConfigReasoningEffort = "none"`

            - `const ResponsesDelegationUpdateConfigReasoningEffortMinimal ResponsesDelegationUpdateConfigReasoningEffort = "minimal"`

            - `const ResponsesDelegationUpdateConfigReasoningEffortLow ResponsesDelegationUpdateConfigReasoningEffort = "low"`

            - `const ResponsesDelegationUpdateConfigReasoningEffortMedium ResponsesDelegationUpdateConfigReasoningEffort = "medium"`

            - `const ResponsesDelegationUpdateConfigReasoningEffortHigh ResponsesDelegationUpdateConfigReasoningEffort = "high"`

            - `const ResponsesDelegationUpdateConfigReasoningEffortXhigh ResponsesDelegationUpdateConfigReasoningEffort = "xhigh"`

          - `Summary string`

            The reasoning summary to request from the delegated Responses model, when supported.

            - `const ResponsesDelegationUpdateConfigReasoningSummaryConcise ResponsesDelegationUpdateConfigReasoningSummary = "concise"`

            - `const ResponsesDelegationUpdateConfigReasoningSummaryDetailed ResponsesDelegationUpdateConfigReasoningSummary = "detailed"`

            - `const ResponsesDelegationUpdateConfigReasoningSummaryAuto ResponsesDelegationUpdateConfigReasoningSummary = "auto"`

        - `ServiceTier ResponsesDelegationUpdateConfigServiceTier`

          Service tier for delegated Responses requests.

          - `const ResponsesDelegationUpdateConfigServiceTierAuto ResponsesDelegationUpdateConfigServiceTier = "auto"`

          - `const ResponsesDelegationUpdateConfigServiceTierDefault ResponsesDelegationUpdateConfigServiceTier = "default"`

          - `const ResponsesDelegationUpdateConfigServiceTierFastTierTempPilot ResponsesDelegationUpdateConfigServiceTier = "fast_tier_temp_pilot"`

          - `const ResponsesDelegationUpdateConfigServiceTierFlex ResponsesDelegationUpdateConfigServiceTier = "flex"`

          - `const ResponsesDelegationUpdateConfigServiceTierPriority ResponsesDelegationUpdateConfigServiceTier = "priority"`

          - `const ResponsesDelegationUpdateConfigServiceTierUltrafast ResponsesDelegationUpdateConfigServiceTier = "ultrafast"`

        - `Text ResponsesDelegationUpdateConfigText`

          Text generation settings passed to each delegated Responses request.

          - `Verbosity string`

            The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

            - `const ResponsesDelegationUpdateConfigTextVerbosityLow ResponsesDelegationUpdateConfigTextVerbosity = "low"`

            - `const ResponsesDelegationUpdateConfigTextVerbosityMedium ResponsesDelegationUpdateConfigTextVerbosity = "medium"`

            - `const ResponsesDelegationUpdateConfigTextVerbosityHigh ResponsesDelegationUpdateConfigTextVerbosity = "high"`

        - `ToolChoice ResponsesDelegationUpdateConfigToolChoiceUnion`

          Controls which tool the Responses backend uses when handling a task delegated by the Live model.

          - `string`

            - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "auto"`

            - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "none"`

            - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "required"`

          - `ResponsesDelegationUpdateConfigToolChoiceLiveFunctionToolChoiceParam`

            - `Name string`

            - `Type Function`

              - `const FunctionFunction Function = "function"`

          - `ResponsesDelegationUpdateConfigToolChoiceLiveMcpToolChoiceParam`

            - `Name string`

            - `ServerLabel string`

            - `Type Mcp`

              - `const McpMcp Mcp = "mcp"`

        - `Tools []ResponsesDelegationUpdateConfigToolUnion`

          Tools available to the Responses backend while it handles tasks delegated by the Live model.

          - `type FunctionTool struct{…}`

            A function tool available to the Responses backend when the Live model delegates a task.

            - `Name string`

              The name the delegated Responses model uses when calling this function.

            - `Type Function`

              The tool type. Always `function`.

              - `const FunctionFunction Function = "function"`

            - `Description string`

              What the function does and when the delegated Responses model should call it.

            - `Parameters map[string, any]`

              A JSON Schema object describing the arguments accepted by the function.

            - `Strict bool`

              Whether the delegated Responses model must follow the function’s parameter schema exactly.

          - `ResponsesDelegationUpdateConfigToolWebSearch`

            - `Type WebSearch`

              The tool type. Always `web_search`.

              - `const WebSearchWebSearch WebSearch = "web_search"`

### Session Update Event

- `type SessionUpdateEvent struct{…}`

  Update the delegation settings of an active Live session. The server acknowledges accepted changes with `session.updated`.

  - `Session SessionUpdateConfig`

    Sparse delegation updates. Omitted settings retain their values. The delegation type cannot change, including resetting Responses delegation to null or client. Model, frontend instructions, audio, and startup input are immutable.

    - `Delegation SessionUpdateConfigDelegationUnion`

      Delegation settings to update. The delegation type must match the current session; omitted settings retain their values.

      - `type ClientDelegation struct{…}`

        Delegate tasks to your application. The Live session emits delegation events that your backend handles.

        - `Type Client`

          The delegation owner. Always `client` for tasks handled by your application.

          - `const ClientClient Client = "client"`

      - `SessionUpdateConfigDelegationResponses`

        - `Type Responses`

          The delegation owner. Always `responses` for tasks handled by the Responses API.

          - `const ResponsesResponses Responses = "responses"`

        - `Responses ResponsesDelegationUpdateConfig`

          Responses backend settings to update. Omitted settings keep their existing values.

          - `Instructions string`

            Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

          - `MaxOutputTokens int64`

            Maximum number of output tokens for each delegated response.

          - `Model string`

            The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.

          - `ParallelToolCalls bool`

            Whether the delegated Responses model may request multiple tool calls in a single response.

          - `Reasoning ResponsesDelegationUpdateConfigReasoning`

            Reasoning settings passed to each delegated Responses request.

            - `Effort string`

              How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

              - `const ResponsesDelegationUpdateConfigReasoningEffortNone ResponsesDelegationUpdateConfigReasoningEffort = "none"`

              - `const ResponsesDelegationUpdateConfigReasoningEffortMinimal ResponsesDelegationUpdateConfigReasoningEffort = "minimal"`

              - `const ResponsesDelegationUpdateConfigReasoningEffortLow ResponsesDelegationUpdateConfigReasoningEffort = "low"`

              - `const ResponsesDelegationUpdateConfigReasoningEffortMedium ResponsesDelegationUpdateConfigReasoningEffort = "medium"`

              - `const ResponsesDelegationUpdateConfigReasoningEffortHigh ResponsesDelegationUpdateConfigReasoningEffort = "high"`

              - `const ResponsesDelegationUpdateConfigReasoningEffortXhigh ResponsesDelegationUpdateConfigReasoningEffort = "xhigh"`

            - `Summary string`

              The reasoning summary to request from the delegated Responses model, when supported.

              - `const ResponsesDelegationUpdateConfigReasoningSummaryConcise ResponsesDelegationUpdateConfigReasoningSummary = "concise"`

              - `const ResponsesDelegationUpdateConfigReasoningSummaryDetailed ResponsesDelegationUpdateConfigReasoningSummary = "detailed"`

              - `const ResponsesDelegationUpdateConfigReasoningSummaryAuto ResponsesDelegationUpdateConfigReasoningSummary = "auto"`

          - `ServiceTier ResponsesDelegationUpdateConfigServiceTier`

            Service tier for delegated Responses requests.

            - `const ResponsesDelegationUpdateConfigServiceTierAuto ResponsesDelegationUpdateConfigServiceTier = "auto"`

            - `const ResponsesDelegationUpdateConfigServiceTierDefault ResponsesDelegationUpdateConfigServiceTier = "default"`

            - `const ResponsesDelegationUpdateConfigServiceTierFastTierTempPilot ResponsesDelegationUpdateConfigServiceTier = "fast_tier_temp_pilot"`

            - `const ResponsesDelegationUpdateConfigServiceTierFlex ResponsesDelegationUpdateConfigServiceTier = "flex"`

            - `const ResponsesDelegationUpdateConfigServiceTierPriority ResponsesDelegationUpdateConfigServiceTier = "priority"`

            - `const ResponsesDelegationUpdateConfigServiceTierUltrafast ResponsesDelegationUpdateConfigServiceTier = "ultrafast"`

          - `Text ResponsesDelegationUpdateConfigText`

            Text generation settings passed to each delegated Responses request.

            - `Verbosity string`

              The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

              - `const ResponsesDelegationUpdateConfigTextVerbosityLow ResponsesDelegationUpdateConfigTextVerbosity = "low"`

              - `const ResponsesDelegationUpdateConfigTextVerbosityMedium ResponsesDelegationUpdateConfigTextVerbosity = "medium"`

              - `const ResponsesDelegationUpdateConfigTextVerbosityHigh ResponsesDelegationUpdateConfigTextVerbosity = "high"`

          - `ToolChoice ResponsesDelegationUpdateConfigToolChoiceUnion`

            Controls which tool the Responses backend uses when handling a task delegated by the Live model.

            - `string`

              - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "auto"`

              - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "none"`

              - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "required"`

            - `ResponsesDelegationUpdateConfigToolChoiceLiveFunctionToolChoiceParam`

              - `Name string`

              - `Type Function`

                - `const FunctionFunction Function = "function"`

            - `ResponsesDelegationUpdateConfigToolChoiceLiveMcpToolChoiceParam`

              - `Name string`

              - `ServerLabel string`

              - `Type Mcp`

                - `const McpMcp Mcp = "mcp"`

          - `Tools []ResponsesDelegationUpdateConfigToolUnion`

            Tools available to the Responses backend while it handles tasks delegated by the Live model.

            - `type FunctionTool struct{…}`

              A function tool available to the Responses backend when the Live model delegates a task.

              - `Name string`

                The name the delegated Responses model uses when calling this function.

              - `Type Function`

                The tool type. Always `function`.

                - `const FunctionFunction Function = "function"`

              - `Description string`

                What the function does and when the delegated Responses model should call it.

              - `Parameters map[string, any]`

                A JSON Schema object describing the arguments accepted by the function.

              - `Strict bool`

                Whether the delegated Responses model must follow the function’s parameter schema exactly.

            - `ResponsesDelegationUpdateConfigToolWebSearch`

              - `Type WebSearch`

                The tool type. Always `web_search`.

                - `const WebSearchWebSearch WebSearch = "web_search"`

  - `Type SessionUpdate`

    The Live client event type. Always `session.update`.

    - `const SessionUpdateSessionUpdate SessionUpdate = "session.update"`

  - `EventID string`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Session Updated Event

- `type SessionUpdatedEvent struct{…}`

  Returned when a Live session update is accepted. Contains the resolved session configuration after the update.

  - `EventID string`

    The unique ID of the Live server event.

  - `Session SessionResource`

    The resolved Live session configuration and server-assigned session metadata.

    - `ID string`

      The unique ID of the Live session. Use this ID for sideband connections, forking, and recording download.

    - `ExpiresAt int64`

      The Unix timestamp, in seconds, at which the Live session expires.

    - `Model SessionResourceModel`

      The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

      - `string`

      - `SessionResourceModel`

        - `const SessionResourceModelGPTLive1 SessionResourceModel = "gpt-live-1"`

    - `Status Active`

      The status of the session snapshot. Always `active`, including the final snapshot in session.closed; use the event type to determine that the session has closed.

      - `const ActiveActive Active = "active"`

    - `Audio SessionResourceAudio`

      Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

      - `Format AudioFormatUnion`

        Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

        - `AudioFormatAudioPCM`

          - `Rate int64`

            Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

            - `const AudioFormatAudioPCMRate16000 AudioFormatAudioPCMRate = 16000`

            - `const AudioFormatAudioPCMRate24000 AudioFormatAudioPCMRate = 24000`

          - `Type AudioPCM`

            The audio encoding. Always `audio/pcm`.

            - `const AudioPCMAudioPCM AudioPCM = "audio/pcm"`

        - `AudioFormatAudioPCMU`

          - `Rate int64`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `Type AudioPCMU`

            The audio encoding. Always `audio/pcmu`.

            - `const AudioPCMUAudioPCMU AudioPCMU = "audio/pcmu"`

        - `AudioFormatAudioPCMA`

          - `Rate int64`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `Type AudioPCMA`

            The audio encoding. Always `audio/pcma`.

            - `const AudioPCMAAudioPCMA AudioPCMA = "audio/pcma"`

      - `Output SessionResourceAudioOutput`

        The voice used for speech generated by the Live model.

        - `Voice SessionResourceAudioOutputVoiceUnion`

          The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

          - `string`

          - `type BuiltInVoice string`

            A built-in voice available for Live speech.

            - `const BuiltInVoiceAlloy BuiltInVoice = "alloy"`

            - `const BuiltInVoiceAsh BuiltInVoice = "ash"`

            - `const BuiltInVoiceBallad BuiltInVoice = "ballad"`

            - `const BuiltInVoiceBeacon BuiltInVoice = "beacon"`

            - `const BuiltInVoiceBossa BuiltInVoice = "bossa"`

            - `const BuiltInVoiceCedar BuiltInVoice = "cedar"`

            - `const BuiltInVoiceCinder BuiltInVoice = "cinder"`

            - `const BuiltInVoiceCoral BuiltInVoice = "coral"`

            - `const BuiltInVoiceDelta BuiltInVoice = "delta"`

            - `const BuiltInVoiceEcho BuiltInVoice = "echo"`

            - `const BuiltInVoiceGleam BuiltInVoice = "gleam"`

            - `const BuiltInVoiceMarin BuiltInVoice = "marin"`

            - `const BuiltInVoiceMeridian BuiltInVoice = "meridian"`

            - `const BuiltInVoiceQuartz BuiltInVoice = "quartz"`

            - `const BuiltInVoiceRipple BuiltInVoice = "ripple"`

            - `const BuiltInVoiceSage BuiltInVoice = "sage"`

            - `const BuiltInVoiceShimmer BuiltInVoice = "shimmer"`

            - `const BuiltInVoiceStone BuiltInVoice = "stone"`

            - `const BuiltInVoiceTempo BuiltInVoice = "tempo"`

            - `const BuiltInVoiceVerse BuiltInVoice = "verse"`

            - `const BuiltInVoiceVesper BuiltInVoice = "vesper"`

            - `const BuiltInVoiceWillow BuiltInVoice = "willow"`

          - `type CustomVoice struct{…}`

            - `ID string`

    - `Client ClientConfig`

      Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

      - `DataChannel DataChannelConfig`

        Client and server event permissions for the WebRTC frontend data channel.

        - `AllowedClientEvents DataChannelConfigAllowedClientEventsUnion`

          Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

          - `All`

            - `const AllAll All = "all"`

          - `[]string`

        - `AllowedServerEvents DataChannelConfigAllowedServerEventsUnion`

          Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

          - `All`

            - `const AllAll All = "all"`

          - `[]ServerEventSelector`

            - `Type string`

              The outer Live server event type. Use 'response.event' for Responses events.

            - `ResponseEvent string`

              The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

    - `Delegation SessionResourceDelegationUnion`

      Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

      - `type ClientDelegation struct{…}`

        Delegate tasks to your application. The Live session emits delegation events that your backend handles.

        - `Type Client`

          The delegation owner. Always `client` for tasks handled by your application.

          - `const ClientClient Client = "client"`

      - `SessionResourceDelegationResponses`

        - `Responses ResponsesDelegationConfig`

          Backend model, prompt, and tools used when the Live session delegates a task to Responses.

          - `Model string`

            The model used for server-owned Responses delegations.

          - `Instructions string`

            Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

          - `MaxOutputTokens int64`

            Maximum number of output tokens for each delegated response.

          - `ParallelToolCalls bool`

            Whether the delegated Responses model may request multiple tool calls in a single response.

          - `Reasoning ResponsesDelegationConfigReasoning`

            Reasoning settings passed to each delegated Responses request.

            - `Effort string`

              How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

              - `const ResponsesDelegationConfigReasoningEffortNone ResponsesDelegationConfigReasoningEffort = "none"`

              - `const ResponsesDelegationConfigReasoningEffortMinimal ResponsesDelegationConfigReasoningEffort = "minimal"`

              - `const ResponsesDelegationConfigReasoningEffortLow ResponsesDelegationConfigReasoningEffort = "low"`

              - `const ResponsesDelegationConfigReasoningEffortMedium ResponsesDelegationConfigReasoningEffort = "medium"`

              - `const ResponsesDelegationConfigReasoningEffortHigh ResponsesDelegationConfigReasoningEffort = "high"`

              - `const ResponsesDelegationConfigReasoningEffortXhigh ResponsesDelegationConfigReasoningEffort = "xhigh"`

            - `Summary string`

              The reasoning summary to request from the delegated Responses model, when supported.

              - `const ResponsesDelegationConfigReasoningSummaryConcise ResponsesDelegationConfigReasoningSummary = "concise"`

              - `const ResponsesDelegationConfigReasoningSummaryDetailed ResponsesDelegationConfigReasoningSummary = "detailed"`

              - `const ResponsesDelegationConfigReasoningSummaryAuto ResponsesDelegationConfigReasoningSummary = "auto"`

          - `ServiceTier ResponsesDelegationConfigServiceTier`

            Service tier for delegated Responses requests.

            - `const ResponsesDelegationConfigServiceTierAuto ResponsesDelegationConfigServiceTier = "auto"`

            - `const ResponsesDelegationConfigServiceTierDefault ResponsesDelegationConfigServiceTier = "default"`

            - `const ResponsesDelegationConfigServiceTierFastTierTempPilot ResponsesDelegationConfigServiceTier = "fast_tier_temp_pilot"`

            - `const ResponsesDelegationConfigServiceTierFlex ResponsesDelegationConfigServiceTier = "flex"`

            - `const ResponsesDelegationConfigServiceTierPriority ResponsesDelegationConfigServiceTier = "priority"`

            - `const ResponsesDelegationConfigServiceTierUltrafast ResponsesDelegationConfigServiceTier = "ultrafast"`

          - `Text ResponsesDelegationConfigText`

            Text generation settings passed to each delegated Responses request.

            - `Verbosity string`

              The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

              - `const ResponsesDelegationConfigTextVerbosityLow ResponsesDelegationConfigTextVerbosity = "low"`

              - `const ResponsesDelegationConfigTextVerbosityMedium ResponsesDelegationConfigTextVerbosity = "medium"`

              - `const ResponsesDelegationConfigTextVerbosityHigh ResponsesDelegationConfigTextVerbosity = "high"`

          - `ToolChoice ResponsesDelegationConfigToolChoiceUnion`

            Controls which tool the Responses backend uses when handling a task delegated by the Live model.

            - `string`

              - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "auto"`

              - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "none"`

              - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "required"`

            - `ResponsesDelegationConfigToolChoiceLiveFunctionToolChoiceParam`

              - `Name string`

              - `Type Function`

                - `const FunctionFunction Function = "function"`

            - `ResponsesDelegationConfigToolChoiceLiveMcpToolChoiceParam`

              - `Name string`

              - `ServerLabel string`

              - `Type Mcp`

                - `const McpMcp Mcp = "mcp"`

          - `Tools []ResponsesDelegationConfigToolUnion`

            Tools available to the Responses backend while it handles tasks delegated by the Live model.

            - `type FunctionTool struct{…}`

              A function tool available to the Responses backend when the Live model delegates a task.

              - `Name string`

                The name the delegated Responses model uses when calling this function.

              - `Type Function`

                The tool type. Always `function`.

                - `const FunctionFunction Function = "function"`

              - `Description string`

                What the function does and when the delegated Responses model should call it.

              - `Parameters map[string, any]`

                A JSON Schema object describing the arguments accepted by the function.

              - `Strict bool`

                Whether the delegated Responses model must follow the function’s parameter schema exactly.

            - `ResponsesDelegationConfigToolWebSearch`

              - `Type WebSearch`

                The tool type. Always `web_search`.

                - `const WebSearchWebSearch WebSearch = "web_search"`

        - `Type Responses`

          The delegation owner. Always `responses` for tasks handled by the Responses API.

          - `const ResponsesResponses Responses = "responses"`

    - `Input []InitialItemUnion`

      Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

      - `InitialItemDeveloper`

        - `Content []InitialItemDeveloperContent`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `Text string`

            The message text to include in the Live session’s initial conversation history.

          - `Type string`

            The text content type. Always `input_text`.

            - `const InitialItemDeveloperContentTypeInputText InitialItemDeveloperContentType = "input_text"`

        - `Role Developer`

          The author of this history message. Always `developer`.

          - `const DeveloperDeveloper Developer = "developer"`

        - `ID string`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Status string`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `const InitialItemDeveloperStatusIncomplete InitialItemDeveloperStatus = "incomplete"`

          - `const InitialItemDeveloperStatusCompleted InitialItemDeveloperStatus = "completed"`

        - `Type string`

          The history item type. Always `message`.

          - `const InitialItemDeveloperTypeMessage InitialItemDeveloperType = "message"`

      - `InitialItemUser`

        - `Content []InitialItemUserContent`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `Text string`

            The message text to include in the Live session’s initial conversation history.

          - `Type string`

            The text content type. Always `input_text`.

            - `const InitialItemUserContentTypeInputText InitialItemUserContentType = "input_text"`

        - `Role User`

          The author of this history message. Always `user`.

          - `const UserUser User = "user"`

        - `ID string`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Status string`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `const InitialItemUserStatusIncomplete InitialItemUserStatus = "incomplete"`

          - `const InitialItemUserStatusCompleted InitialItemUserStatus = "completed"`

        - `Type string`

          The history item type. Always `message`.

          - `const InitialItemUserTypeMessage InitialItemUserType = "message"`

      - `InitialItemAssistant`

        - `Content []InitialItemAssistantContentUnion`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `InitialItemAssistantContentText`

            - `Text string`

              The message text to include in the Live session’s initial conversation history.

            - `Type string`

              The text content type. Always `text`.

              - `const InitialItemAssistantContentTextTypeText InitialItemAssistantContentTextType = "text"`

          - `InitialItemAssistantContentOutputText`

            - `Text string`

              The message text to include in the Live session’s initial conversation history.

            - `Type OutputText`

              The text content type. Always `output_text`.

              - `const OutputTextOutputText OutputText = "output_text"`

        - `Role Assistant`

          The author of this history message. Always `assistant`.

          - `const AssistantAssistant Assistant = "assistant"`

        - `ID string`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Status string`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `const InitialItemAssistantStatusIncomplete InitialItemAssistantStatus = "incomplete"`

          - `const InitialItemAssistantStatusCompleted InitialItemAssistantStatus = "completed"`

        - `Type string`

          The history item type. Always `message`.

          - `const InitialItemAssistantTypeMessage InitialItemAssistantType = "message"`

    - `Instructions string`

      Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

    - `Store bool`

      Whether to store the session for later forking and recording download. Defaults to false for new sessions.

  - `Type SessionUpdated`

    The event type, always `session.updated`.

    - `const SessionUpdatedSessionUpdated SessionUpdated = "session.updated"`

  - `ClientEventID string`

    The event_id of the client command associated with this server event, when supplied.

### Session Usage

- `type SessionUsage struct{…}`

  Cumulative audio duration for a Live session. Values are totals for the session, not increments to sum across usage events.

  - `Seconds float64`

    The cumulative Live audio duration in seconds. Do not sum this value across usage events.

### Session Usage Updated Event

- `type SessionUsageUpdatedEvent struct{…}`

  Reports cumulative Live audio usage and, when available, the most recent context-window usage. Delegated Responses token usage is reported separately in response.event events.

  - `EventID string`

    The unique ID of the Live server event.

  - `Type SessionUsageUpdated`

    The event type, always `session.usage.updated`.

    - `const SessionUsageUpdatedSessionUsageUpdated SessionUsageUpdated = "session.usage.updated"`

  - `Usage SessionUsage`

    The cumulative Live audio usage so far.

    - `Seconds float64`

      The cumulative Live audio duration in seconds. Do not sum this value across usage events.

  - `ClientEventID string`

    The event_id of the client command associated with this server event, when supplied.

  - `ContextWindow SessionUsageUpdatedEventContextWindow`

    The latest measured Live context-window usage. Omitted when the context limit is unknown.

    - `UsageRatio float64`

      The latest active context token count divided by the Live model context limit. Can decrease after compaction and may lag between measured audio frames.

### Thinking Append Event

- `type ThinkingAppendEvent struct{…}`

  Provide silent reasoning or progress context to the Live model, optionally for an existing client delegation.

  - `Content string`

    Silent reasoning or progress context, limited to 500 tokens. It does not directly request speech, but can influence later speech and is not a secrecy boundary.

  - `DelegationID string`

    Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

  - `Type SessionThinkingAppend`

    The Live client event type. Always `session.thinking.append`.

    - `const SessionThinkingAppendSessionThinkingAppend SessionThinkingAppend = "session.thinking.append"`

  - `EventID string`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Thinking Appended Event

- `type ThinkingAppendedEvent struct{…}`

  Returned when a session.thinking.append command is accepted into the Live session timeline. Acknowledges the added reasoning context without guaranteeing any spoken output.

  - `EndMs int64`

    The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

  - `EventID string`

    The unique ID of the Live server event.

  - `StartMs int64`

    The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

  - `Type SessionThinkingAppended`

    The event type, always `session.thinking.appended`.

    - `const SessionThinkingAppendedSessionThinkingAppended SessionThinkingAppended = "session.thinking.appended"`

  - `ClientEventID string`

    The event_id of the client command associated with this server event, when supplied.

# Forks

## Domain Types

### Fork Client Event

- `type ForkClientEventUnion interface{…}`

  Client events for a Live fork WebSocket. First send session.start with an overrides object (which may be empty), then wait for session.started before sending other commands. The model and conversation are inherited from the stored session.

  - `type ForkSessionStartEvent struct{…}`

    Start a Live session after connecting to a stored session’s fork WebSocket. Send an empty `session` object to use the stored configuration.

    - `Session ForkSessionConfig`

      Overrides for a stored session after connecting to the fork WebSocket. An empty object inherits the stored configuration; do not supply a new model. audio.format applies only to the new WebSocket connection. client overrides are only supported for WebRTC forks.

      - `Audio ForkSessionConfigAudio`

        Audio format for a WebSocket fork. WebRTC forks negotiate their audio format and must omit this field.

        - `Format AudioFormatUnion`

          Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

          - `AudioFormatAudioPCM`

            - `Rate int64`

              Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

              - `const AudioFormatAudioPCMRate16000 AudioFormatAudioPCMRate = 16000`

              - `const AudioFormatAudioPCMRate24000 AudioFormatAudioPCMRate = 24000`

            - `Type AudioPCM`

              The audio encoding. Always `audio/pcm`.

              - `const AudioPCMAudioPCM AudioPCM = "audio/pcm"`

          - `AudioFormatAudioPCMU`

            - `Rate int64`

              Audio sample rate in hertz. G.711 audio uses 8000 Hz.

            - `Type AudioPCMU`

              The audio encoding. Always `audio/pcmu`.

              - `const AudioPCMUAudioPCMU AudioPCMU = "audio/pcmu"`

          - `AudioFormatAudioPCMA`

            - `Rate int64`

              Audio sample rate in hertz. G.711 audio uses 8000 Hz.

            - `Type AudioPCMA`

              The audio encoding. Always `audio/pcma`.

              - `const AudioPCMAAudioPCMA AudioPCMA = "audio/pcma"`

      - `Client ClientConfig`

        Frontend data-channel permissions for a WebRTC fork. Omitted permissions inherit the stored values. Not supported for WebSocket forks.

        - `DataChannel DataChannelConfig`

          Client and server event permissions for the WebRTC frontend data channel.

          - `AllowedClientEvents DataChannelConfigAllowedClientEventsUnion`

            Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

            - `All`

              - `const AllAll All = "all"`

            - `[]string`

          - `AllowedServerEvents DataChannelConfigAllowedServerEventsUnion`

            Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

            - `All`

              - `const AllAll All = "all"`

            - `[]ServerEventSelector`

              - `Type string`

                The outer Live server event type. Use 'response.event' for Responses events.

              - `ResponseEvent string`

                The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

      - `Delegation ForkSessionConfigDelegation`

        Overrides for the stored session’s Responses backend. Only supported when the stored session already uses Responses delegation; the delegation type cannot change.

        - `Type Responses`

          The delegation owner. Always `responses` for tasks handled by the Responses API.

          - `const ResponsesResponses Responses = "responses"`

        - `Responses ResponsesDelegationUpdateConfig`

          Responses backend settings to update. Omitted settings keep their existing values.

          - `Instructions string`

            Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

          - `MaxOutputTokens int64`

            Maximum number of output tokens for each delegated response.

          - `Model string`

            The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.

          - `ParallelToolCalls bool`

            Whether the delegated Responses model may request multiple tool calls in a single response.

          - `Reasoning ResponsesDelegationUpdateConfigReasoning`

            Reasoning settings passed to each delegated Responses request.

            - `Effort string`

              How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

              - `const ResponsesDelegationUpdateConfigReasoningEffortNone ResponsesDelegationUpdateConfigReasoningEffort = "none"`

              - `const ResponsesDelegationUpdateConfigReasoningEffortMinimal ResponsesDelegationUpdateConfigReasoningEffort = "minimal"`

              - `const ResponsesDelegationUpdateConfigReasoningEffortLow ResponsesDelegationUpdateConfigReasoningEffort = "low"`

              - `const ResponsesDelegationUpdateConfigReasoningEffortMedium ResponsesDelegationUpdateConfigReasoningEffort = "medium"`

              - `const ResponsesDelegationUpdateConfigReasoningEffortHigh ResponsesDelegationUpdateConfigReasoningEffort = "high"`

              - `const ResponsesDelegationUpdateConfigReasoningEffortXhigh ResponsesDelegationUpdateConfigReasoningEffort = "xhigh"`

            - `Summary string`

              The reasoning summary to request from the delegated Responses model, when supported.

              - `const ResponsesDelegationUpdateConfigReasoningSummaryConcise ResponsesDelegationUpdateConfigReasoningSummary = "concise"`

              - `const ResponsesDelegationUpdateConfigReasoningSummaryDetailed ResponsesDelegationUpdateConfigReasoningSummary = "detailed"`

              - `const ResponsesDelegationUpdateConfigReasoningSummaryAuto ResponsesDelegationUpdateConfigReasoningSummary = "auto"`

          - `ServiceTier ResponsesDelegationUpdateConfigServiceTier`

            Service tier for delegated Responses requests.

            - `const ResponsesDelegationUpdateConfigServiceTierAuto ResponsesDelegationUpdateConfigServiceTier = "auto"`

            - `const ResponsesDelegationUpdateConfigServiceTierDefault ResponsesDelegationUpdateConfigServiceTier = "default"`

            - `const ResponsesDelegationUpdateConfigServiceTierFastTierTempPilot ResponsesDelegationUpdateConfigServiceTier = "fast_tier_temp_pilot"`

            - `const ResponsesDelegationUpdateConfigServiceTierFlex ResponsesDelegationUpdateConfigServiceTier = "flex"`

            - `const ResponsesDelegationUpdateConfigServiceTierPriority ResponsesDelegationUpdateConfigServiceTier = "priority"`

            - `const ResponsesDelegationUpdateConfigServiceTierUltrafast ResponsesDelegationUpdateConfigServiceTier = "ultrafast"`

          - `Text ResponsesDelegationUpdateConfigText`

            Text generation settings passed to each delegated Responses request.

            - `Verbosity string`

              The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

              - `const ResponsesDelegationUpdateConfigTextVerbosityLow ResponsesDelegationUpdateConfigTextVerbosity = "low"`

              - `const ResponsesDelegationUpdateConfigTextVerbosityMedium ResponsesDelegationUpdateConfigTextVerbosity = "medium"`

              - `const ResponsesDelegationUpdateConfigTextVerbosityHigh ResponsesDelegationUpdateConfigTextVerbosity = "high"`

          - `ToolChoice ResponsesDelegationUpdateConfigToolChoiceUnion`

            Controls which tool the Responses backend uses when handling a task delegated by the Live model.

            - `string`

              - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "auto"`

              - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "none"`

              - `const ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationUpdateConfigToolChoiceLiveToolChoiceEnum = "required"`

            - `ResponsesDelegationUpdateConfigToolChoiceLiveFunctionToolChoiceParam`

              - `Name string`

              - `Type Function`

                - `const FunctionFunction Function = "function"`

            - `ResponsesDelegationUpdateConfigToolChoiceLiveMcpToolChoiceParam`

              - `Name string`

              - `ServerLabel string`

              - `Type Mcp`

                - `const McpMcp Mcp = "mcp"`

          - `Tools []ResponsesDelegationUpdateConfigToolUnion`

            Tools available to the Responses backend while it handles tasks delegated by the Live model.

            - `type FunctionTool struct{…}`

              A function tool available to the Responses backend when the Live model delegates a task.

              - `Name string`

                The name the delegated Responses model uses when calling this function.

              - `Type Function`

                The tool type. Always `function`.

                - `const FunctionFunction Function = "function"`

              - `Description string`

                What the function does and when the delegated Responses model should call it.

              - `Parameters map[string, any]`

                A JSON Schema object describing the arguments accepted by the function.

              - `Strict bool`

                Whether the delegated Responses model must follow the function’s parameter schema exactly.

            - `ResponsesDelegationUpdateConfigToolWebSearch`

              - `Type WebSearch`

                The tool type. Always `web_search`.

                - `const WebSearchWebSearch WebSearch = "web_search"`

      - `Store bool`

        Whether to store the forked session. Omission inherits the stored session's setting.

    - `Type SessionStart`

      The Live client event type. Always `session.start`.

      - `const SessionStartSessionStart SessionStart = "session.start"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type SessionUpdateEvent struct{…}`

    Update the delegation settings of an active Live session. The server acknowledges accepted changes with `session.updated`.

    - `Session SessionUpdateConfig`

      Sparse delegation updates. Omitted settings retain their values. The delegation type cannot change, including resetting Responses delegation to null or client. Model, frontend instructions, audio, and startup input are immutable.

      - `Delegation SessionUpdateConfigDelegationUnion`

        Delegation settings to update. The delegation type must match the current session; omitted settings retain their values.

        - `type ClientDelegation struct{…}`

          Delegate tasks to your application. The Live session emits delegation events that your backend handles.

          - `Type Client`

            The delegation owner. Always `client` for tasks handled by your application.

            - `const ClientClient Client = "client"`

        - `SessionUpdateConfigDelegationResponses`

          - `Type Responses`

            The delegation owner. Always `responses` for tasks handled by the Responses API.

            - `const ResponsesResponses Responses = "responses"`

          - `Responses ResponsesDelegationUpdateConfig`

            Responses backend settings to update. Omitted settings keep their existing values.

    - `Type SessionUpdate`

      The Live client event type. Always `session.update`.

      - `const SessionUpdateSessionUpdate SessionUpdate = "session.update"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type InputAudioAppendEvent struct{…}`

    Send audio to a Live session over its primary WebSocket. WebRTC and SIP sessions send audio over their media transport.

    - `Audio string`

      Base64-encoded raw audio in the startup-selected format, without a WAV or other container header. Primary WebSocket only; media transports use their audio track. Audio appends have no acknowledgment. Reflected sideband server events reuse this event type and audio key, with no timestamps or event_id; their audio is always mono PCM16LE at 24 kHz.

    - `Type SessionInputAudioAppend`

      The Live client event type. Always `session.input_audio.append`.

      - `const SessionInputAudioAppendSessionInputAudioAppend SessionInputAudioAppend = "session.input_audio.append"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type InputAudioMuteEvent struct{…}`

    Mute audio input to the Live model without closing the session. The server acknowledges with `session.input_audio.muted`.

    - `Type SessionInputAudioMute`

      The Live client event type. Always `session.input_audio.mute`.

      - `const SessionInputAudioMuteSessionInputAudioMute SessionInputAudioMute = "session.input_audio.mute"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type InputAudioUnmuteEvent struct{…}`

    Resume audio input to a Live model after muting it. The server acknowledges with `session.input_audio.unmuted`.

    - `Type SessionInputAudioUnmute`

      The Live client event type. Always `session.input_audio.unmute`.

      - `const SessionInputAudioUnmuteSessionInputAudioUnmute SessionInputAudioUnmute = "session.input_audio.unmute"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type InstructionsAppendEvent struct{…}`

    Append instructions to the Live conversation while it is running, optionally associating them with an existing client delegation.

    - `Content string`

      Instruction text to append, limited to 500 tokens. This is a plain string, not an array of content parts.

    - `DelegationID string`

      Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

    - `Type SessionInstructionsAppend`

      The Live client event type. Always `session.instructions.append`.

      - `const SessionInstructionsAppendSessionInstructionsAppend SessionInstructionsAppend = "session.instructions.append"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type ThinkingAppendEvent struct{…}`

    Provide silent reasoning or progress context to the Live model, optionally for an existing client delegation.

    - `Content string`

      Silent reasoning or progress context, limited to 500 tokens. It does not directly request speech, but can influence later speech and is not a secrecy boundary.

    - `DelegationID string`

      Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

    - `Type SessionThinkingAppend`

      The Live client event type. Always `session.thinking.append`.

      - `const SessionThinkingAppendSessionThinkingAppend SessionThinkingAppend = "session.thinking.append"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type CommentaryAppendEvent struct{…}`

    Provide context the Live model can communicate to the user, optionally for an existing client delegation.

    - `Content string`

      Speakable context for the Live model, limited to 500 tokens. Use this for a result the model should communicate; use session.thinking.append for silent context.

    - `DelegationID string`

      Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

    - `Type SessionCommentaryAppend`

      The Live client event type. Always `session.commentary.append`.

      - `const SessionCommentaryAppendSessionCommentaryAppend SessionCommentaryAppend = "session.commentary.append"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type ResponseItemCreateEvent struct{…}`

    Add an input item to the Live session’s Responses backend. Requires Responses delegation; use `response.create` to request a response.

    - `Item ResponseInputItemUnion`

      An input item to append to the Responses backend conversation, such as a user message or a function tool result.

      - `type EasyInputMessage struct{…}`

        A message input to the model with a role indicating instruction following
        hierarchy. Instructions given with the `developer` or `system` role take
        precedence over instructions given with the `user` role. Messages with the
        `assistant` role are presumed to have been generated by the model in previous
        interactions.

        - `Content EasyInputMessageContentUnion`

          Text, image, or audio input to the model, used to generate a response.
          Can also contain previous assistant responses.

          - `string`

          - `type ResponseInputMessageContentList []ResponseInputContentUnion`

            A list of one or many input items to the model, containing different content
            types.

            - `type ResponseInputText struct{…}`

              A text input to the model.

              - `Text string`

                The text input to the model.

              - `Type InputText`

                The type of the input item. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

              - `PromptCacheBreakpoint ResponseInputTextPromptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `Mode Explicit`

                  The breakpoint mode. Always `explicit`.

                  - `const ExplicitExplicit Explicit = "explicit"`

            - `type ResponseInputImage struct{…}`

              An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

              - `Detail ResponseInputImageDetail`

                The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                - `const ResponseInputImageDetailLow ResponseInputImageDetail = "low"`

                - `const ResponseInputImageDetailHigh ResponseInputImageDetail = "high"`

                - `const ResponseInputImageDetailAuto ResponseInputImageDetail = "auto"`

                - `const ResponseInputImageDetailOriginal ResponseInputImageDetail = "original"`

              - `Type InputImage`

                The type of the input item. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

              - `FileID string`

                The ID of the file to be sent to the model.

              - `ImageURL string`

                The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

              - `PromptCacheBreakpoint ResponseInputImagePromptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `Mode Explicit`

                  The breakpoint mode. Always `explicit`.

                  - `const ExplicitExplicit Explicit = "explicit"`

            - `type ResponseInputFile struct{…}`

              A file input to the model.

              - `Type InputFile`

                The type of the input item. Always `input_file`.

                - `const InputFileInputFile InputFile = "input_file"`

              - `Detail ResponseInputFileDetail`

                The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

                - `const ResponseInputFileDetailAuto ResponseInputFileDetail = "auto"`

                - `const ResponseInputFileDetailLow ResponseInputFileDetail = "low"`

                - `const ResponseInputFileDetailHigh ResponseInputFileDetail = "high"`

              - `FileData string`

                The content of the file to be sent to the model.

              - `FileID string`

                The ID of the file to be sent to the model.

              - `FileURL string`

                The URL of the file to be sent to the model.

              - `Filename string`

                The name of the file to be sent to the model.

              - `PromptCacheBreakpoint ResponseInputFilePromptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `Mode Explicit`

                  The breakpoint mode. Always `explicit`.

                  - `const ExplicitExplicit Explicit = "explicit"`

        - `Role EasyInputMessageRole`

          The role of the message input. One of `user`, `assistant`, `system`, or
          `developer`.

          - `const EasyInputMessageRoleUser EasyInputMessageRole = "user"`

          - `const EasyInputMessageRoleAssistant EasyInputMessageRole = "assistant"`

          - `const EasyInputMessageRoleSystem EasyInputMessageRole = "system"`

          - `const EasyInputMessageRoleDeveloper EasyInputMessageRole = "developer"`

        - `Phase EasyInputMessagePhase`

          Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
          For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
          phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

          - `const EasyInputMessagePhaseCommentary EasyInputMessagePhase = "commentary"`

          - `const EasyInputMessagePhaseFinalAnswer EasyInputMessagePhase = "final_answer"`

        - `Type EasyInputMessageType`

          The type of the message input. Always `message`.

          - `const EasyInputMessageTypeMessage EasyInputMessageType = "message"`

      - `type ResponseInputItemMessage struct{…}`

        A message input to the model with a role indicating instruction following
        hierarchy. Instructions given with the `developer` or `system` role take
        precedence over instructions given with the `user` role.

        - `Content ResponseInputMessageContentList`

          A list of one or many input items to the model, containing different content
          types.

        - `Role string`

          The role of the message input. One of `user`, `system`, or `developer`.

          - `const ResponseInputItemMessageRoleUser ResponseInputItemMessageRole = "user"`

          - `const ResponseInputItemMessageRoleSystem ResponseInputItemMessageRole = "system"`

          - `const ResponseInputItemMessageRoleDeveloper ResponseInputItemMessageRole = "developer"`

        - `Status string`

          The status of item. One of `in_progress`, `completed`, or
          `incomplete`. Populated when items are returned via API.

          - `const ResponseInputItemMessageStatusInProgress ResponseInputItemMessageStatus = "in_progress"`

          - `const ResponseInputItemMessageStatusCompleted ResponseInputItemMessageStatus = "completed"`

          - `const ResponseInputItemMessageStatusIncomplete ResponseInputItemMessageStatus = "incomplete"`

        - `Type string`

          The type of the message input. Always set to `message`.

          - `const ResponseInputItemMessageTypeMessage ResponseInputItemMessageType = "message"`

      - `type ResponseOutputMessage struct{…}`

        An output message from the model.

        - `ID string`

          The unique ID of the output message.

        - `Content []ResponseOutputMessageContentUnion`

          The content of the output message.

          - `type ResponseOutputText struct{…}`

            A text output from the model.

            - `Annotations []ResponseOutputTextAnnotationUnion`

              The annotations of the text output.

              - `type ResponseOutputTextAnnotationFileCitation struct{…}`

                A citation to a file.

                - `FileID string`

                  The ID of the file.

                - `Filename string`

                  The filename of the file cited.

                - `Index int64`

                  The index in the output text at which to insert the file citation.

                - `Type FileCitation`

                  The type of the file citation. Always `file_citation`.

                  - `const FileCitationFileCitation FileCitation = "file_citation"`

              - `type ResponseOutputTextAnnotationURLCitation struct{…}`

                A citation for a web resource used to generate a model response.

                - `EndIndex int64`

                  The index of the last character of the URL citation in the message.

                - `StartIndex int64`

                  The index of the first character of the URL citation in the message.

                - `Title string`

                  The title of the web resource.

                - `Type URLCitation`

                  The type of the URL citation. Always `url_citation`.

                  - `const URLCitationURLCitation URLCitation = "url_citation"`

                - `URL string`

                  The URL of the web resource.

              - `type ResponseOutputTextAnnotationContainerFileCitation struct{…}`

                A citation for a container file used to generate a model response.

                - `ContainerID string`

                  The ID of the container file.

                - `EndIndex int64`

                  The index of the last character of the container file citation in the message.

                - `FileID string`

                  The ID of the file.

                - `Filename string`

                  The filename of the container file cited.

                - `StartIndex int64`

                  The index of the first character of the container file citation in the message.

                - `Type ContainerFileCitation`

                  The type of the container file citation. Always `container_file_citation`.

                  - `const ContainerFileCitationContainerFileCitation ContainerFileCitation = "container_file_citation"`

              - `type ResponseOutputTextAnnotationFilePath struct{…}`

                A path to a file.

                - `FileID string`

                  The ID of the file.

                - `Index int64`

                  The index of the file in the list of files.

                - `Type FilePath`

                  The type of the file path. Always `file_path`.

                  - `const FilePathFilePath FilePath = "file_path"`

            - `Text string`

              The text output from the model.

            - `Type OutputText`

              The type of the output text. Always `output_text`.

              - `const OutputTextOutputText OutputText = "output_text"`

            - `Logprobs []ResponseOutputTextLogprob`

              - `Token string`

              - `Bytes []int64`

              - `Logprob float64`

              - `TopLogprobs []ResponseOutputTextLogprobTopLogprob`

                - `Token string`

                - `Bytes []int64`

                - `Logprob float64`

          - `type ResponseOutputRefusal struct{…}`

            A refusal from the model.

            - `Refusal string`

              The refusal explanation from the model.

            - `Type Refusal`

              The type of the refusal. Always `refusal`.

              - `const RefusalRefusal Refusal = "refusal"`

        - `Role Assistant`

          The role of the output message. Always `assistant`.

          - `const AssistantAssistant Assistant = "assistant"`

        - `Status ResponseOutputMessageStatus`

          The status of the message input. One of `in_progress`, `completed`, or
          `incomplete`. Populated when input items are returned via API.

          - `const ResponseOutputMessageStatusInProgress ResponseOutputMessageStatus = "in_progress"`

          - `const ResponseOutputMessageStatusCompleted ResponseOutputMessageStatus = "completed"`

          - `const ResponseOutputMessageStatusIncomplete ResponseOutputMessageStatus = "incomplete"`

        - `Type Message`

          The type of the output message. Always `message`.

          - `const MessageMessage Message = "message"`

        - `Phase ResponseOutputMessagePhase`

          Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
          For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
          phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

          - `const ResponseOutputMessagePhaseCommentary ResponseOutputMessagePhase = "commentary"`

          - `const ResponseOutputMessagePhaseFinalAnswer ResponseOutputMessagePhase = "final_answer"`

      - `type ResponseFileSearchToolCall struct{…}`

        The results of a file search tool call. See the
        [file search guide](/api/docs/guides/tools-file-search) for more information.

        - `ID string`

          The unique ID of the file search tool call.

        - `Queries []string`

          The queries used to search for files.

        - `Status ResponseFileSearchToolCallStatus`

          The status of the file search tool call. One of `in_progress`,
          `searching`, `incomplete` or `failed`,

          - `const ResponseFileSearchToolCallStatusInProgress ResponseFileSearchToolCallStatus = "in_progress"`

          - `const ResponseFileSearchToolCallStatusSearching ResponseFileSearchToolCallStatus = "searching"`

          - `const ResponseFileSearchToolCallStatusCompleted ResponseFileSearchToolCallStatus = "completed"`

          - `const ResponseFileSearchToolCallStatusIncomplete ResponseFileSearchToolCallStatus = "incomplete"`

          - `const ResponseFileSearchToolCallStatusFailed ResponseFileSearchToolCallStatus = "failed"`

        - `Type FileSearchCall`

          The type of the file search tool call. Always `file_search_call`.

          - `const FileSearchCallFileSearchCall FileSearchCall = "file_search_call"`

        - `Results []ResponseFileSearchToolCallResult`

          The results of the file search tool call.

          - `Attributes map[string, ResponseFileSearchToolCallResultAttributeUnion]`

            Set of 16 key-value pairs that can be attached to an object. This can be
            useful for storing additional information about the object in a structured
            format, and querying for objects via API or the dashboard. Keys are strings
            with a maximum length of 64 characters. Values are strings with a maximum
            length of 512 characters, booleans, or numbers.

            - `string`

            - `float64`

            - `bool`

          - `FileID string`

            The unique ID of the file.

          - `Filename string`

            The name of the file.

          - `Score float64`

            The relevance score of the file - a value between 0 and 1.

          - `Text string`

            The text that was retrieved from the file.

      - `type ResponseComputerToolCall struct{…}`

        A tool call to a computer use tool. See the
        [computer use guide](/api/docs/guides/tools-computer-use) for more information.

        - `ID string`

          The unique ID of the computer call.

        - `CallID string`

          An identifier used when responding to the tool call with output.

        - `PendingSafetyChecks []ResponseComputerToolCallPendingSafetyCheck`

          The pending safety checks for the computer call.

          - `ID string`

            The ID of the pending safety check.

          - `Code string`

            The type of the pending safety check.

          - `Message string`

            Details about the pending safety check.

        - `Status ResponseComputerToolCallStatus`

          The status of the item. One of `in_progress`, `completed`, or
          `incomplete`. Populated when items are returned via API.

          - `const ResponseComputerToolCallStatusInProgress ResponseComputerToolCallStatus = "in_progress"`

          - `const ResponseComputerToolCallStatusCompleted ResponseComputerToolCallStatus = "completed"`

          - `const ResponseComputerToolCallStatusIncomplete ResponseComputerToolCallStatus = "incomplete"`

        - `Type ResponseComputerToolCallType`

          The type of the computer call. Always `computer_call`.

          - `const ResponseComputerToolCallTypeComputerCall ResponseComputerToolCallType = "computer_call"`

        - `Action ResponseComputerToolCallActionUnion`

          A click action.

          - `type ResponseComputerToolCallActionClick struct{…}`

            A click action.

            - `Button string`

              Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

              - `const ResponseComputerToolCallActionClickButtonLeft ResponseComputerToolCallActionClickButton = "left"`

              - `const ResponseComputerToolCallActionClickButtonRight ResponseComputerToolCallActionClickButton = "right"`

              - `const ResponseComputerToolCallActionClickButtonWheel ResponseComputerToolCallActionClickButton = "wheel"`

              - `const ResponseComputerToolCallActionClickButtonBack ResponseComputerToolCallActionClickButton = "back"`

              - `const ResponseComputerToolCallActionClickButtonForward ResponseComputerToolCallActionClickButton = "forward"`

            - `Type Click`

              Specifies the event type. For a click action, this property is always `click`.

              - `const ClickClick Click = "click"`

            - `X int64`

              The x-coordinate where the click occurred.

            - `Y int64`

              The y-coordinate where the click occurred.

            - `Keys []string`

              The keys being held while clicking.

          - `type ResponseComputerToolCallActionDoubleClick struct{…}`

            A double click action.

            - `Keys []string`

              The keys being held while double-clicking.

            - `Type DoubleClick`

              Specifies the event type. For a double click action, this property is always set to `double_click`.

              - `const DoubleClickDoubleClick DoubleClick = "double_click"`

            - `X int64`

              The x-coordinate where the double click occurred.

            - `Y int64`

              The y-coordinate where the double click occurred.

          - `type ResponseComputerToolCallActionDrag struct{…}`

            A drag action.

            - `Path []ResponseComputerToolCallActionDragPath`

              An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

              ```
              [
                { x: 100, y: 200 },
                { x: 200, y: 300 }
              ]
              ```

              - `X int64`

                The x-coordinate.

              - `Y int64`

                The y-coordinate.

            - `Type Drag`

              Specifies the event type. For a drag action, this property is always set to `drag`.

              - `const DragDrag Drag = "drag"`

            - `Keys []string`

              The keys being held while dragging the mouse.

          - `type ResponseComputerToolCallActionKeypress struct{…}`

            A collection of keypresses the model would like to perform.

            - `Keys []string`

              The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

            - `Type Keypress`

              Specifies the event type. For a keypress action, this property is always set to `keypress`.

              - `const KeypressKeypress Keypress = "keypress"`

          - `type ResponseComputerToolCallActionMove struct{…}`

            A mouse move action.

            - `Type Move`

              Specifies the event type. For a move action, this property is always set to `move`.

              - `const MoveMove Move = "move"`

            - `X int64`

              The x-coordinate to move to.

            - `Y int64`

              The y-coordinate to move to.

            - `Keys []string`

              The keys being held while moving the mouse.

          - `type ResponseComputerToolCallActionScreenshot struct{…}`

            A screenshot action.

            - `Type Screenshot`

              Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

              - `const ScreenshotScreenshot Screenshot = "screenshot"`

          - `type ResponseComputerToolCallActionScroll struct{…}`

            A scroll action.

            - `ScrollX int64`

              The horizontal scroll distance.

            - `ScrollY int64`

              The vertical scroll distance.

            - `Type Scroll`

              Specifies the event type. For a scroll action, this property is always set to `scroll`.

              - `const ScrollScroll Scroll = "scroll"`

            - `X int64`

              The x-coordinate where the scroll occurred.

            - `Y int64`

              The y-coordinate where the scroll occurred.

            - `Keys []string`

              The keys being held while scrolling.

          - `type ResponseComputerToolCallActionType struct{…}`

            An action to type in text.

            - `Text string`

              The text to type.

            - `Type Type`

              Specifies the event type. For a type action, this property is always set to `type`.

              - `const TypeType Type = "type"`

          - `type ResponseComputerToolCallActionWait struct{…}`

            A wait action.

            - `Type Wait`

              Specifies the event type. For a wait action, this property is always set to `wait`.

              - `const WaitWait Wait = "wait"`

        - `Actions ComputerActionList`

          Flattened batched actions for `computer_use`. Each action includes an
          `type` discriminator and action-specific fields.

          - `type ComputerActionClick struct{…}`

            A click action.

            - `Button string`

              Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

              - `const ComputerActionClickButtonLeft ComputerActionClickButton = "left"`

              - `const ComputerActionClickButtonRight ComputerActionClickButton = "right"`

              - `const ComputerActionClickButtonWheel ComputerActionClickButton = "wheel"`

              - `const ComputerActionClickButtonBack ComputerActionClickButton = "back"`

              - `const ComputerActionClickButtonForward ComputerActionClickButton = "forward"`

            - `Type Click`

              Specifies the event type. For a click action, this property is always `click`.

              - `const ClickClick Click = "click"`

            - `X int64`

              The x-coordinate where the click occurred.

            - `Y int64`

              The y-coordinate where the click occurred.

            - `Keys []string`

              The keys being held while clicking.

          - `type ComputerActionDoubleClick struct{…}`

            A double click action.

            - `Keys []string`

              The keys being held while double-clicking.

            - `Type DoubleClick`

              Specifies the event type. For a double click action, this property is always set to `double_click`.

              - `const DoubleClickDoubleClick DoubleClick = "double_click"`

            - `X int64`

              The x-coordinate where the double click occurred.

            - `Y int64`

              The y-coordinate where the double click occurred.

          - `type ComputerActionDrag struct{…}`

            A drag action.

            - `Path []ComputerActionDragPath`

              An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

              ```
              [
                { x: 100, y: 200 },
                { x: 200, y: 300 }
              ]
              ```

              - `X int64`

                The x-coordinate.

              - `Y int64`

                The y-coordinate.

            - `Type Drag`

              Specifies the event type. For a drag action, this property is always set to `drag`.

              - `const DragDrag Drag = "drag"`

            - `Keys []string`

              The keys being held while dragging the mouse.

          - `type ComputerActionKeypress struct{…}`

            A collection of keypresses the model would like to perform.

            - `Keys []string`

              The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

            - `Type Keypress`

              Specifies the event type. For a keypress action, this property is always set to `keypress`.

              - `const KeypressKeypress Keypress = "keypress"`

          - `type ComputerActionMove struct{…}`

            A mouse move action.

            - `Type Move`

              Specifies the event type. For a move action, this property is always set to `move`.

              - `const MoveMove Move = "move"`

            - `X int64`

              The x-coordinate to move to.

            - `Y int64`

              The y-coordinate to move to.

            - `Keys []string`

              The keys being held while moving the mouse.

          - `type ComputerActionScreenshot struct{…}`

            A screenshot action.

            - `Type Screenshot`

              Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

              - `const ScreenshotScreenshot Screenshot = "screenshot"`

          - `type ComputerActionScroll struct{…}`

            A scroll action.

            - `ScrollX int64`

              The horizontal scroll distance.

            - `ScrollY int64`

              The vertical scroll distance.

            - `Type Scroll`

              Specifies the event type. For a scroll action, this property is always set to `scroll`.

              - `const ScrollScroll Scroll = "scroll"`

            - `X int64`

              The x-coordinate where the scroll occurred.

            - `Y int64`

              The y-coordinate where the scroll occurred.

            - `Keys []string`

              The keys being held while scrolling.

          - `type ComputerActionType struct{…}`

            An action to type in text.

            - `Text string`

              The text to type.

            - `Type Type`

              Specifies the event type. For a type action, this property is always set to `type`.

              - `const TypeType Type = "type"`

          - `type ComputerActionWait struct{…}`

            A wait action.

            - `Type Wait`

              Specifies the event type. For a wait action, this property is always set to `wait`.

              - `const WaitWait Wait = "wait"`

      - `type ResponseInputItemComputerCallOutput struct{…}`

        The output of a computer tool call.

        - `CallID string`

          The ID of the computer tool call that produced the output.

        - `Output ResponseComputerToolCallOutputScreenshot`

          A computer screenshot image used with the computer use tool.

          - `Type ComputerScreenshot`

            Specifies the event type. For a computer screenshot, this property is
            always set to `computer_screenshot`.

            - `const ComputerScreenshotComputerScreenshot ComputerScreenshot = "computer_screenshot"`

          - `FileID string`

            The identifier of an uploaded file that contains the screenshot.

          - `ImageURL string`

            The URL of the screenshot image.

        - `Type ComputerCallOutput`

          The type of the computer tool call output. Always `computer_call_output`.

          - `const ComputerCallOutputComputerCallOutput ComputerCallOutput = "computer_call_output"`

        - `ID string`

          The ID of the computer tool call output.

        - `AcknowledgedSafetyChecks []ResponseInputItemComputerCallOutputAcknowledgedSafetyCheck`

          The safety checks reported by the API that have been acknowledged by the developer.

          - `ID string`

            The ID of the pending safety check.

          - `Code string`

            The type of the pending safety check.

          - `Message string`

            Details about the pending safety check.

        - `Status string`

          The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

          - `const ResponseInputItemComputerCallOutputStatusInProgress ResponseInputItemComputerCallOutputStatus = "in_progress"`

          - `const ResponseInputItemComputerCallOutputStatusCompleted ResponseInputItemComputerCallOutputStatus = "completed"`

          - `const ResponseInputItemComputerCallOutputStatusIncomplete ResponseInputItemComputerCallOutputStatus = "incomplete"`

      - `type ResponseFunctionWebSearch struct{…}`

        The results of a web search tool call. See the
        [web search guide](/api/docs/guides/tools-web-search) for more information.

        - `ID string`

          The unique ID of the web search tool call.

        - `Action ResponseFunctionWebSearchActionUnion`

          An object describing the specific action taken in this web search call.
          Includes details on how the model used the web (search, open_page, find_in_page).

          - `type ResponseFunctionWebSearchActionSearch struct{…}`

            Action type "search" - Performs a web search query.

            - `Type Search`

              The action type.

              - `const SearchSearch Search = "search"`

            - `Queries []string`

              The search queries.

            - `Query string`

              The search query.

            - `Sources []ResponseFunctionWebSearchActionSearchSource`

              The sources used in the search.

              - `Type URL`

                The type of source. Always `url`.

                - `const URLURL URL = "url"`

              - `URL string`

                The URL of the source.

          - `type ResponseFunctionWebSearchActionOpenPage struct{…}`

            Action type "open_page" - Opens a specific URL from search results.

            - `Type OpenPage`

              The action type.

              - `const OpenPageOpenPage OpenPage = "open_page"`

            - `URL string`

              The URL opened by the model.

          - `type ResponseFunctionWebSearchActionFindInPage struct{…}`

            Action type "find_in_page": Searches for a pattern within a loaded page.

            - `Pattern string`

              The pattern or text to search for within the page.

            - `Type FindInPage`

              The action type.

              - `const FindInPageFindInPage FindInPage = "find_in_page"`

            - `URL string`

              The URL of the page searched for the pattern.

        - `Status ResponseFunctionWebSearchStatus`

          The status of the web search tool call.

          - `const ResponseFunctionWebSearchStatusInProgress ResponseFunctionWebSearchStatus = "in_progress"`

          - `const ResponseFunctionWebSearchStatusSearching ResponseFunctionWebSearchStatus = "searching"`

          - `const ResponseFunctionWebSearchStatusCompleted ResponseFunctionWebSearchStatus = "completed"`

          - `const ResponseFunctionWebSearchStatusFailed ResponseFunctionWebSearchStatus = "failed"`

          - `const ResponseFunctionWebSearchStatusIncomplete ResponseFunctionWebSearchStatus = "incomplete"`

        - `Type WebSearchCall`

          The type of the web search tool call. Always `web_search_call`.

          - `const WebSearchCallWebSearchCall WebSearchCall = "web_search_call"`

      - `type ResponseFunctionToolCall struct{…}`

        A tool call to run a function. See the
        [function calling guide](/api/docs/guides/function-calling) for more information.

        - `Arguments string`

          A JSON string of the arguments to pass to the function.

        - `CallID string`

          The unique ID of the function tool call generated by the model.

        - `Name string`

          The name of the function to run.

        - `Type FunctionCall`

          The type of the function tool call. Always `function_call`.

          - `const FunctionCallFunctionCall FunctionCall = "function_call"`

        - `ID string`

          The unique ID of the function tool call.

        - `Async bool`

          Whether the function tool call runs asynchronously.

        - `Caller ResponseFunctionToolCallCallerUnion`

          The execution context that produced this tool call.

          - `type ResponseFunctionToolCallCallerDirect struct{…}`

            - `Type Direct`

              - `const DirectDirect Direct = "direct"`

          - `type ResponseFunctionToolCallCallerProgram struct{…}`

            - `CallerID string`

              The call ID of the program item that produced this tool call.

            - `Type Program`

              - `const ProgramProgram Program = "program"`

        - `Namespace string`

          The namespace of the function to run.

        - `Status ResponseFunctionToolCallStatus`

          The status of the item. One of `in_progress`, `completed`, or
          `incomplete`. Populated when items are returned via API.

          - `const ResponseFunctionToolCallStatusInProgress ResponseFunctionToolCallStatus = "in_progress"`

          - `const ResponseFunctionToolCallStatusCompleted ResponseFunctionToolCallStatus = "completed"`

          - `const ResponseFunctionToolCallStatusIncomplete ResponseFunctionToolCallStatus = "incomplete"`

      - `type ResponseInputItemFunctionCallOutput struct{…}`

        The output of a function tool call.

        - `Output ResponseInputItemFunctionCallOutputOutputUnion`

          Text, image, or file output of the function tool call.

          - `string`

          - `type ResponseFunctionCallOutputItemList []ResponseFunctionCallOutputItemUnion`

            An array of content outputs (text, image, file) for the function tool call.

            - `type ResponseInputTextContent struct{…}`

              A text input to the model.

              - `Text string`

                The text input to the model.

              - `Type InputText`

                The type of the input item. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

              - `PromptCacheBreakpoint ResponseInputTextContentPromptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `Mode Explicit`

                  The breakpoint mode. Always `explicit`.

                  - `const ExplicitExplicit Explicit = "explicit"`

            - `type ResponseInputImageContent struct{…}`

              An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision)

              - `Type InputImage`

                The type of the input item. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

              - `Detail ResponseInputImageContentDetail`

                The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                - `const ResponseInputImageContentDetailLow ResponseInputImageContentDetail = "low"`

                - `const ResponseInputImageContentDetailHigh ResponseInputImageContentDetail = "high"`

                - `const ResponseInputImageContentDetailAuto ResponseInputImageContentDetail = "auto"`

                - `const ResponseInputImageContentDetailOriginal ResponseInputImageContentDetail = "original"`

              - `FileID string`

                The ID of the file to be sent to the model.

              - `ImageURL string`

                The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

              - `PromptCacheBreakpoint ResponseInputImageContentPromptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `Mode Explicit`

                  The breakpoint mode. Always `explicit`.

                  - `const ExplicitExplicit Explicit = "explicit"`

            - `type ResponseInputFileContent struct{…}`

              A file input to the model.

              - `Type InputFile`

                The type of the input item. Always `input_file`.

                - `const InputFileInputFile InputFile = "input_file"`

              - `Detail ResponseInputFileContentDetail`

                The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

                - `const ResponseInputFileContentDetailAuto ResponseInputFileContentDetail = "auto"`

                - `const ResponseInputFileContentDetailLow ResponseInputFileContentDetail = "low"`

                - `const ResponseInputFileContentDetailHigh ResponseInputFileContentDetail = "high"`

              - `FileData string`

                The base64-encoded data of the file to be sent to the model.

              - `FileID string`

                The ID of the file to be sent to the model.

              - `FileURL string`

                The URL of the file to be sent to the model.

              - `Filename string`

                The name of the file to be sent to the model.

              - `PromptCacheBreakpoint ResponseInputFileContentPromptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `Mode Explicit`

                  The breakpoint mode. Always `explicit`.

                  - `const ExplicitExplicit Explicit = "explicit"`

        - `Type FunctionCallOutput`

          The type of the function tool call output. Always `function_call_output`.

          - `const FunctionCallOutputFunctionCallOutput FunctionCallOutput = "function_call_output"`

        - `ID string`

          The unique ID of the function tool call output. Populated when this item is returned via API.

        - `CallID string`

          The unique ID of the function tool call generated by the model.

        - `Caller ResponseInputItemFunctionCallOutputCallerUnion`

          The execution context that produced this tool call.

          - `type ResponseInputItemFunctionCallOutputCallerDirect struct{…}`

            - `Type Direct`

              The caller type. Always `direct`.

              - `const DirectDirect Direct = "direct"`

          - `type ResponseInputItemFunctionCallOutputCallerProgram struct{…}`

            - `CallerID string`

              The call ID of the program item that produced this tool call.

            - `Type Program`

              The caller type. Always `program`.

              - `const ProgramProgram Program = "program"`

        - `Name string`

          The name of the tool that produced the output.

        - `Namespace string`

          The namespace of the tool that produced the output.

        - `Status string`

          The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

          - `const ResponseInputItemFunctionCallOutputStatusInProgress ResponseInputItemFunctionCallOutputStatus = "in_progress"`

          - `const ResponseInputItemFunctionCallOutputStatusCompleted ResponseInputItemFunctionCallOutputStatus = "completed"`

          - `const ResponseInputItemFunctionCallOutputStatusIncomplete ResponseInputItemFunctionCallOutputStatus = "incomplete"`

      - `type ResponseInputItemToolSearchCall struct{…}`

        - `Arguments any`

          The arguments supplied to the tool search call.

        - `Type ToolSearchCall`

          The item type. Always `tool_search_call`.

          - `const ToolSearchCallToolSearchCall ToolSearchCall = "tool_search_call"`

        - `ID string`

          The unique ID of this tool search call.

        - `CallID string`

          The unique ID of the tool search call generated by the model.

        - `Execution string`

          Whether tool search was executed by the server or by the client.

          - `const ResponseInputItemToolSearchCallExecutionServer ResponseInputItemToolSearchCallExecution = "server"`

          - `const ResponseInputItemToolSearchCallExecutionClient ResponseInputItemToolSearchCallExecution = "client"`

        - `Status string`

          The status of the tool search call.

          - `const ResponseInputItemToolSearchCallStatusInProgress ResponseInputItemToolSearchCallStatus = "in_progress"`

          - `const ResponseInputItemToolSearchCallStatusCompleted ResponseInputItemToolSearchCallStatus = "completed"`

          - `const ResponseInputItemToolSearchCallStatusIncomplete ResponseInputItemToolSearchCallStatus = "incomplete"`

      - `type ResponseToolSearchOutputItemParamResp struct{…}`

        - `Tools []ToolUnion`

          The loaded tool definitions returned by the tool search output.

          - `type FunctionTool struct{…}`

            Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

            - `Name string`

              The name of the function to call.

            - `Parameters map[string, any]`

              A JSON schema object describing the parameters of the function.

            - `Strict bool`

              Whether strict parameter validation is enforced for this function tool.

            - `Type Function`

              The type of the function tool. Always `function`.

              - `const FunctionFunction Function = "function"`

            - `AllowedCallers []string`

              The tool invocation context(s).

              - `const FunctionToolAllowedCallerDirect FunctionToolAllowedCaller = "direct"`

              - `const FunctionToolAllowedCallerProgrammatic FunctionToolAllowedCaller = "programmatic"`

            - `Async bool`

            - `DeferLoading bool`

              Whether this function is deferred and loaded via tool search.

            - `Description string`

              A description of the function. Used by the model to determine whether or not to call the function.

            - `OutputSchema map[string, any]`

              A JSON schema object describing the JSON value encoded in string outputs for this function.

          - `type FileSearchTool struct{…}`

            A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

            - `Type FileSearch`

              The type of the file search tool. Always `file_search`.

              - `const FileSearchFileSearch FileSearch = "file_search"`

            - `VectorStoreIDs []string`

              The IDs of the vector stores to search.

            - `Filters FileSearchToolFiltersUnion`

              A filter to apply.

              - `type ComparisonFilter struct{…}`

                A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                - `Key string`

                  The key to compare against the value.

                - `Type ComparisonFilterType`

                  Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                  - `eq`: equals
                  - `ne`: not equal
                  - `gt`: greater than
                  - `gte`: greater than or equal
                  - `lt`: less than
                  - `lte`: less than or equal
                  - `in`: in
                  - `nin`: not in

                  - `const ComparisonFilterTypeEq ComparisonFilterType = "eq"`

                  - `const ComparisonFilterTypeNe ComparisonFilterType = "ne"`

                  - `const ComparisonFilterTypeGt ComparisonFilterType = "gt"`

                  - `const ComparisonFilterTypeGte ComparisonFilterType = "gte"`

                  - `const ComparisonFilterTypeLt ComparisonFilterType = "lt"`

                  - `const ComparisonFilterTypeLte ComparisonFilterType = "lte"`

                  - `const ComparisonFilterTypeIn ComparisonFilterType = "in"`

                  - `const ComparisonFilterTypeNin ComparisonFilterType = "nin"`

                - `Value ComparisonFilterValueUnion`

                  The value to compare against the attribute key; supports string, number, or boolean types.

                  - `string`

                  - `float64`

                  - `bool`

                  - `type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion`

                    - `string`

                    - `float64`

              - `type CompoundFilter struct{…}`

                Combine multiple filters using `and` or `or`.

                - `Filters []CompoundFilterFilterUnion`

                  Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

                  - `type ComparisonFilter struct{…}`

                    A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                  - `type CompoundFilter struct{…}`

                    Combine multiple filters using `and` or `or`.

                - `Type CompoundFilterType`

                  Type of operation: `and` or `or`.

                  - `const CompoundFilterTypeAnd CompoundFilterType = "and"`

                  - `const CompoundFilterTypeOr CompoundFilterType = "or"`

            - `MaxNumResults int64`

              The maximum number of results to return. This number should be between 1 and 50 inclusive.

            - `RankingOptions FileSearchToolRankingOptions`

              Ranking options for search.

              - `HybridSearch FileSearchToolRankingOptionsHybridSearch`

                Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

                - `EmbeddingWeight float64`

                  The weight of the embedding in the reciprocal ranking fusion.

                - `TextWeight float64`

                  The weight of the text in the reciprocal ranking fusion.

              - `Ranker string`

                The ranker to use for the file search.

                - `const FileSearchToolRankingOptionsRankerAuto FileSearchToolRankingOptionsRanker = "auto"`

                - `const FileSearchToolRankingOptionsRankerDefault2024_11_15 FileSearchToolRankingOptionsRanker = "default-2024-11-15"`

              - `ScoreThreshold float64`

                The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

          - `type ComputerTool struct{…}`

            A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

            - `Type Computer`

              The type of the computer tool. Always `computer`.

              - `const ComputerComputer Computer = "computer"`

          - `type ComputerUsePreviewTool struct{…}`

            A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

            - `DisplayHeight int64`

              The height of the computer display.

            - `DisplayWidth int64`

              The width of the computer display.

            - `Environment ComputerUsePreviewToolEnvironment`

              The type of computer environment to control.

              - `const ComputerUsePreviewToolEnvironmentWindows ComputerUsePreviewToolEnvironment = "windows"`

              - `const ComputerUsePreviewToolEnvironmentMac ComputerUsePreviewToolEnvironment = "mac"`

              - `const ComputerUsePreviewToolEnvironmentLinux ComputerUsePreviewToolEnvironment = "linux"`

              - `const ComputerUsePreviewToolEnvironmentUbuntu ComputerUsePreviewToolEnvironment = "ubuntu"`

              - `const ComputerUsePreviewToolEnvironmentBrowser ComputerUsePreviewToolEnvironment = "browser"`

            - `Type ComputerUsePreview`

              The type of the computer use tool. Always `computer_use_preview`.

              - `const ComputerUsePreviewComputerUsePreview ComputerUsePreview = "computer_use_preview"`

          - `type WebSearchTool struct{…}`

            Search the Internet for sources related to the prompt. Learn more about the
            [web search tool](/api/docs/guides/tools-web-search).

            - `Type WebSearchToolType`

              The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

              - `const WebSearchToolTypeWebSearch WebSearchToolType = "web_search"`

              - `const WebSearchToolTypeWebSearch2025_08_26 WebSearchToolType = "web_search_2025_08_26"`

            - `ExternalWebAccess bool`

              Allow live internet access for web search. Defaults to true when omitted. When false, the web search tool runs in offline/cache-only mode and will not fetch new external content.

            - `Filters WebSearchToolFilters`

              Filters for the search.

              - `AllowedDomains []string`

                Allowed domains for the search. If not provided, all domains are allowed.
                Subdomains of the provided domains are allowed as well.

                Example: `["pubmed.ncbi.nlm.nih.gov"]`

            - `SearchContextSize WebSearchToolSearchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `const WebSearchToolSearchContextSizeLow WebSearchToolSearchContextSize = "low"`

              - `const WebSearchToolSearchContextSizeMedium WebSearchToolSearchContextSize = "medium"`

              - `const WebSearchToolSearchContextSizeHigh WebSearchToolSearchContextSize = "high"`

            - `UserLocation WebSearchToolUserLocation`

              The approximate location of the user. If omitted or null, defaults to the
              United States. To avoid this fallback, pass `{"type": "approximate"}` without
              location fields. To localize results, provide the relevant location fields.

              - `City string`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Country string`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Region string`

                Free text input for the region of the user, e.g. `California`.

              - `Timezone string`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

              - `Type string`

                The type of location approximation. Always `approximate`.

                - `const WebSearchToolUserLocationTypeApproximate WebSearchToolUserLocationType = "approximate"`

          - `type ToolMcp struct{…}`

            Give the model access to additional tools via remote Model Context Protocol
            (MCP) servers. [Learn more about MCP](/api/docs/guides/tools-connectors-mcp).

            - `ServerLabel string`

              A label for this MCP server, used to identify it in tool calls.

            - `Type Mcp`

              The type of the MCP tool. Always `mcp`.

              - `const McpMcp Mcp = "mcp"`

            - `AllowedCallers []string`

              The tool invocation context(s).

              - `const ToolMcpAllowedCallerDirect ToolMcpAllowedCaller = "direct"`

              - `const ToolMcpAllowedCallerProgrammatic ToolMcpAllowedCaller = "programmatic"`

            - `AllowedTools ToolMcpAllowedToolsUnion`

              List of allowed tool names or a filter object.

              - `type ToolMcpAllowedToolsMcpAllowedTools []string`

                A string array of allowed tool names

              - `type ToolMcpAllowedToolsMcpToolFilter struct{…}`

                A filter object to specify which tools are allowed.

                - `ReadOnly bool`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `ToolNames []string`

                  List of allowed tool names.

            - `Authorization string`

              An OAuth access token that can be used with a remote MCP server, either
              with a custom MCP server URL or a service connector. Your application
              must handle the OAuth authorization flow and provide the token here.

            - `ConnectorID string`

              Identifier for service connectors, like those available in ChatGPT. One of
              `server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
              about service connectors [here](/api/docs/guides/tools-connectors-mcp#connectors).

              This field is deprecated for models released after September 1, 2026.
              Use `server_url` to connect to a remote MCP server, or `tunnel_id` to
              connect through a Secure MCP Tunnel.

              Currently supported `connector_id` values are:

              - Dropbox: `connector_dropbox`
              - Gmail: `connector_gmail`
              - Google Calendar: `connector_googlecalendar`
              - Google Drive: `connector_googledrive`
              - Microsoft Teams: `connector_microsoftteams`
              - Outlook Calendar: `connector_outlookcalendar`
              - Outlook Email: `connector_outlookemail`
              - SharePoint: `connector_sharepoint`

              - `const ToolMcpConnectorIDConnectorDropbox ToolMcpConnectorID = "connector_dropbox"`

              - `const ToolMcpConnectorIDConnectorGmail ToolMcpConnectorID = "connector_gmail"`

              - `const ToolMcpConnectorIDConnectorGooglecalendar ToolMcpConnectorID = "connector_googlecalendar"`

              - `const ToolMcpConnectorIDConnectorGoogledrive ToolMcpConnectorID = "connector_googledrive"`

              - `const ToolMcpConnectorIDConnectorMicrosoftteams ToolMcpConnectorID = "connector_microsoftteams"`

              - `const ToolMcpConnectorIDConnectorOutlookcalendar ToolMcpConnectorID = "connector_outlookcalendar"`

              - `const ToolMcpConnectorIDConnectorOutlookemail ToolMcpConnectorID = "connector_outlookemail"`

              - `const ToolMcpConnectorIDConnectorSharepoint ToolMcpConnectorID = "connector_sharepoint"`

            - `DeferLoading bool`

              Whether this MCP tool is deferred and discovered via tool search.

            - `Headers map[string, string]`

              Optional HTTP headers to send to the MCP server. Use for authentication
              or other purposes.

            - `RequireApproval ToolMcpRequireApprovalUnion`

              Specify which of the MCP server's tools require approval.

              - `type ToolMcpRequireApprovalMcpToolApprovalFilter struct{…}`

                Specify which of the MCP server's tools require approval. Can be
                `always`, `never`, or a filter object associated with tools
                that require approval.

                - `Always ToolMcpRequireApprovalMcpToolApprovalFilterAlways`

                  A filter object to specify which tools are allowed.

                  - `ReadOnly bool`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `ToolNames []string`

                    List of allowed tool names.

                - `Never ToolMcpRequireApprovalMcpToolApprovalFilterNever`

                  A filter object to specify which tools are allowed.

                  - `ReadOnly bool`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `ToolNames []string`

                    List of allowed tool names.

              - `type ToolMcpRequireApprovalMcpToolApprovalSetting string`

                Specify a single approval policy for all tools. One of `always` or
                `never`. When set to `always`, all tools will require approval. When
                set to `never`, all tools will not require approval.

                - `const ToolMcpRequireApprovalMcpToolApprovalSettingAlways ToolMcpRequireApprovalMcpToolApprovalSetting = "always"`

                - `const ToolMcpRequireApprovalMcpToolApprovalSettingNever ToolMcpRequireApprovalMcpToolApprovalSetting = "never"`

            - `ServerDescription string`

              Optional description of the MCP server, used to provide more context.

            - `ServerURL string`

              The URL for the MCP server. One of `server_url`, `connector_id`, or
              `tunnel_id` must be provided.

            - `TunnelID string`

              The Secure MCP Tunnel ID to use instead of a direct server URL. One of
              `server_url`, `connector_id`, or `tunnel_id` must be provided.

          - `type ToolCodeInterpreter struct{…}`

            A tool that runs Python code to help generate a response to a prompt.

            - `Container ToolCodeInterpreterContainerUnion`

              The code interpreter container. Can be a container ID or an object that
              specifies uploaded file IDs to make available to your code, along with an
              optional `memory_limit` setting.

              - `string`

              - `type ToolCodeInterpreterContainerCodeInterpreterContainerAuto struct{…}`

                Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

                - `Type Auto`

                  Always `auto`.

                  - `const AutoAuto Auto = "auto"`

                - `FileIDs []string`

                  An optional list of uploaded files to make available to your code.

                - `MemoryLimit string`

                  The memory limit for the code interpreter container.

                  - `const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit1g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "1g"`

                  - `const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit4g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "4g"`

                  - `const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit16g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "16g"`

                  - `const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit64g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "64g"`

                - `NetworkPolicy ToolCodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicyUnion`

                  Network access policy for the container.

                  - `type ContainerNetworkPolicyDisabled struct{…}`

                    - `Type Disabled`

                      Disable outbound network access. Always `disabled`.

                      - `const DisabledDisabled Disabled = "disabled"`

                  - `type ContainerNetworkPolicyAllowlist struct{…}`

                    - `AllowedDomains []string`

                      A list of allowed domains when type is `allowlist`.

                    - `Type Allowlist`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `const AllowlistAllowlist Allowlist = "allowlist"`

                    - `DomainSecrets []ContainerNetworkPolicyDomainSecret`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `Domain string`

                        The domain associated with the secret.

                      - `Name string`

                        The name of the secret to inject for the domain.

                      - `Value string`

                        The secret value to inject for the domain.

            - `Type CodeInterpreter`

              The type of the code interpreter tool. Always `code_interpreter`.

              - `const CodeInterpreterCodeInterpreter CodeInterpreter = "code_interpreter"`

            - `AllowedCallers []string`

              The tool invocation context(s).

              - `const ToolCodeInterpreterAllowedCallerDirect ToolCodeInterpreterAllowedCaller = "direct"`

              - `const ToolCodeInterpreterAllowedCallerProgrammatic ToolCodeInterpreterAllowedCaller = "programmatic"`

          - `type ToolProgrammaticToolCalling struct{…}`

            - `Type ProgrammaticToolCalling`

              The type of the tool. Always `programmatic_tool_calling`.

              - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

          - `type ToolImageGeneration struct{…}`

            A tool that generates images using the GPT image models.

            - `Type ImageGeneration`

              The type of the image generation tool. Always `image_generation`.

              - `const ImageGenerationImageGeneration ImageGeneration = "image_generation"`

            - `Action string`

              Whether to generate a new image or edit an existing image. Default: `auto`.

              - `const ToolImageGenerationActionGenerate ToolImageGenerationAction = "generate"`

              - `const ToolImageGenerationActionEdit ToolImageGenerationAction = "edit"`

              - `const ToolImageGenerationActionAuto ToolImageGenerationAction = "auto"`

            - `Background string`

              Allows to set transparency for the background of the generated image(s). Must
              be one of `transparent`, `opaque`, or `auto` (default value). When `auto` is
              used, the model will automatically determine the best background for the
              image.

              `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`, including their
              `2026-09-08` snapshots, support `opaque` and `transparent` backgrounds.
              Transparent backgrounds are available for supported GPT Image models. For
              `gpt-image-2` and `gpt-image-2-2026-04-21`, this support is in preview. When
              using `transparent`, set the output format to `png` or `webp`.

              - `const ToolImageGenerationBackgroundTransparent ToolImageGenerationBackground = "transparent"`

              - `const ToolImageGenerationBackgroundOpaque ToolImageGenerationBackground = "opaque"`

              - `const ToolImageGenerationBackgroundAuto ToolImageGenerationBackground = "auto"`

            - `InputFidelity string`

              Controls fidelity to the original input image(s). This parameter is supported for GPT image models that support input fidelity. `gpt-image-2` and `gpt-image-2-2026-04-21` ignore this parameter.

              - `const ToolImageGenerationInputFidelityHigh ToolImageGenerationInputFidelity = "high"`

              - `const ToolImageGenerationInputFidelityLow ToolImageGenerationInputFidelity = "low"`

            - `InputImageMask ToolImageGenerationInputImageMask`

              Optional mask for inpainting. Contains `image_url`
              (string, optional) and `file_id` (string, optional).

              - `FileID string`

                File ID for the mask image.

              - `ImageURL string`

                Base64-encoded mask image.

            - `Model string`

              The image generation model to use. One of `gpt-image-1`,
              `gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
              `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
              `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
              `gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
              `gpt-image-1`.

              - `string`

              - `string`

                - `const ToolImageGenerationModelGPTImage1 ToolImageGenerationModel = "gpt-image-1"`

                - `const ToolImageGenerationModelGPTImage1Mini ToolImageGenerationModel = "gpt-image-1-mini"`

                - `const ToolImageGenerationModelGPTImage2 ToolImageGenerationModel = "gpt-image-2"`

                - `const ToolImageGenerationModelGPTImage2_2026_04_21 ToolImageGenerationModel = "gpt-image-2-2026-04-21"`

                - `const ToolImageGenerationModelGPTImage2_5Sunburst ToolImageGenerationModel = "gpt-image-2.5-sunburst"`

                - `const ToolImageGenerationModelGPTImage2_5Sunburst2026_09_08 ToolImageGenerationModel = "gpt-image-2.5-sunburst-2026-09-08"`

                - `const ToolImageGenerationModelGPTImage2_5Flare ToolImageGenerationModel = "gpt-image-2.5-flare"`

                - `const ToolImageGenerationModelGPTImage2_5Flare2026_09_08 ToolImageGenerationModel = "gpt-image-2.5-flare-2026-09-08"`

                - `const ToolImageGenerationModelGPTImage1_5 ToolImageGenerationModel = "gpt-image-1.5"`

                - `const ToolImageGenerationModelChatgptImageLatest ToolImageGenerationModel = "chatgpt-image-latest"`

            - `Moderation string`

              Moderation level for the generated image. Default: `auto`.

              - `const ToolImageGenerationModerationAuto ToolImageGenerationModeration = "auto"`

              - `const ToolImageGenerationModerationLow ToolImageGenerationModeration = "low"`

            - `OutputCompression int64`

              Compression level for the output image. Default: 100.

            - `OutputFormat string`

              The output format of the generated image. One of `png`, `webp`, or
              `jpeg`. Default: `png`.

              - `const ToolImageGenerationOutputFormatPNG ToolImageGenerationOutputFormat = "png"`

              - `const ToolImageGenerationOutputFormatWebP ToolImageGenerationOutputFormat = "webp"`

              - `const ToolImageGenerationOutputFormatJPEG ToolImageGenerationOutputFormat = "jpeg"`

            - `PartialImages int64`

              Number of partial images to generate in streaming mode, from 0 (default value) to 3.

            - `Quality string`

              The quality of the generated image. The GPT image models support `low`,
              `medium`, and `high`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`,
              including their `2026-09-08` snapshots, also support `xhigh` and `max`.
              Default: `auto`.

              - `const ToolImageGenerationQualityLow ToolImageGenerationQuality = "low"`

              - `const ToolImageGenerationQualityMedium ToolImageGenerationQuality = "medium"`

              - `const ToolImageGenerationQualityHigh ToolImageGenerationQuality = "high"`

              - `const ToolImageGenerationQualityXhigh ToolImageGenerationQuality = "xhigh"`

              - `const ToolImageGenerationQualityMax ToolImageGenerationQuality = "max"`

              - `const ToolImageGenerationQualityAuto ToolImageGenerationQuality = "auto"`

            - `Size string`

              The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model's current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

              - `string`

              - `string`

                - `const ToolImageGenerationSize1024x1024 ToolImageGenerationSize = "1024x1024"`

                - `const ToolImageGenerationSize1024x1536 ToolImageGenerationSize = "1024x1536"`

                - `const ToolImageGenerationSize1536x1024 ToolImageGenerationSize = "1536x1024"`

                - `const ToolImageGenerationSizeAuto ToolImageGenerationSize = "auto"`

          - `type ToolLocalShell struct{…}`

            A tool that allows the model to execute shell commands in a local environment.

            - `Type LocalShell`

              The type of the local shell tool. Always `local_shell`.

              - `const LocalShellLocalShell LocalShell = "local_shell"`

          - `type FunctionShellTool struct{…}`

            A tool that allows the model to execute shell commands.

            - `Type Shell`

              The type of the shell tool. Always `shell`.

              - `const ShellShell Shell = "shell"`

            - `AllowedCallers []string`

              The tool invocation context(s).

              - `const FunctionShellToolAllowedCallerDirect FunctionShellToolAllowedCaller = "direct"`

              - `const FunctionShellToolAllowedCallerProgrammatic FunctionShellToolAllowedCaller = "programmatic"`

            - `Environment FunctionShellToolEnvironmentUnion`

              - `type ContainerAuto struct{…}`

                - `Type ContainerAuto`

                  Automatically creates a container for this request

                  - `const ContainerAutoContainerAuto ContainerAuto = "container_auto"`

                - `FileIDs []string`

                  An optional list of uploaded files to make available to your code.

                - `MemoryLimit ContainerAutoMemoryLimit`

                  The memory limit for the container.

                  - `const ContainerAutoMemoryLimit1g ContainerAutoMemoryLimit = "1g"`

                  - `const ContainerAutoMemoryLimit4g ContainerAutoMemoryLimit = "4g"`

                  - `const ContainerAutoMemoryLimit16g ContainerAutoMemoryLimit = "16g"`

                  - `const ContainerAutoMemoryLimit64g ContainerAutoMemoryLimit = "64g"`

                - `NetworkPolicy ContainerAutoNetworkPolicyUnion`

                  Network access policy for the container.

                  - `type ContainerNetworkPolicyDisabled struct{…}`

                  - `type ContainerNetworkPolicyAllowlist struct{…}`

                - `Skills []ContainerAutoSkillUnion`

                  An optional list of skills referenced by id or inline data.

                  - `type SkillReference struct{…}`

                    - `SkillID string`

                      The ID of the referenced skill.

                    - `Type SkillReference`

                      References a skill created with the /v1/skills endpoint.

                      - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

                    - `Version string`

                      Optional skill version. Use a positive integer or 'latest'. Omit for default.

                  - `type InlineSkill struct{…}`

                    - `Description string`

                      The description of the skill.

                    - `Name string`

                      The name of the skill.

                    - `Source InlineSkillSource`

                      Inline skill payload

                      - `Data string`

                        Base64-encoded skill zip bundle.

                      - `MediaType ApplicationZip`

                        The media type of the inline skill payload. Must be `application/zip`.

                        - `const ApplicationZipApplicationZip ApplicationZip = "application/zip"`

                      - `Type Base64`

                        The type of the inline skill source. Must be `base64`.

                        - `const Base64Base64 Base64 = "base64"`

                    - `Type Inline`

                      Defines an inline skill for this request.

                      - `const InlineInline Inline = "inline"`

              - `type LocalEnvironment struct{…}`

                - `Type Local`

                  Use a local computer environment.

                  - `const LocalLocal Local = "local"`

                - `Skills []LocalSkill`

                  An optional list of skills.

                  - `Description string`

                    The description of the skill.

                  - `Name string`

                    The name of the skill.

                  - `Path string`

                    The path to the directory containing the skill.

              - `type ContainerReference struct{…}`

                - `ContainerID string`

                  The ID of the referenced container.

                - `Type ContainerReference`

                  References a container created with the /v1/containers endpoint

                  - `const ContainerReferenceContainerReference ContainerReference = "container_reference"`

          - `type CustomTool struct{…}`

            A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

            - `Name string`

              The name of the custom tool, used to identify it in tool calls.

            - `Type Custom`

              The type of the custom tool. Always `custom`.

              - `const CustomCustom Custom = "custom"`

            - `AllowedCallers []string`

              The tool invocation context(s).

              - `const CustomToolAllowedCallerDirect CustomToolAllowedCaller = "direct"`

              - `const CustomToolAllowedCallerProgrammatic CustomToolAllowedCaller = "programmatic"`

            - `Async bool`

              Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

            - `DeferLoading bool`

              Whether this tool should be deferred and discovered via tool search.

            - `Description string`

              Optional description of the custom tool, used to provide more context.

            - `Format CustomToolInputFormatUnion`

              The input format for the custom tool. Default is unconstrained text.

              - `type CustomToolInputFormatText struct{…}`

                Unconstrained free-form text.

                - `Type Text`

                  Unconstrained text format. Always `text`.

                  - `const TextText Text = "text"`

              - `type CustomToolInputFormatGrammar struct{…}`

                A grammar defined by the user.

                - `Definition string`

                  The grammar definition.

                - `Syntax string`

                  The syntax of the grammar definition. One of `lark` or `regex`.

                  - `const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"`

                  - `const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"`

                - `Type Grammar`

                  Grammar format. Always `grammar`.

                  - `const GrammarGrammar Grammar = "grammar"`

          - `type NamespaceTool struct{…}`

            Groups function/custom tools under a shared namespace.

            - `Description string`

              A description of the namespace shown to the model.

            - `Name string`

              The namespace name used in tool calls (for example, `crm`).

            - `Tools []NamespaceToolToolUnion`

              The function/custom tools available inside this namespace.

              - `type NamespaceToolToolFunction struct{…}`

                - `Name string`

                - `Type Function`

                  - `const FunctionFunction Function = "function"`

                - `AllowedCallers []string`

                  The tool invocation context(s).

                  - `const NamespaceToolToolFunctionAllowedCallerDirect NamespaceToolToolFunctionAllowedCaller = "direct"`

                  - `const NamespaceToolToolFunctionAllowedCallerProgrammatic NamespaceToolToolFunctionAllowedCaller = "programmatic"`

                - `Async bool`

                  Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

                - `DeferLoading bool`

                  Whether this function should be deferred and discovered via tool search.

                - `Description string`

                - `OutputSchema map[string, any]`

                  A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

                - `Parameters any`

                - `Strict bool`

                  Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

              - `type CustomTool struct{…}`

                A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

            - `Type Namespace`

              The type of the tool. Always `namespace`.

              - `const NamespaceNamespace Namespace = "namespace"`

          - `type ToolSearchTool struct{…}`

            Hosted or BYOT tool search configuration for deferred tools.

            - `Type ToolSearch`

              The type of the tool. Always `tool_search`.

              - `const ToolSearchToolSearch ToolSearch = "tool_search"`

            - `Description string`

              Description shown to the model for a client-executed tool search tool.

            - `Execution ToolSearchToolExecution`

              Whether tool search is executed by the server or by the client.

              - `const ToolSearchToolExecutionServer ToolSearchToolExecution = "server"`

              - `const ToolSearchToolExecutionClient ToolSearchToolExecution = "client"`

            - `Parameters any`

              Parameter schema for a client-executed tool search tool.

          - `type WebSearchPreviewTool struct{…}`

            This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

            - `Type WebSearchPreviewToolType`

              The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

              - `const WebSearchPreviewToolTypeWebSearchPreview WebSearchPreviewToolType = "web_search_preview"`

              - `const WebSearchPreviewToolTypeWebSearchPreview2025_03_11 WebSearchPreviewToolType = "web_search_preview_2025_03_11"`

            - `SearchContentTypes []string`

              - `const WebSearchPreviewToolSearchContentTypeText WebSearchPreviewToolSearchContentType = "text"`

              - `const WebSearchPreviewToolSearchContentTypeImage WebSearchPreviewToolSearchContentType = "image"`

            - `SearchContextSize WebSearchPreviewToolSearchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `const WebSearchPreviewToolSearchContextSizeLow WebSearchPreviewToolSearchContextSize = "low"`

              - `const WebSearchPreviewToolSearchContextSizeMedium WebSearchPreviewToolSearchContextSize = "medium"`

              - `const WebSearchPreviewToolSearchContextSizeHigh WebSearchPreviewToolSearchContextSize = "high"`

            - `UserLocation WebSearchPreviewToolUserLocation`

              The approximate location of the user. If omitted or null, defaults to the United States. To avoid this fallback, pass `{"type": "approximate"}` without location fields. To localize results, provide the relevant location fields.

              - `Type Approximate`

                The type of location approximation. Always `approximate`.

                - `const ApproximateApproximate Approximate = "approximate"`

              - `City string`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Country string`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Region string`

                Free text input for the region of the user, e.g. `California`.

              - `Timezone string`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

          - `type ApplyPatchTool struct{…}`

            Allows the assistant to create, delete, or update files using unified diffs.

            - `Type ApplyPatch`

              The type of the tool. Always `apply_patch`.

              - `const ApplyPatchApplyPatch ApplyPatch = "apply_patch"`

            - `AllowedCallers []string`

              The tool invocation context(s).

              - `const ApplyPatchToolAllowedCallerDirect ApplyPatchToolAllowedCaller = "direct"`

              - `const ApplyPatchToolAllowedCallerProgrammatic ApplyPatchToolAllowedCaller = "programmatic"`

        - `Type ToolSearchOutput`

          The item type. Always `tool_search_output`.

          - `const ToolSearchOutputToolSearchOutput ToolSearchOutput = "tool_search_output"`

        - `ID string`

          The unique ID of this tool search output.

        - `CallID string`

          The unique ID of the tool search call generated by the model.

        - `Execution ResponseToolSearchOutputItemParamExecution`

          Whether tool search was executed by the server or by the client.

          - `const ResponseToolSearchOutputItemParamExecutionServer ResponseToolSearchOutputItemParamExecution = "server"`

          - `const ResponseToolSearchOutputItemParamExecutionClient ResponseToolSearchOutputItemParamExecution = "client"`

        - `Status ResponseToolSearchOutputItemParamStatus`

          The status of the tool search output.

          - `const ResponseToolSearchOutputItemParamStatusInProgress ResponseToolSearchOutputItemParamStatus = "in_progress"`

          - `const ResponseToolSearchOutputItemParamStatusCompleted ResponseToolSearchOutputItemParamStatus = "completed"`

          - `const ResponseToolSearchOutputItemParamStatusIncomplete ResponseToolSearchOutputItemParamStatus = "incomplete"`

      - `type ResponseInputItemAdditionalTools struct{…}`

        - `Role Developer`

          The role that provided the additional tools. Only `developer` is supported.

          - `const DeveloperDeveloper Developer = "developer"`

        - `Tools []ToolUnion`

          A list of additional tools made available at this item.

          - `type FunctionTool struct{…}`

            Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

          - `type FileSearchTool struct{…}`

            A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

          - `type ComputerTool struct{…}`

            A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

          - `type ComputerUsePreviewTool struct{…}`

            A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

          - `type WebSearchTool struct{…}`

            Search the Internet for sources related to the prompt. Learn more about the
            [web search tool](/api/docs/guides/tools-web-search).

          - `type ToolMcp struct{…}`

            Give the model access to additional tools via remote Model Context Protocol
            (MCP) servers. [Learn more about MCP](/api/docs/guides/tools-connectors-mcp).

          - `type ToolCodeInterpreter struct{…}`

            A tool that runs Python code to help generate a response to a prompt.

          - `type ToolProgrammaticToolCalling struct{…}`

          - `type ToolImageGeneration struct{…}`

            A tool that generates images using the GPT image models.

          - `type ToolLocalShell struct{…}`

            A tool that allows the model to execute shell commands in a local environment.

          - `type FunctionShellTool struct{…}`

            A tool that allows the model to execute shell commands.

          - `type CustomTool struct{…}`

            A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

          - `type NamespaceTool struct{…}`

            Groups function/custom tools under a shared namespace.

          - `type ToolSearchTool struct{…}`

            Hosted or BYOT tool search configuration for deferred tools.

          - `type WebSearchPreviewTool struct{…}`

            This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

          - `type ApplyPatchTool struct{…}`

            Allows the assistant to create, delete, or update files using unified diffs.

        - `Type AdditionalTools`

          The item type. Always `additional_tools`.

          - `const AdditionalToolsAdditionalTools AdditionalTools = "additional_tools"`

        - `ID string`

          The unique ID of this additional tools item.

      - `type ResponseConfigurationUpdateItemParamResp struct{…}`

        An update to the conversation's response configuration. The configuration
        remains in effect for subsequent responses until it is replaced by another
        configuration update.

        - `Type ConfigurationUpdate`

          The item type. Always `configuration_update`.

          - `const ConfigurationUpdateConfigurationUpdate ConfigurationUpdate = "configuration_update"`

        - `ID string`

          The unique ID of the configuration update item.

        - `Reasoning ResponseConfigurationUpdateItemParamReasoningResp`

          Updates to reasoning configuration. Only effort is supported.

          - `Effort ReasoningEffort`

            The reasoning effort to use for subsequent responses until another
            configuration update replaces it.

            - `const ReasoningEffortNone ReasoningEffort = "none"`

            - `const ReasoningEffortMinimal ReasoningEffort = "minimal"`

            - `const ReasoningEffortLow ReasoningEffort = "low"`

            - `const ReasoningEffortMedium ReasoningEffort = "medium"`

            - `const ReasoningEffortHigh ReasoningEffort = "high"`

            - `const ReasoningEffortXhigh ReasoningEffort = "xhigh"`

            - `const ReasoningEffortMax ReasoningEffort = "max"`

      - `type ResponseReasoningItem struct{…}`

        A description of the chain of thought used by a reasoning model while generating
        a response. Be sure to include these items in your `input` to the Responses API
        for subsequent turns of a conversation if you are manually
        [managing context](/api/docs/guides/conversation-state).

        - `ID string`

          The unique identifier of the reasoning content.

        - `Summary []ResponseReasoningItemSummary`

          Reasoning summary content.

          - `Text string`

            A summary of the reasoning output from the model so far.

          - `Type SummaryText`

            The type of the object. Always `summary_text`.

            - `const SummaryTextSummaryText SummaryText = "summary_text"`

        - `Type Reasoning`

          The type of the object. Always `reasoning`.

          - `const ReasoningReasoning Reasoning = "reasoning"`

        - `Content []ResponseReasoningItemContent`

          Reasoning text content.

          - `Text string`

            The reasoning text from the model.

          - `Type ReasoningText`

            The type of the reasoning text. Always `reasoning_text`.

            - `const ReasoningTextReasoningText ReasoningText = "reasoning_text"`

        - `EncryptedContent string`

          The encrypted content of the reasoning item. This is populated by default
          for reasoning items returned by `POST /v1/responses` and WebSocket
          `response.create` requests.

          When streaming, use the completed reasoning item and its
          `encrypted_content` from the `response.output_item.done` event in
          subsequent requests. The `encrypted_content` in
          `response.output_item.added` may be incomplete. This is especially
          important when `store` is `false` or when using Zero Data Retention.

        - `Status ResponseReasoningItemStatus`

          The status of the item. One of `in_progress`, `completed`, or
          `incomplete`. Populated when items are returned via API.

          - `const ResponseReasoningItemStatusInProgress ResponseReasoningItemStatus = "in_progress"`

          - `const ResponseReasoningItemStatusCompleted ResponseReasoningItemStatus = "completed"`

          - `const ResponseReasoningItemStatusIncomplete ResponseReasoningItemStatus = "incomplete"`

      - `type ResponseCompactionItemParamResp struct{…}`

        A compaction item generated by the [`v1/responses/compact` API](/api/reference/resources/responses/methods/compact).

        - `EncryptedContent string`

          The encrypted content of the compaction summary.

        - `Type Compaction`

          The type of the item. Always `compaction`.

          - `const CompactionCompaction Compaction = "compaction"`

        - `ID string`

          The ID of the compaction item.

      - `type ResponseInputItemImageGenerationCall struct{…}`

        An image generation request made by the model.

        - `ID string`

          The unique ID of the image generation call.

        - `Result string`

          The generated image encoded in base64.

        - `Status string`

          The status of the image generation call.

          - `const ResponseInputItemImageGenerationCallStatusInProgress ResponseInputItemImageGenerationCallStatus = "in_progress"`

          - `const ResponseInputItemImageGenerationCallStatusCompleted ResponseInputItemImageGenerationCallStatus = "completed"`

          - `const ResponseInputItemImageGenerationCallStatusGenerating ResponseInputItemImageGenerationCallStatus = "generating"`

          - `const ResponseInputItemImageGenerationCallStatusFailed ResponseInputItemImageGenerationCallStatus = "failed"`

        - `Type ImageGenerationCall`

          The type of the image generation call. Always `image_generation_call`.

          - `const ImageGenerationCallImageGenerationCall ImageGenerationCall = "image_generation_call"`

        - `Action string`

          The action used for image generation.

          - `const ResponseInputItemImageGenerationCallActionGenerate ResponseInputItemImageGenerationCallAction = "generate"`

          - `const ResponseInputItemImageGenerationCallActionEdit ResponseInputItemImageGenerationCallAction = "edit"`

          - `const ResponseInputItemImageGenerationCallActionAuto ResponseInputItemImageGenerationCallAction = "auto"`

        - `Background string`

          The background setting used for generation.

          - `const ResponseInputItemImageGenerationCallBackgroundTransparent ResponseInputItemImageGenerationCallBackground = "transparent"`

          - `const ResponseInputItemImageGenerationCallBackgroundOpaque ResponseInputItemImageGenerationCallBackground = "opaque"`

          - `const ResponseInputItemImageGenerationCallBackgroundAuto ResponseInputItemImageGenerationCallBackground = "auto"`

        - `OutputFormat string`

          The output format used for generation.

          - `const ResponseInputItemImageGenerationCallOutputFormatPNG ResponseInputItemImageGenerationCallOutputFormat = "png"`

          - `const ResponseInputItemImageGenerationCallOutputFormatWebP ResponseInputItemImageGenerationCallOutputFormat = "webp"`

          - `const ResponseInputItemImageGenerationCallOutputFormatJPEG ResponseInputItemImageGenerationCallOutputFormat = "jpeg"`

        - `Quality string`

          The quality of the image generated by the image generation tool call. One of `low`, `medium`, `high`, `xhigh`, `max`, or `auto`.

          - `const ResponseInputItemImageGenerationCallQualityLow ResponseInputItemImageGenerationCallQuality = "low"`

          - `const ResponseInputItemImageGenerationCallQualityMedium ResponseInputItemImageGenerationCallQuality = "medium"`

          - `const ResponseInputItemImageGenerationCallQualityHigh ResponseInputItemImageGenerationCallQuality = "high"`

          - `const ResponseInputItemImageGenerationCallQualityXhigh ResponseInputItemImageGenerationCallQuality = "xhigh"`

          - `const ResponseInputItemImageGenerationCallQualityMax ResponseInputItemImageGenerationCallQuality = "max"`

          - `const ResponseInputItemImageGenerationCallQualityAuto ResponseInputItemImageGenerationCallQuality = "auto"`

        - `RevisedPrompt string`

          The prompt that was used after any model prompt rewriting.

        - `Size string`

          The image dimensions as a `WIDTHxHEIGHT` string, for example `1536x864`.

          - `string`

          - `string`

            - `const ResponseInputItemImageGenerationCallSize1024x1024 ResponseInputItemImageGenerationCallSize = "1024x1024"`

            - `const ResponseInputItemImageGenerationCallSize1024x1536 ResponseInputItemImageGenerationCallSize = "1024x1536"`

            - `const ResponseInputItemImageGenerationCallSize1536x1024 ResponseInputItemImageGenerationCallSize = "1536x1024"`

      - `type ResponseCodeInterpreterToolCall struct{…}`

        A tool call to run code.

        - `ID string`

          The unique ID of the code interpreter tool call.

        - `Code string`

          The code to run, or null if not available.

        - `ContainerID string`

          The ID of the container used to run the code.

        - `Outputs []ResponseCodeInterpreterToolCallOutputUnion`

          The outputs generated by the code interpreter, such as logs or images.
          Can be null if no outputs are available.

          - `type ResponseCodeInterpreterToolCallOutputLogs struct{…}`

            The logs output from the code interpreter.

            - `Logs string`

              The logs output from the code interpreter.

            - `Type Logs`

              The type of the output. Always `logs`.

              - `const LogsLogs Logs = "logs"`

          - `type ResponseCodeInterpreterToolCallOutputImage struct{…}`

            The image output from the code interpreter.

            - `Type Image`

              The type of the output. Always `image`.

              - `const ImageImage Image = "image"`

            - `URL string`

              The URL of the image output from the code interpreter.

        - `Status ResponseCodeInterpreterToolCallStatus`

          The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

          - `const ResponseCodeInterpreterToolCallStatusInProgress ResponseCodeInterpreterToolCallStatus = "in_progress"`

          - `const ResponseCodeInterpreterToolCallStatusCompleted ResponseCodeInterpreterToolCallStatus = "completed"`

          - `const ResponseCodeInterpreterToolCallStatusIncomplete ResponseCodeInterpreterToolCallStatus = "incomplete"`

          - `const ResponseCodeInterpreterToolCallStatusInterpreting ResponseCodeInterpreterToolCallStatus = "interpreting"`

          - `const ResponseCodeInterpreterToolCallStatusFailed ResponseCodeInterpreterToolCallStatus = "failed"`

        - `Type CodeInterpreterCall`

          The type of the code interpreter tool call. Always `code_interpreter_call`.

          - `const CodeInterpreterCallCodeInterpreterCall CodeInterpreterCall = "code_interpreter_call"`

      - `type ResponseInputItemLocalShellCall struct{…}`

        A tool call to run a command on the local shell.

        - `ID string`

          The unique ID of the local shell call.

        - `Action ResponseInputItemLocalShellCallAction`

          Execute a shell command on the server.

          - `Command []string`

            The command to run.

          - `Env map[string, string]`

            Environment variables to set for the command.

          - `Type Exec`

            The type of the local shell action. Always `exec`.

            - `const ExecExec Exec = "exec"`

          - `TimeoutMs int64`

            Optional timeout in milliseconds for the command.

          - `User string`

            Optional user to run the command as.

          - `WorkingDirectory string`

            Optional working directory to run the command in.

        - `CallID string`

          The unique ID of the local shell tool call generated by the model.

        - `Status string`

          The status of the local shell call.

          - `const ResponseInputItemLocalShellCallStatusInProgress ResponseInputItemLocalShellCallStatus = "in_progress"`

          - `const ResponseInputItemLocalShellCallStatusCompleted ResponseInputItemLocalShellCallStatus = "completed"`

          - `const ResponseInputItemLocalShellCallStatusIncomplete ResponseInputItemLocalShellCallStatus = "incomplete"`

        - `Type LocalShellCall`

          The type of the local shell call. Always `local_shell_call`.

          - `const LocalShellCallLocalShellCall LocalShellCall = "local_shell_call"`

      - `type ResponseInputItemLocalShellCallOutput struct{…}`

        The output of a local shell tool call.

        - `ID string`

          The unique ID of the local shell tool call generated by the model.

        - `Output string`

          A JSON string of the output of the local shell tool call.

        - `Type LocalShellCallOutput`

          The type of the local shell tool call output. Always `local_shell_call_output`.

          - `const LocalShellCallOutputLocalShellCallOutput LocalShellCallOutput = "local_shell_call_output"`

        - `Status string`

          The status of the item. One of `in_progress`, `completed`, or `incomplete`.

          - `const ResponseInputItemLocalShellCallOutputStatusInProgress ResponseInputItemLocalShellCallOutputStatus = "in_progress"`

          - `const ResponseInputItemLocalShellCallOutputStatusCompleted ResponseInputItemLocalShellCallOutputStatus = "completed"`

          - `const ResponseInputItemLocalShellCallOutputStatusIncomplete ResponseInputItemLocalShellCallOutputStatus = "incomplete"`

      - `type ResponseInputItemShellCall struct{…}`

        A tool representing a request to execute one or more shell commands.

        - `Action ResponseInputItemShellCallAction`

          The shell commands and limits that describe how to run the tool call.

          - `Commands []string`

            Ordered shell commands for the execution environment to run.

          - `MaxOutputLength int64`

            Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

          - `TimeoutMs int64`

            Maximum wall-clock time in milliseconds to allow the shell commands to run.

        - `CallID string`

          The unique ID of the shell tool call generated by the model.

        - `Type ShellCall`

          The type of the item. Always `shell_call`.

          - `const ShellCallShellCall ShellCall = "shell_call"`

        - `ID string`

          The unique ID of the shell tool call. Populated when this item is returned via API.

        - `Caller ResponseInputItemShellCallCallerUnion`

          The execution context that produced this tool call.

          - `type ResponseInputItemShellCallCallerDirect struct{…}`

            - `Type Direct`

              The caller type. Always `direct`.

              - `const DirectDirect Direct = "direct"`

          - `type ResponseInputItemShellCallCallerProgram struct{…}`

            - `CallerID string`

              The call ID of the program item that produced this tool call.

            - `Type Program`

              The caller type. Always `program`.

              - `const ProgramProgram Program = "program"`

        - `Environment ResponseInputItemShellCallEnvironmentUnion`

          The environment to execute the shell commands in.

          - `type LocalEnvironment struct{…}`

          - `type ContainerReference struct{…}`

        - `Status string`

          The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

          - `const ResponseInputItemShellCallStatusInProgress ResponseInputItemShellCallStatus = "in_progress"`

          - `const ResponseInputItemShellCallStatusCompleted ResponseInputItemShellCallStatus = "completed"`

          - `const ResponseInputItemShellCallStatusIncomplete ResponseInputItemShellCallStatus = "incomplete"`

      - `type ResponseInputItemShellCallOutput struct{…}`

        The streamed output items emitted by a shell tool call.

        - `CallID string`

          The unique ID of the shell tool call generated by the model.

        - `Output []ResponseFunctionShellCallOutputContent`

          Captured chunks of stdout and stderr output, along with their associated outcomes.

          - `Outcome ResponseFunctionShellCallOutputContentOutcomeUnion`

            The exit or timeout outcome associated with this shell call.

            - `type ResponseFunctionShellCallOutputContentOutcomeTimeout struct{…}`

              Indicates that the shell call exceeded its configured time limit.

              - `Type Timeout`

                The outcome type. Always `timeout`.

                - `const TimeoutTimeout Timeout = "timeout"`

            - `type ResponseFunctionShellCallOutputContentOutcomeExit struct{…}`

              Indicates that the shell commands finished and returned an exit code.

              - `ExitCode int64`

                The exit code returned by the shell process.

              - `Type Exit`

                The outcome type. Always `exit`.

                - `const ExitExit Exit = "exit"`

          - `Stderr string`

            Captured stderr output for the shell call.

          - `Stdout string`

            Captured stdout output for the shell call.

        - `Type ShellCallOutput`

          The type of the item. Always `shell_call_output`.

          - `const ShellCallOutputShellCallOutput ShellCallOutput = "shell_call_output"`

        - `ID string`

          The unique ID of the shell tool call output. Populated when this item is returned via API.

        - `Caller ResponseInputItemShellCallOutputCallerUnion`

          The execution context that produced this tool call.

          - `type ResponseInputItemShellCallOutputCallerDirect struct{…}`

            - `Type Direct`

              The caller type. Always `direct`.

              - `const DirectDirect Direct = "direct"`

          - `type ResponseInputItemShellCallOutputCallerProgram struct{…}`

            - `CallerID string`

              The call ID of the program item that produced this tool call.

            - `Type Program`

              The caller type. Always `program`.

              - `const ProgramProgram Program = "program"`

        - `MaxOutputLength int64`

          The maximum number of UTF-8 characters captured for this shell call's combined output.

        - `Status string`

          The status of the shell call output.

          - `const ResponseInputItemShellCallOutputStatusInProgress ResponseInputItemShellCallOutputStatus = "in_progress"`

          - `const ResponseInputItemShellCallOutputStatusCompleted ResponseInputItemShellCallOutputStatus = "completed"`

          - `const ResponseInputItemShellCallOutputStatusIncomplete ResponseInputItemShellCallOutputStatus = "incomplete"`

      - `type ResponseInputItemApplyPatchCall struct{…}`

        A tool call representing a request to create, delete, or update files using diff patches.

        - `CallID string`

          The unique ID of the apply patch tool call generated by the model.

        - `Operation ResponseInputItemApplyPatchCallOperationUnion`

          The specific create, delete, or update instruction for the apply_patch tool call.

          - `type ResponseInputItemApplyPatchCallOperationCreateFile struct{…}`

            Instruction for creating a new file via the apply_patch tool.

            - `Diff string`

              Unified diff content to apply when creating the file.

            - `Path string`

              Path of the file to create relative to the workspace root.

            - `Type CreateFile`

              The operation type. Always `create_file`.

              - `const CreateFileCreateFile CreateFile = "create_file"`

          - `type ResponseInputItemApplyPatchCallOperationDeleteFile struct{…}`

            Instruction for deleting an existing file via the apply_patch tool.

            - `Path string`

              Path of the file to delete relative to the workspace root.

            - `Type DeleteFile`

              The operation type. Always `delete_file`.

              - `const DeleteFileDeleteFile DeleteFile = "delete_file"`

          - `type ResponseInputItemApplyPatchCallOperationUpdateFile struct{…}`

            Instruction for updating an existing file via the apply_patch tool.

            - `Diff string`

              Unified diff content to apply to the existing file.

            - `Path string`

              Path of the file to update relative to the workspace root.

            - `Type UpdateFile`

              The operation type. Always `update_file`.

              - `const UpdateFileUpdateFile UpdateFile = "update_file"`

        - `Status string`

          The status of the apply patch tool call. One of `in_progress` or `completed`.

          - `const ResponseInputItemApplyPatchCallStatusInProgress ResponseInputItemApplyPatchCallStatus = "in_progress"`

          - `const ResponseInputItemApplyPatchCallStatusCompleted ResponseInputItemApplyPatchCallStatus = "completed"`

        - `Type ApplyPatchCall`

          The type of the item. Always `apply_patch_call`.

          - `const ApplyPatchCallApplyPatchCall ApplyPatchCall = "apply_patch_call"`

        - `ID string`

          The unique ID of the apply patch tool call. Populated when this item is returned via API.

        - `Caller ResponseInputItemApplyPatchCallCallerUnion`

          The execution context that produced this tool call.

          - `type ResponseInputItemApplyPatchCallCallerDirect struct{…}`

            - `Type Direct`

              The caller type. Always `direct`.

              - `const DirectDirect Direct = "direct"`

          - `type ResponseInputItemApplyPatchCallCallerProgram struct{…}`

            - `CallerID string`

              The call ID of the program item that produced this tool call.

            - `Type Program`

              The caller type. Always `program`.

              - `const ProgramProgram Program = "program"`

      - `type ResponseInputItemApplyPatchCallOutput struct{…}`

        The streamed output emitted by an apply patch tool call.

        - `CallID string`

          The unique ID of the apply patch tool call generated by the model.

        - `Status string`

          The status of the apply patch tool call output. One of `completed` or `failed`.

          - `const ResponseInputItemApplyPatchCallOutputStatusCompleted ResponseInputItemApplyPatchCallOutputStatus = "completed"`

          - `const ResponseInputItemApplyPatchCallOutputStatusFailed ResponseInputItemApplyPatchCallOutputStatus = "failed"`

        - `Type ApplyPatchCallOutput`

          The type of the item. Always `apply_patch_call_output`.

          - `const ApplyPatchCallOutputApplyPatchCallOutput ApplyPatchCallOutput = "apply_patch_call_output"`

        - `ID string`

          The unique ID of the apply patch tool call output. Populated when this item is returned via API.

        - `Caller ResponseInputItemApplyPatchCallOutputCallerUnion`

          The execution context that produced this tool call.

          - `type ResponseInputItemApplyPatchCallOutputCallerDirect struct{…}`

            - `Type Direct`

              The caller type. Always `direct`.

              - `const DirectDirect Direct = "direct"`

          - `type ResponseInputItemApplyPatchCallOutputCallerProgram struct{…}`

            - `CallerID string`

              The call ID of the program item that produced this tool call.

            - `Type Program`

              The caller type. Always `program`.

              - `const ProgramProgram Program = "program"`

        - `Output string`

          Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

      - `type ResponseInputItemMcpListTools struct{…}`

        A list of tools available on an MCP server.

        - `ID string`

          The unique ID of the list.

        - `ServerLabel string`

          The label of the MCP server.

        - `Tools []ResponseInputItemMcpListToolsTool`

          The tools available on the server.

          - `InputSchema any`

            The JSON schema describing the tool's input.

          - `Name string`

            The name of the tool.

          - `Annotations any`

            Additional annotations about the tool.

          - `Description string`

            The description of the tool.

        - `Type McpListTools`

          The type of the item. Always `mcp_list_tools`.

          - `const McpListToolsMcpListTools McpListTools = "mcp_list_tools"`

        - `Error string`

          Error message if the server could not list tools.

      - `type ResponseInputItemMcpApprovalRequest struct{…}`

        A request for human approval of a tool invocation.

        - `ID string`

          The unique ID of the approval request.

        - `Arguments string`

          A JSON string of arguments for the tool.

        - `Name string`

          The name of the tool to run.

        - `ServerLabel string`

          The label of the MCP server making the request.

        - `Type McpApprovalRequest`

          The type of the item. Always `mcp_approval_request`.

          - `const McpApprovalRequestMcpApprovalRequest McpApprovalRequest = "mcp_approval_request"`

      - `type ResponseInputItemMcpApprovalResponse struct{…}`

        A response to an MCP approval request.

        - `ApprovalRequestID string`

          The ID of the approval request being answered.

        - `Approve bool`

          Whether the request was approved.

        - `Type McpApprovalResponse`

          The type of the item. Always `mcp_approval_response`.

          - `const McpApprovalResponseMcpApprovalResponse McpApprovalResponse = "mcp_approval_response"`

        - `ID string`

          The unique ID of the approval response

        - `Reason string`

          Optional reason for the decision.

      - `type ResponseInputItemMcpCall struct{…}`

        An invocation of a tool on an MCP server.

        - `ID string`

          The unique ID of the tool call.

        - `Arguments string`

          A JSON string of the arguments passed to the tool.

        - `Name string`

          The name of the tool that was run.

        - `ServerLabel string`

          The label of the MCP server running the tool.

        - `Type McpCall`

          The type of the item. Always `mcp_call`.

          - `const McpCallMcpCall McpCall = "mcp_call"`

        - `ApprovalRequestID string`

          Unique identifier for the MCP tool call approval request.
          Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

        - `Error McpToolCallErrorUnion`

          The error from the tool call, if any.

          - `type McpToolCallErrorMcpProtocolError struct{…}`

            - `Code int64`

            - `Message string`

            - `Type McpProtocolError`

              - `const McpProtocolErrorMcpProtocolError McpProtocolError = "mcp_protocol_error"`

          - `type McpToolCallErrorMcpToolExecutionError struct{…}`

            - `Content any`

            - `Type McpToolExecutionError`

              - `const McpToolExecutionErrorMcpToolExecutionError McpToolExecutionError = "mcp_tool_execution_error"`

          - `type McpToolCallErrorHTTPError struct{…}`

            - `Code int64`

            - `Message string`

            - `Type HTTPError`

              - `const HTTPErrorHTTPError HTTPError = "http_error"`

        - `Output string`

          The output from the tool call.

        - `Status string`

          The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

          - `const ResponseInputItemMcpCallStatusInProgress ResponseInputItemMcpCallStatus = "in_progress"`

          - `const ResponseInputItemMcpCallStatusCompleted ResponseInputItemMcpCallStatus = "completed"`

          - `const ResponseInputItemMcpCallStatusIncomplete ResponseInputItemMcpCallStatus = "incomplete"`

          - `const ResponseInputItemMcpCallStatusCalling ResponseInputItemMcpCallStatus = "calling"`

          - `const ResponseInputItemMcpCallStatusFailed ResponseInputItemMcpCallStatus = "failed"`

      - `type ResponseCustomToolCallOutput struct{…}`

        The output of a custom tool call from your code, being sent back to the model.

        - `CallID string`

          The call ID, used to map this custom tool call output to a custom tool call.

        - `Output ResponseCustomToolCallOutputOutputUnion`

          The output from the custom tool call generated by your code.
          Can be a string or an list of output content.

          - `string`

          - `type ResponseCustomToolCallOutputOutputOutputContentList []ResponseCustomToolCallOutputOutputOutputContentListItemUnion`

            Text, image, or file output of the custom tool call.

            - `type ResponseInputText struct{…}`

              A text input to the model.

            - `type ResponseInputImage struct{…}`

              An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

            - `type ResponseInputFile struct{…}`

              A file input to the model.

        - `Type CustomToolCallOutput`

          The type of the custom tool call output. Always `custom_tool_call_output`.

          - `const CustomToolCallOutputCustomToolCallOutput CustomToolCallOutput = "custom_tool_call_output"`

        - `ID string`

          The unique ID of the custom tool call output in the OpenAI platform.

        - `Caller ResponseCustomToolCallOutputCallerUnion`

          The execution context that produced this tool call.

          - `type ResponseCustomToolCallOutputCallerDirect struct{…}`

            - `Type Direct`

              The caller type. Always `direct`.

              - `const DirectDirect Direct = "direct"`

          - `type ResponseCustomToolCallOutputCallerProgram struct{…}`

            - `CallerID string`

              The call ID of the program item that produced this tool call.

            - `Type Program`

              The caller type. Always `program`.

              - `const ProgramProgram Program = "program"`

      - `type ResponseCustomToolCall struct{…}`

        A call to a custom tool created by the model.

        - `CallID string`

          An identifier used to map this custom tool call to a tool call output.

        - `Input string`

          The input for the custom tool call generated by the model.

        - `Name string`

          The name of the custom tool being called.

        - `Type CustomToolCall`

          The type of the custom tool call. Always `custom_tool_call`.

          - `const CustomToolCallCustomToolCall CustomToolCall = "custom_tool_call"`

        - `ID string`

          The unique ID of the custom tool call in the OpenAI platform.

        - `Async bool`

          Whether the custom tool call runs asynchronously.

        - `Caller ResponseCustomToolCallCallerUnion`

          The execution context that produced this tool call.

          - `type ResponseCustomToolCallCallerDirect struct{…}`

            - `Type Direct`

              - `const DirectDirect Direct = "direct"`

          - `type ResponseCustomToolCallCallerProgram struct{…}`

            - `CallerID string`

              The call ID of the program item that produced this tool call.

            - `Type Program`

              - `const ProgramProgram Program = "program"`

        - `Namespace string`

          The namespace of the custom tool being called.

      - `type ResponseInputItemCompactionTrigger struct{…}`

        Compacts the current context. Must be the final input item.

        - `Type CompactionTrigger`

          The type of the item. Always `compaction_trigger`.

          - `const CompactionTriggerCompactionTrigger CompactionTrigger = "compaction_trigger"`

      - `type ResponseInputItemItemReference struct{…}`

        An internal identifier for an item to reference.

        - `ID string`

          The ID of the item to reference.

        - `Type string`

          The type of item to reference. Always `item_reference`.

          - `const ResponseInputItemItemReferenceTypeItemReference ResponseInputItemItemReferenceType = "item_reference"`

      - `type ResponseInputItemProgram struct{…}`

        - `ID string`

          The unique ID of this program item.

        - `CallID string`

          The stable call ID of the program item.

        - `Code string`

          The JavaScript source executed by programmatic tool calling.

        - `Fingerprint string`

          Opaque program replay fingerprint that must be round-tripped.

        - `Type Program`

          The item type. Always `program`.

          - `const ProgramProgram Program = "program"`

      - `type ResponseInputItemProgramOutput struct{…}`

        - `ID string`

          The unique ID of this program output item.

        - `CallID string`

          The call ID of the program item.

        - `Result string`

          The result produced by the program item.

        - `Status string`

          The terminal status of the program output.

          - `const ResponseInputItemProgramOutputStatusCompleted ResponseInputItemProgramOutputStatus = "completed"`

          - `const ResponseInputItemProgramOutputStatusIncomplete ResponseInputItemProgramOutputStatus = "incomplete"`

        - `Type ProgramOutput`

          The item type. Always `program_output`.

          - `const ProgramOutputProgramOutput ProgramOutput = "program_output"`

    - `Type ResponseItemCreate`

      The Live client event type. Always `response.item.create`.

      - `const ResponseItemCreateResponseItemCreate ResponseItemCreate = "response.item.create"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type ResponseCreateEvent struct{…}`

    Request a response from the Live session’s Responses backend, or continue a delegated response waiting for tool results. Requires Responses delegation.

    - `Type ResponseCreate`

      The Live client event type. Always `response.create`.

      - `const ResponseCreateResponseCreate ResponseCreate = "response.create"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `type SessionCloseEvent struct{…}`

    Request that the Live session close. The terminal `session.closed` event contains the close reason and final usage.

    - `Type SessionClose`

      The Live client event type. Always `session.close`.

      - `const SessionCloseSessionClose SessionClose = "session.close"`

    - `EventID string`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Fork Server Event

- `type ForkServerEventUnion interface{…}`

  Server events for Live. Response lifecycle events are wrapped inside response.event; dispatch the nested event by its full type and tolerate new response event types. Follow the [Live prompting guide](https://developers.openai.com/api/docs/guides/live-prompting) when designing the conversation and delegation policy.

  - `type SessionStartedEvent struct{…}`

    Returned when a Live session has started. Contains the resolved session configuration, including server defaults.

    - `EventID string`

      The unique ID of the Live server event.

    - `Session SessionResource`

      The resolved Live session configuration and server-assigned session metadata.

      - `ID string`

        The unique ID of the Live session. Use this ID for sideband connections, forking, and recording download.

      - `ExpiresAt int64`

        The Unix timestamp, in seconds, at which the Live session expires.

      - `Model SessionResourceModel`

        The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

        - `string`

        - `SessionResourceModel`

          - `const SessionResourceModelGPTLive1 SessionResourceModel = "gpt-live-1"`

      - `Status Active`

        The status of the session snapshot. Always `active`, including the final snapshot in session.closed; use the event type to determine that the session has closed.

        - `const ActiveActive Active = "active"`

      - `Audio SessionResourceAudio`

        Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

        - `Format AudioFormatUnion`

          Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

          - `AudioFormatAudioPCM`

            - `Rate int64`

              Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

              - `const AudioFormatAudioPCMRate16000 AudioFormatAudioPCMRate = 16000`

              - `const AudioFormatAudioPCMRate24000 AudioFormatAudioPCMRate = 24000`

            - `Type AudioPCM`

              The audio encoding. Always `audio/pcm`.

              - `const AudioPCMAudioPCM AudioPCM = "audio/pcm"`

          - `AudioFormatAudioPCMU`

            - `Rate int64`

              Audio sample rate in hertz. G.711 audio uses 8000 Hz.

            - `Type AudioPCMU`

              The audio encoding. Always `audio/pcmu`.

              - `const AudioPCMUAudioPCMU AudioPCMU = "audio/pcmu"`

          - `AudioFormatAudioPCMA`

            - `Rate int64`

              Audio sample rate in hertz. G.711 audio uses 8000 Hz.

            - `Type AudioPCMA`

              The audio encoding. Always `audio/pcma`.

              - `const AudioPCMAAudioPCMA AudioPCMA = "audio/pcma"`

        - `Output SessionResourceAudioOutput`

          The voice used for speech generated by the Live model.

          - `Voice SessionResourceAudioOutputVoiceUnion`

            The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

            - `string`

            - `type BuiltInVoice string`

              A built-in voice available for Live speech.

              - `const BuiltInVoiceAlloy BuiltInVoice = "alloy"`

              - `const BuiltInVoiceAsh BuiltInVoice = "ash"`

              - `const BuiltInVoiceBallad BuiltInVoice = "ballad"`

              - `const BuiltInVoiceBeacon BuiltInVoice = "beacon"`

              - `const BuiltInVoiceBossa BuiltInVoice = "bossa"`

              - `const BuiltInVoiceCedar BuiltInVoice = "cedar"`

              - `const BuiltInVoiceCinder BuiltInVoice = "cinder"`

              - `const BuiltInVoiceCoral BuiltInVoice = "coral"`

              - `const BuiltInVoiceDelta BuiltInVoice = "delta"`

              - `const BuiltInVoiceEcho BuiltInVoice = "echo"`

              - `const BuiltInVoiceGleam BuiltInVoice = "gleam"`

              - `const BuiltInVoiceMarin BuiltInVoice = "marin"`

              - `const BuiltInVoiceMeridian BuiltInVoice = "meridian"`

              - `const BuiltInVoiceQuartz BuiltInVoice = "quartz"`

              - `const BuiltInVoiceRipple BuiltInVoice = "ripple"`

              - `const BuiltInVoiceSage BuiltInVoice = "sage"`

              - `const BuiltInVoiceShimmer BuiltInVoice = "shimmer"`

              - `const BuiltInVoiceStone BuiltInVoice = "stone"`

              - `const BuiltInVoiceTempo BuiltInVoice = "tempo"`

              - `const BuiltInVoiceVerse BuiltInVoice = "verse"`

              - `const BuiltInVoiceVesper BuiltInVoice = "vesper"`

              - `const BuiltInVoiceWillow BuiltInVoice = "willow"`

            - `type CustomVoice struct{…}`

              - `ID string`

      - `Client ClientConfig`

        Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

        - `DataChannel DataChannelConfig`

          Client and server event permissions for the WebRTC frontend data channel.

          - `AllowedClientEvents DataChannelConfigAllowedClientEventsUnion`

            Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

            - `All`

              - `const AllAll All = "all"`

            - `[]string`

          - `AllowedServerEvents DataChannelConfigAllowedServerEventsUnion`

            Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

            - `All`

              - `const AllAll All = "all"`

            - `[]ServerEventSelector`

              - `Type string`

                The outer Live server event type. Use 'response.event' for Responses events.

              - `ResponseEvent string`

                The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

      - `Delegation SessionResourceDelegationUnion`

        Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

        - `type ClientDelegation struct{…}`

          Delegate tasks to your application. The Live session emits delegation events that your backend handles.

          - `Type Client`

            The delegation owner. Always `client` for tasks handled by your application.

            - `const ClientClient Client = "client"`

        - `SessionResourceDelegationResponses`

          - `Responses ResponsesDelegationConfig`

            Backend model, prompt, and tools used when the Live session delegates a task to Responses.

            - `Model string`

              The model used for server-owned Responses delegations.

            - `Instructions string`

              Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

            - `MaxOutputTokens int64`

              Maximum number of output tokens for each delegated response.

            - `ParallelToolCalls bool`

              Whether the delegated Responses model may request multiple tool calls in a single response.

            - `Reasoning ResponsesDelegationConfigReasoning`

              Reasoning settings passed to each delegated Responses request.

              - `Effort string`

                How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

                - `const ResponsesDelegationConfigReasoningEffortNone ResponsesDelegationConfigReasoningEffort = "none"`

                - `const ResponsesDelegationConfigReasoningEffortMinimal ResponsesDelegationConfigReasoningEffort = "minimal"`

                - `const ResponsesDelegationConfigReasoningEffortLow ResponsesDelegationConfigReasoningEffort = "low"`

                - `const ResponsesDelegationConfigReasoningEffortMedium ResponsesDelegationConfigReasoningEffort = "medium"`

                - `const ResponsesDelegationConfigReasoningEffortHigh ResponsesDelegationConfigReasoningEffort = "high"`

                - `const ResponsesDelegationConfigReasoningEffortXhigh ResponsesDelegationConfigReasoningEffort = "xhigh"`

              - `Summary string`

                The reasoning summary to request from the delegated Responses model, when supported.

                - `const ResponsesDelegationConfigReasoningSummaryConcise ResponsesDelegationConfigReasoningSummary = "concise"`

                - `const ResponsesDelegationConfigReasoningSummaryDetailed ResponsesDelegationConfigReasoningSummary = "detailed"`

                - `const ResponsesDelegationConfigReasoningSummaryAuto ResponsesDelegationConfigReasoningSummary = "auto"`

            - `ServiceTier ResponsesDelegationConfigServiceTier`

              Service tier for delegated Responses requests.

              - `const ResponsesDelegationConfigServiceTierAuto ResponsesDelegationConfigServiceTier = "auto"`

              - `const ResponsesDelegationConfigServiceTierDefault ResponsesDelegationConfigServiceTier = "default"`

              - `const ResponsesDelegationConfigServiceTierFastTierTempPilot ResponsesDelegationConfigServiceTier = "fast_tier_temp_pilot"`

              - `const ResponsesDelegationConfigServiceTierFlex ResponsesDelegationConfigServiceTier = "flex"`

              - `const ResponsesDelegationConfigServiceTierPriority ResponsesDelegationConfigServiceTier = "priority"`

              - `const ResponsesDelegationConfigServiceTierUltrafast ResponsesDelegationConfigServiceTier = "ultrafast"`

            - `Text ResponsesDelegationConfigText`

              Text generation settings passed to each delegated Responses request.

              - `Verbosity string`

                The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

                - `const ResponsesDelegationConfigTextVerbosityLow ResponsesDelegationConfigTextVerbosity = "low"`

                - `const ResponsesDelegationConfigTextVerbosityMedium ResponsesDelegationConfigTextVerbosity = "medium"`

                - `const ResponsesDelegationConfigTextVerbosityHigh ResponsesDelegationConfigTextVerbosity = "high"`

            - `ToolChoice ResponsesDelegationConfigToolChoiceUnion`

              Controls which tool the Responses backend uses when handling a task delegated by the Live model.

              - `string`

                - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "auto"`

                - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "none"`

                - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "required"`

              - `ResponsesDelegationConfigToolChoiceLiveFunctionToolChoiceParam`

                - `Name string`

                - `Type Function`

                  - `const FunctionFunction Function = "function"`

              - `ResponsesDelegationConfigToolChoiceLiveMcpToolChoiceParam`

                - `Name string`

                - `ServerLabel string`

                - `Type Mcp`

                  - `const McpMcp Mcp = "mcp"`

            - `Tools []ResponsesDelegationConfigToolUnion`

              Tools available to the Responses backend while it handles tasks delegated by the Live model.

              - `type FunctionTool struct{…}`

                A function tool available to the Responses backend when the Live model delegates a task.

                - `Name string`

                  The name the delegated Responses model uses when calling this function.

                - `Type Function`

                  The tool type. Always `function`.

                  - `const FunctionFunction Function = "function"`

                - `Description string`

                  What the function does and when the delegated Responses model should call it.

                - `Parameters map[string, any]`

                  A JSON Schema object describing the arguments accepted by the function.

                - `Strict bool`

                  Whether the delegated Responses model must follow the function’s parameter schema exactly.

              - `ResponsesDelegationConfigToolWebSearch`

                - `Type WebSearch`

                  The tool type. Always `web_search`.

                  - `const WebSearchWebSearch WebSearch = "web_search"`

          - `Type Responses`

            The delegation owner. Always `responses` for tasks handled by the Responses API.

            - `const ResponsesResponses Responses = "responses"`

      - `Input []InitialItemUnion`

        Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

        - `InitialItemDeveloper`

          - `Content []InitialItemDeveloperContent`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `Text string`

              The message text to include in the Live session’s initial conversation history.

            - `Type string`

              The text content type. Always `input_text`.

              - `const InitialItemDeveloperContentTypeInputText InitialItemDeveloperContentType = "input_text"`

          - `Role Developer`

            The author of this history message. Always `developer`.

            - `const DeveloperDeveloper Developer = "developer"`

          - `ID string`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Status string`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `const InitialItemDeveloperStatusIncomplete InitialItemDeveloperStatus = "incomplete"`

            - `const InitialItemDeveloperStatusCompleted InitialItemDeveloperStatus = "completed"`

          - `Type string`

            The history item type. Always `message`.

            - `const InitialItemDeveloperTypeMessage InitialItemDeveloperType = "message"`

        - `InitialItemUser`

          - `Content []InitialItemUserContent`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `Text string`

              The message text to include in the Live session’s initial conversation history.

            - `Type string`

              The text content type. Always `input_text`.

              - `const InitialItemUserContentTypeInputText InitialItemUserContentType = "input_text"`

          - `Role User`

            The author of this history message. Always `user`.

            - `const UserUser User = "user"`

          - `ID string`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Status string`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `const InitialItemUserStatusIncomplete InitialItemUserStatus = "incomplete"`

            - `const InitialItemUserStatusCompleted InitialItemUserStatus = "completed"`

          - `Type string`

            The history item type. Always `message`.

            - `const InitialItemUserTypeMessage InitialItemUserType = "message"`

        - `InitialItemAssistant`

          - `Content []InitialItemAssistantContentUnion`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `InitialItemAssistantContentText`

              - `Text string`

                The message text to include in the Live session’s initial conversation history.

              - `Type string`

                The text content type. Always `text`.

                - `const InitialItemAssistantContentTextTypeText InitialItemAssistantContentTextType = "text"`

            - `InitialItemAssistantContentOutputText`

              - `Text string`

                The message text to include in the Live session’s initial conversation history.

              - `Type OutputText`

                The text content type. Always `output_text`.

                - `const OutputTextOutputText OutputText = "output_text"`

          - `Role Assistant`

            The author of this history message. Always `assistant`.

            - `const AssistantAssistant Assistant = "assistant"`

          - `ID string`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Status string`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `const InitialItemAssistantStatusIncomplete InitialItemAssistantStatus = "incomplete"`

            - `const InitialItemAssistantStatusCompleted InitialItemAssistantStatus = "completed"`

          - `Type string`

            The history item type. Always `message`.

            - `const InitialItemAssistantTypeMessage InitialItemAssistantType = "message"`

      - `Instructions string`

        Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

      - `Store bool`

        Whether to store the session for later forking and recording download. Defaults to false for new sessions.

    - `Type SessionStarted`

      The event type, always `session.started`.

      - `const SessionStartedSessionStarted SessionStarted = "session.started"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type SessionUpdatedEvent struct{…}`

    Returned when a Live session update is accepted. Contains the resolved session configuration after the update.

    - `EventID string`

      The unique ID of the Live server event.

    - `Session SessionResource`

      The resolved Live session configuration and server-assigned session metadata.

    - `Type SessionUpdated`

      The event type, always `session.updated`.

      - `const SessionUpdatedSessionUpdated SessionUpdated = "session.updated"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type InputAudioMutedEvent struct{…}`

    Returned when a session.input_audio.mute command is accepted. Input audio is no longer sent to the model; sideband audio reflection continues.

    - `EventID string`

      The unique ID of the Live server event.

    - `Type SessionInputAudioMuted`

      The event type, always `session.input_audio.muted`.

      - `const SessionInputAudioMutedSessionInputAudioMuted SessionInputAudioMuted = "session.input_audio.muted"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type InputAudioUnmutedEvent struct{…}`

    Returned when a session.input_audio.unmute command is accepted. Input audio is sent to the model again.

    - `EventID string`

      The unique ID of the Live server event.

    - `Type SessionInputAudioUnmuted`

      The event type, always `session.input_audio.unmuted`.

      - `const SessionInputAudioUnmutedSessionInputAudioUnmuted SessionInputAudioUnmuted = "session.input_audio.unmuted"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type InstructionsAppendedEvent struct{…}`

    Returned when a session.instructions.append command is accepted into the Live session timeline. Acknowledges the appended instructions without guaranteeing that the model has acted on them.

    - `EndMs int64`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `EventID string`

      The unique ID of the Live server event.

    - `StartMs int64`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `Type SessionInstructionsAppended`

      The event type, always `session.instructions.appended`.

      - `const SessionInstructionsAppendedSessionInstructionsAppended SessionInstructionsAppended = "session.instructions.appended"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type ThinkingAppendedEvent struct{…}`

    Returned when a session.thinking.append command is accepted into the Live session timeline. Acknowledges the added reasoning context without guaranteeing any spoken output.

    - `EndMs int64`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `EventID string`

      The unique ID of the Live server event.

    - `StartMs int64`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `Type SessionThinkingAppended`

      The event type, always `session.thinking.appended`.

      - `const SessionThinkingAppendedSessionThinkingAppended SessionThinkingAppended = "session.thinking.appended"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type CommentaryAppendedEvent struct{…}`

    Returned when a session.commentary.append command is accepted into the Live session timeline. Acknowledges the added commentary without guaranteeing exact wording or completed audio playback.

    - `EndMs int64`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `EventID string`

      The unique ID of the Live server event.

    - `StartMs int64`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `Type SessionCommentaryAppended`

      The event type, always `session.commentary.appended`.

      - `const SessionCommentaryAppendedSessionCommentaryAppended SessionCommentaryAppended = "session.commentary.appended"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `ForkServerEventSessionInputAudioAppend`

    - `Audio string`

      Base64-encoded raw mono PCM16LE at 24 kHz received from the primary transport, reflected to the sideband before model-input muting. This server event uses the same audio key as the client command, but is not an acknowledgment of it.

    - `Type SessionInputAudioAppend`

      The event type, always `session.input_audio.append`.

      - `const SessionInputAudioAppendSessionInputAudioAppend SessionInputAudioAppend = "session.input_audio.append"`

  - `type OutputAudioDeltaEvent struct{…}`

    An audio chunk generated by the Live model. Decode and play primary WebSocket chunks in delivery order using the configured session audio format. Sideband connections receive reflected output audio with timestamps.

    - `Delta string`

      Base64-encoded raw audio. Primary WebSocket events use the session's configured format; reflected sideband events use mono PCM16LE at 24 kHz.

    - `Type SessionOutputAudioDelta`

      The event type, always `session.output_audio.delta`.

      - `const SessionOutputAudioDeltaSessionOutputAudioDelta SessionOutputAudioDelta = "session.output_audio.delta"`

    - `EndMs int64`

      Exclusive session-relative end in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket. Dropped output frames leave gaps between reflected ranges.

    - `StartMs int64`

      Inclusive session-relative start in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket.

  - `type InputTranscriptDeltaEvent struct{…}`

    A transcript fragment for user input audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

    - `Delta string`

      The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

    - `EndMs int64`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `EventID string`

      The unique ID of the Live server event.

    - `StartMs int64`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `Type SessionInputTranscriptDelta`

      The event type, always `session.input_transcript.delta`.

      - `const SessionInputTranscriptDeltaSessionInputTranscriptDelta SessionInputTranscriptDelta = "session.input_transcript.delta"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type OutputTranscriptDeltaEvent struct{…}`

    A transcript fragment for assistant output audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

    - `Delta string`

      The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

    - `EndMs int64`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `EventID string`

      The unique ID of the Live server event.

    - `StartMs int64`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `Type SessionOutputTranscriptDelta`

      The event type, always `session.output_transcript.delta`.

      - `const SessionOutputTranscriptDeltaSessionOutputTranscriptDelta SessionOutputTranscriptDelta = "session.output_transcript.delta"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type DelegationCreatedEvent struct{…}`

    Returned when the Live model delegates work to your application or a Responses backend. Contains delegation metadata and the position on the session timeline where the work was delegated.

    - `Delegation DelegationCreatedEventDelegation`

      The delegated work identifier and destination. This object contains metadata, not the task text.

      - `ID string`

        The unique ID of the delegation. Use this as delegation_id when replying to client-owned work or correlating Responses events.

      - `Target string`

        Where the Live model delegated the work: `client` for your application, or `responses` for the configured Responses backend.

        - `string`

          - `const DelegationCreatedEventDelegationTargetStringClient DelegationCreatedEventDelegationTargetString = "client"`

          - `const DelegationCreatedEventDelegationTargetStringResponses DelegationCreatedEventDelegationTargetString = "responses"`

      - `Type Delegation`

        The object type, always `delegation`.

        - `const DelegationDelegation Delegation = "delegation"`

      - `ResponseID string`

        The ID of the Responses API response associated with a Responses delegation. Omitted for client delegations.

    - `EventID string`

      The unique ID of the Live server event.

    - `OffsetMs int64`

      The position on the Live session timeline where the delegation was created, in milliseconds from the beginning of the session.

    - `Type SessionDelegationCreated`

      The event type, always `session.delegation.created`.

      - `const SessionDelegationCreatedSessionDelegationCreated SessionDelegationCreated = "session.delegation.created"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type ResponseEvent struct{…}`

    A streaming Responses API event from a backend delegated to by the Live session. Use the outer delegation_id to associate the nested stream with its Live delegation.

    - `Event map[string, any]`

      The nested Responses streaming event. Dispatch on its type field. Response lifecycle snapshots omit input and clear instructions, tools, and output to keep messages small; consume granular output events for the generated content.

    - `EventID string`

      The unique ID of the Live server event.

    - `Type ResponseEvent`

      The event type, always `response.event`.

      - `const ResponseEventResponseEvent ResponseEvent = "response.event"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

    - `DelegationID string`

      The Live delegation associated with the nested Responses event. May be null or omitted when the event cannot be correlated with a delegation.

  - `type SessionUsageUpdatedEvent struct{…}`

    Reports cumulative Live audio usage and, when available, the most recent context-window usage. Delegated Responses token usage is reported separately in response.event events.

    - `EventID string`

      The unique ID of the Live server event.

    - `Type SessionUsageUpdated`

      The event type, always `session.usage.updated`.

      - `const SessionUsageUpdatedSessionUsageUpdated SessionUsageUpdated = "session.usage.updated"`

    - `Usage SessionUsage`

      The cumulative Live audio usage so far.

      - `Seconds float64`

        The cumulative Live audio duration in seconds. Do not sum this value across usage events.

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

    - `ContextWindow SessionUsageUpdatedEventContextWindow`

      The latest measured Live context-window usage. Omitted when the context limit is unknown.

      - `UsageRatio float64`

        The latest active context token count divided by the Live model context limit. Can decrease after compaction and may lag between measured audio frames.

  - `type SessionClosedEvent struct{…}`

    Returned after the Live session finishes finalizing, with the close reason, final session snapshot, and cumulative audio usage. A connection closing without this event does not confirm successful finalization.

    - `EventID string`

      The unique ID of the Live server event.

    - `Reason SessionClosedEventReasonString`

      Why the Live session ended: `close_requested` for an application close or hangup request, `expired` for the session duration limit, `content` for a safety filter, `remote_hangup` for a graceful remote disconnect, or `connection_lost` for an unexpected primary or upstream disconnection.

      - `string`

        - `const SessionClosedEventReasonStringCloseRequested SessionClosedEventReasonString = "close_requested"`

        - `const SessionClosedEventReasonStringExpired SessionClosedEventReasonString = "expired"`

        - `const SessionClosedEventReasonStringContent SessionClosedEventReasonString = "content"`

        - `const SessionClosedEventReasonStringRemoteHangup SessionClosedEventReasonString = "remote_hangup"`

        - `const SessionClosedEventReasonStringConnectionLost SessionClosedEventReasonString = "connection_lost"`

    - `Session SessionResource`

      The resolved Live session configuration and server-assigned session metadata.

    - `Type SessionClosed`

      The event type, always `session.closed`.

      - `const SessionClosedSessionClosed SessionClosed = "session.closed"`

    - `Usage SessionUsage`

      The final cumulative Live audio usage after session finalization.

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type ErrorEvent struct{…}`

    Reports an error in the Live session, such as an invalid client command. Use error.client_event_id, when present, to identify the command that caused the error.

    - `Error Error`

      Details of the Live error and the client command that caused it, when known.

      - `Code string`

        A machine-readable code identifying the Live error, such as `unknown_parameter`.

      - `Message string`

        A human-readable explanation of the Live error.

      - `Type string`

        The category of error, such as `invalid_request_error` for an invalid Live client command.

      - `ClientEventID string`

        The event_id of the client command that caused the error, when supplied.

      - `Param string`

        The parameter that caused the error, when applicable, such as `session.voice`.

    - `EventID string`

      The unique ID of the Live server event.

    - `Type Error`

      The event type, always `error`.

      - `const ErrorError Error = "error"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `type InfoEvent struct{…}`

    An informational notice about the Live session, such as the event permissions applied to a frontend data channel.

    - `Code string`

      A machine-readable code for the notice, such as `data_channel_permissions`.

    - `EventID string`

      The unique ID of the Live server event.

    - `Message string`

      A human-readable explanation of the Live session notice.

    - `Type Info`

      The event type, always `info`.

      - `const InfoInfo Info = "info"`

    - `ClientEventID string`

      The event_id of the client command associated with this server event, when supplied.

  - `ForkServerEventTransportDtmfReceived`

    - `Event string`

    - `EventID string`

    - `Type TransportDtmfReceived`

      - `const TransportDtmfReceivedTransportDtmfReceived TransportDtmfReceived = "transport.dtmf.received"`

  - `ForkServerEventTransportDtmfSend`

    - `Event string`

    - `EventID string`

    - `Type TransportDtmfSend`

      - `const TransportDtmfSendTransportDtmfSend TransportDtmfSend = "transport.dtmf.send"`

    - `ClientEventID string`

      The event_id of the client command, when supplied.

  - `ForkServerEventTransportRinging`

    - `EventID string`

    - `SessionID string`

      The canonical Live session ID.

    - `Type TransportRinging`

      - `const TransportRingingTransportRinging TransportRinging = "transport.ringing"`

  - `ForkServerEventTransportAnswered`

    - `EventID string`

    - `SessionID string`

      The canonical Live session ID.

    - `Type TransportAnswered`

      - `const TransportAnsweredTransportAnswered TransportAnswered = "transport.answered"`

  - `ForkServerEventTransportFailed`

    - `Error ForkServerEventTransportFailedError`

      - `Code string`

        The call setup failure code.

      - `Message string`

      - `Type CallError`

        - `const CallErrorCallError CallError = "call_error"`

      - `Param string`

        The parameter related to the error, if any. Empty when no parameter applies.

    - `EventID string`

    - `SessionID string`

      The canonical Live session ID.

    - `Type TransportFailed`

      - `const TransportFailedTransportFailed TransportFailed = "transport.failed"`

# Sessions

## Accept call

`client.Live.Sessions.Accept(ctx, sessionID, body) error`

**post** `/live/sessions/{session_id}/accept`

Accept an incoming SIP call. Supply session with type live, the model, and startup configuration. Before accepting calls, follow the [Live prompting guide](/api/docs/guides/live-prompting) to write frontend conversation instructions and a separate backend prompt. SIP media format is negotiated; omit audio.format.

### Parameters

- `sessionID string`

- `body SessionAcceptParams`

  - `Session param.Field[SessionAcceptParamsSession]`

    Model and startup configuration for the Live session that answers the incoming SIP call.

    - `Model string`

      The Live model to use for the accepted call.

      - `string`

      - `type SessionAcceptParamsSessionModel string`

        The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

        - `const SessionAcceptParamsSessionModelGPTLive1 SessionAcceptParamsSessionModel = "gpt-live-1"`

    - `Type Live`

      The session type. Always `live`.

      - `const LiveLive Live = "live"`

    - `Audio SessionAcceptParamsSessionAudio`

      Startup audio output configuration. SIP negotiates the media format; audio.format is only accepted for primary WebSockets. Voice cannot change after startup.

      - `Output SessionAcceptParamsSessionAudioOutput`

        Settings for speech generated by the Live model. Choose the voice before starting the session.

        - `Voice SessionAcceptParamsSessionAudioOutputVoiceUnion`

          The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

          - `string`

          - `type BuiltInVoice string`

            A built-in voice available for Live speech.

            - `const BuiltInVoiceAlloy BuiltInVoice = "alloy"`

            - `const BuiltInVoiceAsh BuiltInVoice = "ash"`

            - `const BuiltInVoiceBallad BuiltInVoice = "ballad"`

            - `const BuiltInVoiceBeacon BuiltInVoice = "beacon"`

            - `const BuiltInVoiceBossa BuiltInVoice = "bossa"`

            - `const BuiltInVoiceCedar BuiltInVoice = "cedar"`

            - `const BuiltInVoiceCinder BuiltInVoice = "cinder"`

            - `const BuiltInVoiceCoral BuiltInVoice = "coral"`

            - `const BuiltInVoiceDelta BuiltInVoice = "delta"`

            - `const BuiltInVoiceEcho BuiltInVoice = "echo"`

            - `const BuiltInVoiceGleam BuiltInVoice = "gleam"`

            - `const BuiltInVoiceMarin BuiltInVoice = "marin"`

            - `const BuiltInVoiceMeridian BuiltInVoice = "meridian"`

            - `const BuiltInVoiceQuartz BuiltInVoice = "quartz"`

            - `const BuiltInVoiceRipple BuiltInVoice = "ripple"`

            - `const BuiltInVoiceSage BuiltInVoice = "sage"`

            - `const BuiltInVoiceShimmer BuiltInVoice = "shimmer"`

            - `const BuiltInVoiceStone BuiltInVoice = "stone"`

            - `const BuiltInVoiceTempo BuiltInVoice = "tempo"`

            - `const BuiltInVoiceVerse BuiltInVoice = "verse"`

            - `const BuiltInVoiceVesper BuiltInVoice = "vesper"`

            - `const BuiltInVoiceWillow BuiltInVoice = "willow"`

          - `type CustomVoice struct{…}`

            - `ID string`

    - `Delegation SessionAcceptParamsSessionDelegationUnion`

      Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

      - `type ClientDelegation struct{…}`

        Delegate tasks to your application. The Live session emits delegation events that your backend handles.

        - `Type Client`

          The delegation owner. Always `client` for tasks handled by your application.

          - `const ClientClient Client = "client"`

      - `type SessionAcceptParamsSessionDelegationResponses struct{…}`

        Delegate tasks to a Responses model managed by the Live session.

        - `Responses ResponsesDelegationConfig`

          Backend model, prompt, and tools used when the Live session delegates a task to Responses.

          - `Model string`

            The model used for server-owned Responses delegations.

          - `Instructions string`

            Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

          - `MaxOutputTokens int64`

            Maximum number of output tokens for each delegated response.

          - `ParallelToolCalls bool`

            Whether the delegated Responses model may request multiple tool calls in a single response.

          - `Reasoning ResponsesDelegationConfigReasoning`

            Reasoning settings passed to each delegated Responses request.

            - `Effort string`

              How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

              - `const ResponsesDelegationConfigReasoningEffortNone ResponsesDelegationConfigReasoningEffort = "none"`

              - `const ResponsesDelegationConfigReasoningEffortMinimal ResponsesDelegationConfigReasoningEffort = "minimal"`

              - `const ResponsesDelegationConfigReasoningEffortLow ResponsesDelegationConfigReasoningEffort = "low"`

              - `const ResponsesDelegationConfigReasoningEffortMedium ResponsesDelegationConfigReasoningEffort = "medium"`

              - `const ResponsesDelegationConfigReasoningEffortHigh ResponsesDelegationConfigReasoningEffort = "high"`

              - `const ResponsesDelegationConfigReasoningEffortXhigh ResponsesDelegationConfigReasoningEffort = "xhigh"`

            - `Summary string`

              The reasoning summary to request from the delegated Responses model, when supported.

              - `const ResponsesDelegationConfigReasoningSummaryConcise ResponsesDelegationConfigReasoningSummary = "concise"`

              - `const ResponsesDelegationConfigReasoningSummaryDetailed ResponsesDelegationConfigReasoningSummary = "detailed"`

              - `const ResponsesDelegationConfigReasoningSummaryAuto ResponsesDelegationConfigReasoningSummary = "auto"`

          - `ServiceTier ResponsesDelegationConfigServiceTier`

            Service tier for delegated Responses requests.

            - `const ResponsesDelegationConfigServiceTierAuto ResponsesDelegationConfigServiceTier = "auto"`

            - `const ResponsesDelegationConfigServiceTierDefault ResponsesDelegationConfigServiceTier = "default"`

            - `const ResponsesDelegationConfigServiceTierFastTierTempPilot ResponsesDelegationConfigServiceTier = "fast_tier_temp_pilot"`

            - `const ResponsesDelegationConfigServiceTierFlex ResponsesDelegationConfigServiceTier = "flex"`

            - `const ResponsesDelegationConfigServiceTierPriority ResponsesDelegationConfigServiceTier = "priority"`

            - `const ResponsesDelegationConfigServiceTierUltrafast ResponsesDelegationConfigServiceTier = "ultrafast"`

          - `Text ResponsesDelegationConfigText`

            Text generation settings passed to each delegated Responses request.

            - `Verbosity string`

              The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

              - `const ResponsesDelegationConfigTextVerbosityLow ResponsesDelegationConfigTextVerbosity = "low"`

              - `const ResponsesDelegationConfigTextVerbosityMedium ResponsesDelegationConfigTextVerbosity = "medium"`

              - `const ResponsesDelegationConfigTextVerbosityHigh ResponsesDelegationConfigTextVerbosity = "high"`

          - `ToolChoice ResponsesDelegationConfigToolChoiceUnion`

            Controls which tool the Responses backend uses when handling a task delegated by the Live model.

            - `string`

              - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumAuto ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "auto"`

              - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumNone ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "none"`

              - `const ResponsesDelegationConfigToolChoiceLiveToolChoiceEnumRequired ResponsesDelegationConfigToolChoiceLiveToolChoiceEnum = "required"`

            - `ResponsesDelegationConfigToolChoiceLiveFunctionToolChoiceParam`

              - `Name string`

              - `Type Function`

                - `const FunctionFunction Function = "function"`

            - `ResponsesDelegationConfigToolChoiceLiveMcpToolChoiceParam`

              - `Name string`

              - `ServerLabel string`

              - `Type Mcp`

                - `const McpMcp Mcp = "mcp"`

          - `Tools []ResponsesDelegationConfigToolUnion`

            Tools available to the Responses backend while it handles tasks delegated by the Live model.

            - `type FunctionTool struct{…}`

              A function tool available to the Responses backend when the Live model delegates a task.

              - `Name string`

                The name the delegated Responses model uses when calling this function.

              - `Type Function`

                The tool type. Always `function`.

                - `const FunctionFunction Function = "function"`

              - `Description string`

                What the function does and when the delegated Responses model should call it.

              - `Parameters map[string, any]`

                A JSON Schema object describing the arguments accepted by the function.

              - `Strict bool`

                Whether the delegated Responses model must follow the function’s parameter schema exactly.

            - `ResponsesDelegationConfigToolWebSearch`

              - `Type WebSearch`

                The tool type. Always `web_search`.

                - `const WebSearchWebSearch WebSearch = "web_search"`

        - `Type Responses`

          The delegation owner. Always `responses` for tasks handled by the Responses API.

          - `const ResponsesResponses Responses = "responses"`

    - `Input []InitialItemUnion`

      Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

      - `InitialItemDeveloper`

        - `Content []InitialItemDeveloperContent`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `Text string`

            The message text to include in the Live session’s initial conversation history.

          - `Type string`

            The text content type. Always `input_text`.

            - `const InitialItemDeveloperContentTypeInputText InitialItemDeveloperContentType = "input_text"`

        - `Role Developer`

          The author of this history message. Always `developer`.

          - `const DeveloperDeveloper Developer = "developer"`

        - `ID string`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Status string`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `const InitialItemDeveloperStatusIncomplete InitialItemDeveloperStatus = "incomplete"`

          - `const InitialItemDeveloperStatusCompleted InitialItemDeveloperStatus = "completed"`

        - `Type string`

          The history item type. Always `message`.

          - `const InitialItemDeveloperTypeMessage InitialItemDeveloperType = "message"`

      - `InitialItemUser`

        - `Content []InitialItemUserContent`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `Text string`

            The message text to include in the Live session’s initial conversation history.

          - `Type string`

            The text content type. Always `input_text`.

            - `const InitialItemUserContentTypeInputText InitialItemUserContentType = "input_text"`

        - `Role User`

          The author of this history message. Always `user`.

          - `const UserUser User = "user"`

        - `ID string`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Status string`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `const InitialItemUserStatusIncomplete InitialItemUserStatus = "incomplete"`

          - `const InitialItemUserStatusCompleted InitialItemUserStatus = "completed"`

        - `Type string`

          The history item type. Always `message`.

          - `const InitialItemUserTypeMessage InitialItemUserType = "message"`

      - `InitialItemAssistant`

        - `Content []InitialItemAssistantContentUnion`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `InitialItemAssistantContentText`

            - `Text string`

              The message text to include in the Live session’s initial conversation history.

            - `Type string`

              The text content type. Always `text`.

              - `const InitialItemAssistantContentTextTypeText InitialItemAssistantContentTextType = "text"`

          - `InitialItemAssistantContentOutputText`

            - `Text string`

              The message text to include in the Live session’s initial conversation history.

            - `Type OutputText`

              The text content type. Always `output_text`.

              - `const OutputTextOutputText OutputText = "output_text"`

        - `Role Assistant`

          The author of this history message. Always `assistant`.

          - `const AssistantAssistant Assistant = "assistant"`

        - `ID string`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Status string`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `const InitialItemAssistantStatusIncomplete InitialItemAssistantStatus = "incomplete"`

          - `const InitialItemAssistantStatusCompleted InitialItemAssistantStatus = "completed"`

        - `Type string`

          The history item type. Always `message`.

          - `const InitialItemAssistantTypeMessage InitialItemAssistantType = "message"`

    - `Instructions string`

      Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

    - `Store bool`

      Whether to store the session for later forking and recording download. Defaults to false for new sessions.

### Example

```go
package main

import (
  "context"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/live"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  err := client.Live.Sessions.Accept(
    context.TODO(),
    "session_id",
    live.SessionAcceptParams{
      Session: live.SessionAcceptParamsSession{
        Model: "gpt-live-1",
        Type: live.LiveLive,
      },
    },
  )
  if err != nil {
    panic(err.Error())
  }
}
```

## Download recording

`client.Live.Sessions.DownloadRecording(ctx, sessionID) (*Response, error)`

**get** `/live/sessions/{session_id}/content`

Get Live session content

### Parameters

- `sessionID string`

  The ID of the stored Live session to download. Use the session ID returned when the session started with storage enabled.

### Returns

- `type SessionDownloadRecordingResponse interface{…}`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  response, err := client.Live.Sessions.DownloadRecording(context.TODO(), "live_SQ")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response)
}
```

## Fork session

`client.Live.Sessions.Fork(ctx, sessionID, body) (*SessionForkResponse, error)`

**post** `/live/sessions/{session_id}/fork`

Fork a stored Live session onto a new WebRTC connection.

### Parameters

- `sessionID string`

- `body SessionForkParams`

  - `Transport param.Field[SessionForkParamsTransport]`

    WebRTC transport with an SDP offer for the new connection to the forked session.

    - `Sdp string`

      Session Description Protocol message for the WebRTC connection.

    - `Type Webrtc`

      The transport used for the Live session. Always `webrtc`.

      - `const WebrtcWebrtc Webrtc = "webrtc"`

  - `Session param.Field[MediaSessionForkConfig]`

    Optional configuration overrides for the new Live session. Omit this object or send an empty object to inherit the stored session's settings.

### Returns

- `type SessionForkResponse struct{…}`

  The created Live session identifier and WebRTC answer. Apply transport.sdp as the peer's remote answer and wait for session.started on the data channel before sending commands.

  - `Session SessionForkResponseSession`

    The newly created Live session. Use its ID for session controls and sideband connections.

    - `ID string`

      Opaque session identifier. Preserve the returned value unchanged, including its prefix.

  - `Transport SessionForkResponseTransport`

    WebRTC transport with the SDP answer.

    - `Sdp string`

      Session Description Protocol message for the WebRTC connection.

    - `Type Webrtc`

      The transport used for the Live session. Always `webrtc`.

      - `const WebrtcWebrtc Webrtc = "webrtc"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/live"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  response, err := client.Live.Sessions.Fork(
    context.TODO(),
    "session_id",
    live.SessionForkParams{
      Transport: live.SessionForkParamsTransport{
        Sdp: "x",
      },
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.Session)
}
```

#### Response

```json
{
  "session": {
    "id": "id"
  },
  "transport": {
    "sdp": "x",
    "type": "webrtc"
  }
}
```

## Hang up session

`client.Live.Sessions.Hangup(ctx, sessionID) error`

**post** `/live/sessions/{session_id}/hangup`

End a SIP call identified by session_id.

### Parameters

- `sessionID string`

### Example

```go
package main

import (
  "context"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  err := client.Live.Sessions.Hangup(context.TODO(), "session_id")
  if err != nil {
    panic(err.Error())
  }
}
```

## Transfer call

`client.Live.Sessions.Refer(ctx, sessionID, body) error`

**post** `/live/sessions/{session_id}/refer`

Transfer a SIP call to another destination. Supply a nonblank target_uri for the SIP Refer-To header.

### Parameters

- `sessionID string`

- `body SessionReferParams`

  - `TargetUri param.Field[string]`

    Nonblank URI for the SIP Refer-To header, such as tel:+14155550123 or sip:agent@example.com.

### Example

```go
package main

import (
  "context"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/live"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  err := client.Live.Sessions.Refer(
    context.TODO(),
    "session_id",
    live.SessionReferParams{
      TargetUri: "tel:+14155550123",
    },
  )
  if err != nil {
    panic(err.Error())
  }
}
```

## Reject call

`client.Live.Sessions.Reject(ctx, sessionID, body) error`

**post** `/live/sessions/{session_id}/reject`

Reject an incoming SIP call. Send a required SIP rejection status_code between 300 and 699.

### Parameters

- `sessionID string`

- `body SessionRejectParams`

  - `StatusCode param.Field[int64]`

    SIP rejection status sent to the caller. This field is required.

### Example

```go
package main

import (
  "context"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/live"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  err := client.Live.Sessions.Reject(
    context.TODO(),
    "session_id",
    live.SessionRejectParams{
      StatusCode: 486,
    },
  )
  if err != nil {
    panic(err.Error())
  }
}
```

# Sideband

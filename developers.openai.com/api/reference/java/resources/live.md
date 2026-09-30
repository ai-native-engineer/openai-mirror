<!-- source: https://developers.openai.com/api/reference/java/resources/live/ -->

# Live

## Create session

`LiveCreateResponse live().create(LiveCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/live/sessions`

Create a Live WebRTC session. Start with the [Live prompting guide](/api/docs/guides/live-prompting).

### Parameters

- `LiveCreateParams params`

  - `MediaSessionConfig session`

    Startup configuration for the Live session.

  - `Transport transport`

    WebRTC transport with the browser's SDP offer.

    - `String sdp`

      Session Description Protocol message for the WebRTC connection.

    - `JsonValue; type "webrtc"constant`

      The transport used for the Live session. Always `webrtc`.

      - `WEBRTC("webrtc")`

### Returns

- `class LiveCreateResponse:`

  The created Live session identifier and WebRTC answer. Apply transport.sdp as the peer's remote answer and wait for session.started on the data channel before sending commands.

  - `Session session`

    The newly created Live session. Use its ID for session controls and sideband connections.

    - `String id`

      Opaque session identifier. Preserve the returned value unchanged, including its prefix.

  - `Transport transport`

    WebRTC transport with the SDP answer.

    - `String sdp`

      Session Description Protocol message for the WebRTC connection.

    - `JsonValue; type "webrtc"constant`

      The transport used for the Live session. Always `webrtc`.

      - `WEBRTC("webrtc")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.live.LiveCreateParams;
import com.openai.models.live.LiveCreateResponse;
import com.openai.models.live.MediaSessionConfig;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        LiveCreateParams params = LiveCreateParams.builder()
            .session(MediaSessionConfig.builder()
                .model(MediaSessionConfig.Model.GPT_LIVE_1)
                .build())
            .transport(LiveCreateParams.Transport.builder()
                .sdp("x")
                .build())
            .build();
        LiveCreateResponse live = client.live().create(params);
    }
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

- `class AudioFormat: A class that can be one of several variants.union`

  Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

  - `AudioPcm`

    - `Rate rate`

      Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

      - `_16000(16000)`

      - `_24000(24000)`

    - `JsonValue; type "audio/pcm"constant`

      The audio encoding. Always `audio/pcm`.

      - `AUDIO_PCM("audio/pcm")`

  - `AudioPcmu`

    - `long rate`

      Audio sample rate in hertz. G.711 audio uses 8000 Hz.

    - `JsonValue; type "audio/pcmu"constant`

      The audio encoding. Always `audio/pcmu`.

      - `AUDIO_PCMU("audio/pcmu")`

  - `AudioPcma`

    - `long rate`

      Audio sample rate in hertz. G.711 audio uses 8000 Hz.

    - `JsonValue; type "audio/pcma"constant`

      The audio encoding. Always `audio/pcma`.

      - `AUDIO_PCMA("audio/pcma")`

### Built In Voice

- `enum BuiltInVoice:`

  A built-in voice available for Live speech.

  - `ALLOY("alloy")`

  - `ASH("ash")`

  - `BALLAD("ballad")`

  - `BEACON("beacon")`

  - `BOSSA("bossa")`

  - `CEDAR("cedar")`

  - `CINDER("cinder")`

  - `CORAL("coral")`

  - `DELTA("delta")`

  - `ECHO("echo")`

  - `GLEAM("gleam")`

  - `MARIN("marin")`

  - `MERIDIAN("meridian")`

  - `QUARTZ("quartz")`

  - `RIPPLE("ripple")`

  - `SAGE("sage")`

  - `SHIMMER("shimmer")`

  - `STONE("stone")`

  - `TEMPO("tempo")`

  - `VERSE("verse")`

  - `VESPER("vesper")`

  - `WILLOW("willow")`

### Client Config

- `class ClientConfig:`

  Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

  - `DataChannelConfig dataChannel`

    Client and server event permissions for the WebRTC frontend data channel.

    - `Optional<AllowedClientEvents> allowedClientEvents`

      Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

      - `JsonValue;`

        - `ALL("all")`

      - `List<String>`

    - `Optional<AllowedServerEvents> allowedServerEvents`

      Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

      - `JsonValue;`

        - `ALL("all")`

      - `List<ServerEventSelector>`

        - `String type`

          The outer Live server event type. Use 'response.event' for Responses events.

        - `Optional<String> responseEvent`

          The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

### Client Delegation

- `class ClientDelegation:`

  Delegate tasks to your application. The Live session emits delegation events that your backend handles.

  - `JsonValue; type "client"constant`

    The delegation owner. Always `client` for tasks handled by your application.

    - `CLIENT("client")`

### Client Event

- `class ClientEvent: A class that can be one of several variants.union`

  Client events for Live. Initialize a primary WebSocket with session.start and wait for session.started. WebRTC creation already starts the session. Audio append is primary WebSocket-only. See the [Live prompting guide](https://developers.openai.com/api/docs/guides/live-prompting) before writing frontend instructions and delegation policies.

  - `class SessionStartEvent:`

    Start a Live session on a primary WebSocket. Send this event before other commands and wait for `session.started`.

    - `SessionConfig session`

      Initial configuration for a primary WebSocket. Send session.start first and wait for session.started before application commands. WebRTC creation already starts the session; do not send this event again on its data channel.

      - `Model model`

        The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

        - `GPT_LIVE_1("gpt-live-1")`

      - `Optional<Audio> audio`

        Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

        - `Optional<AudioFormat> format`

          Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

          - `AudioPcm`

            - `Rate rate`

              Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

              - `_16000(16000)`

              - `_24000(24000)`

            - `JsonValue; type "audio/pcm"constant`

              The audio encoding. Always `audio/pcm`.

              - `AUDIO_PCM("audio/pcm")`

          - `AudioPcmu`

            - `long rate`

              Audio sample rate in hertz. G.711 audio uses 8000 Hz.

            - `JsonValue; type "audio/pcmu"constant`

              The audio encoding. Always `audio/pcmu`.

              - `AUDIO_PCMU("audio/pcmu")`

          - `AudioPcma`

            - `long rate`

              Audio sample rate in hertz. G.711 audio uses 8000 Hz.

            - `JsonValue; type "audio/pcma"constant`

              The audio encoding. Always `audio/pcma`.

              - `AUDIO_PCMA("audio/pcma")`

        - `Optional<Output> output`

          The voice used for speech generated by the Live model.

          - `Optional<Voice> voice`

            The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

            - `String`

            - `enum BuiltInVoice:`

              A built-in voice available for Live speech.

              - `ALLOY("alloy")`

              - `ASH("ash")`

              - `BALLAD("ballad")`

              - `BEACON("beacon")`

              - `BOSSA("bossa")`

              - `CEDAR("cedar")`

              - `CINDER("cinder")`

              - `CORAL("coral")`

              - `DELTA("delta")`

              - `ECHO("echo")`

              - `GLEAM("gleam")`

              - `MARIN("marin")`

              - `MERIDIAN("meridian")`

              - `QUARTZ("quartz")`

              - `RIPPLE("ripple")`

              - `SAGE("sage")`

              - `SHIMMER("shimmer")`

              - `STONE("stone")`

              - `TEMPO("tempo")`

              - `VERSE("verse")`

              - `VESPER("vesper")`

              - `WILLOW("willow")`

            - `class CustomVoice:`

              - `String id`

      - `Optional<ClientConfig> client`

        Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

        - `DataChannelConfig dataChannel`

          Client and server event permissions for the WebRTC frontend data channel.

          - `Optional<AllowedClientEvents> allowedClientEvents`

            Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

            - `JsonValue;`

              - `ALL("all")`

            - `List<String>`

          - `Optional<AllowedServerEvents> allowedServerEvents`

            Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

            - `JsonValue;`

              - `ALL("all")`

            - `List<ServerEventSelector>`

              - `String type`

                The outer Live server event type. Use 'response.event' for Responses events.

              - `Optional<String> responseEvent`

                The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

      - `Optional<Delegation> delegation`

        Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

        - `class ClientDelegation:`

          Delegate tasks to your application. The Live session emits delegation events that your backend handles.

          - `JsonValue; type "client"constant`

            The delegation owner. Always `client` for tasks handled by your application.

            - `CLIENT("client")`

        - `class Responses:`

          Delegate tasks to a Responses model managed by the Live session.

          - `ResponsesDelegationConfig responses`

            Backend model, prompt, and tools used when the Live session delegates a task to Responses.

            - `String model`

              The model used for server-owned Responses delegations.

            - `Optional<String> instructions`

              Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

            - `Optional<Long> maxOutputTokens`

              Maximum number of output tokens for each delegated response.

            - `Optional<Boolean> parallelToolCalls`

              Whether the delegated Responses model may request multiple tool calls in a single response.

            - `Optional<Reasoning> reasoning`

              Reasoning settings passed to each delegated Responses request.

              - `Optional<Effort> effort`

                How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

                - `NONE("none")`

                - `MINIMAL("minimal")`

                - `LOW("low")`

                - `MEDIUM("medium")`

                - `HIGH("high")`

                - `XHIGH("xhigh")`

              - `Optional<Summary> summary`

                The reasoning summary to request from the delegated Responses model, when supported.

                - `CONCISE("concise")`

                - `DETAILED("detailed")`

                - `AUTO("auto")`

            - `Optional<ServiceTier> serviceTier`

              Service tier for delegated Responses requests.

              - `AUTO("auto")`

              - `DEFAULT("default")`

              - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

              - `FLEX("flex")`

              - `PRIORITY("priority")`

              - `ULTRAFAST("ultrafast")`

            - `Optional<Text> text`

              Text generation settings passed to each delegated Responses request.

              - `Optional<Verbosity> verbosity`

                The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

                - `LOW("low")`

                - `MEDIUM("medium")`

                - `HIGH("high")`

            - `Optional<ToolChoice> toolChoice`

              Controls which tool the Responses backend uses when handling a task delegated by the Live model.

              - `enum LiveToolChoiceEnum:`

                - `AUTO("auto")`

                - `NONE("none")`

                - `REQUIRED("required")`

              - `class LiveFunctionToolChoiceParam:`

                - `String name`

                - `JsonValue; type "function"constant`

                  - `FUNCTION("function")`

              - `class LiveMcpToolChoiceParam:`

                - `String name`

                - `String serverLabel`

                - `JsonValue; type "mcp"constant`

                  - `MCP("mcp")`

            - `Optional<List<Tool>> tools`

              Tools available to the Responses backend while it handles tasks delegated by the Live model.

              - `class FunctionTool:`

                A function tool available to the Responses backend when the Live model delegates a task.

                - `String name`

                  The name the delegated Responses model uses when calling this function.

                - `JsonValue; type "function"constant`

                  The tool type. Always `function`.

                  - `FUNCTION("function")`

                - `Optional<String> description`

                  What the function does and when the delegated Responses model should call it.

                - `Optional<Parameters> parameters`

                  A JSON Schema object describing the arguments accepted by the function.

                - `Optional<Boolean> strict`

                  Whether the delegated Responses model must follow the function’s parameter schema exactly.

              - `JsonValue;`

                - `JsonValue; type "web_search"constant`

                  The tool type. Always `web_search`.

                  - `WEB_SEARCH("web_search")`

          - `JsonValue; type "responses"constant`

            The delegation owner. Always `responses` for tasks handled by the Responses API.

            - `RESPONSES("responses")`

      - `Optional<List<InitialItem>> input`

        Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

        - `Developer`

          - `List<Content> content`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `String text`

              The message text to include in the Live session’s initial conversation history.

            - `Optional<Type> type`

              The text content type. Always `input_text`.

              - `INPUT_TEXT("input_text")`

          - `JsonValue; role "developer"constant`

            The author of this history message. Always `developer`.

            - `DEVELOPER("developer")`

          - `Optional<String> id`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Optional<Status> status`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `INCOMPLETE("incomplete")`

            - `COMPLETED("completed")`

          - `Optional<Type> type`

            The history item type. Always `message`.

            - `MESSAGE("message")`

        - `User`

          - `List<Content> content`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `String text`

              The message text to include in the Live session’s initial conversation history.

            - `Optional<Type> type`

              The text content type. Always `input_text`.

              - `INPUT_TEXT("input_text")`

          - `JsonValue; role "user"constant`

            The author of this history message. Always `user`.

            - `USER("user")`

          - `Optional<String> id`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Optional<Status> status`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `INCOMPLETE("incomplete")`

            - `COMPLETED("completed")`

          - `Optional<Type> type`

            The history item type. Always `message`.

            - `MESSAGE("message")`

        - `Assistant`

          - `List<Content> content`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `class Text:`

              Assistant text supplied as conversation history when starting a Live session.

              - `String text`

                The message text to include in the Live session’s initial conversation history.

              - `Optional<Type> type`

                The text content type. Always `text`.

                - `TEXT("text")`

            - `class OutputText:`

              Assistant output text supplied as conversation history when starting a Live session.

              - `String text`

                The message text to include in the Live session’s initial conversation history.

              - `JsonValue; type "output_text"constant`

                The text content type. Always `output_text`.

                - `OUTPUT_TEXT("output_text")`

          - `JsonValue; role "assistant"constant`

            The author of this history message. Always `assistant`.

            - `ASSISTANT("assistant")`

          - `Optional<String> id`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Optional<Status> status`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `INCOMPLETE("incomplete")`

            - `COMPLETED("completed")`

          - `Optional<Type> type`

            The history item type. Always `message`.

            - `MESSAGE("message")`

      - `Optional<String> instructions`

        Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

      - `Optional<Boolean> store`

        Whether to store the session for later forking and recording download. Defaults to false for new sessions.

    - `JsonValue; type "session.start"constant`

      The Live client event type. Always `session.start`.

      - `SESSION_START("session.start")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class SessionUpdateEvent:`

    Update the delegation settings of an active Live session. The server acknowledges accepted changes with `session.updated`.

    - `SessionUpdateConfig session`

      Sparse delegation updates. Omitted settings retain their values. The delegation type cannot change, including resetting Responses delegation to null or client. Model, frontend instructions, audio, and startup input are immutable.

      - `Optional<Delegation> delegation`

        Delegation settings to update. The delegation type must match the current session; omitted settings retain their values.

        - `class ClientDelegation:`

          Delegate tasks to your application. The Live session emits delegation events that your backend handles.

        - `class Responses:`

          Update the Responses backend for an existing Live session without changing delegation ownership.

          - `JsonValue; type "responses"constant`

            The delegation owner. Always `responses` for tasks handled by the Responses API.

            - `RESPONSES("responses")`

          - `Optional<ResponsesDelegationUpdateConfig> responses`

            Responses backend settings to update. Omitted settings keep their existing values.

            - `Optional<String> instructions`

              Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

            - `Optional<Long> maxOutputTokens`

              Maximum number of output tokens for each delegated response.

            - `Optional<String> model`

              The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.

            - `Optional<Boolean> parallelToolCalls`

              Whether the delegated Responses model may request multiple tool calls in a single response.

            - `Optional<Reasoning> reasoning`

              Reasoning settings passed to each delegated Responses request.

              - `Optional<Effort> effort`

                How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

                - `NONE("none")`

                - `MINIMAL("minimal")`

                - `LOW("low")`

                - `MEDIUM("medium")`

                - `HIGH("high")`

                - `XHIGH("xhigh")`

              - `Optional<Summary> summary`

                The reasoning summary to request from the delegated Responses model, when supported.

                - `CONCISE("concise")`

                - `DETAILED("detailed")`

                - `AUTO("auto")`

            - `Optional<ServiceTier> serviceTier`

              Service tier for delegated Responses requests.

              - `AUTO("auto")`

              - `DEFAULT("default")`

              - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

              - `FLEX("flex")`

              - `PRIORITY("priority")`

              - `ULTRAFAST("ultrafast")`

            - `Optional<Text> text`

              Text generation settings passed to each delegated Responses request.

              - `Optional<Verbosity> verbosity`

                The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

                - `LOW("low")`

                - `MEDIUM("medium")`

                - `HIGH("high")`

            - `Optional<ToolChoice> toolChoice`

              Controls which tool the Responses backend uses when handling a task delegated by the Live model.

              - `enum LiveToolChoiceEnum:`

                - `AUTO("auto")`

                - `NONE("none")`

                - `REQUIRED("required")`

              - `class LiveFunctionToolChoiceParam:`

                - `String name`

                - `JsonValue; type "function"constant`

                  - `FUNCTION("function")`

              - `class LiveMcpToolChoiceParam:`

                - `String name`

                - `String serverLabel`

                - `JsonValue; type "mcp"constant`

                  - `MCP("mcp")`

            - `Optional<List<Tool>> tools`

              Tools available to the Responses backend while it handles tasks delegated by the Live model.

              - `class FunctionTool:`

                A function tool available to the Responses backend when the Live model delegates a task.

              - `JsonValue;`

                - `JsonValue; type "web_search"constant`

                  The tool type. Always `web_search`.

                  - `WEB_SEARCH("web_search")`

    - `JsonValue; type "session.update"constant`

      The Live client event type. Always `session.update`.

      - `SESSION_UPDATE("session.update")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class InputAudioAppendEvent:`

    Send audio to a Live session over its primary WebSocket. WebRTC and SIP sessions send audio over their media transport.

    - `String audio`

      Base64-encoded raw audio in the startup-selected format, without a WAV or other container header. Primary WebSocket only; media transports use their audio track. Audio appends have no acknowledgment. Reflected sideband server events reuse this event type and audio key, with no timestamps or event_id; their audio is always mono PCM16LE at 24 kHz.

    - `JsonValue; type "session.input_audio.append"constant`

      The Live client event type. Always `session.input_audio.append`.

      - `SESSION_INPUT_AUDIO_APPEND("session.input_audio.append")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class InputAudioMuteEvent:`

    Mute audio input to the Live model without closing the session. The server acknowledges with `session.input_audio.muted`.

    - `JsonValue; type "session.input_audio.mute"constant`

      The Live client event type. Always `session.input_audio.mute`.

      - `SESSION_INPUT_AUDIO_MUTE("session.input_audio.mute")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class InputAudioUnmuteEvent:`

    Resume audio input to a Live model after muting it. The server acknowledges with `session.input_audio.unmuted`.

    - `JsonValue; type "session.input_audio.unmute"constant`

      The Live client event type. Always `session.input_audio.unmute`.

      - `SESSION_INPUT_AUDIO_UNMUTE("session.input_audio.unmute")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class InstructionsAppendEvent:`

    Append instructions to the Live conversation while it is running, optionally associating them with an existing client delegation.

    - `String content`

      Instruction text to append, limited to 500 tokens. This is a plain string, not an array of content parts.

    - `Optional<String> delegationId`

      Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

    - `JsonValue; type "session.instructions.append"constant`

      The Live client event type. Always `session.instructions.append`.

      - `SESSION_INSTRUCTIONS_APPEND("session.instructions.append")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class ThinkingAppendEvent:`

    Provide silent reasoning or progress context to the Live model, optionally for an existing client delegation.

    - `String content`

      Silent reasoning or progress context, limited to 500 tokens. It does not directly request speech, but can influence later speech and is not a secrecy boundary.

    - `Optional<String> delegationId`

      Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

    - `JsonValue; type "session.thinking.append"constant`

      The Live client event type. Always `session.thinking.append`.

      - `SESSION_THINKING_APPEND("session.thinking.append")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class CommentaryAppendEvent:`

    Provide context the Live model can communicate to the user, optionally for an existing client delegation.

    - `String content`

      Speakable context for the Live model, limited to 500 tokens. Use this for a result the model should communicate; use session.thinking.append for silent context.

    - `Optional<String> delegationId`

      Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

    - `JsonValue; type "session.commentary.append"constant`

      The Live client event type. Always `session.commentary.append`.

      - `SESSION_COMMENTARY_APPEND("session.commentary.append")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class ResponseItemCreateEvent:`

    Add an input item to the Live session’s Responses backend. Requires Responses delegation; use `response.create` to request a response.

    - `ResponseInputItem item`

      An input item to append to the Responses backend conversation, such as a user message or a function tool result.

      - `class EasyInputMessage:`

        A message input to the model with a role indicating instruction following
        hierarchy. Instructions given with the `developer` or `system` role take
        precedence over instructions given with the `user` role. Messages with the
        `assistant` role are presumed to have been generated by the model in previous
        interactions.

        - `Content content`

          Text, image, or audio input to the model, used to generate a response.
          Can also contain previous assistant responses.

          - `String`

          - `List<ResponseInputContent>`

            - `class ResponseInputText:`

              A text input to the model.

              - `String text`

                The text input to the model.

              - `JsonValue; type "input_text"constant`

                The type of the input item. Always `input_text`.

                - `INPUT_TEXT("input_text")`

              - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `JsonValue; mode "explicit"constant`

                  The breakpoint mode. Always `explicit`.

                  - `EXPLICIT("explicit")`

            - `class ResponseInputImage:`

              An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

              - `Detail detail`

                The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                - `LOW("low")`

                - `HIGH("high")`

                - `AUTO("auto")`

                - `ORIGINAL("original")`

              - `JsonValue; type "input_image"constant`

                The type of the input item. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

              - `Optional<String> fileId`

                The ID of the file to be sent to the model.

              - `Optional<String> imageUrl`

                The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

              - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `JsonValue; mode "explicit"constant`

                  The breakpoint mode. Always `explicit`.

                  - `EXPLICIT("explicit")`

            - `class ResponseInputFile:`

              A file input to the model.

              - `JsonValue; type "input_file"constant`

                The type of the input item. Always `input_file`.

                - `INPUT_FILE("input_file")`

              - `Optional<Detail> detail`

                The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

                - `AUTO("auto")`

                - `LOW("low")`

                - `HIGH("high")`

              - `Optional<String> fileData`

                The content of the file to be sent to the model.

              - `Optional<String> fileId`

                The ID of the file to be sent to the model.

              - `Optional<String> fileUrl`

                The URL of the file to be sent to the model.

              - `Optional<String> filename`

                The name of the file to be sent to the model.

              - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `JsonValue; mode "explicit"constant`

                  The breakpoint mode. Always `explicit`.

                  - `EXPLICIT("explicit")`

        - `Role role`

          The role of the message input. One of `user`, `assistant`, `system`, or
          `developer`.

          - `USER("user")`

          - `ASSISTANT("assistant")`

          - `SYSTEM("system")`

          - `DEVELOPER("developer")`

        - `Optional<Phase> phase`

          Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
          For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
          phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

          - `COMMENTARY("commentary")`

          - `FINAL_ANSWER("final_answer")`

        - `Optional<Type> type`

          The type of the message input. Always `message`.

          - `MESSAGE("message")`

      - `Message`

        - `List<ResponseInputContent> content`

          A list of one or many input items to the model, containing different content
          types.

          - `class ResponseInputText:`

            A text input to the model.

          - `class ResponseInputImage:`

            An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

          - `class ResponseInputFile:`

            A file input to the model.

        - `Role role`

          The role of the message input. One of `user`, `system`, or `developer`.

          - `USER("user")`

          - `SYSTEM("system")`

          - `DEVELOPER("developer")`

        - `Optional<Status> status`

          The status of item. One of `in_progress`, `completed`, or
          `incomplete`. Populated when items are returned via API.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

        - `Optional<Type> type`

          The type of the message input. Always set to `message`.

          - `MESSAGE("message")`

      - `class ResponseOutputMessage:`

        An output message from the model.

        - `String id`

          The unique ID of the output message.

        - `List<Content> content`

          The content of the output message.

          - `class ResponseOutputText:`

            A text output from the model.

            - `List<Annotation> annotations`

              The annotations of the text output.

              - `class FileCitation:`

                A citation to a file.

                - `String fileId`

                  The ID of the file.

                - `String filename`

                  The filename of the file cited.

                - `long index`

                  The index in the output text at which to insert the file citation.

                - `JsonValue; type "file_citation"constant`

                  The type of the file citation. Always `file_citation`.

                  - `FILE_CITATION("file_citation")`

              - `class UrlCitation:`

                A citation for a web resource used to generate a model response.

                - `long endIndex`

                  The index of the last character of the URL citation in the message.

                - `long startIndex`

                  The index of the first character of the URL citation in the message.

                - `String title`

                  The title of the web resource.

                - `JsonValue; type "url_citation"constant`

                  The type of the URL citation. Always `url_citation`.

                  - `URL_CITATION("url_citation")`

                - `String url`

                  The URL of the web resource.

              - `class ContainerFileCitation:`

                A citation for a container file used to generate a model response.

                - `String containerId`

                  The ID of the container file.

                - `long endIndex`

                  The index of the last character of the container file citation in the message.

                - `String fileId`

                  The ID of the file.

                - `String filename`

                  The filename of the container file cited.

                - `long startIndex`

                  The index of the first character of the container file citation in the message.

                - `JsonValue; type "container_file_citation"constant`

                  The type of the container file citation. Always `container_file_citation`.

                  - `CONTAINER_FILE_CITATION("container_file_citation")`

              - `class FilePath:`

                A path to a file.

                - `String fileId`

                  The ID of the file.

                - `long index`

                  The index of the file in the list of files.

                - `JsonValue; type "file_path"constant`

                  The type of the file path. Always `file_path`.

                  - `FILE_PATH("file_path")`

            - `String text`

              The text output from the model.

            - `JsonValue; type "output_text"constant`

              The type of the output text. Always `output_text`.

              - `OUTPUT_TEXT("output_text")`

            - `Optional<List<Logprob>> logprobs`

              - `String token`

              - `List<long> bytes`

              - `double logprob`

              - `List<TopLogprob> topLogprobs`

                - `String token`

                - `List<long> bytes`

                - `double logprob`

          - `class ResponseOutputRefusal:`

            A refusal from the model.

            - `String refusal`

              The refusal explanation from the model.

            - `JsonValue; type "refusal"constant`

              The type of the refusal. Always `refusal`.

              - `REFUSAL("refusal")`

        - `JsonValue; role "assistant"constant`

          The role of the output message. Always `assistant`.

          - `ASSISTANT("assistant")`

        - `Status status`

          The status of the message input. One of `in_progress`, `completed`, or
          `incomplete`. Populated when input items are returned via API.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

        - `JsonValue; type "message"constant`

          The type of the output message. Always `message`.

          - `MESSAGE("message")`

        - `Optional<Phase> phase`

          Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
          For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
          phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

          - `COMMENTARY("commentary")`

          - `FINAL_ANSWER("final_answer")`

      - `class ResponseFileSearchToolCall:`

        The results of a file search tool call. See the
        [file search guide](/api/docs/guides/tools-file-search) for more information.

        - `String id`

          The unique ID of the file search tool call.

        - `List<String> queries`

          The queries used to search for files.

        - `Status status`

          The status of the file search tool call. One of `in_progress`,
          `searching`, `incomplete` or `failed`,

          - `IN_PROGRESS("in_progress")`

          - `SEARCHING("searching")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

          - `FAILED("failed")`

        - `JsonValue; type "file_search_call"constant`

          The type of the file search tool call. Always `file_search_call`.

          - `FILE_SEARCH_CALL("file_search_call")`

        - `Optional<List<Result>> results`

          The results of the file search tool call.

          - `Optional<Attributes> attributes`

            Set of 16 key-value pairs that can be attached to an object. This can be
            useful for storing additional information about the object in a structured
            format, and querying for objects via API or the dashboard. Keys are strings
            with a maximum length of 64 characters. Values are strings with a maximum
            length of 512 characters, booleans, or numbers.

            - `String`

            - `double`

            - `boolean`

          - `Optional<String> fileId`

            The unique ID of the file.

          - `Optional<String> filename`

            The name of the file.

          - `Optional<Double> score`

            The relevance score of the file - a value between 0 and 1.

          - `Optional<String> text`

            The text that was retrieved from the file.

      - `class ResponseComputerToolCall:`

        A tool call to a computer use tool. See the
        [computer use guide](/api/docs/guides/tools-computer-use) for more information.

        - `String id`

          The unique ID of the computer call.

        - `String callId`

          An identifier used when responding to the tool call with output.

        - `List<PendingSafetyCheck> pendingSafetyChecks`

          The pending safety checks for the computer call.

          - `String id`

            The ID of the pending safety check.

          - `Optional<String> code`

            The type of the pending safety check.

          - `Optional<String> message`

            Details about the pending safety check.

        - `Status status`

          The status of the item. One of `in_progress`, `completed`, or
          `incomplete`. Populated when items are returned via API.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

        - `Type type`

          The type of the computer call. Always `computer_call`.

          - `COMPUTER_CALL("computer_call")`

        - `Optional<Action> action`

          A click action.

          - `class Click:`

            A click action.

            - `Button button`

              Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

              - `LEFT("left")`

              - `RIGHT("right")`

              - `WHEEL("wheel")`

              - `BACK("back")`

              - `FORWARD("forward")`

            - `JsonValue; type "click"constant`

              Specifies the event type. For a click action, this property is always `click`.

              - `CLICK("click")`

            - `long x`

              The x-coordinate where the click occurred.

            - `long y`

              The y-coordinate where the click occurred.

            - `Optional<List<String>> keys`

              The keys being held while clicking.

          - `class DoubleClick:`

            A double click action.

            - `Optional<List<String>> keys`

              The keys being held while double-clicking.

            - `JsonValue; type "double_click"constant`

              Specifies the event type. For a double click action, this property is always set to `double_click`.

              - `DOUBLE_CLICK("double_click")`

            - `long x`

              The x-coordinate where the double click occurred.

            - `long y`

              The y-coordinate where the double click occurred.

          - `class Drag:`

            A drag action.

            - `List<Path> path`

              An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

              ```
              [
                { x: 100, y: 200 },
                { x: 200, y: 300 }
              ]
              ```

              - `long x`

                The x-coordinate.

              - `long y`

                The y-coordinate.

            - `JsonValue; type "drag"constant`

              Specifies the event type. For a drag action, this property is always set to `drag`.

              - `DRAG("drag")`

            - `Optional<List<String>> keys`

              The keys being held while dragging the mouse.

          - `class Keypress:`

            A collection of keypresses the model would like to perform.

            - `List<String> keys`

              The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

            - `JsonValue; type "keypress"constant`

              Specifies the event type. For a keypress action, this property is always set to `keypress`.

              - `KEYPRESS("keypress")`

          - `class Move:`

            A mouse move action.

            - `JsonValue; type "move"constant`

              Specifies the event type. For a move action, this property is always set to `move`.

              - `MOVE("move")`

            - `long x`

              The x-coordinate to move to.

            - `long y`

              The y-coordinate to move to.

            - `Optional<List<String>> keys`

              The keys being held while moving the mouse.

          - `JsonValue;`

            - `JsonValue; type "screenshot"constant`

              Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

              - `SCREENSHOT("screenshot")`

          - `class Scroll:`

            A scroll action.

            - `long scrollX`

              The horizontal scroll distance.

            - `long scrollY`

              The vertical scroll distance.

            - `JsonValue; type "scroll"constant`

              Specifies the event type. For a scroll action, this property is always set to `scroll`.

              - `SCROLL("scroll")`

            - `long x`

              The x-coordinate where the scroll occurred.

            - `long y`

              The y-coordinate where the scroll occurred.

            - `Optional<List<String>> keys`

              The keys being held while scrolling.

          - `class Type:`

            An action to type in text.

            - `String text`

              The text to type.

            - `JsonValue; type "type"constant`

              Specifies the event type. For a type action, this property is always set to `type`.

              - `TYPE("type")`

          - `JsonValue;`

            - `JsonValue; type "wait"constant`

              Specifies the event type. For a wait action, this property is always set to `wait`.

              - `WAIT("wait")`

        - `Optional<List<ComputerAction>> actions`

          Flattened batched actions for `computer_use`. Each action includes an
          `type` discriminator and action-specific fields.

          - `Click`

            - `Button button`

              Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

              - `LEFT("left")`

              - `RIGHT("right")`

              - `WHEEL("wheel")`

              - `BACK("back")`

              - `FORWARD("forward")`

            - `JsonValue; type "click"constant`

              Specifies the event type. For a click action, this property is always `click`.

              - `CLICK("click")`

            - `long x`

              The x-coordinate where the click occurred.

            - `long y`

              The y-coordinate where the click occurred.

            - `Optional<List<String>> keys`

              The keys being held while clicking.

          - `DoubleClick`

            - `Optional<List<String>> keys`

              The keys being held while double-clicking.

            - `JsonValue; type "double_click"constant`

              Specifies the event type. For a double click action, this property is always set to `double_click`.

              - `DOUBLE_CLICK("double_click")`

            - `long x`

              The x-coordinate where the double click occurred.

            - `long y`

              The y-coordinate where the double click occurred.

          - `Drag`

            - `List<Path> path`

              An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

              ```
              [
                { x: 100, y: 200 },
                { x: 200, y: 300 }
              ]
              ```

              - `long x`

                The x-coordinate.

              - `long y`

                The y-coordinate.

            - `JsonValue; type "drag"constant`

              Specifies the event type. For a drag action, this property is always set to `drag`.

              - `DRAG("drag")`

            - `Optional<List<String>> keys`

              The keys being held while dragging the mouse.

          - `Keypress`

            - `List<String> keys`

              The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

            - `JsonValue; type "keypress"constant`

              Specifies the event type. For a keypress action, this property is always set to `keypress`.

              - `KEYPRESS("keypress")`

          - `Move`

            - `JsonValue; type "move"constant`

              Specifies the event type. For a move action, this property is always set to `move`.

              - `MOVE("move")`

            - `long x`

              The x-coordinate to move to.

            - `long y`

              The y-coordinate to move to.

            - `Optional<List<String>> keys`

              The keys being held while moving the mouse.

          - `JsonValue;`

            - `JsonValue; type "screenshot"constant`

              Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

              - `SCREENSHOT("screenshot")`

          - `Scroll`

            - `long scrollX`

              The horizontal scroll distance.

            - `long scrollY`

              The vertical scroll distance.

            - `JsonValue; type "scroll"constant`

              Specifies the event type. For a scroll action, this property is always set to `scroll`.

              - `SCROLL("scroll")`

            - `long x`

              The x-coordinate where the scroll occurred.

            - `long y`

              The y-coordinate where the scroll occurred.

            - `Optional<List<String>> keys`

              The keys being held while scrolling.

          - `Type`

            - `String text`

              The text to type.

            - `JsonValue; type "type"constant`

              Specifies the event type. For a type action, this property is always set to `type`.

              - `TYPE("type")`

          - `JsonValue;`

            - `JsonValue; type "wait"constant`

              Specifies the event type. For a wait action, this property is always set to `wait`.

              - `WAIT("wait")`

      - `ComputerCallOutput`

        - `String callId`

          The ID of the computer tool call that produced the output.

        - `ResponseComputerToolCallOutputScreenshot output`

          A computer screenshot image used with the computer use tool.

          - `JsonValue; type "computer_screenshot"constant`

            Specifies the event type. For a computer screenshot, this property is
            always set to `computer_screenshot`.

            - `COMPUTER_SCREENSHOT("computer_screenshot")`

          - `Optional<String> fileId`

            The identifier of an uploaded file that contains the screenshot.

          - `Optional<String> imageUrl`

            The URL of the screenshot image.

        - `JsonValue; type "computer_call_output"constant`

          The type of the computer tool call output. Always `computer_call_output`.

          - `COMPUTER_CALL_OUTPUT("computer_call_output")`

        - `Optional<String> id`

          The ID of the computer tool call output.

        - `Optional<List<AcknowledgedSafetyCheck>> acknowledgedSafetyChecks`

          The safety checks reported by the API that have been acknowledged by the developer.

          - `String id`

            The ID of the pending safety check.

          - `Optional<String> code`

            The type of the pending safety check.

          - `Optional<String> message`

            Details about the pending safety check.

        - `Optional<Status> status`

          The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `class ResponseFunctionWebSearch:`

        The results of a web search tool call. See the
        [web search guide](/api/docs/guides/tools-web-search) for more information.

        - `String id`

          The unique ID of the web search tool call.

        - `Action action`

          An object describing the specific action taken in this web search call.
          Includes details on how the model used the web (search, open_page, find_in_page).

          - `class Search:`

            Action type "search" - Performs a web search query.

            - `JsonValue; type "search"constant`

              The action type.

              - `SEARCH("search")`

            - `Optional<List<String>> queries`

              The search queries.

            - `Optional<String> query`

              The search query.

            - `Optional<List<Source>> sources`

              The sources used in the search.

              - `JsonValue; type "url"constant`

                The type of source. Always `url`.

                - `URL("url")`

              - `String url`

                The URL of the source.

          - `class OpenPage:`

            Action type "open_page" - Opens a specific URL from search results.

            - `JsonValue; type "open_page"constant`

              The action type.

              - `OPEN_PAGE("open_page")`

            - `Optional<String> url`

              The URL opened by the model.

          - `class FindInPage:`

            Action type "find_in_page": Searches for a pattern within a loaded page.

            - `String pattern`

              The pattern or text to search for within the page.

            - `JsonValue; type "find_in_page"constant`

              The action type.

              - `FIND_IN_PAGE("find_in_page")`

            - `String url`

              The URL of the page searched for the pattern.

        - `Status status`

          The status of the web search tool call.

          - `IN_PROGRESS("in_progress")`

          - `SEARCHING("searching")`

          - `COMPLETED("completed")`

          - `FAILED("failed")`

          - `INCOMPLETE("incomplete")`

        - `JsonValue; type "web_search_call"constant`

          The type of the web search tool call. Always `web_search_call`.

          - `WEB_SEARCH_CALL("web_search_call")`

      - `class ResponseFunctionToolCall:`

        A tool call to run a function. See the
        [function calling guide](/api/docs/guides/function-calling) for more information.

        - `String arguments`

          A JSON string of the arguments to pass to the function.

        - `String callId`

          The unique ID of the function tool call generated by the model.

        - `String name`

          The name of the function to run.

        - `JsonValue; type "function_call"constant`

          The type of the function tool call. Always `function_call`.

          - `FUNCTION_CALL("function_call")`

        - `Optional<String> id`

          The unique ID of the function tool call.

        - `Optional<Boolean> async`

          Whether the function tool call runs asynchronously.

        - `Optional<Caller> caller`

          The execution context that produced this tool call.

          - `JsonValue;`

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class Program:`

            - `String callerId`

              The call ID of the program item that produced this tool call.

            - `JsonValue; type "program"constant`

              - `PROGRAM("program")`

        - `Optional<String> namespace`

          The namespace of the function to run.

        - `Optional<Status> status`

          The status of the item. One of `in_progress`, `completed`, or
          `incomplete`. Populated when items are returned via API.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `FunctionCallOutput`

        - `Output output`

          Text, image, or file output of the function tool call.

          - `String`

          - `List<ResponseFunctionCallOutputItem>`

            - `class ResponseInputTextContent:`

              A text input to the model.

              - `String text`

                The text input to the model.

              - `JsonValue; type "input_text"constant`

                The type of the input item. Always `input_text`.

                - `INPUT_TEXT("input_text")`

              - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `JsonValue; mode "explicit"constant`

                  The breakpoint mode. Always `explicit`.

                  - `EXPLICIT("explicit")`

            - `class ResponseInputImageContent:`

              An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision)

              - `JsonValue; type "input_image"constant`

                The type of the input item. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

              - `Optional<Detail> detail`

                The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                - `LOW("low")`

                - `HIGH("high")`

                - `AUTO("auto")`

                - `ORIGINAL("original")`

              - `Optional<String> fileId`

                The ID of the file to be sent to the model.

              - `Optional<String> imageUrl`

                The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

              - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `JsonValue; mode "explicit"constant`

                  The breakpoint mode. Always `explicit`.

                  - `EXPLICIT("explicit")`

            - `class ResponseInputFileContent:`

              A file input to the model.

              - `JsonValue; type "input_file"constant`

                The type of the input item. Always `input_file`.

                - `INPUT_FILE("input_file")`

              - `Optional<Detail> detail`

                The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

                - `AUTO("auto")`

                - `LOW("low")`

                - `HIGH("high")`

              - `Optional<String> fileData`

                The base64-encoded data of the file to be sent to the model.

              - `Optional<String> fileId`

                The ID of the file to be sent to the model.

              - `Optional<String> fileUrl`

                The URL of the file to be sent to the model.

              - `Optional<String> filename`

                The name of the file to be sent to the model.

              - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `JsonValue; mode "explicit"constant`

                  The breakpoint mode. Always `explicit`.

                  - `EXPLICIT("explicit")`

        - `JsonValue; type "function_call_output"constant`

          The type of the function tool call output. Always `function_call_output`.

          - `FUNCTION_CALL_OUTPUT("function_call_output")`

        - `Optional<String> id`

          The unique ID of the function tool call output. Populated when this item is returned via API.

        - `Optional<String> callId`

          The unique ID of the function tool call generated by the model.

        - `Optional<Caller> caller`

          The execution context that produced this tool call.

          - `JsonValue;`

            - `JsonValue; type "direct"constant`

              The caller type. Always `direct`.

              - `DIRECT("direct")`

          - `class Program:`

            - `String callerId`

              The call ID of the program item that produced this tool call.

            - `JsonValue; type "program"constant`

              The caller type. Always `program`.

              - `PROGRAM("program")`

        - `Optional<String> name`

          The name of the tool that produced the output.

        - `Optional<String> namespace`

          The namespace of the tool that produced the output.

        - `Optional<Status> status`

          The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `ToolSearchCall`

        - `JsonValue arguments`

          The arguments supplied to the tool search call.

        - `JsonValue; type "tool_search_call"constant`

          The item type. Always `tool_search_call`.

          - `TOOL_SEARCH_CALL("tool_search_call")`

        - `Optional<String> id`

          The unique ID of this tool search call.

        - `Optional<String> callId`

          The unique ID of the tool search call generated by the model.

        - `Optional<Execution> execution`

          Whether tool search was executed by the server or by the client.

          - `SERVER("server")`

          - `CLIENT("client")`

        - `Optional<Status> status`

          The status of the tool search call.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `class ResponseToolSearchOutputItemParam:`

        - `List<Tool> tools`

          The loaded tool definitions returned by the tool search output.

          - `class FunctionTool:`

            Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

            - `String name`

              The name of the function to call.

            - `Optional<Parameters> parameters`

              A JSON schema object describing the parameters of the function.

            - `Optional<Boolean> strict`

              Whether strict parameter validation is enforced for this function tool.

            - `JsonValue; type "function"constant`

              The type of the function tool. Always `function`.

              - `FUNCTION("function")`

            - `Optional<List<AllowedCaller>> allowedCallers`

              The tool invocation context(s).

              - `DIRECT("direct")`

              - `PROGRAMMATIC("programmatic")`

            - `Optional<Boolean> async`

            - `Optional<Boolean> deferLoading`

              Whether this function is deferred and loaded via tool search.

            - `Optional<String> description`

              A description of the function. Used by the model to determine whether or not to call the function.

            - `Optional<OutputSchema> outputSchema`

              A JSON schema object describing the JSON value encoded in string outputs for this function.

          - `class FileSearchTool:`

            A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

            - `JsonValue; type "file_search"constant`

              The type of the file search tool. Always `file_search`.

              - `FILE_SEARCH("file_search")`

            - `List<String> vectorStoreIds`

              The IDs of the vector stores to search.

            - `Optional<Filters> filters`

              A filter to apply.

              - `class ComparisonFilter:`

                A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                - `String key`

                  The key to compare against the value.

                - `Type type`

                  Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                  - `eq`: equals
                  - `ne`: not equal
                  - `gt`: greater than
                  - `gte`: greater than or equal
                  - `lt`: less than
                  - `lte`: less than or equal
                  - `in`: in
                  - `nin`: not in

                  - `EQ("eq")`

                  - `NE("ne")`

                  - `GT("gt")`

                  - `GTE("gte")`

                  - `LT("lt")`

                  - `LTE("lte")`

                  - `IN("in")`

                  - `NIN("nin")`

                - `Value value`

                  The value to compare against the attribute key; supports string, number, or boolean types.

                  - `String`

                  - `double`

                  - `boolean`

                  - `List<ComparisonFilterValueItem>`

                    - `String`

                    - `double`

              - `class CompoundFilter:`

                Combine multiple filters using `and` or `or`.

                - `List<Filter> filters`

                  Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

                  - `class ComparisonFilter:`

                    A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                  - `JsonValue`

                - `Type type`

                  Type of operation: `and` or `or`.

                  - `AND("and")`

                  - `OR("or")`

            - `Optional<Long> maxNumResults`

              The maximum number of results to return. This number should be between 1 and 50 inclusive.

            - `Optional<RankingOptions> rankingOptions`

              Ranking options for search.

              - `Optional<HybridSearch> hybridSearch`

                Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

                - `double embeddingWeight`

                  The weight of the embedding in the reciprocal ranking fusion.

                - `double textWeight`

                  The weight of the text in the reciprocal ranking fusion.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search.

                - `AUTO("auto")`

                - `DEFAULT_2024_11_15("default-2024-11-15")`

              - `Optional<Double> scoreThreshold`

                The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

          - `class ComputerTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

            - `JsonValue; type "computer"constant`

              The type of the computer tool. Always `computer`.

              - `COMPUTER("computer")`

          - `class ComputerUsePreviewTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

            - `long displayHeight`

              The height of the computer display.

            - `long displayWidth`

              The width of the computer display.

            - `Environment environment`

              The type of computer environment to control.

              - `WINDOWS("windows")`

              - `MAC("mac")`

              - `LINUX("linux")`

              - `UBUNTU("ubuntu")`

              - `BROWSER("browser")`

            - `JsonValue; type "computer_use_preview"constant`

              The type of the computer use tool. Always `computer_use_preview`.

              - `COMPUTER_USE_PREVIEW("computer_use_preview")`

          - `class WebSearchTool:`

            Search the Internet for sources related to the prompt. Learn more about the
            [web search tool](/api/docs/guides/tools-web-search).

            - `Type type`

              The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

              - `WEB_SEARCH("web_search")`

              - `WEB_SEARCH_2025_08_26("web_search_2025_08_26")`

            - `Optional<Boolean> externalWebAccess`

              Allow live internet access for web search. Defaults to true when omitted. When false, the web search tool runs in offline/cache-only mode and will not fetch new external content.

            - `Optional<Filters> filters`

              Filters for the search.

              - `Optional<List<String>> allowedDomains`

                Allowed domains for the search. If not provided, all domains are allowed.
                Subdomains of the provided domains are allowed as well.

                Example: `["pubmed.ncbi.nlm.nih.gov"]`

            - `Optional<SearchContextSize> searchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<UserLocation> userLocation`

              The approximate location of the user. If omitted or null, defaults to the
              United States. To avoid this fallback, pass `{"type": "approximate"}` without
              location fields. To localize results, provide the relevant location fields.

              - `Optional<String> city`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Optional<String> country`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Optional<String> region`

                Free text input for the region of the user, e.g. `California`.

              - `Optional<String> timezone`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

              - `Optional<Type> type`

                The type of location approximation. Always `approximate`.

                - `APPROXIMATE("approximate")`

          - `Mcp`

            - `String serverLabel`

              A label for this MCP server, used to identify it in tool calls.

            - `JsonValue; type "mcp"constant`

              The type of the MCP tool. Always `mcp`.

              - `MCP("mcp")`

            - `Optional<List<AllowedCaller>> allowedCallers`

              The tool invocation context(s).

              - `DIRECT("direct")`

              - `PROGRAMMATIC("programmatic")`

            - `Optional<AllowedTools> allowedTools`

              List of allowed tool names or a filter object.

              - `List<String>`

              - `class McpToolFilter:`

                A filter object to specify which tools are allowed.

                - `Optional<Boolean> readOnly`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `Optional<List<String>> toolNames`

                  List of allowed tool names.

            - `Optional<String> authorization`

              An OAuth access token that can be used with a remote MCP server, either
              with a custom MCP server URL or a service connector. Your application
              must handle the OAuth authorization flow and provide the token here.

            - `Optional<ConnectorId> connectorId`

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

              - `CONNECTOR_DROPBOX("connector_dropbox")`

              - `CONNECTOR_GMAIL("connector_gmail")`

              - `CONNECTOR_GOOGLECALENDAR("connector_googlecalendar")`

              - `CONNECTOR_GOOGLEDRIVE("connector_googledrive")`

              - `CONNECTOR_MICROSOFTTEAMS("connector_microsoftteams")`

              - `CONNECTOR_OUTLOOKCALENDAR("connector_outlookcalendar")`

              - `CONNECTOR_OUTLOOKEMAIL("connector_outlookemail")`

              - `CONNECTOR_SHAREPOINT("connector_sharepoint")`

            - `Optional<Boolean> deferLoading`

              Whether this MCP tool is deferred and discovered via tool search.

            - `Optional<Headers> headers`

              Optional HTTP headers to send to the MCP server. Use for authentication
              or other purposes.

            - `Optional<RequireApproval> requireApproval`

              Specify which of the MCP server's tools require approval.

              - `class McpToolApprovalFilter:`

                Specify which of the MCP server's tools require approval. Can be
                `always`, `never`, or a filter object associated with tools
                that require approval.

                - `Optional<Always> always`

                  A filter object to specify which tools are allowed.

                  - `Optional<Boolean> readOnly`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `Optional<List<String>> toolNames`

                    List of allowed tool names.

                - `Optional<Never> never`

                  A filter object to specify which tools are allowed.

                  - `Optional<Boolean> readOnly`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `Optional<List<String>> toolNames`

                    List of allowed tool names.

              - `enum McpToolApprovalSetting:`

                Specify a single approval policy for all tools. One of `always` or
                `never`. When set to `always`, all tools will require approval. When
                set to `never`, all tools will not require approval.

                - `ALWAYS("always")`

                - `NEVER("never")`

            - `Optional<String> serverDescription`

              Optional description of the MCP server, used to provide more context.

            - `Optional<String> serverUrl`

              The URL for the MCP server. One of `server_url`, `connector_id`, or
              `tunnel_id` must be provided.

            - `Optional<String> tunnelId`

              The Secure MCP Tunnel ID to use instead of a direct server URL. One of
              `server_url`, `connector_id`, or `tunnel_id` must be provided.

          - `CodeInterpreter`

            - `Container container`

              The code interpreter container. Can be a container ID or an object that
              specifies uploaded file IDs to make available to your code, along with an
              optional `memory_limit` setting.

              - `String`

              - `class CodeInterpreterToolAuto:`

                Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

                - `JsonValue; type "auto"constant`

                  Always `auto`.

                  - `AUTO("auto")`

                - `Optional<List<String>> fileIds`

                  An optional list of uploaded files to make available to your code.

                - `Optional<MemoryLimit> memoryLimit`

                  The memory limit for the code interpreter container.

                  - `_1G("1g")`

                  - `_4G("4g")`

                  - `_16G("16g")`

                  - `_64G("64g")`

                - `Optional<NetworkPolicy> networkPolicy`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled:`

                    - `JsonValue; type "disabled"constant`

                      Disable outbound network access. Always `disabled`.

                      - `DISABLED("disabled")`

                  - `class ContainerNetworkPolicyAllowlist:`

                    - `List<String> allowedDomains`

                      A list of allowed domains when type is `allowlist`.

                    - `JsonValue; type "allowlist"constant`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `ALLOWLIST("allowlist")`

                    - `Optional<List<ContainerNetworkPolicyDomainSecret>> domainSecrets`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `String domain`

                        The domain associated with the secret.

                      - `String name`

                        The name of the secret to inject for the domain.

                      - `String value`

                        The secret value to inject for the domain.

            - `JsonValue; type "code_interpreter"constant`

              The type of the code interpreter tool. Always `code_interpreter`.

              - `CODE_INTERPRETER("code_interpreter")`

            - `Optional<List<AllowedCaller>> allowedCallers`

              The tool invocation context(s).

              - `DIRECT("direct")`

              - `PROGRAMMATIC("programmatic")`

          - `JsonValue;`

            - `JsonValue; type "programmatic_tool_calling"constant`

              The type of the tool. Always `programmatic_tool_calling`.

              - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

          - `ImageGeneration`

            - `JsonValue; type "image_generation"constant`

              The type of the image generation tool. Always `image_generation`.

              - `IMAGE_GENERATION("image_generation")`

            - `Optional<Action> action`

              Whether to generate a new image or edit an existing image. Default: `auto`.

              - `GENERATE("generate")`

              - `EDIT("edit")`

              - `AUTO("auto")`

            - `Optional<Background> background`

              Allows to set transparency for the background of the generated image(s). Must
              be one of `transparent`, `opaque`, or `auto` (default value). When `auto` is
              used, the model will automatically determine the best background for the
              image.

              `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`, including their
              `2026-09-08` snapshots, support `opaque` and `transparent` backgrounds.
              Transparent backgrounds are available for supported GPT Image models. For
              `gpt-image-2` and `gpt-image-2-2026-04-21`, this support is in preview. When
              using `transparent`, set the output format to `png` or `webp`.

              - `TRANSPARENT("transparent")`

              - `OPAQUE("opaque")`

              - `AUTO("auto")`

            - `Optional<InputFidelity> inputFidelity`

              Controls fidelity to the original input image(s). This parameter is supported for GPT image models that support input fidelity. `gpt-image-2` and `gpt-image-2-2026-04-21` ignore this parameter.

              - `HIGH("high")`

              - `LOW("low")`

            - `Optional<InputImageMask> inputImageMask`

              Optional mask for inpainting. Contains `image_url`
              (string, optional) and `file_id` (string, optional).

              - `Optional<String> fileId`

                File ID for the mask image.

              - `Optional<String> imageUrl`

                Base64-encoded mask image.

            - `Optional<Model> model`

              The image generation model to use. One of `gpt-image-1`,
              `gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
              `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
              `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
              `gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
              `gpt-image-1`.

              - `GPT_IMAGE_1("gpt-image-1")`

              - `GPT_IMAGE_1_MINI("gpt-image-1-mini")`

              - `GPT_IMAGE_2("gpt-image-2")`

              - `GPT_IMAGE_2_2026_04_21("gpt-image-2-2026-04-21")`

              - `GPT_IMAGE_2_5_SUNBURST("gpt-image-2.5-sunburst")`

              - `GPT_IMAGE_2_5_SUNBURST_2026_09_08("gpt-image-2.5-sunburst-2026-09-08")`

              - `GPT_IMAGE_2_5_FLARE("gpt-image-2.5-flare")`

              - `GPT_IMAGE_2_5_FLARE_2026_09_08("gpt-image-2.5-flare-2026-09-08")`

              - `GPT_IMAGE_1_5("gpt-image-1.5")`

              - `CHATGPT_IMAGE_LATEST("chatgpt-image-latest")`

            - `Optional<Moderation> moderation`

              Moderation level for the generated image. Default: `auto`.

              - `AUTO("auto")`

              - `LOW("low")`

            - `Optional<Long> outputCompression`

              Compression level for the output image. Default: 100.

            - `Optional<OutputFormat> outputFormat`

              The output format of the generated image. One of `png`, `webp`, or
              `jpeg`. Default: `png`.

              - `PNG("png")`

              - `WEBP("webp")`

              - `JPEG("jpeg")`

            - `Optional<Long> partialImages`

              Number of partial images to generate in streaming mode, from 0 (default value) to 3.

            - `Optional<Quality> quality`

              The quality of the generated image. The GPT image models support `low`,
              `medium`, and `high`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`,
              including their `2026-09-08` snapshots, also support `xhigh` and `max`.
              Default: `auto`.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

              - `XHIGH("xhigh")`

              - `MAX("max")`

              - `AUTO("auto")`

            - `Optional<Size> size`

              The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model's current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

              - `_1024X1024("1024x1024")`

              - `_1024X1536("1024x1536")`

              - `_1536X1024("1536x1024")`

              - `AUTO("auto")`

          - `JsonValue;`

            - `JsonValue; type "local_shell"constant`

              The type of the local shell tool. Always `local_shell`.

              - `LOCAL_SHELL("local_shell")`

          - `class FunctionShellTool:`

            A tool that allows the model to execute shell commands.

            - `JsonValue; type "shell"constant`

              The type of the shell tool. Always `shell`.

              - `SHELL("shell")`

            - `Optional<List<AllowedCaller>> allowedCallers`

              The tool invocation context(s).

              - `DIRECT("direct")`

              - `PROGRAMMATIC("programmatic")`

            - `Optional<Environment> environment`

              - `class ContainerAuto:`

                - `JsonValue; type "container_auto"constant`

                  Automatically creates a container for this request

                  - `CONTAINER_AUTO("container_auto")`

                - `Optional<List<String>> fileIds`

                  An optional list of uploaded files to make available to your code.

                - `Optional<MemoryLimit> memoryLimit`

                  The memory limit for the container.

                  - `_1G("1g")`

                  - `_4G("4g")`

                  - `_16G("16g")`

                  - `_64G("64g")`

                - `Optional<NetworkPolicy> networkPolicy`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled:`

                  - `class ContainerNetworkPolicyAllowlist:`

                - `Optional<List<Skill>> skills`

                  An optional list of skills referenced by id or inline data.

                  - `class SkillReference:`

                    - `String skillId`

                      The ID of the referenced skill.

                    - `JsonValue; type "skill_reference"constant`

                      References a skill created with the /v1/skills endpoint.

                      - `SKILL_REFERENCE("skill_reference")`

                    - `Optional<String> version`

                      Optional skill version. Use a positive integer or 'latest'. Omit for default.

                  - `class InlineSkill:`

                    - `String description`

                      The description of the skill.

                    - `String name`

                      The name of the skill.

                    - `InlineSkillSource source`

                      Inline skill payload

                      - `String data`

                        Base64-encoded skill zip bundle.

                      - `JsonValue; mediaType "application/zip"constant`

                        The media type of the inline skill payload. Must be `application/zip`.

                        - `APPLICATION_ZIP("application/zip")`

                      - `JsonValue; type "base64"constant`

                        The type of the inline skill source. Must be `base64`.

                        - `BASE64("base64")`

                    - `JsonValue; type "inline"constant`

                      Defines an inline skill for this request.

                      - `INLINE("inline")`

              - `class LocalEnvironment:`

                - `JsonValue; type "local"constant`

                  Use a local computer environment.

                  - `LOCAL("local")`

                - `Optional<List<LocalSkill>> skills`

                  An optional list of skills.

                  - `String description`

                    The description of the skill.

                  - `String name`

                    The name of the skill.

                  - `String path`

                    The path to the directory containing the skill.

              - `class ContainerReference:`

                - `String containerId`

                  The ID of the referenced container.

                - `JsonValue; type "container_reference"constant`

                  References a container created with the /v1/containers endpoint

                  - `CONTAINER_REFERENCE("container_reference")`

          - `class CustomTool:`

            A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

            - `String name`

              The name of the custom tool, used to identify it in tool calls.

            - `JsonValue; type "custom"constant`

              The type of the custom tool. Always `custom`.

              - `CUSTOM("custom")`

            - `Optional<List<AllowedCaller>> allowedCallers`

              The tool invocation context(s).

              - `DIRECT("direct")`

              - `PROGRAMMATIC("programmatic")`

            - `Optional<Boolean> async`

              Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

            - `Optional<Boolean> deferLoading`

              Whether this tool should be deferred and discovered via tool search.

            - `Optional<String> description`

              Optional description of the custom tool, used to provide more context.

            - `Optional<CustomToolInputFormat> format`

              The input format for the custom tool. Default is unconstrained text.

              - `JsonValue;`

                - `JsonValue; type "text"constant`

                  Unconstrained text format. Always `text`.

                  - `TEXT("text")`

              - `Grammar`

                - `String definition`

                  The grammar definition.

                - `Syntax syntax`

                  The syntax of the grammar definition. One of `lark` or `regex`.

                  - `LARK("lark")`

                  - `REGEX("regex")`

                - `JsonValue; type "grammar"constant`

                  Grammar format. Always `grammar`.

                  - `GRAMMAR("grammar")`

          - `class NamespaceTool:`

            Groups function/custom tools under a shared namespace.

            - `String description`

              A description of the namespace shown to the model.

            - `String name`

              The namespace name used in tool calls (for example, `crm`).

            - `List<Tool> tools`

              The function/custom tools available inside this namespace.

              - `class Function:`

                - `String name`

                - `JsonValue; type "function"constant`

                  - `FUNCTION("function")`

                - `Optional<List<AllowedCaller>> allowedCallers`

                  The tool invocation context(s).

                  - `DIRECT("direct")`

                  - `PROGRAMMATIC("programmatic")`

                - `Optional<Boolean> async`

                  Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

                - `Optional<Boolean> deferLoading`

                  Whether this function should be deferred and discovered via tool search.

                - `Optional<String> description`

                - `Optional<OutputSchema> outputSchema`

                  A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

                - `Optional<JsonValue> parameters`

                - `Optional<Boolean> strict`

                  Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

              - `class CustomTool:`

                A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

            - `JsonValue; type "namespace"constant`

              The type of the tool. Always `namespace`.

              - `NAMESPACE("namespace")`

          - `class ToolSearchTool:`

            Hosted or BYOT tool search configuration for deferred tools.

            - `JsonValue; type "tool_search"constant`

              The type of the tool. Always `tool_search`.

              - `TOOL_SEARCH("tool_search")`

            - `Optional<String> description`

              Description shown to the model for a client-executed tool search tool.

            - `Optional<Execution> execution`

              Whether tool search is executed by the server or by the client.

              - `SERVER("server")`

              - `CLIENT("client")`

            - `Optional<JsonValue> parameters`

              Parameter schema for a client-executed tool search tool.

          - `class WebSearchPreviewTool:`

            This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

            - `Type type`

              The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

              - `WEB_SEARCH_PREVIEW("web_search_preview")`

              - `WEB_SEARCH_PREVIEW_2025_03_11("web_search_preview_2025_03_11")`

            - `Optional<List<SearchContentType>> searchContentTypes`

              - `TEXT("text")`

              - `IMAGE("image")`

            - `Optional<SearchContextSize> searchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<UserLocation> userLocation`

              The approximate location of the user. If omitted or null, defaults to the United States. To avoid this fallback, pass `{"type": "approximate"}` without location fields. To localize results, provide the relevant location fields.

              - `JsonValue; type "approximate"constant`

                The type of location approximation. Always `approximate`.

                - `APPROXIMATE("approximate")`

              - `Optional<String> city`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Optional<String> country`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Optional<String> region`

                Free text input for the region of the user, e.g. `California`.

              - `Optional<String> timezone`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

          - `class ApplyPatchTool:`

            Allows the assistant to create, delete, or update files using unified diffs.

            - `JsonValue; type "apply_patch"constant`

              The type of the tool. Always `apply_patch`.

              - `APPLY_PATCH("apply_patch")`

            - `Optional<List<AllowedCaller>> allowedCallers`

              The tool invocation context(s).

              - `DIRECT("direct")`

              - `PROGRAMMATIC("programmatic")`

        - `JsonValue; type "tool_search_output"constant`

          The item type. Always `tool_search_output`.

          - `TOOL_SEARCH_OUTPUT("tool_search_output")`

        - `Optional<String> id`

          The unique ID of this tool search output.

        - `Optional<String> callId`

          The unique ID of the tool search call generated by the model.

        - `Optional<Execution> execution`

          Whether tool search was executed by the server or by the client.

          - `SERVER("server")`

          - `CLIENT("client")`

        - `Optional<Status> status`

          The status of the tool search output.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `AdditionalTools`

        - `JsonValue; role "developer"constant`

          The role that provided the additional tools. Only `developer` is supported.

          - `DEVELOPER("developer")`

        - `List<Tool> tools`

          A list of additional tools made available at this item.

          - `class FunctionTool:`

            Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

          - `class FileSearchTool:`

            A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

          - `class ComputerTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

          - `class ComputerUsePreviewTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

          - `class WebSearchTool:`

            Search the Internet for sources related to the prompt. Learn more about the
            [web search tool](/api/docs/guides/tools-web-search).

          - `Mcp`

          - `CodeInterpreter`

          - `JsonValue;`

          - `ImageGeneration`

          - `JsonValue;`

          - `class FunctionShellTool:`

            A tool that allows the model to execute shell commands.

          - `class CustomTool:`

            A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

          - `class NamespaceTool:`

            Groups function/custom tools under a shared namespace.

          - `class ToolSearchTool:`

            Hosted or BYOT tool search configuration for deferred tools.

          - `class WebSearchPreviewTool:`

            This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

          - `class ApplyPatchTool:`

            Allows the assistant to create, delete, or update files using unified diffs.

        - `JsonValue; type "additional_tools"constant`

          The item type. Always `additional_tools`.

          - `ADDITIONAL_TOOLS("additional_tools")`

        - `Optional<String> id`

          The unique ID of this additional tools item.

      - `class ResponseConfigurationUpdateItemParam:`

        An update to the conversation's response configuration. The configuration
        remains in effect for subsequent responses until it is replaced by another
        configuration update.

        - `JsonValue; type "configuration_update"constant`

          The item type. Always `configuration_update`.

          - `CONFIGURATION_UPDATE("configuration_update")`

        - `Optional<String> id`

          The unique ID of the configuration update item.

        - `Optional<Reasoning> reasoning`

          Updates to reasoning configuration. Only effort is supported.

          - `Optional<ReasoningEffort> effort`

            The reasoning effort to use for subsequent responses until another
            configuration update replaces it.

            - `NONE("none")`

            - `MINIMAL("minimal")`

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

            - `XHIGH("xhigh")`

            - `MAX("max")`

      - `class ResponseReasoningItem:`

        A description of the chain of thought used by a reasoning model while generating
        a response. Be sure to include these items in your `input` to the Responses API
        for subsequent turns of a conversation if you are manually
        [managing context](/api/docs/guides/conversation-state).

        - `String id`

          The unique identifier of the reasoning content.

        - `List<Summary> summary`

          Reasoning summary content.

          - `String text`

            A summary of the reasoning output from the model so far.

          - `JsonValue; type "summary_text"constant`

            The type of the object. Always `summary_text`.

            - `SUMMARY_TEXT("summary_text")`

        - `JsonValue; type "reasoning"constant`

          The type of the object. Always `reasoning`.

          - `REASONING("reasoning")`

        - `Optional<List<Content>> content`

          Reasoning text content.

          - `String text`

            The reasoning text from the model.

          - `JsonValue; type "reasoning_text"constant`

            The type of the reasoning text. Always `reasoning_text`.

            - `REASONING_TEXT("reasoning_text")`

        - `Optional<String> encryptedContent`

          The encrypted content of the reasoning item. This is populated by default
          for reasoning items returned by `POST /v1/responses` and WebSocket
          `response.create` requests.

          When streaming, use the completed reasoning item and its
          `encrypted_content` from the `response.output_item.done` event in
          subsequent requests. The `encrypted_content` in
          `response.output_item.added` may be incomplete. This is especially
          important when `store` is `false` or when using Zero Data Retention.

        - `Optional<Status> status`

          The status of the item. One of `in_progress`, `completed`, or
          `incomplete`. Populated when items are returned via API.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `class ResponseCompactionItemParam:`

        A compaction item generated by the [`v1/responses/compact` API](/api/reference/resources/responses/methods/compact).

        - `String encryptedContent`

          The encrypted content of the compaction summary.

        - `JsonValue; type "compaction"constant`

          The type of the item. Always `compaction`.

          - `COMPACTION("compaction")`

        - `Optional<String> id`

          The ID of the compaction item.

      - `ImageGenerationCall`

        - `String id`

          The unique ID of the image generation call.

        - `Optional<String> result`

          The generated image encoded in base64.

        - `Status status`

          The status of the image generation call.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `GENERATING("generating")`

          - `FAILED("failed")`

        - `JsonValue; type "image_generation_call"constant`

          The type of the image generation call. Always `image_generation_call`.

          - `IMAGE_GENERATION_CALL("image_generation_call")`

        - `Optional<Action> action`

          The action used for image generation.

          - `GENERATE("generate")`

          - `EDIT("edit")`

          - `AUTO("auto")`

        - `Optional<Background> background`

          The background setting used for generation.

          - `TRANSPARENT("transparent")`

          - `OPAQUE("opaque")`

          - `AUTO("auto")`

        - `Optional<OutputFormat> outputFormat`

          The output format used for generation.

          - `PNG("png")`

          - `WEBP("webp")`

          - `JPEG("jpeg")`

        - `Optional<Quality> quality`

          The quality of the image generated by the image generation tool call. One of `low`, `medium`, `high`, `xhigh`, `max`, or `auto`.

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

          - `MAX("max")`

          - `AUTO("auto")`

        - `Optional<String> revisedPrompt`

          The prompt that was used after any model prompt rewriting.

        - `Optional<Size> size`

          The image dimensions as a `WIDTHxHEIGHT` string, for example `1536x864`.

          - `_1024X1024("1024x1024")`

          - `_1024X1536("1024x1536")`

          - `_1536X1024("1536x1024")`

      - `class ResponseCodeInterpreterToolCall:`

        A tool call to run code.

        - `String id`

          The unique ID of the code interpreter tool call.

        - `Optional<String> code`

          The code to run, or null if not available.

        - `String containerId`

          The ID of the container used to run the code.

        - `Optional<List<Output>> outputs`

          The outputs generated by the code interpreter, such as logs or images.
          Can be null if no outputs are available.

          - `class Logs:`

            The logs output from the code interpreter.

            - `String logs`

              The logs output from the code interpreter.

            - `JsonValue; type "logs"constant`

              The type of the output. Always `logs`.

              - `LOGS("logs")`

          - `class Image:`

            The image output from the code interpreter.

            - `JsonValue; type "image"constant`

              The type of the output. Always `image`.

              - `IMAGE("image")`

            - `String url`

              The URL of the image output from the code interpreter.

        - `Status status`

          The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

          - `INTERPRETING("interpreting")`

          - `FAILED("failed")`

        - `JsonValue; type "code_interpreter_call"constant`

          The type of the code interpreter tool call. Always `code_interpreter_call`.

          - `CODE_INTERPRETER_CALL("code_interpreter_call")`

      - `LocalShellCall`

        - `String id`

          The unique ID of the local shell call.

        - `Action action`

          Execute a shell command on the server.

          - `List<String> command`

            The command to run.

          - `Env env`

            Environment variables to set for the command.

          - `JsonValue; type "exec"constant`

            The type of the local shell action. Always `exec`.

            - `EXEC("exec")`

          - `Optional<Long> timeoutMs`

            Optional timeout in milliseconds for the command.

          - `Optional<String> user`

            Optional user to run the command as.

          - `Optional<String> workingDirectory`

            Optional working directory to run the command in.

        - `String callId`

          The unique ID of the local shell tool call generated by the model.

        - `Status status`

          The status of the local shell call.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

        - `JsonValue; type "local_shell_call"constant`

          The type of the local shell call. Always `local_shell_call`.

          - `LOCAL_SHELL_CALL("local_shell_call")`

      - `LocalShellCallOutput`

        - `String id`

          The unique ID of the local shell tool call generated by the model.

        - `String output`

          A JSON string of the output of the local shell tool call.

        - `JsonValue; type "local_shell_call_output"constant`

          The type of the local shell tool call output. Always `local_shell_call_output`.

          - `LOCAL_SHELL_CALL_OUTPUT("local_shell_call_output")`

        - `Optional<Status> status`

          The status of the item. One of `in_progress`, `completed`, or `incomplete`.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `ShellCall`

        - `Action action`

          The shell commands and limits that describe how to run the tool call.

          - `List<String> commands`

            Ordered shell commands for the execution environment to run.

          - `Optional<Long> maxOutputLength`

            Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

          - `Optional<Long> timeoutMs`

            Maximum wall-clock time in milliseconds to allow the shell commands to run.

        - `String callId`

          The unique ID of the shell tool call generated by the model.

        - `JsonValue; type "shell_call"constant`

          The type of the item. Always `shell_call`.

          - `SHELL_CALL("shell_call")`

        - `Optional<String> id`

          The unique ID of the shell tool call. Populated when this item is returned via API.

        - `Optional<Caller> caller`

          The execution context that produced this tool call.

          - `JsonValue;`

            - `JsonValue; type "direct"constant`

              The caller type. Always `direct`.

              - `DIRECT("direct")`

          - `class Program:`

            - `String callerId`

              The call ID of the program item that produced this tool call.

            - `JsonValue; type "program"constant`

              The caller type. Always `program`.

              - `PROGRAM("program")`

        - `Optional<Environment> environment`

          The environment to execute the shell commands in.

          - `class LocalEnvironment:`

          - `class ContainerReference:`

        - `Optional<Status> status`

          The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `ShellCallOutput`

        - `String callId`

          The unique ID of the shell tool call generated by the model.

        - `List<ResponseFunctionShellCallOutputContent> output`

          Captured chunks of stdout and stderr output, along with their associated outcomes.

          - `Outcome outcome`

            The exit or timeout outcome associated with this shell call.

            - `JsonValue;`

              - `JsonValue; type "timeout"constant`

                The outcome type. Always `timeout`.

                - `TIMEOUT("timeout")`

            - `class Exit:`

              Indicates that the shell commands finished and returned an exit code.

              - `long exitCode`

                The exit code returned by the shell process.

              - `JsonValue; type "exit"constant`

                The outcome type. Always `exit`.

                - `EXIT("exit")`

          - `String stderr`

            Captured stderr output for the shell call.

          - `String stdout`

            Captured stdout output for the shell call.

        - `JsonValue; type "shell_call_output"constant`

          The type of the item. Always `shell_call_output`.

          - `SHELL_CALL_OUTPUT("shell_call_output")`

        - `Optional<String> id`

          The unique ID of the shell tool call output. Populated when this item is returned via API.

        - `Optional<Caller> caller`

          The execution context that produced this tool call.

          - `JsonValue;`

            - `JsonValue; type "direct"constant`

              The caller type. Always `direct`.

              - `DIRECT("direct")`

          - `class Program:`

            - `String callerId`

              The call ID of the program item that produced this tool call.

            - `JsonValue; type "program"constant`

              The caller type. Always `program`.

              - `PROGRAM("program")`

        - `Optional<Long> maxOutputLength`

          The maximum number of UTF-8 characters captured for this shell call's combined output.

        - `Optional<Status> status`

          The status of the shell call output.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `ApplyPatchCall`

        - `String callId`

          The unique ID of the apply patch tool call generated by the model.

        - `Operation operation`

          The specific create, delete, or update instruction for the apply_patch tool call.

          - `class CreateFile:`

            Instruction for creating a new file via the apply_patch tool.

            - `String diff`

              Unified diff content to apply when creating the file.

            - `String path`

              Path of the file to create relative to the workspace root.

            - `JsonValue; type "create_file"constant`

              The operation type. Always `create_file`.

              - `CREATE_FILE("create_file")`

          - `class DeleteFile:`

            Instruction for deleting an existing file via the apply_patch tool.

            - `String path`

              Path of the file to delete relative to the workspace root.

            - `JsonValue; type "delete_file"constant`

              The operation type. Always `delete_file`.

              - `DELETE_FILE("delete_file")`

          - `class UpdateFile:`

            Instruction for updating an existing file via the apply_patch tool.

            - `String diff`

              Unified diff content to apply to the existing file.

            - `String path`

              Path of the file to update relative to the workspace root.

            - `JsonValue; type "update_file"constant`

              The operation type. Always `update_file`.

              - `UPDATE_FILE("update_file")`

        - `Status status`

          The status of the apply patch tool call. One of `in_progress` or `completed`.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

        - `JsonValue; type "apply_patch_call"constant`

          The type of the item. Always `apply_patch_call`.

          - `APPLY_PATCH_CALL("apply_patch_call")`

        - `Optional<String> id`

          The unique ID of the apply patch tool call. Populated when this item is returned via API.

        - `Optional<Caller> caller`

          The execution context that produced this tool call.

          - `JsonValue;`

            - `JsonValue; type "direct"constant`

              The caller type. Always `direct`.

              - `DIRECT("direct")`

          - `class Program:`

            - `String callerId`

              The call ID of the program item that produced this tool call.

            - `JsonValue; type "program"constant`

              The caller type. Always `program`.

              - `PROGRAM("program")`

      - `ApplyPatchCallOutput`

        - `String callId`

          The unique ID of the apply patch tool call generated by the model.

        - `Status status`

          The status of the apply patch tool call output. One of `completed` or `failed`.

          - `COMPLETED("completed")`

          - `FAILED("failed")`

        - `JsonValue; type "apply_patch_call_output"constant`

          The type of the item. Always `apply_patch_call_output`.

          - `APPLY_PATCH_CALL_OUTPUT("apply_patch_call_output")`

        - `Optional<String> id`

          The unique ID of the apply patch tool call output. Populated when this item is returned via API.

        - `Optional<Caller> caller`

          The execution context that produced this tool call.

          - `JsonValue;`

            - `JsonValue; type "direct"constant`

              The caller type. Always `direct`.

              - `DIRECT("direct")`

          - `class Program:`

            - `String callerId`

              The call ID of the program item that produced this tool call.

            - `JsonValue; type "program"constant`

              The caller type. Always `program`.

              - `PROGRAM("program")`

        - `Optional<String> output`

          Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

      - `McpListTools`

        - `String id`

          The unique ID of the list.

        - `String serverLabel`

          The label of the MCP server.

        - `List<Tool> tools`

          The tools available on the server.

          - `JsonValue inputSchema`

            The JSON schema describing the tool's input.

          - `String name`

            The name of the tool.

          - `Optional<JsonValue> annotations`

            Additional annotations about the tool.

          - `Optional<String> description`

            The description of the tool.

        - `JsonValue; type "mcp_list_tools"constant`

          The type of the item. Always `mcp_list_tools`.

          - `MCP_LIST_TOOLS("mcp_list_tools")`

        - `Optional<String> error`

          Error message if the server could not list tools.

      - `McpApprovalRequest`

        - `String id`

          The unique ID of the approval request.

        - `String arguments`

          A JSON string of arguments for the tool.

        - `String name`

          The name of the tool to run.

        - `String serverLabel`

          The label of the MCP server making the request.

        - `JsonValue; type "mcp_approval_request"constant`

          The type of the item. Always `mcp_approval_request`.

          - `MCP_APPROVAL_REQUEST("mcp_approval_request")`

      - `McpApprovalResponse`

        - `String approvalRequestId`

          The ID of the approval request being answered.

        - `boolean approve`

          Whether the request was approved.

        - `JsonValue; type "mcp_approval_response"constant`

          The type of the item. Always `mcp_approval_response`.

          - `MCP_APPROVAL_RESPONSE("mcp_approval_response")`

        - `Optional<String> id`

          The unique ID of the approval response

        - `Optional<String> reason`

          Optional reason for the decision.

      - `McpCall`

        - `String id`

          The unique ID of the tool call.

        - `String arguments`

          A JSON string of the arguments passed to the tool.

        - `String name`

          The name of the tool that was run.

        - `String serverLabel`

          The label of the MCP server running the tool.

        - `JsonValue; type "mcp_call"constant`

          The type of the item. Always `mcp_call`.

          - `MCP_CALL("mcp_call")`

        - `Optional<String> approvalRequestId`

          Unique identifier for the MCP tool call approval request.
          Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

        - `Optional<McpToolCallError> error`

          The error from the tool call, if any.

          - `McpProtocolError`

            - `long code`

            - `String message`

            - `JsonValue; type "mcp_protocol_error"constant`

              - `MCP_PROTOCOL_ERROR("mcp_protocol_error")`

          - `McpToolExecutionError`

            - `JsonValue content`

            - `JsonValue; type "mcp_tool_execution_error"constant`

              - `MCP_TOOL_EXECUTION_ERROR("mcp_tool_execution_error")`

          - `HttpError`

            - `long code`

            - `String message`

            - `JsonValue; type "http_error"constant`

              - `HTTP_ERROR("http_error")`

        - `Optional<String> output`

          The output from the tool call.

        - `Optional<Status> status`

          The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

          - `CALLING("calling")`

          - `FAILED("failed")`

      - `class ResponseCustomToolCallOutput:`

        The output of a custom tool call from your code, being sent back to the model.

        - `String callId`

          The call ID, used to map this custom tool call output to a custom tool call.

        - `Output output`

          The output from the custom tool call generated by your code.
          Can be a string or an list of output content.

          - `String`

          - `List<FunctionAndCustomToolCallOutput>`

            - `class ResponseInputText:`

              A text input to the model.

            - `class ResponseInputImage:`

              An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

            - `class ResponseInputFile:`

              A file input to the model.

        - `JsonValue; type "custom_tool_call_output"constant`

          The type of the custom tool call output. Always `custom_tool_call_output`.

          - `CUSTOM_TOOL_CALL_OUTPUT("custom_tool_call_output")`

        - `Optional<String> id`

          The unique ID of the custom tool call output in the OpenAI platform.

        - `Optional<Caller> caller`

          The execution context that produced this tool call.

          - `JsonValue;`

            - `JsonValue; type "direct"constant`

              The caller type. Always `direct`.

              - `DIRECT("direct")`

          - `class Program:`

            - `String callerId`

              The call ID of the program item that produced this tool call.

            - `JsonValue; type "program"constant`

              The caller type. Always `program`.

              - `PROGRAM("program")`

      - `class ResponseCustomToolCall:`

        A call to a custom tool created by the model.

        - `String callId`

          An identifier used to map this custom tool call to a tool call output.

        - `String input`

          The input for the custom tool call generated by the model.

        - `String name`

          The name of the custom tool being called.

        - `JsonValue; type "custom_tool_call"constant`

          The type of the custom tool call. Always `custom_tool_call`.

          - `CUSTOM_TOOL_CALL("custom_tool_call")`

        - `Optional<String> id`

          The unique ID of the custom tool call in the OpenAI platform.

        - `Optional<Boolean> async`

          Whether the custom tool call runs asynchronously.

        - `Optional<Caller> caller`

          The execution context that produced this tool call.

          - `JsonValue;`

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class Program:`

            - `String callerId`

              The call ID of the program item that produced this tool call.

            - `JsonValue; type "program"constant`

              - `PROGRAM("program")`

        - `Optional<String> namespace`

          The namespace of the custom tool being called.

      - `JsonValue;`

        - `JsonValue; type "compaction_trigger"constant`

          The type of the item. Always `compaction_trigger`.

          - `COMPACTION_TRIGGER("compaction_trigger")`

      - `ItemReference`

        - `String id`

          The ID of the item to reference.

        - `Optional<Type> type`

          The type of item to reference. Always `item_reference`.

          - `ITEM_REFERENCE("item_reference")`

      - `Program`

        - `String id`

          The unique ID of this program item.

        - `String callId`

          The stable call ID of the program item.

        - `String code`

          The JavaScript source executed by programmatic tool calling.

        - `String fingerprint`

          Opaque program replay fingerprint that must be round-tripped.

        - `JsonValue; type "program"constant`

          The item type. Always `program`.

          - `PROGRAM("program")`

      - `ProgramOutput`

        - `String id`

          The unique ID of this program output item.

        - `String callId`

          The call ID of the program item.

        - `String result`

          The result produced by the program item.

        - `Status status`

          The terminal status of the program output.

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

        - `JsonValue; type "program_output"constant`

          The item type. Always `program_output`.

          - `PROGRAM_OUTPUT("program_output")`

    - `JsonValue; type "response.item.create"constant`

      The Live client event type. Always `response.item.create`.

      - `RESPONSE_ITEM_CREATE("response.item.create")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class ResponseCreateEvent:`

    Request a response from the Live session’s Responses backend, or continue a delegated response waiting for tool results. Requires Responses delegation.

    - `JsonValue; type "response.create"constant`

      The Live client event type. Always `response.create`.

      - `RESPONSE_CREATE("response.create")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class SessionCloseEvent:`

    Request that the Live session close. The terminal `session.closed` event contains the close reason and final usage.

    - `JsonValue; type "session.close"constant`

      The Live client event type. Always `session.close`.

      - `SESSION_CLOSE("session.close")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Commentary Append Event

- `class CommentaryAppendEvent:`

  Provide context the Live model can communicate to the user, optionally for an existing client delegation.

  - `String content`

    Speakable context for the Live model, limited to 500 tokens. Use this for a result the model should communicate; use session.thinking.append for silent context.

  - `Optional<String> delegationId`

    Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

  - `JsonValue; type "session.commentary.append"constant`

    The Live client event type. Always `session.commentary.append`.

    - `SESSION_COMMENTARY_APPEND("session.commentary.append")`

  - `Optional<String> eventId`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Commentary Appended Event

- `class CommentaryAppendedEvent:`

  Returned when a session.commentary.append command is accepted into the Live session timeline. Acknowledges the added commentary without guaranteeing exact wording or completed audio playback.

  - `long endMs`

    The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

  - `String eventId`

    The unique ID of the Live server event.

  - `long startMs`

    The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

  - `JsonValue; type "session.commentary.appended"constant`

    The event type, always `session.commentary.appended`.

    - `SESSION_COMMENTARY_APPENDED("session.commentary.appended")`

  - `Optional<String> clientEventId`

    The event_id of the client command associated with this server event, when supplied.

### Custom Voice

- `class CustomVoice:`

  - `String id`

### Data Channel Config

- `class DataChannelConfig:`

  Control which Live events an untrusted WebRTC frontend can send and receive over its data channel. These restrictions do not apply to trusted sideband connections.

  - `Optional<AllowedClientEvents> allowedClientEvents`

    Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

    - `JsonValue;`

      - `ALL("all")`

    - `List<String>`

  - `Optional<AllowedServerEvents> allowedServerEvents`

    Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

    - `JsonValue;`

      - `ALL("all")`

    - `List<ServerEventSelector>`

      - `String type`

        The outer Live server event type. Use 'response.event' for Responses events.

      - `Optional<String> responseEvent`

        The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

### Delegation Created Event

- `class DelegationCreatedEvent:`

  Returned when the Live model delegates work to your application or a Responses backend. Contains delegation metadata and the position on the session timeline where the work was delegated.

  - `Delegation delegation`

    The delegated work identifier and destination. This object contains metadata, not the task text.

    - `String id`

      The unique ID of the delegation. Use this as delegation_id when replying to client-owned work or correlating Responses events.

    - `Target target`

      Where the Live model delegated the work: `client` for your application, or `responses` for the configured Responses backend.

      - `CLIENT("client")`

      - `RESPONSES("responses")`

    - `JsonValue; type "delegation"constant`

      The object type, always `delegation`.

      - `DELEGATION("delegation")`

    - `Optional<String> responseId`

      The ID of the Responses API response associated with a Responses delegation. Omitted for client delegations.

  - `String eventId`

    The unique ID of the Live server event.

  - `long offsetMs`

    The position on the Live session timeline where the delegation was created, in milliseconds from the beginning of the session.

  - `JsonValue; type "session.delegation.created"constant`

    The event type, always `session.delegation.created`.

    - `SESSION_DELEGATION_CREATED("session.delegation.created")`

  - `Optional<String> clientEventId`

    The event_id of the client command associated with this server event, when supplied.

### Error

- `class Error:`

  Details of an error encountered by the Live session, including the affected parameter or client command when available.

  - `String code`

    A machine-readable code identifying the Live error, such as `unknown_parameter`.

  - `String message`

    A human-readable explanation of the Live error.

  - `String type`

    The category of error, such as `invalid_request_error` for an invalid Live client command.

  - `Optional<String> clientEventId`

    The event_id of the client command that caused the error, when supplied.

  - `Optional<String> param`

    The parameter that caused the error, when applicable, such as `session.voice`.

### Error Event

- `class ErrorEvent:`

  Reports an error in the Live session, such as an invalid client command. Use error.client_event_id, when present, to identify the command that caused the error.

  - `Error error`

    Details of the Live error and the client command that caused it, when known.

    - `String code`

      A machine-readable code identifying the Live error, such as `unknown_parameter`.

    - `String message`

      A human-readable explanation of the Live error.

    - `String type`

      The category of error, such as `invalid_request_error` for an invalid Live client command.

    - `Optional<String> clientEventId`

      The event_id of the client command that caused the error, when supplied.

    - `Optional<String> param`

      The parameter that caused the error, when applicable, such as `session.voice`.

  - `String eventId`

    The unique ID of the Live server event.

  - `JsonValue; type "error"constant`

    The event type, always `error`.

    - `ERROR("error")`

  - `Optional<String> clientEventId`

    The event_id of the client command associated with this server event, when supplied.

### Fork Session Config

- `class ForkSessionConfig:`

  Overrides for a stored session after connecting to the fork WebSocket. An empty object inherits the stored configuration; do not supply a new model. audio.format applies only to the new WebSocket connection. client overrides are only supported for WebRTC forks.

  - `Optional<Audio> audio`

    Audio format for a WebSocket fork. WebRTC forks negotiate their audio format and must omit this field.

    - `Optional<AudioFormat> format`

      Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

      - `AudioPcm`

        - `Rate rate`

          Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

          - `_16000(16000)`

          - `_24000(24000)`

        - `JsonValue; type "audio/pcm"constant`

          The audio encoding. Always `audio/pcm`.

          - `AUDIO_PCM("audio/pcm")`

      - `AudioPcmu`

        - `long rate`

          Audio sample rate in hertz. G.711 audio uses 8000 Hz.

        - `JsonValue; type "audio/pcmu"constant`

          The audio encoding. Always `audio/pcmu`.

          - `AUDIO_PCMU("audio/pcmu")`

      - `AudioPcma`

        - `long rate`

          Audio sample rate in hertz. G.711 audio uses 8000 Hz.

        - `JsonValue; type "audio/pcma"constant`

          The audio encoding. Always `audio/pcma`.

          - `AUDIO_PCMA("audio/pcma")`

  - `Optional<ClientConfig> client`

    Frontend data-channel permissions for a WebRTC fork. Omitted permissions inherit the stored values. Not supported for WebSocket forks.

    - `DataChannelConfig dataChannel`

      Client and server event permissions for the WebRTC frontend data channel.

      - `Optional<AllowedClientEvents> allowedClientEvents`

        Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

        - `JsonValue;`

          - `ALL("all")`

        - `List<String>`

      - `Optional<AllowedServerEvents> allowedServerEvents`

        Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

        - `JsonValue;`

          - `ALL("all")`

        - `List<ServerEventSelector>`

          - `String type`

            The outer Live server event type. Use 'response.event' for Responses events.

          - `Optional<String> responseEvent`

            The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

  - `Optional<Delegation> delegation`

    Overrides for the stored session’s Responses backend. Only supported when the stored session already uses Responses delegation; the delegation type cannot change.

    - `JsonValue; type "responses"constant`

      The delegation owner. Always `responses` for tasks handled by the Responses API.

      - `RESPONSES("responses")`

    - `Optional<ResponsesDelegationUpdateConfig> responses`

      Responses backend settings to update. Omitted settings keep their existing values.

      - `Optional<String> instructions`

        Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

      - `Optional<Long> maxOutputTokens`

        Maximum number of output tokens for each delegated response.

      - `Optional<String> model`

        The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.

      - `Optional<Boolean> parallelToolCalls`

        Whether the delegated Responses model may request multiple tool calls in a single response.

      - `Optional<Reasoning> reasoning`

        Reasoning settings passed to each delegated Responses request.

        - `Optional<Effort> effort`

          How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

        - `Optional<Summary> summary`

          The reasoning summary to request from the delegated Responses model, when supported.

          - `CONCISE("concise")`

          - `DETAILED("detailed")`

          - `AUTO("auto")`

      - `Optional<ServiceTier> serviceTier`

        Service tier for delegated Responses requests.

        - `AUTO("auto")`

        - `DEFAULT("default")`

        - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

        - `FLEX("flex")`

        - `PRIORITY("priority")`

        - `ULTRAFAST("ultrafast")`

      - `Optional<Text> text`

        Text generation settings passed to each delegated Responses request.

        - `Optional<Verbosity> verbosity`

          The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

      - `Optional<ToolChoice> toolChoice`

        Controls which tool the Responses backend uses when handling a task delegated by the Live model.

        - `enum LiveToolChoiceEnum:`

          - `AUTO("auto")`

          - `NONE("none")`

          - `REQUIRED("required")`

        - `class LiveFunctionToolChoiceParam:`

          - `String name`

          - `JsonValue; type "function"constant`

            - `FUNCTION("function")`

        - `class LiveMcpToolChoiceParam:`

          - `String name`

          - `String serverLabel`

          - `JsonValue; type "mcp"constant`

            - `MCP("mcp")`

      - `Optional<List<Tool>> tools`

        Tools available to the Responses backend while it handles tasks delegated by the Live model.

        - `class FunctionTool:`

          A function tool available to the Responses backend when the Live model delegates a task.

          - `String name`

            The name the delegated Responses model uses when calling this function.

          - `JsonValue; type "function"constant`

            The tool type. Always `function`.

            - `FUNCTION("function")`

          - `Optional<String> description`

            What the function does and when the delegated Responses model should call it.

          - `Optional<Parameters> parameters`

            A JSON Schema object describing the arguments accepted by the function.

          - `Optional<Boolean> strict`

            Whether the delegated Responses model must follow the function’s parameter schema exactly.

        - `JsonValue;`

          - `JsonValue; type "web_search"constant`

            The tool type. Always `web_search`.

            - `WEB_SEARCH("web_search")`

  - `Optional<Boolean> store`

    Whether to store the forked session. Omission inherits the stored session's setting.

### Fork Session Start Event

- `class ForkSessionStartEvent:`

  Start a Live session after connecting to a stored session’s fork WebSocket. Send an empty `session` object to use the stored configuration.

  - `ForkSessionConfig session`

    Overrides for a stored session after connecting to the fork WebSocket. An empty object inherits the stored configuration; do not supply a new model. audio.format applies only to the new WebSocket connection. client overrides are only supported for WebRTC forks.

    - `Optional<Audio> audio`

      Audio format for a WebSocket fork. WebRTC forks negotiate their audio format and must omit this field.

      - `Optional<AudioFormat> format`

        Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

        - `AudioPcm`

          - `Rate rate`

            Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

            - `_16000(16000)`

            - `_24000(24000)`

          - `JsonValue; type "audio/pcm"constant`

            The audio encoding. Always `audio/pcm`.

            - `AUDIO_PCM("audio/pcm")`

        - `AudioPcmu`

          - `long rate`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `JsonValue; type "audio/pcmu"constant`

            The audio encoding. Always `audio/pcmu`.

            - `AUDIO_PCMU("audio/pcmu")`

        - `AudioPcma`

          - `long rate`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `JsonValue; type "audio/pcma"constant`

            The audio encoding. Always `audio/pcma`.

            - `AUDIO_PCMA("audio/pcma")`

    - `Optional<ClientConfig> client`

      Frontend data-channel permissions for a WebRTC fork. Omitted permissions inherit the stored values. Not supported for WebSocket forks.

      - `DataChannelConfig dataChannel`

        Client and server event permissions for the WebRTC frontend data channel.

        - `Optional<AllowedClientEvents> allowedClientEvents`

          Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

          - `JsonValue;`

            - `ALL("all")`

          - `List<String>`

        - `Optional<AllowedServerEvents> allowedServerEvents`

          Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

          - `JsonValue;`

            - `ALL("all")`

          - `List<ServerEventSelector>`

            - `String type`

              The outer Live server event type. Use 'response.event' for Responses events.

            - `Optional<String> responseEvent`

              The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

    - `Optional<Delegation> delegation`

      Overrides for the stored session’s Responses backend. Only supported when the stored session already uses Responses delegation; the delegation type cannot change.

      - `JsonValue; type "responses"constant`

        The delegation owner. Always `responses` for tasks handled by the Responses API.

        - `RESPONSES("responses")`

      - `Optional<ResponsesDelegationUpdateConfig> responses`

        Responses backend settings to update. Omitted settings keep their existing values.

        - `Optional<String> instructions`

          Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

        - `Optional<Long> maxOutputTokens`

          Maximum number of output tokens for each delegated response.

        - `Optional<String> model`

          The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.

        - `Optional<Boolean> parallelToolCalls`

          Whether the delegated Responses model may request multiple tool calls in a single response.

        - `Optional<Reasoning> reasoning`

          Reasoning settings passed to each delegated Responses request.

          - `Optional<Effort> effort`

            How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

            - `NONE("none")`

            - `MINIMAL("minimal")`

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

            - `XHIGH("xhigh")`

          - `Optional<Summary> summary`

            The reasoning summary to request from the delegated Responses model, when supported.

            - `CONCISE("concise")`

            - `DETAILED("detailed")`

            - `AUTO("auto")`

        - `Optional<ServiceTier> serviceTier`

          Service tier for delegated Responses requests.

          - `AUTO("auto")`

          - `DEFAULT("default")`

          - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

          - `FLEX("flex")`

          - `PRIORITY("priority")`

          - `ULTRAFAST("ultrafast")`

        - `Optional<Text> text`

          Text generation settings passed to each delegated Responses request.

          - `Optional<Verbosity> verbosity`

            The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

        - `Optional<ToolChoice> toolChoice`

          Controls which tool the Responses backend uses when handling a task delegated by the Live model.

          - `enum LiveToolChoiceEnum:`

            - `AUTO("auto")`

            - `NONE("none")`

            - `REQUIRED("required")`

          - `class LiveFunctionToolChoiceParam:`

            - `String name`

            - `JsonValue; type "function"constant`

              - `FUNCTION("function")`

          - `class LiveMcpToolChoiceParam:`

            - `String name`

            - `String serverLabel`

            - `JsonValue; type "mcp"constant`

              - `MCP("mcp")`

        - `Optional<List<Tool>> tools`

          Tools available to the Responses backend while it handles tasks delegated by the Live model.

          - `class FunctionTool:`

            A function tool available to the Responses backend when the Live model delegates a task.

            - `String name`

              The name the delegated Responses model uses when calling this function.

            - `JsonValue; type "function"constant`

              The tool type. Always `function`.

              - `FUNCTION("function")`

            - `Optional<String> description`

              What the function does and when the delegated Responses model should call it.

            - `Optional<Parameters> parameters`

              A JSON Schema object describing the arguments accepted by the function.

            - `Optional<Boolean> strict`

              Whether the delegated Responses model must follow the function’s parameter schema exactly.

          - `JsonValue;`

            - `JsonValue; type "web_search"constant`

              The tool type. Always `web_search`.

              - `WEB_SEARCH("web_search")`

    - `Optional<Boolean> store`

      Whether to store the forked session. Omission inherits the stored session's setting.

  - `JsonValue; type "session.start"constant`

    The Live client event type. Always `session.start`.

    - `SESSION_START("session.start")`

  - `Optional<String> eventId`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Function Tool

- `class FunctionTool:`

  A function tool available to the Responses backend when the Live model delegates a task.

  - `String name`

    The name the delegated Responses model uses when calling this function.

  - `JsonValue; type "function"constant`

    The tool type. Always `function`.

    - `FUNCTION("function")`

  - `Optional<String> description`

    What the function does and when the delegated Responses model should call it.

  - `Optional<Parameters> parameters`

    A JSON Schema object describing the arguments accepted by the function.

  - `Optional<Boolean> strict`

    Whether the delegated Responses model must follow the function’s parameter schema exactly.

### Info Event

- `class InfoEvent:`

  An informational notice about the Live session, such as the event permissions applied to a frontend data channel.

  - `String code`

    A machine-readable code for the notice, such as `data_channel_permissions`.

  - `String eventId`

    The unique ID of the Live server event.

  - `String message`

    A human-readable explanation of the Live session notice.

  - `JsonValue; type "info"constant`

    The event type, always `info`.

    - `INFO("info")`

  - `Optional<String> clientEventId`

    The event_id of the client command associated with this server event, when supplied.

### Initial Item

- `class InitialItem: A class that can be one of several variants.union`

  A developer, user, or assistant message supplied as text history before the Live session starts.

  - `Developer`

    - `List<Content> content`

      The message content. Supply exactly one text part for the initial Live conversation history.

      - `String text`

        The message text to include in the Live session’s initial conversation history.

      - `Optional<Type> type`

        The text content type. Always `input_text`.

        - `INPUT_TEXT("input_text")`

    - `JsonValue; role "developer"constant`

      The author of this history message. Always `developer`.

      - `DEVELOPER("developer")`

    - `Optional<String> id`

      An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

    - `Optional<Status> status`

      The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

      - `INCOMPLETE("incomplete")`

      - `COMPLETED("completed")`

    - `Optional<Type> type`

      The history item type. Always `message`.

      - `MESSAGE("message")`

  - `User`

    - `List<Content> content`

      The message content. Supply exactly one text part for the initial Live conversation history.

      - `String text`

        The message text to include in the Live session’s initial conversation history.

      - `Optional<Type> type`

        The text content type. Always `input_text`.

        - `INPUT_TEXT("input_text")`

    - `JsonValue; role "user"constant`

      The author of this history message. Always `user`.

      - `USER("user")`

    - `Optional<String> id`

      An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

    - `Optional<Status> status`

      The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

      - `INCOMPLETE("incomplete")`

      - `COMPLETED("completed")`

    - `Optional<Type> type`

      The history item type. Always `message`.

      - `MESSAGE("message")`

  - `Assistant`

    - `List<Content> content`

      The message content. Supply exactly one text part for the initial Live conversation history.

      - `class Text:`

        Assistant text supplied as conversation history when starting a Live session.

        - `String text`

          The message text to include in the Live session’s initial conversation history.

        - `Optional<Type> type`

          The text content type. Always `text`.

          - `TEXT("text")`

      - `class OutputText:`

        Assistant output text supplied as conversation history when starting a Live session.

        - `String text`

          The message text to include in the Live session’s initial conversation history.

        - `JsonValue; type "output_text"constant`

          The text content type. Always `output_text`.

          - `OUTPUT_TEXT("output_text")`

    - `JsonValue; role "assistant"constant`

      The author of this history message. Always `assistant`.

      - `ASSISTANT("assistant")`

    - `Optional<String> id`

      An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

    - `Optional<Status> status`

      The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

      - `INCOMPLETE("incomplete")`

      - `COMPLETED("completed")`

    - `Optional<Type> type`

      The history item type. Always `message`.

      - `MESSAGE("message")`

### Input Audio Append Event

- `class InputAudioAppendEvent:`

  Send audio to a Live session over its primary WebSocket. WebRTC and SIP sessions send audio over their media transport.

  - `String audio`

    Base64-encoded raw audio in the startup-selected format, without a WAV or other container header. Primary WebSocket only; media transports use their audio track. Audio appends have no acknowledgment. Reflected sideband server events reuse this event type and audio key, with no timestamps or event_id; their audio is always mono PCM16LE at 24 kHz.

  - `JsonValue; type "session.input_audio.append"constant`

    The Live client event type. Always `session.input_audio.append`.

    - `SESSION_INPUT_AUDIO_APPEND("session.input_audio.append")`

  - `Optional<String> eventId`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Input Audio Mute Event

- `class InputAudioMuteEvent:`

  Mute audio input to the Live model without closing the session. The server acknowledges with `session.input_audio.muted`.

  - `JsonValue; type "session.input_audio.mute"constant`

    The Live client event type. Always `session.input_audio.mute`.

    - `SESSION_INPUT_AUDIO_MUTE("session.input_audio.mute")`

  - `Optional<String> eventId`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Input Audio Muted Event

- `class InputAudioMutedEvent:`

  Returned when a session.input_audio.mute command is accepted. Input audio is no longer sent to the model; sideband audio reflection continues.

  - `String eventId`

    The unique ID of the Live server event.

  - `JsonValue; type "session.input_audio.muted"constant`

    The event type, always `session.input_audio.muted`.

    - `SESSION_INPUT_AUDIO_MUTED("session.input_audio.muted")`

  - `Optional<String> clientEventId`

    The event_id of the client command associated with this server event, when supplied.

### Input Audio Unmute Event

- `class InputAudioUnmuteEvent:`

  Resume audio input to a Live model after muting it. The server acknowledges with `session.input_audio.unmuted`.

  - `JsonValue; type "session.input_audio.unmute"constant`

    The Live client event type. Always `session.input_audio.unmute`.

    - `SESSION_INPUT_AUDIO_UNMUTE("session.input_audio.unmute")`

  - `Optional<String> eventId`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Input Audio Unmuted Event

- `class InputAudioUnmutedEvent:`

  Returned when a session.input_audio.unmute command is accepted. Input audio is sent to the model again.

  - `String eventId`

    The unique ID of the Live server event.

  - `JsonValue; type "session.input_audio.unmuted"constant`

    The event type, always `session.input_audio.unmuted`.

    - `SESSION_INPUT_AUDIO_UNMUTED("session.input_audio.unmuted")`

  - `Optional<String> clientEventId`

    The event_id of the client command associated with this server event, when supplied.

### Input Transcript Delta Event

- `class InputTranscriptDeltaEvent:`

  A transcript fragment for user input audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

  - `String delta`

    The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

  - `long endMs`

    The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

  - `String eventId`

    The unique ID of the Live server event.

  - `long startMs`

    The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

  - `JsonValue; type "session.input_transcript.delta"constant`

    The event type, always `session.input_transcript.delta`.

    - `SESSION_INPUT_TRANSCRIPT_DELTA("session.input_transcript.delta")`

  - `Optional<String> clientEventId`

    The event_id of the client command associated with this server event, when supplied.

### Instructions Append Event

- `class InstructionsAppendEvent:`

  Append instructions to the Live conversation while it is running, optionally associating them with an existing client delegation.

  - `String content`

    Instruction text to append, limited to 500 tokens. This is a plain string, not an array of content parts.

  - `Optional<String> delegationId`

    Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

  - `JsonValue; type "session.instructions.append"constant`

    The Live client event type. Always `session.instructions.append`.

    - `SESSION_INSTRUCTIONS_APPEND("session.instructions.append")`

  - `Optional<String> eventId`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Instructions Appended Event

- `class InstructionsAppendedEvent:`

  Returned when a session.instructions.append command is accepted into the Live session timeline. Acknowledges the appended instructions without guaranteeing that the model has acted on them.

  - `long endMs`

    The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

  - `String eventId`

    The unique ID of the Live server event.

  - `long startMs`

    The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

  - `JsonValue; type "session.instructions.appended"constant`

    The event type, always `session.instructions.appended`.

    - `SESSION_INSTRUCTIONS_APPENDED("session.instructions.appended")`

  - `Optional<String> clientEventId`

    The event_id of the client command associated with this server event, when supplied.

### Media Session Config

- `class MediaSessionConfig:`

  Startup configuration for a Live media session. Follow the [Live prompting guide](https://developers.openai.com/api/docs/guides/live-prompting) when writing frontend instructions and the backend prompt under delegation.responses.instructions.

  - `Model model`

    The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

    - `GPT_LIVE_1("gpt-live-1")`

  - `Optional<Audio> audio`

    Startup audio configuration. WebRTC and SIP negotiate their audio format on the media transport.

    - `Optional<Output> output`

      Settings for speech generated by the Live model. Choose the voice before starting the session.

      - `Optional<Voice> voice`

        The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

        - `String`

        - `enum BuiltInVoice:`

          A built-in voice available for Live speech.

          - `ALLOY("alloy")`

          - `ASH("ash")`

          - `BALLAD("ballad")`

          - `BEACON("beacon")`

          - `BOSSA("bossa")`

          - `CEDAR("cedar")`

          - `CINDER("cinder")`

          - `CORAL("coral")`

          - `DELTA("delta")`

          - `ECHO("echo")`

          - `GLEAM("gleam")`

          - `MARIN("marin")`

          - `MERIDIAN("meridian")`

          - `QUARTZ("quartz")`

          - `RIPPLE("ripple")`

          - `SAGE("sage")`

          - `SHIMMER("shimmer")`

          - `STONE("stone")`

          - `TEMPO("tempo")`

          - `VERSE("verse")`

          - `VESPER("vesper")`

          - `WILLOW("willow")`

        - `class CustomVoice:`

          - `String id`

  - `Optional<ClientConfig> client`

    Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

    - `DataChannelConfig dataChannel`

      Client and server event permissions for the WebRTC frontend data channel.

      - `Optional<AllowedClientEvents> allowedClientEvents`

        Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

        - `JsonValue;`

          - `ALL("all")`

        - `List<String>`

      - `Optional<AllowedServerEvents> allowedServerEvents`

        Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

        - `JsonValue;`

          - `ALL("all")`

        - `List<ServerEventSelector>`

          - `String type`

            The outer Live server event type. Use 'response.event' for Responses events.

          - `Optional<String> responseEvent`

            The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

  - `Optional<Delegation> delegation`

    Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

    - `class ClientDelegation:`

      Delegate tasks to your application. The Live session emits delegation events that your backend handles.

      - `JsonValue; type "client"constant`

        The delegation owner. Always `client` for tasks handled by your application.

        - `CLIENT("client")`

    - `class Responses:`

      Delegate tasks to a Responses model managed by the Live session.

      - `ResponsesDelegationConfig responses`

        Backend model, prompt, and tools used when the Live session delegates a task to Responses.

        - `String model`

          The model used for server-owned Responses delegations.

        - `Optional<String> instructions`

          Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

        - `Optional<Long> maxOutputTokens`

          Maximum number of output tokens for each delegated response.

        - `Optional<Boolean> parallelToolCalls`

          Whether the delegated Responses model may request multiple tool calls in a single response.

        - `Optional<Reasoning> reasoning`

          Reasoning settings passed to each delegated Responses request.

          - `Optional<Effort> effort`

            How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

            - `NONE("none")`

            - `MINIMAL("minimal")`

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

            - `XHIGH("xhigh")`

          - `Optional<Summary> summary`

            The reasoning summary to request from the delegated Responses model, when supported.

            - `CONCISE("concise")`

            - `DETAILED("detailed")`

            - `AUTO("auto")`

        - `Optional<ServiceTier> serviceTier`

          Service tier for delegated Responses requests.

          - `AUTO("auto")`

          - `DEFAULT("default")`

          - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

          - `FLEX("flex")`

          - `PRIORITY("priority")`

          - `ULTRAFAST("ultrafast")`

        - `Optional<Text> text`

          Text generation settings passed to each delegated Responses request.

          - `Optional<Verbosity> verbosity`

            The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

        - `Optional<ToolChoice> toolChoice`

          Controls which tool the Responses backend uses when handling a task delegated by the Live model.

          - `enum LiveToolChoiceEnum:`

            - `AUTO("auto")`

            - `NONE("none")`

            - `REQUIRED("required")`

          - `class LiveFunctionToolChoiceParam:`

            - `String name`

            - `JsonValue; type "function"constant`

              - `FUNCTION("function")`

          - `class LiveMcpToolChoiceParam:`

            - `String name`

            - `String serverLabel`

            - `JsonValue; type "mcp"constant`

              - `MCP("mcp")`

        - `Optional<List<Tool>> tools`

          Tools available to the Responses backend while it handles tasks delegated by the Live model.

          - `class FunctionTool:`

            A function tool available to the Responses backend when the Live model delegates a task.

            - `String name`

              The name the delegated Responses model uses when calling this function.

            - `JsonValue; type "function"constant`

              The tool type. Always `function`.

              - `FUNCTION("function")`

            - `Optional<String> description`

              What the function does and when the delegated Responses model should call it.

            - `Optional<Parameters> parameters`

              A JSON Schema object describing the arguments accepted by the function.

            - `Optional<Boolean> strict`

              Whether the delegated Responses model must follow the function’s parameter schema exactly.

          - `JsonValue;`

            - `JsonValue; type "web_search"constant`

              The tool type. Always `web_search`.

              - `WEB_SEARCH("web_search")`

      - `JsonValue; type "responses"constant`

        The delegation owner. Always `responses` for tasks handled by the Responses API.

        - `RESPONSES("responses")`

  - `Optional<List<InitialItem>> input`

    Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

    - `Developer`

      - `List<Content> content`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `String text`

          The message text to include in the Live session’s initial conversation history.

        - `Optional<Type> type`

          The text content type. Always `input_text`.

          - `INPUT_TEXT("input_text")`

      - `JsonValue; role "developer"constant`

        The author of this history message. Always `developer`.

        - `DEVELOPER("developer")`

      - `Optional<String> id`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Optional<Status> status`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `INCOMPLETE("incomplete")`

        - `COMPLETED("completed")`

      - `Optional<Type> type`

        The history item type. Always `message`.

        - `MESSAGE("message")`

    - `User`

      - `List<Content> content`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `String text`

          The message text to include in the Live session’s initial conversation history.

        - `Optional<Type> type`

          The text content type. Always `input_text`.

          - `INPUT_TEXT("input_text")`

      - `JsonValue; role "user"constant`

        The author of this history message. Always `user`.

        - `USER("user")`

      - `Optional<String> id`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Optional<Status> status`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `INCOMPLETE("incomplete")`

        - `COMPLETED("completed")`

      - `Optional<Type> type`

        The history item type. Always `message`.

        - `MESSAGE("message")`

    - `Assistant`

      - `List<Content> content`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `class Text:`

          Assistant text supplied as conversation history when starting a Live session.

          - `String text`

            The message text to include in the Live session’s initial conversation history.

          - `Optional<Type> type`

            The text content type. Always `text`.

            - `TEXT("text")`

        - `class OutputText:`

          Assistant output text supplied as conversation history when starting a Live session.

          - `String text`

            The message text to include in the Live session’s initial conversation history.

          - `JsonValue; type "output_text"constant`

            The text content type. Always `output_text`.

            - `OUTPUT_TEXT("output_text")`

      - `JsonValue; role "assistant"constant`

        The author of this history message. Always `assistant`.

        - `ASSISTANT("assistant")`

      - `Optional<String> id`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Optional<Status> status`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `INCOMPLETE("incomplete")`

        - `COMPLETED("completed")`

      - `Optional<Type> type`

        The history item type. Always `message`.

        - `MESSAGE("message")`

  - `Optional<String> instructions`

    Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

  - `Optional<Boolean> store`

    Whether to store the session for later forking and recording download. Defaults to false for new sessions.

### Media Session Fork Config

- `class MediaSessionForkConfig:`

  Optional overrides for a stored Live session. Omitted settings are inherited. The model, voice, frontend instructions, and prior conversation come from the stored session. WebRTC negotiates its audio format; audio.format is only supported on WebSocket forks.

  - `Optional<ClientConfig> client`

    Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

    - `DataChannelConfig dataChannel`

      Client and server event permissions for the WebRTC frontend data channel.

      - `Optional<AllowedClientEvents> allowedClientEvents`

        Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

        - `JsonValue;`

          - `ALL("all")`

        - `List<String>`

      - `Optional<AllowedServerEvents> allowedServerEvents`

        Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

        - `JsonValue;`

          - `ALL("all")`

        - `List<ServerEventSelector>`

          - `String type`

            The outer Live server event type. Use 'response.event' for Responses events.

          - `Optional<String> responseEvent`

            The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

  - `Optional<Delegation> delegation`

    Update the Responses backend for an existing Live session without changing delegation ownership.

    - `JsonValue; type "responses"constant`

      The delegation owner. Always `responses` for tasks handled by the Responses API.

      - `RESPONSES("responses")`

    - `Optional<ResponsesDelegationUpdateConfig> responses`

      Responses backend settings to update. Omitted settings keep their existing values.

      - `Optional<String> instructions`

        Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

      - `Optional<Long> maxOutputTokens`

        Maximum number of output tokens for each delegated response.

      - `Optional<String> model`

        The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.

      - `Optional<Boolean> parallelToolCalls`

        Whether the delegated Responses model may request multiple tool calls in a single response.

      - `Optional<Reasoning> reasoning`

        Reasoning settings passed to each delegated Responses request.

        - `Optional<Effort> effort`

          How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

        - `Optional<Summary> summary`

          The reasoning summary to request from the delegated Responses model, when supported.

          - `CONCISE("concise")`

          - `DETAILED("detailed")`

          - `AUTO("auto")`

      - `Optional<ServiceTier> serviceTier`

        Service tier for delegated Responses requests.

        - `AUTO("auto")`

        - `DEFAULT("default")`

        - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

        - `FLEX("flex")`

        - `PRIORITY("priority")`

        - `ULTRAFAST("ultrafast")`

      - `Optional<Text> text`

        Text generation settings passed to each delegated Responses request.

        - `Optional<Verbosity> verbosity`

          The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

      - `Optional<ToolChoice> toolChoice`

        Controls which tool the Responses backend uses when handling a task delegated by the Live model.

        - `enum LiveToolChoiceEnum:`

          - `AUTO("auto")`

          - `NONE("none")`

          - `REQUIRED("required")`

        - `class LiveFunctionToolChoiceParam:`

          - `String name`

          - `JsonValue; type "function"constant`

            - `FUNCTION("function")`

        - `class LiveMcpToolChoiceParam:`

          - `String name`

          - `String serverLabel`

          - `JsonValue; type "mcp"constant`

            - `MCP("mcp")`

      - `Optional<List<Tool>> tools`

        Tools available to the Responses backend while it handles tasks delegated by the Live model.

        - `class FunctionTool:`

          A function tool available to the Responses backend when the Live model delegates a task.

          - `String name`

            The name the delegated Responses model uses when calling this function.

          - `JsonValue; type "function"constant`

            The tool type. Always `function`.

            - `FUNCTION("function")`

          - `Optional<String> description`

            What the function does and when the delegated Responses model should call it.

          - `Optional<Parameters> parameters`

            A JSON Schema object describing the arguments accepted by the function.

          - `Optional<Boolean> strict`

            Whether the delegated Responses model must follow the function’s parameter schema exactly.

        - `JsonValue;`

          - `JsonValue; type "web_search"constant`

            The tool type. Always `web_search`.

            - `WEB_SEARCH("web_search")`

  - `Optional<Boolean> store`

    Whether to store the forked session. Omission inherits the stored session's setting.

### Output Audio Delta Event

- `class OutputAudioDeltaEvent:`

  An audio chunk generated by the Live model. Decode and play primary WebSocket chunks in delivery order using the configured session audio format. Sideband connections receive reflected output audio with timestamps.

  - `String delta`

    Base64-encoded raw audio. Primary WebSocket events use the session's configured format; reflected sideband events use mono PCM16LE at 24 kHz.

  - `JsonValue; type "session.output_audio.delta"constant`

    The event type, always `session.output_audio.delta`.

    - `SESSION_OUTPUT_AUDIO_DELTA("session.output_audio.delta")`

  - `Optional<Long> endMs`

    Exclusive session-relative end in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket. Dropped output frames leave gaps between reflected ranges.

  - `Optional<Long> startMs`

    Inclusive session-relative start in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket.

### Output Transcript Delta Event

- `class OutputTranscriptDeltaEvent:`

  A transcript fragment for assistant output audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

  - `String delta`

    The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

  - `long endMs`

    The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

  - `String eventId`

    The unique ID of the Live server event.

  - `long startMs`

    The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

  - `JsonValue; type "session.output_transcript.delta"constant`

    The event type, always `session.output_transcript.delta`.

    - `SESSION_OUTPUT_TRANSCRIPT_DELTA("session.output_transcript.delta")`

  - `Optional<String> clientEventId`

    The event_id of the client command associated with this server event, when supplied.

### Response Create Event

- `class ResponseCreateEvent:`

  Request a response from the Live session’s Responses backend, or continue a delegated response waiting for tool results. Requires Responses delegation.

  - `JsonValue; type "response.create"constant`

    The Live client event type. Always `response.create`.

    - `RESPONSE_CREATE("response.create")`

  - `Optional<String> eventId`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Response Event

- `class ResponseEvent:`

  A streaming Responses API event from a backend delegated to by the Live session. Use the outer delegation_id to associate the nested stream with its Live delegation.

  - `Event event`

    The nested Responses streaming event. Dispatch on its type field. Response lifecycle snapshots omit input and clear instructions, tools, and output to keep messages small; consume granular output events for the generated content.

  - `String eventId`

    The unique ID of the Live server event.

  - `JsonValue; type "response.event"constant`

    The event type, always `response.event`.

    - `RESPONSE_EVENT("response.event")`

  - `Optional<String> clientEventId`

    The event_id of the client command associated with this server event, when supplied.

  - `Optional<String> delegationId`

    The Live delegation associated with the nested Responses event. May be null or omitted when the event cannot be correlated with a delegation.

### Response Item Create Event

- `class ResponseItemCreateEvent:`

  Add an input item to the Live session’s Responses backend. Requires Responses delegation; use `response.create` to request a response.

  - `ResponseInputItem item`

    An input item to append to the Responses backend conversation, such as a user message or a function tool result.

    - `class EasyInputMessage:`

      A message input to the model with a role indicating instruction following
      hierarchy. Instructions given with the `developer` or `system` role take
      precedence over instructions given with the `user` role. Messages with the
      `assistant` role are presumed to have been generated by the model in previous
      interactions.

      - `Content content`

        Text, image, or audio input to the model, used to generate a response.
        Can also contain previous assistant responses.

        - `String`

        - `List<ResponseInputContent>`

          - `class ResponseInputText:`

            A text input to the model.

            - `String text`

              The text input to the model.

            - `JsonValue; type "input_text"constant`

              The type of the input item. Always `input_text`.

              - `INPUT_TEXT("input_text")`

            - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

              Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

              - `JsonValue; mode "explicit"constant`

                The breakpoint mode. Always `explicit`.

                - `EXPLICIT("explicit")`

          - `class ResponseInputImage:`

            An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

            - `Detail detail`

              The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

              - `LOW("low")`

              - `HIGH("high")`

              - `AUTO("auto")`

              - `ORIGINAL("original")`

            - `JsonValue; type "input_image"constant`

              The type of the input item. Always `input_image`.

              - `INPUT_IMAGE("input_image")`

            - `Optional<String> fileId`

              The ID of the file to be sent to the model.

            - `Optional<String> imageUrl`

              The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

            - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

              Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

              - `JsonValue; mode "explicit"constant`

                The breakpoint mode. Always `explicit`.

                - `EXPLICIT("explicit")`

          - `class ResponseInputFile:`

            A file input to the model.

            - `JsonValue; type "input_file"constant`

              The type of the input item. Always `input_file`.

              - `INPUT_FILE("input_file")`

            - `Optional<Detail> detail`

              The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

            - `Optional<String> fileData`

              The content of the file to be sent to the model.

            - `Optional<String> fileId`

              The ID of the file to be sent to the model.

            - `Optional<String> fileUrl`

              The URL of the file to be sent to the model.

            - `Optional<String> filename`

              The name of the file to be sent to the model.

            - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

              Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

              - `JsonValue; mode "explicit"constant`

                The breakpoint mode. Always `explicit`.

                - `EXPLICIT("explicit")`

      - `Role role`

        The role of the message input. One of `user`, `assistant`, `system`, or
        `developer`.

        - `USER("user")`

        - `ASSISTANT("assistant")`

        - `SYSTEM("system")`

        - `DEVELOPER("developer")`

      - `Optional<Phase> phase`

        Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
        For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
        phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

        - `COMMENTARY("commentary")`

        - `FINAL_ANSWER("final_answer")`

      - `Optional<Type> type`

        The type of the message input. Always `message`.

        - `MESSAGE("message")`

    - `Message`

      - `List<ResponseInputContent> content`

        A list of one or many input items to the model, containing different content
        types.

        - `class ResponseInputText:`

          A text input to the model.

        - `class ResponseInputImage:`

          An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

        - `class ResponseInputFile:`

          A file input to the model.

      - `Role role`

        The role of the message input. One of `user`, `system`, or `developer`.

        - `USER("user")`

        - `SYSTEM("system")`

        - `DEVELOPER("developer")`

      - `Optional<Status> status`

        The status of item. One of `in_progress`, `completed`, or
        `incomplete`. Populated when items are returned via API.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

      - `Optional<Type> type`

        The type of the message input. Always set to `message`.

        - `MESSAGE("message")`

    - `class ResponseOutputMessage:`

      An output message from the model.

      - `String id`

        The unique ID of the output message.

      - `List<Content> content`

        The content of the output message.

        - `class ResponseOutputText:`

          A text output from the model.

          - `List<Annotation> annotations`

            The annotations of the text output.

            - `class FileCitation:`

              A citation to a file.

              - `String fileId`

                The ID of the file.

              - `String filename`

                The filename of the file cited.

              - `long index`

                The index in the output text at which to insert the file citation.

              - `JsonValue; type "file_citation"constant`

                The type of the file citation. Always `file_citation`.

                - `FILE_CITATION("file_citation")`

            - `class UrlCitation:`

              A citation for a web resource used to generate a model response.

              - `long endIndex`

                The index of the last character of the URL citation in the message.

              - `long startIndex`

                The index of the first character of the URL citation in the message.

              - `String title`

                The title of the web resource.

              - `JsonValue; type "url_citation"constant`

                The type of the URL citation. Always `url_citation`.

                - `URL_CITATION("url_citation")`

              - `String url`

                The URL of the web resource.

            - `class ContainerFileCitation:`

              A citation for a container file used to generate a model response.

              - `String containerId`

                The ID of the container file.

              - `long endIndex`

                The index of the last character of the container file citation in the message.

              - `String fileId`

                The ID of the file.

              - `String filename`

                The filename of the container file cited.

              - `long startIndex`

                The index of the first character of the container file citation in the message.

              - `JsonValue; type "container_file_citation"constant`

                The type of the container file citation. Always `container_file_citation`.

                - `CONTAINER_FILE_CITATION("container_file_citation")`

            - `class FilePath:`

              A path to a file.

              - `String fileId`

                The ID of the file.

              - `long index`

                The index of the file in the list of files.

              - `JsonValue; type "file_path"constant`

                The type of the file path. Always `file_path`.

                - `FILE_PATH("file_path")`

          - `String text`

            The text output from the model.

          - `JsonValue; type "output_text"constant`

            The type of the output text. Always `output_text`.

            - `OUTPUT_TEXT("output_text")`

          - `Optional<List<Logprob>> logprobs`

            - `String token`

            - `List<long> bytes`

            - `double logprob`

            - `List<TopLogprob> topLogprobs`

              - `String token`

              - `List<long> bytes`

              - `double logprob`

        - `class ResponseOutputRefusal:`

          A refusal from the model.

          - `String refusal`

            The refusal explanation from the model.

          - `JsonValue; type "refusal"constant`

            The type of the refusal. Always `refusal`.

            - `REFUSAL("refusal")`

      - `JsonValue; role "assistant"constant`

        The role of the output message. Always `assistant`.

        - `ASSISTANT("assistant")`

      - `Status status`

        The status of the message input. One of `in_progress`, `completed`, or
        `incomplete`. Populated when input items are returned via API.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

      - `JsonValue; type "message"constant`

        The type of the output message. Always `message`.

        - `MESSAGE("message")`

      - `Optional<Phase> phase`

        Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
        For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
        phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

        - `COMMENTARY("commentary")`

        - `FINAL_ANSWER("final_answer")`

    - `class ResponseFileSearchToolCall:`

      The results of a file search tool call. See the
      [file search guide](/api/docs/guides/tools-file-search) for more information.

      - `String id`

        The unique ID of the file search tool call.

      - `List<String> queries`

        The queries used to search for files.

      - `Status status`

        The status of the file search tool call. One of `in_progress`,
        `searching`, `incomplete` or `failed`,

        - `IN_PROGRESS("in_progress")`

        - `SEARCHING("searching")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `FAILED("failed")`

      - `JsonValue; type "file_search_call"constant`

        The type of the file search tool call. Always `file_search_call`.

        - `FILE_SEARCH_CALL("file_search_call")`

      - `Optional<List<Result>> results`

        The results of the file search tool call.

        - `Optional<Attributes> attributes`

          Set of 16 key-value pairs that can be attached to an object. This can be
          useful for storing additional information about the object in a structured
          format, and querying for objects via API or the dashboard. Keys are strings
          with a maximum length of 64 characters. Values are strings with a maximum
          length of 512 characters, booleans, or numbers.

          - `String`

          - `double`

          - `boolean`

        - `Optional<String> fileId`

          The unique ID of the file.

        - `Optional<String> filename`

          The name of the file.

        - `Optional<Double> score`

          The relevance score of the file - a value between 0 and 1.

        - `Optional<String> text`

          The text that was retrieved from the file.

    - `class ResponseComputerToolCall:`

      A tool call to a computer use tool. See the
      [computer use guide](/api/docs/guides/tools-computer-use) for more information.

      - `String id`

        The unique ID of the computer call.

      - `String callId`

        An identifier used when responding to the tool call with output.

      - `List<PendingSafetyCheck> pendingSafetyChecks`

        The pending safety checks for the computer call.

        - `String id`

          The ID of the pending safety check.

        - `Optional<String> code`

          The type of the pending safety check.

        - `Optional<String> message`

          Details about the pending safety check.

      - `Status status`

        The status of the item. One of `in_progress`, `completed`, or
        `incomplete`. Populated when items are returned via API.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

      - `Type type`

        The type of the computer call. Always `computer_call`.

        - `COMPUTER_CALL("computer_call")`

      - `Optional<Action> action`

        A click action.

        - `class Click:`

          A click action.

          - `Button button`

            Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

            - `LEFT("left")`

            - `RIGHT("right")`

            - `WHEEL("wheel")`

            - `BACK("back")`

            - `FORWARD("forward")`

          - `JsonValue; type "click"constant`

            Specifies the event type. For a click action, this property is always `click`.

            - `CLICK("click")`

          - `long x`

            The x-coordinate where the click occurred.

          - `long y`

            The y-coordinate where the click occurred.

          - `Optional<List<String>> keys`

            The keys being held while clicking.

        - `class DoubleClick:`

          A double click action.

          - `Optional<List<String>> keys`

            The keys being held while double-clicking.

          - `JsonValue; type "double_click"constant`

            Specifies the event type. For a double click action, this property is always set to `double_click`.

            - `DOUBLE_CLICK("double_click")`

          - `long x`

            The x-coordinate where the double click occurred.

          - `long y`

            The y-coordinate where the double click occurred.

        - `class Drag:`

          A drag action.

          - `List<Path> path`

            An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

            ```
            [
              { x: 100, y: 200 },
              { x: 200, y: 300 }
            ]
            ```

            - `long x`

              The x-coordinate.

            - `long y`

              The y-coordinate.

          - `JsonValue; type "drag"constant`

            Specifies the event type. For a drag action, this property is always set to `drag`.

            - `DRAG("drag")`

          - `Optional<List<String>> keys`

            The keys being held while dragging the mouse.

        - `class Keypress:`

          A collection of keypresses the model would like to perform.

          - `List<String> keys`

            The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

          - `JsonValue; type "keypress"constant`

            Specifies the event type. For a keypress action, this property is always set to `keypress`.

            - `KEYPRESS("keypress")`

        - `class Move:`

          A mouse move action.

          - `JsonValue; type "move"constant`

            Specifies the event type. For a move action, this property is always set to `move`.

            - `MOVE("move")`

          - `long x`

            The x-coordinate to move to.

          - `long y`

            The y-coordinate to move to.

          - `Optional<List<String>> keys`

            The keys being held while moving the mouse.

        - `JsonValue;`

          - `JsonValue; type "screenshot"constant`

            Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

            - `SCREENSHOT("screenshot")`

        - `class Scroll:`

          A scroll action.

          - `long scrollX`

            The horizontal scroll distance.

          - `long scrollY`

            The vertical scroll distance.

          - `JsonValue; type "scroll"constant`

            Specifies the event type. For a scroll action, this property is always set to `scroll`.

            - `SCROLL("scroll")`

          - `long x`

            The x-coordinate where the scroll occurred.

          - `long y`

            The y-coordinate where the scroll occurred.

          - `Optional<List<String>> keys`

            The keys being held while scrolling.

        - `class Type:`

          An action to type in text.

          - `String text`

            The text to type.

          - `JsonValue; type "type"constant`

            Specifies the event type. For a type action, this property is always set to `type`.

            - `TYPE("type")`

        - `JsonValue;`

          - `JsonValue; type "wait"constant`

            Specifies the event type. For a wait action, this property is always set to `wait`.

            - `WAIT("wait")`

      - `Optional<List<ComputerAction>> actions`

        Flattened batched actions for `computer_use`. Each action includes an
        `type` discriminator and action-specific fields.

        - `Click`

          - `Button button`

            Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

            - `LEFT("left")`

            - `RIGHT("right")`

            - `WHEEL("wheel")`

            - `BACK("back")`

            - `FORWARD("forward")`

          - `JsonValue; type "click"constant`

            Specifies the event type. For a click action, this property is always `click`.

            - `CLICK("click")`

          - `long x`

            The x-coordinate where the click occurred.

          - `long y`

            The y-coordinate where the click occurred.

          - `Optional<List<String>> keys`

            The keys being held while clicking.

        - `DoubleClick`

          - `Optional<List<String>> keys`

            The keys being held while double-clicking.

          - `JsonValue; type "double_click"constant`

            Specifies the event type. For a double click action, this property is always set to `double_click`.

            - `DOUBLE_CLICK("double_click")`

          - `long x`

            The x-coordinate where the double click occurred.

          - `long y`

            The y-coordinate where the double click occurred.

        - `Drag`

          - `List<Path> path`

            An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

            ```
            [
              { x: 100, y: 200 },
              { x: 200, y: 300 }
            ]
            ```

            - `long x`

              The x-coordinate.

            - `long y`

              The y-coordinate.

          - `JsonValue; type "drag"constant`

            Specifies the event type. For a drag action, this property is always set to `drag`.

            - `DRAG("drag")`

          - `Optional<List<String>> keys`

            The keys being held while dragging the mouse.

        - `Keypress`

          - `List<String> keys`

            The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

          - `JsonValue; type "keypress"constant`

            Specifies the event type. For a keypress action, this property is always set to `keypress`.

            - `KEYPRESS("keypress")`

        - `Move`

          - `JsonValue; type "move"constant`

            Specifies the event type. For a move action, this property is always set to `move`.

            - `MOVE("move")`

          - `long x`

            The x-coordinate to move to.

          - `long y`

            The y-coordinate to move to.

          - `Optional<List<String>> keys`

            The keys being held while moving the mouse.

        - `JsonValue;`

          - `JsonValue; type "screenshot"constant`

            Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

            - `SCREENSHOT("screenshot")`

        - `Scroll`

          - `long scrollX`

            The horizontal scroll distance.

          - `long scrollY`

            The vertical scroll distance.

          - `JsonValue; type "scroll"constant`

            Specifies the event type. For a scroll action, this property is always set to `scroll`.

            - `SCROLL("scroll")`

          - `long x`

            The x-coordinate where the scroll occurred.

          - `long y`

            The y-coordinate where the scroll occurred.

          - `Optional<List<String>> keys`

            The keys being held while scrolling.

        - `Type`

          - `String text`

            The text to type.

          - `JsonValue; type "type"constant`

            Specifies the event type. For a type action, this property is always set to `type`.

            - `TYPE("type")`

        - `JsonValue;`

          - `JsonValue; type "wait"constant`

            Specifies the event type. For a wait action, this property is always set to `wait`.

            - `WAIT("wait")`

    - `ComputerCallOutput`

      - `String callId`

        The ID of the computer tool call that produced the output.

      - `ResponseComputerToolCallOutputScreenshot output`

        A computer screenshot image used with the computer use tool.

        - `JsonValue; type "computer_screenshot"constant`

          Specifies the event type. For a computer screenshot, this property is
          always set to `computer_screenshot`.

          - `COMPUTER_SCREENSHOT("computer_screenshot")`

        - `Optional<String> fileId`

          The identifier of an uploaded file that contains the screenshot.

        - `Optional<String> imageUrl`

          The URL of the screenshot image.

      - `JsonValue; type "computer_call_output"constant`

        The type of the computer tool call output. Always `computer_call_output`.

        - `COMPUTER_CALL_OUTPUT("computer_call_output")`

      - `Optional<String> id`

        The ID of the computer tool call output.

      - `Optional<List<AcknowledgedSafetyCheck>> acknowledgedSafetyChecks`

        The safety checks reported by the API that have been acknowledged by the developer.

        - `String id`

          The ID of the pending safety check.

        - `Optional<String> code`

          The type of the pending safety check.

        - `Optional<String> message`

          Details about the pending safety check.

      - `Optional<Status> status`

        The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

    - `class ResponseFunctionWebSearch:`

      The results of a web search tool call. See the
      [web search guide](/api/docs/guides/tools-web-search) for more information.

      - `String id`

        The unique ID of the web search tool call.

      - `Action action`

        An object describing the specific action taken in this web search call.
        Includes details on how the model used the web (search, open_page, find_in_page).

        - `class Search:`

          Action type "search" - Performs a web search query.

          - `JsonValue; type "search"constant`

            The action type.

            - `SEARCH("search")`

          - `Optional<List<String>> queries`

            The search queries.

          - `Optional<String> query`

            The search query.

          - `Optional<List<Source>> sources`

            The sources used in the search.

            - `JsonValue; type "url"constant`

              The type of source. Always `url`.

              - `URL("url")`

            - `String url`

              The URL of the source.

        - `class OpenPage:`

          Action type "open_page" - Opens a specific URL from search results.

          - `JsonValue; type "open_page"constant`

            The action type.

            - `OPEN_PAGE("open_page")`

          - `Optional<String> url`

            The URL opened by the model.

        - `class FindInPage:`

          Action type "find_in_page": Searches for a pattern within a loaded page.

          - `String pattern`

            The pattern or text to search for within the page.

          - `JsonValue; type "find_in_page"constant`

            The action type.

            - `FIND_IN_PAGE("find_in_page")`

          - `String url`

            The URL of the page searched for the pattern.

      - `Status status`

        The status of the web search tool call.

        - `IN_PROGRESS("in_progress")`

        - `SEARCHING("searching")`

        - `COMPLETED("completed")`

        - `FAILED("failed")`

        - `INCOMPLETE("incomplete")`

      - `JsonValue; type "web_search_call"constant`

        The type of the web search tool call. Always `web_search_call`.

        - `WEB_SEARCH_CALL("web_search_call")`

    - `class ResponseFunctionToolCall:`

      A tool call to run a function. See the
      [function calling guide](/api/docs/guides/function-calling) for more information.

      - `String arguments`

        A JSON string of the arguments to pass to the function.

      - `String callId`

        The unique ID of the function tool call generated by the model.

      - `String name`

        The name of the function to run.

      - `JsonValue; type "function_call"constant`

        The type of the function tool call. Always `function_call`.

        - `FUNCTION_CALL("function_call")`

      - `Optional<String> id`

        The unique ID of the function tool call.

      - `Optional<Boolean> async`

        Whether the function tool call runs asynchronously.

      - `Optional<Caller> caller`

        The execution context that produced this tool call.

        - `JsonValue;`

          - `JsonValue; type "direct"constant`

            - `DIRECT("direct")`

        - `class Program:`

          - `String callerId`

            The call ID of the program item that produced this tool call.

          - `JsonValue; type "program"constant`

            - `PROGRAM("program")`

      - `Optional<String> namespace`

        The namespace of the function to run.

      - `Optional<Status> status`

        The status of the item. One of `in_progress`, `completed`, or
        `incomplete`. Populated when items are returned via API.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

    - `FunctionCallOutput`

      - `Output output`

        Text, image, or file output of the function tool call.

        - `String`

        - `List<ResponseFunctionCallOutputItem>`

          - `class ResponseInputTextContent:`

            A text input to the model.

            - `String text`

              The text input to the model.

            - `JsonValue; type "input_text"constant`

              The type of the input item. Always `input_text`.

              - `INPUT_TEXT("input_text")`

            - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

              Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

              - `JsonValue; mode "explicit"constant`

                The breakpoint mode. Always `explicit`.

                - `EXPLICIT("explicit")`

          - `class ResponseInputImageContent:`

            An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision)

            - `JsonValue; type "input_image"constant`

              The type of the input item. Always `input_image`.

              - `INPUT_IMAGE("input_image")`

            - `Optional<Detail> detail`

              The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

              - `LOW("low")`

              - `HIGH("high")`

              - `AUTO("auto")`

              - `ORIGINAL("original")`

            - `Optional<String> fileId`

              The ID of the file to be sent to the model.

            - `Optional<String> imageUrl`

              The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

            - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

              Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

              - `JsonValue; mode "explicit"constant`

                The breakpoint mode. Always `explicit`.

                - `EXPLICIT("explicit")`

          - `class ResponseInputFileContent:`

            A file input to the model.

            - `JsonValue; type "input_file"constant`

              The type of the input item. Always `input_file`.

              - `INPUT_FILE("input_file")`

            - `Optional<Detail> detail`

              The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

            - `Optional<String> fileData`

              The base64-encoded data of the file to be sent to the model.

            - `Optional<String> fileId`

              The ID of the file to be sent to the model.

            - `Optional<String> fileUrl`

              The URL of the file to be sent to the model.

            - `Optional<String> filename`

              The name of the file to be sent to the model.

            - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

              Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

              - `JsonValue; mode "explicit"constant`

                The breakpoint mode. Always `explicit`.

                - `EXPLICIT("explicit")`

      - `JsonValue; type "function_call_output"constant`

        The type of the function tool call output. Always `function_call_output`.

        - `FUNCTION_CALL_OUTPUT("function_call_output")`

      - `Optional<String> id`

        The unique ID of the function tool call output. Populated when this item is returned via API.

      - `Optional<String> callId`

        The unique ID of the function tool call generated by the model.

      - `Optional<Caller> caller`

        The execution context that produced this tool call.

        - `JsonValue;`

          - `JsonValue; type "direct"constant`

            The caller type. Always `direct`.

            - `DIRECT("direct")`

        - `class Program:`

          - `String callerId`

            The call ID of the program item that produced this tool call.

          - `JsonValue; type "program"constant`

            The caller type. Always `program`.

            - `PROGRAM("program")`

      - `Optional<String> name`

        The name of the tool that produced the output.

      - `Optional<String> namespace`

        The namespace of the tool that produced the output.

      - `Optional<Status> status`

        The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

    - `ToolSearchCall`

      - `JsonValue arguments`

        The arguments supplied to the tool search call.

      - `JsonValue; type "tool_search_call"constant`

        The item type. Always `tool_search_call`.

        - `TOOL_SEARCH_CALL("tool_search_call")`

      - `Optional<String> id`

        The unique ID of this tool search call.

      - `Optional<String> callId`

        The unique ID of the tool search call generated by the model.

      - `Optional<Execution> execution`

        Whether tool search was executed by the server or by the client.

        - `SERVER("server")`

        - `CLIENT("client")`

      - `Optional<Status> status`

        The status of the tool search call.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

    - `class ResponseToolSearchOutputItemParam:`

      - `List<Tool> tools`

        The loaded tool definitions returned by the tool search output.

        - `class FunctionTool:`

          Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

          - `String name`

            The name of the function to call.

          - `Optional<Parameters> parameters`

            A JSON schema object describing the parameters of the function.

          - `Optional<Boolean> strict`

            Whether strict parameter validation is enforced for this function tool.

          - `JsonValue; type "function"constant`

            The type of the function tool. Always `function`.

            - `FUNCTION("function")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            The tool invocation context(s).

            - `DIRECT("direct")`

            - `PROGRAMMATIC("programmatic")`

          - `Optional<Boolean> async`

          - `Optional<Boolean> deferLoading`

            Whether this function is deferred and loaded via tool search.

          - `Optional<String> description`

            A description of the function. Used by the model to determine whether or not to call the function.

          - `Optional<OutputSchema> outputSchema`

            A JSON schema object describing the JSON value encoded in string outputs for this function.

        - `class FileSearchTool:`

          A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

          - `JsonValue; type "file_search"constant`

            The type of the file search tool. Always `file_search`.

            - `FILE_SEARCH("file_search")`

          - `List<String> vectorStoreIds`

            The IDs of the vector stores to search.

          - `Optional<Filters> filters`

            A filter to apply.

            - `class ComparisonFilter:`

              A filter used to compare a specified attribute key to a given value using a defined comparison operation.

              - `String key`

                The key to compare against the value.

              - `Type type`

                Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                - `eq`: equals
                - `ne`: not equal
                - `gt`: greater than
                - `gte`: greater than or equal
                - `lt`: less than
                - `lte`: less than or equal
                - `in`: in
                - `nin`: not in

                - `EQ("eq")`

                - `NE("ne")`

                - `GT("gt")`

                - `GTE("gte")`

                - `LT("lt")`

                - `LTE("lte")`

                - `IN("in")`

                - `NIN("nin")`

              - `Value value`

                The value to compare against the attribute key; supports string, number, or boolean types.

                - `String`

                - `double`

                - `boolean`

                - `List<ComparisonFilterValueItem>`

                  - `String`

                  - `double`

            - `class CompoundFilter:`

              Combine multiple filters using `and` or `or`.

              - `List<Filter> filters`

                Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

                - `class ComparisonFilter:`

                  A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                - `JsonValue`

              - `Type type`

                Type of operation: `and` or `or`.

                - `AND("and")`

                - `OR("or")`

          - `Optional<Long> maxNumResults`

            The maximum number of results to return. This number should be between 1 and 50 inclusive.

          - `Optional<RankingOptions> rankingOptions`

            Ranking options for search.

            - `Optional<HybridSearch> hybridSearch`

              Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

              - `double embeddingWeight`

                The weight of the embedding in the reciprocal ranking fusion.

              - `double textWeight`

                The weight of the text in the reciprocal ranking fusion.

            - `Optional<Ranker> ranker`

              The ranker to use for the file search.

              - `AUTO("auto")`

              - `DEFAULT_2024_11_15("default-2024-11-15")`

            - `Optional<Double> scoreThreshold`

              The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

        - `class ComputerTool:`

          A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

          - `JsonValue; type "computer"constant`

            The type of the computer tool. Always `computer`.

            - `COMPUTER("computer")`

        - `class ComputerUsePreviewTool:`

          A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

          - `long displayHeight`

            The height of the computer display.

          - `long displayWidth`

            The width of the computer display.

          - `Environment environment`

            The type of computer environment to control.

            - `WINDOWS("windows")`

            - `MAC("mac")`

            - `LINUX("linux")`

            - `UBUNTU("ubuntu")`

            - `BROWSER("browser")`

          - `JsonValue; type "computer_use_preview"constant`

            The type of the computer use tool. Always `computer_use_preview`.

            - `COMPUTER_USE_PREVIEW("computer_use_preview")`

        - `class WebSearchTool:`

          Search the Internet for sources related to the prompt. Learn more about the
          [web search tool](/api/docs/guides/tools-web-search).

          - `Type type`

            The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

            - `WEB_SEARCH("web_search")`

            - `WEB_SEARCH_2025_08_26("web_search_2025_08_26")`

          - `Optional<Boolean> externalWebAccess`

            Allow live internet access for web search. Defaults to true when omitted. When false, the web search tool runs in offline/cache-only mode and will not fetch new external content.

          - `Optional<Filters> filters`

            Filters for the search.

            - `Optional<List<String>> allowedDomains`

              Allowed domains for the search. If not provided, all domains are allowed.
              Subdomains of the provided domains are allowed as well.

              Example: `["pubmed.ncbi.nlm.nih.gov"]`

          - `Optional<SearchContextSize> searchContextSize`

            High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

          - `Optional<UserLocation> userLocation`

            The approximate location of the user. If omitted or null, defaults to the
            United States. To avoid this fallback, pass `{"type": "approximate"}` without
            location fields. To localize results, provide the relevant location fields.

            - `Optional<String> city`

              Free text input for the city of the user, e.g. `San Francisco`.

            - `Optional<String> country`

              The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

            - `Optional<String> region`

              Free text input for the region of the user, e.g. `California`.

            - `Optional<String> timezone`

              The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

            - `Optional<Type> type`

              The type of location approximation. Always `approximate`.

              - `APPROXIMATE("approximate")`

        - `Mcp`

          - `String serverLabel`

            A label for this MCP server, used to identify it in tool calls.

          - `JsonValue; type "mcp"constant`

            The type of the MCP tool. Always `mcp`.

            - `MCP("mcp")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            The tool invocation context(s).

            - `DIRECT("direct")`

            - `PROGRAMMATIC("programmatic")`

          - `Optional<AllowedTools> allowedTools`

            List of allowed tool names or a filter object.

            - `List<String>`

            - `class McpToolFilter:`

              A filter object to specify which tools are allowed.

              - `Optional<Boolean> readOnly`

                Indicates whether or not a tool modifies data or is read-only. If an
                MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                it will match this filter.

              - `Optional<List<String>> toolNames`

                List of allowed tool names.

          - `Optional<String> authorization`

            An OAuth access token that can be used with a remote MCP server, either
            with a custom MCP server URL or a service connector. Your application
            must handle the OAuth authorization flow and provide the token here.

          - `Optional<ConnectorId> connectorId`

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

            - `CONNECTOR_DROPBOX("connector_dropbox")`

            - `CONNECTOR_GMAIL("connector_gmail")`

            - `CONNECTOR_GOOGLECALENDAR("connector_googlecalendar")`

            - `CONNECTOR_GOOGLEDRIVE("connector_googledrive")`

            - `CONNECTOR_MICROSOFTTEAMS("connector_microsoftteams")`

            - `CONNECTOR_OUTLOOKCALENDAR("connector_outlookcalendar")`

            - `CONNECTOR_OUTLOOKEMAIL("connector_outlookemail")`

            - `CONNECTOR_SHAREPOINT("connector_sharepoint")`

          - `Optional<Boolean> deferLoading`

            Whether this MCP tool is deferred and discovered via tool search.

          - `Optional<Headers> headers`

            Optional HTTP headers to send to the MCP server. Use for authentication
            or other purposes.

          - `Optional<RequireApproval> requireApproval`

            Specify which of the MCP server's tools require approval.

            - `class McpToolApprovalFilter:`

              Specify which of the MCP server's tools require approval. Can be
              `always`, `never`, or a filter object associated with tools
              that require approval.

              - `Optional<Always> always`

                A filter object to specify which tools are allowed.

                - `Optional<Boolean> readOnly`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `Optional<List<String>> toolNames`

                  List of allowed tool names.

              - `Optional<Never> never`

                A filter object to specify which tools are allowed.

                - `Optional<Boolean> readOnly`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `Optional<List<String>> toolNames`

                  List of allowed tool names.

            - `enum McpToolApprovalSetting:`

              Specify a single approval policy for all tools. One of `always` or
              `never`. When set to `always`, all tools will require approval. When
              set to `never`, all tools will not require approval.

              - `ALWAYS("always")`

              - `NEVER("never")`

          - `Optional<String> serverDescription`

            Optional description of the MCP server, used to provide more context.

          - `Optional<String> serverUrl`

            The URL for the MCP server. One of `server_url`, `connector_id`, or
            `tunnel_id` must be provided.

          - `Optional<String> tunnelId`

            The Secure MCP Tunnel ID to use instead of a direct server URL. One of
            `server_url`, `connector_id`, or `tunnel_id` must be provided.

        - `CodeInterpreter`

          - `Container container`

            The code interpreter container. Can be a container ID or an object that
            specifies uploaded file IDs to make available to your code, along with an
            optional `memory_limit` setting.

            - `String`

            - `class CodeInterpreterToolAuto:`

              Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

              - `JsonValue; type "auto"constant`

                Always `auto`.

                - `AUTO("auto")`

              - `Optional<List<String>> fileIds`

                An optional list of uploaded files to make available to your code.

              - `Optional<MemoryLimit> memoryLimit`

                The memory limit for the code interpreter container.

                - `_1G("1g")`

                - `_4G("4g")`

                - `_16G("16g")`

                - `_64G("64g")`

              - `Optional<NetworkPolicy> networkPolicy`

                Network access policy for the container.

                - `class ContainerNetworkPolicyDisabled:`

                  - `JsonValue; type "disabled"constant`

                    Disable outbound network access. Always `disabled`.

                    - `DISABLED("disabled")`

                - `class ContainerNetworkPolicyAllowlist:`

                  - `List<String> allowedDomains`

                    A list of allowed domains when type is `allowlist`.

                  - `JsonValue; type "allowlist"constant`

                    Allow outbound network access only to specified domains. Always `allowlist`.

                    - `ALLOWLIST("allowlist")`

                  - `Optional<List<ContainerNetworkPolicyDomainSecret>> domainSecrets`

                    Optional domain-scoped secrets for allowlisted domains.

                    - `String domain`

                      The domain associated with the secret.

                    - `String name`

                      The name of the secret to inject for the domain.

                    - `String value`

                      The secret value to inject for the domain.

          - `JsonValue; type "code_interpreter"constant`

            The type of the code interpreter tool. Always `code_interpreter`.

            - `CODE_INTERPRETER("code_interpreter")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            The tool invocation context(s).

            - `DIRECT("direct")`

            - `PROGRAMMATIC("programmatic")`

        - `JsonValue;`

          - `JsonValue; type "programmatic_tool_calling"constant`

            The type of the tool. Always `programmatic_tool_calling`.

            - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

        - `ImageGeneration`

          - `JsonValue; type "image_generation"constant`

            The type of the image generation tool. Always `image_generation`.

            - `IMAGE_GENERATION("image_generation")`

          - `Optional<Action> action`

            Whether to generate a new image or edit an existing image. Default: `auto`.

            - `GENERATE("generate")`

            - `EDIT("edit")`

            - `AUTO("auto")`

          - `Optional<Background> background`

            Allows to set transparency for the background of the generated image(s). Must
            be one of `transparent`, `opaque`, or `auto` (default value). When `auto` is
            used, the model will automatically determine the best background for the
            image.

            `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`, including their
            `2026-09-08` snapshots, support `opaque` and `transparent` backgrounds.
            Transparent backgrounds are available for supported GPT Image models. For
            `gpt-image-2` and `gpt-image-2-2026-04-21`, this support is in preview. When
            using `transparent`, set the output format to `png` or `webp`.

            - `TRANSPARENT("transparent")`

            - `OPAQUE("opaque")`

            - `AUTO("auto")`

          - `Optional<InputFidelity> inputFidelity`

            Controls fidelity to the original input image(s). This parameter is supported for GPT image models that support input fidelity. `gpt-image-2` and `gpt-image-2-2026-04-21` ignore this parameter.

            - `HIGH("high")`

            - `LOW("low")`

          - `Optional<InputImageMask> inputImageMask`

            Optional mask for inpainting. Contains `image_url`
            (string, optional) and `file_id` (string, optional).

            - `Optional<String> fileId`

              File ID for the mask image.

            - `Optional<String> imageUrl`

              Base64-encoded mask image.

          - `Optional<Model> model`

            The image generation model to use. One of `gpt-image-1`,
            `gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
            `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
            `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
            `gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
            `gpt-image-1`.

            - `GPT_IMAGE_1("gpt-image-1")`

            - `GPT_IMAGE_1_MINI("gpt-image-1-mini")`

            - `GPT_IMAGE_2("gpt-image-2")`

            - `GPT_IMAGE_2_2026_04_21("gpt-image-2-2026-04-21")`

            - `GPT_IMAGE_2_5_SUNBURST("gpt-image-2.5-sunburst")`

            - `GPT_IMAGE_2_5_SUNBURST_2026_09_08("gpt-image-2.5-sunburst-2026-09-08")`

            - `GPT_IMAGE_2_5_FLARE("gpt-image-2.5-flare")`

            - `GPT_IMAGE_2_5_FLARE_2026_09_08("gpt-image-2.5-flare-2026-09-08")`

            - `GPT_IMAGE_1_5("gpt-image-1.5")`

            - `CHATGPT_IMAGE_LATEST("chatgpt-image-latest")`

          - `Optional<Moderation> moderation`

            Moderation level for the generated image. Default: `auto`.

            - `AUTO("auto")`

            - `LOW("low")`

          - `Optional<Long> outputCompression`

            Compression level for the output image. Default: 100.

          - `Optional<OutputFormat> outputFormat`

            The output format of the generated image. One of `png`, `webp`, or
            `jpeg`. Default: `png`.

            - `PNG("png")`

            - `WEBP("webp")`

            - `JPEG("jpeg")`

          - `Optional<Long> partialImages`

            Number of partial images to generate in streaming mode, from 0 (default value) to 3.

          - `Optional<Quality> quality`

            The quality of the generated image. The GPT image models support `low`,
            `medium`, and `high`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`,
            including their `2026-09-08` snapshots, also support `xhigh` and `max`.
            Default: `auto`.

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

            - `XHIGH("xhigh")`

            - `MAX("max")`

            - `AUTO("auto")`

          - `Optional<Size> size`

            The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model's current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

            - `_1024X1024("1024x1024")`

            - `_1024X1536("1024x1536")`

            - `_1536X1024("1536x1024")`

            - `AUTO("auto")`

        - `JsonValue;`

          - `JsonValue; type "local_shell"constant`

            The type of the local shell tool. Always `local_shell`.

            - `LOCAL_SHELL("local_shell")`

        - `class FunctionShellTool:`

          A tool that allows the model to execute shell commands.

          - `JsonValue; type "shell"constant`

            The type of the shell tool. Always `shell`.

            - `SHELL("shell")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            The tool invocation context(s).

            - `DIRECT("direct")`

            - `PROGRAMMATIC("programmatic")`

          - `Optional<Environment> environment`

            - `class ContainerAuto:`

              - `JsonValue; type "container_auto"constant`

                Automatically creates a container for this request

                - `CONTAINER_AUTO("container_auto")`

              - `Optional<List<String>> fileIds`

                An optional list of uploaded files to make available to your code.

              - `Optional<MemoryLimit> memoryLimit`

                The memory limit for the container.

                - `_1G("1g")`

                - `_4G("4g")`

                - `_16G("16g")`

                - `_64G("64g")`

              - `Optional<NetworkPolicy> networkPolicy`

                Network access policy for the container.

                - `class ContainerNetworkPolicyDisabled:`

                - `class ContainerNetworkPolicyAllowlist:`

              - `Optional<List<Skill>> skills`

                An optional list of skills referenced by id or inline data.

                - `class SkillReference:`

                  - `String skillId`

                    The ID of the referenced skill.

                  - `JsonValue; type "skill_reference"constant`

                    References a skill created with the /v1/skills endpoint.

                    - `SKILL_REFERENCE("skill_reference")`

                  - `Optional<String> version`

                    Optional skill version. Use a positive integer or 'latest'. Omit for default.

                - `class InlineSkill:`

                  - `String description`

                    The description of the skill.

                  - `String name`

                    The name of the skill.

                  - `InlineSkillSource source`

                    Inline skill payload

                    - `String data`

                      Base64-encoded skill zip bundle.

                    - `JsonValue; mediaType "application/zip"constant`

                      The media type of the inline skill payload. Must be `application/zip`.

                      - `APPLICATION_ZIP("application/zip")`

                    - `JsonValue; type "base64"constant`

                      The type of the inline skill source. Must be `base64`.

                      - `BASE64("base64")`

                  - `JsonValue; type "inline"constant`

                    Defines an inline skill for this request.

                    - `INLINE("inline")`

            - `class LocalEnvironment:`

              - `JsonValue; type "local"constant`

                Use a local computer environment.

                - `LOCAL("local")`

              - `Optional<List<LocalSkill>> skills`

                An optional list of skills.

                - `String description`

                  The description of the skill.

                - `String name`

                  The name of the skill.

                - `String path`

                  The path to the directory containing the skill.

            - `class ContainerReference:`

              - `String containerId`

                The ID of the referenced container.

              - `JsonValue; type "container_reference"constant`

                References a container created with the /v1/containers endpoint

                - `CONTAINER_REFERENCE("container_reference")`

        - `class CustomTool:`

          A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

          - `String name`

            The name of the custom tool, used to identify it in tool calls.

          - `JsonValue; type "custom"constant`

            The type of the custom tool. Always `custom`.

            - `CUSTOM("custom")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            The tool invocation context(s).

            - `DIRECT("direct")`

            - `PROGRAMMATIC("programmatic")`

          - `Optional<Boolean> async`

            Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

          - `Optional<Boolean> deferLoading`

            Whether this tool should be deferred and discovered via tool search.

          - `Optional<String> description`

            Optional description of the custom tool, used to provide more context.

          - `Optional<CustomToolInputFormat> format`

            The input format for the custom tool. Default is unconstrained text.

            - `JsonValue;`

              - `JsonValue; type "text"constant`

                Unconstrained text format. Always `text`.

                - `TEXT("text")`

            - `Grammar`

              - `String definition`

                The grammar definition.

              - `Syntax syntax`

                The syntax of the grammar definition. One of `lark` or `regex`.

                - `LARK("lark")`

                - `REGEX("regex")`

              - `JsonValue; type "grammar"constant`

                Grammar format. Always `grammar`.

                - `GRAMMAR("grammar")`

        - `class NamespaceTool:`

          Groups function/custom tools under a shared namespace.

          - `String description`

            A description of the namespace shown to the model.

          - `String name`

            The namespace name used in tool calls (for example, `crm`).

          - `List<Tool> tools`

            The function/custom tools available inside this namespace.

            - `class Function:`

              - `String name`

              - `JsonValue; type "function"constant`

                - `FUNCTION("function")`

              - `Optional<List<AllowedCaller>> allowedCallers`

                The tool invocation context(s).

                - `DIRECT("direct")`

                - `PROGRAMMATIC("programmatic")`

              - `Optional<Boolean> async`

                Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

              - `Optional<Boolean> deferLoading`

                Whether this function should be deferred and discovered via tool search.

              - `Optional<String> description`

              - `Optional<OutputSchema> outputSchema`

                A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

              - `Optional<JsonValue> parameters`

              - `Optional<Boolean> strict`

                Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

            - `class CustomTool:`

              A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

          - `JsonValue; type "namespace"constant`

            The type of the tool. Always `namespace`.

            - `NAMESPACE("namespace")`

        - `class ToolSearchTool:`

          Hosted or BYOT tool search configuration for deferred tools.

          - `JsonValue; type "tool_search"constant`

            The type of the tool. Always `tool_search`.

            - `TOOL_SEARCH("tool_search")`

          - `Optional<String> description`

            Description shown to the model for a client-executed tool search tool.

          - `Optional<Execution> execution`

            Whether tool search is executed by the server or by the client.

            - `SERVER("server")`

            - `CLIENT("client")`

          - `Optional<JsonValue> parameters`

            Parameter schema for a client-executed tool search tool.

        - `class WebSearchPreviewTool:`

          This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

          - `Type type`

            The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

            - `WEB_SEARCH_PREVIEW("web_search_preview")`

            - `WEB_SEARCH_PREVIEW_2025_03_11("web_search_preview_2025_03_11")`

          - `Optional<List<SearchContentType>> searchContentTypes`

            - `TEXT("text")`

            - `IMAGE("image")`

          - `Optional<SearchContextSize> searchContextSize`

            High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

          - `Optional<UserLocation> userLocation`

            The approximate location of the user. If omitted or null, defaults to the United States. To avoid this fallback, pass `{"type": "approximate"}` without location fields. To localize results, provide the relevant location fields.

            - `JsonValue; type "approximate"constant`

              The type of location approximation. Always `approximate`.

              - `APPROXIMATE("approximate")`

            - `Optional<String> city`

              Free text input for the city of the user, e.g. `San Francisco`.

            - `Optional<String> country`

              The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

            - `Optional<String> region`

              Free text input for the region of the user, e.g. `California`.

            - `Optional<String> timezone`

              The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

        - `class ApplyPatchTool:`

          Allows the assistant to create, delete, or update files using unified diffs.

          - `JsonValue; type "apply_patch"constant`

            The type of the tool. Always `apply_patch`.

            - `APPLY_PATCH("apply_patch")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            The tool invocation context(s).

            - `DIRECT("direct")`

            - `PROGRAMMATIC("programmatic")`

      - `JsonValue; type "tool_search_output"constant`

        The item type. Always `tool_search_output`.

        - `TOOL_SEARCH_OUTPUT("tool_search_output")`

      - `Optional<String> id`

        The unique ID of this tool search output.

      - `Optional<String> callId`

        The unique ID of the tool search call generated by the model.

      - `Optional<Execution> execution`

        Whether tool search was executed by the server or by the client.

        - `SERVER("server")`

        - `CLIENT("client")`

      - `Optional<Status> status`

        The status of the tool search output.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

    - `AdditionalTools`

      - `JsonValue; role "developer"constant`

        The role that provided the additional tools. Only `developer` is supported.

        - `DEVELOPER("developer")`

      - `List<Tool> tools`

        A list of additional tools made available at this item.

        - `class FunctionTool:`

          Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

        - `class FileSearchTool:`

          A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

        - `class ComputerTool:`

          A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

        - `class ComputerUsePreviewTool:`

          A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

        - `class WebSearchTool:`

          Search the Internet for sources related to the prompt. Learn more about the
          [web search tool](/api/docs/guides/tools-web-search).

        - `Mcp`

        - `CodeInterpreter`

        - `JsonValue;`

        - `ImageGeneration`

        - `JsonValue;`

        - `class FunctionShellTool:`

          A tool that allows the model to execute shell commands.

        - `class CustomTool:`

          A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

        - `class NamespaceTool:`

          Groups function/custom tools under a shared namespace.

        - `class ToolSearchTool:`

          Hosted or BYOT tool search configuration for deferred tools.

        - `class WebSearchPreviewTool:`

          This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

        - `class ApplyPatchTool:`

          Allows the assistant to create, delete, or update files using unified diffs.

      - `JsonValue; type "additional_tools"constant`

        The item type. Always `additional_tools`.

        - `ADDITIONAL_TOOLS("additional_tools")`

      - `Optional<String> id`

        The unique ID of this additional tools item.

    - `class ResponseConfigurationUpdateItemParam:`

      An update to the conversation's response configuration. The configuration
      remains in effect for subsequent responses until it is replaced by another
      configuration update.

      - `JsonValue; type "configuration_update"constant`

        The item type. Always `configuration_update`.

        - `CONFIGURATION_UPDATE("configuration_update")`

      - `Optional<String> id`

        The unique ID of the configuration update item.

      - `Optional<Reasoning> reasoning`

        Updates to reasoning configuration. Only effort is supported.

        - `Optional<ReasoningEffort> effort`

          The reasoning effort to use for subsequent responses until another
          configuration update replaces it.

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

          - `MAX("max")`

    - `class ResponseReasoningItem:`

      A description of the chain of thought used by a reasoning model while generating
      a response. Be sure to include these items in your `input` to the Responses API
      for subsequent turns of a conversation if you are manually
      [managing context](/api/docs/guides/conversation-state).

      - `String id`

        The unique identifier of the reasoning content.

      - `List<Summary> summary`

        Reasoning summary content.

        - `String text`

          A summary of the reasoning output from the model so far.

        - `JsonValue; type "summary_text"constant`

          The type of the object. Always `summary_text`.

          - `SUMMARY_TEXT("summary_text")`

      - `JsonValue; type "reasoning"constant`

        The type of the object. Always `reasoning`.

        - `REASONING("reasoning")`

      - `Optional<List<Content>> content`

        Reasoning text content.

        - `String text`

          The reasoning text from the model.

        - `JsonValue; type "reasoning_text"constant`

          The type of the reasoning text. Always `reasoning_text`.

          - `REASONING_TEXT("reasoning_text")`

      - `Optional<String> encryptedContent`

        The encrypted content of the reasoning item. This is populated by default
        for reasoning items returned by `POST /v1/responses` and WebSocket
        `response.create` requests.

        When streaming, use the completed reasoning item and its
        `encrypted_content` from the `response.output_item.done` event in
        subsequent requests. The `encrypted_content` in
        `response.output_item.added` may be incomplete. This is especially
        important when `store` is `false` or when using Zero Data Retention.

      - `Optional<Status> status`

        The status of the item. One of `in_progress`, `completed`, or
        `incomplete`. Populated when items are returned via API.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

    - `class ResponseCompactionItemParam:`

      A compaction item generated by the [`v1/responses/compact` API](/api/reference/resources/responses/methods/compact).

      - `String encryptedContent`

        The encrypted content of the compaction summary.

      - `JsonValue; type "compaction"constant`

        The type of the item. Always `compaction`.

        - `COMPACTION("compaction")`

      - `Optional<String> id`

        The ID of the compaction item.

    - `ImageGenerationCall`

      - `String id`

        The unique ID of the image generation call.

      - `Optional<String> result`

        The generated image encoded in base64.

      - `Status status`

        The status of the image generation call.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

        - `GENERATING("generating")`

        - `FAILED("failed")`

      - `JsonValue; type "image_generation_call"constant`

        The type of the image generation call. Always `image_generation_call`.

        - `IMAGE_GENERATION_CALL("image_generation_call")`

      - `Optional<Action> action`

        The action used for image generation.

        - `GENERATE("generate")`

        - `EDIT("edit")`

        - `AUTO("auto")`

      - `Optional<Background> background`

        The background setting used for generation.

        - `TRANSPARENT("transparent")`

        - `OPAQUE("opaque")`

        - `AUTO("auto")`

      - `Optional<OutputFormat> outputFormat`

        The output format used for generation.

        - `PNG("png")`

        - `WEBP("webp")`

        - `JPEG("jpeg")`

      - `Optional<Quality> quality`

        The quality of the image generated by the image generation tool call. One of `low`, `medium`, `high`, `xhigh`, `max`, or `auto`.

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

        - `XHIGH("xhigh")`

        - `MAX("max")`

        - `AUTO("auto")`

      - `Optional<String> revisedPrompt`

        The prompt that was used after any model prompt rewriting.

      - `Optional<Size> size`

        The image dimensions as a `WIDTHxHEIGHT` string, for example `1536x864`.

        - `_1024X1024("1024x1024")`

        - `_1024X1536("1024x1536")`

        - `_1536X1024("1536x1024")`

    - `class ResponseCodeInterpreterToolCall:`

      A tool call to run code.

      - `String id`

        The unique ID of the code interpreter tool call.

      - `Optional<String> code`

        The code to run, or null if not available.

      - `String containerId`

        The ID of the container used to run the code.

      - `Optional<List<Output>> outputs`

        The outputs generated by the code interpreter, such as logs or images.
        Can be null if no outputs are available.

        - `class Logs:`

          The logs output from the code interpreter.

          - `String logs`

            The logs output from the code interpreter.

          - `JsonValue; type "logs"constant`

            The type of the output. Always `logs`.

            - `LOGS("logs")`

        - `class Image:`

          The image output from the code interpreter.

          - `JsonValue; type "image"constant`

            The type of the output. Always `image`.

            - `IMAGE("image")`

          - `String url`

            The URL of the image output from the code interpreter.

      - `Status status`

        The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `INTERPRETING("interpreting")`

        - `FAILED("failed")`

      - `JsonValue; type "code_interpreter_call"constant`

        The type of the code interpreter tool call. Always `code_interpreter_call`.

        - `CODE_INTERPRETER_CALL("code_interpreter_call")`

    - `LocalShellCall`

      - `String id`

        The unique ID of the local shell call.

      - `Action action`

        Execute a shell command on the server.

        - `List<String> command`

          The command to run.

        - `Env env`

          Environment variables to set for the command.

        - `JsonValue; type "exec"constant`

          The type of the local shell action. Always `exec`.

          - `EXEC("exec")`

        - `Optional<Long> timeoutMs`

          Optional timeout in milliseconds for the command.

        - `Optional<String> user`

          Optional user to run the command as.

        - `Optional<String> workingDirectory`

          Optional working directory to run the command in.

      - `String callId`

        The unique ID of the local shell tool call generated by the model.

      - `Status status`

        The status of the local shell call.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

      - `JsonValue; type "local_shell_call"constant`

        The type of the local shell call. Always `local_shell_call`.

        - `LOCAL_SHELL_CALL("local_shell_call")`

    - `LocalShellCallOutput`

      - `String id`

        The unique ID of the local shell tool call generated by the model.

      - `String output`

        A JSON string of the output of the local shell tool call.

      - `JsonValue; type "local_shell_call_output"constant`

        The type of the local shell tool call output. Always `local_shell_call_output`.

        - `LOCAL_SHELL_CALL_OUTPUT("local_shell_call_output")`

      - `Optional<Status> status`

        The status of the item. One of `in_progress`, `completed`, or `incomplete`.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

    - `ShellCall`

      - `Action action`

        The shell commands and limits that describe how to run the tool call.

        - `List<String> commands`

          Ordered shell commands for the execution environment to run.

        - `Optional<Long> maxOutputLength`

          Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

        - `Optional<Long> timeoutMs`

          Maximum wall-clock time in milliseconds to allow the shell commands to run.

      - `String callId`

        The unique ID of the shell tool call generated by the model.

      - `JsonValue; type "shell_call"constant`

        The type of the item. Always `shell_call`.

        - `SHELL_CALL("shell_call")`

      - `Optional<String> id`

        The unique ID of the shell tool call. Populated when this item is returned via API.

      - `Optional<Caller> caller`

        The execution context that produced this tool call.

        - `JsonValue;`

          - `JsonValue; type "direct"constant`

            The caller type. Always `direct`.

            - `DIRECT("direct")`

        - `class Program:`

          - `String callerId`

            The call ID of the program item that produced this tool call.

          - `JsonValue; type "program"constant`

            The caller type. Always `program`.

            - `PROGRAM("program")`

      - `Optional<Environment> environment`

        The environment to execute the shell commands in.

        - `class LocalEnvironment:`

        - `class ContainerReference:`

      - `Optional<Status> status`

        The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

    - `ShellCallOutput`

      - `String callId`

        The unique ID of the shell tool call generated by the model.

      - `List<ResponseFunctionShellCallOutputContent> output`

        Captured chunks of stdout and stderr output, along with their associated outcomes.

        - `Outcome outcome`

          The exit or timeout outcome associated with this shell call.

          - `JsonValue;`

            - `JsonValue; type "timeout"constant`

              The outcome type. Always `timeout`.

              - `TIMEOUT("timeout")`

          - `class Exit:`

            Indicates that the shell commands finished and returned an exit code.

            - `long exitCode`

              The exit code returned by the shell process.

            - `JsonValue; type "exit"constant`

              The outcome type. Always `exit`.

              - `EXIT("exit")`

        - `String stderr`

          Captured stderr output for the shell call.

        - `String stdout`

          Captured stdout output for the shell call.

      - `JsonValue; type "shell_call_output"constant`

        The type of the item. Always `shell_call_output`.

        - `SHELL_CALL_OUTPUT("shell_call_output")`

      - `Optional<String> id`

        The unique ID of the shell tool call output. Populated when this item is returned via API.

      - `Optional<Caller> caller`

        The execution context that produced this tool call.

        - `JsonValue;`

          - `JsonValue; type "direct"constant`

            The caller type. Always `direct`.

            - `DIRECT("direct")`

        - `class Program:`

          - `String callerId`

            The call ID of the program item that produced this tool call.

          - `JsonValue; type "program"constant`

            The caller type. Always `program`.

            - `PROGRAM("program")`

      - `Optional<Long> maxOutputLength`

        The maximum number of UTF-8 characters captured for this shell call's combined output.

      - `Optional<Status> status`

        The status of the shell call output.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

    - `ApplyPatchCall`

      - `String callId`

        The unique ID of the apply patch tool call generated by the model.

      - `Operation operation`

        The specific create, delete, or update instruction for the apply_patch tool call.

        - `class CreateFile:`

          Instruction for creating a new file via the apply_patch tool.

          - `String diff`

            Unified diff content to apply when creating the file.

          - `String path`

            Path of the file to create relative to the workspace root.

          - `JsonValue; type "create_file"constant`

            The operation type. Always `create_file`.

            - `CREATE_FILE("create_file")`

        - `class DeleteFile:`

          Instruction for deleting an existing file via the apply_patch tool.

          - `String path`

            Path of the file to delete relative to the workspace root.

          - `JsonValue; type "delete_file"constant`

            The operation type. Always `delete_file`.

            - `DELETE_FILE("delete_file")`

        - `class UpdateFile:`

          Instruction for updating an existing file via the apply_patch tool.

          - `String diff`

            Unified diff content to apply to the existing file.

          - `String path`

            Path of the file to update relative to the workspace root.

          - `JsonValue; type "update_file"constant`

            The operation type. Always `update_file`.

            - `UPDATE_FILE("update_file")`

      - `Status status`

        The status of the apply patch tool call. One of `in_progress` or `completed`.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

      - `JsonValue; type "apply_patch_call"constant`

        The type of the item. Always `apply_patch_call`.

        - `APPLY_PATCH_CALL("apply_patch_call")`

      - `Optional<String> id`

        The unique ID of the apply patch tool call. Populated when this item is returned via API.

      - `Optional<Caller> caller`

        The execution context that produced this tool call.

        - `JsonValue;`

          - `JsonValue; type "direct"constant`

            The caller type. Always `direct`.

            - `DIRECT("direct")`

        - `class Program:`

          - `String callerId`

            The call ID of the program item that produced this tool call.

          - `JsonValue; type "program"constant`

            The caller type. Always `program`.

            - `PROGRAM("program")`

    - `ApplyPatchCallOutput`

      - `String callId`

        The unique ID of the apply patch tool call generated by the model.

      - `Status status`

        The status of the apply patch tool call output. One of `completed` or `failed`.

        - `COMPLETED("completed")`

        - `FAILED("failed")`

      - `JsonValue; type "apply_patch_call_output"constant`

        The type of the item. Always `apply_patch_call_output`.

        - `APPLY_PATCH_CALL_OUTPUT("apply_patch_call_output")`

      - `Optional<String> id`

        The unique ID of the apply patch tool call output. Populated when this item is returned via API.

      - `Optional<Caller> caller`

        The execution context that produced this tool call.

        - `JsonValue;`

          - `JsonValue; type "direct"constant`

            The caller type. Always `direct`.

            - `DIRECT("direct")`

        - `class Program:`

          - `String callerId`

            The call ID of the program item that produced this tool call.

          - `JsonValue; type "program"constant`

            The caller type. Always `program`.

            - `PROGRAM("program")`

      - `Optional<String> output`

        Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

    - `McpListTools`

      - `String id`

        The unique ID of the list.

      - `String serverLabel`

        The label of the MCP server.

      - `List<Tool> tools`

        The tools available on the server.

        - `JsonValue inputSchema`

          The JSON schema describing the tool's input.

        - `String name`

          The name of the tool.

        - `Optional<JsonValue> annotations`

          Additional annotations about the tool.

        - `Optional<String> description`

          The description of the tool.

      - `JsonValue; type "mcp_list_tools"constant`

        The type of the item. Always `mcp_list_tools`.

        - `MCP_LIST_TOOLS("mcp_list_tools")`

      - `Optional<String> error`

        Error message if the server could not list tools.

    - `McpApprovalRequest`

      - `String id`

        The unique ID of the approval request.

      - `String arguments`

        A JSON string of arguments for the tool.

      - `String name`

        The name of the tool to run.

      - `String serverLabel`

        The label of the MCP server making the request.

      - `JsonValue; type "mcp_approval_request"constant`

        The type of the item. Always `mcp_approval_request`.

        - `MCP_APPROVAL_REQUEST("mcp_approval_request")`

    - `McpApprovalResponse`

      - `String approvalRequestId`

        The ID of the approval request being answered.

      - `boolean approve`

        Whether the request was approved.

      - `JsonValue; type "mcp_approval_response"constant`

        The type of the item. Always `mcp_approval_response`.

        - `MCP_APPROVAL_RESPONSE("mcp_approval_response")`

      - `Optional<String> id`

        The unique ID of the approval response

      - `Optional<String> reason`

        Optional reason for the decision.

    - `McpCall`

      - `String id`

        The unique ID of the tool call.

      - `String arguments`

        A JSON string of the arguments passed to the tool.

      - `String name`

        The name of the tool that was run.

      - `String serverLabel`

        The label of the MCP server running the tool.

      - `JsonValue; type "mcp_call"constant`

        The type of the item. Always `mcp_call`.

        - `MCP_CALL("mcp_call")`

      - `Optional<String> approvalRequestId`

        Unique identifier for the MCP tool call approval request.
        Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

      - `Optional<McpToolCallError> error`

        The error from the tool call, if any.

        - `McpProtocolError`

          - `long code`

          - `String message`

          - `JsonValue; type "mcp_protocol_error"constant`

            - `MCP_PROTOCOL_ERROR("mcp_protocol_error")`

        - `McpToolExecutionError`

          - `JsonValue content`

          - `JsonValue; type "mcp_tool_execution_error"constant`

            - `MCP_TOOL_EXECUTION_ERROR("mcp_tool_execution_error")`

        - `HttpError`

          - `long code`

          - `String message`

          - `JsonValue; type "http_error"constant`

            - `HTTP_ERROR("http_error")`

      - `Optional<String> output`

        The output from the tool call.

      - `Optional<Status> status`

        The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `CALLING("calling")`

        - `FAILED("failed")`

    - `class ResponseCustomToolCallOutput:`

      The output of a custom tool call from your code, being sent back to the model.

      - `String callId`

        The call ID, used to map this custom tool call output to a custom tool call.

      - `Output output`

        The output from the custom tool call generated by your code.
        Can be a string or an list of output content.

        - `String`

        - `List<FunctionAndCustomToolCallOutput>`

          - `class ResponseInputText:`

            A text input to the model.

          - `class ResponseInputImage:`

            An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

          - `class ResponseInputFile:`

            A file input to the model.

      - `JsonValue; type "custom_tool_call_output"constant`

        The type of the custom tool call output. Always `custom_tool_call_output`.

        - `CUSTOM_TOOL_CALL_OUTPUT("custom_tool_call_output")`

      - `Optional<String> id`

        The unique ID of the custom tool call output in the OpenAI platform.

      - `Optional<Caller> caller`

        The execution context that produced this tool call.

        - `JsonValue;`

          - `JsonValue; type "direct"constant`

            The caller type. Always `direct`.

            - `DIRECT("direct")`

        - `class Program:`

          - `String callerId`

            The call ID of the program item that produced this tool call.

          - `JsonValue; type "program"constant`

            The caller type. Always `program`.

            - `PROGRAM("program")`

    - `class ResponseCustomToolCall:`

      A call to a custom tool created by the model.

      - `String callId`

        An identifier used to map this custom tool call to a tool call output.

      - `String input`

        The input for the custom tool call generated by the model.

      - `String name`

        The name of the custom tool being called.

      - `JsonValue; type "custom_tool_call"constant`

        The type of the custom tool call. Always `custom_tool_call`.

        - `CUSTOM_TOOL_CALL("custom_tool_call")`

      - `Optional<String> id`

        The unique ID of the custom tool call in the OpenAI platform.

      - `Optional<Boolean> async`

        Whether the custom tool call runs asynchronously.

      - `Optional<Caller> caller`

        The execution context that produced this tool call.

        - `JsonValue;`

          - `JsonValue; type "direct"constant`

            - `DIRECT("direct")`

        - `class Program:`

          - `String callerId`

            The call ID of the program item that produced this tool call.

          - `JsonValue; type "program"constant`

            - `PROGRAM("program")`

      - `Optional<String> namespace`

        The namespace of the custom tool being called.

    - `JsonValue;`

      - `JsonValue; type "compaction_trigger"constant`

        The type of the item. Always `compaction_trigger`.

        - `COMPACTION_TRIGGER("compaction_trigger")`

    - `ItemReference`

      - `String id`

        The ID of the item to reference.

      - `Optional<Type> type`

        The type of item to reference. Always `item_reference`.

        - `ITEM_REFERENCE("item_reference")`

    - `Program`

      - `String id`

        The unique ID of this program item.

      - `String callId`

        The stable call ID of the program item.

      - `String code`

        The JavaScript source executed by programmatic tool calling.

      - `String fingerprint`

        Opaque program replay fingerprint that must be round-tripped.

      - `JsonValue; type "program"constant`

        The item type. Always `program`.

        - `PROGRAM("program")`

    - `ProgramOutput`

      - `String id`

        The unique ID of this program output item.

      - `String callId`

        The call ID of the program item.

      - `String result`

        The result produced by the program item.

      - `Status status`

        The terminal status of the program output.

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

      - `JsonValue; type "program_output"constant`

        The item type. Always `program_output`.

        - `PROGRAM_OUTPUT("program_output")`

  - `JsonValue; type "response.item.create"constant`

    The Live client event type. Always `response.item.create`.

    - `RESPONSE_ITEM_CREATE("response.item.create")`

  - `Optional<String> eventId`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Responses Delegation Config

- `class ResponsesDelegationConfig:`

  Model, prompt, and tool settings for tasks delegated by the Live session to a Responses backend.

  - `String model`

    The model used for server-owned Responses delegations.

  - `Optional<String> instructions`

    Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

  - `Optional<Long> maxOutputTokens`

    Maximum number of output tokens for each delegated response.

  - `Optional<Boolean> parallelToolCalls`

    Whether the delegated Responses model may request multiple tool calls in a single response.

  - `Optional<Reasoning> reasoning`

    Reasoning settings passed to each delegated Responses request.

    - `Optional<Effort> effort`

      How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

      - `NONE("none")`

      - `MINIMAL("minimal")`

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

      - `XHIGH("xhigh")`

    - `Optional<Summary> summary`

      The reasoning summary to request from the delegated Responses model, when supported.

      - `CONCISE("concise")`

      - `DETAILED("detailed")`

      - `AUTO("auto")`

  - `Optional<ServiceTier> serviceTier`

    Service tier for delegated Responses requests.

    - `AUTO("auto")`

    - `DEFAULT("default")`

    - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

    - `FLEX("flex")`

    - `PRIORITY("priority")`

    - `ULTRAFAST("ultrafast")`

  - `Optional<Text> text`

    Text generation settings passed to each delegated Responses request.

    - `Optional<Verbosity> verbosity`

      The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

  - `Optional<ToolChoice> toolChoice`

    Controls which tool the Responses backend uses when handling a task delegated by the Live model.

    - `enum LiveToolChoiceEnum:`

      - `AUTO("auto")`

      - `NONE("none")`

      - `REQUIRED("required")`

    - `class LiveFunctionToolChoiceParam:`

      - `String name`

      - `JsonValue; type "function"constant`

        - `FUNCTION("function")`

    - `class LiveMcpToolChoiceParam:`

      - `String name`

      - `String serverLabel`

      - `JsonValue; type "mcp"constant`

        - `MCP("mcp")`

  - `Optional<List<Tool>> tools`

    Tools available to the Responses backend while it handles tasks delegated by the Live model.

    - `class FunctionTool:`

      A function tool available to the Responses backend when the Live model delegates a task.

      - `String name`

        The name the delegated Responses model uses when calling this function.

      - `JsonValue; type "function"constant`

        The tool type. Always `function`.

        - `FUNCTION("function")`

      - `Optional<String> description`

        What the function does and when the delegated Responses model should call it.

      - `Optional<Parameters> parameters`

        A JSON Schema object describing the arguments accepted by the function.

      - `Optional<Boolean> strict`

        Whether the delegated Responses model must follow the function’s parameter schema exactly.

    - `JsonValue;`

      - `JsonValue; type "web_search"constant`

        The tool type. Always `web_search`.

        - `WEB_SEARCH("web_search")`

### Responses Delegation Update Config

- `class ResponsesDelegationUpdateConfig:`

  Updates to the Responses backend of an existing Live session. Omitted settings retain their current values.

  - `Optional<String> instructions`

    Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

  - `Optional<Long> maxOutputTokens`

    Maximum number of output tokens for each delegated response.

  - `Optional<String> model`

    The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.

  - `Optional<Boolean> parallelToolCalls`

    Whether the delegated Responses model may request multiple tool calls in a single response.

  - `Optional<Reasoning> reasoning`

    Reasoning settings passed to each delegated Responses request.

    - `Optional<Effort> effort`

      How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

      - `NONE("none")`

      - `MINIMAL("minimal")`

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

      - `XHIGH("xhigh")`

    - `Optional<Summary> summary`

      The reasoning summary to request from the delegated Responses model, when supported.

      - `CONCISE("concise")`

      - `DETAILED("detailed")`

      - `AUTO("auto")`

  - `Optional<ServiceTier> serviceTier`

    Service tier for delegated Responses requests.

    - `AUTO("auto")`

    - `DEFAULT("default")`

    - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

    - `FLEX("flex")`

    - `PRIORITY("priority")`

    - `ULTRAFAST("ultrafast")`

  - `Optional<Text> text`

    Text generation settings passed to each delegated Responses request.

    - `Optional<Verbosity> verbosity`

      The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

  - `Optional<ToolChoice> toolChoice`

    Controls which tool the Responses backend uses when handling a task delegated by the Live model.

    - `enum LiveToolChoiceEnum:`

      - `AUTO("auto")`

      - `NONE("none")`

      - `REQUIRED("required")`

    - `class LiveFunctionToolChoiceParam:`

      - `String name`

      - `JsonValue; type "function"constant`

        - `FUNCTION("function")`

    - `class LiveMcpToolChoiceParam:`

      - `String name`

      - `String serverLabel`

      - `JsonValue; type "mcp"constant`

        - `MCP("mcp")`

  - `Optional<List<Tool>> tools`

    Tools available to the Responses backend while it handles tasks delegated by the Live model.

    - `class FunctionTool:`

      A function tool available to the Responses backend when the Live model delegates a task.

      - `String name`

        The name the delegated Responses model uses when calling this function.

      - `JsonValue; type "function"constant`

        The tool type. Always `function`.

        - `FUNCTION("function")`

      - `Optional<String> description`

        What the function does and when the delegated Responses model should call it.

      - `Optional<Parameters> parameters`

        A JSON Schema object describing the arguments accepted by the function.

      - `Optional<Boolean> strict`

        Whether the delegated Responses model must follow the function’s parameter schema exactly.

    - `JsonValue;`

      - `JsonValue; type "web_search"constant`

        The tool type. Always `web_search`.

        - `WEB_SEARCH("web_search")`

### Server Event

- `class ServerEvent: A class that can be one of several variants.union`

  Server events for Live. Response lifecycle events are wrapped inside response.event; dispatch the nested event by its full type and tolerate new response event types. Follow the [Live prompting guide](https://developers.openai.com/api/docs/guides/live-prompting) when designing the conversation and delegation policy.

  - `class SessionStartedEvent:`

    Returned when a Live session has started. Contains the resolved session configuration, including server defaults.

    - `String eventId`

      The unique ID of the Live server event.

    - `SessionResource session`

      The resolved Live session configuration and server-assigned session metadata.

      - `String id`

        The unique ID of the Live session. Use this ID for sideband connections, forking, and recording download.

      - `long expiresAt`

        The Unix timestamp, in seconds, at which the Live session expires.

      - `Model model`

        The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

        - `GPT_LIVE_1("gpt-live-1")`

      - `JsonValue; status "active"constant`

        The status of the session snapshot. Always `active`, including the final snapshot in session.closed; use the event type to determine that the session has closed.

        - `ACTIVE("active")`

      - `Optional<Audio> audio`

        Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

        - `Optional<AudioFormat> format`

          Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

          - `AudioPcm`

            - `Rate rate`

              Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

              - `_16000(16000)`

              - `_24000(24000)`

            - `JsonValue; type "audio/pcm"constant`

              The audio encoding. Always `audio/pcm`.

              - `AUDIO_PCM("audio/pcm")`

          - `AudioPcmu`

            - `long rate`

              Audio sample rate in hertz. G.711 audio uses 8000 Hz.

            - `JsonValue; type "audio/pcmu"constant`

              The audio encoding. Always `audio/pcmu`.

              - `AUDIO_PCMU("audio/pcmu")`

          - `AudioPcma`

            - `long rate`

              Audio sample rate in hertz. G.711 audio uses 8000 Hz.

            - `JsonValue; type "audio/pcma"constant`

              The audio encoding. Always `audio/pcma`.

              - `AUDIO_PCMA("audio/pcma")`

        - `Optional<Output> output`

          The voice used for speech generated by the Live model.

          - `Optional<Voice> voice`

            The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

            - `String`

            - `enum BuiltInVoice:`

              A built-in voice available for Live speech.

              - `ALLOY("alloy")`

              - `ASH("ash")`

              - `BALLAD("ballad")`

              - `BEACON("beacon")`

              - `BOSSA("bossa")`

              - `CEDAR("cedar")`

              - `CINDER("cinder")`

              - `CORAL("coral")`

              - `DELTA("delta")`

              - `ECHO("echo")`

              - `GLEAM("gleam")`

              - `MARIN("marin")`

              - `MERIDIAN("meridian")`

              - `QUARTZ("quartz")`

              - `RIPPLE("ripple")`

              - `SAGE("sage")`

              - `SHIMMER("shimmer")`

              - `STONE("stone")`

              - `TEMPO("tempo")`

              - `VERSE("verse")`

              - `VESPER("vesper")`

              - `WILLOW("willow")`

            - `class CustomVoice:`

              - `String id`

      - `Optional<ClientConfig> client`

        Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

        - `DataChannelConfig dataChannel`

          Client and server event permissions for the WebRTC frontend data channel.

          - `Optional<AllowedClientEvents> allowedClientEvents`

            Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

            - `JsonValue;`

              - `ALL("all")`

            - `List<String>`

          - `Optional<AllowedServerEvents> allowedServerEvents`

            Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

            - `JsonValue;`

              - `ALL("all")`

            - `List<ServerEventSelector>`

              - `String type`

                The outer Live server event type. Use 'response.event' for Responses events.

              - `Optional<String> responseEvent`

                The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

      - `Optional<Delegation> delegation`

        Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

        - `class ClientDelegation:`

          Delegate tasks to your application. The Live session emits delegation events that your backend handles.

          - `JsonValue; type "client"constant`

            The delegation owner. Always `client` for tasks handled by your application.

            - `CLIENT("client")`

        - `class Responses:`

          Delegate tasks to a Responses model managed by the Live session.

          - `ResponsesDelegationConfig responses`

            Backend model, prompt, and tools used when the Live session delegates a task to Responses.

            - `String model`

              The model used for server-owned Responses delegations.

            - `Optional<String> instructions`

              Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

            - `Optional<Long> maxOutputTokens`

              Maximum number of output tokens for each delegated response.

            - `Optional<Boolean> parallelToolCalls`

              Whether the delegated Responses model may request multiple tool calls in a single response.

            - `Optional<Reasoning> reasoning`

              Reasoning settings passed to each delegated Responses request.

              - `Optional<Effort> effort`

                How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

                - `NONE("none")`

                - `MINIMAL("minimal")`

                - `LOW("low")`

                - `MEDIUM("medium")`

                - `HIGH("high")`

                - `XHIGH("xhigh")`

              - `Optional<Summary> summary`

                The reasoning summary to request from the delegated Responses model, when supported.

                - `CONCISE("concise")`

                - `DETAILED("detailed")`

                - `AUTO("auto")`

            - `Optional<ServiceTier> serviceTier`

              Service tier for delegated Responses requests.

              - `AUTO("auto")`

              - `DEFAULT("default")`

              - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

              - `FLEX("flex")`

              - `PRIORITY("priority")`

              - `ULTRAFAST("ultrafast")`

            - `Optional<Text> text`

              Text generation settings passed to each delegated Responses request.

              - `Optional<Verbosity> verbosity`

                The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

                - `LOW("low")`

                - `MEDIUM("medium")`

                - `HIGH("high")`

            - `Optional<ToolChoice> toolChoice`

              Controls which tool the Responses backend uses when handling a task delegated by the Live model.

              - `enum LiveToolChoiceEnum:`

                - `AUTO("auto")`

                - `NONE("none")`

                - `REQUIRED("required")`

              - `class LiveFunctionToolChoiceParam:`

                - `String name`

                - `JsonValue; type "function"constant`

                  - `FUNCTION("function")`

              - `class LiveMcpToolChoiceParam:`

                - `String name`

                - `String serverLabel`

                - `JsonValue; type "mcp"constant`

                  - `MCP("mcp")`

            - `Optional<List<Tool>> tools`

              Tools available to the Responses backend while it handles tasks delegated by the Live model.

              - `class FunctionTool:`

                A function tool available to the Responses backend when the Live model delegates a task.

                - `String name`

                  The name the delegated Responses model uses when calling this function.

                - `JsonValue; type "function"constant`

                  The tool type. Always `function`.

                  - `FUNCTION("function")`

                - `Optional<String> description`

                  What the function does and when the delegated Responses model should call it.

                - `Optional<Parameters> parameters`

                  A JSON Schema object describing the arguments accepted by the function.

                - `Optional<Boolean> strict`

                  Whether the delegated Responses model must follow the function’s parameter schema exactly.

              - `JsonValue;`

                - `JsonValue; type "web_search"constant`

                  The tool type. Always `web_search`.

                  - `WEB_SEARCH("web_search")`

          - `JsonValue; type "responses"constant`

            The delegation owner. Always `responses` for tasks handled by the Responses API.

            - `RESPONSES("responses")`

      - `Optional<List<InitialItem>> input`

        Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

        - `Developer`

          - `List<Content> content`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `String text`

              The message text to include in the Live session’s initial conversation history.

            - `Optional<Type> type`

              The text content type. Always `input_text`.

              - `INPUT_TEXT("input_text")`

          - `JsonValue; role "developer"constant`

            The author of this history message. Always `developer`.

            - `DEVELOPER("developer")`

          - `Optional<String> id`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Optional<Status> status`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `INCOMPLETE("incomplete")`

            - `COMPLETED("completed")`

          - `Optional<Type> type`

            The history item type. Always `message`.

            - `MESSAGE("message")`

        - `User`

          - `List<Content> content`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `String text`

              The message text to include in the Live session’s initial conversation history.

            - `Optional<Type> type`

              The text content type. Always `input_text`.

              - `INPUT_TEXT("input_text")`

          - `JsonValue; role "user"constant`

            The author of this history message. Always `user`.

            - `USER("user")`

          - `Optional<String> id`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Optional<Status> status`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `INCOMPLETE("incomplete")`

            - `COMPLETED("completed")`

          - `Optional<Type> type`

            The history item type. Always `message`.

            - `MESSAGE("message")`

        - `Assistant`

          - `List<Content> content`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `class Text:`

              Assistant text supplied as conversation history when starting a Live session.

              - `String text`

                The message text to include in the Live session’s initial conversation history.

              - `Optional<Type> type`

                The text content type. Always `text`.

                - `TEXT("text")`

            - `class OutputText:`

              Assistant output text supplied as conversation history when starting a Live session.

              - `String text`

                The message text to include in the Live session’s initial conversation history.

              - `JsonValue; type "output_text"constant`

                The text content type. Always `output_text`.

                - `OUTPUT_TEXT("output_text")`

          - `JsonValue; role "assistant"constant`

            The author of this history message. Always `assistant`.

            - `ASSISTANT("assistant")`

          - `Optional<String> id`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Optional<Status> status`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `INCOMPLETE("incomplete")`

            - `COMPLETED("completed")`

          - `Optional<Type> type`

            The history item type. Always `message`.

            - `MESSAGE("message")`

      - `Optional<String> instructions`

        Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

      - `Optional<Boolean> store`

        Whether to store the session for later forking and recording download. Defaults to false for new sessions.

    - `JsonValue; type "session.started"constant`

      The event type, always `session.started`.

      - `SESSION_STARTED("session.started")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class SessionUpdatedEvent:`

    Returned when a Live session update is accepted. Contains the resolved session configuration after the update.

    - `String eventId`

      The unique ID of the Live server event.

    - `SessionResource session`

      The resolved Live session configuration and server-assigned session metadata.

    - `JsonValue; type "session.updated"constant`

      The event type, always `session.updated`.

      - `SESSION_UPDATED("session.updated")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class InputAudioMutedEvent:`

    Returned when a session.input_audio.mute command is accepted. Input audio is no longer sent to the model; sideband audio reflection continues.

    - `String eventId`

      The unique ID of the Live server event.

    - `JsonValue; type "session.input_audio.muted"constant`

      The event type, always `session.input_audio.muted`.

      - `SESSION_INPUT_AUDIO_MUTED("session.input_audio.muted")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class InputAudioUnmutedEvent:`

    Returned when a session.input_audio.unmute command is accepted. Input audio is sent to the model again.

    - `String eventId`

      The unique ID of the Live server event.

    - `JsonValue; type "session.input_audio.unmuted"constant`

      The event type, always `session.input_audio.unmuted`.

      - `SESSION_INPUT_AUDIO_UNMUTED("session.input_audio.unmuted")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class InstructionsAppendedEvent:`

    Returned when a session.instructions.append command is accepted into the Live session timeline. Acknowledges the appended instructions without guaranteeing that the model has acted on them.

    - `long endMs`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `String eventId`

      The unique ID of the Live server event.

    - `long startMs`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `JsonValue; type "session.instructions.appended"constant`

      The event type, always `session.instructions.appended`.

      - `SESSION_INSTRUCTIONS_APPENDED("session.instructions.appended")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class ThinkingAppendedEvent:`

    Returned when a session.thinking.append command is accepted into the Live session timeline. Acknowledges the added reasoning context without guaranteeing any spoken output.

    - `long endMs`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `String eventId`

      The unique ID of the Live server event.

    - `long startMs`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `JsonValue; type "session.thinking.appended"constant`

      The event type, always `session.thinking.appended`.

      - `SESSION_THINKING_APPENDED("session.thinking.appended")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class CommentaryAppendedEvent:`

    Returned when a session.commentary.append command is accepted into the Live session timeline. Acknowledges the added commentary without guaranteeing exact wording or completed audio playback.

    - `long endMs`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `String eventId`

      The unique ID of the Live server event.

    - `long startMs`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `JsonValue; type "session.commentary.appended"constant`

      The event type, always `session.commentary.appended`.

      - `SESSION_COMMENTARY_APPENDED("session.commentary.appended")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `SessionInputAudioAppend`

    - `String audio`

      Base64-encoded raw mono PCM16LE at 24 kHz received from the primary transport, reflected to the sideband before model-input muting. This server event uses the same audio key as the client command, but is not an acknowledgment of it.

    - `JsonValue; type "session.input_audio.append"constant`

      The event type, always `session.input_audio.append`.

      - `SESSION_INPUT_AUDIO_APPEND("session.input_audio.append")`

  - `class OutputAudioDeltaEvent:`

    An audio chunk generated by the Live model. Decode and play primary WebSocket chunks in delivery order using the configured session audio format. Sideband connections receive reflected output audio with timestamps.

    - `String delta`

      Base64-encoded raw audio. Primary WebSocket events use the session's configured format; reflected sideband events use mono PCM16LE at 24 kHz.

    - `JsonValue; type "session.output_audio.delta"constant`

      The event type, always `session.output_audio.delta`.

      - `SESSION_OUTPUT_AUDIO_DELTA("session.output_audio.delta")`

    - `Optional<Long> endMs`

      Exclusive session-relative end in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket. Dropped output frames leave gaps between reflected ranges.

    - `Optional<Long> startMs`

      Inclusive session-relative start in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket.

  - `class InputTranscriptDeltaEvent:`

    A transcript fragment for user input audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

    - `String delta`

      The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

    - `long endMs`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `String eventId`

      The unique ID of the Live server event.

    - `long startMs`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `JsonValue; type "session.input_transcript.delta"constant`

      The event type, always `session.input_transcript.delta`.

      - `SESSION_INPUT_TRANSCRIPT_DELTA("session.input_transcript.delta")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class OutputTranscriptDeltaEvent:`

    A transcript fragment for assistant output audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

    - `String delta`

      The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

    - `long endMs`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `String eventId`

      The unique ID of the Live server event.

    - `long startMs`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `JsonValue; type "session.output_transcript.delta"constant`

      The event type, always `session.output_transcript.delta`.

      - `SESSION_OUTPUT_TRANSCRIPT_DELTA("session.output_transcript.delta")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class DelegationCreatedEvent:`

    Returned when the Live model delegates work to your application or a Responses backend. Contains delegation metadata and the position on the session timeline where the work was delegated.

    - `Delegation delegation`

      The delegated work identifier and destination. This object contains metadata, not the task text.

      - `String id`

        The unique ID of the delegation. Use this as delegation_id when replying to client-owned work or correlating Responses events.

      - `Target target`

        Where the Live model delegated the work: `client` for your application, or `responses` for the configured Responses backend.

        - `CLIENT("client")`

        - `RESPONSES("responses")`

      - `JsonValue; type "delegation"constant`

        The object type, always `delegation`.

        - `DELEGATION("delegation")`

      - `Optional<String> responseId`

        The ID of the Responses API response associated with a Responses delegation. Omitted for client delegations.

    - `String eventId`

      The unique ID of the Live server event.

    - `long offsetMs`

      The position on the Live session timeline where the delegation was created, in milliseconds from the beginning of the session.

    - `JsonValue; type "session.delegation.created"constant`

      The event type, always `session.delegation.created`.

      - `SESSION_DELEGATION_CREATED("session.delegation.created")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class ResponseEvent:`

    A streaming Responses API event from a backend delegated to by the Live session. Use the outer delegation_id to associate the nested stream with its Live delegation.

    - `Event event`

      The nested Responses streaming event. Dispatch on its type field. Response lifecycle snapshots omit input and clear instructions, tools, and output to keep messages small; consume granular output events for the generated content.

    - `String eventId`

      The unique ID of the Live server event.

    - `JsonValue; type "response.event"constant`

      The event type, always `response.event`.

      - `RESPONSE_EVENT("response.event")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

    - `Optional<String> delegationId`

      The Live delegation associated with the nested Responses event. May be null or omitted when the event cannot be correlated with a delegation.

  - `class SessionUsageUpdatedEvent:`

    Reports cumulative Live audio usage and, when available, the most recent context-window usage. Delegated Responses token usage is reported separately in response.event events.

    - `String eventId`

      The unique ID of the Live server event.

    - `JsonValue; type "session.usage.updated"constant`

      The event type, always `session.usage.updated`.

      - `SESSION_USAGE_UPDATED("session.usage.updated")`

    - `SessionUsage usage`

      The cumulative Live audio usage so far.

      - `double seconds`

        The cumulative Live audio duration in seconds. Do not sum this value across usage events.

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

    - `Optional<ContextWindow> contextWindow`

      The latest measured Live context-window usage. Omitted when the context limit is unknown.

      - `double usageRatio`

        The latest active context token count divided by the Live model context limit. Can decrease after compaction and may lag between measured audio frames.

  - `class SessionClosedEvent:`

    Returned after the Live session finishes finalizing, with the close reason, final session snapshot, and cumulative audio usage. A connection closing without this event does not confirm successful finalization.

    - `String eventId`

      The unique ID of the Live server event.

    - `Reason reason`

      Why the Live session ended: `close_requested` for an application close or hangup request, `expired` for the session duration limit, `content` for a safety filter, `remote_hangup` for a graceful remote disconnect, or `connection_lost` for an unexpected primary or upstream disconnection.

      - `CLOSE_REQUESTED("close_requested")`

      - `EXPIRED("expired")`

      - `CONTENT("content")`

      - `REMOTE_HANGUP("remote_hangup")`

      - `CONNECTION_LOST("connection_lost")`

    - `SessionResource session`

      The resolved Live session configuration and server-assigned session metadata.

    - `JsonValue; type "session.closed"constant`

      The event type, always `session.closed`.

      - `SESSION_CLOSED("session.closed")`

    - `SessionUsage usage`

      The final cumulative Live audio usage after session finalization.

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class ErrorEvent:`

    Reports an error in the Live session, such as an invalid client command. Use error.client_event_id, when present, to identify the command that caused the error.

    - `Error error`

      Details of the Live error and the client command that caused it, when known.

      - `String code`

        A machine-readable code identifying the Live error, such as `unknown_parameter`.

      - `String message`

        A human-readable explanation of the Live error.

      - `String type`

        The category of error, such as `invalid_request_error` for an invalid Live client command.

      - `Optional<String> clientEventId`

        The event_id of the client command that caused the error, when supplied.

      - `Optional<String> param`

        The parameter that caused the error, when applicable, such as `session.voice`.

    - `String eventId`

      The unique ID of the Live server event.

    - `JsonValue; type "error"constant`

      The event type, always `error`.

      - `ERROR("error")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class InfoEvent:`

    An informational notice about the Live session, such as the event permissions applied to a frontend data channel.

    - `String code`

      A machine-readable code for the notice, such as `data_channel_permissions`.

    - `String eventId`

      The unique ID of the Live server event.

    - `String message`

      A human-readable explanation of the Live session notice.

    - `JsonValue; type "info"constant`

      The event type, always `info`.

      - `INFO("info")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `TransportDtmfReceived`

    - `String event`

    - `String eventId`

    - `JsonValue; type "transport.dtmf.received"constant`

      - `TRANSPORT_DTMF_RECEIVED("transport.dtmf.received")`

  - `TransportDtmfSend`

    - `String event`

    - `String eventId`

    - `JsonValue; type "transport.dtmf.send"constant`

      - `TRANSPORT_DTMF_SEND("transport.dtmf.send")`

    - `Optional<String> clientEventId`

      The event_id of the client command, when supplied.

  - `TransportRinging`

    - `String eventId`

    - `String sessionId`

      The canonical Live session ID.

    - `JsonValue; type "transport.ringing"constant`

      - `TRANSPORT_RINGING("transport.ringing")`

  - `TransportAnswered`

    - `String eventId`

    - `String sessionId`

      The canonical Live session ID.

    - `JsonValue; type "transport.answered"constant`

      - `TRANSPORT_ANSWERED("transport.answered")`

  - `TransportFailed`

    - `Error error`

      - `String code`

        The call setup failure code.

      - `String message`

      - `JsonValue; type "call_error"constant`

        - `CALL_ERROR("call_error")`

      - `Optional<String> param`

        The parameter related to the error, if any. Empty when no parameter applies.

    - `String eventId`

    - `String sessionId`

      The canonical Live session ID.

    - `JsonValue; type "transport.failed"constant`

      - `TRANSPORT_FAILED("transport.failed")`

### Server Event Selector

- `class ServerEventSelector:`

  A Live server event selector for the WebRTC frontend data channel.

  - `String type`

    The outer Live server event type. Use 'response.event' for Responses events.

  - `Optional<String> responseEvent`

    The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

### Session Close Event

- `class SessionCloseEvent:`

  Request that the Live session close. The terminal `session.closed` event contains the close reason and final usage.

  - `JsonValue; type "session.close"constant`

    The Live client event type. Always `session.close`.

    - `SESSION_CLOSE("session.close")`

  - `Optional<String> eventId`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Session Closed Event

- `class SessionClosedEvent:`

  Returned after the Live session finishes finalizing, with the close reason, final session snapshot, and cumulative audio usage. A connection closing without this event does not confirm successful finalization.

  - `String eventId`

    The unique ID of the Live server event.

  - `Reason reason`

    Why the Live session ended: `close_requested` for an application close or hangup request, `expired` for the session duration limit, `content` for a safety filter, `remote_hangup` for a graceful remote disconnect, or `connection_lost` for an unexpected primary or upstream disconnection.

    - `CLOSE_REQUESTED("close_requested")`

    - `EXPIRED("expired")`

    - `CONTENT("content")`

    - `REMOTE_HANGUP("remote_hangup")`

    - `CONNECTION_LOST("connection_lost")`

  - `SessionResource session`

    The resolved Live session configuration and server-assigned session metadata.

    - `String id`

      The unique ID of the Live session. Use this ID for sideband connections, forking, and recording download.

    - `long expiresAt`

      The Unix timestamp, in seconds, at which the Live session expires.

    - `Model model`

      The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

      - `GPT_LIVE_1("gpt-live-1")`

    - `JsonValue; status "active"constant`

      The status of the session snapshot. Always `active`, including the final snapshot in session.closed; use the event type to determine that the session has closed.

      - `ACTIVE("active")`

    - `Optional<Audio> audio`

      Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

      - `Optional<AudioFormat> format`

        Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

        - `AudioPcm`

          - `Rate rate`

            Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

            - `_16000(16000)`

            - `_24000(24000)`

          - `JsonValue; type "audio/pcm"constant`

            The audio encoding. Always `audio/pcm`.

            - `AUDIO_PCM("audio/pcm")`

        - `AudioPcmu`

          - `long rate`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `JsonValue; type "audio/pcmu"constant`

            The audio encoding. Always `audio/pcmu`.

            - `AUDIO_PCMU("audio/pcmu")`

        - `AudioPcma`

          - `long rate`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `JsonValue; type "audio/pcma"constant`

            The audio encoding. Always `audio/pcma`.

            - `AUDIO_PCMA("audio/pcma")`

      - `Optional<Output> output`

        The voice used for speech generated by the Live model.

        - `Optional<Voice> voice`

          The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

          - `String`

          - `enum BuiltInVoice:`

            A built-in voice available for Live speech.

            - `ALLOY("alloy")`

            - `ASH("ash")`

            - `BALLAD("ballad")`

            - `BEACON("beacon")`

            - `BOSSA("bossa")`

            - `CEDAR("cedar")`

            - `CINDER("cinder")`

            - `CORAL("coral")`

            - `DELTA("delta")`

            - `ECHO("echo")`

            - `GLEAM("gleam")`

            - `MARIN("marin")`

            - `MERIDIAN("meridian")`

            - `QUARTZ("quartz")`

            - `RIPPLE("ripple")`

            - `SAGE("sage")`

            - `SHIMMER("shimmer")`

            - `STONE("stone")`

            - `TEMPO("tempo")`

            - `VERSE("verse")`

            - `VESPER("vesper")`

            - `WILLOW("willow")`

          - `class CustomVoice:`

            - `String id`

    - `Optional<ClientConfig> client`

      Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

      - `DataChannelConfig dataChannel`

        Client and server event permissions for the WebRTC frontend data channel.

        - `Optional<AllowedClientEvents> allowedClientEvents`

          Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

          - `JsonValue;`

            - `ALL("all")`

          - `List<String>`

        - `Optional<AllowedServerEvents> allowedServerEvents`

          Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

          - `JsonValue;`

            - `ALL("all")`

          - `List<ServerEventSelector>`

            - `String type`

              The outer Live server event type. Use 'response.event' for Responses events.

            - `Optional<String> responseEvent`

              The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

    - `Optional<Delegation> delegation`

      Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

      - `class ClientDelegation:`

        Delegate tasks to your application. The Live session emits delegation events that your backend handles.

        - `JsonValue; type "client"constant`

          The delegation owner. Always `client` for tasks handled by your application.

          - `CLIENT("client")`

      - `class Responses:`

        Delegate tasks to a Responses model managed by the Live session.

        - `ResponsesDelegationConfig responses`

          Backend model, prompt, and tools used when the Live session delegates a task to Responses.

          - `String model`

            The model used for server-owned Responses delegations.

          - `Optional<String> instructions`

            Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

          - `Optional<Long> maxOutputTokens`

            Maximum number of output tokens for each delegated response.

          - `Optional<Boolean> parallelToolCalls`

            Whether the delegated Responses model may request multiple tool calls in a single response.

          - `Optional<Reasoning> reasoning`

            Reasoning settings passed to each delegated Responses request.

            - `Optional<Effort> effort`

              How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

              - `NONE("none")`

              - `MINIMAL("minimal")`

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

              - `XHIGH("xhigh")`

            - `Optional<Summary> summary`

              The reasoning summary to request from the delegated Responses model, when supported.

              - `CONCISE("concise")`

              - `DETAILED("detailed")`

              - `AUTO("auto")`

          - `Optional<ServiceTier> serviceTier`

            Service tier for delegated Responses requests.

            - `AUTO("auto")`

            - `DEFAULT("default")`

            - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

            - `FLEX("flex")`

            - `PRIORITY("priority")`

            - `ULTRAFAST("ultrafast")`

          - `Optional<Text> text`

            Text generation settings passed to each delegated Responses request.

            - `Optional<Verbosity> verbosity`

              The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

          - `Optional<ToolChoice> toolChoice`

            Controls which tool the Responses backend uses when handling a task delegated by the Live model.

            - `enum LiveToolChoiceEnum:`

              - `AUTO("auto")`

              - `NONE("none")`

              - `REQUIRED("required")`

            - `class LiveFunctionToolChoiceParam:`

              - `String name`

              - `JsonValue; type "function"constant`

                - `FUNCTION("function")`

            - `class LiveMcpToolChoiceParam:`

              - `String name`

              - `String serverLabel`

              - `JsonValue; type "mcp"constant`

                - `MCP("mcp")`

          - `Optional<List<Tool>> tools`

            Tools available to the Responses backend while it handles tasks delegated by the Live model.

            - `class FunctionTool:`

              A function tool available to the Responses backend when the Live model delegates a task.

              - `String name`

                The name the delegated Responses model uses when calling this function.

              - `JsonValue; type "function"constant`

                The tool type. Always `function`.

                - `FUNCTION("function")`

              - `Optional<String> description`

                What the function does and when the delegated Responses model should call it.

              - `Optional<Parameters> parameters`

                A JSON Schema object describing the arguments accepted by the function.

              - `Optional<Boolean> strict`

                Whether the delegated Responses model must follow the function’s parameter schema exactly.

            - `JsonValue;`

              - `JsonValue; type "web_search"constant`

                The tool type. Always `web_search`.

                - `WEB_SEARCH("web_search")`

        - `JsonValue; type "responses"constant`

          The delegation owner. Always `responses` for tasks handled by the Responses API.

          - `RESPONSES("responses")`

    - `Optional<List<InitialItem>> input`

      Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

      - `Developer`

        - `List<Content> content`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `String text`

            The message text to include in the Live session’s initial conversation history.

          - `Optional<Type> type`

            The text content type. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `JsonValue; role "developer"constant`

          The author of this history message. Always `developer`.

          - `DEVELOPER("developer")`

        - `Optional<String> id`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Optional<Status> status`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `INCOMPLETE("incomplete")`

          - `COMPLETED("completed")`

        - `Optional<Type> type`

          The history item type. Always `message`.

          - `MESSAGE("message")`

      - `User`

        - `List<Content> content`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `String text`

            The message text to include in the Live session’s initial conversation history.

          - `Optional<Type> type`

            The text content type. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `JsonValue; role "user"constant`

          The author of this history message. Always `user`.

          - `USER("user")`

        - `Optional<String> id`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Optional<Status> status`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `INCOMPLETE("incomplete")`

          - `COMPLETED("completed")`

        - `Optional<Type> type`

          The history item type. Always `message`.

          - `MESSAGE("message")`

      - `Assistant`

        - `List<Content> content`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `class Text:`

            Assistant text supplied as conversation history when starting a Live session.

            - `String text`

              The message text to include in the Live session’s initial conversation history.

            - `Optional<Type> type`

              The text content type. Always `text`.

              - `TEXT("text")`

          - `class OutputText:`

            Assistant output text supplied as conversation history when starting a Live session.

            - `String text`

              The message text to include in the Live session’s initial conversation history.

            - `JsonValue; type "output_text"constant`

              The text content type. Always `output_text`.

              - `OUTPUT_TEXT("output_text")`

        - `JsonValue; role "assistant"constant`

          The author of this history message. Always `assistant`.

          - `ASSISTANT("assistant")`

        - `Optional<String> id`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Optional<Status> status`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `INCOMPLETE("incomplete")`

          - `COMPLETED("completed")`

        - `Optional<Type> type`

          The history item type. Always `message`.

          - `MESSAGE("message")`

    - `Optional<String> instructions`

      Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

    - `Optional<Boolean> store`

      Whether to store the session for later forking and recording download. Defaults to false for new sessions.

  - `JsonValue; type "session.closed"constant`

    The event type, always `session.closed`.

    - `SESSION_CLOSED("session.closed")`

  - `SessionUsage usage`

    The final cumulative Live audio usage after session finalization.

    - `double seconds`

      The cumulative Live audio duration in seconds. Do not sum this value across usage events.

  - `Optional<String> clientEventId`

    The event_id of the client command associated with this server event, when supplied.

### Session Config

- `class SessionConfig:`

  Initial configuration for a Live session, including its model, conversation instructions, audio, and delegated task handling.

  - `Model model`

    The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

    - `GPT_LIVE_1("gpt-live-1")`

  - `Optional<Audio> audio`

    Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

    - `Optional<AudioFormat> format`

      Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

      - `AudioPcm`

        - `Rate rate`

          Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

          - `_16000(16000)`

          - `_24000(24000)`

        - `JsonValue; type "audio/pcm"constant`

          The audio encoding. Always `audio/pcm`.

          - `AUDIO_PCM("audio/pcm")`

      - `AudioPcmu`

        - `long rate`

          Audio sample rate in hertz. G.711 audio uses 8000 Hz.

        - `JsonValue; type "audio/pcmu"constant`

          The audio encoding. Always `audio/pcmu`.

          - `AUDIO_PCMU("audio/pcmu")`

      - `AudioPcma`

        - `long rate`

          Audio sample rate in hertz. G.711 audio uses 8000 Hz.

        - `JsonValue; type "audio/pcma"constant`

          The audio encoding. Always `audio/pcma`.

          - `AUDIO_PCMA("audio/pcma")`

    - `Optional<Output> output`

      The voice used for speech generated by the Live model.

      - `Optional<Voice> voice`

        The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

        - `String`

        - `enum BuiltInVoice:`

          A built-in voice available for Live speech.

          - `ALLOY("alloy")`

          - `ASH("ash")`

          - `BALLAD("ballad")`

          - `BEACON("beacon")`

          - `BOSSA("bossa")`

          - `CEDAR("cedar")`

          - `CINDER("cinder")`

          - `CORAL("coral")`

          - `DELTA("delta")`

          - `ECHO("echo")`

          - `GLEAM("gleam")`

          - `MARIN("marin")`

          - `MERIDIAN("meridian")`

          - `QUARTZ("quartz")`

          - `RIPPLE("ripple")`

          - `SAGE("sage")`

          - `SHIMMER("shimmer")`

          - `STONE("stone")`

          - `TEMPO("tempo")`

          - `VERSE("verse")`

          - `VESPER("vesper")`

          - `WILLOW("willow")`

        - `class CustomVoice:`

          - `String id`

  - `Optional<ClientConfig> client`

    Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

    - `DataChannelConfig dataChannel`

      Client and server event permissions for the WebRTC frontend data channel.

      - `Optional<AllowedClientEvents> allowedClientEvents`

        Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

        - `JsonValue;`

          - `ALL("all")`

        - `List<String>`

      - `Optional<AllowedServerEvents> allowedServerEvents`

        Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

        - `JsonValue;`

          - `ALL("all")`

        - `List<ServerEventSelector>`

          - `String type`

            The outer Live server event type. Use 'response.event' for Responses events.

          - `Optional<String> responseEvent`

            The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

  - `Optional<Delegation> delegation`

    Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

    - `class ClientDelegation:`

      Delegate tasks to your application. The Live session emits delegation events that your backend handles.

      - `JsonValue; type "client"constant`

        The delegation owner. Always `client` for tasks handled by your application.

        - `CLIENT("client")`

    - `class Responses:`

      Delegate tasks to a Responses model managed by the Live session.

      - `ResponsesDelegationConfig responses`

        Backend model, prompt, and tools used when the Live session delegates a task to Responses.

        - `String model`

          The model used for server-owned Responses delegations.

        - `Optional<String> instructions`

          Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

        - `Optional<Long> maxOutputTokens`

          Maximum number of output tokens for each delegated response.

        - `Optional<Boolean> parallelToolCalls`

          Whether the delegated Responses model may request multiple tool calls in a single response.

        - `Optional<Reasoning> reasoning`

          Reasoning settings passed to each delegated Responses request.

          - `Optional<Effort> effort`

            How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

            - `NONE("none")`

            - `MINIMAL("minimal")`

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

            - `XHIGH("xhigh")`

          - `Optional<Summary> summary`

            The reasoning summary to request from the delegated Responses model, when supported.

            - `CONCISE("concise")`

            - `DETAILED("detailed")`

            - `AUTO("auto")`

        - `Optional<ServiceTier> serviceTier`

          Service tier for delegated Responses requests.

          - `AUTO("auto")`

          - `DEFAULT("default")`

          - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

          - `FLEX("flex")`

          - `PRIORITY("priority")`

          - `ULTRAFAST("ultrafast")`

        - `Optional<Text> text`

          Text generation settings passed to each delegated Responses request.

          - `Optional<Verbosity> verbosity`

            The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

        - `Optional<ToolChoice> toolChoice`

          Controls which tool the Responses backend uses when handling a task delegated by the Live model.

          - `enum LiveToolChoiceEnum:`

            - `AUTO("auto")`

            - `NONE("none")`

            - `REQUIRED("required")`

          - `class LiveFunctionToolChoiceParam:`

            - `String name`

            - `JsonValue; type "function"constant`

              - `FUNCTION("function")`

          - `class LiveMcpToolChoiceParam:`

            - `String name`

            - `String serverLabel`

            - `JsonValue; type "mcp"constant`

              - `MCP("mcp")`

        - `Optional<List<Tool>> tools`

          Tools available to the Responses backend while it handles tasks delegated by the Live model.

          - `class FunctionTool:`

            A function tool available to the Responses backend when the Live model delegates a task.

            - `String name`

              The name the delegated Responses model uses when calling this function.

            - `JsonValue; type "function"constant`

              The tool type. Always `function`.

              - `FUNCTION("function")`

            - `Optional<String> description`

              What the function does and when the delegated Responses model should call it.

            - `Optional<Parameters> parameters`

              A JSON Schema object describing the arguments accepted by the function.

            - `Optional<Boolean> strict`

              Whether the delegated Responses model must follow the function’s parameter schema exactly.

          - `JsonValue;`

            - `JsonValue; type "web_search"constant`

              The tool type. Always `web_search`.

              - `WEB_SEARCH("web_search")`

      - `JsonValue; type "responses"constant`

        The delegation owner. Always `responses` for tasks handled by the Responses API.

        - `RESPONSES("responses")`

  - `Optional<List<InitialItem>> input`

    Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

    - `Developer`

      - `List<Content> content`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `String text`

          The message text to include in the Live session’s initial conversation history.

        - `Optional<Type> type`

          The text content type. Always `input_text`.

          - `INPUT_TEXT("input_text")`

      - `JsonValue; role "developer"constant`

        The author of this history message. Always `developer`.

        - `DEVELOPER("developer")`

      - `Optional<String> id`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Optional<Status> status`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `INCOMPLETE("incomplete")`

        - `COMPLETED("completed")`

      - `Optional<Type> type`

        The history item type. Always `message`.

        - `MESSAGE("message")`

    - `User`

      - `List<Content> content`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `String text`

          The message text to include in the Live session’s initial conversation history.

        - `Optional<Type> type`

          The text content type. Always `input_text`.

          - `INPUT_TEXT("input_text")`

      - `JsonValue; role "user"constant`

        The author of this history message. Always `user`.

        - `USER("user")`

      - `Optional<String> id`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Optional<Status> status`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `INCOMPLETE("incomplete")`

        - `COMPLETED("completed")`

      - `Optional<Type> type`

        The history item type. Always `message`.

        - `MESSAGE("message")`

    - `Assistant`

      - `List<Content> content`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `class Text:`

          Assistant text supplied as conversation history when starting a Live session.

          - `String text`

            The message text to include in the Live session’s initial conversation history.

          - `Optional<Type> type`

            The text content type. Always `text`.

            - `TEXT("text")`

        - `class OutputText:`

          Assistant output text supplied as conversation history when starting a Live session.

          - `String text`

            The message text to include in the Live session’s initial conversation history.

          - `JsonValue; type "output_text"constant`

            The text content type. Always `output_text`.

            - `OUTPUT_TEXT("output_text")`

      - `JsonValue; role "assistant"constant`

        The author of this history message. Always `assistant`.

        - `ASSISTANT("assistant")`

      - `Optional<String> id`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Optional<Status> status`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `INCOMPLETE("incomplete")`

        - `COMPLETED("completed")`

      - `Optional<Type> type`

        The history item type. Always `message`.

        - `MESSAGE("message")`

  - `Optional<String> instructions`

    Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

  - `Optional<Boolean> store`

    Whether to store the session for later forking and recording download. Defaults to false for new sessions.

### Session Resource

- `class SessionResource:`

  The resolved Live session configuration and server-assigned session metadata.

  - `String id`

    The unique ID of the Live session. Use this ID for sideband connections, forking, and recording download.

  - `long expiresAt`

    The Unix timestamp, in seconds, at which the Live session expires.

  - `Model model`

    The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

    - `GPT_LIVE_1("gpt-live-1")`

  - `JsonValue; status "active"constant`

    The status of the session snapshot. Always `active`, including the final snapshot in session.closed; use the event type to determine that the session has closed.

    - `ACTIVE("active")`

  - `Optional<Audio> audio`

    Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

    - `Optional<AudioFormat> format`

      Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

      - `AudioPcm`

        - `Rate rate`

          Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

          - `_16000(16000)`

          - `_24000(24000)`

        - `JsonValue; type "audio/pcm"constant`

          The audio encoding. Always `audio/pcm`.

          - `AUDIO_PCM("audio/pcm")`

      - `AudioPcmu`

        - `long rate`

          Audio sample rate in hertz. G.711 audio uses 8000 Hz.

        - `JsonValue; type "audio/pcmu"constant`

          The audio encoding. Always `audio/pcmu`.

          - `AUDIO_PCMU("audio/pcmu")`

      - `AudioPcma`

        - `long rate`

          Audio sample rate in hertz. G.711 audio uses 8000 Hz.

        - `JsonValue; type "audio/pcma"constant`

          The audio encoding. Always `audio/pcma`.

          - `AUDIO_PCMA("audio/pcma")`

    - `Optional<Output> output`

      The voice used for speech generated by the Live model.

      - `Optional<Voice> voice`

        The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

        - `String`

        - `enum BuiltInVoice:`

          A built-in voice available for Live speech.

          - `ALLOY("alloy")`

          - `ASH("ash")`

          - `BALLAD("ballad")`

          - `BEACON("beacon")`

          - `BOSSA("bossa")`

          - `CEDAR("cedar")`

          - `CINDER("cinder")`

          - `CORAL("coral")`

          - `DELTA("delta")`

          - `ECHO("echo")`

          - `GLEAM("gleam")`

          - `MARIN("marin")`

          - `MERIDIAN("meridian")`

          - `QUARTZ("quartz")`

          - `RIPPLE("ripple")`

          - `SAGE("sage")`

          - `SHIMMER("shimmer")`

          - `STONE("stone")`

          - `TEMPO("tempo")`

          - `VERSE("verse")`

          - `VESPER("vesper")`

          - `WILLOW("willow")`

        - `class CustomVoice:`

          - `String id`

  - `Optional<ClientConfig> client`

    Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

    - `DataChannelConfig dataChannel`

      Client and server event permissions for the WebRTC frontend data channel.

      - `Optional<AllowedClientEvents> allowedClientEvents`

        Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

        - `JsonValue;`

          - `ALL("all")`

        - `List<String>`

      - `Optional<AllowedServerEvents> allowedServerEvents`

        Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

        - `JsonValue;`

          - `ALL("all")`

        - `List<ServerEventSelector>`

          - `String type`

            The outer Live server event type. Use 'response.event' for Responses events.

          - `Optional<String> responseEvent`

            The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

  - `Optional<Delegation> delegation`

    Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

    - `class ClientDelegation:`

      Delegate tasks to your application. The Live session emits delegation events that your backend handles.

      - `JsonValue; type "client"constant`

        The delegation owner. Always `client` for tasks handled by your application.

        - `CLIENT("client")`

    - `class Responses:`

      Delegate tasks to a Responses model managed by the Live session.

      - `ResponsesDelegationConfig responses`

        Backend model, prompt, and tools used when the Live session delegates a task to Responses.

        - `String model`

          The model used for server-owned Responses delegations.

        - `Optional<String> instructions`

          Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

        - `Optional<Long> maxOutputTokens`

          Maximum number of output tokens for each delegated response.

        - `Optional<Boolean> parallelToolCalls`

          Whether the delegated Responses model may request multiple tool calls in a single response.

        - `Optional<Reasoning> reasoning`

          Reasoning settings passed to each delegated Responses request.

          - `Optional<Effort> effort`

            How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

            - `NONE("none")`

            - `MINIMAL("minimal")`

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

            - `XHIGH("xhigh")`

          - `Optional<Summary> summary`

            The reasoning summary to request from the delegated Responses model, when supported.

            - `CONCISE("concise")`

            - `DETAILED("detailed")`

            - `AUTO("auto")`

        - `Optional<ServiceTier> serviceTier`

          Service tier for delegated Responses requests.

          - `AUTO("auto")`

          - `DEFAULT("default")`

          - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

          - `FLEX("flex")`

          - `PRIORITY("priority")`

          - `ULTRAFAST("ultrafast")`

        - `Optional<Text> text`

          Text generation settings passed to each delegated Responses request.

          - `Optional<Verbosity> verbosity`

            The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

        - `Optional<ToolChoice> toolChoice`

          Controls which tool the Responses backend uses when handling a task delegated by the Live model.

          - `enum LiveToolChoiceEnum:`

            - `AUTO("auto")`

            - `NONE("none")`

            - `REQUIRED("required")`

          - `class LiveFunctionToolChoiceParam:`

            - `String name`

            - `JsonValue; type "function"constant`

              - `FUNCTION("function")`

          - `class LiveMcpToolChoiceParam:`

            - `String name`

            - `String serverLabel`

            - `JsonValue; type "mcp"constant`

              - `MCP("mcp")`

        - `Optional<List<Tool>> tools`

          Tools available to the Responses backend while it handles tasks delegated by the Live model.

          - `class FunctionTool:`

            A function tool available to the Responses backend when the Live model delegates a task.

            - `String name`

              The name the delegated Responses model uses when calling this function.

            - `JsonValue; type "function"constant`

              The tool type. Always `function`.

              - `FUNCTION("function")`

            - `Optional<String> description`

              What the function does and when the delegated Responses model should call it.

            - `Optional<Parameters> parameters`

              A JSON Schema object describing the arguments accepted by the function.

            - `Optional<Boolean> strict`

              Whether the delegated Responses model must follow the function’s parameter schema exactly.

          - `JsonValue;`

            - `JsonValue; type "web_search"constant`

              The tool type. Always `web_search`.

              - `WEB_SEARCH("web_search")`

      - `JsonValue; type "responses"constant`

        The delegation owner. Always `responses` for tasks handled by the Responses API.

        - `RESPONSES("responses")`

  - `Optional<List<InitialItem>> input`

    Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

    - `Developer`

      - `List<Content> content`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `String text`

          The message text to include in the Live session’s initial conversation history.

        - `Optional<Type> type`

          The text content type. Always `input_text`.

          - `INPUT_TEXT("input_text")`

      - `JsonValue; role "developer"constant`

        The author of this history message. Always `developer`.

        - `DEVELOPER("developer")`

      - `Optional<String> id`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Optional<Status> status`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `INCOMPLETE("incomplete")`

        - `COMPLETED("completed")`

      - `Optional<Type> type`

        The history item type. Always `message`.

        - `MESSAGE("message")`

    - `User`

      - `List<Content> content`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `String text`

          The message text to include in the Live session’s initial conversation history.

        - `Optional<Type> type`

          The text content type. Always `input_text`.

          - `INPUT_TEXT("input_text")`

      - `JsonValue; role "user"constant`

        The author of this history message. Always `user`.

        - `USER("user")`

      - `Optional<String> id`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Optional<Status> status`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `INCOMPLETE("incomplete")`

        - `COMPLETED("completed")`

      - `Optional<Type> type`

        The history item type. Always `message`.

        - `MESSAGE("message")`

    - `Assistant`

      - `List<Content> content`

        The message content. Supply exactly one text part for the initial Live conversation history.

        - `class Text:`

          Assistant text supplied as conversation history when starting a Live session.

          - `String text`

            The message text to include in the Live session’s initial conversation history.

          - `Optional<Type> type`

            The text content type. Always `text`.

            - `TEXT("text")`

        - `class OutputText:`

          Assistant output text supplied as conversation history when starting a Live session.

          - `String text`

            The message text to include in the Live session’s initial conversation history.

          - `JsonValue; type "output_text"constant`

            The text content type. Always `output_text`.

            - `OUTPUT_TEXT("output_text")`

      - `JsonValue; role "assistant"constant`

        The author of this history message. Always `assistant`.

        - `ASSISTANT("assistant")`

      - `Optional<String> id`

        An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

      - `Optional<Status> status`

        The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

        - `INCOMPLETE("incomplete")`

        - `COMPLETED("completed")`

      - `Optional<Type> type`

        The history item type. Always `message`.

        - `MESSAGE("message")`

  - `Optional<String> instructions`

    Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

  - `Optional<Boolean> store`

    Whether to store the session for later forking and recording download. Defaults to false for new sessions.

### Session Start Event

- `class SessionStartEvent:`

  Start a Live session on a primary WebSocket. Send this event before other commands and wait for `session.started`.

  - `SessionConfig session`

    Initial configuration for a primary WebSocket. Send session.start first and wait for session.started before application commands. WebRTC creation already starts the session; do not send this event again on its data channel.

    - `Model model`

      The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

      - `GPT_LIVE_1("gpt-live-1")`

    - `Optional<Audio> audio`

      Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

      - `Optional<AudioFormat> format`

        Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

        - `AudioPcm`

          - `Rate rate`

            Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

            - `_16000(16000)`

            - `_24000(24000)`

          - `JsonValue; type "audio/pcm"constant`

            The audio encoding. Always `audio/pcm`.

            - `AUDIO_PCM("audio/pcm")`

        - `AudioPcmu`

          - `long rate`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `JsonValue; type "audio/pcmu"constant`

            The audio encoding. Always `audio/pcmu`.

            - `AUDIO_PCMU("audio/pcmu")`

        - `AudioPcma`

          - `long rate`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `JsonValue; type "audio/pcma"constant`

            The audio encoding. Always `audio/pcma`.

            - `AUDIO_PCMA("audio/pcma")`

      - `Optional<Output> output`

        The voice used for speech generated by the Live model.

        - `Optional<Voice> voice`

          The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

          - `String`

          - `enum BuiltInVoice:`

            A built-in voice available for Live speech.

            - `ALLOY("alloy")`

            - `ASH("ash")`

            - `BALLAD("ballad")`

            - `BEACON("beacon")`

            - `BOSSA("bossa")`

            - `CEDAR("cedar")`

            - `CINDER("cinder")`

            - `CORAL("coral")`

            - `DELTA("delta")`

            - `ECHO("echo")`

            - `GLEAM("gleam")`

            - `MARIN("marin")`

            - `MERIDIAN("meridian")`

            - `QUARTZ("quartz")`

            - `RIPPLE("ripple")`

            - `SAGE("sage")`

            - `SHIMMER("shimmer")`

            - `STONE("stone")`

            - `TEMPO("tempo")`

            - `VERSE("verse")`

            - `VESPER("vesper")`

            - `WILLOW("willow")`

          - `class CustomVoice:`

            - `String id`

    - `Optional<ClientConfig> client`

      Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

      - `DataChannelConfig dataChannel`

        Client and server event permissions for the WebRTC frontend data channel.

        - `Optional<AllowedClientEvents> allowedClientEvents`

          Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

          - `JsonValue;`

            - `ALL("all")`

          - `List<String>`

        - `Optional<AllowedServerEvents> allowedServerEvents`

          Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

          - `JsonValue;`

            - `ALL("all")`

          - `List<ServerEventSelector>`

            - `String type`

              The outer Live server event type. Use 'response.event' for Responses events.

            - `Optional<String> responseEvent`

              The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

    - `Optional<Delegation> delegation`

      Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

      - `class ClientDelegation:`

        Delegate tasks to your application. The Live session emits delegation events that your backend handles.

        - `JsonValue; type "client"constant`

          The delegation owner. Always `client` for tasks handled by your application.

          - `CLIENT("client")`

      - `class Responses:`

        Delegate tasks to a Responses model managed by the Live session.

        - `ResponsesDelegationConfig responses`

          Backend model, prompt, and tools used when the Live session delegates a task to Responses.

          - `String model`

            The model used for server-owned Responses delegations.

          - `Optional<String> instructions`

            Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

          - `Optional<Long> maxOutputTokens`

            Maximum number of output tokens for each delegated response.

          - `Optional<Boolean> parallelToolCalls`

            Whether the delegated Responses model may request multiple tool calls in a single response.

          - `Optional<Reasoning> reasoning`

            Reasoning settings passed to each delegated Responses request.

            - `Optional<Effort> effort`

              How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

              - `NONE("none")`

              - `MINIMAL("minimal")`

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

              - `XHIGH("xhigh")`

            - `Optional<Summary> summary`

              The reasoning summary to request from the delegated Responses model, when supported.

              - `CONCISE("concise")`

              - `DETAILED("detailed")`

              - `AUTO("auto")`

          - `Optional<ServiceTier> serviceTier`

            Service tier for delegated Responses requests.

            - `AUTO("auto")`

            - `DEFAULT("default")`

            - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

            - `FLEX("flex")`

            - `PRIORITY("priority")`

            - `ULTRAFAST("ultrafast")`

          - `Optional<Text> text`

            Text generation settings passed to each delegated Responses request.

            - `Optional<Verbosity> verbosity`

              The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

          - `Optional<ToolChoice> toolChoice`

            Controls which tool the Responses backend uses when handling a task delegated by the Live model.

            - `enum LiveToolChoiceEnum:`

              - `AUTO("auto")`

              - `NONE("none")`

              - `REQUIRED("required")`

            - `class LiveFunctionToolChoiceParam:`

              - `String name`

              - `JsonValue; type "function"constant`

                - `FUNCTION("function")`

            - `class LiveMcpToolChoiceParam:`

              - `String name`

              - `String serverLabel`

              - `JsonValue; type "mcp"constant`

                - `MCP("mcp")`

          - `Optional<List<Tool>> tools`

            Tools available to the Responses backend while it handles tasks delegated by the Live model.

            - `class FunctionTool:`

              A function tool available to the Responses backend when the Live model delegates a task.

              - `String name`

                The name the delegated Responses model uses when calling this function.

              - `JsonValue; type "function"constant`

                The tool type. Always `function`.

                - `FUNCTION("function")`

              - `Optional<String> description`

                What the function does and when the delegated Responses model should call it.

              - `Optional<Parameters> parameters`

                A JSON Schema object describing the arguments accepted by the function.

              - `Optional<Boolean> strict`

                Whether the delegated Responses model must follow the function’s parameter schema exactly.

            - `JsonValue;`

              - `JsonValue; type "web_search"constant`

                The tool type. Always `web_search`.

                - `WEB_SEARCH("web_search")`

        - `JsonValue; type "responses"constant`

          The delegation owner. Always `responses` for tasks handled by the Responses API.

          - `RESPONSES("responses")`

    - `Optional<List<InitialItem>> input`

      Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

      - `Developer`

        - `List<Content> content`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `String text`

            The message text to include in the Live session’s initial conversation history.

          - `Optional<Type> type`

            The text content type. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `JsonValue; role "developer"constant`

          The author of this history message. Always `developer`.

          - `DEVELOPER("developer")`

        - `Optional<String> id`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Optional<Status> status`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `INCOMPLETE("incomplete")`

          - `COMPLETED("completed")`

        - `Optional<Type> type`

          The history item type. Always `message`.

          - `MESSAGE("message")`

      - `User`

        - `List<Content> content`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `String text`

            The message text to include in the Live session’s initial conversation history.

          - `Optional<Type> type`

            The text content type. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `JsonValue; role "user"constant`

          The author of this history message. Always `user`.

          - `USER("user")`

        - `Optional<String> id`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Optional<Status> status`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `INCOMPLETE("incomplete")`

          - `COMPLETED("completed")`

        - `Optional<Type> type`

          The history item type. Always `message`.

          - `MESSAGE("message")`

      - `Assistant`

        - `List<Content> content`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `class Text:`

            Assistant text supplied as conversation history when starting a Live session.

            - `String text`

              The message text to include in the Live session’s initial conversation history.

            - `Optional<Type> type`

              The text content type. Always `text`.

              - `TEXT("text")`

          - `class OutputText:`

            Assistant output text supplied as conversation history when starting a Live session.

            - `String text`

              The message text to include in the Live session’s initial conversation history.

            - `JsonValue; type "output_text"constant`

              The text content type. Always `output_text`.

              - `OUTPUT_TEXT("output_text")`

        - `JsonValue; role "assistant"constant`

          The author of this history message. Always `assistant`.

          - `ASSISTANT("assistant")`

        - `Optional<String> id`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Optional<Status> status`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `INCOMPLETE("incomplete")`

          - `COMPLETED("completed")`

        - `Optional<Type> type`

          The history item type. Always `message`.

          - `MESSAGE("message")`

    - `Optional<String> instructions`

      Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

    - `Optional<Boolean> store`

      Whether to store the session for later forking and recording download. Defaults to false for new sessions.

  - `JsonValue; type "session.start"constant`

    The Live client event type. Always `session.start`.

    - `SESSION_START("session.start")`

  - `Optional<String> eventId`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Session Started Event

- `class SessionStartedEvent:`

  Returned when a Live session has started. Contains the resolved session configuration, including server defaults.

  - `String eventId`

    The unique ID of the Live server event.

  - `SessionResource session`

    The resolved Live session configuration and server-assigned session metadata.

    - `String id`

      The unique ID of the Live session. Use this ID for sideband connections, forking, and recording download.

    - `long expiresAt`

      The Unix timestamp, in seconds, at which the Live session expires.

    - `Model model`

      The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

      - `GPT_LIVE_1("gpt-live-1")`

    - `JsonValue; status "active"constant`

      The status of the session snapshot. Always `active`, including the final snapshot in session.closed; use the event type to determine that the session has closed.

      - `ACTIVE("active")`

    - `Optional<Audio> audio`

      Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

      - `Optional<AudioFormat> format`

        Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

        - `AudioPcm`

          - `Rate rate`

            Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

            - `_16000(16000)`

            - `_24000(24000)`

          - `JsonValue; type "audio/pcm"constant`

            The audio encoding. Always `audio/pcm`.

            - `AUDIO_PCM("audio/pcm")`

        - `AudioPcmu`

          - `long rate`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `JsonValue; type "audio/pcmu"constant`

            The audio encoding. Always `audio/pcmu`.

            - `AUDIO_PCMU("audio/pcmu")`

        - `AudioPcma`

          - `long rate`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `JsonValue; type "audio/pcma"constant`

            The audio encoding. Always `audio/pcma`.

            - `AUDIO_PCMA("audio/pcma")`

      - `Optional<Output> output`

        The voice used for speech generated by the Live model.

        - `Optional<Voice> voice`

          The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

          - `String`

          - `enum BuiltInVoice:`

            A built-in voice available for Live speech.

            - `ALLOY("alloy")`

            - `ASH("ash")`

            - `BALLAD("ballad")`

            - `BEACON("beacon")`

            - `BOSSA("bossa")`

            - `CEDAR("cedar")`

            - `CINDER("cinder")`

            - `CORAL("coral")`

            - `DELTA("delta")`

            - `ECHO("echo")`

            - `GLEAM("gleam")`

            - `MARIN("marin")`

            - `MERIDIAN("meridian")`

            - `QUARTZ("quartz")`

            - `RIPPLE("ripple")`

            - `SAGE("sage")`

            - `SHIMMER("shimmer")`

            - `STONE("stone")`

            - `TEMPO("tempo")`

            - `VERSE("verse")`

            - `VESPER("vesper")`

            - `WILLOW("willow")`

          - `class CustomVoice:`

            - `String id`

    - `Optional<ClientConfig> client`

      Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

      - `DataChannelConfig dataChannel`

        Client and server event permissions for the WebRTC frontend data channel.

        - `Optional<AllowedClientEvents> allowedClientEvents`

          Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

          - `JsonValue;`

            - `ALL("all")`

          - `List<String>`

        - `Optional<AllowedServerEvents> allowedServerEvents`

          Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

          - `JsonValue;`

            - `ALL("all")`

          - `List<ServerEventSelector>`

            - `String type`

              The outer Live server event type. Use 'response.event' for Responses events.

            - `Optional<String> responseEvent`

              The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

    - `Optional<Delegation> delegation`

      Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

      - `class ClientDelegation:`

        Delegate tasks to your application. The Live session emits delegation events that your backend handles.

        - `JsonValue; type "client"constant`

          The delegation owner. Always `client` for tasks handled by your application.

          - `CLIENT("client")`

      - `class Responses:`

        Delegate tasks to a Responses model managed by the Live session.

        - `ResponsesDelegationConfig responses`

          Backend model, prompt, and tools used when the Live session delegates a task to Responses.

          - `String model`

            The model used for server-owned Responses delegations.

          - `Optional<String> instructions`

            Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

          - `Optional<Long> maxOutputTokens`

            Maximum number of output tokens for each delegated response.

          - `Optional<Boolean> parallelToolCalls`

            Whether the delegated Responses model may request multiple tool calls in a single response.

          - `Optional<Reasoning> reasoning`

            Reasoning settings passed to each delegated Responses request.

            - `Optional<Effort> effort`

              How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

              - `NONE("none")`

              - `MINIMAL("minimal")`

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

              - `XHIGH("xhigh")`

            - `Optional<Summary> summary`

              The reasoning summary to request from the delegated Responses model, when supported.

              - `CONCISE("concise")`

              - `DETAILED("detailed")`

              - `AUTO("auto")`

          - `Optional<ServiceTier> serviceTier`

            Service tier for delegated Responses requests.

            - `AUTO("auto")`

            - `DEFAULT("default")`

            - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

            - `FLEX("flex")`

            - `PRIORITY("priority")`

            - `ULTRAFAST("ultrafast")`

          - `Optional<Text> text`

            Text generation settings passed to each delegated Responses request.

            - `Optional<Verbosity> verbosity`

              The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

          - `Optional<ToolChoice> toolChoice`

            Controls which tool the Responses backend uses when handling a task delegated by the Live model.

            - `enum LiveToolChoiceEnum:`

              - `AUTO("auto")`

              - `NONE("none")`

              - `REQUIRED("required")`

            - `class LiveFunctionToolChoiceParam:`

              - `String name`

              - `JsonValue; type "function"constant`

                - `FUNCTION("function")`

            - `class LiveMcpToolChoiceParam:`

              - `String name`

              - `String serverLabel`

              - `JsonValue; type "mcp"constant`

                - `MCP("mcp")`

          - `Optional<List<Tool>> tools`

            Tools available to the Responses backend while it handles tasks delegated by the Live model.

            - `class FunctionTool:`

              A function tool available to the Responses backend when the Live model delegates a task.

              - `String name`

                The name the delegated Responses model uses when calling this function.

              - `JsonValue; type "function"constant`

                The tool type. Always `function`.

                - `FUNCTION("function")`

              - `Optional<String> description`

                What the function does and when the delegated Responses model should call it.

              - `Optional<Parameters> parameters`

                A JSON Schema object describing the arguments accepted by the function.

              - `Optional<Boolean> strict`

                Whether the delegated Responses model must follow the function’s parameter schema exactly.

            - `JsonValue;`

              - `JsonValue; type "web_search"constant`

                The tool type. Always `web_search`.

                - `WEB_SEARCH("web_search")`

        - `JsonValue; type "responses"constant`

          The delegation owner. Always `responses` for tasks handled by the Responses API.

          - `RESPONSES("responses")`

    - `Optional<List<InitialItem>> input`

      Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

      - `Developer`

        - `List<Content> content`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `String text`

            The message text to include in the Live session’s initial conversation history.

          - `Optional<Type> type`

            The text content type. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `JsonValue; role "developer"constant`

          The author of this history message. Always `developer`.

          - `DEVELOPER("developer")`

        - `Optional<String> id`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Optional<Status> status`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `INCOMPLETE("incomplete")`

          - `COMPLETED("completed")`

        - `Optional<Type> type`

          The history item type. Always `message`.

          - `MESSAGE("message")`

      - `User`

        - `List<Content> content`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `String text`

            The message text to include in the Live session’s initial conversation history.

          - `Optional<Type> type`

            The text content type. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `JsonValue; role "user"constant`

          The author of this history message. Always `user`.

          - `USER("user")`

        - `Optional<String> id`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Optional<Status> status`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `INCOMPLETE("incomplete")`

          - `COMPLETED("completed")`

        - `Optional<Type> type`

          The history item type. Always `message`.

          - `MESSAGE("message")`

      - `Assistant`

        - `List<Content> content`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `class Text:`

            Assistant text supplied as conversation history when starting a Live session.

            - `String text`

              The message text to include in the Live session’s initial conversation history.

            - `Optional<Type> type`

              The text content type. Always `text`.

              - `TEXT("text")`

          - `class OutputText:`

            Assistant output text supplied as conversation history when starting a Live session.

            - `String text`

              The message text to include in the Live session’s initial conversation history.

            - `JsonValue; type "output_text"constant`

              The text content type. Always `output_text`.

              - `OUTPUT_TEXT("output_text")`

        - `JsonValue; role "assistant"constant`

          The author of this history message. Always `assistant`.

          - `ASSISTANT("assistant")`

        - `Optional<String> id`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Optional<Status> status`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `INCOMPLETE("incomplete")`

          - `COMPLETED("completed")`

        - `Optional<Type> type`

          The history item type. Always `message`.

          - `MESSAGE("message")`

    - `Optional<String> instructions`

      Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

    - `Optional<Boolean> store`

      Whether to store the session for later forking and recording download. Defaults to false for new sessions.

  - `JsonValue; type "session.started"constant`

    The event type, always `session.started`.

    - `SESSION_STARTED("session.started")`

  - `Optional<String> clientEventId`

    The event_id of the client command associated with this server event, when supplied.

### Session Update Config

- `class SessionUpdateConfig:`

  Changes to an active Live session. Only delegation backend settings can be updated after startup.

  - `Optional<Delegation> delegation`

    Delegation settings to update. The delegation type must match the current session; omitted settings retain their values.

    - `class ClientDelegation:`

      Delegate tasks to your application. The Live session emits delegation events that your backend handles.

      - `JsonValue; type "client"constant`

        The delegation owner. Always `client` for tasks handled by your application.

        - `CLIENT("client")`

    - `class Responses:`

      Update the Responses backend for an existing Live session without changing delegation ownership.

      - `JsonValue; type "responses"constant`

        The delegation owner. Always `responses` for tasks handled by the Responses API.

        - `RESPONSES("responses")`

      - `Optional<ResponsesDelegationUpdateConfig> responses`

        Responses backend settings to update. Omitted settings keep their existing values.

        - `Optional<String> instructions`

          Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

        - `Optional<Long> maxOutputTokens`

          Maximum number of output tokens for each delegated response.

        - `Optional<String> model`

          The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.

        - `Optional<Boolean> parallelToolCalls`

          Whether the delegated Responses model may request multiple tool calls in a single response.

        - `Optional<Reasoning> reasoning`

          Reasoning settings passed to each delegated Responses request.

          - `Optional<Effort> effort`

            How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

            - `NONE("none")`

            - `MINIMAL("minimal")`

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

            - `XHIGH("xhigh")`

          - `Optional<Summary> summary`

            The reasoning summary to request from the delegated Responses model, when supported.

            - `CONCISE("concise")`

            - `DETAILED("detailed")`

            - `AUTO("auto")`

        - `Optional<ServiceTier> serviceTier`

          Service tier for delegated Responses requests.

          - `AUTO("auto")`

          - `DEFAULT("default")`

          - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

          - `FLEX("flex")`

          - `PRIORITY("priority")`

          - `ULTRAFAST("ultrafast")`

        - `Optional<Text> text`

          Text generation settings passed to each delegated Responses request.

          - `Optional<Verbosity> verbosity`

            The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

        - `Optional<ToolChoice> toolChoice`

          Controls which tool the Responses backend uses when handling a task delegated by the Live model.

          - `enum LiveToolChoiceEnum:`

            - `AUTO("auto")`

            - `NONE("none")`

            - `REQUIRED("required")`

          - `class LiveFunctionToolChoiceParam:`

            - `String name`

            - `JsonValue; type "function"constant`

              - `FUNCTION("function")`

          - `class LiveMcpToolChoiceParam:`

            - `String name`

            - `String serverLabel`

            - `JsonValue; type "mcp"constant`

              - `MCP("mcp")`

        - `Optional<List<Tool>> tools`

          Tools available to the Responses backend while it handles tasks delegated by the Live model.

          - `class FunctionTool:`

            A function tool available to the Responses backend when the Live model delegates a task.

            - `String name`

              The name the delegated Responses model uses when calling this function.

            - `JsonValue; type "function"constant`

              The tool type. Always `function`.

              - `FUNCTION("function")`

            - `Optional<String> description`

              What the function does and when the delegated Responses model should call it.

            - `Optional<Parameters> parameters`

              A JSON Schema object describing the arguments accepted by the function.

            - `Optional<Boolean> strict`

              Whether the delegated Responses model must follow the function’s parameter schema exactly.

          - `JsonValue;`

            - `JsonValue; type "web_search"constant`

              The tool type. Always `web_search`.

              - `WEB_SEARCH("web_search")`

### Session Update Event

- `class SessionUpdateEvent:`

  Update the delegation settings of an active Live session. The server acknowledges accepted changes with `session.updated`.

  - `SessionUpdateConfig session`

    Sparse delegation updates. Omitted settings retain their values. The delegation type cannot change, including resetting Responses delegation to null or client. Model, frontend instructions, audio, and startup input are immutable.

    - `Optional<Delegation> delegation`

      Delegation settings to update. The delegation type must match the current session; omitted settings retain their values.

      - `class ClientDelegation:`

        Delegate tasks to your application. The Live session emits delegation events that your backend handles.

        - `JsonValue; type "client"constant`

          The delegation owner. Always `client` for tasks handled by your application.

          - `CLIENT("client")`

      - `class Responses:`

        Update the Responses backend for an existing Live session without changing delegation ownership.

        - `JsonValue; type "responses"constant`

          The delegation owner. Always `responses` for tasks handled by the Responses API.

          - `RESPONSES("responses")`

        - `Optional<ResponsesDelegationUpdateConfig> responses`

          Responses backend settings to update. Omitted settings keep their existing values.

          - `Optional<String> instructions`

            Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

          - `Optional<Long> maxOutputTokens`

            Maximum number of output tokens for each delegated response.

          - `Optional<String> model`

            The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.

          - `Optional<Boolean> parallelToolCalls`

            Whether the delegated Responses model may request multiple tool calls in a single response.

          - `Optional<Reasoning> reasoning`

            Reasoning settings passed to each delegated Responses request.

            - `Optional<Effort> effort`

              How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

              - `NONE("none")`

              - `MINIMAL("minimal")`

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

              - `XHIGH("xhigh")`

            - `Optional<Summary> summary`

              The reasoning summary to request from the delegated Responses model, when supported.

              - `CONCISE("concise")`

              - `DETAILED("detailed")`

              - `AUTO("auto")`

          - `Optional<ServiceTier> serviceTier`

            Service tier for delegated Responses requests.

            - `AUTO("auto")`

            - `DEFAULT("default")`

            - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

            - `FLEX("flex")`

            - `PRIORITY("priority")`

            - `ULTRAFAST("ultrafast")`

          - `Optional<Text> text`

            Text generation settings passed to each delegated Responses request.

            - `Optional<Verbosity> verbosity`

              The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

          - `Optional<ToolChoice> toolChoice`

            Controls which tool the Responses backend uses when handling a task delegated by the Live model.

            - `enum LiveToolChoiceEnum:`

              - `AUTO("auto")`

              - `NONE("none")`

              - `REQUIRED("required")`

            - `class LiveFunctionToolChoiceParam:`

              - `String name`

              - `JsonValue; type "function"constant`

                - `FUNCTION("function")`

            - `class LiveMcpToolChoiceParam:`

              - `String name`

              - `String serverLabel`

              - `JsonValue; type "mcp"constant`

                - `MCP("mcp")`

          - `Optional<List<Tool>> tools`

            Tools available to the Responses backend while it handles tasks delegated by the Live model.

            - `class FunctionTool:`

              A function tool available to the Responses backend when the Live model delegates a task.

              - `String name`

                The name the delegated Responses model uses when calling this function.

              - `JsonValue; type "function"constant`

                The tool type. Always `function`.

                - `FUNCTION("function")`

              - `Optional<String> description`

                What the function does and when the delegated Responses model should call it.

              - `Optional<Parameters> parameters`

                A JSON Schema object describing the arguments accepted by the function.

              - `Optional<Boolean> strict`

                Whether the delegated Responses model must follow the function’s parameter schema exactly.

            - `JsonValue;`

              - `JsonValue; type "web_search"constant`

                The tool type. Always `web_search`.

                - `WEB_SEARCH("web_search")`

  - `JsonValue; type "session.update"constant`

    The Live client event type. Always `session.update`.

    - `SESSION_UPDATE("session.update")`

  - `Optional<String> eventId`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Session Updated Event

- `class SessionUpdatedEvent:`

  Returned when a Live session update is accepted. Contains the resolved session configuration after the update.

  - `String eventId`

    The unique ID of the Live server event.

  - `SessionResource session`

    The resolved Live session configuration and server-assigned session metadata.

    - `String id`

      The unique ID of the Live session. Use this ID for sideband connections, forking, and recording download.

    - `long expiresAt`

      The Unix timestamp, in seconds, at which the Live session expires.

    - `Model model`

      The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

      - `GPT_LIVE_1("gpt-live-1")`

    - `JsonValue; status "active"constant`

      The status of the session snapshot. Always `active`, including the final snapshot in session.closed; use the event type to determine that the session has closed.

      - `ACTIVE("active")`

    - `Optional<Audio> audio`

      Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

      - `Optional<AudioFormat> format`

        Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

        - `AudioPcm`

          - `Rate rate`

            Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

            - `_16000(16000)`

            - `_24000(24000)`

          - `JsonValue; type "audio/pcm"constant`

            The audio encoding. Always `audio/pcm`.

            - `AUDIO_PCM("audio/pcm")`

        - `AudioPcmu`

          - `long rate`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `JsonValue; type "audio/pcmu"constant`

            The audio encoding. Always `audio/pcmu`.

            - `AUDIO_PCMU("audio/pcmu")`

        - `AudioPcma`

          - `long rate`

            Audio sample rate in hertz. G.711 audio uses 8000 Hz.

          - `JsonValue; type "audio/pcma"constant`

            The audio encoding. Always `audio/pcma`.

            - `AUDIO_PCMA("audio/pcma")`

      - `Optional<Output> output`

        The voice used for speech generated by the Live model.

        - `Optional<Voice> voice`

          The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

          - `String`

          - `enum BuiltInVoice:`

            A built-in voice available for Live speech.

            - `ALLOY("alloy")`

            - `ASH("ash")`

            - `BALLAD("ballad")`

            - `BEACON("beacon")`

            - `BOSSA("bossa")`

            - `CEDAR("cedar")`

            - `CINDER("cinder")`

            - `CORAL("coral")`

            - `DELTA("delta")`

            - `ECHO("echo")`

            - `GLEAM("gleam")`

            - `MARIN("marin")`

            - `MERIDIAN("meridian")`

            - `QUARTZ("quartz")`

            - `RIPPLE("ripple")`

            - `SAGE("sage")`

            - `SHIMMER("shimmer")`

            - `STONE("stone")`

            - `TEMPO("tempo")`

            - `VERSE("verse")`

            - `VESPER("vesper")`

            - `WILLOW("willow")`

          - `class CustomVoice:`

            - `String id`

    - `Optional<ClientConfig> client`

      Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

      - `DataChannelConfig dataChannel`

        Client and server event permissions for the WebRTC frontend data channel.

        - `Optional<AllowedClientEvents> allowedClientEvents`

          Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

          - `JsonValue;`

            - `ALL("all")`

          - `List<String>`

        - `Optional<AllowedServerEvents> allowedServerEvents`

          Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

          - `JsonValue;`

            - `ALL("all")`

          - `List<ServerEventSelector>`

            - `String type`

              The outer Live server event type. Use 'response.event' for Responses events.

            - `Optional<String> responseEvent`

              The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

    - `Optional<Delegation> delegation`

      Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

      - `class ClientDelegation:`

        Delegate tasks to your application. The Live session emits delegation events that your backend handles.

        - `JsonValue; type "client"constant`

          The delegation owner. Always `client` for tasks handled by your application.

          - `CLIENT("client")`

      - `class Responses:`

        Delegate tasks to a Responses model managed by the Live session.

        - `ResponsesDelegationConfig responses`

          Backend model, prompt, and tools used when the Live session delegates a task to Responses.

          - `String model`

            The model used for server-owned Responses delegations.

          - `Optional<String> instructions`

            Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

          - `Optional<Long> maxOutputTokens`

            Maximum number of output tokens for each delegated response.

          - `Optional<Boolean> parallelToolCalls`

            Whether the delegated Responses model may request multiple tool calls in a single response.

          - `Optional<Reasoning> reasoning`

            Reasoning settings passed to each delegated Responses request.

            - `Optional<Effort> effort`

              How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

              - `NONE("none")`

              - `MINIMAL("minimal")`

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

              - `XHIGH("xhigh")`

            - `Optional<Summary> summary`

              The reasoning summary to request from the delegated Responses model, when supported.

              - `CONCISE("concise")`

              - `DETAILED("detailed")`

              - `AUTO("auto")`

          - `Optional<ServiceTier> serviceTier`

            Service tier for delegated Responses requests.

            - `AUTO("auto")`

            - `DEFAULT("default")`

            - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

            - `FLEX("flex")`

            - `PRIORITY("priority")`

            - `ULTRAFAST("ultrafast")`

          - `Optional<Text> text`

            Text generation settings passed to each delegated Responses request.

            - `Optional<Verbosity> verbosity`

              The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

          - `Optional<ToolChoice> toolChoice`

            Controls which tool the Responses backend uses when handling a task delegated by the Live model.

            - `enum LiveToolChoiceEnum:`

              - `AUTO("auto")`

              - `NONE("none")`

              - `REQUIRED("required")`

            - `class LiveFunctionToolChoiceParam:`

              - `String name`

              - `JsonValue; type "function"constant`

                - `FUNCTION("function")`

            - `class LiveMcpToolChoiceParam:`

              - `String name`

              - `String serverLabel`

              - `JsonValue; type "mcp"constant`

                - `MCP("mcp")`

          - `Optional<List<Tool>> tools`

            Tools available to the Responses backend while it handles tasks delegated by the Live model.

            - `class FunctionTool:`

              A function tool available to the Responses backend when the Live model delegates a task.

              - `String name`

                The name the delegated Responses model uses when calling this function.

              - `JsonValue; type "function"constant`

                The tool type. Always `function`.

                - `FUNCTION("function")`

              - `Optional<String> description`

                What the function does and when the delegated Responses model should call it.

              - `Optional<Parameters> parameters`

                A JSON Schema object describing the arguments accepted by the function.

              - `Optional<Boolean> strict`

                Whether the delegated Responses model must follow the function’s parameter schema exactly.

            - `JsonValue;`

              - `JsonValue; type "web_search"constant`

                The tool type. Always `web_search`.

                - `WEB_SEARCH("web_search")`

        - `JsonValue; type "responses"constant`

          The delegation owner. Always `responses` for tasks handled by the Responses API.

          - `RESPONSES("responses")`

    - `Optional<List<InitialItem>> input`

      Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

      - `Developer`

        - `List<Content> content`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `String text`

            The message text to include in the Live session’s initial conversation history.

          - `Optional<Type> type`

            The text content type. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `JsonValue; role "developer"constant`

          The author of this history message. Always `developer`.

          - `DEVELOPER("developer")`

        - `Optional<String> id`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Optional<Status> status`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `INCOMPLETE("incomplete")`

          - `COMPLETED("completed")`

        - `Optional<Type> type`

          The history item type. Always `message`.

          - `MESSAGE("message")`

      - `User`

        - `List<Content> content`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `String text`

            The message text to include in the Live session’s initial conversation history.

          - `Optional<Type> type`

            The text content type. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `JsonValue; role "user"constant`

          The author of this history message. Always `user`.

          - `USER("user")`

        - `Optional<String> id`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Optional<Status> status`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `INCOMPLETE("incomplete")`

          - `COMPLETED("completed")`

        - `Optional<Type> type`

          The history item type. Always `message`.

          - `MESSAGE("message")`

      - `Assistant`

        - `List<Content> content`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `class Text:`

            Assistant text supplied as conversation history when starting a Live session.

            - `String text`

              The message text to include in the Live session’s initial conversation history.

            - `Optional<Type> type`

              The text content type. Always `text`.

              - `TEXT("text")`

          - `class OutputText:`

            Assistant output text supplied as conversation history when starting a Live session.

            - `String text`

              The message text to include in the Live session’s initial conversation history.

            - `JsonValue; type "output_text"constant`

              The text content type. Always `output_text`.

              - `OUTPUT_TEXT("output_text")`

        - `JsonValue; role "assistant"constant`

          The author of this history message. Always `assistant`.

          - `ASSISTANT("assistant")`

        - `Optional<String> id`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Optional<Status> status`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `INCOMPLETE("incomplete")`

          - `COMPLETED("completed")`

        - `Optional<Type> type`

          The history item type. Always `message`.

          - `MESSAGE("message")`

    - `Optional<String> instructions`

      Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

    - `Optional<Boolean> store`

      Whether to store the session for later forking and recording download. Defaults to false for new sessions.

  - `JsonValue; type "session.updated"constant`

    The event type, always `session.updated`.

    - `SESSION_UPDATED("session.updated")`

  - `Optional<String> clientEventId`

    The event_id of the client command associated with this server event, when supplied.

### Session Usage

- `class SessionUsage:`

  Cumulative audio duration for a Live session. Values are totals for the session, not increments to sum across usage events.

  - `double seconds`

    The cumulative Live audio duration in seconds. Do not sum this value across usage events.

### Session Usage Updated Event

- `class SessionUsageUpdatedEvent:`

  Reports cumulative Live audio usage and, when available, the most recent context-window usage. Delegated Responses token usage is reported separately in response.event events.

  - `String eventId`

    The unique ID of the Live server event.

  - `JsonValue; type "session.usage.updated"constant`

    The event type, always `session.usage.updated`.

    - `SESSION_USAGE_UPDATED("session.usage.updated")`

  - `SessionUsage usage`

    The cumulative Live audio usage so far.

    - `double seconds`

      The cumulative Live audio duration in seconds. Do not sum this value across usage events.

  - `Optional<String> clientEventId`

    The event_id of the client command associated with this server event, when supplied.

  - `Optional<ContextWindow> contextWindow`

    The latest measured Live context-window usage. Omitted when the context limit is unknown.

    - `double usageRatio`

      The latest active context token count divided by the Live model context limit. Can decrease after compaction and may lag between measured audio frames.

### Thinking Append Event

- `class ThinkingAppendEvent:`

  Provide silent reasoning or progress context to the Live model, optionally for an existing client delegation.

  - `String content`

    Silent reasoning or progress context, limited to 500 tokens. It does not directly request speech, but can influence later speech and is not a secrecy boundary.

  - `Optional<String> delegationId`

    Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

  - `JsonValue; type "session.thinking.append"constant`

    The Live client event type. Always `session.thinking.append`.

    - `SESSION_THINKING_APPEND("session.thinking.append")`

  - `Optional<String> eventId`

    Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Thinking Appended Event

- `class ThinkingAppendedEvent:`

  Returned when a session.thinking.append command is accepted into the Live session timeline. Acknowledges the added reasoning context without guaranteeing any spoken output.

  - `long endMs`

    The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

  - `String eventId`

    The unique ID of the Live server event.

  - `long startMs`

    The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

  - `JsonValue; type "session.thinking.appended"constant`

    The event type, always `session.thinking.appended`.

    - `SESSION_THINKING_APPENDED("session.thinking.appended")`

  - `Optional<String> clientEventId`

    The event_id of the client command associated with this server event, when supplied.

# Forks

## Domain Types

### Fork Client Event

- `class ForkClientEvent: A class that can be one of several variants.union`

  Client events for a Live fork WebSocket. First send session.start with an overrides object (which may be empty), then wait for session.started before sending other commands. The model and conversation are inherited from the stored session.

  - `class ForkSessionStartEvent:`

    Start a Live session after connecting to a stored session’s fork WebSocket. Send an empty `session` object to use the stored configuration.

    - `ForkSessionConfig session`

      Overrides for a stored session after connecting to the fork WebSocket. An empty object inherits the stored configuration; do not supply a new model. audio.format applies only to the new WebSocket connection. client overrides are only supported for WebRTC forks.

      - `Optional<Audio> audio`

        Audio format for a WebSocket fork. WebRTC forks negotiate their audio format and must omit this field.

        - `Optional<AudioFormat> format`

          Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

          - `AudioPcm`

            - `Rate rate`

              Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

              - `_16000(16000)`

              - `_24000(24000)`

            - `JsonValue; type "audio/pcm"constant`

              The audio encoding. Always `audio/pcm`.

              - `AUDIO_PCM("audio/pcm")`

          - `AudioPcmu`

            - `long rate`

              Audio sample rate in hertz. G.711 audio uses 8000 Hz.

            - `JsonValue; type "audio/pcmu"constant`

              The audio encoding. Always `audio/pcmu`.

              - `AUDIO_PCMU("audio/pcmu")`

          - `AudioPcma`

            - `long rate`

              Audio sample rate in hertz. G.711 audio uses 8000 Hz.

            - `JsonValue; type "audio/pcma"constant`

              The audio encoding. Always `audio/pcma`.

              - `AUDIO_PCMA("audio/pcma")`

      - `Optional<ClientConfig> client`

        Frontend data-channel permissions for a WebRTC fork. Omitted permissions inherit the stored values. Not supported for WebSocket forks.

        - `DataChannelConfig dataChannel`

          Client and server event permissions for the WebRTC frontend data channel.

          - `Optional<AllowedClientEvents> allowedClientEvents`

            Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

            - `JsonValue;`

              - `ALL("all")`

            - `List<String>`

          - `Optional<AllowedServerEvents> allowedServerEvents`

            Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

            - `JsonValue;`

              - `ALL("all")`

            - `List<ServerEventSelector>`

              - `String type`

                The outer Live server event type. Use 'response.event' for Responses events.

              - `Optional<String> responseEvent`

                The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

      - `Optional<Delegation> delegation`

        Overrides for the stored session’s Responses backend. Only supported when the stored session already uses Responses delegation; the delegation type cannot change.

        - `JsonValue; type "responses"constant`

          The delegation owner. Always `responses` for tasks handled by the Responses API.

          - `RESPONSES("responses")`

        - `Optional<ResponsesDelegationUpdateConfig> responses`

          Responses backend settings to update. Omitted settings keep their existing values.

          - `Optional<String> instructions`

            Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

          - `Optional<Long> maxOutputTokens`

            Maximum number of output tokens for each delegated response.

          - `Optional<String> model`

            The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.

          - `Optional<Boolean> parallelToolCalls`

            Whether the delegated Responses model may request multiple tool calls in a single response.

          - `Optional<Reasoning> reasoning`

            Reasoning settings passed to each delegated Responses request.

            - `Optional<Effort> effort`

              How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

              - `NONE("none")`

              - `MINIMAL("minimal")`

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

              - `XHIGH("xhigh")`

            - `Optional<Summary> summary`

              The reasoning summary to request from the delegated Responses model, when supported.

              - `CONCISE("concise")`

              - `DETAILED("detailed")`

              - `AUTO("auto")`

          - `Optional<ServiceTier> serviceTier`

            Service tier for delegated Responses requests.

            - `AUTO("auto")`

            - `DEFAULT("default")`

            - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

            - `FLEX("flex")`

            - `PRIORITY("priority")`

            - `ULTRAFAST("ultrafast")`

          - `Optional<Text> text`

            Text generation settings passed to each delegated Responses request.

            - `Optional<Verbosity> verbosity`

              The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

          - `Optional<ToolChoice> toolChoice`

            Controls which tool the Responses backend uses when handling a task delegated by the Live model.

            - `enum LiveToolChoiceEnum:`

              - `AUTO("auto")`

              - `NONE("none")`

              - `REQUIRED("required")`

            - `class LiveFunctionToolChoiceParam:`

              - `String name`

              - `JsonValue; type "function"constant`

                - `FUNCTION("function")`

            - `class LiveMcpToolChoiceParam:`

              - `String name`

              - `String serverLabel`

              - `JsonValue; type "mcp"constant`

                - `MCP("mcp")`

          - `Optional<List<Tool>> tools`

            Tools available to the Responses backend while it handles tasks delegated by the Live model.

            - `class FunctionTool:`

              A function tool available to the Responses backend when the Live model delegates a task.

              - `String name`

                The name the delegated Responses model uses when calling this function.

              - `JsonValue; type "function"constant`

                The tool type. Always `function`.

                - `FUNCTION("function")`

              - `Optional<String> description`

                What the function does and when the delegated Responses model should call it.

              - `Optional<Parameters> parameters`

                A JSON Schema object describing the arguments accepted by the function.

              - `Optional<Boolean> strict`

                Whether the delegated Responses model must follow the function’s parameter schema exactly.

            - `JsonValue;`

              - `JsonValue; type "web_search"constant`

                The tool type. Always `web_search`.

                - `WEB_SEARCH("web_search")`

      - `Optional<Boolean> store`

        Whether to store the forked session. Omission inherits the stored session's setting.

    - `JsonValue; type "session.start"constant`

      The Live client event type. Always `session.start`.

      - `SESSION_START("session.start")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class SessionUpdateEvent:`

    Update the delegation settings of an active Live session. The server acknowledges accepted changes with `session.updated`.

    - `SessionUpdateConfig session`

      Sparse delegation updates. Omitted settings retain their values. The delegation type cannot change, including resetting Responses delegation to null or client. Model, frontend instructions, audio, and startup input are immutable.

      - `Optional<Delegation> delegation`

        Delegation settings to update. The delegation type must match the current session; omitted settings retain their values.

        - `class ClientDelegation:`

          Delegate tasks to your application. The Live session emits delegation events that your backend handles.

          - `JsonValue; type "client"constant`

            The delegation owner. Always `client` for tasks handled by your application.

            - `CLIENT("client")`

        - `class Responses:`

          Update the Responses backend for an existing Live session without changing delegation ownership.

          - `JsonValue; type "responses"constant`

            The delegation owner. Always `responses` for tasks handled by the Responses API.

            - `RESPONSES("responses")`

          - `Optional<ResponsesDelegationUpdateConfig> responses`

            Responses backend settings to update. Omitted settings keep their existing values.

    - `JsonValue; type "session.update"constant`

      The Live client event type. Always `session.update`.

      - `SESSION_UPDATE("session.update")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class InputAudioAppendEvent:`

    Send audio to a Live session over its primary WebSocket. WebRTC and SIP sessions send audio over their media transport.

    - `String audio`

      Base64-encoded raw audio in the startup-selected format, without a WAV or other container header. Primary WebSocket only; media transports use their audio track. Audio appends have no acknowledgment. Reflected sideband server events reuse this event type and audio key, with no timestamps or event_id; their audio is always mono PCM16LE at 24 kHz.

    - `JsonValue; type "session.input_audio.append"constant`

      The Live client event type. Always `session.input_audio.append`.

      - `SESSION_INPUT_AUDIO_APPEND("session.input_audio.append")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class InputAudioMuteEvent:`

    Mute audio input to the Live model without closing the session. The server acknowledges with `session.input_audio.muted`.

    - `JsonValue; type "session.input_audio.mute"constant`

      The Live client event type. Always `session.input_audio.mute`.

      - `SESSION_INPUT_AUDIO_MUTE("session.input_audio.mute")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class InputAudioUnmuteEvent:`

    Resume audio input to a Live model after muting it. The server acknowledges with `session.input_audio.unmuted`.

    - `JsonValue; type "session.input_audio.unmute"constant`

      The Live client event type. Always `session.input_audio.unmute`.

      - `SESSION_INPUT_AUDIO_UNMUTE("session.input_audio.unmute")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class InstructionsAppendEvent:`

    Append instructions to the Live conversation while it is running, optionally associating them with an existing client delegation.

    - `String content`

      Instruction text to append, limited to 500 tokens. This is a plain string, not an array of content parts.

    - `Optional<String> delegationId`

      Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

    - `JsonValue; type "session.instructions.append"constant`

      The Live client event type. Always `session.instructions.append`.

      - `SESSION_INSTRUCTIONS_APPEND("session.instructions.append")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class ThinkingAppendEvent:`

    Provide silent reasoning or progress context to the Live model, optionally for an existing client delegation.

    - `String content`

      Silent reasoning or progress context, limited to 500 tokens. It does not directly request speech, but can influence later speech and is not a secrecy boundary.

    - `Optional<String> delegationId`

      Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

    - `JsonValue; type "session.thinking.append"constant`

      The Live client event type. Always `session.thinking.append`.

      - `SESSION_THINKING_APPEND("session.thinking.append")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class CommentaryAppendEvent:`

    Provide context the Live model can communicate to the user, optionally for an existing client delegation.

    - `String content`

      Speakable context for the Live model, limited to 500 tokens. Use this for a result the model should communicate; use session.thinking.append for silent context.

    - `Optional<String> delegationId`

      Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

    - `JsonValue; type "session.commentary.append"constant`

      The Live client event type. Always `session.commentary.append`.

      - `SESSION_COMMENTARY_APPEND("session.commentary.append")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class ResponseItemCreateEvent:`

    Add an input item to the Live session’s Responses backend. Requires Responses delegation; use `response.create` to request a response.

    - `ResponseInputItem item`

      An input item to append to the Responses backend conversation, such as a user message or a function tool result.

      - `class EasyInputMessage:`

        A message input to the model with a role indicating instruction following
        hierarchy. Instructions given with the `developer` or `system` role take
        precedence over instructions given with the `user` role. Messages with the
        `assistant` role are presumed to have been generated by the model in previous
        interactions.

        - `Content content`

          Text, image, or audio input to the model, used to generate a response.
          Can also contain previous assistant responses.

          - `String`

          - `List<ResponseInputContent>`

            - `class ResponseInputText:`

              A text input to the model.

              - `String text`

                The text input to the model.

              - `JsonValue; type "input_text"constant`

                The type of the input item. Always `input_text`.

                - `INPUT_TEXT("input_text")`

              - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `JsonValue; mode "explicit"constant`

                  The breakpoint mode. Always `explicit`.

                  - `EXPLICIT("explicit")`

            - `class ResponseInputImage:`

              An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

              - `Detail detail`

                The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                - `LOW("low")`

                - `HIGH("high")`

                - `AUTO("auto")`

                - `ORIGINAL("original")`

              - `JsonValue; type "input_image"constant`

                The type of the input item. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

              - `Optional<String> fileId`

                The ID of the file to be sent to the model.

              - `Optional<String> imageUrl`

                The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

              - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `JsonValue; mode "explicit"constant`

                  The breakpoint mode. Always `explicit`.

                  - `EXPLICIT("explicit")`

            - `class ResponseInputFile:`

              A file input to the model.

              - `JsonValue; type "input_file"constant`

                The type of the input item. Always `input_file`.

                - `INPUT_FILE("input_file")`

              - `Optional<Detail> detail`

                The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

                - `AUTO("auto")`

                - `LOW("low")`

                - `HIGH("high")`

              - `Optional<String> fileData`

                The content of the file to be sent to the model.

              - `Optional<String> fileId`

                The ID of the file to be sent to the model.

              - `Optional<String> fileUrl`

                The URL of the file to be sent to the model.

              - `Optional<String> filename`

                The name of the file to be sent to the model.

              - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `JsonValue; mode "explicit"constant`

                  The breakpoint mode. Always `explicit`.

                  - `EXPLICIT("explicit")`

        - `Role role`

          The role of the message input. One of `user`, `assistant`, `system`, or
          `developer`.

          - `USER("user")`

          - `ASSISTANT("assistant")`

          - `SYSTEM("system")`

          - `DEVELOPER("developer")`

        - `Optional<Phase> phase`

          Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
          For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
          phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

          - `COMMENTARY("commentary")`

          - `FINAL_ANSWER("final_answer")`

        - `Optional<Type> type`

          The type of the message input. Always `message`.

          - `MESSAGE("message")`

      - `Message`

        - `List<ResponseInputContent> content`

          A list of one or many input items to the model, containing different content
          types.

          - `class ResponseInputText:`

            A text input to the model.

          - `class ResponseInputImage:`

            An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

          - `class ResponseInputFile:`

            A file input to the model.

        - `Role role`

          The role of the message input. One of `user`, `system`, or `developer`.

          - `USER("user")`

          - `SYSTEM("system")`

          - `DEVELOPER("developer")`

        - `Optional<Status> status`

          The status of item. One of `in_progress`, `completed`, or
          `incomplete`. Populated when items are returned via API.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

        - `Optional<Type> type`

          The type of the message input. Always set to `message`.

          - `MESSAGE("message")`

      - `class ResponseOutputMessage:`

        An output message from the model.

        - `String id`

          The unique ID of the output message.

        - `List<Content> content`

          The content of the output message.

          - `class ResponseOutputText:`

            A text output from the model.

            - `List<Annotation> annotations`

              The annotations of the text output.

              - `class FileCitation:`

                A citation to a file.

                - `String fileId`

                  The ID of the file.

                - `String filename`

                  The filename of the file cited.

                - `long index`

                  The index in the output text at which to insert the file citation.

                - `JsonValue; type "file_citation"constant`

                  The type of the file citation. Always `file_citation`.

                  - `FILE_CITATION("file_citation")`

              - `class UrlCitation:`

                A citation for a web resource used to generate a model response.

                - `long endIndex`

                  The index of the last character of the URL citation in the message.

                - `long startIndex`

                  The index of the first character of the URL citation in the message.

                - `String title`

                  The title of the web resource.

                - `JsonValue; type "url_citation"constant`

                  The type of the URL citation. Always `url_citation`.

                  - `URL_CITATION("url_citation")`

                - `String url`

                  The URL of the web resource.

              - `class ContainerFileCitation:`

                A citation for a container file used to generate a model response.

                - `String containerId`

                  The ID of the container file.

                - `long endIndex`

                  The index of the last character of the container file citation in the message.

                - `String fileId`

                  The ID of the file.

                - `String filename`

                  The filename of the container file cited.

                - `long startIndex`

                  The index of the first character of the container file citation in the message.

                - `JsonValue; type "container_file_citation"constant`

                  The type of the container file citation. Always `container_file_citation`.

                  - `CONTAINER_FILE_CITATION("container_file_citation")`

              - `class FilePath:`

                A path to a file.

                - `String fileId`

                  The ID of the file.

                - `long index`

                  The index of the file in the list of files.

                - `JsonValue; type "file_path"constant`

                  The type of the file path. Always `file_path`.

                  - `FILE_PATH("file_path")`

            - `String text`

              The text output from the model.

            - `JsonValue; type "output_text"constant`

              The type of the output text. Always `output_text`.

              - `OUTPUT_TEXT("output_text")`

            - `Optional<List<Logprob>> logprobs`

              - `String token`

              - `List<long> bytes`

              - `double logprob`

              - `List<TopLogprob> topLogprobs`

                - `String token`

                - `List<long> bytes`

                - `double logprob`

          - `class ResponseOutputRefusal:`

            A refusal from the model.

            - `String refusal`

              The refusal explanation from the model.

            - `JsonValue; type "refusal"constant`

              The type of the refusal. Always `refusal`.

              - `REFUSAL("refusal")`

        - `JsonValue; role "assistant"constant`

          The role of the output message. Always `assistant`.

          - `ASSISTANT("assistant")`

        - `Status status`

          The status of the message input. One of `in_progress`, `completed`, or
          `incomplete`. Populated when input items are returned via API.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

        - `JsonValue; type "message"constant`

          The type of the output message. Always `message`.

          - `MESSAGE("message")`

        - `Optional<Phase> phase`

          Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
          For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
          phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

          - `COMMENTARY("commentary")`

          - `FINAL_ANSWER("final_answer")`

      - `class ResponseFileSearchToolCall:`

        The results of a file search tool call. See the
        [file search guide](/api/docs/guides/tools-file-search) for more information.

        - `String id`

          The unique ID of the file search tool call.

        - `List<String> queries`

          The queries used to search for files.

        - `Status status`

          The status of the file search tool call. One of `in_progress`,
          `searching`, `incomplete` or `failed`,

          - `IN_PROGRESS("in_progress")`

          - `SEARCHING("searching")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

          - `FAILED("failed")`

        - `JsonValue; type "file_search_call"constant`

          The type of the file search tool call. Always `file_search_call`.

          - `FILE_SEARCH_CALL("file_search_call")`

        - `Optional<List<Result>> results`

          The results of the file search tool call.

          - `Optional<Attributes> attributes`

            Set of 16 key-value pairs that can be attached to an object. This can be
            useful for storing additional information about the object in a structured
            format, and querying for objects via API or the dashboard. Keys are strings
            with a maximum length of 64 characters. Values are strings with a maximum
            length of 512 characters, booleans, or numbers.

            - `String`

            - `double`

            - `boolean`

          - `Optional<String> fileId`

            The unique ID of the file.

          - `Optional<String> filename`

            The name of the file.

          - `Optional<Double> score`

            The relevance score of the file - a value between 0 and 1.

          - `Optional<String> text`

            The text that was retrieved from the file.

      - `class ResponseComputerToolCall:`

        A tool call to a computer use tool. See the
        [computer use guide](/api/docs/guides/tools-computer-use) for more information.

        - `String id`

          The unique ID of the computer call.

        - `String callId`

          An identifier used when responding to the tool call with output.

        - `List<PendingSafetyCheck> pendingSafetyChecks`

          The pending safety checks for the computer call.

          - `String id`

            The ID of the pending safety check.

          - `Optional<String> code`

            The type of the pending safety check.

          - `Optional<String> message`

            Details about the pending safety check.

        - `Status status`

          The status of the item. One of `in_progress`, `completed`, or
          `incomplete`. Populated when items are returned via API.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

        - `Type type`

          The type of the computer call. Always `computer_call`.

          - `COMPUTER_CALL("computer_call")`

        - `Optional<Action> action`

          A click action.

          - `class Click:`

            A click action.

            - `Button button`

              Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

              - `LEFT("left")`

              - `RIGHT("right")`

              - `WHEEL("wheel")`

              - `BACK("back")`

              - `FORWARD("forward")`

            - `JsonValue; type "click"constant`

              Specifies the event type. For a click action, this property is always `click`.

              - `CLICK("click")`

            - `long x`

              The x-coordinate where the click occurred.

            - `long y`

              The y-coordinate where the click occurred.

            - `Optional<List<String>> keys`

              The keys being held while clicking.

          - `class DoubleClick:`

            A double click action.

            - `Optional<List<String>> keys`

              The keys being held while double-clicking.

            - `JsonValue; type "double_click"constant`

              Specifies the event type. For a double click action, this property is always set to `double_click`.

              - `DOUBLE_CLICK("double_click")`

            - `long x`

              The x-coordinate where the double click occurred.

            - `long y`

              The y-coordinate where the double click occurred.

          - `class Drag:`

            A drag action.

            - `List<Path> path`

              An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

              ```
              [
                { x: 100, y: 200 },
                { x: 200, y: 300 }
              ]
              ```

              - `long x`

                The x-coordinate.

              - `long y`

                The y-coordinate.

            - `JsonValue; type "drag"constant`

              Specifies the event type. For a drag action, this property is always set to `drag`.

              - `DRAG("drag")`

            - `Optional<List<String>> keys`

              The keys being held while dragging the mouse.

          - `class Keypress:`

            A collection of keypresses the model would like to perform.

            - `List<String> keys`

              The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

            - `JsonValue; type "keypress"constant`

              Specifies the event type. For a keypress action, this property is always set to `keypress`.

              - `KEYPRESS("keypress")`

          - `class Move:`

            A mouse move action.

            - `JsonValue; type "move"constant`

              Specifies the event type. For a move action, this property is always set to `move`.

              - `MOVE("move")`

            - `long x`

              The x-coordinate to move to.

            - `long y`

              The y-coordinate to move to.

            - `Optional<List<String>> keys`

              The keys being held while moving the mouse.

          - `JsonValue;`

            - `JsonValue; type "screenshot"constant`

              Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

              - `SCREENSHOT("screenshot")`

          - `class Scroll:`

            A scroll action.

            - `long scrollX`

              The horizontal scroll distance.

            - `long scrollY`

              The vertical scroll distance.

            - `JsonValue; type "scroll"constant`

              Specifies the event type. For a scroll action, this property is always set to `scroll`.

              - `SCROLL("scroll")`

            - `long x`

              The x-coordinate where the scroll occurred.

            - `long y`

              The y-coordinate where the scroll occurred.

            - `Optional<List<String>> keys`

              The keys being held while scrolling.

          - `class Type:`

            An action to type in text.

            - `String text`

              The text to type.

            - `JsonValue; type "type"constant`

              Specifies the event type. For a type action, this property is always set to `type`.

              - `TYPE("type")`

          - `JsonValue;`

            - `JsonValue; type "wait"constant`

              Specifies the event type. For a wait action, this property is always set to `wait`.

              - `WAIT("wait")`

        - `Optional<List<ComputerAction>> actions`

          Flattened batched actions for `computer_use`. Each action includes an
          `type` discriminator and action-specific fields.

          - `Click`

            - `Button button`

              Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

              - `LEFT("left")`

              - `RIGHT("right")`

              - `WHEEL("wheel")`

              - `BACK("back")`

              - `FORWARD("forward")`

            - `JsonValue; type "click"constant`

              Specifies the event type. For a click action, this property is always `click`.

              - `CLICK("click")`

            - `long x`

              The x-coordinate where the click occurred.

            - `long y`

              The y-coordinate where the click occurred.

            - `Optional<List<String>> keys`

              The keys being held while clicking.

          - `DoubleClick`

            - `Optional<List<String>> keys`

              The keys being held while double-clicking.

            - `JsonValue; type "double_click"constant`

              Specifies the event type. For a double click action, this property is always set to `double_click`.

              - `DOUBLE_CLICK("double_click")`

            - `long x`

              The x-coordinate where the double click occurred.

            - `long y`

              The y-coordinate where the double click occurred.

          - `Drag`

            - `List<Path> path`

              An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

              ```
              [
                { x: 100, y: 200 },
                { x: 200, y: 300 }
              ]
              ```

              - `long x`

                The x-coordinate.

              - `long y`

                The y-coordinate.

            - `JsonValue; type "drag"constant`

              Specifies the event type. For a drag action, this property is always set to `drag`.

              - `DRAG("drag")`

            - `Optional<List<String>> keys`

              The keys being held while dragging the mouse.

          - `Keypress`

            - `List<String> keys`

              The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

            - `JsonValue; type "keypress"constant`

              Specifies the event type. For a keypress action, this property is always set to `keypress`.

              - `KEYPRESS("keypress")`

          - `Move`

            - `JsonValue; type "move"constant`

              Specifies the event type. For a move action, this property is always set to `move`.

              - `MOVE("move")`

            - `long x`

              The x-coordinate to move to.

            - `long y`

              The y-coordinate to move to.

            - `Optional<List<String>> keys`

              The keys being held while moving the mouse.

          - `JsonValue;`

            - `JsonValue; type "screenshot"constant`

              Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

              - `SCREENSHOT("screenshot")`

          - `Scroll`

            - `long scrollX`

              The horizontal scroll distance.

            - `long scrollY`

              The vertical scroll distance.

            - `JsonValue; type "scroll"constant`

              Specifies the event type. For a scroll action, this property is always set to `scroll`.

              - `SCROLL("scroll")`

            - `long x`

              The x-coordinate where the scroll occurred.

            - `long y`

              The y-coordinate where the scroll occurred.

            - `Optional<List<String>> keys`

              The keys being held while scrolling.

          - `Type`

            - `String text`

              The text to type.

            - `JsonValue; type "type"constant`

              Specifies the event type. For a type action, this property is always set to `type`.

              - `TYPE("type")`

          - `JsonValue;`

            - `JsonValue; type "wait"constant`

              Specifies the event type. For a wait action, this property is always set to `wait`.

              - `WAIT("wait")`

      - `ComputerCallOutput`

        - `String callId`

          The ID of the computer tool call that produced the output.

        - `ResponseComputerToolCallOutputScreenshot output`

          A computer screenshot image used with the computer use tool.

          - `JsonValue; type "computer_screenshot"constant`

            Specifies the event type. For a computer screenshot, this property is
            always set to `computer_screenshot`.

            - `COMPUTER_SCREENSHOT("computer_screenshot")`

          - `Optional<String> fileId`

            The identifier of an uploaded file that contains the screenshot.

          - `Optional<String> imageUrl`

            The URL of the screenshot image.

        - `JsonValue; type "computer_call_output"constant`

          The type of the computer tool call output. Always `computer_call_output`.

          - `COMPUTER_CALL_OUTPUT("computer_call_output")`

        - `Optional<String> id`

          The ID of the computer tool call output.

        - `Optional<List<AcknowledgedSafetyCheck>> acknowledgedSafetyChecks`

          The safety checks reported by the API that have been acknowledged by the developer.

          - `String id`

            The ID of the pending safety check.

          - `Optional<String> code`

            The type of the pending safety check.

          - `Optional<String> message`

            Details about the pending safety check.

        - `Optional<Status> status`

          The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `class ResponseFunctionWebSearch:`

        The results of a web search tool call. See the
        [web search guide](/api/docs/guides/tools-web-search) for more information.

        - `String id`

          The unique ID of the web search tool call.

        - `Action action`

          An object describing the specific action taken in this web search call.
          Includes details on how the model used the web (search, open_page, find_in_page).

          - `class Search:`

            Action type "search" - Performs a web search query.

            - `JsonValue; type "search"constant`

              The action type.

              - `SEARCH("search")`

            - `Optional<List<String>> queries`

              The search queries.

            - `Optional<String> query`

              The search query.

            - `Optional<List<Source>> sources`

              The sources used in the search.

              - `JsonValue; type "url"constant`

                The type of source. Always `url`.

                - `URL("url")`

              - `String url`

                The URL of the source.

          - `class OpenPage:`

            Action type "open_page" - Opens a specific URL from search results.

            - `JsonValue; type "open_page"constant`

              The action type.

              - `OPEN_PAGE("open_page")`

            - `Optional<String> url`

              The URL opened by the model.

          - `class FindInPage:`

            Action type "find_in_page": Searches for a pattern within a loaded page.

            - `String pattern`

              The pattern or text to search for within the page.

            - `JsonValue; type "find_in_page"constant`

              The action type.

              - `FIND_IN_PAGE("find_in_page")`

            - `String url`

              The URL of the page searched for the pattern.

        - `Status status`

          The status of the web search tool call.

          - `IN_PROGRESS("in_progress")`

          - `SEARCHING("searching")`

          - `COMPLETED("completed")`

          - `FAILED("failed")`

          - `INCOMPLETE("incomplete")`

        - `JsonValue; type "web_search_call"constant`

          The type of the web search tool call. Always `web_search_call`.

          - `WEB_SEARCH_CALL("web_search_call")`

      - `class ResponseFunctionToolCall:`

        A tool call to run a function. See the
        [function calling guide](/api/docs/guides/function-calling) for more information.

        - `String arguments`

          A JSON string of the arguments to pass to the function.

        - `String callId`

          The unique ID of the function tool call generated by the model.

        - `String name`

          The name of the function to run.

        - `JsonValue; type "function_call"constant`

          The type of the function tool call. Always `function_call`.

          - `FUNCTION_CALL("function_call")`

        - `Optional<String> id`

          The unique ID of the function tool call.

        - `Optional<Boolean> async`

          Whether the function tool call runs asynchronously.

        - `Optional<Caller> caller`

          The execution context that produced this tool call.

          - `JsonValue;`

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class Program:`

            - `String callerId`

              The call ID of the program item that produced this tool call.

            - `JsonValue; type "program"constant`

              - `PROGRAM("program")`

        - `Optional<String> namespace`

          The namespace of the function to run.

        - `Optional<Status> status`

          The status of the item. One of `in_progress`, `completed`, or
          `incomplete`. Populated when items are returned via API.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `FunctionCallOutput`

        - `Output output`

          Text, image, or file output of the function tool call.

          - `String`

          - `List<ResponseFunctionCallOutputItem>`

            - `class ResponseInputTextContent:`

              A text input to the model.

              - `String text`

                The text input to the model.

              - `JsonValue; type "input_text"constant`

                The type of the input item. Always `input_text`.

                - `INPUT_TEXT("input_text")`

              - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `JsonValue; mode "explicit"constant`

                  The breakpoint mode. Always `explicit`.

                  - `EXPLICIT("explicit")`

            - `class ResponseInputImageContent:`

              An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision)

              - `JsonValue; type "input_image"constant`

                The type of the input item. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

              - `Optional<Detail> detail`

                The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                - `LOW("low")`

                - `HIGH("high")`

                - `AUTO("auto")`

                - `ORIGINAL("original")`

              - `Optional<String> fileId`

                The ID of the file to be sent to the model.

              - `Optional<String> imageUrl`

                The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

              - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `JsonValue; mode "explicit"constant`

                  The breakpoint mode. Always `explicit`.

                  - `EXPLICIT("explicit")`

            - `class ResponseInputFileContent:`

              A file input to the model.

              - `JsonValue; type "input_file"constant`

                The type of the input item. Always `input_file`.

                - `INPUT_FILE("input_file")`

              - `Optional<Detail> detail`

                The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

                - `AUTO("auto")`

                - `LOW("low")`

                - `HIGH("high")`

              - `Optional<String> fileData`

                The base64-encoded data of the file to be sent to the model.

              - `Optional<String> fileId`

                The ID of the file to be sent to the model.

              - `Optional<String> fileUrl`

                The URL of the file to be sent to the model.

              - `Optional<String> filename`

                The name of the file to be sent to the model.

              - `Optional<PromptCacheBreakpoint> promptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `JsonValue; mode "explicit"constant`

                  The breakpoint mode. Always `explicit`.

                  - `EXPLICIT("explicit")`

        - `JsonValue; type "function_call_output"constant`

          The type of the function tool call output. Always `function_call_output`.

          - `FUNCTION_CALL_OUTPUT("function_call_output")`

        - `Optional<String> id`

          The unique ID of the function tool call output. Populated when this item is returned via API.

        - `Optional<String> callId`

          The unique ID of the function tool call generated by the model.

        - `Optional<Caller> caller`

          The execution context that produced this tool call.

          - `JsonValue;`

            - `JsonValue; type "direct"constant`

              The caller type. Always `direct`.

              - `DIRECT("direct")`

          - `class Program:`

            - `String callerId`

              The call ID of the program item that produced this tool call.

            - `JsonValue; type "program"constant`

              The caller type. Always `program`.

              - `PROGRAM("program")`

        - `Optional<String> name`

          The name of the tool that produced the output.

        - `Optional<String> namespace`

          The namespace of the tool that produced the output.

        - `Optional<Status> status`

          The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `ToolSearchCall`

        - `JsonValue arguments`

          The arguments supplied to the tool search call.

        - `JsonValue; type "tool_search_call"constant`

          The item type. Always `tool_search_call`.

          - `TOOL_SEARCH_CALL("tool_search_call")`

        - `Optional<String> id`

          The unique ID of this tool search call.

        - `Optional<String> callId`

          The unique ID of the tool search call generated by the model.

        - `Optional<Execution> execution`

          Whether tool search was executed by the server or by the client.

          - `SERVER("server")`

          - `CLIENT("client")`

        - `Optional<Status> status`

          The status of the tool search call.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `class ResponseToolSearchOutputItemParam:`

        - `List<Tool> tools`

          The loaded tool definitions returned by the tool search output.

          - `class FunctionTool:`

            Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

            - `String name`

              The name of the function to call.

            - `Optional<Parameters> parameters`

              A JSON schema object describing the parameters of the function.

            - `Optional<Boolean> strict`

              Whether strict parameter validation is enforced for this function tool.

            - `JsonValue; type "function"constant`

              The type of the function tool. Always `function`.

              - `FUNCTION("function")`

            - `Optional<List<AllowedCaller>> allowedCallers`

              The tool invocation context(s).

              - `DIRECT("direct")`

              - `PROGRAMMATIC("programmatic")`

            - `Optional<Boolean> async`

            - `Optional<Boolean> deferLoading`

              Whether this function is deferred and loaded via tool search.

            - `Optional<String> description`

              A description of the function. Used by the model to determine whether or not to call the function.

            - `Optional<OutputSchema> outputSchema`

              A JSON schema object describing the JSON value encoded in string outputs for this function.

          - `class FileSearchTool:`

            A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

            - `JsonValue; type "file_search"constant`

              The type of the file search tool. Always `file_search`.

              - `FILE_SEARCH("file_search")`

            - `List<String> vectorStoreIds`

              The IDs of the vector stores to search.

            - `Optional<Filters> filters`

              A filter to apply.

              - `class ComparisonFilter:`

                A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                - `String key`

                  The key to compare against the value.

                - `Type type`

                  Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                  - `eq`: equals
                  - `ne`: not equal
                  - `gt`: greater than
                  - `gte`: greater than or equal
                  - `lt`: less than
                  - `lte`: less than or equal
                  - `in`: in
                  - `nin`: not in

                  - `EQ("eq")`

                  - `NE("ne")`

                  - `GT("gt")`

                  - `GTE("gte")`

                  - `LT("lt")`

                  - `LTE("lte")`

                  - `IN("in")`

                  - `NIN("nin")`

                - `Value value`

                  The value to compare against the attribute key; supports string, number, or boolean types.

                  - `String`

                  - `double`

                  - `boolean`

                  - `List<ComparisonFilterValueItem>`

                    - `String`

                    - `double`

              - `class CompoundFilter:`

                Combine multiple filters using `and` or `or`.

                - `List<Filter> filters`

                  Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

                  - `class ComparisonFilter:`

                    A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                  - `JsonValue`

                - `Type type`

                  Type of operation: `and` or `or`.

                  - `AND("and")`

                  - `OR("or")`

            - `Optional<Long> maxNumResults`

              The maximum number of results to return. This number should be between 1 and 50 inclusive.

            - `Optional<RankingOptions> rankingOptions`

              Ranking options for search.

              - `Optional<HybridSearch> hybridSearch`

                Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

                - `double embeddingWeight`

                  The weight of the embedding in the reciprocal ranking fusion.

                - `double textWeight`

                  The weight of the text in the reciprocal ranking fusion.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search.

                - `AUTO("auto")`

                - `DEFAULT_2024_11_15("default-2024-11-15")`

              - `Optional<Double> scoreThreshold`

                The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

          - `class ComputerTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

            - `JsonValue; type "computer"constant`

              The type of the computer tool. Always `computer`.

              - `COMPUTER("computer")`

          - `class ComputerUsePreviewTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

            - `long displayHeight`

              The height of the computer display.

            - `long displayWidth`

              The width of the computer display.

            - `Environment environment`

              The type of computer environment to control.

              - `WINDOWS("windows")`

              - `MAC("mac")`

              - `LINUX("linux")`

              - `UBUNTU("ubuntu")`

              - `BROWSER("browser")`

            - `JsonValue; type "computer_use_preview"constant`

              The type of the computer use tool. Always `computer_use_preview`.

              - `COMPUTER_USE_PREVIEW("computer_use_preview")`

          - `class WebSearchTool:`

            Search the Internet for sources related to the prompt. Learn more about the
            [web search tool](/api/docs/guides/tools-web-search).

            - `Type type`

              The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

              - `WEB_SEARCH("web_search")`

              - `WEB_SEARCH_2025_08_26("web_search_2025_08_26")`

            - `Optional<Boolean> externalWebAccess`

              Allow live internet access for web search. Defaults to true when omitted. When false, the web search tool runs in offline/cache-only mode and will not fetch new external content.

            - `Optional<Filters> filters`

              Filters for the search.

              - `Optional<List<String>> allowedDomains`

                Allowed domains for the search. If not provided, all domains are allowed.
                Subdomains of the provided domains are allowed as well.

                Example: `["pubmed.ncbi.nlm.nih.gov"]`

            - `Optional<SearchContextSize> searchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<UserLocation> userLocation`

              The approximate location of the user. If omitted or null, defaults to the
              United States. To avoid this fallback, pass `{"type": "approximate"}` without
              location fields. To localize results, provide the relevant location fields.

              - `Optional<String> city`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Optional<String> country`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Optional<String> region`

                Free text input for the region of the user, e.g. `California`.

              - `Optional<String> timezone`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

              - `Optional<Type> type`

                The type of location approximation. Always `approximate`.

                - `APPROXIMATE("approximate")`

          - `Mcp`

            - `String serverLabel`

              A label for this MCP server, used to identify it in tool calls.

            - `JsonValue; type "mcp"constant`

              The type of the MCP tool. Always `mcp`.

              - `MCP("mcp")`

            - `Optional<List<AllowedCaller>> allowedCallers`

              The tool invocation context(s).

              - `DIRECT("direct")`

              - `PROGRAMMATIC("programmatic")`

            - `Optional<AllowedTools> allowedTools`

              List of allowed tool names or a filter object.

              - `List<String>`

              - `class McpToolFilter:`

                A filter object to specify which tools are allowed.

                - `Optional<Boolean> readOnly`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `Optional<List<String>> toolNames`

                  List of allowed tool names.

            - `Optional<String> authorization`

              An OAuth access token that can be used with a remote MCP server, either
              with a custom MCP server URL or a service connector. Your application
              must handle the OAuth authorization flow and provide the token here.

            - `Optional<ConnectorId> connectorId`

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

              - `CONNECTOR_DROPBOX("connector_dropbox")`

              - `CONNECTOR_GMAIL("connector_gmail")`

              - `CONNECTOR_GOOGLECALENDAR("connector_googlecalendar")`

              - `CONNECTOR_GOOGLEDRIVE("connector_googledrive")`

              - `CONNECTOR_MICROSOFTTEAMS("connector_microsoftteams")`

              - `CONNECTOR_OUTLOOKCALENDAR("connector_outlookcalendar")`

              - `CONNECTOR_OUTLOOKEMAIL("connector_outlookemail")`

              - `CONNECTOR_SHAREPOINT("connector_sharepoint")`

            - `Optional<Boolean> deferLoading`

              Whether this MCP tool is deferred and discovered via tool search.

            - `Optional<Headers> headers`

              Optional HTTP headers to send to the MCP server. Use for authentication
              or other purposes.

            - `Optional<RequireApproval> requireApproval`

              Specify which of the MCP server's tools require approval.

              - `class McpToolApprovalFilter:`

                Specify which of the MCP server's tools require approval. Can be
                `always`, `never`, or a filter object associated with tools
                that require approval.

                - `Optional<Always> always`

                  A filter object to specify which tools are allowed.

                  - `Optional<Boolean> readOnly`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `Optional<List<String>> toolNames`

                    List of allowed tool names.

                - `Optional<Never> never`

                  A filter object to specify which tools are allowed.

                  - `Optional<Boolean> readOnly`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `Optional<List<String>> toolNames`

                    List of allowed tool names.

              - `enum McpToolApprovalSetting:`

                Specify a single approval policy for all tools. One of `always` or
                `never`. When set to `always`, all tools will require approval. When
                set to `never`, all tools will not require approval.

                - `ALWAYS("always")`

                - `NEVER("never")`

            - `Optional<String> serverDescription`

              Optional description of the MCP server, used to provide more context.

            - `Optional<String> serverUrl`

              The URL for the MCP server. One of `server_url`, `connector_id`, or
              `tunnel_id` must be provided.

            - `Optional<String> tunnelId`

              The Secure MCP Tunnel ID to use instead of a direct server URL. One of
              `server_url`, `connector_id`, or `tunnel_id` must be provided.

          - `CodeInterpreter`

            - `Container container`

              The code interpreter container. Can be a container ID or an object that
              specifies uploaded file IDs to make available to your code, along with an
              optional `memory_limit` setting.

              - `String`

              - `class CodeInterpreterToolAuto:`

                Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

                - `JsonValue; type "auto"constant`

                  Always `auto`.

                  - `AUTO("auto")`

                - `Optional<List<String>> fileIds`

                  An optional list of uploaded files to make available to your code.

                - `Optional<MemoryLimit> memoryLimit`

                  The memory limit for the code interpreter container.

                  - `_1G("1g")`

                  - `_4G("4g")`

                  - `_16G("16g")`

                  - `_64G("64g")`

                - `Optional<NetworkPolicy> networkPolicy`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled:`

                    - `JsonValue; type "disabled"constant`

                      Disable outbound network access. Always `disabled`.

                      - `DISABLED("disabled")`

                  - `class ContainerNetworkPolicyAllowlist:`

                    - `List<String> allowedDomains`

                      A list of allowed domains when type is `allowlist`.

                    - `JsonValue; type "allowlist"constant`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `ALLOWLIST("allowlist")`

                    - `Optional<List<ContainerNetworkPolicyDomainSecret>> domainSecrets`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `String domain`

                        The domain associated with the secret.

                      - `String name`

                        The name of the secret to inject for the domain.

                      - `String value`

                        The secret value to inject for the domain.

            - `JsonValue; type "code_interpreter"constant`

              The type of the code interpreter tool. Always `code_interpreter`.

              - `CODE_INTERPRETER("code_interpreter")`

            - `Optional<List<AllowedCaller>> allowedCallers`

              The tool invocation context(s).

              - `DIRECT("direct")`

              - `PROGRAMMATIC("programmatic")`

          - `JsonValue;`

            - `JsonValue; type "programmatic_tool_calling"constant`

              The type of the tool. Always `programmatic_tool_calling`.

              - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

          - `ImageGeneration`

            - `JsonValue; type "image_generation"constant`

              The type of the image generation tool. Always `image_generation`.

              - `IMAGE_GENERATION("image_generation")`

            - `Optional<Action> action`

              Whether to generate a new image or edit an existing image. Default: `auto`.

              - `GENERATE("generate")`

              - `EDIT("edit")`

              - `AUTO("auto")`

            - `Optional<Background> background`

              Allows to set transparency for the background of the generated image(s). Must
              be one of `transparent`, `opaque`, or `auto` (default value). When `auto` is
              used, the model will automatically determine the best background for the
              image.

              `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`, including their
              `2026-09-08` snapshots, support `opaque` and `transparent` backgrounds.
              Transparent backgrounds are available for supported GPT Image models. For
              `gpt-image-2` and `gpt-image-2-2026-04-21`, this support is in preview. When
              using `transparent`, set the output format to `png` or `webp`.

              - `TRANSPARENT("transparent")`

              - `OPAQUE("opaque")`

              - `AUTO("auto")`

            - `Optional<InputFidelity> inputFidelity`

              Controls fidelity to the original input image(s). This parameter is supported for GPT image models that support input fidelity. `gpt-image-2` and `gpt-image-2-2026-04-21` ignore this parameter.

              - `HIGH("high")`

              - `LOW("low")`

            - `Optional<InputImageMask> inputImageMask`

              Optional mask for inpainting. Contains `image_url`
              (string, optional) and `file_id` (string, optional).

              - `Optional<String> fileId`

                File ID for the mask image.

              - `Optional<String> imageUrl`

                Base64-encoded mask image.

            - `Optional<Model> model`

              The image generation model to use. One of `gpt-image-1`,
              `gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
              `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
              `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
              `gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
              `gpt-image-1`.

              - `GPT_IMAGE_1("gpt-image-1")`

              - `GPT_IMAGE_1_MINI("gpt-image-1-mini")`

              - `GPT_IMAGE_2("gpt-image-2")`

              - `GPT_IMAGE_2_2026_04_21("gpt-image-2-2026-04-21")`

              - `GPT_IMAGE_2_5_SUNBURST("gpt-image-2.5-sunburst")`

              - `GPT_IMAGE_2_5_SUNBURST_2026_09_08("gpt-image-2.5-sunburst-2026-09-08")`

              - `GPT_IMAGE_2_5_FLARE("gpt-image-2.5-flare")`

              - `GPT_IMAGE_2_5_FLARE_2026_09_08("gpt-image-2.5-flare-2026-09-08")`

              - `GPT_IMAGE_1_5("gpt-image-1.5")`

              - `CHATGPT_IMAGE_LATEST("chatgpt-image-latest")`

            - `Optional<Moderation> moderation`

              Moderation level for the generated image. Default: `auto`.

              - `AUTO("auto")`

              - `LOW("low")`

            - `Optional<Long> outputCompression`

              Compression level for the output image. Default: 100.

            - `Optional<OutputFormat> outputFormat`

              The output format of the generated image. One of `png`, `webp`, or
              `jpeg`. Default: `png`.

              - `PNG("png")`

              - `WEBP("webp")`

              - `JPEG("jpeg")`

            - `Optional<Long> partialImages`

              Number of partial images to generate in streaming mode, from 0 (default value) to 3.

            - `Optional<Quality> quality`

              The quality of the generated image. The GPT image models support `low`,
              `medium`, and `high`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`,
              including their `2026-09-08` snapshots, also support `xhigh` and `max`.
              Default: `auto`.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

              - `XHIGH("xhigh")`

              - `MAX("max")`

              - `AUTO("auto")`

            - `Optional<Size> size`

              The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model's current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

              - `_1024X1024("1024x1024")`

              - `_1024X1536("1024x1536")`

              - `_1536X1024("1536x1024")`

              - `AUTO("auto")`

          - `JsonValue;`

            - `JsonValue; type "local_shell"constant`

              The type of the local shell tool. Always `local_shell`.

              - `LOCAL_SHELL("local_shell")`

          - `class FunctionShellTool:`

            A tool that allows the model to execute shell commands.

            - `JsonValue; type "shell"constant`

              The type of the shell tool. Always `shell`.

              - `SHELL("shell")`

            - `Optional<List<AllowedCaller>> allowedCallers`

              The tool invocation context(s).

              - `DIRECT("direct")`

              - `PROGRAMMATIC("programmatic")`

            - `Optional<Environment> environment`

              - `class ContainerAuto:`

                - `JsonValue; type "container_auto"constant`

                  Automatically creates a container for this request

                  - `CONTAINER_AUTO("container_auto")`

                - `Optional<List<String>> fileIds`

                  An optional list of uploaded files to make available to your code.

                - `Optional<MemoryLimit> memoryLimit`

                  The memory limit for the container.

                  - `_1G("1g")`

                  - `_4G("4g")`

                  - `_16G("16g")`

                  - `_64G("64g")`

                - `Optional<NetworkPolicy> networkPolicy`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled:`

                  - `class ContainerNetworkPolicyAllowlist:`

                - `Optional<List<Skill>> skills`

                  An optional list of skills referenced by id or inline data.

                  - `class SkillReference:`

                    - `String skillId`

                      The ID of the referenced skill.

                    - `JsonValue; type "skill_reference"constant`

                      References a skill created with the /v1/skills endpoint.

                      - `SKILL_REFERENCE("skill_reference")`

                    - `Optional<String> version`

                      Optional skill version. Use a positive integer or 'latest'. Omit for default.

                  - `class InlineSkill:`

                    - `String description`

                      The description of the skill.

                    - `String name`

                      The name of the skill.

                    - `InlineSkillSource source`

                      Inline skill payload

                      - `String data`

                        Base64-encoded skill zip bundle.

                      - `JsonValue; mediaType "application/zip"constant`

                        The media type of the inline skill payload. Must be `application/zip`.

                        - `APPLICATION_ZIP("application/zip")`

                      - `JsonValue; type "base64"constant`

                        The type of the inline skill source. Must be `base64`.

                        - `BASE64("base64")`

                    - `JsonValue; type "inline"constant`

                      Defines an inline skill for this request.

                      - `INLINE("inline")`

              - `class LocalEnvironment:`

                - `JsonValue; type "local"constant`

                  Use a local computer environment.

                  - `LOCAL("local")`

                - `Optional<List<LocalSkill>> skills`

                  An optional list of skills.

                  - `String description`

                    The description of the skill.

                  - `String name`

                    The name of the skill.

                  - `String path`

                    The path to the directory containing the skill.

              - `class ContainerReference:`

                - `String containerId`

                  The ID of the referenced container.

                - `JsonValue; type "container_reference"constant`

                  References a container created with the /v1/containers endpoint

                  - `CONTAINER_REFERENCE("container_reference")`

          - `class CustomTool:`

            A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

            - `String name`

              The name of the custom tool, used to identify it in tool calls.

            - `JsonValue; type "custom"constant`

              The type of the custom tool. Always `custom`.

              - `CUSTOM("custom")`

            - `Optional<List<AllowedCaller>> allowedCallers`

              The tool invocation context(s).

              - `DIRECT("direct")`

              - `PROGRAMMATIC("programmatic")`

            - `Optional<Boolean> async`

              Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

            - `Optional<Boolean> deferLoading`

              Whether this tool should be deferred and discovered via tool search.

            - `Optional<String> description`

              Optional description of the custom tool, used to provide more context.

            - `Optional<CustomToolInputFormat> format`

              The input format for the custom tool. Default is unconstrained text.

              - `JsonValue;`

                - `JsonValue; type "text"constant`

                  Unconstrained text format. Always `text`.

                  - `TEXT("text")`

              - `Grammar`

                - `String definition`

                  The grammar definition.

                - `Syntax syntax`

                  The syntax of the grammar definition. One of `lark` or `regex`.

                  - `LARK("lark")`

                  - `REGEX("regex")`

                - `JsonValue; type "grammar"constant`

                  Grammar format. Always `grammar`.

                  - `GRAMMAR("grammar")`

          - `class NamespaceTool:`

            Groups function/custom tools under a shared namespace.

            - `String description`

              A description of the namespace shown to the model.

            - `String name`

              The namespace name used in tool calls (for example, `crm`).

            - `List<Tool> tools`

              The function/custom tools available inside this namespace.

              - `class Function:`

                - `String name`

                - `JsonValue; type "function"constant`

                  - `FUNCTION("function")`

                - `Optional<List<AllowedCaller>> allowedCallers`

                  The tool invocation context(s).

                  - `DIRECT("direct")`

                  - `PROGRAMMATIC("programmatic")`

                - `Optional<Boolean> async`

                  Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

                - `Optional<Boolean> deferLoading`

                  Whether this function should be deferred and discovered via tool search.

                - `Optional<String> description`

                - `Optional<OutputSchema> outputSchema`

                  A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

                - `Optional<JsonValue> parameters`

                - `Optional<Boolean> strict`

                  Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

              - `class CustomTool:`

                A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

            - `JsonValue; type "namespace"constant`

              The type of the tool. Always `namespace`.

              - `NAMESPACE("namespace")`

          - `class ToolSearchTool:`

            Hosted or BYOT tool search configuration for deferred tools.

            - `JsonValue; type "tool_search"constant`

              The type of the tool. Always `tool_search`.

              - `TOOL_SEARCH("tool_search")`

            - `Optional<String> description`

              Description shown to the model for a client-executed tool search tool.

            - `Optional<Execution> execution`

              Whether tool search is executed by the server or by the client.

              - `SERVER("server")`

              - `CLIENT("client")`

            - `Optional<JsonValue> parameters`

              Parameter schema for a client-executed tool search tool.

          - `class WebSearchPreviewTool:`

            This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

            - `Type type`

              The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

              - `WEB_SEARCH_PREVIEW("web_search_preview")`

              - `WEB_SEARCH_PREVIEW_2025_03_11("web_search_preview_2025_03_11")`

            - `Optional<List<SearchContentType>> searchContentTypes`

              - `TEXT("text")`

              - `IMAGE("image")`

            - `Optional<SearchContextSize> searchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<UserLocation> userLocation`

              The approximate location of the user. If omitted or null, defaults to the United States. To avoid this fallback, pass `{"type": "approximate"}` without location fields. To localize results, provide the relevant location fields.

              - `JsonValue; type "approximate"constant`

                The type of location approximation. Always `approximate`.

                - `APPROXIMATE("approximate")`

              - `Optional<String> city`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Optional<String> country`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Optional<String> region`

                Free text input for the region of the user, e.g. `California`.

              - `Optional<String> timezone`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

          - `class ApplyPatchTool:`

            Allows the assistant to create, delete, or update files using unified diffs.

            - `JsonValue; type "apply_patch"constant`

              The type of the tool. Always `apply_patch`.

              - `APPLY_PATCH("apply_patch")`

            - `Optional<List<AllowedCaller>> allowedCallers`

              The tool invocation context(s).

              - `DIRECT("direct")`

              - `PROGRAMMATIC("programmatic")`

        - `JsonValue; type "tool_search_output"constant`

          The item type. Always `tool_search_output`.

          - `TOOL_SEARCH_OUTPUT("tool_search_output")`

        - `Optional<String> id`

          The unique ID of this tool search output.

        - `Optional<String> callId`

          The unique ID of the tool search call generated by the model.

        - `Optional<Execution> execution`

          Whether tool search was executed by the server or by the client.

          - `SERVER("server")`

          - `CLIENT("client")`

        - `Optional<Status> status`

          The status of the tool search output.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `AdditionalTools`

        - `JsonValue; role "developer"constant`

          The role that provided the additional tools. Only `developer` is supported.

          - `DEVELOPER("developer")`

        - `List<Tool> tools`

          A list of additional tools made available at this item.

          - `class FunctionTool:`

            Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

          - `class FileSearchTool:`

            A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

          - `class ComputerTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

          - `class ComputerUsePreviewTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

          - `class WebSearchTool:`

            Search the Internet for sources related to the prompt. Learn more about the
            [web search tool](/api/docs/guides/tools-web-search).

          - `Mcp`

          - `CodeInterpreter`

          - `JsonValue;`

          - `ImageGeneration`

          - `JsonValue;`

          - `class FunctionShellTool:`

            A tool that allows the model to execute shell commands.

          - `class CustomTool:`

            A custom tool that processes input using a specified format. Learn more about   [custom tools](/api/docs/guides/function-calling#custom-tools)

          - `class NamespaceTool:`

            Groups function/custom tools under a shared namespace.

          - `class ToolSearchTool:`

            Hosted or BYOT tool search configuration for deferred tools.

          - `class WebSearchPreviewTool:`

            This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

          - `class ApplyPatchTool:`

            Allows the assistant to create, delete, or update files using unified diffs.

        - `JsonValue; type "additional_tools"constant`

          The item type. Always `additional_tools`.

          - `ADDITIONAL_TOOLS("additional_tools")`

        - `Optional<String> id`

          The unique ID of this additional tools item.

      - `class ResponseConfigurationUpdateItemParam:`

        An update to the conversation's response configuration. The configuration
        remains in effect for subsequent responses until it is replaced by another
        configuration update.

        - `JsonValue; type "configuration_update"constant`

          The item type. Always `configuration_update`.

          - `CONFIGURATION_UPDATE("configuration_update")`

        - `Optional<String> id`

          The unique ID of the configuration update item.

        - `Optional<Reasoning> reasoning`

          Updates to reasoning configuration. Only effort is supported.

          - `Optional<ReasoningEffort> effort`

            The reasoning effort to use for subsequent responses until another
            configuration update replaces it.

            - `NONE("none")`

            - `MINIMAL("minimal")`

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

            - `XHIGH("xhigh")`

            - `MAX("max")`

      - `class ResponseReasoningItem:`

        A description of the chain of thought used by a reasoning model while generating
        a response. Be sure to include these items in your `input` to the Responses API
        for subsequent turns of a conversation if you are manually
        [managing context](/api/docs/guides/conversation-state).

        - `String id`

          The unique identifier of the reasoning content.

        - `List<Summary> summary`

          Reasoning summary content.

          - `String text`

            A summary of the reasoning output from the model so far.

          - `JsonValue; type "summary_text"constant`

            The type of the object. Always `summary_text`.

            - `SUMMARY_TEXT("summary_text")`

        - `JsonValue; type "reasoning"constant`

          The type of the object. Always `reasoning`.

          - `REASONING("reasoning")`

        - `Optional<List<Content>> content`

          Reasoning text content.

          - `String text`

            The reasoning text from the model.

          - `JsonValue; type "reasoning_text"constant`

            The type of the reasoning text. Always `reasoning_text`.

            - `REASONING_TEXT("reasoning_text")`

        - `Optional<String> encryptedContent`

          The encrypted content of the reasoning item. This is populated by default
          for reasoning items returned by `POST /v1/responses` and WebSocket
          `response.create` requests.

          When streaming, use the completed reasoning item and its
          `encrypted_content` from the `response.output_item.done` event in
          subsequent requests. The `encrypted_content` in
          `response.output_item.added` may be incomplete. This is especially
          important when `store` is `false` or when using Zero Data Retention.

        - `Optional<Status> status`

          The status of the item. One of `in_progress`, `completed`, or
          `incomplete`. Populated when items are returned via API.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `class ResponseCompactionItemParam:`

        A compaction item generated by the [`v1/responses/compact` API](/api/reference/resources/responses/methods/compact).

        - `String encryptedContent`

          The encrypted content of the compaction summary.

        - `JsonValue; type "compaction"constant`

          The type of the item. Always `compaction`.

          - `COMPACTION("compaction")`

        - `Optional<String> id`

          The ID of the compaction item.

      - `ImageGenerationCall`

        - `String id`

          The unique ID of the image generation call.

        - `Optional<String> result`

          The generated image encoded in base64.

        - `Status status`

          The status of the image generation call.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `GENERATING("generating")`

          - `FAILED("failed")`

        - `JsonValue; type "image_generation_call"constant`

          The type of the image generation call. Always `image_generation_call`.

          - `IMAGE_GENERATION_CALL("image_generation_call")`

        - `Optional<Action> action`

          The action used for image generation.

          - `GENERATE("generate")`

          - `EDIT("edit")`

          - `AUTO("auto")`

        - `Optional<Background> background`

          The background setting used for generation.

          - `TRANSPARENT("transparent")`

          - `OPAQUE("opaque")`

          - `AUTO("auto")`

        - `Optional<OutputFormat> outputFormat`

          The output format used for generation.

          - `PNG("png")`

          - `WEBP("webp")`

          - `JPEG("jpeg")`

        - `Optional<Quality> quality`

          The quality of the image generated by the image generation tool call. One of `low`, `medium`, `high`, `xhigh`, `max`, or `auto`.

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

          - `MAX("max")`

          - `AUTO("auto")`

        - `Optional<String> revisedPrompt`

          The prompt that was used after any model prompt rewriting.

        - `Optional<Size> size`

          The image dimensions as a `WIDTHxHEIGHT` string, for example `1536x864`.

          - `_1024X1024("1024x1024")`

          - `_1024X1536("1024x1536")`

          - `_1536X1024("1536x1024")`

      - `class ResponseCodeInterpreterToolCall:`

        A tool call to run code.

        - `String id`

          The unique ID of the code interpreter tool call.

        - `Optional<String> code`

          The code to run, or null if not available.

        - `String containerId`

          The ID of the container used to run the code.

        - `Optional<List<Output>> outputs`

          The outputs generated by the code interpreter, such as logs or images.
          Can be null if no outputs are available.

          - `class Logs:`

            The logs output from the code interpreter.

            - `String logs`

              The logs output from the code interpreter.

            - `JsonValue; type "logs"constant`

              The type of the output. Always `logs`.

              - `LOGS("logs")`

          - `class Image:`

            The image output from the code interpreter.

            - `JsonValue; type "image"constant`

              The type of the output. Always `image`.

              - `IMAGE("image")`

            - `String url`

              The URL of the image output from the code interpreter.

        - `Status status`

          The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

          - `INTERPRETING("interpreting")`

          - `FAILED("failed")`

        - `JsonValue; type "code_interpreter_call"constant`

          The type of the code interpreter tool call. Always `code_interpreter_call`.

          - `CODE_INTERPRETER_CALL("code_interpreter_call")`

      - `LocalShellCall`

        - `String id`

          The unique ID of the local shell call.

        - `Action action`

          Execute a shell command on the server.

          - `List<String> command`

            The command to run.

          - `Env env`

            Environment variables to set for the command.

          - `JsonValue; type "exec"constant`

            The type of the local shell action. Always `exec`.

            - `EXEC("exec")`

          - `Optional<Long> timeoutMs`

            Optional timeout in milliseconds for the command.

          - `Optional<String> user`

            Optional user to run the command as.

          - `Optional<String> workingDirectory`

            Optional working directory to run the command in.

        - `String callId`

          The unique ID of the local shell tool call generated by the model.

        - `Status status`

          The status of the local shell call.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

        - `JsonValue; type "local_shell_call"constant`

          The type of the local shell call. Always `local_shell_call`.

          - `LOCAL_SHELL_CALL("local_shell_call")`

      - `LocalShellCallOutput`

        - `String id`

          The unique ID of the local shell tool call generated by the model.

        - `String output`

          A JSON string of the output of the local shell tool call.

        - `JsonValue; type "local_shell_call_output"constant`

          The type of the local shell tool call output. Always `local_shell_call_output`.

          - `LOCAL_SHELL_CALL_OUTPUT("local_shell_call_output")`

        - `Optional<Status> status`

          The status of the item. One of `in_progress`, `completed`, or `incomplete`.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `ShellCall`

        - `Action action`

          The shell commands and limits that describe how to run the tool call.

          - `List<String> commands`

            Ordered shell commands for the execution environment to run.

          - `Optional<Long> maxOutputLength`

            Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

          - `Optional<Long> timeoutMs`

            Maximum wall-clock time in milliseconds to allow the shell commands to run.

        - `String callId`

          The unique ID of the shell tool call generated by the model.

        - `JsonValue; type "shell_call"constant`

          The type of the item. Always `shell_call`.

          - `SHELL_CALL("shell_call")`

        - `Optional<String> id`

          The unique ID of the shell tool call. Populated when this item is returned via API.

        - `Optional<Caller> caller`

          The execution context that produced this tool call.

          - `JsonValue;`

            - `JsonValue; type "direct"constant`

              The caller type. Always `direct`.

              - `DIRECT("direct")`

          - `class Program:`

            - `String callerId`

              The call ID of the program item that produced this tool call.

            - `JsonValue; type "program"constant`

              The caller type. Always `program`.

              - `PROGRAM("program")`

        - `Optional<Environment> environment`

          The environment to execute the shell commands in.

          - `class LocalEnvironment:`

          - `class ContainerReference:`

        - `Optional<Status> status`

          The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `ShellCallOutput`

        - `String callId`

          The unique ID of the shell tool call generated by the model.

        - `List<ResponseFunctionShellCallOutputContent> output`

          Captured chunks of stdout and stderr output, along with their associated outcomes.

          - `Outcome outcome`

            The exit or timeout outcome associated with this shell call.

            - `JsonValue;`

              - `JsonValue; type "timeout"constant`

                The outcome type. Always `timeout`.

                - `TIMEOUT("timeout")`

            - `class Exit:`

              Indicates that the shell commands finished and returned an exit code.

              - `long exitCode`

                The exit code returned by the shell process.

              - `JsonValue; type "exit"constant`

                The outcome type. Always `exit`.

                - `EXIT("exit")`

          - `String stderr`

            Captured stderr output for the shell call.

          - `String stdout`

            Captured stdout output for the shell call.

        - `JsonValue; type "shell_call_output"constant`

          The type of the item. Always `shell_call_output`.

          - `SHELL_CALL_OUTPUT("shell_call_output")`

        - `Optional<String> id`

          The unique ID of the shell tool call output. Populated when this item is returned via API.

        - `Optional<Caller> caller`

          The execution context that produced this tool call.

          - `JsonValue;`

            - `JsonValue; type "direct"constant`

              The caller type. Always `direct`.

              - `DIRECT("direct")`

          - `class Program:`

            - `String callerId`

              The call ID of the program item that produced this tool call.

            - `JsonValue; type "program"constant`

              The caller type. Always `program`.

              - `PROGRAM("program")`

        - `Optional<Long> maxOutputLength`

          The maximum number of UTF-8 characters captured for this shell call's combined output.

        - `Optional<Status> status`

          The status of the shell call output.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

      - `ApplyPatchCall`

        - `String callId`

          The unique ID of the apply patch tool call generated by the model.

        - `Operation operation`

          The specific create, delete, or update instruction for the apply_patch tool call.

          - `class CreateFile:`

            Instruction for creating a new file via the apply_patch tool.

            - `String diff`

              Unified diff content to apply when creating the file.

            - `String path`

              Path of the file to create relative to the workspace root.

            - `JsonValue; type "create_file"constant`

              The operation type. Always `create_file`.

              - `CREATE_FILE("create_file")`

          - `class DeleteFile:`

            Instruction for deleting an existing file via the apply_patch tool.

            - `String path`

              Path of the file to delete relative to the workspace root.

            - `JsonValue; type "delete_file"constant`

              The operation type. Always `delete_file`.

              - `DELETE_FILE("delete_file")`

          - `class UpdateFile:`

            Instruction for updating an existing file via the apply_patch tool.

            - `String diff`

              Unified diff content to apply to the existing file.

            - `String path`

              Path of the file to update relative to the workspace root.

            - `JsonValue; type "update_file"constant`

              The operation type. Always `update_file`.

              - `UPDATE_FILE("update_file")`

        - `Status status`

          The status of the apply patch tool call. One of `in_progress` or `completed`.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

        - `JsonValue; type "apply_patch_call"constant`

          The type of the item. Always `apply_patch_call`.

          - `APPLY_PATCH_CALL("apply_patch_call")`

        - `Optional<String> id`

          The unique ID of the apply patch tool call. Populated when this item is returned via API.

        - `Optional<Caller> caller`

          The execution context that produced this tool call.

          - `JsonValue;`

            - `JsonValue; type "direct"constant`

              The caller type. Always `direct`.

              - `DIRECT("direct")`

          - `class Program:`

            - `String callerId`

              The call ID of the program item that produced this tool call.

            - `JsonValue; type "program"constant`

              The caller type. Always `program`.

              - `PROGRAM("program")`

      - `ApplyPatchCallOutput`

        - `String callId`

          The unique ID of the apply patch tool call generated by the model.

        - `Status status`

          The status of the apply patch tool call output. One of `completed` or `failed`.

          - `COMPLETED("completed")`

          - `FAILED("failed")`

        - `JsonValue; type "apply_patch_call_output"constant`

          The type of the item. Always `apply_patch_call_output`.

          - `APPLY_PATCH_CALL_OUTPUT("apply_patch_call_output")`

        - `Optional<String> id`

          The unique ID of the apply patch tool call output. Populated when this item is returned via API.

        - `Optional<Caller> caller`

          The execution context that produced this tool call.

          - `JsonValue;`

            - `JsonValue; type "direct"constant`

              The caller type. Always `direct`.

              - `DIRECT("direct")`

          - `class Program:`

            - `String callerId`

              The call ID of the program item that produced this tool call.

            - `JsonValue; type "program"constant`

              The caller type. Always `program`.

              - `PROGRAM("program")`

        - `Optional<String> output`

          Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

      - `McpListTools`

        - `String id`

          The unique ID of the list.

        - `String serverLabel`

          The label of the MCP server.

        - `List<Tool> tools`

          The tools available on the server.

          - `JsonValue inputSchema`

            The JSON schema describing the tool's input.

          - `String name`

            The name of the tool.

          - `Optional<JsonValue> annotations`

            Additional annotations about the tool.

          - `Optional<String> description`

            The description of the tool.

        - `JsonValue; type "mcp_list_tools"constant`

          The type of the item. Always `mcp_list_tools`.

          - `MCP_LIST_TOOLS("mcp_list_tools")`

        - `Optional<String> error`

          Error message if the server could not list tools.

      - `McpApprovalRequest`

        - `String id`

          The unique ID of the approval request.

        - `String arguments`

          A JSON string of arguments for the tool.

        - `String name`

          The name of the tool to run.

        - `String serverLabel`

          The label of the MCP server making the request.

        - `JsonValue; type "mcp_approval_request"constant`

          The type of the item. Always `mcp_approval_request`.

          - `MCP_APPROVAL_REQUEST("mcp_approval_request")`

      - `McpApprovalResponse`

        - `String approvalRequestId`

          The ID of the approval request being answered.

        - `boolean approve`

          Whether the request was approved.

        - `JsonValue; type "mcp_approval_response"constant`

          The type of the item. Always `mcp_approval_response`.

          - `MCP_APPROVAL_RESPONSE("mcp_approval_response")`

        - `Optional<String> id`

          The unique ID of the approval response

        - `Optional<String> reason`

          Optional reason for the decision.

      - `McpCall`

        - `String id`

          The unique ID of the tool call.

        - `String arguments`

          A JSON string of the arguments passed to the tool.

        - `String name`

          The name of the tool that was run.

        - `String serverLabel`

          The label of the MCP server running the tool.

        - `JsonValue; type "mcp_call"constant`

          The type of the item. Always `mcp_call`.

          - `MCP_CALL("mcp_call")`

        - `Optional<String> approvalRequestId`

          Unique identifier for the MCP tool call approval request.
          Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

        - `Optional<McpToolCallError> error`

          The error from the tool call, if any.

          - `McpProtocolError`

            - `long code`

            - `String message`

            - `JsonValue; type "mcp_protocol_error"constant`

              - `MCP_PROTOCOL_ERROR("mcp_protocol_error")`

          - `McpToolExecutionError`

            - `JsonValue content`

            - `JsonValue; type "mcp_tool_execution_error"constant`

              - `MCP_TOOL_EXECUTION_ERROR("mcp_tool_execution_error")`

          - `HttpError`

            - `long code`

            - `String message`

            - `JsonValue; type "http_error"constant`

              - `HTTP_ERROR("http_error")`

        - `Optional<String> output`

          The output from the tool call.

        - `Optional<Status> status`

          The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

          - `IN_PROGRESS("in_progress")`

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

          - `CALLING("calling")`

          - `FAILED("failed")`

      - `class ResponseCustomToolCallOutput:`

        The output of a custom tool call from your code, being sent back to the model.

        - `String callId`

          The call ID, used to map this custom tool call output to a custom tool call.

        - `Output output`

          The output from the custom tool call generated by your code.
          Can be a string or an list of output content.

          - `String`

          - `List<FunctionAndCustomToolCallOutput>`

            - `class ResponseInputText:`

              A text input to the model.

            - `class ResponseInputImage:`

              An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

            - `class ResponseInputFile:`

              A file input to the model.

        - `JsonValue; type "custom_tool_call_output"constant`

          The type of the custom tool call output. Always `custom_tool_call_output`.

          - `CUSTOM_TOOL_CALL_OUTPUT("custom_tool_call_output")`

        - `Optional<String> id`

          The unique ID of the custom tool call output in the OpenAI platform.

        - `Optional<Caller> caller`

          The execution context that produced this tool call.

          - `JsonValue;`

            - `JsonValue; type "direct"constant`

              The caller type. Always `direct`.

              - `DIRECT("direct")`

          - `class Program:`

            - `String callerId`

              The call ID of the program item that produced this tool call.

            - `JsonValue; type "program"constant`

              The caller type. Always `program`.

              - `PROGRAM("program")`

      - `class ResponseCustomToolCall:`

        A call to a custom tool created by the model.

        - `String callId`

          An identifier used to map this custom tool call to a tool call output.

        - `String input`

          The input for the custom tool call generated by the model.

        - `String name`

          The name of the custom tool being called.

        - `JsonValue; type "custom_tool_call"constant`

          The type of the custom tool call. Always `custom_tool_call`.

          - `CUSTOM_TOOL_CALL("custom_tool_call")`

        - `Optional<String> id`

          The unique ID of the custom tool call in the OpenAI platform.

        - `Optional<Boolean> async`

          Whether the custom tool call runs asynchronously.

        - `Optional<Caller> caller`

          The execution context that produced this tool call.

          - `JsonValue;`

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class Program:`

            - `String callerId`

              The call ID of the program item that produced this tool call.

            - `JsonValue; type "program"constant`

              - `PROGRAM("program")`

        - `Optional<String> namespace`

          The namespace of the custom tool being called.

      - `JsonValue;`

        - `JsonValue; type "compaction_trigger"constant`

          The type of the item. Always `compaction_trigger`.

          - `COMPACTION_TRIGGER("compaction_trigger")`

      - `ItemReference`

        - `String id`

          The ID of the item to reference.

        - `Optional<Type> type`

          The type of item to reference. Always `item_reference`.

          - `ITEM_REFERENCE("item_reference")`

      - `Program`

        - `String id`

          The unique ID of this program item.

        - `String callId`

          The stable call ID of the program item.

        - `String code`

          The JavaScript source executed by programmatic tool calling.

        - `String fingerprint`

          Opaque program replay fingerprint that must be round-tripped.

        - `JsonValue; type "program"constant`

          The item type. Always `program`.

          - `PROGRAM("program")`

      - `ProgramOutput`

        - `String id`

          The unique ID of this program output item.

        - `String callId`

          The call ID of the program item.

        - `String result`

          The result produced by the program item.

        - `Status status`

          The terminal status of the program output.

          - `COMPLETED("completed")`

          - `INCOMPLETE("incomplete")`

        - `JsonValue; type "program_output"constant`

          The item type. Always `program_output`.

          - `PROGRAM_OUTPUT("program_output")`

    - `JsonValue; type "response.item.create"constant`

      The Live client event type. Always `response.item.create`.

      - `RESPONSE_ITEM_CREATE("response.item.create")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class ResponseCreateEvent:`

    Request a response from the Live session’s Responses backend, or continue a delegated response waiting for tool results. Requires Responses delegation.

    - `JsonValue; type "response.create"constant`

      The Live client event type. Always `response.create`.

      - `RESPONSE_CREATE("response.create")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

  - `class SessionCloseEvent:`

    Request that the Live session close. The terminal `session.closed` event contains the close reason and final usage.

    - `JsonValue; type "session.close"constant`

      The Live client event type. Always `session.close`.

      - `SESSION_CLOSE("session.close")`

    - `Optional<String> eventId`

      Optional client identifier for correlating this command with a server event's client_event_id or error.client_event_id.

### Fork Server Event

- `class ForkServerEvent: A class that can be one of several variants.union`

  Server events for Live. Response lifecycle events are wrapped inside response.event; dispatch the nested event by its full type and tolerate new response event types. Follow the [Live prompting guide](https://developers.openai.com/api/docs/guides/live-prompting) when designing the conversation and delegation policy.

  - `class SessionStartedEvent:`

    Returned when a Live session has started. Contains the resolved session configuration, including server defaults.

    - `String eventId`

      The unique ID of the Live server event.

    - `SessionResource session`

      The resolved Live session configuration and server-assigned session metadata.

      - `String id`

        The unique ID of the Live session. Use this ID for sideband connections, forking, and recording download.

      - `long expiresAt`

        The Unix timestamp, in seconds, at which the Live session expires.

      - `Model model`

        The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

        - `GPT_LIVE_1("gpt-live-1")`

      - `JsonValue; status "active"constant`

        The status of the session snapshot. Always `active`, including the final snapshot in session.closed; use the event type to determine that the session has closed.

        - `ACTIVE("active")`

      - `Optional<Audio> audio`

        Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

        - `Optional<AudioFormat> format`

          Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

          - `AudioPcm`

            - `Rate rate`

              Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

              - `_16000(16000)`

              - `_24000(24000)`

            - `JsonValue; type "audio/pcm"constant`

              The audio encoding. Always `audio/pcm`.

              - `AUDIO_PCM("audio/pcm")`

          - `AudioPcmu`

            - `long rate`

              Audio sample rate in hertz. G.711 audio uses 8000 Hz.

            - `JsonValue; type "audio/pcmu"constant`

              The audio encoding. Always `audio/pcmu`.

              - `AUDIO_PCMU("audio/pcmu")`

          - `AudioPcma`

            - `long rate`

              Audio sample rate in hertz. G.711 audio uses 8000 Hz.

            - `JsonValue; type "audio/pcma"constant`

              The audio encoding. Always `audio/pcma`.

              - `AUDIO_PCMA("audio/pcma")`

        - `Optional<Output> output`

          The voice used for speech generated by the Live model.

          - `Optional<Voice> voice`

            The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

            - `String`

            - `enum BuiltInVoice:`

              A built-in voice available for Live speech.

              - `ALLOY("alloy")`

              - `ASH("ash")`

              - `BALLAD("ballad")`

              - `BEACON("beacon")`

              - `BOSSA("bossa")`

              - `CEDAR("cedar")`

              - `CINDER("cinder")`

              - `CORAL("coral")`

              - `DELTA("delta")`

              - `ECHO("echo")`

              - `GLEAM("gleam")`

              - `MARIN("marin")`

              - `MERIDIAN("meridian")`

              - `QUARTZ("quartz")`

              - `RIPPLE("ripple")`

              - `SAGE("sage")`

              - `SHIMMER("shimmer")`

              - `STONE("stone")`

              - `TEMPO("tempo")`

              - `VERSE("verse")`

              - `VESPER("vesper")`

              - `WILLOW("willow")`

            - `class CustomVoice:`

              - `String id`

      - `Optional<ClientConfig> client`

        Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

        - `DataChannelConfig dataChannel`

          Client and server event permissions for the WebRTC frontend data channel.

          - `Optional<AllowedClientEvents> allowedClientEvents`

            Client event types that the frontend data channel may send. Use 'all' to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

            - `JsonValue;`

              - `ALL("all")`

            - `List<String>`

          - `Optional<AllowedServerEvents> allowedServerEvents`

            Server events that may be sent to the frontend data channel. Use 'all' to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type 'response.event' and a response_event selector.

            - `JsonValue;`

              - `ALL("all")`

            - `List<ServerEventSelector>`

              - `String type`

                The outer Live server event type. Use 'response.event' for Responses events.

              - `Optional<String> responseEvent`

                The nested Responses event type. Required when type is 'response.event'; forbidden for other event types.

      - `Optional<Delegation> delegation`

        Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

        - `class ClientDelegation:`

          Delegate tasks to your application. The Live session emits delegation events that your backend handles.

          - `JsonValue; type "client"constant`

            The delegation owner. Always `client` for tasks handled by your application.

            - `CLIENT("client")`

        - `class Responses:`

          Delegate tasks to a Responses model managed by the Live session.

          - `ResponsesDelegationConfig responses`

            Backend model, prompt, and tools used when the Live session delegates a task to Responses.

            - `String model`

              The model used for server-owned Responses delegations.

            - `Optional<String> instructions`

              Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

            - `Optional<Long> maxOutputTokens`

              Maximum number of output tokens for each delegated response.

            - `Optional<Boolean> parallelToolCalls`

              Whether the delegated Responses model may request multiple tool calls in a single response.

            - `Optional<Reasoning> reasoning`

              Reasoning settings passed to each delegated Responses request.

              - `Optional<Effort> effort`

                How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

                - `NONE("none")`

                - `MINIMAL("minimal")`

                - `LOW("low")`

                - `MEDIUM("medium")`

                - `HIGH("high")`

                - `XHIGH("xhigh")`

              - `Optional<Summary> summary`

                The reasoning summary to request from the delegated Responses model, when supported.

                - `CONCISE("concise")`

                - `DETAILED("detailed")`

                - `AUTO("auto")`

            - `Optional<ServiceTier> serviceTier`

              Service tier for delegated Responses requests.

              - `AUTO("auto")`

              - `DEFAULT("default")`

              - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

              - `FLEX("flex")`

              - `PRIORITY("priority")`

              - `ULTRAFAST("ultrafast")`

            - `Optional<Text> text`

              Text generation settings passed to each delegated Responses request.

              - `Optional<Verbosity> verbosity`

                The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

                - `LOW("low")`

                - `MEDIUM("medium")`

                - `HIGH("high")`

            - `Optional<ToolChoice> toolChoice`

              Controls which tool the Responses backend uses when handling a task delegated by the Live model.

              - `enum LiveToolChoiceEnum:`

                - `AUTO("auto")`

                - `NONE("none")`

                - `REQUIRED("required")`

              - `class LiveFunctionToolChoiceParam:`

                - `String name`

                - `JsonValue; type "function"constant`

                  - `FUNCTION("function")`

              - `class LiveMcpToolChoiceParam:`

                - `String name`

                - `String serverLabel`

                - `JsonValue; type "mcp"constant`

                  - `MCP("mcp")`

            - `Optional<List<Tool>> tools`

              Tools available to the Responses backend while it handles tasks delegated by the Live model.

              - `class FunctionTool:`

                A function tool available to the Responses backend when the Live model delegates a task.

                - `String name`

                  The name the delegated Responses model uses when calling this function.

                - `JsonValue; type "function"constant`

                  The tool type. Always `function`.

                  - `FUNCTION("function")`

                - `Optional<String> description`

                  What the function does and when the delegated Responses model should call it.

                - `Optional<Parameters> parameters`

                  A JSON Schema object describing the arguments accepted by the function.

                - `Optional<Boolean> strict`

                  Whether the delegated Responses model must follow the function’s parameter schema exactly.

              - `JsonValue;`

                - `JsonValue; type "web_search"constant`

                  The tool type. Always `web_search`.

                  - `WEB_SEARCH("web_search")`

          - `JsonValue; type "responses"constant`

            The delegation owner. Always `responses` for tasks handled by the Responses API.

            - `RESPONSES("responses")`

      - `Optional<List<InitialItem>> input`

        Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

        - `Developer`

          - `List<Content> content`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `String text`

              The message text to include in the Live session’s initial conversation history.

            - `Optional<Type> type`

              The text content type. Always `input_text`.

              - `INPUT_TEXT("input_text")`

          - `JsonValue; role "developer"constant`

            The author of this history message. Always `developer`.

            - `DEVELOPER("developer")`

          - `Optional<String> id`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Optional<Status> status`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `INCOMPLETE("incomplete")`

            - `COMPLETED("completed")`

          - `Optional<Type> type`

            The history item type. Always `message`.

            - `MESSAGE("message")`

        - `User`

          - `List<Content> content`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `String text`

              The message text to include in the Live session’s initial conversation history.

            - `Optional<Type> type`

              The text content type. Always `input_text`.

              - `INPUT_TEXT("input_text")`

          - `JsonValue; role "user"constant`

            The author of this history message. Always `user`.

            - `USER("user")`

          - `Optional<String> id`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Optional<Status> status`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `INCOMPLETE("incomplete")`

            - `COMPLETED("completed")`

          - `Optional<Type> type`

            The history item type. Always `message`.

            - `MESSAGE("message")`

        - `Assistant`

          - `List<Content> content`

            The message content. Supply exactly one text part for the initial Live conversation history.

            - `class Text:`

              Assistant text supplied as conversation history when starting a Live session.

              - `String text`

                The message text to include in the Live session’s initial conversation history.

              - `Optional<Type> type`

                The text content type. Always `text`.

                - `TEXT("text")`

            - `class OutputText:`

              Assistant output text supplied as conversation history when starting a Live session.

              - `String text`

                The message text to include in the Live session’s initial conversation history.

              - `JsonValue; type "output_text"constant`

                The text content type. Always `output_text`.

                - `OUTPUT_TEXT("output_text")`

          - `JsonValue; role "assistant"constant`

            The author of this history message. Always `assistant`.

            - `ASSISTANT("assistant")`

          - `Optional<String> id`

            An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

          - `Optional<Status> status`

            The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

            - `INCOMPLETE("incomplete")`

            - `COMPLETED("completed")`

          - `Optional<Type> type`

            The history item type. Always `message`.

            - `MESSAGE("message")`

      - `Optional<String> instructions`

        Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

      - `Optional<Boolean> store`

        Whether to store the session for later forking and recording download. Defaults to false for new sessions.

    - `JsonValue; type "session.started"constant`

      The event type, always `session.started`.

      - `SESSION_STARTED("session.started")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class SessionUpdatedEvent:`

    Returned when a Live session update is accepted. Contains the resolved session configuration after the update.

    - `String eventId`

      The unique ID of the Live server event.

    - `SessionResource session`

      The resolved Live session configuration and server-assigned session metadata.

    - `JsonValue; type "session.updated"constant`

      The event type, always `session.updated`.

      - `SESSION_UPDATED("session.updated")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class InputAudioMutedEvent:`

    Returned when a session.input_audio.mute command is accepted. Input audio is no longer sent to the model; sideband audio reflection continues.

    - `String eventId`

      The unique ID of the Live server event.

    - `JsonValue; type "session.input_audio.muted"constant`

      The event type, always `session.input_audio.muted`.

      - `SESSION_INPUT_AUDIO_MUTED("session.input_audio.muted")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class InputAudioUnmutedEvent:`

    Returned when a session.input_audio.unmute command is accepted. Input audio is sent to the model again.

    - `String eventId`

      The unique ID of the Live server event.

    - `JsonValue; type "session.input_audio.unmuted"constant`

      The event type, always `session.input_audio.unmuted`.

      - `SESSION_INPUT_AUDIO_UNMUTED("session.input_audio.unmuted")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class InstructionsAppendedEvent:`

    Returned when a session.instructions.append command is accepted into the Live session timeline. Acknowledges the appended instructions without guaranteeing that the model has acted on them.

    - `long endMs`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `String eventId`

      The unique ID of the Live server event.

    - `long startMs`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `JsonValue; type "session.instructions.appended"constant`

      The event type, always `session.instructions.appended`.

      - `SESSION_INSTRUCTIONS_APPENDED("session.instructions.appended")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class ThinkingAppendedEvent:`

    Returned when a session.thinking.append command is accepted into the Live session timeline. Acknowledges the added reasoning context without guaranteeing any spoken output.

    - `long endMs`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `String eventId`

      The unique ID of the Live server event.

    - `long startMs`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `JsonValue; type "session.thinking.appended"constant`

      The event type, always `session.thinking.appended`.

      - `SESSION_THINKING_APPENDED("session.thinking.appended")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class CommentaryAppendedEvent:`

    Returned when a session.commentary.append command is accepted into the Live session timeline. Acknowledges the added commentary without guaranteeing exact wording or completed audio playback.

    - `long endMs`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `String eventId`

      The unique ID of the Live server event.

    - `long startMs`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `JsonValue; type "session.commentary.appended"constant`

      The event type, always `session.commentary.appended`.

      - `SESSION_COMMENTARY_APPENDED("session.commentary.appended")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `SessionInputAudioAppend`

    - `String audio`

      Base64-encoded raw mono PCM16LE at 24 kHz received from the primary transport, reflected to the sideband before model-input muting. This server event uses the same audio key as the client command, but is not an acknowledgment of it.

    - `JsonValue; type "session.input_audio.append"constant`

      The event type, always `session.input_audio.append`.

      - `SESSION_INPUT_AUDIO_APPEND("session.input_audio.append")`

  - `class OutputAudioDeltaEvent:`

    An audio chunk generated by the Live model. Decode and play primary WebSocket chunks in delivery order using the configured session audio format. Sideband connections receive reflected output audio with timestamps.

    - `String delta`

      Base64-encoded raw audio. Primary WebSocket events use the session's configured format; reflected sideband events use mono PCM16LE at 24 kHz.

    - `JsonValue; type "session.output_audio.delta"constant`

      The event type, always `session.output_audio.delta`.

      - `SESSION_OUTPUT_AUDIO_DELTA("session.output_audio.delta")`

    - `Optional<Long> endMs`

      Exclusive session-relative end in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket. Dropped output frames leave gaps between reflected ranges.

    - `Optional<Long> startMs`

      Inclusive session-relative start in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket.

  - `class InputTranscriptDeltaEvent:`

    A transcript fragment for user input audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

    - `String delta`

      The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

    - `long endMs`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `String eventId`

      The unique ID of the Live server event.

    - `long startMs`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `JsonValue; type "session.input_transcript.delta"constant`

      The event type, always `session.input_transcript.delta`.

      - `SESSION_INPUT_TRANSCRIPT_DELTA("session.input_transcript.delta")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class OutputTranscriptDeltaEvent:`

    A transcript fragment for assistant output audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

    - `String delta`

      The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

    - `long endMs`

      The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start_ms.

    - `String eventId`

      The unique ID of the Live server event.

    - `long startMs`

      The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

    - `JsonValue; type "session.output_transcript.delta"constant`

      The event type, always `session.output_transcript.delta`.

      - `SESSION_OUTPUT_TRANSCRIPT_DELTA("session.output_transcript.delta")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class DelegationCreatedEvent:`

    Returned when the Live model delegates work to your application or a Responses backend. Contains delegation metadata and the position on the session timeline where the work was delegated.

    - `Delegation delegation`

      The delegated work identifier and destination. This object contains metadata, not the task text.

      - `String id`

        The unique ID of the delegation. Use this as delegation_id when replying to client-owned work or correlating Responses events.

      - `Target target`

        Where the Live model delegated the work: `client` for your application, or `responses` for the configured Responses backend.

        - `CLIENT("client")`

        - `RESPONSES("responses")`

      - `JsonValue; type "delegation"constant`

        The object type, always `delegation`.

        - `DELEGATION("delegation")`

      - `Optional<String> responseId`

        The ID of the Responses API response associated with a Responses delegation. Omitted for client delegations.

    - `String eventId`

      The unique ID of the Live server event.

    - `long offsetMs`

      The position on the Live session timeline where the delegation was created, in milliseconds from the beginning of the session.

    - `JsonValue; type "session.delegation.created"constant`

      The event type, always `session.delegation.created`.

      - `SESSION_DELEGATION_CREATED("session.delegation.created")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class ResponseEvent:`

    A streaming Responses API event from a backend delegated to by the Live session. Use the outer delegation_id to associate the nested stream with its Live delegation.

    - `Event event`

      The nested Responses streaming event. Dispatch on its type field. Response lifecycle snapshots omit input and clear instructions, tools, and output to keep messages small; consume granular output events for the generated content.

    - `String eventId`

      The unique ID of the Live server event.

    - `JsonValue; type "response.event"constant`

      The event type, always `response.event`.

      - `RESPONSE_EVENT("response.event")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

    - `Optional<String> delegationId`

      The Live delegation associated with the nested Responses event. May be null or omitted when the event cannot be correlated with a delegation.

  - `class SessionUsageUpdatedEvent:`

    Reports cumulative Live audio usage and, when available, the most recent context-window usage. Delegated Responses token usage is reported separately in response.event events.

    - `String eventId`

      The unique ID of the Live server event.

    - `JsonValue; type "session.usage.updated"constant`

      The event type, always `session.usage.updated`.

      - `SESSION_USAGE_UPDATED("session.usage.updated")`

    - `SessionUsage usage`

      The cumulative Live audio usage so far.

      - `double seconds`

        The cumulative Live audio duration in seconds. Do not sum this value across usage events.

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

    - `Optional<ContextWindow> contextWindow`

      The latest measured Live context-window usage. Omitted when the context limit is unknown.

      - `double usageRatio`

        The latest active context token count divided by the Live model context limit. Can decrease after compaction and may lag between measured audio frames.

  - `class SessionClosedEvent:`

    Returned after the Live session finishes finalizing, with the close reason, final session snapshot, and cumulative audio usage. A connection closing without this event does not confirm successful finalization.

    - `String eventId`

      The unique ID of the Live server event.

    - `Reason reason`

      Why the Live session ended: `close_requested` for an application close or hangup request, `expired` for the session duration limit, `content` for a safety filter, `remote_hangup` for a graceful remote disconnect, or `connection_lost` for an unexpected primary or upstream disconnection.

      - `CLOSE_REQUESTED("close_requested")`

      - `EXPIRED("expired")`

      - `CONTENT("content")`

      - `REMOTE_HANGUP("remote_hangup")`

      - `CONNECTION_LOST("connection_lost")`

    - `SessionResource session`

      The resolved Live session configuration and server-assigned session metadata.

    - `JsonValue; type "session.closed"constant`

      The event type, always `session.closed`.

      - `SESSION_CLOSED("session.closed")`

    - `SessionUsage usage`

      The final cumulative Live audio usage after session finalization.

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class ErrorEvent:`

    Reports an error in the Live session, such as an invalid client command. Use error.client_event_id, when present, to identify the command that caused the error.

    - `Error error`

      Details of the Live error and the client command that caused it, when known.

      - `String code`

        A machine-readable code identifying the Live error, such as `unknown_parameter`.

      - `String message`

        A human-readable explanation of the Live error.

      - `String type`

        The category of error, such as `invalid_request_error` for an invalid Live client command.

      - `Optional<String> clientEventId`

        The event_id of the client command that caused the error, when supplied.

      - `Optional<String> param`

        The parameter that caused the error, when applicable, such as `session.voice`.

    - `String eventId`

      The unique ID of the Live server event.

    - `JsonValue; type "error"constant`

      The event type, always `error`.

      - `ERROR("error")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `class InfoEvent:`

    An informational notice about the Live session, such as the event permissions applied to a frontend data channel.

    - `String code`

      A machine-readable code for the notice, such as `data_channel_permissions`.

    - `String eventId`

      The unique ID of the Live server event.

    - `String message`

      A human-readable explanation of the Live session notice.

    - `JsonValue; type "info"constant`

      The event type, always `info`.

      - `INFO("info")`

    - `Optional<String> clientEventId`

      The event_id of the client command associated with this server event, when supplied.

  - `TransportDtmfReceived`

    - `String event`

    - `String eventId`

    - `JsonValue; type "transport.dtmf.received"constant`

      - `TRANSPORT_DTMF_RECEIVED("transport.dtmf.received")`

  - `TransportDtmfSend`

    - `String event`

    - `String eventId`

    - `JsonValue; type "transport.dtmf.send"constant`

      - `TRANSPORT_DTMF_SEND("transport.dtmf.send")`

    - `Optional<String> clientEventId`

      The event_id of the client command, when supplied.

  - `TransportRinging`

    - `String eventId`

    - `String sessionId`

      The canonical Live session ID.

    - `JsonValue; type "transport.ringing"constant`

      - `TRANSPORT_RINGING("transport.ringing")`

  - `TransportAnswered`

    - `String eventId`

    - `String sessionId`

      The canonical Live session ID.

    - `JsonValue; type "transport.answered"constant`

      - `TRANSPORT_ANSWERED("transport.answered")`

  - `TransportFailed`

    - `Error error`

      - `String code`

        The call setup failure code.

      - `String message`

      - `JsonValue; type "call_error"constant`

        - `CALL_ERROR("call_error")`

      - `Optional<String> param`

        The parameter related to the error, if any. Empty when no parameter applies.

    - `String eventId`

    - `String sessionId`

      The canonical Live session ID.

    - `JsonValue; type "transport.failed"constant`

      - `TRANSPORT_FAILED("transport.failed")`

# Sessions

## Accept call

`live().sessions().accept(SessionAcceptParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/live/sessions/{session_id}/accept`

Accept an incoming SIP call. Supply session with type live, the model, and startup configuration. Before accepting calls, follow the [Live prompting guide](/api/docs/guides/live-prompting) to write frontend conversation instructions and a separate backend prompt. SIP media format is negotiated; omit audio.format.

### Parameters

- `SessionAcceptParams params`

  - `Optional<String> sessionId`

  - `Session session`

    Model and startup configuration for the Live session that answers the incoming SIP call.

    - `Model model`

      The Live model to use for the accepted call.

      - `GPT_LIVE_1("gpt-live-1")`

    - `JsonValue; type "live"constant`

      The session type. Always `live`.

      - `LIVE("live")`

    - `Optional<Audio> audio`

      Startup audio output configuration. SIP negotiates the media format; audio.format is only accepted for primary WebSockets. Voice cannot change after startup.

      - `Optional<Output> output`

        Settings for speech generated by the Live model. Choose the voice before starting the session.

        - `Optional<Voice> voice`

          The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

          - `String`

          - `enum BuiltInVoice:`

            A built-in voice available for Live speech.

            - `ALLOY("alloy")`

            - `ASH("ash")`

            - `BALLAD("ballad")`

            - `BEACON("beacon")`

            - `BOSSA("bossa")`

            - `CEDAR("cedar")`

            - `CINDER("cinder")`

            - `CORAL("coral")`

            - `DELTA("delta")`

            - `ECHO("echo")`

            - `GLEAM("gleam")`

            - `MARIN("marin")`

            - `MERIDIAN("meridian")`

            - `QUARTZ("quartz")`

            - `RIPPLE("ripple")`

            - `SAGE("sage")`

            - `SHIMMER("shimmer")`

            - `STONE("stone")`

            - `TEMPO("tempo")`

            - `VERSE("verse")`

            - `VESPER("vesper")`

            - `WILLOW("willow")`

          - `class CustomVoice:`

            - `String id`

    - `Optional<Delegation> delegation`

      Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

      - `class ClientDelegation:`

        Delegate tasks to your application. The Live session emits delegation events that your backend handles.

        - `JsonValue; type "client"constant`

          The delegation owner. Always `client` for tasks handled by your application.

          - `CLIENT("client")`

      - `class Responses:`

        Delegate tasks to a Responses model managed by the Live session.

        - `ResponsesDelegationConfig responses`

          Backend model, prompt, and tools used when the Live session delegates a task to Responses.

          - `String model`

            The model used for server-owned Responses delegations.

          - `Optional<String> instructions`

            Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

          - `Optional<Long> maxOutputTokens`

            Maximum number of output tokens for each delegated response.

          - `Optional<Boolean> parallelToolCalls`

            Whether the delegated Responses model may request multiple tool calls in a single response.

          - `Optional<Reasoning> reasoning`

            Reasoning settings passed to each delegated Responses request.

            - `Optional<Effort> effort`

              How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

              - `NONE("none")`

              - `MINIMAL("minimal")`

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

              - `XHIGH("xhigh")`

            - `Optional<Summary> summary`

              The reasoning summary to request from the delegated Responses model, when supported.

              - `CONCISE("concise")`

              - `DETAILED("detailed")`

              - `AUTO("auto")`

          - `Optional<ServiceTier> serviceTier`

            Service tier for delegated Responses requests.

            - `AUTO("auto")`

            - `DEFAULT("default")`

            - `FAST_TIER_TEMP_PILOT("fast_tier_temp_pilot")`

            - `FLEX("flex")`

            - `PRIORITY("priority")`

            - `ULTRAFAST("ultrafast")`

          - `Optional<Text> text`

            Text generation settings passed to each delegated Responses request.

            - `Optional<Verbosity> verbosity`

              The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

          - `Optional<ToolChoice> toolChoice`

            Controls which tool the Responses backend uses when handling a task delegated by the Live model.

            - `enum LiveToolChoiceEnum:`

              - `AUTO("auto")`

              - `NONE("none")`

              - `REQUIRED("required")`

            - `class LiveFunctionToolChoiceParam:`

              - `String name`

              - `JsonValue; type "function"constant`

                - `FUNCTION("function")`

            - `class LiveMcpToolChoiceParam:`

              - `String name`

              - `String serverLabel`

              - `JsonValue; type "mcp"constant`

                - `MCP("mcp")`

          - `Optional<List<Tool>> tools`

            Tools available to the Responses backend while it handles tasks delegated by the Live model.

            - `class FunctionTool:`

              A function tool available to the Responses backend when the Live model delegates a task.

              - `String name`

                The name the delegated Responses model uses when calling this function.

              - `JsonValue; type "function"constant`

                The tool type. Always `function`.

                - `FUNCTION("function")`

              - `Optional<String> description`

                What the function does and when the delegated Responses model should call it.

              - `Optional<Parameters> parameters`

                A JSON Schema object describing the arguments accepted by the function.

              - `Optional<Boolean> strict`

                Whether the delegated Responses model must follow the function’s parameter schema exactly.

            - `JsonValue;`

              - `JsonValue; type "web_search"constant`

                The tool type. Always `web_search`.

                - `WEB_SEARCH("web_search")`

        - `JsonValue; type "responses"constant`

          The delegation owner. Always `responses` for tasks handled by the Responses API.

          - `RESPONSES("responses")`

    - `Optional<List<InitialItem>> input`

      Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

      - `Developer`

        - `List<Content> content`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `String text`

            The message text to include in the Live session’s initial conversation history.

          - `Optional<Type> type`

            The text content type. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `JsonValue; role "developer"constant`

          The author of this history message. Always `developer`.

          - `DEVELOPER("developer")`

        - `Optional<String> id`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Optional<Status> status`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `INCOMPLETE("incomplete")`

          - `COMPLETED("completed")`

        - `Optional<Type> type`

          The history item type. Always `message`.

          - `MESSAGE("message")`

      - `User`

        - `List<Content> content`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `String text`

            The message text to include in the Live session’s initial conversation history.

          - `Optional<Type> type`

            The text content type. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `JsonValue; role "user"constant`

          The author of this history message. Always `user`.

          - `USER("user")`

        - `Optional<String> id`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Optional<Status> status`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `INCOMPLETE("incomplete")`

          - `COMPLETED("completed")`

        - `Optional<Type> type`

          The history item type. Always `message`.

          - `MESSAGE("message")`

      - `Assistant`

        - `List<Content> content`

          The message content. Supply exactly one text part for the initial Live conversation history.

          - `class Text:`

            Assistant text supplied as conversation history when starting a Live session.

            - `String text`

              The message text to include in the Live session’s initial conversation history.

            - `Optional<Type> type`

              The text content type. Always `text`.

              - `TEXT("text")`

          - `class OutputText:`

            Assistant output text supplied as conversation history when starting a Live session.

            - `String text`

              The message text to include in the Live session’s initial conversation history.

            - `JsonValue; type "output_text"constant`

              The text content type. Always `output_text`.

              - `OUTPUT_TEXT("output_text")`

        - `JsonValue; role "assistant"constant`

          The author of this history message. Always `assistant`.

          - `ASSISTANT("assistant")`

        - `Optional<String> id`

          An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

        - `Optional<Status> status`

          The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

          - `INCOMPLETE("incomplete")`

          - `COMPLETED("completed")`

        - `Optional<Type> type`

          The history item type. Always `message`.

          - `MESSAGE("message")`

    - `Optional<String> instructions`

      Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

    - `Optional<Boolean> store`

      Whether to store the session for later forking and recording download. Defaults to false for new sessions.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.live.sessions.SessionAcceptParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SessionAcceptParams params = SessionAcceptParams.builder()
            .sessionId("session_id")
            .session(SessionAcceptParams.Session.builder()
                .model(SessionAcceptParams.Session.Model.GPT_LIVE_1)
                .build())
            .build();
        client.live().sessions().accept(params);
    }
}
```

## Download recording

`HttpResponse live().sessions().downloadRecording(SessionDownloadRecordingParamsparams = SessionDownloadRecordingParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/live/sessions/{session_id}/content`

Get Live session content

### Parameters

- `SessionDownloadRecordingParams params`

  - `Optional<String> sessionId`

    The ID of the stored Live session to download. Use the session ID returned when the session started with storage enabled.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.http.HttpResponse;
import com.openai.models.live.sessions.SessionDownloadRecordingParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        HttpResponse response = client.live().sessions().downloadRecording("live_SQ");
    }
}
```

## Fork session

`SessionForkResponse live().sessions().fork(SessionForkParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/live/sessions/{session_id}/fork`

Fork a stored Live session onto a new WebRTC connection.

### Parameters

- `SessionForkParams params`

  - `Optional<String> sessionId`

  - `Transport transport`

    WebRTC transport with an SDP offer for the new connection to the forked session.

    - `String sdp`

      Session Description Protocol message for the WebRTC connection.

    - `JsonValue; type "webrtc"constant`

      The transport used for the Live session. Always `webrtc`.

      - `WEBRTC("webrtc")`

  - `Optional<MediaSessionForkConfig> session`

    Optional configuration overrides for the new Live session. Omit this object or send an empty object to inherit the stored session's settings.

### Returns

- `class SessionForkResponse:`

  The created Live session identifier and WebRTC answer. Apply transport.sdp as the peer's remote answer and wait for session.started on the data channel before sending commands.

  - `Session session`

    The newly created Live session. Use its ID for session controls and sideband connections.

    - `String id`

      Opaque session identifier. Preserve the returned value unchanged, including its prefix.

  - `Transport transport`

    WebRTC transport with the SDP answer.

    - `String sdp`

      Session Description Protocol message for the WebRTC connection.

    - `JsonValue; type "webrtc"constant`

      The transport used for the Live session. Always `webrtc`.

      - `WEBRTC("webrtc")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.live.sessions.SessionForkParams;
import com.openai.models.live.sessions.SessionForkResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SessionForkParams params = SessionForkParams.builder()
            .sessionId("session_id")
            .transport(SessionForkParams.Transport.builder()
                .sdp("x")
                .build())
            .build();
        SessionForkResponse response = client.live().sessions().fork(params);
    }
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

`live().sessions().hangup(SessionHangupParamsparams = SessionHangupParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/live/sessions/{session_id}/hangup`

End a SIP call identified by session_id.

### Parameters

- `SessionHangupParams params`

  - `Optional<String> sessionId`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.live.sessions.SessionHangupParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        client.live().sessions().hangup("session_id");
    }
}
```

## Transfer call

`live().sessions().refer(SessionReferParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/live/sessions/{session_id}/refer`

Transfer a SIP call to another destination. Supply a nonblank target_uri for the SIP Refer-To header.

### Parameters

- `SessionReferParams params`

  - `Optional<String> sessionId`

  - `String targetUri`

    Nonblank URI for the SIP Refer-To header, such as tel:+14155550123 or sip:agent@example.com.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.live.sessions.SessionReferParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SessionReferParams params = SessionReferParams.builder()
            .sessionId("session_id")
            .targetUri("tel:+14155550123")
            .build();
        client.live().sessions().refer(params);
    }
}
```

## Reject call

`live().sessions().reject(SessionRejectParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/live/sessions/{session_id}/reject`

Reject an incoming SIP call. Send a required SIP rejection status_code between 300 and 699.

### Parameters

- `SessionRejectParams params`

  - `Optional<String> sessionId`

  - `long statusCode`

    SIP rejection status sent to the caller. This field is required.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.live.sessions.SessionRejectParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SessionRejectParams params = SessionRejectParams.builder()
            .sessionId("session_id")
            .statusCode(486L)
            .build();
        client.live().sessions().reject(params);
    }
}
```

# Sideband

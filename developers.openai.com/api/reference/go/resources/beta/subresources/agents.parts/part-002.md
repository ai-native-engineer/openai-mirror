<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/ -->
<!-- part of: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/ -->

<!-- chunk-start -->

      - `const FunctionCallOutputFunctionCallOutput FunctionCallOutput = "function_call_output"`

  - `type AgentSessionItemAgentMessage struct{…}`

    A message exchanged between agent threads.

    - `ID string`

      The ID of the message.

    - `Content []AgentContentUnion`

      The content exchanged between the agents.

      - `type OutputText struct{…}`

        A text content part produced by the agent.

        - `Text string`

          The text produced by the agent.

        - `Type OutputText`

          The content type. Always `output_text`.

          - `const OutputTextOutputText OutputText = "output_text"`

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

        - `EncryptedContent string`

          The encrypted content payload.

        - `Type EncryptedContent`

          The content type. Always `encrypted_content`.

          - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

    - `RecipientAgentID string`

      The ID or name of the receiving agent.

    - `SenderAgentID string`

      The ID or name of the sending agent.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type AgentMessage`

      The item type. Always `agent_message`.

      - `const AgentMessageAgentMessage AgentMessage = "agent_message"`

  - `type AgentMcpCallItem struct{…}`

    A call to a tool on an MCP server.

    - `ID string`

      The ID of the MCP call item.

    - `Arguments any`

      The arguments passed to the MCP tool.

    - `Error any`

      The error returned by the MCP tool, if any.

    - `Name string`

      The name of the MCP tool.

    - `Output any`

      The output returned by the MCP tool, if any.

    - `ServerLabel string`

      The label of the MCP server.

    - `Status AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type McpCall`

      The item type. Always `mcp_call`.

      - `const McpCallMcpCall McpCall = "mcp_call"`

  - `type AgentSessionItemComputerUseCall struct{…}`

    One execution of the platform-provided computer-use capability.

    - `ID string`

      The ID of the activity item.

    - `Output AgentSessionItemComputerUseCallOutput`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `ImageURL string`

        The complete JPEG image as a base64 data URL.

      - `Type ComputerScreenshot`

        The content type. Always `computer_screenshot`.

        - `const ComputerScreenshotComputerScreenshot ComputerScreenshot = "computer_screenshot"`

    - `Status AgentFunctionCallStatus`

      The execution status of the activity.

    - `Title string`

      A model-generated description of the activity, when available.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type ComputerUseCall`

      The item type. Always `computer_use_call`.

      - `const ComputerUseCallComputerUseCall ComputerUseCall = "computer_use_call"`

  - `type AgentSessionItemComputerUseApprovalRequest struct{…}`

    A credential-free history record of the emitted login request.

    - `ID string`

      The stable history item ID.

    - `Request AgentSessionItemComputerUseApprovalRequestRequest`

      A registered form awaiting the application's response.

      - `CredentialOrigin string`

        The registered form or frame origin where values will be entered.

      - `Fields []AgentSessionItemComputerUseApprovalRequestRequestField`

        Controls to render. All submitted values are sensitive.

        - `ID string`

          The field ID to submit as field_id in a fields entry.

        - `Label string`

          The label to display beside the control.

        - `Required bool`

          Whether this control requires a nonempty value.

        - `Type string`

          The rendering type, such as email, password, or text.

      - `Options []AgentSessionItemComputerUseApprovalRequestRequestOption`

        Sign-in methods. Empty for a plain form.

        - `ID string`

          The option ID to submit as selected_option.

        - `FieldIDs []string`

          IDs from the registered fields that this method accepts.

        - `Label string`

          The method label to display.

      - `Reason string`

        Why the agent needs the user to sign in.

      - `Type BrowserAuthentication`

        The type of the object. Always `browser_authentication`.

        - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

    - `RequestID string`

    - `TurnID string`

    - `Type ComputerUseApprovalRequest`

      The item type. Always computer_use_approval_request.

      - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

  - `type AgentSessionItemComputerUseApprovalRequestResult struct{…}`

    A credential-free record of an admitted response, not proof of completion.

    - `ID string`

      The stable history item ID.

    - `RequestID string`

      The registered request answered by this item.

    - `Response AgentSessionItemComputerUseApprovalRequestResultResponseUnion`

      The admitted response, without submitted credential values.

      - `type AgentSessionItemComputerUseApprovalRequestResultResponseSubmit struct{…}`

        - `Action Submit`

          - `const SubmitSubmit Submit = "submit"`

        - `SelectedOption string`

          The chosen sign-in method, or null when no options were offered.

        - `Type BrowserAuthentication`

          - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

      - `type AgentSessionItemComputerUseApprovalRequestResultResponseCancel struct{…}`

        - `Action Cancel`

          - `const CancelCancel Cancel = "cancel"`

        - `Type BrowserAuthentication`

          - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type ComputerUseApprovalRequestResult`

      - `const ComputerUseApprovalRequestResultComputerUseApprovalRequestResult ComputerUseApprovalRequestResult = "computer_use_approval_request_result"`

  - `type AgentWebSearchCallItem struct{…}`

    A web search call produced by the agent.

    - `ID string`

      The ID of the web search call.

    - `Action WebSearchActionUnion`

      The action performed by the web search tool.

      - `type WebSearchActionSearch struct{…}`

        A search query or group of search queries.

        - `Queries []string`

          The search queries, when multiple queries were used.

        - `Query string`

          The search query, when a single query was used.

        - `Type Search`

          The type of the object. Always `search`.

          - `const SearchSearch Search = "search"`

      - `type WebSearchActionOpenPage struct{…}`

        Opens a web page.

        - `Type OpenPage`

          The type of the object. Always `open_page`.

          - `const OpenPageOpenPage OpenPage = "open_page"`

        - `URL string`

          The URL of the page that was opened.

      - `type WebSearchActionFindInPage struct{…}`

        Finds text within a web page.

        - `Pattern string`

          The text pattern that was searched for.

        - `Type FindInPage`

          The type of the object. Always `find_in_page`.

          - `const FindInPageFindInPage FindInPage = "find_in_page"`

        - `URL string`

          The URL of the page that was searched.

      - `type WebSearchActionOther struct{…}`

        Another web search action.

        - `Type Other`

          The type of the object. Always `other`.

          - `const OtherOther Other = "other"`

    - `Status AgentOutputItemStatus`

      The status of the web search call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type WebSearchCall`

      The item type. Always `web_search_call`.

      - `const WebSearchCallWebSearchCall WebSearchCall = "web_search_call"`

  - `type AgentCommandExecutionItem struct{…}`

    A command execution produced by the agent.

    - `ID string`

      The ID of the command execution item.

    - `Command string`

      The command that was executed.

    - `Cwd string`

      The working directory used to execute the command.

    - `DurationMs int64`

      The command duration in milliseconds.

    - `ExitCode int64`

      The process exit code, if the command completed.

    - `Output string`

      The command output, if available.

    - `Status AgentFunctionCallStatus`

      The status of the command execution.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type CommandExecution`

      The item type. Always `command_execution`.

      - `const CommandExecutionCommandExecution CommandExecution = "command_execution"`

  - `type AgentCreateSubagentCallItem struct{…}`

    A request to spawn a subagent.

    - `ID string`

      The ID of the tool call item.

    - `AgentID string`

      The ID of the agent that requested the subagent.

    - `Content []AgentContentUnion`

      The task given to the spawned agent.

      - `type OutputText struct{…}`

        A text content part produced by the agent.

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

    - `Model string`

      The model requested for the spawned agent.

    - `ReasoningEffort string`

      The reasoning effort requested for the spawned agent.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type CreateSubagentCall`

      The item type. Always `create_subagent_call`.

      - `const CreateSubagentCallCreateSubagentCall CreateSubagentCall = "create_subagent_call"`

        The current public item type.

  - `type AgentSendSubagentInputCallItem struct{…}`

    A request to send input to another agent.

    - `ID string`

      The ID of the tool call item.

    - `Content []AgentContentUnion`

      The input sent to the receiving agent.

      - `type OutputText struct{…}`

        A text content part produced by the agent.

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

    - `RecipientAgentID string`

      The ID of the agent receiving the input.

    - `SenderAgentID string`

      The ID of the agent sending the input.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type SendSubagentInputCall`

      The item type. Always `send_subagent_input_call`.

      - `const SendSubagentInputCallSendSubagentInputCall SendSubagentInputCall = "send_subagent_input_call"`

        The current public item type.

  - `type AgentResumeSubagentCallItem struct{…}`

    A request to resume a subagent.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentID string`

      The ID of the agent to resume.

    - `SenderAgentID string`

      The ID of the agent requesting the resume.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type ResumeSubagentCall`

      The item type. Always `resume_subagent_call`.

      - `const ResumeSubagentCallResumeSubagentCall ResumeSubagentCall = "resume_subagent_call"`

        The current public item type.

  - `type AgentWaitForSubagentsCallItem struct{…}`

    A request to wait for one or more subagents.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentIDs []string`

      The IDs of the agents to wait for.

    - `SenderAgentID string`

      The ID of the agent waiting for results.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type WaitForSubagentsCall`

      The item type. Always `wait_for_subagents_call`.

      - `const WaitForSubagentsCallWaitForSubagentsCall WaitForSubagentsCall = "wait_for_subagents_call"`

        The current public item type.

  - `type AgentInterruptSubagentCallItem struct{…}`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentID string`

      The ID of the agent to interrupt.

    - `SenderAgentID string`

      The ID of the agent requesting the interrupt.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type InterruptSubagentCall`

      The item type. Always `interrupt_subagent_call`.

      - `const InterruptSubagentCallInterruptSubagentCall InterruptSubagentCall = "interrupt_subagent_call"`

        The current public item type.

  - `type AgentCloseSubagentCallItem struct{…}`

    A request to close a subagent.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentID string`

      The ID of the agent to close.

    - `SenderAgentID string`

      The ID of the agent requesting the close.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type CloseSubagentCall`

      The item type. Always `close_subagent_call`.

      - `const CloseSubagentCallCloseSubagentCall CloseSubagentCall = "close_subagent_call"`

        The current public item type.

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
  page, err := client.Beta.Agents.Sessions.Items.List(
    context.TODO(),
    "session_id",
    openai.BetaAgentSessionItemListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "content": [
        {
          "text": "text",
          "type": "input_text"
        }
      ],
      "phase": "commentary",
      "role": "user",
      "status": "in_progress",
      "turn_id": "turn_id",
      "type": "message"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

# Subagents

## List session subagents

`client.Beta.Agents.Sessions.Subagents.List(ctx, sessionID, query) (*CursorPage[Subagent], error)`

**get** `/agents/sessions/{session_id}/subagents`

Lists subagents in a session, including nested and closed subagents. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `sessionID string`

- `query BetaAgentSessionSubagentListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `Limit param.Field[int64]`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Order param.Field[BetaAgentSessionSubagentListParamsOrder]`

    The order in which resources are returned. Defaults to `desc`.

    - `const BetaAgentSessionSubagentListParamsOrderAsc BetaAgentSessionSubagentListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentSessionSubagentListParamsOrderDesc BetaAgentSessionSubagentListParamsOrder = "desc"`

      Returns resources in descending order.

### Returns

- `type Subagent struct{…}`

  A subagent created within a session.

  - `ID string`

    The ID of the subagent.

  - `ClosedAt int64`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `Instructions []AgentContentUnion`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `type OutputText struct{…}`

      A text content part produced by the agent.

      - `Text string`

        The text produced by the agent.

      - `Type OutputText`

        The content type. Always `output_text`.

        - `const OutputTextOutputText OutputText = "output_text"`

    - `type AgentContentEncryptedContent struct{…}`

      Encrypted content exchanged between agents.

      - `EncryptedContent string`

        The encrypted content payload.

      - `Type EncryptedContent`

        The content type. Always `encrypted_content`.

        - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

  - `Name string`

    The runner-assigned nickname, or null when unavailable.

  - `Object SubagentObject`

    The object type. Always `agent.session.subagent`.

    - `const SubagentObjectAgentSessionSubagent SubagentObject = "agent.session.subagent"`

  - `OpenedAt int64`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `ParentAgentID string`

    The ID of the agent that created this subagent.

  - `SessionID string`

    The ID of the session that owns the subagent.

  - `Status SubagentStatus`

    The current status of the subagent.

    - `const SubagentStatusActive SubagentStatus = "active"`

      The subagent remains available, including while idle between turns.

    - `const SubagentStatusClosed SubagentStatus = "closed"`

      The subagent is closed.

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
  page, err := client.Beta.Agents.Sessions.Subagents.List(
    context.TODO(),
    "session_id",
    openai.BetaAgentSessionSubagentListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "closed_at": 0,
      "instructions": [
        {
          "text": "text",
          "type": "output_text"
        }
      ],
      "name": "name",
      "object": "agent.session.subagent",
      "opened_at": 0,
      "parent_agent_id": "parent_agent_id",
      "session_id": "session_id",
      "status": "active"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve a session subagent

`client.Beta.Agents.Sessions.Subagents.Get(ctx, sessionID, subagentID) (*Subagent, error)`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}`

Retrieves a subagent belonging to this session. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `sessionID string`

- `subagentID string`

### Returns

- `type Subagent struct{…}`

  A subagent created within a session.

  - `ID string`

    The ID of the subagent.

  - `ClosedAt int64`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `Instructions []AgentContentUnion`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `type OutputText struct{…}`

      A text content part produced by the agent.

      - `Text string`

        The text produced by the agent.

      - `Type OutputText`

        The content type. Always `output_text`.

        - `const OutputTextOutputText OutputText = "output_text"`

    - `type AgentContentEncryptedContent struct{…}`

      Encrypted content exchanged between agents.

      - `EncryptedContent string`

        The encrypted content payload.

      - `Type EncryptedContent`

        The content type. Always `encrypted_content`.

        - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

  - `Name string`

    The runner-assigned nickname, or null when unavailable.

  - `Object SubagentObject`

    The object type. Always `agent.session.subagent`.

    - `const SubagentObjectAgentSessionSubagent SubagentObject = "agent.session.subagent"`

  - `OpenedAt int64`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `ParentAgentID string`

    The ID of the agent that created this subagent.

  - `SessionID string`

    The ID of the session that owns the subagent.

  - `Status SubagentStatus`

    The current status of the subagent.

    - `const SubagentStatusActive SubagentStatus = "active"`

      The subagent remains available, including while idle between turns.

    - `const SubagentStatusClosed SubagentStatus = "closed"`

      The subagent is closed.

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
  subagent, err := client.Beta.Agents.Sessions.Subagents.Get(
    context.TODO(),
    "session_id",
    "subagent_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", subagent.ID)
}
```

#### Response

```json
{
  "id": "id",
  "closed_at": 0,
  "instructions": [
    {
      "text": "text",
      "type": "output_text"
    }
  ],
  "name": "name",
  "object": "agent.session.subagent",
  "opened_at": 0,
  "parent_agent_id": "parent_agent_id",
  "session_id": "session_id",
  "status": "active"
}
```

# Items

## List subagent items

`client.Beta.Agents.Sessions.Subagents.Items.List(ctx, sessionID, subagentID, query) (*CursorPage[AgentSessionItemUnion], error)`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/items`

Lists this subagent's own items across all of its turns. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `sessionID string`

- `subagentID string`

- `query BetaAgentSessionSubagentItemListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `Limit param.Field[int64]`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Order param.Field[BetaAgentSessionSubagentItemListParamsOrder]`

    The order in which resources are returned. Defaults to `desc`.

    - `const BetaAgentSessionSubagentItemListParamsOrderAsc BetaAgentSessionSubagentItemListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentSessionSubagentItemListParamsOrderDesc BetaAgentSessionSubagentItemListParamsOrder = "desc"`

      Returns resources in descending order.

### Returns

- `type AgentSessionItemUnion interface{…}`

  An item associated with a session turn.

  - `type AgentSessionMessage struct{…}`

    A user or assistant message recorded in a session.

    - `ID string`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `Content []AgentSessionMessageContentUnion`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `type AgentSessionMessageContentInputText struct{…}`

        Text supplied by the user.

        - `Text string`

          The text supplied by the user.

        - `Type InputText`

          The type of the object. Always `input_text`.

          - `const InputTextInputText InputText = "input_text"`

      - `type AgentSessionMessageContentInputImage struct{…}`

        An image supplied by the user.

        - `ImageURL string`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `Type InputImage`

          The type of the object. Always `input_image`.

          - `const InputImageInputImage InputImage = "input_image"`

      - `type AgentSessionMessageContentOutputText struct{…}`

        Text produced by the assistant.

        - `Text string`

          The text produced by the assistant.

        - `Type OutputText`

          The type of the object. Always `output_text`.

          - `const OutputTextOutputText OutputText = "output_text"`

    - `Phase AgentSessionMessagePhase`

      The phase of an assistant message. Null for user messages.

      - `const AgentSessionMessagePhaseCommentary AgentSessionMessagePhase = "commentary"`

        Commentary produced while the agent works.

      - `const AgentSessionMessagePhaseFinalAnswer AgentSessionMessagePhase = "final_answer"`

        The agent's final answer.

    - `Role AgentSessionMessageRole`

      The role of the message author.

      - `const AgentSessionMessageRoleUser AgentSessionMessageRole = "user"`

      - `const AgentSessionMessageRoleAssistant AgentSessionMessageRole = "assistant"`

    - `Status AgentOutputItemStatus`

      The status of the message. User messages are always `completed`.

      - `const AgentOutputItemStatusInProgress AgentOutputItemStatus = "in_progress"`

        The item is in progress.

      - `const AgentOutputItemStatusCompleted AgentOutputItemStatus = "completed"`

        The item is complete.

      - `const AgentOutputItemStatusIncomplete AgentOutputItemStatus = "incomplete"`

        The item stopped before completing.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type Message`

      The item type. Always `message`.

      - `const MessageMessage Message = "message"`

  - `type AgentReasoningItem struct{…}`

    A reasoning item produced by the agent.

    - `ID string`

      The ID of the reasoning item.

    - `Status AgentOutputItemStatus`

      The status of the reasoning item.

    - `Summary []SummaryText`

      The reasoning summaries produced by the agent.

      - `Text string`

        The reasoning summary text.

      - `Type SummaryText`

        The content type. Always `summary_text`.

        - `const SummaryTextSummaryText SummaryText = "summary_text"`

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type Reasoning`

      The item type. Always `reasoning`.

      - `const ReasoningReasoning Reasoning = "reasoning"`

  - `type AgentFunctionCallItem struct{…}`

    A function call produced by the agent.

    - `ID string`

      The ID of the function call item.

    - `Arguments any`

      The arguments to pass to the function.

    - `CallID string`

      The ID used to submit the function result.

    - `Name string`

      The name of the function to call.

    - `Status AgentFunctionCallStatus`

      The status of the function call.

      - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

        The call is in progress.

      - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

        The call completed successfully.

      - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

        The call failed.

      - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

        The call stopped before completing.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type FunctionCall`

      The item type. Always `function_call`.

      - `const FunctionCallFunctionCall FunctionCall = "function_call"`

  - `type AgentSessionItemFunctionCallOutput struct{…}`

    The result supplied for a function call.

    - `ID string`

      The ID of the function call output item.

    - `CallID string`

      The ID of the function call that produced this output.

    - `Error string`

      The error message, if the call failed.

    - `Output AgentFunctionCallOutputUnion`

      The function result, if the call succeeded.

      - `string`

      - `type AgentFunctionCallOutputArray []InputContentUnion`

        - `type InputContentInputText struct{…}`

          Text input recorded in a session item.

          - `Text string`

            The text supplied to the agent.

          - `Type InputText`

            The type of the object. Always `input_text`.

            - `const InputTextInputText InputText = "input_text"`

        - `type InputContentInputImage struct{…}`

          Image input recorded in a session item.

          - `ImageURL string`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `Type InputImage`

            The type of the object. Always `input_image`.

            - `const InputImageInputImage InputImage = "input_image"`

    - `Status AgentFunctionCallStatus`

      The status of the function call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type FunctionCallOutput`

      The item type. Always `function_call_output`.

      - `const FunctionCallOutputFunctionCallOutput FunctionCallOutput = "function_call_output"`

  - `type AgentSessionItemAgentMessage struct{…}`

    A message exchanged between agent threads.

    - `ID string`

      The ID of the message.

    - `Content []AgentContentUnion`

      The content exchanged between the agents.

      - `type OutputText struct{…}`

        A text content part produced by the agent.

        - `Text string`

          The text produced by the agent.

        - `Type OutputText`

          The content type. Always `output_text`.

          - `const OutputTextOutputText OutputText = "output_text"`

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

        - `EncryptedContent string`

          The encrypted content payload.

        - `Type EncryptedContent`

          The content type. Always `encrypted_content`.

          - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

    - `RecipientAgentID string`

      The ID or name of the receiving agent.

    - `SenderAgentID string`

      The ID or name of the sending agent.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type AgentMessage`

      The item type. Always `agent_message`.

      - `const AgentMessageAgentMessage AgentMessage = "agent_message"`

  - `type AgentMcpCallItem struct{…}`

    A call to a tool on an MCP server.

    - `ID string`

      The ID of the MCP call item.

    - `Arguments any`

      The arguments passed to the MCP tool.

    - `Error any`

      The error returned by the MCP tool, if any.

    - `Name string`

      The name of the MCP tool.

    - `Output any`

      The output returned by the MCP tool, if any.

    - `ServerLabel string`

      The label of the MCP server.

    - `Status AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type McpCall`

      The item type. Always `mcp_call`.

      - `const McpCallMcpCall McpCall = "mcp_call"`

  - `type AgentSessionItemComputerUseCall struct{…}`

    One execution of the platform-provided computer-use capability.

    - `ID string`

      The ID of the activity item.

    - `Output AgentSessionItemComputerUseCallOutput`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `ImageURL string`

        The complete JPEG image as a base64 data URL.

      - `Type ComputerScreenshot`

        The content type. Always `computer_screenshot`.

        - `const ComputerScreenshotComputerScreenshot ComputerScreenshot = "computer_screenshot"`

    - `Status AgentFunctionCallStatus`

      The execution status of the activity.

    - `Title string`

      A model-generated description of the activity, when available.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type ComputerUseCall`

      The item type. Always `computer_use_call`.

      - `const ComputerUseCallComputerUseCall ComputerUseCall = "computer_use_call"`

  - `type AgentSessionItemComputerUseApprovalRequest struct{…}`

    A credential-free history record of the emitted login request.

    - `ID string`

      The stable history item ID.

    - `Request AgentSessionItemComputerUseApprovalRequestRequest`

      A registered form awaiting the application's response.

      - `CredentialOrigin string`

        The registered form or frame origin where values will be entered.

      - `Fields []AgentSessionItemComputerUseApprovalRequestRequestField`

        Controls to render. All submitted values are sensitive.

        - `ID string`

          The field ID to submit as field_id in a fields entry.

        - `Label string`

          The label to display beside the control.

        - `Required bool`

          Whether this control requires a nonempty value.

        - `Type string`

          The rendering type, such as email, password, or text.

      - `Options []AgentSessionItemComputerUseApprovalRequestRequestOption`

        Sign-in methods. Empty for a plain form.

        - `ID string`

          The option ID to submit as selected_option.

        - `FieldIDs []string`

          IDs from the registered fields that this method accepts.

        - `Label string`

          The method label to display.

      - `Reason string`

        Why the agent needs the user to sign in.

      - `Type BrowserAuthentication`

        The type of the object. Always `browser_authentication`.

        - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

    - `RequestID string`

    - `TurnID string`

    - `Type ComputerUseApprovalRequest`

      The item type. Always computer_use_approval_request.

      - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

  - `type AgentSessionItemComputerUseApprovalRequestResult struct{…}`

    A credential-free record of an admitted response, not proof of completion.

    - `ID string`

      The stable history item ID.

    - `RequestID string`

      The registered request answered by this item.

    - `Response AgentSessionItemComputerUseApprovalRequestResultResponseUnion`

      The admitted response, without submitted credential values.

      - `type AgentSessionItemComputerUseApprovalRequestResultResponseSubmit struct{…}`

        - `Action Submit`

          - `const SubmitSubmit Submit = "submit"`

        - `SelectedOption string`

          The chosen sign-in method, or null when no options were offered.

        - `Type BrowserAuthentication`

          - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

      - `type AgentSessionItemComputerUseApprovalRequestResultResponseCancel struct{…}`

        - `Action Cancel`

          - `const CancelCancel Cancel = "cancel"`

        - `Type BrowserAuthentication`

          - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type ComputerUseApprovalRequestResult`

      - `const ComputerUseApprovalRequestResultComputerUseApprovalRequestResult ComputerUseApprovalRequestResult = "computer_use_approval_request_result"`

  - `type AgentWebSearchCallItem struct{…}`

    A web search call produced by the agent.

    - `ID string`

      The ID of the web search call.

    - `Action WebSearchActionUnion`

      The action performed by the web search tool.

      - `type WebSearchActionSearch struct{…}`

        A search query or group of search queries.

        - `Queries []string`

          The search queries, when multiple queries were used.

        - `Query string`

          The search query, when a single query was used.

        - `Type Search`

          The type of the object. Always `search`.

          - `const SearchSearch Search = "search"`

      - `type WebSearchActionOpenPage struct{…}`

        Opens a web page.

        - `Type OpenPage`

          The type of the object. Always `open_page`.

          - `const OpenPageOpenPage OpenPage = "open_page"`

        - `URL string`

          The URL of the page that was opened.

      - `type WebSearchActionFindInPage struct{…}`

        Finds text within a web page.

        - `Pattern string`

          The text pattern that was searched for.

        - `Type FindInPage`

          The type of the object. Always `find_in_page`.

          - `const FindInPageFindInPage FindInPage = "find_in_page"`

        - `URL string`

          The URL of the page that was searched.

      - `type WebSearchActionOther struct{…}`

        Another web search action.

        - `Type Other`

          The type of the object. Always `other`.

          - `const OtherOther Other = "other"`

    - `Status AgentOutputItemStatus`

      The status of the web search call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type WebSearchCall`

      The item type. Always `web_search_call`.

      - `const WebSearchCallWebSearchCall WebSearchCall = "web_search_call"`

  - `type AgentCommandExecutionItem struct{…}`

    A command execution produced by the agent.

    - `ID string`

      The ID of the command execution item.

    - `Command string`

      The command that was executed.

    - `Cwd string`

      The working directory used to execute the command.

    - `DurationMs int64`

      The command duration in milliseconds.

    - `ExitCode int64`

      The process exit code, if the command completed.

    - `Output string`

      The command output, if available.

    - `Status AgentFunctionCallStatus`

      The status of the command execution.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type CommandExecution`

      The item type. Always `command_execution`.

      - `const CommandExecutionCommandExecution CommandExecution = "command_execution"`

  - `type AgentCreateSubagentCallItem struct{…}`

    A request to spawn a subagent.

    - `ID string`

      The ID of the tool call item.

    - `AgentID string`

      The ID of the agent that requested the subagent.

    - `Content []AgentContentUnion`

      The task given to the spawned agent.

      - `type OutputText struct{…}`

        A text content part produced by the agent.

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

    - `Model string`

      The model requested for the spawned agent.

    - `ReasoningEffort string`

      The reasoning effort requested for the spawned agent.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type CreateSubagentCall`

      The item type. Always `create_subagent_call`.

      - `const CreateSubagentCallCreateSubagentCall CreateSubagentCall = "create_subagent_call"`

        The current public item type.

  - `type AgentSendSubagentInputCallItem struct{…}`

    A request to send input to another agent.

    - `ID string`

      The ID of the tool call item.

    - `Content []AgentContentUnion`

      The input sent to the receiving agent.

      - `type OutputText struct{…}`

        A text content part produced by the agent.

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

    - `RecipientAgentID string`

      The ID of the agent receiving the input.

    - `SenderAgentID string`

      The ID of the agent sending the input.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type SendSubagentInputCall`

      The item type. Always `send_subagent_input_call`.

      - `const SendSubagentInputCallSendSubagentInputCall SendSubagentInputCall = "send_subagent_input_call"`

        The current public item type.

  - `type AgentResumeSubagentCallItem struct{…}`

    A request to resume a subagent.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentID string`

      The ID of the agent to resume.

    - `SenderAgentID string`

      The ID of the agent requesting the resume.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type ResumeSubagentCall`

      The item type. Always `resume_subagent_call`.

      - `const ResumeSubagentCallResumeSubagentCall ResumeSubagentCall = "resume_subagent_call"`

        The current public item type.

  - `type AgentWaitForSubagentsCallItem struct{…}`

    A request to wait for one or more subagents.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentIDs []string`

      The IDs of the agents to wait for.

    - `SenderAgentID string`

      The ID of the agent waiting for results.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type WaitForSubagentsCall`

      The item type. Always `wait_for_subagents_call`.

      - `const WaitForSubagentsCallWaitForSubagentsCall WaitForSubagentsCall = "wait_for_subagents_call"`

        The current public item type.

  - `type AgentInterruptSubagentCallItem struct{…}`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentID string`

      The ID of the agent to interrupt.

    - `SenderAgentID string`

      The ID of the agent requesting the interrupt.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type InterruptSubagentCall`

      The item type. Always `interrupt_subagent_call`.

      - `const InterruptSubagentCallInterruptSubagentCall InterruptSubagentCall = "interrupt_subagent_call"`

        The current public item type.

  - `type AgentCloseSubagentCallItem struct{…}`

    A request to close a subagent.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentID string`

      The ID of the agent to close.

    - `SenderAgentID string`

      The ID of the agent requesting the close.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type CloseSubagentCall`

      The item type. Always `close_subagent_call`.

      - `const CloseSubagentCallCloseSubagentCall CloseSubagentCall = "close_subagent_call"`

        The current public item type.

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
  page, err := client.Beta.Agents.Sessions.Subagents.Items.List(
    context.TODO(),
    "session_id",
    "subagent_id",
    openai.BetaAgentSessionSubagentItemListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "content": [
        {
          "text": "text",
          "type": "input_text"
        }
      ],
      "phase": "commentary",
      "role": "user",
      "status": "in_progress",
      "turn_id": "turn_id",
      "type": "message"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

# Turns

## List subagent turns

`client.Beta.Agents.Sessions.Subagents.Turns.List(ctx, sessionID, subagentID, query) (*CursorPage[Turn], error)`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns`

Lists all turns of this subagent, including turns after a resume. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `sessionID string`

- `subagentID string`

- `query BetaAgentSessionSubagentTurnListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `Limit param.Field[int64]`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Order param.Field[BetaAgentSessionSubagentTurnListParamsOrder]`

    The order in which resources are returned. Defaults to `desc`.

    - `const BetaAgentSessionSubagentTurnListParamsOrderAsc BetaAgentSessionSubagentTurnListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentSessionSubagentTurnListParamsOrderDesc BetaAgentSessionSubagentTurnListParamsOrder = "desc"`

      Returns resources in descending order.

### Returns

- `type Turn struct{…}`

  The canonical public representation of a session turn.

  - `ID string`

    The ID of the turn.

  - `AgentID string`

    The ID of the agent that ran the turn.

  - `CompletedAt int64`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `Error SessionTurnError`

    A customer-safe error. Non-null only for a failed turn.

    - `Code SessionTurnErrorCode`

      A stable, machine-readable failure category.

      - `const SessionTurnErrorCodeContextLengthExceeded SessionTurnErrorCode = "context_length_exceeded"`

        The request exceeds the model's context window.

      - `const SessionTurnErrorCodeSessionBudgetExceeded SessionTurnErrorCode = "session_budget_exceeded"`

        The session has reached its usage budget.

      - `const SessionTurnErrorCodeUsageLimitExceeded SessionTurnErrorCode = "usage_limit_exceeded"`

        The organization has reached a usage, plan, or billing limit.

      - `const SessionTurnErrorCodeCreditBalanceExhausted SessionTurnErrorCode = "credit_balance_exhausted"`

        The organization has no API credits remaining.

      - `const SessionTurnErrorCodeRateLimitExceeded SessionTurnErrorCode = "rate_limit_exceeded"`

        The request exceeds the available rate limit.

      - `const SessionTurnErrorCodeFlexUnavailable SessionTurnErrorCode = "flex_unavailable"`

        Flex processing is temporarily unavailable.

      - `const SessionTurnErrorCodeServerOverloaded SessionTurnErrorCode = "server_overloaded"`

        The model service is temporarily overloaded.

      - `const SessionTurnErrorCodeCyberPolicy SessionTurnErrorCode = "cyber_policy"`

        The request was rejected by a safety policy.

      - `const SessionTurnErrorCodeMisalignmentPolicyViolation SessionTurnErrorCode = "misalignment_policy_violation"`

        The request was blocked by the safety systems.

      - `const SessionTurnErrorCodeConnectionFailed SessionTurnErrorCode = "connection_failed"`

        The request could not connect to the model service.

      - `const SessionTurnErrorCodeServerError SessionTurnErrorCode = "server_error"`

        The model service encountered an unexpected error.

      - `const SessionTurnErrorCodeAuthenticationError SessionTurnErrorCode = "authentication_error"`

        The API credentials are invalid or lack the required access.

      - `const SessionTurnErrorCodeInvalidRequest SessionTurnErrorCode = "invalid_request"`

        The request contains invalid input or configuration.

      - `const SessionTurnErrorCodeResourceNotFound SessionTurnErrorCode = "resource_not_found"`

        The requested model or resource is unavailable.

      - `const SessionTurnErrorCodeSandboxError SessionTurnErrorCode = "sandbox_error"`

        The request could not complete in its execution environment.

      - `const SessionTurnErrorCodeExecutorVersionIncompatible SessionTurnErrorCode = "executor_version_incompatible"`

        The executor must be upgraded before it can run this turn.

      - `const SessionTurnErrorCodeActiveTurnNotSteerable SessionTurnErrorCode = "active_turn_not_steerable"`

        The session cannot accept additional input while a request is running.

      - `const SessionTurnErrorCodeRequestTimeout SessionTurnErrorCode = "request_timeout"`

        The request timed out before the model service responded.

      - `const SessionTurnErrorCodeInternalError SessionTurnErrorCode = "internal_error"`

        An unexpected internal error prevented the session request from completing.

    - `Message string`

      A customer-safe explanation of the failure.

  - `Object TurnObject`

    The object type. Always `agent.session.turn`.

    - `const TurnObjectAgentSessionTurn TurnObject = "agent.session.turn"`

  - `SessionID string`

    The ID of the session that owns the turn.

  - `StartedAt int64`

    The Unix timestamp, in seconds, when the turn started.

  - `Status TurnStatus`

    The current status of the turn.

    - `const TurnStatusQueued TurnStatus = "queued"`

      The turn is waiting to start.

    - `const TurnStatusInProgress TurnStatus = "in_progress"`

      The turn is in progress.

    - `const TurnStatusWaiting TurnStatus = "waiting"`

      The turn is waiting for external input.

    - `const TurnStatusCompleted TurnStatus = "completed"`

      The turn completed successfully.

    - `const TurnStatusFailed TurnStatus = "failed"`

      The turn failed.

    - `const TurnStatusCancelled TurnStatus = "cancelled"`

      The turn was cancelled.

  - `SubagentID string`

    The ID of the subagent that ran the turn, if applicable.

  - `Usage TokenUsage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `InputTokens int64`

      The number of input tokens used by the agent.

    - `InputTokensDetails TokenUsageInputTokensDetails`

      A breakdown of the agent's input token usage.

      - `CachedTokens int64`

        The number of input tokens retrieved from the prompt cache.

    - `OutputTokens int64`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails TokenUsageOutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `ReasoningTokens int64`

        The number of output tokens used for reasoning.

    - `TotalTokens int64`

      The total number of input and output tokens used by the agent.

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
  page, err := client.Beta.Agents.Sessions.Subagents.Turns.List(
    context.TODO(),
    "session_id",
    "subagent_id",
    openai.BetaAgentSessionSubagentTurnListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "agent_id": "agent_id",
      "completed_at": 0,
      "created_at": 0,
      "error": {
        "code": "context_length_exceeded",
        "message": "message"
      },
      "object": "agent.session.turn",
      "session_id": "session_id",
      "started_at": 0,
      "status": "queued",
      "subagent_id": "subagent_id",
      "usage": {
        "input_tokens": 0,
        "input_tokens_details": {
          "cached_tokens": 0
        },
        "output_tokens": 0,
        "output_tokens_details": {
          "reasoning_tokens": 0
        },
        "total_tokens": 0
      }
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve a subagent turn

`client.Beta.Agents.Sessions.Subagents.Turns.Get(ctx, sessionID, subagentID, turnID) (*Turn, error)`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns/{turn_id}`

Retrieves a turn belonging to this subagent. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `sessionID string`

- `subagentID string`

- `turnID string`

### Returns

- `type Turn struct{…}`

  The canonical public representation of a session turn.

  - `ID string`

    The ID of the turn.

  - `AgentID string`

    The ID of the agent that ran the turn.

  - `CompletedAt int64`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `Error SessionTurnError`

    A customer-safe error. Non-null only for a failed turn.

    - `Code SessionTurnErrorCode`

      A stable, machine-readable failure category.

      - `const SessionTurnErrorCodeContextLengthExceeded SessionTurnErrorCode = "context_length_exceeded"`

        The request exceeds the model's context window.

      - `const SessionTurnErrorCodeSessionBudgetExceeded SessionTurnErrorCode = "session_budget_exceeded"`

        The session has reached its usage budget.

      - `const SessionTurnErrorCodeUsageLimitExceeded SessionTurnErrorCode = "usage_limit_exceeded"`

        The organization has reached a usage, plan, or billing limit.

      - `const SessionTurnErrorCodeCreditBalanceExhausted SessionTurnErrorCode = "credit_balance_exhausted"`

        The organization has no API credits remaining.

      - `const SessionTurnErrorCodeRateLimitExceeded SessionTurnErrorCode = "rate_limit_exceeded"`

        The request exceeds the available rate limit.

      - `const SessionTurnErrorCodeFlexUnavailable SessionTurnErrorCode = "flex_unavailable"`

        Flex processing is temporarily unavailable.

      - `const SessionTurnErrorCodeServerOverloaded SessionTurnErrorCode = "server_overloaded"`

        The model service is temporarily overloaded.

      - `const SessionTurnErrorCodeCyberPolicy SessionTurnErrorCode = "cyber_policy"`

        The request was rejected by a safety policy.

      - `const SessionTurnErrorCodeMisalignmentPolicyViolation SessionTurnErrorCode = "misalignment_policy_violation"`

        The request was blocked by the safety systems.

      - `const SessionTurnErrorCodeConnectionFailed SessionTurnErrorCode = "connection_failed"`

        The request could not connect to the model service.

      - `const SessionTurnErrorCodeServerError SessionTurnErrorCode = "server_error"`

        The model service encountered an unexpected error.

      - `const SessionTurnErrorCodeAuthenticationError SessionTurnErrorCode = "authentication_error"`

        The API credentials are invalid or lack the required access.

      - `const SessionTurnErrorCodeInvalidRequest SessionTurnErrorCode = "invalid_request"`

        The request contains invalid input or configuration.

      - `const SessionTurnErrorCodeResourceNotFound SessionTurnErrorCode = "resource_not_found"`

        The requested model or resource is unavailable.

      - `const SessionTurnErrorCodeSandboxError SessionTurnErrorCode = "sandbox_error"`

        The request could not complete in its execution environment.

      - `const SessionTurnErrorCodeExecutorVersionIncompatible SessionTurnErrorCode = "executor_version_incompatible"`

        The executor must be upgraded before it can run this turn.

      - `const SessionTurnErrorCodeActiveTurnNotSteerable SessionTurnErrorCode = "active_turn_not_steerable"`

        The session cannot accept additional input while a request is running.

      - `const SessionTurnErrorCodeRequestTimeout SessionTurnErrorCode = "request_timeout"`

        The request timed out before the model service responded.

      - `const SessionTurnErrorCodeInternalError SessionTurnErrorCode = "internal_error"`

        An unexpected internal error prevented the session request from completing.

    - `Message string`

      A customer-safe explanation of the failure.

  - `Object TurnObject`

    The object type. Always `agent.session.turn`.

    - `const TurnObjectAgentSessionTurn TurnObject = "agent.session.turn"`

  - `SessionID string`

    The ID of the session that owns the turn.

  - `StartedAt int64`

    The Unix timestamp, in seconds, when the turn started.

  - `Status TurnStatus`

    The current status of the turn.

    - `const TurnStatusQueued TurnStatus = "queued"`

      The turn is waiting to start.

    - `const TurnStatusInProgress TurnStatus = "in_progress"`

      The turn is in progress.

    - `const TurnStatusWaiting TurnStatus = "waiting"`

      The turn is waiting for external input.

    - `const TurnStatusCompleted TurnStatus = "completed"`

      The turn completed successfully.

    - `const TurnStatusFailed TurnStatus = "failed"`

      The turn failed.

    - `const TurnStatusCancelled TurnStatus = "cancelled"`

      The turn was cancelled.

  - `SubagentID string`

    The ID of the subagent that ran the turn, if applicable.

  - `Usage TokenUsage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `InputTokens int64`

      The number of input tokens used by the agent.

    - `InputTokensDetails TokenUsageInputTokensDetails`

      A breakdown of the agent's input token usage.

      - `CachedTokens int64`

        The number of input tokens retrieved from the prompt cache.

    - `OutputTokens int64`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails TokenUsageOutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `ReasoningTokens int64`

        The number of output tokens used for reasoning.

    - `TotalTokens int64`

      The total number of input and output tokens used by the agent.

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
  turn, err := client.Beta.Agents.Sessions.Subagents.Turns.Get(
    context.TODO(),
    "session_id",
    "subagent_id",
    "turn_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", turn.ID)
}
```

#### Response

```json
{
  "id": "id",
  "agent_id": "agent_id",
  "completed_at": 0,
  "created_at": 0,
  "error": {
    "code": "context_length_exceeded",
    "message": "message"
  },
  "object": "agent.session.turn",
  "session_id": "session_id",
  "started_at": 0,
  "status": "queued",
  "subagent_id": "subagent_id",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 0
  }
}
```

# Items

## List subagent turn items

`client.Beta.Agents.Sessions.Subagents.Turns.Items.List(ctx, sessionID, subagentID, turnID, query) (*CursorPage[AgentSessionItemUnion], error)`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns/{turn_id}/items`

Lists items belonging to one turn of this subagent. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `sessionID string`

- `subagentID string`

- `turnID string`

- `query BetaAgentSessionSubagentTurnItemListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `Limit param.Field[int64]`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Order param.Field[BetaAgentSessionSubagentTurnItemListParamsOrder]`

    The order in which resources are returned. Defaults to `desc`.

    - `const BetaAgentSessionSubagentTurnItemListParamsOrderAsc BetaAgentSessionSubagentTurnItemListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentSessionSubagentTurnItemListParamsOrderDesc BetaAgentSessionSubagentTurnItemListParamsOrder = "desc"`

      Returns resources in descending order.

### Returns

- `type AgentSessionItemUnion interface{…}`

  An item associated with a session turn.

  - `type AgentSessionMessage struct{…}`

    A user or assistant message recorded in a session.

    - `ID string`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `Content []AgentSessionMessageContentUnion`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `type AgentSessionMessageContentInputText struct{…}`

        Text supplied by the user.

        - `Text string`

          The text supplied by the user.

        - `Type InputText`

          The type of the object. Always `input_text`.

          - `const InputTextInputText InputText = "input_text"`

      - `type AgentSessionMessageContentInputImage struct{…}`

        An image supplied by the user.

        - `ImageURL string`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `Type InputImage`

          The type of the object. Always `input_image`.

          - `const InputImageInputImage InputImage = "input_image"`

      - `type AgentSessionMessageContentOutputText struct{…}`

        Text produced by the assistant.

        - `Text string`

          The text produced by the assistant.

        - `Type OutputText`

          The type of the object. Always `output_text`.

          - `const OutputTextOutputText OutputText = "output_text"`

    - `Phase AgentSessionMessagePhase`

      The phase of an assistant message. Null for user messages.

      - `const AgentSessionMessagePhaseCommentary AgentSessionMessagePhase = "commentary"`

        Commentary produced while the agent works.

      - `const AgentSessionMessagePhaseFinalAnswer AgentSessionMessagePhase = "final_answer"`

        The agent's final answer.

    - `Role AgentSessionMessageRole`

      The role of the message author.

      - `const AgentSessionMessageRoleUser AgentSessionMessageRole = "user"`

      - `const AgentSessionMessageRoleAssistant AgentSessionMessageRole = "assistant"`

    - `Status AgentOutputItemStatus`

      The status of the message. User messages are always `completed`.

      - `const AgentOutputItemStatusInProgress AgentOutputItemStatus = "in_progress"`

        The item is in progress.

      - `const AgentOutputItemStatusCompleted AgentOutputItemStatus = "completed"`

        The item is complete.

      - `const AgentOutputItemStatusIncomplete AgentOutputItemStatus = "incomplete"`

        The item stopped before completing.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type Message`

      The item type. Always `message`.

      - `const MessageMessage Message = "message"`

  - `type AgentReasoningItem struct{…}`

    A reasoning item produced by the agent.

    - `ID string`

      The ID of the reasoning item.

    - `Status AgentOutputItemStatus`

      The status of the reasoning item.

    - `Summary []SummaryText`

      The reasoning summaries produced by the agent.

      - `Text string`

        The reasoning summary text.

      - `Type SummaryText`

        The content type. Always `summary_text`.

        - `const SummaryTextSummaryText SummaryText = "summary_text"`

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type Reasoning`

      The item type. Always `reasoning`.

      - `const ReasoningReasoning Reasoning = "reasoning"`

  - `type AgentFunctionCallItem struct{…}`

    A function call produced by the agent.

    - `ID string`

      The ID of the function call item.

    - `Arguments any`

      The arguments to pass to the function.

    - `CallID string`

      The ID used to submit the function result.

    - `Name string`

      The name of the function to call.

    - `Status AgentFunctionCallStatus`

      The status of the function call.

      - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

        The call is in progress.

      - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

        The call completed successfully.

      - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

        The call failed.

      - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

        The call stopped before completing.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type FunctionCall`

      The item type. Always `function_call`.

      - `const FunctionCallFunctionCall FunctionCall = "function_call"`

  - `type AgentSessionItemFunctionCallOutput struct{…}`

    The result supplied for a function call.

    - `ID string`

      The ID of the function call output item.

    - `CallID string`

      The ID of the function call that produced this output.

    - `Error string`

      The error message, if the call failed.

    - `Output AgentFunctionCallOutputUnion`

      The function result, if the call succeeded.

      - `string`

      - `type AgentFunctionCallOutputArray []InputContentUnion`

        - `type InputContentInputText struct{…}`

          Text input recorded in a session item.

          - `Text string`

            The text supplied to the agent.

          - `Type InputText`

            The type of the object. Always `input_text`.

            - `const InputTextInputText InputText = "input_text"`

        - `type InputContentInputImage struct{…}`

          Image input recorded in a session item.

          - `ImageURL string`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `Type InputImage`

            The type of the object. Always `input_image`.

            - `const InputImageInputImage InputImage = "input_image"`

    - `Status AgentFunctionCallStatus`

      The status of the function call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type FunctionCallOutput`

      The item type. Always `function_call_output`.

      - `const FunctionCallOutputFunctionCallOutput FunctionCallOutput = "function_call_output"`

  - `type AgentSessionItemAgentMessage struct{…}`

    A message exchanged between agent threads.

    - `ID string`

      The ID of the message.

    - `Content []AgentContentUnion`

      The content exchanged between the agents.

      - `type OutputText struct{…}`

        A text content part produced by the agent.

        - `Text string`

          The text produced by the agent.

        - `Type OutputText`

          The content type. Always `output_text`.

          - `const OutputTextOutputText OutputText = "output_text"`

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

        - `EncryptedContent string`

          The encrypted content payload.

        - `Type EncryptedContent`

          The content type. Always `encrypted_content`.

          - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

    - `RecipientAgentID string`

      The ID or name of the receiving agent.

    - `SenderAgentID string`

      The ID or name of the sending agent.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type AgentMessage`

      The item type. Always `agent_message`.

      - `const AgentMessageAgentMessage AgentMessage = "agent_message"`

  - `type AgentMcpCallItem struct{…}`

    A call to a tool on an MCP server.

    - `ID string`

      The ID of the MCP call item.

    - `Arguments any`

      The arguments passed to the MCP tool.

    - `Error any`

      The error returned by the MCP tool, if any.

    - `Name string`

      The name of the MCP tool.

    - `Output any`

      The output returned by the MCP tool, if any.

    - `ServerLabel string`

      The label of the MCP server.

    - `Status AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type McpCall`

      The item type. Always `mcp_call`.

      - `const McpCallMcpCall McpCall = "mcp_call"`

  - `type AgentSessionItemComputerUseCall struct{…}`

    One execution of the platform-provided computer-use capability.

    - `ID string`

      The ID of the activity item.

    - `Output AgentSessionItemComputerUseCallOutput`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `ImageURL string`

        The complete JPEG image as a base64 data URL.

      - `Type ComputerScreenshot`

        The content type. Always `computer_screenshot`.

        - `const ComputerScreenshotComputerScreenshot ComputerScreenshot = "computer_screenshot"`

    - `Status AgentFunctionCallStatus`

      The execution status of the activity.

    - `Title string`

      A model-generated description of the activity, when available.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type ComputerUseCall`

      The item type. Always `computer_use_call`.

      - `const ComputerUseCallComputerUseCall ComputerUseCall = "computer_use_call"`

  - `type AgentSessionItemComputerUseApprovalRequest struct{…}`

    A credential-free history record of the emitted login request.

    - `ID string`

      The stable history item ID.

    - `Request AgentSessionItemComputerUseApprovalRequestRequest`

      A registered form awaiting the application's response.

      - `CredentialOrigin string`

        The registered form or frame origin where values will be entered.

      - `Fields []AgentSessionItemComputerUseApprovalRequestRequestField`

        Controls to render. All submitted values are sensitive.

        - `ID string`

          The field ID to submit as field_id in a fields entry.

        - `Label string`

          The label to display beside the control.

        - `Required bool`

          Whether this control requires a nonempty value.

        - `Type string`

          The rendering type, such as email, password, or text.

      - `Options []AgentSessionItemComputerUseApprovalRequestRequestOption`

        Sign-in methods. Empty for a plain form.

        - `ID string`

          The option ID to submit as selected_option.

        - `FieldIDs []string`

          IDs from the registered fields that this method accepts.

        - `Label string`

          The method label to display.

      - `Reason string`

        Why the agent needs the user to sign in.

      - `Type BrowserAuthentication`

        The type of the object. Always `browser_authentication`.

        - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

    - `RequestID string`

    - `TurnID string`

    - `Type ComputerUseApprovalRequest`

      The item type. Always computer_use_approval_request.

      - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

  - `type AgentSessionItemComputerUseApprovalRequestResult struct{…}`

    A credential-free record of an admitted response, not proof of completion.

    - `ID string`

      The stable history item ID.

    - `RequestID string`

      The registered request answered by this item.

    - `Response AgentSessionItemComputerUseApprovalRequestResultResponseUnion`

      The admitted response, without submitted credential values.

      - `type AgentSessionItemComputerUseApprovalRequestResultResponseSubmit struct{…}`

        - `Action Submit`

          - `const SubmitSubmit Submit = "submit"`

        - `SelectedOption string`

          The chosen sign-in method, or null when no options were offered.

        - `Type BrowserAuthentication`

          - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

      - `type AgentSessionItemComputerUseApprovalRequestResultResponseCancel struct{…}`

        - `Action Cancel`

          - `const CancelCancel Cancel = "cancel"`

        - `Type BrowserAuthentication`

          - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type ComputerUseApprovalRequestResult`

      - `const ComputerUseApprovalRequestResultComputerUseApprovalRequestResult ComputerUseApprovalRequestResult = "computer_use_approval_request_result"`

  - `type AgentWebSearchCallItem struct{…}`

    A web search call produced by the agent.

    - `ID string`

      The ID of the web search call.

    - `Action WebSearchActionUnion`

      The action performed by the web search tool.

      - `type WebSearchActionSearch struct{…}`

        A search query or group of search queries.

        - `Queries []string`

          The search queries, when multiple queries were used.

        - `Query string`

          The search query, when a single query was used.

        - `Type Search`

          The type of the object. Always `search`.

          - `const SearchSearch Search = "search"`

      - `type WebSearchActionOpenPage struct{…}`

        Opens a web page.

        - `Type OpenPage`

          The type of the object. Always `open_page`.

          - `const OpenPageOpenPage OpenPage = "open_page"`

        - `URL string`

          The URL of the page that was opened.

      - `type WebSearchActionFindInPage struct{…}`

        Finds text within a web page.

        - `Pattern string`

          The text pattern that was searched for.

        - `Type FindInPage`

          The type of the object. Always `find_in_page`.

          - `const FindInPageFindInPage FindInPage = "find_in_page"`

        - `URL string`

          The URL of the page that was searched.

      - `type WebSearchActionOther struct{…}`

        Another web search action.

        - `Type Other`

          The type of the object. Always `other`.

          - `const OtherOther Other = "other"`

    - `Status AgentOutputItemStatus`

      The status of the web search call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type WebSearchCall`

      The item type. Always `web_search_call`.

      - `const WebSearchCallWebSearchCall WebSearchCall = "web_search_call"`

  - `type AgentCommandExecutionItem struct{…}`

    A command execution produced by the agent.

    - `ID string`

      The ID of the command execution item.

    - `Command string`

      The command that was executed.

    - `Cwd string`

      The working directory used to execute the command.

    - `DurationMs int64`

      The command duration in milliseconds.

    - `ExitCode int64`

      The process exit code, if the command completed.

    - `Output string`

      The command output, if available.

    - `Status AgentFunctionCallStatus`

      The status of the command execution.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type CommandExecution`

      The item type. Always `command_execution`.

      - `const CommandExecutionCommandExecution CommandExecution = "command_execution"`

  - `type AgentCreateSubagentCallItem struct{…}`

    A request to spawn a subagent.

    - `ID string`

      The ID of the tool call item.

    - `AgentID string`

      The ID of the agent that requested the subagent.

    - `Content []AgentContentUnion`

      The task given to the spawned agent.

      - `type OutputText struct{…}`

        A text content part produced by the agent.

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

    - `Model string`

      The model requested for the spawned agent.

    - `ReasoningEffort string`

      The reasoning effort requested for the spawned agent.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type CreateSubagentCall`

      The item type. Always `create_subagent_call`.

      - `const CreateSubagentCallCreateSubagentCall CreateSubagentCall = "create_subagent_call"`

        The current public item type.

  - `type AgentSendSubagentInputCallItem struct{…}`

    A request to send input to another agent.

    - `ID string`

      The ID of the tool call item.

    - `Content []AgentContentUnion`

      The input sent to the receiving agent.

      - `type OutputText struct{…}`

        A text content part produced by the agent.

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

    - `RecipientAgentID string`

      The ID of the agent receiving the input.

    - `SenderAgentID string`

      The ID of the agent sending the input.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type SendSubagentInputCall`

      The item type. Always `send_subagent_input_call`.

      - `const SendSubagentInputCallSendSubagentInputCall SendSubagentInputCall = "send_subagent_input_call"`

        The current public item type.

  - `type AgentResumeSubagentCallItem struct{…}`

    A request to resume a subagent.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentID string`

      The ID of the agent to resume.

    - `SenderAgentID string`

      The ID of the agent requesting the resume.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type ResumeSubagentCall`

      The item type. Always `resume_subagent_call`.

      - `const ResumeSubagentCallResumeSubagentCall ResumeSubagentCall = "resume_subagent_call"`

        The current public item type.

  - `type AgentWaitForSubagentsCallItem struct{…}`

    A request to wait for one or more subagents.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentIDs []string`

      The IDs of the agents to wait for.

    - `SenderAgentID string`

      The ID of the agent waiting for results.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type WaitForSubagentsCall`

      The item type. Always `wait_for_subagents_call`.

      - `const WaitForSubagentsCallWaitForSubagentsCall WaitForSubagentsCall = "wait_for_subagents_call"`

        The current public item type.

  - `type AgentInterruptSubagentCallItem struct{…}`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentID string`

      The ID of the agent to interrupt.

    - `SenderAgentID string`

      The ID of the agent requesting the interrupt.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type InterruptSubagentCall`

      The item type. Always `interrupt_subagent_call`.

      - `const InterruptSubagentCallInterruptSubagentCall InterruptSubagentCall = "interrupt_subagent_call"`

        The current public item type.

  - `type AgentCloseSubagentCallItem struct{…}`

    A request to close a subagent.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentID string`

      The ID of the agent to close.

    - `SenderAgentID string`

      The ID of the agent requesting the close.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type CloseSubagentCall`

      The item type. Always `close_subagent_call`.

      - `const CloseSubagentCallCloseSubagentCall CloseSubagentCall = "close_subagent_call"`

        The current public item type.

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
  page, err := client.Beta.Agents.Sessions.Subagents.Turns.Items.List(
    context.TODO(),
    "session_id",
    "subagent_id",
    "turn_id",
    openai.BetaAgentSessionSubagentTurnItemListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "content": [
        {
          "text": "text",
          "type": "input_text"
        }
      ],
      "phase": "commentary",
      "role": "user",
      "status": "in_progress",
      "turn_id": "turn_id",
      "type": "message"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

# Turns

## List agent session turns

`client.Beta.Agents.Sessions.Turns.List(ctx, sessionID, query) (*CursorPage[Turn], error)`

**get** `/agents/sessions/{session_id}/turns`

Lists turns by creation time and turn ID. The after cursor is exclusive in the selected order. See [session turns](/api/docs/guides/agents-api/sessions/manage#inspect-session-turns).

### Parameters

- `sessionID string`

- `query BetaAgentSessionTurnListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `Limit param.Field[int64]`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Order param.Field[BetaAgentSessionTurnListParamsOrder]`

    The order in which resources are returned. Defaults to `desc`.

    - `const BetaAgentSessionTurnListParamsOrderAsc BetaAgentSessionTurnListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentSessionTurnListParamsOrderDesc BetaAgentSessionTurnListParamsOrder = "desc"`

      Returns resources in descending order.

### Returns

- `type Turn struct{…}`

  The canonical public representation of a session turn.

  - `ID string`

    The ID of the turn.

  - `AgentID string`

    The ID of the agent that ran the turn.

  - `CompletedAt int64`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `Error SessionTurnError`

    A customer-safe error. Non-null only for a failed turn.

    - `Code SessionTurnErrorCode`

      A stable, machine-readable failure category.

      - `const SessionTurnErrorCodeContextLengthExceeded SessionTurnErrorCode = "context_length_exceeded"`

        The request exceeds the model's context window.

      - `const SessionTurnErrorCodeSessionBudgetExceeded SessionTurnErrorCode = "session_budget_exceeded"`

        The session has reached its usage budget.

      - `const SessionTurnErrorCodeUsageLimitExceeded SessionTurnErrorCode = "usage_limit_exceeded"`

        The organization has reached a usage, plan, or billing limit.

      - `const SessionTurnErrorCodeCreditBalanceExhausted SessionTurnErrorCode = "credit_balance_exhausted"`

        The organization has no API credits remaining.

      - `const SessionTurnErrorCodeRateLimitExceeded SessionTurnErrorCode = "rate_limit_exceeded"`

        The request exceeds the available rate limit.

      - `const SessionTurnErrorCodeFlexUnavailable SessionTurnErrorCode = "flex_unavailable"`

        Flex processing is temporarily unavailable.

      - `const SessionTurnErrorCodeServerOverloaded SessionTurnErrorCode = "server_overloaded"`

        The model service is temporarily overloaded.

      - `const SessionTurnErrorCodeCyberPolicy SessionTurnErrorCode = "cyber_policy"`

        The request was rejected by a safety policy.

      - `const SessionTurnErrorCodeMisalignmentPolicyViolation SessionTurnErrorCode = "misalignment_policy_violation"`

        The request was blocked by the safety systems.

      - `const SessionTurnErrorCodeConnectionFailed SessionTurnErrorCode = "connection_failed"`

        The request could not connect to the model service.

      - `const SessionTurnErrorCodeServerError SessionTurnErrorCode = "server_error"`

        The model service encountered an unexpected error.

      - `const SessionTurnErrorCodeAuthenticationError SessionTurnErrorCode = "authentication_error"`

        The API credentials are invalid or lack the required access.

      - `const SessionTurnErrorCodeInvalidRequest SessionTurnErrorCode = "invalid_request"`

        The request contains invalid input or configuration.

      - `const SessionTurnErrorCodeResourceNotFound SessionTurnErrorCode = "resource_not_found"`

        The requested model or resource is unavailable.

      - `const SessionTurnErrorCodeSandboxError SessionTurnErrorCode = "sandbox_error"`

        The request could not complete in its execution environment.

      - `const SessionTurnErrorCodeExecutorVersionIncompatible SessionTurnErrorCode = "executor_version_incompatible"`

        The executor must be upgraded before it can run this turn.

      - `const SessionTurnErrorCodeActiveTurnNotSteerable SessionTurnErrorCode = "active_turn_not_steerable"`

        The session cannot accept additional input while a request is running.

      - `const SessionTurnErrorCodeRequestTimeout SessionTurnErrorCode = "request_timeout"`

        The request timed out before the model service responded.

      - `const SessionTurnErrorCodeInternalError SessionTurnErrorCode = "internal_error"`

        An unexpected internal error prevented the session request from completing.

    - `Message string`

      A customer-safe explanation of the failure.

  - `Object TurnObject`

    The object type. Always `agent.session.turn`.

    - `const TurnObjectAgentSessionTurn TurnObject = "agent.session.turn"`

  - `SessionID string`

    The ID of the session that owns the turn.

  - `StartedAt int64`

    The Unix timestamp, in seconds, when the turn started.

  - `Status TurnStatus`

    The current status of the turn.

    - `const TurnStatusQueued TurnStatus = "queued"`

      The turn is waiting to start.

    - `const TurnStatusInProgress TurnStatus = "in_progress"`

      The turn is in progress.

    - `const TurnStatusWaiting TurnStatus = "waiting"`

      The turn is waiting for external input.

    - `const TurnStatusCompleted TurnStatus = "completed"`

      The turn completed successfully.

    - `const TurnStatusFailed TurnStatus = "failed"`

      The turn failed.

    - `const TurnStatusCancelled TurnStatus = "cancelled"`

      The turn was cancelled.

  - `SubagentID string`

    The ID of the subagent that ran the turn, if applicable.

  - `Usage TokenUsage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `InputTokens int64`

      The number of input tokens used by the agent.

    - `InputTokensDetails TokenUsageInputTokensDetails`

      A breakdown of the agent's input token usage.

      - `CachedTokens int64`

        The number of input tokens retrieved from the prompt cache.

    - `OutputTokens int64`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails TokenUsageOutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `ReasoningTokens int64`

        The number of output tokens used for reasoning.

    - `TotalTokens int64`

      The total number of input and output tokens used by the agent.

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
  page, err := client.Beta.Agents.Sessions.Turns.List(
    context.TODO(),
    "session_id",
    openai.BetaAgentSessionTurnListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "agent_id": "agent_id",
      "completed_at": 0,
      "created_at": 0,
      "error": {
        "code": "context_length_exceeded",
        "message": "message"
      },
      "object": "agent.session.turn",
      "session_id": "session_id",
      "started_at": 0,
      "status": "queued",
      "subagent_id": "subagent_id",
      "usage": {
        "input_tokens": 0,
        "input_tokens_details": {
          "cached_tokens": 0
        },
        "output_tokens": 0,
        "output_tokens_details": {
          "reasoning_tokens": 0
        },
        "total_tokens": 0
      }
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve an agent session turn

`client.Beta.Agents.Sessions.Turns.Get(ctx, sessionID, turnID) (*Turn, error)`

**get** `/agents/sessions/{session_id}/turns/{turn_id}`

Retrieves a turn's current status, timestamps, usage, and error. Returns 404 if the turn does not belong to the session. See [session turns](/api/docs/guides/agents-api/sessions/manage#inspect-session-turns).

### Parameters

- `sessionID string`

- `turnID string`

### Returns

- `type Turn struct{…}`

  The canonical public representation of a session turn.

  - `ID string`

    The ID of the turn.

  - `AgentID string`

    The ID of the agent that ran the turn.

  - `CompletedAt int64`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `Error SessionTurnError`

    A customer-safe error. Non-null only for a failed turn.

    - `Code SessionTurnErrorCode`

      A stable, machine-readable failure category.

      - `const SessionTurnErrorCodeContextLengthExceeded SessionTurnErrorCode = "context_length_exceeded"`

        The request exceeds the model's context window.

      - `const SessionTurnErrorCodeSessionBudgetExceeded SessionTurnErrorCode = "session_budget_exceeded"`

        The session has reached its usage budget.

      - `const SessionTurnErrorCodeUsageLimitExceeded SessionTurnErrorCode = "usage_limit_exceeded"`

        The organization has reached a usage, plan, or billing limit.

      - `const SessionTurnErrorCodeCreditBalanceExhausted SessionTurnErrorCode = "credit_balance_exhausted"`

        The organization has no API credits remaining.

      - `const SessionTurnErrorCodeRateLimitExceeded SessionTurnErrorCode = "rate_limit_exceeded"`

        The request exceeds the available rate limit.

      - `const SessionTurnErrorCodeFlexUnavailable SessionTurnErrorCode = "flex_unavailable"`

        Flex processing is temporarily unavailable.

      - `const SessionTurnErrorCodeServerOverloaded SessionTurnErrorCode = "server_overloaded"`

        The model service is temporarily overloaded.

      - `const SessionTurnErrorCodeCyberPolicy SessionTurnErrorCode = "cyber_policy"`

        The request was rejected by a safety policy.

      - `const SessionTurnErrorCodeMisalignmentPolicyViolation SessionTurnErrorCode = "misalignment_policy_violation"`

        The request was blocked by the safety systems.

      - `const SessionTurnErrorCodeConnectionFailed SessionTurnErrorCode = "connection_failed"`

        The request could not connect to the model service.

      - `const SessionTurnErrorCodeServerError SessionTurnErrorCode = "server_error"`

        The model service encountered an unexpected error.

      - `const SessionTurnErrorCodeAuthenticationError SessionTurnErrorCode = "authentication_error"`

        The API credentials are invalid or lack the required access.

      - `const SessionTurnErrorCodeInvalidRequest SessionTurnErrorCode = "invalid_request"`

        The request contains invalid input or configuration.

      - `const SessionTurnErrorCodeResourceNotFound SessionTurnErrorCode = "resource_not_found"`

        The requested model or resource is unavailable.

      - `const SessionTurnErrorCodeSandboxError SessionTurnErrorCode = "sandbox_error"`

        The request could not complete in its execution environment.

      - `const SessionTurnErrorCodeExecutorVersionIncompatible SessionTurnErrorCode = "executor_version_incompatible"`

        The executor must be upgraded before it can run this turn.

      - `const SessionTurnErrorCodeActiveTurnNotSteerable SessionTurnErrorCode = "active_turn_not_steerable"`

        The session cannot accept additional input while a request is running.

      - `const SessionTurnErrorCodeRequestTimeout SessionTurnErrorCode = "request_timeout"`

        The request timed out before the model service responded.

      - `const SessionTurnErrorCodeInternalError SessionTurnErrorCode = "internal_error"`

        An unexpected internal error prevented the session request from completing.

    - `Message string`

      A customer-safe explanation of the failure.

  - `Object TurnObject`

    The object type. Always `agent.session.turn`.

    - `const TurnObjectAgentSessionTurn TurnObject = "agent.session.turn"`

  - `SessionID string`

    The ID of the session that owns the turn.

  - `StartedAt int64`

    The Unix timestamp, in seconds, when the turn started.

  - `Status TurnStatus`

    The current status of the turn.

    - `const TurnStatusQueued TurnStatus = "queued"`

      The turn is waiting to start.

    - `const TurnStatusInProgress TurnStatus = "in_progress"`

      The turn is in progress.

    - `const TurnStatusWaiting TurnStatus = "waiting"`

      The turn is waiting for external input.

    - `const TurnStatusCompleted TurnStatus = "completed"`

      The turn completed successfully.

    - `const TurnStatusFailed TurnStatus = "failed"`

      The turn failed.

    - `const TurnStatusCancelled TurnStatus = "cancelled"`

      The turn was cancelled.

  - `SubagentID string`

    The ID of the subagent that ran the turn, if applicable.

  - `Usage TokenUsage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `InputTokens int64`

      The number of input tokens used by the agent.

    - `InputTokensDetails TokenUsageInputTokensDetails`

      A breakdown of the agent's input token usage.

      - `CachedTokens int64`

        The number of input tokens retrieved from the prompt cache.

    - `OutputTokens int64`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails TokenUsageOutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `ReasoningTokens int64`

        The number of output tokens used for reasoning.

    - `TotalTokens int64`

      The total number of input and output tokens used by the agent.

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
  turn, err := client.Beta.Agents.Sessions.Turns.Get(
    context.TODO(),
    "session_id",
    "turn_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", turn.ID)
}
```

#### Response

```json
{
  "id": "id",
  "agent_id": "agent_id",
  "completed_at": 0,
  "created_at": 0,
  "error": {
    "code": "context_length_exceeded",
    "message": "message"
  },
  "object": "agent.session.turn",
  "session_id": "session_id",
  "started_at": 0,
  "status": "queued",
  "subagent_id": "subagent_id",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 0
  }
}
```

## Domain Types

### Turn

- `type Turn struct{…}`

  The canonical public representation of a session turn.

  - `ID string`

    The ID of the turn.

  - `AgentID string`

    The ID of the agent that ran the turn.

  - `CompletedAt int64`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `Error SessionTurnError`

    A customer-safe error. Non-null only for a failed turn.

    - `Code SessionTurnErrorCode`

      A stable, machine-readable failure category.

      - `const SessionTurnErrorCodeContextLengthExceeded SessionTurnErrorCode = "context_length_exceeded"`

        The request exceeds the model's context window.

      - `const SessionTurnErrorCodeSessionBudgetExceeded SessionTurnErrorCode = "session_budget_exceeded"`

        The session has reached its usage budget.

      - `const SessionTurnErrorCodeUsageLimitExceeded SessionTurnErrorCode = "usage_limit_exceeded"`

        The organization has reached a usage, plan, or billing limit.

      - `const SessionTurnErrorCodeCreditBalanceExhausted SessionTurnErrorCode = "credit_balance_exhausted"`

        The organization has no API credits remaining.

      - `const SessionTurnErrorCodeRateLimitExceeded SessionTurnErrorCode = "rate_limit_exceeded"`

        The request exceeds the available rate limit.

      - `const SessionTurnErrorCodeFlexUnavailable SessionTurnErrorCode = "flex_unavailable"`

        Flex processing is temporarily unavailable.

      - `const SessionTurnErrorCodeServerOverloaded SessionTurnErrorCode = "server_overloaded"`

        The model service is temporarily overloaded.

      - `const SessionTurnErrorCodeCyberPolicy SessionTurnErrorCode = "cyber_policy"`

        The request was rejected by a safety policy.

      - `const SessionTurnErrorCodeMisalignmentPolicyViolation SessionTurnErrorCode = "misalignment_policy_violation"`

        The request was blocked by the safety systems.

      - `const SessionTurnErrorCodeConnectionFailed SessionTurnErrorCode = "connection_failed"`

        The request could not connect to the model service.

      - `const SessionTurnErrorCodeServerError SessionTurnErrorCode = "server_error"`

        The model service encountered an unexpected error.

      - `const SessionTurnErrorCodeAuthenticationError SessionTurnErrorCode = "authentication_error"`

        The API credentials are invalid or lack the required access.

      - `const SessionTurnErrorCodeInvalidRequest SessionTurnErrorCode = "invalid_request"`

        The request contains invalid input or configuration.

      - `const SessionTurnErrorCodeResourceNotFound SessionTurnErrorCode = "resource_not_found"`

        The requested model or resource is unavailable.

      - `const SessionTurnErrorCodeSandboxError SessionTurnErrorCode = "sandbox_error"`

        The request could not complete in its execution environment.

      - `const SessionTurnErrorCodeExecutorVersionIncompatible SessionTurnErrorCode = "executor_version_incompatible"`

        The executor must be upgraded before it can run this turn.

      - `const SessionTurnErrorCodeActiveTurnNotSteerable SessionTurnErrorCode = "active_turn_not_steerable"`

        The session cannot accept additional input while a request is running.

      - `const SessionTurnErrorCodeRequestTimeout SessionTurnErrorCode = "request_timeout"`

        The request timed out before the model service responded.

      - `const SessionTurnErrorCodeInternalError SessionTurnErrorCode = "internal_error"`

        An unexpected internal error prevented the session request from completing.

    - `Message string`

      A customer-safe explanation of the failure.

  - `Object TurnObject`

    The object type. Always `agent.session.turn`.

    - `const TurnObjectAgentSessionTurn TurnObject = "agent.session.turn"`

  - `SessionID string`

    The ID of the session that owns the turn.

  - `StartedAt int64`

    The Unix timestamp, in seconds, when the turn started.

  - `Status TurnStatus`

    The current status of the turn.

    - `const TurnStatusQueued TurnStatus = "queued"`

      The turn is waiting to start.

    - `const TurnStatusInProgress TurnStatus = "in_progress"`

      The turn is in progress.

    - `const TurnStatusWaiting TurnStatus = "waiting"`

      The turn is waiting for external input.

    - `const TurnStatusCompleted TurnStatus = "completed"`

      The turn completed successfully.

    - `const TurnStatusFailed TurnStatus = "failed"`

      The turn failed.

    - `const TurnStatusCancelled TurnStatus = "cancelled"`

      The turn was cancelled.

  - `SubagentID string`

    The ID of the subagent that ran the turn, if applicable.

  - `Usage TokenUsage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `InputTokens int64`

      The number of input tokens used by the agent.

    - `InputTokensDetails TokenUsageInputTokensDetails`

      A breakdown of the agent's input token usage.

      - `CachedTokens int64`

        The number of input tokens retrieved from the prompt cache.

    - `OutputTokens int64`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails TokenUsageOutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `ReasoningTokens int64`

        The number of output tokens used for reasoning.

    - `TotalTokens int64`

      The total number of input and output tokens used by the agent.

# Vaults

## Create a vault

`client.Beta.Agents.Vaults.New(ctx, body) (*Vault, error)`

**post** `/vaults`

Creates a vault for the current project. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `body BetaAgentVaultNewParams`

  - `Metadata param.Field[map[string, string]]`

    Key-value pairs to associate with the vault, such as an application or team identifier.

  - `Name param.Field[string]`

    The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

### Returns

- `type Vault struct{…}`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `ID string`

    The ID of the vault.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the vault was created.

  - `Metadata map[string, string]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `Name string`

    The human-readable name of the vault, if set.

  - `Object Vault`

    The object type. Always `vault`.

    - `const VaultVault Vault = "vault"`

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
  vault, err := client.Beta.Agents.Vaults.New(context.TODO(), openai.BetaAgentVaultNewParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", vault.ID)
}
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "vault"
}
```

## Delete a vault

`client.Beta.Agents.Vaults.Delete(ctx, vaultID) (*VaultDeleted, error)`

**delete** `/vaults/{vault_id}`

Deletes a vault and all its credentials. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID string`

### Returns

- `type VaultDeleted struct{…}`

  Confirmation that a vault was deleted.

  - `ID string`

    The ID of the deleted vault.

  - `Deleted bool`

    Whether the resource was deleted. Always `true`.

  - `Object VaultDeleted`

    The object type. Always `vault.deleted`.

    - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

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
  vaultDeleted, err := client.Beta.Agents.Vaults.Delete(context.TODO(), "vault_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", vaultDeleted.ID)
}
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "vault.deleted"
}
```

## List vaults

`client.Beta.Agents.Vaults.List(ctx, query) (*CursorPage[Vault], error)`

**get** `/vaults`

Lists vaults using ID-based pagination. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `query BetaAgentVaultListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `Limit param.Field[int64]`

    The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

  - `Order param.Field[BetaAgentVaultListParamsOrder]`

    Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

    - `const BetaAgentVaultListParamsOrderAsc BetaAgentVaultListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentVaultListParamsOrderDesc BetaAgentVaultListParamsOrder = "desc"`

      Returns resources in descending order.

  - `Status param.Field[VaultStatusFilterUnion]`

    Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

### Returns

- `type Vault struct{…}`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `ID string`

    The ID of the vault.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the vault was created.

  - `Metadata map[string, string]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `Name string`

    The human-readable name of the vault, if set.

  - `Object Vault`

    The object type. Always `vault`.

    - `const VaultVault Vault = "vault"`

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
  page, err := client.Beta.Agents.Vaults.List(context.TODO(), openai.BetaAgentVaultListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": 0,
      "metadata": {
        "foo": "string"
      },
      "name": "name",
      "object": "vault"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve a vault

`client.Beta.Agents.Vaults.Get(ctx, vaultID) (*Vault, error)`

**get** `/vaults/{vault_id}`

Retrieves a vault by its ID. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID string`

### Returns

- `type Vault struct{…}`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `ID string`

    The ID of the vault.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the vault was created.

  - `Metadata map[string, string]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `Name string`

    The human-readable name of the vault, if set.

  - `Object Vault`

    The object type. Always `vault`.

    - `const VaultVault Vault = "vault"`

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
  vault, err := client.Beta.Agents.Vaults.Get(context.TODO(), "vault_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", vault.ID)
}
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "vault"
}
```

## Domain Types

### Vault

- `type Vault struct{…}`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `ID string`

    The ID of the vault.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the vault was created.

  - `Metadata map[string, string]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `Name string`

    The human-readable name of the vault, if set.

  - `Object Vault`

    The object type. Always `vault`.

    - `const VaultVault Vault = "vault"`

### Vault Deleted

- `type VaultDeleted struct{…}`

  Confirmation that a vault was deleted.

  - `ID string`

    The ID of the deleted vault.

  - `Deleted bool`

    Whether the resource was deleted. Always `true`.

  - `Object VaultDeleted`

    The object type. Always `vault.deleted`.

    - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

### Vault Status

- `type VaultStatus string`

  Whether a vault or credential is active or archived.

  - `const VaultStatusActive VaultStatus = "active"`

  - `const VaultStatusArchived VaultStatus = "archived"`

### Vault Status Filter

- `type VaultStatusFilterUnion interface{…}`

  One or more lifecycle statuses to include when listing vaults or credentials.

  - `type VaultStatus string`

    Whether a vault or credential is active or archived.

    - `const VaultStatusActive VaultStatus = "active"`

    - `const VaultStatusArchived VaultStatus = "archived"`

  - `[]VaultStatus`

    - `const VaultStatusActive VaultStatus = "active"`

    - `const VaultStatusArchived VaultStatus = "archived"`

# Credentials

## Create a vault credential

`client.Beta.Agents.Vaults.Credentials.New(ctx, vaultID, body) (*Credential, error)`

**post** `/vaults/{vault_id}/credentials`

Creates a vault credential. Secret values are write-only and are never returned. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID string`

- `body BetaAgentVaultCredentialNewParams`

  - `Auth param.Field[CredentialAuthCreateParamUnionResp]`

    The authentication method and write-only secret values to store.

  - `Name param.Field[string]`

    The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

  - `Metadata param.Field[map[string, string]]`

    Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Defaults to an empty map.

### Returns

- `type Credential struct{…}`

  Metadata for a stored credential. Secret values are never returned.

  - `ID string`

    The ID of the credential.

  - `Auth CredentialAuthUnion`

    The authentication method and non-secret configuration of the credential.

    - `type CredentialAuthMcpOAuth struct{…}`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `ExpiresAt string`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Refresh CredentialAuthMcpOAuthRefresh`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `ClientID string`

          The OAuth client ID used when requesting a new access token.

        - `Resource string`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `Scope string`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `TokenEndpoint string`

          The HTTPS OAuth token endpoint used for refresh.

        - `TokenEndpointAuth McpOAuthTokenEndpointAuthUnion`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `type McpOAuthTokenEndpointAuthNone struct{…}`

            Sends the client ID without a client secret.

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `type McpOAuthTokenEndpointAuthClientSecretBasic struct{…}`

            Sends the client ID and secret using HTTP Basic authentication.

            - `Type ClientSecretBasic`

              The type of the object. Always `client_secret_basic`.

              - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

          - `type McpOAuthTokenEndpointAuthClientSecretPost struct{…}`

            Sends the client ID and secret in the token request body.

            - `Type ClientSecretPost`

              The type of the object. Always `client_secret_post`.

              - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

      - `Type McpOAuth`

        The type of the object. Always `mcp_oauth`.

        - `const McpOAuthMcpOAuth McpOAuth = "mcp_oauth"`

    - `type CredentialAuthStaticBearer struct{…}`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Type StaticBearer`

        The type of the object. Always `static_bearer`.

        - `const StaticBearerStaticBearer StaticBearer = "static_bearer"`

    - `type CredentialAuthEnvironmentVariable struct{…}`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `Networking CredentialNetworkingUnion`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `type CredentialNetworkingUnrestricted struct{…}`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `Type Unrestricted`

            The type of the object. Always `unrestricted`.

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type CredentialNetworkingLimited struct{…}`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `AllowedHosts []string`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `Type Limited`

            The type of the object. Always `limited`.

            - `const LimitedLimited Limited = "limited"`

      - `SecretName string`

        The environment variable name that receives the placeholder in the sandbox.

      - `Type EnvironmentVariable`

        The type of the object. Always `environment_variable`.

        - `const EnvironmentVariableEnvironmentVariable EnvironmentVariable = "environment_variable"`

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the credential was created.

  - `Metadata map[string, string]`

    Application-defined key-value pairs associated with this credential.

  - `Name string`

    The human-readable name of the credential.

  - `Object VaultCredential`

    The object type. Always `vault.credential`.

    - `const VaultCredentialVaultCredential VaultCredential = "vault.credential"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `VaultID string`

    The ID of the vault containing this credential.

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
  credential, err := client.Beta.Agents.Vaults.Credentials.New(
    context.TODO(),
    "vault_id",
    openai.BetaAgentVaultCredentialNewParams{
      Auth: openai.CredentialAuthCreateParamUnion{
        OfMcpOauth: &openai.CredentialAuthCreateParamMcpOAuth{
          AccessToken: "access_token",
          McpServerURL: "mcp_server_url",
        },
      },
      Name: "x",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", credential.ID)
}
```

#### Response

```json
{
  "id": "id",
  "auth": {
    "expires_at": "expires_at",
    "mcp_server_url": "mcp_server_url",
    "refresh": {
      "client_id": "client_id",
      "resource": "resource",
      "scope": "scope",
      "token_endpoint": "token_endpoint",
      "token_endpoint_auth": {
        "type": "none"
      }
    },
    "type": "mcp_oauth"
  },
  "created_at": 0,
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "vault.credential",
  "updated_at": 0,
  "vault_id": "vault_id"
}
```

## Delete a vault credential

`client.Beta.Agents.Vaults.Credentials.Delete(ctx, vaultID, credentialID) (*CredentialDeleted, error)`

**delete** `/vaults/{vault_id}/credentials/{credential_id}`

Deletes a vault credential. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID string`

- `credentialID string`

### Returns

- `type CredentialDeleted struct{…}`

  Confirmation that a vault credential was deleted.

  - `ID string`

    The ID of the deleted credential.

  - `Deleted bool`

    Whether the resource was deleted. Always `true`.

  - `Object VaultCredentialDeleted`

    The object type. Always `vault.credential.deleted`.

    - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault.credential.deleted"`

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
  credentialDeleted, err := client.Beta.Agents.Vaults.Credentials.Delete(
    context.TODO(),
    "vault_id",
    "credential_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", credentialDeleted.ID)
}
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "vault.credential.deleted"
}
```

## List vault credentials

`client.Beta.Agents.Vaults.Credentials.List(ctx, vaultID, query) (*CursorPage[Credential], error)`

**get** `/vaults/{vault_id}/credentials`

Lists a vault's credentials using ID-based pagination without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID string`

- `query BetaAgentVaultCredentialListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `Limit param.Field[int64]`

    The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

  - `Order param.Field[BetaAgentVaultCredentialListParamsOrder]`

    Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

    - `const BetaAgentVaultCredentialListParamsOrderAsc BetaAgentVaultCredentialListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentVaultCredentialListParamsOrderDesc BetaAgentVaultCredentialListParamsOrder = "desc"`

      Returns resources in descending order.

  - `Status param.Field[VaultStatusFilterUnion]`

    Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

### Returns

- `type Credential struct{…}`

  Metadata for a stored credential. Secret values are never returned.

  - `ID string`

    The ID of the credential.

  - `Auth CredentialAuthUnion`

    The authentication method and non-secret configuration of the credential.

    - `type CredentialAuthMcpOAuth struct{…}`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `ExpiresAt string`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Refresh CredentialAuthMcpOAuthRefresh`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `ClientID string`

          The OAuth client ID used when requesting a new access token.

        - `Resource string`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `Scope string`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `TokenEndpoint string`

          The HTTPS OAuth token endpoint used for refresh.

        - `TokenEndpointAuth McpOAuthTokenEndpointAuthUnion`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `type McpOAuthTokenEndpointAuthNone struct{…}`

            Sends the client ID without a client secret.

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `type McpOAuthTokenEndpointAuthClientSecretBasic struct{…}`

            Sends the client ID and secret using HTTP Basic authentication.

            - `Type ClientSecretBasic`

              The type of the object. Always `client_secret_basic`.

              - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

          - `type McpOAuthTokenEndpointAuthClientSecretPost struct{…}`

            Sends the client ID and secret in the token request body.

            - `Type ClientSecretPost`

              The type of the object. Always `client_secret_post`.

              - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

      - `Type McpOAuth`

        The type of the object. Always `mcp_oauth`.

        - `const McpOAuthMcpOAuth McpOAuth = "mcp_oauth"`

    - `type CredentialAuthStaticBearer struct{…}`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Type StaticBearer`

        The type of the object. Always `static_bearer`.

        - `const StaticBearerStaticBearer StaticBearer = "static_bearer"`

    - `type CredentialAuthEnvironmentVariable struct{…}`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `Networking CredentialNetworkingUnion`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `type CredentialNetworkingUnrestricted struct{…}`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `Type Unrestricted`

            The type of the object. Always `unrestricted`.

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type CredentialNetworkingLimited struct{…}`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `AllowedHosts []string`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `Type Limited`

            The type of the object. Always `limited`.

            - `const LimitedLimited Limited = "limited"`

      - `SecretName string`

        The environment variable name that receives the placeholder in the sandbox.

      - `Type EnvironmentVariable`

        The type of the object. Always `environment_variable`.

        - `const EnvironmentVariableEnvironmentVariable EnvironmentVariable = "environment_variable"`

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the credential was created.

  - `Metadata map[string, string]`

    Application-defined key-value pairs associated with this credential.

  - `Name string`

    The human-readable name of the credential.

  - `Object VaultCredential`

    The object type. Always `vault.credential`.

    - `const VaultCredentialVaultCredential VaultCredential = "vault.credential"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `VaultID string`

    The ID of the vault containing this credential.

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
  page, err := client.Beta.Agents.Vaults.Credentials.List(
    context.TODO(),
    "vault_id",
    openai.BetaAgentVaultCredentialListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "auth": {
        "expires_at": "expires_at",
        "mcp_server_url": "mcp_server_url",
        "refresh": {
          "client_id": "client_id",
          "resource": "resource",
          "scope": "scope",
          "token_endpoint": "token_endpoint",
          "token_endpoint_auth": {
            "type": "none"
          }
        },
        "type": "mcp_oauth"
      },
      "created_at": 0,
      "metadata": {
        "foo": "string"
      },
      "name": "name",
      "object": "vault.credential",
      "updated_at": 0,
      "vault_id": "vault_id"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve a vault credential

`client.Beta.Agents.Vaults.Credentials.Get(ctx, vaultID, credentialID) (*Credential, error)`

**get** `/vaults/{vault_id}/credentials/{credential_id}`

Retrieves vault credential metadata without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID string`

- `credentialID string`

### Returns

- `type Credential struct{…}`

  Metadata for a stored credential. Secret values are never returned.

  - `ID string`

    The ID of the credential.

  - `Auth CredentialAuthUnion`

    The authentication method and non-secret configuration of the credential.

    - `type CredentialAuthMcpOAuth struct{…}`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `ExpiresAt string`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Refresh CredentialAuthMcpOAuthRefresh`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `ClientID string`

          The OAuth client ID used when requesting a new access token.

        - `Resource string`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `Scope string`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `TokenEndpoint string`

          The HTTPS OAuth token endpoint used for refresh.

        - `TokenEndpointAuth McpOAuthTokenEndpointAuthUnion`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `type McpOAuthTokenEndpointAuthNone struct{…}`

            Sends the client ID without a client secret.

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `type McpOAuthTokenEndpointAuthClientSecretBasic struct{…}`

            Sends the client ID and secret using HTTP Basic authentication.

            - `Type ClientSecretBasic`

              The type of the object. Always `client_secret_basic`.

              - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

          - `type McpOAuthTokenEndpointAuthClientSecretPost struct{…}`

            Sends the client ID and secret in the token request body.

            - `Type ClientSecretPost`

              The type of the object. Always `client_secret_post`.

              - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

      - `Type McpOAuth`

        The type of the object. Always `mcp_oauth`.

        - `const McpOAuthMcpOAuth McpOAuth = "mcp_oauth"`

    - `type CredentialAuthStaticBearer struct{…}`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Type StaticBearer`

        The type of the object. Always `static_bearer`.

        - `const StaticBearerStaticBearer StaticBearer = "static_bearer"`

    - `type CredentialAuthEnvironmentVariable struct{…}`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `Networking CredentialNetworkingUnion`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `type CredentialNetworkingUnrestricted struct{…}`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `Type Unrestricted`

            The type of the object. Always `unrestricted`.

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type CredentialNetworkingLimited struct{…}`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `AllowedHosts []string`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `Type Limited`

            The type of the object. Always `limited`.

            - `const LimitedLimited Limited = "limited"`

      - `SecretName string`

        The environment variable name that receives the placeholder in the sandbox.

      - `Type EnvironmentVariable`

        The type of the object. Always `environment_variable`.

        - `const EnvironmentVariableEnvironmentVariable EnvironmentVariable = "environment_variable"`

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the credential was created.

  - `Metadata map[string, string]`

    Application-defined key-value pairs associated with this credential.

  - `Name string`

    The human-readable name of the credential.

  - `Object VaultCredential`

    The object type. Always `vault.credential`.

    - `const VaultCredentialVaultCredential VaultCredential = "vault.credential"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `VaultID string`

    The ID of the vault containing this credential.

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
  credential, err := client.Beta.Agents.Vaults.Credentials.Get(
    context.TODO(),
    "vault_id",
    "credential_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", credential.ID)
}
```

#### Response

```json
{
  "id": "id",
  "auth": {
    "expires_at": "expires_at",
    "mcp_server_url": "mcp_server_url",
    "refresh": {
      "client_id": "client_id",
      "resource": "resource",
      "scope": "scope",
      "token_endpoint": "token_endpoint",
      "token_endpoint_auth": {
        "type": "none"
      }
    },
    "type": "mcp_oauth"
  },
  "created_at": 0,
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "vault.credential",
  "updated_at": 0,
  "vault_id": "vault_id"
}
```

## Update a vault credential

`client.Beta.Agents.Vaults.Credentials.Update(ctx, vaultID, credentialID, body) (*Credential, error)`

**post** `/vaults/{vault_id}/credentials/{credential_id}`

Updates credential metadata or rotates its write-only secret. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID string`

- `credentialID string`

- `body BetaAgentVaultCredentialUpdateParams`

  - `Auth param.Field[CredentialAuthRotateParamUnionResp]`

    Replacement values for the credential's existing authentication method.

  - `Metadata param.Field[map[string, string]]`

    Replaces all metadata. Omit to preserve it, or pass {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

### Returns

- `type Credential struct{…}`

  Metadata for a stored credential. Secret values are never returned.

  - `ID string`

    The ID of the credential.

  - `Auth CredentialAuthUnion`

    The authentication method and non-secret configuration of the credential.

    - `type CredentialAuthMcpOAuth struct{…}`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `ExpiresAt string`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Refresh CredentialAuthMcpOAuthRefresh`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `ClientID string`

          The OAuth client ID used when requesting a new access token.

        - `Resource string`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `Scope string`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `TokenEndpoint string`

          The HTTPS OAuth token endpoint used for refresh.

        - `TokenEndpointAuth McpOAuthTokenEndpointAuthUnion`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `type McpOAuthTokenEndpointAuthNone struct{…}`

            Sends the client ID without a client secret.

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `type McpOAuthTokenEndpointAuthClientSecretBasic struct{…}`

            Sends the client ID and secret using HTTP Basic authentication.

            - `Type ClientSecretBasic`

              The type of the object. Always `client_secret_basic`.

              - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

          - `type McpOAuthTokenEndpointAuthClientSecretPost struct{…}`

            Sends the client ID and secret in the token request body.

            - `Type ClientSecretPost`

              The type of the object. Always `client_secret_post`.

              - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

      - `Type McpOAuth`

        The type of the object. Always `mcp_oauth`.

        - `const McpOAuthMcpOAuth McpOAuth = "mcp_oauth"`

    - `type CredentialAuthStaticBearer struct{…}`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Type StaticBearer`

        The type of the object. Always `static_bearer`.

        - `const StaticBearerStaticBearer StaticBearer = "static_bearer"`

    - `type CredentialAuthEnvironmentVariable struct{…}`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `Networking CredentialNetworkingUnion`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `type CredentialNetworkingUnrestricted struct{…}`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `Type Unrestricted`

            The type of the object. Always `unrestricted`.

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type CredentialNetworkingLimited struct{…}`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `AllowedHosts []string`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `Type Limited`

            The type of the object. Always `limited`.

            - `const LimitedLimited Limited = "limited"`

      - `SecretName string`

        The environment variable name that receives the placeholder in the sandbox.

      - `Type EnvironmentVariable`

        The type of the object. Always `environment_variable`.

        - `const EnvironmentVariableEnvironmentVariable EnvironmentVariable = "environment_variable"`

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the credential was created.

  - `Metadata map[string, string]`

    Application-defined key-value pairs associated with this credential.

  - `Name string`

    The human-readable name of the credential.

  - `Object VaultCredential`

    The object type. Always `vault.credential`.

    - `const VaultCredentialVaultCredential VaultCredential = "vault.credential"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `VaultID string`

    The ID of the vault containing this credential.

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
  credential, err := client.Beta.Agents.Vaults.Credentials.Update(
    context.TODO(),
    "vault_id",
    "credential_id",
    openai.BetaAgentVaultCredentialUpdateParams{
      Metadata: map[string]string{
      },
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", credential.ID)
}
```

#### Response

```json
{
  "id": "id",
  "auth": {
    "expires_at": "expires_at",
    "mcp_server_url": "mcp_server_url",
    "refresh": {
      "client_id": "client_id",
      "resource": "resource",
      "scope": "scope",
      "token_endpoint": "token_endpoint",
      "token_endpoint_auth": {
        "type": "none"
      }
    },
    "type": "mcp_oauth"
  },
  "created_at": 0,
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "vault.credential",
  "updated_at": 0,
  "vault_id": "vault_id"
}
```

## Domain Types

### Credential

- `type Credential struct{…}`

  Metadata for a stored credential. Secret values are never returned.

  - `ID string`

    The ID of the credential.

  - `Auth CredentialAuthUnion`

    The authentication method and non-secret configuration of the credential.

    - `type CredentialAuthMcpOAuth struct{…}`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `ExpiresAt string`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Refresh CredentialAuthMcpOAuthRefresh`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `ClientID string`

          The OAuth client ID used when requesting a new access token.

        - `Resource string`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `Scope string`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `TokenEndpoint string`

          The HTTPS OAuth token endpoint used for refresh.

        - `TokenEndpointAuth McpOAuthTokenEndpointAuthUnion`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `type McpOAuthTokenEndpointAuthNone struct{…}`

            Sends the client ID without a client secret.

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `type McpOAuthTokenEndpointAuthClientSecretBasic struct{…}`

            Sends the client ID and secret using HTTP Basic authentication.

            - `Type ClientSecretBasic`

              The type of the object. Always `client_secret_basic`.

              - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

          - `type McpOAuthTokenEndpointAuthClientSecretPost struct{…}`

            Sends the client ID and secret in the token request body.

            - `Type ClientSecretPost`

              The type of the object. Always `client_secret_post`.

              - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

      - `Type McpOAuth`

        The type of the object. Always `mcp_oauth`.

        - `const McpOAuthMcpOAuth McpOAuth = "mcp_oauth"`

    - `type CredentialAuthStaticBearer struct{…}`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Type StaticBearer`

        The type of the object. Always `static_bearer`.

        - `const StaticBearerStaticBearer StaticBearer = "static_bearer"`

    - `type CredentialAuthEnvironmentVariable struct{…}`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `Networking CredentialNetworkingUnion`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `type CredentialNetworkingUnrestricted struct{…}`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `Type Unrestricted`

            The type of the object. Always `unrestricted`.

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type CredentialNetworkingLimited struct{…}`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `AllowedHosts []string`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `Type Limited`

            The type of the object. Always `limited`.

            - `const LimitedLimited Limited = "limited"`

      - `SecretName string`

        The environment variable name that receives the placeholder in the sandbox.

      - `Type EnvironmentVariable`

        The type of the object. Always `environment_variable`.

        - `const EnvironmentVariableEnvironmentVariable EnvironmentVariable = "environment_variable"`

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the credential was created.

  - `Metadata map[string, string]`

    Application-defined key-value pairs associated with this credential.

  - `Name string`

    The human-readable name of the credential.

  - `Object VaultCredential`

    The object type. Always `vault.credential`.

    - `const VaultCredentialVaultCredential VaultCredential = "vault.credential"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `VaultID string`

    The ID of the vault containing this credential.

### Credential Auth

- `type CredentialAuthUnion interface{…}`

  The authentication configuration of a vault credential, excluding secrets.

  - `type CredentialAuthMcpOAuth struct{…}`

    Public metadata for an OAuth credential; tokens and client secrets are never returned.

    - `ExpiresAt string`

      When the OAuth access token expires, as an RFC 3339 timestamp, if known.

    - `McpServerURL string`

      The HTTPS MCP server URL authorized by this credential.

    - `Refresh CredentialAuthMcpOAuthRefresh`

      Public refresh metadata without refresh tokens or OAuth client secrets.

      - `ClientID string`

        The OAuth client ID used when requesting a new access token.

      - `Resource string`

        The resource URI sent to the OAuth token endpoint during refresh, if configured.

      - `Scope string`

        Space-separated OAuth scopes requested during refresh, if configured.

      - `TokenEndpoint string`

        The HTTPS OAuth token endpoint used for refresh.

      - `TokenEndpointAuth McpOAuthTokenEndpointAuthUnion`

        How the OAuth client authenticates to the token endpoint, excluding its client secret.

        - `type McpOAuthTokenEndpointAuthNone struct{…}`

          Sends the client ID without a client secret.

          - `Type None`

            The type of the object. Always `none`.

            - `const NoneNone None = "none"`

        - `type McpOAuthTokenEndpointAuthClientSecretBasic struct{…}`

          Sends the client ID and secret using HTTP Basic authentication.

          - `Type ClientSecretBasic`

            The type of the object. Always `client_secret_basic`.

            - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

        - `type McpOAuthTokenEndpointAuthClientSecretPost struct{…}`

          Sends the client ID and secret in the token request body.

          - `Type ClientSecretPost`

            The type of the object. Always `client_secret_post`.

            - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

    - `Type McpOAuth`

      The type of the object. Always `mcp_oauth`.

      - `const McpOAuthMcpOAuth McpOAuth = "mcp_oauth"`

  - `type CredentialAuthStaticBearer struct{…}`

    Metadata for a bearer-token credential, without automatic OAuth refresh.

    - `McpServerURL string`

      The HTTPS MCP server URL authorized by this credential.

    - `Type StaticBearer`

      The type of the object. Always `static_bearer`.

      - `const StaticBearerStaticBearer StaticBearer = "static_bearer"`

  - `type CredentialAuthEnvironmentVariable struct{…}`

    Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

    - `Networking CredentialNetworkingUnion`

      The destinations where the proxy can substitute the secret, subject to the environment network policy.

      - `type CredentialNetworkingUnrestricted struct{…}`

        Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

        - `Type Unrestricted`

          The type of the object. Always `unrestricted`.

          - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

      - `type CredentialNetworkingLimited struct{…}`

        Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

        - `AllowedHosts []string`

          The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

        - `Type Limited`

          The type of the object. Always `limited`.

          - `const LimitedLimited Limited = "limited"`

    - `SecretName string`

      The environment variable name that receives the placeholder in the sandbox.

    - `Type EnvironmentVariable`

      The type of the object. Always `environment_variable`.

      - `const EnvironmentVariableEnvironmentVariable EnvironmentVariable = "environment_variable"`

### Credential Auth Create Param

- `type CredentialAuthCreateParamUnionResp interface{…}`

  Authentication credentials for an MCP server or an OpenAI-hosted environment.

  - `CredentialAuthCreateParamMcpOAuthResp`

    - `AccessToken string`

      A write-only OAuth access token; never returned by credential resources.

    - `McpServerURL string`

      The HTTPS MCP server URL authorized by this credential.

    - `Type McpOAuth`

      The type of the object. Always `mcp_oauth`.

      - `const McpOAuthMcpOAuth McpOAuth = "mcp_oauth"`

    - `ExpiresAt string`

      When the OAuth access token expires, as an RFC 3339 timestamp, if known.

    - `Refresh CredentialAuthCreateParamMcpOAuthRefreshResp`

      Optional refresh configuration for an HTTPS OAuth token endpoint.

      - `ClientID string`

        The OAuth client ID used when requesting a new access token.

      - `RefreshToken string`

        The refresh token to store. This secret is never returned in credential resources.

      - `TokenEndpoint string`

        The HTTPS OAuth token endpoint used to exchange the refresh token for a new access token.

      - `TokenEndpointAuth McpOAuthTokenEndpointAuthCreateParamUnionResp`

        How the OAuth client authenticates to the token endpoint.

        - `McpOAuthTokenEndpointAuthCreateParamNoneResp`

          - `Type None`

            The type of the object. Always `none`.

            - `const NoneNone None = "none"`

        - `McpOAuthTokenEndpointAuthCreateParamClientSecretBasicResp`

          - `ClientSecret string`

            The OAuth client secret to store. Never returned in credential resources.

          - `Type ClientSecretBasic`

            The type of the object. Always `client_secret_basic`.

            - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

        - `McpOAuthTokenEndpointAuthCreateParamClientSecretPostResp`

          - `ClientSecret string`

            The OAuth client secret to store. Never returned in credential resources.

          - `Type ClientSecretPost`

            The type of the object. Always `client_secret_post`.

            - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

      - `Resource string`

        The resource URI to send to the OAuth token endpoint during refresh, if required.

      - `Scope string`

        Space-separated OAuth scopes to request during refresh, if required.

  - `CredentialAuthCreateParamStaticBearerResp`

    - `Token string`

      The bearer token to store. This secret is never returned in credential resources.

    - `McpServerURL string`

      The HTTPS MCP server URL authorized by this credential.

    - `Type StaticBearer`

      The type of the object. Always `static_bearer`.

      - `const StaticBearerStaticBearer StaticBearer = "static_bearer"`

  - `CredentialAuthCreateParamEnvironmentVariableResp`

    - `Networking CredentialNetworkingParamUnionResp`

      The destinations where the proxy can substitute this secret. The environment network policy must also allow them.

      - `CredentialNetworkingParamUnrestrictedResp`

        - `Type Unrestricted`

          The type of the object. Always `unrestricted`.

          - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

      - `CredentialNetworkingParamLimitedResp`

        - `AllowedHosts []string`

          The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

        - `Type Limited`

          The type of the object. Always `limited`.

          - `const LimitedLimited Limited = "limited"`

    - `SecretName string`

      The environment variable name that receives the placeholder, such as `SERVICE_API_KEY`. Use ASCII letters, digits, and underscores, starting with a letter or underscore. Names starting with `CODEX_` and managed proxy or certificate variable names are reserved.

    - `SecretValue string`

      The write-only secret to store. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `Type EnvironmentVariable`

      The type of the object. Always `environment_variable`.

      - `const EnvironmentVariableEnvironmentVariable EnvironmentVariable = "environment_variable"`

### Credential Auth Rotate Param

- `type CredentialAuthRotateParamUnionResp interface{…}`

  Updates to a vault credential without changing its authentication method or destination configuration.

  - `CredentialAuthRotateParamMcpOAuthResp`

    - `Type McpOAuth`

      The type of the object. Always `mcp_oauth`.

      - `const McpOAuthMcpOAuth McpOAuth = "mcp_oauth"`

    - `AccessToken string`

      A write-only replacement OAuth access token.

    - `ExpiresAt string`

      The replacement expiry as an RFC 3339 timestamp, or `null` to clear it. Omitting this field preserves the expiry unless a new access token is supplied, in which case the expiry is cleared.

    - `Refresh CredentialAuthRotateParamMcpOAuthRefreshResp`

      Optional write-only refresh-token and client-secret updates.

      - `RefreshToken string`

        The replacement refresh token. Omit or pass `null` to keep the stored token. This secret is never returned in resources.

      - `Scope string`

        Replacement space-separated OAuth scopes for refresh requests. Omit to keep the scopes, or pass `null` to stop sending a scope parameter.

      - `TokenEndpointAuth McpOAuthTokenEndpointAuthRotateParamUnionResp`

        Client-secret updates for the existing token endpoint authentication method.

        - `McpOAuthTokenEndpointAuthRotateParamClientSecretBasicResp`

          - `Type ClientSecretBasic`

            The type of the object. Always `client_secret_basic`.

            - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

          - `ClientSecret string`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

        - `McpOAuthTokenEndpointAuthRotateParamClientSecretPostResp`

          - `Type ClientSecretPost`

            The type of the object. Always `client_secret_post`.

            - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

          - `ClientSecret string`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

  - `CredentialAuthRotateParamStaticBearerResp`

    - `Token string`

      The replacement bearer token. This secret is never returned in credential resources.

    - `Type StaticBearer`

      The type of the object. Always `static_bearer`.

      - `const StaticBearerStaticBearer StaticBearer = "static_bearer"`

  - `CredentialAuthRotateParamEnvironmentVariableResp`

    - `SecretValue string`

      The write-only replacement secret. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `Type EnvironmentVariable`

      The type of the object. Always `environment_variable`.

      - `const EnvironmentVariableEnvironmentVariable EnvironmentVariable = "environment_variable"`

### Credential Deleted

- `type CredentialDeleted struct{…}`

  Confirmation that a vault credential was deleted.

  - `ID string`

    The ID of the deleted credential.

  - `Deleted bool`

    Whether the resource was deleted. Always `true`.

  - `Object VaultCredentialDeleted`

    The object type. Always `vault.credential.deleted`.

    - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault.credential.deleted"`

### Credential Networking

- `type CredentialNetworkingUnion interface{…}`

  Destination permissions for an environment-variable credential. These do not grant network access to the environment.

  - `type CredentialNetworkingUnrestricted struct{…}`

    Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

    - `Type Unrestricted`

      The type of the object. Always `unrestricted`.

      - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

  - `type CredentialNetworkingLimited struct{…}`

    Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

    - `AllowedHosts []string`

      The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

    - `Type Limited`

      The type of the object. Always `limited`.

      - `const LimitedLimited Limited = "limited"`

### Credential Networking Param

- `type CredentialNetworkingParamUnionResp interface{…}`

  Destination permissions for an environment-variable credential. These do not grant network access to the environment.

  - `CredentialNetworkingParamUnrestrictedResp`

    - `Type Unrestricted`

      The type of the object. Always `unrestricted`.

      - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

  - `CredentialNetworkingParamLimitedResp`

    - `AllowedHosts []string`

      The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

    - `Type Limited`

      The type of the object. Always `limited`.

      - `const LimitedLimited Limited = "limited"`

### Mcp OAuth Token Endpoint Auth

- `type McpOAuthTokenEndpointAuthUnion interface{…}`

  The client authentication method used for OAuth token refresh.

  - `type McpOAuthTokenEndpointAuthNone struct{…}`

    Sends the client ID without a client secret.

    - `Type None`

      The type of the object. Always `none`.

      - `const NoneNone None = "none"`

  - `type McpOAuthTokenEndpointAuthClientSecretBasic struct{…}`

    Sends the client ID and secret using HTTP Basic authentication.

    - `Type ClientSecretBasic`

      The type of the object. Always `client_secret_basic`.

      - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

  - `type McpOAuthTokenEndpointAuthClientSecretPost struct{…}`

    Sends the client ID and secret in the token request body.

    - `Type ClientSecretPost`

      The type of the object. Always `client_secret_post`.

      - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

### Mcp OAuth Token Endpoint Auth Create Param

- `type McpOAuthTokenEndpointAuthCreateParamUnionResp interface{…}`

  Client authentication credentials for OAuth token refresh.

  - `McpOAuthTokenEndpointAuthCreateParamNoneResp`

    - `Type None`

      The type of the object. Always `none`.

      - `const NoneNone None = "none"`

  - `McpOAuthTokenEndpointAuthCreateParamClientSecretBasicResp`

    - `ClientSecret string`

      The OAuth client secret to store. Never returned in credential resources.

    - `Type ClientSecretBasic`

      The type of the object. Always `client_secret_basic`.

      - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

  - `McpOAuthTokenEndpointAuthCreateParamClientSecretPostResp`

    - `ClientSecret string`

      The OAuth client secret to store. Never returned in credential resources.

    - `Type ClientSecretPost`

      The type of the object. Always `client_secret_post`.

      - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

### Mcp OAuth Token Endpoint Auth Rotate Param

- `type McpOAuthTokenEndpointAuthRotateParamUnionResp interface{…}`

  Client-secret updates that preserve the credential's OAuth authentication method.

  - `McpOAuthTokenEndpointAuthRotateParamClientSecretBasicResp`

    - `Type ClientSecretBasic`

      The type of the object. Always `client_secret_basic`.

      - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

    - `ClientSecret string`

      The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

  - `McpOAuthTokenEndpointAuthRotateParamClientSecretPostResp`

    - `Type ClientSecretPost`

      The type of the object. Always `client_secret_post`.

      - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

    - `ClientSecret string`

      The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

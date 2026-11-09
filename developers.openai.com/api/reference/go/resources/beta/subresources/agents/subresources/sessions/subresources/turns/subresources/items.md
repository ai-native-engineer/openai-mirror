<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/sessions/subresources/turns/subresources/items/ -->

# Items

## List agent session turn items

`client.Beta.Agents.Sessions.Turns.Items.List(ctx, sessionID, turnID, query) (*ConversationCursorPage[AgentSessionItemUnion], error)`

**get** `/agents/sessions/{session_id}/turns/{turn_id}/items`

Lists items belonging to one root-agent turn, including its interactions with subagents. See [inspecting agent output](/api/docs/guides/agents-api/observability).

### Parameters

- `sessionID string`

  `minLength: 0`, `maxLength: 1048576`

- `turnID string`

  `minLength: 0`, `maxLength: 1048576`

- `query BetaAgentSessionTurnItemListParams`

  - `After param.Field[string]`

    Return items after this cursor in the selected order. Pass the previous response's last_id, which can differ from the last item's ID.

    `minLength: 0`, `maxLength: 1048576`

  - `Limit param.Field[int64]`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

    `format: int64`, `minimum: 1`, `maximum: 100`

  - `Order param.Field[BetaAgentSessionTurnItemListParamsOrder]`

    The order in which resources are returned. Defaults to `desc`.

    - `const BetaAgentSessionTurnItemListParamsOrderAsc BetaAgentSessionTurnItemListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentSessionTurnItemListParamsOrderDesc BetaAgentSessionTurnItemListParamsOrder = "desc"`

      Returns resources in descending order.

### Returns

- `type AgentSessionItemUnion interface{…}`

  An item associated with a session turn.

  - `type AgentSessionMessage struct{…}`

    A user or assistant message recorded in a session.

    - `ID string`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

      `minLength: 0`

    - `Content []AgentSessionMessageContentUnion`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      `minItems: 0`, `maxItems: 2000`

      - `type AgentSessionMessageContentInputText struct{…}`

        Text supplied by the user.

        - `Text string`

          The text supplied by the user.

          `minLength: 0`

        - `Type InputText`

          The type of the object. Always `input_text`.

          - `const InputTextInputText InputText = "input_text"`

      - `type AgentSessionMessageContentInputImage struct{…}`

        An image supplied by the user.

        - `ImageURL string`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

          `minLength: 0`

        - `Type InputImage`

          The type of the object. Always `input_image`.

          - `const InputImageInputImage InputImage = "input_image"`

      - `type AgentSessionMessageContentOutputText struct{…}`

        Text produced by the assistant.

        - `Text string`

          The text produced by the assistant.

          `minLength: 0`

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

      `minLength: 0`

    - `Type Message`

      The item type. Always `message`.

      - `const MessageMessage Message = "message"`

  - `type AgentReasoningItem struct{…}`

    A reasoning item produced by the agent.

    - `ID string`

      The ID of the reasoning item.

      `minLength: 0`

    - `Status AgentOutputItemStatus`

      The status of the reasoning item.

    - `Summary []SummaryText`

      The reasoning summaries produced by the agent.

      `minItems: 0`, `maxItems: 2000`

      - `Text string`

        The reasoning summary text.

        `minLength: 0`

      - `Type SummaryText`

        The content type. Always `summary_text`.

        - `const SummaryTextSummaryText SummaryText = "summary_text"`

    - `TurnID string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `Type Reasoning`

      The item type. Always `reasoning`.

      - `const ReasoningReasoning Reasoning = "reasoning"`

  - `type AgentFunctionCallItem struct{…}`

    A function call produced by the agent.

    - `ID string`

      The ID of the function call item.

      `minLength: 0`

    - `Arguments any`

      The arguments to pass to the function.

    - `CallID string`

      The ID used to submit the function result.

      `minLength: 0`

    - `Name string`

      The name of the function to call.

      `minLength: 0`

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

      `minLength: 0`

    - `Type FunctionCall`

      The item type. Always `function_call`.

      - `const FunctionCallFunctionCall FunctionCall = "function_call"`

  - `type AgentSessionItemFunctionCallOutput struct{…}`

    The result supplied for a function call.

    - `ID string`

      The ID of the function call output item.

      `minLength: 0`

    - `CallID string`

      The ID of the function call that produced this output.

      `minLength: 0`

    - `Error string`

      The error message, if the call failed.

      `minLength: 0`

    - `Output AgentFunctionCallOutputUnion`

      The function result, if the call succeeded.

      - `string`

      - `type AgentFunctionCallOutputArray []InputContentUnion`

        - `type InputContentInputText struct{…}`

          Text input recorded in a session item.

          - `Text string`

            The text supplied to the agent.

            `minLength: 0`

          - `Type InputText`

            The type of the object. Always `input_text`.

            - `const InputTextInputText InputText = "input_text"`

        - `type InputContentInputImage struct{…}`

          Image input recorded in a session item.

          - `ImageURL string`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

            `minLength: 0`

          - `Type InputImage`

            The type of the object. Always `input_image`.

            - `const InputImageInputImage InputImage = "input_image"`

    - `Status AgentFunctionCallStatus`

      The status of the function call.

    - `TurnID string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `Type FunctionCallOutput`

      The item type. Always `function_call_output`.

      - `const FunctionCallOutputFunctionCallOutput FunctionCallOutput = "function_call_output"`

  - `type AgentSessionItemAgentMessage struct{…}`

    A message exchanged between agent threads.

    - `ID string`

      The ID of the message.

      `minLength: 0`

    - `Content []AgentContentUnion`

      The content exchanged between the agents.

      `minItems: 0`, `maxItems: 2000`

      - `type OutputText struct{…}`

        A text content part produced by the agent.

        - `Text string`

          The text produced by the agent.

          `minLength: 0`

        - `Type OutputText`

          The content type. Always `output_text`.

          - `const OutputTextOutputText OutputText = "output_text"`

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

        - `EncryptedContent string`

          The encrypted content payload.

          `minLength: 0`

        - `Type EncryptedContent`

          The content type. Always `encrypted_content`.

          - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

    - `RecipientAgentID string`

      The ID or name of the receiving agent.

      `minLength: 0`

    - `SenderAgentID string`

      The ID or name of the sending agent.

      `minLength: 0`

    - `TurnID string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `Type AgentMessage`

      The item type. Always `agent_message`.

      - `const AgentMessageAgentMessage AgentMessage = "agent_message"`

  - `type AgentMcpCallItem struct{…}`

    A call to a tool on an MCP server.

    - `ID string`

      The ID of the MCP call item.

      `minLength: 0`

    - `Arguments any`

      The arguments passed to the MCP tool.

    - `Error any`

      The error returned by the MCP tool, if any.

    - `Name string`

      The name of the MCP tool.

      `minLength: 0`

    - `Output any`

      The output returned by the MCP tool, if any.

    - `ServerLabel string`

      The label of the MCP server.

      `minLength: 0`

    - `Status AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `Type McpCall`

      The item type. Always `mcp_call`.

      - `const McpCallMcpCall McpCall = "mcp_call"`

  - `type AgentSessionItemComputerUseCall struct{…}`

    One execution of the platform-provided computer-use capability.

    - `ID string`

      The ID of the activity item.

      `minLength: 0`

    - `Output AgentSessionItemComputerUseCallOutput`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `ImageURL string`

        The complete JPEG image as a base64 data URL.

        `minLength: 0`

      - `Type ComputerScreenshot`

        The content type. Always `computer_screenshot`.

        - `const ComputerScreenshotComputerScreenshot ComputerScreenshot = "computer_screenshot"`

    - `Status AgentFunctionCallStatus`

      The execution status of the activity.

    - `Title string`

      A model-generated description of the activity, when available.

      `minLength: 0`

    - `TurnID string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `Type ComputerUseCall`

      The item type. Always `computer_use_call`.

      - `const ComputerUseCallComputerUseCall ComputerUseCall = "computer_use_call"`

  - `type AgentSessionItemComputerUseApprovalRequest struct{…}`

    A credential-free history record of the emitted login request.

    - `ID string`

      The stable history item ID.

      `minLength: 0`

    - `Request AgentSessionItemComputerUseApprovalRequestRequest`

      A registered form awaiting the application's response.

      - `CredentialOrigin string`

        The registered form or frame origin where values will be entered.

        `minLength: 0`

      - `Fields []AgentSessionItemComputerUseApprovalRequestRequestField`

        Controls to render. All submitted values are sensitive.

        `minItems: 0`, `maxItems: 2000`

        - `ID string`

          The field ID to submit as field_id in a fields entry.

          `minLength: 0`

        - `Label string`

          The label to display beside the control.

          `minLength: 0`

        - `Required bool`

          Whether this control requires a nonempty value.

        - `Type string`

          The rendering type, such as email, password, or text.

          `minLength: 0`

      - `Options []AgentSessionItemComputerUseApprovalRequestRequestOption`

        Sign-in methods. Empty for a plain form.

        `minItems: 0`, `maxItems: 2000`

        - `ID string`

          The option ID to submit as selected_option.

          `minLength: 0`

        - `FieldIDs []string`

          IDs from the registered fields that this method accepts.

          `minItems: 0`, `maxItems: 2000`

        - `Label string`

          The method label to display.

          `minLength: 0`

      - `Reason string`

        Why the agent needs the user to sign in.

        `minLength: 0`

      - `Type BrowserAuthentication`

        The type of the object. Always `browser_authentication`.

        - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

    - `RequestID string`

      `minLength: 0`

    - `TurnID string`

      `minLength: 0`

    - `Type ComputerUseApprovalRequest`

      The item type. Always computer_use_approval_request.

      - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

  - `type AgentSessionItemComputerUseApprovalRequestResult struct{…}`

    A credential-free record of an admitted response, not proof of completion.

    - `ID string`

      The stable history item ID.

      `minLength: 0`

    - `RequestID string`

      The registered request answered by this item.

      `minLength: 0`

    - `Response AgentSessionItemComputerUseApprovalRequestResultResponseUnion`

      The admitted response, without submitted credential values.

      - `type AgentSessionItemComputerUseApprovalRequestResultResponseSubmit struct{…}`

        - `Action Submit`

          - `const SubmitSubmit Submit = "submit"`

        - `SelectedOption string`

          The chosen sign-in method, or null when no options were offered.

          `minLength: 0`

        - `Type BrowserAuthentication`

          - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

      - `type AgentSessionItemComputerUseApprovalRequestResultResponseCancel struct{…}`

        - `Action Cancel`

          - `const CancelCancel Cancel = "cancel"`

        - `Type BrowserAuthentication`

          - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

    - `TurnID string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `Type ComputerUseApprovalRequestResult`

      - `const ComputerUseApprovalRequestResultComputerUseApprovalRequestResult ComputerUseApprovalRequestResult = "computer_use_approval_request_result"`

  - `type AgentWebSearchCallItem struct{…}`

    A web search call produced by the agent.

    - `ID string`

      The ID of the web search call.

      `minLength: 0`

    - `Action WebSearchActionUnion`

      The action performed by the web search tool.

      - `type WebSearchActionSearch struct{…}`

        A search query or group of search queries.

        - `Queries []string`

          The search queries, when multiple queries were used.

          `minItems: 0`, `maxItems: 2000`

        - `Query string`

          The search query, when a single query was used.

          `minLength: 0`

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

          `minLength: 0`

      - `type WebSearchActionFindInPage struct{…}`

        Finds text within a web page.

        - `Pattern string`

          The text pattern that was searched for.

          `minLength: 0`

        - `Type FindInPage`

          The type of the object. Always `find_in_page`.

          - `const FindInPageFindInPage FindInPage = "find_in_page"`

        - `URL string`

          The URL of the page that was searched.

          `minLength: 0`

      - `type WebSearchActionOther struct{…}`

        Another web search action.

        - `Type Other`

          The type of the object. Always `other`.

          - `const OtherOther Other = "other"`

    - `Status AgentOutputItemStatus`

      The status of the web search call.

    - `TurnID string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `Type WebSearchCall`

      The item type. Always `web_search_call`.

      - `const WebSearchCallWebSearchCall WebSearchCall = "web_search_call"`

  - `type AgentCommandExecutionItem struct{…}`

    A command execution produced by the agent.

    - `ID string`

      The ID of the command execution item.

      `minLength: 0`

    - `Command string`

      The command that was executed.

      `minLength: 0`

    - `Cwd string`

      The working directory used to execute the command.

      `minLength: 0`

    - `DurationMs int64`

      The command duration in milliseconds.

      `format: int64`

    - `ExitCode int64`

      The process exit code, if the command completed.

      `format: int64`

    - `Output string`

      The command output, if available.

      `minLength: 0`

    - `Status AgentFunctionCallStatus`

      The status of the command execution.

    - `TurnID string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `Type CommandExecution`

      The item type. Always `command_execution`.

      - `const CommandExecutionCommandExecution CommandExecution = "command_execution"`

  - `type AgentCreateSubagentCallItem struct{…}`

    A request to spawn a subagent.

    - `ID string`

      The ID of the tool call item.

      `minLength: 0`

    - `AgentID string`

      The ID of the agent that requested the subagent.

      `minLength: 0`

    - `Content []AgentContentUnion`

      The task given to the spawned agent.

      `minItems: 0`, `maxItems: 2000`

      - `type OutputText struct{…}`

        A text content part produced by the agent.

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

    - `Model string`

      The model requested for the spawned agent.

      `minLength: 0`

    - `ReasoningEffort string`

      The reasoning effort requested for the spawned agent.

      `minLength: 0`

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `Type CreateSubagentCall`

      The item type. Always `create_subagent_call`.

      - `const CreateSubagentCallCreateSubagentCall CreateSubagentCall = "create_subagent_call"`

  - `type AgentSendSubagentInputCallItem struct{…}`

    A request to send input to another agent.

    - `ID string`

      The ID of the tool call item.

      `minLength: 0`

    - `Content []AgentContentUnion`

      The input sent to the receiving agent.

      `minItems: 0`, `maxItems: 2000`

      - `type OutputText struct{…}`

        A text content part produced by the agent.

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

    - `RecipientAgentID string`

      The ID of the agent receiving the input.

      `minLength: 0`

    - `SenderAgentID string`

      The ID of the agent sending the input.

      `minLength: 0`

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `Type SendSubagentInputCall`

      The item type. Always `send_subagent_input_call`.

      - `const SendSubagentInputCallSendSubagentInputCall SendSubagentInputCall = "send_subagent_input_call"`

  - `type AgentResumeSubagentCallItem struct{…}`

    A request to resume a subagent.

    - `ID string`

      The ID of the tool call item.

      `minLength: 0`

    - `RecipientAgentID string`

      The ID of the agent to resume.

      `minLength: 0`

    - `SenderAgentID string`

      The ID of the agent requesting the resume.

      `minLength: 0`

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `Type ResumeSubagentCall`

      The item type. Always `resume_subagent_call`.

      - `const ResumeSubagentCallResumeSubagentCall ResumeSubagentCall = "resume_subagent_call"`

  - `type AgentWaitForSubagentsCallItem struct{…}`

    A request to wait for one or more subagents.

    - `ID string`

      The ID of the tool call item.

      `minLength: 0`

    - `RecipientAgentIDs []string`

      The IDs of the agents to wait for.

      `minItems: 0`, `maxItems: 2000`

    - `SenderAgentID string`

      The ID of the agent waiting for results.

      `minLength: 0`

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `Type WaitForSubagentsCall`

      The item type. Always `wait_for_subagents_call`.

      - `const WaitForSubagentsCallWaitForSubagentsCall WaitForSubagentsCall = "wait_for_subagents_call"`

  - `type AgentInterruptSubagentCallItem struct{…}`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `ID string`

      The ID of the tool call item.

      `minLength: 0`

    - `RecipientAgentID string`

      The ID of the agent to interrupt.

      `minLength: 0`

    - `SenderAgentID string`

      The ID of the agent requesting the interrupt.

      `minLength: 0`

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `Type InterruptSubagentCall`

      The item type. Always `interrupt_subagent_call`.

      - `const InterruptSubagentCallInterruptSubagentCall InterruptSubagentCall = "interrupt_subagent_call"`

  - `type AgentCloseSubagentCallItem struct{…}`

    A request to close a subagent.

    - `ID string`

      The ID of the tool call item.

      `minLength: 0`

    - `RecipientAgentID string`

      The ID of the agent to close.

      `minLength: 0`

    - `SenderAgentID string`

      The ID of the agent requesting the close.

      `minLength: 0`

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `Type CloseSubagentCall`

      The item type. Always `close_subagent_call`.

      - `const CloseSubagentCallCloseSubagentCall CloseSubagentCall = "close_subagent_call"`

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
  page, err := client.Beta.Agents.Sessions.Turns.Items.List(
    context.TODO(),
    "session_id",
    "turn_id",
    openai.BetaAgentSessionTurnItemListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

#### 200 — Example

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

<!-- source: https://learn.chatgpt.com/ko-KR/docs/config-file/config-reference -->

이 페이지에서 Codex 구성 파일에 대한 참조 정보를 검색할 수 있습니다. 개념 설명과 예시는 [기본 구성](/ko-KR/codex/config-file/config-basic)과 [고급 구성](/ko-KR/codex/config-file/config-advanced)부터 살펴보세요.

## `config.toml`

사용자 수준 구성은 `~/.codex/config.toml`에 저장됩니다. `.codex/config.toml` 파일에서 프로젝트 범위의 설정을 재정의할 수도 있습니다. Codex는 사용자가 프로젝트를 신뢰할 때만 프로젝트 범위 구성 파일을 로드합니다.

프로젝트 범위 구성에서는 머신 로컬 공급자, 인증,
호스트가 관리하는 앱 요청 메타데이터, 알림, 구성 프로필 선택,
텔레메트리 라우팅 키를 재정의할 수 없습니다. Codex는 `openai_base_url`,
`chatgpt_base_url`, `apps_mcp_product_sku`, `model_provider`,
`model_providers`, `notify`, `profile`, `profiles`,
`experimental_realtime_ws_base_url`, `otel`이
프로젝트 로컬 `.codex/config.toml` 파일에 있으면 무시합니다. 공급자, 알림, 텔레메트리
키는 사용자 수준 구성에 넣으세요. 구성 [프로필 파일](/ko-KR/codex/config-file/config-advanced#profiles)은
`config.toml` 파일과 같은 디렉터리의 `$CODEX_HOME/profile-name.config.toml`에 저장됩니다.
`--profile profile-name` 옵션으로 원하는 프로필을 선택하세요.

샌드박스 및 승인 키(`approval_policy`, `sandbox_mode`, `sandbox_workspace_write.*`)에 대해서는 이 참조 자료와 [샌드박스 및 승인](/ko-KR/codex/agent-approvals-security#sandbox-and-approvals), [쓰기 가능한 루트의 보호된 경로](/ko-KR/codex/agent-approvals-security#protected-paths-in-writable-roots), [네트워크 액세스](/ko-KR/codex/agent-approvals-security#network-access)를 함께 참고하세요. 베타 권한 프로필은 [권한](/ko-KR/codex/permissions)을 참고하세요.

<ConfigTable
  options={[
    {
      key: "model",
      type: "string",
      description: "사용할 모델입니다(예: `gpt-5.5`).",
    },
    {
      key: "review_model",
      type: "string",
      description:
        "`/review`에 사용할 모델을 별도로 지정합니다(선택 사항, 기본값: 현재 세션 모델).",
    },
    {
      key: "model_provider",
      type: "string",
      description: "`model_providers`의 공급자 ID입니다(기본값: `openai`).",
    },
    {
      key: "openai_base_url",
      type: "string",
      description:
        "기본 제공 `openai` 모델 공급자의 기본 URL을 재정의합니다.",
    },
    {
      key: "model_context_window",
      type: "number",
      description: "활성 모델에서 사용할 수 있는 컨텍스트 윈도우의 토큰 수입니다.",
    },
    {
      key: "model_auto_compact_token_limit",
      type: "number",
      description:
        "대화 기록의 자동 컨텍스트 압축을 시작하는 토큰 임계값입니다(설정하지 않으면 모델 기본값 사용).",
    },
    {
      key: "model_auto_compact_token_limit_scope",
      type: "total | body_after_prefix",
      description:
        "자동 컨텍스트 압축 임계값을 계산할 때 활성 컨텍스트 전체(`total`, 기본값)를 포함할지, 이어받은 컨텍스트 압축 윈도우의 접두사 이후 증가분(`body_after_prefix`)만 포함할지 제어합니다.",
    },
    {
      key: "model_catalog_json",
      type: "string (path)",
      description:
        "시작 시 로드할 JSON 모델 카탈로그의 경로입니다(선택 사항). 선택한 `$CODEX_HOME/profile-name.config.toml` 프로필 파일에서 프로필별로 이 경로를 재정의할 수 있습니다.",
    },
    {
      key: "oss_provider",
      type: "lmstudio | ollama",
      description:
        "`--oss`로 실행할 때 사용하는 기본 로컬 공급자입니다(설정하지 않으면 선택 프롬프트 표시).",
    },
    {
      key: "approval_policy",
      type: "untrusted | on-request | never | { granular = { sandbox_approval = bool, rules = bool, mcp_elicitations = bool, request_permissions = bool, skill_approval = bool } }",
      description:
        "명령어를 실행하기 전에 Codex가 승인을 기다리며 일시 중지하는 시점을 제어합니다. `approval_policy = { granular = { ... } }`를 사용하면 다른 프롬프트는 대화형으로 유지하면서 특정 프롬프트 범주를 허용하거나 자동으로 거부할 수도 있습니다. `on-failure`는 사용 중단 예정(deprecated)입니다. 대화형 실행에는 `on-request`, 비대화형 실행에는 `never`를 사용하세요.",
    },
    {
      key: "approval_policy.granular.sandbox_approval",
      type: "boolean",
      description:
        "`true`로 설정하면 샌드박스 권한 상승 승인 프롬프트 표시를 허용합니다.",
    },
    {
      key: "approval_policy.granular.rules",
      type: "boolean",
      description:
        "`true`로 설정하면 execpolicy의 `prompt` 규칙에 따른 승인 요청 표시를 허용합니다.",
    },
    {
      key: "approval_policy.granular.mcp_elicitations",
      type: "boolean",
      description:
        "`true`로 설정하면 MCP 유도 프롬프트가 자동으로 거부되지 않고 표시되도록 허용합니다.",
    },
    {
      key: "approval_policy.granular.request_permissions",
      type: "boolean",
      description:
        "`true`로 설정하면 `request_permissions` 도구의 프롬프트 표시를 허용합니다.",
    },
    {
      key: "approval_policy.granular.skill_approval",
      type: "boolean",
      description:
        "`true`로 설정하면 스킬 스크립트 승인 프롬프트 표시를 허용합니다.",
    },
    {
      key: "approvals_reviewer",
      type: "user | auto_review",
      description:
        "`on-request` 또는 세분화된 승인 정책에서 검토 대상 승인 프롬프트를 검토할 주체입니다. 기본값은 `user`이며, `auto_review`는 검토자 하위 에이전트를 사용합니다. 이 설정은 샌드박스 적용 방식을 변경하지 않으며, 샌드박스 내에서 이미 허용된 작업을 검토하지도 않습니다.",
    },
    {
      key: "auto_review.policy",
      type: "string",
      description:
        "자동 검토에 적용할 로컬 Markdown 정책 지침입니다. 관리형 `guardian_policy_config`가 우선합니다. 빈 값은 무시됩니다.",
    },
    {
      key: "allow_login_shell",
      type: "boolean",
      description:
        "셸 기반 도구에서 로그인 셸 동작을 사용하도록 허용합니다. 기본값은 `true`입니다. `false`로 설정하면 `login = true` 요청이 거부되고, `login`을 생략하면 기본적으로 비로그인 셸을 사용합니다.",
    },
    {
      key: "sandbox_mode",
      type: "read-only | workspace-write | danger-full-access",
      description:
        "명령어 실행 중 파일 시스템 및 네트워크 액세스에 적용되는 샌드박스 정책입니다.",
    },
    {
      key: "sandbox_workspace_write.writable_roots",
      type: "array<string>",
      description:
        "`sandbox_mode = \"workspace-write\"`일 때 추가로 쓰기 가능한 루트입니다.",
    },
    {
      key: "sandbox_workspace_write.network_access",
      type: "boolean",
      description:
        "workspace-write 샌드박스 내에서 아웃바운드 네트워크 액세스를 허용합니다.",
    },
    {
      key: "sandbox_workspace_write.exclude_tmpdir_env_var",
      type: "boolean",
      description:
        "workspace-write 모드의 쓰기 가능한 루트에서 `$TMPDIR`을 제외합니다.",
    },
    {
      key: "sandbox_workspace_write.exclude_slash_tmp",
      type: "boolean",
      description:
        "workspace-write 모드의 쓰기 가능한 루트에서 `/tmp`를 제외합니다.",
    },
    {
      key: "windows.sandbox",
      type: "unelevated | elevated",
      description:
        "Codex를 Windows에서 네이티브로 실행할 때 사용하는 Windows 전용 네이티브 샌드박스 모드입니다.",
    },
    {
      key: "windows.sandbox_private_desktop",
      type: "boolean",
      description:
        "Windows에서 네이티브로 실행할 때는 기본적으로 샌드박스가 적용된 최종 자식 프로세스를 프라이빗 데스크톱에서 실행합니다. 이전 `Winsta0\\\\Default` 동작과의 호환성이 필요한 경우에만 `false`로 설정하세요.",
    },
    {
      key: "browser_use.allow_history_access",
      type: "boolean",
      description:
        "브라우저 방문 기록에 대한 액세스를 제한하려면 `false`로 설정하세요. 관리형 요구 사항으로 이 제한을 강제할 수 있습니다.",
    },
    {
      key: "browser_use.default_origin_policy",
      type: "table",
      description:
        "별도 설정이 없을 때 적용되는 브라우저 오리진 제한입니다. `access`, `uploads`, `downloads`, `full_cdp_access`를 지원하며, 각각 `allow` 또는 `deny`로 설정합니다.",
    },
    {
      key: "browser_use.origins.<origin>",
      type: "table",
      description:
        "`browser_use.default_origin_policy`와 동일한 필드를 사용하는 오리진별 브라우저 제한입니다. HTTP 또는 HTTPS 스킴을 포함하고 필요하면 포트를 지정하세요. 경로, 쿼리, 프래그먼트는 제외하세요. 로컬 설정값으로 관리형 거부 규칙을 완화할 수는 없습니다.",
    },
    {
      key: "computer_use.default_app_access",
      type: "allow | deny",
      description:
        "컴퓨터 사용 기능에서 별도 설정이 없을 때 적용되는 네이티브 앱 액세스 정책입니다. 앱별 항목에서 정책을 지정할 수 있지만, 로컬 구성으로 관리형 제한을 완화할 수는 없습니다.",
    },
    {
      key: "computer_use.macos.bundle_ids",
      type: "map<string, allow | deny>",
      description: "번들 식별자를 키로 사용하는 네이티브 macOS 앱 액세스 설정입니다.",
    },
    {
      key: "computer_use.windows.aumids",
      type: "map<string, allow | deny>",
      description:
        "Application User Model ID(AUMID)를 키로 사용하는 패키지형 Windows 앱 액세스 설정입니다.",
    },
    {
      key: "computer_use.windows.exes",
      type: "array<table>",
      description:
        "Windows 실행 파일 액세스 규칙입니다. 각 규칙에는 `publisher_name`, `product_name`, `access`(`allow` 또는 `deny`)가 필수이며, `binary_name`은 선택 사항입니다.",
    },
    {
      key: "computer_use.windows.always_allowed_app_ids",
      type: "array<string>",
      description:
        "컴퓨터 사용 기능에서 프롬프트 없이 열 수 있는 Windows 앱의 식별자입니다. 목록에 없는 앱은 승인이 필요합니다. 저장된 항목은 ChatGPT 데스크톱 앱의 컴퓨터 사용 설정에서 삭제하세요.",
    },
    {
      key: "notify",
      type: "array<string>",
      description:
        "알림을 위해 호출되는 명령어로, Codex에서 JSON 페이로드를 받습니다.",
    },
    {
      key: "check_for_update_on_startup",
      type: "boolean",
      description:
        "시작할 때 Codex 업데이트를 확인합니다(업데이트를 중앙에서 관리하는 경우에만 false로 설정하세요).",
    },
    {
      key: "feedback.enabled",
      type: "boolean",
      description:
        "모든 로컬 클라이언트에서 `/feedback`을 통한 피드백 제출을 활성화합니다(기본값: true).",
    },
    {
      key: "analytics.enabled",
      type: "boolean",
      description:
        "이 머신 또는 프로필의 분석 기능을 활성화하거나 비활성화합니다. 설정하지 않으면 클라이언트 기본값이 적용됩니다.",
    },
    {
      key: "instructions",
      type: "string",
      description:
        "향후 사용을 위해 남겨둔 설정입니다. 가급적 `model_instructions_file` 또는 `AGENTS.md`를 사용하세요.",
    },
    {
      key: "developer_instructions",
      type: "string",
      description:
        "세션에 추가되는 개발자 지침입니다(선택 사항).",
    },
    {
      key: "log_dir",
      type: "string (path)",
      description:
        "Codex가 로그 파일을 쓰는 디렉터리입니다. 기본값은 `$CODEX_HOME/log`입니다. 이 설정을 명시적으로 지정하면 선택적으로 제공되는 일반 텍스트 TUI 로그 `codex-tui.log`도 활성화되어 해당 디렉터리에 기록됩니다.",
    },
    {
      key: "sqlite_home",
      type: "string (path)",
      description:
        "Codex가 에이전트 작업 및 기타 재개 가능한 런타임 상태에 사용하는 SQLite 기반 상태 DB를 저장하는 디렉터리입니다.",
    },
    {
      key: "compact_prompt",
      type: "string",
      description: "대화 기록의 컨텍스트 압축 프롬프트를 인라인으로 재정의합니다.",
    },
    {
      key: "model_instructions_file",
      type: "string (path)",
      description:
        "`AGENTS.md`가 아니라 기본 제공 지침을 대체합니다.",
    },
    {
      key: "personality",
      type: "none | friendly | pragmatic",
      description:
        "`supportsPersonality` 지원을 명시하는 모델의 기본 커뮤니케이션 스타일입니다. 스레드나 턴별로 또는 `/personality`를 통해 재정의할 수 있습니다.",
    },
    {
      key: "service_tier",
      type: "string",
      description:
        "새 턴에 사용할 선호 서비스 등급입니다. `fast` 또는 활성 모델이 지원한다고 명시한 다른 등급을 사용하세요. `fast`는 요청 값 `priority`에 매핑됩니다.",
    },
    {
      key: "experimental_compact_prompt_file",
      type: "string (path)",
      description:
        "컨텍스트 압축 프롬프트의 재정의 내용을 파일에서 로드합니다(실험적).",
    },
    {
      key: "skills.max_context_tokens",
      type: "integer (positive)",
      description:
        "사용 가능한 스킬 카탈로그의 토큰 예산입니다. 기본값은 모델 컨텍스트 윈도우의 2%입니다. 명시적으로 지정한 값은 최대 `10000`토큰으로 제한됩니다.",
    },
    {
      key: "skills.config",
      type: "array<object>",
      description: "config.toml에 저장되는 스킬별 활성화 상태 재정의입니다.",
    },
    {
      key: "skills.config.<index>.path",
      type: "string (path)",
      description: "`SKILL.md`가 포함된 스킬 폴더의 경로입니다.",
    },
    {
      key: "skills.config.<index>.enabled",
      type: "boolean",
      description: "참조된 스킬을 활성화하거나 비활성화합니다.",
    },
    {
      key: "apps.<id>.enabled",
      type: "boolean",
      description:
        "ID를 기준으로 특정 앱/커넥터를 활성화하거나 비활성화합니다(기본값: true).",
    },
    {
      key: "apps._default.enabled",
      type: "boolean",
      description:
        "앱별 재정의가 없을 때 모든 앱에 적용되는 기본 활성화 상태입니다.",
    },
    {
      key: "apps._default.destructive_enabled",
      type: "boolean",
      description:
        "`destructive_hint = true`인 앱 도구의 기본 허용/거부 설정입니다.",
    },
    {
      key: "apps._default.open_world_enabled",
      type: "boolean",
      description:
        "`open_world_hint = true`인 앱 도구의 기본 허용/거부 설정입니다.",
    },
    {
      key: "apps._default.approvals_reviewer",
      type: "user | auto_review",
      description:
        "앱별 재정의가 없을 때 앱 도구 승인 프롬프트에 적용되는 기본 검토자입니다. 생략하면 앱은 최상위 `approvals_reviewer` 값을 상속합니다.",
    },
    {
      key: "apps._default.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "앱별 또는 도구별 재정의가 없는 앱 도구의 기본 승인 동작입니다.",
    },
    {
      key: "apps.<id>.destructive_enabled",
      type: "boolean",
      description:
        "이 앱에서 `destructive_hint = true`를 명시한 도구를 허용하거나 차단합니다.",
    },
    {
      key: "apps.<id>.open_world_enabled",
      type: "boolean",
      description:
        "이 앱에서 `open_world_hint = true`를 명시한 도구를 허용하거나 차단합니다.",
    },
    {
      key: "apps.<id>.default_tools_enabled",
      type: "boolean",
      description:
        "도구별 재정의가 없을 때 이 앱의 도구에 적용되는 기본 활성화 상태입니다.",
    },
    {
      key: "apps.<id>.approvals_reviewer",
      type: "user | auto_review",
      description:
        "이 앱의 도구 승인 요청을 검토하는 주체입니다. `apps._default.approvals_reviewer`를 재정의합니다.",
    },
    {
      key: "apps.<id>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "도구별 재정의가 없을 때 이 앱의 도구에 적용되는 기본 승인 동작입니다.",
    },
    {
      key: "apps.<id>.tools.<tool>.enabled",
      type: "boolean",
      description:
        "앱의 개별 도구(예: `repos/list`)에 적용할 활성화 상태 재정의입니다.",
    },
    {
      key: "apps.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description: "앱의 개별 도구에 적용할 승인 동작 재정의입니다.",
    },
    {
      key: "tool_suggest.discoverables",
      type: "array<table>",
      description:
        "추가로 검색 가능한 커넥터나 플러그인의 도구 추천을 허용합니다. 각 항목에는 `type = \"connector\"` 또는 `\"plugin\"`과 `id`를 사용합니다.",
    },
    {
      key: "tool_suggest.disabled_tools",
      type: "array<table>",
      description:
        "검색 가능한 특정 커넥터나 플러그인의 추천을 비활성화합니다. 각 항목에는 `type = \"connector\"` 또는 `\"plugin\"`과 `id`를 사용합니다.",
    },
    {
      key: "features.apps",
      type: "boolean",
      description:
        "앱(커넥터) 통합을 활성화합니다(안정화된 기능, 기본적으로 활성화됨). 앱과 커넥터의 트래픽은 샌드박스 명령어용 네트워크 프록시나 해당 프록시의 도메인 허용 목록으로 제어되지 않습니다.",
    },
    {
      key: "features.hooks",
      type: "boolean",
      description:
        "`hooks.json` 또는 인라인 `[hooks]` 구성에서 불러온 라이프사이클 훅을 활성화합니다. `features.codex_hooks`는 사용 중단 예정(deprecated)인 별칭입니다.",
    },
    {
      key: "features.code_mode.enabled",
      type: "boolean",
      description:
        "코드 모드 기능 구성을 활성화합니다. 이 기능은 개발 중이며 기본적으로 비활성화되어 있습니다.",
    },
    {
      key: "features.code_mode.excluded_tool_namespaces",
      type: "array<string>",
      description:
        "코드 모드가 중첩 코드 모드의 도구 안내와 실행기 노출 대상에서 제외하는 도구 네임스페이스입니다.",
    },
    {
      key: "features.code_mode.direct_only_tool_namespaces",
      type: "array<string>",
      description:
        "코드 모드에서 직접 도구 호출로만 사용할 수 있는 도구 네임스페이스입니다.",
    },
    {
      key: "features.context_management.experimental_mode",
      type: "boolean",
      description:
        "실험적 컨텍스트 관리를 활성화합니다(기본적으로 비활성화됨). 컨텍스트를 하나의 요약으로 반복해서 압축하는 대신, 노트와 검색 가능한 기록을 사용해 누적된 세부 정보를 보존합니다. Plus, Pro 또는 Pro Lite 플랜의 ChatGPT 계정으로 로그인해야 합니다.",
    },
    {
      key: "features.rollout_budget.enabled",
      type: "boolean",
      description:
        "롤아웃 예산 추적을 활성화합니다. 이 기능은 개발 중이며 기본적으로 비활성화되어 있습니다. 활성화하면 `features.rollout_budget.limit_tokens`가 필요합니다.",
    },
    {
      key: "features.rollout_budget.limit_tokens",
      type: "integer",
      description:
        "롤아웃 예산 추적에 사용할 0보다 큰 토큰 한도입니다. 롤아웃 예산을 활성화하면 필수입니다.",
    },
    {
      key: "features.rollout_budget.reminder_interval_tokens",
      type: "integer",
      description:
        "롤아웃 예산 알림 사이의 토큰 간격입니다. 0보다 커야 하며, 기본값은 `limit_tokens`의 10%이고 최솟값은 토큰 1개입니다.",
    },
    {
      key: "features.rollout_budget.sampling_token_weight",
      type: "number",
      description:
        "롤아웃 예산 계산에서 샘플링된 토큰에 적용하는 배율입니다. 0 이상의 유한한 값이어야 하며 기본값은 `1.0`입니다.",
    },
    {
      key: "features.rollout_budget.prefill_token_weight",
      type: "number",
      description:
        "롤아웃 예산 계산에서 프리필 토큰에 적용하는 배율입니다. 0 이상의 유한한 값이어야 하며 기본값은 `1.0`입니다.",
    },
    {
      key: "hooks",
      type: "table",
      description:
        "`config.toml`에서 인라인으로 구성하는 라이프사이클 훅입니다. `hooks.json`과 동일한 이벤트 스키마를 사용합니다. 예시와 지원되는 이벤트는 훅 가이드를 참조하세요.",
    },
    {
      key: "hooks.",
      type: "array<table>",
      description:
        "`PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `SessionStart`, `SessionEnd`, `SubagentStart`, `SubagentStop`, `UserPromptSubmit`, `Stop`, `Interrupt`와 같은 훅 이벤트의 매처 그룹입니다.",
    },
    {
      key: "hooks.[].hooks",
      type: "array<table>",
      description:
        "매처 그룹의 훅 핸들러입니다. 명령어 훅과 MCP 도구 훅을 지원하며, 프롬프트 및 에이전트 훅 핸들러는 파싱 후 건너뜁니다.",
    },
    {
      key: "hooks.[].hooks[].async",
      type: "boolean",
      description:
        "훅을 트리거한 작업을 지연시키지 않고 명령어 훅을 백그라운드에서 실행합니다. 기본값은 `false`이며 `SessionEnd`는 항상 동기식으로 실행됩니다. [백그라운드에서 훅 실행](/codex/hooks#run-hooks-in-the-background)을 참조하세요.",
    },
    {
      key: "hooks.[].hooks[].additionalContextLimit",
      type: "integer",
      description:
        "크기가 너무 큰 `additionalContext`를 디스크에 저장하고 모델에는 더 짧은 미리보기를 표시하기 위한 핸들러별 대략적인 토큰 임곗값입니다. 기본값은 `2500`이며 `0`이면 전체 컨텍스트를 모델에 직접 전달합니다. [대용량 훅 출력](/codex/hooks#large-hook-output)을 참조하세요.",
    },
    {
      key: "hooks.[].hooks[].commandWindows",
      type: "string",
      description:
        "명령어 훅에 적용되는 Windows 전용 명령어 재정의입니다. TOML 별칭 `command_windows`도 사용할 수 있습니다.",
    },
    {
      key: "features.memories",
      type: "boolean",
      description:
        "[메모리](/codex/customization/memories)를 활성화합니다(기본적으로 비활성화됨).",
    },
    {
      key: "mcp_optional_startup_grace_ms",
      type: "integer (milliseconds)",
      description:
        "초기 도구 카탈로그를 구성할 때 선택적 MCP 서버들을 기다리는 공통 대기 시간입니다. 기본값은 `1000`입니다. 대신 각 서버의 `startup_timeout_sec`만큼 기다리려면 `0`으로 설정하세요.",
    },
    {
      key: "mcp_servers.<id>.command",
      type: "string",
      description: "MCP stdio 서버를 시작하는 명령어입니다.",
    },
    {
      key: "mcp_servers.<id>.args",
      type: "array<string>",
      description: "MCP stdio 서버 명령어에 전달하는 인수입니다.",
    },
    {
      key: "mcp_servers.<id>.env",
      type: "map<string,string>",
      description: "MCP stdio 서버에 전달하는 환경 변수입니다.",
    },
    {
      key: "mcp_servers.<id>.env_vars",
      type: 'array<string | { name = string, source = "local" | "remote" }>',
      description:
        "MCP stdio 서버의 허용 목록에 추가할 환경 변수입니다. 문자열 항목의 기본값은 `source = \"local\"`입니다. `source = \"remote\"`는 실행기 기반 원격 stdio에서만 사용하세요.",
    },
    {
      key: "mcp_servers.<id>.cwd",
      type: "string",
      description: "MCP stdio 서버 프로세스의 작업 디렉터리입니다.",
    },
    {
      key: "mcp_servers.<id>.url",
      type: "string",
      description: "MCP streamable HTTP 서버의 엔드포인트입니다.",
    },
    {
      key: "mcp_servers.<id>.auth",
      type: "oauth | chatgpt",
      description:
        "MCP HTTP 서버에서 구성된 베어러 토큰과 권한 부여 헤더 다음으로 시도하는 대체 인증 방식입니다. `oauth`(기본값)는 저장된 MCP OAuth 자격 증명이 있으면 이를 사용합니다. `chatgpt`는 신뢰할 수 있는 자사 ChatGPT 오리진에 현재 ChatGPT 세션을 사용하며, 이를 사용할 수 없으면 저장된 OAuth 자격 증명을 사용합니다. 두 모드 모두 어느 소스에서도 자격 증명을 얻을 수 없으면 인증 없이 연결할 수 있습니다.",
    },
    {
      key: "mcp_servers.<id>.oauth.client_id",
      type: "string",
      description:
        "이 MCP 서버에서 권한 부여와 토큰 교환에 사용하는 사전 등록된 OAuth 클라이언트 ID입니다.",
    },
    {
      key: "mcp_servers.<id>.oauth.callback_url",
      type: "string",
      description:
        "서버별 OAuth 콜백입니다. 사전 등록된 클라이언트는 발급자 식별이 지원되거나 URL이 이미 서버별 콜백 ID로 끝나면 이 콜백을 재사용합니다. 그렇지 않으면 Codex는 전역 콜백 또는 기본 콜백에 해당 ID를 덧붙여 사용합니다. 사전 등록된 ID가 없는 클라이언트는 클라이언트 등록 시 이 콜백을 사용합니다.",
    },
    {
      key: "mcp_servers.<id>.oauth.callback_port",
      type: "integer",
      description:
        "이 MCP 서버의 고정 OAuth 콜백 리스너 포트입니다. `mcp_oauth_callback_port`를 재정의합니다. 직접 루프백 콜백을 사용하고 URL에 포트를 명시했다면 리스너 포트도 동일하게 설정하세요.",
    },
    {
      key: "mcp_servers.<id>.bearer_token_env_var",
      type: "string",
      description:
        "MCP HTTP 서버의 베어러 토큰을 제공하는 환경 변수입니다.",
    },
    {
      key: "mcp_servers.<id>.http_headers",
      type: "map<string,string>",
      description: "각 MCP HTTP 요청에 포함되는 정적 HTTP 헤더입니다.",
    },
    {
      key: "mcp_servers.<id>.http_headers_helper",
      type: "string (command)",
      description:
        "HTTP 헤더 이름과 값을 담은 JSON 객체를 출력하는 로컬 명령어입니다. 로컬로 연결된 HTTP MCP 서버에서만 지원됩니다. 명시적으로 지정한 베어러 토큰과 OAuth 자격 증명이 헬퍼에서 제공한 Authorization 헤더보다 우선합니다.",
    },
    {
      key: "mcp_servers.<id>.env_http_headers",
      type: "map<string,string>",
      description:
        "환경 변수에서 값을 가져오는 MCP HTTP 서버용 HTTP 헤더입니다.",
    },
    {
      key: "mcp_servers.<id>.enabled",
      type: "boolean",
      description: "구성을 제거하지 않고 MCP 서버를 비활성화합니다.",
    },
    {
      key: "mcp_servers.<id>.required",
      type: "boolean",
      description:
        "true이면 활성화된 이 MCP 서버를 초기화할 수 없을 때 시작 또는 재개에 실패합니다.",
    },
    {
      key: "mcp_servers.<id>.startup_timeout_sec",
      type: "number",
      description:
        "MCP 서버의 기본 시작 제한 시간인 10초를 재정의합니다.",
    },
    {
      key: "mcp_servers.<id>.startup_timeout_ms",
      type: "number",
      description: "`startup_timeout_sec`의 밀리초 단위 별칭입니다.",
    },
    {
      key: "mcp_servers.<id>.tool_timeout_sec",
      type: "number",
      description:
        "MCP 서버의 도구별 기본 제한 시간인 60초를 재정의합니다.",
    },
    {
      key: "mcp_servers.<id>.enabled_tools",
      type: "array<string>",
      description: "MCP 서버가 노출하는 도구 이름의 허용 목록입니다.",
    },
    {
      key: "mcp_servers.<id>.disabled_tools",
      type: "array<string>",
      description:
        "MCP 서버에서 `enabled_tools` 다음에 적용되는 거부 목록입니다.",
    },
    {
      key: "mcp_servers.<id>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "도구별 재정의가 없을 때 이 서버의 MCP 도구에 적용되는 기본 승인 동작입니다.",
    },
    {
      key: "mcp_servers.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "이 서버의 개별 MCP 도구에 적용할 승인 동작 재정의입니다.",
    },
    {
      key: "mcp_servers.<id>.tools.<tool>.output_token_limit",
      type: "integer (positive)",
      description:
        "표준 직렬화 여유분 20%를 더하기 전의 개별 MCP 도구 출력 토큰 예산입니다. 해당 도구의 출력 잘림 기준이 되는 모델의 기본 예산을 재정의합니다.",
    },
    {
      key: "mcp_servers.<id>.scopes",
      type: "array<string>",
      description:
        "해당 MCP 서버에서 인증할 때 요청하는 OAuth 범위입니다.",
    },
    {
      key: "mcp_servers.<id>.oauth_resource",
      type: "string",
      description:
        "MCP 로그인 시 포함할 수 있는 선택적 RFC 8707 OAuth 리소스 매개변수입니다.",
    },
    {
      key: "mcp_servers.<id>.experimental_environment",
      type: "local | remote",
      description:
        "MCP 서버의 실험적 배치 설정입니다. `remote`는 원격 실행기 환경을 통해 stdio 서버를 시작합니다. streamable HTTP의 원격 배치는 구현되지 않았습니다.",
    },
    {
      key: "agents",
      type: "table",
      description:
        "멀티 에이전트 설정과 사용자 지정 역할 선언입니다. 스칼라 설정 이름은 예약되어 있어 사용자 지정 역할 이름으로 사용할 수 없습니다.",
    },
    {
      key: "agents.enabled",
      type: "boolean",
      description: "멀티 에이전트 도구를 활성화하거나 비활성화합니다(기본값: true).",
    },
    {
      key: "agents.max_concurrent_threads_per_session",
      type: "number",
      description:
        "생성된 에이전트 스레드 중 동시에 열어 둘 수 있는 최대 개수입니다. 주 스레드는 제외합니다. 설정하지 않으면 Codex가 기본값을 선택합니다.",
    },
    {
      key: "agents.max_threads",
      type: "number",
      description:
        "`agents.max_concurrent_threads_per_session`의 레거시 별칭입니다.",
    },
    {
      key: "agents.default_subagent_model",
      type: "string",
      description:
        "생성할 에이전트의 기본 모델입니다. 생성 시 모델을 명시하면 해당 모델이 우선합니다.",
    },
    {
      key: "agents.default_subagent_reasoning_effort",
      type: "string",
      description:
        "생성할 에이전트의 기본 추론 수준입니다. 생성 시 추론 수준을 명시하면 해당 값이 우선합니다.",
    },
    {
      key: "agents.interrupt_message",
      type: "boolean",
      description:
        "에이전트 턴이 중단될 때 모델이 볼 수 있는 메시지를 기록합니다(기본값: true).",
    },
    {
      key: "agents.<name>.description",
      type: "string",
      description:
        "해당 유형의 에이전트를 선택하고 생성할 때 Codex에 표시되는 역할 지침입니다.",
    },
    {
      key: "agents.<name>.config_file",
      type: "string (path)",
      description:
        "해당 역할의 TOML 구성 레이어 경로입니다. 상대 경로는 역할을 선언한 구성 파일을 기준으로 해석됩니다.",
    },
    {
      key: "memories.generate_memories",
      type: "boolean",
      description:
        "`false`이면 새로 생성된 스레드를 메모리 생성용 입력으로 저장하지 않습니다. 기본값은 `true`입니다.",
    },
    {
      key: "memories.use_memories",
      type: "boolean",
      description:
        "`false`이면 Codex가 이후 세션에 기존 메모리를 포함하지 않습니다. 기본값은 `true`입니다.",
    },
    {
      key: "memories.disable_on_external_context",
      type: "boolean",
      description:
        "`true`이면 MCP 도구 호출, 웹 검색, 도구 검색 등 외부 컨텍스트를 사용하는 스레드는 메모리 생성 대상에서 제외됩니다. 기본값은 `false`입니다. 레거시 별칭: `memories.no_memories_if_mcp_or_web_search`.",
    },
    {
      key: "memories.max_raw_memories_for_consolidation",
      type: "number",
      description:
        "전역 통합을 위해 보관할 최근 원시 메모리의 최대 개수입니다. 기본값은 `256`이며, 상한은 `4096`입니다.",
    },
    {
      key: "memories.max_unused_days",
      type: "number",
      description:
        "메모리를 마지막으로 사용한 후 통합 대상에서 제외되기까지의 최대 일수입니다. 기본값은 `30`이며, `0`-`365` 범위로 제한됩니다.",
    },
    {
      key: "memories.max_rollout_age_days",
      type: "number",
      description:
        "메모리 생성 대상 스레드의 최대 경과 기간입니다. 기본값은 `30`이며, `0`-`90` 범위로 제한됩니다.",
    },
    {
      key: "memories.max_rollouts_per_startup",
      type: "number",
      description:
        "시작 시 한 차례 처리할 롤아웃 후보의 최대 개수입니다. 기본값은 `16`이며, 상한은 `128`입니다.",
    },
    {
      key: "memories.min_rollout_idle_hours",
      type: "number",
      description:
        "스레드가 메모리 생성 대상이 되기까지 필요한 최소 유휴 시간입니다. 기본값은 `6`이며, `1`-`48` 범위로 제한됩니다.",
    },
    {
      key: "memories.min_rate_limit_remaining_percent",
      type: "number",
      description:
        "메모리 생성을 시작하려면 Codex의 요청 한도 적용 구간에 남아 있어야 하는 최소 잔여 비율입니다. 기본값은 `25`이며, `0`-`100` 범위로 제한됩니다.",
    },
    {
      key: "memories.extract_model",
      type: "string",
      description: "스레드별 메모리 추출에 사용할 모델을 선택적으로 재정의합니다.",
    },
    {
      key: "memories.consolidation_model",
      type: "string",
      description: "전역 메모리 통합에 사용할 모델을 선택적으로 재정의합니다.",
    },
    {
      key: "features.unified_exec",
      type: "boolean",
      description:
        "통합 PTY 기반 exec 도구를 사용합니다(안정화된 기능, Windows를 제외한 환경에서 기본적으로 활성화).",
    },
    {
      key: "features.shell_snapshot",
      type: "boolean",
      description:
        "셸 환경의 스냅샷을 생성해 반복되는 명령어의 실행 속도를 높입니다(안정화된 기능, 기본적으로 활성화).",
    },
    {
      key: "features.multi_agent",
      type: "boolean",
      description:
        "다중 에이전트 협업 도구(`spawn_agent`, `send_input`, `resume_agent`, `wait_agent`, `close_agent`)를 활성화합니다(안정화된 기능, 기본적으로 활성화).",
    },
    {
      key: "features.goals",
      type: "boolean",
      description:
        "목표를 영구 저장하고 자동으로 이어서 진행하는 기능을 활성화합니다(안정화된 기능, 기본적으로 활성화).",
    },
    {
      key: "features.remote_plugin",
      type: "boolean",
      description: "원격 플러그인 카탈로그를 활성화합니다(안정화된 기능, 기본적으로 활성화).",
    },
    {
      key: "features.personality",
      type: "boolean",
      description:
        "성격 선택 기능을 활성화합니다(안정화된 기능, 기본적으로 활성화).",
    },
    {
      key: "features.network_proxy",
      type: "boolean | table",
      description:
        "샌드박스에서 실행되는 명령어의 네트워크 프록시를 시작합니다(실험적 기능, 기본적으로 비활성화). 관리자가 관리하는 `experimental_network` 요구 사항이 활성화되어 프록시를 시작하는 경우가 아니라면, 권한 프로필의 도메인 규칙을 적용하려면 이 설정이 필요합니다. `domains`와 같은 기능 수준의 정책 옵션을 설정할 때는 테이블 형식을 사용하세요. 웹 검색, 앱, MCP 또는 기타 호스팅 도구는 필터링하지 않습니다.",
    },
    {
      key: "features.network_proxy.enabled",
      type: "boolean",
      description:
        "명령어의 네트워크 액세스가 활성화된 경우 샌드박스에서 실행되는 명령어의 네트워크 프록시를 시작합니다. 기본값은 `false`이며, 프록시가 비활성화된 동안에는 권한 프로필의 도메인 규칙이 적용되지 않습니다.",
    },
    {
      key: "features.network_proxy.domains",
      type: "map<string, allow | deny>",
      description:
        "샌드박스 네트워킹의 도메인 정책입니다. 기본적으로 설정되어 있지 않으므로 `allow` 규칙을 추가하기 전에는 외부 대상에 대한 액세스가 허용되지 않습니다. 정확히 일치하는 호스트, 하위 도메인만 허용하는 `*.example.com`, 루트 도메인과 하위 도메인을 허용하는 `**.example.com`, 전체에 적용되는 `*` 허용 규칙을 지원합니다. `*`는 공용 네트워크에 대한 아웃바운드 액세스를 광범위하게 허용하므로 범위를 제한한 규칙을 사용하는 것이 좋습니다. 차단할 대상에는 `deny` 규칙을 추가하세요. 규칙이 충돌하면 `deny`가 우선합니다.",
    },
    {
      key: "features.network_proxy.unix_sockets",
      type: "map<string, allow | deny>",
      description:
        "샌드박스 네트워킹의 Unix 소켓 정책입니다. 기본적으로 설정되어 있지 않습니다. 허용할 소켓에는 `allow` 항목을 추가하세요.",
    },
    {
      key: "features.network_proxy.allow_local_binding",
      type: "boolean",
      description:
        "로컬/사설 네트워크에 대한 더 광범위한 액세스를 허용합니다. 기본값은 `false`이지만, 정확한 로컬 IP 리터럴이나 `localhost`를 허용하는 규칙으로 특정 로컬 대상에 대한 액세스를 허용할 수 있습니다.",
    },
    {
      key: "features.network_proxy.enable_socks5",
      type: "boolean",
      description: "SOCKS5를 사용할 수 있도록 합니다. 기본값은 `true`입니다.",
    },
    {
      key: "features.network_proxy.enable_socks5_udp",
      type: "boolean",
      description: "SOCKS5를 통한 UDP 사용을 허용합니다. 기본값은 `true`입니다.",
    },
    {
      key: "features.network_proxy.allow_upstream_proxy",
      type: "boolean",
      description:
        "환경에 설정된 업스트림 프록시를 통한 체이닝을 허용합니다. 기본값은 `true`입니다.",
    },
    {
      key: "features.network_proxy.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "루프백이 아닌 리스너 주소를 허용합니다. 기본값은 `false`이며, 활성화하면 프록시 리스너가 로컬호스트 외부에 노출될 수 있습니다.",
    },
    {
      key: "features.network_proxy.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "허용 목록으로 액세스를 제한하는 대신 임의의 Unix 소켓 대상에 대한 액세스를 허용합니다. 기본값은 `false`이며, 엄격하게 통제되는 환경에서만 사용하세요.",
    },
    {
      key: "features.network_proxy.proxy_url",
      type: "string",
      description:
        "샌드박스 네트워킹용 HTTP 리스너 URL입니다. 기본값은 `\"http://127.0.0.1:3128\"`입니다.",
    },
    {
      key: "features.network_proxy.socks_url",
      type: "string",
      description:
        "SOCKS5 리스너 URL입니다. 기본값은 `\"http://127.0.0.1:8081\"`입니다.",
    },
    {
      key: "features.web_search",
      type: "boolean",
      description:
        "사용 중단 예정(deprecated)인 레거시 토글입니다. 최상위 `web_search` 설정을 사용하는 것이 좋습니다.",
    },
    {
      key: "features.web_search_cached",
      type: "boolean",
      description:
        "사용 중단 예정(deprecated)인 레거시 토글입니다. `web_search`가 설정되어 있지 않으면 true는 `web_search = \"cached\"`로 매핑됩니다.",
    },
    {
      key: "features.web_search_request",
      type: "boolean",
      description:
        "사용 중단 예정(deprecated)인 레거시 토글입니다. `web_search`가 설정되어 있지 않으면 true는 `web_search = \"live\"`로 매핑됩니다.",
    },
    {
      key: "features.shell_tool",
      type: "boolean",
      description:
        "명령어를 실행하는 기본 `shell` 도구를 활성화합니다(안정화된 기능, 기본적으로 활성화).",
    },
    {
      key: "features.enable_request_compression",
      type: "boolean",
      description:
        "지원되는 경우 스트리밍 요청 본문을 zstd로 압축합니다(안정화된 기능, 기본적으로 활성화).",
    },
    {
      key: "features.skill_mcp_dependency_install",
      type: "boolean",
      description:
        "스킬에 필요한 MCP 종속성이 없을 때 설치 여부를 묻고 설치할 수 있도록 허용합니다(안정화된 기능, 기본적으로 활성화).",
    },
    {
      key: "features.fast_mode",
      type: "boolean",
      description:
        "TUI에서 모델 카탈로그의 서비스 등급을 선택할 수 있도록 합니다. 활성 모델이 Fast 등급 명령어 지원을 명시하면 해당 명령어도 사용할 수 있습니다(안정화된 기능, 기본적으로 활성화).",
    },
    {
      key: "features.prevent_idle_sleep",
      type: "boolean",
      description:
        "턴이 실행되는 동안 컴퓨터가 절전 모드로 전환되지 않도록 합니다(실험적 기능, 기본적으로 비활성화).",
    },
    {
      key: "suppress_unstable_features_warning",
      type: "boolean",
      description:
        "개발 중인 기능 플래그를 활성화했을 때 나타나는 경고를 숨깁니다.",
    },
    {
      key: "model_providers.<id>",
      type: "table",
      description:
        "사용자 지정 제공자 정의입니다. 기본 제공자 ID(`openai`, `ollama`, `lmstudio`)는 예약되어 있어 재정의할 수 없습니다.",
    },
    {
      key: "model_providers.<id>.name",
      type: "string",
      description: "사용자 지정 모델 제공자의 표시 이름입니다.",
    },
    {
      key: "model_providers.<id>.base_url",
      type: "string",
      description: "모델 제공자의 API 기본 URL입니다.",
    },
    {
      key: "model_providers.<id>.env_key",
      type: "string",
      description: "제공자의 API 키를 제공하는 환경 변수입니다.",
    },
    {
      key: "model_providers.<id>.env_key_instructions",
      type: "string",
      description: "선택적으로 지정할 수 있는 제공자 API 키 설정 안내입니다.",
    },
    {
      key: "model_providers.<id>.experimental_bearer_token",
      type: "string",
      description:
        "제공자에 직접 지정하는 베어러 토큰입니다(권장하지 않으며, `env_key`를 사용하세요).",
    },
    {
      key: "model_providers.<id>.requires_openai_auth",
      type: "boolean",
      description:
        "제공자가 OpenAI 인증을 사용할지 여부입니다(기본값: false).",
    },
    {
      key: "model_providers.<id>.wire_api",
      type: "responses",
      description:
        "제공자가 사용하는 프로토콜입니다. 지원되는 값은 `responses`뿐이며, 생략하면 이 값이 기본값으로 사용됩니다.",
    },
    {
      key: "model_providers.<id>.query_params",
      type: "map<string,string>",
      description: "제공자 요청에 추가되는 쿼리 매개변수입니다.",
    },
    {
      key: "model_providers.<id>.http_headers",
      type: "map<string,string>",
      description: "제공자 요청에 추가되는 고정 HTTP 헤더입니다.",
    },
    {
      key: "model_providers.<id>.env_http_headers",
      type: "map<string,string>",
      description:
        "환경 변수가 있으면 해당 변수 값으로 채우는 HTTP 헤더입니다.",
    },
    {
      key: "model_providers.<id>.request_max_retries",
      type: "number",
      description:
        "제공자에 보내는 HTTP 요청의 재시도 횟수입니다(기본값: 4).",
    },
    {
      key: "model_providers.<id>.stream_max_retries",
      type: "number",
      description: "SSE 스트리밍 중단 시 재시도 횟수입니다(기본값: 5).",
    },
    {
      key: "model_providers.<id>.stream_idle_timeout_ms",
      type: "number",
      description:
        "SSE 스트림의 유휴 제한 시간(밀리초)입니다(기본값: 300000).",
    },
    {
      key: "model_providers.<id>.supports_websockets",
      type: "boolean",
      description:
        "해당 제공자가 Responses API WebSocket 전송 방식을 지원하는지 여부입니다.",
    },
    {
      key: "model_providers.<id>.supports_standalone_web_search",
      type: "boolean",
      description:
        "호환되는 독립형 웹 검색 엔드포인트를 지원한다고 표시합니다(기본값: false). 독립형 검색은 아직 개발 중이며 기본적으로 비활성화되어 있습니다. 제공자가 호환된다는 것만으로는 이 기능이 활성화되지 않습니다.",
    },
    {
      key: "model_providers.<id>.auth",
      type: "table",
      description:
        "사용자 지정 제공자의 명령어 기반 베어러 토큰 구성입니다. `env_key`, `experimental_bearer_token`, `requires_openai_auth`와 함께 사용하지 마세요.",
    },
    {
      key: "model_providers.<id>.auth.command",
      type: "string",
      description:
        "Codex에 베어러 토큰이 필요할 때 실행할 명령어입니다. 이 명령어는 토큰을 stdout에 출력해야 합니다.",
    },
    {
      key: "model_providers.<id>.auth.args",
      type: "array<string>",
      description: "토큰 명령어에 전달하는 인수입니다.",
    },
    {
      key: "model_providers.<id>.auth.timeout_ms",
      type: "number",
      description:
        "토큰 명령어의 최대 실행 시간(밀리초)입니다(기본값: 5000).",
    },
    {
      key: "model_providers.<id>.auth.refresh_interval_ms",
      type: "number",
      description:
        "Codex가 토큰을 선제적으로 갱신하는 주기(밀리초)입니다(기본값: 300000). 인증 재시도 후에만 갱신하려면 `0`으로 설정하세요.",
    },
    {
      key: "model_providers.<id>.auth.cwd",
      type: "string (path)",
      description: "토큰 명령어의 작업 디렉터리입니다.",
    },
    {
      key: "model_providers.amazon-bedrock.aws.profile",
      type: "string",
      description:
        "기본 제공 `amazon-bedrock` 제공자가 사용하는 AWS 프로필 이름입니다.",
    },
    {
      key: "model_providers.amazon-bedrock.aws.region",
      type: "string",
      description: "기본 제공 `amazon-bedrock` 제공자가 사용하는 AWS 리전입니다.",
    },
    {
      key: "model_reasoning_effort",
      type: "minimal | low | medium | high | xhigh",
      description:
        "지원되는 모델의 추론 수준을 조정합니다(Responses API에서만 사용 가능하며, `xhigh` 지원 여부는 모델에 따라 다름).",
    },
    {
      key: "plan_mode_reasoning_effort",
      type: "none | minimal | low | medium | high | xhigh",
      description:
        "플랜 모드 전용 추론 설정 재정의입니다. 설정하지 않으면 플랜 모드에 내장된 프리셋의 기본값이 적용됩니다.",
    },
    {
      key: "model_reasoning_summary",
      type: "auto | concise | detailed | none",
      description:
        "추론 요약의 상세 수준을 선택하거나 요약을 완전히 비활성화합니다.",
    },
    {
      key: "model_verbosity",
      type: "low | medium | high",
      description:
        "GPT-5 Responses API의 응답 상세도를 선택적으로 재정의합니다. 설정하지 않으면 선택한 모델/프리셋의 기본값을 사용합니다.",
    },
    {
      key: "model_supports_reasoning_summaries",
      type: "boolean",
      description: "Codex가 추론 메타데이터를 반드시 보내거나 보내지 않도록 설정합니다.",
    },
    {
      key: "shell_environment_policy.inherit",
      type: "all | core | none",
      description:
        "하위 프로세스를 생성할 때 적용할 기본 환경 상속 방식입니다.",
    },
    {
      key: "shell_environment_policy.ignore_default_excludes",
      type: "boolean",
      description:
        "다른 필터가 실행되기 전에 이름에 KEY, SECRET 또는 TOKEN이 포함된 변수를 유지합니다(기본값: true). 비밀 정보 관련 이름을 자동으로 제외하려면 false로 설정하세요.",
    },
    {
      key: "shell_environment_policy.filters",
      type: "map<string, include | exclude>",
      description:
        "대소문자를 구분하지 않는 표준 환경 변수 패턴 필터입니다. 포함 항목은 허용 목록을 구성하며, 이미 제외된 값을 복원할 수는 없습니다. 명시적인 `set` 값은 제외 처리 후에 적용됩니다. 같은 구성 계층에서 필터를 레거시 `exclude` 또는 `include_only` 배열과 함께 사용하지 마세요.",
    },
    {
      key: "shell_environment_policy.exclude",
      type: "array<string>",
      description:
        "레거시 환경 변수 제외 패턴입니다. 새 구성에는 `shell_environment_policy.filters`를 사용하고, 같은 구성 계층에서 두 형식을 함께 사용하지 마세요.",
    },
    {
      key: "shell_environment_policy.include_only",
      type: "array<string>",
      description:
        "레거시 환경 변수 패턴 허용 목록입니다. 새 구성에는 `shell_environment_policy.filters`를 사용하고, 같은 구성 계층에서 두 형식을 함께 사용하지 마세요.",
    },
    {
      key: "shell_environment_policy.set",
      type: "map<string,string>",
      description:
        "제외 처리 후 명시적으로 주입할 환경 변수 값입니다. 이 값도 포함 필터에 의해 제거될 수 있습니다.",
    },
    {
      key: "shell_environment_policy.experimental_use_profile",
      type: "boolean",
      description: "하위 프로세스를 생성할 때 사용자의 셸 프로필을 사용합니다.",
    },
    {
      key: "project_root_markers",
      type: "array<string>",
      description:
        "프로젝트 루트를 나타내는 파일 이름 목록입니다. 상위 디렉터리에서 프로젝트 루트를 찾을 때 사용합니다.",
    },
    {
      key: "project_doc_max_bytes",
      type: "number",
      description:
        "프로젝트 지침을 구성할 때 `AGENTS.md`에서 읽을 최대 바이트 수입니다.",
    },
    {
      key: "project_doc_fallback_filenames",
      type: "array<string>",
      description: "`AGENTS.md`가 없을 때 추가로 찾아볼 파일 이름입니다.",
    },
    {
      key: "history.persistence",
      type: "save-all | none",
      description:
        "Codex가 세션 대화 기록을 history.jsonl에 저장할지 제어합니다.",
    },
    {
      key: "tool_output_token_limit",
      type: "number",
      description:
        "개별 도구/함수 출력을 기록에 저장하는 데 사용할 토큰 한도입니다.",
    },
    {
      key: "background_terminal_max_timeout",
      type: "number",
      description:
        "빈 입력으로 수행하는 `write_stdin` 폴링(백그라운드 터미널 폴링)의 최대 대기 시간(밀리초)입니다. 기본값은 `300000`(5분)이며, 기존 `background_terminal_timeout` 키를 대체합니다.",
    },
    {
      key: "history.max_bytes",
      type: "number",
      description:
        "설정하면 가장 오래된 항목부터 삭제해 기록 파일의 크기를 지정된 바이트 수 이내로 제한합니다.",
    },
    {
      key: "file_opener",
      type: "vscode | vscode-insiders | windsurf | cursor | none",
      description:
        "Codex 출력의 인용을 열 때 사용하는 URI 스킴입니다(기본값: `vscode`).",
    },
    {
      key: "otel.environment",
      type: "string",
      description:
        "내보내는 OpenTelemetry 이벤트에 적용되는 환경 태그입니다(기본값: `dev`).",
    },
    {
      key: "otel.exporter",
      type: "none | otlp-http | otlp-grpc",
      description:
        "OpenTelemetry 익스포터를 선택하고 엔드포인트 메타데이터를 지정합니다.",
    },
    {
      key: "otel.trace_exporter",
      type: "none | otlp-http | otlp-grpc",
      description:
        "OpenTelemetry 트레이스 익스포터를 선택하고 엔드포인트 메타데이터를 지정합니다.",
    },
    {
      key: "otel.metrics_exporter",
      type: "none | statsig | otlp-http | otlp-grpc",
      description:
        "OpenTelemetry 메트릭 익스포터를 선택합니다(기본값: `statsig`).",
    },
    {
      key: "otel.log_user_prompt",
      type: "boolean",
      description:
        "사용자 프롬프트 원문을 OpenTelemetry 로그와 함께 내보내도록 명시적으로 허용합니다.",
    },
    {
      key: "otel.exporter.<id>.endpoint",
      type: "string",
      description: "OTEL 로그 익스포터의 엔드포인트입니다.",
    },
    {
      key: "otel.exporter.<id>.protocol",
      type: "binary | json",
      description: "OTLP/HTTP 익스포터에서 사용하는 프로토콜입니다.",
    },
    {
      key: "otel.exporter.<id>.headers",
      type: "map<string,string>",
      description: "OTEL 익스포터 요청에 포함되는 정적 헤더입니다.",
    },
    {
      key: "otel.trace_exporter.<id>.endpoint",
      type: "string",
      description: "OTEL 로그의 트레이스 익스포터 엔드포인트입니다.",
    },
    {
      key: "otel.trace_exporter.<id>.protocol",
      type: "binary | json",
      description: "OTLP/HTTP 트레이스 익스포터에서 사용하는 프로토콜입니다.",
    },
    {
      key: "otel.trace_exporter.<id>.headers",
      type: "map<string,string>",
      description: "OTEL 트레이스 익스포터 요청에 포함되는 정적 헤더입니다.",
    },
    {
      key: "otel.exporter.<id>.tls.ca-certificate",
      type: "string",
      description: "OTEL 익스포터의 TLS에 사용할 CA 인증서 경로입니다.",
    },
    {
      key: "otel.exporter.<id>.tls.client-certificate",
      type: "string",
      description: "OTEL 익스포터의 TLS에 사용할 클라이언트 인증서 경로입니다.",
    },
    {
      key: "otel.exporter.<id>.tls.client-private-key",
      type: "string",
      description: "OTEL 익스포터의 TLS에 사용할 클라이언트 개인 키 경로입니다.",
    },
    {
      key: "otel.trace_exporter.<id>.tls.ca-certificate",
      type: "string",
      description: "OTEL 트레이스 익스포터의 TLS에 사용할 CA 인증서 경로입니다.",
    },
    {
      key: "otel.trace_exporter.<id>.tls.client-certificate",
      type: "string",
      description: "OTEL 트레이스 익스포터의 TLS에 사용할 클라이언트 인증서 경로입니다.",
    },
    {
      key: "otel.trace_exporter.<id>.tls.client-private-key",
      type: "string",
      description: "OTEL 트레이스 익스포터의 TLS에 사용할 클라이언트 개인 키 경로입니다.",
    },
    {
      key: "desktop.custom_file_handlers.<id>",
      type: "table",
      description:
        "사용자 수준에서만 설정할 수 있습니다. ChatGPT 데스크톱 앱의 **다음에서 열기** 대상을 추가로 정의합니다. 예시와 핸들러 ID 제약 조건은 [사용자 지정 파일 핸들러 추가](/codex/config-file/config-advanced#add-custom-file-handlers)를 참조하세요.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.label",
      type: "string",
      description: "**다음에서 열기** 메뉴에 표시되는 이름입니다. 필수 항목입니다.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.icon",
      type: "string",
      description:
        "핸들러 아이콘에 사용할 번들 에셋 경로, Base64로 인코딩된 `data:image/...` URL, 파일 URI 또는 로컬 절대 경로입니다. 필수 항목이며, 지원되지 않는 소스에는 기본 VS Code 아이콘이 사용됩니다.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.command",
      type: "string",
      description:
        "감지하고 실행할 실행 파일의 경로 또는 명령어 이름입니다. 필수 항목입니다.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.args",
      type: "array<string>",
      description:
        "명령어와 파일 입력 사이에 삽입할 인수입니다(기본값: `[]`).",
    },
    {
      key: "desktop.custom_file_handlers.<id>.input",
      type: "path | json_argument | json_stdin",
      description:
        "앱이 파일 입력을 핸들러로 전송하는 방식입니다(기본값: `path`).",
    },
    {
      key: "desktop.custom_file_handlers.<id>.supports_ssh",
      type: "boolean",
      description:
        "SSH 워크스페이스의 파일에도 이 핸들러를 제공합니다(기본값: `false`).",
    },
    {
      key: "tui",
      type: "table",
      description:
        "인라인 데스크톱 알림 활성화와 같은 TUI 전용 옵션입니다.",
    },
    {
      key: "tui.notifications",
      type: "boolean | array<string>",
      description:
        "TUI 알림을 활성화하며, 필요에 따라 특정 이벤트 유형으로 제한할 수 있습니다.",
    },
    {
      key: "tui.notification_method",
      type: "auto | osc9 | bel",
      description:
        "터미널 알림을 표시하는 방식입니다(기본값: auto).",
    },
    {
      key: "tui.notification_condition",
      type: "unfocused | always",
      description:
        "터미널에 포커스가 없을 때만 TUI 알림을 표시할지, 포커스와 관계없이 표시할지 제어합니다. 기본값은 `unfocused`입니다.",
    },
    {
      key: "tui.animations",
      type: "boolean",
      description:
        "터미널 애니메이션(환영 화면, 시머 효과, 스피너)을 활성화합니다(기본값: true).",
    },
    {
      key: "tui.alternate_screen",
      type: "auto | always | never",
      description:
        "TUI의 대체 화면 사용을 제어합니다(기본값: auto. auto에서는 스크롤백을 유지하기 위해 Zellij에서 대체 화면을 사용하지 않습니다).",
    },
    {
      key: "tui.resume_cwd",
      type: "current | session",
      description:
        "세션을 재개하거나 포크할 때 사용할 작업 디렉터리입니다. 설정하지 않은 상태에서 현재 디렉터리가 세션에 저장된 디렉터리와 다르면 Codex가 사용할 디렉터리를 선택하도록 요청합니다.",
    },
    {
      key: "tui.vim_mode_default",
      type: "boolean",
      description:
        "Composer를 Vim 삽입 모드 대신 일반 모드로 시작합니다(기본값: false). 세션별로 `/vim`을 사용해 전환할 수도 있습니다.",
    },
    {
      key: "tui.raw_output_mode",
      type: "boolean",
      description:
        "TUI를 원시 스크롤백 모드로 시작해 터미널에서 텍스트를 쉽게 선택하고 복사할 수 있도록 합니다(기본값: false). `/raw` 또는 기본 `alt-r` 키 바인딩으로 전환할 수 있습니다.",
    },
    {
      key: "tui.show_tooltips",
      type: "boolean",
      description:
        "TUI 환영 화면에 온보딩 툴팁을 표시합니다(기본값: true).",
    },
    {
      key: "tui.status_line",
      type: "array<string> | null",
      description:
        "TUI 하단 상태 표시줄의 항목 식별자를 순서대로 나열한 목록입니다. `null`로 설정하면 상태 표시줄을 비활성화합니다.",
    },
    {
      key: "tui.terminal_title",
      type: "array<string> | null",
      description:
        "터미널 창 및 탭의 제목 항목 식별자를 순서대로 나열한 목록입니다. 기본값은 `[\"spinner\", \"project\"]`이며, `null`로 설정하면 제목 업데이트를 비활성화합니다.",
    },
    {
      key: "tui.theme",
      type: "string",
      description:
        "구문 강조 테마를 재정의합니다(케밥 케이스 형식의 테마 이름).",
    },
    {
      key: "tui.keymap.<context>.<action>",
      type: "string | array<string>",
      description:
        "TUI 작업에 대한 키보드 단축키 바인딩입니다. 지원되는 컨텍스트에는 `global`, `chat`, `composer`, `editor`, `vim_normal`, `vim_operator`, `vim_text_object`, `pager`, `list`, `approval`이 포함됩니다. 일부 Composer 작업은 일치하는 `tui.keymap.global` 바인딩을 폴백으로 사용하며, 컨텍스트별 바인딩이 지원되면 해당 바인딩이 우선합니다.",
    },
    {
      key: "tui.keymap.<context>.<action> = []",
      type: "empty array",
      description:
        "해당 키맵 컨텍스트에서 작업의 바인딩을 해제합니다. 키 이름에는 `ctrl-a`, `shift-enter`, `page-down`, `minus`와 같은 정규화된 문자열을 사용합니다.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.enabled",
      type: "boolean",
      description:
        "플러그인 매니페스트를 변경하지 않고 설치된 플러그인에 포함된 MCP 서버를 활성화하거나 비활성화합니다.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "플러그인이 제공하는 MCP 서버의 도구에 적용되는 기본 승인 동작입니다.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.enabled_tools",
      type: "array<string>",
      description:
        "플러그인이 제공하는 MCP 서버에서 노출하는 도구의 허용 목록입니다.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.disabled_tools",
      type: "array<string>",
      description:
        "플러그인이 제공하는 MCP 서버에서 `enabled_tools` 다음에 적용되는 거부 목록입니다.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "플러그인이 제공하는 MCP 도구의 승인 동작을 도구별로 재정의합니다.",
    },
    {
      key: "tui.model_availability_nux.<model>",
      type: "integer",
      description: "모델 슬러그를 키로 사용하는 시작 툴팁의 내부 상태입니다.",
    },
    {
      key: "hide_agent_reasoning",
      type: "boolean",
      description:
        "TUI와 `codex exec` 출력 모두에서 추론 이벤트를 표시하지 않습니다.",
    },
    {
      key: "show_raw_agent_reasoning",
      type: "boolean",
      description:
        "활성 모델이 추론 원문을 출력하면 이를 표시합니다.",
    },
    {
      key: "disable_paste_burst",
      type: "boolean",
      description: "TUI에서 버스트 붙여넣기 감지를 비활성화합니다.",
    },
    {
      key: "windows_wsl_setup_acknowledged",
      type: "boolean",
      description: "Windows 온보딩 안내의 확인 여부를 기록합니다(Windows 전용).",
    },
    {
      key: "chatgpt_base_url",
      type: "string",
      description: "ChatGPT 로그인 플로우에서 사용하는 기본 URL을 재정의합니다.",
    },
    {
      key: "cli_auth_credentials_store",
      type: "file | keyring | auto",
      description:
        "CLI가 캐시된 자격 증명을 저장할 위치를 설정합니다(파일 기반 auth.json 또는 OS 키체인).",
    },
    {
      key: "mcp_oauth_credentials_store",
      type: "auto | file | keyring",
      description: "MCP OAuth 자격 증명을 저장할 기본 저장소입니다.",
    },
    {
      key: "mcp_oauth_callback_port",
      type: "integer",
      description:
        "MCP OAuth 로그인 시 사용하는 로컬 HTTP 콜백 서버의 전역 고정 포트입니다(선택 사항). 서버별 `oauth.callback_port`가 우선합니다. 둘 다 설정하지 않으면 Codex는 OS가 선택한 임시 포트에 바인딩합니다.",
    },
    {
      key: "mcp_oauth_callback_url",
      type: "string",
      description:
        "MCP OAuth 로그인에 사용할 기본 콜백 URL입니다(선택 사항). 예를 들어 devbox 인그레스 URL을 사용할 수 있습니다. 인증 서버가 발급자 식별을 지원하면 새로 추가한 사전 등록 클라이언트는 이 URL을 그대로 사용합니다. 저장된 콜백이 없는 기존 클라이언트는 서버별 콜백 ID를 추가합니다. 발급자 식별을 지원하지 않는 경우, 사전 등록된 MCP 서버의 콜백 설정에 필수 ID가 없으면 이 URL에 ID를 추가한 주소를 대신 사용합니다. 콜백 URL의 포트는 리스너 포트를 결정하지 않습니다.",
    },
    {
      key: "experimental_use_unified_exec_tool",
      type: "boolean",
      description:
        "통합 실행을 활성화하는 기존 설정 이름입니다. `[features].unified_exec` 또는 `codex --enable unified_exec`를 사용하세요.",
    },
    {
      key: "tools.web_search",
      type: 'boolean | { context_size = "low|medium|high", allowed_domains = [string], location = { country, region, city, timezone } }',
      description:
        "웹 검색 도구 구성입니다(선택 사항). 객체 형식으로 검색 컨텍스트 크기, 허용할 검색 도메인, 사용자의 대략적인 위치를 설정할 수 있습니다. 이 검색 도메인 필터는 샌드박스 내 명령어에 적용되는 네트워크 도메인 규칙과 별개이며, 커넥터나 MCP 서버를 제한하지 않습니다.",
    },
    {
      key: "tools.view_image",
      type: "boolean",
      description: "로컬 이미지 첨부 도구 `view_image`를 활성화합니다.",
    },
    {
      key: "web_search",
      type: "disabled | cached | indexed | live",
      description:
        "웹 검색 모드입니다(기본값: `\"cached\"`). cached는 외부 웹에 접근하지 않고 OpenAI가 관리하는 인덱스를 사용합니다. indexed는 검색 인덱스가 허용하는 경우에만 외부 접근을 허용합니다. `--yolo` 또는 전체 권한을 부여하는 다른 샌드박스 설정을 사용하면 기본값은 `\"live\"`입니다. 제한 없는 실시간 검색에는 `\"live\"`를 사용하고, 도구를 제거하려면 `\"disabled\"`를 사용하세요.",
    },
    {
      key: "default_permissions",
      type: "string",
      description:
        "샌드박스 내 도구 호출에 적용할 기본 권한 프로필의 이름입니다. 기본 제공 프로필은 `:read-only`, `:workspace`, `:danger-full-access`입니다. 사용자 지정 프로필 이름에는 해당하는 `[permissions.<name>]` 테이블이 필요합니다. `sandbox_mode` 또는 `[sandbox_workspace_write]`와 함께 사용하지 마세요.",
    },
    {
      key: "permissions.<name>.description",
      type: "string",
      description:
        "이름이 지정된 이 프로필에 대한 사람이 읽기 쉬운 설명입니다. 프로필은 `extends`를 통해 상위 프로필의 설명을 상속하지 않습니다.",
    },
    {
      key: "permissions.<name>.extends",
      type: "string",
      description:
        "이름이 지정된 이 프로필에 앞서 적용할 상위 프로필입니다(선택 사항). 이름이 지정된 다른 프로필, `:read-only` 또는 `:workspace`로 설정하세요. `:danger-full-access`, 정의되지 않은 상위 프로필, 순환 참조는 허용되지 않습니다.",
    },
    {
      key: "permissions.<name>.workspace_roots",
      type: "table",
      description:
        "프로필에서 정의한 워크스페이스 루트입니다. 세션의 런타임 워크스페이스 루트와 함께 `:workspace_roots` 파일 시스템 규칙이 적용됩니다.",
    },
    {
      key: "permissions.<name>.workspace_roots.<path>",
      type: "boolean",
      description:
        "`true`이면 해당 경로를 프로필의 워크스페이스 루트 집합에 포함합니다. 비활성화된 항목은 적용되지 않습니다.",
    },
    {
      key: "permissions.<name>.filesystem",
      type: "table",
      description:
        "이름이 지정된 파일 시스템 권한 프로필입니다. 각 키는 절대 경로 또는 `:minimal`, `:workspace_roots` 같은 특수 토큰입니다.",
    },
    {
      key: "permissions.<name>.filesystem.glob_scan_max_depth",
      type: "number",
      description:
        "샌드박스가 시작되기 전에 일치 결과의 스냅샷을 생성하는 플랫폼에서 읽기 거부 glob 패턴을 확장할 최대 깊이입니다. 설정할 때는 `1` 이상이어야 합니다.",
    },
    {
      key: "permissions.<name>.filesystem.<path-or-glob>",
      type: '"read" | "write" | "deny" | table',
      description:
        "경로, glob 패턴 또는 특수 토큰에 대한 직접 접근을 허용하거나 중첩 항목의 범위를 해당 루트 아래로 지정합니다. 일치하는 경로의 읽기를 거부하려면 `\"deny\"`를 사용하세요.",
    },
    {
      key: 'permissions.<name>.filesystem.":workspace_roots".<subpath-or-glob>',
      type: '"read" | "write" | "deny"',
      description:
        "실제 적용되는 각 워크스페이스 루트를 기준으로 설정하는 파일 시스템 접근 범위입니다. 루트 자체에는 `\".\"`을 사용하세요. `\"**/*.env\"` 같은 glob 하위 경로에 `\"deny\"`를 설정해 읽기를 거부할 수 있습니다.",
    },
    {
      key: "permissions.<name>.network.enabled",
      type: "boolean",
      description:
        "이 권한 프로필에서 명령어의 네트워크 접근을 활성화합니다. 이 설정만으로는 네트워크 프록시가 시작되지 않습니다. `features.network_proxy`가 활성화되지 않았고 관리자가 설정한 네트워킹 요구 사항도 활성화되지 않은 경우, 명령어는 네트워크에 직접 접근하며 프로필의 도메인 규칙은 적용되지 않습니다.",
    },
    {
      key: "permissions.<name>.network.proxy_url",
      type: "string",
      description:
        "이 권한 프로필에서 샌드박스 네트워킹을 활성화할 때 사용하는 HTTP 리스너 URL입니다.",
    },
    {
      key: "permissions.<name>.network.enable_socks5",
      type: "boolean",
      description:
        "이 권한 프로필에서 샌드박스 네트워킹을 활성화할 때 SOCKS5 기능을 제공합니다.",
    },
    {
      key: "permissions.<name>.network.socks_url",
      type: "string",
      description: "이 권한 프로필에서 사용하는 SOCKS5 프록시 엔드포인트입니다.",
    },
    {
      key: "permissions.<name>.network.enable_socks5_udp",
      type: "boolean",
      description: "활성화하면 SOCKS5 리스너를 통한 UDP를 허용합니다.",
    },
    {
      key: "permissions.<name>.network.allow_upstream_proxy",
      type: "boolean",
      description:
        "샌드박스 네트워킹에서 다른 업스트림 프록시를 경유하도록 허용합니다.",
    },
    {
      key: "permissions.<name>.network.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "샌드박스 네트워킹 리스너가 루프백이 아닌 주소에 바인딩하도록 허용합니다. 활성화하면 리스너가 로컬호스트 외부에 노출될 수 있습니다.",
    },
    {
      key: "permissions.<name>.network.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "기본 허용 범위에 한정하지 않고 임의의 Unix 소켓 대상을 허용합니다. 엄격하게 통제되는 환경에서만 사용하세요.",
    },
    {
      key: "permissions.<name>.network.mode",
      type: "limited | full",
      description: "하위 프로세스 트래픽에 사용하는 네트워크 프록시 모드입니다.",
    },
    {
      key: "permissions.<name>.network.domains",
      type: "table",
      description:
        "샌드박스에서 실행하는 명령어에 적용되는 도메인 규칙입니다. `features.network_proxy` 또는 활성화된 관리자 지정 네트워킹 요구 사항이 프록시를 활성화하는 경우에만 적용됩니다. 정확히 일치하는 호스트, `*.example.com`, `**.example.com`, 전역 `*` 허용 규칙을 지원하며, `deny`가 우선합니다. 웹 검색, 앱, MCP 서버는 제한하지 않습니다.",
    },
    {
      key: "permissions.<name>.network.domains.<pattern>",
      type: "allow | deny",
      description:
        "정확히 일치하는 호스트 또는 `*.example.com`, `**.example.com` 같은 범위가 지정된 와일드카드 패턴을 허용하거나 거부합니다.",
    },
    {
      key: "permissions.<name>.network.unix_sockets",
      type: "table",
      description:
        "샌드박스 네트워킹의 Unix 소켓 허용 목록을 재정의합니다. 소켓 경로를 키로 사용하세요. `allow`는 경로를 추가하고 `deny`는 거부합니다.",
    },
    {
      key: "permissions.<name>.network.unix_sockets.<path>",
      type: "allow | deny",
      description:
        "`allow`로 Unix 소켓의 절대 경로를 실제 적용되는 허용 목록에 추가하거나 `deny`로 거부합니다. 거부된 항목은 실제 적용되는 허용 목록에서 제외됩니다.",
    },
    {
      key: "permissions.<name>.network.allow_local_binding",
      type: "boolean",
      description:
        "샌드박스 네트워킹을 통한 더 넓은 범위의 로컬/사설 네트워크 접근을 허용합니다. 이 설정이 `false`여도 정확한 로컬 IP 리터럴이나 `localhost`를 지정한 허용 규칙으로 특정 로컬 대상에 대한 접근을 허용할 수 있습니다.",
    },
    {
      key: "projects.<path>.trust_level",
      type: "string",
      description:
        "프로젝트나 작업 트리를 신뢰함 또는 신뢰하지 않음(`\"trusted\"` | `\"untrusted\"`)으로 표시합니다. 신뢰할 수 없는 프로젝트에서는 프로젝트 로컬 구성, 훅, 규칙을 비롯한 프로젝트 범위의 `.codex/` 레이어를 건너뜁니다.",
    },
    {
      key: "notice.hide_full_access_warning",
      type: "boolean",
      description: "전체 권한 경고 프롬프트의 확인 여부를 기록합니다.",
    },
    {
      key: "notice.hide_world_writable_warning",
      type: "boolean",
      description:
        "Windows에서 모든 사용자가 쓸 수 있는 디렉터리에 대한 경고를 확인했는지 기록합니다.",
    },
    {
      key: "notice.hide_rate_limit_model_nudge",
      type: "boolean",
      description: "요청 한도에 따른 모델 전환 알림을 끄기로 선택했는지 기록합니다.",
    },
    {
      key: "notice.hide_gpt5_1_migration_prompt",
      type: "boolean",
      description: "GPT-5.1 마이그레이션 프롬프트의 확인 여부를 기록합니다.",
    },
    {
      key: "notice.hide_gpt-5.1-codex-max_migration_prompt",
      type: "boolean",
      description:
        "gpt-5.1-codex-max 마이그레이션 프롬프트의 확인 여부를 기록합니다.",
    },
    {
      key: "notice.model_migrations",
      type: "map<string,string>",
      description: "사용자가 확인한 모델 마이그레이션을 old->new 매핑으로 기록합니다.",
    },
    {
      key: "forced_login_method",
      type: "chatgpt | api",
      description: "특정 인증 방식만 사용하도록 Codex를 제한합니다.",
    },
    {
      key: "forced_chatgpt_workspace_id",
      type: "string (uuid)",
      description: "ChatGPT 로그인을 특정 워크스페이스 식별자로 제한합니다.",
    },
  ]}
  client:load
/>

`config.toml`의 최신 JSON 스키마는 [여기](/codex/config-schema.json)에서 확인할 수 있습니다.

VS Code 또는 Cursor에서 `config.toml`을 편집할 때 자동 완성과 진단 기능을 사용하려면 [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) 확장 프로그램을 설치하고 `config.toml` 맨 위에 다음 줄을 추가하세요:

```toml
#:schema https://developers.openai.com/codex/config-schema.json

참고: `experimental_instructions_file`의 이름을 `model_instructions_file`로 변경하세요. Codex에서 이전 키는 사용 중단 예정(deprecated)입니다. 기존 구성도 새 이름을 사용하도록 업데이트하세요.

## `requirements.toml`

`requirements.toml`은 관리자가 강제 적용하는 구성 파일로, 보안에 민감한 설정을 사용자가 재정의할 수 없도록 제한합니다. 자세한 내용과 파일 위치, 예시는 [관리자 강제 적용 요구 사항](/ko-KR/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml)을 참조하세요.

ChatGPT Business 및 ChatGPT Enterprise 사용자의 경우 Codex는 클라우드에서 가져온
요구 사항도 적용할 수 있습니다. 우선순위에 관한 자세한 내용은 보안 페이지를 참조하세요.

`requirements.toml`의 `[features]`에서 `config.toml`과 동일한 정식 키를 사용해
런타임 기능 플래그를 고정하세요. 요구 사항에는 문서에 명시된 앱 전용 키도 포함할 수 있으며,
이러한 키는 `config.toml`에서 사용하지 않습니다. 생략한 키에는
제약이 적용되지 않습니다.

일부 관리형 요구 사항은 허용 목록 대신 특정 구성 값을
강제 적용합니다. 사용자는 강제 적용된 경로, 업데이트 기본 설정, 로그인 셸
정책, 피드백 설정 또는 Windows 비공개 데스크톱 설정을 재정의할 수 없습니다.

관리형 권한 프로필 허용 목록을 사용하려면 Codex 0.138.0 이상이 필요합니다.
Codex 0.137.0 이하에서는 `allowed_permission_profiles` 설정과
관리형 `default_permissions` 설정이 무시됩니다.

`allowed_sandbox_modes` 설정은 `sandbox_mode` 설정과 함께 사용하세요.
권한 프로필을 사용하는 배포에서는 `allowed_permission_profiles` 설정을
관리형 `default_permissions` 설정과 함께 사용하세요.

`[models.new_thread]` 테이블은 관리형 기본값을 제공하며, 값을 강제하지는 않습니다.
전용 CLI 플래그나 `--config` 재정의로 명시한 실행 옵션이 우선합니다.
모델이나 추론 수준을 명시적으로 재정의하면 관리형 모델 필드 두 개를 모두 건너뜁니다.
`service_tier` 설정은 이와 독립적으로 적용됩니다.

브라우저 요구 사항은 서로 구분되는 세 영역에 적용됩니다.
`in_app_browser`는 사용자가 직접 열고 사용하는 브라우저 창을 제어합니다.
`browser_use`는 에이전트가 브라우저에서 수행하는 작업을 제어합니다.
`computer_use`는 에이전트가 네이티브 데스크톱 앱에서 수행하는 작업을 제어합니다.

브라우저 및 컴퓨터 사용의 중첩 정책 값은 그 자체로 접근 권한을 부여하지 않습니다.
오리진별 또는 앱별 `allow`는 같은 정책 소스의 기본 대체 값을 재정의할 수 있지만,
일반적인 기능, 승인 및 기타 정책 검사는 계속 적용됩니다.
관리형 요구 사항과 `config.toml`이 모두 적용되는 경우에는
어느 쪽이든 `deny`가 있으면 우선합니다.

<ConfigTable
  options={[
    {
      key: "sqlite_home",
      type: "string (path)",
      description:
        "Codex가 SQLite 기반 런타임 상태를 저장할 디렉터리를 강제 지정합니다.",
    },
    {
      key: "log_dir",
      type: "string (path)",
      description: "Codex가 로컬 로그 파일을 기록할 디렉터리를 강제 지정합니다.",
    },
    {
      key: "model_catalog_json",
      type: "string (path)",
      description: "Codex가 시작할 때 사용할 JSON 모델 카탈로그를 강제 지정합니다.",
    },
    {
      key: "check_for_update_on_startup",
      type: "boolean",
      description: "Codex가 시작할 때 업데이트를 확인할지 여부를 강제 적용합니다.",
    },
    {
      key: "allow_login_shell",
      type: "boolean",
      description: "셸 도구가 로그인 셸을 시작할 수 있는지 여부를 강제 적용합니다.",
    },
    {
      key: "feedback",
      type: "table",
      description: "관리형 피드백 설정입니다.",
    },
    {
      key: "feedback.enabled",
      type: "boolean",
      description:
        "사용자가 모든 Codex 클라이언트에서 피드백을 제출할 수 있는지 여부를 강제 적용합니다.",
    },
    {
      key: "allowed_approval_policies",
      type: "array<string>",
      description:
        "`approval_policy`에 허용되는 값입니다(예: `untrusted`, `on-request`, `never`, `granular`).",
    },
    {
      key: "allowed_approvals_reviewers",
      type: "array<string>",
      description:
        "`approvals_reviewer`에 허용되는 값입니다(예: `user`, `auto_review`).",
    },
    {
      key: "guardian_policy_config",
      type: "string",
      description:
        "자동 검토를 위한 관리형 Markdown 정책 지침입니다. 로컬 `[auto_review].policy`보다 우선합니다. 빈 값은 무시됩니다.",
    },
    {
      key: "allowed_permission_profiles",
      type: "table<boolean>",
      description:
        "허용되는 권한 프로필의 전체 목록입니다. `true`로 설정된 프로필은 허용됩니다. 생략되거나 `false`로 설정된 프로필은 향후 버전에 추가되는 프로필을 포함해 모두 거부됩니다. 요구사항 소스를 결합할 때는 프로필 이름을 기준으로 항목을 매칭합니다.",
    },
    {
      key: "allowed_permission_profiles.<name>",
      type: "boolean",
      description:
        "로드된 설정 또는 요구사항 소스에 정의된 기본 제공 권한 프로필이나 사용자 지정 권한 프로필을 허용하거나 거부합니다. 나중에 적용되는 우선순위가 높은 요구사항 소스에서는 `false`를 사용해 앞서 적용된 우선순위가 낮은 소스에서 허용한 프로필을 비활성화할 수 있습니다.",
    },
    {
      key: "default_permissions",
      type: "string",
      description:
        "관리형 기본 권한 프로필입니다. 이 프로필은 `allowed_permission_profiles`에서 허용되어야 합니다. 동작을 예측할 수 있도록 명시적으로 설정하세요. 생략하면 Codex는 `:workspace`와 `:read-only`가 모두 명시적으로 허용된 경우에만 `:workspace`를 기본값으로 사용합니다.",
    },
    {
      key: "enforce_residency",
      type: "string",
      description:
        "Codex 서비스 트래픽에 지원되는 데이터 레지던시를 사용하도록 강제합니다. 현재는 `us`를 허용합니다.",
    },
    {
      key: "models",
      type: "table",
      description:
        "새 스레드에 적용할 관리형 모델 기본값입니다. 사용자 및 프로젝트 기본값보다 우선하지만, 새 스레드에서 명시적으로 선택한 값으로 재정의할 수 있습니다.",
    },
    {
      key: "models.new_thread",
      type: "table",
      description:
        "새 로컬 스레드를 시작할 때 적용할 기본값입니다. 각 모델 설정은 선택 사항입니다.",
    },
    {
      key: "models.new_thread.model",
      type: "string",
      description:
        "새 스레드의 기본 모델입니다. `--model` 또는 모델/추론 관련 `--config`로 명시적으로 재정의한 값이 우선합니다.",
    },
    {
      key: "models.new_thread.model_reasoning_effort",
      type: "string",
      description:
        "새 스레드의 기본 추론 노력 수준입니다. 모델 또는 추론 노력 수준을 명시적으로 재정의하면 두 관리형 모델 필드를 모두 건너뜁니다.",
    },
    {
      key: "models.new_thread.service_tier",
      type: "string",
      description:
        "새 스레드의 기본 서비스 등급입니다. 서비스 등급을 명시적으로 재정의한 값은 모델 필드와 독립적으로 우선 적용됩니다.",
    },
    {
      key: "permissions",
      type: "table",
      description:
        "프로필 이름을 키로 사용하는 관리자 정의 권한 프로필입니다. `config.toml`과 동일한 프로필 필드를 사용합니다.",
    },
    {
      key: "permissions.<name>",
      type: "table",
      description:
        "관리자가 정의한 권한 프로필입니다. 이름은 `:`로 시작할 수 없고, 예약된 이름인 `filesystem`을 사용할 수 없으며, 로드된 설정의 프로필 이름과 중복될 수 없습니다. `config.toml`과 동일한 프로필 필드를 사용합니다. 전체 프로필 스키마는 권한 가이드를 참고하세요.",
    },
    {
      key: "allowed_sandbox_modes",
      type: "array<string>",
      description: "`sandbox_mode`에 허용되는 값입니다.",
    },
    {
      key: "windows",
      type: "table",
      description: "네이티브 Windows 샌드박스 요구사항입니다.",
    },
    {
      key: "windows.allowed_sandbox_implementations",
      type: "array<string>",
      description:
        "`windows.sandbox`에 허용되는 네이티브 Windows 샌드박스 구현(`elevated` 및 `unelevated`)입니다. 목록은 비어 있으면 안 됩니다. 둘 다 허용되고 모드를 선택하지 않은 경우 Codex는 `elevated`를 우선 사용합니다.",
    },
    {
      key: "windows.sandbox_private_desktop",
      type: "boolean",
      description:
        "네이티브 Windows 샌드박스가 전용 데스크톱에서 자식 프로세스를 시작할지 여부를 강제 설정합니다.",
    },
    {
      key: "remote_sandbox_config",
      type: "array<table>",
      description:
        "호스트별 샌드박스 요구사항입니다. 확인된 호스트 이름과 `hostname_patterns`가 일치하는 첫 번째 항목이 해당 요구사항 소스의 최상위 `allowed_sandbox_modes`를 재정의합니다. 현재 호스트별 항목은 샌드박스 모드만 재정의합니다.",
    },
    {
      key: "remote_sandbox_config[].hostname_patterns",
      type: "array<string>",
      description:
        "대소문자를 구분하지 않는 호스트 이름 패턴입니다. 임의 길이의 문자열을 나타내는 `*`와 문자 하나를 나타내는 `?`를 지원합니다.",
    },
    {
      key: "remote_sandbox_config[].allowed_sandbox_modes",
      type: "array<string>",
      description:
        "이 호스트별 항목과 일치하는 경우 적용할 허용 샌드박스 모드입니다.",
    },
    {
      key: "allowed_web_search_modes",
      type: "array<string>",
      description:
        "`web_search`에 허용되는 값(`disabled`, `cached`, `indexed`, `live`)입니다. `disabled`는 항상 허용되며, 빈 목록을 설정하면 사실상 `disabled`만 허용됩니다.",
    },
    {
      key: "allow_managed_hooks_only",
      type: "boolean",
      description:
        "`true`이면 Codex는 사용자, 프로젝트, 세션 및 플러그인 훅을 건너뛰지만, `requirements.toml` 및 다른 관리형 설정 레이어의 관리형 훅은 계속 허용합니다.",
    },
    {
      key: "allow_appshots",
      type: "boolean",
      description:
        "관리 대상 사용자의 앱샷을 비활성화하려면 `false`로 설정하세요. 생략하면 앱샷은 요구사항의 제한 없이 일반적인 제품 제공 조건을 따릅니다.",
    },
    {
      key: "allow_remote_control",
      type: "boolean",
      description:
        "관리 대상 사용자의 기기 원격 제어를 비활성화하려면 `false`로 설정하세요. 생략하면 기기 원격 제어는 요구사항의 제한 없이 일반적인 제품 제공 조건을 따릅니다.",
    },
    {
      key: "allow_browser_and_computer_use",
      type: "boolean",
      description:
        "에이전트가 제어하는 브라우저 기능과 네이티브 앱에서의 컴퓨터 사용 기능을 모두 차단하려면 `false`로 설정하세요. `true`로 설정하거나 생략해도 두 기능 중 어느 것도 활성화되지 않으며, 나머지 기능, 정책 및 승인 검사가 계속 적용됩니다.",
    },
    {
      key: "features.plugin_sharing",
      type: "boolean",
      description:
        "로컬에서 빌드한 플러그인의 워크스페이스 공유를 비활성화하려면 클라우드에서 관리하는 `requirements.toml`에서 `false`로 설정하세요.",
    },
    {
      key: "features",
      type: "table",
      description:
        "고정된 기능 값입니다. 런타임 기능에는 `config.toml`의 정식 이름을 사용하세요. 문서에 명시된 앱 전용 요구사항 키도 여기에서 지원합니다.",
    },
    {
      key: "features.<name>",
      type: "boolean",
      description:
        "문서에 명시된 런타임 또는 앱 기능을 활성화 또는 비활성화 상태로 유지하도록 강제합니다.",
    },
    {
      key: "features.apps",
      type: "boolean",
      description:
        "관리 대상 사용자의 앱 통합 기능을 활성화 또는 비활성화 상태로 고정합니다.",
    },
    {
      key: "features.in_app_updates",
      type: "boolean",
      description:
        "앱 내 업데이트를 비활성화하려면 `requirements.toml`에서 `false`로 설정하세요. 이 요구사항을 생략하면 업데이트는 기본적으로 활성화됩니다.",
    },
    {
      key: "features.in_app_browser",
      type: "boolean",
      description:
        "사용자가 직접 열고 제어하는 내장 브라우저 패널을 비활성화하려면 `requirements.toml`에서 `false`로 설정하세요.",
    },
    {
      key: "features.browser_use",
      type: "boolean",
      description:
        "에이전트가 제어하는 브라우저 기능을 비활성화하려면 `requirements.toml`에서 `false`로 설정하세요.",
    },
    {
      key: "features.browser_use_external",
      type: "boolean",
      description:
        "Codex가 ChatGPT 브라우저 확장 프로그램을 통해 기존 탭과 로그인된 세션을 포함한 지원 브라우저를 조작하지 못하게 하려면 `requirements.toml`에서 `false`로 설정하세요.",
    },
    {
      key: "features.browser_use_full_cdp_access",
      type: "boolean",
      description:
        "`requirements.toml`에서 `false`로 설정하면 브라우저 개발자 모드를 비롯해 로컬 런타임의 Chrome DevTools Protocol에 대한 전체 접근이 비활성화되며, ChatGPT 데스크톱 앱에서도 해당 설정을 활성화할 수 없게 됩니다. 생략하면 일반적인 제품 제공 조건이 적용됩니다.",
    },
    {
      key: "features.fast_mode",
      type: "boolean",
      description:
        "관리 대상 사용자의 정식 `fast_mode` 기능을 활성화 또는 비활성화 상태로 고정합니다.",
    },
    {
      key: "features.guardian_approval",
      type: "boolean",
      description:
        "관리 대상 사용자의 Guardian 승인 기능을 활성화 또는 비활성화 상태로 고정합니다.",
    },
    {
      key: "features.memories",
      type: "boolean",
      description: "관리 대상 사용자의 메모리 기능을 활성화 또는 비활성화 상태로 고정합니다.",
    },
    {
      key: "features.multi_agent",
      type: "boolean",
      description: "관리 대상 사용자의 다중 에이전트 기능을 활성화 또는 비활성화 상태로 고정합니다.",
    },
    {
      key: "features.plugins",
      type: "boolean",
      description: "관리 대상 사용자의 플러그인 기능을 활성화 또는 비활성화 상태로 고정합니다.",
    },
    {
      key: "features.remote_plugin",
      type: "boolean",
      description:
        "관리 대상 사용자의 원격 플러그인 카탈로그 기능을 활성화 또는 비활성화 상태로 고정합니다.",
    },
    {
      key: "features.computer_use",
      type: "boolean",
      description:
        "컴퓨터 사용, 기록 및 재생, 관련 설치 또는 활성화 플로우를 비활성화하려면 `requirements.toml`에서 `false`로 설정하세요.",
    },
    {
      key: "features.workspace_dependencies",
      type: "boolean",
      description:
        "관리 대상 사용자에게 번들로 제공되는 워크스페이스 종속성 런타임을 활성화 또는 비활성화 상태로 고정합니다.",
    },
    {
      key: "in_app_browser",
      type: "table",
      description:
        "내장 브라우저 패널의 요구사항입니다. 이 설정은 에이전트가 제어하는 브라우저 기능에는 적용되지 않습니다.",
    },
    {
      key: "in_app_browser.allow_external_browser_settings_import",
      type: "boolean",
      description:
        "사용자가 외부 브라우저의 설정이나 탐색 데이터를 내장 브라우저로 가져오지 못하게 하려면 `false`로 설정하세요. `true`로 설정하거나 생략하면 다른 제품 검사에서 허용하는 경우 가져오기 기능을 계속 사용할 수 있습니다. 관리형 전용 설정이며 `config.toml`로 재정의할 수 없습니다.",
    },
    {
      key: "browser_use",
      type: "table",
      description: "에이전트가 제어하는 브라우저 기능에 대한 관리형 요구사항입니다.",
    },
    {
      key: "browser_use.allow_history_access",
      type: "boolean",
      description:
        "브라우저 기능이 브라우저 방문 기록을 읽지 못하게 하려면 `false`로 설정하세요. `true`로 설정하거나 생략하면 일반적인 방문 기록 설정과 사용 가능 여부 검사가 그대로 적용됩니다.",
    },
    {
      key: "browser_use.disable_auto_review",
      type: "boolean",
      description:
        "브라우저 기능의 자동 검토를 건너뛰고 대신 사용자에게 승인을 요청하려면 `true`로 설정하세요. `false`로 설정하거나 생략하면 다른 설정에서 허용하는 경우 자동 검토를 계속 사용할 수 있습니다.",
    },
    {
      key: "browser_use.allow_global_persistent_approval",
      type: "boolean",
      description:
        "브라우저 기능이 모든 사이트에서 다운로드를 허용하는 것처럼 모든 사이트에 적용되는 `Always allow` 승인을 생성하거나 적용하지 못하게 하려면 `false`로 설정하세요. 기존에 저장된 승인은 삭제되지 않고 무시됩니다. `true`로 설정하거나 생략해도 승인이 생성되지는 않습니다.",
    },
    {
      key: "browser_use.default_origin_policy",
      type: "table",
      description:
        "`browser_use.origins`에서 일치하는 항목에 정의되지 않은 각 브라우저 설정에 적용할 대체값입니다. 일치하는 오리진 규칙이 있으면 해당 소스의 대체값을 대신합니다. 그런 다음 Codex는 관리형 요구사항과 사용자 설정 중 더 엄격한 결과를 적용합니다.",
    },
    {
      key: "browser_use.default_origin_policy.access",
      type: "allow | deny",
      description:
        "대체값을 사용하는 오리진에서 브라우저 기능을 차단하려면 `deny`를 사용하세요. 거부된 오리진에서는 업로드, 다운로드, 전체 브라우저 디버깅 접근 및 자동 검토도 차단됩니다. `allow`는 일반적인 승인 및 정책 검사를 계속 진행할 수 있게 할 뿐입니다.",
    },
    {
      key: "browser_use.default_origin_policy.downloads",
      type: "allow | deny",
      description:
        "대체값을 사용하는 오리진에서 브라우저 기능의 다운로드를 차단하려면 `deny`를 사용하세요. `allow`는 일반적인 승인 및 정책 검사를 계속 진행할 수 있게 할 뿐입니다.",
    },
    {
      key: "browser_use.default_origin_policy.uploads",
      type: "allow | deny",
      description:
        "대체값을 사용하는 오리진에서 브라우저 기능의 업로드를 차단하려면 `deny`를 사용하세요. `allow`는 일반적인 승인 및 정책 검사를 계속 진행할 수 있게 할 뿐입니다.",
    },
    {
      key: "browser_use.default_origin_policy.full_cdp_access",
      type: "allow | deny",
      description:
        "대체값을 사용하는 오리진에서 Chrome DevTools Protocol(CDP)에 대한 전체 접근을 차단하려면 `deny`를 사용하세요. `allow`는 일반적인 사용 동의 및 승인 검사를 계속 진행할 수 있게 할 뿐입니다.",
    },
    {
      key: "browser_use.default_origin_policy.auto_review",
      type: "allow | deny",
      description:
        "대체값을 사용하는 오리진에서 자동 검토를 건너뛰고 대신 사용자에게 승인을 요청하려면 `deny`를 사용하세요. `allow`는 다른 설정에서 허용하는 경우 자동 검토를 계속 사용할 수 있게 합니다.",
    },
    {
      key: "browser_use.default_origin_policy.persistent_approval",
      type: "boolean",
      description:
        "대체값을 사용하는 오리진에서 브라우저 기능이 `Always allow` 승인을 저장하거나 적용하지 못하게 하려면 `false`로 설정하세요. 현재 턴이나 스레드에 대한 승인은 계속 적용될 수 있습니다. `true`는 다른 조건에서 허용하는 경우 `Always allow`를 사용할 수 있게 하지만, 승인을 생성하지는 않습니다.",
    },
    {
      key: "browser_use.default_origin_policy.access_approval_lifetime",
      type: "turn | thread",
      description:
        "영구 저장되지 않는 사이트 접근 승인의 유효 기간을 설정합니다. `turn`은 현재 턴으로 제한하고, `thread`는 현재 스레드가 끝날 때까지 유지합니다. `Always allow` 사용 가능 여부는 `persistent_approval`에서 별도로 제어합니다. 제품 기본값은 `thread`입니다.",
    },
    {
      key: "browser_use.origins",
      type: "map<string, table>",
      description:
        "오리진별 브라우저 정책입니다. 키는 `http` 또는 `https`를 사용한 `<scheme>://<host-pattern>[:<port>]` 형식입니다. 정확한 호스트를 지정하거나, 하위 도메인만 지정하려면 `*.example.com`을, 기본 도메인과 하위 도메인을 모두 지정하려면 `**.example.com`을 사용하세요. 그 외의 `*` 와일드카드는 점도 포함할 수 있으므로 `region*.example.com`은 `region.api.example.com`과도 일치합니다. 호스트가 `*`이면 해당 스킴의 모든 호스트와 일치합니다. 스킴과 기본값이 아닌 포트는 구분되며, 명시적으로 지정한 기본 포트는 정규화 과정에서 제거됩니다. 경로, 쿼리, URL에 포함된 사용자 이름이나 비밀번호, 와일드카드 스킴 또는 포트는 허용되지 않습니다. TOML에서는 `[browser_use.origins.\"https://**.example.com\"]`과 같이 패턴을 따옴표로 감싸세요.",
    },
    {
      key: "browser_use.origins.<pattern>",
      type: "table",
      description:
        "이 패턴과 일치하는 오리진에 적용할 정책입니다. 여러 패턴이 일치하면 Codex는 각 기능에 대해 가장 제한적인 값을 사용합니다. `allow`보다 `deny`, `true`보다 `false`, `thread`보다 `turn`이 우선합니다.",
    },
    {
      key: "browser_use.origins.<pattern>.access",
      type: "allow | deny",
      description:
        "일치하는 오리진에서 브라우저 기능을 차단하려면 `deny`를 사용하세요. 거부하면 해당 오리진의 업로드, 다운로드, 전체 브라우저 디버깅 접근 및 자동 검토도 차단됩니다. `allow`는 일반적인 승인 및 정책 검사를 계속 진행할 수 있게 할 뿐입니다.",
    },
    {
      key: "browser_use.origins.<pattern>.downloads",
      type: "allow | deny",
      description:
        "일치하는 오리진에서 브라우저 기능의 다운로드를 차단하려면 `deny`를 사용하세요. `allow`는 일반적인 승인 및 정책 검사를 계속 진행할 수 있게 할 뿐입니다.",
    },
    {
      key: "browser_use.origins.<pattern>.uploads",
      type: "allow | deny",
      description:
        "일치하는 오리진에서 브라우저 기능의 업로드를 차단하려면 `deny`를 사용하세요. `allow`는 일반적인 승인 및 정책 검사를 계속 진행할 수 있게 할 뿐입니다.",
    },
    {
      key: "browser_use.origins.<pattern>.full_cdp_access",
      type: "allow | deny",
      description:
        "일치하는 오리진에서 Chrome DevTools Protocol(CDP)에 대한 전체 접근을 차단하려면 `deny`를 사용하세요. `allow`는 일반적인 사용 동의 및 승인 검사를 계속 진행할 수 있게 할 뿐입니다.",
    },
    {
      key: "browser_use.origins.<pattern>.auto_review",
      type: "allow | deny",
      description:
        "일치하는 오리진에서 자동 검토를 건너뛰고 대신 사용자에게 승인을 요청하려면 `deny`를 사용하세요. `allow`는 다른 설정에서 허용하는 경우 자동 검토를 계속 사용할 수 있게 합니다.",
    },
    {
      key: "browser_use.origins.<pattern>.persistent_approval",
      type: "boolean",
      description:
        "일치하는 오리진에서 브라우저 기능이 `Always allow` 승인을 저장하거나 적용하지 못하게 하려면 `false`로 설정하세요. 현재 턴이나 스레드에 대한 승인은 계속 적용될 수 있습니다. `true`는 다른 조건에서 허용하는 경우 `Always allow`를 사용할 수 있게 하지만, 승인을 생성하지는 않습니다.",
    },
    {
      key: "browser_use.origins.<pattern>.access_approval_lifetime",
      type: "turn | thread",
      description:
        "일치하는 오리진에 대해 영구 저장되지 않는 사이트 접근 승인의 유효 기간을 설정합니다. `turn`은 현재 턴으로 제한하고, `thread`는 현재 스레드가 끝날 때까지 유지합니다. `Always allow` 사용 가능 여부는 `persistent_approval`에서 별도로 제어합니다.",
    },
    {
      key: "computer_use",
      type: "table",
      description:
        "네이티브 데스크톱 앱에서 에이전트가 수행하는 작업에 대한 관리형 요구사항입니다. 관리형 앱 규칙과 `config.toml`의 앱 규칙이 모두 적용되며, 앱은 각 정책 소스에서 모두 허용되어야 합니다.",
    },
    {
      key: "computer_use.allow_locked_computer_use",
      type: "boolean",
      description:
        "`false`로 설정하면 관리형 macOS 기기에서 사용자가 잠금 상태 사용을 활성화할 수 없습니다. 이 요구사항은 활성화 컨트롤을 제거하지만, 이미 활성화된 잠금 상태 사용을 끄지는 않습니다. 생략하면 일반적인 제품 제공 조건이 적용됩니다.",
    },
    {
      key: "computer_use.allow_persistent_approval",
      type: "boolean",
      description:
        "`false`로 설정하면 앱 승인을 세션 간에 유지하도록 저장하는 옵션이 제거됩니다. 현재 세션에 대한 승인은 계속 사용할 수 있습니다. `true`로 설정하거나 생략해도 앱이 승인되지는 않습니다.",
    },
    {
      key: "computer_use.default_app_access",
      type: "allow | deny",
      description:
        "플랫폼별 규칙과 일치하지 않는 네이티브 앱에 적용할 기본 접근 설정입니다. `deny`는 접근을 차단합니다. `allow`는 일반적인 승인 및 정책 검사를 계속 진행하도록 허용할 뿐입니다. 제품 기본값은 `allow`입니다.",
    },
    {
      key: "computer_use.macos",
      type: "table",
      description: "macOS 앱에 대한 컴퓨터 사용 규칙입니다.",
    },
    {
      key: "computer_use.macos.bundle_ids",
      type: "map<string, allow | deny>",
      description:
        "정확한 macOS 번들 식별자를 `allow` 또는 `deny`에 매핑합니다. 일치하는 규칙은 같은 정책 소스의 `computer_use.default_app_access`를 대체합니다. 관리형 요구사항이나 사용자 설정 중 어느 한쪽에서라도 거부하면 접근이 차단됩니다.",
    },
    {
      key: "computer_use.macos.bundle_ids.<bundle-id>",
      type: "allow | deny",
      description:
        "정확히 일치하는 번들 식별자를 차단하려면 `deny`를 사용합니다. `allow`는 이 정책 소스의 기본값만 재정의하며, 다른 모든 정책 소스와 일반적인 승인 플로우에서도 해당 앱을 허용해야 합니다.",
    },
    {
      key: "computer_use.windows",
      type: "table",
      description:
        "패키징된 Windows 앱과 패키징되지 않은 Windows 앱에 대한 컴퓨터 사용 규칙입니다.",
    },
    {
      key: "computer_use.windows.aumids",
      type: "map<string, allow | deny>",
      description:
        "서명된 패키지 앱에 등록된 정확한 Application User Model ID(AUMID)를 `allow` 또는 `deny`에 매핑합니다. 일치하는 규칙은 같은 정책 소스의 `computer_use.default_app_access`를 대체합니다.",
    },
    {
      key: "computer_use.windows.aumids.<aumid>",
      type: "allow | deny",
      description:
        "정확히 일치하는 패키지 앱 식별 정보를 차단하려면 `deny`를 사용합니다. `allow`는 이 정책 소스의 기본값만 재정의하며, 다른 모든 정책 소스와 일반적인 승인 플로우에서도 해당 앱을 허용해야 합니다.",
    },
    {
      key: "computer_use.windows.exes",
      type: "array<table>",
      description:
        "서명되었지만 패키징되지 않은 Windows 실행 파일에 대한 규칙입니다. 규칙은 실행 파일의 경로나 현재 파일 이름이 아니라 검증된 게시자와 서명된 버전 정보를 기준으로 일치 여부를 확인합니다. 일치하는 거부 규칙은 일치하는 허용 규칙보다 우선합니다. 서명되지 않은 실행 파일에는 `computer_use.default_app_access`가 적용되며, 서명된 식별 정보를 명확하게 검증할 수 없는 실행 파일은 차단됩니다.",
    },
    {
      key: "computer_use.windows.exes[].publisher_name",
      type: "string",
      description:
        "실행 파일의 신뢰할 수 있는 서명 인증서에 기재된 정확한 게시자 이름입니다. 필수 항목이며 Windows X.500 고유 이름 형식으로 지정합니다.",
    },
    {
      key: "computer_use.windows.exes[].product_name",
      type: "string",
      description:
        "실행 파일의 서명된 버전 정보에 기재된 정확한 `ProductName`입니다. 필수 항목입니다.",
    },
    {
      key: "computer_use.windows.exes[].binary_name",
      type: "string",
      description:
        "실행 파일의 서명된 버전 정보에 기재된 `OriginalFilename`입니다. 선택 사항이며, 일치 여부를 확인할 때 대소문자를 구분하지 않습니다. 게시자와 제품이 일치하는 규칙에서 이 값을 요구하지만 실행 파일이 제공하지 않으면 컴퓨터 사용이 해당 실행 파일을 차단합니다.",
    },
    {
      key: "computer_use.windows.exes[].access",
      type: "allow | deny",
      description:
        "일치하는 실행 파일의 접근 허용 여부를 결정하는 필수 설정입니다. `deny`는 접근을 차단합니다. `allow`는 이 정책 소스의 기본값만 재정의하며, 다른 모든 정책 소스와 일반적인 승인 플로우에서도 해당 앱을 허용해야 합니다.",
    },
    {
      key: "experimental_network",
      type: "table",
      description:
        "샌드박스 내 로컬 명령어에 대해 관리자가 관리하고 `requirements.toml`에서 강제 적용하는 네트워크 요구사항입니다. 활성화하면 `features.network_proxy` 없이도 명령어 네트워크 프록시를 시작할 수 있습니다. 브라우저 도구는 관리형 네트워크 거부 규칙과 배타적 허용 목록을 별도로 확인합니다. 이 요구사항은 브라우저 트래픽을 프록시로 라우팅하지 않으며, 웹 검색, 앱, MCP 서버, 네이티브 앱 트래픽 또는 Codex 클라우드 네트워킹을 제어하지 않습니다.",
    },
    {
      key: "experimental_network.enabled",
      type: "boolean",
      description:
        "샌드박스 네트워킹 요구사항을 활성화합니다. 활성 샌드박스에서 명령어 네트워킹을 꺼 둔 경우에는 네트워크 접근을 허용하지 않습니다.",
    },
    {
      key: "experimental_network.http_port",
      type: "integer",
      description:
        "`[experimental_network]` 요구사항에 사용할 루프백 HTTP 리스너 포트입니다.",
    },
    {
      key: "experimental_network.socks_port",
      type: "integer",
      description:
        "`[experimental_network]` 요구사항에 사용할 루프백 SOCKS5 리스너 포트입니다.",
    },
    {
      key: "experimental_network.allow_upstream_proxy",
      type: "boolean",
      description:
        "샌드박스 네트워킹이 환경에 설정된 업스트림 프록시를 경유하도록 허용합니다.",
    },
    {
      key: "experimental_network.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "`[experimental_network]` 요구사항에서 루프백이 아닌 리스너 주소를 허용합니다. 활성화하면 로컬호스트 외부에 리스너가 노출될 수 있습니다.",
    },
    {
      key: "experimental_network.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "허용 목록에 있는 대상뿐 아니라 임의의 Unix 소켓 대상에 접근하도록 허용합니다. 엄격하게 통제되는 환경에서만 사용하세요.",
    },
    {
      key: "experimental_network.domains",
      type: "map<string, allow | deny>",
      description:
        "샌드박스 네트워킹에 적용되는 맵 형식의 관리자 도메인 정책입니다. 정확한 호스트, 하위 도메인만 포함하는 `*.example.com`, 루트 도메인과 하위 도메인을 모두 포함하는 `**.example.com`, 전역 `*` 허용 규칙을 지원합니다. `*`는 공용 네트워크로의 아웃바운드 접근을 광범위하게 열기 때문에 범위를 제한한 규칙을 사용하는 것이 좋습니다. 충돌 시 `deny`가 우선합니다. `experimental_network.allowed_domains` 또는 `experimental_network.denied_domains`와 함께 사용하지 마세요.",
    },
    {
      key: "experimental_network.allowed_domains",
      type: "array<string>",
      description:
        "관리형 네트워크 프록시가 활성화된 동안 샌드박스 내 명령어의 네트워킹에 적용되는 관리자 허용 규칙입니다. 웹 검색, 앱 또는 MCP 서버에는 적용되지 않습니다. `experimental_network.domains`와 함께 사용하지 마세요.",
    },
    {
      key: "experimental_network.denied_domains",
      type: "array<string>",
      description:
        "샌드박스 네트워킹에 적용되는 목록 형식의 관리자 거부 규칙입니다. `experimental_network.domains`와 함께 사용하지 마세요.",
    },
    {
      key: "experimental_network.managed_allowed_domains_only",
      type: "boolean",
      description:
        "`true`이면 샌드박스 네트워킹 요구사항이 활성화된 동안 관리자가 관리하는 허용 규칙만 적용되며, 사용자가 허용 목록에 추가한 항목은 무시됩니다. 관리형 허용 규칙이 없어도 사용자가 추가한 도메인 허용 규칙은 적용되지 않습니다.",
    },
    {
      key: "experimental_network.unix_sockets",
      type: "map<string, allow | deny>",
      description:
        "샌드박스 네트워킹에 대해 관리자가 관리하는 Unix 소켓 정책입니다.",
    },
    {
      key: "experimental_network.allow_local_binding",
      type: "boolean",
      description:
        "샌드박스 네트워킹에서 더 광범위한 로컬 및 사설 네트워크 접근을 허용합니다. `false`로 유지해도 정확한 로컬 IP 리터럴이나 `localhost` 허용 규칙으로 특정 로컬 대상에 대한 접근을 허용할 수 있습니다.",
    },
    {
      key: "hooks",
      type: "table",
      description:
        "관리자가 강제 적용하는 관리형 수명 주기 훅입니다. 관리형 훅 디렉터리가 필요하며, `config.toml`의 인라인 `[hooks]`와 동일한 이벤트 스키마를 사용합니다.",
    },
    {
      key: "hooks.managed_dir",
      type: "string (absolute path)",
      description:
        "macOS와 Linux에서 관리형 훅 스크립트가 있는 디렉터리입니다. Codex는 관리형 훅을 로드하기 전에 이 경로가 절대 경로이고 실제로 존재하는지 검증합니다.",
    },
    {
      key: "hooks.windows_managed_dir",
      type: "string (absolute path)",
      description:
        "Windows에서 관리형 훅 스크립트가 있는 디렉터리입니다. Codex는 관리형 훅을 로드하기 전에 이 경로가 절대 경로이고 실제로 존재하는지 검증합니다.",
    },
    {
      key: "hooks.",
      type: "array<table>",
      description:
        "`PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `SessionStart`, `SessionEnd`, `SubagentStart`, `SubagentStop`, `UserPromptSubmit`, `Stop` 등의 훅 이벤트에 대한 매처 그룹입니다.",
    },
    {
      key: "hooks.[].hooks",
      type: "array<table>",
      description:
        "매처 그룹의 훅 핸들러입니다. 명령어 훅과 MCP 도구 훅을 지원하며, 프롬프트 및 에이전트 훅 핸들러는 파싱하지만 실행하지 않습니다.",
    },
    {
      key: "hooks.[].hooks[].async",
      type: "boolean",
      description:
        "훅을 트리거한 작업을 지연시키지 않고 명령어 훅을 백그라운드에서 실행합니다. 기본값은 `false`이며, `SessionEnd`는 항상 동기적으로 실행됩니다. [백그라운드에서 훅 실행](/codex/hooks#run-hooks-in-the-background)을 참고하세요.",
    },
    {
      key: "hooks.[].hooks[].additionalContextLimit",
      type: "integer",
      description:
        "너무 큰 `additionalContext`를 디스크에 저장하고 모델에 더 짧은 미리보기를 표시하는 핸들러별 대략적인 토큰 임계값입니다. 기본값은 `2500`이며, `0`이면 전체 컨텍스트를 모델에 직접 전달합니다. [대용량 훅 출력](/codex/hooks#large-hook-output)을 참고하세요.",
    },
    {
      key: "hooks.[].hooks[].commandWindows",
      type: "string",
      description:
        "명령어 훅의 명령어를 Windows에서만 재정의하는 설정입니다. TOML 별칭인 `command_windows`도 사용할 수 있습니다.",
    },
    {
      key: "permissions.filesystem.deny_read",
      type: "array<string>",
      description:
        "관리자가 강제 적용하는 파일 시스템 읽기 거부 규칙입니다. 항목으로 경로나 glob 패턴을 지정할 수 있으며, 사용자는 로컬 설정으로 이 제한을 완화할 수 없습니다.",
    },
    {
      key: "mcp_servers",
      type: "table",
      description:
        "활성화할 수 있는 MCP 서버의 허용 목록입니다. MCP 서버를 활성화하려면 서버 이름(`<id>`)과 식별 정보가 모두 일치해야 합니다. 설정된 MCP 서버라도 허용 목록에 없거나 식별 정보가 일치하지 않으면 비활성화됩니다.",
    },
    {
      key: "mcp_servers.<id>.identity",
      type: "table",
      description:
        "단일 MCP 서버의 식별 규칙입니다. `command`(stdio) 또는 `url`(스트리밍 가능한 HTTP) 중 하나를 설정합니다.",
    },
    {
      key: "mcp_servers.<id>.identity.command",
      type: "string | table",
      description:
        "MCP stdio 서버를 정확히 일치하는 명령어 문자열로 허용하거나, 매처 테이블을 사용해 실행 파일이 정확히 일치하고 인수가 순서대로 지정된 매처와 일치하도록 요구합니다. 문자열 형식은 인수, `cwd`, `env`, `env_vars`를 검사하지 않습니다.",
    },
    {
      key: "mcp_servers.<id>.identity.command.executable",
      type: "string",
      description:
        "stdio 서버에 설정된 `command`가 정확히 일치해야 하는 실행 파일입니다.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args",
      type: "array<table>",
      description:
        "stdio 서버의 인수 매처를 순서대로 나열한 목록입니다. 설정된 인수 목록은 길이가 같아야 하며, 각 위치의 인수가 해당 매처와 일치해야 합니다. 명령어 매처는 `cwd`, `env`, `env_vars`를 검사하지 않습니다.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].match",
      type: "exact | prefix | regex",
      description: "이 인수 위치에 적용할 매칭 연산입니다.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].value",
      type: "string",
      description: "`exact` 또는 `prefix` 인수 매처가 사용하는 값입니다.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].expression",
      type: "string",
      description:
        "`regex` 인수 매처가 사용하는 정규식입니다. 이 정규식은 유효해야 하며 인수 값 전체와 일치해야 합니다.",
    },
    {
      key: "mcp_servers.<id>.identity.url",
      type: "string | table",
      description:
        "MCP 스트리밍 가능한 HTTP 서버를 정확히 일치하는 URL 문자열로 허용하거나, `exact`, `prefix` 또는 `regex` 값 매처 테이블을 사용합니다.",
    },
    {
      key: "mcp_servers.<id>.identity.url.match",
      type: "exact | prefix | regex",
      description: "설정된 MCP 서버 URL에 적용할 매칭 연산입니다.",
    },
    {
      key: "mcp_servers.<id>.identity.url.value",
      type: "string",
      description: "`exact` 또는 `prefix` URL 매처가 사용하는 값입니다.",
    },
    {
      key: "mcp_servers.<id>.identity.url.expression",
      type: "string",
      description:
        "`regex` URL 매처가 사용하는 정규식입니다. 이 정규식은 유효해야 하며 URL 값 전체와 일치해야 합니다.",
    },
    {
      key: "plugins",
      type: "table",
      description:
        "플러그인 식별자를 키로 사용하는 플러그인별 MCP 서버 허용 목록입니다. 이 테이블이 있으면 일치하는 플러그인 및 서버 항목이 없는 플러그인 내장 서버는 비활성화됩니다.",
    },
    {
      key: "plugins.<plugin>.mcp_servers",
      type: "table",
      description:
        "플러그인 하나에 포함된 MCP 서버의 허용 목록입니다. 플러그인 서버 요구사항은 최상위 `mcp_servers` 요구사항과 동일한 형식으로 식별 정보의 정확한 일치 조건이나 매처를 지정합니다.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity",
      type: "table",
      description:
        "플러그인에 포함된 MCP 서버 하나의 식별 규칙입니다. `command`(stdio) 또는 `url`(스트리밍 가능한 HTTP) 중 하나를 설정합니다.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command",
      type: "string | table",
      description:
        "플러그인의 stdio MCP 서버를 정확히 일치하는 명령어 문자열로 허용하거나, 매처 테이블을 사용해 실행 파일이 정확히 일치하고 인수가 순서대로 지정된 매처와 일치하도록 요구합니다.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.executable",
      type: "string",
      description:
        "플러그인에 포함된 stdio 서버의 명령어 설정이 정확히 일치해야 하는 실행 파일입니다.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args",
      type: "array<table>",
      description:
        "플러그인에 포함된 stdio 서버의 인수 매처를 순서대로 나열한 목록입니다. 설정된 인수 목록은 길이가 같아야 하며, 각 위치의 인수가 해당 매처와 일치해야 합니다.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].match",
      type: "exact | prefix | regex",
      description: "이 인수 위치에 적용할 매칭 연산입니다.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].value",
      type: "string",
      description: "`exact` 또는 `prefix` 인수 매처가 사용하는 값입니다.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].expression",
      type: "string",
      description:
        "`regex` 인수 매처가 사용하는 정규식입니다. 이 정규식은 인수 값 전체와 일치해야 합니다.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url",
      type: "string | table",
      description:
        "플러그인의 스트리밍 가능한 HTTP MCP 서버를 정확히 일치하는 URL 문자열로 허용하거나, `exact`, `prefix` 또는 `regex` 값 매처 테이블을 사용합니다.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.match",
      type: "exact | prefix | regex",
      description: "플러그인에 포함된 MCP 서버 URL에 적용할 매칭 연산입니다.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.value",
      type: "string",
      description: "`exact` 또는 `prefix` URL 매처가 사용하는 값입니다.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.expression",
      type: "string",
      description:
        "`regex` URL 매처가 사용하는 정규식입니다. 이 정규식은 URL 값 전체와 일치해야 합니다.",
    },
    {
      key: "marketplaces",
      type: "table",
      description:
        "플러그인 마켓플레이스 소스에 대한 관리자 요구사항입니다. `restrict_to_allowed_sources`가 `true`일 때 규칙이 적용됩니다.",
    },
    {
      key: "marketplaces.restrict_to_allowed_sources",
      type: "boolean",
      description:
        "`true`이면 마켓플레이스 추가, 플러그인 설치, 설정된 Git 마켓플레이스 새로 고침 작업에서 사용자가 설정한 마켓플레이스 소스가 `allowed_sources`와 일치해야 합니다. Codex가 관리하는 OpenAI 마켓플레이스는 예약된 소스와 이름이 일치하면 계속 허용됩니다. 이미 설정된 사용자 마켓플레이스를 런타임에 필터링하지는 않습니다.",
    },
    {
      key: "marketplaces.allowed_sources",
      type: "table",
      description:
        "관리자가 지정한 규칙 이름을 키로 사용하는 허용된 마켓플레이스 소스입니다. 서로 다른 이름의 규칙은 요구사항 레이어 간에 누적되며, 같은 이름 아래의 필드에는 일반적인 레이어 우선순위가 적용됩니다.",
    },
    {
      key: "marketplaces.allowed_sources.<name>",
      type: "table",
      description:
        "허용된 소스 하나에 대한 규칙입니다. 요구사항을 병합한 후의 최종 `source` 값에 따라 Codex가 해석할 동일 수준의 필드가 결정됩니다.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.source",
      type: "git | host_pattern | local",
      description:
        "마켓플레이스 소스 매처 유형입니다. 단일 레포지토리에는 `git`, 정규식과 일치하는 Git 호스트에는 `host_pattern`, 단일 디렉터리에는 `local`을 사용하세요.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.url",
      type: "string",
      description:
        "`source = \"git\"`일 때 필요한 Git 레포지토리 URL입니다. Codex는 설정된 URL과 허용된 URL을 정규화한 후 레포지토리가 정확히 일치하는지 확인합니다.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.ref",
      type: "string",
      description:
        "`git` 규칙에 선택적으로 지정하는 정확한 Git ref입니다. 생략하면 일치하는 레포지토리의 모든 ref가 허용됩니다.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.host_pattern",
      type: "string",
      description:
        "`source = \"host_pattern\"`일 때 필요한 정규식입니다. Codex는 HTTPS, SSH 또는 SCP 형식의 Git 소스에서 추출한 소문자 호스트 이름을 이 정규식과 비교합니다. 호스트 이름 전체가 일치하도록 하려면 `^`와 `$`를 사용하세요.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.path",
      type: "string (absolute path)",
      description:
        "`source = \"local\"`일 때 필요한 로컬 마켓플레이스 디렉터리입니다. Codex에는 절대 경로를 지정해야 하며, 경로는 정규화 후 비교됩니다.",
    },
    {
      key: "apps",
      type: "table",
      description:
        "앱 식별자를 키로 사용하는 관리형 앱 요구사항입니다. 요구사항으로 앱을 비활성화하거나 개별 도구의 승인 동작을 제한할 수 있습니다.",
    },
    {
      key: "apps.<id>.enabled",
      type: "boolean",
      description:
        "앱을 비활성화하려면 `false`로 설정하세요. 여러 요구사항 소스를 병합해도 앱 비활성화 요구사항의 제한은 유지됩니다.",
    },
    {
      key: "apps.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description: "앱 도구 하나에 대한 관리형 승인 모드를 설정합니다.",
    },
    {
      key: "rules",
      type: "table",
      description:
        "관리자가 강제 적용하는 명령어 규칙으로, `.rules` 파일과 병합됩니다. 요구사항 규칙은 반드시 제한을 가하는 규칙이어야 합니다.",
    },
    {
      key: "rules.prefix_rules",
      type: "array<table>",
      description:
        "강제 적용되는 접두사 규칙 목록입니다. 각 규칙에는 `pattern`과 `decision`이 포함되어야 합니다.",
    },
    {
      key: "rules.prefix_rules[].pattern",
      type: "array<table>",
      description:
        "패턴 토큰으로 표현한 명령어 접두사입니다. 각 토큰에는 `token` 또는 `any_of` 중 하나를 설정합니다.",
    },
    {
      key: "rules.prefix_rules[].pattern[].token",
      type: "string",
      description: "이 위치에 사용할 단일 리터럴 토큰입니다.",
    },
    {
      key: "rules.prefix_rules[].pattern[].any_of",
      type: "array<string>",
      description: "이 위치에서 대안으로 허용되는 토큰 목록입니다.",
    },
    {
      key: "rules.prefix_rules[].decision",
      type: "prompt | forbidden",
      description:
        "필수 항목입니다. 요구사항 규칙은 승인 요청이나 금지만 할 수 있으며, 허용은 할 수 없습니다.",
    },
    {
      key: "rules.prefix_rules[].justification",
      type: "string",
      description:
        "승인 요청이나 거부 메시지에 표시할 근거 설명입니다. 선택 사항이며, 지정할 경우 비어 있으면 안 됩니다.",
    },
  ]}
  client:load
/>

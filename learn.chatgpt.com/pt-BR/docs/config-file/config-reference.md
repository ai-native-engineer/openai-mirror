<!-- source: https://learn.chatgpt.com/pt-BR/docs/config-file/config-reference -->

Use esta página como uma referência pesquisável para os arquivos de configuração do Codex. Para orientações conceituais e exemplos, comece por [Configuração básica](/pt-BR/codex/config-file/config-basic) e [Configuração avançada](/pt-BR/codex/config-file/config-advanced).

## `config.toml`

A configuração no nível do usuário fica em `~/.codex/config.toml`. Você também pode adicionar substituições específicas do projeto em arquivos `.codex/config.toml`. O Codex carrega arquivos de configuração específicos do projeto somente quando você confia no projeto.

A configuração no escopo do projeto não pode substituir chaves locais da máquina relacionadas a provedor, autenticação,
metadados controlados pelo host para solicitações de aplicativos, notificações, seleção do perfil de configuração
ou roteamento de telemetria. O Codex ignora `openai_base_url`,
`chatgpt_base_url`, `apps_mcp_product_sku`, `model_provider`,
`model_providers`, `notify`, `profile`, `profiles`,
`experimental_realtime_ws_base_url` e `otel` quando aparecem em um
arquivo `.codex/config.toml` local do projeto; coloque as chaves de provedor, notificação e telemetria
na configuração no nível do usuário. Os [arquivos de perfil](/pt-BR/codex/config-file/config-advanced#profiles) de configuração ficam no mesmo diretório de
`config.toml`, com o nome `$CODEX_HOME/profile-name.config.toml`; selecione um com
`--profile profile-name`.

Para as chaves de sandbox e aprovação (`approval_policy`, `sandbox_mode` e `sandbox_workspace_write.*`), consulte também [Sandbox e aprovações](/pt-BR/codex/agent-approvals-security#sandbox-and-approvals), [Caminhos protegidos em raízes graváveis](/pt-BR/codex/agent-approvals-security#protected-paths-in-writable-roots) e [Acesso à rede](/pt-BR/codex/agent-approvals-security#network-access). Para perfis de permissão em versão beta, consulte [Permissões](/pt-BR/codex/permissions).

<ConfigTable
  options={[
    {
      key: "model",
      type: "string",
      description: "Modelo a ser usado (por exemplo, `gpt-5.5`).",
    },
    {
      key: "review_model",
      type: "string",
      description:
        "Substituição opcional do modelo usado por `/review` (o padrão é o modelo da sessão atual).",
    },
    {
      key: "model_provider",
      type: "string",
      description: "ID do provedor em `model_providers` (padrão: `openai`).",
    },
    {
      key: "openai_base_url",
      type: "string",
      description:
        "Substituição da URL base do provedor de modelos integrado `openai`.",
    },
    {
      key: "model_context_window",
      type: "number",
      description: "Tokens da janela de contexto disponíveis para o modelo ativo.",
    },
    {
      key: "model_auto_compact_token_limit",
      type: "number",
      description:
        "Limite de tokens que aciona a compactação automática do histórico (quando não definido, usa os padrões do modelo).",
    },
    {
      key: "model_auto_compact_token_limit_scope",
      type: "total | body_after_prefix",
      description:
        "Controla se o limite de compactação automática contabiliza todo o contexto ativo (`total`, o padrão) ou apenas o crescimento após o prefixo preservado da janela de compactação (`body_after_prefix`).",
    },
    {
      key: "model_catalog_json",
      type: "string (path)",
      description:
        "Caminho opcional para um catálogo de modelos em JSON carregado na inicialização. O arquivo de perfil selecionado, `$CODEX_HOME/profile-name.config.toml`, pode substituir esse valor para o respectivo perfil.",
    },
    {
      key: "oss_provider",
      type: "lmstudio | ollama",
      description:
        "Provedor local padrão usado na execução com `--oss` (se não definido, o padrão é solicitar a escolha do provedor).",
    },
    {
      key: "approval_policy",
      type: "untrusted | on-request | never | { granular = { sandbox_approval = bool, rules = bool, mcp_elicitations = bool, request_permissions = bool, skill_approval = bool } }",
      description:
        "Controla quando o Codex pausa para solicitar aprovação antes de executar comandos. Você também pode usar `approval_policy = { granular = { ... } }` para permitir ou rejeitar automaticamente categorias específicas de solicitações, mantendo as demais interativas. `on-failure` foi descontinuado; use `on-request` para execuções interativas ou `never` para execuções não interativas.",
    },
    {
      key: "approval_policy.granular.sandbox_approval",
      type: "boolean",
      description:
        "Quando definido como `true`, as solicitações de aprovação para elevação de permissões do sandbox podem ser exibidas.",
    },
    {
      key: "approval_policy.granular.rules",
      type: "boolean",
      description:
        "Quando definido como `true`, as solicitações de aprovação acionadas pelas regras `prompt` do execpolicy podem ser exibidas.",
    },
    {
      key: "approval_policy.granular.mcp_elicitations",
      type: "boolean",
      description:
        "Quando definido como `true`, os prompts de elicitação do MCP podem ser exibidos em vez de serem rejeitados automaticamente.",
    },
    {
      key: "approval_policy.granular.request_permissions",
      type: "boolean",
      description:
        "Quando definido como `true`, as solicitações da ferramenta `request_permissions` podem ser exibidas.",
    },
    {
      key: "approval_policy.granular.skill_approval",
      type: "boolean",
      description:
        "Quando definido como `true`, as solicitações de aprovação de scripts de habilidades podem ser exibidas.",
    },
    {
      key: "approvals_reviewer",
      type: "user | auto_review",
      description:
        "Define quem revisa as solicitações de aprovação elegíveis em políticas de aprovação `on-request` ou granulares. O padrão é `user`; `auto_review` usa o subagente revisor. Essa configuração não altera o ambiente isolado nem submete à revisão ações já permitidas dentro do sandbox.",
    },
    {
      key: "auto_review.policy",
      type: "string",
      description:
        "Instruções locais de política em Markdown para revisão automática. A configuração gerenciada `guardian_policy_config` tem precedência. Valores em branco são ignorados.",
    },
    {
      key: "allow_login_shell",
      type: "boolean",
      description:
        "Permite que ferramentas baseadas em shell usem a semântica de shell de login. O padrão é `true`; quando definido como `false`, solicitações `login = true` são rejeitadas e, quando `login` é omitido, o padrão é usar shells sem login.",
    },
    {
      key: "sandbox_mode",
      type: "read-only | workspace-write | danger-full-access",
      description:
        "Política de sandbox para acesso ao sistema de arquivos e à rede durante a execução de comandos.",
    },
    {
      key: "sandbox_workspace_write.writable_roots",
      type: "array<string>",
      description:
        "Raízes graváveis adicionais quando `sandbox_mode = \"workspace-write\"`.",
    },
    {
      key: "sandbox_workspace_write.network_access",
      type: "boolean",
      description:
        "Permite acesso de saída à rede dentro do sandbox workspace-write.",
    },
    {
      key: "sandbox_workspace_write.exclude_tmpdir_env_var",
      type: "boolean",
      description:
        "Exclui `$TMPDIR` das raízes graváveis no modo workspace-write.",
    },
    {
      key: "sandbox_workspace_write.exclude_slash_tmp",
      type: "boolean",
      description:
        "Exclui `/tmp` das raízes graváveis no modo workspace-write.",
    },
    {
      key: "windows.sandbox",
      type: "unelevated | elevated",
      description:
        "Modo de sandbox nativo exclusivo do Windows ao executar o Codex nativamente no Windows.",
    },
    {
      key: "windows.sandbox_private_desktop",
      type: "boolean",
      description:
        "Por padrão, executa o processo filho final em sandbox em uma área de trabalho privada ao usar o Codex nativamente no Windows. Defina como `false` somente para manter a compatibilidade com o comportamento anterior de `Winsta0\\\\Default`.",
    },
    {
      key: "browser_use.allow_history_access",
      type: "boolean",
      description:
        "Defina como `false` para restringir o acesso ao histórico do navegador. Requisitos gerenciados podem impor essa restrição.",
    },
    {
      key: "browser_use.default_origin_policy",
      type: "table",
      description:
        "Restrições por origem aplicadas por padrão no navegador. Oferece suporte a `access`, `uploads`, `downloads` e `full_cdp_access`, cada um definido como `allow` ou `deny`.",
    },
    {
      key: "browser_use.origins.<origin>",
      type: "table",
      description:
        "Restrições do navegador por origem, com os mesmos campos de `browser_use.default_origin_policy`. Inclua um esquema HTTP ou HTTPS e, opcionalmente, uma porta; omita caminhos, parâmetros de consulta e fragmentos. Valores locais não podem flexibilizar bloqueios gerenciados.",
    },
    {
      key: "computer_use.default_app_access",
      type: "allow | deny",
      description:
        "Política de acesso a aplicativos nativos aplicada por padrão no Uso do computador. Entradas específicas por aplicativo podem definir uma política; a configuração local não pode flexibilizar restrições gerenciadas.",
    },
    {
      key: "computer_use.macos.bundle_ids",
      type: "map<string, allow | deny>",
      description: "Acesso a aplicativos nativos do macOS, usando o identificador de bundle como chave.",
    },
    {
      key: "computer_use.windows.aumids",
      type: "map<string, allow | deny>",
      description:
        "Acesso a aplicativos empacotados do Windows, usando o Application User Model ID (AUMID) como chave.",
    },
    {
      key: "computer_use.windows.exes",
      type: "array<table>",
      description:
        "Regras de acesso a executáveis do Windows. Cada regra exige `publisher_name`, `product_name` e `access` (`allow` ou `deny`); `binary_name` é opcional.",
    },
    {
      key: "computer_use.windows.always_allowed_app_ids",
      type: "array<string>",
      description:
        "Identificadores de aplicativos do Windows que o Uso do computador pode abrir sem solicitar aprovação. Aplicativos fora da lista exigem aprovação; remova as entradas salvas nas configurações de Uso do computador do aplicativo do ChatGPT para desktop.",
    },
    {
      key: "notify",
      type: "array<string>",
      description:
        "Comando executado para notificações; recebe uma carga útil JSON do Codex.",
    },
    {
      key: "check_for_update_on_startup",
      type: "boolean",
      description:
        "Verifica se há atualizações do Codex na inicialização (defina como false somente quando as atualizações forem gerenciadas de forma centralizada).",
    },
    {
      key: "feedback.enabled",
      type: "boolean",
      description:
        "Ativa o envio de feedback por meio de `/feedback` em todos os clientes locais (padrão: true).",
    },
    {
      key: "analytics.enabled",
      type: "boolean",
      description:
        "Ativa ou desativa a coleta de dados analíticos para esta máquina/perfil. Quando não definido, aplica-se o padrão do cliente.",
    },
    {
      key: "instructions",
      type: "string",
      description:
        "Reservado para uso futuro; prefira `model_instructions_file` ou `AGENTS.md`.",
    },
    {
      key: "developer_instructions",
      type: "string",
      description:
        "Instruções adicionais do desenvolvedor inseridas na sessão (opcionais).",
    },
    {
      key: "log_dir",
      type: "string (path)",
      description:
        "Diretório em que o Codex grava arquivos de log; o padrão é `$CODEX_HOME/log`. Definir explicitamente esse diretório também ativa nele o log opcional da TUI em texto simples, `codex-tui.log`.",
    },
    {
      key: "sqlite_home",
      type: "string (path)",
      description:
        "Diretório em que o Codex armazena o banco de dados de estado baseado em SQLite, usado por tarefas de agentes e para outros estados de execução que podem ser retomados.",
    },
    {
      key: "compact_prompt",
      type: "string",
      description: "Substituição do prompt de compactação do histórico definida diretamente na configuração.",
    },
    {
      key: "model_instructions_file",
      type: "string (path)",
      description:
        "Substituição das instruções integradas usada no lugar de `AGENTS.md`.",
    },
    {
      key: "personality",
      type: "none | friendly | pragmatic",
      description:
        "Estilo de comunicação padrão para modelos que declaram `supportsPersonality`; pode ser substituído em cada conversa ou turno ou por meio de `/personality`.",
    },
    {
      key: "service_tier",
      type: "string",
      description:
        "Nível de serviço preferencial para novos turnos. Use `fast` ou outro nível indicado pelo modelo ativo; `fast` corresponde ao valor `priority` na solicitação.",
    },
    {
      key: "experimental_compact_prompt_file",
      type: "string (path)",
      description:
        "Carrega de um arquivo a substituição do prompt de compactação (experimental).",
    },
    {
      key: "skills.max_context_tokens",
      type: "integer (positive)",
      description:
        "Limite de tokens para o catálogo de habilidades disponíveis. O padrão é 2% da janela de contexto do modelo. Valores definidos explicitamente são limitados a `10000` tokens.",
    },
    {
      key: "skills.config",
      type: "array<object>",
      description: "Substituições do estado de ativação por habilidade, armazenadas em config.toml.",
    },
    {
      key: "skills.config.<index>.path",
      type: "string (path)",
      description: "Caminho para uma pasta de habilidade que contém `SKILL.md`.",
    },
    {
      key: "skills.config.<index>.enabled",
      type: "boolean",
      description: "Ativa ou desativa a habilidade referenciada.",
    },
    {
      key: "apps.<id>.enabled",
      type: "boolean",
      description:
        "Ativa ou desativa um aplicativo/conector específico pelo ID (padrão: true).",
    },
    {
      key: "apps._default.enabled",
      type: "boolean",
      description:
        "Estado padrão de ativação de todos os aplicativos, a menos que seja substituído para um aplicativo específico.",
    },
    {
      key: "apps._default.destructive_enabled",
      type: "boolean",
      description:
        "Decisão padrão de permitir ou negar ferramentas de aplicativos com `destructive_hint = true`.",
    },
    {
      key: "apps._default.open_world_enabled",
      type: "boolean",
      description:
        "Decisão padrão de permitir ou negar ferramentas de aplicativos com `open_world_hint = true`.",
    },
    {
      key: "apps._default.approvals_reviewer",
      type: "user | auto_review",
      description:
        "Revisor padrão das solicitações de aprovação de ferramentas de aplicativos, a menos que outro seja definido para um aplicativo específico. Quando omitido, os aplicativos herdam o valor de `approvals_reviewer` no nível superior.",
    },
    {
      key: "apps._default.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Comportamento padrão de aprovação para ferramentas de aplicativos sem substituições específicas por aplicativo ou ferramenta.",
    },
    {
      key: "apps.<id>.destructive_enabled",
      type: "boolean",
      description:
        "Permite ou bloqueia ferramentas deste aplicativo que indicam `destructive_hint = true`.",
    },
    {
      key: "apps.<id>.open_world_enabled",
      type: "boolean",
      description:
        "Permite ou bloqueia ferramentas deste aplicativo que indicam `open_world_hint = true`.",
    },
    {
      key: "apps.<id>.default_tools_enabled",
      type: "boolean",
      description:
        "Estado padrão de ativação das ferramentas deste aplicativo, a menos que exista uma configuração específica por ferramenta.",
    },
    {
      key: "apps.<id>.approvals_reviewer",
      type: "user | auto_review",
      description:
        "Revisor das solicitações de aprovação de ferramentas deste aplicativo. Substitui `apps._default.approvals_reviewer`.",
    },
    {
      key: "apps.<id>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Comportamento padrão de aprovação das ferramentas deste aplicativo, a menos que exista uma configuração específica por ferramenta.",
    },
    {
      key: "apps.<id>.tools.<tool>.enabled",
      type: "boolean",
      description:
        "Configuração de ativação específica para uma ferramenta do aplicativo (por exemplo, `repos/list`).",
    },
    {
      key: "apps.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description: "Configuração do comportamento de aprovação de uma ferramenta específica do aplicativo.",
    },
    {
      key: "tool_suggest.discoverables",
      type: "array<table>",
      description:
        "Permita sugestões de ferramentas de outros conectores ou plug-ins que podem ser descobertos. Cada entrada usa `type = \"connector\"` ou `\"plugin\"` e um `id`.",
    },
    {
      key: "tool_suggest.disabled_tools",
      type: "array<table>",
      description:
        "Desative sugestões de conectores ou plug-ins específicos que podem ser descobertos. Cada entrada usa `type = \"connector\"` ou `\"plugin\"` e um `id`.",
    },
    {
      key: "features.apps",
      type: "boolean",
      description:
        "Ative as integrações de aplicativos (conectores) (estáveis; ativadas por padrão). O tráfego de aplicativos e conectores não é controlado pelo proxy de rede dos comandos executados no sandbox nem por sua lista de domínios permitidos.",
    },
    {
      key: "features.hooks",
      type: "boolean",
      description:
        "Ative os ganchos de ciclo de vida carregados de `hooks.json` ou definidos diretamente na configuração `[hooks]`. `features.codex_hooks` é um nome alternativo obsoleto.",
    },
    {
      key: "features.code_mode.enabled",
      type: "boolean",
      description:
        "Ative a configuração do recurso de modo de código. Esse recurso está em desenvolvimento e fica desativado por padrão.",
    },
    {
      key: "features.code_mode.excluded_tool_namespaces",
      type: "array<string>",
      description:
        "Espaços de nomes de ferramentas que o modo de código exclui das orientações sobre ferramentas aninhadas nesse modo e não disponibiliza ao executor.",
    },
    {
      key: "features.code_mode.direct_only_tool_namespaces",
      type: "array<string>",
      description:
        "Espaços de nomes de ferramentas que o modo de código pode usar somente por meio de chamadas diretas de ferramentas.",
    },
    {
      key: "features.context_management.experimental_mode",
      type: "boolean",
      description:
        "Ative o gerenciamento experimental de contexto (desativado por padrão). Em vez de comprimir repetidamente o contexto em um único resumo, ele usa notas e um histórico pesquisável para preservar os detalhes acumulados. Exige login no ChatGPT com um plano Plus, Pro ou Pro Lite.",
    },
    {
      key: "features.rollout_budget.enabled",
      type: "boolean",
      description:
        "Ative o acompanhamento do orçamento de execução. Esse recurso está em desenvolvimento e fica desativado por padrão. Quando ativado, é obrigatório definir `features.rollout_budget.limit_tokens`.",
    },
    {
      key: "features.rollout_budget.limit_tokens",
      type: "integer",
      description:
        "Limite positivo de tokens para acompanhar o orçamento de execução. Obrigatório quando o orçamento de execução está ativado.",
    },
    {
      key: "features.rollout_budget.reminder_interval_tokens",
      type: "integer",
      description:
        "Intervalo positivo, em tokens, entre os lembretes do orçamento de execução. O padrão é 10% de `limit_tokens`, com um mínimo de 1 token.",
    },
    {
      key: "features.rollout_budget.sampling_token_weight",
      type: "number",
      description:
        "Multiplicador finito e não negativo para tokens amostrados na contabilização do orçamento de execução. O padrão é `1.0`.",
    },
    {
      key: "features.rollout_budget.prefill_token_weight",
      type: "number",
      description:
        "Multiplicador finito e não negativo para tokens de pré-preenchimento na contabilização do orçamento de execução. O padrão é `1.0`.",
    },
    {
      key: "hooks",
      type: "table",
      description:
        "Ganchos de ciclo de vida configurados diretamente em `config.toml`. A configuração usa o mesmo esquema de eventos de `hooks.json`; consulte o guia de Ganchos para ver exemplos e eventos compatíveis.",
    },
    {
      key: "hooks.",
      type: "array<table>",
      description:
        "Grupos de correspondência para eventos de ganchos, como `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `SessionStart`, `SessionEnd`, `SubagentStart`, `SubagentStop`, `UserPromptSubmit`, `Stop` ou `Interrupt`.",
    },
    {
      key: "hooks.[].hooks",
      type: "array<table>",
      description:
        "Manipuladores de ganchos para um grupo de correspondência. Há suporte para ganchos de comando e de ferramentas MCP; os manipuladores de ganchos de prompt e de agente passam pela análise sintática, mas não são executados.",
    },
    {
      key: "hooks.[].hooks[].async",
      type: "boolean",
      description:
        "Execute um gancho de comando em segundo plano sem atrasar a operação que o acionou. O padrão é `false`; `SessionEnd` sempre é executado de forma síncrona. Consulte [Executar ganchos em segundo plano](/codex/hooks#run-hooks-in-the-background).",
    },
    {
      key: "hooks.[].hooks[].additionalContextLimit",
      type: "integer",
      description:
        "Limite aproximado de tokens por manipulador para salvar em disco valores muito grandes de `additionalContext` e mostrar ao modelo uma prévia mais curta. O padrão é `2500`; `0` envia todo o contexto diretamente ao modelo. Consulte [Saída extensa de ganchos](/codex/hooks#large-hook-output).",
    },
    {
      key: "hooks.[].hooks[].commandWindows",
      type: "string",
      description:
        "Comando alternativo para ganchos de comando, exclusivo do Windows. O nome alternativo TOML `command_windows` também é aceito.",
    },
    {
      key: "features.memories",
      type: "boolean",
      description:
        "Ative [Memórias](/codex/customization/memories) (desativadas por padrão).",
    },
    {
      key: "mcp_optional_startup_grace_ms",
      type: "integer (milliseconds)",
      description:
        "Tempo de espera compartilhado entre os servidores MCP opcionais ao montar o catálogo inicial de ferramentas. O padrão é `1000`. Defina como `0` para usar o tempo limite `startup_timeout_sec` de cada servidor.",
    },
    {
      key: "mcp_servers.<id>.command",
      type: "string",
      description: "Comando para iniciar um servidor MCP stdio.",
    },
    {
      key: "mcp_servers.<id>.args",
      type: "array<string>",
      description: "Argumentos passados ao comando do servidor MCP stdio.",
    },
    {
      key: "mcp_servers.<id>.env",
      type: "map<string,string>",
      description: "Variáveis do ambiente encaminhadas ao servidor MCP stdio.",
    },
    {
      key: "mcp_servers.<id>.env_vars",
      type: 'array<string | { name = string, source = "local" | "remote" }>',
      description:
        "Variáveis do ambiente adicionais a incluir na lista de permissões de um servidor MCP stdio. As entradas de texto usam `source = \"local\"` por padrão; use `source = \"remote\"` somente com stdio remoto fornecido por um executor.",
    },
    {
      key: "mcp_servers.<id>.cwd",
      type: "string",
      description: "Diretório de trabalho do processo do servidor MCP stdio.",
    },
    {
      key: "mcp_servers.<id>.url",
      type: "string",
      description: "Endpoint de um servidor MCP HTTP com streaming.",
    },
    {
      key: "mcp_servers.<id>.auth",
      type: "oauth | chatgpt",
      description:
        "Método alternativo de autenticação para um servidor MCP HTTP, usado após os tokens bearer e os cabeçalhos de autorização configurados. `oauth` (padrão) usa credenciais OAuth do MCP armazenadas, quando disponíveis. `chatgpt` usa a sessão atual do ChatGPT para a origem confiável do próprio ChatGPT e, se necessário, recorre às credenciais OAuth armazenadas. Ambos os modos podem se conectar sem autenticação se nenhuma fonte fornecer credenciais.",
    },
    {
      key: "mcp_servers.<id>.oauth.client_id",
      type: "string",
      description:
        "ID de cliente OAuth pré-registrado usado para autorização e troca de tokens com este servidor MCP.",
    },
    {
      key: "mcp_servers.<id>.oauth.callback_url",
      type: "string",
      description:
        "URL de retorno OAuth específica do servidor. Clientes pré-registrados a reutilizam quando há suporte à identificação do emissor ou quando a URL já termina com o ID de retorno específico do servidor. Caso contrário, o Codex usa a URL de retorno global ou padrão com esse ID acrescentado ao final. Clientes sem um ID pré-registrado usam essa URL de retorno durante o registro do cliente.",
    },
    {
      key: "mcp_servers.<id>.oauth.callback_port",
      type: "integer",
      description:
        "Porta fixa de escuta para o retorno OAuth deste servidor MCP. Substitui `mcp_oauth_callback_port`. Para um retorno direto via loopback com uma porta explícita na URL, configure a mesma porta de escuta.",
    },
    {
      key: "mcp_servers.<id>.bearer_token_env_var",
      type: "string",
      description:
        "Variável do ambiente que fornece o token bearer de um servidor MCP HTTP.",
    },
    {
      key: "mcp_servers.<id>.http_headers",
      type: "map<string,string>",
      description: "Cabeçalhos HTTP estáticos incluídos em cada solicitação HTTP do MCP.",
    },
    {
      key: "mcp_servers.<id>.http_headers_helper",
      type: "string (command)",
      description:
        "Comando local que imprime um objeto JSON com nomes e valores de cabeçalhos HTTP. Compatível apenas com servidores MCP HTTP conectados localmente. Tokens bearer explícitos e credenciais OAuth têm precedência sobre cabeçalhos Authorization fornecidos pelo comando auxiliar.",
    },
    {
      key: "mcp_servers.<id>.env_http_headers",
      type: "map<string,string>",
      description:
        "Cabeçalhos HTTP de um servidor MCP HTTP preenchidos a partir de variáveis do ambiente.",
    },
    {
      key: "mcp_servers.<id>.enabled",
      type: "boolean",
      description: "Desative um servidor MCP sem remover sua configuração.",
    },
    {
      key: "mcp_servers.<id>.required",
      type: "boolean",
      description:
        "Quando definido como true, faz a inicialização ou a retomada falhar se este servidor MCP estiver ativado e não puder ser inicializado.",
    },
    {
      key: "mcp_servers.<id>.startup_timeout_sec",
      type: "number",
      description:
        "Substitua o tempo limite padrão de 10 segundos para a inicialização de um servidor MCP.",
    },
    {
      key: "mcp_servers.<id>.startup_timeout_ms",
      type: "number",
      description: "Nome alternativo de `startup_timeout_sec`, em milissegundos.",
    },
    {
      key: "mcp_servers.<id>.tool_timeout_sec",
      type: "number",
      description:
        "Substitua o tempo limite padrão de 60 segundos por ferramenta de um servidor MCP.",
    },
    {
      key: "mcp_servers.<id>.enabled_tools",
      type: "array<string>",
      description: "Lista de nomes de ferramentas que o servidor MCP tem permissão para expor.",
    },
    {
      key: "mcp_servers.<id>.disabled_tools",
      type: "array<string>",
      description:
        "Lista de bloqueio aplicada após `enabled_tools` para o servidor MCP.",
    },
    {
      key: "mcp_servers.<id>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Comportamento padrão de aprovação das ferramentas MCP neste servidor, a menos que exista uma configuração específica por ferramenta.",
    },
    {
      key: "mcp_servers.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Configuração do comportamento de aprovação de uma ferramenta MCP específica neste servidor.",
    },
    {
      key: "mcp_servers.<id>.tools.<tool>.output_token_limit",
      type: "integer (positive)",
      description:
        "Orçamento de tokens para a saída de uma ferramenta MCP, antes da margem padrão de 20% para serialização. Substitui o orçamento padrão de truncamento de saída do modelo para essa ferramenta.",
    },
    {
      key: "mcp_servers.<id>.scopes",
      type: "array<string>",
      description:
        "Escopos OAuth a solicitar durante a autenticação nesse servidor MCP.",
    },
    {
      key: "mcp_servers.<id>.oauth_resource",
      type: "string",
      description:
        "Parâmetro opcional de recurso OAuth, conforme a RFC 8707, a incluir durante o login no MCP.",
    },
    {
      key: "mcp_servers.<id>.experimental_environment",
      type: "local | remote",
      description:
        "Local de execução experimental para um servidor MCP. `remote` inicia servidores stdio por meio de um ambiente com executor remoto; a execução remota de servidores HTTP com streaming não está implementada.",
    },
    {
      key: "agents",
      type: "table",
      description:
        "Configurações para vários agentes e declarações de funções personalizadas. Os nomes de configurações escalares são reservados e não podem ser usados como nomes de funções personalizadas.",
    },
    {
      key: "agents.enabled",
      type: "boolean",
      description: "Ative ou desative as ferramentas para vários agentes (padrão: true).",
    },
    {
      key: "agents.max_concurrent_threads_per_session",
      type: "number",
      description:
        "Número máximo de conversas de agentes criados que podem ficar abertas simultaneamente, sem contar a conversa principal. Quando nenhum valor é definido, o Codex escolhe o padrão.",
    },
    {
      key: "agents.max_threads",
      type: "number",
      description:
        "Nome alternativo legado de `agents.max_concurrent_threads_per_session`.",
    },
    {
      key: "agents.default_subagent_model",
      type: "string",
      description:
        "Modelo padrão para agentes criados. Um modelo especificado explicitamente na criação do agente tem precedência.",
    },
    {
      key: "agents.default_subagent_reasoning_effort",
      type: "string",
      description:
        "Esforço de raciocínio padrão para agentes criados. Um esforço especificado explicitamente na criação do agente tem precedência.",
    },
    {
      key: "agents.interrupt_message",
      type: "boolean",
      description:
        "Registre uma mensagem visível para o modelo quando o turno de um agente for interrompido (padrão: true).",
    },
    {
      key: "agents.<name>.description",
      type: "string",
      description:
        "Orientações sobre a função fornecidas ao Codex ao escolher e criar esse tipo de agente.",
    },
    {
      key: "agents.<name>.config_file",
      type: "string (path)",
      description:
        "Caminho para uma camada de configuração TOML dessa função; caminhos relativos são resolvidos a partir do arquivo de configuração que declara a função.",
    },
    {
      key: "memories.generate_memories",
      type: "boolean",
      description:
        "Quando `false`, as conversas recém-criadas não são armazenadas como entradas para a geração de memórias. O padrão é `true`.",
    },
    {
      key: "memories.use_memories",
      type: "boolean",
      description:
        "Quando `false`, o Codex deixa de inserir memórias existentes em sessões futuras. O padrão é `true`.",
    },
    {
      key: "memories.disable_on_external_context",
      type: "boolean",
      description:
        "Quando definido como `true`, as conversas que usam contexto externo, como chamadas de ferramentas MCP, pesquisa na Web ou pesquisa de ferramentas, são excluídas da geração de memórias. O padrão é `false`. Alias legado: `memories.no_memories_if_mcp_or_web_search`.",
    },
    {
      key: "memories.max_raw_memories_for_consolidation",
      type: "number",
      description:
        "Número máximo de memórias brutas recentes mantidas para consolidação global. O padrão é `256`, com limite máximo de `4096`.",
    },
    {
      key: "memories.max_unused_days",
      type: "number",
      description:
        "Número máximo de dias desde o último uso de uma memória antes que ela deixe de ser elegível para consolidação. O padrão é `30`, limitado ao intervalo de `0` a `365`.",
    },
    {
      key: "memories.max_rollout_age_days",
      type: "number",
      description:
        "Idade máxima das conversas consideradas para geração de memórias. O padrão é `30`, limitado ao intervalo de `0` a `90`.",
    },
    {
      key: "memories.max_rollouts_per_startup",
      type: "number",
      description:
        "Número máximo de registros de execução candidatos processados por rodada de inicialização. O padrão é `16`, com limite máximo de `128`.",
    },
    {
      key: "memories.min_rollout_idle_hours",
      type: "number",
      description:
        "Tempo mínimo de inatividade antes que uma conversa seja considerada para geração de memórias. O padrão é `6`, limitado ao intervalo de `1` a `48`.",
    },
    {
      key: "memories.min_rate_limit_remaining_percent",
      type: "number",
      description:
        "Percentual mínimo restante exigido nas janelas de limite de taxa do Codex antes de iniciar a geração de memórias. O padrão é `25`, limitado ao intervalo de `0` a `100`.",
    },
    {
      key: "memories.extract_model",
      type: "string",
      description: "Substituição opcional do modelo para a extração de memórias de cada conversa.",
    },
    {
      key: "memories.consolidation_model",
      type: "string",
      description: "Substituição opcional do modelo para a consolidação global de memórias.",
    },
    {
      key: "features.unified_exec",
      type: "boolean",
      description:
        "Use a ferramenta exec unificada baseada em PTY (estável; ativada por padrão, exceto no Windows).",
    },
    {
      key: "features.shell_snapshot",
      type: "boolean",
      description:
        "Capture o estado do ambiente do shell para agilizar a execução repetida de comandos (estável; ativado por padrão).",
    },
    {
      key: "features.multi_agent",
      type: "boolean",
      description:
        "Ative as ferramentas de colaboração entre agentes (`spawn_agent`, `send_input`, `resume_agent`, `wait_agent` e `close_agent`) (estável; ativado por padrão).",
    },
    {
      key: "features.goals",
      type: "boolean",
      description:
        "Ative metas persistentes e a continuação automática (estável; ativado por padrão).",
    },
    {
      key: "features.remote_plugin",
      type: "boolean",
      description: "Ative o catálogo remoto de plug-ins (estável; ativado por padrão).",
    },
    {
      key: "features.personality",
      type: "boolean",
      description:
        "Ative os controles de seleção de personalidade (estável; ativado por padrão).",
    },
    {
      key: "features.network_proxy",
      type: "boolean | table",
      description:
        "Inicie o proxy de rede para comandos executados em ambiente isolado (experimental; desativado por padrão). É necessário para aplicar as regras de domínio dos perfis de permissões, a menos que requisitos `experimental_network` ativados e gerenciados por administradores iniciem o proxy. Use uma tabela ao definir opções de política no nível do recurso, como `domains`. Não filtra a pesquisa na Web, os aplicativos, o MCP nem outras ferramentas hospedadas.",
    },
    {
      key: "features.network_proxy.enabled",
      type: "boolean",
      description:
        "Inicie o proxy de rede para comandos executados em ambiente isolado quando o acesso desses comandos à rede estiver ativado. O padrão é `false`; as regras de domínio dos perfis de permissões não são aplicadas enquanto o proxy estiver desativado.",
    },
    {
      key: "features.network_proxy.domains",
      type: "map<string, allow | deny>",
      description:
        "Política de domínios para a rede em ambiente isolado. Por padrão, não é definida, o que significa que nenhum destino externo é permitido até você adicionar regras `allow`. Oferece suporte a correspondências exatas de hosts, a `*.example.com` apenas para subdomínios, a `**.example.com` para o domínio raiz e seus subdomínios e a regras globais de permissão com `*`; prefira regras com escopo delimitado, pois `*` libera amplamente o acesso de saída à rede pública. Adicione regras `deny` para destinos bloqueados; em caso de conflito, `deny` prevalece.",
    },
    {
      key: "features.network_proxy.unix_sockets",
      type: "map<string, allow | deny>",
      description:
        "Política de sockets Unix para a rede em ambiente isolado. Por padrão, não é definida; adicione entradas `allow` para os sockets permitidos.",
    },
    {
      key: "features.network_proxy.allow_local_binding",
      type: "boolean",
      description:
        "Permita acesso mais amplo à rede local/privada. O padrão é `false`; regras de permissão para um endereço IP local literal exato ou `localhost` ainda podem permitir destinos locais específicos.",
    },
    {
      key: "features.network_proxy.enable_socks5",
      type: "boolean",
      description: "Disponibilize suporte a SOCKS5. O padrão é `true`.",
    },
    {
      key: "features.network_proxy.enable_socks5_udp",
      type: "boolean",
      description: "Permita UDP por SOCKS5. O padrão é `true`.",
    },
    {
      key: "features.network_proxy.allow_upstream_proxy",
      type: "boolean",
      description:
        "Permita o encadeamento por meio de um proxy de saída definido no ambiente. O padrão é `true`.",
    },
    {
      key: "features.network_proxy.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "Permita endereços de escuta que não sejam de loopback. O padrão é `false`; ativar essa opção pode expor os pontos de escuta do proxy para além de localhost.",
    },
    {
      key: "features.network_proxy.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "Permita destinos arbitrários de sockets Unix, em vez de restringir o acesso à lista de permissões. O padrão é `false`; use somente em ambientes rigidamente controlados.",
    },
    {
      key: "features.network_proxy.proxy_url",
      type: "string",
      description:
        "URL de escuta HTTP para a rede em ambiente isolado. O padrão é `\"http://127.0.0.1:3128\"`.",
    },
    {
      key: "features.network_proxy.socks_url",
      type: "string",
      description:
        "URL de escuta SOCKS5. O padrão é `\"http://127.0.0.1:8081\"`.",
    },
    {
      key: "features.web_search",
      type: "boolean",
      description:
        "Opção legada obsoleta; prefira a configuração de nível superior `web_search`.",
    },
    {
      key: "features.web_search_cached",
      type: "boolean",
      description:
        "Opção legada obsoleta. Quando `web_search` não estiver definido, true corresponde a `web_search = \"cached\"`.",
    },
    {
      key: "features.web_search_request",
      type: "boolean",
      description:
        "Opção legada obsoleta. Quando `web_search` não estiver definido, true corresponde a `web_search = \"live\"`.",
    },
    {
      key: "features.shell_tool",
      type: "boolean",
      description:
        "Ative a ferramenta padrão `shell` para executar comandos (estável; ativada por padrão).",
    },
    {
      key: "features.enable_request_compression",
      type: "boolean",
      description:
        "Compacte os corpos das solicitações de streaming com zstd quando houver suporte (estável; ativado por padrão).",
    },
    {
      key: "features.skill_mcp_dependency_install",
      type: "boolean",
      description:
        "Permita solicitar e realizar a instalação de dependências MCP ausentes para habilidades (estável; ativado por padrão).",
    },
    {
      key: "features.fast_mode",
      type: "boolean",
      description:
        "Ative a seleção de níveis de serviço do catálogo de modelos na TUI, incluindo comandos do nível Fast quando o modelo ativo indicar suporte a eles (estável; ativada por padrão).",
    },
    {
      key: "features.prevent_idle_sleep",
      type: "boolean",
      description:
        "Impeça que o computador entre em suspensão enquanto um turno estiver em execução (experimental; desativado por padrão).",
    },
    {
      key: "suppress_unstable_features_warning",
      type: "boolean",
      description:
        "Oculte o aviso exibido quando sinalizadores de recursos em desenvolvimento estiverem ativados.",
    },
    {
      key: "model_providers.<id>",
      type: "table",
      description:
        "Definição de provedor personalizado. Os IDs dos provedores integrados (`openai`, `ollama` e `lmstudio`) são reservados e não podem ser substituídos.",
    },
    {
      key: "model_providers.<id>.name",
      type: "string",
      description: "Nome de exibição de um provedor de modelos personalizado.",
    },
    {
      key: "model_providers.<id>.base_url",
      type: "string",
      description: "URL base da API do provedor de modelos.",
    },
    {
      key: "model_providers.<id>.env_key",
      type: "string",
      description: "Variável do ambiente que fornece a chave de API do provedor.",
    },
    {
      key: "model_providers.<id>.env_key_instructions",
      type: "string",
      description: "Instruções opcionais de configuração da chave de API do provedor.",
    },
    {
      key: "model_providers.<id>.experimental_bearer_token",
      type: "string",
      description:
        "Token de portador definido diretamente para o provedor (não recomendado; use `env_key`).",
    },
    {
      key: "model_providers.<id>.requires_openai_auth",
      type: "boolean",
      description:
        "O provedor usa a autenticação da OpenAI (o padrão é false).",
    },
    {
      key: "model_providers.<id>.wire_api",
      type: "responses",
      description:
        "Protocolo usado pelo provedor. `responses` é o único valor aceito e o padrão quando omitido.",
    },
    {
      key: "model_providers.<id>.query_params",
      type: "map<string,string>",
      description: "Parâmetros de consulta adicionais anexados às solicitações ao provedor.",
    },
    {
      key: "model_providers.<id>.http_headers",
      type: "map<string,string>",
      description: "Cabeçalhos HTTP estáticos adicionados às solicitações ao provedor.",
    },
    {
      key: "model_providers.<id>.env_http_headers",
      type: "map<string,string>",
      description:
        "Cabeçalhos HTTP preenchidos a partir de variáveis do ambiente, quando presentes.",
    },
    {
      key: "model_providers.<id>.request_max_retries",
      type: "number",
      description:
        "Número de novas tentativas para solicitações HTTP ao provedor (padrão: 4).",
    },
    {
      key: "model_providers.<id>.stream_max_retries",
      type: "number",
      description: "Número de novas tentativas após interrupções do streaming SSE (padrão: 5).",
    },
    {
      key: "model_providers.<id>.stream_idle_timeout_ms",
      type: "number",
      description:
        "Tempo limite de inatividade dos fluxos SSE, em milissegundos (padrão: 300000).",
    },
    {
      key: "model_providers.<id>.supports_websockets",
      type: "boolean",
      description:
        "Indica se esse provedor oferece suporte ao transporte WebSocket da Responses API.",
    },
    {
      key: "model_providers.<id>.supports_standalone_web_search",
      type: "boolean",
      description:
        "Declare suporte a um endpoint compatível para pesquisa independente na Web (padrão: false). A pesquisa independente continua em desenvolvimento e desativada por padrão; a compatibilidade do provedor, por si só, não ativa esse recurso.",
    },
    {
      key: "model_providers.<id>.auth",
      type: "table",
      description:
        "Configuração de token de portador obtido por comando para um provedor personalizado. Não combine com `env_key`, `experimental_bearer_token` ou `requires_openai_auth`.",
    },
    {
      key: "model_providers.<id>.auth.command",
      type: "string",
      description:
        "Comando a executar quando o Codex precisar de um token de portador. O comando deve imprimir o token em stdout.",
    },
    {
      key: "model_providers.<id>.auth.args",
      type: "array<string>",
      description: "Argumentos passados ao comando que obtém o token.",
    },
    {
      key: "model_providers.<id>.auth.timeout_ms",
      type: "number",
      description:
        "Tempo máximo de execução do comando que obtém o token, em milissegundos (padrão: 5000).",
    },
    {
      key: "model_providers.<id>.auth.refresh_interval_ms",
      type: "number",
      description:
        "Intervalo, em milissegundos, entre as atualizações proativas do token feitas pelo Codex (padrão: 300000). Defina como `0` para atualizá-lo somente após uma nova tentativa de autenticação.",
    },
    {
      key: "model_providers.<id>.auth.cwd",
      type: "string (path)",
      description: "Diretório de trabalho do comando que obtém o token.",
    },
    {
      key: "model_providers.amazon-bedrock.aws.profile",
      type: "string",
      description:
        "Nome do perfil da AWS usado pelo provedor integrado `amazon-bedrock`.",
    },
    {
      key: "model_providers.amazon-bedrock.aws.region",
      type: "string",
      description: "Região da AWS usada pelo provedor integrado `amazon-bedrock`.",
    },
    {
      key: "model_reasoning_effort",
      type: "minimal | low | medium | high | xhigh",
      description:
        "Ajuste o esforço de raciocínio para modelos compatíveis (somente na Responses API; `xhigh` depende do modelo).",
    },
    {
      key: "plan_mode_reasoning_effort",
      type: "none | minimal | low | medium | high | xhigh",
      description:
        "Substituição do esforço de raciocínio específica do Modo planejamento. Quando essa opção não está definida, o Modo planejamento usa sua predefinição padrão integrada.",
    },
    {
      key: "model_reasoning_summary",
      type: "auto | concise | detailed | none",
      description:
        "Selecione o nível de detalhe do resumo do raciocínio ou desative os resumos por completo.",
    },
    {
      key: "model_verbosity",
      type: "low | medium | high",
      description:
        "Substituição opcional da verbosidade do GPT-5 na Responses API; quando essa opção não está definida, é usado o padrão do modelo ou da predefinição selecionada.",
    },
    {
      key: "model_supports_reasoning_summaries",
      type: "boolean",
      description: "Força o Codex a enviar ou não enviar metadados de raciocínio.",
    },
    {
      key: "shell_environment_policy.inherit",
      type: "all | core | none",
      description:
        "Herança básica de variáveis de ambiente ao criar subprocessos.",
    },
    {
      key: "shell_environment_policy.ignore_default_excludes",
      type: "boolean",
      description:
        "Mantém variáveis que contêm KEY, SECRET ou TOKEN antes da execução dos demais filtros (padrão: true). Defina como false para aplicar exclusões automáticas por nomes que indicam segredos.",
    },
    {
      key: "shell_environment_policy.filters",
      type: "map<string, include | exclude>",
      description:
        "Filtros canônicos de padrões de variáveis de ambiente, sem distinção entre maiúsculas e minúsculas. As entradas de inclusão criam uma lista de permissões e não podem restaurar valores excluídos. Os valores explícitos de `set` são aplicados após as exclusões. Não combine filtros com os arrays legados `exclude` ou `include_only` na mesma camada.",
    },
    {
      key: "shell_environment_policy.exclude",
      type: "array<string>",
      description:
        "Padrões legados de exclusão de variáveis de ambiente. Use `shell_environment_policy.filters` em novas configurações; não combine os dois formatos na mesma camada.",
    },
    {
      key: "shell_environment_policy.include_only",
      type: "array<string>",
      description:
        "Lista legada de padrões de variáveis de ambiente permitidas. Use `shell_environment_policy.filters` em novas configurações; não combine os dois formatos na mesma camada.",
    },
    {
      key: "shell_environment_policy.set",
      type: "map<string,string>",
      description:
        "Valores explícitos de variáveis de ambiente injetados após as exclusões; os filtros de inclusão ainda podem removê-los.",
    },
    {
      key: "shell_environment_policy.experimental_use_profile",
      type: "boolean",
      description: "Usa o perfil de shell do usuário ao criar subprocessos.",
    },
    {
      key: "project_root_markers",
      type: "array<string>",
      description:
        "Lista de nomes de arquivos que marcam a raiz do projeto; usada ao procurar a raiz do projeto nos diretórios superiores.",
    },
    {
      key: "project_doc_max_bytes",
      type: "number",
      description:
        "Número máximo de bytes lidos de `AGENTS.md` ao montar as instruções do projeto.",
    },
    {
      key: "project_doc_fallback_filenames",
      type: "array<string>",
      description: "Nomes de arquivos adicionais a procurar quando `AGENTS.md` não estiver presente.",
    },
    {
      key: "history.persistence",
      type: "save-all | none",
      description:
        "Controla se o Codex salva transcrições das sessões em history.jsonl.",
    },
    {
      key: "tool_output_token_limit",
      type: "number",
      description:
        "Limite de tokens para armazenar saídas individuais de ferramentas/funções no histórico.",
    },
    {
      key: "background_terminal_max_timeout",
      type: "number",
      description:
        "Duração máxima da janela de consulta, em milissegundos, para consultas vazias com `write_stdin` (consulta periódica ao terminal em segundo plano). Padrão: `300000` (5 minutos). Substitui a antiga chave `background_terminal_timeout`.",
    },
    {
      key: "history.max_bytes",
      type: "number",
      description:
        "Quando definido, limita o tamanho do arquivo de histórico em bytes, descartando as entradas mais antigas.",
    },
    {
      key: "file_opener",
      type: "vscode | vscode-insiders | windsurf | cursor | none",
      description:
        "Esquema de URI usado para abrir citações da saída do Codex (padrão: `vscode`).",
    },
    {
      key: "otel.environment",
      type: "string",
      description:
        "Tag de ambiente aplicada aos eventos OpenTelemetry emitidos (padrão: `dev`).",
    },
    {
      key: "otel.exporter",
      type: "none | otlp-http | otlp-grpc",
      description:
        "Seleciona o exportador do OpenTelemetry e fornece os metadados do endpoint, se houver.",
    },
    {
      key: "otel.trace_exporter",
      type: "none | otlp-http | otlp-grpc",
      description:
        "Seleciona o exportador de rastreamentos do OpenTelemetry e fornece os metadados do endpoint, se houver.",
    },
    {
      key: "otel.metrics_exporter",
      type: "none | statsig | otlp-http | otlp-grpc",
      description:
        "Seleciona o exportador de métricas do OpenTelemetry (padrão: `statsig`).",
    },
    {
      key: "otel.log_user_prompt",
      type: "boolean",
      description:
        "Ativa a exportação dos prompts brutos do usuário junto com os logs do OpenTelemetry.",
    },
    {
      key: "otel.exporter.<id>.endpoint",
      type: "string",
      description: "Endpoint do exportador para logs OTEL.",
    },
    {
      key: "otel.exporter.<id>.protocol",
      type: "binary | json",
      description: "Protocolo usado pelo exportador OTLP/HTTP.",
    },
    {
      key: "otel.exporter.<id>.headers",
      type: "map<string,string>",
      description: "Cabeçalhos estáticos incluídos nas solicitações do exportador OTEL.",
    },
    {
      key: "otel.trace_exporter.<id>.endpoint",
      type: "string",
      description: "Endpoint do exportador de rastreamentos para logs OTEL.",
    },
    {
      key: "otel.trace_exporter.<id>.protocol",
      type: "binary | json",
      description: "Protocolo usado pelo exportador de rastreamentos OTLP/HTTP.",
    },
    {
      key: "otel.trace_exporter.<id>.headers",
      type: "map<string,string>",
      description: "Cabeçalhos estáticos incluídos nas solicitações do exportador de rastreamentos OTEL.",
    },
    {
      key: "otel.exporter.<id>.tls.ca-certificate",
      type: "string",
      description: "Caminho do certificado da CA para o TLS do exportador OTEL.",
    },
    {
      key: "otel.exporter.<id>.tls.client-certificate",
      type: "string",
      description: "Caminho do certificado do cliente para o TLS do exportador OTEL.",
    },
    {
      key: "otel.exporter.<id>.tls.client-private-key",
      type: "string",
      description: "Caminho da chave privada do cliente para o TLS do exportador OTEL.",
    },
    {
      key: "otel.trace_exporter.<id>.tls.ca-certificate",
      type: "string",
      description: "Caminho do certificado da CA para o TLS do exportador de rastreamentos OTEL.",
    },
    {
      key: "otel.trace_exporter.<id>.tls.client-certificate",
      type: "string",
      description: "Caminho do certificado do cliente para o TLS do exportador de rastreamentos OTEL.",
    },
    {
      key: "otel.trace_exporter.<id>.tls.client-private-key",
      type: "string",
      description: "Caminho da chave privada do cliente para o TLS do exportador de rastreamentos OTEL.",
    },
    {
      key: "desktop.custom_file_handlers.<id>",
      type: "table",
      description:
        "Somente no nível do usuário. Define um destino adicional de **Abrir em** para o aplicativo do ChatGPT para desktop. Consulte [Adicionar manipuladores de arquivos personalizados](/codex/config-file/config-advanced#add-custom-file-handlers) para ver exemplos e restrições para os IDs dos manipuladores.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.label",
      type: "string",
      description: "Nome de exibição mostrado nos menus **Abrir em**. Obrigatório.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.icon",
      type: "string",
      description:
        "Caminho de um recurso incluído no pacote, URL `data:image/...` codificada em Base64, URI de arquivo ou caminho local absoluto para o ícone do manipulador. Obrigatório; origens não compatíveis usam o ícone padrão do VS Code.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.command",
      type: "string",
      description:
        "Caminho do executável ou nome do comando a ser detectado e iniciado. Obrigatório.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.args",
      type: "array<string>",
      description:
        "Argumentos inseridos entre o comando e a entrada de arquivo (padrão: `[]`).",
    },
    {
      key: "desktop.custom_file_handlers.<id>.input",
      type: "path | json_argument | json_stdin",
      description:
        "Forma como o aplicativo envia a entrada de arquivo ao manipulador (padrão: `path`).",
    },
    {
      key: "desktop.custom_file_handlers.<id>.supports_ssh",
      type: "boolean",
      description:
        "Disponibiliza o manipulador para arquivos em workspaces SSH (padrão: `false`).",
    },
    {
      key: "tui",
      type: "table",
      description:
        "Opções específicas da TUI, como ativar notificações integradas da área de trabalho.",
    },
    {
      key: "tui.notifications",
      type: "boolean | array<string>",
      description:
        "Ativa as notificações da TUI; opcionalmente, restringe-as a tipos específicos de evento.",
    },
    {
      key: "tui.notification_method",
      type: "auto | osc9 | bel",
      description:
        "Método usado para notificações do terminal (padrão: auto).",
    },
    {
      key: "tui.notification_condition",
      type: "unfocused | always",
      description:
        "Controla se a TUI emite notificações apenas quando o terminal está sem foco ou independentemente do foco. O padrão é `unfocused`.",
    },
    {
      key: "tui.animations",
      type: "boolean",
      description:
        "Ativa animações do terminal (tela de boas-vindas, efeito de brilho e indicador giratório) (padrão: true).",
    },
    {
      key: "tui.alternate_screen",
      type: "auto | always | never",
      description:
        "Controla o uso da tela alternativa na TUI (padrão: auto; no modo auto, ela não é usada no Zellij para preservar o histórico de rolagem).",
    },
    {
      key: "tui.resume_cwd",
      type: "current | session",
      description:
        "Diretório de trabalho usado ao retomar uma sessão ou criar um fork dela. Quando não definido, o Codex pede que você escolha caso o diretório atual seja diferente do diretório salvo da sessão.",
    },
    {
      key: "tui.vim_mode_default",
      type: "boolean",
      description:
        "Inicia o editor no modo normal do Vim, em vez do modo de inserção (padrão: false). Você ainda pode alternar esse modo por sessão com `/vim`.",
    },
    {
      key: "tui.raw_output_mode",
      type: "boolean",
      description:
        "Inicia a TUI no modo de histórico de rolagem bruto para facilitar a seleção e a cópia de texto no terminal (padrão: false). Você pode alterná-lo com `/raw` ou com o atalho de teclado padrão `alt-r`.",
    },
    {
      key: "tui.show_tooltips",
      type: "boolean",
      description:
        "Exibe dicas de introdução na tela de boas-vindas da TUI (padrão: true).",
    },
    {
      key: "tui.status_line",
      type: "array<string> | null",
      description:
        "Lista ordenada de identificadores dos itens da linha de status do rodapé da TUI. `null` desativa a linha de status.",
    },
    {
      key: "tui.terminal_title",
      type: "array<string> | null",
      description:
        "Lista ordenada de identificadores dos itens do título da janela/aba do terminal. O padrão é `[\"spinner\", \"project\"]`; `null` desativa as atualizações do título.",
    },
    {
      key: "tui.theme",
      type: "string",
      description:
        "Substituição do tema de realce de sintaxe (nome do tema em kebab-case).",
    },
    {
      key: "tui.keymap.<context>.<action>",
      type: "string | array<string>",
      description:
        "Vinculação de um atalho de teclado a uma ação da TUI. Os contextos compatíveis incluem `global`, `chat`, `composer`, `editor`, `vim_normal`, `vim_operator`, `vim_text_object`, `pager`, `list` e `approval`. Algumas ações do editor usam, como alternativa, as vinculações correspondentes de `tui.keymap.global`; quando houver suporte, as vinculações específicas do contexto têm precedência.",
    },
    {
      key: "tui.keymap.<context>.<action> = []",
      type: "empty array",
      description:
        "Remove a vinculação da ação nesse contexto do mapa de teclas. Os nomes das teclas usam strings normalizadas, como `ctrl-a`, `shift-enter`, `page-down` ou `minus`.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.enabled",
      type: "boolean",
      description:
        "Ativa ou desativa um servidor MCP incluído em um plug-in instalado sem alterar o manifesto do plug-in.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Comportamento padrão de aprovação para ferramentas em um servidor MCP fornecido por um plug-in.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.enabled_tools",
      type: "array<string>",
      description:
        "Lista de ferramentas permitidas expostas por um servidor MCP fornecido por um plug-in.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.disabled_tools",
      type: "array<string>",
      description:
        "Lista de bloqueio aplicada após `enabled_tools` para um servidor MCP fornecido por um plug-in.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Substituição individual do comportamento de aprovação de uma ferramenta MCP fornecida por um plug-in.",
    },
    {
      key: "tui.model_availability_nux.<model>",
      type: "integer",
      description: "Estado interno da dica exibida na inicialização, indexado pelo slug do modelo.",
    },
    {
      key: "hide_agent_reasoning",
      type: "boolean",
      description:
        "Suprime eventos de raciocínio tanto na TUI quanto na saída de `codex exec`.",
    },
    {
      key: "show_raw_agent_reasoning",
      type: "boolean",
      description:
        "Exibe o conteúdo bruto do raciocínio quando o modelo ativo o emite.",
    },
    {
      key: "disable_paste_burst",
      type: "boolean",
      description: "Desativa a detecção de colagem em rajadas na TUI.",
    },
    {
      key: "windows_wsl_setup_acknowledged",
      type: "boolean",
      description: "Registra a confirmação da apresentação inicial do Windows (somente no Windows).",
    },
    {
      key: "chatgpt_base_url",
      type: "string",
      description: "Substitui a URL base usada durante o fluxo de login do ChatGPT.",
    },
    {
      key: "cli_auth_credentials_store",
      type: "file | keyring | auto",
      description:
        "Controla onde a CLI armazena as credenciais em cache (arquivo auth.json ou chaveiro do sistema operacional).",
    },
    {
      key: "mcp_oauth_credentials_store",
      type: "auto | file | keyring",
      description: "Local de armazenamento preferido para credenciais OAuth do MCP.",
    },
    {
      key: "mcp_oauth_callback_port",
      type: "integer",
      description:
        "Porta fixa global opcional para o servidor HTTP local de callback usado durante o login OAuth do MCP. O `oauth.callback_port` específico de um servidor tem precedência. Quando nenhum dos dois é definido, o Codex se vincula a uma porta efêmera escolhida pelo sistema operacional.",
    },
    {
      key: "mcp_oauth_callback_url",
      type: "string",
      description:
        "URL base de callback opcional para o login OAuth do MCP, como uma URL de entrada de um devbox. Clientes pré-registrados recém-adicionados usam essa URL sem alterações quando o servidor de autorização oferece suporte à identificação do emissor; clientes existentes sem um callback salvo acrescentam um ID de callback específico do servidor. Sem suporte à identificação do emissor, qualquer servidor MCP pré-registrado cujo callback configurado não contenha o ID obrigatório usa essa URL com o ID acrescentado. As portas nas URLs de callback não definem a porta de escuta.",
    },
    {
      key: "experimental_use_unified_exec_tool",
      type: "boolean",
      description:
        "Nome legado para ativar a execução unificada; prefira `[features].unified_exec` ou `codex --enable unified_exec`.",
    },
    {
      key: "tools.web_search",
      type: 'boolean | { context_size = "low|medium|high", allowed_domains = [string], location = { country, region, city, timezone } }',
      description:
        "Configuração opcional da ferramenta de pesquisa na Web. O formato de objeto permite definir o tamanho do contexto de pesquisa, os domínios de pesquisa permitidos e a localização aproximada do usuário. Esses filtros de domínio de pesquisa são separados das regras de domínio de rede para comandos executados no Sandbox e não restringem conectores nem servidores MCP.",
    },
    {
      key: "tools.view_image",
      type: "boolean",
      description: "Ativa a ferramenta `view_image` para anexar imagens locais.",
    },
    {
      key: "web_search",
      type: "disabled | cached | indexed | live",
      description:
        "Modo de pesquisa na Web (padrão: `\"cached\"`; cached usa um índice mantido pela OpenAI sem acesso externo à Web; indexed permite acesso externo somente quando autorizado pelo índice de pesquisa; se você usar `--yolo` ou outra configuração de Sandbox com acesso completo, o padrão será `\"live\"`). Use `\"live\"` para acessar conteúdo em tempo real sem restrições ou `\"disabled\"` para remover a ferramenta.",
    },
    {
      key: "default_permissions",
      type: "string",
      description:
        "Nome do perfil de permissões padrão a ser aplicado às chamadas de ferramentas no Sandbox. Os perfis integrados são `:read-only`, `:workspace` e `:danger-full-access`; nomes de perfis personalizados exigem tabelas `[permissions.<name>]` correspondentes. Não combine com `sandbox_mode` ou `[sandbox_workspace_write]`.",
    },
    {
      key: "permissions.<name>.description",
      type: "string",
      description:
        "Descrição legível por humanos deste perfil nomeado. Um perfil não herda a descrição do perfil pai por meio de `extends`.",
    },
    {
      key: "permissions.<name>.extends",
      type: "string",
      description:
        "Perfil pai opcional aplicado antes deste perfil nomeado. Defina-o como outro perfil nomeado, `:read-only` ou `:workspace`; `:danger-full-access`, perfis pais indefinidos e ciclos são rejeitados.",
    },
    {
      key: "permissions.<name>.workspace_roots",
      type: "table",
      description:
        "Raízes do workspace definidas pelo perfil que recebem as regras de sistema de arquivos de `:workspace_roots` junto com as raízes do workspace usadas pela sessão em tempo de execução.",
    },
    {
      key: "permissions.<name>.workspace_roots.<path>",
      type: "boolean",
      description:
        "Inclui um caminho no conjunto de raízes do workspace do perfil quando definido como `true`. Entradas desativadas permanecem inativas.",
    },
    {
      key: "permissions.<name>.filesystem",
      type: "table",
      description:
        "Perfil nomeado de permissões do sistema de arquivos. Cada chave é um caminho absoluto ou um token especial, como `:minimal` ou `:workspace_roots`.",
    },
    {
      key: "permissions.<name>.filesystem.glob_scan_max_depth",
      type: "number",
      description:
        "Profundidade máxima para expandir padrões glob de negação de leitura em plataformas que capturam as correspondências antes da inicialização do Sandbox. Quando definida, deve ser de pelo menos `1`.",
    },
    {
      key: "permissions.<name>.filesystem.<path-or-glob>",
      type: '"read" | "write" | "deny" | table',
      description:
        "Concede acesso direto a um caminho, padrão glob ou token especial, ou delimita o escopo de entradas aninhadas nessa raiz. Use `\"deny\"` para negar a leitura dos caminhos correspondentes.",
    },
    {
      key: 'permissions.<name>.filesystem.":workspace_roots".<subpath-or-glob>',
      type: '"read" | "write" | "deny"',
      description:
        "Acesso ao sistema de arquivos com escopo relativo a cada raiz efetiva do workspace. Use `\".\"` para a própria raiz; subcaminhos com padrões glob, como `\"**/*.env\"`, podem negar leituras com `\"deny\"`.",
    },
    {
      key: "permissions.<name>.network.enabled",
      type: "boolean",
      description:
        "Ativa o acesso à rede para comandos neste perfil de permissões. Isso não inicia o proxy de rede. Quando nem `features.network_proxy` nem os requisitos de rede gerenciados pelo administrador estão ativados, os comandos acessam a rede diretamente, e as regras de domínio do perfil não são aplicadas.",
    },
    {
      key: "permissions.<name>.network.proxy_url",
      type: "string",
      description:
        "URL do serviço de escuta HTTP usada quando este perfil de permissões ativa o acesso à rede no Sandbox.",
    },
    {
      key: "permissions.<name>.network.enable_socks5",
      type: "boolean",
      description:
        "Disponibiliza suporte a SOCKS5 quando este perfil de permissões ativa o acesso à rede no Sandbox.",
    },
    {
      key: "permissions.<name>.network.socks_url",
      type: "string",
      description: "Endpoint do proxy SOCKS5 usado por este perfil de permissões.",
    },
    {
      key: "permissions.<name>.network.enable_socks5_udp",
      type: "boolean",
      description: "Permite UDP pelo serviço de escuta SOCKS5 quando ativado.",
    },
    {
      key: "permissions.<name>.network.allow_upstream_proxy",
      type: "boolean",
      description:
        "Permite encadear o tráfego de rede no Sandbox por meio de outro proxy antes de chegar ao destino.",
    },
    {
      key: "permissions.<name>.network.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "Permite que os serviços de escuta de rede no Sandbox se vinculem a endereços que não sejam de loopback. Ativar esta opção pode expor esses serviços além de localhost.",
    },
    {
      key: "permissions.<name>.network.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "Permite destinos arbitrários de soquetes Unix em vez do conjunto restrito padrão. Use apenas em ambientes rigorosamente controlados.",
    },
    {
      key: "permissions.<name>.network.mode",
      type: "limited | full",
      description: "Modo do proxy de rede usado para o tráfego de subprocessos.",
    },
    {
      key: "permissions.<name>.network.domains",
      type: "table",
      description:
        "Regras de domínio para comandos executados no Sandbox. São aplicadas somente quando `features.network_proxy` ou requisitos de rede ativados e gerenciados pelo administrador ativam o proxy. Oferecem suporte a hosts exatos, `*.example.com`, `**.example.com` e regras globais de permissão `*`; `deny` prevalece. Não restringem a pesquisa na Web, aplicativos ou servidores MCP.",
    },
    {
      key: "permissions.<name>.network.domains.<pattern>",
      type: "allow | deny",
      description:
        "Permite ou nega um host exato ou um padrão curinga com escopo delimitado, como `*.example.com` ou `**.example.com`.",
    },
    {
      key: "permissions.<name>.network.unix_sockets",
      type: "table",
      description:
        "Substituições da lista de permissões de soquetes Unix para o acesso à rede no Sandbox. Use caminhos de soquete como chaves; `allow` adiciona um caminho, e `deny` o rejeita.",
    },
    {
      key: "permissions.<name>.network.unix_sockets.<path>",
      type: "allow | deny",
      description:
        "Adiciona um caminho absoluto de soquete Unix à lista de permissões efetiva com `allow` ou o rejeita com `deny`. As entradas negadas são omitidas da lista de permissões efetiva.",
    },
    {
      key: "permissions.<name>.network.allow_local_binding",
      type: "boolean",
      description:
        "Permite acesso mais amplo a redes locais ou privadas por meio da rede no Sandbox. Regras de permissão para um endereço IP local literal exato ou para `localhost` ainda podem autorizar destinos locais específicos quando esta opção permanece definida como `false`.",
    },
    {
      key: "projects.<path>.trust_level",
      type: "string",
      description:
        "Marca um projeto ou uma árvore de trabalho como confiável ou não confiável (`\"trusted\"` | `\"untrusted\"`). Projetos não confiáveis ignoram as camadas `.codex/` específicas do projeto, incluindo a configuração local do projeto, os ganchos e as regras.",
    },
    {
      key: "notice.hide_full_access_warning",
      type: "boolean",
      description: "Registra a confirmação do prompt de aviso sobre acesso completo.",
    },
    {
      key: "notice.hide_world_writable_warning",
      type: "boolean",
      description:
        "Registra a confirmação do aviso sobre diretórios do Windows com permissão de gravação para qualquer usuário.",
    },
    {
      key: "notice.hide_rate_limit_model_nudge",
      type: "boolean",
      description: "Registra a desativação do lembrete de troca de modelo devido ao limite de taxa.",
    },
    {
      key: "notice.hide_gpt5_1_migration_prompt",
      type: "boolean",
      description: "Registra a confirmação do prompt de migração para o GPT-5.1.",
    },
    {
      key: "notice.hide_gpt-5.1-codex-max_migration_prompt",
      type: "boolean",
      description:
        "Registra a confirmação do prompt de migração para o gpt-5.1-codex-max.",
    },
    {
      key: "notice.model_migrations",
      type: "map<string,string>",
      description: "Registra as migrações de modelo confirmadas como mapeamentos do modelo antigo para o novo.",
    },
    {
      key: "forced_login_method",
      type: "chatgpt | api",
      description: "Restringe o Codex a um método de autenticação específico.",
    },
    {
      key: "forced_chatgpt_workspace_id",
      type: "string (uuid)",
      description: "Limita os logins do ChatGPT a um identificador específico de workspace.",
    },
  ]}
  client:load
/>

Você encontra o esquema JSON mais recente de `config.toml` [aqui](/codex/config-schema.json).

Para ter preenchimento automático e diagnósticos ao editar `config.toml` no VS Code ou no Cursor, você pode instalar a extensão [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) e adicionar esta linha no início do seu `config.toml`:

```toml
#:schema https://developers.openai.com/codex/config-schema.json

Observação: renomeie `experimental_instructions_file` para `model_instructions_file`. O Codex considera a chave antiga obsoleta; atualize as configurações existentes para usar o novo nome.

## `requirements.toml`

`requirements.toml` é um arquivo de configuração imposto pelo administrador que restringe configurações sensíveis à segurança que os usuários não podem substituir. Para detalhes, locais e exemplos, consulte [Requisitos impostos pelo administrador](/pt-BR/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).

Para usuários do ChatGPT Business e do ChatGPT Enterprise, o Codex também pode aplicar requisitos
obtidos da nuvem. Consulte a página de segurança para saber mais sobre a precedência.

Use `[features]` em `requirements.toml` para fixar flags de recursos em tempo de execução usando as mesmas
chaves canônicas de `config.toml`. Os requisitos também podem incluir chaves documentadas
exclusivas do aplicativo que não pertencem a `config.toml`. As chaves omitidas permanecem
sem restrições.

Alguns requisitos gerenciados impõem um valor de configuração exato em vez de uma
lista de permissões. Os usuários não podem substituir valores impostos para caminhos, preferências de atualização, políticas de shell de login,
configurações de feedback ou configurações de área de trabalho privada do Windows.

As listas gerenciadas de perfis de permissões autorizados exigem o Codex 0.138.0 ou posterior. O Codex
0.137.0 e versões anteriores ignoram `allowed_permission_profiles` e a configuração gerenciada
`default_permissions`.

Use `allowed_sandbox_modes` com `sandbox_mode`. Nas implantações com perfis de permissões,
use `allowed_permission_profiles` com a configuração gerenciada
`default_permissions`.

A tabela `[models.new_thread]` fornece valores padrão gerenciados, mas não os impõe.
As opções explícitas de inicialização definidas por flags dedicadas da CLI ou por substituições com `--config` têm
precedência. Uma substituição explícita de modelo ou de esforço de raciocínio ignora os dois campos gerenciados
de modelo; `service_tier` é independente.

Os requisitos de navegador abrangem três interfaces distintas. `in_app_browser`
controla o painel do navegador que uma pessoa abre e usa diretamente. `browser_use`
controla o trabalho realizado pelo agente em um navegador. `computer_use` controla o trabalho realizado pelo agente
em aplicativos nativos para desktop.

Os valores aninhados das políticas de Navegador e Uso do computador não concedem acesso por
si só. Um `allow` específico de uma origem ou aplicativo pode substituir o valor padrão da
mesma fonte de política, mas as verificações normais de recursos, aprovação e outras políticas
continuam sendo aplicadas. Quando tanto os requisitos gerenciados quanto `config.toml` se aplicam, um `deny`
de qualquer um deles prevalece.

<ConfigTable
  options={[
    {
      key: "sqlite_home",
      type: "string (path)",
      description:
        "Impõe o uso do diretório em que o Codex armazena o estado de execução baseado em SQLite.",
    },
    {
      key: "log_dir",
      type: "string (path)",
      description: "Impõe o uso do diretório em que o Codex grava os arquivos de log locais.",
    },
    {
      key: "model_catalog_json",
      type: "string (path)",
      description: "Impõe o catálogo de modelos em JSON que o Codex usa na inicialização.",
    },
    {
      key: "check_for_update_on_startup",
      type: "boolean",
      description: "Impõe a configuração que determina se o Codex verifica atualizações ao iniciar.",
    },
    {
      key: "allow_login_shell",
      type: "boolean",
      description: "Impõe a configuração que determina se as ferramentas de shell podem iniciar um shell de login.",
    },
    {
      key: "feedback",
      type: "table",
      description: "Configurações gerenciadas de feedback.",
    },
    {
      key: "feedback.enabled",
      type: "boolean",
      description:
        "Impõe a configuração que determina se os usuários podem enviar feedback nos clientes do Codex.",
    },
    {
      key: "allowed_approval_policies",
      type: "array<string>",
      description:
        "Valores permitidos para `approval_policy` (por exemplo, `untrusted`, `on-request`, `never` e `granular`).",
    },
    {
      key: "allowed_approvals_reviewers",
      type: "array<string>",
      description:
        "Valores permitidos para `approvals_reviewer`, como `user` e `auto_review`.",
    },
    {
      key: "guardian_policy_config",
      type: "string",
      description:
        "Instruções gerenciadas de política em Markdown para revisão automática. Essas instruções têm precedência sobre a política local `[auto_review].policy`. Valores em branco são ignorados.",
    },
    {
      key: "allowed_permission_profiles",
      type: "table<boolean>",
      description:
        "Lista completa dos perfis de permissões permitidos. Perfis definidos como `true` são permitidos. Perfis omitidos ou definidos como `false` são bloqueados, inclusive os adicionados em versões futuras. Quando fontes de requisitos são combinadas, as entradas são associadas pelo nome do perfil.",
    },
    {
      key: "allowed_permission_profiles.<name>",
      type: "boolean",
      description:
        "Permita ou bloqueie um perfil de permissões integrado ou personalizado definido em uma fonte de configuração ou de requisitos carregada. Uma fonte de requisitos posterior, de maior precedência, pode usar `false` para desativar um perfil permitido por uma fonte anterior, de menor precedência.",
    },
    {
      key: "default_permissions",
      type: "string",
      description:
        "Perfil de permissões padrão gerenciado. O perfil deve ser permitido por `allowed_permission_profiles`. Defina esta opção explicitamente para obter um comportamento previsível; se ela for omitida, o Codex usará `:workspace` como padrão somente quando tanto `:workspace` quanto `:read-only` forem explicitamente permitidos.",
    },
    {
      key: "enforce_residency",
      type: "string",
      description:
        "Exija que o tráfego do serviço Codex use uma residência de dados compatível. Atualmente, aceita `us`.",
    },
    {
      key: "models",
      type: "table",
      description:
        "Configurações padrão de modelo gerenciadas para novas conversas. Esses valores têm prioridade sobre os padrões do usuário e do projeto, mas uma seleção explícita para a nova conversa pode substituí-los.",
    },
    {
      key: "models.new_thread",
      type: "table",
      description:
        "Configurações padrão a aplicar quando uma nova conversa local começa. Cada configuração de modelo é opcional.",
    },
    {
      key: "models.new_thread.model",
      type: "string",
      description:
        "Modelo padrão para novas conversas. Uma substituição explícita por `--model` ou por `--config` para modelo ou raciocínio tem precedência.",
    },
    {
      key: "models.new_thread.model_reasoning_effort",
      type: "string",
      description:
        "Esforço de raciocínio padrão para novas conversas. Uma substituição explícita de modelo ou de esforço de raciocínio faz com que ambos os campos de modelo gerenciados sejam ignorados.",
    },
    {
      key: "models.new_thread.service_tier",
      type: "string",
      description:
        "Nível de serviço padrão para novas conversas. Uma substituição explícita do nível de serviço tem precedência, independentemente dos campos de modelo.",
    },
    {
      key: "permissions",
      type: "table",
      description:
        "Perfis de permissões definidos pelo administrador, identificados pelo nome do perfil. Usa os mesmos campos de perfil de `config.toml`.",
    },
    {
      key: "permissions.<name>",
      type: "table",
      description:
        "Perfil de permissões definido pelo administrador. O nome não pode começar com `:`, usar o nome reservado `filesystem` nem duplicar um perfil de uma configuração carregada. Usa os mesmos campos de perfil de `config.toml`; consulte o guia de Permissões para ver o esquema completo do perfil.",
    },
    {
      key: "allowed_sandbox_modes",
      type: "array<string>",
      description: "Valores permitidos para `sandbox_mode`.",
    },
    {
      key: "windows",
      type: "table",
      description: "Requisitos do Sandbox nativo do Windows.",
    },
    {
      key: "windows.allowed_sandbox_implementations",
      type: "array<string>",
      description:
        "Implementações do Sandbox nativo do Windows permitidas para `windows.sandbox` (`elevated` e `unelevated`). A lista não pode estar vazia. Quando ambas são permitidas e nenhum modo está selecionado, o Codex dá preferência a `elevated`.",
    },
    {
      key: "windows.sandbox_private_desktop",
      type: "boolean",
      description:
        "Defina de forma obrigatória se o Sandbox nativo do Windows inicia seu processo filho em uma área de trabalho privada.",
    },
    {
      key: "remote_sandbox_config",
      type: "array<table>",
      description:
        "Requisitos de Sandbox específicos por host. A primeira entrada cujos `hostname_patterns` correspondem ao nome de host resolvido substitui `allowed_sandbox_modes` de nível superior nessa fonte de requisitos. Atualmente, as entradas específicas por host substituem apenas os modos de Sandbox.",
    },
    {
      key: "remote_sandbox_config[].hostname_patterns",
      type: "array<string>",
      description:
        "Padrões de nomes de host sem distinção entre maiúsculas e minúsculas. Aceita `*` para qualquer sequência de caracteres e `?` para um caractere.",
    },
    {
      key: "remote_sandbox_config[].allowed_sandbox_modes",
      type: "array<string>",
      description:
        "Modos de Sandbox permitidos que se aplicam quando há correspondência com esta entrada específica do host.",
    },
    {
      key: "allowed_web_search_modes",
      type: "array<string>",
      description:
        "Valores permitidos para `web_search` (`disabled`, `cached`, `indexed`, `live`). `disabled` é sempre permitido; na prática, uma lista vazia permite apenas `disabled`.",
    },
    {
      key: "allow_managed_hooks_only",
      type: "boolean",
      description:
        "Quando `true`, o Codex ignora ganchos de usuário, projeto, sessão e plug-in, mas continua permitindo ganchos gerenciados de `requirements.toml` e de outras camadas de configuração gerenciadas.",
    },
    {
      key: "allow_appshots",
      type: "boolean",
      description:
        "Defina como `false` para desativar as Capturas do app para usuários gerenciados. Se esta opção for omitida, as Capturas do app não ficam limitadas pelos requisitos e seguem a disponibilidade normal do produto.",
    },
    {
      key: "allow_remote_control",
      type: "boolean",
      description:
        "Defina como `false` para desativar o controle remoto de dispositivos para usuários gerenciados. Se esta opção for omitida, o controle remoto de dispositivos não fica limitado pelos requisitos e segue a disponibilidade normal do produto.",
    },
    {
      key: "allow_browser_and_computer_use",
      type: "boolean",
      description:
        "Defina como `false` para bloquear tanto o recurso Navegador controlado pelo agente quanto o Uso do computador em aplicativos nativos. Definir como `true` ou omitir esta opção não ativa nenhum dos dois recursos; as demais verificações de recursos, políticas e aprovação continuam se aplicando.",
    },
    {
      key: "features.plugin_sharing",
      type: "boolean",
      description:
        "No `requirements.toml` gerenciado na nuvem, defina como `false` para desativar o compartilhamento de plug-ins criados localmente no workspace.",
    },
    {
      key: "features",
      type: "table",
      description:
        "Valores fixados dos recursos. Use os nomes canônicos de `config.toml` para recursos do ambiente de execução; as chaves documentadas de requisitos exclusivos do aplicativo também são aceitas aqui.",
    },
    {
      key: "features.<name>",
      type: "boolean",
      description:
        "Exija que um recurso documentado do ambiente de execução ou do aplicativo permaneça ativado ou desativado.",
    },
    {
      key: "features.apps",
      type: "boolean",
      description:
        "Fixe a integração com Apps como disponível ou indisponível para usuários gerenciados.",
    },
    {
      key: "features.in_app_updates",
      type: "boolean",
      description:
        "Em `requirements.toml`, defina como `false` para desativar as atualizações no aplicativo. Quando este requisito é omitido, as atualizações permanecem ativadas por padrão.",
    },
    {
      key: "features.in_app_browser",
      type: "boolean",
      description:
        "Em `requirements.toml`, defina como `false` para desativar o painel do navegador integrado que os usuários abrem e controlam diretamente.",
    },
    {
      key: "features.browser_use",
      type: "boolean",
      description:
        "Em `requirements.toml`, defina como `false` para desativar o recurso Navegador controlado pelo agente.",
    },
    {
      key: "features.browser_use_external",
      type: "boolean",
      description:
        "Em `requirements.toml`, defina como `false` para impedir que o Codex opere navegadores compatíveis por meio da extensão do navegador do ChatGPT, inclusive abas existentes e sessões autenticadas.",
    },
    {
      key: "features.browser_use_full_cdp_access",
      type: "boolean",
      description:
        "Em `requirements.toml`, defina como `false` para desativar o acesso completo ao Chrome DevTools Protocol no ambiente de execução local, inclusive o modo de desenvolvedor do navegador, e impedir que o aplicativo do ChatGPT para desktop ative a configuração correspondente. Se esta opção for omitida, aplica-se a disponibilidade normal do produto.",
    },
    {
      key: "features.fast_mode",
      type: "boolean",
      description:
        "Fixe o recurso canônico `fast_mode` como ativado ou desativado para usuários gerenciados.",
    },
    {
      key: "features.guardian_approval",
      type: "boolean",
      description:
        "Fixe a aprovação pelo Guardian como disponível ou indisponível para usuários gerenciados.",
    },
    {
      key: "features.memories",
      type: "boolean",
      description: "Fixe o recurso Memórias como disponível ou indisponível para usuários gerenciados.",
    },
    {
      key: "features.multi_agent",
      type: "boolean",
      description: "Fixe o recurso multiagente como disponível ou indisponível para usuários gerenciados.",
    },
    {
      key: "features.plugins",
      type: "boolean",
      description: "Fixe os plug-ins como disponíveis ou indisponíveis para usuários gerenciados.",
    },
    {
      key: "features.remote_plugin",
      type: "boolean",
      description:
        "Fixe o catálogo remoto de plug-ins como disponível ou indisponível para usuários gerenciados.",
    },
    {
      key: "features.computer_use",
      type: "boolean",
      description:
        "Em `requirements.toml`, defina como `false` para desativar o Uso do computador, o recurso Gravar e reproduzir e os fluxos relacionados de instalação ou ativação.",
    },
    {
      key: "features.workspace_dependencies",
      type: "boolean",
      description:
        "Fixe o ambiente de execução incluído para dependências do workspace como disponível ou indisponível para usuários gerenciados.",
    },
    {
      key: "in_app_browser",
      type: "table",
      description:
        "Requisitos do painel do navegador integrado. Estas configurações não controlam o recurso Navegador operado pelo agente.",
    },
    {
      key: "in_app_browser.allow_external_browser_settings_import",
      type: "boolean",
      description:
        "Defina como `false` para impedir que os usuários importem configurações ou dados de navegação de um navegador externo para o navegador integrado. Definir como `true` ou omitir esta opção mantém a importação disponível quando as demais verificações do produto a permitem. Esta configuração é exclusivamente gerenciada e não pode ser substituída em `config.toml`.",
    },
    {
      key: "browser_use",
      type: "table",
      description: "Requisitos gerenciados para o recurso Navegador controlado pelo agente.",
    },
    {
      key: "browser_use.allow_history_access",
      type: "boolean",
      description:
        "Defina como `false` para impedir que o recurso Navegador leia o histórico de navegação. Definir como `true` ou omitir esta opção mantém em vigor as configurações normais de histórico e as verificações de disponibilidade.",
    },
    {
      key: "browser_use.disable_auto_review",
      type: "boolean",
      description:
        "Defina como `true` para ignorar a revisão automática do recurso Navegador e pedir aprovação ao usuário em seu lugar. Definir como `false` ou omitir esta opção mantém a revisão automática disponível quando outras configurações a permitem.",
    },
    {
      key: "browser_use.allow_global_persistent_approval",
      type: "boolean",
      description:
        "Defina como `false` para impedir que o recurso Navegador crie ou respeite aprovações `Always allow` que abranjam todos os sites, como permitir downloads de qualquer site. As aprovações já salvas são ignoradas, não excluídas. Definir como `true` ou omitir esta opção não cria uma aprovação.",
    },
    {
      key: "browser_use.default_origin_policy",
      type: "table",
      description:
        "Configuração alternativa para cada opção do recurso Navegador quando nenhuma entrada correspondente em `browser_use.origins` a define. Uma regra de origem correspondente substitui a configuração alternativa nessa fonte. Em seguida, o Codex aplica o resultado mais restritivo entre os requisitos gerenciados e a configuração do usuário.",
    },
    {
      key: "browser_use.default_origin_policy.access",
      type: "allow | deny",
      description:
        "Use `deny` para bloquear o recurso Navegador nas origens que usam a configuração alternativa. Bloquear uma origem também bloqueia uploads, downloads, acesso completo à depuração do navegador e revisão automática nessa origem. `allow` apenas permite que as verificações normais de aprovação e de políticas prossigam.",
    },
    {
      key: "browser_use.default_origin_policy.downloads",
      type: "allow | deny",
      description:
        "Use `deny` para bloquear downloads pelo recurso Navegador nas origens que usam a configuração alternativa. `allow` apenas permite que as verificações normais de aprovação e de políticas prossigam.",
    },
    {
      key: "browser_use.default_origin_policy.uploads",
      type: "allow | deny",
      description:
        "Use `deny` para bloquear uploads pelo recurso Navegador nas origens que usam a configuração alternativa. `allow` apenas permite que as verificações normais de aprovação e de políticas prossigam.",
    },
    {
      key: "browser_use.default_origin_policy.full_cdp_access",
      type: "allow | deny",
      description:
        "Use `deny` para bloquear o acesso completo ao Chrome DevTools Protocol (CDP) nas origens que usam a configuração alternativa. `allow` apenas permite que as verificações normais de adesão e aprovação prossigam.",
    },
    {
      key: "browser_use.default_origin_policy.auto_review",
      type: "allow | deny",
      description:
        "Use `deny` para ignorar a revisão automática nas origens que usam a configuração alternativa e pedir aprovação ao usuário em seu lugar. `allow` mantém a revisão automática disponível quando outras configurações a permitem.",
    },
    {
      key: "browser_use.default_origin_policy.persistent_approval",
      type: "boolean",
      description:
        "Defina como `false` para impedir que o recurso Navegador salve ou respeite uma aprovação `Always allow` nas origens que usam a configuração alternativa. Aprovações para o turno ou a conversa atual ainda podem se aplicar. `true` disponibiliza `Always allow` quando as demais condições o permitem, mas não cria uma aprovação.",
    },
    {
      key: "browser_use.default_origin_policy.access_approval_lifetime",
      type: "turn | thread",
      description:
        "Defina a duração de uma aprovação não persistente de acesso a sites: `turn` a limita ao turno atual, e `thread` a mantém pelo restante da conversa atual. `persistent_approval` controla separadamente se `Always allow` está disponível. O padrão do produto é `thread`.",
    },
    {
      key: "browser_use.origins",
      type: "map<string, table>",
      description:
        "Políticas do recurso Navegador específicas por origem. As chaves usam `<scheme>://<host-pattern>[:<port>]` com `http` ou `https`. Use um host exato, `*.example.com` apenas para subdomínios ou `**.example.com` para o domínio base e seus subdomínios. Outros curingas `*` podem abranger pontos, portanto `region*.example.com` também corresponde a `region.api.example.com`; um host `*` corresponde a todos os hosts desse esquema. Esquemas e portas não padrão são relevantes; portas padrão explícitas são removidas durante a normalização. Caminhos, consultas, nomes de usuário ou senhas incorporados e esquemas ou portas com curingas são inválidos. Coloque o padrão entre aspas no TOML, por exemplo `[browser_use.origins.\"https://**.example.com\"]`.",
    },
    {
      key: "browser_use.origins.<pattern>",
      type: "table",
      description:
        "Política para origens que correspondem a este padrão. Se vários padrões corresponderem, o Codex usará o valor mais restritivo para cada capacidade: `deny` prevalece sobre `allow`, `false` sobre `true` e `turn` sobre `thread`.",
    },
    {
      key: "browser_use.origins.<pattern>.access",
      type: "allow | deny",
      description:
        "Use `deny` para bloquear o recurso Navegador nas origens correspondentes. O bloqueio também impede uploads, downloads, acesso completo à depuração do navegador e revisão automática nessas origens. `allow` apenas permite que as verificações normais de aprovação e de políticas prossigam.",
    },
    {
      key: "browser_use.origins.<pattern>.downloads",
      type: "allow | deny",
      description:
        "Use `deny` para bloquear downloads pelo recurso Navegador nas origens correspondentes. `allow` apenas permite que as verificações normais de aprovação e de políticas prossigam.",
    },
    {
      key: "browser_use.origins.<pattern>.uploads",
      type: "allow | deny",
      description:
        "Use `deny` para bloquear uploads pelo recurso Navegador nas origens correspondentes. `allow` apenas permite que as verificações normais de aprovação e de políticas prossigam.",
    },
    {
      key: "browser_use.origins.<pattern>.full_cdp_access",
      type: "allow | deny",
      description:
        "Use `deny` para bloquear o acesso completo ao Chrome DevTools Protocol (CDP) nas origens correspondentes. `allow` apenas permite que as verificações normais de adesão e aprovação prossigam.",
    },
    {
      key: "browser_use.origins.<pattern>.auto_review",
      type: "allow | deny",
      description:
        "Use `deny` para ignorar a revisão automática nas origens correspondentes e pedir aprovação ao usuário em seu lugar. `allow` mantém a revisão automática disponível quando outras configurações a permitem.",
    },
    {
      key: "browser_use.origins.<pattern>.persistent_approval",
      type: "boolean",
      description:
        "Defina como `false` para impedir que o recurso Navegador salve ou respeite uma aprovação `Always allow` nas origens correspondentes. Aprovações para o turno ou a conversa atual ainda podem se aplicar. `true` disponibiliza `Always allow` quando as demais condições o permitem, mas não cria uma aprovação.",
    },
    {
      key: "browser_use.origins.<pattern>.access_approval_lifetime",
      type: "turn | thread",
      description:
        "Defina a duração de uma aprovação não persistente de acesso a sites para as origens correspondentes: `turn` a limita ao turno atual, e `thread` a mantém pelo restante da conversa atual. `persistent_approval` controla separadamente se `Always allow` está disponível.",
    },
    {
      key: "computer_use",
      type: "table",
      description:
        "Requisitos gerenciados para o trabalho realizado pelo agente em aplicativos nativos para desktop. Tanto as regras gerenciadas de aplicativos quanto as regras de aplicativos de `config.toml` são impostas; um aplicativo deve ser permitido por cada fonte de políticas.",
    },
    {
      key: "computer_use.allow_locked_computer_use",
      type: "boolean",
      description:
        "Defina como `false` para impedir que os usuários ativem o Uso com o dispositivo bloqueado em um dispositivo macOS gerenciado. Esse requisito remove os controles de ativação; ele não desativa o Uso com o dispositivo bloqueado se o recurso já estiver ativado. Se omitido, aplica-se a disponibilidade normal do produto.",
    },
    {
      key: "computer_use.allow_persistent_approval",
      type: "boolean",
      description:
        "Defina como `false` para remover a opção de salvar aprovações de aplicativos entre sessões. As aprovações para a sessão atual continuam disponíveis. Definir como `true` ou omitir esse valor não aprova um aplicativo.",
    },
    {
      key: "computer_use.default_app_access",
      type: "allow | deny",
      description:
        "Acesso padrão para aplicativos nativos que não correspondem a uma regra específica da plataforma. `deny` bloqueia o acesso. `allow` apenas permite que as verificações normais de aprovação e de políticas prossigam. O padrão do produto é `allow`.",
    },
    {
      key: "computer_use.macos",
      type: "table",
      description: "Regras de aplicativos para Uso do computador no macOS.",
    },
    {
      key: "computer_use.macos.bundle_ids",
      type: "map<string, allow | deny>",
      description:
        "Mapeie identificadores exatos de bundle do macOS para `allow` ou `deny`. Uma regra correspondente substitui `computer_use.default_app_access` na mesma fonte de políticas. Uma negação nos requisitos gerenciados ou na configuração do usuário continua bloqueando o acesso.",
    },
    {
      key: "computer_use.macos.bundle_ids.<bundle-id>",
      type: "allow | deny",
      description:
        "Use `deny` para bloquear o identificador exato de bundle. `allow` substitui apenas o padrão desta fonte de políticas e ainda exige que qualquer outra fonte de políticas e o fluxo normal de aprovação permitam o aplicativo.",
    },
    {
      key: "computer_use.windows",
      type: "table",
      description:
        "Regras de aplicativos para Uso do computador com aplicativos Windows empacotados e não empacotados.",
    },
    {
      key: "computer_use.windows.aumids",
      type: "map<string, allow | deny>",
      description:
        "Mapeie os Application User Model IDs (AUMIDs) exatos e registrados de aplicativos empacotados e assinados para `allow` ou `deny`. Uma regra correspondente substitui `computer_use.default_app_access` na mesma fonte de políticas.",
    },
    {
      key: "computer_use.windows.aumids.<aumid>",
      type: "allow | deny",
      description:
        "Use `deny` para bloquear a identidade exata do aplicativo empacotado. `allow` substitui apenas o padrão desta fonte de políticas e ainda exige que qualquer outra fonte de políticas e o fluxo normal de aprovação permitam o aplicativo.",
    },
    {
      key: "computer_use.windows.exes",
      type: "array<table>",
      description:
        "Regras para executáveis Windows assinados e não empacotados. As regras verificam a correspondência com o editor verificado do executável e suas informações de versão assinadas, não com seu caminho ou nome de arquivo atual. Uma regra de negação correspondente tem precedência sobre regras de permissão correspondentes. Executáveis não assinados usam `computer_use.default_app_access`; executáveis cuja identidade assinada não pode ser verificada sem ambiguidade são bloqueados.",
    },
    {
      key: "computer_use.windows.exes[].publisher_name",
      type: "string",
      description:
        "Nome exato e obrigatório do editor no certificado de assinatura confiável do executável, formatado como um nome distinto X.500 do Windows.",
    },
    {
      key: "computer_use.windows.exes[].product_name",
      type: "string",
      description:
        "Valor exato e obrigatório de `ProductName` nas informações de versão assinadas do executável.",
    },
    {
      key: "computer_use.windows.exes[].binary_name",
      type: "string",
      description:
        "Valor opcional de `OriginalFilename` nas informações de versão assinadas do executável. A comparação não diferencia maiúsculas de minúsculas. Se uma regra correspondente de editor e produto exigir esse valor, mas o executável não o fornecer, o Uso do computador bloqueará o executável.",
    },
    {
      key: "computer_use.windows.exes[].access",
      type: "allow | deny",
      description:
        "Decisão de acesso obrigatória para executáveis correspondentes. `deny` bloqueia o acesso. `allow` substitui apenas o padrão desta fonte de políticas e ainda exige que qualquer outra fonte de políticas e o fluxo normal de aprovação permitam o aplicativo.",
    },
    {
      key: "experimental_network",
      type: "table",
      description:
        "Requisitos de rede gerenciados pelo administrador para comandos locais executados no sandbox, impostos por meio de `requirements.toml`. Quando ativados, esses requisitos podem iniciar o proxy de rede de comandos sem `features.network_proxy`. As ferramentas de navegador verificam separadamente as negações de rede gerenciadas e as listas exclusivas de permissões. Esses requisitos não encaminham o tráfego do navegador pelo proxy nem controlam a pesquisa na Web, os aplicativos, os servidores MCP, o tráfego de aplicativos nativos ou a rede do Codex Cloud.",
    },
    {
      key: "experimental_network.enabled",
      type: "boolean",
      description:
        "Ative os requisitos de rede no sandbox. Isso não concede acesso à rede quando o sandbox ativo mantém desativado o acesso à rede para comandos.",
    },
    {
      key: "experimental_network.http_port",
      type: "integer",
      description:
        "Porta de escuta HTTP em loopback a ser usada para os requisitos de `[experimental_network]`.",
    },
    {
      key: "experimental_network.socks_port",
      type: "integer",
      description:
        "Porta de escuta SOCKS5 em loopback a ser usada para os requisitos de `[experimental_network]`.",
    },
    {
      key: "experimental_network.allow_upstream_proxy",
      type: "boolean",
      description:
        "Permita que a rede no sandbox use um proxy upstream definido no ambiente em uma cadeia de proxies.",
    },
    {
      key: "experimental_network.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "Permita endereços de escuta fora do loopback para os requisitos de `[experimental_network]`. Ativar essa opção pode expor os serviços de escuta além de localhost.",
    },
    {
      key: "experimental_network.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "Permita destinos arbitrários de sockets Unix em vez de restringir o acesso à lista de permissões. Use apenas em ambientes rigorosamente controlados.",
    },
    {
      key: "experimental_network.domains",
      type: "map<string, allow | deny>",
      description:
        "Política de domínios do administrador em formato de mapa para a rede no sandbox. Aceita hosts exatos, `*.example.com` apenas para subdomínios, `**.example.com` para o domínio raiz e seus subdomínios, e regras globais de permissão com `*`; prefira regras com escopo delimitado, pois `*` libera amplamente o acesso de saída à rede pública. `deny` prevalece em caso de conflito. Não combine esta configuração com `experimental_network.allowed_domains` ou `experimental_network.denied_domains`.",
    },
    {
      key: "experimental_network.allowed_domains",
      type: "array<string>",
      description:
        "Regras de permissão do administrador para o acesso à rede por comandos no sandbox enquanto o proxy de rede gerenciado estiver ativado. Essas regras não se aplicam à pesquisa na Web, aos aplicativos ou aos servidores MCP. Não combine esta configuração com `experimental_network.domains`.",
    },
    {
      key: "experimental_network.denied_domains",
      type: "array<string>",
      description:
        "Regras de negação do administrador em formato de lista para a rede no sandbox. Não combine esta configuração com `experimental_network.domains`.",
    },
    {
      key: "experimental_network.managed_allowed_domains_only",
      type: "boolean",
      description:
        "Quando `true`, apenas as regras de permissão gerenciadas pelo administrador permanecem em vigor enquanto os requisitos de rede no sandbox estiverem ativos; adições do usuário à lista de permissões são ignoradas. Sem regras de permissão gerenciadas, as regras de permissão de domínios adicionadas pelo usuário não permanecem em vigor.",
    },
    {
      key: "experimental_network.unix_sockets",
      type: "map<string, allow | deny>",
      description:
        "Política de sockets Unix gerenciada pelo administrador para a rede no sandbox.",
    },
    {
      key: "experimental_network.allow_local_binding",
      type: "boolean",
      description:
        "Permita acesso mais amplo à rede local ou privada para a rede no sandbox. Regras de permissão para um endereço IP local literal exato ou para `localhost` ainda podem permitir destinos locais específicos quando esta configuração permanece como `false`.",
    },
    {
      key: "hooks",
      type: "table",
      description:
        "Ganchos de ciclo de vida gerenciados e impostos pelo administrador. Exige um diretório de ganchos gerenciados e usa o mesmo esquema de eventos de `[hooks]` definido diretamente em `config.toml`.",
    },
    {
      key: "hooks.managed_dir",
      type: "string (absolute path)",
      description:
        "Diretório que contém scripts de ganchos gerenciados no macOS e no Linux. O Codex verifica se o caminho é absoluto e se o diretório existe antes de carregar os ganchos gerenciados.",
    },
    {
      key: "hooks.windows_managed_dir",
      type: "string (absolute path)",
      description:
        "Diretório que contém scripts de ganchos gerenciados no Windows. O Codex verifica se o caminho é absoluto e se o diretório existe antes de carregar os ganchos gerenciados.",
    },
    {
      key: "hooks.",
      type: "array<table>",
      description:
        "Grupos de comparadores para um evento de gancho, como `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `SessionStart`, `SessionEnd`, `SubagentStart`, `SubagentStop`, `UserPromptSubmit` ou `Stop`.",
    },
    {
      key: "hooks.[].hooks",
      type: "array<table>",
      description:
        "Manipuladores de ganchos para um grupo de comparadores. Ganchos de comando e de ferramentas MCP são compatíveis, enquanto manipuladores de ganchos de prompt e de agente são analisados, mas não executados.",
    },
    {
      key: "hooks.[].hooks[].async",
      type: "boolean",
      description:
        "Execute um gancho de comando em segundo plano sem atrasar a operação que o acionou. O padrão é `false`; `SessionEnd` sempre é executado de forma síncrona. Consulte [Execute ganchos em segundo plano](/codex/hooks#run-hooks-in-the-background).",
    },
    {
      key: "hooks.[].hooks[].additionalContextLimit",
      type: "integer",
      description:
        "Limite aproximado de tokens por manipulador para salvar no disco um `additionalContext` excessivamente grande e mostrar uma prévia mais curta ao modelo. O padrão é `2500`; `0` passa o contexto completo diretamente ao modelo. Consulte [Saídas grandes de ganchos](/codex/hooks#large-hook-output).",
    },
    {
      key: "hooks.[].hooks[].commandWindows",
      type: "string",
      description:
        "Substituição de comando exclusiva do Windows para ganchos de comando. O alias TOML `command_windows` também é aceito.",
    },
    {
      key: "permissions.filesystem.deny_read",
      type: "array<string>",
      description:
        "Restrições de leitura no sistema de arquivos impostas pelo administrador. As entradas podem ser caminhos ou padrões glob, e os usuários não podem flexibilizá-las com configurações locais.",
    },
    {
      key: "mcp_servers",
      type: "table",
      description:
        "Lista de permissões de servidores MCP que podem ser ativados. Tanto o nome do servidor (`<id>`) quanto sua identidade devem corresponder para que o servidor MCP seja ativado. Qualquer servidor MCP configurado que não esteja na lista de permissões (ou cuja identidade não corresponda) é desativado.",
    },
    {
      key: "mcp_servers.<id>.identity",
      type: "table",
      description:
        "Regra de identidade para um único servidor MCP. Defina `command` (stdio) ou `url` (HTTP com streaming).",
    },
    {
      key: "mcp_servers.<id>.identity.command",
      type: "string | table",
      description:
        "Permita um servidor MCP stdio por meio de uma string de comando exata ou use uma tabela de comparação para exigir um executável exato e comparadores de argumentos ordenados. O formato de string não inspeciona argumentos, `cwd`, `env` ou `env_vars`.",
    },
    {
      key: "mcp_servers.<id>.identity.command.executable",
      type: "string",
      description:
        "Executável ao qual o `command` configurado para o servidor stdio deve corresponder exatamente.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args",
      type: "array<table>",
      description:
        "Comparadores de argumentos ordenados para um servidor stdio. A lista de argumentos configurada deve ter o mesmo tamanho, e deve haver correspondência em todas as posições. Comparadores de comandos não inspecionam `cwd`, `env` ou `env_vars`.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].match",
      type: "exact | prefix | regex",
      description: "Operação de correspondência para o argumento nesta posição.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].value",
      type: "string",
      description: "Valor usado por um comparador de argumentos `exact` ou `prefix`.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].expression",
      type: "string",
      description:
        "Expressão regular usada por um comparador de argumentos `regex`. A expressão deve ser válida e corresponder ao valor completo do argumento.",
    },
    {
      key: "mcp_servers.<id>.identity.url",
      type: "string | table",
      description:
        "Permita um servidor MCP HTTP com streaming por meio de uma string de URL exata ou use uma tabela de comparação de valores `exact`, `prefix` ou `regex`.",
    },
    {
      key: "mcp_servers.<id>.identity.url.match",
      type: "exact | prefix | regex",
      description: "Operação de correspondência para a URL configurada do servidor MCP.",
    },
    {
      key: "mcp_servers.<id>.identity.url.value",
      type: "string",
      description: "Valor usado por um comparador de URLs `exact` ou `prefix`.",
    },
    {
      key: "mcp_servers.<id>.identity.url.expression",
      type: "string",
      description:
        "Expressão regular usada por um comparador de URLs `regex`. A expressão deve ser válida e corresponder ao valor completo da URL.",
    },
    {
      key: "plugins",
      type: "table",
      description:
        "Listas de permissões de servidores MCP específicas por plug-in, indexadas pelo identificador do plug-in. Quando esta tabela está presente, os servidores incluídos em plug-ins são desativados se não houver uma entrada correspondente para o plug-in e o servidor.",
    },
    {
      key: "plugins.<plugin>.mcp_servers",
      type: "table",
      description:
        "Lista de permissões para servidores MCP incluídos em um plug-in. Os requisitos para servidores de plug-ins usam os mesmos formatos de identidade exata e de comparadores que os requisitos `mcp_servers` de nível superior.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity",
      type: "table",
      description:
        "Regra de identidade para um servidor MCP incluído em um plug-in. Defina `command` (stdio) ou `url` (HTTP com streaming).",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command",
      type: "string | table",
      description:
        "Permita um servidor MCP stdio de um plug-in por meio de uma string de comando exata ou use uma tabela de comparação para exigir um executável exato e comparadores de argumentos ordenados.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.executable",
      type: "string",
      description:
        "Executável ao qual o comando configurado para o servidor stdio incluído no plug-in deve corresponder exatamente.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args",
      type: "array<table>",
      description:
        "Comparadores de argumentos ordenados para um servidor stdio incluído no plug-in. A lista de argumentos configurada deve ter o mesmo tamanho, e deve haver correspondência em todas as posições.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].match",
      type: "exact | prefix | regex",
      description: "Operação de correspondência para o argumento nesta posição.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].value",
      type: "string",
      description: "Valor usado por um comparador de argumentos `exact` ou `prefix`.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].expression",
      type: "string",
      description:
        "Expressão regular usada por um comparador de argumentos `regex`. A expressão deve corresponder ao valor completo do argumento.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url",
      type: "string | table",
      description:
        "Permita um servidor MCP HTTP com streaming de um plug-in por meio de uma string de URL exata ou use uma tabela de comparação de valores `exact`, `prefix` ou `regex`.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.match",
      type: "exact | prefix | regex",
      description: "Operação de correspondência para a URL do servidor MCP incluído no plug-in.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.value",
      type: "string",
      description: "Valor usado por um comparador de URLs `exact` ou `prefix`.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.expression",
      type: "string",
      description:
        "Expressão regular usada por um comparador de URLs `regex`. A expressão deve corresponder ao valor completo da URL.",
    },
    {
      key: "marketplaces",
      type: "table",
      description:
        "Requisitos definidos pelo administrador para fontes de marketplaces de plug-ins. As regras entram em vigor quando `restrict_to_allowed_sources` é `true`.",
    },
    {
      key: "marketplaces.restrict_to_allowed_sources",
      type: "boolean",
      description:
        "Quando `true`, exige que as fontes de marketplace configuradas pelo usuário correspondam a `allowed_sources` nas operações de adição de marketplace, instalação de plug-ins e atualização de marketplaces Git configurados. Os marketplaces da OpenAI gerenciados pelo Codex continuam permitidos quando a fonte e o nome correspondem aos valores reservados. Isso não filtra, em tempo de execução, os marketplaces já configurados pelo usuário.",
    },
    {
      key: "marketplaces.allowed_sources",
      type: "table",
      description:
        "Fontes permitidas de marketplace indexadas pelo nome da regra escolhido pelo administrador. Nomes distintos se acumulam entre as camadas de requisitos; os campos associados ao mesmo nome seguem a precedência normal das camadas.",
    },
    {
      key: "marketplaces.allowed_sources.<name>",
      type: "table",
      description:
        "Uma regra de fonte permitida. O valor final de `source` após a mesclagem dos requisitos determina quais campos no mesmo nível o Codex interpreta.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.source",
      type: "git | host_pattern | local",
      description:
        "Tipo de correspondência para fontes do marketplace. Use `git` para um repositório, `host_pattern` para hosts Git que correspondam a uma expressão regular ou `local` para um diretório.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.url",
      type: "string",
      description:
        "URL do repositório Git, obrigatória quando `source = \"git\"`. O Codex normaliza as URLs configuradas e permitidas antes de exigir uma correspondência exata do repositório.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.ref",
      type: "string",
      description:
        "Referência Git exata opcional para uma regra `git`. Quando omitida, a regra permite qualquer referência do repositório correspondente.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.host_pattern",
      type: "string",
      description:
        "Expressão regular obrigatória quando `source = \"host_pattern\"`. O Codex verifica a correspondência com o nome do host em letras minúsculas extraído de uma fonte Git HTTPS, SSH ou no formato SCP. Use `^` e `$` para exigir uma correspondência com o nome completo do host.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.path",
      type: "string (absolute path)",
      description:
        "Diretório local do marketplace, obrigatório quando `source = \"local\"`. O Codex exige um caminho absoluto e compara os caminhos após a normalização.",
    },
    {
      key: "apps",
      type: "table",
      description:
        "Requisitos gerenciados de aplicativos, organizados por identificador do aplicativo. Os requisitos podem desativar um aplicativo ou restringir o comportamento de aprovação de ferramentas individuais.",
    },
    {
      key: "apps.<id>.enabled",
      type: "boolean",
      description:
        "Defina como `false` para desativar um aplicativo. Um requisito definido como desativado mantém seu efeito restritivo quando várias fontes de requisitos são mescladas.",
    },
    {
      key: "apps.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description: "Defina o modo de aprovação gerenciado para uma ferramenta de um aplicativo.",
    },
    {
      key: "rules",
      type: "table",
      description:
        "Regras de comandos impostas pelo administrador e mescladas com arquivos `.rules`. As regras de requisitos devem ser restritivas.",
    },
    {
      key: "rules.prefix_rules",
      type: "array<table>",
      description:
        "Lista de regras de prefixo obrigatórias. Cada regra deve incluir `pattern` e `decision`.",
    },
    {
      key: "rules.prefix_rules[].pattern",
      type: "array<table>",
      description:
        "Prefixo de comando expresso como tokens de padrão. Cada token define `token` ou `any_of`.",
    },
    {
      key: "rules.prefix_rules[].pattern[].token",
      type: "string",
      description: "Um único token literal nesta posição.",
    },
    {
      key: "rules.prefix_rules[].pattern[].any_of",
      type: "array<string>",
      description: "Uma lista de tokens alternativos permitidos nesta posição.",
    },
    {
      key: "rules.prefix_rules[].decision",
      type: "prompt | forbidden",
      description:
        "Obrigatório. As regras de requisitos só podem solicitar aprovação ou proibir (não permitir).",
    },
    {
      key: "rules.prefix_rules[].justification",
      type: "string",
      description:
        "Justificativa opcional, não vazia, exibida em solicitações de aprovação ou mensagens de rejeição.",
    },
  ]}
  client:load
/>

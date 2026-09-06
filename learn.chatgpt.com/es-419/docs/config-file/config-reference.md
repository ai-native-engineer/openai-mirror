<!-- source: https://learn.chatgpt.com/es-419/docs/config-file/config-reference -->

Usa esta página como referencia para buscar información sobre los archivos de configuración de Codex. Para obtener orientación conceptual y ejemplos, comienza por [Configuración básica](/es-419/codex/config-file/config-basic) y [Configuración avanzada](/es-419/codex/config-file/config-advanced).

## `config.toml`

La configuración a nivel de usuario se encuentra en `~/.codex/config.toml`. También puedes sobrescribir valores para un proyecto mediante archivos `.codex/config.toml`. Codex solo carga los archivos de configuración específicos del proyecto si confías en el proyecto.

La configuración específica del proyecto no puede sobrescribir las claves locales del equipo relativas al proveedor, la autenticación,
los metadatos de solicitudes de Apps controlados por el host, las notificaciones, la selección del perfil de configuración
o el enrutamiento de telemetría. Codex ignora `openai_base_url`,
`chatgpt_base_url`, `apps_mcp_product_sku`, `model_provider`,
`model_providers`, `notify`, `profile`, `profiles`,
`experimental_realtime_ws_base_url` y `otel` cuando aparecen en un archivo
`.codex/config.toml` local del proyecto; coloca las claves de proveedor, notificación y telemetría
en la configuración a nivel de usuario. Los [archivos de perfil](/es-419/codex/config-file/config-advanced#profiles) de configuración se encuentran junto a
`config.toml` con el formato `$CODEX_HOME/profile-name.config.toml`; selecciona uno con
`--profile profile-name`.

Para las claves de sandbox y aprobación (`approval_policy`, `sandbox_mode` y `sandbox_workspace_write.*`), complementa esta referencia con [Sandbox y aprobaciones](/es-419/codex/agent-approvals-security#sandbox-and-approvals), [Rutas protegidas en raíces con permiso de escritura](/es-419/codex/agent-approvals-security#protected-paths-in-writable-roots) y [Acceso a la red](/es-419/codex/agent-approvals-security#network-access). Para los perfiles de permisos en beta, consulta [Permisos](/es-419/codex/permissions).

<ConfigTable
  options={[
    {
      key: "model",
      type: "string",
      description: "Modelo que se usará (p. ej., `gpt-5.5`).",
    },
    {
      key: "review_model",
      type: "string",
      description:
        "Modelo alternativo opcional que usa `/review` (el valor predeterminado es el modelo de la sesión actual).",
    },
    {
      key: "model_provider",
      type: "string",
      description: "ID del proveedor de `model_providers` (valor predeterminado: `openai`).",
    },
    {
      key: "openai_base_url",
      type: "string",
      description:
        "URL base alternativa para el proveedor de modelos `openai` integrado.",
    },
    {
      key: "model_context_window",
      type: "number",
      description: "Tokens disponibles en la ventana de contexto del modelo activo.",
    },
    {
      key: "model_auto_compact_token_limit",
      type: "number",
      description:
        "Umbral de tokens que activa la compactación automática del historial (si no se establece, se usan los valores predeterminados del modelo).",
    },
    {
      key: "model_auto_compact_token_limit_scope",
      type: "total | body_after_prefix",
      description:
        "Controla si el umbral de compactación automática cuenta todo el contexto activo (`total`, el valor predeterminado) o solo el crecimiento posterior al prefijo conservado de la ventana de compactación (`body_after_prefix`).",
    },
    {
      key: "model_catalog_json",
      type: "string (path)",
      description:
        "Ruta opcional a un catálogo de modelos en JSON que se carga al iniciar. El archivo de perfil `$CODEX_HOME/profile-name.config.toml` seleccionado puede sobrescribir este valor para ese perfil.",
    },
    {
      key: "oss_provider",
      type: "lmstudio | ollama",
      description:
        "Proveedor local predeterminado que se usa en ejecuciones con `--oss` (si no se establece, se solicita al usuario que elija uno).",
    },
    {
      key: "approval_policy",
      type: "untrusted | on-request | never | { granular = { sandbox_approval = bool, rules = bool, mcp_elicitations = bool, request_permissions = bool, skill_approval = bool } }",
      description:
        "Controla cuándo Codex se detiene para solicitar aprobación antes de ejecutar comandos. También puedes usar `approval_policy = { granular = { ... } }` para permitir o rechazar automáticamente categorías específicas de prompts mientras los demás prompts siguen siendo interactivos. `on-failure` está obsoleto; usa `on-request` para ejecuciones interactivas o `never` para ejecuciones no interactivas.",
    },
    {
      key: "approval_policy.granular.sandbox_approval",
      type: "boolean",
      description:
        "Cuando es `true`, se permite mostrar los prompts de aprobación para elevar los permisos del sandbox.",
    },
    {
      key: "approval_policy.granular.rules",
      type: "boolean",
      description:
        "Cuando es `true`, se permite mostrar las solicitudes de aprobación activadas por reglas `prompt` de execpolicy.",
    },
    {
      key: "approval_policy.granular.mcp_elicitations",
      type: "boolean",
      description:
        "Cuando es `true`, se permite mostrar las solicitudes de información de MCP en lugar de rechazarlas automáticamente.",
    },
    {
      key: "approval_policy.granular.request_permissions",
      type: "boolean",
      description:
        "Cuando es `true`, se permite mostrar los prompts de la herramienta `request_permissions`.",
    },
    {
      key: "approval_policy.granular.skill_approval",
      type: "boolean",
      description:
        "Cuando es `true`, se permite mostrar los prompts de aprobación de scripts de habilidades.",
    },
    {
      key: "approvals_reviewer",
      type: "user | auto_review",
      description:
        "Determina quién revisa los prompts de aprobación que cumplen los requisitos según las políticas de aprobación `on-request` o granulares. El valor predeterminado es `user`; `auto_review` usa el subagente revisor. Esta configuración no modifica el entorno aislado ni revisa las acciones que ya están permitidas dentro del sandbox.",
    },
    {
      key: "auto_review.policy",
      type: "string",
      description:
        "Instrucciones locales de política en Markdown para la revisión automática. La configuración administrada `guardian_policy_config` tiene prioridad. Se ignoran los valores en blanco.",
    },
    {
      key: "allow_login_shell",
      type: "boolean",
      description:
        "Permite que las herramientas basadas en shell usen la semántica de un shell de inicio de sesión. El valor predeterminado es `true`; cuando es `false`, se rechazan las solicitudes `login = true` y, si se omite `login`, se usan shells sin inicio de sesión de forma predeterminada.",
    },
    {
      key: "sandbox_mode",
      type: "read-only | workspace-write | danger-full-access",
      description:
        "Política del sandbox para el acceso al sistema de archivos y a la red durante la ejecución de comandos.",
    },
    {
      key: "sandbox_workspace_write.writable_roots",
      type: "array<string>",
      description:
        "Raíces adicionales con permiso de escritura cuando `sandbox_mode = \"workspace-write\"`.",
    },
    {
      key: "sandbox_workspace_write.network_access",
      type: "boolean",
      description:
        "Permite el acceso saliente a la red dentro del sandbox workspace-write.",
    },
    {
      key: "sandbox_workspace_write.exclude_tmpdir_env_var",
      type: "boolean",
      description:
        "Excluye `$TMPDIR` de las raíces con permiso de escritura en el modo workspace-write.",
    },
    {
      key: "sandbox_workspace_write.exclude_slash_tmp",
      type: "boolean",
      description:
        "Excluye `/tmp` de las raíces con permiso de escritura en el modo workspace-write.",
    },
    {
      key: "windows.sandbox",
      type: "unelevated | elevated",
      description:
        "Modo de sandbox nativo exclusivo de Windows que se usa al ejecutar Codex de forma nativa en Windows.",
    },
    {
      key: "windows.sandbox_private_desktop",
      type: "boolean",
      description:
        "En Windows nativo, ejecuta de forma predeterminada el proceso secundario final dentro del sandbox en un escritorio privado. Establece `false` solo para mantener la compatibilidad con el comportamiento anterior de `Winsta0\\\\Default`.",
    },
    {
      key: "browser_use.allow_history_access",
      type: "boolean",
      description:
        "Establece `false` para restringir el acceso al historial del navegador. Los requisitos administrados pueden imponer esta restricción.",
    },
    {
      key: "browser_use.default_origin_policy",
      type: "table",
      description:
        "Restricciones predeterminadas para los orígenes del navegador. Admite `access`, `uploads`, `downloads` y `full_cdp_access`, cada uno con el valor `allow` o `deny`.",
    },
    {
      key: "browser_use.origins.<origin>",
      type: "table",
      description:
        "Restricciones del navegador por origen con los mismos campos que `browser_use.default_origin_policy`. Incluye un esquema HTTP o HTTPS y, opcionalmente, un puerto; omite las rutas, las consultas y los fragmentos. Los valores locales no pueden flexibilizar las denegaciones administradas.",
    },
    {
      key: "computer_use.default_app_access",
      type: "allow | deny",
      description:
        "Política predeterminada de acceso a Apps nativas para Uso de la computadora. Las entradas específicas de cada App pueden proporcionar una política; la configuración local no puede flexibilizar las restricciones administradas.",
    },
    {
      key: "computer_use.macos.bundle_ids",
      type: "map<string, allow | deny>",
      description: "Acceso a Apps nativas de macOS con el identificador del bundle como clave.",
    },
    {
      key: "computer_use.windows.aumids",
      type: "map<string, allow | deny>",
      description:
        "Acceso a Apps empaquetadas de Windows con el Application User Model ID (AUMID) como clave.",
    },
    {
      key: "computer_use.windows.exes",
      type: "array<table>",
      description:
        "Reglas de acceso a ejecutables de Windows. Cada regla requiere `publisher_name`, `product_name` y `access` (`allow` o `deny`); `binary_name` es opcional.",
    },
    {
      key: "computer_use.windows.always_allowed_app_ids",
      type: "array<string>",
      description:
        "Identificadores de las Apps de Windows que Uso de la computadora puede abrir sin solicitar aprobación. Las Apps que no están en la lista requieren aprobación; elimina las entradas guardadas desde la configuración de Uso de la computadora de la aplicación de escritorio de ChatGPT.",
    },
    {
      key: "notify",
      type: "array<string>",
      description:
        "Comando que se invoca para las notificaciones; recibe una carga útil JSON de Codex.",
    },
    {
      key: "check_for_update_on_startup",
      type: "boolean",
      description:
        "Comprueba si hay actualizaciones de Codex al iniciar (configúralo como false solo cuando las actualizaciones se administren de manera centralizada).",
    },
    {
      key: "feedback.enabled",
      type: "boolean",
      description:
        "Habilita el envío de comentarios mediante `/feedback` en los clientes locales (valor predeterminado: true).",
    },
    {
      key: "analytics.enabled",
      type: "boolean",
      description:
        "Habilita o deshabilita la analítica para este equipo o perfil. Si no se establece, se aplica el valor predeterminado del cliente.",
    },
    {
      key: "instructions",
      type: "string",
      description:
        "Reservado para uso futuro; es preferible usar `model_instructions_file` o `AGENTS.md`.",
    },
    {
      key: "developer_instructions",
      type: "string",
      description:
        "Instrucciones adicionales del desarrollador que se agregan a la sesión (opcionales).",
    },
    {
      key: "log_dir",
      type: "string (path)",
      description:
        "Directorio donde Codex escribe los archivos de registro; el valor predeterminado es `$CODEX_HOME/log`. Al establecer este valor explícitamente, también se habilita en ese directorio el registro opcional de la TUI en texto sin formato, `codex-tui.log`.",
    },
    {
      key: "sqlite_home",
      type: "string (path)",
      description:
        "Directorio donde Codex almacena la base de datos de estado basada en SQLite para las tareas de los agentes y otros estados reanudables del entorno de ejecución.",
    },
    {
      key: "compact_prompt",
      type: "string",
      description: "Reemplazo del prompt de compactación del historial definido directamente en la configuración.",
    },
    {
      key: "model_instructions_file",
      type: "string (path)",
      description:
        "Reemplazo de las instrucciones integradas que se usa en lugar de `AGENTS.md`.",
    },
    {
      key: "personality",
      type: "none | friendly | pragmatic",
      description:
        "Estilo de comunicación predeterminado para los modelos que declaran `supportsPersonality`; puede sobrescribirse por hilo o turno, o mediante `/personality`.",
    },
    {
      key: "service_tier",
      type: "string",
      description:
        "Nivel de servicio preferido para turnos nuevos. Usa `fast` u otro nivel que ofrezca el modelo activo; `fast` se asigna al valor de solicitud `priority`.",
    },
    {
      key: "experimental_compact_prompt_file",
      type: "string (path)",
      description:
        "Carga desde un archivo el prompt alternativo de compactación (experimental).",
    },
    {
      key: "skills.max_context_tokens",
      type: "integer (positive)",
      description:
        "Presupuesto de tokens para el catálogo de habilidades disponibles. El valor predeterminado es el 2 % de la ventana de contexto del modelo. Los valores explícitos tienen un límite de `10000` tokens.",
    },
    {
      key: "skills.config",
      type: "array<object>",
      description: "Valores de habilitación específicos por habilidad almacenados en config.toml.",
    },
    {
      key: "skills.config.<index>.path",
      type: "string (path)",
      description: "Ruta a la carpeta de una habilidad que contiene `SKILL.md`.",
    },
    {
      key: "skills.config.<index>.enabled",
      type: "boolean",
      description: "Habilita o deshabilita la habilidad indicada.",
    },
    {
      key: "apps.<id>.enabled",
      type: "boolean",
      description:
        "Habilita o deshabilita una App o un conector específico por su ID (valor predeterminado: true).",
    },
    {
      key: "apps._default.enabled",
      type: "boolean",
      description:
        "Estado de habilitación predeterminado para todas las Apps, salvo que se establezca otro para una App específica.",
    },
    {
      key: "apps._default.destructive_enabled",
      type: "boolean",
      description:
        "Valor predeterminado para permitir o denegar herramientas de Apps con `destructive_hint = true`.",
    },
    {
      key: "apps._default.open_world_enabled",
      type: "boolean",
      description:
        "Valor predeterminado para permitir o denegar herramientas de Apps con `open_world_hint = true`.",
    },
    {
      key: "apps._default.approvals_reviewer",
      type: "user | auto_review",
      description:
        "Revisor predeterminado de los prompts de aprobación de herramientas de Apps, salvo que se configure otro para una App específica. Si se omite, las Apps heredan el valor `approvals_reviewer` de nivel superior.",
    },
    {
      key: "apps._default.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Comportamiento de aprobación predeterminado para las herramientas de Apps sin valores específicos por App o herramienta.",
    },
    {
      key: "apps.<id>.destructive_enabled",
      type: "boolean",
      description:
        "Permite o bloquea las herramientas de esta App que declaran `destructive_hint = true`.",
    },
    {
      key: "apps.<id>.open_world_enabled",
      type: "boolean",
      description:
        "Permite o bloquea las herramientas de esta App que declaran `open_world_hint = true`.",
    },
    {
      key: "apps.<id>.default_tools_enabled",
      type: "boolean",
      description:
        "Estado de habilitación predeterminado para las herramientas de esta app, salvo que exista una configuración específica por herramienta que lo reemplace.",
    },
    {
      key: "apps.<id>.approvals_reviewer",
      type: "user | auto_review",
      description:
        "Revisor de las solicitudes de aprobación de herramientas de esta app. Reemplaza `apps._default.approvals_reviewer`.",
    },
    {
      key: "apps.<id>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Comportamiento de aprobación predeterminado para las herramientas de esta app, salvo que exista una configuración específica por herramienta que lo reemplace.",
    },
    {
      key: "apps.<id>.tools.<tool>.enabled",
      type: "boolean",
      description:
        "Configuración que reemplaza el estado de habilitación de una herramienta específica de una app (por ejemplo, `repos/list`).",
    },
    {
      key: "apps.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description: "Configuración que reemplaza el comportamiento de aprobación de una herramienta específica de una app.",
    },
    {
      key: "tool_suggest.discoverables",
      type: "array<table>",
      description:
        "Permite sugerencias de herramientas de conectores o complementos adicionales que se pueden descubrir. Cada entrada usa `type = \"connector\"` o `\"plugin\"` y un `id`.",
    },
    {
      key: "tool_suggest.disabled_tools",
      type: "array<table>",
      description:
        "Deshabilita las sugerencias de conectores o complementos específicos que se pueden descubrir. Cada entrada usa `type = \"connector\"` o `\"plugin\"` y un `id`.",
    },
    {
      key: "features.apps",
      type: "boolean",
      description:
        "Habilita las integraciones de apps (conectores) (estables; habilitadas de forma predeterminada). El tráfico de apps y conectores no está controlado por el proxy de red de los comandos ejecutados en el sandbox ni por su lista de dominios permitidos.",
    },
    {
      key: "features.hooks",
      type: "boolean",
      description:
        "Habilita los hooks del ciclo de vida cargados desde `hooks.json` o definidos directamente en la configuración `[hooks]`. `features.codex_hooks` es un alias obsoleto.",
    },
    {
      key: "features.code_mode.enabled",
      type: "boolean",
      description:
        "Habilita la configuración del modo de código. Esta función está en desarrollo y deshabilitada de forma predeterminada.",
    },
    {
      key: "features.code_mode.excluded_tool_namespaces",
      type: "array<string>",
      description:
        "Espacios de nombres de herramientas que el modo de código excluye de las instrucciones sobre llamadas anidadas a herramientas y no expone al ejecutor.",
    },
    {
      key: "features.code_mode.direct_only_tool_namespaces",
      type: "array<string>",
      description:
        "Espacios de nombres de herramientas que el modo de código solo puede usar mediante llamadas directas a herramientas.",
    },
    {
      key: "features.context_management.experimental_mode",
      type: "boolean",
      description:
        "Habilita la gestión experimental del contexto (deshabilitada de forma predeterminada). En lugar de comprimir repetidamente el contexto en un único resumen, usa notas y un historial con función de búsqueda para conservar los detalles acumulados. Requiere iniciar sesión en ChatGPT con un plan Plus, Pro o Pro Lite.",
    },
    {
      key: "features.rollout_budget.enabled",
      type: "boolean",
      description:
        "Habilita el seguimiento del presupuesto de ejecución. Esta función está en desarrollo y deshabilitada de forma predeterminada. Cuando está habilitada, se requiere `features.rollout_budget.limit_tokens`.",
    },
    {
      key: "features.rollout_budget.limit_tokens",
      type: "integer",
      description:
        "Límite de tokens mayor que cero para el seguimiento del presupuesto de ejecución. Es obligatorio cuando el presupuesto de ejecución está habilitado.",
    },
    {
      key: "features.rollout_budget.reminder_interval_tokens",
      type: "integer",
      description:
        "Intervalo de tokens mayor que cero entre los recordatorios del presupuesto de ejecución. De forma predeterminada, equivale al 10 % de `limit_tokens`, con un mínimo de 1 token.",
    },
    {
      key: "features.rollout_budget.sampling_token_weight",
      type: "number",
      description:
        "Multiplicador finito y no negativo para los tokens muestreados en la contabilización del presupuesto de ejecución. El valor predeterminado es `1.0`.",
    },
    {
      key: "features.rollout_budget.prefill_token_weight",
      type: "number",
      description:
        "Multiplicador finito y no negativo para los tokens de precarga en la contabilización del presupuesto de ejecución. El valor predeterminado es `1.0`.",
    },
    {
      key: "hooks",
      type: "table",
      description:
        "Hooks del ciclo de vida configurados directamente en `config.toml`. Usan el mismo esquema de eventos que `hooks.json`; consulta la guía de Hooks para ver ejemplos y eventos compatibles.",
    },
    {
      key: "hooks.",
      type: "array<table>",
      description:
        "Grupos de criterios de coincidencia para eventos de hooks como `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `SessionStart`, `SessionEnd`, `SubagentStart`, `SubagentStop`, `UserPromptSubmit`, `Stop` o `Interrupt`.",
    },
    {
      key: "hooks.[].hooks",
      type: "array<table>",
      description:
        "Controladores de hooks para un grupo de criterios de coincidencia. Se admiten los hooks de comando y de herramientas MCP; los controladores de hooks de prompt y de agente se analizan sintácticamente, pero se omiten.",
    },
    {
      key: "hooks.[].hooks[].async",
      type: "boolean",
      description:
        "Ejecuta un hook de comando en segundo plano sin retrasar la operación que lo activa. El valor predeterminado es `false`; `SessionEnd` siempre se ejecuta de forma síncrona. Consulta [Ejecutar hooks en segundo plano](/codex/hooks#run-hooks-in-the-background).",
    },
    {
      key: "hooks.[].hooks[].additionalContextLimit",
      type: "integer",
      description:
        "Umbral aproximado de tokens por controlador para guardar en disco valores de `additionalContext` demasiado grandes y mostrarle al modelo una vista previa más breve. El valor predeterminado es `2500`; `0` pasa el contexto completo directamente al modelo. Consulta [Resultados extensos de hooks](/codex/hooks#large-hook-output).",
    },
    {
      key: "hooks.[].hooks[].commandWindows",
      type: "string",
      description:
        "Comando de reemplazo exclusivo de Windows para hooks de comando. También se acepta el alias de TOML `command_windows`.",
    },
    {
      key: "features.memories",
      type: "boolean",
      description:
        "Habilita [Memorias](/codex/customization/memories) (deshabilitadas de forma predeterminada).",
    },
    {
      key: "mcp_optional_startup_grace_ms",
      type: "integer (milliseconds)",
      description:
        "Tiempo de espera compartido para los servidores MCP opcionales al crear el catálogo inicial de herramientas. El valor predeterminado es `1000`. Establécelo en `0` para usar en su lugar el tiempo de espera `startup_timeout_sec` de cada servidor.",
    },
    {
      key: "mcp_servers.<id>.command",
      type: "string",
      description: "Comando para iniciar un servidor MCP stdio.",
    },
    {
      key: "mcp_servers.<id>.args",
      type: "array<string>",
      description: "Argumentos que se pasan al comando del servidor MCP stdio.",
    },
    {
      key: "mcp_servers.<id>.env",
      type: "map<string,string>",
      description: "Variables de entorno que se reenvían al servidor MCP stdio.",
    },
    {
      key: "mcp_servers.<id>.env_vars",
      type: 'array<string | { name = string, source = "local" | "remote" }>',
      description:
        "Variables de entorno adicionales que se incluirán en la lista de permitidas para un servidor MCP stdio. Las entradas de tipo cadena usan `source = \"local\"` de forma predeterminada; usa `source = \"remote\"` solo con stdio remoto que use un ejecutor.",
    },
    {
      key: "mcp_servers.<id>.cwd",
      type: "string",
      description: "Directorio de trabajo del proceso del servidor MCP stdio.",
    },
    {
      key: "mcp_servers.<id>.url",
      type: "string",
      description: "Punto de acceso de un servidor MCP HTTP con streaming.",
    },
    {
      key: "mcp_servers.<id>.auth",
      type: "oauth | chatgpt",
      description:
        "Método alternativo de autenticación para un servidor MCP HTTP, después de los tokens de portador y los encabezados de autorización configurados. `oauth` (valor predeterminado) usa las credenciales OAuth de MCP almacenadas cuando están disponibles. `chatgpt` usa la sesión actual de ChatGPT para el origen propio y de confianza de ChatGPT y, después, recurre a las credenciales OAuth almacenadas. Ambos modos pueden conectarse sin autenticación si ninguna fuente proporciona credenciales.",
    },
    {
      key: "mcp_servers.<id>.oauth.client_id",
      type: "string",
      description:
        "ID de cliente OAuth registrado previamente que se usa para la autorización y el intercambio de tokens con este servidor MCP.",
    },
    {
      key: "mcp_servers.<id>.oauth.callback_url",
      type: "string",
      description:
        "Callback de OAuth específico del servidor. Los clientes registrados previamente lo reutilizan cuando se admite la identificación del emisor o la URL ya termina con el ID de callback específico del servidor. De lo contrario, Codex usa el callback global o predeterminado con ese ID agregado al final. Los clientes sin un ID registrado previamente usan este callback durante el registro del cliente.",
    },
    {
      key: "mcp_servers.<id>.oauth.callback_port",
      type: "integer",
      description:
        "Puerto de escucha fijo para el callback de OAuth de este servidor MCP. Reemplaza `mcp_oauth_callback_port`. Para un callback directo de loopback con un puerto explícito en la URL, configura el mismo puerto de escucha.",
    },
    {
      key: "mcp_servers.<id>.bearer_token_env_var",
      type: "string",
      description:
        "Variable de entorno de la que se obtiene el token de portador para un servidor MCP HTTP.",
    },
    {
      key: "mcp_servers.<id>.http_headers",
      type: "map<string,string>",
      description: "Encabezados HTTP estáticos incluidos en cada solicitud HTTP de MCP.",
    },
    {
      key: "mcp_servers.<id>.http_headers_helper",
      type: "string (command)",
      description:
        "Comando local que imprime un objeto JSON con nombres y valores de encabezados HTTP. Solo se admite para servidores MCP HTTP conectados localmente. Los tokens de portador explícitos y las credenciales OAuth tienen prioridad sobre los encabezados Authorization proporcionados por el comando auxiliar.",
    },
    {
      key: "mcp_servers.<id>.env_http_headers",
      type: "map<string,string>",
      description:
        "Encabezados HTTP cuyos valores se obtienen de variables de entorno para un servidor MCP HTTP.",
    },
    {
      key: "mcp_servers.<id>.enabled",
      type: "boolean",
      description: "Deshabilita un servidor MCP sin quitar su configuración.",
    },
    {
      key: "mcp_servers.<id>.required",
      type: "boolean",
      description:
        "Cuando el valor es true, el inicio o la reanudación fallan si este servidor MCP habilitado no puede inicializarse.",
    },
    {
      key: "mcp_servers.<id>.startup_timeout_sec",
      type: "number",
      description:
        "Reemplaza el tiempo de espera de inicio predeterminado de 10 s para un servidor MCP.",
    },
    {
      key: "mcp_servers.<id>.startup_timeout_ms",
      type: "number",
      description: "Alias de `startup_timeout_sec` expresado en milisegundos.",
    },
    {
      key: "mcp_servers.<id>.tool_timeout_sec",
      type: "number",
      description:
        "Reemplaza el tiempo de espera predeterminado de 60 s por herramienta para un servidor MCP.",
    },
    {
      key: "mcp_servers.<id>.enabled_tools",
      type: "array<string>",
      description: "Lista de nombres de herramientas permitidas que expone el servidor MCP.",
    },
    {
      key: "mcp_servers.<id>.disabled_tools",
      type: "array<string>",
      description:
        "Lista de herramientas denegadas que se aplica después de `enabled_tools` para el servidor MCP.",
    },
    {
      key: "mcp_servers.<id>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Comportamiento de aprobación predeterminado para las herramientas MCP de este servidor, salvo que exista una configuración específica por herramienta que lo reemplace.",
    },
    {
      key: "mcp_servers.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Configuración que reemplaza el comportamiento de aprobación para una herramienta MCP específica de este servidor.",
    },
    {
      key: "mcp_servers.<id>.tools.<tool>.output_token_limit",
      type: "integer (positive)",
      description:
        "Presupuesto de tokens para la salida de una herramienta MCP, antes del margen estándar del 20 % para la serialización. Reemplaza el presupuesto predeterminado del modelo para truncar la salida de esa herramienta.",
    },
    {
      key: "mcp_servers.<id>.scopes",
      type: "array<string>",
      description:
        "Alcances de OAuth que se solicitarán al autenticarse en ese servidor MCP.",
    },
    {
      key: "mcp_servers.<id>.oauth_resource",
      type: "string",
      description:
        "Parámetro opcional de recurso OAuth de RFC 8707 que se incluirá durante el inicio de sesión de MCP.",
    },
    {
      key: "mcp_servers.<id>.experimental_environment",
      type: "local | remote",
      description:
        "Ubicación experimental para un servidor MCP. `remote` inicia servidores stdio mediante un entorno con un ejecutor remoto; la ubicación remota para HTTP con streaming no está implementada.",
    },
    {
      key: "agents",
      type: "table",
      description:
        "Configuración multiagente y declaraciones de roles personalizados. Los nombres de las opciones de configuración escalares están reservados y no pueden usarse como nombres de roles personalizados.",
    },
    {
      key: "agents.enabled",
      type: "boolean",
      description: "Habilita o deshabilita las herramientas multiagente (valor predeterminado: true).",
    },
    {
      key: "agents.max_concurrent_threads_per_session",
      type: "number",
      description:
        "Cantidad máxima de hilos de agentes creados que pueden estar abiertos al mismo tiempo, sin contar el hilo principal. Si no se establece, Codex elige el valor predeterminado.",
    },
    {
      key: "agents.max_threads",
      type: "number",
      description:
        "Alias heredado de `agents.max_concurrent_threads_per_session`.",
    },
    {
      key: "agents.default_subagent_model",
      type: "string",
      description:
        "Modelo predeterminado para los agentes creados. Un modelo especificado explícitamente al crear el agente tiene prioridad.",
    },
    {
      key: "agents.default_subagent_reasoning_effort",
      type: "string",
      description:
        "Esfuerzo de razonamiento predeterminado para los agentes creados. Un esfuerzo especificado explícitamente al crear el agente tiene prioridad.",
    },
    {
      key: "agents.interrupt_message",
      type: "boolean",
      description:
        "Registra un mensaje visible para el modelo cuando se interrumpe el turno de un agente (valor predeterminado: true).",
    },
    {
      key: "agents.<name>.description",
      type: "string",
      description:
        "Indicaciones sobre el rol que se muestran a Codex al elegir y crear ese tipo de agente.",
    },
    {
      key: "agents.<name>.config_file",
      type: "string (path)",
      description:
        "Ruta a una capa de configuración TOML para ese rol; las rutas relativas se resuelven a partir del archivo de configuración que declara el rol.",
    },
    {
      key: "memories.generate_memories",
      type: "boolean",
      description:
        "Cuando el valor es `false`, los hilos recién creados no se almacenan como entradas para la generación de memorias. El valor predeterminado es `true`.",
    },
    {
      key: "memories.use_memories",
      type: "boolean",
      description:
        "Cuando el valor es `false`, Codex no incorpora las memorias existentes en sesiones futuras. El valor predeterminado es `true`.",
    },
    {
      key: "memories.disable_on_external_context",
      type: "boolean",
      description:
        "Cuando es `true`, los hilos que usan contexto externo, como llamadas a herramientas MCP, búsqueda web o búsqueda de herramientas, se excluyen de la generación de memorias. El valor predeterminado es `false`. Alias heredado: `memories.no_memories_if_mcp_or_web_search`.",
    },
    {
      key: "memories.max_raw_memories_for_consolidation",
      type: "number",
      description:
        "Cantidad máxima de memorias recientes sin procesar que se conservan para la consolidación global. El valor predeterminado es `256` y el límite máximo es `4096`.",
    },
    {
      key: "memories.max_unused_days",
      type: "number",
      description:
        "Cantidad máxima de días desde el último uso de una memoria antes de que deje de ser apta para la consolidación. El valor predeterminado es `30` y se limita al rango de `0`-`365`.",
    },
    {
      key: "memories.max_rollout_age_days",
      type: "number",
      description:
        "Antigüedad máxima de los hilos que se consideran para la generación de memorias. El valor predeterminado es `30` y se limita al rango de `0`-`90`.",
    },
    {
      key: "memories.max_rollouts_per_startup",
      type: "number",
      description:
        "Cantidad máxima de ejecuciones candidatas que se procesan en cada pasada de inicio. El valor predeterminado es `16` y el límite máximo es `128`.",
    },
    {
      key: "memories.min_rollout_idle_hours",
      type: "number",
      description:
        "Tiempo mínimo de inactividad antes de que un hilo se considere para la generación de memorias. El valor predeterminado es `6` y se limita al rango de `1`-`48`.",
    },
    {
      key: "memories.min_rate_limit_remaining_percent",
      type: "number",
      description:
        "Porcentaje restante mínimo requerido en las ventanas de límites de solicitudes de Codex antes de iniciar la generación de memorias. El valor predeterminado es `25` y se limita al rango de `0`-`100`.",
    },
    {
      key: "memories.extract_model",
      type: "string",
      description: "Modelo opcional que reemplaza al predeterminado para la extracción de memorias de cada hilo.",
    },
    {
      key: "memories.consolidation_model",
      type: "string",
      description: "Modelo opcional que reemplaza al predeterminado para la consolidación global de memorias.",
    },
    {
      key: "features.unified_exec",
      type: "boolean",
      description:
        "Usa la herramienta exec unificada basada en PTY (estable; habilitada de forma predeterminada excepto en Windows).",
    },
    {
      key: "features.shell_snapshot",
      type: "boolean",
      description:
        "Guarda una instantánea del entorno del shell para acelerar los comandos repetidos (estable; se activa de forma predeterminada).",
    },
    {
      key: "features.multi_agent",
      type: "boolean",
      description:
        "Habilita las herramientas de colaboración entre agentes (`spawn_agent`, `send_input`, `resume_agent`, `wait_agent` y `close_agent`) (estable; se activa de forma predeterminada).",
    },
    {
      key: "features.goals",
      type: "boolean",
      description:
        "Habilita la persistencia de objetivos y la continuación automática (estable; se activa de forma predeterminada).",
    },
    {
      key: "features.remote_plugin",
      type: "boolean",
      description: "Habilita el catálogo remoto de complementos (estable; se activa de forma predeterminada).",
    },
    {
      key: "features.personality",
      type: "boolean",
      description:
        "Habilita los controles de selección de personalidad (estable; se activa de forma predeterminada).",
    },
    {
      key: "features.network_proxy",
      type: "boolean | table",
      description:
        "Inicia el proxy de red para los comandos ejecutados en el sandbox (experimental; desactivado de forma predeterminada). Es necesario para aplicar las reglas de dominios del perfil de permisos, a menos que los requisitos `experimental_network` habilitados y gestionados por administradores inicien el proxy. Usa una tabla cuando configures opciones de política de la función, como `domains`. No filtra la búsqueda web, las apps, MCP ni otras herramientas alojadas.",
    },
    {
      key: "features.network_proxy.enabled",
      type: "boolean",
      description:
        "Inicia el proxy de red para los comandos ejecutados en el sandbox cuando el acceso de los comandos a la red está habilitado. El valor predeterminado es `false`; las reglas de dominios del perfil de permisos no se aplican mientras el proxy está desactivado.",
    },
    {
      key: "features.network_proxy.domains",
      type: "map<string, allow | deny>",
      description:
        "Política de dominios para el acceso a la red en el sandbox. No está definida de forma predeterminada, por lo que no se permite ningún destino externo hasta que agregues reglas `allow`. Admite hosts exactos, `*.example.com` solo para subdominios, `**.example.com` para el dominio raíz y sus subdominios, y reglas globales de permiso con `*`; prioriza las reglas con alcance limitado, ya que `*` habilita ampliamente el acceso saliente a redes públicas. Agrega reglas `deny` para los destinos bloqueados; `deny` prevalece en caso de conflicto.",
    },
    {
      key: "features.network_proxy.unix_sockets",
      type: "map<string, allow | deny>",
      description:
        "Política de sockets Unix para el acceso a la red en el sandbox. No está definida de forma predeterminada; agrega entradas `allow` para los sockets permitidos.",
    },
    {
      key: "features.network_proxy.allow_local_binding",
      type: "boolean",
      description:
        "Permite un acceso más amplio a redes locales o privadas. El valor predeterminado es `false`; las reglas de permiso para una dirección IP local literal exacta o para `localhost` aún pueden permitir destinos locales específicos.",
    },
    {
      key: "features.network_proxy.enable_socks5",
      type: "boolean",
      description: "Habilita la compatibilidad con SOCKS5. El valor predeterminado es `true`.",
    },
    {
      key: "features.network_proxy.enable_socks5_udp",
      type: "boolean",
      description: "Permite UDP mediante SOCKS5. El valor predeterminado es `true`.",
    },
    {
      key: "features.network_proxy.allow_upstream_proxy",
      type: "boolean",
      description:
        "Permite encadenar la conexión a través de un proxy ascendente definido en el entorno. El valor predeterminado es `true`.",
    },
    {
      key: "features.network_proxy.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "Permite usar direcciones de escucha distintas de loopback. El valor predeterminado es `false`; habilitar esta opción puede exponer los puntos de escucha del proxy fuera de localhost.",
    },
    {
      key: "features.network_proxy.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "Permite destinos arbitrarios de sockets Unix en lugar de limitar el acceso a una lista de permitidos. El valor predeterminado es `false`; usa esta opción solo en entornos estrictamente controlados.",
    },
    {
      key: "features.network_proxy.proxy_url",
      type: "string",
      description:
        "URL de escucha HTTP para el acceso a la red en el sandbox. El valor predeterminado es `\"http://127.0.0.1:3128\"`.",
    },
    {
      key: "features.network_proxy.socks_url",
      type: "string",
      description:
        "URL de escucha de SOCKS5. El valor predeterminado es `\"http://127.0.0.1:8081\"`.",
    },
    {
      key: "features.web_search",
      type: "boolean",
      description:
        "Opción heredada obsoleta; usa preferentemente la configuración `web_search` de nivel superior.",
    },
    {
      key: "features.web_search_cached",
      type: "boolean",
      description:
        "Opción heredada obsoleta. Si `web_search` no está definido, true equivale a `web_search = \"cached\"`.",
    },
    {
      key: "features.web_search_request",
      type: "boolean",
      description:
        "Opción heredada obsoleta. Si `web_search` no está definido, true equivale a `web_search = \"live\"`.",
    },
    {
      key: "features.shell_tool",
      type: "boolean",
      description:
        "Habilita la herramienta `shell` predeterminada para ejecutar comandos (estable; se activa de forma predeterminada).",
    },
    {
      key: "features.enable_request_compression",
      type: "boolean",
      description:
        "Comprime con zstd los cuerpos de las solicitudes de streaming cuando se admita esta compresión (estable; se activa de forma predeterminada).",
    },
    {
      key: "features.skill_mcp_dependency_install",
      type: "boolean",
      description:
        "Permite solicitar la instalación de las dependencias de MCP que faltan para las habilidades e instalarlas (estable; se activa de forma predeterminada).",
    },
    {
      key: "features.fast_mode",
      type: "boolean",
      description:
        "Habilita la selección del nivel de servicio del catálogo de modelos en la TUI, incluidos los comandos del nivel rápido cuando el modelo activo indique que los admite (estable; se activa de forma predeterminada).",
    },
    {
      key: "features.prevent_idle_sleep",
      type: "boolean",
      description:
        "Impide que la computadora entre en suspensión mientras haya un turno en ejecución (experimental; se desactiva de forma predeterminada).",
    },
    {
      key: "suppress_unstable_features_warning",
      type: "boolean",
      description:
        "Oculta la advertencia que aparece cuando se habilitan flags de funciones en desarrollo.",
    },
    {
      key: "model_providers.<id>",
      type: "table",
      description:
        "Definición de un proveedor personalizado. Los identificadores de proveedores integrados (`openai`, `ollama` y `lmstudio`) están reservados y no se pueden reemplazar.",
    },
    {
      key: "model_providers.<id>.name",
      type: "string",
      description: "Nombre para mostrar de un proveedor de modelos personalizado.",
    },
    {
      key: "model_providers.<id>.base_url",
      type: "string",
      description: "URL base de la API del proveedor de modelos.",
    },
    {
      key: "model_providers.<id>.env_key",
      type: "string",
      description: "Variable de entorno que proporciona la clave de API del proveedor.",
    },
    {
      key: "model_providers.<id>.env_key_instructions",
      type: "string",
      description: "Instrucciones opcionales para configurar la clave de API del proveedor.",
    },
    {
      key: "model_providers.<id>.experimental_bearer_token",
      type: "string",
      description:
        "Token de portador directo para el proveedor (no se recomienda; usa `env_key`).",
    },
    {
      key: "model_providers.<id>.requires_openai_auth",
      type: "boolean",
      description:
        "El proveedor usa la autenticación de OpenAI (el valor predeterminado es false).",
    },
    {
      key: "model_providers.<id>.wire_api",
      type: "responses",
      description:
        "Protocolo que usa el proveedor. `responses` es el único valor admitido y se usa de forma predeterminada cuando se omite.",
    },
    {
      key: "model_providers.<id>.query_params",
      type: "map<string,string>",
      description: "Parámetros de consulta adicionales que se agregan a las solicitudes al proveedor.",
    },
    {
      key: "model_providers.<id>.http_headers",
      type: "map<string,string>",
      description: "Encabezados HTTP estáticos que se agregan a las solicitudes al proveedor.",
    },
    {
      key: "model_providers.<id>.env_http_headers",
      type: "map<string,string>",
      description:
        "Encabezados HTTP que se completan a partir de variables de entorno cuando estas están disponibles.",
    },
    {
      key: "model_providers.<id>.request_max_retries",
      type: "number",
      description:
        "Cantidad de reintentos de las solicitudes HTTP al proveedor (valor predeterminado: 4).",
    },
    {
      key: "model_providers.<id>.stream_max_retries",
      type: "number",
      description: "Cantidad de reintentos ante interrupciones del streaming SSE (valor predeterminado: 5).",
    },
    {
      key: "model_providers.<id>.stream_idle_timeout_ms",
      type: "number",
      description:
        "Tiempo de espera por inactividad para los flujos SSE, en milisegundos (valor predeterminado: 300 000).",
    },
    {
      key: "model_providers.<id>.supports_websockets",
      type: "boolean",
      description:
        "Indica si ese proveedor admite el transporte WebSocket de la Responses API.",
    },
    {
      key: "model_providers.<id>.supports_standalone_web_search",
      type: "boolean",
      description:
        "Declara que admite un punto de acceso compatible para la búsqueda web independiente (valor predeterminado: false). La búsqueda independiente sigue en desarrollo y desactivada de forma predeterminada; que el proveedor sea compatible no basta para habilitarla.",
    },
    {
      key: "model_providers.<id>.auth",
      type: "table",
      description:
        "Configuración de un token de portador obtenido mediante un comando para un proveedor personalizado. No la combines con `env_key`, `experimental_bearer_token` ni `requires_openai_auth`.",
    },
    {
      key: "model_providers.<id>.auth.command",
      type: "string",
      description:
        "Comando que se ejecuta cuando Codex necesita un token de portador. El comando debe imprimir el token en stdout.",
    },
    {
      key: "model_providers.<id>.auth.args",
      type: "array<string>",
      description: "Argumentos que se pasan al comando de obtención del token.",
    },
    {
      key: "model_providers.<id>.auth.timeout_ms",
      type: "number",
      description:
        "Tiempo máximo de ejecución del comando de obtención del token en milisegundos (valor predeterminado: 5000).",
    },
    {
      key: "model_providers.<id>.auth.refresh_interval_ms",
      type: "number",
      description:
        "Intervalo de actualización proactiva del token por parte de Codex, en milisegundos (valor predeterminado: 300 000). Establécelo en `0` para actualizar el token solo después de un reintento de autenticación.",
    },
    {
      key: "model_providers.<id>.auth.cwd",
      type: "string (path)",
      description: "Directorio de trabajo del comando de obtención del token.",
    },
    {
      key: "model_providers.amazon-bedrock.aws.profile",
      type: "string",
      description:
        "Nombre del perfil de AWS que usa el proveedor integrado `amazon-bedrock`.",
    },
    {
      key: "model_providers.amazon-bedrock.aws.region",
      type: "string",
      description: "Región de AWS que usa el proveedor integrado `amazon-bedrock`.",
    },
    {
      key: "model_reasoning_effort",
      type: "minimal | low | medium | high | xhigh",
      description:
        "Ajusta el esfuerzo de razonamiento para los modelos compatibles (solo para la Responses API; `xhigh` depende del modelo).",
    },
    {
      key: "plan_mode_reasoning_effort",
      type: "none | minimal | low | medium | high | xhigh",
      description:
        "Ajuste de razonamiento específico del Modo plan. Si no se define, el Modo plan usa el valor predeterminado de su ajuste preestablecido integrado.",
    },
    {
      key: "model_reasoning_summary",
      type: "auto | concise | detailed | none",
      description:
        "Selecciona el nivel de detalle de los resúmenes del razonamiento o desactívalos por completo.",
    },
    {
      key: "model_verbosity",
      type: "low | medium | high",
      description:
        "Ajuste opcional de la verbosidad de la Responses API para GPT-5; si no se define, se usa el valor predeterminado del modelo o ajuste preestablecido seleccionado.",
    },
    {
      key: "model_supports_reasoning_summaries",
      type: "boolean",
      description: "Obliga a Codex a enviar o no enviar metadatos de razonamiento.",
    },
    {
      key: "shell_environment_policy.inherit",
      type: "all | core | none",
      description:
        "Herencia básica del entorno al crear subprocesos.",
    },
    {
      key: "shell_environment_policy.ignore_default_excludes",
      type: "boolean",
      description:
        "Conserva las variables que contienen KEY, SECRET o TOKEN antes de aplicar otros filtros (valor predeterminado: true). Establece false para aplicar exclusiones automáticas por nombres de secretos.",
    },
    {
      key: "shell_environment_policy.filters",
      type: "map<string, include | exclude>",
      description:
        "Filtros canónicos de patrones de variables de entorno que no distinguen entre mayúsculas y minúsculas. Las entradas de inclusión crean una lista de permitidos y no pueden restaurar valores excluidos. Los valores explícitos de `set` se aplican después de las exclusiones. No combines filtros con los arreglos heredados `exclude` o `include_only` en la misma capa.",
    },
    {
      key: "shell_environment_policy.exclude",
      type: "array<string>",
      description:
        "Patrones heredados de exclusión de variables de entorno. Usa `shell_environment_policy.filters` para las configuraciones nuevas; no combines ambos formatos en la misma capa.",
    },
    {
      key: "shell_environment_policy.include_only",
      type: "array<string>",
      description:
        "Lista heredada de patrones de variables de entorno permitidas. Usa `shell_environment_policy.filters` para las configuraciones nuevas; no combines ambos formatos en la misma capa.",
    },
    {
      key: "shell_environment_policy.set",
      type: "map<string,string>",
      description:
        "Valores explícitos de entorno que se insertan después de las exclusiones; los filtros de inclusión aún pueden eliminarlos.",
    },
    {
      key: "shell_environment_policy.experimental_use_profile",
      type: "boolean",
      description: "Usa el perfil de shell del usuario al crear subprocesos.",
    },
    {
      key: "project_root_markers",
      type: "array<string>",
      description:
        "Lista de nombres de archivos que indican la raíz del proyecto; se usa al buscar la raíz del proyecto en los directorios superiores.",
    },
    {
      key: "project_doc_max_bytes",
      type: "number",
      description:
        "Cantidad máxima de bytes que se leen de `AGENTS.md` al preparar las instrucciones del proyecto.",
    },
    {
      key: "project_doc_fallback_filenames",
      type: "array<string>",
      description: "Nombres de archivo adicionales que se buscan cuando falta `AGENTS.md`.",
    },
    {
      key: "history.persistence",
      type: "save-all | none",
      description:
        "Controla si Codex guarda las transcripciones de las sesiones en history.jsonl.",
    },
    {
      key: "tool_output_token_limit",
      type: "number",
      description:
        "Presupuesto de tokens para almacenar en el historial la salida de cada herramienta o función.",
    },
    {
      key: "background_terminal_max_timeout",
      type: "number",
      description:
        "Duración máxima, en milisegundos, de los sondeos de `write_stdin` sin entrada (sondeo de la terminal en segundo plano). Valor predeterminado: `300000` (5 minutos). Reemplaza la antigua clave `background_terminal_timeout`.",
    },
    {
      key: "history.max_bytes",
      type: "number",
      description:
        "Si se configura, limita el tamaño del archivo de historial en bytes eliminando las entradas más antiguas.",
    },
    {
      key: "file_opener",
      type: "vscode | vscode-insiders | windsurf | cursor | none",
      description:
        "Esquema de URI que se usa para abrir citas de la salida de Codex (valor predeterminado: `vscode`).",
    },
    {
      key: "otel.environment",
      type: "string",
      description:
        "Etiqueta de entorno aplicada a los eventos de OpenTelemetry emitidos (valor predeterminado: `dev`).",
    },
    {
      key: "otel.exporter",
      type: "none | otlp-http | otlp-grpc",
      description:
        "Selecciona el exportador de OpenTelemetry y proporciona los metadatos del punto de acceso que correspondan.",
    },
    {
      key: "otel.trace_exporter",
      type: "none | otlp-http | otlp-grpc",
      description:
        "Selecciona el exportador de trazas de OpenTelemetry y proporciona los metadatos del punto de acceso que correspondan.",
    },
    {
      key: "otel.metrics_exporter",
      type: "none | statsig | otlp-http | otlp-grpc",
      description:
        "Selecciona el exportador de métricas de OpenTelemetry (el valor predeterminado es `statsig`).",
    },
    {
      key: "otel.log_user_prompt",
      type: "boolean",
      description:
        "Habilita la exportación de los prompts sin procesar de los usuarios junto con los registros de OpenTelemetry.",
    },
    {
      key: "otel.exporter.<id>.endpoint",
      type: "string",
      description: "Punto de acceso del exportador para los registros de OTEL.",
    },
    {
      key: "otel.exporter.<id>.protocol",
      type: "binary | json",
      description: "Protocolo que usa el exportador OTLP/HTTP.",
    },
    {
      key: "otel.exporter.<id>.headers",
      type: "map<string,string>",
      description: "Encabezados estáticos incluidos en las solicitudes del exportador de OTEL.",
    },
    {
      key: "otel.trace_exporter.<id>.endpoint",
      type: "string",
      description: "Punto de acceso del exportador de trazas para los registros de OTEL.",
    },
    {
      key: "otel.trace_exporter.<id>.protocol",
      type: "binary | json",
      description: "Protocolo que usa el exportador de trazas OTLP/HTTP.",
    },
    {
      key: "otel.trace_exporter.<id>.headers",
      type: "map<string,string>",
      description: "Encabezados estáticos incluidos en las solicitudes del exportador de trazas de OTEL.",
    },
    {
      key: "otel.exporter.<id>.tls.ca-certificate",
      type: "string",
      description: "Ruta del certificado de CA para TLS del exportador de OTEL.",
    },
    {
      key: "otel.exporter.<id>.tls.client-certificate",
      type: "string",
      description: "Ruta del certificado del cliente para TLS del exportador de OTEL.",
    },
    {
      key: "otel.exporter.<id>.tls.client-private-key",
      type: "string",
      description: "Ruta de la clave privada del cliente para TLS del exportador de OTEL.",
    },
    {
      key: "otel.trace_exporter.<id>.tls.ca-certificate",
      type: "string",
      description: "Ruta del certificado de CA para TLS del exportador de trazas de OTEL.",
    },
    {
      key: "otel.trace_exporter.<id>.tls.client-certificate",
      type: "string",
      description: "Ruta del certificado del cliente para TLS del exportador de trazas de OTEL.",
    },
    {
      key: "otel.trace_exporter.<id>.tls.client-private-key",
      type: "string",
      description: "Ruta de la clave privada del cliente para TLS del exportador de trazas de OTEL.",
    },
    {
      key: "desktop.custom_file_handlers.<id>",
      type: "table",
      description:
        "Solo a nivel de usuario. Define un destino adicional en **Abrir en** para la aplicación de escritorio de ChatGPT. Consulta [Agregar controladores de archivos personalizados](/codex/config-file/config-advanced#add-custom-file-handlers) para ver ejemplos y las restricciones de los ID de los controladores.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.label",
      type: "string",
      description: "Nombre para mostrar que aparece en los menús **Abrir en**. Obligatorio.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.icon",
      type: "string",
      description:
        "Ruta de un recurso incluido en el paquete, URL `data:image/...` codificada en Base64, URI de archivo o ruta local absoluta para el ícono del controlador. Obligatorio; las fuentes no compatibles usan el ícono predeterminado de VS Code.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.command",
      type: "string",
      description:
        "Ruta del ejecutable o nombre del comando que se debe detectar y ejecutar. Obligatorio.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.args",
      type: "array<string>",
      description:
        "Argumentos que se insertan entre el comando y la entrada de archivo (valor predeterminado: `[]`).",
    },
    {
      key: "desktop.custom_file_handlers.<id>.input",
      type: "path | json_argument | json_stdin",
      description:
        "Forma en que la aplicación pasa el archivo al controlador (valor predeterminado: `path`).",
    },
    {
      key: "desktop.custom_file_handlers.<id>.supports_ssh",
      type: "boolean",
      description:
        "Muestra el controlador como opción para los archivos de espacios de trabajo SSH (valor predeterminado: `false`).",
    },
    {
      key: "tui",
      type: "table",
      description:
        "Opciones específicas de la TUI, como habilitar las notificaciones de escritorio integradas.",
    },
    {
      key: "tui.notifications",
      type: "boolean | array<string>",
      description:
        "Habilita las notificaciones de la TUI; opcionalmente, restríngelas a tipos específicos de eventos.",
    },
    {
      key: "tui.notification_method",
      type: "auto | osc9 | bel",
      description:
        "Método usado para las notificaciones de la terminal (valor predeterminado: auto).",
    },
    {
      key: "tui.notification_condition",
      type: "unfocused | always",
      description:
        "Controla si las notificaciones de la TUI se activan solo cuando la terminal no tiene el foco o independientemente del foco. El valor predeterminado es `unfocused`.",
    },
    {
      key: "tui.animations",
      type: "boolean",
      description:
        "Habilita las animaciones de la terminal (pantalla de bienvenida, efecto de brillo e indicador giratorio) (valor predeterminado: true).",
    },
    {
      key: "tui.alternate_screen",
      type: "auto | always | never",
      description:
        "Controla el uso de la pantalla alternativa de la TUI (valor predeterminado: auto; auto la omite en Zellij para conservar el historial de desplazamiento).",
    },
    {
      key: "tui.resume_cwd",
      type: "current | session",
      description:
        "Directorio de trabajo que se usa al reanudar una sesión o crear un fork de ella. Si no se configura, Codex te pide que elijas uno si el directorio actual difiere del directorio guardado para la sesión.",
    },
    {
      key: "tui.vim_mode_default",
      type: "boolean",
      description:
        "Inicia el editor en el modo normal de Vim en lugar del modo de inserción (valor predeterminado: false). Puedes seguir cambiando esta opción en cada sesión con `/vim`.",
    },
    {
      key: "tui.raw_output_mode",
      type: "boolean",
      description:
        "Inicia la TUI en el modo de historial de desplazamiento sin procesar para facilitar la selección y copia de texto de la terminal (valor predeterminado: false). Puedes activarlo o desactivarlo con `/raw` o con la combinación de teclas predeterminada `alt-r`.",
    },
    {
      key: "tui.show_tooltips",
      type: "boolean",
      description:
        "Muestra sugerencias de introducción en la pantalla de bienvenida de la TUI (valor predeterminado: true).",
    },
    {
      key: "tui.status_line",
      type: "array<string> | null",
      description:
        "Lista ordenada de identificadores de los elementos de la línea de estado al pie de la TUI. `null` deshabilita la línea de estado.",
    },
    {
      key: "tui.terminal_title",
      type: "array<string> | null",
      description:
        "Lista ordenada de identificadores de elementos del título de la ventana o pestaña de la terminal. El valor predeterminado es `[\"spinner\", \"project\"]`; `null` deshabilita las actualizaciones del título.",
    },
    {
      key: "tui.theme",
      type: "string",
      description:
        "Sustitución del tema de resaltado de sintaxis (nombre del tema en kebab-case).",
    },
    {
      key: "tui.keymap.<context>.<action>",
      type: "string | array<string>",
      description:
        "Asignación de un atajo de teclado a una acción de la TUI. Los contextos compatibles incluyen `global`, `chat`, `composer`, `editor`, `vim_normal`, `vim_operator`, `vim_text_object`, `pager`, `list` y `approval`. Ciertas acciones del editor usan como alternativa las asignaciones coincidentes de `tui.keymap.global`; las asignaciones específicas del contexto tienen prioridad cuando se admiten.",
    },
    {
      key: "tui.keymap.<context>.<action> = []",
      type: "empty array",
      description:
        "Quita la asignación de la acción en ese contexto del mapa de teclas. Los nombres de las teclas usan cadenas normalizadas como `ctrl-a`, `shift-enter`, `page-down` o `minus`.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.enabled",
      type: "boolean",
      description:
        "Habilita o deshabilita un servidor MCP incluido en un complemento instalado sin cambiar el archivo de manifiesto del complemento.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Comportamiento de aprobación predeterminado para las herramientas de un servidor MCP proporcionado por un complemento.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.enabled_tools",
      type: "array<string>",
      description:
        "Lista de herramientas permitidas que expone un servidor MCP proporcionado por un complemento.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.disabled_tools",
      type: "array<string>",
      description:
        "Lista de herramientas denegadas que se aplica después de `enabled_tools` para un servidor MCP proporcionado por un complemento.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Comportamiento de aprobación específico que sustituye el predeterminado para una herramienta MCP proporcionada por un complemento.",
    },
    {
      key: "tui.model_availability_nux.<model>",
      type: "integer",
      description: "Estado interno de las sugerencias de inicio, indexado por el slug del modelo.",
    },
    {
      key: "hide_agent_reasoning",
      type: "boolean",
      description:
        "Suprime los eventos de razonamiento tanto en la TUI como en la salida de `codex exec`.",
    },
    {
      key: "show_raw_agent_reasoning",
      type: "boolean",
      description:
        "Muestra el contenido de razonamiento sin procesar cuando el modelo activo lo emite.",
    },
    {
      key: "disable_paste_burst",
      type: "boolean",
      description: "Deshabilita la detección de pegado en ráfaga en la TUI.",
    },
    {
      key: "windows_wsl_setup_acknowledged",
      type: "boolean",
      description: "Registra la confirmación de la introducción a Windows (solo Windows).",
    },
    {
      key: "chatgpt_base_url",
      type: "string",
      description: "Reemplaza la URL base utilizada durante el flujo de inicio de sesión en ChatGPT.",
    },
    {
      key: "cli_auth_credentials_store",
      type: "file | keyring | auto",
      description:
        "Controla dónde almacena la CLI las credenciales en caché (archivo auth.json o llavero del sistema operativo).",
    },
    {
      key: "mcp_oauth_credentials_store",
      type: "auto | file | keyring",
      description: "Almacén preferido para las credenciales OAuth de MCP.",
    },
    {
      key: "mcp_oauth_callback_port",
      type: "integer",
      description:
        "Puerto fijo global opcional para el servidor HTTP local de devolución de llamada utilizado durante el inicio de sesión OAuth de MCP. El valor `oauth.callback_port` específico de un servidor tiene prioridad. Si no se establece ninguno de los dos, Codex escucha en un puerto efímero elegido por el sistema operativo.",
    },
    {
      key: "mcp_oauth_callback_url",
      type: "string",
      description:
        "URL base opcional de devolución de llamada para el inicio de sesión OAuth de MCP, como la URL de entrada de una devbox. Los clientes registrados previamente que se agregan por primera vez usan esta URL sin cambios cuando el servidor de autorización admite la identificación del emisor; los clientes existentes sin una devolución de llamada guardada agregan un ID de devolución de llamada específico del servidor. Si no se admite la identificación del emisor, cualquier servidor MCP registrado previamente cuya devolución de llamada configurada carezca del ID requerido usa esta URL con el ID agregado. Los puertos de las URL de devolución de llamada no determinan el puerto de escucha.",
    },
    {
      key: "experimental_use_unified_exec_tool",
      type: "boolean",
      description:
        "Nombre heredado para habilitar la ejecución unificada; usa preferentemente `[features].unified_exec` o `codex --enable unified_exec`.",
    },
    {
      key: "tools.web_search",
      type: 'boolean | { context_size = "low|medium|high", allowed_domains = [string], location = { country, region, city, timezone } }',
      description:
        "Configuración opcional de la herramienta de búsqueda web. El formato de objeto permite establecer el tamaño del contexto de búsqueda, los dominios de búsqueda permitidos y la ubicación aproximada del usuario. Estos filtros de dominios de búsqueda son independientes de las reglas de dominios de red para comandos ejecutados en el sandbox y no restringen los conectores ni los servidores MCP.",
    },
    {
      key: "tools.view_image",
      type: "boolean",
      description: "Habilita la herramienta `view_image` para adjuntar imágenes locales.",
    },
    {
      key: "web_search",
      type: "disabled | cached | indexed | live",
      description:
        "Modo de búsqueda web (predeterminado: `\"cached\"`; cached usa un índice mantenido por OpenAI sin acceso a la web externa; indexed permite el acceso externo solo cuando lo autoriza el índice de búsqueda; si usas `--yolo` u otra configuración de sandbox con acceso completo, el valor predeterminado es `\"live\"`). Usa `\"live\"` para obtener contenido en tiempo real sin restricciones o `\"disabled\"` para eliminar la herramienta.",
    },
    {
      key: "default_permissions",
      type: "string",
      description:
        "Nombre del perfil de permisos predeterminado que se aplica a las llamadas a herramientas en el sandbox. Los perfiles integrados son `:read-only`, `:workspace` y `:danger-full-access`; los nombres de perfiles personalizados requieren tablas `[permissions.<name>]` correspondientes. No lo combines con `sandbox_mode` ni con `[sandbox_workspace_write]`.",
    },
    {
      key: "permissions.<name>.description",
      type: "string",
      description:
        "Descripción legible para las personas de este perfil con nombre. Un perfil no hereda la descripción de su perfil padre mediante `extends`.",
    },
    {
      key: "permissions.<name>.extends",
      type: "string",
      description:
        "Perfil padre opcional que se aplica antes de este perfil con nombre. Establécelo en otro perfil con nombre, `:read-only` o `:workspace`; se rechazan `:danger-full-access`, los perfiles padre sin definir y los ciclos.",
    },
    {
      key: "permissions.<name>.workspace_roots",
      type: "table",
      description:
        "Raíces del espacio de trabajo definidas por el perfil a las que se aplican las reglas del sistema de archivos de `:workspace_roots`, junto con las raíces del espacio de trabajo de la sesión en tiempo de ejecución.",
    },
    {
      key: "permissions.<name>.workspace_roots.<path>",
      type: "boolean",
      description:
        "Incluye una ruta en el conjunto de raíces del espacio de trabajo del perfil cuando es `true`. Las entradas deshabilitadas permanecen inactivas.",
    },
    {
      key: "permissions.<name>.filesystem",
      type: "table",
      description:
        "Perfil de permisos con nombre para el sistema de archivos. Cada clave es una ruta absoluta o un token especial, como `:minimal` o `:workspace_roots`.",
    },
    {
      key: "permissions.<name>.filesystem.glob_scan_max_depth",
      type: "number",
      description:
        "Profundidad máxima para expandir patrones glob que deniegan la lectura en plataformas que toman una instantánea de las coincidencias antes de iniciar el sandbox. Si se establece, debe ser al menos `1`.",
    },
    {
      key: "permissions.<name>.filesystem.<path-or-glob>",
      type: '"read" | "write" | "deny" | table',
      description:
        "Otorga acceso directo a una ruta, un patrón glob o un token especial, o limita a esa raíz el alcance de las entradas anidadas. Usa `\"deny\"` para denegar la lectura de las rutas coincidentes.",
    },
    {
      key: 'permissions.<name>.filesystem.":workspace_roots".<subpath-or-glob>',
      type: '"read" | "write" | "deny"',
      description:
        "Acceso al sistema de archivos con alcance definido respecto de cada raíz efectiva del espacio de trabajo. Usa `\".\"` para la raíz en sí; las subrutas glob, como `\"**/*.env\"`, pueden denegar la lectura con `\"deny\"`.",
    },
    {
      key: "permissions.<name>.network.enabled",
      type: "boolean",
      description:
        "Habilita el acceso a la red para los comandos de este perfil de permisos. Esto no inicia el proxy de red. Si no están habilitados `features.network_proxy` ni los requisitos de red administrados, el acceso a la red de los comandos es directo y las reglas de dominio del perfil no se aplican.",
    },
    {
      key: "permissions.<name>.network.proxy_url",
      type: "string",
      description:
        "URL del servicio de escucha HTTP que se usa cuando este perfil de permisos habilita las conexiones de red en el sandbox.",
    },
    {
      key: "permissions.<name>.network.enable_socks5",
      type: "boolean",
      description:
        "Habilita la compatibilidad con SOCKS5 cuando este perfil de permisos habilita las conexiones de red en el sandbox.",
    },
    {
      key: "permissions.<name>.network.socks_url",
      type: "string",
      description: "Punto de acceso del proxy SOCKS5 que usa este perfil de permisos.",
    },
    {
      key: "permissions.<name>.network.enable_socks5_udp",
      type: "boolean",
      description: "Permite UDP a través del servicio de escucha SOCKS5 cuando está habilitado.",
    },
    {
      key: "permissions.<name>.network.allow_upstream_proxy",
      type: "boolean",
      description:
        "Permite encadenar las conexiones de red en el sandbox a través de otro proxy ascendente.",
    },
    {
      key: "permissions.<name>.network.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "Permite direcciones de enlace distintas de loopback para los servicios de escucha de red del sandbox. Habilitar esta opción puede exponerlos más allá de localhost.",
    },
    {
      key: "permissions.<name>.network.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "Permite destinos arbitrarios de sockets Unix en lugar del conjunto restringido predeterminado. Usa esta opción solo en entornos estrictamente controlados.",
    },
    {
      key: "permissions.<name>.network.mode",
      type: "limited | full",
      description: "Modo de proxy de red que se usa para el tráfico de los subprocesos.",
    },
    {
      key: "permissions.<name>.network.domains",
      type: "table",
      description:
        "Reglas de dominio para comandos ejecutados en el sandbox. Solo se aplican cuando `features.network_proxy` o los requisitos de red administrados habilitados activan el proxy. Admiten hosts exactos, `*.example.com`, `**.example.com` y reglas globales de permiso con `*`; `deny` tiene prioridad. No restringen la búsqueda web, las apps ni los servidores MCP.",
    },
    {
      key: "permissions.<name>.network.domains.<pattern>",
      type: "allow | deny",
      description:
        "Permite o deniega un host exacto o un patrón comodín con alcance definido, como `*.example.com` o `**.example.com`.",
    },
    {
      key: "permissions.<name>.network.unix_sockets",
      type: "table",
      description:
        "Modificaciones de la lista de sockets Unix permitidos para las conexiones de red en el sandbox. Usa las rutas de sockets como claves; `allow` agrega una ruta y `deny` la rechaza.",
    },
    {
      key: "permissions.<name>.network.unix_sockets.<path>",
      type: "allow | deny",
      description:
        "Agrega una ruta absoluta de socket Unix a la lista efectiva de permitidos con `allow`, o recházala con `deny`. Las entradas denegadas se omiten de la lista efectiva de permitidos.",
    },
    {
      key: "permissions.<name>.network.allow_local_binding",
      type: "boolean",
      description:
        "Permite un acceso más amplio a la red local o privada mediante las conexiones de red en el sandbox. Las reglas que permiten una dirección IP local literal exacta o `localhost` pueden seguir permitiendo destinos locales específicos cuando esta opción permanece en `false`.",
    },
    {
      key: "projects.<path>.trust_level",
      type: "string",
      description:
        "Marca un proyecto o worktree como confiable o no confiable (`\"trusted\"` | `\"untrusted\"`). Los proyectos no confiables omiten las capas `.codex/` específicas del proyecto, incluidas la configuración local del proyecto, los hooks y las reglas.",
    },
    {
      key: "notice.hide_full_access_warning",
      type: "boolean",
      description: "Registra la confirmación del prompt de advertencia sobre el acceso completo.",
    },
    {
      key: "notice.hide_world_writable_warning",
      type: "boolean",
      description:
        "Registra la confirmación de la advertencia sobre los directorios de Windows con permisos de escritura para todos.",
    },
    {
      key: "notice.hide_rate_limit_model_nudge",
      type: "boolean",
      description: "Registra la decisión de no recibir el recordatorio para cambiar de modelo por el límite de solicitudes.",
    },
    {
      key: "notice.hide_gpt5_1_migration_prompt",
      type: "boolean",
      description: "Registra la confirmación del prompt de migración a GPT-5.1.",
    },
    {
      key: "notice.hide_gpt-5.1-codex-max_migration_prompt",
      type: "boolean",
      description:
        "Registra la confirmación del prompt de migración a gpt-5.1-codex-max.",
    },
    {
      key: "notice.model_migrations",
      type: "map<string,string>",
      description: "Registra las migraciones de modelos confirmadas como correspondencias del modelo anterior al nuevo.",
    },
    {
      key: "forced_login_method",
      type: "chatgpt | api",
      description: "Restringe Codex a un método de autenticación específico.",
    },
    {
      key: "forced_chatgpt_workspace_id",
      type: "string (uuid)",
      description: "Limita los inicios de sesión en ChatGPT a un identificador de espacio de trabajo específico.",
    },
  ]}
  client:load
/>

Puedes encontrar el esquema JSON más reciente para `config.toml` [aquí](/codex/config-schema.json).

Para obtener autocompletado y diagnósticos al editar `config.toml` en VS Code o Cursor, puedes instalar la extensión [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) y agregar esta línea al principio de tu `config.toml`:

```toml
#:schema https://developers.openai.com/codex/config-schema.json

Nota: cambia el nombre de `experimental_instructions_file` a `model_instructions_file`. Codex marca la clave anterior como obsoleta; actualiza las configuraciones existentes para usar el nombre nuevo.

## `requirements.toml`

`requirements.toml` es un archivo de configuración impuesto por el administrador que restringe ajustes sensibles para la seguridad que los usuarios no pueden reemplazar. Para obtener detalles, ubicaciones y ejemplos, consulta [Requisitos impuestos por el administrador](/es-419/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).

Para los usuarios de ChatGPT Business y ChatGPT Enterprise, Codex también puede aplicar
requisitos obtenidos de la nube. Consulta la página de seguridad para conocer los detalles sobre la precedencia.

Usa `[features]` en `requirements.toml` para fijar los indicadores de funciones del entorno de ejecución mediante las mismas
claves canónicas que usa `config.toml`. Los requisitos también pueden incluir claves documentadas
exclusivas de la App que no pertenecen a `config.toml`. Las claves omitidas quedan
sin restricciones.

Algunos requisitos administrados imponen un valor de configuración exacto en lugar de una
lista de permitidos. Los usuarios no pueden reemplazar valores impuestos para una ruta, una preferencia de actualización, una política de shell de inicio de sesión,
una configuración de comentarios o una configuración del escritorio privado de Windows.

Las listas administradas de perfiles de permisos permitidos requieren Codex 0.138.0 o posterior. Codex
0.137.0 y las versiones anteriores ignoran `allowed_permission_profiles` y la clave administrada
`default_permissions`.

Usa `allowed_sandbox_modes` con `sandbox_mode`. Para las implementaciones con perfiles de permisos,
usa `allowed_permission_profiles` con la clave administrada
`default_permissions`.

La tabla `[models.new_thread]` proporciona valores predeterminados administrados, pero no los impone.
Las selecciones explícitas al iniciar Codex mediante flags específicos de la CLI o valores de reemplazo con `--config` tienen
prioridad. Si se reemplaza explícitamente el modelo o el esfuerzo de razonamiento, se omiten ambos campos administrados
del modelo; `service_tier` es independiente.

Los requisitos del navegador abarcan tres ámbitos distintos. `in_app_browser`
controla el panel del navegador que una persona abre y usa directamente. `browser_use`
controla el trabajo realizado por agentes en un navegador. `computer_use` controla el trabajo realizado por agentes
en apps de escritorio nativas.

Los valores anidados de las políticas de Navegador y Uso de la computadora no otorgan acceso por
sí solos. Un valor `allow` específico de un origen o una app puede reemplazar el valor de respaldo de
la misma fuente de políticas, pero las comprobaciones habituales de funciones, aprobación y otras políticas
siguen aplicándose. Cuando se aplican tanto los requisitos administrados como `config.toml`, un valor `deny`
de cualquiera de los dos tiene prioridad.

<ConfigTable
  options={[
    {
      key: "sqlite_home",
      type: "string (path)",
      description:
        "Impone el directorio que Codex usa para almacenar el estado de ejecución en SQLite.",
    },
    {
      key: "log_dir",
      type: "string (path)",
      description: "Impone el directorio donde Codex escribe los archivos de registro locales.",
    },
    {
      key: "model_catalog_json",
      type: "string (path)",
      description: "Impone el catálogo JSON de modelos que Codex usa al iniciarse.",
    },
    {
      key: "check_for_update_on_startup",
      type: "boolean",
      description: "Establece obligatoriamente si Codex busca actualizaciones al iniciarse.",
    },
    {
      key: "allow_login_shell",
      type: "boolean",
      description: "Establece obligatoriamente si las herramientas de shell pueden iniciar un shell de inicio de sesión.",
    },
    {
      key: "feedback",
      type: "table",
      description: "Configuración administrada del envío de comentarios.",
    },
    {
      key: "feedback.enabled",
      type: "boolean",
      description:
        "Establece obligatoriamente si los usuarios pueden enviar comentarios a través de los clientes de Codex.",
    },
    {
      key: "allowed_approval_policies",
      type: "array<string>",
      description:
        "Valores permitidos para `approval_policy` (por ejemplo, `untrusted`, `on-request`, `never` y `granular`).",
    },
    {
      key: "allowed_approvals_reviewers",
      type: "array<string>",
      description:
        "Valores permitidos para `approvals_reviewer`, como `user` y `auto_review`.",
    },
    {
      key: "guardian_policy_config",
      type: "string",
      description:
        "Instrucciones de política administradas en formato Markdown para la revisión automática. Tienen prioridad sobre la política local `[auto_review].policy`. Se ignoran los valores en blanco.",
    },
    {
      key: "allowed_permission_profiles",
      type: "table<boolean>",
      description:
        "Lista completa de perfiles de permisos permitidos. Se permiten los perfiles establecidos en `true`. Se deniegan los perfiles omitidos o establecidos en `false`, incluidos los que se agreguen en versiones futuras. Cuando se combinan fuentes de requisitos, las entradas se emparejan por nombre de perfil.",
    },
    {
      key: "allowed_permission_profiles.<name>",
      type: "boolean",
      description:
        "Permite o deniega un perfil de permisos integrado o personalizado definido en una fuente de configuración o de requisitos cargada. Una fuente de requisitos posterior y de mayor prioridad puede usar `false` para deshabilitar un perfil permitido por una fuente anterior de menor prioridad.",
    },
    {
      key: "default_permissions",
      type: "string",
      description:
        "Perfil de permisos predeterminado administrado. El perfil debe estar permitido por `allowed_permission_profiles`. Establece este valor explícitamente para obtener un comportamiento predecible; si se omite, Codex usa `:workspace` de forma predeterminada solo cuando tanto `:workspace` como `:read-only` están permitidos explícitamente.",
    },
    {
      key: "enforce_residency",
      type: "string",
      description:
        "Exige que el tráfico del servicio de Codex use una residencia de datos compatible. Actualmente acepta `us`.",
    },
    {
      key: "models",
      type: "table",
      description:
        "Valores predeterminados administrados del modelo para los hilos nuevos. Estos valores tienen prioridad sobre los valores predeterminados del usuario y del proyecto, pero una selección explícita para el nuevo hilo puede reemplazarlos.",
    },
    {
      key: "models.new_thread",
      type: "table",
      description:
        "Valores predeterminados que se aplican al iniciar un nuevo hilo local. Cada ajuste del modelo es opcional.",
    },
    {
      key: "models.new_thread.model",
      type: "string",
      description:
        "Modelo predeterminado para los hilos nuevos. Tiene prioridad un valor explícito de `--model` o un ajuste del modelo o del razonamiento mediante `--config`.",
    },
    {
      key: "models.new_thread.model_reasoning_effort",
      type: "string",
      description:
        "Esfuerzo de razonamiento predeterminado para los hilos nuevos. Si se especifica explícitamente otro modelo o esfuerzo de razonamiento, se omiten ambos campos administrados del modelo.",
    },
    {
      key: "models.new_thread.service_tier",
      type: "string",
      description:
        "Nivel de servicio predeterminado para los hilos nuevos. Si se especifica explícitamente otro nivel de servicio, este tiene prioridad, independientemente de los campos del modelo.",
    },
    {
      key: "permissions",
      type: "table",
      description:
        "Perfiles de permisos definidos por el administrador, con el nombre del perfil como clave. Usan los mismos campos de perfil que `config.toml`.",
    },
    {
      key: "permissions.<name>",
      type: "table",
      description:
        "Perfil de permisos definido por el administrador. El nombre no puede comenzar con `:`, ser el nombre reservado `filesystem` ni duplicar el de un perfil de una configuración cargada. Usa los mismos campos de perfil que `config.toml`; consulta la guía de Permisos para ver el esquema completo del perfil.",
    },
    {
      key: "allowed_sandbox_modes",
      type: "array<string>",
      description: "Valores permitidos para `sandbox_mode`.",
    },
    {
      key: "windows",
      type: "table",
      description: "Requisitos del sandbox nativo de Windows.",
    },
    {
      key: "windows.allowed_sandbox_implementations",
      type: "array<string>",
      description:
        "Implementaciones del sandbox nativo de Windows permitidas para `windows.sandbox` (`elevated` y `unelevated`). La lista no debe estar vacía. Cuando ambas están permitidas y no se selecciona ningún modo, Codex prefiere `elevated`.",
    },
    {
      key: "windows.sandbox_private_desktop",
      type: "boolean",
      description:
        "Fija si el sandbox nativo de Windows inicia su proceso secundario en un escritorio privado.",
    },
    {
      key: "remote_sandbox_config",
      type: "array<table>",
      description:
        "Requisitos de sandbox específicos del host. La primera entrada cuyos `hostname_patterns` coincidan con el nombre de host resuelto reemplaza el valor de `allowed_sandbox_modes` de nivel superior para esa fuente de requisitos. Actualmente, las entradas específicas del host solo reemplazan los modos de sandbox.",
    },
    {
      key: "remote_sandbox_config[].hostname_patterns",
      type: "array<string>",
      description:
        "Patrones de nombres de host que no distinguen entre mayúsculas y minúsculas. Admiten `*` para cualquier secuencia de caracteres y `?` para un solo carácter.",
    },
    {
      key: "remote_sandbox_config[].allowed_sandbox_modes",
      type: "array<string>",
      description:
        "Modos de sandbox permitidos que se aplicarán cuando coincida esta entrada específica del host.",
    },
    {
      key: "allowed_web_search_modes",
      type: "array<string>",
      description:
        "Valores permitidos para `web_search` (`disabled`, `cached`, `indexed`, `live`). `disabled` siempre está permitido; una lista vacía, en la práctica, solo permite `disabled`.",
    },
    {
      key: "allow_managed_hooks_only",
      type: "boolean",
      description:
        "Cuando el valor es `true`, Codex omite los hooks del usuario, del proyecto, de la sesión y de los complementos, pero sigue permitiendo los hooks administrados de `requirements.toml` y de otras capas de configuración administrada.",
    },
    {
      key: "allow_appshots",
      type: "boolean",
      description:
        "Establece el valor en `false` para deshabilitar Capturas de la aplicación para los usuarios administrados. Si se omite, los requisitos no restringen Capturas de la aplicación y se aplica la disponibilidad normal del producto.",
    },
    {
      key: "allow_remote_control",
      type: "boolean",
      description:
        "Establece el valor en `false` para deshabilitar el control remoto del dispositivo para los usuarios administrados. Si se omite, los requisitos no imponen restricciones al control remoto del dispositivo y se aplica la disponibilidad normal del producto.",
    },
    {
      key: "allow_browser_and_computer_use",
      type: "boolean",
      description:
        "Establece el valor en `false` para bloquear tanto la función Navegador controlada por agentes como Uso de la computadora en aplicaciones nativas. Establecerlo en `true` u omitirlo no habilita ninguna de las dos funciones; siguen aplicándose las demás verificaciones de funciones, políticas y aprobaciones.",
    },
    {
      key: "features.plugin_sharing",
      type: "boolean",
      description:
        "En un `requirements.toml` administrado desde la nube, establece el valor en `false` para impedir que los complementos creados localmente se compartan en el espacio de trabajo.",
    },
    {
      key: "features",
      type: "table",
      description:
        "Valores fijados para las funciones. Usa los nombres canónicos de `config.toml` para las funciones del entorno de ejecución; aquí también se admiten las claves documentadas de requisitos exclusivas de la aplicación.",
    },
    {
      key: "features.<name>",
      type: "boolean",
      description:
        "Exige que una función documentada del entorno de ejecución o de la aplicación permanezca habilitada o deshabilitada.",
    },
    {
      key: "features.apps",
      type: "boolean",
      description:
        "Fija si la integración con Apps está disponible o no para los usuarios administrados.",
    },
    {
      key: "features.in_app_updates",
      type: "boolean",
      description:
        "En `requirements.toml`, establece el valor en `false` para deshabilitar las actualizaciones en la aplicación. Si se omite este requisito, las actualizaciones permanecen habilitadas de forma predeterminada.",
    },
    {
      key: "features.in_app_browser",
      type: "boolean",
      description:
        "En `requirements.toml`, establece el valor en `false` para deshabilitar el panel del navegador integrado que los usuarios abren y controlan directamente.",
    },
    {
      key: "features.browser_use",
      type: "boolean",
      description:
        "En `requirements.toml`, establece el valor en `false` para deshabilitar la función Navegador controlada por agentes.",
    },
    {
      key: "features.browser_use_external",
      type: "boolean",
      description:
        "En `requirements.toml`, establece el valor en `false` para impedir que Codex opere navegadores compatibles mediante la extensión del navegador de ChatGPT, incluidas las pestañas existentes y las sesiones con acceso autenticado.",
    },
    {
      key: "features.browser_use_full_cdp_access",
      type: "boolean",
      description:
        "En `requirements.toml`, establece el valor en `false` para deshabilitar el acceso completo a Chrome DevTools Protocol en el entorno de ejecución local, incluido el modo de desarrollador del navegador, e impedir que la aplicación de escritorio de ChatGPT habilite la opción correspondiente. Si se omite, se aplica la disponibilidad normal del producto.",
    },
    {
      key: "features.fast_mode",
      type: "boolean",
      description:
        "Fija la función canónica `fast_mode` como habilitada o deshabilitada para los usuarios administrados.",
    },
    {
      key: "features.guardian_approval",
      type: "boolean",
      description:
        "Fija si la aprobación de Guardian está disponible o no para los usuarios administrados.",
    },
    {
      key: "features.memories",
      type: "boolean",
      description: "Fija si la función Memorias está disponible o no para los usuarios administrados.",
    },
    {
      key: "features.multi_agent",
      type: "boolean",
      description: "Fija si la funcionalidad multiagente está disponible o no para los usuarios administrados.",
    },
    {
      key: "features.plugins",
      type: "boolean",
      description: "Fija si los complementos están disponibles o no para los usuarios administrados.",
    },
    {
      key: "features.remote_plugin",
      type: "boolean",
      description:
        "Fija si el catálogo remoto de complementos está disponible o no para los usuarios administrados.",
    },
    {
      key: "features.computer_use",
      type: "boolean",
      description:
        "En `requirements.toml`, establece el valor en `false` para deshabilitar Uso de la computadora, Grabar y reproducir y los flujos relacionados de instalación o habilitación.",
    },
    {
      key: "features.workspace_dependencies",
      type: "boolean",
      description:
        "Fija si el entorno de ejecución incluido para las dependencias del espacio de trabajo está disponible o no para los usuarios administrados.",
    },
    {
      key: "in_app_browser",
      type: "table",
      description:
        "Requisitos del panel del navegador integrado. Estos ajustes no controlan la función Navegador controlada por agentes.",
    },
    {
      key: "in_app_browser.allow_external_browser_settings_import",
      type: "boolean",
      description:
        "Establece el valor en `false` para impedir que los usuarios importen configuraciones o datos de navegación desde un navegador externo al navegador integrado. Establecerlo en `true` u omitirlo mantiene disponible la importación cuando las demás verificaciones del producto lo permiten. Este ajuste es exclusivamente administrado y no puede reemplazarse mediante `config.toml`.",
    },
    {
      key: "browser_use",
      type: "table",
      description: "Requisitos administrados para la función Navegador controlada por agentes.",
    },
    {
      key: "browser_use.allow_history_access",
      type: "boolean",
      description:
        "Establece el valor en `false` para impedir que la función Navegador lea el historial de navegación. Establecerlo en `true` u omitirlo mantiene vigentes los ajustes normales del historial y las verificaciones de disponibilidad.",
    },
    {
      key: "browser_use.disable_auto_review",
      type: "boolean",
      description:
        "Establece el valor en `true` para omitir la revisión automática de la función Navegador y solicitar la aprobación del usuario en su lugar. Establecerlo en `false` u omitirlo mantiene disponible la revisión automática cuando los demás ajustes lo permiten.",
    },
    {
      key: "browser_use.allow_global_persistent_approval",
      type: "boolean",
      description:
        "Establece el valor en `false` para impedir que la función Navegador cree o aplique aprobaciones de `Always allow` que abarquen todos los sitios, como permitir descargas desde cualquier sitio. Las aprobaciones guardadas existentes se ignoran, pero no se eliminan. Establecerlo en `true` u omitirlo no crea una aprobación.",
    },
    {
      key: "browser_use.default_origin_policy",
      type: "table",
      description:
        "Valor de respaldo para cada ajuste de la función Navegador cuando ninguna entrada coincidente en `browser_use.origins` lo define. Una regla de origen coincidente reemplaza el valor de respaldo de esa fuente. Luego, Codex aplica el resultado más restrictivo entre los requisitos administrados y la configuración del usuario.",
    },
    {
      key: "browser_use.default_origin_policy.access",
      type: "allow | deny",
      description:
        "Usa `deny` para bloquear la función Navegador en los orígenes que usan el valor de respaldo. Denegar un origen también bloquea allí las cargas, las descargas, el acceso completo a la depuración del navegador y la revisión automática. `allow` solo permite que continúen las verificaciones normales de aprobación y de políticas.",
    },
    {
      key: "browser_use.default_origin_policy.downloads",
      type: "allow | deny",
      description:
        "Usa `deny` para bloquear las descargas de la función Navegador en los orígenes que usan el valor de respaldo. `allow` solo permite que continúen las verificaciones normales de aprobación y de políticas.",
    },
    {
      key: "browser_use.default_origin_policy.uploads",
      type: "allow | deny",
      description:
        "Usa `deny` para bloquear las cargas de la función Navegador en los orígenes que usan el valor de respaldo. `allow` solo permite que continúen las verificaciones normales de aprobación y de políticas.",
    },
    {
      key: "browser_use.default_origin_policy.full_cdp_access",
      type: "allow | deny",
      description:
        "Usa `deny` para bloquear el acceso completo a Chrome DevTools Protocol (CDP) en los orígenes que usan el valor de respaldo. `allow` solo permite que continúen las verificaciones normales de habilitación voluntaria y aprobación.",
    },
    {
      key: "browser_use.default_origin_policy.auto_review",
      type: "allow | deny",
      description:
        "Usa `deny` para omitir la revisión automática en los orígenes que usan el valor de respaldo y solicitar la aprobación del usuario en su lugar. `allow` mantiene disponible la revisión automática cuando los demás ajustes lo permiten.",
    },
    {
      key: "browser_use.default_origin_policy.persistent_approval",
      type: "boolean",
      description:
        "Establece el valor en `false` para impedir que la función Navegador guarde o aplique una aprobación de `Always allow` en los orígenes que usan el valor de respaldo. Las aprobaciones para el turno o hilo actual aún pueden aplicarse. `true` habilita la opción `Always allow` cuando las demás condiciones lo permiten, pero no crea una aprobación.",
    },
    {
      key: "browser_use.default_origin_policy.access_approval_lifetime",
      type: "turn | thread",
      description:
        "Establece cuánto dura una aprobación no persistente de acceso a un sitio: `turn` la limita al turno actual y `thread` la mantiene durante el resto del hilo actual. `persistent_approval` controla por separado si la opción `Always allow` está disponible. El valor predeterminado del producto es `thread`.",
    },
    {
      key: "browser_use.origins",
      type: "map<string, table>",
      description:
        "Políticas de la función Navegador específicas por origen. Las claves usan `<scheme>://<host-pattern>[:<port>]` con `http` o `https`. Usa un host exacto, `*.example.com` solo para subdominios o `**.example.com` para el dominio base y sus subdominios. Otros comodines `*` pueden abarcar puntos, por lo que `region*.example.com` también coincide con `region.api.example.com`; un host de `*` coincide con todos los hosts de ese esquema. Los esquemas y los puertos no predeterminados se tienen en cuenta; los puertos predeterminados explícitos se eliminan al normalizar. No son válidas las rutas, las consultas, los nombres de usuario o contraseñas incorporados ni los esquemas o puertos con comodines. Escribe el patrón entre comillas en TOML, por ejemplo, `[browser_use.origins.\"https://**.example.com\"]`.",
    },
    {
      key: "browser_use.origins.<pattern>",
      type: "table",
      description:
        "Política para los orígenes que coinciden con este patrón. Si coinciden varios patrones, Codex usa el valor más restrictivo para cada capacidad: `deny` prevalece sobre `allow`, `false` sobre `true` y `turn` sobre `thread`.",
    },
    {
      key: "browser_use.origins.<pattern>.access",
      type: "allow | deny",
      description:
        "Usa `deny` para bloquear la función Navegador en los orígenes coincidentes. La denegación también bloquea allí las cargas, las descargas, el acceso completo a la depuración del navegador y la revisión automática. `allow` solo permite que continúen las verificaciones normales de aprobación y de políticas.",
    },
    {
      key: "browser_use.origins.<pattern>.downloads",
      type: "allow | deny",
      description:
        "Usa `deny` para bloquear las descargas de la función Navegador en los orígenes coincidentes. `allow` solo permite que continúen las verificaciones normales de aprobación y de políticas.",
    },
    {
      key: "browser_use.origins.<pattern>.uploads",
      type: "allow | deny",
      description:
        "Usa `deny` para bloquear las cargas de la función Navegador en los orígenes coincidentes. `allow` solo permite que continúen las verificaciones normales de aprobación y de políticas.",
    },
    {
      key: "browser_use.origins.<pattern>.full_cdp_access",
      type: "allow | deny",
      description:
        "Usa `deny` para bloquear el acceso completo a Chrome DevTools Protocol (CDP) en los orígenes coincidentes. `allow` solo permite que continúen las verificaciones normales de habilitación voluntaria y aprobación.",
    },
    {
      key: "browser_use.origins.<pattern>.auto_review",
      type: "allow | deny",
      description:
        "Usa `deny` para omitir la revisión automática en los orígenes coincidentes y solicitar la aprobación del usuario en su lugar. `allow` mantiene disponible la revisión automática cuando los demás ajustes lo permiten.",
    },
    {
      key: "browser_use.origins.<pattern>.persistent_approval",
      type: "boolean",
      description:
        "Establece el valor en `false` para impedir que la función Navegador guarde o aplique una aprobación de `Always allow` en los orígenes coincidentes. Las aprobaciones para el turno o hilo actual aún pueden aplicarse. `true` habilita la opción `Always allow` cuando las demás condiciones lo permiten, pero no crea una aprobación.",
    },
    {
      key: "browser_use.origins.<pattern>.access_approval_lifetime",
      type: "turn | thread",
      description:
        "Establece cuánto dura una aprobación no persistente de acceso a un sitio para los orígenes coincidentes: `turn` la limita al turno actual y `thread` la mantiene durante el resto del hilo actual. `persistent_approval` controla por separado si la opción `Always allow` está disponible.",
    },
    {
      key: "computer_use",
      type: "table",
      description:
        "Requisitos administrados para el trabajo realizado por agentes en aplicaciones nativas de escritorio. Se aplican tanto las reglas administradas de aplicaciones como las de `config.toml`; cada fuente de políticas debe permitir la aplicación.",
    },
    {
      key: "computer_use.allow_locked_computer_use",
      type: "boolean",
      description:
        "Establécelo en `false` para impedir que los usuarios habiliten el uso con el dispositivo bloqueado en un dispositivo macOS administrado. Este requisito elimina los controles de habilitación; no desactiva el uso con el dispositivo bloqueado si ya está habilitado. Si se omite, se aplica la disponibilidad normal del producto.",
    },
    {
      key: "computer_use.allow_persistent_approval",
      type: "boolean",
      description:
        "Establécelo en `false` para eliminar la opción de guardar aprobaciones de apps entre sesiones. Las aprobaciones para la sesión actual siguen disponibles. Establecerlo en `true` u omitirlo no aprueba ninguna app.",
    },
    {
      key: "computer_use.default_app_access",
      type: "allow | deny",
      description:
        "Acceso predeterminado para las apps nativas que no coinciden con una regla específica de la plataforma. `deny` bloquea el acceso. `allow` solo permite que continúen las comprobaciones normales de aprobación y de políticas. El valor predeterminado del producto es `allow`.",
    },
    {
      key: "computer_use.macos",
      type: "table",
      description: "Reglas de apps para Uso de la computadora en macOS.",
    },
    {
      key: "computer_use.macos.bundle_ids",
      type: "map<string, allow | deny>",
      description:
        "Asigna `allow` o `deny` a identificadores de bundle exactos de macOS. Una regla coincidente reemplaza `computer_use.default_app_access` dentro de la misma fuente de políticas. Una denegación de los requisitos administrados o de la configuración del usuario sigue bloqueando el acceso.",
    },
    {
      key: "computer_use.macos.bundle_ids.<bundle-id>",
      type: "allow | deny",
      description:
        "Usa `deny` para bloquear el identificador de bundle exacto. `allow` solo reemplaza el valor predeterminado de esta fuente de políticas y sigue requiriendo que cualquier otra fuente de políticas y el flujo normal de aprobación permitan la app.",
    },
    {
      key: "computer_use.windows",
      type: "table",
      description:
        "Reglas de apps para Uso de la computadora en apps de Windows empaquetadas y no empaquetadas.",
    },
    {
      key: "computer_use.windows.aumids",
      type: "map<string, allow | deny>",
      description:
        "Asigna `allow` o `deny` a los identificadores exactos y registrados del modelo de usuario de la aplicación (AUMID) de apps empaquetadas y firmadas. Una regla coincidente reemplaza `computer_use.default_app_access` dentro de la misma fuente de políticas.",
    },
    {
      key: "computer_use.windows.aumids.<aumid>",
      type: "allow | deny",
      description:
        "Usa `deny` para bloquear la identidad exacta de la app empaquetada. `allow` solo reemplaza el valor predeterminado de esta fuente de políticas y sigue requiriendo que cualquier otra fuente de políticas y el flujo normal de aprobación permitan la app.",
    },
    {
      key: "computer_use.windows.exes",
      type: "array<table>",
      description:
        "Reglas para ejecutables de Windows firmados y no empaquetados. Las reglas se comparan con el editor verificado y la información de versión firmada del ejecutable, no con su ruta ni con su nombre de archivo actual. Una denegación coincidente tiene precedencia sobre los permisos coincidentes. Los ejecutables sin firma usan `computer_use.default_app_access`; se bloquean los ejecutables cuya identidad firmada no se pueda verificar de forma inequívoca.",
    },
    {
      key: "computer_use.windows.exes[].publisher_name",
      type: "string",
      description:
        "Nombre exacto obligatorio del editor, tomado del certificado de firma de confianza del ejecutable y con formato de nombre distintivo X.500 de Windows.",
    },
    {
      key: "computer_use.windows.exes[].product_name",
      type: "string",
      description:
        "Valor exacto obligatorio de `ProductName`, tomado de la información de versión firmada del ejecutable.",
    },
    {
      key: "computer_use.windows.exes[].binary_name",
      type: "string",
      description:
        "Valor opcional de `OriginalFilename`, tomado de la información de versión firmada del ejecutable. La comparación no distingue entre mayúsculas y minúsculas. Si una regla que coincide con el editor y el producto exige este valor, pero el ejecutable no lo proporciona, Uso de la computadora bloquea el ejecutable.",
    },
    {
      key: "computer_use.windows.exes[].access",
      type: "allow | deny",
      description:
        "Decisión de acceso obligatoria para los ejecutables coincidentes. `deny` bloquea el acceso. `allow` solo reemplaza el valor predeterminado de esta fuente de políticas y sigue requiriendo que cualquier otra fuente de políticas y el flujo normal de aprobación permitan la app.",
    },
    {
      key: "experimental_network",
      type: "table",
      description:
        "Requisitos de red administrados por el administrador para comandos locales ejecutados en un sandbox, impuestos desde `requirements.toml`. Cuando están habilitados, estos requisitos pueden iniciar el proxy de red para comandos sin `features.network_proxy`. Las herramientas de navegador comprueban por separado las denegaciones de red administradas y las listas exclusivas de destinos permitidos. Estos requisitos no enrutan el tráfico del navegador a través del proxy ni controlan la búsqueda web, las apps, los servidores MCP, el tráfico de apps nativas o la conectividad de red de Codex Cloud.",
    },
    {
      key: "experimental_network.enabled",
      type: "boolean",
      description:
        "Habilita los requisitos de red del sandbox. Esto no otorga acceso a la red cuando el sandbox activo mantiene deshabilitada la conectividad de red de los comandos.",
    },
    {
      key: "experimental_network.http_port",
      type: "integer",
      description:
        "Puerto de escucha HTTP en loopback que se usa para los requisitos de `[experimental_network]`.",
    },
    {
      key: "experimental_network.socks_port",
      type: "integer",
      description:
        "Puerto de escucha SOCKS5 en loopback que se usa para los requisitos de `[experimental_network]`.",
    },
    {
      key: "experimental_network.allow_upstream_proxy",
      type: "boolean",
      description:
        "Permite que la conectividad de red del sandbox se encadene a través de un proxy ascendente definido en el entorno.",
    },
    {
      key: "experimental_network.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "Permite direcciones de escucha que no sean de loopback para los requisitos de `[experimental_network]`. Habilitar esta opción puede exponer los servicios de escucha más allá de localhost.",
    },
    {
      key: "experimental_network.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "Permite destinos de sockets Unix arbitrarios en lugar de limitar el acceso a una lista de destinos permitidos. Úsalo solo en entornos estrictamente controlados.",
    },
    {
      key: "experimental_network.domains",
      type: "map<string, allow | deny>",
      description:
        "Política de dominios del administrador en formato de mapa para la conectividad de red del sandbox. Admite hosts exactos, `*.example.com` solo para subdominios, `**.example.com` para el dominio raíz y sus subdominios, y reglas globales de permiso con `*`; prefiere reglas de alcance limitado, porque `*` habilita ampliamente el acceso saliente a destinos públicos. `deny` tiene precedencia en caso de conflicto. No combines esta opción con `experimental_network.allowed_domains` ni con `experimental_network.denied_domains`.",
    },
    {
      key: "experimental_network.allowed_domains",
      type: "array<string>",
      description:
        "Reglas de permiso del administrador para la conectividad de red de comandos ejecutados en un sandbox mientras el proxy de red administrado está habilitado. Estas reglas no se aplican a la búsqueda web, las apps ni los servidores MCP. No combines esta opción con `experimental_network.domains`.",
    },
    {
      key: "experimental_network.denied_domains",
      type: "array<string>",
      description:
        "Reglas de denegación del administrador en formato de lista para la conectividad de red del sandbox. No combines esta opción con `experimental_network.domains`.",
    },
    {
      key: "experimental_network.managed_allowed_domains_only",
      type: "boolean",
      description:
        "Cuando es `true`, solo las reglas de permiso administradas por el administrador siguen vigentes mientras los requisitos de red del sandbox están activos; se ignoran las adiciones del usuario a la lista de destinos permitidos. Si no hay reglas de permiso administradas, las reglas de permiso de dominios agregadas por el usuario no siguen vigentes.",
    },
    {
      key: "experimental_network.unix_sockets",
      type: "map<string, allow | deny>",
      description:
        "Política de sockets Unix administrada por el administrador para la conectividad de red del sandbox.",
    },
    {
      key: "experimental_network.allow_local_binding",
      type: "boolean",
      description:
        "Permite un acceso más amplio a redes locales o privadas desde la red del sandbox. Las reglas que permiten una dirección IP local literal exacta o `localhost` pueden seguir permitiendo destinos locales específicos cuando esta opción permanece en `false`.",
    },
    {
      key: "hooks",
      type: "table",
      description:
        "Hooks administrados del ciclo de vida impuestos por el administrador. Requiere un directorio de hooks administrados y usa el mismo esquema de eventos que `[hooks]` definido directamente en `config.toml`.",
    },
    {
      key: "hooks.managed_dir",
      type: "string (absolute path)",
      description:
        "Directorio que contiene los scripts de hooks administrados en macOS y Linux. Codex valida que la ruta sea absoluta y que el directorio exista antes de cargar los hooks administrados.",
    },
    {
      key: "hooks.windows_managed_dir",
      type: "string (absolute path)",
      description:
        "Directorio que contiene los scripts de hooks administrados en Windows. Codex valida que la ruta sea absoluta y que el directorio exista antes de cargar los hooks administrados.",
    },
    {
      key: "hooks.",
      type: "array<table>",
      description:
        "Grupos de comparadores para un evento de hook como `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `SessionStart`, `SessionEnd`, `SubagentStart`, `SubagentStop`, `UserPromptSubmit` o `Stop`.",
    },
    {
      key: "hooks.[].hooks",
      type: "array<table>",
      description:
        "Manejadores de hooks para un grupo de comparadores. Se admiten hooks de comandos y herramientas MCP, mientras que los manejadores de hooks de prompts y agentes se analizan, pero se omiten.",
    },
    {
      key: "hooks.[].hooks[].async",
      type: "boolean",
      description:
        "Ejecuta un hook de comando en segundo plano sin retrasar la operación que lo activa. El valor predeterminado es `false`; `SessionEnd` siempre se ejecuta de forma síncrona. Consulta [Ejecutar hooks en segundo plano](/codex/hooks#run-hooks-in-the-background).",
    },
    {
      key: "hooks.[].hooks[].additionalContextLimit",
      type: "integer",
      description:
        "Umbral aproximado de tokens por manejador para guardar en disco un `additionalContext` demasiado grande y mostrar al modelo una vista previa más breve. El valor predeterminado es `2500`; `0` pasa el contexto completo directamente al modelo. Consulta [Salida de hooks de gran tamaño](/codex/hooks#large-hook-output).",
    },
    {
      key: "hooks.[].hooks[].commandWindows",
      type: "string",
      description:
        "Comando alternativo exclusivo de Windows para hooks de comandos. También se acepta el alias de TOML `command_windows`.",
    },
    {
      key: "permissions.filesystem.deny_read",
      type: "array<string>",
      description:
        "Denegaciones de lectura del sistema de archivos impuestas por el administrador. Las entradas pueden ser rutas o patrones glob, y los usuarios no pueden flexibilizarlas mediante la configuración local.",
    },
    {
      key: "mcp_servers",
      type: "table",
      description:
        "Lista de servidores MCP que se pueden habilitar. Tanto el nombre del servidor (`<id>`) como su identidad deben coincidir para que se habilite el servidor MCP. Se deshabilita cualquier servidor MCP configurado que no esté en la lista de permitidos o cuya identidad no coincida.",
    },
    {
      key: "mcp_servers.<id>.identity",
      type: "table",
      description:
        "Regla de identidad para un único servidor MCP. Configura `command` (stdio) o `url` (HTTP con streaming).",
    },
    {
      key: "mcp_servers.<id>.identity.command",
      type: "string | table",
      description:
        "Permite un servidor MCP stdio mediante una cadena de comando exacta, o usa una tabla de comparación para exigir un ejecutable exacto y comparadores de argumentos ordenados. El formato de cadena no inspecciona los argumentos, `cwd`, `env` ni `env_vars`.",
    },
    {
      key: "mcp_servers.<id>.identity.command.executable",
      type: "string",
      description:
        "Ejecutable con el que debe coincidir exactamente el valor de `command` configurado para el servidor stdio.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args",
      type: "array<table>",
      description:
        "Comparadores de argumentos ordenados para un servidor stdio. La lista de argumentos configurada debe tener la misma longitud y cada argumento debe coincidir en su posición. Los comparadores de comandos no inspeccionan `cwd`, `env` ni `env_vars`.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].match",
      type: "exact | prefix | regex",
      description: "Operación de comparación para el argumento en esta posición.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].value",
      type: "string",
      description: "Valor utilizado por un comparador de argumentos `exact` o `prefix`.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].expression",
      type: "string",
      description:
        "Expresión regular utilizada por un comparador de argumentos `regex`. La expresión debe ser válida y coincidir con el valor completo del argumento.",
    },
    {
      key: "mcp_servers.<id>.identity.url",
      type: "string | table",
      description:
        "Permite un servidor MCP que usa HTTP con streaming mediante una cadena de URL exacta, o usa una tabla de comparación de valores con `exact`, `prefix` o `regex`.",
    },
    {
      key: "mcp_servers.<id>.identity.url.match",
      type: "exact | prefix | regex",
      description: "Operación de comparación para la URL configurada del servidor MCP.",
    },
    {
      key: "mcp_servers.<id>.identity.url.value",
      type: "string",
      description: "Valor utilizado por un comparador de URL `exact` o `prefix`.",
    },
    {
      key: "mcp_servers.<id>.identity.url.expression",
      type: "string",
      description:
        "Expresión regular utilizada por un comparador de URL `regex`. La expresión debe ser válida y coincidir con el valor completo de la URL.",
    },
    {
      key: "plugins",
      type: "table",
      description:
        "Listas de servidores MCP permitidos por complemento, con el identificador del complemento como clave. Cuando esta tabla está presente, se deshabilitan los servidores incluidos en complementos que no tengan entradas coincidentes para el complemento y el servidor.",
    },
    {
      key: "plugins.<plugin>.mcp_servers",
      type: "table",
      description:
        "Lista de servidores MCP permitidos que se incluyen en un complemento. Los requisitos para los servidores del complemento usan los mismos formatos de identidad exacta y de comparación que los requisitos `mcp_servers` de nivel superior.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity",
      type: "table",
      description:
        "Regla de identidad para un servidor MCP incluido en un complemento. Configura `command` (stdio) o `url` (HTTP con streaming).",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command",
      type: "string | table",
      description:
        "Permite un servidor MCP stdio de un complemento mediante una cadena de comando exacta, o usa una tabla de comparación para exigir un ejecutable exacto y comparadores de argumentos ordenados.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.executable",
      type: "string",
      description:
        "Ejecutable con el que debe coincidir exactamente el comando configurado del servidor stdio incluido en el complemento.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args",
      type: "array<table>",
      description:
        "Comparadores de argumentos ordenados para un servidor stdio incluido en un complemento. La lista de argumentos configurada debe tener la misma longitud y cada argumento debe coincidir en su posición.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].match",
      type: "exact | prefix | regex",
      description: "Operación de comparación para el argumento en esta posición.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].value",
      type: "string",
      description: "Valor utilizado por un comparador de argumentos `exact` o `prefix`.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].expression",
      type: "string",
      description:
        "Expresión regular utilizada por un comparador de argumentos `regex`. La expresión debe coincidir con el valor completo del argumento.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url",
      type: "string | table",
      description:
        "Permite un servidor MCP de un complemento que usa HTTP con streaming mediante una cadena de URL exacta, o usa una tabla de comparación de valores con `exact`, `prefix` o `regex`.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.match",
      type: "exact | prefix | regex",
      description: "Operación de comparación para la URL del servidor MCP incluido en el complemento.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.value",
      type: "string",
      description: "Valor utilizado por un comparador de URL `exact` o `prefix`.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.expression",
      type: "string",
      description:
        "Expresión regular utilizada por un comparador de URL `regex`. La expresión debe coincidir con el valor completo de la URL.",
    },
    {
      key: "marketplaces",
      type: "table",
      description:
        "Requisitos del administrador para las fuentes de Marketplace de complementos. Las reglas entran en vigor cuando `restrict_to_allowed_sources` es `true`.",
    },
    {
      key: "marketplaces.restrict_to_allowed_sources",
      type: "boolean",
      description:
        "Cuando es `true`, exige que las fuentes de Marketplace configuradas por el usuario coincidan con `allowed_sources` en las operaciones para agregar un Marketplace, instalar complementos y actualizar los Marketplace configurados que usan Git. Los Marketplace de OpenAI administrados por Codex siguen estando permitidos cuando su fuente y su nombre coinciden con los valores reservados. Esto no filtra en tiempo de ejecución los Marketplace ya configurados por el usuario.",
    },
    {
      key: "marketplaces.allowed_sources",
      type: "table",
      description:
        "Fuentes de Marketplace permitidas cuyas claves son nombres de reglas elegidos por el administrador. Los nombres distintos se acumulan entre las capas de requisitos; los campos asociados al mismo nombre siguen la precedencia normal de las capas.",
    },
    {
      key: "marketplaces.allowed_sources.<name>",
      type: "table",
      description:
        "Una regla de fuente permitida. El valor final de `source` después de combinar los requisitos determina qué campos del mismo nivel interpreta Codex.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.source",
      type: "git | host_pattern | local",
      description:
        "Tipo de criterio de coincidencia para la fuente de Marketplace. Usa `git` para un repositorio, `host_pattern` para hosts de Git que coincidan con una expresión regular o `local` para un directorio.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.url",
      type: "string",
      description:
        "URL del repositorio Git requerida cuando `source = \"git\"`. Codex normaliza las URL configuradas y permitidas antes de exigir una coincidencia exacta del repositorio.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.ref",
      type: "string",
      description:
        "Referencia exacta de Git opcional para una regla `git`. Si se omite, la regla permite cualquier referencia del repositorio coincidente.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.host_pattern",
      type: "string",
      description:
        "Expresión regular requerida cuando `source = \"host_pattern\"`. Codex la compara con el nombre de host en minúsculas extraído de una fuente Git en formato HTTPS, SSH o SCP. Usa `^` y `$` para exigir que coincida el nombre de host completo.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.path",
      type: "string (absolute path)",
      description:
        "Directorio local de Marketplace requerido cuando `source = \"local\"`. Codex exige una ruta absoluta y compara las rutas después de normalizarlas.",
    },
    {
      key: "apps",
      type: "table",
      description:
        "Requisitos administrados para aplicaciones, con el identificador de la aplicación como clave. Los requisitos pueden deshabilitar una aplicación o restringir el comportamiento de aprobación de herramientas individuales.",
    },
    {
      key: "apps.<id>.enabled",
      type: "boolean",
      description:
        "Establece el valor en `false` para deshabilitar una aplicación. Un requisito de deshabilitación mantiene su efecto restrictivo cuando se combinan varias fuentes de requisitos.",
    },
    {
      key: "apps.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description: "Establece el modo de aprobación administrado para una herramienta de una aplicación.",
    },
    {
      key: "rules",
      type: "table",
      description:
        "Reglas de comandos impuestas por el administrador que se combinan con los archivos `.rules`. Las reglas de requisitos deben ser restrictivas.",
    },
    {
      key: "rules.prefix_rules",
      type: "array<table>",
      description:
        "Lista de reglas de prefijo de cumplimiento obligatorio. Cada regla debe incluir `pattern` y `decision`.",
    },
    {
      key: "rules.prefix_rules[].pattern",
      type: "array<table>",
      description:
        "Prefijo del comando expresado como tokens de patrón. Cada token define `token` o `any_of`.",
    },
    {
      key: "rules.prefix_rules[].pattern[].token",
      type: "string",
      description: "Un único token literal en esta posición.",
    },
    {
      key: "rules.prefix_rules[].pattern[].any_of",
      type: "array<string>",
      description: "Una lista de tokens alternativos permitidos en esta posición.",
    },
    {
      key: "rules.prefix_rules[].decision",
      type: "prompt | forbidden",
      description:
        "Obligatorio. Las reglas de requisitos solo pueden solicitar aprobación o prohibir (no permitir).",
    },
    {
      key: "rules.prefix_rules[].justification",
      type: "string",
      description:
        "Justificación opcional que no debe estar vacía y que se muestra en las solicitudes de aprobación o en los mensajes de rechazo.",
    },
  ]}
  client:load
/>
